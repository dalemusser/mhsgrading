# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b7b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b7b
- **Game version string(s) in log:** 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b7b.jsonl
- **Records:** 15370 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b7b
- **Time span:** 2026-10-05T19:15:40.048000+00:00 .. 2026-10-16T16:13:38.170000+00:00 (260h 57m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b7b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 15370 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 95 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5160 | 33.57 | 1 | 9 | 0 | 2026-10-05T19:15:53.196000+00:00 | 2026-10-16T16:13:38.170000+00:00 | 260h 57m |
| PuzzlePieceVisibleEvent | 3522 | 22.91 | 1 | 4 | 0 | 2026-10-07T18:47:51.787000+00:00 | 2026-10-16T13:44:13.383000+00:00 | 210h 56m |
| DialogueEvent | 2530 | 16.46 | 1 | 9 | 1572 | 2026-10-05T19:16:09.705000+00:00 | 2026-10-16T16:13:32.606000+00:00 | 260h 57m |
| PlayerPositionEvent | 2478 | 16.12 | 1 | 9 | 0 | 2026-10-05T19:15:49.849000+00:00 | 2026-10-16T16:13:36.766000+00:00 | 260h 57m |
| argumentationNodeEvent | 671 | 4.37 | 1 | 5 | 0 | 2026-10-06T18:57:25.619000+00:00 | 2026-10-16T16:02:37.671000+00:00 | 237h 5m |
| ObjectInterEvent | 352 | 2.29 | 1 | 9 | 0 | 2026-10-06T18:39:44.926000+00:00 | 2026-10-16T16:13:38.170000+00:00 | 237h 33m |
| TopographicMapEvent | 154 | 1.0 | 1 | 2 | 0 | 2026-10-07T18:48:18.870000+00:00 | 2026-10-15T01:44:38.121000+00:00 | 174h 56m |
| argumentationAnswerEvent | 114 | 0.74 | 1 | 5 | 0 | 2026-10-06T18:58:51.006000+00:00 | 2026-10-16T16:02:38.613000+00:00 | 237h 3m |
| questEvent | 97 | 0.63 | 1 | 9 | 97 | 2026-10-05T19:16:09.677000+00:00 | 2026-10-16T16:08:59.127000+00:00 | 260h 52m |
| Soil Key Puzzle | 87 | 0.57 | 1 | 3 | 0 | 2026-10-07T19:00:33.041000+00:00 | 2026-10-15T01:58:05.575000+00:00 | 174h 57m |
| DEBUGMenu | 45 | 0.29 | 1 | 9 | 0 | 2026-10-05T19:15:49.831000+00:00 | 2026-10-16T15:56:46.202000+00:00 | 260h 40m |
| WaterChamberEvent | 27 | 0.18 | 1 | 1 | 0 | 2026-10-16T13:43:19.815000+00:00 | 2026-10-16T13:53:05.603000+00:00 | 9m 45s |
| gameWindowFocusEvent | 27 | 0.18 | 1 | 4 | 0 | 2026-10-05T19:15:40.048000+00:00 | 2026-10-16T16:11:35.445000+00:00 | 260h 55m |
| gameStartEvent | 21 | 0.14 | 1 | 1 | 0 | 2026-10-05T19:15:40.049000+00:00 | 2026-10-16T15:56:46.352000+00:00 | 260h 41m |
| SolarStillDesignEvent | 20 | 0.13 | 1 | 1 | 0 | 2026-10-16T16:05:37.759000+00:00 | 2026-10-16T16:06:42.015000+00:00 | 1m 4s |
| argumentationEvent | 18 | 0.12 | 1 | 5 | 0 | 2026-10-06T18:58:31.146000+00:00 | 2026-10-16T16:02:38.656000+00:00 | 237h 4m |
| soilMachine | 13 | 0.08 | 1 | 1 | 0 | 2026-10-15T18:45:15.498000+00:00 | 2026-10-15T18:52:32.095000+00:00 | 7m 16s |
| gameWindowUnfocusEvent | 12 | 0.08 | 1 | 4 | 0 | 2026-10-05T19:18:05.212000+00:00 | 2026-10-16T16:11:33.996000+00:00 | 260h 53m |
| TerasGardenBox | 8 | 0.05 | 1 | 1 | 0 | 2026-10-16T00:36:45.977000+00:00 | 2026-10-16T00:37:40.254000+00:00 | 54.3s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T19:04:57.429000+00:00 | 2026-10-16T16:13:38.155000+00:00 | 237h 8m |
| chatEvent | 5 | 0.03 | 1 | 3 | 0 | 2026-10-06T19:14:32.862000+00:00 | 2026-10-16T15:57:03.784000+00:00 | 236h 42m |
| DaniEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-06T19:14:28.738000+00:00 | 2026-10-06T19:14:32.684000+00:00 | 3.9s |
| argumentationToolEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-10-06T19:00:27.809000+00:00 | 2026-10-06T19:00:27.809000+00:00 | 0.0s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 88148.796s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.017s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.069s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.244s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 9.577s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 4.181s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 148.286s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 4137.552s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 16229.401s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 3760.828s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 8012.069s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.957s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.8x vs baseline. 
  - Observed: 45 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 22.8x vs baseline. 
  - Observed: 114 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,3,II; A,B,2,II; A,B,C,1,II; A,B,C,2,II; A,B,C,3,II; A,B,C,4,II; A,D,2,II; A,D,C,2,II; B,1,II; B,2,II; B,3,I; B,3,II; B,4,II; B,C,2,II; C,2,II; C,3,II; C,A,2,II; C,A,B,2,II; C,B,A,3,II; C,D,3,II; D,1,II; D,2,II; D,A,1,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 671 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 1 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [17-17, 17-19, 17-20, 17-22, 17-26] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 27 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
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
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[195] _id=6ac540ebde269131f9b6bab1 ts=2026-10-06T18:41:47.1060000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[235] _id=6ac541cdde269131f9b6d478 ts=2026-10-06T18:45:32.9000000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[295] _id=6ac54274de269131f9b6eba1 ts=2026-10-06T18:48:19.2700000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[1] _id=6ac3f75dde269131f9af6d5d ts=2026-10-05T19:15:40.0490000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[32] _id=6ac53ec0de269131f9b67ae3 ts=2026-10-06T18:32:31.1490000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[644] _id=6ac546aede269131f9b74e77 ts=2026-10-06T19:06:21.5510000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[0] _id=6ac3f75cde269131f9af6d5b ts=2026-10-05T19:15:40.0480000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[31] _id=6ac53ec0de269131f9b67ae1 ts=2026-10-06T18:32:31.1470000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[643] _id=6ac546aede269131f9b74e6d ts=2026-10-06T19:06:21.5500000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[30] _id=6ac53ebfde269131f9b67ad1 ts=2026-10-05T19:18:05.212Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[959] _id=6ac6932bde269131f9bdfb4c ts=2026-10-06T19:17:44.446Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[2396] _id=6ac697d7de269131f9beda27 ts=2026-10-07T19:04:55.1370000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5159 | 0.0 | 1.004 | 182.102 | 12.838 | 346610.674 | 0.33 | 103 | 16 |
| PuzzlePieceVisibleEvent | 3521 | 0.0 | 0.069 | 215.672 | 2.007 | 346667.579 | 0.28 | 1513 | 9 |
| DialogueEvent | 2529 | 0.0 | 4.125 | 371.468 | 31.843 | 346551.871 | 0.16 | 729 | 16 |
| PlayerPositionEvent | 2464 | 0.0 | 10.003 | 334.609 | 10.2 | 346473.929 | 0.18 | 1 | 10 |
| argumentationNodeEvent | 670 | 0.004 | 0.501 | 1273.899 | 10.107 | 621742.474 | 0.05 | 59 | 6 |
| ObjectInterEvent | 351 | 0.0 | 12.017 | 2436.562 | 608.093 | 348869.627 | 0.02 | 7 | 18 |
| TopographicMapEvent | 153 | 0.017 | 5.244 | 4116.204 | 471.604 | 431315.21 | 0.01 | 1 | 8 |
| argumentationAnswerEvent | 113 | 0.13 | 4.181 | 7552.457 | 83.432 | 621841.518 | 0.01 | 0 | 5 |
| questEvent | 96 | 0.0 | 228.339 | 9783.015 | 70086.136 | 346602.845 | 0.01 | 14 | 24 |
| Soil Key Puzzle | 86 | 0.006 | 1.077 | 7323.867 | 21.854 | 518528.951 | 0.01 | 3 | 3 |
| DEBUGMenu | 44 | 6.904 | 749.59 | 21328.554 | 84904.965 | 346988.241 | 0.0 | 0 | 25 |
| WaterChamberEvent | 26 | 0.843 | 9.577 | 22.53 | 59.965 | 85.645 | 2.66 | 0 | 0 |
| gameWindowFocusEvent | 26 | 1.122 | 3760.828 | 36129.054 | 85331.604 | 346999.611 | 0.0 | 0 | 22 |
| gameStartEvent | 20 | 434.817 | 16229.401 | 46923.315 | 99624.693 | 346999.611 | 0.0 | 0 | 19 |
| SolarStillDesignEvent | 19 | 0.316 | 1.628 | 3.382 | 10.396 | 19.085 | 17.74 | 0 | 0 |
| argumentationEvent | 17 | 0.028 | 148.286 | 50202.795 | 193281.358 | 621734.592 | 0.0 | 3 | 6 |
| soilMachine | 12 | 2.279 | 7.957 | 36.383 | 169.748 | 183.095 | 1.65 | 0 | 0 |
| gameWindowUnfocusEvent | 11 | 1.522 | 8012.069 | 85382.617 | 337411.174 | 588392.776 | 0.0 | 0 | 7 |
| TerasGardenBox | 7 | 0.89 | 2.249 | 7.754 | 20.651 | 20.817 | 7.74 | 0 | 0 |
| EndOfUnit | 4 | 55530.112 | 88148.796 | 213430.182 | 542655.116 | 621893.022 | 0.0 | 0 | 4 |
| chatEvent | 4 | 3.676 | 4137.552 | 213037.731 | 718399.192 | 843872.142 | 0.0 | 0 | 3 |
| DaniEvent | 1 | 3.946 | 3.946 | 3.946 | 3.946 | 3.946 | 15.21 | 0 | 0 |
| argumentationToolEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 15 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[2643] _id=6ac7e5a7de269131f9c58b90 ts=2026-10-08T18:49:10.2360000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[2644] _id=6ac7e5a7de269131f9c58b91 ts=2026-10-08T18:49:10.2360000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[2648] _id=6ac7e5a7de269131f9c58b95 ts=2026-10-08T18:49:10.2370000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[2649] _id=6ac7e5a7de269131f9c58b96 ts=2026-10-08T18:49:10.2370000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[4252] _id=6ace7a79de269131f9d0fe04 ts=2026-10-13T18:37:43.1520000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[4253] _id=6ace7a79de269131f9d0fe05 ts=2026-10-13T18:37:43.1520000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 40 group(s), 60 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[3282] _id=6ac7eb7fde269131f9c66e59 ts=2026-10-08T19:14:06.7170000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[3283] _id=6ac7eb7fde269131f9c66e5a ts=2026-10-08T19:14:06.7170000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[3275] _id=6ac7eb80de269131f9c66e74 ts=2026-10-08T19:14:06.9070000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[3276] _id=6ac7eb80de269131f9c66e75 ts=2026-10-08T19:14:06.9070000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[3293] _id=6ac7eb82de269131f9c66eac ts=2026-10-08T19:14:07.6940000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[3294] _id=6ac7eb82de269131f9c66eb2 ts=2026-10-08T19:14:07.6940000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[15121] _id=6ad24ae3de269131f9e58a9a ts=2026-10-16T16:03:47.1100000Z == 6ab9a9279a8420a1e6b56b7b.jsonl[15122] _id=6ad24ae3de269131f9e58a9b ts=2026-10-16T16:03:47.1100000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 43 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b7b.jsonl[162] _id=6ac54071de269131f9b6adcb ts=2026-10-06T18:39:44.9260000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[159] _id=6ac54071de269131f9b6adcf ts=2026-10-06T18:39:44.9310000Z`; `139ms: 6ab9a9279a8420a1e6b56b7b.jsonl[573] _id=6ac545e6de269131f9b732ad ts=2026-10-06T19:03:01.4430000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[574] _id=6ac545e6de269131f9b732b7 ts=2026-10-06T19:03:01.5820000Z`; `824ms: 6ab9a9279a8420a1e6b56b7b.jsonl[698] _id=6ac547dade269131f9b76d28 ts=2026-10-06T19:11:22.0290000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[701] _id=6ac547dbde269131f9b76d3d ts=2026-10-06T19:11:22.8530000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `637ms: 6ab9a9279a8420a1e6b56b7b.jsonl[3024] _id=6ac7e93ede269131f9c6125e ts=2026-10-08T19:04:30.0470000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[3032] _id=6ac7e93ede269131f9c61281 ts=2026-10-08T19:04:30.6840000Z`
- **INFO / Info** `SolarStillDesignEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `899ms: 6ab9a9279a8420a1e6b56b7b.jsonl[15209] _id=6ad24b8ade269131f9e594cc ts=2026-10-16T16:06:33.8300000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[15213] _id=6ad24b8bde269131f9e594d9 ts=2026-10-16T16:06:34.7290000Z`; `739ms: 6ab9a9279a8420a1e6b56b7b.jsonl[15212] _id=6ad24b8ade269131f9e594d2 ts=2026-10-16T16:06:34.3060000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[15211] _id=6ad24b8bde269131f9e594e3 ts=2026-10-16T16:06:35.0450000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `428ms: 6ab9a9279a8420a1e6b56b7b.jsonl[2823] _id=6ac7e7f8de269131f9c5de27 ts=2026-10-08T18:59:03.8540000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[2844] _id=6ac7e7f8de269131f9c5de32 ts=2026-10-08T18:59:04.2820000Z`; `923ms: 6ab9a9279a8420a1e6b56b7b.jsonl[4500] _id=6ace7cddde269131f9d1260b ts=2026-10-13T18:47:57.2040000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[4498] _id=6ace7cdede269131f9d12613 ts=2026-10-13T18:47:58.1270000Z`; `751ms: 6ab9a9279a8420a1e6b56b7b.jsonl[7041] _id=6acfcd07de269131f9d75ff9 ts=2026-10-14T18:42:14.5090000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[7046] _id=6acfcd07de269131f9d76015 ts=2026-10-14T18:42:15.2600000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 29 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `282ms: 6ab9a9279a8420a1e6b56b7b.jsonl[5462] _id=6acec2a1de269131f9d28eac ts=2026-10-13T23:45:36.4980000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[5463] _id=6acec2a1de269131f9d28eae ts=2026-10-13T23:45:36.7800000Z`; `283ms: 6ab9a9279a8420a1e6b56b7b.jsonl[5463] _id=6acec2a1de269131f9d28eae ts=2026-10-13T23:45:36.7800000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[5474] _id=6acec2a1de269131f9d28eb0 ts=2026-10-13T23:45:37.0630000Z`; `474ms: 6ab9a9279a8420a1e6b56b7b.jsonl[5474] _id=6acec2a1de269131f9d28eb0 ts=2026-10-13T23:45:37.0630000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[5464] _id=6acec2a2de269131f9d28eb2 ts=2026-10-13T23:45:37.5370000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6ab9a9279a8420a1e6b56b7b.jsonl[8384] _id=6acfd395de269131f9d83114 ts=2026-10-14T19:10:12.6860000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[8387] _id=6acfd395de269131f9d83117 ts=2026-10-14T19:10:12.7140000Z`; `44ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13294] _id=6ad1267ede269131f9e03d30 ts=2026-10-15T19:16:14.2560000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[13297] _id=6ad1267ede269131f9e03d33 ts=2026-10-15T19:16:14.3000000Z`; `35ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13877] _id=6ad17056de269131f9e23b1e ts=2026-10-16T00:31:17.9180000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[13880] _id=6ad17056de269131f9e23b21 ts=2026-10-16T00:31:17.9530000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 39 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6ab9a9279a8420a1e6b56b7b.jsonl[453] _id=6ac544ddde269131f9b71e59 ts=2026-10-06T18:58:36.6170000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[456] _id=6ac544ddde269131f9b71e5b ts=2026-10-06T18:58:36.6620000Z`; `39ms: 6ab9a9279a8420a1e6b56b7b.jsonl[449] _id=6ac544e4de269131f9b71ec3 ts=2026-10-06T18:58:43.2890000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[468] _id=6ac544e4de269131f9b71ec5 ts=2026-10-06T18:58:43.3280000Z`; `527ms: 6ab9a9279a8420a1e6b56b7b.jsonl[508] _id=6ac54563de269131f9b72885 ts=2026-10-06T19:00:51.0380000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[509] _id=6ac54564de269131f9b7288f ts=2026-10-06T19:00:51.5650000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9279a8420a1e6b56b7b.jsonl[15273] _id=6ad24bd5de269131f9e59aad ts=2026-10-16T16:07:49.3310000Z ~ 6ab9a9279a8420a1e6b56b7b.jsonl[15269] _id=6ad24bd5de269131f9e59ab1 ts=2026-10-16T16:07:49.3350000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6ab9a9279a8420a1e6b56b7b.jsonl[3750] _id=6ac92efdde269131f9cad9a9 ts=2026-10-09T18:14:19.1790000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4239] _id=6ace7a68de269131f9d0fcff ts=2026-10-13T18:37:27.4200000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7b.jsonl[961] _id=6ac69336de269131f9bdfcef ts=2026-10-07T18:45:10.3320000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2637] _id=6ac7e579de269131f9c588bd ts=2026-10-08T18:48:24.2880000Z; 23h 38m: 6ab9a9279a8420a1e6b56b7b.jsonl[645] _id=6ac546c4de269131f9b752ab ts=2026-10-06T19:06:43.8230000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[956] _id=6ac6932bde269131f9bdfb56 ts=2026-10-07T18:44:59.3080000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 96h 15m 
  - Evidence: 96h 15m: 6ab9a9279a8420a1e6b56b7b.jsonl[4238] _id=6ac93108de269131f9cae650 ts=2026-10-09T18:23:03.8740000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4329] _id=6ace7ac0de269131f9d10444 ts=2026-10-13T18:38:55.7450000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7b.jsonl[2627] _id=6ac69aaede269131f9bf1fde ts=2026-10-07T19:17:02.3100000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2701] _id=6ac7e637de269131f9c59d74 ts=2026-10-08T18:51:35.1320000Z; 23h 28m: 6ab9a9279a8420a1e6b56b7b.jsonl[949] _id=6ac54935de269131f9b798c5 ts=2026-10-06T19:17:08.5830000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[970] _id=6ac69353de269131f9be00ef ts=2026-10-07T18:45:39.4040000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 729 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12744] _id=6ad12477de269131f9dff0db ts=2026-10-15T19:07:33.9900000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12745] _id=6ad12477de269131f9dff0dc ts=2026-10-15T19:07:33.9900000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12797] _id=6ad1245fde269131f9dfee4f ts=2026-10-15T19:07:10.6340000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12798] _id=6ad1245fde269131f9dfee50 ts=2026-10-15T19:07:10.6340000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12832] _id=6ad1248ade269131f9dff3f1 ts=2026-10-15T19:07:53.5490000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12833] _id=6ad1248ade269131f9dff3f2 ts=2026-10-15T19:07:53.5490000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 172h 44m 
  - Evidence: 172h 44m: 6ab9a9279a8420a1e6b56b7b.jsonl[638] _id=6ac5465ade269131f9b74093 ts=2026-10-06T19:04:57.4290000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[5543] _id=6acec39fde269131f9d28f4f ts=2026-10-13T23:49:50.4510000Z; 26h 0m: 6ab9a9279a8420a1e6b56b7b.jsonl[5543] _id=6acec39fde269131f9d28f4f ts=2026-10-13T23:49:50.4510000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[10220] _id=6ad03167de269131f9da2072 ts=2026-10-15T01:50:30.7660000Z; 22h 57m: 6ab9a9279a8420a1e6b56b7b.jsonl[10220] _id=6ad03167de269131f9da2072 ts=2026-10-15T01:50:30.7660000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[14226] _id=6ad17448de269131f9e24ba3 ts=2026-10-16T00:48:08.0430000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6ab9a9279a8420a1e6b56b7b.jsonl[4189] _id=6ac93085de269131f9cae2bf ts=2026-10-09T18:20:52.4770000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4251] _id=6ace7a79de269131f9d0fe03 ts=2026-10-13T18:37:43.1510000Z; 23h 31m: 6ab9a9279a8420a1e6b56b7b.jsonl[2635] _id=6ac69abbde269131f9bf208e ts=2026-10-07T19:17:14.8350000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2642] _id=6ac7e5a7de269131f9c58b8f ts=2026-10-08T18:49:10.2340000Z; 23h 28m: 6ab9a9279a8420a1e6b56b7b.jsonl[951] _id=6ac54939de269131f9b7996b ts=2026-10-06T19:17:13.2060000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[965] _id=6ac69342de269131f9bdff0e ts=2026-10-07T18:45:22.6580000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 103 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12337] _id=6ad12128de269131f9df7400 ts=2026-10-15T18:53:28.1150000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12338] _id=6ad12128de269131f9df7401 ts=2026-10-15T18:53:28.1150000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12338] _id=6ad12128de269131f9df7401 ts=2026-10-15T18:53:28.1150000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12339] _id=6ad12128de269131f9df7402 ts=2026-10-15T18:53:28.1150000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12569] _id=6ad122e9de269131f9dfb0b8 ts=2026-10-15T19:00:56.3450000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12570] _id=6ad122e9de269131f9dfb0b9 ts=2026-10-15T19:00:56.3450000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 96h 54m 
  - Evidence: 96h 54m: 6ab9a9279a8420a1e6b56b7b.jsonl[4034] _id=6ac92fa4de269131f9cadfbb ts=2026-10-09T18:17:07.3830000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4744] _id=6ace8269de269131f9d18775 ts=2026-10-13T19:11:37.0100000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7b.jsonl[2338] _id=6ac696d1de269131f9beb84d ts=2026-10-07T19:00:33.0460000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3028] _id=6ac7e938de269131f9c61116 ts=2026-10-08T19:04:24.0980000Z; 23h 30m: 6ab9a9279a8420a1e6b56b7b.jsonl[939] _id=6ac54926de269131f9b79692 ts=2026-10-06T19:16:53.8580000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[985] _id=6ac693a5de269131f9be0b72 ts=2026-10-07T18:47:00.8510000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12630] _id=6ad1235ade269131f9dfc118 ts=2026-10-15T19:02:50.1320000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12631] _id=6ad1235ade269131f9dfc119 ts=2026-10-15T19:02:50.1320000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[12678] _id=6ad123acde269131f9dfcf3b ts=2026-10-15T19:04:12.2200000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12679] _id=6ad123acde269131f9dfcf3c ts=2026-10-15T19:04:12.2200000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13405] _id=6ad1327dde269131f9e1138d ts=2026-10-15T20:07:24.9320000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[13406] _id=6ad1327dde269131f9e1138e ts=2026-10-15T20:07:24.9320000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 96h 14m 
  - Evidence: 96h 14m: 6ab9a9279a8420a1e6b56b7b.jsonl[4232] _id=6ac93109de269131f9cae652 ts=2026-10-09T18:23:04.2380000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4250] _id=6ace7a79de269131f9d0fe02 ts=2026-10-13T18:37:38.1670000Z; 23h 31m: 6ab9a9279a8420a1e6b56b7b.jsonl[2630] _id=6ac69ab4de269131f9bf2043 ts=2026-10-07T19:17:08.1270000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2640] _id=6ac7e5a7de269131f9c58b8e ts=2026-10-08T18:49:07.9290000Z; 23h 27m: 6ab9a9279a8420a1e6b56b7b.jsonl[953] _id=6ac5494fde269131f9b79c3b ts=2026-10-06T19:17:35.1420000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[962] _id=6ac69339de269131f9bdfdba ts=2026-10-07T18:45:10.3460000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[7163] _id=6acfcd77de269131f9d770a6 ts=2026-10-14T18:44:06.3890000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[7157] _id=6acfcd84de269131f9d77262 ts=2026-10-14T18:44:06.389Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 96h 17m 
  - Evidence: 96h 17m: 6ab9a9279a8420a1e6b56b7b.jsonl[4177] _id=6ac9304ede269131f9cae215 ts=2026-10-09T18:19:55.6080000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4244] _id=6ace7a79de269131f9d0fe13 ts=2026-10-13T18:37:43.1870000Z; 24h 13m: 6ab9a9279a8420a1e6b56b7b.jsonl[2308] _id=6ac69695de269131f9bead3e ts=2026-10-07T18:59:31.4130000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3249] _id=6ac7eb3ade269131f9c666d3 ts=2026-10-08T19:12:58.2860000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7b.jsonl[4799] _id=6ace82d6de269131f9d19d41 ts=2026-10-13T19:13:23.9760000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[8654] _id=6acfd4d2de269131f9d8676d ts=2026-10-14T19:15:28.9040000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1513 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[1021] _id=6ac69441de269131f9be261f ts=2026-10-07T18:47:52.2820000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[1022] _id=6ac69441de269131f9be2628 ts=2026-10-07T18:47:52.2820000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[10269] _id=6ad03379de269131f9da278d ts=2026-10-15T01:59:19.0690000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[10270] _id=6ad03379de269131f9da278e ts=2026-10-15T01:59:19.0690000Z; 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[1028] _id=6ac69441de269131f9be2600 ts=2026-10-07T18:47:52.0380000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[1031] _id=6ac69441de269131f9be2604 ts=2026-10-07T18:47:52.0380000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 2m 
  - Evidence: 144h 2m: 6ab9a9279a8420a1e6b56b7b.jsonl[3225] _id=6ac7eb11de269131f9c66165 ts=2026-10-08T19:12:16.9240000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[8625] _id=6acfd492de269131f9d85d24 ts=2026-10-14T19:14:25.8750000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7b.jsonl[2341] _id=6ac696d4de269131f9beb8a0 ts=2026-10-07T19:00:36.0200000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3027] _id=6ac7e938de269131f9c6110d ts=2026-10-08T19:04:24.0920000Z; 6h 42m: 6ab9a9279a8420a1e6b56b7b.jsonl[8632] _id=6acfd4abde269131f9d8615e ts=2026-10-14T19:14:50.7190000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[10249] _id=6ad0330dde269131f9da24ad ts=2026-10-15T01:57:32.7080000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.006s..0.007s shown 
  - Evidence: 6ms: 6ab9a9279a8420a1e6b56b7b.jsonl[3032] _id=6ac7e93ede269131f9c61281 ts=2026-10-08T19:04:30.6840000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3033] _id=6ac7e93fde269131f9c6128e ts=2026-10-08T19:04:30.6900000Z; 6ms: 6ab9a9279a8420a1e6b56b7b.jsonl[3041] _id=6ac7e951de269131f9c6161e ts=2026-10-08T19:04:49.1970000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3043] _id=6ac7e951de269131f9c61637 ts=2026-10-08T19:04:49.2030000Z; 7ms: 6ab9a9279a8420a1e6b56b7b.jsonl[3214] _id=6ac7eafcde269131f9c65f93 ts=2026-10-08T19:11:56.6730000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3215] _id=6ac7eafdde269131f9c65f95 ts=2026-10-08T19:11:56.6800000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b7b.jsonl[2845] _id=6ac7e7f9de269131f9c5de5c ts=2026-10-08T18:59:05.7160000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4493] _id=6ace7ccdde269131f9d1258e ts=2026-10-13T18:47:40.9260000Z; 23h 33m: 6ab9a9279a8420a1e6b56b7b.jsonl[2629] _id=6ac69aafde269131f9bf1fea ts=2026-10-07T19:17:03.5550000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2673] _id=6ac7e5ddde269131f9c59056 ts=2026-10-08T18:50:05.2020000Z; 18h 32m: 6ab9a9279a8420a1e6b56b7b.jsonl[5168] _id=6acec054de269131f9d28c30 ts=2026-10-13T23:35:48.0250000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[5645] _id=6acfc51bde269131f9d6e6b2 ts=2026-10-14T18:08:26.6940000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.017s..0.017s shown 
  - Evidence: 17ms: 6ab9a9279a8420a1e6b56b7b.jsonl[2486] _id=6ac6992ade269131f9befe6a ts=2026-10-07T19:10:34.5570000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2490] _id=6ac6992ade269131f9befe6e ts=2026-10-07T19:10:34.5740000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 172h 44m 
  - Evidence: 172h 44m: 6ab9a9279a8420a1e6b56b7b.jsonl[519] _id=6ac5456cde269131f9b7293d ts=2026-10-06T19:00:59.8600000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[5436] _id=6acec27ede269131f9d28e79 ts=2026-10-13T23:45:01.3780000Z; 23h 56m: 6ab9a9279a8420a1e6b56b7b.jsonl[8381] _id=6acfd395de269131f9d8310c ts=2026-10-14T19:10:12.6580000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12774] _id=6ad1244bde269131f9dfec1c ts=2026-10-15T19:06:51.3440000Z; 19h 23m: 6ab9a9279a8420a1e6b56b7b.jsonl[5465] _id=6acec2a7de269131f9d28eb6 ts=2026-10-13T23:45:42.7620000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[8309] _id=6acfd359de269131f9d82713 ts=2026-10-14T19:09:12.7860000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 172h 42m 
  - Evidence: 172h 42m: 6ab9a9279a8420a1e6b56b7b.jsonl[516] _id=6ac5456cde269131f9b7293f ts=2026-10-06T19:00:59.9030000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[5308] _id=6acec213de269131f9d28de7 ts=2026-10-13T23:43:14.4950000Z; 23h 56m: 6ab9a9279a8420a1e6b56b7b.jsonl[8387] _id=6acfd395de269131f9d83117 ts=2026-10-14T19:10:12.7140000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12750] _id=6ad1242dde269131f9dfe7c5 ts=2026-10-15T19:06:20.7640000Z; 19h 22m: 6ab9a9279a8420a1e6b56b7b.jsonl[5476] _id=6acec2a7de269131f9d28eb8 ts=2026-10-13T23:45:42.7810000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[8263] _id=6acfd326de269131f9d81f2a ts=2026-10-14T19:08:21.8400000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.028s..0.044s shown 
  - Evidence: 28ms: 6ab9a9279a8420a1e6b56b7b.jsonl[8384] _id=6acfd395de269131f9d83114 ts=2026-10-14T19:10:12.6860000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[8387] _id=6acfd395de269131f9d83117 ts=2026-10-14T19:10:12.7140000Z; 35ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13877] _id=6ad17056de269131f9e23b1e ts=2026-10-16T00:31:17.9180000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[13880] _id=6ad17056de269131f9e23b21 ts=2026-10-16T00:31:17.9530000Z; 44ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13294] _id=6ad1267ede269131f9e03d30 ts=2026-10-15T19:16:14.2560000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[13297] _id=6ad1267ede269131f9e03d33 ts=2026-10-15T19:16:14.3000000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 172h 42m 
  - Evidence: 172h 42m: 6ab9a9279a8420a1e6b56b7b.jsonl[514] _id=6ac54569de269131f9b728f5 ts=2026-10-06T19:00:56.2740000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[5368] _id=6acec217de269131f9d28dec ts=2026-10-13T23:43:18.7480000Z; 23h 56m: 6ab9a9279a8420a1e6b56b7b.jsonl[8377] _id=6acfd391de269131f9d83035 ts=2026-10-14T19:10:08.2720000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[12757] _id=6ad1242ede269131f9dfe816 ts=2026-10-15T19:06:22.4400000Z; 19h 22m: 6ab9a9279a8420a1e6b56b7b.jsonl[5472] _id=6acec29bde269131f9d28ea4 ts=2026-10-13T23:45:30.4370000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[8249] _id=6acfd317de269131f9d81cc1 ts=2026-10-14T19:08:06.9820000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 59 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13244] _id=6ad12654de269131f9e037ab ts=2026-10-15T19:15:31.9370000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[13228] _id=6ad12654de269131f9e037ad ts=2026-10-15T19:15:31.9410000Z; 5ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13115] _id=6ad125bcde269131f9e02282 ts=2026-10-15T19:13:00.2870000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[13114] _id=6ad125bcde269131f9e0228a ts=2026-10-15T19:13:00.2920000Z; 5ms: 6ab9a9279a8420a1e6b56b7b.jsonl[13252] _id=6ad1265fde269131f9e038eb ts=2026-10-15T19:15:43.2100000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[13255] _id=6ad12660de269131f9e038fa ts=2026-10-15T19:15:43.2150000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 234h 24m 
  - Evidence: 234h 24m: 6ab9a9279a8420a1e6b56b7b.jsonl[876] _id=6ac5489dde269131f9b78167 ts=2026-10-06T19:14:36.5380000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[14236] _id=6ad228fdde269131f9e3d067 ts=2026-10-16T13:39:08.6800000Z; 2h 3m: 6ab9a9279a8420a1e6b56b7b.jsonl[14859] _id=6ad22c76de269131f9e427b2 ts=2026-10-16T13:53:57.9770000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[14916] _id=6ad24950de269131f9e56d67 ts=2026-10-16T15:57:03.7840000Z; 14m 49s: 6ab9a9279a8420a1e6b56b7b.jsonl[14236] _id=6ad228fdde269131f9e3d067 ts=2026-10-16T13:39:08.6800000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[14859] _id=6ad22c76de269131f9e427b2 ts=2026-10-16T13:53:57.9770000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6ab9a9279a8420a1e6b56b7b.jsonl[3744] _id=6ac92ef1de269131f9cad8f7 ts=2026-10-09T18:14:08.1460000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4241] _id=6ace7a68de269131f9d0fd02 ts=2026-10-13T18:37:27.7570000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7b.jsonl[958] _id=6ac6932bde269131f9bdfb58 ts=2026-10-07T18:44:59.4540000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2639] _id=6ac7e579de269131f9c588bf ts=2026-10-08T18:48:24.4140000Z; 23h 38m: 6ab9a9279a8420a1e6b56b7b.jsonl[644] _id=6ac546aede269131f9b74e77 ts=2026-10-06T19:06:21.5510000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[958] _id=6ac6932bde269131f9bdfb58 ts=2026-10-07T18:44:59.4540000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6ab9a9279a8420a1e6b56b7b.jsonl[3743] _id=6ac92ef1de269131f9cad8f6 ts=2026-10-09T18:14:08.1460000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4240] _id=6ace7a68de269131f9d0fd01 ts=2026-10-13T18:37:27.7570000Z; 23h 43m: 6ab9a9279a8420a1e6b56b7b.jsonl[2401] _id=6ac697ddde269131f9bedb39 ts=2026-10-07T19:05:01.5770000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2638] _id=6ac7e579de269131f9c588be ts=2026-10-08T18:48:24.4140000Z; 23h 38m: 6ab9a9279a8420a1e6b56b7b.jsonl[643] _id=6ac546aede269131f9b74e6d ts=2026-10-06T19:06:21.5500000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[957] _id=6ac6932bde269131f9bdfb57 ts=2026-10-07T18:44:59.4540000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 163h 26m 
  - Evidence: 163h 26m: 6ab9a9279a8420a1e6b56b7b.jsonl[4233] _id=6ac93109de269131f9cae659 ts=2026-10-09T18:23:04.6840000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[14724] _id=6ad22b72de269131f9e40bee ts=2026-10-16T13:49:37.4600000Z; 24h 0m: 6ab9a9279a8420a1e6b56b7b.jsonl[2636] _id=6ac7e578de269131f9c588b9 ts=2026-10-07T19:17:17.058Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[3745] _id=6ac92ef0de269131f9cad8ef ts=2026-10-08T19:17:46.631Z; 23h 59m: 6ab9a9279a8420a1e6b56b7b.jsonl[30] _id=6ac53ebfde269131f9b67ad1 ts=2026-10-05T19:18:05.212Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[959] _id=6ac6932bde269131f9bdfb4c ts=2026-10-06T19:17:44.446Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6ab9a9279a8420a1e6b56b7b.jsonl[4194] _id=6ac9308dde269131f9cae2d2 ts=2026-10-09T18:21:00.3510000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[4260] _id=6ace7a79de269131f9d0fe0c ts=2026-10-13T18:37:43.1960000Z; 23h 39m: 6ab9a9279a8420a1e6b56b7b.jsonl[2502] _id=6ac6990fde269131f9befc69 ts=2026-10-07T19:10:06.9260000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[2652] _id=6ac7e5a7de269131f9c58b99 ts=2026-10-08T18:49:10.2780000Z; 23h 35m: 6ab9a9279a8420a1e6b56b7b.jsonl[692] _id=6ac54787de269131f9b7679b ts=2026-10-06T19:09:58.3160000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[963] _id=6ac69339de269131f9bdfdbb ts=2026-10-07T18:45:12.9190000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7b.jsonl[15121] _id=6ad24ae3de269131f9e58a9a ts=2026-10-16T16:03:47.1100000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[15122] _id=6ad24ae3de269131f9e58a9b ts=2026-10-16T16:03:47.1100000Z; 1ms: 6ab9a9279a8420a1e6b56b7b.jsonl[11960] _id=6ad11ee7de269131f9df2cd5 ts=2026-10-15T18:43:50.5280000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[11961] _id=6ad11ee7de269131f9df2cd6 ts=2026-10-15T18:43:50.5290000Z; 2ms: 6ab9a9279a8420a1e6b56b7b.jsonl[408] _id=6ac5446dde269131f9b71707 ts=2026-10-06T18:56:44.9040000Z -> 6ab9a9279a8420a1e6b56b7b.jsonl[416] _id=6ac5446ede269131f9b71709 ts=2026-10-06T18:56:44.9060000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 16 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[524] _id=6ac54582de269131f9b72b25 ts=2026-10-06T19:01:21.9890000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[2627] _id=6ac69aaede269131f9bf1fde ts=2026-10-07T19:17:02.3100000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[2728] _id=6ac7e6bcde269131f9c5ad00 ts=2026-10-08T18:53:47.9460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[8387] _id=6acfd395de269131f9d83117 ts=2026-10-14T19:10:12.7140000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[13297] _id=6ad1267ede269131f9e03d33 ts=2026-10-15T19:16:14.3000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[456] _id=6ac544ddde269131f9b71e5b ts=2026-10-06T18:58:36.6620000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[468] _id=6ac544e4de269131f9b71ec5 ts=2026-10-06T18:58:43.3280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[14236] _id=6ad228fdde269131f9e3d067 ts=2026-10-16T13:39:08.6800000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[14859] _id=6ad22c76de269131f9e427b2 ts=2026-10-16T13:53:57.9770000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[14916] _id=6ad24950de269131f9e56d67 ts=2026-10-16T15:57:03.7840000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[9913] _id=6ad02da0de269131f9da11d8 ts=2026-10-15T01:34:24.2320000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[11636] _id=6ad11c72de269131f9deec92 ts=2026-10-15T18:33:21.9030000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[11841] _id=6ad11e24de269131f9df11af ts=2026-10-15T18:40:35.6760000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[10241] _id=6ad031efde269131f9da21ed ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 90 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[3473] _id=6ac7ec0dde269131f9c67e22 ts=2026-10-08T19:16:26.7110000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[3480] _id=6ac7ec0ede269131f9c67e3b ts=2026-10-08T19:16:26.9800000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[3477] _id=6ac7ec0ede269131f9c67e3d ts=2026-10-08T19:16:26.9800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 125 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[3283] _id=6ac7eb7fde269131f9c66e5a ts=2026-10-08T19:14:06.7170000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[3274] _id=6ac7eb80de269131f9c66e73 ts=2026-10-08T19:14:06.8390000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[3275] _id=6ac7eb80de269131f9c66e74 ts=2026-10-08T19:14:06.9070000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[3187] _id=6ac7eac2de269131f9c659bb ts=2026-10-08T19:10:58.5380000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[13712] _id=6ad16f93de269131f9e2373b ts=2026-10-16T00:28:02.9690000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 482 start, 476 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'BecameCameraCentered' (totals: 802 open, 799 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 17 unmatched 'BecameVisible' (totals: 969 open, 952 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 58 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 317 of 15368 adjacent _id pairs reverse in client time; worst 104.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b7b.jsonl[1050] _id=6ac69440de269131f9be25d1 ts=2026-10-07T18:49:35.7370000Z`; `6ab9a9279a8420a1e6b56b7b.jsonl[1026] _id=6ac69440de269131f9be25fa ts=2026-10-07T18:47:51.7870000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.71s, min -84667.55s, max -0.16s over 15369 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b7b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5160 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2337); Unit 2 Prod (Refactor) (1195); Unit 4 Dev - Dungeon (498); Unit 3 Dungeon Dev (317); Unit 4 Dev - Anderson Base (209); Unit 4 Dev (206); Unit 5 Dev - Dungeon (160); Unit 1 Dev (146); Unit 5 Dev (92)
- **Intervals:** median 1.00s (p5 0.13s / p95 12.84s, n=5159)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5160/5160 records)
    "pressed"  x5160
