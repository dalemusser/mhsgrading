# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae3

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae3
- **Game version string(s) in log:** 2.8.1, 2.8.4, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae3.jsonl
- **Records:** 11850 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae3
- **Time span:** 2026-10-06T13:17:49.041000+00:00 .. 2026-10-16T13:59:39.369000+00:00 (240h 41m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae3\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 11850 records, 8 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 99 INFO, 2 NOT_TESTED, 83 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3721 | 31.4 | 1 | 7 | 0 | 2026-10-06T13:18:23.819000+00:00 | 2026-10-16T13:59:39.369000+00:00 | 240h 41m |
| PuzzlePieceVisibleEvent | 2692 | 22.72 | 1 | 3 | 0 | 2026-10-07T13:31:55.722000+00:00 | 2026-10-16T13:55:24.041000+00:00 | 216h 23m |
| PlayerPositionEvent | 2136 | 18.03 | 1 | 7 | 0 | 2026-10-06T13:18:04.812000+00:00 | 2026-10-16T13:59:36.349000+00:00 | 240h 41m |
| DialogueEvent | 2038 | 17.2 | 1 | 7 | 1301 | 2026-10-06T13:18:24.725000+00:00 | 2026-10-16T13:59:34.183000+00:00 | 240h 41m |
| ObjectInterEvent | 398 | 3.36 | 1 | 7 | 0 | 2026-10-06T13:26:14.725000+00:00 | 2026-10-16T13:58:45.799000+00:00 | 240h 32m |
| argumentationNodeEvent | 306 | 2.58 | 1 | 4 | 0 | 2026-10-06T13:50:49.460000+00:00 | 2026-10-16T13:44:56.337000+00:00 | 239h 54m |
| TopographicMapEvent | 166 | 1.4 | 1 | 2 | 0 | 2026-10-07T13:33:18.295000+00:00 | 2026-10-15T16:03:00.866000+00:00 | 194h 29m |
| soilMachine | 103 | 0.87 | 1 | 1 | 0 | 2026-10-15T22:18:50.270000+00:00 | 2026-10-16T13:22:39.219000+00:00 | 15h 3m |
| questEvent | 81 | 0.68 | 1 | 7 | 81 | 2026-10-06T13:18:24.699000+00:00 | 2026-10-16T13:58:30.931000+00:00 | 240h 40m |
| Soil Key Puzzle | 58 | 0.49 | 1 | 3 | 0 | 2026-10-07T13:37:05.730000+00:00 | 2026-10-16T13:25:30.981000+00:00 | 215h 48m |
| DEBUGMenu | 46 | 0.39 | 1 | 8 | 0 | 2026-10-06T13:18:04.794000+00:00 | 2026-10-16T13:55:45.734000+00:00 | 240h 37m |
| gameWindowFocusEvent | 24 | 0.2 | 1 | 4 | 0 | 2026-10-06T13:17:49.041000+00:00 | 2026-10-16T13:50:40.291000+00:00 | 240h 32m |
| gameStartEvent | 20 | 0.17 | 1 | 1 | 0 | 2026-10-06T13:17:49.042000+00:00 | 2026-10-16T13:50:40.291000+00:00 | 240h 32m |
| argumentationAnswerEvent | 19 | 0.16 | 1 | 4 | 0 | 2026-10-06T13:52:45.724000+00:00 | 2026-10-16T13:45:00.175000+00:00 | 239h 52m |
| argumentationEvent | 12 | 0.1 | 1 | 4 | 0 | 2026-10-06T13:50:39.704000+00:00 | 2026-10-16T13:45:00.230000+00:00 | 239h 54m |
| gameWindowUnfocusEvent | 12 | 0.1 | 1 | 4 | 0 | 2026-10-06T14:00:03.305000+00:00 | 2026-10-16T13:50:17.644000+00:00 | 239h 50m |
| crash | 6 | 0.05 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-14T13:18:55.673000+00:00 | 2026-10-15T22:29:06.314000+00:00 | 33h 10m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-06T13:56:48.860000+00:00 | 2026-10-15T16:10:27.130000+00:00 | 218h 13m |
| TerasGardenBox | 3 | 0.03 | 1 | 1 | 0 | 2026-10-16T13:48:53.810000+00:00 | 2026-10-16T13:49:45.277000+00:00 | 51.5s |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T13:50:39.559000+00:00 | 2026-10-06T13:50:42.001000+00:00 | 2.4s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 392809.135s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.288s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.078s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 25.733s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.065s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 23.528s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.442s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 7789.876s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2373.35s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 55050.965s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 0.863s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.8x vs baseline. 
  - Observed: 46 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
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
  - Observed: 180 ft; 210 ft; 270 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,D,1,II; B,2,II; B,A,C,2,II; C,2,II; C,B,2,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 20.6x vs baseline. 
  - Observed: 103 records 
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
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[191] _id=6ac4f77ade269131f9b091f3 ts=2026-10-06T13:28:25.8440000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[252] _id=6ac4f889de269131f9b0c5b6 ts=2026-10-06T13:32:56.7600000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[330] _id=6ac4fa43de269131f9b11368 ts=2026-10-06T13:40:18.7100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[2] _id=6ac4f4fdde269131f9b038f0 ts=2026-10-06T13:17:49.0420000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[677] _id=6ac4fe79de269131f9b221e7 ts=2026-10-06T13:58:16.7800000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[699] _id=6ac64863de269131f9b8f74b ts=2026-10-07T13:25:53.7850000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[1] _id=6ac4f4fdde269131f9b038ee ts=2026-10-06T13:17:49.0410000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[678] _id=6ac4fe79de269131f9b221d9 ts=2026-10-06T13:58:16.7790000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[698] _id=6ac64863de269131f9b8f74a ts=2026-10-07T13:25:53.7850000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[700] _id=6ac64863de269131f9b8f741 ts=2026-10-06T14:00:03.305Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[2361] _id=6ac79aa7de269131f9c03910 ts=2026-10-07T13:59:49.195Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[3418] _id=6ace2f68de269131f9ce8fb7 ts=2026-10-08T13:59:17.478Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 14 of 166 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[1021] _id=6ac64a1fde269131f9b96878 ts=2026-10-07T13:33:18.2950000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[1024] _id=6ac64a22de269131f9b9696e ts=2026-10-07T13:33:21.6320000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[1023] _id=6ac64a23de269131f9b969b1 ts=2026-10-07T13:33:22.4810000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3720 | 0.0 | 1.288 | 232.924 | 16.582 | 429934.596 | 0.26 | 55 | 14 |
| PuzzlePieceVisibleEvent | 2691 | 0.0 | 0.078 | 289.487 | 2.613 | 429951.19 | 0.21 | 1081 | 10 |
| PlayerPositionEvent | 2123 | 0.0 | 10.003 | 407.957 | 10.371 | 429517.336 | 0.15 | 2 | 12 |
| DialogueEvent | 2037 | 0.0 | 4.272 | 425.365 | 38.662 | 429523.702 | 0.14 | 596 | 12 |
| ObjectInterEvent | 397 | 0.0 | 8.76 | 2181.237 | 262.614 | 516792.999 | 0.03 | 3 | 12 |
| argumentationNodeEvent | 305 | 0.008 | 0.688 | 2831.629 | 13.847 | 689932.743 | 0.02 | 38 | 3 |
| TopographicMapEvent | 165 | 0.018 | 4.065 | 4243.531 | 386.535 | 460083.439 | 0.01 | 2 | 8 |
| soilMachine | 102 | 0.141 | 0.863 | 531.656 | 90.781 | 52826.158 | 0.11 | 0 | 1 |
| questEvent | 80 | 0.003 | 197.204 | 10830.078 | 58299.514 | 429716.45 | 0.01 | 11 | 20 |
| Soil Key Puzzle | 57 | 0.148 | 1.414 | 13629.917 | 34593.071 | 604164.031 | 0.0 | 0 | 5 |
| DEBUGMenu | 45 | 8.503 | 482.896 | 19250.243 | 84602.873 | 431285.594 | 0.0 | 0 | 20 |
| gameWindowFocusEvent | 23 | 10.715 | 2373.35 | 37650.924 | 86402.779 | 431296.803 | 0.0 | 0 | 18 |
| gameStartEvent | 19 | 80.191 | 7789.876 | 45577.434 | 121067.282 | 431296.802 | 0.0 | 0 | 17 |
| argumentationAnswerEvent | 18 | 5.11 | 23.528 | 47974.136 | 177448.485 | 690007.953 | 0.0 | 0 | 3 |
| argumentationEvent | 11 | 0.034 | 80.68 | 78514.593 | 388446.968 | 689939.418 | 0.0 | 2 | 3 |
| gameWindowUnfocusEvent | 11 | 9.875 | 55050.965 | 78492.213 | 260991.721 | 429691.413 | 0.0 | 0 | 10 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 3 | 1.558 | 2.965 | 39803.547 | 107465.803 | 119406.118 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 95526.549 | 392809.135 | 392809.135 | 660363.462 | 690091.721 | 0.0 | 0 | 2 |
| TerasGardenBox | 2 | 22.883 | 25.733 | 25.733 | 28.299 | 28.584 | 2.33 | 0 | 0 |
| argumentationToolEvent | 1 | 2.442 | 2.442 | 2.442 | 2.442 | 2.442 | 24.57 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[3778] _id=6ace3700de269131f9cee202 ts=2026-10-13T13:49:50.5800000Z == 6ab9a88e9a8420a1e6b56ae3.jsonl[3779] _id=6ace3700de269131f9cee203 ts=2026-10-13T13:49:50.5800000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 48 group(s), 83 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[976] _id=6ac649f9de269131f9b95de1 ts=2026-10-07T13:32:38.9300000Z == 6ab9a88e9a8420a1e6b56ae3.jsonl[969] _id=6ac649f9de269131f9b95de5 ts=2026-10-07T13:32:38.9300000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[970] _id=6ac649fade269131f9b95e13 ts=2026-10-07T13:32:39.1460000Z == 6ab9a88e9a8420a1e6b56ae3.jsonl[981] _id=6ac649fade269131f9b95e29 ts=2026-10-07T13:32:39.1460000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[962] _id=6ac649fcde269131f9b95eb3 ts=2026-10-07T13:32:41.0040000Z == 6ab9a88e9a8420a1e6b56ae3.jsonl[988] _id=6ac649fcde269131f9b95ec9 ts=2026-10-07T13:32:41.0040000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[7936] _id=6ad11989de269131f9dee542 ts=? == 6ab9a88e9a8420a1e6b56ae3.jsonl[11449] _id=6ad22bbade269131f9e41422 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 97 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[147] _id=6ac4f6f7de269131f9b081b7 ts=2026-10-06T13:26:14.7250000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[148] _id=6ac4f6f7de269131f9b081be ts=2026-10-06T13:26:14.7370000Z`; `946ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[798] _id=6ac64971de269131f9b93970 ts=2026-10-07T13:30:25.0940000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[796] _id=6ac64972de269131f9b939c0 ts=2026-10-07T13:30:26.0400000Z`; `479ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[796] _id=6ac64972de269131f9b939c0 ts=2026-10-07T13:30:26.0400000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[809] _id=6ac64973de269131f9b939ed ts=2026-10-07T13:30:26.5190000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `645ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[1031] _id=6ac64a36de269131f9b96eb9 ts=2026-10-07T13:33:41.1580000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[1016] _id=6ac64a36de269131f9b96edc ts=2026-10-07T13:33:41.8030000Z`; `374ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[1006] _id=6ac64a36de269131f9b96ece ts=2026-10-07T13:33:41.6170000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[1017] _id=6ac64a36de269131f9b96ee8 ts=2026-10-07T13:33:41.9910000Z`; `381ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[1016] _id=6ac64a36de269131f9b96edc ts=2026-10-07T13:33:41.8030000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[1014] _id=6ac64a37de269131f9b96ef2 ts=2026-10-07T13:33:42.1840000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[6379] _id=6ad0d4e4de269131f9da91c8 ts=2026-10-15T13:28:03.6750000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[6382] _id=6ad0d4e4de269131f9da91cb ts=2026-10-15T13:28:03.7090000Z`; `37ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[11271] _id=6ad22a5cde269131f9e3ec0d ts=2026-10-16T13:45:00.1930000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[11274] _id=6ad22a5cde269131f9e3ec10 ts=2026-10-16T13:45:00.2300000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `44ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[480] _id=6ac4fcbbde269131f9b1a648 ts=2026-10-06T13:50:50.4220000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[481] _id=6ac4fcbbde269131f9b1a64d ts=2026-10-06T13:50:50.4660000Z`; `38ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[485] _id=6ac4fcbede269131f9b1a73a ts=2026-10-06T13:50:53.8600000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[486] _id=6ac4fcbede269131f9b1a744 ts=2026-10-06T13:50:53.8980000Z`; `662ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[5246] _id=6acf845cde269131f9d324b0 ts=2026-10-14T13:32:11.9410000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[5244] _id=6acf845dde269131f9d324bc ts=2026-10-14T13:32:12.6030000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 52 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `497ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[9760] _id=6ad1532ede269131f9e1d417 ts=2026-10-15T22:26:52.9400000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[9761] _id=6ad1532ede269131f9e1d41e ts=2026-10-15T22:26:53.4370000Z`; `804ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[9766] _id=6ad1533bde269131f9e1d433 ts=2026-10-15T22:27:06.6220000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[9775] _id=6ad1533cde269131f9e1d438 ts=2026-10-15T22:27:07.4260000Z`; `189ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[9775] _id=6ad1533cde269131f9e1d438 ts=2026-10-15T22:27:07.4260000Z ~ 6ab9a88e9a8420a1e6b56ae3.jsonl[9767] _id=6ad1533cde269131f9e1d43d ts=2026-10-15T22:27:07.6150000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2365] _id=6ac79ab2de269131f9c03a8a ts=2026-10-08T13:29:22.1740000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3415] _id=6ace2f68de269131f9ce8fbb ts=2026-10-13T13:17:27.7680000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae3.jsonl[702] _id=6ac6486dde269131f9b8f911 ts=2026-10-07T13:26:04.3590000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2362] _id=6ac79aa7de269131f9c0391b ts=2026-10-08T13:29:10.9850000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5645] _id=6acf8802de269131f9d36297 ts=2026-10-14T13:47:45.6110000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5991] _id=6ad0d2a3de269131f9da5d89 ts=2026-10-15T13:18:27.4260000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 33h 10m 
  - Evidence: 33h 10m: 6ab9a88e9a8420a1e6b56ae3.jsonl[4734] _id=6acf8141de269131f9d2e3fc ts=2026-10-14T13:18:57.2310000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[9916] _id=6ad153b0de269131f9e1d607 ts=2026-10-15T22:29:03.3490000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3406] _id=6ac7a1a9de269131f9c1595c ts=2026-10-08T13:59:05.4330000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3422] _id=6ace2f7fde269131f9ce9036 ts=2026-10-13T13:17:49.1350000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2349] _id=6ac65020de269131f9ba396f ts=2026-10-07T13:58:55.3790000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2391] _id=6ac79b13de269131f9c0465b ts=2026-10-08T13:30:59.0540000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae3.jsonl[693] _id=6ac4febade269131f9b23248 ts=2026-10-06T13:59:22.0330000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[704] _id=6ac64871de269131f9b8fa13 ts=2026-10-07T13:26:08.4470000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 596 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[11039] _id=6ad228b8de269131f9e3ca51 ts=2026-10-16T13:38:00.5180000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11040] _id=6ad228b8de269131f9e3ca52 ts=2026-10-16T13:38:00.5180000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[11057] _id=6ad228cade269131f9e3cb9d ts=2026-10-16T13:38:17.8180000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11058] _id=6ad228cade269131f9e3cb9e ts=2026-10-16T13:38:17.8180000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[11085] _id=6ad228f3de269131f9e3cf92 ts=2026-10-16T13:38:59.3620000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11086] _id=6ad228f3de269131f9e3cf93 ts=2026-10-16T13:38:59.3620000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 41m 
  - Evidence: 191h 41m: 6ab9a88e9a8420a1e6b56ae3.jsonl[673] _id=6ac4fe21de269131f9b2071a ts=2026-10-06T13:56:48.8600000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5400] _id=6acf85cdde269131f9d33d2a ts=2026-10-14T13:38:20.5810000Z; 26h 32m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5400] _id=6acf85cdde269131f9d33d2a ts=2026-10-14T13:38:20.5810000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[7914] _id=6ad0faf3de269131f9dd50ab ts=2026-10-15T16:10:27.1300000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3304] _id=6ac7a024de269131f9c129a0 ts=2026-10-08T13:52:36.4380000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3486] _id=6ace2f94de269131f9ce912d ts=2026-10-13T13:18:11.0340000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2359] _id=6ac65053de269131f9ba3c69 ts=2026-10-07T13:59:46.3680000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2368] _id=6ac79abdde269131f9c03bcb ts=2026-10-08T13:29:32.7140000Z; 23h 27m: 6ab9a88e9a8420a1e6b56ae3.jsonl[688] _id=6ac4feaade269131f9b22ed0 ts=2026-10-06T13:59:06.1130000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[707] _id=6ac6487fde269131f9b8fd3a ts=2026-10-07T13:26:22.6770000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 55 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[3778] _id=6ace3700de269131f9cee202 ts=2026-10-13T13:49:50.5800000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3779] _id=6ace3700de269131f9cee203 ts=2026-10-13T13:49:50.5800000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[4735] _id=6acf8141de269131f9d2e3fe ts=2026-10-14T13:18:57.2370000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[4736] _id=6acf8141de269131f9d2e3ff ts=2026-10-14T13:18:57.2370000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[6167] _id=6ad0d3a5de269131f9da70f9 ts=2026-10-15T13:22:44.8930000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6168] _id=6ad0d3a5de269131f9da70fa ts=2026-10-15T13:22:44.8930000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 33m 
  - Evidence: 143h 33m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3147] _id=6ac79f4fde269131f9c10320 ts=2026-10-08T13:49:03.3560000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[4916] _id=6acf8208de269131f9d2f1e0 ts=2026-10-14T13:22:16.3550000Z; 24h 0m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2103] _id=6ac64c91de269131f9b9e18b ts=2026-10-07T13:43:44.7280000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2641] _id=6ac79e24de269131f9c0cc9d ts=2026-10-08T13:44:04.4570000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae3.jsonl[650] _id=6ac4fdf6de269131f9b1fb33 ts=2026-10-06T13:56:05.8740000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[792] _id=6ac6496ede269131f9b93876 ts=2026-10-07T13:30:21.4180000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.012s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[10872] _id=6ad227a9de269131f9e3b6ba ts=2026-10-16T13:33:28.5810000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[10873] _id=6ad227a9de269131f9e3b6bb ts=2026-10-16T13:33:28.5810000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[10939] _id=6ad22809de269131f9e3bd7a ts=2026-10-16T13:35:05.3350000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[10940] _id=6ad22809de269131f9e3bd7b ts=2026-10-16T13:35:05.3350000Z; 12ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[147] _id=6ac4f6f7de269131f9b081b7 ts=2026-10-06T13:26:14.7250000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[148] _id=6ac4f6f7de269131f9b081be ts=2026-10-06T13:26:14.7370000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3408] _id=6ac7a1adde269131f9c1598e ts=2026-10-08T13:59:09.2180000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3421] _id=6ace2f7fde269131f9ce9035 ts=2026-10-13T13:17:46.5540000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2360] _id=6ac79aa7de269131f9c0390f ts=2026-10-07T13:59:49.149Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2366] _id=6ac79ab5de269131f9c03af5 ts=2026-10-08T13:29:22.1910000Z; 23h 26m: 6ab9a88e9a8420a1e6b56ae3.jsonl[696] _id=6ac4fee0de269131f9b2395d ts=2026-10-06T13:59:59.5060000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[701] _id=6ac64870de269131f9b8f9df ts=2026-10-07T13:26:04.3710000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[5640] _id=6acf87b5de269131f9d35bde ts=2026-10-14T13:46:28.9060000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5642] _id=6acf87f8de269131f9d3618c ts=2026-10-14T13:46:28.906Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[8667] _id=6ad14bcede269131f9e1acc0 ts=2026-10-15T21:55:25.0700000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[8671] _id=6ad14c61de269131f9e1b131 ts=2026-10-15T21:55:25.07Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3286] _id=6ac7a002de269131f9c12305 ts=2026-10-08T13:51:59.1830000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3411] _id=6ace2f80de269131f9ce9047 ts=2026-10-13T13:17:50.3730000Z; 39h 55m: 6ab9a88e9a8420a1e6b56ae3.jsonl[4478] _id=6acea519de269131f9d272b2 ts=2026-10-13T21:39:36.6120000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6765] _id=6ad0d67bde269131f9dab82f ts=2026-10-15T13:34:50.1090000Z; 24h 1m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2087] _id=6ac64c67de269131f9b9dd6c ts=2026-10-07T13:43:02.3420000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2684] _id=6ac79e5cde269131f9c0d619 ts=2026-10-08T13:44:59.3650000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1081 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[1001] _id=6ac649fdde269131f9b95f63 ts=2026-10-07T13:32:41.4750000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[1002] _id=6ac649fdde269131f9b95f64 ts=2026-10-07T13:32:41.4750000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[1005] _id=6ac649fdde269131f9b95f81 ts=2026-10-07T13:32:41.7200000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[1007] _id=6ac649fede269131f9b95fa3 ts=2026-10-07T13:32:41.7200000Z; 0ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[1009] _id=6ac649fede269131f9b95fa5 ts=2026-10-07T13:32:41.9470000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[996] _id=6ac649fede269131f9b95fc8 ts=2026-10-07T13:32:41.9470000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 49m 
  - Evidence: 167h 49m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2661] _id=6ac79e37de269131f9c0cfa6 ts=2026-10-08T13:44:22.8740000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6732] _id=6ad0d63bde269131f9dab278 ts=2026-10-15T13:33:46.9050000Z; 24h 0m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2106] _id=6ac64c94de269131f9b9e1be ts=2026-10-07T13:43:47.6600000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2650] _id=6ac79e24de269131f9c0cc97 ts=2026-10-08T13:44:04.4510000Z; 15h 25m: 6ab9a88e9a8420a1e6b56ae3.jsonl[8734] _id=6ad14cfcde269131f9e1b6b2 ts=2026-10-15T22:00:26.9330000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[10663] _id=6ad225c9de269131f9e393ce ts=2026-10-16T13:25:29.2570000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 127h 48m 
  - Evidence: 127h 48m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2601] _id=6ac79d6ade269131f9c0b0ac ts=2026-10-08T13:40:58.2050000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[4214] _id=6acea29dde269131f9d270b6 ts=2026-10-13T21:29:01.6440000Z; 23h 32m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2352] _id=6ac6504bde269131f9ba3bf3 ts=2026-10-07T13:59:38.9470000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2408] _id=6ac79b5ede269131f9c04f0a ts=2026-10-08T13:32:14.0460000Z; 23h 27m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5814] _id=6acf897dde269131f9d39520 ts=2026-10-14T13:54:04.4410000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6042] _id=6ad0d35bde269131f9da68f9 ts=2026-10-15T13:21:31.5380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.018s..0.024s shown 
  - Evidence: 18ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[2250] _id=6ac64ea2de269131f9ba11a5 ts=2026-10-07T13:52:33.1620000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2254] _id=6ac64ea2de269131f9ba11a9 ts=2026-10-07T13:52:33.1800000Z; 24ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[2249] _id=6ac64ea2de269131f9ba119f ts=2026-10-07T13:52:33.1380000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2250] _id=6ac64ea2de269131f9ba11a5 ts=2026-10-07T13:52:33.1620000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 40m 
  - Evidence: 191h 40m: 6ab9a88e9a8420a1e6b56ae3.jsonl[537] _id=6ac4fd2ede269131f9b1c1e9 ts=2026-10-06T13:52:45.7240000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5282] _id=6acf8486de269131f9d32830 ts=2026-10-14T13:32:53.6770000Z; 24h 9m: 6ab9a88e9a8420a1e6b56ae3.jsonl[6354] _id=6ad0d4e3de269131f9da91c4 ts=2026-10-15T13:28:03.6560000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11038] _id=6ad228b8de269131f9e3ca4f ts=2026-10-16T13:38:00.4700000Z; 23h 54m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5309] _id=6acf84a7de269131f9d32a9c ts=2026-10-14T13:33:26.7550000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6358] _id=6ad0d4c9de269131f9da8ea6 ts=2026-10-15T13:27:36.9590000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 38m 
  - Evidence: 191h 38m: 6ab9a88e9a8420a1e6b56ae3.jsonl[538] _id=6ac4fd2ede269131f9b1c1eb ts=2026-10-06T13:52:45.7510000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5218] _id=6acf8441de269131f9d32283 ts=2026-10-14T13:31:45.1690000Z; 24h 9m: 6ab9a88e9a8420a1e6b56ae3.jsonl[6382] _id=6ad0d4e4de269131f9da91cb ts=2026-10-15T13:28:03.7090000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11004] _id=6ad2288ede269131f9e3c772 ts=2026-10-16T13:37:18.2280000Z; 23h 53m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5304] _id=6acf84a7de269131f9d32aa0 ts=2026-10-14T13:33:26.7730000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6317] _id=6ad0d493de269131f9da886d ts=2026-10-15T13:26:42.9950000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.034s..0.037s shown 
  - Evidence: 34ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[6379] _id=6ad0d4e4de269131f9da91c8 ts=2026-10-15T13:28:03.6750000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6382] _id=6ad0d4e4de269131f9da91cb ts=2026-10-15T13:28:03.7090000Z; 37ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[11271] _id=6ad22a5cde269131f9e3ec0d ts=2026-10-16T13:45:00.1930000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11274] _id=6ad22a5cde269131f9e3ec10 ts=2026-10-16T13:45:00.2300000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 191h 38m 
  - Evidence: 191h 38m: 6ab9a88e9a8420a1e6b56ae3.jsonl[536] _id=6ac4fd2bde269131f9b1c129 ts=2026-10-06T13:52:43.2420000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5212] _id=6acf8438de269131f9d321bd ts=2026-10-14T13:31:35.9850000Z; 24h 9m: 6ab9a88e9a8420a1e6b56ae3.jsonl[6377] _id=6ad0d4e2de269131f9da919d ts=2026-10-15T13:28:02.0300000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11001] _id=6ad22889de269131f9e3c70f ts=2026-10-16T13:37:12.8710000Z; 23h 53m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5308] _id=6acf84a5de269131f9d32a8e ts=2026-10-14T13:33:24.8780000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6312] _id=6ad0d48cde269131f9da8776 ts=2026-10-15T13:26:36.7050000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.008s..0.025s shown 
  - Evidence: 8ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[11254] _id=6ad22a4ade269131f9e3ea2c ts=2026-10-16T13:44:42.2080000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[11255] _id=6ad22a4ade269131f9e3ea34 ts=2026-10-16T13:44:42.2160000Z; 21ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[6345] _id=6ad0d4abde269131f9da8b4b ts=2026-10-15T13:27:07.1830000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6346] _id=6ad0d4abde269131f9da8b4f ts=2026-10-15T13:27:07.2040000Z; 25ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[6318] _id=6ad0d494de269131f9da888f ts=2026-10-15T13:26:43.6700000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[6319] _id=6ad0d494de269131f9da8897 ts=2026-10-15T13:26:43.6950000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2364] _id=6ac79aa7de269131f9c0391d ts=2026-10-08T13:29:11.1200000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3417] _id=6ace2f68de269131f9ce8fbd ts=2026-10-13T13:17:27.9220000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae3.jsonl[699] _id=6ac64863de269131f9b8f74b ts=2026-10-07T13:25:53.7850000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2364] _id=6ac79aa7de269131f9c0391d ts=2026-10-08T13:29:11.1200000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5644] _id=6acf87f8de269131f9d36192 ts=2026-10-14T13:47:35.7890000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5993] _id=6ad0d2a3de269131f9da5d8b ts=2026-10-15T13:18:27.5770000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2363] _id=6ac79aa7de269131f9c0391c ts=2026-10-08T13:29:11.1190000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3416] _id=6ace2f68de269131f9ce8fbc ts=2026-10-13T13:17:27.9220000Z; 24h 3m: 6ab9a88e9a8420a1e6b56ae3.jsonl[698] _id=6ac64863de269131f9b8f74a ts=2026-10-07T13:25:53.7850000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2363] _id=6ac79aa7de269131f9c0391c ts=2026-10-08T13:29:11.1190000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5643] _id=6acf87f8de269131f9d36191 ts=2026-10-14T13:47:35.7890000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[5992] _id=6ad0d2a3de269131f9da5d8a ts=2026-10-15T13:18:27.5770000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3418] _id=6ace2f68de269131f9ce8fb7 ts=2026-10-08T13:59:17.478Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3643] _id=6ace3031de269131f9ce9735 ts=2026-10-13T13:20:48.8910000Z; 25h 38m: 6ab9a88e9a8420a1e6b56ae3.jsonl[5990] _id=6ad0d2a3de269131f9da5d85 ts=2026-10-14T14:00:02.515Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[7662] _id=6ad0f74fde269131f9dceee0 ts=2026-10-15T15:38:14.544Z; 23h 59m: 6ab9a88e9a8420a1e6b56ae3.jsonl[700] _id=6ac64863de269131f9b8f741 ts=2026-10-06T14:00:03.305Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2361] _id=6ac79aa7de269131f9c03910 ts=2026-10-07T13:59:49.195Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a88e9a8420a1e6b56ae3.jsonl[3365] _id=6ac7a0e9de269131f9c147c6 ts=2026-10-08T13:55:52.7480000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[3424] _id=6ace2f7fde269131f9ce9038 ts=2026-10-13T13:17:49.1980000Z; 23h 37m: 6ab9a88e9a8420a1e6b56ae3.jsonl[2241] _id=6ac64e8cde269131f9ba0e09 ts=2026-10-07T13:52:11.4300000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[2367] _id=6ac79ab5de269131f9c03af6 ts=2026-10-08T13:29:24.7920000Z; 23h 31m: 6ab9a88e9a8420a1e6b56ae3.jsonl[653] _id=6ac4fdf8de269131f9b1fbd5 ts=2026-10-06T13:56:08.2180000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[725] _id=6ac648cbde269131f9b91056 ts=2026-10-07T13:27:38.6290000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.003s..0.004s shown 
  - Evidence: 3ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[456] _id=6ac4fc59de269131f9b188e0 ts=2026-10-06T13:49:12.8450000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[459] _id=6ac4fc59de269131f9b188f0 ts=2026-10-06T13:49:12.8480000Z; 4ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[10158] _id=6ad22380de269131f9e36561 ts=2026-10-16T13:15:43.8380000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[10156] _id=6ad22380de269131f9e36563 ts=2026-10-16T13:15:43.8420000Z; 4ms: 6ab9a88e9a8420a1e6b56ae3.jsonl[8663] _id=6ad14bc4de269131f9e1ac6b ts=2026-10-15T21:55:15.6730000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[8664] _id=6ad14bc4de269131f9e1ac6d ts=2026-10-15T21:55:15.6770000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 14h 40m 
  - Evidence: 14h 40m: 6ab9a88e9a8420a1e6b56ae3.jsonl[10089] _id=6ad154edde269131f9e1d8de ts=2026-10-15T22:34:19.9410000Z -> 6ab9a88e9a8420a1e6b56ae3.jsonl[10269] _id=6ad22346de269131f9e360c8 ts=2026-10-16T13:14:46.0990000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 16 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[439] _id=6ac4fc26de269131f9b17723 ts=2026-10-06T13:48:22.2680000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[546] _id=6ac4fd42de269131f9b1c75e ts=2026-10-06T13:53:06.0390000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[2415] _id=6ac79b73de269131f9c05241 ts=2026-10-08T13:32:35.3690000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[6382] _id=6ad0d4e4de269131f9da91cb ts=2026-10-15T13:28:03.7090000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[11274] _id=6ad22a5cde269131f9e3ec10 ts=2026-10-16T13:45:00.2300000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[481] _id=6ac4fcbbde269131f9b1a64d ts=2026-10-06T13:50:50.4660000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[486] _id=6ac4fcbede269131f9b1a744 ts=2026-10-06T13:50:53.8980000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[166] _id=6ac4f743de269131f9b08b84 ts=2026-10-06T13:27:30.5290000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[8663] _id=6ad14bc4de269131f9e1ac6b ts=2026-10-15T21:55:15.6730000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[9377] _id=6ad14f71de269131f9e1ca81 ts=2026-10-15T22:10:56.8820000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[8] _id=6ac4f520de269131f9b03a79 ts=?`; `6ab9a88e9a8420a1e6b56ae3.jsonl[708] _id=6ac64880de269131f9b8fd3f ts=?`; `6ab9a88e9a8420a1e6b56ae3.jsonl[3780] _id=6ace3700de269131f9cee1f7 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 20 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[2836] _id=6ac79ef3de269131f9c0f11d ts=2026-10-08T13:47:27.8170000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[2837] _id=6ac79ef3de269131f9c0f132 ts=2026-10-08T13:47:27.8170000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[2847] _id=6ac79ef4de269131f9c0f181 ts=2026-10-08T13:47:29.0750000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 93 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[976] _id=6ac649f9de269131f9b95de1 ts=2026-10-07T13:32:38.9300000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[969] _id=6ac649f9de269131f9b95de5 ts=2026-10-07T13:32:38.9300000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[977] _id=6ac649f9de269131f9b95def ts=2026-10-07T13:32:38.9300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 27 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[5443] _id=6acf868ade269131f9d345e1 ts=2026-10-14T13:41:29.7800000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[5592] _id=6acf8787de269131f9d357b4 ts=2026-10-14T13:45:42.8390000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[5667] _id=6acf8838de269131f9d36786 ts=2026-10-14T13:48:39.6210000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 27 unmatched 'DialogueStartEvent' (totals: 374 start, 363 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 819 open, 807 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 53 open, 52 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 49 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 212 of 11843 adjacent _id pairs reverse in client time; worst 290.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae3.jsonl[1135] _id=6ac64aeede269131f9b99a77 ts=2026-10-07T13:36:45.7410000Z`; `6ab9a88e9a8420a1e6b56ae3.jsonl[1150] _id=6ac64aefde269131f9b99a92 ts=2026-10-07T13:31:55.7220000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.58s, min -429491.22s, max -0.07s over 11844 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae3\coverage.yaml

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
  - Observed: 6 records 
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

### `InputEvent` — 3721 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1129); Unit 3 Dev (946); Unit 4 Dev - Dungeon (757); Unit 4 Dev (309); Unit 3 Dungeon Dev (297); Unit 1 Dev (180); Unit 4 Dev - Anderson Base (103)
- **Intervals:** median 1.29s (p5 0.13s / p95 16.58s, n=3720)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3721/3721 records)
    "pressed"  x3721
data.actionType  (string, 3721/3721 records)
    "Move"  x2224
    "Interact"  x562
    "Jump"  x551
    "Sprint"  x122
    "Hoverboard"  x107
    "Ascend"  x87
    "Map"  x45
    "ToggleDebug"  x19
    "Pause"  x3
    "Descend"  x1
data.key  (string, 3721/3721 records, 46 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3721/3721 records)
    "Player"  x3049
    "Drone"  x672
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2692 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1608); Unit 4 Dev (960); Unit 3 Dungeon Dev (124)
- **Intervals:** median 0.08s (p5 0.00s / p95 2.61s, n=2691)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2692/2692 records)
    "BecameVisible"  x819
    "BecameInvisible"  x807
    "BecameCameraCentered"  x533
    "BecameCameraUncentered"  x533
data.pieceId  (string, 2692/2692 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2692/2692 records)
    1990 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2136 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (809); Unit 3 Dev (333); Unit 4 Dev - Dungeon (326); Unit 4 Dev (233); Unit 1 Dev (232); Unit 3 Dungeon Dev (118); Unit 4 Dev - Anderson Base (85)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.37s, n=2123)
- **Fields under `data`:**

```text
data.position  (object, 2136/2136 records)
data.position.x  (number, 2136/2136 records)
    numeric range -724.046 .. 1628.28 (853 unique)
data.position.y  (number, 2136/2136 records)
    numeric range -112.489 .. 176.72 (597 unique)
data.position.z  (number, 2136/2136 records)
    numeric range -1170.64 .. 2228.92 (855 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2038 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (852); Unit 3 Dev (328); Unit 4 Dev (225); Unit 1 Dev (197); Unit 4 Dev - Dungeon (185); Unit 3 Dungeon Dev (131); Unit 4 Dev - Anderson Base (120)
- **eventKey:** present on 1301 of 2038 records
- **Intervals:** median 4.27s (p5 0.00s / p95 38.66s, n=2037)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1301; [conversationId, dialogueEventType] x737
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2038/2038 records)
    numeric range 8 .. 114 (43 unique)
data.dialogueEventType  (string, 2038/2038 records)
    "DialogueNodeEvent"  x1301
    "DialogueStartEvent"  x374
    "DialogueFinishEvent"  x363
data.nodeId  (number, 1301/2038 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 398 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (213); Unit 2 Prod (Refactor) (85); Unit 3 Dungeon Dev (45); Unit 4 Dev (20); Unit 3 Dev (16); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 8.76s (p5 0.14s / p95 262.61s, n=397)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 398/398 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 398/398 records)
    100 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 306 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (157); Unit 2 Prod (Refactor) (67); Unit 3 Dev (49); Unit 1 Dev (33)
- **Intervals:** median 0.69s (p5 0.03s / p95 13.85s, n=305)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 306/306 records)
    "argumentationNodeHoverEnd"  x128
    "argumentationNodeHoverStart"  x126
    "argumentationNodeAdd"  x33
    "argumentationNodeRemove"  x19
