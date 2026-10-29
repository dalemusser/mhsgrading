# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b28

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b28
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b28.jsonl
- **Records:** 13232 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b28
- **Time span:** 2026-10-05T16:32:01.693000+00:00 .. 2026-10-16T17:05:02.012000+00:00 (264h 33m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b28\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 13232 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 103 INFO, 0 NOT_TESTED, 94 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4520 | 34.16 | 1 | 4 | 0 | 2026-10-06T16:47:57.416000+00:00 | 2026-10-16T16:50:10.827000+00:00 | 240h 2m |
| InputEvent | 3463 | 26.17 | 1 | 9 | 0 | 2026-10-05T16:32:35.043000+00:00 | 2026-10-16T17:04:39.072000+00:00 | 264h 32m |
| DialogueEvent | 2071 | 15.65 | 1 | 9 | 1274 | 2026-10-05T16:32:51.631000+00:00 | 2026-10-16T17:04:59.089000+00:00 | 264h 32m |
| PlayerPositionEvent | 1766 | 13.35 | 1 | 9 | 0 | 2026-10-05T16:32:31.508000+00:00 | 2026-10-16T17:05:02.012000+00:00 | 264h 32m |
| argumentationNodeEvent | 671 | 5.07 | 1 | 4 | 0 | 2026-10-05T16:56:18.442000+00:00 | 2026-10-16T16:29:43.754000+00:00 | 263h 33m |
| ObjectInterEvent | 286 | 2.16 | 1 | 9 | 0 | 2026-10-05T16:37:37.870000+00:00 | 2026-10-16T17:04:40.965000+00:00 | 264h 27m |
| Soil Key Puzzle | 74 | 0.56 | 1 | 3 | 0 | 2026-10-06T17:03:42.019000+00:00 | 2026-10-15T16:40:08.052000+00:00 | 215h 36m |
| questEvent | 74 | 0.56 | 1 | 9 | 74 | 2026-10-05T16:32:51.604000+00:00 | 2026-10-16T17:02:53.104000+00:00 | 264h 30m |
| TopographicMapEvent | 59 | 0.45 | 1 | 3 | 0 | 2026-10-05T16:55:23.504000+00:00 | 2026-10-14T17:02:08.158000+00:00 | 216h 6m |
| argumentationAnswerEvent | 53 | 0.4 | 1 | 4 | 0 | 2026-10-05T16:57:32.600000+00:00 | 2026-10-16T16:29:49.751000+00:00 | 263h 32m |
| DEBUGMenu | 33 | 0.25 | 1 | 9 | 0 | 2026-10-05T16:32:31.495000+00:00 | 2026-10-16T16:45:06.284000+00:00 | 264h 12m |
| WaterChamberEvent | 30 | 0.23 | 1 | 1 | 0 | 2026-10-16T16:49:21.622000+00:00 | 2026-10-16T16:59:13.315000+00:00 | 9m 51s |
| soilMachine | 22 | 0.17 | 1 | 1 | 0 | 2026-10-15T16:54:31.225000+00:00 | 2026-10-15T17:02:35.091000+00:00 | 8m 3s |
| gameWindowFocusEvent | 21 | 0.16 | 1 | 4 | 0 | 2026-10-05T16:32:01.693000+00:00 | 2026-10-16T16:44:59.534000+00:00 | 264h 12m |
| DaniEvent | 20 | 0.15 | 1 | 3 | 0 | 2026-10-05T16:55:20.747000+00:00 | 2026-10-14T16:58:23.206000+00:00 | 216h 3m |
| TerasGardenBox | 15 | 0.11 | 1 | 1 | 0 | 2026-10-16T16:34:33.740000+00:00 | 2026-10-16T16:36:02.892000+00:00 | 1m 29s |
| gameStartEvent | 15 | 0.11 | 1 | 1 | 0 | 2026-10-05T16:32:01.694000+00:00 | 2026-10-16T16:44:59.534000+00:00 | 264h 12m |
| argumentationEvent | 14 | 0.11 | 1 | 4 | 0 | 2026-10-05T16:57:12.114000+00:00 | 2026-10-16T16:29:49.808000+00:00 | 263h 32m |
| gameWindowUnfocusEvent | 13 | 0.1 | 1 | 3 | 0 | 2026-10-05T17:05:02.034000+00:00 | 2026-10-15T16:41:29.325000+00:00 | 239h 36m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-05T17:02:20.222000+00:00 | 2026-10-16T16:44:17.830000+00:00 | 263h 41m |
| argumentationToolEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-05T16:57:08.530000+00:00 | 2026-10-14T16:29:42.862000+00:00 | 215h 32m |
| chatEvent | 4 | 0.03 | 1 | 3 | 0 | 2026-10-06T16:55:44.586000+00:00 | 2026-10-16T17:00:10.026000+00:00 | 240h 4m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172119.455s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.056s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.773s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.901s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 11.41s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 180.569s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.476s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 42997.178s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1506.842s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1529.376s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.742s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 20 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up; Press E to place glyph 
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
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.6x vs baseline. 
  - Observed: 53 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,II; A,B,2,I; A,B,2,II; A,B,C,2,II; A,B,D,2,II; A,C,2,II; A,D,2,II; B,2,II; B,D,2,II; B,D,A,3,II; C,2,II; C,4,II; C,B,2,II; C,B,3,II; C,D,A,2,II; C,D,B,2,II; D,1,I; D,2,II; D,4,II; D,B,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 671 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-179, 68-1, 68-2, 68-3, 68-5] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.4x vs baseline. 
  - Observed: 22 records 
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
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[146] _id=6ac3d2c2de269131f9ade83d ts=2026-10-05T16:39:30.1120000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[190] _id=6ac3d3a0de269131f9adf715 ts=2026-10-05T16:43:11.7240000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[238] _id=6ac3d45ade269131f9ae09a1 ts=2026-10-05T16:46:17.1440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[7] _id=6ac3d102de269131f9adc1fd ts=2026-10-05T16:32:01.6940000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[602] _id=6ac3d876de269131f9ae6feb ts=2026-10-05T17:03:49.9660000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[642] _id=6ac52557de269131f9b532fa ts=2026-10-06T16:44:07.3450000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[8] _id=6ac3d102de269131f9adc1f9 ts=2026-10-05T16:32:01.6930000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[601] _id=6ac3d876de269131f9ae6fe7 ts=2026-10-05T17:03:49.9640000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[643] _id=6ac52557de269131f9b532f5 ts=2026-10-06T16:44:07.3440000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[641] _id=6ac52557de269131f9b532e7 ts=2026-10-05T17:05:02.034Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[2629] _id=6ac6741bde269131f9bc8bff ts=2026-10-06T17:05:11.093Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[4860] _id=6ac67ba2de269131f9bd9066 ts=2026-10-07T17:04:33.8720000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4519 | 0.0 | 0.056 | 191.222 | 1.501 | 518283.719 | 0.31 | 2155 | 7 |
| InputEvent | 3462 | 0.0 | 1.045 | 275.079 | 16.254 | 430365.452 | 0.22 | 149 | 9 |
| DialogueEvent | 2070 | 0.0 | 4.121 | 460.062 | 31.397 | 430267.258 | 0.13 | 594 | 7 |
| PlayerPositionEvent | 1754 | 9.766 | 10.003 | 542.767 | 10.167 | 430246.332 | 0.11 | 0 | 7 |
| argumentationNodeEvent | 670 | 0.007 | 0.542 | 1416.127 | 9.742 | 430270.037 | 0.04 | 59 | 5 |
| ObjectInterEvent | 285 | 0.0 | 11.766 | 3340.432 | 416.401 | 431427.062 | 0.02 | 5 | 11 |
| Soil Key Puzzle | 73 | 0.048 | 1.23 | 10632.685 | 34027.701 | 518637.566 | 0.01 | 1 | 4 |
| questEvent | 73 | 0.003 | 200.069 | 13043.856 | 84143.182 | 431566.964 | 0.0 | 11 | 12 |
| TopographicMapEvent | 58 | 0.017 | 8.901 | 13413.873 | 84781.501 | 432222.225 | 0.0 | 2 | 8 |
| argumentationAnswerEvent | 52 | 0.162 | 11.41 | 18244.945 | 39024.46 | 689910.317 | 0.0 | 0 | 4 |
| DEBUGMenu | 32 | 6.903 | 466.568 | 29723.587 | 85900.292 | 432362.295 | 0.0 | 0 | 15 |
| WaterChamberEvent | 29 | 0.258 | 11.189 | 20.403 | 68.068 | 80.738 | 2.94 | 0 | 0 |
| soilMachine | 21 | 0.205 | 6.742 | 23.041 | 73.16 | 169.674 | 2.6 | 0 | 0 |
| gameWindowFocusEvent | 20 | 1.801 | 1506.842 | 47558.892 | 103735.758 | 430494.191 | 0.0 | 0 | 11 |
| DaniEvent | 19 | 0.197 | 2.75 | 40935.919 | 137793.365 | 605055.452 | 0.0 | 0 | 3 |
| TerasGardenBox | 14 | 0.75 | 1.773 | 6.368 | 24.167 | 24.535 | 9.42 | 0 | 0 |
| gameStartEvent | 14 | 50.899 | 42997.178 | 67941.274 | 207579.584 | 432371.198 | 0.0 | 0 | 10 |
| argumentationEvent | 13 | 0.043 | 180.569 | 72981.361 | 327828.076 | 430278.762 | 0.0 | 2 | 5 |
| gameWindowUnfocusEvent | 12 | 0.0 | 1529.376 | 71882.274 | 288024.263 | 431998.985 | 0.0 | 1 | 7 |
| EndOfUnit | 3 | 87115.872 | 172119.455 | 316439.203 | 638285.998 | 690082.281 | 0.0 | 0 | 3 |
| argumentationToolEvent | 3 | 2.295 | 3.476 | 258651.444 | 698354.052 | 775948.561 | 0.0 | 0 | 1 |
| chatEvent | 3 | 7.17 | 903.862 | 288088.48 | 777109.353 | 863354.408 | 0.0 | 0 | 2 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 16 group(s), 62 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[2639] _id=6ac67428de269131f9bc8d28 ts=2026-10-07T16:32:39.3300000Z == 6ab9a8e69a8420a1e6b56b28.jsonl[2640] _id=6ac67428de269131f9bc8d29 ts=2026-10-07T16:32:39.3300000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[2647] _id=6ac67428de269131f9bc8d30 ts=2026-10-07T16:32:39.3310000Z == 6ab9a8e69a8420a1e6b56b28.jsonl[2648] _id=6ac67428de269131f9bc8d31 ts=2026-10-07T16:32:39.3310000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[4882] _id=6ac7c4f6de269131f9c42a71 ts=2026-10-08T16:29:39.8560000Z == 6ab9a8e69a8420a1e6b56b28.jsonl[4884] _id=6ac7c4f6de269131f9c42a72 ts=2026-10-08T16:29:39.8560000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 69 group(s), 115 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[786] _id=6ac526b6de269131f9b564ad ts=2026-10-06T16:49:57.3180000Z == 6ab9a8e69a8420a1e6b56b28.jsonl[792] _id=6ac526b6de269131f9b564b3 ts=2026-10-06T16:49:57.3180000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[780] _id=6ac526b7de269131f9b564e7 ts=2026-10-06T16:49:57.5660000Z == 6ab9a8e69a8420a1e6b56b28.jsonl[793] _id=6ac526b7de269131f9b564ee ts=2026-10-06T16:49:57.5660000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[781] _id=6ac526bade269131f9b56545 ts=2026-10-06T16:49:58.9350000Z == 6ab9a8e69a8420a1e6b56b28.jsonl[794] _id=6ac526bbde269131f9b5655a ts=2026-10-06T16:49:58.9350000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `856ms: 6ab9a8e69a8420a1e6b56b28.jsonl[4476] _id=6ac67924de269131f9bd4f6e ts=2026-10-07T16:53:56.2620000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[4473] _id=6ac67925de269131f9bd4f86 ts=2026-10-07T16:53:57.1180000Z`; `578ms: 6ab9a8e69a8420a1e6b56b28.jsonl[4477] _id=6ac67925de269131f9bd4f80 ts=2026-10-07T16:53:56.9210000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[4480] _id=6ac67925de269131f9bd4f8e ts=2026-10-07T16:53:57.4990000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6ab9a8e69a8420a1e6b56b28.jsonl[107] _id=6ac3d252de269131f9adde31 ts=2026-10-05T16:37:37.8700000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[108] _id=6ac3d252de269131f9adde36 ts=2026-10-05T16:37:37.8800000Z`; `730ms: 6ab9a8e69a8420a1e6b56b28.jsonl[5098] _id=6ac7c648de269131f9c44d37 ts=2026-10-08T16:35:18.9830000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[5107] _id=6ac7c648de269131f9c44d4d ts=2026-10-08T16:35:19.7130000Z`; `562ms: 6ab9a8e69a8420a1e6b56b28.jsonl[5106] _id=6ac7c649de269131f9c44d5d ts=2026-10-08T16:35:20.2010000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[5111] _id=6ac7c64ade269131f9c44d77 ts=2026-10-08T16:35:20.7630000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 184 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a8e69a8420a1e6b56b28.jsonl[826] _id=6ac526bbde269131f9b56570 ts=2026-10-06T16:49:58.9350000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[795] _id=6ac526bbde269131f9b56576 ts=2026-10-06T16:49:58.9410000Z`; `83ms: 6ab9a8e69a8420a1e6b56b28.jsonl[795] _id=6ac526bbde269131f9b56576 ts=2026-10-06T16:49:58.9410000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[815] _id=6ac526bbde269131f9b5657b ts=2026-10-06T16:49:59.0240000Z`; `11ms: 6ab9a8e69a8420a1e6b56b28.jsonl[796] _id=6ac526bcde269131f9b5659b ts=2026-10-06T16:49:59.0240000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[802] _id=6ac526bcde269131f9b5659d ts=2026-10-06T16:49:59.0350000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `750ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12247] _id=6ad2521dde269131f9e5eeec ts=2026-10-16T16:34:36.9060000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[12248] _id=6ad2521ede269131f9e5ef05 ts=2026-10-16T16:34:37.6560000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `737ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11390] _id=6ad24c47de269131f9e5a1e6 ts=2026-10-16T16:09:43.6540000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[11395] _id=6ad24c48de269131f9e5a1fd ts=2026-10-16T16:09:44.3910000Z`; `705ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12006] _id=6ad25091de269131f9e5d81e ts=2026-10-16T16:28:01.0080000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[12007] _id=6ad25092de269131f9e5d824 ts=2026-10-16T16:28:01.7130000Z`; `361ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12007] _id=6ad25092de269131f9e5d824 ts=2026-10-16T16:28:01.7130000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[12004] _id=6ad25092de269131f9e5d82a ts=2026-10-16T16:28:02.0740000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `43ms: 6ab9a8e69a8420a1e6b56b28.jsonl[7593] _id=6acfae23de269131f9d57e74 ts=2026-10-14T16:30:26.5040000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[7596] _id=6acfae23de269131f9d57e78 ts=2026-10-14T16:30:26.5470000Z`; `43ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12124] _id=6ad250fede269131f9e5dfd2 ts=2026-10-16T16:29:49.7650000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[12127] _id=6ad250fede269131f9e5dfd5 ts=2026-10-16T16:29:49.8080000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 48 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `458ms: 6ab9a8e69a8420a1e6b56b28.jsonl[411] _id=6ac3d6b6de269131f9ae44b7 ts=2026-10-05T16:56:22.0040000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[412] _id=6ac3d6b7de269131f9ae44c1 ts=2026-10-05T16:56:22.4620000Z`; `905ms: 6ab9a8e69a8420a1e6b56b28.jsonl[429] _id=6ac3d6f3de269131f9ae4aa3 ts=2026-10-05T16:57:22.2560000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[431] _id=6ac3d6f3de269131f9ae4ab7 ts=2026-10-05T16:57:23.1610000Z`; `21ms: 6ab9a8e69a8420a1e6b56b28.jsonl[428] _id=6ac3d6fade269131f9ae4b3c ts=2026-10-05T16:57:29.1930000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[443] _id=6ac3d6fade269131f9ae4b44 ts=2026-10-05T16:57:29.2140000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[4860] _id=6ac67ba2de269131f9bd9066 ts=2026-10-07T17:04:33.8720000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[4864] _id=6ac7c4b4de269131f9c42658 ts=2026-10-07T17:04:33.872Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `865ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10717] _id=6ad1072ade269131f9de3c0d ts=2026-10-15T17:02:33.7270000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[10731] _id=6ad1072bde269131f9de3c2d ts=2026-10-15T17:02:34.5920000Z`; `294ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10731] _id=6ad1072bde269131f9de3c2d ts=2026-10-15T17:02:34.5920000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[10721] _id=6ad1072bde269131f9de3c36 ts=2026-10-15T17:02:34.8860000Z`; `205ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10721] _id=6ad1072bde269131f9de3c36 ts=2026-10-15T17:02:34.8860000Z ~ 6ab9a8e69a8420a1e6b56b28.jsonl[10722] _id=6ad1072bde269131f9de3c45 ts=2026-10-15T17:02:35.0910000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 120h 6m 
  - Evidence: 120h 6m: 6ab9a8e69a8420a1e6b56b28.jsonl[4883] _id=6ac7c4f0de269131f9c42a49 ts=2026-10-08T16:29:35.2550000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6171] _id=6ace5dd9de269131f9cf86e7 ts=2026-10-13T16:35:37.5500000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b28.jsonl[2635] _id=6ac67425de269131f9bc8cd2 ts=2026-10-07T16:32:37.1780000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4861] _id=6ac7c4b4de269131f9c4265a ts=2026-10-08T16:28:35.4730000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b28.jsonl[640] _id=6ac52561de269131f9b533f3 ts=2026-10-06T16:44:17.2200000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[2630] _id=6ac6741bde269131f9bc8c01 ts=2026-10-07T16:32:26.4180000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 4m 
  - Evidence: 168h 4m: 6ab9a8e69a8420a1e6b56b28.jsonl[4486] _id=6ac6792dde269131f9bd5015 ts=2026-10-07T16:54:05.7560000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[8624] _id=6acfb4aede269131f9d61a0e ts=2026-10-14T16:58:21.2080000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b28.jsonl[600] _id=6ac3d89bde269131f9ae72c3 ts=2026-10-05T17:04:26.2720000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[1650] _id=6ac5280ede269131f9b59e41 ts=2026-10-06T16:55:41.6270000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b28.jsonl[2581] _id=6ac529dade269131f9b5ff8f ts=2026-10-06T17:03:21.9980000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4393] _id=6ac67848de269131f9bd3870 ts=2026-10-07T16:50:16.1350000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a8e69a8420a1e6b56b28.jsonl[6162] _id=6ac7cd2fde269131f9c4e046 ts=2026-10-08T17:04:45.9310000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6175] _id=6ace5de9de269131f9cf8878 ts=2026-10-13T16:35:53.1890000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b28.jsonl[638] _id=6ac3d8b5de269131f9ae74ef ts=2026-10-05T17:04:52.6040000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[646] _id=6ac52565de269131f9b53429 ts=2026-10-06T16:44:20.8240000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b28.jsonl[2621] _id=6ac52a2cde269131f9b60d0b ts=2026-10-06T17:04:44.3450000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[2667] _id=6ac6743ade269131f9bc8e8b ts=2026-10-07T16:32:58.2730000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 594 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11335] _id=6ad24c0ade269131f9e59d49 ts=2026-10-16T16:08:41.9700000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11336] _id=6ad24c0ade269131f9e59d4a ts=2026-10-16T16:08:41.9700000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11433] _id=6ad24c6bde269131f9e5a473 ts=2026-10-16T16:10:19.2320000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11434] _id=6ad24c6bde269131f9e5a474 ts=2026-10-16T16:10:19.2320000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11448] _id=6ad24c77de269131f9e5a526 ts=2026-10-16T16:10:30.9040000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11449] _id=6ad24c77de269131f9e5a527 ts=2026-10-16T16:10:30.9040000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 41m 
  - Evidence: 191h 41m: 6ab9a8e69a8420a1e6b56b28.jsonl[598] _id=6ac3d81cde269131f9ae690d ts=2026-10-05T17:02:20.2220000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6426] _id=6ace5fbede269131f9cfae09 ts=2026-10-13T16:43:42.5030000Z; 47h 48m: 6ab9a8e69a8420a1e6b56b28.jsonl[6426] _id=6ace5fbede269131f9cfae09 ts=2026-10-13T16:43:42.5030000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[8940] _id=6ad10016de269131f9dd9a06 ts=2026-10-15T16:32:21.9580000Z; 24h 11m: 6ab9a8e69a8420a1e6b56b28.jsonl[8940] _id=6ad10016de269131f9dd9a06 ts=2026-10-15T16:32:21.9580000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[12506] _id=6ad25462de269131f9e60dff ts=2026-10-16T16:44:17.8300000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a8e69a8420a1e6b56b28.jsonl[6124] _id=6ac7cccade269131f9c4dc1e ts=2026-10-08T17:03:05.3420000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6177] _id=6ace5de8de269131f9cf885c ts=2026-10-13T16:35:50.7940000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b28.jsonl[633] _id=6ac3d8aade269131f9ae73c1 ts=2026-10-05T17:04:41.3330000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[649] _id=6ac52572de269131f9b535b3 ts=2026-10-06T16:44:34.2710000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b28.jsonl[2604] _id=6ac52a04de269131f9b606dd ts=2026-10-06T17:04:03.7110000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[2637] _id=6ac67428de269131f9bc8d26 ts=2026-10-07T16:32:39.3280000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 149 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10548] _id=6ad10655de269131f9de26ee ts=2026-10-15T16:59:01.0090000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10549] _id=6ad10655de269131f9de26ef ts=2026-10-15T16:59:01.0090000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10760] _id=6ad1077bde269131f9de43c3 ts=2026-10-15T17:03:54.9050000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10761] _id=6ad1077bde269131f9de43c4 ts=2026-10-15T17:03:54.9050000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10762] _id=6ad1077bde269131f9de43c5 ts=2026-10-15T17:03:54.9060000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10763] _id=6ad1077bde269131f9de43c6 ts=2026-10-15T17:03:54.9060000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a8e69a8420a1e6b56b28.jsonl[6102] _id=6ac7cc91de269131f9c4d95e ts=2026-10-08T17:02:08.0220000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6561] _id=6ace61d3de269131f9cfd247 ts=2026-10-13T16:52:35.0840000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b28.jsonl[4217] _id=6ac6762cde269131f9bce95b ts=2026-10-07T16:41:16.3130000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4958] _id=6ac7c558de269131f9c4330d ts=2026-10-08T16:31:19.2310000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b28.jsonl[582] _id=6ac3d7f1de269131f9ae6452 ts=2026-10-05T17:01:36.5480000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[714] _id=6ac5260ede269131f9b54b54 ts=2026-10-06T16:47:10.6550000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11170] _id=6ad24b09de269131f9e58cc2 ts=2026-10-16T16:04:25.1760000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11171] _id=6ad24b09de269131f9e58cc3 ts=2026-10-16T16:04:25.1760000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11236] _id=6ad24b4bde269131f9e59143 ts=2026-10-16T16:05:31.2830000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11237] _id=6ad24b4bde269131f9e59144 ts=2026-10-16T16:05:31.2830000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[11532] _id=6ad24e5ade269131f9e5b149 ts=2026-10-16T16:18:33.6860000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11533] _id=6ad24e5ade269131f9e5b14a ts=2026-10-16T16:18:33.6860000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a8e69a8420a1e6b56b28.jsonl[6167] _id=6ac7cd3ede269131f9c4e06c ts=2026-10-08T17:05:01.7060000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6176] _id=6ace5de8de269131f9cf885b ts=2026-10-13T16:35:48.0380000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b28.jsonl[639] _id=6ac3d8b8de269131f9ae751b ts=2026-10-05T17:04:55.0510000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[644] _id=6ac52564de269131f9b5341f ts=2026-10-06T16:44:17.2300000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b28.jsonl[2623] _id=6ac52a3ede269131f9b60eeb ts=2026-10-06T17:05:02.1040000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[2636] _id=6ac67428de269131f9bc8d25 ts=2026-10-07T16:32:37.2000000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 58m 
  - Evidence: 143h 58m: 6ab9a8e69a8420a1e6b56b28.jsonl[5539] _id=6ac7c733de269131f9c470b5 ts=2026-10-08T16:39:13.6110000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7844] _id=6acfafbfde269131f9d59bec ts=2026-10-14T16:37:17.3300000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b28.jsonl[8084] _id=6acfb063de269131f9d5aca8 ts=2026-10-14T16:40:00.3210000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[9133] _id=6ad101ecde269131f9ddb62b ts=2026-10-15T16:40:11.7960000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b28.jsonl[4203] _id=6ac675ffde269131f9bce2db ts=2026-10-07T16:40:28.5960000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[5029] _id=6ac7c5e9de269131f9c4439c ts=2026-10-08T16:33:43.2360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2155 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10000] _id=6ad102e5de269131f9ddcdba ts=2026-10-15T16:44:19.5140000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10001] _id=6ad102e5de269131f9ddcdbb ts=2026-10-15T16:44:19.5140000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10002] _id=6ad102e5de269131f9ddcdbc ts=2026-10-15T16:44:19.6000000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10007] _id=6ad102e5de269131f9ddcdc8 ts=2026-10-15T16:44:19.6000000Z; 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10004] _id=6ad102e5de269131f9ddcdd2 ts=2026-10-15T16:44:19.8210000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10005] _id=6ad102e5de269131f9ddcdd3 ts=2026-10-15T16:44:19.8210000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 3m 
  - Evidence: 144h 3m: 6ab9a8e69a8420a1e6b56b28.jsonl[4983] _id=6ac7c591de269131f9c43847 ts=2026-10-08T16:32:16.5350000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7803] _id=6acfaf7fde269131f9d5970b ts=2026-10-14T16:36:14.1010000Z; 24h 2m: 6ab9a8e69a8420a1e6b56b28.jsonl[7815] _id=6acfaf97de269131f9d59962 ts=2026-10-14T16:36:38.9740000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[9078] _id=6ad101abde269131f9ddb2e5 ts=2026-10-15T16:39:06.5270000Z; 23h 49m: 6ab9a8e69a8420a1e6b56b28.jsonl[4219] _id=6ac6762fde269131f9bce9d6 ts=2026-10-07T16:41:19.3430000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4957] _id=6ac7c558de269131f9c4330a ts=2026-10-08T16:31:19.2260000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.048s..0.048s shown 
  - Evidence: 48ms: 6ab9a8e69a8420a1e6b56b28.jsonl[7803] _id=6acfaf7fde269131f9d5970b ts=2026-10-14T16:36:14.1010000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7805] _id=6acfaf7fde269131f9d59716 ts=2026-10-14T16:36:14.1490000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 3m 
  - Evidence: 120h 3m: 6ab9a8e69a8420a1e6b56b28.jsonl[5708] _id=6ac7c956de269131f9c4a6a0 ts=2026-10-08T16:48:20.9550000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6551] _id=6ace61b3de269131f9cfd080 ts=2026-10-13T16:52:03.1800000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b28.jsonl[389] _id=6ac3d681de269131f9ae3f74 ts=2026-10-05T16:55:28.9110000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[767] _id=6ac52685de269131f9b55ff5 ts=2026-10-06T16:49:08.2240000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b28.jsonl[4830] _id=6ac67b6dde269131f9bd8cbf ts=2026-10-07T17:03:41.4330000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[5704] _id=6ac7c942de269131f9c4a550 ts=2026-10-08T16:48:01.2270000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.017s..0.036s shown 
  - Evidence: 17ms: 6ab9a8e69a8420a1e6b56b28.jsonl[4375] _id=6ac67822de269131f9bd3507 ts=2026-10-07T16:49:38.1470000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4379] _id=6ac67822de269131f9bd350b ts=2026-10-07T16:49:38.1640000Z; 36ms: 6ab9a8e69a8420a1e6b56b28.jsonl[4374] _id=6ac67822de269131f9bd3503 ts=2026-10-07T16:49:38.1110000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4375] _id=6ac67822de269131f9bd3507 ts=2026-10-07T16:49:38.1470000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 38m 
  - Evidence: 191h 38m: 6ab9a8e69a8420a1e6b56b28.jsonl[505] _id=6ac3d767de269131f9ae55fb ts=2026-10-05T16:59:18.2700000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6272] _id=6ace5e5cde269131f9cf921f ts=2026-10-13T16:37:48.5870000Z; 47h 38m: 6ab9a8e69a8420a1e6b56b28.jsonl[7598] _id=6acfae23de269131f9d57e72 ts=2026-10-14T16:30:26.4840000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11334] _id=6ad24c0ade269131f9e59d45 ts=2026-10-16T16:08:41.9440000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b28.jsonl[6324] _id=6ace5ea9de269131f9cf9812 ts=2026-10-13T16:39:05.2230000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7592] _id=6acfae1ede269131f9d57e0b ts=2026-10-14T16:30:21.1020000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a8e69a8420a1e6b56b28.jsonl[6160] _id=6ac7cd2fde269131f9c4e043 ts=2026-10-08T17:04:45.9180000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6184] _id=6ace5df4de269131f9cf894d ts=2026-10-13T16:36:04.6800000Z; 72h 5m: 6ab9a8e69a8420a1e6b56b28.jsonl[506] _id=6ac3d767de269131f9ae5601 ts=2026-10-05T16:59:18.3000000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6160] _id=6ac7cd2fde269131f9c4e043 ts=2026-10-08T17:04:45.9180000Z; 47h 37m: 6ab9a8e69a8420a1e6b56b28.jsonl[7596] _id=6acfae23de269131f9d57e78 ts=2026-10-14T16:30:26.5470000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11295] _id=6ad24bdbde269131f9e59b20 ts=2026-10-16T16:07:54.9160000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.043s..0.043s shown 
  - Evidence: 43ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12124] _id=6ad250fede269131f9e5dfd2 ts=2026-10-16T16:29:49.7650000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[12127] _id=6ad250fede269131f9e5dfd5 ts=2026-10-16T16:29:49.8080000Z; 43ms: 6ab9a8e69a8420a1e6b56b28.jsonl[7593] _id=6acfae23de269131f9d57e74 ts=2026-10-14T16:30:26.5040000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7596] _id=6acfae23de269131f9d57e78 ts=2026-10-14T16:30:26.5470000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a8e69a8420a1e6b56b28.jsonl[6166] _id=6ac7cd3dde269131f9c4e06a ts=2026-10-08T17:05:00.1860000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6188] _id=6ace5dfade269131f9cf89b1 ts=2026-10-13T16:36:10.2230000Z; 72h 5m: 6ab9a8e69a8420a1e6b56b28.jsonl[503] _id=6ac3d765de269131f9ae55bf ts=2026-10-05T16:59:16.4170000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6152] _id=6ac7cd27de269131f9c4e02f ts=2026-10-08T17:04:37.9680000Z; 47h 37m: 6ab9a8e69a8420a1e6b56b28.jsonl[7590] _id=6acfae1bde269131f9d57dd8 ts=2026-10-14T16:30:18.8220000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[11289] _id=6ad24bcfde269131f9e59a07 ts=2026-10-16T16:07:43.3710000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 59 interval(s) ≤ 0.007s..0.021s shown 
  - Evidence: 7ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12110] _id=6ad250f3de269131f9e5df09 ts=2026-10-16T16:29:39.4300000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[12111] _id=6ad250f3de269131f9e5df0b ts=2026-10-16T16:29:39.4370000Z; 7ms: 6ab9a8e69a8420a1e6b56b28.jsonl[465] _id=6ac3d73bde269131f9ae5121 ts=2026-10-05T16:58:35.1050000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[468] _id=6ac3d73bde269131f9ae5127 ts=2026-10-05T16:58:35.1120000Z; 21ms: 6ab9a8e69a8420a1e6b56b28.jsonl[428] _id=6ac3d6fade269131f9ae4b3c ts=2026-10-05T16:57:29.1930000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[443] _id=6ac3d6fade269131f9ae4b44 ts=2026-10-05T16:57:29.2140000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 32m 
  - Evidence: 215h 32m: 6ab9a8e69a8420a1e6b56b28.jsonl[426] _id=6ac3d6e8de269131f9ae49a5 ts=2026-10-05T16:57:12.0060000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7570] _id=6acfadf5de269131f9d57b7c ts=2026-10-14T16:29:40.5670000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 239h 49m 
  - Evidence: 239h 49m: 6ab9a8e69a8420a1e6b56b28.jsonl[1662] _id=6ac52818de269131f9b59fe9 ts=2026-10-06T16:55:51.7560000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[12514] _id=6ad25492de269131f9e61026 ts=2026-10-16T16:45:06.1640000Z; 15m 3s: 6ab9a8e69a8420a1e6b56b28.jsonl[12514] _id=6ad25492de269131f9e61026 ts=2026-10-16T16:45:06.1640000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[13152] _id=6ad2581ade269131f9e652ac ts=2026-10-16T17:00:10.0260000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 120h 6m 
  - Evidence: 120h 6m: 6ab9a8e69a8420a1e6b56b28.jsonl[4878] _id=6ac7c4e7de269131f9c429da ts=2026-10-08T16:29:26.5190000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6173] _id=6ace5dd9de269131f9cf86e9 ts=2026-10-13T16:35:37.7170000Z; 24h 2m: 6ab9a8e69a8420a1e6b56b28.jsonl[7107] _id=6acfab50de269131f9d54bba ts=2026-10-14T16:18:23.0460000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[8810] _id=6ad0fd59de269131f9dd5f18 ts=2026-10-15T16:20:40.9920000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b28.jsonl[2632] _id=6ac6741bde269131f9bc8c03 ts=2026-10-07T16:32:26.5670000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4863] _id=6ac7c4b4de269131f9c4265c ts=2026-10-08T16:28:35.6200000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 34m 
  - Evidence: 119h 34m: 6ab9a8e69a8420a1e6b56b28.jsonl[6038] _id=6ac7cc3cde269131f9c4d366 ts=2026-10-08T17:00:43.5260000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6172] _id=6ace5dd9de269131f9cf86e8 ts=2026-10-13T16:35:37.7170000Z; 24h 2m: 6ab9a8e69a8420a1e6b56b28.jsonl[7106] _id=6acfab50de269131f9d54bb9 ts=2026-10-14T16:18:23.0460000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[8809] _id=6ad0fd59de269131f9dd5f17 ts=2026-10-15T16:20:40.9920000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b28.jsonl[2631] _id=6ac6741bde269131f9bc8c02 ts=2026-10-07T16:32:26.5670000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4862] _id=6ac7c4b4de269131f9c4265b ts=2026-10-08T16:28:35.6200000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6ab9a8e69a8420a1e6b56b28.jsonl[6170] _id=6ace5dd9de269131f9cf86e0 ts=2026-10-08T17:05:03.731Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[7104] _id=6acfab4fde269131f9d54bb4 ts=2026-10-13T17:05:02.716Z; 47h 17m: 6ab9a8e69a8420a1e6b56b28.jsonl[7104] _id=6acfab4fde269131f9d54bb4 ts=2026-10-13T17:05:02.716Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[8840] _id=6ad0fdb2de269131f9dd66ed ts=2026-10-15T16:22:09.4800000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b28.jsonl[641] _id=6ac52557de269131f9b532e7 ts=2026-10-05T17:05:02.034Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[2629] _id=6ac6741bde269131f9bc8bff ts=2026-10-06T17:05:11.093Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b28.jsonl[4860] _id=6ac67ba2de269131f9bd9066 ts=2026-10-07T17:04:33.8720000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4864] _id=6ac7c4b4de269131f9c42658 ts=2026-10-07T17:04:33.872Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a8e69a8420a1e6b56b28.jsonl[5621] _id=6ac7c819de269131f9c487a1 ts=2026-10-08T16:43:03.8980000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[6180] _id=6ace5de8de269131f9cf885f ts=2026-10-13T16:35:50.8620000Z; 23h 43m: 6ab9a8e69a8420a1e6b56b28.jsonl[583] _id=6ac3d7f3de269131f9ae6499 ts=2026-10-05T17:01:38.8840000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[672] _id=6ac525b2de269131f9b53e2b ts=2026-10-06T16:45:37.8890000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b28.jsonl[4366] _id=6ac67804de269131f9bd3377 ts=2026-10-07T16:49:08.7050000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[4870] _id=6ac7c4c7de269131f9c4280a ts=2026-10-08T16:28:52.4480000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 6ab9a8e69a8420a1e6b56b28.jsonl[387] _id=6ac3d68ede269131f9ae409d ts=2026-10-05T16:55:41.3330000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[397] _id=6ac3d68ede269131f9ae40a5 ts=2026-10-05T16:55:41.3360000Z; 6ms: 6ab9a8e69a8420a1e6b56b28.jsonl[10252] _id=6ad104a2de269131f9ddf825 ts=2026-10-15T16:51:45.7290000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[10253] _id=6ad104a2de269131f9ddf829 ts=2026-10-15T16:51:45.7350000Z; 6ms: 6ab9a8e69a8420a1e6b56b28.jsonl[12882] _id=6ad255eede269131f9e62977 ts=2026-10-16T16:50:53.2790000Z -> 6ab9a8e69a8420a1e6b56b28.jsonl[12883] _id=6ad255eede269131f9e6297f ts=2026-10-16T16:50:53.2850000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[372] _id=6ac3d655de269131f9ae3ae9 ts=2026-10-05T16:54:44.7370000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[514] _id=6ac3d77ede269131f9ae5892 ts=2026-10-05T16:59:41.1780000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[5473] _id=6ac7c723de269131f9c46e25 ts=2026-10-08T16:38:58.7210000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 23 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[942] _id=6ac526efde269131f9b56b73 ts=2026-10-06T16:50:53.3550000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[994] _id=6ac526fbde269131f9b56d23 ts=2026-10-06T16:51:05.1390000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[1082] _id=6ac52716de269131f9b57133 ts=2026-10-06T16:51:32.9940000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 116 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[805] _id=6ac526b8de269131f9b56509 ts=2026-10-06T16:49:57.7740000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[764] _id=6ac526b9de269131f9b56517 ts=2026-10-06T16:49:57.8770000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[794] _id=6ac526bbde269131f9b5655a ts=2026-10-06T16:49:58.9350000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[7596] _id=6acfae23de269131f9d57e78 ts=2026-10-14T16:30:26.5470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[443] _id=6ac3d6fade269131f9ae4b44 ts=2026-10-05T16:57:29.2140000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[448] _id=6ac3d6fbde269131f9ae4b6f ts=2026-10-05T16:57:30.2950000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[12514] _id=6ad25492de269131f9e61026 ts=2026-10-16T16:45:06.1640000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[13152] _id=6ad2581ade269131f9e652ac ts=2026-10-16T17:00:10.0260000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 312 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[872] _id=6ac526cdde269131f9b56755 ts=2026-10-06T16:50:19.8140000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[873] _id=6ac526cdde269131f9b56757 ts=2026-10-06T16:50:20.5540000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[1048] _id=6ac5270bde269131f9b56fcd ts=2026-10-06T16:51:23.3280000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 858 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[792] _id=6ac526b6de269131f9b564b3 ts=2026-10-06T16:49:57.3180000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[780] _id=6ac526b7de269131f9b564e7 ts=2026-10-06T16:49:57.5660000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[793] _id=6ac526b7de269131f9b564ee ts=2026-10-06T16:49:57.5660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[6184] _id=6ace5df4de269131f9cf894d ts=2026-10-13T16:36:04.6800000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[11618] _id=6ad24f11de269131f9e5bf89 ts=2026-10-16T16:21:37.4700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 404 start, 393 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 32 unmatched 'BecameCameraCentered' (totals: 801 open, 792 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 69 unmatched 'BecameVisible' (totals: 1440 open, 1487 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 44 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 349 of 13231 adjacent _id pairs reverse in client time; worst 130.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b28.jsonl[832] _id=6ac526c0de269131f9b565f6 ts=2026-10-06T16:50:08.0570000Z`; `6ab9a8e69a8420a1e6b56b28.jsonl[813] _id=6ac526c1de269131f9b5660f ts=2026-10-06T16:47:57.4160000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.95s, min -430233.99s, max -0.11s over 13232 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b28\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 4520 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3166); Unit 4 Dev (918); Unit 5 Dev - Dungeon (250); Unit 3 Dungeon Dev (186)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.50s, n=4519)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4520/4520 records)
    "BecameInvisible"  x1487
    "BecameVisible"  x1440
    "BecameCameraCentered"  x801
    "BecameCameraUncentered"  x792
