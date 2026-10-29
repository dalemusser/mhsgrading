# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b72

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b72
- **Game version string(s) in log:** 2.8.9, 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b72.jsonl
- **Records:** 17132 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b72
- **Time span:** 2026-10-05T19:11:54.709000+00:00 .. 2026-10-19T16:11:33.879000+00:00 (332h 59m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b72\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 17132 records, 11 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 101 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5934 | 34.64 | 1 | 8 | 0 | 2026-10-06T18:31:37.870000+00:00 | 2026-10-19T16:08:41.902000+00:00 | 309h 37m |
| PuzzlePieceVisibleEvent | 4784 | 27.92 | 1 | 4 | 0 | 2026-10-06T19:15:59.018000+00:00 | 2026-10-19T16:01:43.735000+00:00 | 308h 45m |
| PlayerPositionEvent | 2819 | 16.45 | 1 | 9 | 0 | 2026-10-05T19:12:22.895000+00:00 | 2026-10-19T16:11:33.879000+00:00 | 332h 59m |
| DialogueEvent | 2087 | 12.18 | 1 | 9 | 1239 | 2026-10-05T19:12:42.911000+00:00 | 2026-10-19T16:10:35.290000+00:00 | 332h 57m |
| ObjectInterEvent | 551 | 3.22 | 1 | 8 | 0 | 2026-10-06T18:35:55.077000+00:00 | 2026-10-19T16:02:32.173000+00:00 | 309h 26m |
| argumentationNodeEvent | 421 | 2.46 | 1 | 3 | 0 | 2026-10-06T19:01:28.997000+00:00 | 2026-10-18T05:09:58.705000+00:00 | 274h 8m |
| questEvent | 88 | 0.51 | 1 | 8 | 88 | 2026-10-05T19:12:42.885000+00:00 | 2026-10-19T16:02:55.896000+00:00 | 332h 50m |
| TopographicMapEvent | 82 | 0.48 | 1 | 2 | 0 | 2026-10-06T19:16:55.235000+00:00 | 2026-10-16T01:56:18.457000+00:00 | 222h 39m |
| Soil Key Puzzle | 76 | 0.44 | 1 | 3 | 0 | 2026-10-13T18:39:34.554000+00:00 | 2026-10-16T18:33:11.668000+00:00 | 71h 53m |
| DEBUGMenu | 58 | 0.34 | 1 | 9 | 0 | 2026-10-05T19:12:22.878000+00:00 | 2026-10-19T15:57:26.777000+00:00 | 332h 45m |
| WaterChamberEvent | 55 | 0.32 | 1 | 1 | 0 | 2026-10-18T23:44:05.118000+00:00 | 2026-10-19T16:08:28.091000+00:00 | 16h 24m |
| argumentationAnswerEvent | 36 | 0.21 | 1 | 3 | 0 | 2026-10-06T19:01:21.798000+00:00 | 2026-10-18T05:10:04.869000+00:00 | 274h 8m |
| gameWindowFocusEvent | 36 | 0.21 | 1 | 7 | 0 | 2026-10-05T19:11:54.709000+00:00 | 2026-10-19T15:57:14.137000+00:00 | 332h 45m |
| gameStartEvent | 26 | 0.15 | 1 | 1 | 0 | 2026-10-05T19:11:54.710000+00:00 | 2026-10-19T15:57:14.137000+00:00 | 332h 45m |
| soilMachine | 21 | 0.12 | 1 | 1 | 0 | 2026-10-16T18:48:04.227000+00:00 | 2026-10-18T04:42:03.485000+00:00 | 33h 53m |
| gameWindowUnfocusEvent | 20 | 0.12 | 1 | 8 | 0 | 2026-10-05T19:16:40.201000+00:00 | 2026-10-18T23:29:33.963000+00:00 | 316h 12m |
| TerasGardenBox | 12 | 0.07 | 1 | 1 | 0 | 2026-10-18T05:23:18.352000+00:00 | 2026-10-18T05:25:22.884000+00:00 | 2m 4s |
| argumentationEvent | 10 | 0.06 | 1 | 3 | 0 | 2026-10-06T18:59:38.099000+00:00 | 2026-10-18T05:10:04.934000+00:00 | 274h 10m |
| crash | 5 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-10-06T19:06:30.041000+00:00 | 2026-10-18T05:43:29.843000+00:00 | 274h 36m |
| argumentationToolEvent | 3 | 0.02 | 1 | 1 | 0 | 2026-10-15T18:52:47.137000+00:00 | 2026-10-15T18:52:52.954000+00:00 | 5.8s |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-18T23:28:30.072000+00:00 | 2026-10-19T16:09:22.114000+00:00 | 16h 40m |
| DaniEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-16T01:52:16.780000+00:00 | 2026-10-16T01:52:18.733000+00:00 | 2.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 360.508s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 494309.901s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.069s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.827s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.639s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 14.688s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.909s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 30026.021s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6254.336s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2191.488s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 11191.274s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 25.087s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.8x vs baseline. 
  - Observed: 58 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
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
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: GRAVEL 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 30 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.2x vs baseline. 
  - Observed: 36 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,3,I; A,C,2,II; A,D,2,II; B,2,I; B,2,II; B,A,2,II; B,C,2,II; B,D,2,II; B,D,C,2,II; C,2,II; C,A,2,II; C,B,2,II; C,D,2,II; D,2,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 421 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 44; 45; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
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
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[197] _id=6ac5405ede269131f9b6ab75 ts=2026-10-06T18:39:25.3180000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[260] _id=6ac54171de269131f9b6ca29 ts=2026-10-06T18:44:01.3340000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[314] _id=6ac542c0de269131f9b6f573 ts=2026-10-06T18:49:35.9820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[5] _id=6ac3f67cde269131f9af6acb ts=2026-10-05T19:11:54.7100000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[53] _id=6ac53e7ede269131f9b675d1 ts=2026-10-06T18:31:26.2020000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[671] _id=6ac5470ede269131f9b75e93 ts=2026-10-06T19:07:57.6940000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 36 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 36} 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[0] _id=6ac3f67cde269131f9af6ac9 ts=2026-10-05T19:11:54.7090000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[55] _id=6ac53e7ede269131f9b675cf ts=2026-10-06T18:31:26.2010000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[670] _id=6ac5470ede269131f9b75e89 ts=2026-10-06T19:07:57.6890000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[54] _id=6ac53e7ede269131f9b675c9 ts=2026-10-05T19:16:40.201Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1308] _id=6ac693f9de269131f9be192b ts=2026-10-06T19:17:37.084Z`; `6ab9a9279a8420a1e6b56b72.jsonl[3029] _id=6ac7e59cde269131f9c58af6 ts=2026-10-07T19:17:15.572Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 7 of 82 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[1290] _id=6ac54927de269131f9b796d1 ts=2026-10-06T19:16:55.2350000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1301] _id=6ac54944de269131f9b79b3d ts=2026-10-06T19:17:24.1980000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1460] _id=6ac694e9de269131f9be4621 ts=2026-10-07T18:52:24.4220000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5933 | 0.0 | 0.692 | 187.869 | 13.094 | 429638.189 | 0.32 | 249 | 17 |
| PuzzlePieceVisibleEvent | 4783 | 0.0 | 0.069 | 232.395 | 2.204 | 517183.722 | 0.26 | 2088 | 14 |
| PlayerPositionEvent | 2803 | 0.0 | 10.003 | 341.888 | 10.118 | 429640.442 | 0.18 | 1 | 12 |
| DialogueEvent | 2086 | 0.0 | 5.139 | 574.627 | 58.051 | 429690.524 | 0.1 | 605 | 19 |
| ObjectInterEvent | 550 | 0.0 | 6.356 | 2025.449 | 245.355 | 517030.421 | 0.03 | 4 | 15 |
| argumentationNodeEvent | 420 | 0.006 | 0.524 | 2349.785 | 9.895 | 776975.266 | 0.03 | 45 | 2 |
| questEvent | 87 | 0.0 | 277.455 | 13772.563 | 84046.344 | 430989.079 | 0.0 | 19 | 25 |
| TopographicMapEvent | 81 | 0.02 | 4.639 | 9895.842 | 26018.55 | 516641.257 | 0.01 | 1 | 7 |
| Soil Key Puzzle | 75 | 0.151 | 1.827 | 3450.895 | 3534.603 | 87086.081 | 0.02 | 0 | 5 |
| DEBUGMenu | 57 | 4.737 | 360.508 | 21015.858 | 85451.855 | 431314.236 | 0.0 | 0 | 26 |
| WaterChamberEvent | 54 | 1.234 | 25.004 | 1093.759 | 171.854 | 56852.386 | 0.05 | 0 | 1 |
| argumentationAnswerEvent | 35 | 0.222 | 14.688 | 28197.802 | 62848.935 | 777051.38 | 0.0 | 0 | 2 |
| gameWindowFocusEvent | 35 | 28.292 | 2191.488 | 34226.269 | 97221.277 | 431325.06 | 0.0 | 0 | 23 |
| gameStartEvent | 25 | 68.607 | 6254.336 | 47916.777 | 115198.507 | 431325.06 | 0.0 | 0 | 21 |
| soilMachine | 20 | 0.755 | 25.087 | 6101.963 | 6343.645 | 120976.919 | 0.01 | 0 | 1 |
| gameWindowUnfocusEvent | 19 | 35.331 | 11191.274 | 59914.409 | 164292.697 | 516971.408 | 0.0 | 0 | 15 |
| TerasGardenBox | 11 | 1.496 | 4.42 | 11.321 | 36.12 | 46.145 | 5.3 | 0 | 0 |
| argumentationEvent | 9 | 0.049 | 53.217 | 109669.648 | 549861.327 | 776964.905 | 0.0 | 1 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 2 | 185990.025 | 494309.901 | 494309.901 | 771797.789 | 802629.777 | 0.0 | 0 | 2 |
| argumentationToolEvent | 2 | 2.685 | 2.909 | 2.909 | 3.11 | 3.132 | 20.63 | 0 | 0 |
| chatEvent | 2 | 715.502 | 30026.021 | 30026.021 | 56405.488 | 59336.54 | 0.0 | 0 | 2 |
| DaniEvent | 1 | 1.953 | 1.953 | 1.953 | 1.953 | 1.953 | 30.72 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 30 group(s), 110 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[2900] _id=6ac699a0de269131f9bf08b4 ts=2026-10-07T19:12:32.2580000Z == 6ab9a9279a8420a1e6b56b72.jsonl[2901] _id=6ac699a0de269131f9bf08b5 ts=2026-10-07T19:12:32.2580000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[3033] _id=6ac7e5abde269131f9c58bcf ts=2026-10-08T18:49:12.7100000Z == 6ab9a9279a8420a1e6b56b72.jsonl[3034] _id=6ac7e5abde269131f9c58bd0 ts=2026-10-08T18:49:12.7100000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[3035] _id=6ac7e5abde269131f9c58bd1 ts=2026-10-08T18:49:12.7110000Z == 6ab9a9279a8420a1e6b56b72.jsonl[3036] _id=6ac7e5abde269131f9c58bd2 ts=2026-10-08T18:49:12.7110000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 53 group(s), 82 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[1205] _id=6ac548f0de269131f9b78eb4 ts=2026-10-06T19:15:59.1880000Z == 6ab9a9279a8420a1e6b56b72.jsonl[1219] _id=6ac548f0de269131f9b78eb9 ts=2026-10-06T19:15:59.1880000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1221] _id=6ac548f1de269131f9b78ec4 ts=2026-10-06T19:15:59.2030000Z == 6ab9a9279a8420a1e6b56b72.jsonl[1213] _id=6ac548f2de269131f9b78ed9 ts=2026-10-06T19:15:59.2030000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1216] _id=6ac548f3de269131f9b78f2d ts=2026-10-06T19:16:01.7070000Z == 6ab9a9279a8420a1e6b56b72.jsonl[1229] _id=6ac548f3de269131f9b78f37 ts=2026-10-06T19:16:01.7070000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[4991] _id=6ace8355de269131f9d1b0da ts=? == 6ab9a9279a8420a1e6b56b72.jsonl[7113] _id=6acfd11fde269131f9d7d760 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 177 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6ab9a9279a8420a1e6b56b72.jsonl[140] _id=6ac53f8bde269131f9b691f2 ts=2026-10-06T18:35:55.0770000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[139] _id=6ac53f8bde269131f9b691f5 ts=2026-10-06T18:35:55.0860000Z`; `315ms: 6ab9a9279a8420a1e6b56b72.jsonl[816] _id=6ac54838de269131f9b774db ts=2026-10-06T19:12:55.9290000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[814] _id=6ac54838de269131f9b774e7 ts=2026-10-06T19:12:56.2440000Z`; `200ms: 6ab9a9279a8420a1e6b56b72.jsonl[814] _id=6ac54838de269131f9b774e7 ts=2026-10-06T19:12:56.2440000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[818] _id=6ac54838de269131f9b774f1 ts=2026-10-06T19:12:56.4440000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `712ms: 6ab9a9279a8420a1e6b56b72.jsonl[1213] _id=6ac548f2de269131f9b78ed9 ts=2026-10-06T19:15:59.2030000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[1188] _id=6ac548f2de269131f9b78ee1 ts=2026-10-06T19:15:59.9150000Z`; `683ms: 6ab9a9279a8420a1e6b56b72.jsonl[1226] _id=6ac548f3de269131f9b78f1b ts=2026-10-06T19:16:00.4850000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[1227] _id=6ac548f3de269131f9b78f1f ts=2026-10-06T19:16:01.1680000Z`; `510ms: 6ab9a9279a8420a1e6b56b72.jsonl[1227] _id=6ac548f3de269131f9b78f1f ts=2026-10-06T19:16:01.1680000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[1228] _id=6ac548f3de269131f9b78f25 ts=2026-10-06T19:16:01.6780000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `243ms: 6ab9a9279a8420a1e6b56b72.jsonl[3303] _id=6ac7e715de269131f9c5b7e1 ts=2026-10-08T18:55:16.6720000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[3304] _id=6ac7e715de269131f9c5b7e6 ts=2026-10-08T18:55:16.9150000Z`; `194ms: 6ab9a9279a8420a1e6b56b72.jsonl[3304] _id=6ac7e715de269131f9c5b7e6 ts=2026-10-08T18:55:16.9150000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[3300] _id=6ac7e715de269131f9c5b7f6 ts=2026-10-08T18:55:17.1090000Z`; `230ms: 6ab9a9279a8420a1e6b56b72.jsonl[3300] _id=6ac7e715de269131f9c5b7f6 ts=2026-10-08T18:55:17.1090000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[3305] _id=6ac7e715de269131f9c5b7fd ts=2026-10-08T18:55:17.3390000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `541ms: 6ab9a9279a8420a1e6b56b72.jsonl[510] _id=6ac54584de269131f9b72b4d ts=2026-10-06T19:01:23.6740000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[509] _id=6ac54584de269131f9b72b5f ts=2026-10-06T19:01:24.2150000Z`; `243ms: 6ab9a9279a8420a1e6b56b72.jsonl[509] _id=6ac54584de269131f9b72b5f ts=2026-10-06T19:01:24.2150000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[517] _id=6ac54584de269131f9b72b65 ts=2026-10-06T19:01:24.4580000Z`; `222ms: 6ab9a9279a8420a1e6b56b72.jsonl[517] _id=6ac54584de269131f9b72b65 ts=2026-10-06T19:01:24.4580000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[518] _id=6ac54585de269131f9b72b6b ts=2026-10-06T19:01:24.6800000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `60ms: 6ab9a9279a8420a1e6b56b72.jsonl[8452] _id=6ad12151de269131f9df78ca ts=2026-10-15T18:54:09.0550000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[8456] _id=6ad12151de269131f9df78cd ts=2026-10-15T18:54:09.1150000Z`; `49ms: 6ab9a9279a8420a1e6b56b72.jsonl[15034] _id=6ad454adde269131f9e89574 ts=2026-10-18T05:10:04.8850000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[15045] _id=6ad454adde269131f9e89577 ts=2026-10-18T05:10:04.9340000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `594ms: 6ab9a9279a8420a1e6b56b72.jsonl[8342] _id=6ad120cbde269131f9df68f0 ts=2026-10-15T18:51:55.5030000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[8355] _id=6ad120ccde269131f9df68fe ts=2026-10-15T18:51:56.0970000Z`; `834ms: 6ab9a9279a8420a1e6b56b72.jsonl[8358] _id=6ad120ccde269131f9df68f3 ts=2026-10-15T18:51:55.5640000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[8357] _id=6ad120ccde269131f9df6909 ts=2026-10-15T18:51:56.3980000Z`; `643ms: 6ab9a9279a8420a1e6b56b72.jsonl[8364] _id=6ad120d5de269131f9df69f6 ts=2026-10-15T18:52:04.6030000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[8367] _id=6ad120d5de269131f9df6a09 ts=2026-10-15T18:52:05.2460000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `755ms: 6ab9a9279a8420a1e6b56b72.jsonl[13459] _id=6ad2730ede269131f9e774eb ts=2026-10-16T18:55:09.2950000Z ~ 6ab9a9279a8420a1e6b56b72.jsonl[13460] _id=6ad2730fde269131f9e774fe ts=2026-10-16T18:55:10.0500000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b72.jsonl[3030] _id=6ac7e5a6de269131f9c58b80 ts=2026-10-08T18:49:10.2260000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3683] _id=6ace7a79de269131f9d0fe16 ts=2026-10-13T18:37:44.4620000Z; 33h 31m: 6ab9a9279a8420a1e6b56b72.jsonl[13578] _id=6ad273fade269131f9e785fb ts=2026-10-16T18:59:05.5880000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13628] _id=6ad44b6fde269131f9e887f7 ts=2026-10-18T04:30:39.1980000Z; 24h 0m: 6ab9a9279a8420a1e6b56b72.jsonl[1306] _id=6ac69408de269131f9be1bcf ts=2026-10-07T18:48:39.2640000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3025] _id=6ac7e59cde269131f9c58afd ts=2026-10-08T18:48:59.5890000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a9279a8420a1e6b56b72.jsonl[3669] _id=6ac7ec0ede269131f9c67e45 ts=2026-10-08T19:16:29.9960000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3703] _id=6ace7a8bde269131f9d1002e ts=2026-10-13T18:38:00.5200000Z; 33h 32m: 6ab9a9279a8420a1e6b56b72.jsonl[13568] _id=6ad273e1de269131f9e784e8 ts=2026-10-16T18:58:40.2140000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13670] _id=6ad44b7dde269131f9e88817 ts=2026-10-18T04:30:53.2880000Z; 23h 35m: 6ab9a9279a8420a1e6b56b72.jsonl[3023] _id=6ac69ab3de269131f9bf203f ts=2026-10-07T19:17:07.2070000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3247] _id=6ac7e65dde269131f9c5a234 ts=2026-10-08T18:52:13.2030000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 605 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[14716] _id=6ad4533ade269131f9e8910e ts=2026-10-18T05:03:54.1630000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14717] _id=6ad4533ade269131f9e8910f ts=2026-10-18T05:03:54.1630000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[14909] _id=6ad453fdde269131f9e893be ts=2026-10-18T05:07:09.6680000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14910] _id=6ad453fdde269131f9e893bf ts=2026-10-18T05:07:09.6680000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[14985] _id=6ad45463de269131f9e894ba ts=2026-10-18T05:08:50.7900000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14986] _id=6ad45463de269131f9e894bb ts=2026-10-18T05:08:50.7900000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 222h 57m 
  - Evidence: 222h 57m: 6ab9a9279a8420a1e6b56b72.jsonl[666] _id=6ac546b6de269131f9b74feb ts=2026-10-06T19:06:30.0410000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[11107] _id=6ad185fcde269131f9e2a397 ts=2026-10-16T02:03:39.8180000Z; 51h 39m: 6ab9a9279a8420a1e6b56b72.jsonl[11107] _id=6ad185fcde269131f9e2a397 ts=2026-10-16T02:03:39.8180000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[15498] _id=6ad45c82de269131f9e89e77 ts=2026-10-18T05:43:29.8430000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9279a8420a1e6b56b72.jsonl[3680] _id=6ac7ec42de269131f9c68563 ts=2026-10-08T19:17:22.3070000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3686] _id=6ace7a8bde269131f9d1001e ts=2026-10-13T18:38:00.4960000Z; 33h 31m: 6ab9a9279a8420a1e6b56b72.jsonl[13576] _id=6ad273fbde269131f9e78606 ts=2026-10-16T18:59:06.2150000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13645] _id=6ad44b7dde269131f9e887fe ts=2026-10-18T04:30:53.0710000Z; 23h 34m: 6ab9a9279a8420a1e6b56b72.jsonl[2989] _id=6ac69a31de269131f9bf13ef ts=2026-10-07T19:14:56.7280000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3032] _id=6ac7e5abde269131f9c58bce ts=2026-10-08T18:49:12.7090000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 249 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[10164] _id=6ad17eafde269131f9e28319 ts=2026-10-16T01:32:29.5310000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[10165] _id=6ad17eafde269131f9e2831a ts=2026-10-16T01:32:29.5310000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[10165] _id=6ad17eafde269131f9e2831a ts=2026-10-16T01:32:29.5310000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[10166] _id=6ad17eafde269131f9e2831b ts=2026-10-16T01:32:29.5310000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[10166] _id=6ad17eafde269131f9e2831b ts=2026-10-16T01:32:29.5310000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[10167] _id=6ad17eafde269131f9e2831c ts=2026-10-16T01:32:29.5310000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a9279a8420a1e6b56b72.jsonl[2787] _id=6ac69740de269131f9bec532 ts=2026-10-07T19:02:24.1370000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3728] _id=6ace7ae7de269131f9d1078e ts=2026-10-13T18:39:34.5580000Z; 33h 33m: 6ab9a9279a8420a1e6b56b72.jsonl[13561] _id=6ad273cade269131f9e78366 ts=2026-10-16T18:58:17.4720000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13678] _id=6ad44ba5de269131f9e8882f ts=2026-10-18T04:31:32.8480000Z; 23h 52m: 6ab9a9279a8420a1e6b56b72.jsonl[4180] _id=6ace7cb0de269131f9d12424 ts=2026-10-13T18:47:11.0890000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[5247] _id=6acfcc54de269131f9d74395 ts=2026-10-14T18:39:15.3680000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[14465] _id=6ad4511cde269131f9e88e67 ts=2026-10-18T04:54:52.0030000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14466] _id=6ad4511cde269131f9e88e68 ts=2026-10-18T04:54:52.0030000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[14510] _id=6ad45196de269131f9e88ecb ts=2026-10-18T04:56:54.3030000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14511] _id=6ad45196de269131f9e88ecc ts=2026-10-18T04:56:54.3030000Z; 5ms: 6ab9a9279a8420a1e6b56b72.jsonl[12203] _id=6ad2574dde269131f9e643cf ts=2026-10-16T16:56:44.8490000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[12205] _id=6ad2574dde269131f9e643d4 ts=2026-10-16T16:56:44.8540000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9279a8420a1e6b56b72.jsonl[3677] _id=6ac7ec3bde269131f9c68498 ts=2026-10-08T19:17:15.3130000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3685] _id=6ace7a8bde269131f9d1001d ts=2026-10-13T18:37:55.7550000Z; 23h 31m: 6ab9a9279a8420a1e6b56b72.jsonl[3024] _id=6ac69ab9de269131f9bf2082 ts=2026-10-07T19:17:13.2730000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3031] _id=6ac7e5abde269131f9c58bcd ts=2026-10-08T18:49:10.2380000Z; 23h 31m: 6ab9a9279a8420a1e6b56b72.jsonl[1303] _id=6ac54948de269131f9b79b97 ts=2026-10-06T19:17:28.4040000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[1312] _id=6ac6940bde269131f9be1cf0 ts=2026-10-07T18:48:39.2820000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[7487] _id=6ad0dc2fde269131f9db6557 ts=2026-10-15T13:59:11.5350000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[7488] _id=6ad0e67fde269131f9dbc424 ts=2026-10-15T13:59:11.535Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 143h 39m 
  - Evidence: 143h 39m: 6ab9a9279a8420a1e6b56b72.jsonl[2777] _id=6ac69723de269131f9bec206 ts=2026-10-07T19:01:54.6260000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3776] _id=6ace7b63de269131f9d10dae ts=2026-10-13T18:41:38.3480000Z; 34h 8m: 6ab9a9279a8420a1e6b56b72.jsonl[12912] _id=6ad26e57de269131f9e71111 ts=2026-10-16T18:35:01.2620000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13784] _id=6ad44e72de269131f9e88add ts=2026-10-18T04:43:28.8070000Z; 24h 9m: 6ab9a9279a8420a1e6b56b72.jsonl[6920] _id=6acfcf04de269131f9d79f22 ts=2026-10-14T18:50:42.4330000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[8664] _id=6ad122a3de269131f9dfa6f5 ts=2026-10-15T18:59:46.4340000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2088 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[10142] _id=6ad17eb0de269131f9e28325 ts=2026-10-16T01:32:29.5590000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[10169] _id=6ad17eb0de269131f9e28327 ts=2026-10-16T01:32:29.5590000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[10143] _id=6ad17eb0de269131f9e2832d ts=2026-10-16T01:32:31.2320000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[10172] _id=6ad17eb0de269131f9e2832f ts=2026-10-16T01:32:31.2320000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[10146] _id=6ad17eb2de269131f9e28337 ts=2026-10-16T01:32:32.8500000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[10147] _id=6ad17eb2de269131f9e28339 ts=2026-10-16T01:32:32.8500000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 24h 11m 
  - Evidence: 24h 11m: 6ab9a9279a8420a1e6b56b72.jsonl[3760] _id=6ace7b24de269131f9d10ae1 ts=2026-10-13T18:40:35.1950000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[6957] _id=6acfcf52de269131f9d7a55e ts=2026-10-14T18:52:01.2760000Z; 24h 6m: 6ab9a9279a8420a1e6b56b72.jsonl[6961] _id=6acfcf55de269131f9d7a596 ts=2026-10-14T18:52:04.2760000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[8619] _id=6ad12244de269131f9df9aaf ts=2026-10-15T18:58:11.6200000Z; 21h 10m: 6ab9a9279a8420a1e6b56b72.jsonl[8639] _id=6ad1226ede269131f9dfa063 ts=2026-10-15T18:58:54.1790000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[11336] _id=6ad24c44de269131f9e5a1af ts=2026-10-16T16:09:39.9500000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a9279a8420a1e6b56b72.jsonl[3534] _id=6ac7ea74de269131f9c65002 ts=2026-10-08T19:09:40.0210000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[5272] _id=6acfcc97de269131f9d74d95 ts=2026-10-14T18:40:21.2780000Z; 24h 2m: 6ab9a9279a8420a1e6b56b72.jsonl[1479] _id=6ac69508de269131f9be4cae ts=2026-10-07T18:52:55.2740000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3292] _id=6ac7e710de269131f9c5b73e ts=2026-10-08T18:55:12.2770000Z; 23h 35m: 6ab9a9279a8420a1e6b56b72.jsonl[1301] _id=6ac54944de269131f9b79b3d ts=2026-10-06T19:17:24.1980000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[1460] _id=6ac694e9de269131f9be4621 ts=2026-10-07T18:52:24.4220000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.020s..0.020s shown 
  - Evidence: 20ms: 6ab9a9279a8420a1e6b56b72.jsonl[3294] _id=6ac7e715de269131f9c5b7dc ts=2026-10-08T18:55:16.4110000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3298] _id=6ac7e715de269131f9c5b7e0 ts=2026-10-08T18:55:16.4310000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 15h 47m 
  - Evidence: 15h 47m: 6ab9a9279a8420a1e6b56b72.jsonl[16485] _id=6ad55ff0de269131f9e8f294 ts=2026-10-19T00:10:24.5950000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[16584] _id=6ad63e05de269131f9e98b4a ts=2026-10-19T15:57:56.9810000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 50m 
  - Evidence: 215h 50m: 6ab9a9279a8420a1e6b56b72.jsonl[534] _id=6ac545acde269131f9b72e5b ts=2026-10-06T19:02:04.5010000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[8414] _id=6ad12108de269131f9df7054 ts=2026-10-15T18:52:55.8810000Z; 58h 7m: 6ab9a9279a8420a1e6b56b72.jsonl[8415] _id=6ad12151de269131f9df78c1 ts=2026-10-15T18:54:09.0340000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14635] _id=6ad452c8de269131f9e89004 ts=2026-10-18T05:02:00.0320000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 49m 
  - Evidence: 215h 49m: 6ab9a9279a8420a1e6b56b72.jsonl[526] _id=6ac545adde269131f9b72e5d ts=2026-10-06T19:02:04.5470000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[8321] _id=6ad120b1de269131f9df65f2 ts=2026-10-15T18:51:29.4520000Z; 58h 6m: 6ab9a9279a8420a1e6b56b72.jsonl[8456] _id=6ad12151de269131f9df78cd ts=2026-10-15T18:54:09.1150000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14573] _id=6ad45287de269131f9e88f5a ts=2026-10-18T05:00:55.0760000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.049s..0.049s shown 
  - Evidence: 49ms: 6ab9a9279a8420a1e6b56b72.jsonl[15034] _id=6ad454adde269131f9e89574 ts=2026-10-18T05:10:04.8850000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[15045] _id=6ad454adde269131f9e89577 ts=2026-10-18T05:10:04.9340000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 49m 
  - Evidence: 215h 49m: 6ab9a9279a8420a1e6b56b72.jsonl[533] _id=6ac545a4de269131f9b72de1 ts=2026-10-06T19:01:56.4330000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[8323] _id=6ad120b4de269131f9df6634 ts=2026-10-15T18:51:31.6990000Z; 58h 6m: 6ab9a9279a8420a1e6b56b72.jsonl[8463] _id=6ad1214fde269131f9df7846 ts=2026-10-15T18:54:07.0400000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14536] _id=6ad45280de269131f9e88f50 ts=2026-10-18T05:00:48.3400000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 45 interval(s) ≤ 0.006s..0.018s shown 
  - Evidence: 6ms: 6ab9a9279a8420a1e6b56b72.jsonl[14778] _id=6ad45375de269131f9e8918a ts=2026-10-18T05:04:53.6500000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14764] _id=6ad45376de269131f9e8918c ts=2026-10-18T05:04:53.6560000Z; 9ms: 6ab9a9279a8420a1e6b56b72.jsonl[8398] _id=6ad120f2de269131f9df6e40 ts=2026-10-15T18:52:34.2390000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[8399] _id=6ad120f2de269131f9df6e43 ts=2026-10-15T18:52:34.2480000Z; 18ms: 6ab9a9279a8420a1e6b56b72.jsonl[14764] _id=6ad45376de269131f9e8918c ts=2026-10-18T05:04:53.6560000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[14765] _id=6ad45376de269131f9e8918d ts=2026-10-18T05:04:53.6740000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 16h 28m 
  - Evidence: 16h 28m: 6ab9a9279a8420a1e6b56b72.jsonl[15509] _id=6ad5561ede269131f9e8ddbb ts=2026-10-18T23:28:30.0720000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[16573] _id=6ad63de7de269131f9e98a64 ts=2026-10-19T15:57:26.6120000Z; 11m 55s: 6ab9a9279a8420a1e6b56b72.jsonl[16573] _id=6ad63de7de269131f9e98a64 ts=2026-10-19T15:57:26.6120000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[17105] _id=6ad640b3de269131f9e9a23b ts=2026-10-19T16:09:22.1140000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b72.jsonl[3027] _id=6ac7e59cde269131f9c58aff ts=2026-10-08T18:48:59.7320000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3682] _id=6ace7a79de269131f9d0fe1e ts=2026-10-13T18:37:44.7920000Z; 33h 59m: 6ab9a9279a8420a1e6b56b72.jsonl[12459] _id=6ad26d5bde269131f9e70241 ts=2026-10-16T18:30:49.9360000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13630] _id=6ad44b6fde269131f9e887f9 ts=2026-10-18T04:30:39.3350000Z; 24h 0m: 6ab9a9279a8420a1e6b56b72.jsonl[1311] _id=6ac693f9de269131f9be193d ts=2026-10-07T18:48:24.7930000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3027] _id=6ac7e59cde269131f9c58aff ts=2026-10-08T18:48:59.7320000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b72.jsonl[3026] _id=6ac7e59cde269131f9c58afe ts=2026-10-08T18:48:59.7320000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3681] _id=6ace7a79de269131f9d0fe1d ts=2026-10-13T18:37:44.7920000Z; 33h 59m: 6ab9a9279a8420a1e6b56b72.jsonl[12458] _id=6ad26d5bde269131f9e70240 ts=2026-10-16T18:30:49.9360000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13629] _id=6ad44b6fde269131f9e887f8 ts=2026-10-18T04:30:39.3350000Z; 24h 0m: 6ab9a9279a8420a1e6b56b72.jsonl[1310] _id=6ac693f9de269131f9be193c ts=2026-10-07T18:48:24.7930000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3026] _id=6ac7e59cde269131f9c58afe ts=2026-10-08T18:48:59.7320000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 143h 36m 
  - Evidence: 143h 36m: 6ab9a9279a8420a1e6b56b72.jsonl[3029] _id=6ac7e59cde269131f9c58af6 ts=2026-10-07T19:17:15.572Z -> 6ab9a9279a8420a1e6b56b72.jsonl[4374] _id=6ace7e28de269131f9d13012 ts=2026-10-13T18:53:26.9800000Z; 34h 45m: 6ab9a9279a8420a1e6b56b72.jsonl[13627] _id=6ad44b6fde269131f9e887f5 ts=2026-10-16T18:59:18Z -> 6ab9a9279a8420a1e6b56b72.jsonl[15494] _id=6ad45cb8de269131f9e89e7b ts=2026-10-18T05:44:24.1730000Z; 24h 0m: 6ab9a9279a8420a1e6b56b72.jsonl[54] _id=6ac53e7ede269131f9b675c9 ts=2026-10-05T19:16:40.201Z -> 6ab9a9279a8420a1e6b56b72.jsonl[1308] _id=6ac693f9de269131f9be192b ts=2026-10-06T19:17:37.084Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a9279a8420a1e6b56b72.jsonl[3286] _id=6ac7e6fbde269131f9c5b4ea ts=2026-10-08T18:54:51.4900000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[3705] _id=6ace7a8bde269131f9d10030 ts=2026-10-13T18:38:00.5690000Z; 33h 37m: 6ab9a9279a8420a1e6b56b72.jsonl[13406] _id=6ad272aede269131f9e76e51 ts=2026-10-16T18:53:33.4340000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13669] _id=6ad44b7dde269131f9e88816 ts=2026-10-18T04:30:53.1160000Z; 23h 38m: 6ab9a9279a8420a1e6b56b72.jsonl[714] _id=6ac5479fde269131f9b7693a ts=2026-10-06T19:10:23.0570000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[1313] _id=6ac6940bde269131f9be1cf1 ts=2026-10-07T18:48:41.8380000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[16840] _id=6ad63f30de269131f9e995a6 ts=2026-10-19T16:02:55.8960000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[16841] _id=6ad63f30de269131f9e995a7 ts=2026-10-19T16:02:55.8960000Z; 0ms: 6ab9a9279a8420a1e6b56b72.jsonl[7197] _id=6acfd1e6de269131f9d7f10c ts=2026-10-14T19:03:01.1030000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[7198] _id=6acfd1e6de269131f9d7f10d ts=2026-10-14T19:03:01.1030000Z; 1ms: 6ab9a9279a8420a1e6b56b72.jsonl[13112] _id=6ad27070de269131f9e7413d ts=2026-10-16T18:43:59.8380000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13113] _id=6ad27070de269131f9e7413e ts=2026-10-16T18:43:59.8390000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 33h 36m 
  - Evidence: 33h 36m: 6ab9a9279a8420a1e6b56b72.jsonl[13557] _id=6ad273c6de269131f9e78300 ts=2026-10-16T18:58:13.6150000Z -> 6ab9a9279a8420a1e6b56b72.jsonl[13589] _id=6ad44c56de269131f9e888df ts=2026-10-18T04:34:30.5340000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[543] _id=6ac545d7de269131f9b73153 ts=2026-10-06T19:02:47.2660000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[4400] _id=6ace80fede269131f9d153f0 ts=2026-10-13T19:05:33.8210000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[7872] _id=6ad11e51de269131f9df1605 ts=2026-10-15T18:41:20.6020000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[1222] _id=6ac548f2de269131f9b78f01 ts=2026-10-06T19:16:00.2530000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1227] _id=6ac548f3de269131f9b78f1f ts=2026-10-06T19:16:01.1680000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1228] _id=6ac548f3de269131f9b78f25 ts=2026-10-06T19:16:01.6780000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[8456] _id=6ad12151de269131f9df78cd ts=2026-10-15T18:54:09.1150000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[15045] _id=6ad454adde269131f9e89577 ts=2026-10-18T05:10:04.9340000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[15509] _id=6ad5561ede269131f9e8ddbb ts=2026-10-18T23:28:30.0720000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[16573] _id=6ad63de7de269131f9e98a64 ts=2026-10-19T15:57:26.6120000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[17105] _id=6ad640b3de269131f9e9a23b ts=2026-10-19T16:09:22.1140000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[13674] _id=6ad44b95de269131f9e88822 ts=2026-10-18T04:31:17.3190000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[16826] _id=6ad63f30de269131f9e995a3 ts=2026-10-19T16:02:55.8470000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[16839] _id=6ad63f30de269131f9e995a5 ts=2026-10-19T16:02:55.8670000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[4991] _id=6ace8355de269131f9d1b0da ts=?`; `6ab9a9279a8420a1e6b56b72.jsonl[5185] _id=6acfcb8dde269131f9d729b9 ts=?`; `6ab9a9279a8420a1e6b56b72.jsonl[7113] _id=6acfd11fde269131f9d7d760 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 119 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[3960] _id=6ace7c4dde269131f9d11c29 ts=2026-10-13T18:45:31.0510000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[3966] _id=6ace7c4fde269131f9d11c3a ts=2026-10-13T18:45:31.2500000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[4008] _id=6ace7c60de269131f9d11d63 ts=2026-10-13T18:45:48.6750000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 751 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[1205] _id=6ac548f0de269131f9b78eb4 ts=2026-10-06T19:15:59.1880000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1219] _id=6ac548f0de269131f9b78eb9 ts=2026-10-06T19:15:59.1880000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1213] _id=6ac548f2de269131f9b78ed9 ts=2026-10-06T19:15:59.2030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[8412] _id=6ad12105de269131f9df7017 ts=2026-10-15T18:52:52.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 431 start, 417 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'BecameCameraCentered' (totals: 877 open, 873 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 32 unmatched 'BecameVisible' (totals: 1526 open, 1508 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 3 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'questActiveEvent' (totals: 54 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 406 of 17126 adjacent _id pairs reverse in client time; worst 196.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b72.jsonl[1510] _id=6ac69575de269131f9be6922 ts=2026-10-07T18:54:44.7200000Z`; `6ab9a9279a8420a1e6b56b72.jsonl[1528] _id=6ac69576de269131f9be695b ts=2026-10-07T18:51:27.8850000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.87s, min -120681.49s, max -0.21s over 17127 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b72\coverage.yaml

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
  - Observed: 5 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5934 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1923); Unit 3 Dungeon Dev (895); Unit 5 Dev - Dungeon (811); Unit 4 Dev (766); Unit 4 Dev - Dungeon (698); Unit 3 Dev (586); Unit 1 Dev (162); Unit 4 Dev - Anderson Base (93)
- **Intervals:** median 0.69s (p5 0.07s / p95 13.09s, n=5933)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5934/5934 records)
    "pressed"  x5934
data.actionType  (string, 5934/5934 records)
    "Move"  x2622
    "Jump"  x2020
    "Interact"  x978
    "Hoverboard"  x200
    "Sprint"  x57
    "Ascend"  x30
    "Map"  x19
    "SkipCinematic"  x3
    "ToggleDebug"  x3
    "Pause"  x2
data.key  (string, 5934/5934 records, 13 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5934/5934 records)
    "Player"  x5550
    "Drone"  x384
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4784 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3172); Unit 4 Dev (782); Unit 3 Dungeon Dev (560); Unit 5 Dev - Dungeon (270)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.20s, n=4783)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4784/4784 records)
    "BecameVisible"  x1526
    "BecameInvisible"  x1508
    "BecameCameraCentered"  x877
    "BecameCameraUncentered"  x873
