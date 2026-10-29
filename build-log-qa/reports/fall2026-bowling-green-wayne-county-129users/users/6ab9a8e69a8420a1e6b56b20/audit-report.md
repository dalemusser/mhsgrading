# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b20

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b20
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b20.jsonl
- **Records:** 15968 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b20
- **Time span:** 2026-10-05T16:33:02.981000+00:00 .. 2026-10-15T17:04:11.151000+00:00 (240h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b20\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 15968 records, 10 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 98 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 7393 | 46.3 | 1 | 9 | 0 | 2026-10-05T16:33:15.885000+00:00 | 2026-10-15T17:04:05.867000+00:00 | 240h 30m |
| PuzzlePieceVisibleEvent | 3423 | 21.44 | 1 | 4 | 0 | 2026-10-06T16:58:33.103000+00:00 | 2026-10-15T16:44:49.884000+00:00 | 215h 46m |
| DialogueEvent | 2225 | 13.93 | 1 | 9 | 1377 | 2026-10-05T16:33:32.447000+00:00 | 2026-10-15T17:04:11.151000+00:00 | 240h 30m |
| PlayerPositionEvent | 1783 | 11.17 | 1 | 9 | 0 | 2026-10-05T16:33:12.218000+00:00 | 2026-10-15T17:04:09.200000+00:00 | 240h 30m |
| argumentationNodeEvent | 414 | 2.59 | 1 | 5 | 0 | 2026-10-05T16:55:14.834000+00:00 | 2026-10-15T17:02:51.438000+00:00 | 240h 7m |
| ObjectInterEvent | 279 | 1.75 | 1 | 9 | 0 | 2026-10-05T16:38:43.421000+00:00 | 2026-10-15T16:59:44.031000+00:00 | 240h 21m |
| Soil Key Puzzle | 97 | 0.61 | 1 | 3 | 0 | 2026-10-07T16:45:07.394000+00:00 | 2026-10-15T16:25:44.457000+00:00 | 191h 40m |
| questEvent | 81 | 0.51 | 1 | 9 | 81 | 2026-10-05T16:33:32.425000+00:00 | 2026-10-15T17:04:06.575000+00:00 | 240h 30m |
| TopographicMapEvent | 70 | 0.44 | 1 | 4 | 0 | 2026-10-06T16:59:20.934000+00:00 | 2026-10-15T15:52:10.094000+00:00 | 214h 52m |
| argumentationAnswerEvent | 46 | 0.29 | 1 | 5 | 0 | 2026-10-05T16:56:13.220000+00:00 | 2026-10-15T17:02:52.632000+00:00 | 240h 6m |
| DEBUGMenu | 37 | 0.23 | 1 | 9 | 0 | 2026-10-05T16:33:12.200000+00:00 | 2026-10-15T16:40:57.328000+00:00 | 240h 7m |
| WaterChamberEvent | 26 | 0.16 | 1 | 1 | 0 | 2026-10-15T16:46:54.512000+00:00 | 2026-10-15T16:54:57.140000+00:00 | 8m 2s |
| gameWindowFocusEvent | 23 | 0.14 | 1 | 5 | 0 | 2026-10-05T16:33:02.981000+00:00 | 2026-10-15T16:37:28.545000+00:00 | 240h 4m |
| argumentationEvent | 17 | 0.11 | 1 | 5 | 0 | 2026-10-05T16:56:01.575000+00:00 | 2026-10-15T17:02:52.658000+00:00 | 240h 6m |
| gameStartEvent | 16 | 0.1 | 1 | 1 | 0 | 2026-10-05T16:33:02.982000+00:00 | 2026-10-15T16:37:28.546000+00:00 | 240h 4m |
| gameWindowUnfocusEvent | 15 | 0.09 | 1 | 6 | 0 | 2026-10-05T17:00:05.956000+00:00 | 2026-10-15T16:11:33.478000+00:00 | 239h 11m |
| TerasGardenBox | 10 | 0.06 | 1 | 1 | 0 | 2026-10-15T16:27:00.007000+00:00 | 2026-10-15T16:28:39.040000+00:00 | 1m 39s |
| DaniEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-05T16:37:30.269000+00:00 | 2026-10-14T16:06:30.393000+00:00 | 215h 29m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-05T17:01:02.112000+00:00 | 2026-10-15T16:37:05.868000+00:00 | 239h 36m |
| argumentationToolEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-05T16:55:59.570000+00:00 | 2026-10-05T16:56:01.515000+00:00 | 1.9s |
| chatEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-10-15T16:40:57.090000+00:00 | 2026-10-15T16:55:57.314000+00:00 | 15m 0s |
| soilMachine | 1 | 0.01 | 1 | 1 | 0 | 2026-10-14T16:55:46.974000+00:00 | 2026-10-14T16:55:46.974000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87187.63s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.855s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 4.138s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.945s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1456.161s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1698.216s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.1x vs baseline. 
  - Observed: 37 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 7393 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to Switch Canister; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 330 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 9.2x vs baseline. 
  - Observed: 46 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,3,II; B,2,I; C,2,II; C,D,3,2,II; C,D,3,4,II; C,D,3,II; C,D,A,2,II; D,1,II; D,2,II; D,C,2,II; D,C,B,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[224] _id=6ac3d312de269131f9adedbb ts=2026-10-05T16:40:49.6410000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[261] _id=6ac3d3fade269131f9adfee5 ts=2026-10-05T16:44:42.0110000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[444] _id=6ac3d48cde269131f9ae1067 ts=2026-10-05T16:47:07.9940000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[46] _id=6ac3d13fde269131f9adcaeb ts=2026-10-05T16:33:02.9820000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1093] _id=6ac3d82ade269131f9ae69f5 ts=2026-10-05T17:02:33.5160000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1192] _id=6ac5275cde269131f9b57971 ts=2026-10-06T16:52:43.4990000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[45] _id=6ac3d13fde269131f9adcae7 ts=2026-10-05T16:33:02.9810000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1094] _id=6ac3d79ade269131f9ae5b9d ts=2026-10-05T17:00:08.0720000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1092] _id=6ac3d82ade269131f9ae69f2 ts=2026-10-05T17:02:33.5140000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1116] _id=6ac3d79ade269131f9ae5b96 ts=2026-10-05T17:00:05.9560000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1193] _id=6ac5275cde269131f9b57951 ts=2026-10-05T17:04:38.25Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[2339] _id=6ac67405de269131f9bc8aa1 ts=2026-10-06T17:04:28.383Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 16 of 70 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1675] _id=6ac528e9de269131f9b5d27d ts=2026-10-06T16:59:20.9340000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1677] _id=6ac528ebde269131f9b5d2eb ts=2026-10-06T16:59:22.7910000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1681] _id=6ac528efde269131f9b5d3bb ts=2026-10-06T16:59:26.9440000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 7392 | 0.0 | 0.318 | 117.133 | 4.941 | 429378.621 | 0.51 | 774 | 8 |
