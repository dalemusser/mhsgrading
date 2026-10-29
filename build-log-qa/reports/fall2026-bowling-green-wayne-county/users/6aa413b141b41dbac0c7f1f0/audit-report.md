# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f0

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f0
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f0.jsonl
- **Records:** 16825 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f0
- **Time span:** 2026-09-22T12:58:42.971000+00:00 .. 2026-10-07T15:16:08.794000+00:00 (362h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f0\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 16825 records, 10 scenes.
- Findings: **0 FAIL**, **39 WARNING**, 100 INFO, 0 NOT_TESTED, 92 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5702 | 33.89 | 1 | 4 | 0 | 2026-09-24T13:10:19.397000+00:00 | 2026-10-07T15:09:31.583000+00:00 | 313h 59m |
| InputEvent | 4964 | 29.5 | 1 | 8 | 0 | 2026-09-22T12:59:15.921000+00:00 | 2026-10-07T15:16:00.398000+00:00 | 362h 16m |
| PlayerPositionEvent | 2281 | 13.56 | 1 | 8 | 0 | 2026-09-22T12:58:55.406000+00:00 | 2026-10-07T15:16:02.505000+00:00 | 362h 17m |
| DialogueEvent | 2233 | 13.27 | 1 | 8 | 1360 | 2026-09-22T12:59:18.093000+00:00 | 2026-10-07T15:15:57.479000+00:00 | 362h 16m |
| argumentationNodeEvent | 746 | 4.43 | 1 | 3 | 0 | 2026-09-23T13:39:52.385000+00:00 | 2026-10-07T13:34:53.451000+00:00 | 335h 55m |
| ObjectInterEvent | 387 | 2.3 | 1 | 8 | 0 | 2026-09-23T13:12:47.823000+00:00 | 2026-10-07T15:14:48.316000+00:00 | 338h 2m |
| Soil Key Puzzle | 104 | 0.62 | 1 | 3 | 0 | 2026-09-24T13:27:37.227000+00:00 | 2026-10-06T13:23:11.167000+00:00 | 287h 55m |
| questEvent | 81 | 0.48 | 1 | 8 | 81 | 2026-09-22T12:59:18.081000+00:00 | 2026-10-07T15:14:55.050000+00:00 | 362h 15m |
| argumentationAnswerEvent | 58 | 0.34 | 1 | 3 | 0 | 2026-09-24T12:58:25.290000+00:00 | 2026-10-07T13:34:56.453000+00:00 | 312h 36m |
| TopographicMapEvent | 55 | 0.33 | 1 | 2 | 0 | 2026-09-24T13:11:14.257000+00:00 | 2026-10-05T13:32:36.419000+00:00 | 264h 21m |
| gameWindowFocusEvent | 45 | 0.27 | 1 | 8 | 0 | 2026-09-22T12:58:42.971000+00:00 | 2026-10-07T15:04:46.690000+00:00 | 362h 6m |
| gameWindowUnfocusEvent | 36 | 0.21 | 1 | 10 | 0 | 2026-09-23T13:40:19.256000+00:00 | 2026-10-07T15:16:08.794000+00:00 | 337h 35m |
| DEBUGMenu | 26 | 0.15 | 1 | 9 | 0 | 2026-09-22T12:58:55.400000+00:00 | 2026-10-07T15:04:51.548000+00:00 | 362h 5m |
| WaterChamberEvent | 25 | 0.15 | 1 | 1 | 0 | 2026-10-07T15:08:38.332000+00:00 | 2026-10-07T15:15:28.096000+00:00 | 6m 49s |
| gameStartEvent | 17 | 0.1 | 1 | 1 | 0 | 2026-09-22T12:58:42.972000+00:00 | 2026-10-07T15:04:46.690000+00:00 | 362h 6m |
| TerasGardenBox | 14 | 0.08 | 1 | 1 | 0 | 2026-10-07T13:39:25.166000+00:00 | 2026-10-07T14:57:14.721000+00:00 | 1h 17m |
| argumentationEvent | 11 | 0.07 | 1 | 3 | 0 | 2026-09-24T12:57:39.865000+00:00 | 2026-10-07T13:34:56.493000+00:00 | 312h 37m |
| DaniEvent | 10 | 0.06 | 1 | 2 | 0 | 2026-09-24T13:16:25.992000+00:00 | 2026-10-05T13:14:46.067000+00:00 | 263h 58m |
| soilMachine | 10 | 0.06 | 1 | 1 | 0 | 2026-10-06T13:37:25.520000+00:00 | 2026-10-06T14:54:19.280000+00:00 | 1h 16m |
| argumentationToolEvent | 9 | 0.05 | 1 | 1 | 0 | 2026-09-24T12:57:38.949000+00:00 | 2026-09-24T13:00:53.435000+00:00 | 3m 14s |
| crash | 7 | 0.04 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-24T13:04:54.404000+00:00 | 2026-10-07T15:04:30.610000+00:00 | 313h 59m |
| chatEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-10-07T15:04:51.440000+00:00 | 2026-10-07T15:04:51.440000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1977.372s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 565188.103s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.832s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 12.824s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 7.259s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 10.044s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 144.163s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.181s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 80982.327s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 539.568s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 290.106s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 10 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 11.6x vs baseline. 
  - Observed: 58 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,I; A,2,II; A,3,I; A,4,I; B,1,I; B,2,I; B,2,II; B,3,I; B,3,II; C,2,II; C,3,II; C,D,2,II; C,D,A,2,II; D,1,II; D,2,II; D,3,II; D,4,II; D,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.3x vs baseline. 
  - Observed: 746 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 39 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[420] _id=6ab3d341485cab4c954c0a28 ts=2026-09-23T13:25:21.3670000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[472] _id=6ab3d427485cab4c954c3fbd ts=2026-09-23T13:29:11.0970000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[541] _id=6ab3d53a485cab4c954c7941 ts=2026-09-23T13:33:46.3790000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[7270] _id=6abd1f16485cab4c958b4f49 ts=2026-09-30T14:39:19.9820000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1] _id=6ab27b83485cab4c95479cee ts=2026-09-22T12:58:42.9720000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[28] _id=6ab3ce16485cab4c954b846a ts=2026-09-23T13:03:18.7450000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[681] _id=6ab51d93485cab4c954fc265 ts=2026-09-24T12:54:43.4180000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 45 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 45} 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[0] _id=6ab27b83485cab4c95479cec ts=2026-09-22T12:58:42.9710000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[27] _id=6ab3ce16485cab4c954b8468 ts=2026-09-23T13:03:18.7440000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[677] _id=6ab3d6c4485cab4c954cae11 ts=2026-09-23T13:40:20.3480000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 36 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 36} 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[676] _id=6ab3d6c3485cab4c954cadf5 ts=2026-09-23T13:40:19.2560000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[678] _id=6ab3d6c4485cab4c954cae1d ts=2026-09-23T13:40:20.9010000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[732] _id=6ab51ded485cab4c954fcd81 ts=2026-09-24T12:56:13.6180000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5701 | 0.0 | 0.026 | 198.273 | 0.963 | 345054.654 | 0.3 | 3651 | 10 |