data.pieceId  (string, 4784/4784 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4784/4784 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2819 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (777); Unit 3 Dev (377); Unit 4 Dev (376); Unit 3 Dungeon Dev (334); Unit 5 Dev - Dungeon (323); Unit 4 Dev - Dungeon (267); Unit 1 Dev (235); Unit 4 Dev - Anderson Base (116); Unit 5 Dev (14)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=2803)
- **Fields under `data`:**

```text
data.position  (object, 2819/2819 records)
data.position.x  (number, 2819/2819 records)
    numeric range -679.521 .. 1550.99 (1135 unique)
data.position.y  (number, 2819/2819 records)
    numeric range -115.127 .. 226.251 (695 unique)
data.position.z  (number, 2819/2819 records)
    numeric range -1090.63 .. 1805.82 (1132 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2087 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (501); Unit 3 Dev (387); Unit 4 Dev (311); Unit 3 Dungeon Dev (237); Unit 1 Dev (209); Unit 4 Dev - Dungeon (171); Unit 4 Dev - Anderson Base (153); Unit 5 Dev - Dungeon (114); Unit 5 Dev (4)
- **eventKey:** present on 1239 of 2087 records
- **Intervals:** median 5.14s (p5 0.00s / p95 58.05s, n=2086)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1239; [conversationId, dialogueEventType] x848
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2087/2087 records)
    numeric range 10 .. 116 (46 unique)
data.dialogueEventType  (string, 2087/2087 records)
    "DialogueNodeEvent"  x1239
    "DialogueStartEvent"  x431
    "DialogueFinishEvent"  x417
data.nodeId  (number, 1239/2087 records)
    numeric range 0 .. 289 (209 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 551 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (219); Unit 4 Dev - Dungeon (159); Unit 3 Dungeon Dev (94); Unit 4 Dev (29); Unit 5 Dev - Dungeon (17); Unit 3 Dev (13); Unit 1 Dev (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 6.36s (p5 0.14s / p95 245.36s, n=550)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 551/551 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 551/551 records)
    95 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 421 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (301); Unit 3 Dev (107); Unit 1 Dev (13)
- **Intervals:** median 0.52s (p5 0.03s / p95 9.89s, n=420)
- **Fields under `data`:**

```text
data.actionType  (string, 421/421 records)
    "argumentationNodeHoverEnd"  x176
    "argumentationNodeHoverStart"  x176
    "argumentationNodeAdd"  x40
    "argumentationNodeRemove"  x29