| PuzzlePieceVisibleEvent | 3422 | 0.0 | 0.018 | 226.995 | 1.366 | 514479.2 | 0.26 | 1840 | 8 |
| DialogueEvent | 2224 | 0.0 | 4.011 | 389.316 | 25.219 | 429445.815 | 0.15 | 625 | 6 |
| PlayerPositionEvent | 1769 | 0.0 | 10.002 | 488.947 | 10.13 | 429353.643 | 0.12 | 2 | 6 |
| argumentationNodeEvent | 413 | 0.004 | 0.74 | 2093.115 | 9.169 | 689816.993 | 0.03 | 40 | 5 |
| ObjectInterEvent | 278 | 0.0 | 9.41 | 3112.448 | 438.595 | 431177.065 | 0.02 | 5 | 12 |
| Soil Key Puzzle | 96 | 0.0 | 0.916 | 7187.886 | 561.723 | 514665.93 | 0.01 | 5 | 5 |
| questEvent | 80 | 0.0 | 203.526 | 10822.927 | 82209.653 | 429378.624 | 0.01 | 12 | 18 |
| TopographicMapEvent | 69 | 0.024 | 2.901 | 11211.147 | 81633.359 | 431636.987 | 0.01 | 3 | 10 |
| argumentationAnswerEvent | 45 | 0.14 | 4.138 | 19208.876 | 66575.456 | 689846.779 | 0.0 | 0 | 5 |
| DEBUGMenu | 36 | 9.028 | 422.34 | 24012.92 | 85899.865 | 429367.042 | 0.0 | 0 | 17 |
| WaterChamberEvent | 25 | 0.972 | 6.855 | 19.305 | 47.043 | 68.869 | 3.11 | 0 | 0 |
| gameWindowFocusEvent | 22 | 8.25 | 1456.161 | 39284.798 | 86221.817 | 429379.03 | 0.0 | 0 | 15 |
| argumentationEvent | 16 | 0.034 | 75.024 | 54025.693 | 238584.739 | 689802.831 | 0.0 | 3 | 5 |
| gameStartEvent | 15 | 259.911 | 1999.312 | 57617.704 | 189184.153 | 429379.03 | 0.0 | 0 | 14 |
| gameWindowUnfocusEvent | 14 | 8.163 | 1698.216 | 61506.252 | 207019.089 | 431011.168 | 0.0 | 0 | 10 |
| TerasGardenBox | 9 | 1.315 | 5.129 | 11.004 | 28.118 | 29.964 | 5.45 | 0 | 0 |
| DaniEvent | 3 | 1.998 | 4.161 | 258580.041 | 698160.985 | 775733.965 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 85419.323 | 87187.63 | 287521.252 | 629679.886 | 689956.803 | 0.0 | 0 | 3 |
| argumentationToolEvent | 1 | 1.945 | 1.945 | 1.945 | 1.945 | 1.945 | 30.85 | 0 | 0 |
| chatEvent | 1 | 900.224 | 900.224 | 900.224 | 900.224 | 900.224 | 0.07 | 0 | 1 |
| soilMachine | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 12 group(s), 22 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[2348] _id=6ac67425de269131f9bc8cbd ts=2026-10-07T16:32:35.1650000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[2349] _id=6ac67425de269131f9bc8cbe ts=2026-10-07T16:32:35.1650000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[2353] _id=6ac67425de269131f9bc8cc2 ts=2026-10-07T16:32:35.6560000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[2354] _id=6ac67425de269131f9bc8cc3 ts=2026-10-07T16:32:35.6560000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[5388] _id=6ac7ccc9de269131f9c4dbfe ts=2026-10-08T17:03:03.5990000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[5389] _id=6ac7ccc9de269131f9c4dbff ts=2026-10-08T17:03:03.5990000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 71 group(s), 129 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1567] _id=6ac528bade269131f9b5c8ac ts=2026-10-06T16:58:33.1710000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[1605] _id=6ac528bbde269131f9b5c8d0 ts=2026-10-06T16:58:33.1710000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1641] _id=6ac528bcde269131f9b5c96d ts=2026-10-06T16:58:33.9170000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[1632] _id=6ac528bdde269131f9b5c979 ts=2026-10-06T16:58:33.9170000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1649] _id=6ac528bdde269131f9b5c9be ts=2026-10-06T16:58:33.9440000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[1652] _id=6ac528bede269131f9b5c9cd ts=2026-10-06T16:58:33.9440000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[15962] _id=6ad10787de269131f9de4555 ts=2026-10-15T17:04:06.5750000Z == 6ab9a8e69a8420a1e6b56b20.jsonl[15963] _id=6ad10787de269131f9de4556 ts=2026-10-15T17:04:06.5750000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8e69a8420a1e6b56b20.jsonl[167] _id=6ac3d294de269131f9ade48b ts=2026-10-05T16:38:43.4210000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[163] _id=6ac3d294de269131f9ade48f ts=2026-10-05T16:38:43.4260000Z`; `198ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1527] _id=6ac5287ade269131f9b5b89f ts=2026-10-06T16:57:29.4720000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1525] _id=6ac5287ade269131f9b5b8c7 ts=2026-10-06T16:57:29.6700000Z`; `271ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1525] _id=6ac5287ade269131f9b5b8c7 ts=2026-10-06T16:57:29.6700000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1541] _id=6ac5287ade269131f9b5b8e9 ts=2026-10-06T16:57:29.9410000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 87 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `88ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1651] _id=6ac528bfde269131f9b5ca41 ts=2026-10-06T16:58:37.4920000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1583] _id=6ac528bfde269131f9b5ca53 ts=2026-10-06T16:58:37.5800000Z`; `61ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1648] _id=6ac528c1de269131f9b5ca97 ts=2026-10-06T16:58:38.2450000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1631] _id=6ac528c1de269131f9b5caa5 ts=2026-10-06T16:58:38.3060000Z`; `301ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1748] _id=6ac52941de269131f9b5e1f3 ts=2026-10-06T17:00:33.6490000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1712] _id=6ac52941de269131f9b5e1fd ts=2026-10-06T17:00:33.9500000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `127ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1681] _id=6ac528efde269131f9b5d3bb ts=2026-10-06T16:59:26.9440000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1683] _id=6ac528efde269131f9b5d3c7 ts=2026-10-06T16:59:27.0710000Z`; `185ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1683] _id=6ac528efde269131f9b5d3c7 ts=2026-10-06T16:59:27.0710000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1682] _id=6ac528f0de269131f9b5d3d5 ts=2026-10-06T16:59:27.2560000Z`; `335ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1687] _id=6ac528fbde269131f9b5d5b2 ts=2026-10-06T16:59:38.3600000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[1690] _id=6ac528fbde269131f9b5d5c9 ts=2026-10-06T16:59:38.6950000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `667ms: 6ab9a8e69a8420a1e6b56b20.jsonl[930] _id=6ac3d6f7de269131f9ae4af3 ts=2026-10-05T16:57:26.6860000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[931] _id=6ac3d6f8de269131f9ae4afb ts=2026-10-05T16:57:27.3530000Z`; `160ms: 6ab9a8e69a8420a1e6b56b20.jsonl[931] _id=6ac3d6f8de269131f9ae4afb ts=2026-10-05T16:57:27.3530000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[932] _id=6ac3d6f8de269131f9ae4aff ts=2026-10-05T16:57:27.5130000Z`; `140ms: 6ab9a8e69a8420a1e6b56b20.jsonl[932] _id=6ac3d6f8de269131f9ae4aff ts=2026-10-05T16:57:27.5130000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[925] _id=6ac3d6f8de269131f9ae4b09 ts=2026-10-05T16:57:27.6530000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6ab9a8e69a8420a1e6b56b20.jsonl[7775] _id=6acfa0e0de269131f9d4bfdd ts=2026-10-14T15:33:51.9700000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[7778] _id=6acfa0e0de269131f9d4bfe0 ts=2026-10-14T15:33:52.0050000Z`; `44ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13633] _id=6ad0fadbde269131f9dd4dd4 ts=2026-10-15T16:10:02.8630000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[13716] _id=6ad0fadbde269131f9dd4dde ts=2026-10-15T16:10:02.9070000Z`; `34ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13995] _id=6ad0fdf1de269131f9dd6c77 ts=2026-10-15T16:23:12.3780000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[13998] _id=6ad0fdf1de269131f9dd6c7a ts=2026-10-15T16:23:12.4120000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 26 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `954ms: 6ab9a8e69a8420a1e6b56b20.jsonl[854] _id=6ac3d688de269131f9ae4007 ts=2026-10-05T16:55:35.5600000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[859] _id=6ac3d689de269131f9ae4027 ts=2026-10-05T16:55:36.5140000Z`; `692ms: 6ab9a8e69a8420a1e6b56b20.jsonl[857] _id=6ac3d688de269131f9ae4013 ts=2026-10-05T16:55:36.0650000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[860] _id=6ac3d689de269131f9ae4029 ts=2026-10-05T16:55:36.7570000Z`; `719ms: 6ab9a8e69a8420a1e6b56b20.jsonl[859] _id=6ac3d689de269131f9ae4027 ts=2026-10-05T16:55:36.5140000Z ~ 6ab9a8e69a8420a1e6b56b20.jsonl[851] _id=6ac3d689de269131f9ae4043 ts=2026-10-05T16:55:37.2330000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b20.jsonl[5385] _id=6ac7ccc3de269131f9c4dbac ts=2026-10-08T17:02:58.7270000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5401] _id=6ace59fbde269131f9cf595f ts=2026-10-13T16:19:05.7690000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b20.jsonl[2337] _id=6ac67422de269131f9bc8c8b ts=2026-10-07T16:32:33.5800000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4065] _id=6ac7c4e8de269131f9c429e3 ts=2026-10-08T16:29:27.5900000Z; 23h 49m: 6ab9a8e69a8420a1e6b56b20.jsonl[1151] _id=6ac3d84dde269131f9ae6cbf ts=2026-10-05T17:03:09.0310000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1195] _id=6ac52771de269131f9b57c9d ts=2026-10-06T16:53:04.1810000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 28m 
  - Evidence: 215h 28m: 6ab9a8e69a8420a1e6b56b20.jsonl[124] _id=6ac3d24fde269131f9addddd ts=2026-10-05T16:37:34.4300000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10196] _id=6acfa884de269131f9d52fce ts=2026-10-14T16:06:28.3950000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b20.jsonl[5377] _id=6ac7cc90de269131f9c4d95a ts=2026-10-08T17:02:08.2630000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5421] _id=6ace5a17de269131f9cf59ff ts=2026-10-13T16:19:34.0780000Z; 23h 49m: 6ab9a8e69a8420a1e6b56b20.jsonl[1185] _id=6ac3d880de269131f9ae70a9 ts=2026-10-05T17:03:59.6490000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1190] _id=6ac52776de269131f9b57d65 ts=2026-10-06T16:53:07.6810000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b20.jsonl[2229] _id=6ac529edde269131f9b60271 ts=2026-10-06T17:03:40.3360000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2364] _id=6ac67437de269131f9bc8e51 ts=2026-10-07T16:32:54.8010000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 625 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13664] _id=6ad0fa9ade269131f9dd45a3 ts=2026-10-15T16:08:58.2730000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13665] _id=6ad0fa9ade269131f9dd45a4 ts=2026-10-15T16:08:58.2730000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13698] _id=6ad0fabcde269131f9dd498e ts=2026-10-15T16:09:32.5190000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13699] _id=6ad0fabcde269131f9dd498f ts=2026-10-15T16:09:32.5190000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13955] _id=6ad0fdcdde269131f9dd6983 ts=2026-10-15T16:22:36.2420000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13956] _id=6ad0fdcdde269131f9dd6984 ts=2026-10-15T16:22:36.2420000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 39m 
  - Evidence: 191h 39m: 6ab9a8e69a8420a1e6b56b20.jsonl[1127] _id=6ac3d7cede269131f9ae6089 ts=2026-10-05T17:01:02.1120000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5886] _id=6ace5ef3de269131f9cf9d8e ts=2026-10-13T16:40:18.9150000Z; 24h 13m: 6ab9a8e69a8420a1e6b56b20.jsonl[10453] _id=6acfac9ede269131f9d562a7 ts=2026-10-14T16:23:58.2380000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[14481] _id=6ad10132de269131f9ddaa60 ts=2026-10-15T16:37:05.8680000Z; 23h 43m: 6ab9a8e69a8420a1e6b56b20.jsonl[5886] _id=6ace5ef3de269131f9cf9d8e ts=2026-10-13T16:40:18.9150000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10453] _id=6acfac9ede269131f9d562a7 ts=2026-10-14T16:23:58.2380000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b20.jsonl[5395] _id=6ac7ccc9de269131f9c4dc05 ts=2026-10-08T17:03:03.6000000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5406] _id=6ace5a0cde269131f9cf59b4 ts=2026-10-13T16:19:22.2210000Z; 23h 49m: 6ab9a8e69a8420a1e6b56b20.jsonl[1175] _id=6ac3d861de269131f9ae6e51 ts=2026-10-05T17:03:28.9130000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1194] _id=6ac52775de269131f9b57d3b ts=2026-10-06T16:53:06.0200000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b20.jsonl[2296] _id=6ac52a03de269131f9b606a5 ts=2026-10-06T17:04:01.0290000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2347] _id=6ac67425de269131f9bc8cbc ts=2026-10-07T16:32:35.1630000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 774 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[10461] _id=6acfacb6de269131f9d564aa ts=2026-10-14T16:24:21.9300000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10462] _id=6acfacb6de269131f9d564ab ts=2026-10-14T16:24:21.9300000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[10677] _id=6acfb025de269131f9d5a52d ts=2026-10-14T16:39:00.9210000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10678] _id=6acfb025de269131f9d5a52e ts=2026-10-14T16:39:00.9210000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[10688] _id=6acfaffdde269131f9d5a0ac ts=2026-10-14T16:38:20.5670000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10689] _id=6acfaffdde269131f9d5a0ad ts=2026-10-14T16:38:20.5670000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8e69a8420a1e6b56b20.jsonl[4889] _id=6ac7c75fde269131f9c4766f ts=2026-10-08T16:39:58.3960000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5542] _id=6ace5ba8de269131f9cf6939 ts=2026-10-13T16:26:15.4610000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b20.jsonl[1129] _id=6ac3d7a3de269131f9ae5cca ts=2026-10-05T17:00:19.0000000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1528] _id=6ac52878de269131f9b5b815 ts=2026-10-06T16:57:27.6240000Z; 23h 30m: 6ab9a8e69a8420a1e6b56b20.jsonl[2295] _id=6ac52a03de269131f9b606a1 ts=2026-10-06T17:04:01.0260000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2407] _id=6ac674a2de269131f9bc97d5 ts=2026-10-07T16:34:41.5580000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13358] _id=6ad0f89ade269131f9dd081e ts=2026-10-15T16:00:26.7180000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13359] _id=6ad0f89ade269131f9dd081f ts=2026-10-15T16:00:26.7180000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13428] _id=6ad0f8d5de269131f9dd0fc1 ts=2026-10-15T16:01:25.6270000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13429] _id=6ad0f8d5de269131f9dd0fc2 ts=2026-10-15T16:01:25.6270000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13838] _id=6ad0fd15de269131f9dd5a1b ts=2026-10-15T16:19:32.9840000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13839] _id=6ad0fd15de269131f9dd5a1c ts=2026-10-15T16:19:32.9840000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b20.jsonl[5398] _id=6ac7ccdcde269131f9c4dd2e ts=2026-10-08T17:03:23.8780000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5405] _id=6ace5a0cde269131f9cf59b3 ts=2026-10-13T16:19:17.5210000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b20.jsonl[1189] _id=6ac3d8a0de269131f9ae730b ts=2026-10-05T17:04:31.7200000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1196] _id=6ac52773de269131f9b57cfd ts=2026-10-06T16:53:04.2020000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b20.jsonl[2328] _id=6ac52a1bde269131f9b60b77 ts=2026-10-06T17:04:26.4550000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2346] _id=6ac67425de269131f9bc8cbb ts=2026-10-07T16:32:33.5920000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[4056] _id=6ac67ba5de269131f9bd9078 ts=2026-10-07T17:04:36.0870000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4068] _id=6ac7c4e8de269131f9c429dc ts=2026-10-07T17:04:36.087Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[5380] _id=6ac7cca1de269131f9c4da15 ts=2026-10-08T17:02:24.4400000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5384] _id=6ac7ccb7de269131f9c4db18 ts=2026-10-08T17:02:24.44Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 142h 54m 
  - Evidence: 142h 54m: 6ab9a8e69a8420a1e6b56b20.jsonl[4981] _id=6ac7c808de269131f9c485e2 ts=2026-10-08T16:42:46.0920000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[8019] _id=6acfa1b7de269131f9d4ce86 ts=2026-10-14T15:37:25.2920000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b20.jsonl[3386] _id=6ac676e1de269131f9bd077c ts=2026-10-07T16:44:14.0800000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4264] _id=6ac7c5bfde269131f9c43e8c ts=2026-10-08T16:33:02.8460000Z; 23h 30m: 6ab9a8e69a8420a1e6b56b20.jsonl[2309] _id=6ac52a06de269131f9b607b5 ts=2026-10-06T17:04:02.7740000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2541] _id=6ac67524de269131f9bcb079 ts=2026-10-07T16:35:01.6420000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1840 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[10515] _id=6acfaffede269131f9d5a0e2 ts=2026-10-14T16:38:20.0070000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10516] _id=6acfaffede269131f9d5a0e3 ts=2026-10-14T16:38:20.0070000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[10615] _id=6acfb024de269131f9d5a505 ts=2026-10-14T16:38:58.2510000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10932] _id=6acfb024de269131f9d5a50f ts=2026-10-14T16:38:58.2510000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[10620] _id=6acfb001de269131f9d5a11a ts=2026-10-14T16:38:21.9360000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[10621] _id=6acfb001de269131f9d5a120 ts=2026-10-14T16:38:21.9360000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 142h 57m 
  - Evidence: 142h 57m: 6ab9a8e69a8420a1e6b56b20.jsonl[4208] _id=6ac7c595de269131f9c43896 ts=2026-10-08T16:32:21.0380000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[7671] _id=6acf9fffde269131f9d4b62a ts=2026-10-14T15:30:06.9680000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b20.jsonl[10697] _id=6acfaff9de269131f9d5a059 ts=2026-10-14T16:38:16.8650000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[14071] _id=6ad0fe88de269131f9dd7891 ts=2026-10-15T16:25:43.6280000Z; 23h 26m: 6ab9a8e69a8420a1e6b56b20.jsonl[4062] _id=6ac67ba2de269131f9bd905a ts=2026-10-07T17:04:33.0100000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4187] _id=6ac7c55ede269131f9c43392 ts=2026-10-08T16:31:25.7550000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.006s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[4045] _id=6ac67b95de269131f9bd8fab ts=2026-10-07T17:04:20.7630000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4046] _id=6ac67b95de269131f9bd8fac ts=2026-10-07T17:04:20.7630000Z; 5ms: 6ab9a8e69a8420a1e6b56b20.jsonl[4057] _id=6ac67b9dde269131f9bd9018 ts=2026-10-07T17:04:28.2690000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4054] _id=6ac67b9dde269131f9bd901d ts=2026-10-07T17:04:28.2740000Z; 6ms: 6ab9a8e69a8420a1e6b56b20.jsonl[4042] _id=6ac67b95de269131f9bd8fa3 ts=2026-10-07T17:04:20.4180000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4043] _id=6ac67b95de269131f9bd8fa9 ts=2026-10-07T17:04:20.4240000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a8e69a8420a1e6b56b20.jsonl[5298] _id=6ac7cb0ade269131f9c4bcfd ts=2026-10-08T16:55:37.7930000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[6135] _id=6ace611fde269131f9cfc61d ts=2026-10-13T16:49:34.7800000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b20.jsonl[3729] _id=6ac67a2ade269131f9bd67b3 ts=2026-10-07T16:58:17.5340000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5291] _id=6ac7caecde269131f9c4bac3 ts=2026-10-08T16:55:07.6000000Z; 23h 35m: 6ab9a8e69a8420a1e6b56b20.jsonl[1705] _id=6ac52907de269131f9b5d867 ts=2026-10-06T16:59:50.1190000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2445] _id=6ac674ddde269131f9bca239 ts=2026-10-07T16:35:40.3940000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.024s..0.048s shown 
  - Evidence: 24ms: 6ab9a8e69a8420a1e6b56b20.jsonl[3604] _id=6ac678c6de269131f9bd48f4 ts=2026-10-07T16:52:21.5220000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[3608] _id=6ac678c6de269131f9bd48f8 ts=2026-10-07T16:52:21.5460000Z; 32ms: 6ab9a8e69a8420a1e6b56b20.jsonl[1699] _id=6ac528fdde269131f9b5d64d ts=2026-10-06T16:59:39.8590000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1695] _id=6ac528fdde269131f9b5d665 ts=2026-10-06T16:59:39.8910000Z; 48ms: 6ab9a8e69a8420a1e6b56b20.jsonl[3603] _id=6ac678c6de269131f9bd48f2 ts=2026-10-07T16:52:21.4740000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[3604] _id=6ac678c6de269131f9bd48f4 ts=2026-10-07T16:52:21.5220000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 37m 
  - Evidence: 191h 37m: 6ab9a8e69a8420a1e6b56b20.jsonl[958] _id=6ac3d710de269131f9ae4d89 ts=2026-10-05T16:57:52.2630000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5775] _id=6ace5dc7de269131f9cf8566 ts=2026-10-13T16:35:19.0420000Z; 24h 32m: 6ab9a8e69a8420a1e6b56b20.jsonl[7771] _id=6acfa0e0de269131f9d4bfdb ts=2026-10-14T15:33:51.9520000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13582] _id=6ad0f9e5de269131f9dd309b ts=2026-10-15T16:05:56.8930000Z; 22h 57m: 6ab9a8e69a8420a1e6b56b20.jsonl[5789] _id=6ace5dddde269131f9cf8769 ts=2026-10-13T16:35:40.8350000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[7669] _id=6acfa0adde269131f9d4bdd3 ts=2026-10-14T15:33:00.8410000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 36m 
  - Evidence: 191h 36m: 6ab9a8e69a8420a1e6b56b20.jsonl[957] _id=6ac3d711de269131f9ae4d8f ts=2026-10-05T16:57:52.2910000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5740] _id=6ace5d9cde269131f9cf8280 ts=2026-10-13T16:34:35.1220000Z; 24h 29m: 6ab9a8e69a8420a1e6b56b20.jsonl[7778] _id=6acfa0e0de269131f9d4bfe0 ts=2026-10-14T15:33:52.0050000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13473] _id=6ad0f952de269131f9dd209a ts=2026-10-15T16:03:30.7140000Z; 22h 56m: 6ab9a8e69a8420a1e6b56b20.jsonl[5790] _id=6ace5dddde269131f9cf876d ts=2026-10-13T16:35:40.8580000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[7713] _id=6acfa08cde269131f9d4bc23 ts=2026-10-14T15:32:27.6580000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.034s..0.044s shown 
  - Evidence: 34ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13995] _id=6ad0fdf1de269131f9dd6c77 ts=2026-10-15T16:23:12.3780000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13998] _id=6ad0fdf1de269131f9dd6c7a ts=2026-10-15T16:23:12.4120000Z; 35ms: 6ab9a8e69a8420a1e6b56b20.jsonl[7775] _id=6acfa0e0de269131f9d4bfdd ts=2026-10-14T15:33:51.9700000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[7778] _id=6acfa0e0de269131f9d4bfe0 ts=2026-10-14T15:33:52.0050000Z; 44ms: 6ab9a8e69a8420a1e6b56b20.jsonl[13633] _id=6ad0fadbde269131f9dd4dd4 ts=2026-10-15T16:10:02.8630000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13716] _id=6ad0fadbde269131f9dd4dde ts=2026-10-15T16:10:02.9070000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 36m 
  - Evidence: 191h 36m: 6ab9a8e69a8420a1e6b56b20.jsonl[949] _id=6ac3d707de269131f9ae4cb7 ts=2026-10-05T16:57:42.7150000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5741] _id=6ace5da0de269131f9cf82e4 ts=2026-10-13T16:34:39.7080000Z; 24h 29m: 6ab9a8e69a8420a1e6b56b20.jsonl[7770] _id=6acfa0dede269131f9d4bfcd ts=2026-10-14T15:33:50.1590000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[13470] _id=6ad0f951de269131f9dd2079 ts=2026-10-15T16:03:29.6230000Z; 22h 56m: 6ab9a8e69a8420a1e6b56b20.jsonl[5785] _id=6ace5ddbde269131f9cf870d ts=2026-10-13T16:35:38.6980000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[7711] _id=6acfa08bde269131f9d4bc17 ts=2026-10-14T15:32:26.4830000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 40 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6ab9a8e69a8420a1e6b56b20.jsonl[15888] _id=6ad1070dde269131f9de3978 ts=2026-10-15T17:02:04.5340000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[15889] _id=6ad1070dde269131f9de397a ts=2026-10-15T17:02:04.5380000Z; 6ms: 6ab9a8e69a8420a1e6b56b20.jsonl[852] _id=6ac3d68ade269131f9ae404b ts=2026-10-05T16:55:37.4100000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[861] _id=6ac3d68ade269131f9ae404f ts=2026-10-05T16:55:37.4160000Z; 7ms: 6ab9a8e69a8420a1e6b56b20.jsonl[7721] _id=6acfa094de269131f9d4bc7b ts=2026-10-14T15:32:35.4680000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[7722] _id=6acfa094de269131f9d4bc7d ts=2026-10-14T15:32:35.4750000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 15m 0s 
  - Evidence: 15m 0s: 6ab9a8e69a8420a1e6b56b20.jsonl[14484] _id=6ad1021ade269131f9ddb9b0 ts=2026-10-15T16:40:57.0900000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[15602] _id=6ad1059ede269131f9de14c4 ts=2026-10-15T16:55:57.3140000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b20.jsonl[5383] _id=6ac7ccb7de269131f9c4db20 ts=2026-10-08T17:02:47.0420000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5403] _id=6ace59fbde269131f9cf5961 ts=2026-10-13T16:19:06.0720000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b20.jsonl[2342] _id=6ac67405de269131f9bc8aa5 ts=2026-10-07T16:32:04.2380000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4067] _id=6ac7c4e8de269131f9c429e5 ts=2026-10-08T16:29:27.7300000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b20.jsonl[1093] _id=6ac3d82ade269131f9ae69f5 ts=2026-10-05T17:02:33.5160000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1192] _id=6ac5275cde269131f9b57971 ts=2026-10-06T16:52:43.4990000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b20.jsonl[5382] _id=6ac7ccb7de269131f9c4db1f ts=2026-10-08T17:02:47.0420000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5402] _id=6ace59fbde269131f9cf5960 ts=2026-10-13T16:19:06.0720000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b20.jsonl[2341] _id=6ac67405de269131f9bc8aa4 ts=2026-10-07T16:32:04.2380000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4066] _id=6ac7c4e8de269131f9c429e4 ts=2026-10-08T16:29:27.7300000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b20.jsonl[1092] _id=6ac3d82ade269131f9ae69f2 ts=2026-10-05T17:02:33.5140000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1191] _id=6ac5275cde269131f9b5796b ts=2026-10-06T16:52:43.4970000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8e69a8420a1e6b56b20.jsonl[5400] _id=6ace59fade269131f9cf5959 ts=2026-10-08T17:03:31.95Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[6062] _id=6ace6088de269131f9cfbb00 ts=2026-10-13T16:47:03.1180000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b20.jsonl[2339] _id=6ac67405de269131f9bc8aa1 ts=2026-10-06T17:04:28.383Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[4069] _id=6ac7c4e8de269131f9c429dd ts=2026-10-07T17:04:36.352Z; 23h 59m: 6ab9a8e69a8420a1e6b56b20.jsonl[1193] _id=6ac5275cde269131f9b57951 ts=2026-10-05T17:04:38.25Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2339] _id=6ac67405de269131f9bc8aa1 ts=2026-10-06T17:04:28.383Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b20.jsonl[5396] _id=6ac7ccc9de269131f9c4dc06 ts=2026-10-08T17:03:03.6420000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[5413] _id=6ace5a0cde269131f9cf59bb ts=2026-10-13T16:19:22.2660000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b20.jsonl[1133] _id=6ac3d7a5de269131f9ae5ced ts=2026-10-05T17:00:21.2050000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[1217] _id=6ac52812de269131f9b59ef1 ts=2026-10-06T16:55:45.3390000Z; 23h 38m: 6ab9a8e69a8420a1e6b56b20.jsonl[1217] _id=6ac52812de269131f9b59ef1 ts=2026-10-06T16:55:45.3390000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[2378] _id=6ac6746ade269131f9bc92df ts=2026-10-07T16:33:45.7780000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[15136] _id=6ad103cade269131f9ddde37 ts=2026-10-15T16:48:09.5530000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[15137] _id=6ad103cade269131f9ddde38 ts=2026-10-15T16:48:09.5530000Z; 0ms: 6ab9a8e69a8420a1e6b56b20.jsonl[15962] _id=6ad10787de269131f9de4555 ts=2026-10-15T17:04:06.5750000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[15963] _id=6ad10787de269131f9de4556 ts=2026-10-15T17:04:06.5750000Z; 1ms: 6ab9a8e69a8420a1e6b56b20.jsonl[11599] _id=6acfb244de269131f9d5d871 ts=2026-10-14T16:48:03.5940000Z -> 6ab9a8e69a8420a1e6b56b20.jsonl[11600] _id=6acfb244de269131f9d5d872 ts=2026-10-14T16:48:03.5950000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[687] _id=6ac3d637de269131f9ae35b9 ts=2026-10-05T16:54:15.0360000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[967] _id=6ac3d729de269131f9ae4fad ts=2026-10-05T16:58:17.1850000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[4974] _id=6ac7c804de269131f9c48566 ts=2026-10-08T16:42:43.7740000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 15 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1858] _id=6ac52952de269131f9b5e577 ts=2026-10-06T17:01:04.6840000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1835] _id=6ac52969de269131f9b5eadb ts=2026-10-06T17:01:27.4120000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1836] _id=6ac52969de269131f9b5eadf ts=2026-10-06T17:01:27.4150000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 67 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1643] _id=6ac528bdde269131f9b5c9a2 ts=2026-10-06T16:58:33.9440000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1652] _id=6ac528bede269131f9b5c9cd ts=2026-10-06T16:58:33.9440000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1745] _id=6ac5293ede269131f9b5e131 ts=2026-10-06T16:58:35.4990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[7778] _id=6acfa0e0de269131f9d4bfe0 ts=2026-10-14T15:33:52.0050000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[13716] _id=6ad0fadbde269131f9dd4dde ts=2026-10-15T16:10:02.9070000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[13998] _id=6ad0fdf1de269131f9dd6c7a ts=2026-10-15T16:23:12.4120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[883] _id=6ac3d6a9de269131f9ae4367 ts=2026-10-05T16:56:08.3100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[14484] _id=6ad1021ade269131f9ddb9b0 ts=2026-10-15T16:40:57.0900000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[15602] _id=6ad1059ede269131f9de14c4 ts=2026-10-15T16:55:57.3140000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 109 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1882] _id=6ac52959de269131f9b5e73b ts=2026-10-06T17:01:12.0460000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[2008] _id=6ac5297ade269131f9b5ee0d ts=2026-10-06T17:01:45.4110000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[2012] _id=6ac5297cde269131f9b5ee41 ts=2026-10-06T17:01:47.0780000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 431 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1605] _id=6ac528bbde269131f9b5c8d0 ts=2026-10-06T16:58:33.1710000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1568] _id=6ac528bbde269131f9b5c8d8 ts=2026-10-06T16:58:33.1710000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1634] _id=6ac528bbde269131f9b5c8e4 ts=2026-10-06T16:58:33.1710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[4187] _id=6ac7c55ede269131f9c43392 ts=2026-10-08T16:31:25.7550000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 429 start, 419 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameCameraCentered' (totals: 712 open, 715 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 63 unmatched 'BecameVisible' (totals: 996 open, 1000 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 49 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 533 of 15967 adjacent _id pairs reverse in client time; worst 128.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b20.jsonl[1731] _id=6ac5293cde269131f9b5e0cc ts=2026-10-06T17:00:43.5170000Z`; `6ab9a8e69a8420a1e6b56b20.jsonl[1732] _id=6ac5293dde269131f9b5e109 ts=2026-10-06T16:58:35.3270000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.94s, min -429334.80s, max -0.10s over 15968 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b20\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)

