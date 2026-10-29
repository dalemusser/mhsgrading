# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7c
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b7c.jsonl
- **Records:** 15121 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b7c
- **Time span:** 2026-10-05T19:12:19.196000+00:00 .. 2026-10-19T01:31:35.842000+00:00 (318h 19m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 15121 records, 8 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 102 INFO, 2 NOT_TESTED, 85 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4549 | 30.08 | 1 | 7 | 0 | 2026-10-05T19:12:35.139000+00:00 | 2026-10-19T01:30:56.529000+00:00 | 318h 18m |
| PuzzlePieceVisibleEvent | 3985 | 26.35 | 1 | 3 | 0 | 2026-10-08T18:52:10.722000+00:00 | 2026-10-16T15:57:49.552000+00:00 | 189h 5m |
| DialogueEvent | 2530 | 16.73 | 1 | 7 | 1578 | 2026-10-05T19:12:51.683000+00:00 | 2026-10-19T01:31:15.189000+00:00 | 318h 18m |
| PlayerPositionEvent | 2276 | 15.05 | 1 | 7 | 0 | 2026-10-05T19:12:31.721000+00:00 | 2026-10-19T01:31:14.272000+00:00 | 318h 18m |
| argumentationNodeEvent | 926 | 6.12 | 1 | 4 | 0 | 2026-10-06T19:05:18.516000+00:00 | 2026-10-16T18:47:43.683000+00:00 | 239h 42m |
| ObjectInterEvent | 356 | 2.35 | 1 | 7 | 0 | 2026-10-06T18:32:41.417000+00:00 | 2026-10-19T01:30:57.492000+00:00 | 294h 58m |
| argumentationAnswerEvent | 123 | 0.81 | 1 | 4 | 0 | 2026-10-06T19:06:26.063000+00:00 | 2026-10-16T18:47:48.775000+00:00 | 239h 41m |
| questEvent | 86 | 0.57 | 1 | 7 | 86 | 2026-10-05T19:12:51.658000+00:00 | 2026-10-19T01:31:04.716000+00:00 | 318h 18m |
| DEBUGMenu | 49 | 0.32 | 1 | 8 | 0 | 2026-10-05T19:12:31.702000+00:00 | 2026-10-19T01:31:35.679000+00:00 | 318h 19m |
| Soil Key Puzzle | 48 | 0.32 | 1 | 3 | 0 | 2026-10-08T19:07:21.468000+00:00 | 2026-10-15T18:41:56.859000+00:00 | 167h 34m |
| TopographicMapEvent | 39 | 0.26 | 1 | 3 | 0 | 2026-10-08T18:53:34.087000+00:00 | 2026-10-15T16:06:02.315000+00:00 | 165h 12m |
| gameWindowFocusEvent | 32 | 0.21 | 1 | 5 | 0 | 2026-10-05T19:12:19.196000+00:00 | 2026-10-19T01:31:35.842000+00:00 | 318h 19m |
| soilMachine | 27 | 0.18 | 1 | 1 | 0 | 2026-10-15T18:57:48.800000+00:00 | 2026-10-15T19:08:23.307000+00:00 | 10m 34s |
| gameStartEvent | 24 | 0.16 | 1 | 1 | 0 | 2026-10-05T19:12:19.198000+00:00 | 2026-10-19T01:31:35.842000+00:00 | 318h 19m |
| TerasGardenBox | 20 | 0.13 | 1 | 1 | 0 | 2026-10-16T18:52:15.395000+00:00 | 2026-10-19T01:23:41.386000+00:00 | 54h 31m |
| gameWindowUnfocusEvent | 19 | 0.13 | 1 | 7 | 0 | 2026-10-05T19:18:02.314000+00:00 | 2026-10-16T17:05:03.695000+00:00 | 261h 47m |
| argumentationEvent | 16 | 0.11 | 1 | 4 | 0 | 2026-10-06T19:06:09.887000+00:00 | 2026-10-16T18:47:48.829000+00:00 | 239h 41m |
| argumentationToolEvent | 5 | 0.03 | 1 | 3 | 0 | 2026-10-06T19:06:09.807000+00:00 | 2026-10-15T02:28:07.609000+00:00 | 199h 21m |
| DaniEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-14T18:44:19.699000+00:00 | 2026-10-14T18:44:43.506000+00:00 | 23.8s |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-06T19:11:36.250000+00:00 | 2026-10-19T01:31:15.178000+00:00 | 294h 19m |
| chatEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-14T18:44:23.746000+00:00 | 2026-10-14T18:44:31.047000+00:00 | 7.3s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 289992.605s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.055s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 8.538s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 9.62s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 12.69s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 233.166s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 13590.579s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 7.301s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 5342.88s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2867.608s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 9707.652s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.784s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.1x vs baseline. 
  - Observed: 49 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Sprint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
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
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 24.6x vs baseline. 
  - Observed: 123 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,1,; A,2,I; A,2,II; A,3,I; A,3,II; A,4,I; A,4,II; A,B,1,II; A,B,2,II; A,B,4,II; A,B,C,2,II; A,B,D,2,II; A,C,2,II; A,C,B,2,II; A,D,2,II; B,1,I; B,1,II; B,2,I; B,2,II; B,3,II; B,4,II; B,A,2,II; B,C,1,I; B,C,2,I; B,C,2,II; B,C,4,II; B,C,D,2,II; C,1,I; C,2,II; C,4,II; C,A,2,II; C,B,1,I; C,B,3,II; C,D,2,II; D,1,I; D,1,II; D,2,I; D,2,II; D,3,II; D,4,I; D,4,II; D,A,2,II; D,B,2,II; D,C,2,II; I 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 6.6x vs baseline. 
  - Observed: 926 records 
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
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [23-36, 23-38, 23-40, 23-41, 23-42] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 24 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.4x vs baseline. 
  - Observed: 27 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 10 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[364] _id=6ac53fd6de269131f9b69a03 ts=2026-10-06T18:37:10.6900000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[421] _id=6ac540dbde269131f9b6b8ef ts=2026-10-06T18:41:31.2660000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[492] _id=6ac54139de269131f9b6c3f7 ts=2026-10-06T18:43:04.9560000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[3] _id=6ac3f694de269131f9af6b01 ts=2026-10-05T19:12:19.1980000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[118] _id=6ac53e60de269131f9b673d9 ts=2026-10-06T18:30:56.3290000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[512] _id=6ac5426bde269131f9b6eaa7 ts=2026-10-06T18:48:11.3340000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 32 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 32} 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[2] _id=6ac3f693de269131f9af6aff ts=2026-10-05T19:12:19.1960000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[119] _id=6ac53e60de269131f9b673d5 ts=2026-10-06T18:30:56.3280000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[513] _id=6ac5426bde269131f9b6eaa5 ts=2026-10-06T18:48:11.3320000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[117] _id=6ac53e60de269131f9b673cd ts=2026-10-05T19:18:02.314Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[511] _id=6ac5426bde269131f9b6ea93 ts=2026-10-06T18:44:30.653Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[1217] _id=6ac7e5cbde269131f9c58e76 ts=2026-10-06T19:18:03.792Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4548 | 0.0 | 0.912 | 251.957 | 13.76 | 399352.306 | 0.24 | 106 | 19 |