data.argumentationTitle  (string, 421/421 records)
    "Unit 4 - Flooding"  x301
    "Unit 3 - Pollution Upstream"  x107
    "Unit 1 - Freshwater"  x13
data.nodeName  (string, 421/421 records)
    "B"  x92
    "A"  x61
    "C"  x57
    "D"  x45
    "3"  x40
    "I"  x30
    "2"  x29
    "II"  x25
    "4"  x22
    "1"  x17
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 88 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 4 Dev - Dungeon (15); Unit 1 Dev (13); Unit 5 Dev - Dungeon (12); Unit 3 Dev (10); Unit 4 Dev (10); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 88 of 88 records
- **Intervals:** median 277.45s (p5 0.00s / p95 84046.34s, n=87)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 88/88 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x34
data.questID  (string, 88/88 records)
    29 unique values (see csv/event_unique_values.csv)
data.questName  (string, 88/88 records)
    29 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/88 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 82 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (51); Unit 3 Dev (31)
- **Intervals:** median 4.64s (p5 0.17s / p95 26018.55s, n=81)
- **`data` key-set variants:** [actionType, featureUsed] x50; [actionType, featureUsed, location] x25; [actionType, featureUsed, legendName] x7
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 82/82 records)
    "MapCloseEvent"  x25
    "MapOpenEvent"  x25
    "WaypointMoveEvent"  x21
    "Selected"  x6
    "WaypointSetEvent"  x3
    "Unselected"  x1
    "WaypointResetEvent"  x1
