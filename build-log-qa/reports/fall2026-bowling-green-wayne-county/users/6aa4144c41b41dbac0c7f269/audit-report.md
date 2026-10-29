# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f269

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f269
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f269.jsonl
- **Records:** 15021 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f269
- **Time span:** 2026-09-23T18:32:59.060000+00:00 .. 2026-10-07T18:50:28.959000+00:00 (336h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f269\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 15021 records, 9 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 93 INFO, 2 NOT_TESTED, 81 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
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
| PuzzlePieceVisibleEvent | 4634 | 30.85 | 1 | 3 | 0 | 2026-09-25T18:20:37.151000+00:00 | 2026-10-07T15:43:57.190000+00:00 | 285h 23m |
| InputEvent | 4170 | 27.76 | 1 | 7 | 0 | 2026-09-23T18:33:15.881000+00:00 | 2026-10-07T18:50:28.463000+00:00 | 336h 17m |
| PlayerPositionEvent | 2350 | 15.64 | 1 | 7 | 0 | 2026-09-23T18:33:10.223000+00:00 | 2026-10-07T18:50:28.959000+00:00 | 336h 17m |
| DialogueEvent | 2332 | 15.52 | 1 | 7 | 1435 | 2026-09-23T18:33:32.878000+00:00 | 2026-10-07T18:50:27.308000+00:00 | 336h 16m |
| argumentationNodeEvent | 700 | 4.66 | 1 | 3 | 0 | 2026-09-24T18:06:21.833000+00:00 | 2026-10-07T18:43:59.133000+00:00 | 312h 37m |
| ObjectInterEvent | 362 | 2.41 | 1 | 7 | 0 | 2026-09-23T18:38:11.189000+00:00 | 2026-10-07T18:49:05.769000+00:00 | 336h 10m |
| questEvent | 88 | 0.59 | 1 | 7 | 88 | 2026-09-23T18:33:32.839000+00:00 | 2026-10-07T18:50:23.522000+00:00 | 336h 16m |
| argumentationAnswerEvent | 72 | 0.48 | 1 | 3 | 0 | 2026-09-24T18:06:19.078000+00:00 | 2026-10-07T18:44:00.926000+00:00 | 312h 37m |
| Soil Key Puzzle | 60 | 0.4 | 1 | 3 | 0 | 2026-09-25T18:29:32.299000+00:00 | 2026-10-06T15:44:44.034000+00:00 | 261h 15m |
| gameWindowFocusEvent | 51 | 0.34 | 1 | 7 | 0 | 2026-09-23T18:32:59.060000+00:00 | 2026-10-07T18:45:43.403000+00:00 | 336h 12m |
| TopographicMapEvent | 45 | 0.3 | 1 | 2 | 0 | 2026-09-25T18:22:29.463000+00:00 | 2026-10-05T18:26:29.281000+00:00 | 240h 3m |
| soilMachine | 36 | 0.24 | 1 | 1 | 0 | 2026-10-06T18:30:57.792000+00:00 | 2026-10-06T18:41:46.893000+00:00 | 10m 49s |
| DEBUGMenu | 34 | 0.23 | 1 | 8 | 0 | 2026-09-23T18:33:10.212000+00:00 | 2026-10-07T18:44:54.794000+00:00 | 336h 11m |
| gameWindowUnfocusEvent | 27 | 0.18 | 1 | 6 | 0 | 2026-09-25T18:20:27.301000+00:00 | 2026-10-07T18:45:40.791000+00:00 | 288h 25m |
| gameStartEvent | 26 | 0.17 | 1 | 1 | 0 | 2026-09-23T18:32:59.060000+00:00 | 2026-10-07T18:34:02.432000+00:00 | 336h 1m |
| argumentationEvent | 14 | 0.09 | 1 | 3 | 0 | 2026-09-24T18:04:22.389000+00:00 | 2026-10-07T18:44:00.963000+00:00 | 312h 39m |
| argumentationToolEvent | 7 | 0.05 | 1 | 1 | 0 | 2026-10-01T15:52:06.570000+00:00 | 2026-10-01T15:54:23.716000+00:00 | 2m 17s |
| TerasGardenBox | 6 | 0.04 | 1 | 1 | 0 | 2026-10-07T18:47:48.706000+00:00 | 2026-10-07T18:48:24.732000+00:00 | 36.0s |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-09-29T18:39:44.778000+00:00 | 2026-09-29T18:39:45.263000+00:00 | 0.5s |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-24T18:09:38.364000+00:00 | 2026-10-05T18:42:18.775000+00:00 | 264h 32m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1707.107s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 952360.411s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.403s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.504s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 7.809s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 199.768s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.581s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8895.884s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 515.176s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 364.192s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.248s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Pick Up; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 14.4x vs baseline. 
  - Observed: 72 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 2,II; A,2,I; A,2,II; A,4,I; A,4,II; A,B,1,I; A,B,2,II; A,B,3,II; A,C,2,II; A,D,2,II; B,2,I; B,2,II; B,C,2,II; B,C,D,; B,D,2,II; C,2,II; C,3,II; C,D,2,II; D,1,II; D,2,II; D,4,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 700 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 7.2x vs baseline. 
  - Observed: 36 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 20 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[132] _id=6ab41d11485cab4c954f63ef ts=2026-09-23T18:40:17.0780000Z`; `6aa4144c41b41dbac0c7f269.jsonl[234] _id=6ab41e32485cab4c954f6e71 ts=2026-09-23T18:45:06.3900000Z`; `6aa4144c41b41dbac0c7f269.jsonl[345] _id=6ab56295485cab4c95539dc6 ts=2026-09-24T17:49:09.3600000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[5564] _id=6abbfef5485cab4c95841bcb ts=2026-09-29T18:09:55.4640000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[5] _id=6ab41b5b485cab4c954f55fe ts=2026-09-23T18:32:59.0600000Z`; `6aa4144c41b41dbac0c7f269.jsonl[260] _id=6ab56106485cab4c95537d21 ts=2026-09-24T17:42:30.2140000Z`; `6aa4144c41b41dbac0c7f269.jsonl[765] _id=6ab567b1485cab4c95541f8e ts=2026-09-24T18:10:57.6670000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 51 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 51} 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[4] _id=6ab41b5b485cab4c954f55fa ts=2026-09-23T18:32:59.0600000Z`; `6aa4144c41b41dbac0c7f269.jsonl[259] _id=6ab56106485cab4c95537d1f ts=2026-09-24T17:42:30.2120000Z`; `6aa4144c41b41dbac0c7f269.jsonl[764] _id=6ab567b1485cab4c95541f8c ts=2026-09-24T18:10:57.6660000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[911] _id=6ab6bb68485cab4c955e0a40 ts=2026-09-25T18:20:27.3010000Z`; `6aa4144c41b41dbac0c7f269.jsonl[2793] _id=6ab6be69485cab4c955e4aaf ts=2026-09-25T18:33:16.2860000Z`; `6aa4144c41b41dbac0c7f269.jsonl[2797] _id=6ab6be7d485cab4c955e4b51 ts=2026-09-25T18:33:36.3050000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4633 | 0.0 | 0.034 | 221.757 | 1.218 | 345974.543 | 0.27 | 2754 | 8 |