| PuzzlePieceVisibleEvent | 3984 | 0.0 | 0.055 | 170.868 | 1.7 | 399338.77 | 0.35 | 1933 | 13 |
| DialogueEvent | 2529 | 0.0 | 4.376 | 453.105 | 32.172 | 399302.482 | 0.13 | 751 | 17 |
| PlayerPositionEvent | 2266 | 0.0 | 10.001 | 502.997 | 10.13 | 399293.877 | 0.12 | 1 | 16 |
| argumentationNodeEvent | 925 | 0.001 | 0.451 | 932.914 | 13.521 | 690419.145 | 0.06 | 109 | 5 |
| ObjectInterEvent | 355 | 0.0 | 10.325 | 2991.257 | 403.871 | 486436.754 | 0.02 | 9 | 17 |
| argumentationAnswerEvent | 122 | 0.705 | 12.69 | 7072.809 | 117.252 | 690433.152 | 0.01 | 0 | 5 |
| questEvent | 85 | 0.002 | 254.001 | 13481.095 | 81160.942 | 399307.518 | 0.0 | 11 | 24 |
| DEBUGMenu | 48 | 8.093 | 971.946 | 23873.833 | 141567.552 | 399846.548 | 0.0 | 0 | 26 |
| Soil Key Puzzle | 47 | 0.194 | 1.396 | 12835.647 | 21126.288 | 514955.715 | 0.0 | 0 | 3 |
| TopographicMapEvent | 38 | 0.02 | 9.62 | 15651.269 | 76726.89 | 402396.487 | 0.0 | 2 | 7 |
| gameWindowFocusEvent | 31 | 12.719 | 2867.608 | 36966.343 | 183651.5 | 399856.305 | 0.0 | 0 | 25 |
| soilMachine | 26 | 1.089 | 4.784 | 24.404 | 121.932 | 168.505 | 2.46 | 0 | 0 |
| gameStartEvent | 23 | 709.338 | 5342.88 | 49824.202 | 193450.917 | 399856.305 | 0.0 | 0 | 23 |
| TerasGardenBox | 19 | 0.251 | 8.538 | 10330.842 | 19777.072 | 195921.054 | 0.01 | 0 | 1 |
| gameWindowUnfocusEvent | 18 | 17.261 | 9707.652 | 52356.743 | 206944.078 | 400461.319 | 0.0 | 0 | 16 |
| argumentationEvent | 15 | 0.024 | 233.166 | 57526.596 | 302007.812 | 690418.763 | 0.0 | 2 | 6 |
| argumentationToolEvent | 4 | 1.611 | 13590.579 | 179429.451 | 591020.104 | 690535.033 | 0.0 | 0 | 2 |
| DaniEvent | 3 | 3.214 | 3.858 | 7.936 | 15.447 | 16.735 | 7.56 | 0 | 0 |
| EndOfUnit | 3 | 78827.179 | 289992.605 | 353192.976 | 650682.49 | 690759.144 | 0.0 | 0 | 3 |
| chatEvent | 1 | 7.301 | 7.301 | 7.301 | 7.301 | 7.301 | 8.22 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[8226] _id=6ad03c5cde269131f9da44ac ts=2026-10-15T02:37:16.6330000Z == 6ab9a9279a8420a1e6b56b7c.jsonl[8227] _id=6ad03c5cde269131f9da44ad ts=2026-10-15T02:37:16.6330000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[9933] _id=6ad0fb40de269131f9dd53bf ts=2026-10-15T16:11:43.8730000Z == 6ab9a9279a8420a1e6b56b7c.jsonl[9934] _id=6ad0fb40de269131f9dd53c0 ts=2026-10-15T16:11:43.8730000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[9994] _id=6ad103b7de269131f9dddc7d ts=2026-10-15T16:47:48.8350000Z == 6ab9a9279a8420a1e6b56b7c.jsonl[9995] _id=6ad103b7de269131f9dddc7e ts=2026-10-15T16:47:48.8350000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 76 group(s), 133 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[1305] _id=6ac7e66cde269131f9c5a407 ts=2026-10-08T18:52:27.3080000Z == 6ab9a9279a8420a1e6b56b7c.jsonl[1301] _id=6ac7e66dde269131f9c5a40d ts=2026-10-08T18:52:27.3080000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[1316] _id=6ac7e670de269131f9c5a45e ts=2026-10-08T18:52:30.3420000Z == 6ab9a9279a8420a1e6b56b7c.jsonl[1311] _id=6ac7e670de269131f9c5a466 ts=2026-10-08T18:52:30.3420000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[1321] _id=6ac7e67ade269131f9c5a5ac ts=2026-10-08T18:52:41.1020000Z == 6ab9a9279a8420a1e6b56b7c.jsonl[1322] _id=6ac7e67bde269131f9c5a5b5 ts=2026-10-08T18:52:41.1020000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 31 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6ab9a9279a8420a1e6b56b7c.jsonl[190] _id=6ac53ec9de269131f9b67b85 ts=2026-10-06T18:32:41.4170000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[163] _id=6ac53ec9de269131f9b67b87 ts=2026-10-06T18:32:41.4270000Z`; `8ms: 6ab9a9279a8420a1e6b56b7c.jsonl[558] _id=6ac542a7de269131f9b6f257 ts=2026-10-06T18:49:11.7060000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[559] _id=6ac542a8de269131f9b6f25b ts=2026-10-06T18:49:11.7140000Z`; `404ms: 6ab9a9279a8420a1e6b56b7c.jsonl[1179] _id=6ac54910de269131f9b7938d ts=2026-10-06T19:16:32.5340000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[1174] _id=6ac54911de269131f9b793a1 ts=2026-10-06T19:16:32.9380000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `251ms: 6ab9a9279a8420a1e6b56b7c.jsonl[14654] _id=6ad27282de269131f9e76aec ts=2026-10-16T18:52:49.6460000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[14656] _id=6ad27282de269131f9e76af3 ts=2026-10-16T18:52:49.8970000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `705ms: 6ab9a9279a8420a1e6b56b7c.jsonl[14390] _id=6ad27097de269131f9e74447 ts=2026-10-16T18:44:39.3240000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[14379] _id=6ad27098de269131f9e74451 ts=2026-10-16T18:44:40.0290000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `56ms: 6ab9a9279a8420a1e6b56b7c.jsonl[7883] _id=6ad03a99de269131f9da406f ts=2026-10-15T02:29:45.2180000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[7886] _id=6ad03a99de269131f9da4072 ts=2026-10-15T02:29:45.2740000Z`; `24ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13757] _id=6ad2592cde269131f9e66128 ts=2026-10-16T17:04:44.4460000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[13760] _id=6ad2592cde269131f9e6612b ts=2026-10-16T17:04:44.4700000Z`; `39ms: 6ab9a9279a8420a1e6b56b7c.jsonl[14485] _id=6ad27155de269131f9e75373 ts=2026-10-16T18:47:48.7900000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[14488] _id=6ad27155de269131f9e75376 ts=2026-10-16T18:47:48.8290000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 65 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `365ms: 6ab9a9279a8420a1e6b56b7c.jsonl[863] _id=6ac5466ede269131f9b7445b ts=2026-10-06T19:05:18.5160000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[865] _id=6ac5466fde269131f9b74473 ts=2026-10-06T19:05:18.8810000Z`; `28ms: 6ab9a9279a8420a1e6b56b7c.jsonl[889] _id=6ac546a9de269131f9b74da1 ts=2026-10-06T19:06:16.2480000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[874] _id=6ac546a9de269131f9b74daf ts=2026-10-06T19:06:16.2760000Z`; `929ms: 6ab9a9279a8420a1e6b56b7c.jsonl[921] _id=6ac546f6de269131f9b75a9d ts=2026-10-06T19:07:34.0450000Z ~ 6ab9a9279a8420a1e6b56b7c.jsonl[917] _id=6ac546f7de269131f9b75ac1 ts=2026-10-06T19:07:34.9740000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 111h 4m 
  - Evidence: 111h 4m: 6ab9a9279a8420a1e6b56b7c.jsonl[4652] _id=6ac860b4de269131f9c7cd9b ts=2026-10-09T03:34:11.6290000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5715] _id=6ace7a9ade269131f9d1019b ts=2026-10-13T18:38:18.1770000Z; 54h 24m: 6ab9a9279a8420a1e6b56b7c.jsonl[14684] _id=6ad272fede269131f9e773d4 ts=2026-10-16T18:54:54.4490000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14789] _id=6ad57033de269131f9e910e7 ts=2026-10-19T01:19:46.3630000Z; 47h 36m: 6ab9a9279a8420a1e6b56b7c.jsonl[1100] _id=6ac5484ade269131f9b77789 ts=2026-10-06T19:13:13.9960000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1218] _id=6ac7e5cbde269131f9c58e7a ts=2026-10-08T18:49:46.2350000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 110h 55m 
  - Evidence: 110h 55m: 6ab9a9279a8420a1e6b56b7c.jsonl[5712] _id=6ac862fbde269131f9c7da42 ts=2026-10-09T03:43:54.5730000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5717] _id=6ace7ac2de269131f9d10468 ts=2026-10-13T18:38:57.0550000Z; 54h 24m: 6ab9a9279a8420a1e6b56b7c.jsonl[14776] _id=6ad2737fde269131f9e77dd4 ts=2026-10-16T18:57:02.7910000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14817] _id=6ad5707fde269131f9e9116a ts=2026-10-19T01:21:03.0480000Z; 47h 33m: 6ab9a9279a8420a1e6b56b7c.jsonl[1210] _id=6ac54937de269131f9b79917 ts=2026-10-06T19:17:11.1480000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1231] _id=6ac7e5f2de269131f9c592d5 ts=2026-10-08T18:50:25.4410000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 751 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13069] _id=6ad24c5ade269131f9e5a347 ts=2026-10-16T16:10:02.5760000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13070] _id=6ad24c5ade269131f9e5a348 ts=2026-10-16T16:10:02.5760000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13100] _id=6ad24c81de269131f9e5a60f ts=2026-10-16T16:10:40.7200000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13101] _id=6ad24c81de269131f9e5a610 ts=2026-10-16T16:10:40.7200000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13258] _id=6ad25522de269131f9e61856 ts=2026-10-16T16:47:30.5720000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13259] _id=6ad25522de269131f9e61857 ts=2026-10-16T16:47:30.5720000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 52m 
  - Evidence: 191h 52m: 6ab9a9279a8420a1e6b56b7c.jsonl[1095] _id=6ac547e8de269131f9b76e47 ts=2026-10-06T19:11:36.2500000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6954] _id=6acfd22fde269131f9d7fa38 ts=2026-10-14T19:04:15.3940000Z; 80h 33m: 6ab9a9279a8420a1e6b56b7c.jsonl[10223] _id=6ad1061bde269131f9de209f ts=2026-10-15T16:58:02.5730000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[15115] _id=6ad572e4de269131f9e91829 ts=2026-10-19T01:31:15.1780000Z; 21h 53m: 6ab9a9279a8420a1e6b56b7c.jsonl[6954] _id=6acfd22fde269131f9d7fa38 ts=2026-10-14T19:04:15.3940000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[10223] _id=6ad1061bde269131f9de209f ts=2026-10-15T16:58:02.5730000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 110h 55m 
  - Evidence: 110h 55m: 6ab9a9279a8420a1e6b56b7c.jsonl[5690] _id=6ac862d9de269131f9c7d9de ts=2026-10-09T03:43:19.9850000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5753] _id=6ace7ad0de269131f9d105b1 ts=2026-10-13T18:39:12.2910000Z; 54h 23m: 6ab9a9279a8420a1e6b56b7c.jsonl[14773] _id=6ad27380de269131f9e77de4 ts=2026-10-16T18:57:03.9600000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14806] _id=6ad57076de269131f9e9115a ts=2026-10-19T01:20:53.7470000Z; 47h 32m: 6ab9a9279a8420a1e6b56b7c.jsonl[1209] _id=6ac54936de269131f9b798e1 ts=2026-10-06T19:17:10.1250000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1225] _id=6ac7e5ddde269131f9c59058 ts=2026-10-08T18:50:04.0270000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 106 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[10963] _id=6ad11fbede269131f9df4b4a ts=2026-10-15T18:47:26.1600000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[10964] _id=6ad11fbede269131f9df4b4b ts=2026-10-15T18:47:26.1600000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[11057] _id=6ad1209cde269131f9df63ad ts=2026-10-15T18:51:07.5980000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[11058] _id=6ad1209cde269131f9df63ae ts=2026-10-15T18:51:07.5980000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[11455] _id=6ad1229ade269131f9dfa5dc ts=2026-10-15T18:59:37.9860000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[11456] _id=6ad1229ade269131f9dfa5dd ts=2026-10-15T18:59:37.9860000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 135h 7m 
  - Evidence: 135h 7m: 6ab9a9279a8420a1e6b56b7c.jsonl[5527] _id=6ac861abde269131f9c7d604 ts=2026-10-09T03:38:18.8280000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6448] _id=6acfcdcfde269131f9d77bf3 ts=2026-10-14T18:45:35.5820000Z; 54h 24m: 6ab9a9279a8420a1e6b56b7c.jsonl[14774] _id=6ad27381de269131f9e77dee ts=2026-10-16T18:57:04.8620000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14826] _id=6ad5708cde269131f9e91192 ts=2026-10-19T01:21:15.8370000Z; 47h 34m: 6ab9a9279a8420a1e6b56b7c.jsonl[1208] _id=6ac54937de269131f9b7990d ts=2026-10-06T19:17:11.1190000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1261] _id=6ac7e62fde269131f9c59c5a ts=2026-10-08T18:51:26.9770000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[12916] _id=6ad24b0cde269131f9e58cec ts=2026-10-16T16:04:27.9910000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[12917] _id=6ad24b0cde269131f9e58ced ts=2026-10-16T16:04:27.9910000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[12949] _id=6ad24b48de269131f9e590ec ts=2026-10-16T16:05:27.4190000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[12950] _id=6ad24b48de269131f9e590ed ts=2026-10-16T16:05:27.4190000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13152] _id=6ad25419de269131f9e60a59 ts=2026-10-16T16:43:04.8430000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13153] _id=6ad25419de269131f9e60a5a ts=2026-10-16T16:43:04.8430000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 110h 54m 
  - Evidence: 110h 54m: 6ab9a9279a8420a1e6b56b7c.jsonl[5705] _id=6ac862ffde269131f9c7da52 ts=2026-10-09T03:43:58.4510000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5716] _id=6ace7ac2de269131f9d10467 ts=2026-10-13T18:38:52.3280000Z; 54h 22m: 6ab9a9279a8420a1e6b56b7c.jsonl[14797] _id=6ad57033de269131f9e910e5 ts=2026-10-16T18:58:16.334Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14803] _id=6ad57059de269131f9e91122 ts=2026-10-19T01:20:21.7530000Z; 47h 32m: 6ab9a9279a8420a1e6b56b7c.jsonl[1214] _id=6ac54965de269131f9b79cb5 ts=2026-10-06T19:17:57.3760000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1222] _id=6ac7e5d9de269131f9c58fe5 ts=2026-10-08T18:49:57.8430000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[14783] _id=6ad273c8de269131f9e78339 ts=2026-10-16T18:58:16.3340000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14797] _id=6ad57033de269131f9e910e5 ts=2026-10-16T18:58:16.334Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 110h 55m 
  - Evidence: 110h 55m: 6ab9a9279a8420a1e6b56b7c.jsonl[5701] _id=6ac862d8de269131f9c7d9da ts=2026-10-09T03:43:18.3220000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5727] _id=6ace7ac3de269131f9d1047c ts=2026-10-13T18:38:57.0920000Z; 24h 5m: 6ab9a9279a8420a1e6b56b7c.jsonl[5779] _id=6ace7ad7de269131f9d1062f ts=2026-10-13T18:39:18.2550000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6379] _id=6acfcd91de269131f9d773f6 ts=2026-10-14T18:44:32.9660000Z; 19h 46m: 6ab9a9279a8420a1e6b56b7c.jsonl[12329] _id=6ad132a1de269131f9e11715 ts=2026-10-15T20:07:58.5550000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[12526] _id=6ad248b1de269131f9e566cb ts=2026-10-16T15:54:24.7930000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1933 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[10292] _id=6ad11eb1de269131f9df2348 ts=2026-10-15T18:42:56.5620000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[10293] _id=6ad11eb1de269131f9df234b ts=2026-10-15T18:42:56.5620000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[10312] _id=6ad11eb8de269131f9df245e ts=2026-10-15T18:43:02.2840000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[10397] _id=6ad11eb8de269131f9df2462 ts=2026-10-15T18:43:02.2840000Z; 0ms: 6ab9a9279a8420a1e6b56b7c.jsonl[10313] _id=6ad11eb8de269131f9df2467 ts=2026-10-15T18:43:02.3000000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[10550] _id=6ad11eb9de269131f9df2478 ts=2026-10-15T18:43:02.3000000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 2m 
  - Evidence: 143h 2m: 6ab9a9279a8420a1e6b56b7c.jsonl[4539] _id=6ac85fffde269131f9c7cb44 ts=2026-10-09T03:31:10.3860000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7983] _id=6ad03b8ade269131f9da41c6 ts=2026-10-15T02:33:46.1010000Z; 16h 7m: 6ab9a9279a8420a1e6b56b7c.jsonl[7962] _id=6ad03ba9de269131f9da4201 ts=2026-10-15T02:34:16.7790000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[10355] _id=6ad11e5cde269131f9df1765 ts=2026-10-15T18:41:31.9060000Z; 8h 22m: 6ab9a9279a8420a1e6b56b7c.jsonl[3487] _id=6ac7e9edde269131f9c63623 ts=2026-10-08T19:07:24.3860000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[4526] _id=6ac85fc9de269131f9c7caa4 ts=2026-10-09T03:30:16.5300000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 54h 25m 
  - Evidence: 54h 25m: 6ab9a9279a8420a1e6b56b7c.jsonl[14756] _id=6ad2736fde269131f9e77cb9 ts=2026-10-16T18:56:47.4740000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14852] _id=6ad570c1de269131f9e91210 ts=2026-10-19T01:22:08.5280000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 111h 46m 
  - Evidence: 111h 46m: 6ab9a9279a8420a1e6b56b7c.jsonl[4404] _id=6ac85e53de269131f9c7c727 ts=2026-10-09T03:24:02.7390000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5983] _id=6ace822fde269131f9d17ea5 ts=2026-10-13T19:10:39.2260000Z; 23h 31m: 6ab9a9279a8420a1e6b56b7c.jsonl[5987] _id=6ace823ede269131f9d18102 ts=2026-10-13T19:10:54.4470000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6283] _id=6acfcd19de269131f9d762c0 ts=2026-10-14T18:42:32.6580000Z; 20h 55m: 6ab9a9279a8420a1e6b56b7c.jsonl[7045] _id=6acfd3aede269131f9d83515 ts=2026-10-14T19:10:38.4600000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[9692] _id=6ad0f9e7de269131f9dd30dc ts=2026-10-15T16:05:58.6460000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.038s shown 
  - Evidence: 20ms: 6ab9a9279a8420a1e6b56b7c.jsonl[3658] _id=6ac7ebacde269131f9c67388 ts=2026-10-08T19:14:51.9540000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[3662] _id=6ac7ebacde269131f9c6738c ts=2026-10-08T19:14:51.9740000Z; 38ms: 6ab9a9279a8420a1e6b56b7c.jsonl[3657] _id=6ac7ebacde269131f9c67386 ts=2026-10-08T19:14:51.9160000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[3658] _id=6ac7ebacde269131f9c67388 ts=2026-10-08T19:14:51.9540000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 47m 
  - Evidence: 191h 47m: 6ab9a9279a8420a1e6b56b7c.jsonl[961] _id=6ac5471ade269131f9b76035 ts=2026-10-06T19:08:10.5010000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6706] _id=6acfd01cde269131f9d7ba1d ts=2026-10-14T18:55:23.6530000Z; 37h 39m: 6ab9a9279a8420a1e6b56b7c.jsonl[7874] _id=6ad03a99de269131f9da406d ts=2026-10-15T02:29:45.1840000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13045] _id=6ad24c3cde269131f9e5a0fd ts=2026-10-16T16:09:31.9810000Z; 7h 28m: 6ab9a9279a8420a1e6b56b7c.jsonl[6860] _id=6acfd0f6de269131f9d7d2c9 ts=2026-10-14T18:59:02.4310000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7698] _id=6ad03a02de269131f9da3f56 ts=2026-10-15T02:27:14.3440000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 191h 46m 
  - Evidence: 191h 46m: 6ab9a9279a8420a1e6b56b7c.jsonl[956] _id=6ac5471ade269131f9b7603b ts=2026-10-06T19:08:10.5210000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6697] _id=6acfd00dde269131f9d7b889 ts=2026-10-14T18:55:09.2840000Z; 37h 39m: 6ab9a9279a8420a1e6b56b7c.jsonl[7886] _id=6ad03a99de269131f9da4072 ts=2026-10-15T02:29:45.2740000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13015] _id=6ad24c13de269131f9e59dff ts=2026-10-16T16:08:51.2500000Z; 7h 27m: 6ab9a9279a8420a1e6b56b7c.jsonl[6861] _id=6acfd0f6de269131f9d7d2cc ts=2026-10-14T18:59:02.4500000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7714] _id=6ad039c2de269131f9da3ed4 ts=2026-10-15T02:26:10.2040000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.024s..0.039s shown 
  - Evidence: 24ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13757] _id=6ad2592cde269131f9e66128 ts=2026-10-16T17:04:44.4460000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13760] _id=6ad2592cde269131f9e6612b ts=2026-10-16T17:04:44.4700000Z; 39ms: 6ab9a9279a8420a1e6b56b7c.jsonl[14485] _id=6ad27155de269131f9e75373 ts=2026-10-16T18:47:48.7900000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14488] _id=6ad27155de269131f9e75376 ts=2026-10-16T18:47:48.8290000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 46m 
  - Evidence: 191h 46m: 6ab9a9279a8420a1e6b56b7c.jsonl[959] _id=6ac54718de269131f9b7600d ts=2026-10-06T19:08:08.0690000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6694] _id=6acfd00bde269131f9d7b866 ts=2026-10-14T18:55:07.2140000Z; 37h 39m: 6ab9a9279a8420a1e6b56b7c.jsonl[7873] _id=6ad03a97de269131f9da406b ts=2026-10-15T02:29:43.6460000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13006] _id=6ad24c10de269131f9e59dc5 ts=2026-10-16T16:08:48.2270000Z; 7h 27m: 6ab9a9279a8420a1e6b56b7c.jsonl[6858] _id=6acfd0f5de269131f9d7d296 ts=2026-10-14T18:59:01.0100000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7716] _id=6ad039c9de269131f9da3ee2 ts=2026-10-15T02:26:17.1340000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 109 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b7c.jsonl[7808] _id=6ad03a4bde269131f9da3fe8 ts=2026-10-15T02:28:26.7580000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7809] _id=6ad03a4bde269131f9da3fe9 ts=2026-10-15T02:28:26.7590000Z; 5ms: 6ab9a9279a8420a1e6b56b7c.jsonl[13806] _id=6ad25822de269131f9e65360 ts=2026-10-16T17:00:18.1520000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[13808] _id=6ad25822de269131f9e65362 ts=2026-10-16T17:00:18.1570000Z; 5ms: 6ab9a9279a8420a1e6b56b7c.jsonl[14354] _id=6ad27037de269131f9e73d92 ts=2026-10-16T18:43:03.2280000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14350] _id=6ad27037de269131f9e73d96 ts=2026-10-16T18:43:03.2330000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 48m 
  - Evidence: 191h 48m: 6ab9a9279a8420a1e6b56b7c.jsonl[915] _id=6ac546f2de269131f9b75a31 ts=2026-10-06T19:07:30.4000000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[6754] _id=6acfd059de269131f9d7c138 ts=2026-10-14T18:56:25.4330000Z; 7h 31m: 6ab9a9279a8420a1e6b56b7c.jsonl[6754] _id=6acfd059de269131f9d7c138 ts=2026-10-14T18:56:25.4330000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7793] _id=6ad03a37de269131f9da3fcc ts=2026-10-15T02:28:07.6090000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 111h 4m 
  - Evidence: 111h 4m: 6ab9a9279a8420a1e6b56b7c.jsonl[4603] _id=6ac860abde269131f9c7cd7e ts=2026-10-09T03:34:02.1940000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5714] _id=6ace7a9ade269131f9d101a6 ts=2026-10-13T18:38:18.4990000Z; 54h 25m: 6ab9a9279a8420a1e6b56b7c.jsonl[14682] _id=6ad272f6de269131f9e77356 ts=2026-10-16T18:54:45.7320000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14802] _id=6ad57033de269131f9e910e9 ts=2026-10-19T01:19:46.5040000Z; 47h 36m: 6ab9a9279a8420a1e6b56b7c.jsonl[1099] _id=6ac54840de269131f9b775e9 ts=2026-10-06T19:13:04.1490000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1220] _id=6ac7e5cbde269131f9c58e7c ts=2026-10-08T18:49:46.3760000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 111h 4m 
  - Evidence: 111h 4m: 6ab9a9279a8420a1e6b56b7c.jsonl[4602] _id=6ac860abde269131f9c7cd7d ts=2026-10-09T03:34:02.1940000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5713] _id=6ace7a9ade269131f9d101a5 ts=2026-10-13T18:38:18.4990000Z; 54h 25m: 6ab9a9279a8420a1e6b56b7c.jsonl[14681] _id=6ad272f6de269131f9e77355 ts=2026-10-16T18:54:45.7320000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14790] _id=6ad57033de269131f9e910e8 ts=2026-10-19T01:19:46.5040000Z; 47h 36m: 6ab9a9279a8420a1e6b56b7c.jsonl[1098] _id=6ac54840de269131f9b775dd ts=2026-10-06T19:13:04.1480000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1219] _id=6ac7e5cbde269131f9c58e7b ts=2026-10-08T18:49:46.3760000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 111h 14m 
  - Evidence: 111h 14m: 6ab9a9279a8420a1e6b56b7c.jsonl[4649] _id=6ac86089de269131f9c7cd1d ts=2026-10-09T03:33:28.5300000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5875] _id=6ace7cd6de269131f9d125d1 ts=2026-10-13T18:47:49.8490000Z; 47h 59m: 6ab9a9279a8420a1e6b56b7c.jsonl[1217] _id=6ac7e5cbde269131f9c58e76 ts=2026-10-06T19:18:03.792Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[3765] _id=6ac85732de269131f9c7b90b ts=2026-10-08T19:17:57.769Z; 23h 59m: 6ab9a9279a8420a1e6b56b7c.jsonl[6130] _id=6acfcb5fde269131f9d72247 ts=2026-10-13T19:18:11.528Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[7194] _id=6ad036cede269131f9da37ca ts=2026-10-14T19:18:02.783Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 110h 55m 
  - Evidence: 110h 55m: 6ab9a9279a8420a1e6b56b7c.jsonl[5704] _id=6ac862f6de269131f9c7da25 ts=2026-10-09T03:43:49.5830000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[5719] _id=6ace7ac2de269131f9d1046a ts=2026-10-13T18:38:57.1010000Z; 54h 25m: 6ab9a9279a8420a1e6b56b7c.jsonl[14686] _id=6ad27300de269131f9e773fb ts=2026-10-16T18:54:56.0380000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[14804] _id=6ad57059de269131f9e91123 ts=2026-10-19T01:20:23.3310000Z; 47h 34m: 6ab9a9279a8420a1e6b56b7c.jsonl[1139] _id=6ac548c5de269131f9b78824 ts=2026-10-06T19:15:17.7550000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[1223] _id=6ac7e5d9de269131f9c58fe6 ts=2026-10-08T18:50:00.4110000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.002s..0.005s shown 
  - Evidence: 2ms: 6ab9a9279a8420a1e6b56b7c.jsonl[854] _id=6ac5464dde269131f9b73f74 ts=2026-10-06T19:04:45.4330000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[837] _id=6ac5464ede269131f9b73f79 ts=2026-10-06T19:04:45.4350000Z; 3ms: 6ab9a9279a8420a1e6b56b7c.jsonl[4669] _id=6ac860bbde269131f9c7cdbe ts=2026-10-09T03:34:16.8220000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[4670] _id=6ac860bbde269131f9c7cdbf ts=2026-10-09T03:34:16.8250000Z; 5ms: 6ab9a9279a8420a1e6b56b7c.jsonl[11432] _id=6ad12277de269131f9dfa192 ts=2026-10-15T18:59:03.4160000Z -> 6ab9a9279a8420a1e6b56b7c.jsonl[11429] _id=6ad12278de269131f9dfa19b ts=2026-10-15T18:59:03.4210000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[843] _id=6ac54633de269131f9b73bed ts=2026-10-06T19:04:19.6990000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[969] _id=6ac5472fde269131f9b761b9 ts=2026-10-06T19:08:31.2780000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[5614] _id=6ac862bdde269131f9c7d8ff ts=2026-10-09T03:42:52.3040000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[7886] _id=6ad03a99de269131f9da4072 ts=2026-10-15T02:29:45.2740000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[14488] _id=6ad27155de269131f9e75376 ts=2026-10-16T18:47:48.8290000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[874] _id=6ac546a9de269131f9b74daf ts=2026-10-06T19:06:16.2760000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[913] _id=6ac546f8de269131f9b75adb ts=2026-10-06T19:07:35.8550000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[942] _id=6ac5470ade269131f9b75dfe ts=2026-10-06T19:07:53.7790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[5726] _id=6ace7ac2de269131f9d10465 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 136 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[4779] _id=6ac86122de269131f9c7cf3f ts=2026-10-09T03:35:59.4250000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[4822] _id=6ac86129de269131f9c7cf85 ts=2026-10-09T03:36:05.4430000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[4795] _id=6ac8612ade269131f9c7cf9f ts=2026-10-09T03:36:08.8930000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 139 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[1301] _id=6ac7e66dde269131f9c5a40d ts=2026-10-08T18:52:27.3080000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[1302] _id=6ac7e66dde269131f9c5a40f ts=2026-10-08T18:52:27.3080000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[1299] _id=6ac7e66dde269131f9c5a416 ts=2026-10-08T18:52:27.3080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[13235] _id=6ad2550ede269131f9e616f8 ts=2026-10-16T16:47:10.6320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'DialogueStartEvent' (totals: 484 start, 468 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 9 unmatched 'BecameCameraCentered' (totals: 773 open, 764 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 18 unmatched 'BecameVisible' (totals: 1233 open, 1215 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 4 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 54 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 480 of 15119 adjacent _id pairs reverse in client time; worst 236.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b7c.jsonl[1435] _id=6ac7e748de269131f9c5bf75 ts=2026-10-08T18:56:07.5720000Z`; `6ab9a9279a8420a1e6b56b7c.jsonl[1437] _id=6ac7e749de269131f9c5bf9a ts=2026-10-08T18:52:10.7220000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.59s, min -195691.00s, max -0.10s over 15120 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7c\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

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

### `InputEvent` — 4549 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1213); Unit 3 Dungeon Dev (836); Unit 4 Dev (700); Unit 4 Dev - Dungeon (681); Unit 3 Dev (523); Unit 1 Dev (488); Unit 4 Dev - Anderson Base (108)
- **Intervals:** median 0.91s (p5 0.12s / p95 13.76s, n=4548)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4549/4549 records)
    "pressed"  x4549
data.actionType  (string, 4549/4549 records)
    "Move"  x3632
    "Interact"  x561
    "Jump"  x235
    "Ascend"  x58
    "Hoverboard"  x46
    "Map"  x8
    "Descend"  x5
    "Pause"  x2
    "ToggleDebug"  x2
data.key  (string, 4549/4549 records, 7 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4549/4549 records)
    "Player"  x3906
    "Drone"  x643
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3985 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2788); Unit 4 Dev (622); Unit 3 Dungeon Dev (575)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.70s, n=3984)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3985/3985 records)
    "BecameVisible"  x1233
    "BecameInvisible"  x1215
    "BecameCameraCentered"  x773
    "BecameCameraUncentered"  x764
