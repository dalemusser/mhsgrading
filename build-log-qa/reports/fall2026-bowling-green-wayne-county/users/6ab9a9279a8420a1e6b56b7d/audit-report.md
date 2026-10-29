# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b7d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b7d
- **Game version string(s) in log:** 2.8.1, 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b7d.jsonl
- **Records:** 15110 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b7d
- **Time span:** 2026-10-06T18:31:10.454000+00:00 .. 2026-10-19T16:57:39.860000+00:00 (310h 26m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b7d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 15110 records, 9 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 103 INFO, 0 NOT_TESTED, 85 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `WaterChamberEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4714 | 31.2 | 1 | 7 | 0 | 2026-10-06T18:31:31.270000+00:00 | 2026-10-19T15:32:56.115000+00:00 | 309h 1m |
| PlayerPositionEvent | 3363 | 22.26 | 1 | 8 | 0 | 2026-10-06T18:31:27.850000+00:00 | 2026-10-19T16:57:38.613000+00:00 | 310h 26m |
| PuzzlePieceVisibleEvent | 3349 | 22.16 | 1 | 4 | 0 | 2026-10-07T18:49:55.657000+00:00 | 2026-10-19T15:39:25.456000+00:00 | 284h 49m |
| DialogueEvent | 2353 | 15.57 | 1 | 8 | 1489 | 2026-10-06T18:31:47.971000+00:00 | 2026-10-19T15:40:08.321000+00:00 | 309h 8m |
| argumentationNodeEvent | 436 | 2.89 | 1 | 4 | 0 | 2026-10-06T19:05:32.534000+00:00 | 2026-10-19T15:16:03.650000+00:00 | 308h 10m |
| ObjectInterEvent | 396 | 2.62 | 1 | 7 | 0 | 2026-10-06T18:42:35.485000+00:00 | 2026-10-19T15:32:59.872000+00:00 | 308h 50m |
| questEvent | 96 | 0.64 | 1 | 8 | 96 | 2026-10-06T18:31:47.943000+00:00 | 2026-10-19T15:39:15.660000+00:00 | 309h 7m |
| Soil Key Puzzle | 88 | 0.58 | 1 | 3 | 0 | 2026-10-07T19:01:22.171000+00:00 | 2026-10-15T23:22:53.632000+00:00 | 196h 21m |
| TopographicMapEvent | 77 | 0.51 | 1 | 3 | 0 | 2026-10-07T18:51:15.268000+00:00 | 2026-10-15T19:08:34.734000+00:00 | 192h 17m |
| DEBUGMenu | 47 | 0.31 | 1 | 9 | 0 | 2026-10-06T18:31:27.836000+00:00 | 2026-10-19T15:39:15.682000+00:00 | 309h 7m |
| argumentationAnswerEvent | 29 | 0.19 | 1 | 4 | 0 | 2026-10-06T19:05:52.085000+00:00 | 2026-10-19T15:16:09.913000+00:00 | 308h 10m |
| gameWindowFocusEvent | 25 | 0.17 | 1 | 4 | 0 | 2026-10-06T18:31:10.454000+00:00 | 2026-10-19T15:39:02.481000+00:00 | 309h 7m |
| TerasGardenBox | 23 | 0.15 | 1 | 1 | 0 | 2026-10-19T13:37:17.218000+00:00 | 2026-10-19T15:22:22.410000+00:00 | 1h 45m |
| soilMachine | 21 | 0.14 | 1 | 1 | 0 | 2026-10-16T18:47:55.044000+00:00 | 2026-10-19T15:00:12.432000+00:00 | 68h 12m |
| gameStartEvent | 20 | 0.13 | 1 | 1 | 0 | 2026-10-06T18:31:10.455000+00:00 | 2026-10-19T15:39:02.481000+00:00 | 309h 7m |
| chatEvent | 19 | 0.13 | 1 | 4 | 0 | 2026-10-07T19:03:39.710000+00:00 | 2026-10-19T15:39:15.348000+00:00 | 284h 35m |
| DaniEvent | 18 | 0.12 | 1 | 3 | 0 | 2026-10-07T19:03:21.334000+00:00 | 2026-10-15T01:19:47.765000+00:00 | 174h 16m |
| argumentationEvent | 15 | 0.1 | 1 | 4 | 0 | 2026-10-06T19:05:25.415000+00:00 | 2026-10-19T15:16:09.980000+00:00 | 308h 10m |
| gameWindowUnfocusEvent | 13 | 0.09 | 1 | 5 | 0 | 2026-10-06T19:17:40.137000+00:00 | 2026-10-19T16:57:39.860000+00:00 | 309h 39m |
| EndOfUnit | 5 | 0.03 | 1 | 4 | 0 | 2026-10-06T19:11:18.771000+00:00 | 2026-10-19T15:33:17.288000+00:00 | 308h 21m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |
| argumentationToolEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-10-06T19:07:32.564000+00:00 | 2026-10-06T19:07:32.564000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 207410.933s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.327s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 15.75s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.055s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.261s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.678s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 13.825s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 19.017s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 22545.136s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 3914.747s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 58532.201s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.9x vs baseline. 
  - Observed: 47 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.8x vs baseline. 
  - Observed: 29 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,D,1,II; B,2,II; C,2,II; C,D,A,2,II; D,1,II; D,2,II; D,A,1,II; D,C,A,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 436 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 9.5x vs baseline. 
  - Observed: 19 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-8, 10-10, 10-13, 10-15, 10-16]; [11-31, 11-25, 11-230, 11-29, 11-26]; [18-37, 18-38, 18-39, 18-269, 18-271, 18-273]; [68-1, 68-2, 68-5, 68-29, 18-41, 18-47]; [68-2, 68-5, 68-29, 18-41, 18-47]; [78-0, 78-3, 78-0, 78-7, 78-24]; [79-122, 79-125, 79-121, 79-123, 79-124]; [79-79, 79-80, 79-81, 79-83, 79-115] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 44; 45; 51; 52; 53; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
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
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[307] _id=6ac541cdde269131f9b6d45d ts=2026-10-06T18:45:31.7680000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[414] _id=6ac5430cde269131f9b6fe43 ts=2026-10-06T18:50:50.9990000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[507] _id=6ac54423de269131f9b712fd ts=2026-10-06T18:55:30.7450000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[11] _id=6ac53e6fde269131f9b674df ts=2026-10-06T18:31:10.4550000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[912] _id=6ac54848de269131f9b7775b ts=2026-10-06T19:13:11.5590000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1044] _id=6ac69392de269131f9be08e3 ts=2026-10-07T18:46:41.1910000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[10] _id=6ac53e6fde269131f9b674d9 ts=2026-10-06T18:31:10.4540000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[911] _id=6ac54848de269131f9b77753 ts=2026-10-06T19:13:11.5560000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1043] _id=6ac69392de269131f9be08e2 ts=2026-10-07T18:46:41.1910000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[1046] _id=6ac69392de269131f9be08df ts=2026-10-06T19:17:40.137Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[2965] _id=6ac7e5aede269131f9c58c09 ts=2026-10-07T19:17:50.249Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[3567] _id=6ace7a52de269131f9d0fc2b ts=2026-10-08T19:17:58.314Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 77 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[1309] _id=6ac694a4de269131f9be390a ts=2026-10-07T18:51:15.2680000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1312] _id=6ac694aade269131f9be39ee ts=2026-10-07T18:51:21.3860000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1319] _id=6ac694b9de269131f9be3cd0 ts=2026-10-07T18:51:36.7300000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4713 | 0.0 | 1.327 | 236.046 | 18.846 | 429577.525 | 0.25 | 139 | 17 |
| PlayerPositionEvent | 3348 | 0.0 | 10.0 | 333.507 | 10.081 | 429570.603 | 0.18 | 1 | 14 |
| PuzzlePieceVisibleEvent | 3348 | 0.0 | 0.055 | 306.263 | 2.304 | 517803.782 | 0.2 | 1611 | 10 |
| DialogueEvent | 2352 | 0.0 | 4.662 | 473.172 | 45.425 | 429575.08 | 0.13 | 645 | 15 |
| argumentationNodeEvent | 435 | 0.0 | 0.713 | 2550.416 | 8.006 | 580587.341 | 0.02 | 32 | 5 |
| ObjectInterEvent | 395 | 0.0 | 15.75 | 2814.745 | 386.272 | 431062.374 | 0.02 | 5 | 14 |
| questEvent | 95 | 0.002 | 281.605 | 11714.186 | 64101.623 | 429953.507 | 0.01 | 14 | 24 |
| Soil Key Puzzle | 87 | 0.148 | 2.261 | 8125.189 | 71.166 | 430746.006 | 0.01 | 0 | 4 |
| TopographicMapEvent | 76 | 0.021 | 6.678 | 9108.414 | 37288.496 | 430155.787 | 0.01 | 2 | 9 |
| DEBUGMenu | 46 | 7.915 | 571.34 | 24192.779 | 86108.05 | 431230.979 | 0.0 | 0 | 23 |
| argumentationAnswerEvent | 28 | 0.15 | 13.825 | 39622.065 | 276123.762 | 666861.753 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 24 | 134.787 | 3914.747 | 46369.668 | 215527.024 | 431268.15 | 0.0 | 0 | 17 |
| TerasGardenBox | 22 | 1.296 | 5.739 | 286.6 | 37.457 | 6055.035 | 0.21 | 0 | 1 |
| soilMachine | 20 | 2.051 | 40.724 | 12276.869 | 17369.493 | 237162.288 | 0.0 | 0 | 3 |
| gameStartEvent | 19 | 213.294 | 22545.136 | 58572.212 | 257584.681 | 431268.15 | 0.0 | 0 | 17 |
| chatEvent | 18 | 0.963 | 19.017 | 56918.647 | 428102.748 | 603387.643 | 0.0 | 0 | 5 |
| DaniEvent | 17 | 1.692 | 7.446 | 36905.084 | 137443.319 | 603276.397 | 0.0 | 0 | 5 |
| argumentationEvent | 14 | 0.033 | 75.001 | 79246.04 | 500929.709 | 666717.746 | 0.0 | 3 | 4 |
| gameWindowUnfocusEvent | 12 | 131.712 | 58532.201 | 92899.977 | 337973.025 | 461106.222 | 0.0 | 0 | 10 |
| EndOfUnit | 4 | 6220.439 | 207410.933 | 277529.629 | 634635.177 | 689076.211 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationToolEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 10 group(s), 28 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[1034] _id=6ac693a1de269131f9be0ae7 ts=2026-10-07T18:46:55.9450000Z == 6ab9a9279a8420a1e6b56b7d.jsonl[1035] _id=6ac693a1de269131f9be0ae8 ts=2026-10-07T18:46:55.9450000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1038] _id=6ac693a1de269131f9be0aeb ts=2026-10-07T18:46:55.9460000Z == 6ab9a9279a8420a1e6b56b7d.jsonl[1039] _id=6ac693a1de269131f9be0aec ts=2026-10-07T18:46:55.9460000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[3170] _id=6ac7e83cde269131f9c5e616 ts=2026-10-08T19:00:11.0960000Z == 6ab9a9279a8420a1e6b56b7d.jsonl[3171] _id=6ac7e83cde269131f9c5e617 ts=2026-10-08T19:00:11.0960000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 97 group(s), 187 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[1145] _id=6ac6945cde269131f9be2b50 ts=2026-10-07T18:50:02.5130000Z == 6ab9a9279a8420a1e6b56b7d.jsonl[1146] _id=6ac6945cde269131f9be2b51 ts=2026-10-07T18:50:02.5130000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1156] _id=6ac6945ede269131f9be2b7d ts=2026-10-07T18:50:02.7470000Z == 6ab9a9279a8420a1e6b56b7d.jsonl[1158] _id=6ac6945ede269131f9be2b8c ts=2026-10-07T18:50:02.7470000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1170] _id=6ac6946cde269131f9be2de1 ts=2026-10-07T18:50:19.4060000Z == 6ab9a9279a8420a1e6b56b7d.jsonl[1173] _id=6ac6946cde269131f9be2de9 ts=2026-10-07T18:50:19.4060000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[921] _id=6ac54867de269131f9b77adf ts=? == 6ab9a9279a8420a1e6b56b7d.jsonl[3580] _id=6ace7a6bde269131f9d0fd28 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a9279a8420a1e6b56b7d.jsonl[234] _id=6ac5411cde269131f9b6c0c7 ts=2026-10-06T18:42:35.4850000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[235] _id=6ac5411cde269131f9b6c0cf ts=2026-10-06T18:42:35.4910000Z`; `244ms: 6ab9a9279a8420a1e6b56b7d.jsonl[994] _id=6ac54935de269131f9b798b6 ts=2026-10-06T19:17:08.0550000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[995] _id=6ac54935de269131f9b798c7 ts=2026-10-06T19:17:08.2990000Z`; `140ms: 6ab9a9279a8420a1e6b56b7d.jsonl[995] _id=6ac54935de269131f9b798c7 ts=2026-10-06T19:17:08.2990000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[1003] _id=6ac54935de269131f9b798d1 ts=2026-10-06T19:17:08.4390000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `297ms: 6ab9a9279a8420a1e6b56b7d.jsonl[804] _id=6ac54708de269131f9b75db9 ts=2026-10-06T19:07:51.8410000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[805] _id=6ac54709de269131f9b75dd7 ts=2026-10-06T19:07:52.1380000Z`; `150ms: 6ab9a9279a8420a1e6b56b7d.jsonl[805] _id=6ac54709de269131f9b75dd7 ts=2026-10-06T19:07:52.1380000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[807] _id=6ac54709de269131f9b75ddf ts=2026-10-06T19:07:52.2880000Z`; `218ms: 6ab9a9279a8420a1e6b56b7d.jsonl[807] _id=6ac54709de269131f9b75ddf ts=2026-10-06T19:07:52.2880000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[812] _id=6ac54709de269131f9b75deb ts=2026-10-06T19:07:52.5060000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `33ms: 6ab9a9279a8420a1e6b56b7d.jsonl[7276] _id=6acfd30ede269131f9d81b3c ts=2026-10-14T19:07:57.8590000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[7279] _id=6acfd30ede269131f9d81b3f ts=2026-10-14T19:07:57.8920000Z`; `50ms: 6ab9a9279a8420a1e6b56b7d.jsonl[12796] _id=6ad62170de269131f9e96f6d ts=2026-10-19T13:32:56.898Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[12799] _id=6ad62170de269131f9e96f70 ts=2026-10-19T13:32:56.948Z`; `48ms: 6ab9a9279a8420a1e6b56b7d.jsonl[14268] _id=6ad6343ade269131f9e98398 ts=2026-10-19T15:16:09.9320000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[14271] _id=6ad6343ade269131f9e9839b ts=2026-10-19T15:16:09.9800000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 20 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `63ms: 6ab9a9279a8420a1e6b56b7d.jsonl[726] _id=6ac5467ede269131f9b74703 ts=2026-10-06T19:05:32.9070000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[722] _id=6ac5467ede269131f9b7470a ts=2026-10-06T19:05:32.9700000Z`; `47ms: 6ab9a9279a8420a1e6b56b7d.jsonl[672] _id=6ac54685de269131f9b747e3 ts=2026-10-06T19:05:40.5400000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[668] _id=6ac54685de269131f9b747e5 ts=2026-10-06T19:05:40.5870000Z`; `523ms: 6ab9a9279a8420a1e6b56b7d.jsonl[790] _id=6ac546f9de269131f9b75b03 ts=2026-10-06T19:07:36.5240000Z ~ 6ab9a9279a8420a1e6b56b7d.jsonl[788] _id=6ac546fade269131f9b75b2b ts=2026-10-06T19:07:37.0470000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a9279a8420a1e6b56b7d.jsonl[2967] _id=6ac7e5d3de269131f9c58f34 ts=2026-10-08T18:49:54.6060000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3568] _id=6ace7a52de269131f9d0fc2d ts=2026-10-13T18:37:05.5850000Z; 66h 11m: 6ab9a9279a8420a1e6b56b7d.jsonl[11153] _id=6ad26dfcde269131f9e707b0 ts=2026-10-16T18:33:31.8190000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11740] _id=6ad610c1de269131f9e96a07 ts=2026-10-19T12:44:48.7990000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7d.jsonl[1049] _id=6ac6939ede269131f9be0a65 ts=2026-10-07T18:46:53.1170000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2962] _id=6ac7e5aede269131f9c58c0b ts=2026-10-08T18:49:17.6180000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 34m 
  - Evidence: 167h 34m: 6ab9a9279a8420a1e6b56b7d.jsonl[2671] _id=6ac6981ade269131f9bee596 ts=2026-10-07T19:06:01.4890000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[6159] _id=6acfcca7de269131f9d75013 ts=2026-10-14T18:40:37.8860000Z; 5h 49m: 6ab9a9279a8420a1e6b56b7d.jsonl[7795] _id=6acfd550de269131f9d8833d ts=2026-10-14T19:17:35.9730000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[8425] _id=6ad02749de269131f9d9eccf ts=2026-10-15T01:07:21.0230000Z; 20m 44s: 6ab9a9279a8420a1e6b56b7d.jsonl[6667] _id=6acfd071de269131f9d7c393 ts=2026-10-14T18:56:48.0930000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7792] _id=6acfd54dde269131f9d882f7 ts=2026-10-14T19:17:32.8410000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b7d.jsonl[3566] _id=6ac7ec63de269131f9c6883d ts=2026-10-08T19:17:54.5830000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3587] _id=6ace7a6bde269131f9d0fd22 ts=2026-10-13T18:37:29.6630000Z; 65h 45m: 6ab9a9279a8420a1e6b56b7d.jsonl[11728] _id=6ad27401de269131f9e7862b ts=2026-10-16T18:59:12.7070000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11750] _id=6ad610cbde269131f9e96a13 ts=2026-10-19T12:44:58.6790000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7d.jsonl[2957] _id=6ac69ab8de269131f9bf2073 ts=2026-10-07T19:17:11.4300000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3006] _id=6ac7e628de269131f9c59b08 ts=2026-10-08T18:51:19.0340000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 645 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[12662] _id=6ad6216fde269131f9e96eea ts=2026-10-19T13:30:18.758Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12663] _id=6ad6216fde269131f9e96eeb ts=2026-10-19T13:30:18.758Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[12770] _id=6ad6216fde269131f9e96f54 ts=2026-10-19T13:32:37.722Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12771] _id=6ad6216fde269131f9e96f55 ts=2026-10-19T13:32:37.722Z; 1ms: 6ab9a9279a8420a1e6b56b7d.jsonl[12690] _id=6ad6216fde269131f9e96f00 ts=2026-10-19T13:30:58.842Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12691] _id=6ad6216fde269131f9e96f01 ts=2026-10-19T13:30:58.843Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 24m 
  - Evidence: 191h 24m: 6ab9a9279a8420a1e6b56b7d.jsonl[747] _id=6ac547d7de269131f9b76cf3 ts=2026-10-06T19:11:18.7710000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[6098] _id=6acfcb8cde269131f9d7298d ts=2026-10-14T18:35:54.9820000Z; 90h 35m: 6ab9a9279a8420a1e6b56b7d.jsonl[10000] _id=6ad125f9de269131f9e02afc ts=2026-10-15T19:14:00.8650000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[13143] _id=6ad62172de269131f9e970dd ts=2026-10-19T13:49:36.849Z; 24h 38m: 6ab9a9279a8420a1e6b56b7d.jsonl[6098] _id=6acfcb8cde269131f9d7298d ts=2026-10-14T18:35:54.9820000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10000] _id=6ad125f9de269131f9e02afc ts=2026-10-15T19:14:00.8650000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b7d.jsonl[3563] _id=6ac7ec61de269131f9c6880e ts=2026-10-08T19:17:52.1160000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3575] _id=6ace7a6bde269131f9d0fd17 ts=2026-10-13T18:37:29.6410000Z; 65h 46m: 6ab9a9279a8420a1e6b56b7d.jsonl[11719] _id=6ad273d5de269131f9e78434 ts=2026-10-16T18:58:28.6890000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11745] _id=6ad610cbde269131f9e96a0e ts=2026-10-19T12:44:58.4330000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7d.jsonl[2919] _id=6ac69a54de269131f9bf1738 ts=2026-10-07T19:15:31.0280000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2973] _id=6ac7e5e6de269131f9c59199 ts=2026-10-08T18:50:13.8260000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 139 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[10036] _id=6ad15eb7de269131f9e1f721 ts=2026-10-15T23:16:05.8490000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10037] _id=6ad15eb7de269131f9e1f722 ts=2026-10-15T23:16:05.8490000Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[10037] _id=6ad15eb7de269131f9e1f722 ts=2026-10-15T23:16:05.8490000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10038] _id=6ad15eb7de269131f9e1f723 ts=2026-10-15T23:16:05.8490000Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[10038] _id=6ad15eb7de269131f9e1f723 ts=2026-10-15T23:16:05.8490000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10039] _id=6ad15eb7de269131f9e1f724 ts=2026-10-15T23:16:05.8490000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a9279a8420a1e6b56b7d.jsonl[3471] _id=6ac7eb1ade269131f9c662f4 ts=2026-10-08T19:12:24.8550000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3741] _id=6ace7ef0de269131f9d133b4 ts=2026-10-13T18:56:47.2290000Z; 65h 46m: 6ab9a9279a8420a1e6b56b7d.jsonl[11724] _id=6ad273dcde269131f9e784b0 ts=2026-10-16T18:58:35.2780000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11776] _id=6ad610e8de269131f9e96a2a ts=2026-10-19T12:45:27.5950000Z; 24h 11m: 6ab9a9279a8420a1e6b56b7d.jsonl[2565] _id=6ac69703de269131f9bebe60 ts=2026-10-07T19:01:22.1770000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3471] _id=6ac7eb1ade269131f9c662f4 ts=2026-10-08T19:12:24.8550000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[12447] _id=6ad6216dde269131f9e96e07 ts=2026-10-19T13:24:06.027Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12448] _id=6ad6216dde269131f9e96e08 ts=2026-10-19T13:24:06.027Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[13857] _id=6ad632f8de269131f9e981f5 ts=2026-10-19T15:10:47.6580000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[13858] _id=6ad632f8de269131f9e981f6 ts=2026-10-19T15:10:47.6580000Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[14115] _id=6ad6334fde269131f9e98287 ts=2026-10-19T15:12:14.8900000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[14116] _id=6ad6334fde269131f9e98288 ts=2026-10-19T15:12:14.8900000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b7d.jsonl[3564] _id=6ac7ec63de269131f9c68837 ts=2026-10-08T19:17:54.4640000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3574] _id=6ace7a6bde269131f9d0fd16 ts=2026-10-13T18:37:25.0670000Z; 65h 45m: 6ab9a9279a8420a1e6b56b7d.jsonl[11729] _id=6ad27402de269131f9e7862f ts=2026-10-16T18:59:13.9590000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11744] _id=6ad610cbde269131f9e96a0d ts=2026-10-19T12:44:56.7640000Z; 23h 32m: 6ab9a9279a8420a1e6b56b7d.jsonl[2961] _id=6ac69adbde269131f9bf20de ts=2026-10-07T19:17:46.0740000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2968] _id=6ac7e5d7de269131f9c58fb1 ts=2026-10-08T18:49:54.6180000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[5064] _id=6ace83e1de269131f9d1c006 ts=2026-10-13T19:17:52.2900000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[5086] _id=6acef229de269131f9d2b219 ts=2026-10-13T19:17:52.29Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 50m 
  - Evidence: 143h 50m: 6ab9a9279a8420a1e6b56b7d.jsonl[2791] _id=6ac6988ede269131f9bef10d ts=2026-10-07T19:07:55.9030000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3795] _id=6ace7f3ade269131f9d135b3 ts=2026-10-13T18:57:59.6850000Z; 85h 47m: 6ab9a9279a8420a1e6b56b7d.jsonl[10513] _id=6ad16120de269131f9e20281 ts=2026-10-15T23:26:21.3040000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12079] _id=6ad6216bde269131f9e96c91 ts=2026-10-19T13:13:32.445Z; 17h 41m: 6ab9a9279a8420a1e6b56b7d.jsonl[8110] _id=6ad02452de269131f9d9e345 ts=2026-10-15T00:54:40.2330000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[8797] _id=6ad11d21de269131f9def6a9 ts=2026-10-15T18:36:14.9030000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1611 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[10110] _id=6ad1609dde269131f9e1ff32 ts=2026-10-15T23:23:55.7290000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10111] _id=6ad1609dde269131f9e1ff33 ts=2026-10-15T23:23:55.7290000Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[10111] _id=6ad1609dde269131f9e1ff33 ts=2026-10-15T23:23:55.7290000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10260] _id=6ad1609dde269131f9e1ff34 ts=2026-10-15T23:23:55.7290000Z; 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[10123] _id=6ad16072de269131f9e1fe4a ts=2026-10-15T23:23:27.9690000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10184] _id=6ad16072de269131f9e1fe4c ts=2026-10-15T23:23:27.9690000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 39m 
  - Evidence: 119h 39m: 6ab9a9279a8420a1e6b56b7d.jsonl[3559] _id=6ac7ec56de269131f9c68718 ts=2026-10-08T19:17:41.2160000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3740] _id=6ace7ef0de269131f9d133af ts=2026-10-13T18:56:47.2220000Z; 28h 9m: 6ab9a9279a8420a1e6b56b7d.jsonl[7447] _id=6acfd437de269131f9d84c94 ts=2026-10-14T19:12:54.2120000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[10127] _id=6ad16030de269131f9e1fd08 ts=2026-10-15T23:22:23.8660000Z; 24h 15m: 6ab9a9279a8420a1e6b56b7d.jsonl[3764] _id=6ace7f12de269131f9d1346a ts=2026-10-13T18:57:21.9510000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7436] _id=6acfd417de269131f9d847d3 ts=2026-10-14T19:12:22.7300000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 40m 
  - Evidence: 1h 40m: 6ab9a9279a8420a1e6b56b7d.jsonl[12966] _id=6ad62171de269131f9e9701a ts=2026-10-19T13:39:26.33Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[14370] _id=6ad63536de269131f9e9846b ts=2026-10-19T15:20:21.3650000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a9279a8420a1e6b56b7d.jsonl[3352] _id=6ac7ea2dde269131f9c644a7 ts=2026-10-08T19:08:28.4880000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3592] _id=6ace7a79de269131f9d0fdf4 ts=2026-10-13T18:37:44.2750000Z; 23h 35m: 6ab9a9279a8420a1e6b56b7d.jsonl[2959] _id=6ac69ab8de269131f9bf2074 ts=2026-10-07T19:17:11.4620000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3040] _id=6ac7e685de269131f9c5a73b ts=2026-10-08T18:52:52.8210000Z; 17h 44m: 6ab9a9279a8420a1e6b56b7d.jsonl[8698] _id=6ad02a37de269131f9d9fd15 ts=2026-10-15T01:19:51.5110000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[9811] _id=6ad123cade269131f9dfd5d1 ts=2026-10-15T19:04:40.8920000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.027s shown 
  - Evidence: 21ms: 6ab9a9279a8420a1e6b56b7d.jsonl[3045] _id=6ac7e696de269131f9c5a880 ts=2026-10-08T18:53:08.9680000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3049] _id=6ac7e696de269131f9c5a884 ts=2026-10-08T18:53:08.9890000Z; 27ms: 6ab9a9279a8420a1e6b56b7d.jsonl[3044] _id=6ac7e696de269131f9c5a87c ts=2026-10-08T18:53:08.9410000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3045] _id=6ac7e696de269131f9c5a880 ts=2026-10-08T18:53:08.9680000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 185h 14m 
  - Evidence: 185h 14m: 6ab9a9279a8420a1e6b56b7d.jsonl[814] _id=6ac5470fde269131f9b75ebd ts=2026-10-06T19:07:58.4800000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[5900] _id=6acf73fcde269131f9d2cd60 ts=2026-10-14T12:22:20.2330000Z; 114h 22m: 6ab9a9279a8420a1e6b56b7d.jsonl[7274] _id=6acfd30ede269131f9d81b35 ts=2026-10-14T19:07:57.8350000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12661] _id=6ad6216fde269131f9e96ee9 ts=2026-10-19T13:30:18.667Z; 6h 44m: 6ab9a9279a8420a1e6b56b7d.jsonl[5974] _id=6acf7442de269131f9d2cdc8 ts=2026-10-14T12:23:30.1440000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7272] _id=6acfd30ade269131f9d81a78 ts=2026-10-14T19:07:53.6330000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 185h 11m 
  - Evidence: 185h 11m: 6ab9a9279a8420a1e6b56b7d.jsonl[809] _id=6ac5470fde269131f9b75ec3 ts=2026-10-06T19:07:58.5070000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[5836] _id=6acf736cde269131f9d2ccb6 ts=2026-10-14T12:19:56.2530000Z; 114h 20m: 6ab9a9279a8420a1e6b56b7d.jsonl[7279] _id=6acfd30ede269131f9d81b3f ts=2026-10-14T19:07:57.8920000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12599] _id=6ad6216ede269131f9e96eaa ts=2026-10-19T13:28:57.12Z; 6h 43m: 6ab9a9279a8420a1e6b56b7d.jsonl[5970] _id=6acf7442de269131f9d2cdca ts=2026-10-14T12:23:30.1690000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7218] _id=6acfd2c7de269131f9d80e8a ts=2026-10-14T19:06:46.6190000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.033s..0.050s shown 
  - Evidence: 33ms: 6ab9a9279a8420a1e6b56b7d.jsonl[7276] _id=6acfd30ede269131f9d81b3c ts=2026-10-14T19:07:57.8590000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7279] _id=6acfd30ede269131f9d81b3f ts=2026-10-14T19:07:57.8920000Z; 48ms: 6ab9a9279a8420a1e6b56b7d.jsonl[14268] _id=6ad6343ade269131f9e98398 ts=2026-10-19T15:16:09.9320000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[14271] _id=6ad6343ade269131f9e9839b ts=2026-10-19T15:16:09.9800000Z; 50ms: 6ab9a9279a8420a1e6b56b7d.jsonl[12796] _id=6ad62170de269131f9e96f6d ts=2026-10-19T13:32:56.898Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12799] _id=6ad62170de269131f9e96f70 ts=2026-10-19T13:32:56.948Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 161h 16m 
  - Evidence: 161h 16m: 6ab9a9279a8420a1e6b56b7d.jsonl[2617] _id=6ac69788de269131f9beccbf ts=2026-10-07T19:03:35.7470000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[5829] _id=6acf7373de269131f9d2ccbc ts=2026-10-14T12:20:03.0880000Z; 114h 20m: 6ab9a9279a8420a1e6b56b7d.jsonl[7246] _id=6acfd305de269131f9d819c7 ts=2026-10-14T19:07:48.4560000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[12582] _id=6ad6216ede269131f9e96e99 ts=2026-10-19T13:28:45.082Z; 23h 55m: 6ab9a9279a8420a1e6b56b7d.jsonl[803] _id=6ac54704de269131f9b75ccf ts=2026-10-06T19:07:47.2480000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2614] _id=6ac69786de269131f9becc77 ts=2026-10-07T19:03:33.1520000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 32 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7d.jsonl[7250] _id=6acfd2fcde269131f9d8186f ts=2026-10-14T19:07:39.0040000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7251] _id=6acfd2fcde269131f9d81870 ts=2026-10-14T19:07:39.0040000Z; 1ms: 6ab9a9279a8420a1e6b56b7d.jsonl[7269] _id=6acfd303de269131f9d8197d ts=2026-10-14T19:07:46.5010000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[7270] _id=6acfd303de269131f9d8197e ts=2026-10-14T19:07:46.5020000Z; 5ms: 6ab9a9279a8420a1e6b56b7d.jsonl[5898] _id=6acf73f7de269131f9d2cd52 ts=2026-10-14T12:22:14.4500000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[5912] _id=6acf73f7de269131f9d2cd54 ts=2026-10-14T12:22:14.4550000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 36m 
  - Evidence: 167h 36m: 6ab9a9279a8420a1e6b56b7d.jsonl[2628] _id=6ac697b0de269131f9bed25b ts=2026-10-07T19:04:15.8010000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[6162] _id=6acfccacde269131f9d750d0 ts=2026-10-14T18:40:43.4440000Z; 110h 19m: 6ab9a9279a8420a1e6b56b7d.jsonl[8692] _id=6ad02a31de269131f9d9fcf3 ts=2026-10-15T01:19:45.2280000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[14613] _id=6ad639a4de269131f9e98657 ts=2026-10-19T15:39:15.3480000Z; 5h 49m: 6ab9a9279a8420a1e6b56b7d.jsonl[7802] _id=6acfd55fde269131f9d88493 ts=2026-10-14T19:17:50.2620000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[8434] _id=6ad02751de269131f9d9ecfd ts=2026-10-15T01:07:28.6470000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a9279a8420a1e6b56b7d.jsonl[2964] _id=6ac7e5aede269131f9c58c0d ts=2026-10-08T18:49:17.7480000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3570] _id=6ace7a52de269131f9d0fc2f ts=2026-10-13T18:37:05.8980000Z; 66h 11m: 6ab9a9279a8420a1e6b56b7d.jsonl[11150] _id=6ad26df4de269131f9e706cd ts=2026-10-16T18:33:22.4110000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11742] _id=6ad610c1de269131f9e96a09 ts=2026-10-19T12:44:48.9290000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7d.jsonl[1044] _id=6ac69392de269131f9be08e3 ts=2026-10-07T18:46:41.1910000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2964] _id=6ac7e5aede269131f9c58c0d ts=2026-10-08T18:49:17.7480000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a9279a8420a1e6b56b7d.jsonl[2963] _id=6ac7e5aede269131f9c58c0c ts=2026-10-08T18:49:17.7480000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3569] _id=6ace7a52de269131f9d0fc2e ts=2026-10-13T18:37:05.8980000Z; 66h 11m: 6ab9a9279a8420a1e6b56b7d.jsonl[11149] _id=6ad26df4de269131f9e706cc ts=2026-10-16T18:33:22.4110000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11741] _id=6ad610c1de269131f9e96a08 ts=2026-10-19T12:44:48.9290000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7d.jsonl[1043] _id=6ac69392de269131f9be08e2 ts=2026-10-07T18:46:41.1910000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2963] _id=6ac7e5aede269131f9c58c0c ts=2026-10-08T18:49:17.7480000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 128h 5m 
  - Evidence: 128h 5m: 6ab9a9279a8420a1e6b56b7d.jsonl[3567] _id=6ace7a52de269131f9d0fc2b ts=2026-10-08T19:17:58.314Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[5427] _id=6acf6ea4de269131f9d2c96f ts=2026-10-14T03:23:04.536Z; 65h 53m: 6ab9a9279a8420a1e6b56b7d.jsonl[11730] _id=6ad610c1de269131f9e96a05 ts=2026-10-16T18:59:18.613Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11863] _id=6ad612b3de269131f9e96b09 ts=2026-10-19T12:53:06.2950000Z; 24h 0m: 6ab9a9279a8420a1e6b56b7d.jsonl[1046] _id=6ac69392de269131f9be08df ts=2026-10-06T19:17:40.137Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2965] _id=6ac7e5aede269131f9c58c09 ts=2026-10-07T19:17:50.249Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a9279a8420a1e6b56b7d.jsonl[3450] _id=6ac7eae9de269131f9c65dc0 ts=2026-10-08T19:11:36.2010000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[3589] _id=6ace7a6bde269131f9d0fd24 ts=2026-10-13T18:37:29.7080000Z; 65h 47m: 6ab9a9279a8420a1e6b56b7d.jsonl[11708] _id=6ad273aade269131f9e7808e ts=2026-10-16T18:57:46.0580000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11749] _id=6ad610cbde269131f9e96a12 ts=2026-10-19T12:44:58.4800000Z; 23h 33m: 6ab9a9279a8420a1e6b56b7d.jsonl[2951] _id=6ac69aa9de269131f9bf1fac ts=2026-10-07T19:16:56.5570000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[2969] _id=6ac7e5d7de269131f9c58fb2 ts=2026-10-08T18:49:57.9350000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 6ab9a9279a8420a1e6b56b7d.jsonl[11347] _id=6ad27006de269131f9e73aa1 ts=2026-10-16T18:42:13.9740000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11348] _id=6ad27006de269131f9e73aa2 ts=2026-10-16T18:42:13.9760000Z; 2ms: 6ab9a9279a8420a1e6b56b7d.jsonl[700] _id=6ac54626de269131f9b739af ts=2026-10-06T19:04:04.6200000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[688] _id=6ac54626de269131f9b739b1 ts=2026-10-06T19:04:04.6220000Z; 5ms: 6ab9a9279a8420a1e6b56b7d.jsonl[11706] _id=6ad273aade269131f9e7808a ts=2026-10-16T18:57:46.0530000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11708] _id=6ad273aade269131f9e7808e ts=2026-10-16T18:57:46.0580000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 65h 52m 
  - Evidence: 65h 52m: 6ab9a9279a8420a1e6b56b7d.jsonl[11657] _id=6ad27323de269131f9e7768a ts=2026-10-16T18:55:30.7890000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11824] _id=6ad6118dde269131f9e96a9f ts=2026-10-19T12:48:13.0770000Z; 1h 36m: 6ab9a9279a8420a1e6b56b7d.jsonl[12041] _id=6ad6216bde269131f9e96c6a ts=2026-10-19T13:11:59.679Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[13361] _id=6ad62dc9de269131f9e97cdf ts=2026-10-19T14:48:41.1300000Z; 21m 21s: 6ab9a9279a8420a1e6b56b7d.jsonl[11824] _id=6ad6118dde269131f9e96a9f ts=2026-10-19T12:48:13.0770000Z -> 6ab9a9279a8420a1e6b56b7d.jsonl[11978] _id=6ad6216ade269131f9e96c30 ts=2026-10-19T13:09:34.825Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[673] _id=6ac545f8de269131f9b734d5 ts=2026-10-06T19:03:19.8280000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[824] _id=6ac5472dde269131f9b761a1 ts=2026-10-06T19:08:28.7760000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[3160] _id=6ac7e828de269131f9c5e402 ts=2026-10-08T18:59:51.5030000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[7279] _id=6acfd30ede269131f9d81b3f ts=2026-10-14T19:07:57.8920000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[12799] _id=6ad62170de269131f9e96f70 ts=2026-10-19T13:32:56.948Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[14271] _id=6ad6343ade269131f9e9839b ts=2026-10-19T15:16:09.9800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[722] _id=6ac5467ede269131f9b7470a ts=2026-10-06T19:05:32.9700000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[668] _id=6ac54685de269131f9b747e5 ts=2026-10-06T19:05:40.5870000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[14613] _id=6ad639a4de269131f9e98657 ts=2026-10-19T15:39:15.3480000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[13300] _id=6ad62c6bde269131f9e97c0a ts=2026-10-19T14:42:50.9950000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[921] _id=6ac54867de269131f9b77adf ts=?`; `6ab9a9279a8420a1e6b56b7d.jsonl[3580] _id=6ace7a6bde269131f9d0fd28 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 113 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[3945] _id=6ace7fddde269131f9d13cab ts=2026-10-13T19:00:43.3280000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[4036] _id=6ace7fdede269131f9d13cb3 ts=2026-10-13T19:00:43.3710000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[3994] _id=6ace7fdede269131f9d13cb7 ts=2026-10-13T19:00:43.3720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 145 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[1146] _id=6ac6945cde269131f9be2b51 ts=2026-10-07T18:50:02.5130000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1154] _id=6ac6945cde269131f9be2b55 ts=2026-10-07T18:50:02.5130000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1173] _id=6ac6946cde269131f9be2de9 ts=2026-10-07T18:50:19.4060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 23 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[3040] _id=6ac7e685de269131f9c5a73b ts=2026-10-08T18:52:52.8210000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[3049] _id=6ac7e696de269131f9c5a884 ts=2026-10-08T18:53:08.9890000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[3101] _id=6ac7e754de269131f9c5c1fd ts=2026-10-08T18:56:19.1340000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'DialogueStartEvent' (totals: 438 start, 426 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'BecameCameraCentered' (totals: 600 open, 597 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 1082 open, 1070 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 26 open, 25 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 57 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 235 of 15107 adjacent _id pairs reverse in client time; worst 200.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b7d.jsonl[1433] _id=6ac6951dde269131f9be51bb ts=2026-10-07T18:53:16.5770000Z`; `6ab9a9279a8420a1e6b56b7d.jsonl[1434] _id=6ac6951ede269131f9be5203 ts=2026-10-07T18:49:55.6570000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.03s, min -429548.25s, max -0.37s over 15108 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b7d\coverage.yaml

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
- **WARNING / Medium** `WaterChamberEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4714 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1042); Unit 3 Dungeon Dev (991); Unit 4 Dev - Dungeon (902); Unit 3 Dev (860); Unit 1 Dev (379); Unit 4 Dev (301); Unit 4 Dev - Anderson Base (239)
- **Intervals:** median 1.33s (p5 0.10s / p95 18.85s, n=4713)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4714/4714 records)
    "pressed"  x4714
data.actionType  (string, 4714/4714 records)
    "Move"  x3477
    "Interact"  x555
    "Jump"  x424
    "Sprint"  x98
    "Hoverboard"  x75
    "Ascend"  x47
    "Descend"  x17
    "Pause"  x12
    "Map"  x9
data.key  (string, 4714/4714 records, 11 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4714/4714 records)
    "Player"  x3717
    "Drone"  x997
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 3363 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (901); Unit 4 Dev - Dungeon (627); Unit 5 Dev - Dungeon (471); Unit 4 Dev (372); Unit 3 Dungeon Dev (348); Unit 3 Dev (277); Unit 1 Dev (239); Unit 4 Dev - Anderson Base (128)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.08s, n=3348)
- **Fields under `data`:**

```text
data.position  (object, 3363/3363 records)
data.position.x  (number, 3363/3363 records)
    numeric range -684.652 .. 1701.72 (1111 unique)
data.position.y  (number, 3363/3363 records)
    numeric range -114.72 .. 170.436 (631 unique)
data.position.z  (number, 3363/3363 records)
    numeric range -1144.09 .. 2303.69 (1110 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 3349 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2189); Unit 3 Dungeon Dev (618); Unit 4 Dev (524); Unit 5 Dev - Dungeon (18)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.30s, n=3348)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3349/3349 records)
    "BecameVisible"  x1082
    "BecameInvisible"  x1070
    "BecameCameraCentered"  x600
    "BecameCameraUncentered"  x597