| InputEvent | 4169 | 0.0 | 0.923 | 290.389 | 15.16 | 345117.677 | 0.21 | 212 | 17 |
| PlayerPositionEvent | 2340 | 9.398 | 10.0 | 517.242 | 10.032 | 345121.032 | 0.12 | 0 | 17 |
| DialogueEvent | 2331 | 0.0 | 4.276 | 519.354 | 35.201 | 345188.841 | 0.12 | 686 | 17 |
| argumentationNodeEvent | 699 | 0.019 | 0.262 | 1610.096 | 8.483 | 596619.438 | 0.04 | 159 | 4 |
| ObjectInterEvent | 361 | 0.0 | 9.483 | 3352.506 | 442.519 | 345252.092 | 0.02 | 8 | 15 |
| questEvent | 87 | 0.001 | 257.46 | 13915.065 | 80619.802 | 346111.005 | 0.0 | 12 | 26 |
| argumentationAnswerEvent | 71 | 0.15 | 7.809 | 15851.575 | 647.958 | 596652.977 | 0.0 | 0 | 4 |
| Soil Key Puzzle | 59 | 0.136 | 0.727 | 15940.877 | 25021.961 | 431088.234 | 0.0 | 0 | 3 |
| gameWindowFocusEvent | 50 | 1.676 | 515.176 | 24207.287 | 86081.866 | 347288.887 | 0.0 | 0 | 23 |
| TopographicMapEvent | 44 | 0.012 | 7.504 | 19641.814 | 86683.383 | 431745.781 | 0.0 | 2 | 5 |
| soilMachine | 35 | 0.187 | 2.248 | 18.546 | 83.044 | 229.766 | 3.24 | 0 | 0 |
| DEBUGMenu | 33 | 5.761 | 1707.107 | 36675.896 | 155487.321 | 346116.844 | 0.0 | 0 | 24 |
| gameWindowUnfocusEvent | 26 | 0.198 | 364.192 | 39935.134 | 234111.409 | 358275.548 | 0.0 | 0 | 10 |
| gameStartEvent | 25 | 37.627 | 8895.884 | 48386.535 | 224232.804 | 347288.887 | 0.0 | 0 | 21 |
| argumentationEvent | 13 | 0.019 | 199.768 | 86582.967 | 549675.163 | 596610.998 | 0.0 | 3 | 5 |
| argumentationToolEvent | 6 | 1.263 | 3.581 | 22.858 | 64.234 | 65.029 | 2.62 | 0 | 0 |
| TerasGardenBox | 5 | 0.894 | 1.403 | 7.205 | 18.073 | 19.186 | 8.33 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 1 | 0.485 | 0.485 | 0.485 | 0.485 | 0.485 | 123.71 | 0 | 0 |
| EndOfUnit | 1 | 952360.411 | 952360.411 | 952360.411 | 952360.411 | 952360.411 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 11 group(s), 41 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[11662] _id=6ac5396dde269131f9b6288a ts=2026-10-06T18:09:49.0960000Z == 6aa4144c41b41dbac0c7f269.jsonl[11658] _id=6ac5396dde269131f9b6288e ts=2026-10-06T18:09:49.0960000Z`; `6aa4144c41b41dbac0c7f269.jsonl[11666] _id=6ac5396dde269131f9b6289c ts=2026-10-06T18:09:49.1020000Z == 6aa4144c41b41dbac0c7f269.jsonl[11667] _id=6ac5396dde269131f9b6289e ts=2026-10-06T18:09:49.1020000Z`; `6aa4144c41b41dbac0c7f269.jsonl[13035] _id=6ac667c0de269131f9bc0be9 ts=2026-10-07T15:39:43.6360000Z == 6aa4144c41b41dbac0c7f269.jsonl[13036] _id=6ac667c0de269131f9bc0bea ts=2026-10-07T15:39:43.6360000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 179 group(s), 266 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[909] _id=6ab6bb85485cab4c955e1021 ts=2026-09-25T18:20:54.9450000Z == 6aa4144c41b41dbac0c7f269.jsonl[940] _id=6ab6bb85485cab4c955e1023 ts=2026-09-25T18:20:54.9450000Z`; `6aa4144c41b41dbac0c7f269.jsonl[889] _id=6ab6bb86485cab4c955e102f ts=2026-09-25T18:20:55.4120000Z == 6aa4144c41b41dbac0c7f269.jsonl[932] _id=6ab6bb86485cab4c955e1036 ts=2026-09-25T18:20:55.4120000Z`; `6aa4144c41b41dbac0c7f269.jsonl[931] _id=6ab6bb87485cab4c955e1078 ts=2026-09-25T18:20:55.4950000Z == 6aa4144c41b41dbac0c7f269.jsonl[916] _id=6ab6bb87485cab4c955e107e ts=2026-09-25T18:20:55.4950000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[791] _id=6ab6ba97485cab4c955de604 ts=? == 6aa4144c41b41dbac0c7f269.jsonl[5538] _id=6abbfef3485cab4c95841bbb ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 27 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6aa4144c41b41dbac0c7f269.jsonl[90] _id=6ab41c93485cab4c954f6036 ts=2026-09-23T18:38:11.1890000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[91] _id=6ab41c93485cab4c954f6039 ts=2026-09-23T18:38:11.1990000Z`; `7ms: 6aa4144c41b41dbac0c7f269.jsonl[279] _id=6ab5613e485cab4c955380e0 ts=2026-09-24T17:43:26.0690000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[280] _id=6ab5613e485cab4c955380e5 ts=2026-09-24T17:43:26.0760000Z`; `493ms: 6aa4144c41b41dbac0c7f269.jsonl[864] _id=6ab6bb39485cab4c955e01c0 ts=2026-09-25T18:19:41.0020000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[869] _id=6ab6bb3a485cab4c955e01e3 ts=2026-09-25T18:19:41.4950000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 607 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa4144c41b41dbac0c7f269.jsonl[940] _id=6ab6bb85485cab4c955e1023 ts=2026-09-25T18:20:54.9450000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[888] _id=6ab6bb85485cab4c955e1027 ts=2026-09-25T18:20:54.9680000Z`; `19ms: 6aa4144c41b41dbac0c7f269.jsonl[927] _id=6ab6bb87485cab4c955e1083 ts=2026-09-25T18:20:55.4950000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[897] _id=6ab6bb87485cab4c955e1087 ts=2026-09-25T18:20:55.5140000Z`; `22ms: 6aa4144c41b41dbac0c7f269.jsonl[897] _id=6ab6bb87485cab4c955e1087 ts=2026-09-25T18:20:55.5140000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[898] _id=6ab6bb87485cab4c955e1091 ts=2026-09-25T18:20:55.5360000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `12ms: 6aa4144c41b41dbac0c7f269.jsonl[3062] _id=6abaad91485cab4c956f8957 ts=2026-09-28T18:10:25.9920000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[3060] _id=6abaad92485cab4c956f8967 ts=2026-09-28T18:10:26.0040000Z`; `766ms: 6aa4144c41b41dbac0c7f269.jsonl[3070] _id=6abaada9485cab4c956f8cb3 ts=2026-09-28T18:10:49.4430000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[3057] _id=6abaadaa485cab4c956f8cc7 ts=2026-09-28T18:10:50.2090000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `682ms: 6aa4144c41b41dbac0c7f269.jsonl[627] _id=6ab5669b485cab4c955408f4 ts=2026-09-24T18:06:19.0780000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[628] _id=6ab5669b485cab4c95540910 ts=2026-09-24T18:06:19.7600000Z`; `217ms: 6aa4144c41b41dbac0c7f269.jsonl[628] _id=6ab5669b485cab4c95540910 ts=2026-09-24T18:06:19.7600000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[629] _id=6ab5669b485cab4c95540916 ts=2026-09-24T18:06:19.9770000Z`; `152ms: 6aa4144c41b41dbac0c7f269.jsonl[629] _id=6ab5669b485cab4c95540916 ts=2026-09-24T18:06:19.9770000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[630] _id=6ab5669c485cab4c95540918 ts=2026-09-24T18:06:20.1290000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6aa4144c41b41dbac0c7f269.jsonl[8483] _id=6abe8247485cab4c95ab956e ts=2026-10-01T15:54:47.0280000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[8486] _id=6abe8247485cab4c95ab9576 ts=2026-10-01T15:54:47.0640000Z`; `45ms: 6aa4144c41b41dbac0c7f269.jsonl[14198] _id=6ac66e67de269131f9bc4a58 ts=2026-10-07T16:08:07.5920000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[14201] _id=6ac66e67de269131f9bc4a5b ts=2026-10-07T16:08:07.6370000Z`; `19ms: 6aa4144c41b41dbac0c7f269.jsonl[14775] _id=6ac692f1de269131f9bdf4aa ts=2026-10-07T18:44:00.9440000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[14778] _id=6ac692f1de269131f9bdf4ad ts=2026-10-07T18:44:00.9630000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 105 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `571ms: 6aa4144c41b41dbac0c7f269.jsonl[642] _id=6ab566a4485cab4c955409e8 ts=2026-09-24T18:06:28.3880000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[636] _id=6ab566a4485cab4c95540a0a ts=2026-09-24T18:06:28.9590000Z`; `470ms: 6aa4144c41b41dbac0c7f269.jsonl[647] _id=6ab566a4485cab4c955409f2 ts=2026-09-24T18:06:28.5140000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[637] _id=6ab566a5485cab4c95540a0e ts=2026-09-24T18:06:28.9840000Z`; `295ms: 6aa4144c41b41dbac0c7f269.jsonl[636] _id=6ab566a4485cab4c95540a0a ts=2026-09-24T18:06:28.9590000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[643] _id=6ab566a5485cab4c95540a19 ts=2026-09-24T18:06:29.2540000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `198ms: 6aa4144c41b41dbac0c7f269.jsonl[14229] _id=6ac66ee3de269131f9bc4c72 ts=2026-10-07T16:10:11.0770000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[14232] _id=6ac66ee3de269131f9bc4c76 ts=2026-10-07T16:10:11.2750000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f269.jsonl[5564] _id=6abbfef5485cab4c95841bcb ts=2026-09-29T18:09:55.4640000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[5565] _id=6abbfef5485cab4c95841bcd ts=2026-09-29T18:09:55.4680000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `661ms: 6aa4144c41b41dbac0c7f269.jsonl[12510] _id=6ac5402ede269131f9b6a45d ts=2026-10-06T18:38:38.5160000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[12517] _id=6ac5402fde269131f9b6a477 ts=2026-10-06T18:38:39.1770000Z`; `382ms: 6aa4144c41b41dbac0c7f269.jsonl[12517] _id=6ac5402fde269131f9b6a477 ts=2026-10-06T18:38:39.1770000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[12518] _id=6ac5402fde269131f9b6a493 ts=2026-10-06T18:38:39.5590000Z`; `342ms: 6aa4144c41b41dbac0c7f269.jsonl[12518] _id=6ac5402fde269131f9b6a493 ts=2026-10-06T18:38:39.5590000Z ~ 6aa4144c41b41dbac0c7f269.jsonl[12507] _id=6ac5402fde269131f9b6a4a7 ts=2026-10-06T18:38:39.9010000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 96h 8m 
  - Evidence: 96h 8m: 6aa4144c41b41dbac0c7f269.jsonl[8709] _id=6abe8398485cab4c95abacac ts=2026-10-01T16:00:24.0150000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9356] _id=6ac3cb9cde269131f9ad9447 ts=2026-10-05T16:09:00.8590000Z; 71h 49m: 6aa4144c41b41dbac0c7f269.jsonl[785] _id=6ab6ba91485cab4c955de587 ts=2026-09-25T18:16:52.2870000Z -> 6aa4144c41b41dbac0c7f269.jsonl[2950] _id=6abaacbb485cab4c956f723b ts=2026-09-28T18:06:51.3670000Z; 24h 5m: 6aa4144c41b41dbac0c7f269.jsonl[768] _id=6ab567ba485cab4c95541fd4 ts=2026-09-24T18:11:06.1380000Z -> 6aa4144c41b41dbac0c7f269.jsonl[785] _id=6ab6ba91485cab4c955de587 ts=2026-09-25T18:16:52.2870000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa4144c41b41dbac0c7f269.jsonl[9336] _id=6abe8765485cab4c95abd2be ts=2026-10-01T16:16:37.0250000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9502] _id=6ac3cbc9de269131f9ad96a3 ts=2026-10-05T16:09:45.8660000Z; 71h 26m: 6aa4144c41b41dbac0c7f269.jsonl[2941] _id=6ab6c059485cab4c955e65b5 ts=2026-09-25T18:41:29.4150000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3016] _id=6abaad10485cab4c956f771b ts=2026-09-28T18:08:16.9860000Z; 24h 5m: 6aa4144c41b41dbac0c7f269.jsonl[781] _id=6ab567da485cab4c955420d6 ts=2026-09-24T18:11:38.6350000Z -> 6aa4144c41b41dbac0c7f269.jsonl[793] _id=6ab6ba98485cab4c955de62f ts=2026-09-25T18:16:59.4980000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 686 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f269.jsonl[13760] _id=6ac66c4bde269131f9bc3f35 ts=2026-10-07T15:59:07.8320000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13761] _id=6ac66c4bde269131f9bc3f36 ts=2026-10-07T15:59:07.8320000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[13855] _id=6ac66d14de269131f9bc42e9 ts=2026-10-07T16:02:28.0200000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13856] _id=6ac66d14de269131f9bc42ea ts=2026-10-07T16:02:28.0200000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[13977] _id=6ac66d6ade269131f9bc454e ts=2026-10-07T16:03:54.7440000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13978] _id=6ac66d6ade269131f9bc454f ts=2026-10-07T16:03:54.7440000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 264h 32m 
  - Evidence: 264h 32m: 6aa4144c41b41dbac0c7f269.jsonl[763] _id=6ab56762485cab4c95541c94 ts=2026-09-24T18:09:38.3640000Z -> 6aa4144c41b41dbac0c7f269.jsonl[10681] _id=6ac3ef8ade269131f9af4909 ts=2026-10-05T18:42:18.7750000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 6aa4144c41b41dbac0c7f269.jsonl[9348] _id=6abe8781485cab4c95abd44a ts=2026-10-01T16:17:05.9320000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9357] _id=6ac3cba1de269131f9ad9469 ts=2026-10-05T16:09:03.6090000Z; 71h 27m: 6aa4144c41b41dbac0c7f269.jsonl[2917] _id=6ab6bfde485cab4c955e5f53 ts=2026-09-25T18:39:26.8290000Z -> 6aa4144c41b41dbac0c7f269.jsonl[2952] _id=6abaacc1485cab4c956f7297 ts=2026-09-28T18:06:57.4000000Z; 24h 5m: 6aa4144c41b41dbac0c7f269.jsonl[777] _id=6ab567cb485cab4c9554205a ts=2026-09-24T18:11:23.6180000Z -> 6aa4144c41b41dbac0c7f269.jsonl[786] _id=6ab6ba97485cab4c955de60d ts=2026-09-25T18:16:58.1490000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 212 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f269.jsonl[11662] _id=6ac5396dde269131f9b6288a ts=2026-10-06T18:09:49.0960000Z -> 6aa4144c41b41dbac0c7f269.jsonl[11658] _id=6ac5396dde269131f9b6288e ts=2026-10-06T18:09:49.0960000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[11666] _id=6ac5396dde269131f9b6289c ts=2026-10-06T18:09:49.1020000Z -> 6aa4144c41b41dbac0c7f269.jsonl[11667] _id=6ac5396dde269131f9b6289e ts=2026-10-06T18:09:49.1020000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[13035] _id=6ac667c0de269131f9bc0be9 ts=2026-10-07T15:39:43.6360000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13036] _id=6ac667c0de269131f9bc0bea ts=2026-10-07T15:39:43.6360000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 54m 
  - Evidence: 95h 54m: 6aa4144c41b41dbac0c7f269.jsonl[9309] _id=6abe871a485cab4c95abcdfc ts=2026-10-01T16:15:22.1850000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9428] _id=6ac3cbbede269131f9ad9615 ts=2026-10-05T16:09:34.2770000Z; 72h 0m: 6aa4144c41b41dbac0c7f269.jsonl[2756] _id=6ab6bd89485cab4c955e42e0 ts=2026-09-25T18:29:32.3050000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3500] _id=6abab22f485cab4c95700b27 ts=2026-09-28T18:30:07.5120000Z; 24h 10m: 6aa4144c41b41dbac0c7f269.jsonl[739] _id=6ab56738485cab4c95541958 ts=2026-09-24T18:08:56.8910000Z -> 6aa4144c41b41dbac0c7f269.jsonl[858] _id=6ab6bb36485cab4c955e0095 ts=2026-09-25T18:19:37.1830000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f269.jsonl[14316] _id=6ac68c36de269131f9bdadba ts=2026-10-07T18:15:18.7770000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14317] _id=6ac68c36de269131f9bdadbb ts=2026-10-07T18:15:18.7770000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[14364] _id=6ac68c7dde269131f9bdaed9 ts=2026-10-07T18:16:29.2360000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14365] _id=6ac68c7dde269131f9bdaeda ts=2026-10-07T18:16:29.2360000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[14574] _id=6ac6912cde269131f9bdd0e5 ts=2026-10-07T18:36:28.4000000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14575] _id=6ac6912cde269131f9bdd0e6 ts=2026-10-07T18:36:28.4000000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa4144c41b41dbac0c7f269.jsonl[9346] _id=6abe877b485cab4c95abd3f2 ts=2026-10-01T16:16:59.8340000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9365] _id=6ac3cba1de269131f9ad9467 ts=2026-10-05T16:09:00.8660000Z; 71h 25m: 6aa4144c41b41dbac0c7f269.jsonl[2943] _id=6ab6c05f485cab4c955e65d9 ts=2026-09-25T18:41:35.6430000Z -> 6aa4144c41b41dbac0c7f269.jsonl[2955] _id=6abaacc1485cab4c956f7295 ts=2026-09-28T18:06:51.3740000Z; 24h 5m: 6aa4144c41b41dbac0c7f269.jsonl[779] _id=6ab567d8485cab4c955420c4 ts=2026-09-24T18:11:36.9620000Z -> 6aa4144c41b41dbac0c7f269.jsonl[789] _id=6ab6ba97485cab4c955de608 ts=2026-09-25T18:16:52.2920000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa4144c41b41dbac0c7f269.jsonl[8995] _id=6abe842c485cab4c95abb1e6 ts=2026-10-01T16:02:49.0840000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9373] _id=6ac3cba2de269131f9ad9479 ts=2026-10-05T16:09:03.6270000Z; 71h 59m: 6aa4144c41b41dbac0c7f269.jsonl[2724] _id=6ab6bd45485cab4c955e4041 ts=2026-09-25T18:28:23.3040000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3461] _id=6abab18e485cab4c957000c9 ts=2026-09-28T18:27:25.0710000Z; 45h 44m: 6aa4144c41b41dbac0c7f269.jsonl[5921] _id=6abc0063485cab4c95843595 ts=2026-09-29T18:16:02.7660000Z -> 6aa4144c41b41dbac0c7f269.jsonl[8706] _id=6abe8399485cab4c95abacb0 ts=2026-10-01T16:00:25.0330000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2754 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f269.jsonl[1004] _id=6ab6bb92485cab4c955e12b3 ts=2026-09-25T18:21:07.6510000Z -> 6aa4144c41b41dbac0c7f269.jsonl[1005] _id=6ab6bb92485cab4c955e12b5 ts=2026-09-25T18:21:07.6510000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[1016] _id=6ab6bb94485cab4c955e12f0 ts=2026-09-25T18:21:10.4320000Z -> 6aa4144c41b41dbac0c7f269.jsonl[1017] _id=6ab6bb94485cab4c955e12f5 ts=2026-09-25T18:21:10.4320000Z; 0ms: 6aa4144c41b41dbac0c7f269.jsonl[1017] _id=6ab6bb94485cab4c955e12f5 ts=2026-09-25T18:21:10.4320000Z -> 6aa4144c41b41dbac0c7f269.jsonl[1018] _id=6ab6bb94485cab4c955e12f9 ts=2026-09-25T18:21:10.4320000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6aa4144c41b41dbac0c7f269.jsonl[8682] _id=6abe836e485cab4c95aba9de ts=2026-10-01T15:59:42.3590000Z -> 6aa4144c41b41dbac0c7f269.jsonl[10835] _id=6ac5175ede269131f9b4ab1f ts=2026-10-06T15:44:30.5930000Z; 72h 0m: 6aa4144c41b41dbac0c7f269.jsonl[2757] _id=6ab6bd8c485cab4c955e42ed ts=2026-09-25T18:29:35.2770000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3539] _id=6abab22f485cab4c95700b23 ts=2026-09-28T18:30:07.5070000Z; 69h 28m: 6aa4144c41b41dbac0c7f269.jsonl[3568] _id=6abab259485cab4c95700dad ts=2026-09-28T18:30:49.1980000Z -> 6aa4144c41b41dbac0c7f269.jsonl[8658] _id=6abe835b485cab4c95aba7c0 ts=2026-10-01T15:59:23.6190000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6aa4144c41b41dbac0c7f269.jsonl[7012] _id=6abd5412485cab4c9591693b ts=2026-09-30T18:25:22.7350000Z -> 6aa4144c41b41dbac0c7f269.jsonl[10406] _id=6ac3ea94de269131f9aee8e7 ts=2026-10-05T18:21:08.5160000Z; 71h 28m: 6aa4144c41b41dbac0c7f269.jsonl[2935] _id=6ab6c04c485cab4c955e653b ts=2026-09-25T18:41:16.2550000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3058] _id=6abaad7b485cab4c956f861f ts=2026-09-28T18:10:02.6810000Z; 24h 6m: 6aa4144c41b41dbac0c7f269.jsonl[3385] _id=6abab0e5485cab4c956ff47b ts=2026-09-28T18:24:37.3050000Z -> 6aa4144c41b41dbac0c7f269.jsonl[6202] _id=6abc03fe485cab4c95848447 ts=2026-09-29T18:31:26.5890000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.012s..0.029s shown 
  - Evidence: 12ms: 6aa4144c41b41dbac0c7f269.jsonl[3062] _id=6abaad91485cab4c956f8957 ts=2026-09-28T18:10:25.9920000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3060] _id=6abaad92485cab4c956f8967 ts=2026-09-28T18:10:26.0040000Z; 29ms: 6aa4144c41b41dbac0c7f269.jsonl[3061] _id=6abaad91485cab4c956f8953 ts=2026-09-28T18:10:25.9630000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3062] _id=6abaad91485cab4c956f8957 ts=2026-09-28T18:10:25.9920000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 165h 44m 
  - Evidence: 165h 44m: 6aa4144c41b41dbac0c7f269.jsonl[667] _id=6ab566b1485cab4c95540b9e ts=2026-09-24T18:06:40.9970000Z -> 6aa4144c41b41dbac0c7f269.jsonl[8245] _id=6abe815e485cab4c95ab832d ts=2026-10-01T15:50:53.9740000Z; 144h 0m: 6aa4144c41b41dbac0c7f269.jsonl[8313] _id=6abe8247485cab4c95ab956a ts=2026-10-01T15:54:47.0030000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13671] _id=6ac66b64de269131f9bc3b3a ts=2026-10-07T15:55:16.0120000Z; 2h 14m: 6aa4144c41b41dbac0c7f269.jsonl[14204] _id=6ac66e67de269131f9bc4a56 ts=2026-10-07T16:08:07.5690000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14463] _id=6ac68deede269131f9bdb597 ts=2026-10-07T18:22:38.1030000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 165h 43m 
  - Evidence: 165h 43m: 6aa4144c41b41dbac0c7f269.jsonl[664] _id=6ab566b1485cab4c95540ba4 ts=2026-09-24T18:06:41.0220000Z -> 6aa4144c41b41dbac0c7f269.jsonl[8191] _id=6abe8134485cab4c95ab7ec6 ts=2026-10-01T15:50:12.0200000Z; 143h 59m: 6aa4144c41b41dbac0c7f269.jsonl[8486] _id=6abe8247485cab4c95ab9576 ts=2026-10-01T15:54:47.0640000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13603] _id=6ac66b37de269131f9bc3a0a ts=2026-10-07T15:54:31.6700000Z; 2h 14m: 6aa4144c41b41dbac0c7f269.jsonl[14201] _id=6ac66e67de269131f9bc4a5b ts=2026-10-07T16:08:07.6370000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14438] _id=6ac68de3de269131f9bdb55f ts=2026-10-07T18:22:27.4820000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.019s..0.045s shown 
  - Evidence: 19ms: 6aa4144c41b41dbac0c7f269.jsonl[14775] _id=6ac692f1de269131f9bdf4aa ts=2026-10-07T18:44:00.9440000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14778] _id=6ac692f1de269131f9bdf4ad ts=2026-10-07T18:44:00.9630000Z; 36ms: 6aa4144c41b41dbac0c7f269.jsonl[8483] _id=6abe8247485cab4c95ab956e ts=2026-10-01T15:54:47.0280000Z -> 6aa4144c41b41dbac0c7f269.jsonl[8486] _id=6abe8247485cab4c95ab9576 ts=2026-10-01T15:54:47.0640000Z; 45ms: 6aa4144c41b41dbac0c7f269.jsonl[14198] _id=6ac66e67de269131f9bc4a58 ts=2026-10-07T16:08:07.5920000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14201] _id=6ac66e67de269131f9bc4a5b ts=2026-10-07T16:08:07.6370000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 165h 43m 
  - Evidence: 165h 43m: 6aa4144c41b41dbac0c7f269.jsonl[662] _id=6ab566ae485cab4c95540b3e ts=2026-09-24T18:06:38.2490000Z -> 6aa4144c41b41dbac0c7f269.jsonl[8175] _id=6abe8139485cab4c95ab7f6e ts=2026-10-01T15:50:17.6870000Z; 143h 59m: 6aa4144c41b41dbac0c7f269.jsonl[8312] _id=6abe8245485cab4c95ab955a ts=2026-10-01T15:54:45.4630000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13609] _id=6ac66b33de269131f9bc39f0 ts=2026-10-07T15:54:27.0050000Z; 2h 14m: 6aa4144c41b41dbac0c7f269.jsonl[14181] _id=6ac66e65de269131f9bc4a48 ts=2026-10-07T16:08:05.7570000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14439] _id=6ac68de7de269131f9bdb56c ts=2026-10-07T18:22:31.4470000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 159 interval(s) ≤ 0.019s..0.021s shown 
  - Evidence: 19ms: 6aa4144c41b41dbac0c7f269.jsonl[14460] _id=6ac68decde269131f9bdb58d ts=2026-10-07T18:22:36.2710000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14466] _id=6ac68decde269131f9bdb58f ts=2026-10-07T18:22:36.2900000Z; 19ms: 6aa4144c41b41dbac0c7f269.jsonl[14747] _id=6ac6929dde269131f9bdec02 ts=2026-10-07T18:42:37.5240000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14748] _id=6ac6929dde269131f9bdec04 ts=2026-10-07T18:42:37.5430000Z; 21ms: 6aa4144c41b41dbac0c7f269.jsonl[14484] _id=6ac68df9de269131f9bdb604 ts=2026-10-07T18:22:49.5580000Z -> 6aa4144c41b41dbac0c7f269.jsonl[14485] _id=6ac68df9de269131f9bdb606 ts=2026-10-07T18:22:49.5790000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 96h 28m 
  - Evidence: 96h 28m: 6aa4144c41b41dbac0c7f269.jsonl[7816] _id=6abe7ec9485cab4c95ab0e84 ts=2026-10-01T15:39:54.2560000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9354] _id=6ac3cb63de269131f9ad9249 ts=2026-10-05T16:08:03.1430000Z; 71h 50m: 6aa4144c41b41dbac0c7f269.jsonl[782] _id=6ab6ba83485cab4c955de42d ts=2026-09-25T18:16:38.7560000Z -> 6aa4144c41b41dbac0c7f269.jsonl[2947] _id=6abaacb4485cab4c956f71c1 ts=2026-09-28T18:06:44.4890000Z; 24h 5m: 6aa4144c41b41dbac0c7f269.jsonl[765] _id=6ab567b1485cab4c95541f8e ts=2026-09-24T18:10:57.6670000Z -> 6aa4144c41b41dbac0c7f269.jsonl[782] _id=6ab6ba83485cab4c955de42d ts=2026-09-25T18:16:38.7560000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 96h 28m 
  - Evidence: 96h 28m: 6aa4144c41b41dbac0c7f269.jsonl[7817] _id=6abe7ec8485cab4c95ab0e6e ts=2026-10-01T15:39:54.2550000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9353] _id=6ac3cb63de269131f9ad9247 ts=2026-10-05T16:08:03.1420000Z; 71h 32m: 6aa4144c41b41dbac0c7f269.jsonl[2801] _id=6ab6be8a485cab4c955e4bab ts=2026-09-25T18:33:48.6820000Z -> 6aa4144c41b41dbac0c7f269.jsonl[2948] _id=6abaacb4485cab4c956f71b5 ts=2026-09-28T18:06:44.4890000Z; 24h 5m: 6aa4144c41b41dbac0c7f269.jsonl[764] _id=6ab567b1485cab4c95541f8c ts=2026-09-24T18:10:57.6660000Z -> 6aa4144c41b41dbac0c7f269.jsonl[784] _id=6ab6ba83485cab4c955de425 ts=2026-09-25T18:16:38.7550000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 99h 31m 
  - Evidence: 99h 31m: 6aa4144c41b41dbac0c7f269.jsonl[7560] _id=6abe55bf485cab4c95a3de33 ts=2026-10-01T12:44:47.7360000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9788] _id=6ac3cd43de269131f9ada297 ts=2026-10-05T16:16:03.2840000Z; 71h 36m: 6aa4144c41b41dbac0c7f269.jsonl[2942] _id=6ab6c061485cab4c955e65dd ts=2026-09-25T18:41:37.2510000Z -> 6aa4144c41b41dbac0c7f269.jsonl[3199] _id=6abaaf46485cab4c956fbf8f ts=2026-09-28T18:17:42.2060000Z; 45h 19m: 6aa4144c41b41dbac0c7f269.jsonl[10423] _id=6ac3eac4de269131f9aeec47 ts=2026-10-05T18:21:55.9740000Z -> 6aa4144c41b41dbac0c7f269.jsonl[13142] _id=6ac66812de269131f9bc13b6 ts=2026-10-07T15:41:06.7460000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 96h 8m 
  - Evidence: 96h 8m: 6aa4144c41b41dbac0c7f269.jsonl[8712] _id=6abe83a2485cab4c95abad14 ts=2026-10-01T16:00:34.2340000Z -> 6aa4144c41b41dbac0c7f269.jsonl[9360] _id=6ac3cba2de269131f9ad9475 ts=2026-10-05T16:09:05.2390000Z; 71h 26m: 6aa4144c41b41dbac0c7f269.jsonl[2932] _id=6ab6c038485cab4c955e6497 ts=2026-09-25T18:40:56.5200000Z -> 6aa4144c41b41dbac0c7f269.jsonl[2961] _id=6abaacc2485cab4c956f72a9 ts=2026-09-28T18:06:57.4340000Z; 24h 9m: 6aa4144c41b41dbac0c7f269.jsonl[740] _id=6ab5673b485cab4c9554199a ts=2026-09-24T18:08:59.0270000Z -> 6aa4144c41b41dbac0c7f269.jsonl[823] _id=6ab6baf3485cab4c955df49d ts=2026-09-25T18:18:30.7680000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f269.jsonl[578] _id=6ab565c7485cab4c9553f058 ts=2026-09-24T18:02:47.6820000Z -> 6aa4144c41b41dbac0c7f269.jsonl[579] _id=6ab565c7485cab4c9553f05a ts=2026-09-24T18:02:47.6830000Z; 4ms: 6aa4144c41b41dbac0c7f269.jsonl[5564] _id=6abbfef5485cab4c95841bcb ts=2026-09-29T18:09:55.4640000Z -> 6aa4144c41b41dbac0c7f269.jsonl[5565] _id=6abbfef5485cab4c95841bcd ts=2026-09-29T18:09:55.4680000Z; 5ms: 6aa4144c41b41dbac0c7f269.jsonl[11455] _id=6ac5196ede269131f9b4c719 ts=2026-10-06T15:53:18.4410000Z -> 6aa4144c41b41dbac0c7f269.jsonl[11456] _id=6ac5196ede269131f9b4c71b ts=2026-10-06T15:53:18.4460000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[558] _id=6ab565a7485cab4c9553ea82 ts=2026-09-24T18:02:15.3180000Z`; `6aa4144c41b41dbac0c7f269.jsonl[679] _id=6ab566ce485cab4c95540f8a ts=2026-09-24T18:07:10.8470000Z`; `6aa4144c41b41dbac0c7f269.jsonl[5265] _id=6abab5d9485cab4c95705a0b ts=2026-09-28T18:45:45.5560000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 98 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[1487] _id=6ab6bc4d485cab4c955e2269 ts=2026-09-25T18:24:16.0530000Z`; `6aa4144c41b41dbac0c7f269.jsonl[1861] _id=6ab6bca7485cab4c955e2c5f ts=2026-09-25T18:25:44.9750000Z`; `6aa4144c41b41dbac0c7f269.jsonl[1930] _id=6ab6bcb5485cab4c955e2e0b ts=2026-09-25T18:25:58.4700000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 248 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[1131] _id=6ab6bc1b485cab4c955e1d85 ts=2026-09-25T18:20:52.4080000Z`; `6aa4144c41b41dbac0c7f269.jsonl[925] _id=6ab6bb86485cab4c955e104a ts=2026-09-25T18:20:55.4120000Z`; `6aa4144c41b41dbac0c7f269.jsonl[915] _id=6ab6bb86485cab4c955e1071 ts=2026-09-25T18:20:55.4260000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[8486] _id=6abe8247485cab4c95ab9576 ts=2026-10-01T15:54:47.0640000Z`; `6aa4144c41b41dbac0c7f269.jsonl[14201] _id=6ac66e67de269131f9bc4a5b ts=2026-10-07T16:08:07.6370000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[8476] _id=6abe823d485cab4c95ab948c ts=2026-10-01T15:54:37.0660000Z`; `6aa4144c41b41dbac0c7f269.jsonl[8460] _id=6abe823d485cab4c95ab9490 ts=2026-10-01T15:54:37.1100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[791] _id=6ab6ba97485cab4c955de604 ts=?`; `6aa4144c41b41dbac0c7f269.jsonl[2951] _id=6abaacc1485cab4c956f7293 ts=?`; `6aa4144c41b41dbac0c7f269.jsonl[5538] _id=6abbfef3485cab4c95841bbb ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 728 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[1262] _id=6ab6bc27485cab4c955e1fbf ts=2026-09-25T18:23:23.7070000Z`; `6aa4144c41b41dbac0c7f269.jsonl[1244] _id=6ab6bc27485cab4c955e1fc1 ts=2026-09-25T18:23:23.7740000Z`; `6aa4144c41b41dbac0c7f269.jsonl[1275] _id=6ab6bc27485cab4c955e1fc5 ts=2026-09-25T18:23:23.8730000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 914 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[1133] _id=6ab6bc1b485cab4c955e1d8b ts=2026-09-25T18:20:54.0420000Z`; `6aa4144c41b41dbac0c7f269.jsonl[935] _id=6ab6bb85485cab4c955e0ffb ts=2026-09-25T18:20:54.8500000Z`; `6aa4144c41b41dbac0c7f269.jsonl[903] _id=6ab6bb85485cab4c955e1011 ts=2026-09-25T18:20:54.8670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 13 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[3058] _id=6abaad7b485cab4c956f861f ts=2026-09-28T18:10:02.6810000Z`; `6aa4144c41b41dbac0c7f269.jsonl[3062] _id=6abaad91485cab4c956f8957 ts=2026-09-28T18:10:25.9920000Z`; `6aa4144c41b41dbac0c7f269.jsonl[3060] _id=6abaad92485cab4c956f8967 ts=2026-09-28T18:10:26.0040000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[14699] _id=6ac69229de269131f9bde130 ts=2026-10-07T18:40:41.1760000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[8319] _id=6abe81ab485cab4c95ab89b6 ts=2026-10-01T15:52:11.0090000Z`; `6aa4144c41b41dbac0c7f269.jsonl[8405] _id=6abe81ec485cab4c95ab8e38 ts=2026-10-01T15:53:16.0380000Z`; `6aa4144c41b41dbac0c7f269.jsonl[8406] _id=6abe81f0485cab4c95ab8e7a ts=2026-10-01T15:53:20.0240000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 454 start, 443 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 172 unmatched 'BecameCameraCentered' (totals: 955 open, 881 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 124 unmatched 'BecameVisible' (totals: 1337 open, 1461 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 15 open, 12 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 7 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'questActiveEvent' (totals: 56 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 393 of 15017 adjacent _id pairs reverse in client time; worst 168.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f269.jsonl[1118] _id=6ab6bc1a485cab4c955e1d69 ts=2026-09-25T18:23:25.2710000Z`; `6aa4144c41b41dbac0c7f269.jsonl[1121] _id=6ab6bc1b485cab4c955e1d6b ts=2026-09-25T18:20:37.1510000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -166.13s, max +3.14s over 15018 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f269\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
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

### `PuzzlePieceVisibleEvent` — 4634 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3420); Unit 4 Dev (618); Unit 3 Dungeon Dev (596)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.22s, n=4633)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4634/4634 records)
    "BecameInvisible"  x1461
    "BecameVisible"  x1337
    "BecameCameraCentered"  x955
    "BecameCameraUncentered"  x881
data.pieceId  (string, 4634/4634 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4634/4634 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4170 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1095); Unit 3 Dev (942); Unit 4 Dev - Dungeon (759); Unit 3 Dungeon Dev (521); Unit 4 Dev (397); Unit 4 Dev - Anderson Base (246); Unit 1 Dev (210)
- **Intervals:** median 0.92s (p5 0.05s / p95 15.16s, n=4169)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4170/4170 records)
    "pressed"  x4170
data.actionType  (string, 4170/4170 records)
    "Move"  x2421
    "Interact"  x587
    "Sprint"  x497
    "Jump"  x399
    "Ascend"  x206
    "Hoverboard"  x38
    "Map"  x7
    "Descend"  x6
    "SkipCinematic"  x6
    "Pause"  x3
data.key  (string, 4170/4170 records, 6 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4170/4170 records)
    "Player"  x3116
    "Drone"  x1054
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2350 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (743); Unit 3 Dev (438); Unit 4 Dev - Dungeon (269); Unit 4 Dev - Anderson Base (248); Unit 1 Dev (240); Unit 3 Dungeon Dev (220); Unit 4 Dev (192)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2340)
- **Fields under `data`:**

```text
data.position  (object, 2350/2350 records)
data.position.x  (number, 2350/2350 records)
    numeric range -678.01 .. 1585.51 (668 unique)
