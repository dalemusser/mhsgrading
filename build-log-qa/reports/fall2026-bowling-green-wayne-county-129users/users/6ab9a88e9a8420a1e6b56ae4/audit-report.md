# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae4

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae4
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae4.jsonl
- **Records:** 10681 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae4
- **Time span:** 2026-10-06T13:15:43.078000+00:00 .. 2026-10-16T18:50:06.543000+00:00 (245h 34m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae4\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 10681 records, 11 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 95 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2643 | 24.74 | 1 | 9 | 0 | 2026-10-06T13:19:28.757000+00:00 | 2026-10-16T13:56:58.313000+00:00 | 240h 37m |
| PuzzlePieceVisibleEvent | 2537 | 23.75 | 1 | 4 | 0 | 2026-10-06T13:54:54.864000+00:00 | 2026-10-16T13:40:36.468000+00:00 | 239h 45m |
| DialogueEvent | 2152 | 20.15 | 1 | 9 | 1312 | 2026-10-06T13:16:21.805000+00:00 | 2026-10-16T13:59:29.766000+00:00 | 240h 43m |
| PlayerPositionEvent | 2150 | 20.13 | 1 | 9 | 0 | 2026-10-06T13:16:01.447000+00:00 | 2026-10-16T18:50:06.543000+00:00 | 245h 34m |
| argumentationNodeEvent | 432 | 4.04 | 1 | 5 | 0 | 2026-10-06T13:40:03.195000+00:00 | 2026-10-16T13:58:36.751000+00:00 | 240h 18m |
| ObjectInterEvent | 281 | 2.63 | 1 | 9 | 0 | 2026-10-06T13:20:53.594000+00:00 | 2026-10-16T13:56:32.582000+00:00 | 240h 35m |
| TopographicMapEvent | 106 | 0.99 | 1 | 2 | 0 | 2026-10-06T13:54:04.772000+00:00 | 2026-10-14T13:30:19.499000+00:00 | 191h 36m |
| questEvent | 76 | 0.71 | 1 | 9 | 76 | 2026-10-06T13:16:21.778000+00:00 | 2026-10-16T18:49:56.004000+00:00 | 245h 33m |
| Soil Key Puzzle | 62 | 0.58 | 1 | 3 | 0 | 2026-10-08T13:43:37.065000+00:00 | 2026-10-14T13:48:31.057000+00:00 | 144h 4m |
| soilMachine | 37 | 0.35 | 1 | 1 | 0 | 2026-10-15T13:23:55.176000+00:00 | 2026-10-15T13:40:56.861000+00:00 | 17m 1s |
| WaterChamberEvent | 34 | 0.32 | 1 | 1 | 0 | 2026-10-16T13:39:04.859000+00:00 | 2026-10-16T13:50:15.394000+00:00 | 11m 10s |
| DEBUGMenu | 33 | 0.31 | 1 | 9 | 0 | 2026-10-06T13:16:01.427000+00:00 | 2026-10-16T18:49:42.889000+00:00 | 245h 33m |
| gameWindowFocusEvent | 22 | 0.21 | 1 | 4 | 0 | 2026-10-06T13:15:43.078000+00:00 | 2026-10-16T18:49:43.046000+00:00 | 245h 33m |
| argumentationAnswerEvent | 21 | 0.2 | 1 | 5 | 0 | 2026-10-06T13:41:08.693000+00:00 | 2026-10-16T13:58:37.485000+00:00 | 240h 17m |
| argumentationToolEvent | 21 | 0.2 | 1 | 3 | 0 | 2026-10-06T13:40:54.499000+00:00 | 2026-10-13T22:26:47.700000+00:00 | 176h 45m |
| argumentationEvent | 16 | 0.15 | 1 | 5 | 0 | 2026-10-06T13:40:56.478000+00:00 | 2026-10-16T13:58:37.522000+00:00 | 240h 17m |
| gameStartEvent | 15 | 0.14 | 1 | 1 | 0 | 2026-10-06T13:15:43.079000+00:00 | 2026-10-16T18:49:43.046000+00:00 | 245h 33m |
| gameWindowUnfocusEvent | 12 | 0.11 | 1 | 4 | 0 | 2026-10-06T13:59:32.408000+00:00 | 2026-10-15T13:30:31.007000+00:00 | 215h 30m |
| chatEvent | 11 | 0.1 | 1 | 3 | 0 | 2026-10-15T13:34:50.347000+00:00 | 2026-10-16T18:49:52.928000+00:00 | 29h 15m |
| TerasGardenBox | 10 | 0.09 | 1 | 1 | 0 | 2026-10-16T13:25:18.989000+00:00 | 2026-10-16T13:26:47.698000+00:00 | 1m 28s |
| DaniEvent | 6 | 0.06 | 1 | 3 | 0 | 2026-10-13T22:12:02.735000+00:00 | 2026-10-15T13:34:50.109000+00:00 | 39h 22m |
| EndOfUnit | 4 | 0.04 | 1 | 4 | 0 | 2026-10-06T13:46:48.887000+00:00 | 2026-10-16T13:34:20.275000+00:00 | 239h 47m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172657.872s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.781s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 15.604s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.097s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.309s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.852s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.66s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 36.898s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.476s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 4.054s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 24309.641s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1510.569s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2344.885s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.611s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
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
  - Observed: Press E 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,C,2,II; B,1,I; B,2,II; B,3,I; C,1,I; C,2,II; D,2,II; D,4,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 432 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.5x vs baseline. 
  - Observed: 11 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [91-14, 91-16, 91-18, 91-19, 91-20]; [91-63, 91-65, 91-67, 91-68, 91-70, 91-72]; [91-89, 91-91, 91-92, 91-98, 91-99] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 7.4x vs baseline. 
  - Observed: 37 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[130] _id=6ac4f63cde269131f9b05cff ts=2026-10-06T13:23:07.2830000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[179] _id=6ac4f725de269131f9b087ca ts=2026-10-06T13:27:00.6170000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[219] _id=6ac4f7bfde269131f9b0a3d3 ts=2026-10-06T13:29:35.0830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[7] _id=6ac4f47fde269131f9b03508 ts=2026-10-06T13:15:43.0790000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[600] _id=6ac4fc2ede269131f9b17988 ts=2026-10-06T13:48:29.4490000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[1124] _id=6ac64860de269131f9b8f69a ts=2026-10-07T13:25:50.9360000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[6] _id=6ac4f47fde269131f9b03506 ts=2026-10-06T13:15:43.0780000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[599] _id=6ac4fc2ede269131f9b17970 ts=2026-10-06T13:48:29.4480000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[1123] _id=6ac64860de269131f9b8f699 ts=2026-10-07T13:25:50.9350000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[1125] _id=6ac64860de269131f9b8f688 ts=2026-10-06T13:59:32.408Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[3203] _id=6ace2f93de269131f9ce9115 ts=2026-10-08T13:58:12.78Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[3337] _id=6ace3046de269131f9ce97e4 ts=2026-10-13T13:21:09.0180000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2642 | 0.0 | 1.781 | 327.876 | 27.56 | 429771.307 | 0.18 | 50 | 8 |
| PuzzlePieceVisibleEvent | 2536 | 0.0 | 0.097 | 340.356 | 2.735 | 429805.533 | 0.18 | 961 | 9 |
| DialogueEvent | 2151 | 0.0 | 3.855 | 402.877 | 36.447 | 429630.771 | 0.15 | 638 | 8 |
| PlayerPositionEvent | 2138 | 0.0 | 10.001 | 413.187 | 10.129 | 429616.398 | 0.15 | 1 | 8 |
| argumentationNodeEvent | 431 | 0.005 | 0.61 | 2007.224 | 10.819 | 605599.87 | 0.03 | 53 | 6 |
| ObjectInterEvent | 280 | 0.0 | 15.604 | 3093.354 | 357.976 | 431691.718 | 0.02 | 5 | 10 |
| TopographicMapEvent | 105 | 0.022 | 5.852 | 6569.283 | 774.923 | 431854.24 | 0.01 | 2 | 8 |
| questEvent | 75 | 0.002 | 229.879 | 11786.856 | 83815.797 | 429758.985 | 0.01 | 11 | 17 |
| Soil Key Puzzle | 61 | 0.148 | 2.309 | 8503.18 | 25.219 | 463985.063 | 0.01 | 0 | 2 |
| soilMachine | 36 | 0.321 | 4.611 | 28.38 | 126.599 | 239.866 | 2.11 | 0 | 0 |
| WaterChamberEvent | 33 | 0.231 | 8.66 | 20.319 | 79.788 | 101.592 | 2.95 | 0 | 0 |
| DEBUGMenu | 32 | 6.419 | 599.483 | 27625.671 | 85726.83 | 431329.595 | 0.0 | 0 | 16 |
| gameWindowFocusEvent | 21 | 9.935 | 1510.569 | 42097.141 | 86599.965 | 431339.728 | 0.0 | 0 | 14 |
| argumentationAnswerEvent | 20 | 2.234 | 36.898 | 43252.44 | 165500.604 | 605639.307 | 0.0 | 0 | 6 |
| argumentationToolEvent | 20 | 0.008 | 1.476 | 31817.66 | 59310.857 | 605672.547 | 0.0 | 2 | 2 |
| argumentationEvent | 15 | 0.028 | 127.427 | 57670.736 | 281271.883 | 605591.794 | 0.0 | 2 | 6 |
| gameStartEvent | 14 | 92.11 | 24309.641 | 63145.712 | 207258.881 | 431339.728 | 0.0 | 0 | 11 |
| gameWindowUnfocusEvent | 11 | 2.571 | 2344.885 | 70532.6 | 301248.305 | 429776.238 | 0.0 | 0 | 8 |
| chatEvent | 10 | 0.692 | 4.054 | 10530.258 | 55578.325 | 86388.695 | 0.01 | 0 | 3 |
| TerasGardenBox | 9 | 1.892 | 3.451 | 9.857 | 25.047 | 25.893 | 6.09 | 0 | 0 |
| DaniEvent | 5 | 4.384 | 5.151 | 28353.475 | 80864.481 | 87523.008 | 0.0 | 0 | 2 |
| EndOfUnit | 3 | 57053.208 | 172657.872 | 287750.463 | 587452.064 | 633540.308 | 0.0 | 0 | 3 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[1130] _id=6ac6486dde269131f9b8f91b ts=2026-10-07T13:26:03.7130000Z == 6ab9a88e9a8420a1e6b56ae4.jsonl[1131] _id=6ac6486dde269131f9b8f91c ts=2026-10-07T13:26:03.7130000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[3219] _id=6ace2fa7de269131f9ce921a ts=2026-10-13T13:18:28.5680000Z == 6ab9a88e9a8420a1e6b56ae4.jsonl[3220] _id=6ace2fa7de269131f9ce921b ts=2026-10-13T13:18:28.5680000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[9004] _id=6ad0da3fde269131f9db2930 ts=2026-10-15T13:50:55.0890000Z == 6ab9a88e9a8420a1e6b56ae4.jsonl[9005] _id=6ad0da3fde269131f9db2931 ts=2026-10-15T13:50:55.0890000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 31 group(s), 49 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[771] _id=6ac4fdc5de269131f9b1ec06 ts=2026-10-06T13:55:09.3780000Z == 6ab9a88e9a8420a1e6b56ae4.jsonl[767] _id=6ac4fdc5de269131f9b1ec0c ts=2026-10-06T13:55:09.3780000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[699] _id=6ac4fdc5de269131f9b1ec22 ts=2026-10-06T13:55:09.6520000Z == 6ab9a88e9a8420a1e6b56ae4.jsonl[768] _id=6ac4fdc5de269131f9b1ec28 ts=2026-10-06T13:55:09.6520000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[842] _id=6ac4fddbde269131f9b1f2ce ts=2026-10-06T13:55:37.3640000Z == 6ab9a88e9a8420a1e6b56ae4.jsonl[822] _id=6ac4fddcde269131f9b1f2f0 ts=2026-10-06T13:55:37.3640000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[76] _id=6ac4f5b6de269131f9b04361 ts=2026-10-06T13:20:53.5940000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[90] _id=6ac4f5b6de269131f9b04369 ts=2026-10-06T13:20:53.5980000Z`; `730ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[8468] _id=6ad0d641de269131f9dab327 ts=2026-10-15T13:33:52.7740000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[8473] _id=6ad0d641de269131f9dab33e ts=2026-10-15T13:33:53.5040000Z`; `321ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[8473] _id=6ad0d641de269131f9dab33e ts=2026-10-15T13:33:53.5040000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[8470] _id=6ad0d642de269131f9dab345 ts=2026-10-15T13:33:53.8250000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 44 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `160ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[739] _id=6ac4fdc2de269131f9b1ead9 ts=2026-10-06T13:54:55.3870000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[723] _id=6ac4fdc2de269131f9b1eae1 ts=2026-10-06T13:54:55.5470000Z`; `72ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[759] _id=6ac4fdc4de269131f9b1ebc2 ts=2026-10-06T13:55:02.0680000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[756] _id=6ac4fdc4de269131f9b1ebcc ts=2026-10-06T13:55:02.1400000Z`; `200ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[761] _id=6ac4fdc5de269131f9b1ebec ts=2026-10-06T13:55:08.9130000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[765] _id=6ac4fdc5de269131f9b1ebf6 ts=2026-10-06T13:55:09.1130000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `467ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[10448] _id=6ad22b7bde269131f9e40d61 ts=2026-10-16T13:49:47.2160000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[10450] _id=6ad22b7cde269131f9e40d7f ts=2026-10-16T13:49:47.6830000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `42ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[5742] _id=6aceb034de269131f9d2812a ts=2026-10-13T22:26:59.9630000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[5745] _id=6aceb034de269131f9d2812d ts=2026-10-13T22:27:00.0050000Z`; `28ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9605] _id=6ad224c1de269131f9e3806f ts=2026-10-16T13:21:05.0040000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[9564] _id=6ad224c1de269131f9e38072 ts=2026-10-16T13:21:05.0320000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `495ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[398] _id=6ac4fa6bde269131f9b11a94 ts=2026-10-06T13:40:59.1780000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[396] _id=6ac4fa6cde269131f9b11a9f ts=2026-10-06T13:40:59.6730000Z`; `982ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[399] _id=6ac4fa6bde269131f9b11a96 ts=2026-10-06T13:40:59.2470000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[400] _id=6ac4fa6cde269131f9b11aba ts=2026-10-06T13:41:00.2290000Z`; `51ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[397] _id=6ac4fa6fde269131f9b11b2a ts=2026-10-06T13:41:01.5970000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[404] _id=6ac4fa6fde269131f9b11b37 ts=2026-10-06T13:41:01.6480000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `924ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[431] _id=6ac4faafde269131f9b128c6 ts=2026-10-06T13:42:07.2560000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[435] _id=6ac4fab0de269131f9b12902 ts=2026-10-06T13:42:08.1800000Z`; `980ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[436] _id=6ac4fab0de269131f9b128e3 ts=2026-10-06T13:42:07.2800000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[437] _id=6ac4fab0de269131f9b12906 ts=2026-10-06T13:42:08.2600000Z`; `874ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[466] _id=6ac4fac5de269131f9b12be0 ts=2026-10-06T13:42:28.7440000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[464] _id=6ac4fac6de269131f9b12bfa ts=2026-10-06T13:42:29.6180000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `731ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[8467] _id=6ad0d641de269131f9dab324 ts=2026-10-15T13:33:52.7690000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[8472] _id=6ad0d641de269131f9dab33a ts=2026-10-15T13:33:53.5000000Z`; `321ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[8472] _id=6ad0d641de269131f9dab33a ts=2026-10-15T13:33:53.5000000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[8475] _id=6ad0d642de269131f9dab343 ts=2026-10-15T13:33:53.8210000Z`; `786ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[8566] _id=6ad0d75ede269131f9dac9d6 ts=2026-10-15T13:38:38.1890000Z ~ 6ab9a88e9a8420a1e6b56ae4.jsonl[8569] _id=6ad0d75fde269131f9daca08 ts=2026-10-15T13:38:38.9750000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2344] _id=6ac79ab1de269131f9c03a67 ts=2026-10-08T13:29:20.7340000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3200] _id=6ace2f93de269131f9ce911b ts=2026-10-13T13:18:10.3290000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1126] _id=6ac6486ade269131f9b8f887 ts=2026-10-07T13:26:01.7100000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2343] _id=6ac79aa7de269131f9c0392e ts=2026-10-08T13:29:10.7350000Z; 23h 37m: 6ab9a88e9a8420a1e6b56ae4.jsonl[602] _id=6ac4fc42de269131f9b1805e ts=2026-10-06T13:48:49.4040000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1122] _id=6ac64860de269131f9b8f698 ts=2026-10-07T13:25:50.8010000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 24h 18m 
  - Evidence: 24h 18m: 6ab9a88e9a8420a1e6b56ae4.jsonl[6774] _id=6acf8092de269131f9d2da66 ts=2026-10-14T13:16:02.7170000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[8497] _id=6ad0d676de269131f9dab7b3 ts=2026-10-15T13:34:45.7250000Z; 15h 3m: 6ab9a88e9a8420a1e6b56ae4.jsonl[5226] _id=6aceacb8de269131f9d27d3b ts=2026-10-13T22:12:07.8860000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[6773] _id=6acf808ede269131f9d2da3f ts=2026-10-14T13:15:58.2610000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3197] _id=6ac7a166de269131f9c154ae ts=2026-10-08T13:57:57.8170000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3222] _id=6ace2fa7de269131f9ce921d ts=2026-10-13T13:18:28.5880000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2310] _id=6ac64ffcde269131f9ba36ee ts=2026-10-07T13:58:19.1460000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2368] _id=6ac79b06de269131f9c04498 ts=2026-10-08T13:30:45.5150000Z; 23h 31m: 6ab9a88e9a8420a1e6b56ae4.jsonl[775] _id=6ac4fdc6de269131f9b1ec4e ts=2026-10-06T13:55:16.9540000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1136] _id=6ac64884de269131f9b8fe99 ts=2026-10-07T13:26:27.9910000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 638 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[4072] _id=6ace38ccde269131f9cefacc ts=2026-10-13T13:57:31.3140000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[4073] _id=6ace38ccde269131f9cefacd ts=2026-10-13T13:57:31.3140000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9442] _id=6ad223e4de269131f9e36c64 ts=2026-10-16T13:17:23.5530000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9443] _id=6ad223e4de269131f9e36c65 ts=2026-10-16T13:17:23.5530000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9461] _id=6ad223f9de269131f9e36e69 ts=2026-10-16T13:17:45.4600000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9462] _id=6ad223f9de269131f9e36e6a ts=2026-10-16T13:17:45.4600000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 175h 59m 
  - Evidence: 175h 59m: 6ab9a88e9a8420a1e6b56ae4.jsonl[597] _id=6ac4fbc9de269131f9b160d4 ts=2026-10-06T13:46:48.8870000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[4263] _id=6acea68dde269131f9d27491 ts=2026-10-13T21:45:49.1950000Z; 47h 57m: 6ab9a88e9a8420a1e6b56ae4.jsonl[7199] _id=6acf856ade269131f9d33846 ts=2026-10-14T13:36:42.4030000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9932] _id=6ad227dcde269131f9e3ba8a ts=2026-10-16T13:34:20.2750000Z; 15h 50m: 6ab9a88e9a8420a1e6b56ae4.jsonl[4263] _id=6acea68dde269131f9d27491 ts=2026-10-13T21:45:49.1950000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[7199] _id=6acf856ade269131f9d33846 ts=2026-10-14T13:36:42.4030000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3150] _id=6ac7a0dade269131f9c14600 ts=2026-10-08T13:55:37.2590000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3218] _id=6ace2fa7de269131f9ce9219 ts=2026-10-13T13:18:28.5660000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2333] _id=6ac65017de269131f9ba38dd ts=2026-10-07T13:58:46.4160000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2346] _id=6ac79ab5de269131f9c03ade ts=2026-10-08T13:29:23.0420000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1086] _id=6ac4febbde269131f9b2327e ts=2026-10-06T13:59:23.0710000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1129] _id=6ac6486dde269131f9b8f91a ts=2026-10-07T13:26:03.7110000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 50 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[1130] _id=6ac6486dde269131f9b8f91b ts=2026-10-07T13:26:03.7130000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1131] _id=6ac6486dde269131f9b8f91c ts=2026-10-07T13:26:03.7130000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[3219] _id=6ace2fa7de269131f9ce921a ts=2026-10-13T13:18:28.5680000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3220] _id=6ace2fa7de269131f9ce921b ts=2026-10-13T13:18:28.5680000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[3220] _id=6ace2fa7de269131f9ce921b ts=2026-10-13T13:18:28.5680000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3221] _id=6ace2fa7de269131f9ce921c ts=2026-10-13T13:18:28.5680000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 54m 
  - Evidence: 119h 54m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3048] _id=6ac7a008de269131f9c12432 ts=2026-10-08T13:52:07.4000000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3802] _id=6ace3654de269131f9ced9e1 ts=2026-10-13T13:46:59.1180000Z; 24h 9m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1852] _id=6ac64a4fde269131f9b974b2 ts=2026-10-07T13:34:06.7200000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2579] _id=6ac79e0ade269131f9c0ca06 ts=2026-10-08T13:43:37.0710000Z; 23h 27m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1085] _id=6ac4febbde269131f9b2327c ts=2026-10-06T13:59:23.0620000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1153] _id=6ac648b2de269131f9b90976 ts=2026-10-07T13:27:13.4760000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9070] _id=6ad0dabdde269131f9db3876 ts=2026-10-15T13:53:01.0890000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9071] _id=6ad0dabdde269131f9db3877 ts=2026-10-15T13:53:01.0890000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9315] _id=6ad222e5de269131f9e358e1 ts=2026-10-16T13:13:08.5110000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9316] _id=6ad222e5de269131f9e358e2 ts=2026-10-16T13:13:08.5110000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9351] _id=6ad2232bde269131f9e35ed6 ts=2026-10-16T13:14:19.3630000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9352] _id=6ad2232bde269131f9e35ed7 ts=2026-10-16T13:14:19.3630000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3198] _id=6ac7a170de269131f9c15560 ts=2026-10-08T13:58:07.4680000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3217] _id=6ace2fa7de269131f9ce9218 ts=2026-10-13T13:18:23.8660000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2338] _id=6ac6504ede269131f9ba3c1f ts=2026-10-07T13:59:41.7850000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2345] _id=6ac79ab5de269131f9c03add ts=2026-10-08T13:29:20.7460000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1114] _id=6ac4fec4de269131f9b23437 ts=2026-10-06T13:59:31.8240000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1128] _id=6ac6486dde269131f9b8f919 ts=2026-10-07T13:26:01.7230000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[7928] _id=6acf8ae1de269131f9d3cd6c ts=2026-10-14T14:00:00.8850000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[7956] _id=6ad0d141de269131f9da5089 ts=2026-10-14T14:00:00.885Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3139] _id=6ac7a0bade269131f9c142dc ts=2026-10-08T13:55:03.9310000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3211] _id=6ace2fa7de269131f9ce9225 ts=2026-10-13T13:18:29.4640000Z; 24h 14m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1832] _id=6ac64a29de269131f9b96b7f ts=2026-10-07T13:33:27.4170000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2662] _id=6ac79f0ede269131f9c0f6e3 ts=2026-10-08T13:47:56.9220000Z; 23h 49m: 6ab9a88e9a8420a1e6b56ae4.jsonl[8907] _id=6ad0d90bde269131f9db0268 ts=2026-10-15T13:45:45.4510000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9942] _id=6ad2280ade269131f9e3bd7e ts=2026-10-16T13:35:04.9790000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 961 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[10000] _id=6ad2290fde269131f9e3d1bf ts=2026-10-16T13:39:25.7400000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10001] _id=6ad2290fde269131f9e3d1c1 ts=2026-10-16T13:39:25.7400000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[10003] _id=6ad22844de269131f9e3c119 ts=2026-10-16T13:36:03.7280000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10004] _id=6ad22844de269131f9e3c11f ts=2026-10-16T13:36:03.7280000Z; 0ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[10004] _id=6ad22844de269131f9e3c11f ts=2026-10-16T13:36:03.7280000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10005] _id=6ad22844de269131f9e3c120 ts=2026-10-16T13:36:03.7280000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 128h 53m 
  - Evidence: 128h 53m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2643] _id=6ac79ed3de269131f9c0ebdb ts=2026-10-08T13:46:58.1430000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[5905] _id=6aceb343de269131f9d2825f ts=2026-10-13T22:40:03.2060000Z; 15h 7m: 6ab9a88e9a8420a1e6b56ae4.jsonl[5894] _id=6aceb36dde269131f9d2827b ts=2026-10-13T22:40:45.1740000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[7275] _id=6acf8812de269131f9d363e9 ts=2026-10-14T13:48:02.1750000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 57m 
  - Evidence: 119h 57m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2528] _id=6ac79d60de269131f9c0aeb1 ts=2026-10-08T13:40:47.8970000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3605] _id=6ace344fde269131f9cec0ac ts=2026-10-13T13:38:22.1370000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae4.jsonl[728] _id=6ac4fd92de269131f9b1dc10 ts=2026-10-06T13:54:25.7600000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1177] _id=6ac648fade269131f9b91c1a ts=2026-10-07T13:28:25.8020000Z; 23h 33m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2258] _id=6ac64f60de269131f9ba2ce4 ts=2026-10-07T13:55:43.2210000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2349] _id=6ac79ac1de269131f9c03c45 ts=2026-10-08T13:29:36.8450000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.023s shown 
  - Evidence: 22ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[1959] _id=6ac64c1cde269131f9b9d440 ts=2026-10-07T13:41:47.8200000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1963] _id=6ac64c1cde269131f9b9d444 ts=2026-10-07T13:41:47.8420000Z; 23ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[1958] _id=6ac64c1cde269131f9b9d43b ts=2026-10-07T13:41:47.7970000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1959] _id=6ac64c1cde269131f9b9d440 ts=2026-10-07T13:41:47.8200000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 168h 13m 
  - Evidence: 168h 13m: 6ab9a88e9a8420a1e6b56ae4.jsonl[458] _id=6ac4faddde269131f9b12ec8 ts=2026-10-06T13:42:53.0440000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3997] _id=6ace38a5de269131f9cef919 ts=2026-10-13T13:56:52.3510000Z; 39h 32m: 6ab9a88e9a8420a1e6b56ae4.jsonl[5741] _id=6aceb034de269131f9d28128 ts=2026-10-13T22:26:59.9360000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9233] _id=6ad0dc33de269131f9db65e8 ts=2026-10-15T13:59:15.3450000Z; 23h 17m: 6ab9a88e9a8420a1e6b56ae4.jsonl[9233] _id=6ad0dc33de269131f9db65e8 ts=2026-10-15T13:59:15.3450000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9425] _id=6ad223dbde269131f9e36b3f ts=2026-10-16T13:17:14.7340000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 168h 13m 
  - Evidence: 168h 13m: 6ab9a88e9a8420a1e6b56ae4.jsonl[492] _id=6ac4faddde269131f9b12eca ts=2026-10-06T13:42:53.0660000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[4019] _id=6ace3875de269131f9cef68e ts=2026-10-13T13:56:04.8600000Z; 39h 31m: 6ab9a88e9a8420a1e6b56ae4.jsonl[5745] _id=6aceb034de269131f9d2812d ts=2026-10-13T22:27:00.0050000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9199] _id=6ad0dbf9de269131f9db5de7 ts=2026-10-15T13:58:17.6400000Z; 23h 18m: 6ab9a88e9a8420a1e6b56ae4.jsonl[9199] _id=6ad0dbf9de269131f9db5de7 ts=2026-10-15T13:58:17.6400000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9395] _id=6ad223a7de269131f9e36810 ts=2026-10-16T13:16:22.5940000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.028s..0.042s shown 
  - Evidence: 28ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[9605] _id=6ad224c1de269131f9e3806f ts=2026-10-16T13:21:05.0040000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9564] _id=6ad224c1de269131f9e38072 ts=2026-10-16T13:21:05.0320000Z; 42ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[5742] _id=6aceb034de269131f9d2812a ts=2026-10-13T22:26:59.9630000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[5745] _id=6aceb034de269131f9d2812d ts=2026-10-13T22:27:00.0050000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 168h 13m 
  - Evidence: 168h 13m: 6ab9a88e9a8420a1e6b56ae4.jsonl[485] _id=6ac4fadbde269131f9b12e96 ts=2026-10-06T13:42:50.9510000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[4023] _id=6ace387bde269131f9cef6d3 ts=2026-10-13T13:56:10.8210000Z; 39h 31m: 6ab9a88e9a8420a1e6b56ae4.jsonl[5740] _id=6aceb033de269131f9d28126 ts=2026-10-13T22:26:58.3820000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9193] _id=6ad0dbf5de269131f9db5d64 ts=2026-10-15T13:58:12.7090000Z; 23h 16m: 6ab9a88e9a8420a1e6b56ae4.jsonl[9250] _id=6ad0dc4cde269131f9db6820 ts=2026-10-15T13:59:40.1590000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9387] _id=6ad223a8de269131f9e3682c ts=2026-10-16T13:16:24.4400000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 53 interval(s) ≤ 0.005s..0.006s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[5733] _id=6aceb032de269131f9d2811c ts=2026-10-13T22:26:57.5410000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[5723] _id=6aceb032de269131f9d2811e ts=2026-10-13T22:26:57.5460000Z; 6ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[4013] _id=6ace3887de269131f9cef775 ts=2026-10-13T13:56:22.9650000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[4027] _id=6ace3887de269131f9cef777 ts=2026-10-13T13:56:22.9710000Z; 6ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[5573] _id=6aceafdbde269131f9d28088 ts=2026-10-13T22:25:30.3950000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[5656] _id=6aceafdbde269131f9d2808a ts=2026-10-13T22:25:30.4010000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 14m 
  - Evidence: 168h 14m: 6ab9a88e9a8420a1e6b56ae4.jsonl[468] _id=6ac4fac6de269131f9b12c10 ts=2026-10-06T13:42:30.2380000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[4050] _id=6ace38afde269131f9cef981 ts=2026-10-13T13:57:02.7850000Z; 8h 29m: 6ab9a88e9a8420a1e6b56ae4.jsonl[4050] _id=6ace38afde269131f9cef981 ts=2026-10-13T13:57:02.7850000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[5705] _id=6aceb00ade269131f9d280ee ts=2026-10-13T22:26:17.7640000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.008s..0.024s shown 
  - Evidence: 8ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[464] _id=6ac4fac6de269131f9b12bfa ts=2026-10-06T13:42:29.6180000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[467] _id=6ac4fac6de269131f9b12bfc ts=2026-10-06T13:42:29.6260000Z; 24ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[431] _id=6ac4faafde269131f9b128c6 ts=2026-10-06T13:42:07.2560000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[436] _id=6ac4fab0de269131f9b128e3 ts=2026-10-06T13:42:07.2800000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 23h 59m 
  - Evidence: 23h 59m: 6ab9a88e9a8420a1e6b56ae4.jsonl[8504] _id=6ad0d68ede269131f9dab9ba ts=2026-10-15T13:35:10.0360000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9927] _id=6ad22803de269131f9e3bd31 ts=2026-10-16T13:34:58.7310000Z; 4h 58m: 6ab9a88e9a8420a1e6b56ae4.jsonl[10486] _id=6ad22bd0de269131f9e417db ts=2026-10-16T13:51:11.7220000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10677] _id=6ad271d1de269131f9e75d6b ts=2026-10-16T18:49:52.9280000Z; 16m 12s: 6ab9a88e9a8420a1e6b56ae4.jsonl[9927] _id=6ad22803de269131f9e3bd31 ts=2026-10-16T13:34:58.7310000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10486] _id=6ad22bd0de269131f9e417db ts=2026-10-16T13:51:11.7220000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2342] _id=6ac79aa7de269131f9c03933 ts=2026-10-08T13:29:10.9000000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3210] _id=6ace2f93de269131f9ce911d ts=2026-10-13T13:18:10.6280000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1124] _id=6ac64860de269131f9b8f69a ts=2026-10-07T13:25:50.9360000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2342] _id=6ac79aa7de269131f9c03933 ts=2026-10-08T13:29:10.9000000Z; 23h 56m: 6ab9a88e9a8420a1e6b56ae4.jsonl[7959] _id=6ad0d142de269131f9da508d ts=2026-10-15T13:12:33.4840000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9256] _id=6ad221fcde269131f9e34e7c ts=2026-10-16T13:09:15.7080000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae4.jsonl[2341] _id=6ac79aa7de269131f9c03932 ts=2026-10-08T13:29:10.9000000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3201] _id=6ace2f93de269131f9ce911c ts=2026-10-13T13:18:10.6280000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1123] _id=6ac64860de269131f9b8f699 ts=2026-10-07T13:25:50.9350000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2341] _id=6ac79aa7de269131f9c03932 ts=2026-10-08T13:29:10.9000000Z; 23h 38m: 6ab9a88e9a8420a1e6b56ae4.jsonl[8382] _id=6ad0d578de269131f9daa019 ts=2026-10-15T13:30:32.5800000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[9255] _id=6ad221fcde269131f9e34e7b ts=2026-10-16T13:09:15.7080000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3203] _id=6ace2f93de269131f9ce9115 ts=2026-10-08T13:58:12.78Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3337] _id=6ace3046de269131f9ce97e4 ts=2026-10-13T13:21:09.0180000Z; 47h 58m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1125] _id=6ac64860de269131f9b8f688 ts=2026-10-06T13:59:32.408Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3203] _id=6ace2f93de269131f9ce9115 ts=2026-10-08T13:58:12.78Z; 23h 48m: 6ab9a88e9a8420a1e6b56ae4.jsonl[7208] _id=6acf86b0de269131f9d34811 ts=2026-10-14T13:42:08.2100000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[8380] _id=6ad0d577de269131f9da9ff1 ts=2026-10-15T13:30:31.0070000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a88e9a8420a1e6b56ae4.jsonl[3152] _id=6ac7a0e6de269131f9c14782 ts=2026-10-08T13:55:49.6530000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[3224] _id=6ace2fa7de269131f9ce921f ts=2026-10-13T13:18:28.6380000Z; 23h 48m: 6ab9a88e9a8420a1e6b56ae4.jsonl[1994] _id=6ac64c02de269131f9b9d07c ts=2026-10-07T13:41:21.9400000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[2347] _id=6ac79ab5de269131f9c03adf ts=2026-10-08T13:29:23.0840000Z; 23h 35m: 6ab9a88e9a8420a1e6b56ae4.jsonl[646] _id=6ac4fca1de269131f9b19f45 ts=2026-10-06T13:50:25.2430000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[1132] _id=6ac6486dde269131f9b8f91d ts=2026-10-07T13:26:03.7470000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[351] _id=6ac4fa11de269131f9b107ec ts=2026-10-06T13:39:28.2190000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[354] _id=6ac4fa11de269131f9b107fb ts=2026-10-06T13:39:28.2210000Z; 5ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[10245] _id=6ad22964de269131f9e3d84c ts=2026-10-16T13:40:52.3890000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10241] _id=6ad22965de269131f9e3d851 ts=2026-10-16T13:40:52.3940000Z; 5ms: 6ab9a88e9a8420a1e6b56ae4.jsonl[10285] _id=6ad229e5de269131f9e3e25c ts=2026-10-16T13:43:01.5130000Z -> 6ab9a88e9a8420a1e6b56ae4.jsonl[10286] _id=6ad229e6de269131f9e3e262 ts=2026-10-16T13:43:01.5180000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[345] _id=6ac4f9e7de269131f9b0ff38 ts=2026-10-06T13:38:47.0330000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[501] _id=6ac4fafbde269131f9b134c1 ts=2026-10-06T13:43:22.3680000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[2148] _id=6ac64e0ade269131f9b9fecf ts=2026-10-07T13:50:01.2540000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[815] _id=6ac4fdd9de269131f9b1f1bb ts=2026-10-06T13:55:34.8810000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[715] _id=6ac4fdd9de269131f9b1f1c1 ts=2026-10-06T13:55:35.2920000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[830] _id=6ac4fdd9de269131f9b1f1c3 ts=2026-10-06T13:55:35.4980000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 32 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[739] _id=6ac4fdc2de269131f9b1ead9 ts=2026-10-06T13:54:55.3870000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[723] _id=6ac4fdc2de269131f9b1eae1 ts=2026-10-06T13:54:55.5470000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[721] _id=6ac4fdc3de269131f9b1eb26 ts=2026-10-06T13:54:56.1650000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[5745] _id=6aceb034de269131f9d2812d ts=2026-10-13T22:27:00.0050000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[404] _id=6ac4fa6fde269131f9b11b37 ts=2026-10-06T13:41:01.6480000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[409] _id=6ac4fa72de269131f9b11be1 ts=2026-10-06T13:41:06.0420000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[9927] _id=6ad22803de269131f9e3bd31 ts=2026-10-16T13:34:58.7310000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[10486] _id=6ad22bd0de269131f9e417db ts=2026-10-16T13:51:11.7220000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[10677] _id=6ad271d1de269131f9e75d6b ts=2026-10-16T18:49:52.9280000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 69 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[855] _id=6ac4fde3de269131f9b1f4f4 ts=2026-10-06T13:55:46.0670000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[937] _id=6ac4fe89de269131f9b22638 ts=2026-10-06T13:58:31.4920000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[983] _id=6ac4fe8cde269131f9b22700 ts=2026-10-06T13:58:34.6500000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 262 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[760] _id=6ac4fdc4de269131f9b1ebac ts=2026-10-06T13:55:00.3180000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[756] _id=6ac4fdc4de269131f9b1ebcc ts=2026-10-06T13:55:02.1400000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[762] _id=6ac4fdc5de269131f9b1ebdb ts=2026-10-06T13:55:02.3660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[4152] _id=6acea56fde269131f9d272f7 ts=2026-10-13T21:41:02.7190000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[9395] _id=6ad223a7de269131f9e36810 ts=2026-10-16T13:16:22.5940000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 21 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[4163] _id=6acea573de269131f9d272fe ts=2026-10-13T21:41:06.8690000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[4174] _id=6acea57ade269131f9d27314 ts=2026-10-13T21:41:13.5950000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[9198] _id=6ad0dbf8de269131f9db5dbe ts=2026-10-15T13:58:16.2790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[429] _id=6ac4faadde269131f9b12854 ts=2026-10-06T13:42:05.1570000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[436] _id=6ac4fab0de269131f9b128e3 ts=2026-10-06T13:42:07.2800000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[437] _id=6ac4fab0de269131f9b12906 ts=2026-10-06T13:42:08.2600000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 423 start, 417 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'BecameCameraCentered' (totals: 479 open, 482 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 34 unmatched 'BecameVisible' (totals: 789 open, 787 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 8 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 187 open, 187 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 14 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 44 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 160 of 10680 adjacent _id pairs reverse in client time; worst 88.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae4.jsonl[1250] _id=6ac6493bde269131f9b92b53 ts=2026-10-07T13:29:30.9000000Z`; `6ab9a88e9a8420a1e6b56ae4.jsonl[1253] _id=6ac6493cde269131f9b92ba0 ts=2026-10-07T13:28:02.3010000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.77s, min -429598.96s, max -0.26s over 10681 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae4\coverage.yaml

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

### `InputEvent` — 2643 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1034); Unit 2 Prod (Refactor) (556); Unit 4 Dev - Dungeon (309); Unit 3 Dungeon Dev (227); Unit 4 Dev (157); Unit 5 Dev - Dungeon (118); Unit 4 Dev - Anderson Base (117); Unit 1 Dev (105); Unit 5 Dev (20)
- **Intervals:** median 1.78s (p5 0.16s / p95 27.56s, n=2642)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2643/2643 records)
    "pressed"  x2643
data.actionType  (string, 2643/2643 records)
    "Move"  x2003
    "Interact"  x371
    "Jump"  x81
    "Ascend"  x54
    "Descend"  x53
    "Hoverboard"  x49
    "Map"  x17
    "Sprint"  x12
    "Pause"  x3
data.key  (string, 2643/2643 records, 12 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2643/2643 records)
    "Player"  x1408
    "Drone"  x1235
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2537 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1385); Unit 4 Dev (630); Unit 3 Dungeon Dev (314); Unit 5 Dev - Dungeon (208)
- **Intervals:** median 0.10s (p5 0.00s / p95 2.73s, n=2536)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2537/2537 records)
    "BecameVisible"  x789
    "BecameInvisible"  x787
    "BecameCameraUncentered"  x482
    "BecameCameraCentered"  x479