data.pieceId  (string, 3985/3985 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3985/3985 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2530 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (734); Unit 4 Dev - Anderson Base (439); Unit 4 Dev (428); Unit 3 Dev (368); Unit 1 Dev (249); Unit 3 Dungeon Dev (218); Unit 4 Dev - Dungeon (94)
- **eventKey:** present on 1578 of 2530 records
- **Intervals:** median 4.38s (p5 0.00s / p95 32.17s, n=2529)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1578; [conversationId, dialogueEventType] x952
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2530/2530 records)
    numeric range 8 .. 114 (46 unique)
data.dialogueEventType  (string, 2530/2530 records)
    "DialogueNodeEvent"  x1578
    "DialogueStartEvent"  x484
    "DialogueFinishEvent"  x468
data.nodeId  (number, 1578/2530 records)
    numeric range 0 .. 290 (229 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2276 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (791); Unit 4 Dev (321); Unit 4 Dev - Anderson Base (286); Unit 3 Dev (281); Unit 1 Dev (253); Unit 3 Dungeon Dev (197); Unit 4 Dev - Dungeon (147)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=2266)
- **Fields under `data`:**

```text
data.position  (object, 2276/2276 records)
data.position.x  (number, 2276/2276 records)
    numeric range -736.906 .. 1557.17 (798 unique)
data.position.y  (number, 2276/2276 records)
    numeric range -114.337 .. 232.105 (606 unique)
data.position.z  (number, 2276/2276 records)
    numeric range -1268.36 .. 2284.81 (796 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 926 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (675); Unit 3 Dev (107); Unit 2 Prod (Refactor) (99); Unit 1 Dev (45)
- **Intervals:** median 0.45s (p5 0.04s / p95 13.52s, n=925)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 926/926 records)
    "argumentationNodeHoverEnd"  x382
    "argumentationNodeHoverStart"  x378
    "argumentationNodeAdd"  x94
    "argumentationNodeRemove"  x72
data.argumentationTitle  (string, 926/926 records)
    "Unit 4 - Flooding"  x675
    "Unit 3 - Pollution Upstream"  x107
    "Unit 2 – Watershed"  x99
    "Unit 1 - Freshwater"  x31
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 926/926 records)
    "B"  x132
    "C"  x122
    "A"  x100
    "3"  x94
    "2"  x87
    "D"  x87
    "4"  x80
    "II"  x76
    "1"  x73
    "I"  x70
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 356 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (95); Unit 2 Prod (Refactor) (88); Unit 3 Dungeon Dev (69); Unit 4 Dev (45); Unit 4 Dev - Anderson Base (27); Unit 1 Dev (20); Unit 3 Dev (12)
- **Intervals:** median 10.32s (p5 0.18s / p95 403.87s, n=355)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 356/356 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 356/356 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationAnswerEvent` — 123 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (101); Unit 2 Prod (Refactor) (9); Unit 3 Dev (7); Unit 1 Dev (6)
- **Intervals:** median 12.69s (p5 1.88s / p95 117.25s, n=122)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 123/123 records)
    "submitAnswerEvent"  x123
