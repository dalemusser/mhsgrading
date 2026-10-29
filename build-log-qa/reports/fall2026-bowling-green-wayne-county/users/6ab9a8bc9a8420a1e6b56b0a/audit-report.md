# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b0a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b0a
- **Game version string(s) in log:** 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b0a.jsonl
- **Records:** 11229 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b0a
- **Time span:** 2026-10-05T15:07:28.402000+00:00 .. 2026-10-16T15:48:02.260000+00:00 (264h 40m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b0a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 11229 records, 8 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 103 INFO, 2 NOT_TESTED, 82 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3818 | 34.0 | 1 | 7 | 0 | 2026-10-05T15:16:23.824000+00:00 | 2026-10-16T15:47:56.479000+00:00 | 264h 31m |
| PuzzlePieceVisibleEvent | 2913 | 25.94 | 1 | 3 | 0 | 2026-10-06T15:27:17.942000+00:00 | 2026-10-16T15:26:32.284000+00:00 | 239h 59m |
| DialogueEvent | 1883 | 16.77 | 1 | 7 | 1192 | 2026-10-05T15:16:24.400000+00:00 | 2026-10-16T15:47:58.846000+00:00 | 264h 31m |
| PlayerPositionEvent | 1604 | 14.28 | 1 | 7 | 0 | 2026-10-05T15:16:04.487000+00:00 | 2026-10-16T15:48:02.260000+00:00 | 264h 31m |
| argumentationNodeEvent | 361 | 3.21 | 1 | 4 | 0 | 2026-10-05T15:38:40.879000+00:00 | 2026-10-16T15:42:03.112000+00:00 | 264h 3m |
| ObjectInterEvent | 244 | 2.17 | 1 | 7 | 0 | 2026-10-05T15:22:12.782000+00:00 | 2026-10-16T15:47:12.262000+00:00 | 264h 24m |
| TopographicMapEvent | 79 | 0.7 | 1 | 2 | 0 | 2026-10-06T15:27:38.415000+00:00 | 2026-10-15T15:13:21.811000+00:00 | 215h 45m |
| Soil Key Puzzle | 74 | 0.66 | 1 | 3 | 0 | 2026-10-07T15:41:17.352000+00:00 | 2026-10-15T15:25:06.155000+00:00 | 191h 43m |
| questEvent | 65 | 0.58 | 1 | 7 | 65 | 2026-10-05T15:16:24.372000+00:00 | 2026-10-16T15:47:51.964000+00:00 | 264h 31m |
| argumentationAnswerEvent | 61 | 0.54 | 1 | 4 | 0 | 2026-10-05T15:38:57.536000+00:00 | 2026-10-16T15:42:08.634000+00:00 | 264h 3m |
| DEBUGMenu | 29 | 0.26 | 1 | 8 | 0 | 2026-10-05T15:16:04.450000+00:00 | 2026-10-16T15:47:50.404000+00:00 | 264h 31m |
| soilMachine | 23 | 0.2 | 1 | 1 | 0 | 2026-10-16T15:11:15.630000+00:00 | 2026-10-16T15:22:23.172000+00:00 | 11m 7s |
| gameWindowFocusEvent | 18 | 0.16 | 1 | 3 | 0 | 2026-10-05T15:07:28.402000+00:00 | 2026-10-16T15:47:41.605000+00:00 | 264h 40m |
| gameStartEvent | 13 | 0.12 | 1 | 1 | 0 | 2026-10-05T15:07:28.404000+00:00 | 2026-10-16T15:47:41.605000+00:00 | 264h 40m |
| argumentationEvent | 12 | 0.11 | 1 | 4 | 0 | 2026-10-05T15:38:34.801000+00:00 | 2026-10-16T15:42:08.685000+00:00 | 264h 3m |
| gameWindowUnfocusEvent | 10 | 0.09 | 1 | 4 | 0 | 2026-10-06T15:47:33.758000+00:00 | 2026-10-16T15:47:23.419000+00:00 | 239h 59m |
| argumentationToolEvent | 9 | 0.08 | 1 | 2 | 0 | 2026-10-05T15:38:33.006000+00:00 | 2026-10-13T15:30:58.983000+00:00 | 191h 52m |
| DaniEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-10-07T15:24:22.410000+00:00 | 2026-10-14T15:08:38.073000+00:00 | 167h 44m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-05T15:43:42.344000+00:00 | 2026-10-15T15:18:44.892000+00:00 | 239h 35m |
| TerasGardenBox | 3 | 0.03 | 1 | 1 | 0 | 2026-10-16T15:46:10.565000+00:00 | 2026-10-16T15:46:59.205000+00:00 | 48.6s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 431251.274s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.62s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.044s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 24.32s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.907s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.137s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.396s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84740.706s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2259.28s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86295.536s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.605s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 11 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 12.2x vs baseline. 
  - Observed: 61 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 2,II; A,2,I; A,2,II; A,3,I; A,4,I; B,2,I; B,2,II; B,3,I; B,3,II; C,2,II; C,D,A,2,II; D,1,II; D,2,II; D,3,II; D,4,II; D,C,2,II 
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
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 10 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.6x vs baseline. 
  - Observed: 23 records 
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
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[171] _id=6ac3c117de269131f9ad1d61 ts=2026-10-05T15:24:07.3460000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[223] _id=6ac3c1fede269131f9ad2de6 ts=2026-10-05T15:27:57.9130000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[269] _id=6ac3c297de269131f9ad3613 ts=2026-10-05T15:30:31.0990000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[0] _id=6ac3bd30de269131f9acd55b ts=2026-10-05T15:07:28.4040000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[593] _id=6ac3c604de269131f9ad6a3e ts=2026-10-05T15:45:07.6830000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[669] _id=6ac512d7de269131f9b45a79 ts=2026-10-06T15:25:11.1090000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[1] _id=6ac3bd30de269131f9acd559 ts=2026-10-05T15:07:28.4020000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[592] _id=6ac3c603de269131f9ad6a3b ts=2026-10-05T15:45:07.6820000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[668] _id=6ac512d7de269131f9b45a77 ts=2026-10-06T15:25:11.1070000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[2295] _id=6ac662c2de269131f9bb9995 ts=2026-10-06T15:47:33.758Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[3257] _id=6ac7b45ede269131f9c37f4d ts=2026-10-07T15:47:24.896Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[4277] _id=6ace4b04de269131f9cf0b3b ts=2026-10-08T15:45:40.432Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 18 of 79 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[746] _id=6ac5136bde269131f9b45d63 ts=2026-10-06T15:27:38.4150000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[752] _id=6ac5137bde269131f9b45dba ts=2026-10-06T15:27:54.7230000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[2197] _id=6ac516eade269131f9b4a17f ts=2026-10-06T15:42:33.8990000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3817 | 0.0 | 1.002 | 249.487 | 11.742 | 430239.723 | 0.24 | 56 | 7 |
| PuzzlePieceVisibleEvent | 2912 | 0.0 | 0.044 | 296.688 | 1.854 | 518337.489 | 0.2 | 1503 | 6 |
| DialogueEvent | 1882 | 0.0 | 3.726 | 506.001 | 29.104 | 430195.15 | 0.12 | 526 | 7 |
| PlayerPositionEvent | 1594 | 9.762 | 10.001 | 597.255 | 10.104 | 430187.745 | 0.1 | 0 | 7 |
| argumentationNodeEvent | 360 | 0.022 | 0.312 | 2640.562 | 13.574 | 690599.3 | 0.02 | 52 | 3 |
| ObjectInterEvent | 243 | 0.0 | 12.62 | 3917.282 | 354.985 | 430611.151 | 0.02 | 3 | 11 |
| TopographicMapEvent | 78 | 0.023 | 3.907 | 9958.249 | 84660.014 | 432506.508 | 0.01 | 4 | 6 |
| Soil Key Puzzle | 73 | 0.038 | 0.997 | 9455.189 | 19.456 | 603522.287 | 0.01 | 1 | 2 |
| questEvent | 64 | 0.003 | 198.867 | 14879.494 | 84855.699 | 431195.013 | 0.0 | 8 | 14 |
| argumentationAnswerEvent | 60 | 0.116 | 7.137 | 15843.185 | 4368.374 | 690635.214 | 0.0 | 0 | 3 |
| DEBUGMenu | 28 | 6.639 | 721.518 | 34010.927 | 86265.58 | 431772.242 | 0.0 | 0 | 15 |
| soilMachine | 22 | 0.5 | 5.605 | 30.343 | 170.28 | 207.234 | 1.98 | 0 | 0 |
| gameWindowFocusEvent | 17 | 1.65 | 2259.28 | 56047.835 | 155608.908 | 431782.281 | 0.0 | 0 | 11 |
| gameStartEvent | 12 | 270.699 | 84740.706 | 79401.1 | 241913.087 | 431782.281 | 0.0 | 0 | 11 |
| argumentationEvent | 11 | 0.033 | 57.473 | 86419.444 | 432213.117 | 690591.803 | 0.0 | 1 | 3 |
| gameWindowUnfocusEvent | 9 | 1.559 | 86295.536 | 95998.851 | 328176.631 | 431762.635 | 0.0 | 0 | 5 |
| argumentationToolEvent | 8 | 0.012 | 3.396 | 86343.247 | 448948.594 | 690642.234 | 0.0 | 1 | 1 |
| DaniEvent | 5 | 0.295 | 0.776 | 120771.133 | 483081.737 | 603851.622 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 171765.103 | 431251.274 | 431251.274 | 664788.828 | 690737.445 | 0.0 | 0 | 2 |
| TerasGardenBox | 2 | 16.968 | 24.32 | 24.32 | 30.937 | 31.672 | 2.47 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[2301] _id=6ac662d2de269131f9bb99c6 ts=2026-10-07T15:18:41.1920000Z == 6ab9a8bc9a8420a1e6b56b0a.jsonl[2304] _id=6ac662d2de269131f9bb99c7 ts=2026-10-07T15:18:41.1920000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 96 group(s), 155 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[809] _id=6ac513aade269131f9b45ead ts=2026-10-06T15:28:29.1590000Z == 6ab9a8bc9a8420a1e6b56b0a.jsonl[700] _id=6ac513aade269131f9b45eaf ts=2026-10-06T15:28:29.1590000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[703] _id=6ac513abde269131f9b45ebd ts=2026-10-06T15:28:35.8660000Z == 6ab9a8bc9a8420a1e6b56b0a.jsonl[813] _id=6ac513abde269131f9b45ec5 ts=2026-10-06T15:28:35.8660000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[901] _id=6ac513cfde269131f9b460b3 ts=2026-10-06T15:29:17.1640000Z == 6ab9a8bc9a8420a1e6b56b0a.jsonl[936] _id=6ac513d0de269131f9b460b5 ts=2026-10-06T15:29:17.1640000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[135] _id=6ac3c0a4de269131f9ad0f7d ts=2026-10-05T15:22:12.7820000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[137] _id=6ac3c0a5de269131f9ad0f83 ts=2026-10-05T15:22:12.7900000Z`; `937ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[801] _id=6ac513b2de269131f9b45f25 ts=2026-10-06T15:28:50.0480000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[803] _id=6ac513b3de269131f9b45f2d ts=2026-10-06T15:28:50.9850000Z`; `582ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[803] _id=6ac513b3de269131f9b45f2d ts=2026-10-06T15:28:50.9850000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[838] _id=6ac513b4de269131f9b45f35 ts=2026-10-06T15:28:51.5670000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 212 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `103ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[781] _id=6ac513a8de269131f9b45e91 ts=2026-10-06T15:28:22.5380000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[796] _id=6ac513a8de269131f9b45e93 ts=2026-10-06T15:28:22.6410000Z`; `77ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[808] _id=6ac513aade269131f9b45eab ts=2026-10-06T15:28:29.0820000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[809] _id=6ac513aade269131f9b45ead ts=2026-10-06T15:28:29.1590000Z`; `438ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[700] _id=6ac513aade269131f9b45eaf ts=2026-10-06T15:28:29.1590000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[810] _id=6ac513aade269131f9b45eb1 ts=2026-10-06T15:28:29.5970000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2180] _id=6ac516f9de269131f9b4a2b5 ts=2026-10-06T15:42:49.2310000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[2183] _id=6ac516fade269131f9b4a2bf ts=2026-10-06T15:42:49.2580000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `676ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10848] _id=6ad244c8de269131f9e553f8 ts=2026-10-16T15:37:44.6660000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[10849] _id=6ad244c9de269131f9e553fc ts=2026-10-16T15:37:45.3420000Z`; `173ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10891] _id=6ad244edde269131f9e55525 ts=2026-10-16T15:38:21.0290000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[10892] _id=6ad244edde269131f9e55527 ts=2026-10-16T15:38:21.2020000Z`; `176ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10892] _id=6ad244edde269131f9e55527 ts=2026-10-16T15:38:21.2020000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[10888] _id=6ad244edde269131f9e5552b ts=2026-10-16T15:38:21.3780000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `62ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5847] _id=6acf9d51de269131f9d48fe3 ts=2026-10-14T15:18:39.9500000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[5845] _id=6acf9d51de269131f9d48fe7 ts=2026-10-14T15:18:40.0120000Z`; `33ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[11043] _id=6ad245d0de269131f9e55aea ts=2026-10-16T15:42:08.6520000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[11046] _id=6ad245d0de269131f9e55aed ts=2026-10-16T15:42:08.6850000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 36 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[399] _id=6ac3c486de269131f9ad5407 ts=2026-10-05T15:38:46.3850000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[400] _id=6ac3c486de269131f9ad540b ts=2026-10-05T15:38:46.4190000Z`; `41ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[408] _id=6ac3c48bde269131f9ad5468 ts=2026-10-05T15:38:51.6820000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[388] _id=6ac3c48cde269131f9ad546b ts=2026-10-05T15:38:51.7230000Z`; `23ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[402] _id=6ac3c48dde269131f9ad5491 ts=2026-10-05T15:38:53.5860000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[410] _id=6ac3c48dde269131f9ad5493 ts=2026-10-05T15:38:53.6090000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `393ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[459] _id=6ac3c4dade269131f9ad5a09 ts=2026-10-05T15:40:10.5130000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[457] _id=6ac3c4dbde269131f9ad5a0f ts=2026-10-05T15:40:10.9060000Z`; `793ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4754] _id=6ace4eb2de269131f9cf2383 ts=2026-10-13T15:30:58.1900000Z ~ 6ab9a8bc9a8420a1e6b56b0a.jsonl[4755] _id=6ace4eb3de269131f9cf2389 ts=2026-10-13T15:30:58.9830000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3261] _id=6ac7b468de269131f9c3801d ts=2026-10-08T15:19:04.0460000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4278] _id=6ace4b04de269131f9cf0b3d ts=2026-10-13T15:15:16.2880000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2303] _id=6ac662cdde269131f9bb99b6 ts=2026-10-07T15:18:36.8920000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3258] _id=6ac7b45ede269131f9c37f4f ts=2026-10-08T15:18:54.0090000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[670] _id=6ac512e1de269131f9b45a9b ts=2026-10-06T15:25:21.1110000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2296] _id=6ac662c2de269131f9bb9997 ts=2026-10-07T15:18:25.2660000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 44m 
  - Evidence: 167h 44m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2464] _id=6ac66429de269131f9bbb293 ts=2026-10-07T15:24:24.6070000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5244] _id=6acf9af5de269131f9d45d4d ts=2026-10-14T15:08:36.2290000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4264] _id=6ac7ba9ede269131f9c41ef5 ts=2026-10-08T15:45:34.7100000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4287] _id=6ace4b14de269131f9cf0b76 ts=2026-10-13T15:15:29.8600000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[636] _id=6ac3c6b1de269131f9ad7873 ts=2026-10-05T15:48:01.6400000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[681] _id=6ac51302de269131f9b45b37 ts=2026-10-06T15:25:53.5780000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2277] _id=6ac517ebde269131f9b4bb6d ts=2026-10-06T15:46:50.7970000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2343] _id=6ac66319de269131f9bb9b55 ts=2026-10-07T15:19:52.3620000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 526 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10758] _id=6ad2446cde269131f9e550e4 ts=2026-10-16T15:36:12.1860000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10759] _id=6ad2446cde269131f9e550e5 ts=2026-10-16T15:36:12.1860000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10790] _id=6ad2448bde269131f9e55223 ts=2026-10-16T15:36:42.8290000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10794] _id=6ad2448bde269131f9e55224 ts=2026-10-16T15:36:42.8290000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10813] _id=6ad2449cde269131f9e552b2 ts=2026-10-16T15:37:00.5700000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10814] _id=6ad2449cde269131f9e552b3 ts=2026-10-16T15:37:00.5700000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 52m 
  - Evidence: 191h 52m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[590] _id=6ac3c5aede269131f9ad6620 ts=2026-10-05T15:43:42.3440000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4881] _id=6ace4fe0de269131f9cf2f0c ts=2026-10-13T15:35:59.7890000Z; 47h 42m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4881] _id=6ace4fe0de269131f9cf2f0c ts=2026-10-13T15:35:59.7890000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7586] _id=6ad0eed5de269131f9dc70ba ts=2026-10-15T15:18:44.8920000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4181] _id=6ac7ba7ede269131f9c41df7 ts=2026-10-08T15:45:02.2130000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4290] _id=6ace4b1ede269131f9cf0bb2 ts=2026-10-13T15:15:41.9360000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[634] _id=6ac3c68cde269131f9ad768f ts=2026-10-05T15:47:24.0980000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[673] _id=6ac512e5de269131f9b45abd ts=2026-10-06T15:25:23.7790000Z; 23h 31m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3235] _id=6ac66989de269131f9bc2fa2 ts=2026-10-07T15:47:20.7520000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3285] _id=6ac7b475de269131f9c38143 ts=2026-10-08T15:19:17.7230000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 56 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2301] _id=6ac662d2de269131f9bb99c6 ts=2026-10-07T15:18:41.1920000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2304] _id=6ac662d2de269131f9bb99c7 ts=2026-10-07T15:18:41.1920000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2304] _id=6ac662d2de269131f9bb99c7 ts=2026-10-07T15:18:41.1920000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2305] _id=6ac662d2de269131f9bb99c8 ts=2026-10-07T15:18:41.1920000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5319] _id=6acf9b2fde269131f9d4631f ts=2026-10-14T15:09:34.1180000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5320] _id=6acf9b2fde269131f9d46320 ts=2026-10-14T15:09:34.1180000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 36m 
  - Evidence: 119h 36m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4182] _id=6ac7ba7fde269131f9c41e01 ts=2026-10-08T15:45:03.7750000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4414] _id=6ace4c93de269131f9cf1382 ts=2026-10-13T15:21:54.9260000Z; 24h 6m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2007] _id=6ac51513de269131f9b47701 ts=2026-10-06T15:34:43.0350000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2874] _id=6ac6681ede269131f9bc151b ts=2026-10-07T15:41:17.3580000Z; 23h 43m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[568] _id=6ac3c584de269131f9ad61e5 ts=2026-10-05T15:43:00.6000000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[717] _id=6ac5132dde269131f9b45c67 ts=2026-10-06T15:26:36.8420000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.008s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10607] _id=6ad2438ede269131f9e546dd ts=2026-10-16T15:32:30.1250000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10608] _id=6ad2438ede269131f9e546de ts=2026-10-16T15:32:30.1250000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10672] _id=6ad243d6de269131f9e54b11 ts=2026-10-16T15:33:42.5150000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10673] _id=6ad243d6de269131f9e54b12 ts=2026-10-16T15:33:42.5150000Z; 8ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[135] _id=6ac3c0a4de269131f9ad0f7d ts=2026-10-05T15:22:12.7820000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[137] _id=6ac3c0a5de269131f9ad0f83 ts=2026-10-05T15:22:12.7900000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4269] _id=6ac7baa3de269131f9c41f01 ts=2026-10-08T15:45:39.2500000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4286] _id=6ace4b14de269131f9cf0b75 ts=2026-10-13T15:15:26.9950000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[650] _id=6ac3c6afde269131f9ad7865 ts=2026-10-05T15:47:59.3210000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[672] _id=6ac512e5de269131f9b45ab9 ts=2026-10-06T15:25:21.1230000Z; 23h 31m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3238] _id=6ac6698bde269131f9bc2fd9 ts=2026-10-07T15:47:22.3830000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3263] _id=6ac7b46bde269131f9c3804b ts=2026-10-08T15:19:04.0650000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 58m 
  - Evidence: 143h 58m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3766] _id=6ac7b5cade269131f9c3a3d6 ts=2026-10-08T15:24:56.5050000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[6013] _id=6acf9e8cde269131f9d4a383 ts=2026-10-14T15:23:53.9940000Z; 23h 58m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[6384] _id=6acf9f1fde269131f9d4abdb ts=2026-10-14T15:26:21.0820000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7752] _id=6ad0f056de269131f9dc8627 ts=2026-10-15T15:25:09.8580000Z; 23h 58m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[1391] _id=6ac514efde269131f9b473df ts=2026-10-06T15:34:05.0940000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2634] _id=6ac6660ede269131f9bbec5b ts=2026-10-07T15:32:29.5090000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1503 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[1006] _id=6ac513e4de269131f9b46237 ts=2026-10-06T15:29:38.4230000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[1022] _id=6ac513e4de269131f9b46239 ts=2026-10-06T15:29:38.4230000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[1008] _id=6ac513e0de269131f9b461d7 ts=2026-10-06T15:29:34.4470000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[990] _id=6ac513e0de269131f9b461d9 ts=2026-10-06T15:29:34.4470000Z; 0ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[1009] _id=6ac513e0de269131f9b461df ts=2026-10-06T15:29:34.4470000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[1010] _id=6ac513e1de269131f9b461e3 ts=2026-10-06T15:29:34.4470000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 38m 
  - Evidence: 167h 38m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2947] _id=6ac668c0de269131f9bc1ed8 ts=2026-10-07T15:43:59.7810000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5975] _id=6acf9e43de269131f9d4a00c ts=2026-10-14T15:22:42.0680000Z; 24h 1m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5987] _id=6acf9e5bde269131f9d4a10f ts=2026-10-14T15:23:06.8610000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7741] _id=6ad0f03bde269131f9dc8550 ts=2026-10-15T15:24:43.4110000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.038s..0.038s shown 
  - Evidence: 38ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[7723] _id=6ad0f044de269131f9dc859b ts=2026-10-15T15:24:51.7060000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7747] _id=6ad0f044de269131f9dc859d ts=2026-10-15T15:24:51.7440000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 8m 
  - Evidence: 120h 8m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3989] _id=6ac7b800de269131f9c3f1b0 ts=2026-10-08T15:34:24.8540000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4992] _id=6ace517bde269131f9cf3e7f ts=2026-10-13T15:42:51.3620000Z; 23h 57m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2746] _id=6ac666fbde269131f9bc019e ts=2026-10-07T15:36:27.1470000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3980] _id=6ac7b7eede269131f9c3f073 ts=2026-10-08T15:34:06.4880000Z; 23h 56m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5101] _id=6ace527ade269131f9cf49a8 ts=2026-10-13T15:47:06.1490000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7064] _id=6acfa322de269131f9d4e797 ts=2026-10-14T15:43:29.5990000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.023s..0.027s shown 
  - Evidence: 23ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2393] _id=6ac663bbde269131f9bba64f ts=2026-10-07T15:22:34.5170000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2397] _id=6ac663bbde269131f9bba653 ts=2026-10-07T15:22:34.5400000Z; 25ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2179] _id=6ac516f9de269131f9b4a2af ts=2026-10-06T15:42:49.2060000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2180] _id=6ac516f9de269131f9b4a2b5 ts=2026-10-06T15:42:49.2310000Z; 27ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2180] _id=6ac516f9de269131f9b4a2b5 ts=2026-10-06T15:42:49.2310000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[2183] _id=6ac516fade269131f9b4a2bf ts=2026-10-06T15:42:49.2580000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 50m 
  - Evidence: 191h 50m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[490] _id=6ac3c503de269131f9ad5bf9 ts=2026-10-05T15:40:51.5030000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4794] _id=6ace4ecede269131f9cf249f ts=2026-10-13T15:31:26.7170000Z; 48h 17m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5844] _id=6acf9d51de269131f9d48fde ts=2026-10-14T15:18:39.9250000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10748] _id=6ad24460de269131f9e55071 ts=2026-10-16T15:35:59.9980000Z; 23h 45m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4794] _id=6ace4ecede269131f9cf249f ts=2026-10-13T15:31:26.7170000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5745] _id=6acf9ce5de269131f9d48744 ts=2026-10-14T15:16:52.4980000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 49m 
  - Evidence: 191h 49m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[493] _id=6ac3c503de269131f9ad5bfb ts=2026-10-05T15:40:51.5330000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4719] _id=6ace4ea3de269131f9cf22f1 ts=2026-10-13T15:30:43.3360000Z; 48h 17m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5845] _id=6acf9d51de269131f9d48fe7 ts=2026-10-14T15:18:40.0120000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10734] _id=6ad2445ade269131f9e5501b ts=2026-10-16T15:35:54.4430000Z; 23h 44m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4796] _id=6ace4ecfde269131f9cf24a1 ts=2026-10-13T15:31:26.7390000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5691] _id=6acf9cc4de269131f9d48334 ts=2026-10-14T15:16:19.4500000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.033s..0.033s shown 
  - Evidence: 33ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[11043] _id=6ad245d0de269131f9e55aea ts=2026-10-16T15:42:08.6520000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[11046] _id=6ad245d0de269131f9e55aed ts=2026-10-16T15:42:08.6850000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 49m 
  - Evidence: 191h 49m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[489] _id=6ac3c502de269131f9ad5be7 ts=2026-10-05T15:40:50.1230000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4747] _id=6ace4ea9de269131f9cf232e ts=2026-10-13T15:30:49.4230000Z; 48h 17m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5842] _id=6acf9d4dde269131f9d48f95 ts=2026-10-14T15:18:33.3640000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10719] _id=6ad2445cde269131f9e5503b ts=2026-10-16T15:35:56.4020000Z; 23h 44m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4795] _id=6ace4eccde269131f9cf248b ts=2026-10-13T15:31:24.1810000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5694] _id=6acf9cc8de269131f9d483e9 ts=2026-10-14T15:16:23.8410000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 52 interval(s) ≤ 0.022s..0.023s shown 
  - Evidence: 22ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[10796] _id=6ad24497de269131f9e5527b ts=2026-10-16T15:36:54.9290000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[10806] _id=6ad24497de269131f9e5527d ts=2026-10-16T15:36:54.9510000Z; 22ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5729] _id=6acf9cdcde269131f9d4864c ts=2026-10-14T15:16:42.9410000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[5730] _id=6acf9cdcde269131f9d4864e ts=2026-10-14T15:16:42.9630000Z; 23ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[402] _id=6ac3c48dde269131f9ad5491 ts=2026-10-05T15:38:53.5860000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[410] _id=6ac3c48dde269131f9ad5493 ts=2026-10-05T15:38:53.6090000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 50m 
  - Evidence: 191h 50m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[462] _id=6ac3c4e0de269131f9ad5a31 ts=2026-10-05T15:40:15.9560000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4754] _id=6ace4eb2de269131f9cf2383 ts=2026-10-13T15:30:58.1900000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.012s..0.012s shown 
  - Evidence: 12ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[460] _id=6ac3c4dbde269131f9ad5a0d ts=2026-10-05T15:40:10.8940000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[457] _id=6ac3c4dbde269131f9ad5a0f ts=2026-10-05T15:40:10.9060000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3260] _id=6ac7b45ede269131f9c37f51 ts=2026-10-08T15:18:54.1550000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4280] _id=6ace4b04de269131f9cf0b3f ts=2026-10-13T15:15:16.4360000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5108] _id=6acf997cde269131f9d4428d ts=2026-10-14T15:02:19.1560000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7205] _id=6ad0eba1de269131f9dc2558 ts=2026-10-15T15:05:04.7210000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2298] _id=6ac662c2de269131f9bb9999 ts=2026-10-07T15:18:25.4010000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3260] _id=6ac7b45ede269131f9c37f51 ts=2026-10-08T15:18:54.1550000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3259] _id=6ac7b45ede269131f9c37f50 ts=2026-10-08T15:18:54.1550000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4279] _id=6ace4b04de269131f9cf0b3e ts=2026-10-13T15:15:16.4360000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5107] _id=6acf997cde269131f9d4428c ts=2026-10-14T15:02:19.1560000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[7204] _id=6ad0eba1de269131f9dc2557 ts=2026-10-15T15:05:04.7210000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2297] _id=6ac662c2de269131f9bb9998 ts=2026-10-07T15:18:25.4010000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3259] _id=6ac7b45ede269131f9c37f50 ts=2026-10-08T15:18:54.1550000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[4277] _id=6ace4b04de269131f9cf0b3b ts=2026-10-08T15:45:40.432Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4976] _id=6ace5137de269131f9cf3b1f ts=2026-10-13T15:41:43.0670000Z; 47h 59m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[5109] _id=6acf997bde269131f9d4427b ts=2026-10-13T15:47:22.264Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[9180] _id=6ad0f588de269131f9dcde41 ts=2026-10-15T15:47:19.8890000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[9180] _id=6ad0f588de269131f9dcde41 ts=2026-10-15T15:47:19.8890000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[11219] _id=6ad2471dde269131f9e56287 ts=2026-10-16T15:47:16.172Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3870] _id=6ac7b6b6de269131f9c3ca6c ts=2026-10-08T15:28:54.9070000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[4289] _id=6ace4b14de269131f9cf0b78 ts=2026-10-13T15:15:29.9200000Z; 23h 38m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[628] _id=6ac3c676de269131f9ad73a8 ts=2026-10-05T15:47:02.6200000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[674] _id=6ac512e5de269131f9b45abf ts=2026-10-06T15:25:23.8150000Z; 23h 38m: 6ab9a8bc9a8420a1e6b56b0a.jsonl[2864] _id=6ac66813de269131f9bc13bc ts=2026-10-07T15:41:06.3320000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3266] _id=6ac7b46bde269131f9c3804e ts=2026-10-08T15:19:06.9530000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[3266] _id=6ac7b46bde269131f9c3804e ts=2026-10-08T15:19:06.9530000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[3267] _id=6ac7b46bde269131f9c3804f ts=2026-10-08T15:19:06.9560000Z; 3ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[363] _id=6ac3c42fde269131f9ad4dab ts=2026-10-05T15:37:19.1920000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[362] _id=6ac3c42fde269131f9ad4dad ts=2026-10-05T15:37:19.1950000Z; 5ms: 6ab9a8bc9a8420a1e6b56b0a.jsonl[9091] _id=6ad0f4eede269131f9dcd523 ts=2026-10-15T15:44:45.7440000Z -> 6ab9a8bc9a8420a1e6b56b0a.jsonl[9092] _id=6ad0f4eede269131f9dcd527 ts=2026-10-15T15:44:45.7490000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[350] _id=6ac3c412de269131f9ad4b89 ts=2026-10-05T15:36:50.2310000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[502] _id=6ac3c51bde269131f9ad5ccd ts=2026-10-05T15:41:15.0360000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[2572] _id=6ac66576de269131f9bbda16 ts=2026-10-07T15:29:58.1490000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 29 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[844] _id=6ac513bbde269131f9b45f75 ts=2026-10-06T15:28:57.9340000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[845] _id=6ac513bbde269131f9b45f79 ts=2026-10-06T15:28:57.9970000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[864] _id=6ac513bbde269131f9b45f7c ts=2026-10-06T15:28:58.0510000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 98 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[778] _id=6ac513a7de269131f9b45e7d ts=2026-10-06T15:28:21.6470000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[789] _id=6ac513a8de269131f9b45e85 ts=2026-10-06T15:28:22.0180000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[780] _id=6ac513a8de269131f9b45e8f ts=2026-10-06T15:28:22.5380000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[5845] _id=6acf9d51de269131f9d48fe7 ts=2026-10-14T15:18:40.0120000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[11046] _id=6ad245d0de269131f9e55aed ts=2026-10-16T15:42:08.6850000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[400] _id=6ac3c486de269131f9ad540b ts=2026-10-05T15:38:46.4190000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[388] _id=6ac3c48cde269131f9ad546b ts=2026-10-05T15:38:51.7230000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[410] _id=6ac3c48dde269131f9ad5493 ts=2026-10-05T15:38:53.6090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[9200] _id=6ad23c93de269131f9e4cdc5 ts=2026-10-16T15:02:43.2570000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[9354] _id=6ad23d9cde269131f9e4ec5c ts=2026-10-16T15:07:08.2920000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[11208] _id=6ad24702de269131f9e561f5 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 171 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[912] _id=6ac513cede269131f9b46083 ts=2026-10-06T15:29:15.4230000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[976] _id=6ac513dcde269131f9b46185 ts=2026-10-06T15:29:30.9240000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[981] _id=6ac513ddde269131f9b4619f ts=2026-10-06T15:29:31.7470000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 383 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[797] _id=6ac513a9de269131f9b45e97 ts=2026-10-06T15:28:22.6410000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[807] _id=6ac513a9de269131f9b45ea7 ts=2026-10-06T15:28:22.8550000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[699] _id=6ac513a9de269131f9b45ea9 ts=2026-10-06T15:28:22.8550000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 18 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[2180] _id=6ac516f9de269131f9b4a2b5 ts=2026-10-06T15:42:49.2310000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[2183] _id=6ac516fade269131f9b4a2bf ts=2026-10-06T15:42:49.2580000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[2389] _id=6ac663acde269131f9bba488 ts=2026-10-07T15:22:19.2660000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 22 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[417] _id=6ac3c496de269131f9ad551b ts=2026-10-05T15:39:02.0770000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[390] _id=6ac3c496de269131f9ad551d ts=2026-10-05T15:39:02.1080000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[418] _id=6ac3c496de269131f9ad551f ts=2026-10-05T15:39:02.3170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[459] _id=6ac3c4dade269131f9ad5a09 ts=2026-10-05T15:40:10.5130000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[457] _id=6ac3c4dbde269131f9ad5a0f ts=2026-10-05T15:40:10.9060000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[4755] _id=6ace4eb3de269131f9cf2389 ts=2026-10-13T15:30:58.9830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 348 start, 343 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 39 unmatched 'BecameCameraCentered' (totals: 585 open, 575 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 57 unmatched 'BecameVisible' (totals: 856 open, 897 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 20 open, 18 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 148 open, 151 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 6 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 39 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 298 of 11227 adjacent _id pairs reverse in client time; worst 64.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b0a.jsonl[772] _id=6ac513a5de269131f9b45e67 ts=2026-10-06T15:28:37.1120000Z`; `6ab9a8bc9a8420a1e6b56b0a.jsonl[773] _id=6ac513a6de269131f9b45e69 ts=2026-10-06T15:27:32.8580000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.71s, min -430176.15s, max -0.08s over 11228 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b0a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `InputEvent` — 3818 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1036); Unit 4 Dev - Dungeon (1028); Unit 3 Dev (819); Unit 3 Dungeon Dev (435); Unit 4 Dev (302); Unit 1 Dev (118); Unit 4 Dev - Anderson Base (80)
- **Intervals:** median 1.00s (p5 0.18s / p95 11.74s, n=3817)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3818/3818 records)
    "pressed"  x3818