| InputEvent | 4963 | 0.0 | 0.815 | 262.786 | 13.684 | 344722.178 | 0.23 | 167 | 13 |
| PlayerPositionEvent | 2270 | 9.9 | 9.999 | 574.429 | 10.02 | 344211.23 | 0.1 | 0 | 12 |
| DialogueEvent | 2232 | 0.0 | 3.603 | 584.319 | 37.838 | 344300.517 | 0.1 | 646 | 12 |
| argumentationNodeEvent | 745 | 0.015 | 0.322 | 1623.223 | 4.901 | 606113.181 | 0.04 | 185 | 4 |
| ObjectInterEvent | 386 | 0.0 | 7.224 | 3152.644 | 379.828 | 344926.027 | 0.02 | 5 | 13 |
| Soil Key Puzzle | 103 | 0.024 | 0.823 | 10063.436 | 10.416 | 518456.397 | 0.01 | 1 | 3 |
| questEvent | 80 | 0.0 | 231.825 | 16301.712 | 84932.553 | 344713.648 | 0.0 | 14 | 18 |
| argumentationAnswerEvent | 57 | 0.168 | 10.044 | 19743.705 | 16223.276 | 606152.701 | 0.0 | 0 | 3 |
| TopographicMapEvent | 54 | 0.01 | 12.824 | 17623.744 | 85343.077 | 346611.258 | 0.0 | 3 | 7 |
| gameWindowFocusEvent | 44 | 1.165 | 539.568 | 29626.448 | 86612.958 | 345711.481 | 0.0 | 0 | 19 |
| gameWindowUnfocusEvent | 35 | 1.645 | 290.106 | 34724.273 | 165163.857 | 345533.785 | 0.0 | 0 | 17 |
| DEBUGMenu | 25 | 4.937 | 1977.372 | 52142.246 | 292378.539 | 345207.541 | 0.0 | 0 | 18 |
| WaterChamberEvent | 24 | 0.323 | 7.259 | 17.073 | 53.922 | 73.77 | 3.51 | 0 | 0 |
| gameStartEvent | 16 | 234.246 | 80982.327 | 81472.732 | 345297.952 | 345711.481 | 0.0 | 0 | 15 |
| TerasGardenBox | 13 | 0.235 | 1.832 | 359.197 | 1857.555 | 4610.221 | 0.17 | 0 | 1 |
| argumentationEvent | 10 | 0.023 | 144.163 | 112543.663 | 530400.074 | 606094.201 | 0.0 | 2 | 3 |
| DaniEvent | 9 | 0.005 | 2.003 | 105588.897 | 483647.716 | 517654.862 | 0.0 | 2 | 2 |
| soilMachine | 9 | 0.641 | 38.861 | 512.64 | 2506.181 | 4041.004 | 0.12 | 0 | 1 |
| argumentationToolEvent | 8 | 0.083 | 1.181 | 24.311 | 122.631 | 187.757 | 2.47 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 2 | 92972.525 | 565188.103 | 565188.103 | 990182.123 | 1037403.681 | 0.0 | 0 | 2 |
| chatEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[10169] _id=6abe61d8485cab4c95a62b61 ts=2026-10-01T13:36:24.0460000Z == 6aa413b141b41dbac0c7f1f0.jsonl[10665] _id=6abe61d8485cab4c95a62b6d ts=2026-10-01T13:36:24.0460000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[12044] _id=6ac3a66ede269131f9a92cb5 ts=2026-10-05T13:30:22.6560000Z == 6aa413b141b41dbac0c7f1f0.jsonl[12045] _id=6ac3a66fde269131f9a92cbb ts=2026-10-05T13:30:22.6560000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 213 group(s), 281 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1127] _id=6ab52151485cab4c95502359 ts=2026-09-24T13:10:40.7900000Z == 6aa413b141b41dbac0c7f1f0.jsonl[1130] _id=6ab52151485cab4c9550235d ts=2026-09-24T13:10:40.7900000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1131] _id=6ab52152485cab4c9550237f ts=2026-09-24T13:10:40.8160000Z == 6aa413b141b41dbac0c7f1f0.jsonl[1123] _id=6ab52152485cab4c95502385 ts=2026-09-24T13:10:40.8160000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1138] _id=6ab52153485cab4c9550238c ts=2026-09-24T13:10:40.8320000Z == 6aa413b141b41dbac0c7f1f0.jsonl[1124] _id=6ab52153485cab4c9550238f ts=2026-09-24T13:10:40.8320000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[976] _id=6ab52056485cab4c955017c3 ts=? == 6aa413b141b41dbac0c7f1f0.jsonl[4174] _id=6abbb809485cab4c957c23ec ts=?`; `6aa413b141b41dbac0c7f1f0.jsonl[3329] _id=6ab67390485cab4c95548bab ts=? == 6aa413b141b41dbac0c7f1f0.jsonl[8836] _id=6abe58b0485cab4c95a40498 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `300ms: 6aa413b141b41dbac0c7f1f0.jsonl[121] _id=6ab3d05b485cab4c954b960e ts=2026-09-23T13:12:59.9030000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[125] _id=6ab3d05c485cab4c954b9625 ts=2026-09-23T13:13:00.2030000Z`; `284ms: 6aa413b141b41dbac0c7f1f0.jsonl[125] _id=6ab3d05c485cab4c954b9625 ts=2026-09-23T13:13:00.2030000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[126] _id=6ab3d05c485cab4c954b962e ts=2026-09-23T13:13:00.4870000Z`; `300ms: 6aa413b141b41dbac0c7f1f0.jsonl[128] _id=6ab3d063485cab4c954b96e0 ts=2026-09-23T13:13:07.8850000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[127] _id=6ab3d064485cab4c954b96e8 ts=2026-09-23T13:13:08.1850000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 816 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `77ms: 6aa413b141b41dbac0c7f1f0.jsonl[1302] _id=6ab521ac485cab4c95502ae7 ts=2026-09-24T13:10:50.6690000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[1303] _id=6ab521ac485cab4c95502ae9 ts=2026-09-24T13:10:50.7460000Z`; `7ms: 6aa413b141b41dbac0c7f1f0.jsonl[1326] _id=6ab521ad485cab4c95502b3f ts=2026-09-24T13:11:03.1100000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[1327] _id=6ab521ad485cab4c95502b41 ts=2026-09-24T13:11:03.1170000Z`; `22ms: 6aa413b141b41dbac0c7f1f0.jsonl[1339] _id=6ab521ae485cab4c95502b57 ts=2026-09-24T13:11:03.3850000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[1333] _id=6ab521ae485cab4c95502b59 ts=2026-09-24T13:11:03.4070000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `235ms: 6aa413b141b41dbac0c7f1f0.jsonl[15923] _id=6ac64b8fde269131f9b9bb51 ts=2026-10-07T13:39:26.9980000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[15920] _id=6ac64b8fde269131f9b9bb5f ts=2026-10-07T13:39:27.2330000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa413b141b41dbac0c7f1f0.jsonl[5206] _id=6abbbd64485cab4c957d204c ts=2026-09-29T13:30:12.2500000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[5207] _id=6abbbd64485cab4c957d204e ts=2026-09-29T13:30:12.2720000Z`; `10ms: 6aa413b141b41dbac0c7f1f0.jsonl[5207] _id=6abbbd64485cab4c957d204e ts=2026-09-29T13:30:12.2720000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[5204] _id=6abbbd64485cab4c957d2064 ts=2026-09-29T13:30:12.2820000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `699ms: 6aa413b141b41dbac0c7f1f0.jsonl[10071] _id=6abe5fae485cab4c95a58a87 ts=2026-10-01T13:27:10.4810000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[10065] _id=6abe5faf485cab4c95a58ab3 ts=2026-10-01T13:27:11.1800000Z`; `900ms: 6aa413b141b41dbac0c7f1f0.jsonl[15071] _id=6ac50edede269131f9b43a61 ts=2026-10-06T15:08:14.5570000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[15072] _id=6ac50edfde269131f9b43a76 ts=2026-10-06T15:08:15.4570000Z`; `619ms: 6aa413b141b41dbac0c7f1f0.jsonl[15142] _id=6ac50f0fde269131f9b43fb7 ts=2026-10-06T15:09:03.3000000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[15137] _id=6ac50f0fde269131f9b43fce ts=2026-10-06T15:09:03.9190000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6aa413b141b41dbac0c7f1f0.jsonl[10163] _id=6abe6016485cab4c95a5a881 ts=2026-10-01T13:28:54.3110000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[10164] _id=6abe6016485cab4c95a5a897 ts=2026-10-01T13:28:54.3380000Z`; `23ms: 6aa413b141b41dbac0c7f1f0.jsonl[15798] _id=6ac64a80de269131f9b984de ts=2026-10-07T13:34:56.4700000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[15801] _id=6ac64a80de269131f9b984e1 ts=2026-10-07T13:34:56.4930000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 128 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `366ms: 6aa413b141b41dbac0c7f1f0.jsonl[748] _id=6ab51e36485cab4c954fd76d ts=2026-09-24T12:57:26.2000000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[750] _id=6ab51e36485cab4c954fd779 ts=2026-09-24T12:57:26.5660000Z`; `402ms: 6aa413b141b41dbac0c7f1f0.jsonl[749] _id=6ab51e36485cab4c954fd771 ts=2026-09-24T12:57:26.3130000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[751] _id=6ab51e36485cab4c954fd782 ts=2026-09-24T12:57:26.7150000Z`; `379ms: 6aa413b141b41dbac0c7f1f0.jsonl[807] _id=6ab51ef5485cab4c954ff289 ts=2026-09-24T13:00:37.8740000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[809] _id=6ab51ef6485cab4c954ff295 ts=2026-09-24T13:00:38.2530000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `883ms: 6aa413b141b41dbac0c7f1f0.jsonl[818] _id=6ab51f02485cab4c954ff439 ts=2026-09-24T13:00:50.8520000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[820] _id=6ab51f03485cab4c954ff46f ts=2026-09-24T13:00:51.7350000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa413b141b41dbac0c7f1f0.jsonl[7270] _id=6abd1f16485cab4c958b4f49 ts=2026-09-30T14:39:19.9820000Z ~ 6aa413b141b41dbac0c7f1f0.jsonl[7278] _id=6abd1f16485cab4c958b4f4b ts=2026-09-30T14:39:19.9850000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa413b141b41dbac0c7f1f0.jsonl[3328] _id=6ab6738a485cab4c95548b2b ts=2026-09-25T13:13:46.6390000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4171] _id=6abbb802485cab4c957c23ae ts=2026-09-29T13:07:14.1800000Z; 95h 28m: 6aa413b141b41dbac0c7f1f0.jsonl[10372] _id=6abe6158485cab4c95a6056d ts=2026-10-01T13:34:16.4150000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10824] _id=6ac3a013de269131f9a84876 ts=2026-10-05T13:03:15.1050000Z; 24h 8m: 6aa413b141b41dbac0c7f1f0.jsonl[2] _id=6ab27b8f485cab4c95479cf0 ts=2026-09-22T12:58:55.4000000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[31] _id=6ab3cf29485cab4c954b86f2 ts=2026-09-23T13:07:53.3340000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 47m 
  - Evidence: 143h 47m: 6aa413b141b41dbac0c7f1f0.jsonl[2687] _id=6ab522aa485cab4c955062fe ts=2026-09-24T13:16:26.8080000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[5531] _id=6abd08c1485cab4c95868abd ts=2026-09-30T13:04:01.6700000Z; 120h 10m: 6aa413b141b41dbac0c7f1f0.jsonl[5534] _id=6abd08c6485cab4c95868aed ts=2026-09-30T13:04:06.5700000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[11417] _id=6ac3a2c3de269131f9a879f2 ts=2026-10-05T13:14:43.5670000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6aa413b141b41dbac0c7f1f0.jsonl[5529] _id=6abd08c2485cab4c95868ac1 ts=2026-09-30T13:04:02.0370000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[5530] _id=6abd08c2485cab4c95868ac3 ts=2026-09-30T13:04:02.0420000Z; 7ms: 6aa413b141b41dbac0c7f1f0.jsonl[5532] _id=6abd08c4485cab4c95868ad1 ts=2026-09-30T13:04:04.0450000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[5533] _id=6abd08c4485cab4c95868ad3 ts=2026-09-30T13:04:04.0520000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa413b141b41dbac0c7f1f0.jsonl[4151] _id=6ab67730485cab4c955504d8 ts=2026-09-25T13:29:21.0370000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4188] _id=6abbb81d485cab4c957c24c8 ts=2026-09-29T13:07:41.5540000Z; 95h 23m: 6aa413b141b41dbac0c7f1f0.jsonl[10763] _id=6abe62b6485cab4c95a67221 ts=2026-10-01T13:40:06.3330000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10937] _id=6ac3a043de269131f9a84b7e ts=2026-10-05T13:04:03.1090000Z; 24h 7m: 6aa413b141b41dbac0c7f1f0.jsonl[9] _id=6ab27be9485cab4c95479d34 ts=2026-09-22T13:00:25.0400000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[34] _id=6ab3cf40485cab4c954b8760 ts=2026-09-23T13:08:16.0570000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 646 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[15610] _id=6ac64a0cde269131f9b9636c ts=2026-10-07T13:33:00.9200000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15611] _id=6ac64a0cde269131f9b9636d ts=2026-10-07T13:33:00.9200000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[15671] _id=6ac64a27de269131f9b96aea ts=2026-10-07T13:33:27.4260000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15672] _id=6ac64a27de269131f9b96aeb ts=2026-10-07T13:33:27.4260000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[15716] _id=6ac64a4ede269131f9b9746b ts=2026-10-07T13:34:06.6120000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15717] _id=6ac64a4ede269131f9b9746c ts=2026-10-07T13:34:06.6120000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 288h 10m 
  - Evidence: 288h 10m: 6aa413b141b41dbac0c7f1f0.jsonl[962] _id=6ab51ff6485cab4c95501187 ts=2026-09-24T13:04:54.4040000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12662] _id=6ac4f452de269131f9b031d4 ts=2026-10-06T13:14:58.0850000Z; 25h 49m: 6aa413b141b41dbac0c7f1f0.jsonl[12662] _id=6ac4f452de269131f9b031d4 ts=2026-10-06T13:14:58.0850000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[16174] _id=6ac65f7ede269131f9bb73f5 ts=2026-10-07T15:04:30.6100000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 45m 
  - Evidence: 95h 45m: 6aa413b141b41dbac0c7f1f0.jsonl[4080] _id=6ab67577485cab4c9554bdd0 ts=2026-09-25T13:21:59.7410000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4166] _id=6abbb809485cab4c957c23fe ts=2026-09-29T13:07:21.9190000Z; 95h 22m: 6aa413b141b41dbac0c7f1f0.jsonl[10802] _id=6abe62de485cab4c95a67a1b ts=2026-10-01T13:40:45.9950000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10819] _id=6ac3a017de269131f9a84896 ts=2026-10-05T13:03:17.7620000Z; 24h 12m: 6aa413b141b41dbac0c7f1f0.jsonl[11] _id=6ab27ba4485cab4c95479cfa ts=2026-09-22T12:59:16.9410000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[76] _id=6ab3d00a485cab4c954b8e4a ts=2026-09-23T13:11:39.0490000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 167 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[10169] _id=6abe61d8485cab4c95a62b61 ts=2026-10-01T13:36:24.0460000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10665] _id=6abe61d8485cab4c95a62b6d ts=2026-10-01T13:36:24.0460000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[12044] _id=6ac3a66ede269131f9a92cb5 ts=2026-10-05T13:30:22.6560000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12045] _id=6ac3a66fde269131f9a92cbb ts=2026-10-05T13:30:22.6560000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[15382] _id=6ac64895de269131f9b902c0 ts=2026-10-07T13:26:45.2150000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15383] _id=6ac64895de269131f9b902c1 ts=2026-10-07T13:26:45.2150000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 6aa413b141b41dbac0c7f1f0.jsonl[4044] _id=6ab6751c485cab4c9554b524 ts=2026-09-25T13:20:29.1040000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4219] _id=6abbb87b485cab4c957c2cc3 ts=2026-09-29T13:09:15.1310000Z; 95h 24m: 6aa413b141b41dbac0c7f1f0.jsonl[10753] _id=6abe62a6485cab4c95a66ea7 ts=2026-10-01T13:39:50.5880000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10884] _id=6ac3a039de269131f9a84aae ts=2026-10-05T13:03:53.8520000Z; 24h 15m: 6aa413b141b41dbac0c7f1f0.jsonl[4940] _id=6abbb972485cab4c957c4b80 ts=2026-09-29T13:13:22.3850000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[6132] _id=6abd0e84485cab4c9587e2aa ts=2026-09-30T13:28:36.6230000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[15419] _id=6ac64908de269131f9b91f51 ts=2026-10-07T13:28:39.9990000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15420] _id=6ac64908de269131f9b91f52 ts=2026-10-07T13:28:39.9990000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[15489] _id=6ac6495cde269131f9b93446 ts=2026-10-07T13:30:04.1080000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15490] _id=6ac6495cde269131f9b93447 ts=2026-10-07T13:30:04.1080000Z; 1ms: 6aa413b141b41dbac0c7f1f0.jsonl[14856] _id=6ac50e1cde269131f9b42972 ts=2026-10-06T15:04:59.9460000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[14910] _id=6ac50e1cde269131f9b42977 ts=2026-10-06T15:04:59.9470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 6aa413b141b41dbac0c7f1f0.jsonl[4160] _id=6ab6776e485cab4c95550d02 ts=2026-09-25T13:30:22.9560000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4172] _id=6abbb809485cab4c957c23ee ts=2026-09-29T13:07:14.1860000Z; 95h 21m: 6aa413b141b41dbac0c7f1f0.jsonl[10807] _id=6abe630a485cab4c95a68317 ts=2026-10-01T13:41:30.3200000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10830] _id=6ac3a017de269131f9a84894 ts=2026-10-05T13:03:15.1150000Z; 24h 7m: 6aa413b141b41dbac0c7f1f0.jsonl[25] _id=6ab27bf0485cab4c95479d3a ts=2026-09-22T13:00:32.0690000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[32] _id=6ab3cf2f485cab4c954b8710 ts=2026-09-23T13:07:53.3410000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 6aa413b141b41dbac0c7f1f0.jsonl[4026] _id=6ab674b4485cab4c9554abe5 ts=2026-09-25T13:18:42.8640000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4235] _id=6abbb892485cab4c957c2fe7 ts=2026-09-29T13:09:37.5180000Z; 95h 26m: 6aa413b141b41dbac0c7f1f0.jsonl[10657] _id=6abe61d2485cab4c95a62973 ts=2026-10-01T13:36:17.9440000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10820] _id=6ac3a018de269131f9a8489e ts=2026-10-05T13:03:17.7770000Z; 24h 18m: 6aa413b141b41dbac0c7f1f0.jsonl[11080] _id=6ac3a087de269131f9a850ba ts=2026-10-05T13:05:10.8290000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12916] _id=6ac4f641de269131f9b05e90 ts=2026-10-06T13:23:13.5470000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3651 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[10358] _id=6abe6171485cab4c95a60c1e ts=2026-10-01T13:34:41.6030000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10359] _id=6abe6171485cab4c95a60c22 ts=2026-10-01T13:34:41.6030000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[10367] _id=6abe6184485cab4c95a610a6 ts=2026-10-01T13:35:00.0920000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10449] _id=6abe6184485cab4c95a610b0 ts=2026-10-01T13:35:00.0920000Z; 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[10378] _id=6abe6159485cab4c95a605bd ts=2026-10-01T13:34:16.5250000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10379] _id=6abe615c485cab4c95a60699 ts=2026-10-01T13:34:16.5250000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6aa413b141b41dbac0c7f1f0.jsonl[3276] _id=6ab5254c485cab4c9550fcc3 ts=2026-09-24T13:27:40.2150000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[6131] _id=6abd0e84485cab4c9587e294 ts=2026-09-30T13:28:36.6120000Z; 119h 48m: 6aa413b141b41dbac0c7f1f0.jsonl[10331] _id=6abe6129485cab4c95a5fa2d ts=2026-10-01T13:33:29.3870000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12842] _id=6ac4f5eede269131f9b049fa ts=2026-10-06T13:21:50.4420000Z; 24h 3m: 6aa413b141b41dbac0c7f1f0.jsonl[6153] _id=6abd0ea2485cab4c9587f21f ts=2026-09-30T13:29:06.3320000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10303] _id=6abe60ff485cab4c95a5eef1 ts=2026-10-01T13:32:47.6180000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.024s..0.024s shown 
  - Evidence: 24ms: 6aa413b141b41dbac0c7f1f0.jsonl[12842] _id=6ac4f5eede269131f9b049fa ts=2026-10-06T13:21:50.4420000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12837] _id=6ac4f5eede269131f9b04a07 ts=2026-10-06T13:21:50.4660000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 16m 
  - Evidence: 1h 16m: 6aa413b141b41dbac0c7f1f0.jsonl[15930] _id=6ac64b97de269131f9b9bd3c ts=2026-10-07T13:39:35.9640000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15999] _id=6ac65d9ade269131f9bb407a ts=2026-10-07T14:56:26.1850000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6aa413b141b41dbac0c7f1f0.jsonl[9379] _id=6abe5ce7485cab4c95a4911d ts=2026-10-01T13:15:19.1470000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12097] _id=6ac3a6dade269131f9a94047 ts=2026-10-05T13:32:10.4050000Z; 95h 53m: 6aa413b141b41dbac0c7f1f0.jsonl[3428] _id=6ab6743b485cab4c95549953 ts=2026-09-25T13:16:43.4290000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4257] _id=6abbb8b2485cab4c957c362c ts=2026-09-29T13:10:10.2340000Z; 24h 5m: 6aa413b141b41dbac0c7f1f0.jsonl[1158] _id=6ab52180485cab4c955026b1 ts=2026-09-24T13:11:28.2750000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[3421] _id=6ab6742e485cab4c9554977d ts=2026-09-25T13:16:30.6100000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.010s..0.022s shown 
  - Evidence: 10ms: 6aa413b141b41dbac0c7f1f0.jsonl[5207] _id=6abbbd64485cab4c957d204e ts=2026-09-29T13:30:12.2720000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[5204] _id=6abbbd64485cab4c957d2064 ts=2026-09-29T13:30:12.2820000Z; 22ms: 6aa413b141b41dbac0c7f1f0.jsonl[5202] _id=6abbbd64485cab4c957d203c ts=2026-09-29T13:30:12.2280000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[5206] _id=6abbbd64485cab4c957d204c ts=2026-09-29T13:30:12.2500000Z; 22ms: 6aa413b141b41dbac0c7f1f0.jsonl[5206] _id=6abbbd64485cab4c957d204c ts=2026-09-29T13:30:12.2500000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[5207] _id=6abbbd64485cab4c957d204e ts=2026-09-29T13:30:12.2720000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 22m 
  - Evidence: 168h 22m: 6aa413b141b41dbac0c7f1f0.jsonl[866] _id=6ab51f34485cab4c954ffc2b ts=2026-09-24T13:01:40.6960000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[9911] _id=6abe5efd485cab4c95a54fb4 ts=2026-10-01T13:24:13.3970000Z; 121h 38m: 6aa413b141b41dbac0c7f1f0.jsonl[10156] _id=6abe6016485cab4c95a5a87d ts=2026-10-01T13:28:54.2870000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15042] _id=6ac50ec5de269131f9b4382e ts=2026-10-06T15:07:49.6450000Z; 22h 18m: 6aa413b141b41dbac0c7f1f0.jsonl[15363] _id=6ac5103bde269131f9b453ad ts=2026-10-06T15:14:03.3790000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15629] _id=6ac64a0ade269131f9b96298 ts=2026-10-07T13:32:58.1360000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 21m 
  - Evidence: 168h 21m: 6aa413b141b41dbac0c7f1f0.jsonl[864] _id=6ab51f34485cab4c954ffc2f ts=2026-09-24T13:01:40.7150000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[9861] _id=6abe5ec2485cab4c95a537d5 ts=2026-10-01T13:23:14.9160000Z; 121h 38m: 6aa413b141b41dbac0c7f1f0.jsonl[10164] _id=6abe6016485cab4c95a5a897 ts=2026-10-01T13:28:54.3380000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[14978] _id=6ac50e93de269131f9b43322 ts=2026-10-06T15:06:59.3680000Z; 22h 25m: 6aa413b141b41dbac0c7f1f0.jsonl[14978] _id=6ac50e93de269131f9b43322 ts=2026-10-06T15:06:59.3680000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15548] _id=6ac649d8de269131f9b9541a ts=2026-10-07T13:32:08.1130000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.027s shown 
  - Evidence: 23ms: 6aa413b141b41dbac0c7f1f0.jsonl[15798] _id=6ac64a80de269131f9b984de ts=2026-10-07T13:34:56.4700000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15801] _id=6ac64a80de269131f9b984e1 ts=2026-10-07T13:34:56.4930000Z; 27ms: 6aa413b141b41dbac0c7f1f0.jsonl[10163] _id=6abe6016485cab4c95a5a881 ts=2026-10-01T13:28:54.3110000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10164] _id=6abe6016485cab4c95a5a897 ts=2026-10-01T13:28:54.3380000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 21m 
  - Evidence: 168h 21m: 6aa413b141b41dbac0c7f1f0.jsonl[862] _id=6ab51f2c485cab4c954ffadd ts=2026-09-24T13:01:32.3130000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[9870] _id=6abe5ecd485cab4c95a53d51 ts=2026-10-01T13:23:25.4940000Z; 121h 37m: 6aa413b141b41dbac0c7f1f0.jsonl[10149] _id=6abe6012485cab4c95a5a779 ts=2026-10-01T13:28:50.5730000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[14970] _id=6ac50e89de269131f9b43272 ts=2026-10-06T15:06:49.2350000Z; 23h 17m: 6aa413b141b41dbac0c7f1f0.jsonl[671] _id=6ab3d6a8485cab4c954cab5f ts=2026-09-23T13:39:52.4890000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[748] _id=6ab51e36485cab4c954fd76d ts=2026-09-24T12:57:26.2000000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 185 interval(s) ≤ 0.015s..0.015s shown 
  - Evidence: 15ms: 6aa413b141b41dbac0c7f1f0.jsonl[15068] _id=6ac50edbde269131f9b43a19 ts=2026-10-06T15:08:11.4350000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15067] _id=6ac50edbde269131f9b43a1b ts=2026-10-06T15:08:11.4500000Z; 15ms: 6aa413b141b41dbac0c7f1f0.jsonl[15642] _id=6ac64a17de269131f9b9661e ts=2026-10-07T13:33:11.0130000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15643] _id=6ac64a17de269131f9b96625 ts=2026-10-07T13:33:11.0280000Z; 15ms: 6aa413b141b41dbac0c7f1f0.jsonl[15759] _id=6ac64a71de269131f9b9822f ts=2026-10-07T13:34:41.5080000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[15763] _id=6ac64a71de269131f9b98237 ts=2026-10-07T13:34:41.5230000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa413b141b41dbac0c7f1f0.jsonl[8861] _id=6abe5986485cab4c95a417d9 ts=2026-10-01T13:00:54.3510000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10818] _id=6ac39ff6de269131f9a84722 ts=2026-10-05T13:02:45.8320000Z; 95h 52m: 6aa413b141b41dbac0c7f1f0.jsonl[3325] _id=6ab67380485cab4c95548a2b ts=2026-09-25T13:13:36.7190000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4163] _id=6abbb7c9485cab4c957c21a7 ts=2026-09-29T13:06:16.8280000Z; 24h 7m: 6aa413b141b41dbac0c7f1f0.jsonl[969] _id=6ab5204a485cab4c95501757 ts=2026-09-24T13:06:17.8490000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[3325] _id=6ab67380485cab4c95548a2b ts=2026-09-25T13:13:36.7190000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa413b141b41dbac0c7f1f0.jsonl[8860] _id=6abe5986485cab4c95a417d5 ts=2026-10-01T13:00:54.3500000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10816] _id=6ac39ff5de269131f9a84713 ts=2026-10-05T13:02:45.8310000Z; 95h 35m: 6aa413b141b41dbac0c7f1f0.jsonl[4159] _id=6ab6776b485cab4c95550cd2 ts=2026-09-25T13:30:19.9370000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4162] _id=6abbb7c8485cab4c957c21a4 ts=2026-09-29T13:06:16.8270000Z; 24h 4m: 6aa413b141b41dbac0c7f1f0.jsonl[0] _id=6ab27b83485cab4c95479cec ts=2026-09-22T12:58:42.9710000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[27] _id=6ab3ce16485cab4c954b8468 ts=2026-09-23T13:03:18.7440000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 58m 
  - Evidence: 95h 58m: 6aa413b141b41dbac0c7f1f0.jsonl[10806] _id=6abe630d485cab4c95a683ab ts=2026-10-01T13:41:33.9510000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[12288] _id=6ac3a8cbde269131f9a99631 ts=2026-10-05T13:40:27.7360000Z; 95h 36m: 6aa413b141b41dbac0c7f1f0.jsonl[4161] _id=6ab6776f485cab4c95550d06 ts=2026-09-25T13:30:23.2480000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4165] _id=6abbb7fa485cab4c957c2382 ts=2026-09-29T13:07:06.1750000Z; 24h 33m: 6aa413b141b41dbac0c7f1f0.jsonl[4205] _id=6abbb84d485cab4c957c281e ts=2026-09-29T13:08:29.6290000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[7260] _id=6abd11be485cab4c95890298 ts=2026-09-30T13:42:22.4560000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 45m 
  - Evidence: 95h 45m: 6aa413b141b41dbac0c7f1f0.jsonl[4082] _id=6ab6757e485cab4c9554bee4 ts=2026-09-25T13:22:07.0460000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[4173] _id=6abbb809485cab4c957c23f4 ts=2026-09-29T13:07:20.6940000Z; 95h 28m: 6aa413b141b41dbac0c7f1f0.jsonl[10339] _id=6abe6171485cab4c95a60bfe ts=2026-10-01T13:34:41.1820000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[10826] _id=6ac3a017de269131f9a84898 ts=2026-10-05T13:03:19.3750000Z; 24h 8m: 6aa413b141b41dbac0c7f1f0.jsonl[12] _id=6ab27ba6485cab4c95479cfc ts=2026-09-22T12:59:18.0810000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[37] _id=6ab3cf3f485cab4c954b875e ts=2026-09-23T13:08:16.0370000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f0.jsonl[16616] _id=6ac660ccde269131f9bb8b69 ts=2026-10-07T15:10:04.7850000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[16617] _id=6ac660ccde269131f9bb8b6a ts=2026-10-07T15:10:04.7850000Z; 2ms: 6aa413b141b41dbac0c7f1f0.jsonl[657] _id=6ab3d68a485cab4c954ca7ff ts=2026-09-23T13:39:22.1410000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[658] _id=6ab3d68a485cab4c954ca803 ts=2026-09-23T13:39:22.1430000Z; 2ms: 6aa413b141b41dbac0c7f1f0.jsonl[727] _id=6ab51dc2485cab4c954fc831 ts=2026-09-24T12:55:29.8680000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[702] _id=6ab51dc2485cab4c954fc833 ts=2026-09-24T12:55:29.8700000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 7m 
  - Evidence: 1h 7m: 6aa413b141b41dbac0c7f1f0.jsonl[14099] _id=6ac4fa66de269131f9b119a4 ts=2026-10-06T13:40:54.6000000Z -> 6aa413b141b41dbac0c7f1f0.jsonl[14244] _id=6ac50a2fde269131f9b3eb1e ts=2026-10-06T14:48:15.6040000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[5208] _id=6abbbd64485cab4c957d2052 ts=2026-09-29T13:30:12.2750000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[5704] _id=6abd0a6c485cab4c9586a26d ts=2026-09-30T13:11:08.6690000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[7169] _id=6abd10c6485cab4c9588cd97 ts=2026-09-30T13:38:14.1000000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 189 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1503] _id=6ab521bb485cab4c95502da5 ts=2026-09-24T13:12:25.6050000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1504] _id=6ab521bb485cab4c95502da9 ts=2026-09-24T13:12:25.7110000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1176] _id=6ab521bc485cab4c95502ddf ts=2026-09-24T13:12:26.8700000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 395 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1133] _id=6ab52153485cab4c95502391 ts=2026-09-24T13:10:40.8320000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1288] _id=6ab521ac485cab4c95502ae5 ts=2026-09-24T13:10:50.5810000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1355] _id=6ab521af485cab4c95502b93 ts=2026-09-24T13:11:52.8190000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[10164] _id=6abe6016485cab4c95a5a897 ts=2026-10-01T13:28:54.3380000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[9868] _id=6abe5ecd485cab4c95a53d65 ts=2026-10-01T13:23:25.5920000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[9873] _id=6abe5ecd485cab4c95a53d75 ts=2026-10-01T13:23:25.6120000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[9890] _id=6abe5edb485cab4c95a54342 ts=2026-10-01T13:23:39.6780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[16199] _id=6ac65f93de269131f9bb761e ts=2026-10-07T15:04:51.4400000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[12182] _id=6ac3a80bde269131f9a9721d ts=2026-10-05T13:37:15.2760000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[14155] _id=6ac50993de269131f9b3ccf0 ts=2026-10-06T14:45:40.3640000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 7 records 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[4] _id=6ab27b95485cab4c95479cf2 ts=?`; `6aa413b141b41dbac0c7f1f0.jsonl[33] _id=6ab3cf2f485cab4c954b870e ts=?`; `6aa413b141b41dbac0c7f1f0.jsonl[976] _id=6ab52056485cab4c955017c3 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 620 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1509] _id=6ab521b8485cab4c95502d27 ts=2026-09-24T13:12:16.1210000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1209] _id=6ab521b9485cab4c95502d3b ts=2026-09-24T13:12:18.0380000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1533] _id=6ab521cf485cab4c95503027 ts=2026-09-24T13:12:46.1020000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1150 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1121] _id=6ab52151485cab4c95502349 ts=2026-09-24T13:10:40.7410000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1128] _id=6ab52151485cab4c95502351 ts=2026-09-24T13:10:40.7540000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1129] _id=6ab52151485cab4c95502355 ts=2026-09-24T13:10:40.7710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 17 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[5207] _id=6abbbd64485cab4c957d204e ts=2026-09-29T13:30:12.2720000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[5204] _id=6abbbd64485cab4c957d2064 ts=2026-09-29T13:30:12.2820000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[5244] _id=6abbbdde485cab4c957d4219 ts=2026-09-29T13:32:14.0670000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[15548] _id=6ac649d8de269131f9b9541a ts=2026-10-07T13:32:08.1130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 52 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[9928] _id=6abe5ef8485cab4c95a54cfa ts=2026-10-01T13:24:07.7110000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[9925] _id=6abe5efb485cab4c95a54e85 ts=2026-10-01T13:24:11.2900000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[9976] _id=6abe5f42485cab4c95a567d0 ts=2026-10-01T13:25:22.7750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[814] _id=6ab51f01485cab4c954ff40f ts=2026-09-24T13:00:49.1690000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[819] _id=6ab51f02485cab4c954ff43d ts=2026-09-24T13:00:50.9350000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[821] _id=6ab51f03485cab4c954ff47f ts=2026-09-24T13:00:51.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 441 start, 432 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 171 unmatched 'BecameCameraCentered' (totals: 913 open, 931 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 111 unmatched 'BecameVisible' (totals: 1787 open, 2071 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 23 open, 21 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 320 open, 331 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 48 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 517 of 16817 adjacent _id pairs reverse in client time; worst 106.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f0.jsonl[1218] _id=6ab521a6485cab4c955029a9 ts=2026-09-24T13:12:06.0680000Z`; `6aa413b141b41dbac0c7f1f0.jsonl[1199] _id=6ab521a7485cab4c955029c3 ts=2026-09-24T13:10:19.3970000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -108.44s, max +2.28s over 16818 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f0\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 7 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 5702 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (4300); Unit 4 Dev (652); Unit 3 Dungeon Dev (444); Unit 5 Dev - Dungeon (306)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.96s, n=5701)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5702/5702 records)
    "BecameInvisible"  x2071
    "BecameVisible"  x1787
    "BecameCameraUncentered"  x931
    "BecameCameraCentered"  x913