data.pieceId  (string, 3349/3349 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3349/3349 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2353 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (710); Unit 4 Dev (486); Unit 3 Dev (313); Unit 4 Dev - Dungeon (244); Unit 3 Dungeon Dev (234); Unit 1 Dev (201); Unit 4 Dev - Anderson Base (159); Unit 5 Dev - Dungeon (6)
- **eventKey:** present on 1489 of 2353 records
- **Intervals:** median 4.66s (p5 0.00s / p95 45.43s, n=2352)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1489; [conversationId, dialogueEventType] x864
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2353/2353 records)
    numeric range 8 .. 114 (47 unique)
data.dialogueEventType  (string, 2353/2353 records)
    "DialogueNodeEvent"  x1489
    "DialogueStartEvent"  x438
    "DialogueFinishEvent"  x426
data.nodeId  (number, 1489/2353 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 436 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (222); Unit 2 Prod (Refactor) (107); Unit 3 Dev (57); Unit 1 Dev (50)
- **Intervals:** median 0.71s (p5 0.03s / p95 8.01s, n=435)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 436/436 records)
    "argumentationNodeHoverEnd"  x192
    "argumentationNodeHoverStart"  x190
    "argumentationNodeAdd"  x37
    "argumentationNodeRemove"  x17
data.argumentationTitle  (string, 436/436 records)
    "Unit 4 - Flooding"  x222
    "Unit 2 – Watershed"  x107
    "Unit 3 - Pollution Upstream"  x57
    "Unit 1 - Freshwater"  x35
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 436/436 records)
    "A"  x64
    "B"  x58
    "I"  x57
    "D"  x56
    "C"  x44
    "II"  x41
    "1"  x37
    "2"  x30
    "3"  x28
    "4"  x12
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 396 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (176); Unit 3 Dungeon Dev (81); Unit 2 Prod (Refactor) (61); Unit 4 Dev (39); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (11); Unit 1 Dev (10)
- **Intervals:** median 15.75s (p5 0.39s / p95 386.27s, n=395)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 396/396 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 396/396 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 96 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (28); Unit 2 Prod (Refactor) (23); Unit 4 Dev (15); Unit 1 Dev (12); Unit 3 Dev (9); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (4); Unit 5 Dev - Dungeon (1)
- **eventKey:** present on 96 of 96 records
- **Intervals:** median 281.61s (p5 0.01s / p95 64101.62s, n=95)
- **`data` key-set variants:** [questEventType, questID, questName] x57; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 96/96 records)
    "questActiveEvent"  x57
    "questFinishEvent"  x39