data.actionType  (string, 3818/3818 records)
    "Move"  x2676
    "Jump"  x606
    "Interact"  x303
    "Ascend"  x124
    "Sprint"  x49
    "Hoverboard"  x40
    "Descend"  x13
    "Pause"  x4
    "Map"  x3
data.key  (string, 3818/3818 records, 12 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3818/3818 records)
    "Player"  x3090
    "Drone"  x728
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2913 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1699); Unit 4 Dev (908); Unit 3 Dungeon Dev (306)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.85s, n=2912)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2913/2913 records)
    "BecameInvisible"  x897
    "BecameVisible"  x856
    "BecameCameraCentered"  x585
    "BecameCameraUncentered"  x575
data.pieceId  (string, 2913/2913 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2913/2913 records)
    1727 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1883 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (707); Unit 3 Dev (371); Unit 1 Dev (201); Unit 4 Dev (201); Unit 4 Dev - Anderson Base (151); Unit 3 Dungeon Dev (133); Unit 4 Dev - Dungeon (119)
- **eventKey:** present on 1192 of 1883 records
- **Intervals:** median 3.73s (p5 0.00s / p95 29.10s, n=1882)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1192; [conversationId, dialogueEventType] x691
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1883/1883 records)
    numeric range 8 .. 114 (45 unique)