data.position.y  (number, 2350/2350 records)
    numeric range -25334.2 .. 159.087 (473 unique)
data.position.z  (number, 2350/2350 records)
    numeric range -1035.19 .. 1827.05 (669 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2332 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (646); Unit 3 Dev (464); Unit 4 Dev - Anderson Base (320); Unit 4 Dev (273); Unit 3 Dungeon Dev (246); Unit 1 Dev (233); Unit 4 Dev - Dungeon (150)
- **eventKey:** present on 1435 of 2332 records
- **Intervals:** median 4.28s (p5 0.00s / p95 35.20s, n=2331)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1435; [conversationId, dialogueEventType] x897
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2332/2332 records)
    numeric range 8 .. 114 (43 unique)
data.dialogueEventType  (string, 2332/2332 records)
    "DialogueNodeEvent"  x1435
    "DialogueStartEvent"  x454
    "DialogueFinishEvent"  x443
data.nodeId  (number, 1435/2332 records)
    numeric range 0 .. 290 (222 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 700 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (468); Unit 3 Dev (201); Unit 1 Dev (31)
- **Intervals:** median 0.26s (p5 0.03s / p95 8.48s, n=699)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 700/700 records)
    "argumentationNodeHoverEnd"  x288
    "argumentationNodeHoverStart"  x286
    "argumentationNodeAdd"  x73
    "argumentationNodeRemove"  x53