data.featureUsed  (string, 82/82 records)
    "Map"  x50
    "Waypoint"  x25
    "Legend"  x7
data.legendName  (string, 7/82 records)
    "0 ft"  x2
    "90 ft"  x2
    "150 ft"  x1
    "30 ft"  x1
    "360 ft"  x1
data.location  (object, 25/82 records)
data.location.x  (number, 25/82 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 25/82 records)
    numeric range -162.109 .. 121.884 (14 unique)
data.location.z  (number, 25/82 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 76 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (42); Unit 2 Prod (Refactor) (18); Unit 3 Dev (16)
- **Intervals:** median 1.83s (p5 0.41s / p95 3534.60s, n=75)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x64; [Soil Key Puzzle Status, Unit] x12
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/76 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/76 records)
    "Unit 4 Dev"  x6
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 64/76 records)
    "RightDrag"  x35
    "LeftDrag"  x29
data.currentSoilType  (string, 64/76 records)
    "CLAYSAND"  x20
    "CLAY"  x16
    "SAND"  x15
    "CLAYROCK"  x8
    "SANDGRAVEL"  x4
    "BEDROCK"  x1
data.isCorrectSelection  (string, 64/76 records)
    "false"  x40
    "true"  x24
data.waterLevelStatus  (string, 64/76 records)
    "TooHigh"  x30
    "Proper"  x20
    "TooLow"  x14