data.actionType  (string, 5160/5160 records)
    "Move"  x3514
    "Interact"  x827
    "Jump"  x487
    "Ascend"  x179
    "Sprint"  x65
    "Hoverboard"  x31
    "Descend"  x26
    "Map"  x17
    "SkipCinematic"  x9
    "ToggleDebug"  x3
    "Pause"  x2
data.key  (string, 5160/5160 records, 44 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5160/5160 records)
    "Player"  x2743
    "Drone"  x2417
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3522 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1804); Unit 4 Dev (986); Unit 3 Dungeon Dev (466); Unit 5 Dev - Dungeon (266)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.01s, n=3521)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3522/3522 records)
    "BecameVisible"  x969
    "BecameInvisible"  x952
    "BecameCameraCentered"  x802
    "BecameCameraUncentered"  x799
data.pieceId  (string, 3522/3522 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3522/3522 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2530 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (683); Unit 3 Dev (467); Unit 4 Dev - Anderson Base (346); Unit 4 Dev (281); Unit 5 Dev (217); Unit 1 Dev (197); Unit 3 Dungeon Dev (141); Unit 4 Dev - Dungeon (132); Unit 5 Dev - Dungeon (66)
- **eventKey:** present on 1572 of 2530 records
- **Intervals:** median 4.12s (p5 0.00s / p95 31.84s, n=2529)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1572; [conversationId, dialogueEventType] x958
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2530/2530 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2530/2530 records)
    "DialogueNodeEvent"  x1572
    "DialogueStartEvent"  x482
    "DialogueFinishEvent"  x476