data.argumentationTitle  (string, 306/306 records)
    "Unit 4 - Flooding"  x157
    "Unit 2 – Watershed"  x67
    "Unit 3 - Pollution Upstream"  x49
    "Unit 1 - Freshwater"  x21
    "Unit 1 - Argumentation Tutorial"  x12
data.nodeName  (string, 306/306 records)
    "B"  x66
    "A"  x51
    "D"  x39
    "I"  x38
    "C"  x35
    "II"  x28
    "1"  x13
    "2"  x13
    "3"  x10
    "4"  x8
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 166 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (98); Unit 3 Dev (68)
- **Intervals:** median 4.07s (p5 0.80s / p95 386.53s, n=165)
- **`data` key-set variants:** [actionType, featureUsed] x105; [actionType, featureUsed, location] x47; [actionType, featureUsed, legendName] x14
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 166/166 records)
    "MapOpenEvent"  x53
    "MapCloseEvent"  x52
    "WaypointMoveEvent"  x40
    "Selected"  x11
    "WaypointSetEvent"  x7
    "Unselected"  x3
data.featureUsed  (string, 166/166 records)
    "Map"  x105
    "Waypoint"  x47
    "Legend"  x14
data.legendName  (string, 14/166 records)
    "210 ft"  x6
    "Water"  x3
    "0 ft"  x2
    "180 ft"  x1
    "270 ft"  x1
    "90 ft"  x1