data.waterRetentionChange  (string, 64/76 records)
    "NoChange"  x24
    "Increase"  x22
    "Decrease"  x18
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 58 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (23); Unit 2 Prod (Refactor) (11); Unit 3 Dev (7); Unit 4 Dev (6); Unit 3 Dungeon Dev (3); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 360.51s (p5 8.46s / p95 85451.85s, n=57)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 58/58 records)
    "DebugMenuStateChanged"  x58
data.isOpened  (bool, 58/58 records)
    false  x58
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 55 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (55)
- **Intervals:** median 25.00s (p5 2.20s / p95 171.85s, n=54)
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "On"  x37
    "Off"  x18
data.floor  (string, 55/55 records)
    "4"  x28
    "3"  x19
    "1"  x4
    "2"  x4
data.machineNumber  (string, 55/55 records)
    "One"  x51
    "Two"  x4
data.machineType  (string, 55/55 records)
    "Condenser"  x30
    "Evaporator"  x17
    "DualChamber_Condenser"  x5
    "VentSwitch"  x3
data.room  (string, 55/55 records)
    "3"  x24
    "2"  x16
    "4"  x8
    "1"  x7
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 36 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (21); Unit 1 Dev (11); Unit 3 Dev (4)
- **Intervals:** median 14.69s (p5 0.23s / p95 62848.94s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "submitAnswerEvent"  x36
data.answerSubmitted  (string, 36/36 records, 10 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 36/36 records)
    "Unit 4 - Flooding"  x21
    "Unit 1 - Freshwater"  x11
    "Unit 3 - Pollution Upstream"  x4
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 36 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (26); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 4 Dev (2); Transition (1); Unit 3 Dungeon Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 2191.49s (p5 78.35s / p95 97221.28s, n=35)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 36/36 records)
    true  x36
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 26 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (26)
- **Intervals:** median 6254.34s (p5 226.04s / p95 115198.51s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 25.09s (p5 2.17s / p95 6343.65s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Bedrock"  x7
    "Clay"  x7
    "Gravel"  x5
    "Sand"  x2
data.floor  (string, 21/21 records)
    "5"  x15
    "4"  x4
    "3"  x2
data.machine  (string, 21/21 records)
    "1"  x19
    "2"  x2
data.row  (string, 21/21 records)
    "TopRow"  x16
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 20 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (7); Unit 2 Prod (Refactor) (4); Unit 4 Dev (3); Unit 3 Dungeon Dev (2); Transition (1); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 11191.27s (p5 81.22s / p95 164292.70s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    false  x20
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 12 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (12)
- **Intervals:** median 4.42s (p5 1.54s / p95 36.12s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x5
data.boxId  (string, 12/12 records)
    "0"  x8
    "1"  x2
    "2"  x2
data.soilType  (string, 12/12 records)
    "Clay"  x8
    "Sand"  x3
    "Gravel"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 53.22s (p5 0.05s / p95 549861.33s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 10/10 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 10/10 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x1
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 4 empty-string)
    ""  x4
    "TypeError: Permissions check failed"  x1
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit2"  x4
    "unit3"  x1
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 494309.90s (p5 216822.01s / p95 771797.79s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (3)
- **Intervals:** median 2.91s (p5 2.71s / p95 3.11s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationToolOpen"  x3
data.argumentationTitle  (string, 3/3 records)
    "Unit 3 - Pollution Upstream"  x3
data.toolName  (string, 3/3 records)
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 30026.02s (p5 3646.55s / p95 56405.49s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 1.95s (p5 1.95s / p95 1.95s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

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
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TerasGardenBox` data.actionType: "" (7x)
- `TopographicMapEvent` data.actionType: "Selected" (6x); "Unselected" (1x); "WaypointMoveEvent" (21x); "WaypointResetEvent" (1x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (7x); "Waypoint" (25x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (29x)
- `soilMachine` data.canisterType: "Bedrock" (7x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*