data.argumentationTitle  (string, 700/700 records)
    "Unit 4 - Flooding"  x468
    "Unit 3 - Pollution Upstream"  x201
    "Unit 1 - Freshwater"  x31
data.nodeName  (string, 700/700 records)
    "B"  x111
    "A"  x86
    "I"  x86
    "C"  x77
    "II"  x73
    "D"  x70
    "2"  x69
    "3"  x48
    "1"  x45
    "4"  x30
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 362 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (165); Unit 3 Dungeon Dev (64); Unit 2 Prod (Refactor) (59); Unit 4 Dev - Anderson Base (27); Unit 4 Dev (20); Unit 1 Dev (15); Unit 3 Dev (12)
- **Intervals:** median 9.48s (p5 0.26s / p95 442.52s, n=361)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 362/362 records)
    37 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 362/362 records)
    94 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 88 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 1 Dev (17); Unit 3 Dev (16); Unit 4 Dev - Dungeon (12); Unit 4 Dev (10); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (4)
- **eventKey:** present on 88 of 88 records
- **Intervals:** median 257.46s (p5 0.01s / p95 80619.80s, n=87)
- **`data` key-set variants:** [questEventType, questID, questName] x56; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 88/88 records)
    "questActiveEvent"  x56
    "questFinishEvent"  x32