data.location  (object, 47/166 records)
data.location.x  (number, 47/166 records)
    numeric range -278.64 .. 138.914 (40 unique)
data.location.y  (number, 47/166 records)
    numeric range -315.353 .. 279.346 (43 unique)
data.location.z  (number, 47/166 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 103 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (103)
- **Intervals:** median 0.86s (p5 0.19s / p95 90.78s, n=102)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 103/103 records)
    "ChangeCanister"  x103
data.canisterType  (string, 103/103 records)
    "Clay"  x76
    "Bedrock"  x19
    "Gravel"  x5
    "Sand"  x3
data.floor  (string, 103/103 records)
    "5"  x86
    "4"  x15
    "3"  x2
data.machine  (string, 103/103 records)
    "1"  x102
    "2"  x1
data.row  (string, 103/103 records)
    "TopRow"  x77
    "BottomRow"  x26
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `questEvent` — 81 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 4 Dev - Dungeon (20); Unit 3 Dev (15); Unit 1 Dev (10); Unit 4 Dev (9); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 81 of 81 records
- **Intervals:** median 197.20s (p5 0.01s / p95 58299.51s, n=80)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 81/81 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x32
data.questID  (string, 81/81 records)
    26 unique values (see csv/event_unique_values.csv)
data.questName  (string, 81/81 records)
    26 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/81 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (33); Unit 2 Prod (Refactor) (13); Unit 3 Dev (12)