data.answerSubmitted  (string, 123/123 records)
    50 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 123/123 records)
    "Unit 4 - Flooding"  x101
    "Unit 2 – Watershed"  x9
    "Unit 3 - Pollution Upstream"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `questEvent` — 86 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 1 Dev (18); Unit 4 Dev (16); Unit 3 Dev (12); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (4)
- **eventKey:** present on 86 of 86 records
- **Intervals:** median 254.00s (p5 0.01s / p95 81160.94s, n=85)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Fields under `data`:**

```text
data.questEventType  (string, 86/86 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x32
data.questID  (string, 86/86 records)
    27 unique values (see csv/event_unique_values.csv)
data.questName  (string, 86/86 records)
    27 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/86 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 49 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (20); Unit 2 Prod (Refactor) (7); Unit 4 Dev (7); Unit 3 Dev (4); Unit 3 Dungeon Dev (4); Unit 1 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 971.95s (p5 9.35s / p95 141567.55s, n=48)
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "DebugMenuStateChanged"  x49
data.isOpened  (bool, 49/49 records)
    false  x49
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `Soil Key Puzzle` — 48 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (16); Unit 4 Dev (4)
- **Intervals:** median 1.40s (p5 0.22s / p95 21126.29s, n=47)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x40; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/48 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/48 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 40/48 records)
    "RightDrag"  x23
    "LeftDrag"  x17
data.currentSoilType  (string, 40/48 records)
    "CLAYSAND"  x10
    "CLAY"  x9
    "SAND"  x8
    "CLAYROCK"  x5
    "SANDGRAVEL"  x5
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 40/48 records)
    "false"  x30
    "true"  x10
data.waterLevelStatus  (string, 40/48 records)
    "TooHigh"  x25
    "Proper"  x14
    "TooLow"  x1
data.waterRetentionChange  (string, 40/48 records)
    "Increase"  x16
    "Decrease"  x14
    "NoChange"  x10
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 39 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (35); Unit 3 Dev (2); Unit 3 Dungeon Dev (2)
- **Intervals:** median 9.62s (p5 0.39s / p95 76726.89s, n=38)
- **`data` key-set variants:** [actionType, featureUsed] x26; [actionType, featureUsed, location] x13
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "MapCloseEvent"  x13
    "MapOpenEvent"  x13
    "WaypointMoveEvent"  x8
    "WaypointSetEvent"  x5
data.featureUsed  (string, 39/39 records)
    "Map"  x26
    "Waypoint"  x13
data.location  (object, 13/39 records)
data.location.x  (number, 13/39 records)
    numeric range -264.581 .. 65.807 (13 unique)
data.location.y  (number, 13/39 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 13/39 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 32 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (24); Unit 2 Prod (Refactor) (5); Unit 3 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2867.61s (p5 67.39s / p95 183651.50s, n=31)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 32/32 records)
    true  x32
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 27 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (27)
- **Intervals:** median 4.78s (p5 1.29s / p95 121.93s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "ChangeCanister"  x27
data.canisterType  (string, 27/27 records)
    "Bedrock"  x11
    "Clay"  x9
    "Gravel"  x4
    "Sand"  x3
data.floor  (string, 27/27 records)
    "5"  x17
    "4"  x9
    "3"  x1
data.machine  (string, 27/27 records)
    "1"  x26
    "2"  x1
data.row  (string, 27/27 records)
    "TopRow"  x20
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameStartEvent` — 24 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (24)
- **Intervals:** median 5342.88s (p5 992.29s / p95 193450.92s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 20 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (20)
- **Intervals:** median 8.54s (p5 1.05s / p95 19777.07s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records, 7 empty-string)
    "cameraPlaced"  x13
    ""  x7
data.boxId  (string, 20/20 records)
    "1"  x8
    "2"  x7
    "0"  x5
data.soilType  (string, 20/20 records)
    "None"  x7
    "Sand"  x5
    "Clay"  x4
    "Gravel"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 1 Dev (2); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 9707.65s (p5 38.20s / p95 206944.08s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (7); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 233.17s (p5 0.03s / p95 302007.81s, n=15)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 16/16 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x7
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 4 - Flooding"  x7
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 13590.58s (p5 13.22s / p95 591020.10s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4)
- **Intervals:** median 3.86s (p5 3.28s / p95 15.45s, n=3)
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
- **Intervals:** median 289992.60s (p5 99943.72s / p95 650682.49s, n=3)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 7.30s (p5 7.30s / p95 7.30s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[23-36, 23-38, 23-40, 23-41, 23-42]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

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
    "unit2"  x1
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
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (28 records)
- `TerasGardenBox` data.actionType: "" (7x)
- `TerasGardenBox` data.soilType: "None" (7x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (8x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (72x)
- `soilMachine` data.canisterType: "Bedrock" (11x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*