data.pieceId  (string, 4520/4520 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4520/4520 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3463 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1120); Unit 3 Dev (903); Unit 4 Dev - Dungeon (393); Unit 4 Dev (329); Unit 3 Dungeon Dev (279); Unit 5 Dev - Dungeon (160); Unit 4 Dev - Anderson Base (131); Unit 1 Dev (119); Unit 5 Dev (29)
- **Intervals:** median 1.04s (p5 0.08s / p95 16.25s, n=3462)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3463/3463 records)
    "pressed"  x3463
data.actionType  (string, 3463/3463 records)
    "Move"  x2077
    "Jump"  x661
    "Interact"  x511
    "Hoverboard"  x88
    "Ascend"  x55
    "Descend"  x31
    "Sprint"  x19
    "Pause"  x12
    "Map"  x9
data.key  (string, 3463/3463 records, 3 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3463/3463 records)
    "Player"  x2653
    "Drone"  x810
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2071 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (626); Unit 3 Dev (410); Unit 4 Dev (265); Unit 4 Dev - Anderson Base (247); Unit 1 Dev (199); Unit 3 Dungeon Dev (120); Unit 4 Dev - Dungeon (102); Unit 5 Dev - Dungeon (69); Unit 5 Dev (33)
- **eventKey:** present on 1274 of 2071 records
- **Intervals:** median 4.12s (p5 0.00s / p95 31.40s, n=2070)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1274; [conversationId, dialogueEventType] x797
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2071/2071 records)
    numeric range 8 .. 116 (51 unique)