- **Intervals:** median 1.41s (p5 0.16s / p95 34593.07s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x48; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/58 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/58 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 48/58 records)
    "RightDrag"  x29
    "LeftDrag"  x19
data.currentSoilType  (string, 48/58 records)
    "CLAYSAND"  x10
    "SAND"  x10
    "CLAY"  x9
    "CLAYROCK"  x8
    "SANDGRAVEL"  x6
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 48/58 records)
    "false"  x36
    "true"  x12
data.waterLevelStatus  (string, 48/58 records)
    "TooLow"  x19
    "Proper"  x17
    "TooHigh"  x12
data.waterRetentionChange  (string, 48/58 records)
    "Decrease"  x19
    "Increase"  x17
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 46 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (7); Unit 4 Dev (7); Unit 3 Dev (6); Unit 4 Dev - Dungeon (5); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 482.90s (p5 9.75s / p95 84602.87s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "DebugMenuStateChanged"  x46
data.isOpened  (bool, 46/46 records)
    false  x46
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 24 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 4 Dev (2); Unit 2 Prod (Refactor) (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2373.35s (p5 27.64s / p95 86402.78s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 7789.88s (p5 494.30s / p95 121067.28s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 19 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (13); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 1 Dev (1)
- **Intervals:** median 23.53s (p5 10.80s / p95 177448.48s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "submitAnswerEvent"  x19
data.answerSubmitted  (string, 19/19 records)
    "B,2,II"  x3
    "C,2,II"  x3
    "A,2,II"  x2
    "A,3,I"  x2
    "D,2,II"  x2
    "A,1,I"  x1
    "A,1,II"  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "A,D,1,II"  x1
    "B,A,C,2,II"  x1
    "C,B,2,II"  x1
data.argumentationTitle  (string, 19/19 records)
    "Unit 4 - Flooding"  x13
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 80.68s (p5 0.04s / p95 388446.97s, n=11)
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

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (2); Unit 4 Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 55050.96s (p5 307.76s / p95 260991.72s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x1
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 4 empty-string)
    ""  x4
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a915116:wasm-function[108544]:0x24e60da
    at wasm://wasm/0a915116:wasm-function[3309]:0x143bd9
    at wasm://wasm/0a915116:wasm-function[59793]:0x11abccc
    at wasm://wasm/0a915116:wasm-function[3347]:0x145fec
    at wasm://wasm/0a915116:wasm-function[82501]:0x170b4af
    at wasm://wasm/0a915116:wasm-function[83451]:0x171f21d
    at wasm://wasm/0a915116:wasm-function[110308]:0x259f6a8
    at invoke_iiii (blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:474038)
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
    at blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:23580
    at _JS_CallAsLongAsNoExceptionsSeen (blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:23594)
    at wasm://wasm/0a915116:wasm-function[110044]:0x256ebbe
    at wasm://wasm/0a915116:wasm-function[110314]:0x259f6fb
    at browserIterationFunc (blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:115768)
    at callUserCallback (blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:98130)
    at Object.runIter (blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:99497)
    at Browser_mainLoop_runner (blob:https://mhs.adroit.games/7730a607-44d9-45be-b79b-a52fdc1d18df:9:115294)"  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 6/6 records)
    "unhandled_rejection"  x5
    "runtime_error"  x1
data.unitId  (string, 6/6 records)
    "unit4"  x3
    "unit2"  x2
    "unit1"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.96s (p5 1.70s / p95 107465.80s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 392809.14s (p5 125254.81s / p95 660363.46s, n=2)
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
- **Intervals:** median 25.73s (p5 23.17s / p95 28.30s, n=2)
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

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 2.44s (p5 2.44s / p95 2.44s, n=1)
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

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (13 records)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (11x); "Unselected" (3x); "WaypointMoveEvent" (40x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (14x); "Waypoint" (47x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (19x)
- `soilMachine` data.canisterType: "Bedrock" (19x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*