data.questID  (string, 96/96 records)
    28 unique values (see csv/event_unique_values.csv)
data.questName  (string, 96/96 records)
    28 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/96 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 88 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (66); Unit 4 Dev (12); Unit 3 Dev (10)
- **Intervals:** median 2.26s (p5 0.46s / p95 71.17s, n=87)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x78; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/88 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/88 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 78/88 records)
    "RightDrag"  x44
    "LeftDrag"  x34
data.currentSoilType  (string, 78/88 records)
    "SAND"  x20
    "CLAYSAND"  x17
    "SANDGRAVEL"  x16
    "CLAY"  x11
    "GRAVEL"  x7
    "CLAYROCK"  x6
    "BEDROCK"  x1
data.isCorrectSelection  (string, 78/88 records)
    "false"  x55
    "true"  x23
data.waterLevelStatus  (string, 78/88 records)
    "TooLow"  x42
    "TooHigh"  x19
    "Proper"  x17
data.waterRetentionChange  (string, 78/88 records)
    "Decrease"  x28
    "Increase"  x27
    "NoChange"  x23
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 77 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (43); Unit 2 Prod (Refactor) (31); Unit 3 Dungeon Dev (3)
- **Intervals:** median 6.68s (p5 1.40s / p95 37288.50s, n=76)
- **`data` key-set variants:** [actionType, featureUsed] x51; [actionType, featureUsed, location] x25; [actionType, featureUsed, legendName] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 77/77 records)
    "MapOpenEvent"  x26
    "MapCloseEvent"  x25
    "WaypointMoveEvent"  x14
    "WaypointSetEvent"  x9
    "WaypointResetEvent"  x2
    "Selected"  x1