data.dialogueEventType  (string, 2071/2071 records)
    "DialogueNodeEvent"  x1274
    "DialogueStartEvent"  x404
    "DialogueFinishEvent"  x393
data.nodeId  (number, 1274/2071 records)
    numeric range 0 .. 290 (233 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1766 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (574); Unit 3 Dev (340); Unit 4 Dev (202); Unit 1 Dev (178); Unit 4 Dev - Anderson Base (139); Unit 4 Dev - Dungeon (113); Unit 3 Dungeon Dev (100); Unit 5 Dev - Dungeon (90); Unit 5 Dev (30)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.17s, n=1754)
- **Fields under `data`:**

```text
data.position  (object, 1766/1766 records)
data.position.x  (number, 1766/1766 records)
    numeric range -704.035 .. 1555.4 (628 unique)
data.position.y  (number, 1766/1766 records)
    numeric range -115.666 .. 219.838 (452 unique)
data.position.z  (number, 1766/1766 records)
    numeric range -1169.41 .. 2021.87 (627 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 671 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (444); Unit 2 Prod (Refactor) (124); Unit 1 Dev (60); Unit 3 Dev (43)
- **Intervals:** median 0.54s (p5 0.03s / p95 9.74s, n=670)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 671/671 records)
    "argumentationNodeHoverEnd"  x281
    "argumentationNodeHoverStart"  x279
    "argumentationNodeAdd"  x65
    "argumentationNodeRemove"  x46
data.argumentationTitle  (string, 671/671 records)
    "Unit 4 - Flooding"  x444
    "Unit 2 – Watershed"  x124
    "Unit 3 - Pollution Upstream"  x43
    "Unit 1 - Freshwater"  x39
    "Unit 1 - Argumentation Tutorial"  x21
data.nodeName  (string, 671/671 records)
    "A"  x111
    "B"  x100
    "C"  x91
    "D"  x80
    "I"  x71
    "II"  x67
    "1"  x60
    "2"  x34
    "4"  x30
    "3"  x24
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 286 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (90); Unit 4 Dev - Dungeon (80); Unit 3 Dungeon Dev (34); Unit 4 Dev (23); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (15); Unit 3 Dev (12); Unit 1 Dev (10); Unit 5 Dev (4)
- **Intervals:** median 11.77s (p5 0.77s / p95 416.40s, n=285)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 286/286 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 286/286 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 74 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (40); Unit 2 Prod (Refactor) (24); Unit 3 Dev (10)
- **Intervals:** median 1.23s (p5 0.17s / p95 34027.70s, n=73)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x64; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/74 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/74 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 64/74 records)
    "RightDrag"  x35
    "LeftDrag"  x29
data.currentSoilType  (string, 64/74 records)
    "CLAYSAND"  x17
    "SAND"  x16
    "CLAY"  x11
    "SANDGRAVEL"  x8
    "CLAYROCK"  x7
    "BEDROCK"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 64/74 records)
    "false"  x46
    "true"  x18
data.waterLevelStatus  (string, 64/74 records)
    "TooHigh"  x31
    "Proper"  x24
    "TooLow"  x9
data.waterRetentionChange  (string, 64/74 records)
    "Decrease"  x23
    "Increase"  x23
    "NoChange"  x18
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 74 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 3 Dev (14); Unit 1 Dev (12); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2); Unit 5 Dev (1)
- **eventKey:** present on 74 of 74 records
- **Intervals:** median 200.07s (p5 0.01s / p95 84143.18s, n=73)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Fields under `data`:**

```text
data.questEventType  (string, 74/74 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x30
data.questID  (string, 74/74 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 74/74 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/74 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 59 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 3 Dev (25); Unit 1 Dev (2)
- **Intervals:** median 8.90s (p5 1.07s / p95 84781.50s, n=58)
- **`data` key-set variants:** [actionType, featureUsed] x44; [actionType, featureUsed, location] x15
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 59/59 records)
    "MapCloseEvent"  x22
    "MapOpenEvent"  x22
    "WaypointMoveEvent"  x10
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x1
data.featureUsed  (string, 59/59 records)
    "Map"  x44
    "Waypoint"  x15
data.location  (object, 15/59 records)
data.location.x  (number, 15/59 records)
    numeric range -320.817 .. 138.914 (14 unique)
data.location.y  (number, 15/59 records)
    numeric range -191.633 .. 109.094 (14 unique)
data.location.z  (number, 15/59 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 53 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (46); Unit 3 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 11.41s (p5 0.25s / p95 39024.46s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "submitAnswerEvent"  x53
data.answerSubmitted  (string, 53/53 records)
    24 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 53/53 records)
    "Unit 4 - Flooding"  x46
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 33 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (12); Unit 2 Prod (Refactor) (6); Unit 3 Dev (5); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 466.57s (p5 8.61s / p95 85900.29s, n=32)
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "DebugMenuStateChanged"  x33
data.isOpened  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 30 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (30)
- **Intervals:** median 11.19s (p5 0.66s / p95 68.07s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "On"  x21
    "Off"  x9
data.floor  (string, 30/30 records)
    "4"  x15
    "3"  x8
    "2"  x5
    "1"  x2
data.machineNumber  (string, 30/30 records)
    "One"  x29
    "Two"  x1
data.machineType  (string, 30/30 records)
    "Condenser"  x15
    "Evaporator"  x12
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 30/30 records)
    "3"  x14
    "2"  x8
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 22 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (22)
- **Intervals:** median 6.74s (p5 0.29s / p95 73.16s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "ChangeCanister"  x22
data.canisterType  (string, 22/22 records)
    "Gravel"  x8
    "Clay"  x7
    "Sand"  x4
    "Bedrock"  x3
data.floor  (string, 22/22 records)
    "5"  x11
    "3"  x7
    "4"  x4
data.machine  (string, 22/22 records)
    "1"  x17
    "2"  x5
data.row  (string, 22/22 records)
    "TopRow"  x21
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 21 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (4); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 1506.84s (p5 6.73s / p95 103735.76s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 20 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 2.75s (p5 0.36s / p95 137793.36s, n=19)
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "Close"  x10
    "Open"  x10
data.toolName  (string, 20/20 records, 20 empty-string)
    ""  x20
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 1.77s (p5 0.88s / p95 24.17s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records, 10 empty-string)
    ""  x10
    "cameraPlaced"  x5
data.boxId  (string, 15/15 records)
    "0"  x8
    "1"  x5
    "2"  x2
data.soilType  (string, 15/15 records)
    "Sand"  x8
    "Gravel"  x4
    "Clay"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 42997.18s (p5 249.48s / p95 207579.58s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3)
- **Intervals:** median 180.57s (p5 0.04s / p95 327828.08s, n=13)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 14/14 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 4 - Flooding"  x4
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (2); Unit 4 Dev (1)
- **Intervals:** median 1529.38s (p5 0.85s / p95 288024.26s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 172119.45s (p5 95616.23s / p95 638286.00s, n=3)
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

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 3.48s (p5 2.41s / p95 698354.05s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 903.86s (p5 96.84s / p95 777109.35s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x3
    "Open"  x1
data.chatID  (string, 4/4 records)
    "NA"  x3
    "[18-179, 68-1, 68-2, 68-3, 68-5]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (24 records)
- `TerasGardenBox` data.actionType: "" (10x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (10x); "WaypointResetEvent" (1x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (46x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*