data.pieceId  (string, 2537/2537 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2537/2537 records)
    1855 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2152 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (722); Unit 3 Dev (315); Unit 4 Dev (255); Unit 3 Dungeon Dev (226); Unit 1 Dev (199); Unit 4 Dev - Anderson Base (165); Unit 4 Dev - Dungeon (114); Unit 5 Dev (81); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1312 of 2152 records
- **Intervals:** median 3.85s (p5 0.00s / p95 36.45s, n=2151)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1312; [conversationId, dialogueEventType] x840
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2152/2152 records)
    numeric range 8 .. 117 (52 unique)
data.dialogueEventType  (string, 2152/2152 records)
    "DialogueNodeEvent"  x1312
    "DialogueStartEvent"  x423
    "DialogueFinishEvent"  x417
data.nodeId  (number, 1312/2152 records)
    numeric range 0 .. 290 (232 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2150 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (673); Unit 3 Dev (389); Unit 3 Dungeon Dev (223); Unit 4 Dev - Dungeon (205); Unit 4 Dev (203); Unit 1 Dev (184); Unit 4 Dev - Anderson Base (124); Unit 5 Dev - Dungeon (97); Unit 5 Dev (52)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=2138)
- **Fields under `data`:**

```text
data.position  (object, 2150/2150 records)
data.position.x  (number, 2150/2150 records)
    numeric range -640.093 .. 1554.69 (750 unique)
data.position.y  (number, 2150/2150 records)
    numeric range -114.326 .. 222.007 (521 unique)
data.position.z  (number, 2150/2150 records)
    numeric range -1038.73 .. 2235.95 (750 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 432 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (181); Unit 2 Prod (Refactor) (88); Unit 3 Dev (73); Unit 1 Dev (62); Unit 5 Dev (28)
- **Intervals:** median 0.61s (p5 0.03s / p95 10.82s, n=431)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 432/432 records)
    "argumentationNodeHoverEnd"  x187
    "argumentationNodeHoverStart"  x187
    "argumentationNodeAdd"  x40
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 432/432 records)
    "Unit 4 - Flooding"  x181
    "Unit 2 – Watershed"  x88
    "Unit 3 - Pollution Upstream"  x73
    "Unit 1 - Freshwater"  x35
    "Unit 5"  x28
    "Unit 1 - Argumentation Tutorial"  x27
data.nodeName  (string, 432/432 records)
    "II"  x54
    "B"  x50
    "C"  x50
    "I"  x50
    "A"  x48
    "1"  x40
    "D"  x39
    "4"  x34
    "2"  x27
    "3"  x27
    "5"  x13
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 281 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (105); Unit 3 Dungeon Dev (58); Unit 2 Prod (Refactor) (44); Unit 4 Dev (21); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (12); Unit 1 Dev (10); Unit 5 Dev - Dungeon (9); Unit 5 Dev (4)
- **Intervals:** median 15.60s (p5 1.11s / p95 357.98s, n=280)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 281/281 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 281/281 records)
    105 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 106 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (76); Unit 3 Dev (30)
- **Intervals:** median 5.85s (p5 1.63s / p95 774.92s, n=105)
- **`data` key-set variants:** [actionType, featureUsed] x66; [actionType, featureUsed, location] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 106/106 records)
    "WaypointMoveEvent"  x36
    "MapCloseEvent"  x33
    "MapOpenEvent"  x33
    "WaypointSetEvent"  x4
data.featureUsed  (string, 106/106 records)
    "Map"  x66
    "Waypoint"  x40
data.location  (object, 40/106 records)
data.location.x  (number, 40/106 records)
    numeric range -320.817 .. 189.053 (38 unique)
data.location.y  (number, 40/106 records)
    numeric range -354.718 .. 269.504 (37 unique)
data.location.z  (number, 40/106 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (12); Unit 4 Dev - Dungeon (10); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (4); Unit 5 Dev (3)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 229.88s (p5 0.01s / p95 83815.80s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x32
data.questID  (string, 76/76 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/76 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 62 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (44); Unit 3 Dev (10); Unit 4 Dev (8)
- **Intervals:** median 2.31s (p5 0.31s / p95 25.22s, n=61)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x56; [Soil Key Puzzle Status, Unit] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/62 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/62 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 56/62 records)
    "RightDrag"  x31
    "LeftDrag"  x25
data.currentSoilType  (string, 56/62 records)
    "CLAY"  x12
    "CLAYROCK"  x11
    "CLAYSAND"  x11
    "SAND"  x10
    "SANDGRAVEL"  x6
    "BEDROCK"  x4
    "GRAVEL"  x2
data.isCorrectSelection  (string, 56/62 records)
    "false"  x43
    "true"  x13
data.waterLevelStatus  (string, 56/62 records)
    "TooHigh"  x25
    "Proper"  x18
    "TooLow"  x13
data.waterRetentionChange  (string, 56/62 records)
    "Increase"  x31
    "NoChange"  x13
    "Decrease"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `soilMachine` — 37 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (37)
- **Intervals:** median 4.61s (p5 0.62s / p95 126.60s, n=36)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "ChangeCanister"  x37
data.canisterType  (string, 37/37 records)
    "Clay"  x23
    "Bedrock"  x8
    "Gravel"  x4
    "Sand"  x2
data.floor  (string, 37/37 records)
    "5"  x27
    "4"  x6
    "3"  x4
data.machine  (string, 37/37 records)
    "1"  x36
    "2"  x1
data.row  (string, 37/37 records)
    "TopRow"  x22
    "BottomRow"  x15
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 34 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (34)
- **Intervals:** median 8.66s (p5 0.58s / p95 79.79s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "On"  x23
    "Off"  x11
data.floor  (string, 34/34 records)
    "4"  x19
    "3"  x10
    "2"  x3
    "1"  x2
data.machineNumber  (string, 34/34 records)
    "One"  x33
    "Two"  x1
data.machineType  (string, 34/34 records)
    "Evaporator"  x14
    "Condenser"  x13
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 34/34 records)
    "3"  x18
    "2"  x10
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 33 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (6); Unit 4 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 599.48s (p5 7.05s / p95 85726.83s, n=32)
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "DebugMenuStateChanged"  x33
data.isOpened  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 22 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Transition (4); Unit 3 Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1510.57s (p5 12.02s / p95 86599.96s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 21 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (9); Unit 2 Prod (Refactor) (5); Unit 1 Dev (3); Unit 3 Dev (3); Unit 5 Dev (1)
- **Intervals:** median 36.90s (p5 4.72s / p95 165500.60s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "submitAnswerEvent"  x21
data.answerSubmitted  (string, 21/21 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 21/21 records)
    "Unit 4 - Flooding"  x9
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationToolEvent` — 21 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (15); Unit 3 Dev (5); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 1.48s (p5 0.02s / p95 59310.86s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "argumentationToolOpen"  x14
    "argumentationToolClose"  x7
data.argumentationTitle  (string, 21/21 records)
    "Unit 1 - Freshwater"  x13
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x1
data.toolName  (string, 21/21 records)
    "BackingInfoPanel - "  x13
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 127.43s (p5 0.04s / p95 281271.88s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 16/16 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x3
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 4 - Flooding"  x4
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 24309.64s (p5 241.59s / p95 207258.88s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Transition (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2344.89s (p5 4.11s / p95 301248.30s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 11 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 4 Dev - Dungeon (8); Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 4.05s (p5 0.78s / p95 55578.32s, n=10)
- **`data` key-set variants:** [actionType, chatID] x8; [actionKey, chatID] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 3/11 records)
    "ScrollStop"  x3
data.actionType  (string, 8/11 records)
    "Close"  x4
    "ScrollStart"  x3
    "Open"  x1
data.chatID  (string, 11/11 records)
    "NA"  x7
    "[91-14, 91-16, 91-18, 91-19, 91-20]"  x2
    "[91-63, 91-65, 91-67, 91-68, 91-70, 91-72]"  x1
    "[91-89, 91-91, 91-92, 91-98, 91-99]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 3.45s (p5 1.94s / p95 25.05s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records, 6 empty-string)
    ""  x6
    "cameraPlaced"  x4
data.boxId  (string, 10/10 records)
    "0"  x6
    "1"  x2
    "2"  x2
data.soilType  (string, 10/10 records)
    "Clay"  x5
    "Sand"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 5.15s (p5 4.40s / p95 80864.48s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 172657.87s (p5 68613.67s / p95 587452.06s, n=3)
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

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (44 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (36x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (40x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)
- `soilMachine` data.canisterType: "Bedrock" (8x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*