data.pieceId  (string, 5702/5702 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5702/5702 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4964 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1731); Unit 3 Dev (1023); Unit 3 Dungeon Dev (754); Unit 4 Dev - Dungeon (517); Unit 1 Dev (346); Unit 4 Dev (282); Unit 5 Dev - Dungeon (157); Unit 4 Dev - Anderson Base (154)
- **Intervals:** median 0.81s (p5 0.08s / p95 13.68s, n=4963)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4964/4964 records)
    "pressed"  x4964
data.actionType  (string, 4964/4964 records)
    "Move"  x3661
    "Interact"  x617
    "Jump"  x469
    "Sprint"  x75
    "Hoverboard"  x67
    "Ascend"  x47
    "Descend"  x17
    "SkipCinematic"  x6
    "Pause"  x3
    "Map"  x1
    "ToggleDebug"  x1
data.key  (string, 4964/4964 records, 11 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4964/4964 records)
    "Player"  x3898
    "Drone"  x1066
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2281 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (882); Unit 3 Dev (379); Unit 1 Dev (265); Unit 3 Dungeon Dev (205); Unit 4 Dev (200); Unit 4 Dev - Dungeon (153); Unit 4 Dev - Anderson Base (129); Unit 5 Dev - Dungeon (68)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.02s, n=2270)
- **Fields under `data`:**