data.questID  (string, 88/88 records)
    26 unique values (see csv/event_unique_values.csv)
data.questName  (string, 88/88 records)
    26 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/88 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 72 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (52); Unit 3 Dev (14); Unit 1 Dev (6)
- **Intervals:** median 7.81s (p5 0.18s / p95 647.96s, n=71)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 72/72 records)
    "submitAnswerEvent"  x72
data.answerSubmitted  (string, 72/72 records, 5 empty-string)
    25 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 72/72 records)
    "Unit 4 - Flooding"  x52
    "Unit 3 - Pollution Upstream"  x14
    "Unit 1 - Freshwater"  x6
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `Soil Key Puzzle` — 60 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (22); Unit 4 Dev (10)
- **Intervals:** median 0.73s (p5 0.15s / p95 25021.96s, n=59)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/60 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/60 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/60 records)
    "RightDrag"  x29
    "LeftDrag"  x23
data.currentSoilType  (string, 52/60 records)
    "SAND"  x11
    "CLAY"  x9
    "CLAYSAND"  x9
    "SANDGRAVEL"  x9
    "CLAYROCK"  x8
    "BEDROCK"  x3
    "GRAVEL"  x3
data.isCorrectSelection  (string, 52/60 records)
    "false"  x40
    "true"  x12