## 9. Event-Type Details

### `InputEvent` — 7393 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1640); Unit 2 Prod (Refactor) (1482); Unit 4 Dev - Dungeon (1029); Unit 3 Dungeon Dev (947); Unit 4 Dev (845); Unit 1 Dev (670); Unit 5 Dev - Dungeon (479); Unit 4 Dev - Anderson Base (162); Unit 5 Dev (139)
- **Intervals:** median 0.32s (p5 0.01s / p95 4.94s, n=7392)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 7393/7393 records)
    "pressed"  x7393
data.actionType  (string, 7393/7393 records)
    "Move"  x5652
    "Interact"  x611
    "Jump"  x594
    "Sprint"  x389
    "Ascend"  x49
    "Map"  x37
    "Descend"  x30
    "Hoverboard"  x25
    "ToggleDebug"  x4
    "Pause"  x1
    "SkipCinematic"  x1
data.key  (string, 7393/7393 records, 11 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 7393/7393 records)
    "Player"  x6141
    "Drone"  x1252
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3423 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1792); Unit 3 Dungeon Dev (664); Unit 4 Dev (541); Unit 5 Dev - Dungeon (426)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.37s, n=3422)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3423/3423 records)
    "BecameInvisible"  x1000
    "BecameVisible"  x996
    "BecameCameraUncentered"  x715
    "BecameCameraCentered"  x712