data.dialogueEventType  (string, 1883/1883 records)
    "DialogueNodeEvent"  x1192
    "DialogueStartEvent"  x348
    "DialogueFinishEvent"  x343
data.nodeId  (number, 1192/1883 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1604 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (595); Unit 3 Dev (298); Unit 4 Dev - Dungeon (218); Unit 1 Dev (166); Unit 4 Dev (146); Unit 3 Dungeon Dev (107); Unit 4 Dev - Anderson Base (74)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.10s, n=1594)
- **Fields under `data`:**

```text
data.position  (object, 1604/1604 records)
data.position.x  (number, 1604/1604 records)
    numeric range -748.128 .. 1552.25 (648 unique)
data.position.y  (number, 1604/1604 records)
    numeric range -115.12 .. 165.504 (457 unique)
data.position.z  (number, 1604/1604 records)
    numeric range -1139.65 .. 2190.8 (648 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 361 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (151); Unit 3 Dev (99); Unit 1 Dev (64); Unit 2 Prod (Refactor) (47)
- **Intervals:** median 0.31s (p5 0.03s / p95 13.57s, n=360)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 361/361 records)
    "argumentationNodeHoverEnd"  x151
    "argumentationNodeHoverStart"  x148
    "argumentationNodeAdd"  x38
    "argumentationNodeRemove"  x24
data.argumentationTitle  (string, 361/361 records)
    "Unit 4 - Flooding"  x151
    "Unit 3 - Pollution Upstream"  x99
    "Unit 2 – Watershed"  x47
    "Unit 1 - Freshwater"  x39
    "Unit 1 - Argumentation Tutorial"  x25
data.nodeName  (string, 361/361 records)
    "I"  x56
    "1"  x48
    "II"  x48
    "A"  x41
    "B"  x40
    "3"  x30
    "C"  x29
    "2"  x25
    "D"  x19
    "4"  x18
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 244 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (101); Unit 2 Prod (Refactor) (59); Unit 3 Dungeon Dev (33); Unit 4 Dev (19); Unit 3 Dev (12); Unit 1 Dev (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 12.62s (p5 0.84s / p95 354.99s, n=243)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 244/244 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 244/244 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 79 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (70); Unit 3 Dev (9)
- **Intervals:** median 3.91s (p5 0.45s / p95 84660.01s, n=78)
- **`data` key-set variants:** [actionType, featureUsed] x38; [actionType, featureUsed, location] x23; [actionType, featureUsed, legendName] x18
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 79/79 records)
    "MapOpenEvent"  x20
    "MapCloseEvent"  x18
    "WaypointMoveEvent"  x16
    "Selected"  x14
    "WaypointSetEvent"  x7
    "Unselected"  x4
data.featureUsed  (string, 79/79 records)
    "Map"  x38
    "Waypoint"  x23
    "Legend"  x18
data.legendName  (string, 18/79 records)
    "0 ft"  x5
    "330 ft"  x3
    "90 ft"  x3
    "270 ft"  x2
    "360 ft"  x2
    "30 ft"  x1
    "300 ft"  x1
    "Water"  x1
data.location  (object, 23/79 records)
data.location.x  (number, 23/79 records)
    numeric range -316.6 .. 172.656 (21 unique)
data.location.y  (number, 23/79 records)
    numeric range -193.039 .. 242.792 (22 unique)
data.location.z  (number, 23/79 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 74 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (54); Unit 3 Dev (10); Unit 4 Dev (10)
- **Intervals:** median 1.00s (p5 0.17s / p95 19.46s, n=73)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x68; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/74 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/74 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 68/74 records)
    "RightDrag"  x37
    "LeftDrag"  x31
data.currentSoilType  (string, 68/74 records)
    "SAND"  x16
    "CLAYSAND"  x15
    "CLAY"  x11
    "SANDGRAVEL"  x11
    "CLAYROCK"  x8
    "GRAVEL"  x5
    "BEDROCK"  x2
data.isCorrectSelection  (string, 68/74 records)
    "false"  x51
    "true"  x17
data.waterLevelStatus  (string, 68/74 records)
    "TooHigh"  x34
    "Proper"  x18
    "TooLow"  x16
data.waterRetentionChange  (string, 68/74 records)
    "Increase"  x29
    "Decrease"  x22
    "NoChange"  x17
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 65 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 4 Dev - Dungeon (13); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev (6); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 65 of 65 records
- **Intervals:** median 198.87s (p5 0.01s / p95 84855.70s, n=64)
- **`data` key-set variants:** [questEventType, questID, questName] x39; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 65/65 records)
    "questActiveEvent"  x39
    "questFinishEvent"  x26
data.questID  (string, 65/65 records)
    26 unique values (see csv/event_unique_values.csv)
data.questName  (string, 65/65 records)
    26 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/65 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 61 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (48); Unit 3 Dev (9); Unit 1 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 7.14s (p5 0.17s / p95 4368.37s, n=60)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 61/61 records)
    "submitAnswerEvent"  x61
data.answerSubmitted  (string, 61/61 records)
    19 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 61/61 records)
    "Unit 4 - Flooding"  x48
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 4 Dev (4); Unit 4 Dev - Dungeon (3); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 721.52s (p5 8.78s / p95 86265.58s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 23 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (23)
- **Intervals:** median 5.61s (p5 0.70s / p95 170.28s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "ChangeCanister"  x23
data.canisterType  (string, 23/23 records)
    "Clay"  x7
    "Sand"  x6
    "Bedrock"  x5
    "Gravel"  x5
data.floor  (string, 23/23 records)
    "5"  x12
    "4"  x8
    "3"  x3
data.machine  (string, 23/23 records)
    "1"  x20
    "2"  x3
data.row  (string, 23/23 records)
    "TopRow"  x17
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 18 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 4 Dev (3); Unit 3 Dev (2)
- **Intervals:** median 2259.28s (p5 4.41s / p95 155608.91s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 84740.71s (p5 584.95s / p95 241913.09s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 57.47s (p5 0.05s / p95 432213.12s, n=11)
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
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 10 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev (3); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 86295.54s (p5 2.82s / p95 328176.63s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    false  x10
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 3.40s (p5 0.14s / p95 448948.59s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x6
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 0.78s (p5 0.39s / p95 483081.74s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 431251.27s (p5 197713.72s / p95 664788.83s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 3 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (3)
- **Intervals:** median 24.32s (p5 17.70s / p95 30.94s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "cameraPlaced"  x3
data.boxId  (string, 3/3 records)
    "0"  x1
    "1"  x1
    "2"  x1
data.soilType  (string, 3/3 records)
    "None"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a915116:wasm-function[108544]:0x24e60da
    at wasm://wasm/0a915116:wasm-function[3309]:0x143bd9
    at wasm://wasm/0a915116:wasm-function[59793]:0x11abccc
    at wasm://wasm/0a915116:wasm-function[3347]:0x145fec
    at wasm://wasm/0a915116:wasm-function[82501]:0x170b4af
    at wasm://wasm/0a915116:wasm-function[83451]:0x171f21d
    at wasm://wasm/0a915116:wasm-function[110308]:0x259f6a8
    at invoke_iiii (blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:474038)
    at wasm://wasm/0a915116:wasm-function[83436]:0x171e8bd
    at wasm://wasm/0a915116:wasm-function[1942]:0xf58e4
    at wasm://wasm/0a915116:wasm-function[109965]:0x256667c
    at wasm://wasm/0a915116:wasm-function[106271]:0x24b7432
    at wasm://wasm/0a915116:wasm-function[84075]:0x1745541
    at wasm://wasm/0a915116:wasm-function[84074]:0x1745477
    at wasm://wasm/0a915116:wasm-function[104597]:0x23ea9bc
    at wasm://wasm/0a915116:wasm-function[104583]:0x23e6a91
    at wasm://wasm/0a915116:wasm-function[103961]:0x235b2a8
    at wasm://wasm/0a915116:wasm-function[105691]:0x245f4f0
    at wasm://wasm/0a915116:wasm-function[105691]:0x245f565
    at wasm://wasm/0a915116:wasm-function[110043]:0x256eaaf
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:23580
    at _JS_CallAsLongAsNoExceptionsSeen (blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:23594)
    at wasm://wasm/0a915116:wasm-function[110044]:0x256ebbe
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at browserIterationFunc (blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:115768)
    at callUserCallback (blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:98130)
    at Object.runIter (blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:99497)
    at Browser_mainLoop_runner (blob:https://mhs.adroit.games/f0bdbe64-96dd-4e7e-93f4-9caea70e5af2:9:115294)"  x1
data.type  (string, 1/1 records)
    "runtime_error"  x1
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
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (54 records)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (14x); "Unselected" (4x); "WaypointMoveEvent" (16x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (18x); "Waypoint" (23x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (24x)
- `soilMachine` data.canisterType: "Bedrock" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*