data.waterLevelStatus  (string, 52/60 records)
    "Proper"  x28
    "TooHigh"  x21
    "TooLow"  x3
data.waterRetentionChange  (string, 52/60 records)
    "Decrease"  x21
    "Increase"  x19
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 51 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (26); Unit 2 Prod (Refactor) (9); Transition (6); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev (2)
- **Intervals:** median 515.18s (p5 9.84s / p95 86081.87s, n=50)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 51/51 records)
    true  x51
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TopographicMapEvent` — 45 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (17)
- **Intervals:** median 7.50s (p5 0.18s / p95 86683.38s, n=44)
- **`data` key-set variants:** [actionType, featureUsed] x27; [actionType, featureUsed, location] x18
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 45/45 records)
    "MapOpenEvent"  x15
    "MapCloseEvent"  x12
    "WaypointMoveEvent"  x12
    "WaypointSetEvent"  x6
data.featureUsed  (string, 45/45 records)
    "Map"  x27
    "Waypoint"  x18
data.location  (object, 18/45 records)
data.location.x  (number, 18/45 records)
    numeric range -223.09 .. 355.91 (14 unique)
data.location.y  (number, 18/45 records)
    numeric range -207.5 .. 281.5 (15 unique)
data.location.z  (number, 18/45 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 36 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (36)
- **Intervals:** median 2.25s (p5 0.29s / p95 83.04s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "ChangeCanister"  x36
data.canisterType  (string, 36/36 records)
    "Clay"  x24
    "Bedrock"  x6
    "Gravel"  x4
    "Sand"  x2
data.floor  (string, 36/36 records)
    "5"  x28
    "4"  x7
    "3"  x1
data.machine  (string, 36/36 records)
    "1"  x34
    "2"  x2
data.row  (string, 36/36 records)
    "TopRow"  x29
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 34 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 3 Dev (5); Unit 4 Dev (5); MainMenu (3); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1707.11s (p5 57.62s / p95 155487.32s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "DebugMenuStateChanged"  x34
data.isOpened  (bool, 34/34 records)
    false  x34
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 27 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (11); Transition (6); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev (2)
- **Intervals:** median 364.19s (p5 8.87s / p95 234111.41s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 26 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (26)
- **Intervals:** median 8895.88s (p5 110.82s / p95 224232.80s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (7); Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 199.77s (p5 0.03s / p95 549675.16s, n=13)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x7
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 4 - Flooding"  x7
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (7)
- **Intervals:** median 3.58s (p5 1.41s / p95 64.23s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolOpen"  x7
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x7
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - Watershed Image"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.40s (p5 0.90s / p95 18.07s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 6/6 records)
    "Gravel"  x4
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x3
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 0.48s (p5 0.48s / p95 0.48s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 952360.41s (p5 952360.41s / p95 952360.41s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (28 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (12x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (18x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (53x)
- `soilMachine` data.canisterType: "Bedrock" (6x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*