data.pieceId  (string, 3423/3423 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3423/3423 records)
    1984 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2225 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (614); Unit 3 Dev (450); Unit 4 Dev (312); Unit 3 Dungeon Dev (214); Unit 1 Dev (195); Unit 4 Dev - Anderson Base (169); Unit 5 Dev (103); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (69)
- **eventKey:** present on 1377 of 2225 records
- **Intervals:** median 4.01s (p5 0.00s / p95 25.22s, n=2224)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1377; [conversationId, dialogueEventType] x848
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2225/2225 records)
    numeric range 8 .. 117 (53 unique)
data.dialogueEventType  (string, 2225/2225 records)
    "DialogueNodeEvent"  x1377
    "DialogueStartEvent"  x429
    "DialogueFinishEvent"  x419
data.nodeId  (number, 1377/2225 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1783 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (592); Unit 3 Dev (310); Unit 4 Dev (228); Unit 1 Dev (166); Unit 3 Dungeon Dev (141); Unit 4 Dev - Anderson Base (110); Unit 4 Dev - Dungeon (97); Unit 5 Dev - Dungeon (89); Unit 5 Dev (50)
- **Intervals:** median 10.00s (p5 9.93s / p95 10.13s, n=1769)
- **Fields under `data`:**

```text
data.position  (object, 1783/1783 records)
data.position.x  (number, 1783/1783 records)
    numeric range -687.068 .. 1557.52 (569 unique)
data.position.y  (number, 1783/1783 records)
    numeric range -115.127 .. 223.456 (394 unique)
data.position.z  (number, 1783/1783 records)
    numeric range -1033.4 .. 1973 (568 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 414 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (212); Unit 1 Dev (62); Unit 5 Dev (60); Unit 2 Prod (Refactor) (41); Unit 3 Dev (39)
- **Intervals:** median 0.74s (p5 0.03s / p95 9.17s, n=413)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 414/414 records)
    "argumentationNodeHoverEnd"  x178
    "argumentationNodeHoverStart"  x177
    "argumentationNodeAdd"  x42
    "argumentationNodeRemove"  x17
data.argumentationTitle  (string, 414/414 records)
    "Unit 4 - Flooding"  x212
    "Unit 5"  x60
    "Unit 2 – Watershed"  x41
    "Unit 3 - Pollution Upstream"  x39
    "Unit 1 - Argumentation Tutorial"  x33
    "Unit 1 - Freshwater"  x29
data.nodeName  (string, 414/414 records)
    "I"  x75
    "II"  x62
    "C"  x51
    "2"  x46
    "A"  x36
    "3"  x35
    "B"  x30
    "1"  x29
    "D"  x27
    "4"  x20
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 279 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (69); Unit 4 Dev - Dungeon (63); Unit 2 Prod (Refactor) (61); Unit 4 Dev (22); Unit 5 Dev - Dungeon (20); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (12); Unit 1 Dev (10); Unit 5 Dev (4)
- **Intervals:** median 9.41s (p5 0.86s / p95 438.60s, n=278)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 279/279 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 279/279 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 97 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (62); Unit 4 Dev (19); Unit 3 Dev (16)
- **Intervals:** median 0.92s (p5 0.09s / p95 561.72s, n=96)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x88; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/97 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/97 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 88/97 records)
    "RightDrag"  x47
    "LeftDrag"  x41
data.currentSoilType  (string, 88/97 records)
    "SAND"  x18
    "CLAY"  x16
    "CLAYSAND"  x16
    "CLAYROCK"  x14
    "SANDGRAVEL"  x14
    "BEDROCK"  x5
    "GRAVEL"  x5
data.isCorrectSelection  (string, 88/97 records)
    "false"  x68
    "true"  x20
data.waterLevelStatus  (string, 88/97 records)
    "TooHigh"  x45
    "Proper"  x26
    "TooLow"  x17
data.waterRetentionChange  (string, 88/97 records)
    "Increase"  x41
    "Decrease"  x27
    "NoChange"  x20
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev (12); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (4); Unit 5 Dev (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 203.53s (p5 0.00s / p95 82209.65s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x32
data.questID  (string, 81/81 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/81 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 70 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (43); Unit 3 Dev (19); Unit 4 Dev (6); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.90s (p5 0.10s / p95 81633.36s, n=69)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, legendName] x16; [actionType, featureUsed, location] x14
- **Fields under `data`:**

```text
data.actionType  (string, 70/70 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
    "Unselected"  x10
    "WaypointMoveEvent"  x9
    "Selected"  x6
    "WaypointSetEvent"  x5
data.featureUsed  (string, 70/70 records)
    "Map"  x40
    "Legend"  x16
    "Waypoint"  x14
data.legendName  (string, 16/70 records)
    "330 ft"  x16
data.location  (object, 14/70 records)
data.location.x  (number, 14/70 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 14/70 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 14/70 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 46 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (19); Unit 1 Dev (17); Unit 3 Dev (5); Unit 5 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 4.14s (p5 0.15s / p95 66575.46s, n=45)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "submitAnswerEvent"  x46
data.answerSubmitted  (string, 46/46 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 46/46 records)
    "Unit 4 - Flooding"  x19
    "Unit 1 - Freshwater"  x16
    "Unit 3 - Pollution Upstream"  x5
    "Unit 5"  x3
    "Unit 2 – Watershed"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 37 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (7); Unit 4 Dev (6); Unit 3 Dev (4); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 422.34s (p5 10.38s / p95 85899.86s, n=36)
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "DebugMenuStateChanged"  x37
data.isOpened  (bool, 37/37 records)
    false  x37
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 26 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (26)
- **Intervals:** median 6.86s (p5 1.50s / p95 47.04s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "On"  x19
    "Off"  x7
data.floor  (string, 26/26 records)
    "3"  x12
    "4"  x9
    "2"  x3
    "1"  x2
data.machineNumber  (string, 26/26 records)
    "One"  x25
    "Two"  x1
data.machineType  (string, 26/26 records)
    "Condenser"  x11
    "Evaporator"  x6
    "DualChamber_Condenser"  x5
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 26/26 records)
    "2"  x12
    "3"  x8
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 23 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 4 Dev (3); Unit 3 Dev (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1456.16s (p5 8.73s / p95 86221.82s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 75.02s (p5 0.03s / p95 238584.74s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 17/17 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 4 - Flooding"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 1999.31s (p5 899.17s / p95 189184.15s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 3 Dev (3); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1698.22s (p5 20.14s / p95 207019.09s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 5.13s (p5 1.72s / p95 28.12s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records, 4 empty-string)
    "cameraPlaced"  x6
    ""  x4
data.boxId  (string, 10/10 records)
    "0"  x4
    "1"  x3
    "2"  x3
data.soilType  (string, 10/10 records)
    "Sand"  x5
    "Clay"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 4.16s (p5 2.21s / p95 698160.98s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 87187.63s (p5 85596.15s / p95 629679.89s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 1.95s (p5 1.95s / p95 1.95s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 900.22s (p5 900.22s / p95 900.22s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `soilMachine` — 1 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "ChangeCanister"  x1
data.canisterType  (string, 1/1 records)
    "Gravel"  x1
data.floor  (string, 1/1 records)
    "5"  x1
data.machine  (string, 1/1 records)
    "2"  x1
data.row  (string, 1/1 records)
    "TopRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (62 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "Selected" (6x); "Unselected" (10x); "WaypointMoveEvent" (9x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (16x); "Waypoint" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (17x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*