data.featureUsed  (string, 77/77 records)
    "Map"  x51
    "Waypoint"  x25
    "Legend"  x1
data.legendName  (string, 1/77 records)
    "Water"  x1
data.location  (object, 25/77 records)
data.location.x  (number, 25/77 records)
    numeric range -332.065 .. 605.675 (21 unique)
data.location.y  (number, 25/77 records)
    numeric range -281.748 .. 341.205 (23 unique)
data.location.z  (number, 25/77 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 47 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (7); Unit 4 Dev - Dungeon (7); Unit 4 Dev (6); Unit 3 Dungeon Dev (3); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 571.34s (p5 9.24s / p95 86108.05s, n=46)
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "DebugMenuStateChanged"  x47
data.isOpened  (bool, 47/47 records)
    false  x47
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 29 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (11); Unit 4 Dev - Anderson Base (11); Unit 2 Prod (Refactor) (5); Unit 3 Dev (2)
- **Intervals:** median 13.82s (p5 0.25s / p95 276123.76s, n=28)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "submitAnswerEvent"  x29
data.answerSubmitted  (string, 29/29 records)
    "A,1,I"  x11
    "D,2,II"  x4
    "A,2,II"  x2
    "A,5,I"  x2
    "A,D,1,II"  x2
    "D,C,A,2,II"  x2
    "A,1,II"  x1
    "B,2,II"  x1
    "C,2,II"  x1
    "C,D,A,2,II"  x1
    "D,1,II"  x1
    "D,A,1,II"  x1
data.argumentationTitle  (string, 29/29 records)
    "Unit 4 - Flooding"  x11
    "Unit 1 - Freshwater"  x10
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 2 Prod (Refactor) (2); Unit 4 Dev - Dungeon (2); Unit 4 Dev (1)
- **Intervals:** median 3914.75s (p5 163.63s / p95 215527.02s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TerasGardenBox` — 23 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (23)
- **Intervals:** median 5.74s (p5 1.36s / p95 37.46s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records, 12 empty-string)
    ""  x12
    "cameraPlaced"  x11
data.boxId  (string, 23/23 records)
    "1"  x10
    "2"  x7
    "0"  x6
data.soilType  (string, 23/23 records)
    "Sand"  x13
    "Gravel"  x8
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 40.72s (p5 2.06s / p95 17369.49s, n=20)
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Clay"  x8
    "Gravel"  x6
    "Bedrock"  x4
    "Sand"  x3
data.floor  (string, 21/21 records)
    "5"  x14
    "4"  x4
    "3"  x3
data.machine  (string, 21/21 records)
    "1"  x18
    "2"  x3
data.row  (string, 21/21 records)
    "TopRow"  x15
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 22545.14s (p5 328.66s / p95 257584.68s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `chatEvent` — 19 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dungeon Dev (8); Unit 2 Prod (Refactor) (6); Unit 3 Dev (4); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 19.02s (p5 1.29s / p95 428102.75s, n=18)
- **`data` key-set variants:** [actionType, chatID] x16; [actionKey, chatID] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 3/19 records)
    "ScrollStop"  x3
data.actionType  (string, 16/19 records)
    "Close"  x7
    "Open"  x6
    "ScrollStart"  x3
data.chatID  (string, 19/19 records)
    "NA"  x10
    "[79-122, 79-125, 79-121, 79-123, 79-124]"  x2
    "[10-8, 10-10, 10-13, 10-15, 10-16]"  x1
    "[11-31, 11-25, 11-230, 11-29, 11-26]"  x1
    "[18-37, 18-38, 18-39, 18-269, 18-271, 18-273]"  x1
    "[68-1, 68-2, 68-5, 68-29, 18-41, 18-47]"  x1
    "[68-2, 68-5, 68-29, 18-41, 18-47]"  x1
    "[78-0, 78-3, 78-0, 78-7, 78-24]"  x1
    "[79-79, 79-80, 79-81, 79-83, 79-115]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dungeon Dev (8); Unit 2 Prod (Refactor) (6); Unit 3 Dev (4)
- **Intervals:** median 7.45s (p5 1.93s / p95 137443.32s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 18 empty-string)
    ""  x18
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 75.00s (p5 0.04s / p95 500929.71s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 15/15 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 4 - Flooding"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 58532.20s (p5 339.74s / p95 337973.02s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 4 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 207410.93s (p5 18590.26s / p95 634635.18s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "4"  x2
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x2
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

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `WaterChamberEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (66 records)
- `TerasGardenBox` data.actionType: "" (12x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (14x); "WaypointResetEvent" (2x); "WaypointSetEvent" (9x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (25x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (17x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*