data.nodeId  (number, 1572/2530 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2478 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (862); Unit 3 Dev (473); Unit 4 Dev (215); Unit 1 Dev (206); Unit 4 Dev - Anderson Base (201); Unit 4 Dev - Dungeon (193); Unit 3 Dungeon Dev (120); Unit 5 Dev (119); Unit 5 Dev - Dungeon (89)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.20s, n=2464)
- **Fields under `data`:**

```text
data.position  (object, 2478/2478 records)
data.position.x  (number, 2478/2478 records)
    numeric range -682.968 .. 1641.8 (794 unique)
data.position.y  (number, 2478/2478 records)
    numeric range -115.527 .. 222.404 (552 unique)
data.position.z  (number, 2478/2478 records)
    numeric range -1114.42 .. 1963.88 (794 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 671 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (433); Unit 3 Dev (89); Unit 2 Prod (Refactor) (69); Unit 1 Dev (48); Unit 5 Dev (32)
- **Intervals:** median 0.50s (p5 0.04s / p95 10.11s, n=670)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 671/671 records)
    "argumentationNodeHoverEnd"  x279
    "argumentationNodeHoverStart"  x277
    "argumentationNodeAdd"  x71
    "argumentationNodeRemove"  x44
data.argumentationTitle  (string, 671/671 records)
    "Unit 4 - Flooding"  x433
    "Unit 3 - Pollution Upstream"  x89
    "Unit 2 – Watershed"  x69
    "Unit 5"  x32
    "Unit 1 - Freshwater"  x31
    "Unit 1 - Argumentation Tutorial"  x17
data.nodeName  (string, 671/671 records)
    "B"  x96
    "A"  x95
    "II"  x81
    "C"  x73
    "1"  x71
    "2"  x60
    "3"  x58
    "I"  x55
    "D"  x45
    "4"  x34
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 352 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (117); Unit 4 Dev - Dungeon (91); Unit 3 Dungeon Dev (49); Unit 4 Dev - Anderson Base (27); Unit 4 Dev (20); Unit 1 Dev (14); Unit 3 Dev (14); Unit 5 Dev (12); Unit 5 Dev - Dungeon (8)
- **Intervals:** median 12.02s (p5 0.19s / p95 608.09s, n=351)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 352/352 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 352/352 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 154 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (121); Unit 2 Prod (Refactor) (33)
- **Intervals:** median 5.24s (p5 0.61s / p95 471.60s, n=153)
- **`data` key-set variants:** [actionType, featureUsed] x122; [actionType, featureUsed, location] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 154/154 records)
    "MapCloseEvent"  x61
    "MapOpenEvent"  x61
    "WaypointMoveEvent"  x23
    "WaypointSetEvent"  x8
    "WaypointResetEvent"  x1
data.featureUsed  (string, 154/154 records)
    "Map"  x122
    "Waypoint"  x32
data.location  (object, 32/154 records)
data.location.x  (number, 32/154 records)
    numeric range -319.411 .. 377.918 (24 unique)
data.location.y  (number, 32/154 records)
    numeric range -278.8 .. 230.139 (25 unique)
data.location.z  (number, 32/154 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 114 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (83); Unit 3 Dev (18); Unit 2 Prod (Refactor) (9); Unit 1 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 4.18s (p5 0.18s / p95 83.43s, n=113)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 114/114 records)
    "submitAnswerEvent"  x114
data.answerSubmitted  (string, 114/114 records)
    30 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 114/114 records)
    "Unit 4 - Flooding"  x83
    "Unit 3 - Pollution Upstream"  x18
    "Unit 2 – Watershed"  x9
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `questEvent` — 97 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 3 Dev (19); Unit 1 Dev (13); Unit 4 Dev - Dungeon (13); Unit 4 Dev (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 97 of 97 records
- **Intervals:** median 228.34s (p5 0.00s / p95 70086.14s, n=96)
- **`data` key-set variants:** [questEventType, questID, questName] x58; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 97/97 records)
    "questActiveEvent"  x58
    "questFinishEvent"  x39
data.questID  (string, 97/97 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 97/97 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/97 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 87 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (73); Unit 4 Dev (8); Unit 3 Dev (6)
- **Intervals:** median 1.08s (p5 0.16s / p95 21.85s, n=86)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x78; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/87 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/87 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 78/87 records)
    "RightDrag"  x44
    "LeftDrag"  x34
data.currentSoilType  (string, 78/87 records)
    "CLAYSAND"  x17
    "CLAY"  x16
    "SAND"  x13
    "SANDGRAVEL"  x12
    "CLAYROCK"  x10
    "GRAVEL"  x7
    "BEDROCK"  x3
data.isCorrectSelection  (string, 78/87 records)
    "false"  x61
    "true"  x17
data.waterLevelStatus  (string, 78/87 records)
    "TooHigh"  x36
    "Proper"  x23
    "TooLow"  x19
data.waterRetentionChange  (string, 78/87 records)
    "Increase"  x40
    "Decrease"  x21
    "NoChange"  x17
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 45 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (7); Unit 3 Dev (5); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 749.59s (p5 7.96s / p95 84904.96s, n=44)
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "DebugMenuStateChanged"  x45
data.isOpened  (bool, 45/45 records)
    false  x45
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 27 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (27)
- **Intervals:** median 9.58s (p5 2.47s / p95 59.96s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "On"  x20
    "Off"  x7
data.floor  (string, 27/27 records)
    "3"  x14
    "4"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 27/27 records)
    "One"  x24
    "Two"  x3
data.machineType  (string, 27/27 records)
    "Condenser"  x15
    "Evaporator"  x7
    "DualChamber_Condenser"  x2
    "VentSwitch"  x2
    "DualChamber_Evaporator"  x1
data.room  (string, 27/27 records)
    "2"  x10
    "3"  x7
    "4"  x6
    "1"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 27 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21); Unit 2 Prod (Refactor) (4); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 3760.83s (p5 2.09s / p95 85331.60s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    true  x27
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 16229.40s (p5 711.16s / p95 99624.69s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 20 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (20)
- **Intervals:** median 1.63s (p5 0.41s / p95 10.40s, n=19)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x19; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "optionSelected"  x19
    "DesignSubmitted"  x1
data.designSelections  (object, 1/20 records)
data.designSelections.glassRoofTemperature  (string, 1/20 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/20 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/20 records)
    "Tilted Out"  x1
data.featureUsed  (string, 20/20 records)
    "GlassRoofTemperature"  x9
    "RoofStyle"  x9
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 19/20 records, 7 empty-string)
    ""  x7
    "Cold"  x3
    "Hot"  x3
    "Tilted Out"  x3
    "Tilted In"  x2
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (7); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 148.29s (p5 0.03s / p95 193281.36s, n=17)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 18/18 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x7
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x7
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 13 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (13)
- **Intervals:** median 7.96s (p5 2.62s / p95 169.75s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "ChangeCanister"  x13
data.canisterType  (string, 13/13 records)
    "Sand"  x5
    "Clay"  x3
    "Gravel"  x3
    "Bedrock"  x2
data.floor  (string, 13/13 records)
    "5"  x8
    "4"  x5
data.machine  (string, 13/13 records)
    "1"  x8
    "2"  x5
data.row  (string, 13/13 records)
    "TopRow"  x11
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 5 Dev (2); Unit 1 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 8012.07s (p5 1.81s / p95 337411.17s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 2.25s (p5 0.97s / p95 20.65s, n=7)
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
    "Gravel"  x3
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 88148.80s (p5 59599.19s / p95 542655.12s, n=4)
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

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 4137.55s (p5 136.52s / p95 718399.19s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x4
    "Open"  x1
data.chatID  (string, 5/5 records)
    "NA"  x4
    "[17-17, 17-19, 17-20, 17-22, 17-26]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 3.95s (p5 3.95s / p95 3.95s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 1 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 1/1 records)
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 1/1 records)
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
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
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (73 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (23x); "WaypointResetEvent" (1x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (32x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (44x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*