```text
data.position  (object, 2281/2281 records)
data.position.x  (number, 2281/2281 records)
    numeric range -727.152 .. 1550.47 (867 unique)
data.position.y  (number, 2281/2281 records)
    numeric range -115.768 .. 222.005 (653 unique)
data.position.z  (number, 2281/2281 records)
    numeric range -1174.53 .. 2199.76 (867 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2233 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (737); Unit 3 Dev (399); Unit 4 Dev (273); Unit 1 Dev (223); Unit 4 Dev - Anderson Base (222); Unit 3 Dungeon Dev (171); Unit 4 Dev - Dungeon (147); Unit 5 Dev - Dungeon (61)
- **eventKey:** present on 1360 of 2233 records
- **Intervals:** median 3.60s (p5 0.00s / p95 37.84s, n=2232)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1360; [conversationId, dialogueEventType] x873
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2233/2233 records)
    numeric range 8 .. 114 (46 unique)
data.dialogueEventType  (string, 2233/2233 records)
    "DialogueNodeEvent"  x1360
    "DialogueStartEvent"  x441
    "DialogueFinishEvent"  x432
data.nodeId  (number, 1360/2233 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 746 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (466); Unit 3 Dev (231); Unit 1 Dev (49)
- **Intervals:** median 0.32s (p5 0.02s / p95 4.90s, n=745)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 746/746 records)
    "argumentationNodeHoverEnd"  x331
    "argumentationNodeHoverStart"  x320
    "argumentationNodeAdd"  x55
    "argumentationNodeRemove"  x40
data.argumentationTitle  (string, 746/746 records)
    "Unit 4 - Flooding"  x466
    "Unit 3 - Pollution Upstream"  x231
    "Unit 1 - Freshwater"  x43
    "Unit 1 - Argumentation Tutorial"  x6
data.nodeName  (string, 746/746 records)
    "B"  x107
    "A"  x105
    "2"  x93
    "3"  x74
    "1"  x72
    "C"  x69
    "D"  x67
    "II"  x54
    "I"  x49
    "4"  x47
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 387 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (98); Unit 3 Dungeon Dev (97); Unit 2 Prod (Refactor) (96); Unit 1 Dev (31); Unit 4 Dev (23); Unit 3 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (6)
- **Intervals:** median 7.22s (p5 0.32s / p95 379.83s, n=386)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 387/387 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 387/387 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 104 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (58); Unit 2 Prod (Refactor) (24); Unit 3 Dev (22)
- **Intervals:** median 0.82s (p5 0.17s / p95 10.42s, n=103)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x96; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/104 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/104 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 96/104 records)
    "RightDrag"  x51
    "LeftDrag"  x45
data.currentSoilType  (string, 96/104 records)
    "SAND"  x23
    "CLAYSAND"  x21
    "CLAY"  x18
    "SANDGRAVEL"  x17
    "CLAYROCK"  x10
    "GRAVEL"  x6
    "BEDROCK"  x1
data.isCorrectSelection  (string, 96/104 records)
    "false"  x72
    "true"  x24
data.waterLevelStatus  (string, 96/104 records)
    "Proper"  x62
    "TooHigh"  x20
    "TooLow"  x14
data.waterRetentionChange  (string, 96/104 records)
    "Decrease"  x44
    "Increase"  x28
    "NoChange"  x24
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (16); Unit 4 Dev - Dungeon (13); Unit 3 Dev (11); Unit 4 Dev (9); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 231.82s (p5 0.00s / p95 84932.55s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x48; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x48
    "questFinishEvent"  x33
data.questID  (string, 81/81 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/81 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 58 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (39); Unit 3 Dev (17); Unit 1 Dev (2)
- **Intervals:** median 10.04s (p5 0.41s / p95 16223.28s, n=57)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 58/58 records)
    "submitAnswerEvent"  x58
data.answerSubmitted  (string, 58/58 records, 1 empty-string)
    21 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 58/58 records)
    "Unit 4 - Flooding"  x39
    "Unit 3 - Pollution Upstream"  x17
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 55 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (49); Unit 3 Dev (6)
- **Intervals:** median 12.82s (p5 0.51s / p95 85343.08s, n=54)
- **`data` key-set variants:** [actionType, featureUsed] x44; [actionType, featureUsed, location] x11
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "MapOpenEvent"  x23
    "MapCloseEvent"  x21
    "WaypointMoveEvent"  x10
    "WaypointSetEvent"  x1
data.featureUsed  (string, 55/55 records)
    "Map"  x44
    "Waypoint"  x11
data.location  (object, 11/55 records)
data.location.x  (number, 11/55 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 11/55 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 11/55 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 45 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (11); Unit 4 Dev (5); Unit 4 Dev - Dungeon (4); Unit 1 Dev (3); Unit 3 Dev (2); Transition (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 539.57s (p5 3.41s / p95 86612.96s, n=44)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 45/45 records)
    true  x45
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 36 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (14); Unit 4 Dev (6); Unit 4 Dev - Dungeon (5); Unit 1 Dev (3); Unit 3 Dev (3); MainMenu (1); Transition (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 290.11s (p5 3.18s / p95 165163.86s, n=35)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 36/36 records)
    false  x36
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 26 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev (4); MainMenu (3); Unit 1 Dev (3); Unit 3 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1977.37s (p5 7.28s / p95 292378.54s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "DebugMenuStateChanged"  x26
data.isOpened  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 25 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (25)
- **Intervals:** median 7.26s (p5 0.53s / p95 53.92s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "On"  x15
    "Off"  x10
data.floor  (string, 25/25 records)
    "3"  x14
    "1"  x5
    "2"  x4
    "4"  x2
data.machineNumber  (string, 25/25 records)
    "One"  x24
    "Two"  x1
data.machineType  (string, 25/25 records)
    "Condenser"  x11
    "Evaporator"  x6
    "DualChamber_Condenser"  x5
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x1
data.room  (string, 25/25 records)
    "2"  x13
    "1"  x6
    "4"  x4
    "3"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 80982.33s (p5 578.80s / p95 345297.95s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 14 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (14)
- **Intervals:** median 1.83s (p5 0.70s / p95 1857.55s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records, 11 empty-string)
    ""  x11
    "cameraPlaced"  x3
data.boxId  (string, 14/14 records)
    "0"  x10
    "1"  x2
    "2"  x2
data.soilType  (string, 14/14 records)
    "Gravel"  x11
    "Sand"  x2
    "Clay"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3)
- **Intervals:** median 144.16s (p5 0.02s / p95 530400.07s, n=10)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 11/11 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 11/11 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 10 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dungeon Dev (2)
- **Intervals:** median 2.00s (p5 0.01s / p95 483647.72s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "Close"  x5
    "Open"  x5
data.toolName  (string, 10/10 records, 8 empty-string)
    ""  x8
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `soilMachine` — 10 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (10)
- **Intervals:** median 38.86s (p5 0.65s / p95 2506.18s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "ChangeCanister"  x10
data.canisterType  (string, 10/10 records)
    "Clay"  x4
    "Gravel"  x3
    "Sand"  x2
    "Bedrock"  x1
data.floor  (string, 10/10 records)
    "4"  x5
    "5"  x3
    "3"  x2
data.machine  (string, 10/10 records)
    "1"  x9
    "2"  x1
data.row  (string, 10/10 records)
    "TopRow"  x9
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9)
- **Intervals:** median 1.18s (p5 0.13s / p95 122.63s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 7 records

- **Scenes:** <missing sceneName> (7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 7/7 records)
    true  x7
data.message  (string, 7/7 records)
    "Permissions check failed"  x4
    "A user gesture is required to request Pointer Lock."  x3
data.phase  (string, 7/7 records)
    "running"  x7
data.stack  (string, 7/7 records, 3 empty-string)
    "TypeError: Permissions check failed"  x4
    ""  x3
data.type  (string, 7/7 records)
    "unhandled_rejection"  x7
data.unitId  (string, 7/7 records)
    "unit2"  x4
    "unit1"  x2
    "unit4"  x1
data.workspace  (string, 7/7 records)
    "mhs"  x7
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 565188.10s (p5 140194.08s / p95 990182.12s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 1 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "Close"  x1
data.chatID  (string, 1/1 records)
    "NA"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (24 records)
- `TerasGardenBox` data.actionType: "" (11x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (10x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (11x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (40x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*