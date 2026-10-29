# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f271

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f271
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f271.jsonl
- **Records:** 13917 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f271
- **Time span:** 2026-09-23T18:15:43.231000+00:00 .. 2026-10-07T18:47:22.596000+00:00 (336h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f271\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 13917 records, 9 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 104 INFO, 0 NOT_TESTED, 83 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `WaterChamberEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4379 | 31.47 | 1 | 3 | 0 | 2026-09-25T18:41:40.537000+00:00 | 2026-10-07T18:46:09.492000+00:00 | 288h 4m |
| InputEvent | 4169 | 29.96 | 1 | 6 | 0 | 2026-09-23T18:16:21.374000+00:00 | 2026-10-07T18:44:27.735000+00:00 | 336h 28m |
| PlayerPositionEvent | 2505 | 18.0 | 1 | 7 | 0 | 2026-09-23T18:16:16.181000+00:00 | 2026-10-07T18:47:22.063000+00:00 | 336h 31m |
| DialogueEvent | 1790 | 12.86 | 1 | 7 | 1159 | 2026-09-23T18:16:38.026000+00:00 | 2026-10-07T18:47:22.596000+00:00 | 336h 30m |
| ObjectInterEvent | 339 | 2.44 | 1 | 6 | 0 | 2026-09-23T18:24:01.235000+00:00 | 2026-10-07T18:44:58.264000+00:00 | 336h 20m |
| argumentationNodeEvent | 296 | 2.13 | 1 | 3 | 0 | 2026-09-25T18:28:41.595000+00:00 | 2026-10-07T14:54:27.595000+00:00 | 284h 25m |
| questEvent | 93 | 0.67 | 1 | 7 | 93 | 2026-09-23T18:16:38.003000+00:00 | 2026-10-07T18:45:56.231000+00:00 | 336h 29m |
| TopographicMapEvent | 76 | 0.55 | 1 | 3 | 0 | 2026-09-28T18:08:37.832000+00:00 | 2026-10-05T20:01:32.749000+00:00 | 169h 52m |
| gameWindowFocusEvent | 48 | 0.34 | 1 | 8 | 0 | 2026-09-23T18:15:43.231000+00:00 | 2026-10-07T18:45:47.961000+00:00 | 336h 30m |
| Soil Key Puzzle | 42 | 0.3 | 1 | 2 | 0 | 2026-09-30T18:23:00.251000+00:00 | 2026-10-05T18:26:37.302000+00:00 | 120h 3m |
| DEBUGMenu | 34 | 0.24 | 1 | 8 | 0 | 2026-09-23T18:16:16.162000+00:00 | 2026-10-07T18:45:56.241000+00:00 | 336h 29m |
| gameStartEvent | 25 | 0.18 | 1 | 1 | 0 | 2026-09-23T18:15:43.232000+00:00 | 2026-10-07T18:45:47.961000+00:00 | 336h 30m |
| gameWindowUnfocusEvent | 25 | 0.18 | 1 | 7 | 0 | 2026-09-23T18:16:24.835000+00:00 | 2026-10-06T20:02:21.609000+00:00 | 313h 45m |
| argumentationAnswerEvent | 23 | 0.17 | 1 | 3 | 0 | 2026-09-25T18:30:46.422000+00:00 | 2026-10-07T14:54:34.097000+00:00 | 284h 23m |
| soilMachine | 16 | 0.11 | 1 | 1 | 0 | 2026-10-06T18:11:31.755000+00:00 | 2026-10-06T18:31:52.169000+00:00 | 20m 20s |
| TerasGardenBox | 15 | 0.11 | 1 | 1 | 0 | 2026-10-07T15:02:02.201000+00:00 | 2026-10-07T18:32:22.747000+00:00 | 3h 30m |
| DaniEvent | 14 | 0.1 | 1 | 3 | 0 | 2026-09-24T17:45:40.801000+00:00 | 2026-10-05T20:01:29.864000+00:00 | 266h 15m |
| argumentationEvent | 10 | 0.07 | 1 | 3 | 0 | 2026-09-25T18:30:36.475000+00:00 | 2026-10-07T14:54:34.159000+00:00 | 284h 23m |
| crash | 8 | 0.06 | 1 | 1 | 0 |  |  | ? |
| argumentationToolEvent | 5 | 0.04 | 1 | 1 | 0 | 2026-09-25T18:30:34.260000+00:00 | 2026-09-25T18:31:41.384000+00:00 | 1m 7s |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-09-30T18:12:06.031000+00:00 | 2026-10-07T18:45:56.119000+00:00 | 168h 33m |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-25T18:34:51.871000+00:00 | 2026-10-07T18:45:21.132000+00:00 | 288h 10m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 1037429.261s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.2s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 11.527s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 16.123s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.698s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 303415.044s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 5972.263s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 871.851s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2001.385s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 5 Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 14 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; press; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Place Glyph; Press E to Collect; Press E to Plant Seed; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 240 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.6x vs baseline. 
  - Observed: 23 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,3,I; A,4,I; B,1,II; B,2,II; B,3,I; B,3,II; B,4,II; C,D,A,2,II; D,1,II; D,4,II; D,C,B,2,II 
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-287, 18-289] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 25 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 44; 45; 51; 52; 53; 54; 55; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 35 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[484] _id=6ab41c5a485cab4c954f5e5f ts=2026-09-23T18:37:14.9560000Z`; `6aa4144c41b41dbac0c7f271.jsonl[543] _id=6ab41d82485cab4c954f673d ts=2026-09-23T18:42:10.6110000Z`; `6aa4144c41b41dbac0c7f271.jsonl[611] _id=6ab41e1c485cab4c954f6dc9 ts=2026-09-23T18:44:44.8380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:23' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[4626] _id=6abab3e3485cab4c957028bf ts=2026-09-28T18:37:22.8610000Z`; `6aa4144c41b41dbac0c7f271.jsonl[4819] _id=6abbffee485cab4c958429af ts=2026-09-29T18:14:06.9070000Z`; `6aa4144c41b41dbac0c7f271.jsonl[5444] _id=6abd4f60485cab4c9590d937 ts=2026-09-30T18:05:20.4280000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[14] _id=6ab4174f485cab4c954f36a6 ts=2026-09-23T18:15:43.2320000Z`; `6aa4144c41b41dbac0c7f271.jsonl[658] _id=6ab5619e485cab4c95538aaf ts=2026-09-24T17:45:01.6700000Z`; `6aa4144c41b41dbac0c7f271.jsonl[970] _id=6ab6b8fe485cab4c955db555 ts=2026-09-25T18:10:06.2470000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 48 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 48} 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[15] _id=6ab4174f485cab4c954f36a4 ts=2026-09-23T18:15:43.2310000Z`; `6aa4144c41b41dbac0c7f271.jsonl[26] _id=6ab4177d485cab4c954f37e4 ts=2026-09-23T18:16:29.4400000Z`; `6aa4144c41b41dbac0c7f271.jsonl[189] _id=6ab4198a485cab4c954f4856 ts=2026-09-23T18:25:14.7420000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[25] _id=6ab41778485cab4c954f37d2 ts=2026-09-23T18:16:24.8350000Z`; `6aa4144c41b41dbac0c7f271.jsonl[187] _id=6ab41989485cab4c954f4846 ts=2026-09-23T18:25:13.3430000Z`; `6aa4144c41b41dbac0c7f271.jsonl[768] _id=6ab5629b485cab4c95539e2e ts=2026-09-24T17:49:15.3150000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 76 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1947] _id=6abaad25485cab4c956f79c8 ts=2026-09-28T18:08:37.8320000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1963] _id=6abaad49485cab4c956f7f85 ts=2026-09-28T18:09:13.7580000Z`; `6aa4144c41b41dbac0c7f271.jsonl[4547] _id=6abab288485cab4c95701177 ts=2026-09-28T18:31:35.9240000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4378 | 0.0 | 0.032 | 236.882 | 1.507 | 358522.028 | 0.25 | 2684 | 6 |
| InputEvent | 4168 | 0.0 | 1.2 | 290.616 | 19.744 | 343553.067 | 0.21 | 145 | 16 |
| PlayerPositionEvent | 2496 | 9.581 | 9.999 | 485.257 | 10.177 | 343472.716 | 0.12 | 0 | 15 |
| DialogueEvent | 1789 | 0.0 | 5.444 | 677.163 | 62.731 | 343706.59 | 0.09 | 480 | 17 |
| ObjectInterEvent | 338 | 0.0 | 10.889 | 3582.417 | 421.693 | 344135.348 | 0.02 | 8 | 15 |
| argumentationNodeEvent | 295 | 0.006 | 0.311 | 3471.003 | 10.741 | 851963.374 | 0.02 | 66 | 2 |
| questEvent | 92 | 0.002 | 231.344 | 13166.937 | 83796.247 | 344382.172 | 0.0 | 22 | 24 |
| TopographicMapEvent | 75 | 0.565 | 11.527 | 8154.332 | 22925.004 | 363277.192 | 0.01 | 0 | 6 |
| gameWindowFocusEvent | 47 | 1.532 | 871.851 | 25774.569 | 86013.169 | 344678.65 | 0.0 | 0 | 25 |
| Soil Key Puzzle | 41 | 0.186 | 1.001 | 10541.879 | 11.94 | 432105.616 | 0.01 | 0 | 1 |
| DEBUGMenu | 33 | 5.537 | 1565.109 | 36708.487 | 155635.812 | 344682.991 | 0.0 | 0 | 24 |
| gameStartEvent | 24 | 48.626 | 5972.263 | 50475.197 | 231829.724 | 344678.65 | 0.0 | 0 | 21 |
| gameWindowUnfocusEvent | 24 | 2.549 | 2001.385 | 47064.866 | 232982.916 | 421002.181 | 0.0 | 0 | 17 |
| argumentationAnswerEvent | 22 | 0.734 | 16.123 | 46537.622 | 162854.249 | 851999.366 | 0.0 | 0 | 2 |
| soilMachine | 15 | 1.847 | 33.254 | 81.361 | 275.568 | 282.271 | 0.74 | 0 | 0 |
| TerasGardenBox | 14 | 0.186 | 5.287 | 901.468 | 4388.53 | 12431.813 | 0.07 | 0 | 1 |
| DaniEvent | 13 | 0.113 | 4.99 | 73734.543 | 434345.668 | 438552.32 | 0.0 | 0 | 3 |
| argumentationEvent | 9 | 0.031 | 37.368 | 113759.743 | 579754.11 | 851983.804 | 0.0 | 2 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationToolEvent | 4 | 0.635 | 1.698 | 16.781 | 53.955 | 63.092 | 3.58 | 0 | 0 |
| chatEvent | 2 | 4.897 | 303415.044 | 303415.044 | 576484.176 | 606825.191 | 0.0 | 0 | 1 |
| EndOfUnit | 1 | 1037429.261 | 1037429.261 | 1037429.261 | 1037429.261 | 1037429.261 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 6 group(s), 17 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[4625] _id=6abab3e3485cab4c957028b7 ts=2026-09-28T18:37:22.8370000Z == 6aa4144c41b41dbac0c7f271.jsonl[4602] _id=6abab3e3485cab4c957028bd ts=2026-09-28T18:37:22.8370000Z`; `6aa4144c41b41dbac0c7f271.jsonl[12566] _id=6ac5507bde269131f9b7b8b0 ts=2026-10-06T19:48:09.0350000Z == 6aa4144c41b41dbac0c7f271.jsonl[12567] _id=6ac5507bde269131f9b7b8b1 ts=2026-10-06T19:48:09.0350000Z`; `6aa4144c41b41dbac0c7f271.jsonl[12570] _id=6ac5507bde269131f9b7b8b5 ts=2026-10-06T19:48:09.4100000Z == 6aa4144c41b41dbac0c7f271.jsonl[12571] _id=6ac5507bde269131f9b7b8b6 ts=2026-10-06T19:48:09.4100000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[12415] _id=6ac541b5de269131f9b6d20b ts=2026-10-06T18:45:09.5920000Z == 6aa4144c41b41dbac0c7f271.jsonl[12411] _id=6ac541b5de269131f9b6d211 ts=2026-10-06T18:45:09.5920000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 155 group(s), 211 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1866] _id=6abaacd6485cab4c956f738b ts=2026-09-28T18:07:17.9920000Z == 6aa4144c41b41dbac0c7f271.jsonl[1867] _id=6abaacd6485cab4c956f738d ts=2026-09-28T18:07:17.9920000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1879] _id=6abaacd7485cab4c956f7399 ts=2026-09-28T18:07:18.2000000Z == 6aa4144c41b41dbac0c7f271.jsonl[1872] _id=6abaacd7485cab4c956f739d ts=2026-09-28T18:07:18.2000000Z`; `6aa4144c41b41dbac0c7f271.jsonl[2000] _id=6abaad73485cab4c956f84d5 ts=2026-09-28T18:07:42.9650000Z == 6aa4144c41b41dbac0c7f271.jsonl[2018] _id=6abaad73485cab4c956f84d7 ts=2026-09-28T18:07:42.9650000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1723] _id=6abaabfe485cab4c956f674f ts=? == 6aa4144c41b41dbac0c7f271.jsonl[5445] _id=6abd4f60485cab4c9590d92d ts=?`; `6aa4144c41b41dbac0c7f271.jsonl[10657] _id=6ac50e3ede269131f9b42bec ts=? == 6aa4144c41b41dbac0c7f271.jsonl[12606] _id=6ac551b5de269131f9b7c814 ts=?`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `113ms: 6aa4144c41b41dbac0c7f271.jsonl[1108] _id=6ab6bb3d485cab4c955e0265 ts=2026-09-25T18:19:41.2120000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[1105] _id=6ab6bb3d485cab4c955e0269 ts=2026-09-25T18:19:41.3250000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 39 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `199ms: 6aa4144c41b41dbac0c7f271.jsonl[134] _id=6ab41943485cab4c954f4574 ts=2026-09-23T18:24:03.9570000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[136] _id=6ab41944485cab4c954f457c ts=2026-09-23T18:24:04.1560000Z`; `650ms: 6aa4144c41b41dbac0c7f271.jsonl[153] _id=6ab41959485cab4c954f4672 ts=2026-09-23T18:24:25.7310000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[155] _id=6ab4195a485cab4c954f467e ts=2026-09-23T18:24:26.3810000Z`; `633ms: 6aa4144c41b41dbac0c7f271.jsonl[155] _id=6ab4195a485cab4c954f467e ts=2026-09-23T18:24:26.3810000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[159] _id=6ab4195a485cab4c954f4686 ts=2026-09-23T18:24:27.0140000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 615 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6aa4144c41b41dbac0c7f271.jsonl[1869] _id=6abaacd8485cab4c956f73b5 ts=2026-09-28T18:07:19.4010000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[1870] _id=6abaacd8485cab4c956f73b7 ts=2026-09-28T18:07:19.4350000Z`; `16ms: 6aa4144c41b41dbac0c7f271.jsonl[1870] _id=6abaacd8485cab4c956f73b7 ts=2026-09-28T18:07:19.4350000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[1883] _id=6abaacd8485cab4c956f73b9 ts=2026-09-28T18:07:19.4510000Z`; `9ms: 6aa4144c41b41dbac0c7f271.jsonl[2027] _id=6abaad74485cab4c956f84f3 ts=2026-09-28T18:07:53.5960000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[2038] _id=6abaad74485cab4c956f84f7 ts=2026-09-28T18:07:53.6050000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `186ms: 6aa4144c41b41dbac0c7f271.jsonl[13301] _id=6ac65eeade269131f9bb6565 ts=2026-10-07T15:02:02.2010000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[13324] _id=6ac65eeade269131f9bb6567 ts=2026-10-07T15:02:02.3870000Z`; `806ms: 6aa4144c41b41dbac0c7f271.jsonl[13324] _id=6ac65eeade269131f9bb6567 ts=2026-10-07T15:02:02.3870000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[13304] _id=6ac65eebde269131f9bb6571 ts=2026-10-07T15:02:03.1930000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `734ms: 6aa4144c41b41dbac0c7f271.jsonl[8762] _id=6ac3be3cde269131f9acdbb7 ts=2026-10-05T15:11:56.0940000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[8761] _id=6ac3be3cde269131f9acdbc3 ts=2026-10-05T15:11:56.8280000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6aa4144c41b41dbac0c7f271.jsonl[8891] _id=6ac3bed2de269131f9ace362 ts=2026-10-05T15:14:26.1390000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[8902] _id=6ac3bed2de269131f9ace36b ts=2026-10-05T15:14:26.1780000Z`; `31ms: 6aa4144c41b41dbac0c7f271.jsonl[13199] _id=6ac65d2ade269131f9bb3919 ts=2026-10-07T14:54:34.1280000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[13202] _id=6ac65d2ade269131f9bb391c ts=2026-10-07T14:54:34.1590000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 46 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `396ms: 6aa4144c41b41dbac0c7f271.jsonl[1332] _id=6ab6bd59485cab4c955e415f ts=2026-09-25T18:28:41.5950000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[1334] _id=6ab6bd59485cab4c955e4167 ts=2026-09-25T18:28:41.9910000Z`; `691ms: 6aa4144c41b41dbac0c7f271.jsonl[1333] _id=6ab6bd59485cab4c955e4161 ts=2026-09-25T18:28:41.6250000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[1335] _id=6ab6bd5a485cab4c955e4169 ts=2026-09-25T18:28:42.3160000Z`; `697ms: 6aa4144c41b41dbac0c7f271.jsonl[1334] _id=6ab6bd59485cab4c955e4167 ts=2026-09-25T18:28:41.9910000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[1325] _id=6ab6bd5a485cab4c955e416b ts=2026-09-25T18:28:42.6880000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6aa4144c41b41dbac0c7f271.jsonl[4626] _id=6abab3e3485cab4c957028bf ts=2026-09-28T18:37:22.8610000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[4603] _id=6abab3e3485cab4c957028c1 ts=2026-09-28T18:37:22.8870000Z`; `47ms: 6aa4144c41b41dbac0c7f271.jsonl[4819] _id=6abbffee485cab4c958429af ts=2026-09-29T18:14:06.9070000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[4822] _id=6abbffee485cab4c958429b5 ts=2026-09-29T18:14:06.9540000Z`; `3ms: 6aa4144c41b41dbac0c7f271.jsonl[5444] _id=6abd4f60485cab4c9590d937 ts=2026-09-30T18:05:20.4280000Z ~ 6aa4144c41b41dbac0c7f271.jsonl[5450] _id=6abd4f60485cab4c9590d93b ts=2026-09-30T18:05:20.4310000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 6aa4144c41b41dbac0c7f271.jsonl[7659] _id=6abe7476485cab4c95a97c52 ts=2026-10-01T14:55:50.8300000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7957] _id=6ac3b6e1de269131f9ac4786 ts=2026-10-05T14:40:33.8210000Z; 71h 27m: 6aa4144c41b41dbac0c7f271.jsonl[1540] _id=6ab6bf27485cab4c955e5330 ts=2026-09-25T18:36:23.9120000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1706] _id=6abaabf7485cab4c956f6745 ts=2026-09-28T18:03:35.9260000Z; 24h 25m: 6aa4144c41b41dbac0c7f271.jsonl[663] _id=6ab561a9485cab4c95538bc1 ts=2026-09-24T17:45:13.7930000Z -> 6aa4144c41b41dbac0c7f271.jsonl[972] _id=6ab6b90a485cab4c955db66f ts=2026-09-25T18:10:18.8030000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 121h 49m 
  - Evidence: 121h 49m: 6aa4144c41b41dbac0c7f271.jsonl[5657] _id=6abd50fe485cab4c9590f47b ts=2026-09-30T18:12:14.1820000Z -> 6aa4144c41b41dbac0c7f271.jsonl[10567] _id=6ac40217de269131f9af8a65 ts=2026-10-05T20:01:26.5020000Z; 119h 52m: 6aa4144c41b41dbac0c7f271.jsonl[1111] _id=6ab6bb3e485cab4c955e029f ts=2026-09-25T18:19:42.4760000Z -> 6aa4144c41b41dbac0c7f271.jsonl[5648] _id=6abd50f3485cab4c9590f3a5 ts=2026-09-30T18:12:03.7100000Z; 24h 33m: 6aa4144c41b41dbac0c7f271.jsonl[699] _id=6ab561dc485cab4c9553903d ts=2026-09-24T17:46:04.4720000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1108] _id=6ab6bb3d485cab4c955e0265 ts=2026-09-25T18:19:41.2120000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4144c41b41dbac0c7f271.jsonl[7919] _id=6abe78c7485cab4c95a9f53a ts=2026-10-01T15:14:15.1330000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7985] _id=6ac3b761de269131f9ac6608 ts=2026-10-05T14:42:41.7230000Z; 71h 22m: 6aa4144c41b41dbac0c7f271.jsonl[1624] _id=6ab6c055485cab4c955e6596 ts=2026-09-25T18:41:25.7920000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1754] _id=6abaac25485cab4c956f6831 ts=2026-09-28T18:04:21.1390000Z; 23h 58m: 6aa4144c41b41dbac0c7f271.jsonl[1727] _id=6abaabf4485cab4c956f6721 ts=2026-09-24T18:12:27.024Z -> 6aa4144c41b41dbac0c7f271.jsonl[991] _id=6ab6b945485cab4c955dbb99 ts=2026-09-25T18:11:18.4090000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 480 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f271.jsonl[13092] _id=6ac65ca1de269131f9bb2f42 ts=2026-10-07T14:52:17.0850000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13093] _id=6ac65ca1de269131f9bb2f43 ts=2026-10-07T14:52:17.0850000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[13114] _id=6ac65cc0de269131f9bb31d7 ts=2026-10-07T14:52:48.4950000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13115] _id=6ac65cc0de269131f9bb31d8 ts=2026-10-07T14:52:48.4950000Z; 1ms: 6aa4144c41b41dbac0c7f271.jsonl[13045] _id=6ac65c70de269131f9bb2a80 ts=2026-10-07T14:51:28.0770000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13046] _id=6ac65c70de269131f9bb2a81 ts=2026-10-07T14:51:28.0780000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 288h 10m 
  - Evidence: 288h 10m: 6aa4144c41b41dbac0c7f271.jsonl[1534] _id=6ab6becb485cab4c955e4e6f ts=2026-09-25T18:34:51.8710000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13876] _id=6ac69341de269131f9bdfee4 ts=2026-10-07T18:45:21.1320000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4144c41b41dbac0c7f271.jsonl[7944] _id=6abe7907485cab4c95a9fdc6 ts=2026-10-01T15:15:19.0910000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7961] _id=6ac3b708de269131f9ac50c4 ts=2026-10-05T14:41:12.1580000Z; 71h 21m: 6aa4144c41b41dbac0c7f271.jsonl[1631] _id=6ab6c067485cab4c955e6615 ts=2026-09-25T18:41:43.8630000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1734] _id=6abaabff485cab4c956f6753 ts=2026-09-28T18:03:42.6190000Z; 23h 57m: 6aa4144c41b41dbac0c7f271.jsonl[1704] _id=6abaabf5485cab4c956f6737 ts=2026-09-24T18:13:42.9Z -> 6aa4144c41b41dbac0c7f271.jsonl[983] _id=6ab6b926485cab4c955db995 ts=2026-09-25T18:10:46.5580000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 145 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f271.jsonl[12566] _id=6ac5507bde269131f9b7b8b0 ts=2026-10-06T19:48:09.0350000Z -> 6aa4144c41b41dbac0c7f271.jsonl[12567] _id=6ac5507bde269131f9b7b8b1 ts=2026-10-06T19:48:09.0350000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[12567] _id=6ac5507bde269131f9b7b8b1 ts=2026-10-06T19:48:09.0350000Z -> 6aa4144c41b41dbac0c7f271.jsonl[12568] _id=6ac5507bde269131f9b7b8b2 ts=2026-10-06T19:48:09.0350000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[12570] _id=6ac5507bde269131f9b7b8b5 ts=2026-10-06T19:48:09.4100000Z -> 6aa4144c41b41dbac0c7f271.jsonl[12571] _id=6ac5507bde269131f9b7b8b6 ts=2026-10-06T19:48:09.4100000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa4144c41b41dbac0c7f271.jsonl[7886] _id=6abe77f5485cab4c95a9dcba ts=2026-10-01T15:10:45.5170000Z -> 6aa4144c41b41dbac0c7f271.jsonl[8087] _id=6ac3b83cde269131f9ac8960 ts=2026-10-05T14:46:20.8650000Z; 71h 25m: 6aa4144c41b41dbac0c7f271.jsonl[1606] _id=6ab6c025485cab4c955e6401 ts=2026-09-25T18:40:37.4240000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1772] _id=6abaac73485cab4c956f6de5 ts=2026-09-28T18:05:39.7490000Z; 47h 59m: 6aa4144c41b41dbac0c7f271.jsonl[4364] _id=6abab09a485cab4c956fef17 ts=2026-09-28T18:23:22.1870000Z -> 6aa4144c41b41dbac0c7f271.jsonl[5910] _id=6abd5384485cab4c95914d35 ts=2026-09-30T18:23:00.2560000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f271.jsonl[12415] _id=6ac541b5de269131f9b6d20b ts=2026-10-06T18:45:09.5920000Z -> 6aa4144c41b41dbac0c7f271.jsonl[12411] _id=6ac541b5de269131f9b6d211 ts=2026-10-06T18:45:09.5920000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[12680] _id=6ac55264de269131f9b7d74f ts=2026-10-06T19:56:18.7510000Z -> 6aa4144c41b41dbac0c7f271.jsonl[12681] _id=6ac55264de269131f9b7d750 ts=2026-10-06T19:56:18.7510000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[12859] _id=6ac659f8de269131f9bafeab ts=2026-10-07T14:40:55.9030000Z -> 6aa4144c41b41dbac0c7f271.jsonl[12860] _id=6ac659f8de269131f9bafeac ts=2026-10-07T14:40:55.9030000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4144c41b41dbac0c7f271.jsonl[7947] _id=6abe7931485cab4c95aa057a ts=2026-10-01T15:16:01.1110000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7952] _id=6ac3b6e7de269131f9ac48db ts=2026-10-05T14:40:33.8270000Z; 71h 21m: 6aa4144c41b41dbac0c7f271.jsonl[1634] _id=6ab6c068485cab4c955e661b ts=2026-09-25T18:41:44.7690000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1707] _id=6abaabff485cab4c956f6751 ts=2026-09-28T18:03:35.9330000Z; 23h 56m: 6aa4144c41b41dbac0c7f271.jsonl[1721] _id=6abaabf5485cab4c956f673d ts=2026-09-24T18:13:55.126Z -> 6aa4144c41b41dbac0c7f271.jsonl[974] _id=6ab6b910485cab4c955db6c9 ts=2026-09-25T18:10:18.8080000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 99h 35m 
  - Evidence: 99h 35m: 6aa4144c41b41dbac0c7f271.jsonl[7619] _id=6abe7372485cab4c95a9703e ts=2026-10-01T14:51:29.8190000Z -> 6aa4144c41b41dbac0c7f271.jsonl[9172] _id=6ac3ebecde269131f9aeff57 ts=2026-10-05T18:26:51.8470000Z; 71h 25m: 6aa4144c41b41dbac0c7f271.jsonl[1630] _id=6ab6c067485cab4c955e6611 ts=2026-09-25T18:41:43.2990000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1990] _id=6abaad72485cab4c956f84b3 ts=2026-09-28T18:07:15.4120000Z; 48h 0m: 6aa4144c41b41dbac0c7f271.jsonl[4387] _id=6abab09b485cab4c956fef51 ts=2026-09-28T18:23:22.2260000Z -> 6aa4144c41b41dbac0c7f271.jsonl[5994] _id=6abd53d3485cab4c95915d59 ts=2026-09-30T18:24:18.3930000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2684 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f271.jsonl[10002] _id=6ac3ed08de269131f9af17e3 ts=2026-10-05T18:31:35.6490000Z -> 6aa4144c41b41dbac0c7f271.jsonl[9994] _id=6ac3ed08de269131f9af17e9 ts=2026-10-05T18:31:35.6490000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[10004] _id=6ac3ed08de269131f9af17f9 ts=2026-10-05T18:31:35.7590000Z -> 6aa4144c41b41dbac0c7f271.jsonl[9995] _id=6ac3ed08de269131f9af17ff ts=2026-10-05T18:31:35.7590000Z; 0ms: 6aa4144c41b41dbac0c7f271.jsonl[10005] _id=6ac3ed08de269131f9af1801 ts=2026-10-05T18:31:35.8030000Z -> 6aa4144c41b41dbac0c7f271.jsonl[9996] _id=6ac3ed08de269131f9af1804 ts=2026-10-05T18:31:35.8030000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6aa4144c41b41dbac0c7f271.jsonl[5940] _id=6abd539f485cab4c9591526f ts=2026-09-30T18:23:27.3700000Z -> 6aa4144c41b41dbac0c7f271.jsonl[9123] _id=6ac3eb89de269131f9aef82b ts=2026-10-05T18:25:12.9860000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 3h 27m 
  - Evidence: 3h 27m: 6aa4144c41b41dbac0c7f271.jsonl[13385] _id=6ac65f65de269131f9bb70b7 ts=2026-10-07T15:04:05.0260000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13620] _id=6ac68ff4de269131f9bdbea6 ts=2026-10-07T18:31:16.8390000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 100h 54m 
  - Evidence: 100h 54m: 6aa4144c41b41dbac0c7f271.jsonl[7823] _id=6abe770c485cab4c95a9ae16 ts=2026-10-01T15:06:52.6830000Z -> 6aa4144c41b41dbac0c7f271.jsonl[10573] _id=6ac4021ade269131f9af8a7f ts=2026-10-05T20:01:29.8750000Z; 23h 34m: 6aa4144c41b41dbac0c7f271.jsonl[4784] _id=6abab57b485cab4c957052bf ts=2026-09-28T18:44:11.8960000Z -> 6aa4144c41b41dbac0c7f271.jsonl[4892] _id=6abc00f4485cab4c958449f0 ts=2026-09-29T18:18:28.3720000Z; 23h 24m: 6aa4144c41b41dbac0c7f271.jsonl[5389] _id=6abc07d8485cab4c9584c785 ts=2026-09-29T18:47:52.6660000Z -> 6aa4144c41b41dbac0c7f271.jsonl[5642] _id=6abd50ed485cab4c9590f2b5 ts=2026-09-30T18:11:57.3270000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 236h 39m 
  - Evidence: 236h 39m: 6aa4144c41b41dbac0c7f271.jsonl[1431] _id=6ab6be0f485cab4c955e47b3 ts=2026-09-25T18:31:43.8770000Z -> 6aa4144c41b41dbac0c7f271.jsonl[8756] _id=6ac3be2fde269131f9acdb5d ts=2026-10-05T15:11:43.2430000Z; 47h 37m: 6aa4144c41b41dbac0c7f271.jsonl[8890] _id=6ac3bed2de269131f9ace35f ts=2026-10-05T15:14:26.1090000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13044] _id=6ac65c70de269131f9bb2a7e ts=2026-10-07T14:51:28.0370000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 236h 39m 
  - Evidence: 236h 39m: 6aa4144c41b41dbac0c7f271.jsonl[1434] _id=6ab6be0f485cab4c955e47b5 ts=2026-09-25T18:31:43.8950000Z -> 6aa4144c41b41dbac0c7f271.jsonl[8725] _id=6ac3be1fde269131f9acdacb ts=2026-10-05T15:11:27.6990000Z; 47h 36m: 6aa4144c41b41dbac0c7f271.jsonl[8902] _id=6ac3bed2de269131f9ace36b ts=2026-10-05T15:14:26.1780000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13024] _id=6ac65c63de269131f9bb2996 ts=2026-10-07T14:51:15.7470000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.039s shown 
  - Evidence: 31ms: 6aa4144c41b41dbac0c7f271.jsonl[13199] _id=6ac65d2ade269131f9bb3919 ts=2026-10-07T14:54:34.1280000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13202] _id=6ac65d2ade269131f9bb391c ts=2026-10-07T14:54:34.1590000Z; 39ms: 6aa4144c41b41dbac0c7f271.jsonl[8891] _id=6ac3bed2de269131f9ace362 ts=2026-10-05T15:14:26.1390000Z -> 6aa4144c41b41dbac0c7f271.jsonl[8902] _id=6ac3bed2de269131f9ace36b ts=2026-10-05T15:14:26.1780000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 236h 39m 
  - Evidence: 236h 39m: 6aa4144c41b41dbac0c7f271.jsonl[1423] _id=6ab6be0a485cab4c955e478d ts=2026-09-25T18:31:38.0570000Z -> 6aa4144c41b41dbac0c7f271.jsonl[8723] _id=6ac3be05de269131f9acd9bc ts=2026-10-05T15:11:01.4310000Z; 47h 36m: 6aa4144c41b41dbac0c7f271.jsonl[8889] _id=6ac3bed0de269131f9ace357 ts=2026-10-05T15:14:24.6870000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13029] _id=6ac65c67de269131f9bb29ef ts=2026-10-07T14:51:19.6560000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 66 interval(s) ≤ 0.006s..0.022s shown 
  - Evidence: 6ms: 6aa4144c41b41dbac0c7f271.jsonl[1358] _id=6ab6bdc8485cab4c955e451d ts=2026-09-25T18:30:32.5350000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1351] _id=6ab6bdc8485cab4c955e4521 ts=2026-09-25T18:30:32.5410000Z; 17ms: 6aa4144c41b41dbac0c7f271.jsonl[1371] _id=6ab6bdd2485cab4c955e4575 ts=2026-09-25T18:30:42.2290000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1379] _id=6ab6bdd2485cab4c955e4577 ts=2026-09-25T18:30:42.2460000Z; 22ms: 6aa4144c41b41dbac0c7f271.jsonl[1382] _id=6ab6bdd4485cab4c955e458d ts=2026-09-25T18:30:44.3130000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1384] _id=6ab6bdd4485cab4c955e458f ts=2026-09-25T18:30:44.3350000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 168h 33m 
  - Evidence: 168h 33m: 6aa4144c41b41dbac0c7f271.jsonl[5655] _id=6abd50fa485cab4c9590f43f ts=2026-09-30T18:12:10.9280000Z -> 6aa4144c41b41dbac0c7f271.jsonl[13881] _id=6ac69364de269131f9be0360 ts=2026-10-07T18:45:56.1190000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 6aa4144c41b41dbac0c7f271.jsonl[7658] _id=6abe746e485cab4c95a97c22 ts=2026-10-01T14:55:42.2500000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7956] _id=6ac3b6d5de269131f9ac453a ts=2026-10-05T14:40:20.9000000Z; 71h 27m: 6aa4144c41b41dbac0c7f271.jsonl[1537] _id=6ab6bf21485cab4c955e5299 ts=2026-09-25T18:36:17.1410000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1705] _id=6abaabf5485cab4c956f6743 ts=2026-09-28T18:03:25.4200000Z; 24h 25m: 6aa4144c41b41dbac0c7f271.jsonl[658] _id=6ab5619e485cab4c95538aaf ts=2026-09-24T17:45:01.6700000Z -> 6aa4144c41b41dbac0c7f271.jsonl[970] _id=6ab6b8fe485cab4c955db555 ts=2026-09-25T18:10:06.2470000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 6aa4144c41b41dbac0c7f271.jsonl[7657] _id=6abe746e485cab4c95a97c1e ts=2026-10-01T14:55:42.2490000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7955] _id=6ac3b6d4de269131f9ac4534 ts=2026-10-05T14:40:20.8990000Z; 71h 27m: 6aa4144c41b41dbac0c7f271.jsonl[1536] _id=6ab6bf21485cab4c955e5297 ts=2026-09-25T18:36:17.1400000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1722] _id=6abaabf5485cab4c956f6741 ts=2026-09-28T18:03:25.4090000Z; 24h 3m: 6aa4144c41b41dbac0c7f271.jsonl[1646] _id=6abaabec485cab4c956f6689 ts=2026-09-24T18:06:26.057Z -> 6aa4144c41b41dbac0c7f271.jsonl[971] _id=6ab6b8fd485cab4c955db54f ts=2026-09-25T18:10:06.2460000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 116h 56m 
  - Evidence: 116h 56m: 6aa4144c41b41dbac0c7f271.jsonl[5451] _id=6abd4f62485cab4c9590d943 ts=2026-09-30T18:05:23.0100000Z -> 6aa4144c41b41dbac0c7f271.jsonl[8592] _id=6ac3bbedde269131f9acc61f ts=2026-10-05T15:02:05.1910000Z; 71h 53m: 6aa4144c41b41dbac0c7f271.jsonl[976] _id=6ab6b911485cab4c955db6cd ts=2026-09-25T18:10:24.5060000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1746] _id=6abaac08485cab4c956f6769 ts=2026-09-28T18:03:52.6260000Z; 24h 4m: 6aa4144c41b41dbac0c7f271.jsonl[969] _id=6ab566a0485cab4c9554096e ts=2026-09-24T18:06:24.4110000Z -> 6aa4144c41b41dbac0c7f271.jsonl[976] _id=6ab6b911485cab4c955db6cd ts=2026-09-25T18:10:24.5060000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 24 gap(s), longest 95h 39m 
  - Evidence: 95h 39m: 6aa4144c41b41dbac0c7f271.jsonl[7724] _id=6abe75a8485cab4c95a98984 ts=2026-10-01T15:00:56.9610000Z -> 6aa4144c41b41dbac0c7f271.jsonl[7953] _id=6ac3b6e7de269131f9ac48e7 ts=2026-10-05T14:40:39.1330000Z; 71h 25m: 6aa4144c41b41dbac0c7f271.jsonl[1560] _id=6ab6bf96485cab4c955e5963 ts=2026-09-25T18:38:14.9550000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1736] _id=6abaabff485cab4c956f675b ts=2026-09-28T18:03:42.6430000Z; 24h 12m: 6aa4144c41b41dbac0c7f271.jsonl[869] _id=6ab564bf485cab4c9553cb6e ts=2026-09-24T17:58:22.9580000Z -> 6aa4144c41b41dbac0c7f271.jsonl[975] _id=6ab6b911485cab4c955db6cf ts=2026-09-25T18:10:25.0640000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 6aa4144c41b41dbac0c7f271.jsonl[1319] _id=6ab6bd3e485cab4c955e3f3f ts=2026-09-25T18:28:14.2690000Z -> 6aa4144c41b41dbac0c7f271.jsonl[1310] _id=6ab6bd3e485cab4c955e3f43 ts=2026-09-25T18:28:14.2710000Z; 3ms: 6aa4144c41b41dbac0c7f271.jsonl[5444] _id=6abd4f60485cab4c9590d937 ts=2026-09-30T18:05:20.4280000Z -> 6aa4144c41b41dbac0c7f271.jsonl[5450] _id=6abd4f60485cab4c9590d93b ts=2026-09-30T18:05:20.4310000Z; 4ms: 6aa4144c41b41dbac0c7f271.jsonl[11771] _id=6ac53e03de269131f9b66e25 ts=2026-10-06T18:29:23.3820000Z -> 6aa4144c41b41dbac0c7f271.jsonl[11772] _id=6ac53e03de269131f9b66e29 ts=2026-10-06T18:29:23.3860000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1108] _id=6ab6bb3d485cab4c955e0265 ts=2026-09-25T18:19:41.2120000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1105] _id=6ab6bb3d485cab4c955e0269 ts=2026-09-25T18:19:41.3250000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1648] _id=6abaabed485cab4c956f6691 ts=2026-09-24T18:07:36.777Z`; `6aa4144c41b41dbac0c7f271.jsonl[1660] _id=6abaabf0485cab4c956f66b9 ts=2026-09-24T18:09:04.509Z`; `6aa4144c41b41dbac0c7f271.jsonl[1285] _id=6ab6bd27485cab4c955e3b54 ts=2026-09-25T18:27:52.0090000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 138 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[2110] _id=6abaad7b485cab4c956f864f ts=2026-09-28T18:09:42.2600000Z`; `6aa4144c41b41dbac0c7f271.jsonl[2111] _id=6abaad7c485cab4c956f8653 ts=2026-09-28T18:09:42.2670000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1977] _id=6abaad7c485cab4c956f8655 ts=2026-09-28T18:09:42.2720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 261 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1870] _id=6abaacd8485cab4c956f73b7 ts=2026-09-28T18:07:19.4350000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1883] _id=6abaacd8485cab4c956f73b9 ts=2026-09-28T18:07:19.4510000Z`; `6aa4144c41b41dbac0c7f271.jsonl[2018] _id=6abaad73485cab4c956f84d7 ts=2026-09-28T18:07:42.9650000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[8902] _id=6ac3bed2de269131f9ace36b ts=2026-10-05T15:14:26.1780000Z`; `6aa4144c41b41dbac0c7f271.jsonl[13202] _id=6ac65d2ade269131f9bb391c ts=2026-10-07T14:54:34.1590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1351] _id=6ab6bdc8485cab4c955e4521 ts=2026-09-25T18:30:32.5410000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1359] _id=6ab6bdc8485cab4c955e4527 ts=2026-09-25T18:30:32.5850000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1379] _id=6ab6bdd2485cab4c955e4577 ts=2026-09-25T18:30:42.2460000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[13881] _id=6ac69364de269131f9be0360 ts=2026-10-07T18:45:56.1190000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[11447] _id=6ac53c7dde269131f9b654cd ts=2026-10-06T18:22:53.4100000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 8 records 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[22] _id=6ab41775485cab4c954f37b2 ts=?`; `6aa4144c41b41dbac0c7f271.jsonl[973] _id=6ab6b910485cab4c955db6c3 ts=?`; `6aa4144c41b41dbac0c7f271.jsonl[1723] _id=6abaabfe485cab4c956f674f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 409 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[2357] _id=6abaadcf485cab4c956f938f ts=2026-09-28T18:11:24.9820000Z`; `6aa4144c41b41dbac0c7f271.jsonl[2392] _id=6abaadd6485cab4c956f9518 ts=2026-09-28T18:11:32.3870000Z`; `6aa4144c41b41dbac0c7f271.jsonl[2403] _id=6abaadd7485cab4c956f956b ts=2026-09-28T18:11:34.7950000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 968 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1867] _id=6abaacd6485cab4c956f738d ts=2026-09-28T18:07:17.9920000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1878] _id=6abaacd7485cab4c956f7393 ts=2026-09-28T18:07:17.9920000Z`; `6aa4144c41b41dbac0c7f271.jsonl[2038] _id=6abaad74485cab4c956f84f7 ts=2026-09-28T18:07:53.6050000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1425] _id=6ab6be0c485cab4c955e479b ts=2026-09-25T18:31:40.7490000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'DialogueStartEvent' (totals: 322 start, 309 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 85 unmatched 'BecameCameraCentered' (totals: 644 open, 697 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 127 unmatched 'BecameVisible' (totals: 1452 open, 1586 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 3 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 30 unmatched 'questActiveEvent' (totals: 61 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 283 of 13908 adjacent _id pairs reverse in client time; worst 88518.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f271.jsonl[1634] _id=6ab6c068485cab4c955e661b ts=2026-09-25T18:41:44.7690000Z`; `6aa4144c41b41dbac0c7f271.jsonl[1646] _id=6abaabec485cab4c956f6689 ts=2026-09-24T18:06:26.057Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -345418.74s, max +2.11s over 13909 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f271\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
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
  - Observed: 8 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4379 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3421); Unit 4 Dev (940); Unit 5 Dev - Dungeon (18)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.51s, n=4378)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4379/4379 records)
    "BecameInvisible"  x1586
    "BecameVisible"  x1452
    "BecameCameraUncentered"  x697
    "BecameCameraCentered"  x644
data.pieceId  (string, 4379/4379 records)
    35 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4379/4379 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4169 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1248); Unit 4 Dev - Dungeon (1088); Unit 3 Dev (608); Unit 1 Dev (588); Unit 4 Dev - Anderson Base (348); Unit 4 Dev (289)
- **Intervals:** median 1.20s (p5 0.10s / p95 19.74s, n=4168)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4169/4169 records)
    "pressed"  x4169
data.actionType  (string, 4169/4169 records)
    "Move"  x3098
    "Interact"  x458
    "Jump"  x286
    "Sprint"  x191
    "Ascend"  x42
    "Hoverboard"  x39
    "Map"  x31
    "Pause"  x17
    "ToggleDebug"  x5
    "SkipCinematic"  x2
data.key  (string, 4169/4169 records, 21 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4169/4169 records)
    "Player"  x3349
    "Drone"  x820
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2505 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (705); Unit 1 Dev (491); Unit 3 Dev (382); Unit 4 Dev (347); Unit 4 Dev - Dungeon (346); Unit 4 Dev - Anderson Base (225); Unit 5 Dev - Dungeon (9)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.18s, n=2496)
- **Fields under `data`:**

```text
data.position  (object, 2505/2505 records)
data.position.x  (number, 2505/2505 records)
    numeric range -106.831 .. 1624.8 (810 unique)
data.position.y  (number, 2505/2505 records)
    numeric range -115.03 .. 179.379 (575 unique)
data.position.z  (number, 2505/2505 records)
    numeric range -723.587 .. 2079.28 (808 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1790 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (441); Unit 4 Dev (391); Unit 1 Dev (359); Unit 3 Dev (216); Unit 4 Dev - Dungeon (213); Unit 4 Dev - Anderson Base (163); Unit 5 Dev - Dungeon (7)
- **eventKey:** present on 1159 of 1790 records
- **Intervals:** median 5.44s (p5 0.01s / p95 62.73s, n=1789)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1159; [conversationId, dialogueEventType] x631
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1790/1790 records)
    numeric range 10 .. 114 (38 unique)
data.dialogueEventType  (string, 1790/1790 records)
    "DialogueNodeEvent"  x1159
    "DialogueStartEvent"  x322
    "DialogueFinishEvent"  x309
data.nodeId  (number, 1159/1790 records)
    numeric range 0 .. 289 (161 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 339 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (140); Unit 2 Prod (Refactor) (91); Unit 1 Dev (42); Unit 4 Dev (37); Unit 4 Dev - Anderson Base (24); Unit 3 Dev (5)
- **Intervals:** median 10.89s (p5 0.20s / p95 421.69s, n=338)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 339/339 records)
    34 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 339/339 records)
    80 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 296 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (119); Unit 3 Dev (113); Unit 1 Dev (64)
- **Intervals:** median 0.31s (p5 0.03s / p95 10.74s, n=295)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 296/296 records)
    "argumentationNodeHoverEnd"  x131
    "argumentationNodeHoverStart"  x124
    "argumentationNodeAdd"  x26
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 296/296 records)
    "Unit 4 - Flooding"  x119
    "Unit 3 - Pollution Upstream"  x113
    "Unit 1 - Argumentation Tutorial"  x35
    "Unit 1 - Freshwater"  x29
data.nodeName  (string, 296/296 records)
    "B"  x48
    "3"  x40
    "1"  x38
    "A"  x38
    "II"  x35
    "I"  x23
    "4"  x22
    "2"  x21
    "D"  x15
    "5"  x11
    "C"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 93 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 1 Dev (22); Unit 4 Dev - Dungeon (22); Unit 4 Dev (12); Unit 3 Dev (8); Unit 4 Dev - Anderson Base (4); Unit 5 Dev - Dungeon (1)
- **eventKey:** present on 93 of 93 records
- **Intervals:** median 231.34s (p5 0.01s / p95 83796.25s, n=92)
- **`data` key-set variants:** [questEventType, questID, questName] x61; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 93/93 records)
    "questActiveEvent"  x61
    "questFinishEvent"  x32
data.questID  (string, 93/93 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 93/93 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/93 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 76 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (63); Unit 3 Dev (11); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 11.53s (p5 0.90s / p95 22925.00s, n=75)
- **`data` key-set variants:** [actionType, featureUsed] x56; [actionType, featureUsed, location] x18; [actionType, featureUsed, legendName] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapCloseEvent"  x28
    "MapOpenEvent"  x28
    "WaypointMoveEvent"  x13
    "WaypointSetEvent"  x5
    "Selected"  x2
data.featureUsed  (string, 76/76 records)
    "Map"  x56
    "Waypoint"  x18
    "Legend"  x2
data.legendName  (string, 2/76 records)
    "240 ft"  x1
    "90 ft"  x1
data.location  (object, 18/76 records)
data.location.x  (number, 18/76 records)
    numeric range -256.804 .. 550.212 (16 unique)
data.location.y  (number, 18/76 records)
    numeric range -107.5 .. 156.5 (17 unique)
data.location.z  (number, 18/76 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 48 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (25); Unit 1 Dev (7); Unit 2 Prod (Refactor) (6); Unit 4 Dev - Dungeon (4); Unit 3 Dev (2); Unit 4 Dev (2); Transition (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 871.85s (p5 6.67s / p95 86013.17s, n=47)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 48/48 records)
    true  x48
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 42 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (32); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 1.00s (p5 0.25s / p95 11.94s, n=41)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x38; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/42 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/42 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 38/42 records)
    "RightDrag"  x21
    "LeftDrag"  x17
data.currentSoilType  (string, 38/42 records)
    "SAND"  x9
    "CLAYSAND"  x7
    "SANDGRAVEL"  x7
    "CLAY"  x6
    "CLAYROCK"  x5
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 38/42 records)
    "false"  x29
    "true"  x9
data.waterLevelStatus  (string, 38/42 records)
    "TooLow"  x17
    "TooHigh"  x11
    "Proper"  x10
data.waterRetentionChange  (string, 38/42 records)
    "Decrease"  x15
    "Increase"  x14
    "NoChange"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 34 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 4 Dev - Dungeon (6); MainMenu (5); Unit 4 Dev (5); Unit 3 Dev (4); Unit 1 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1565.11s (p5 9.26s / p95 155635.81s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "DebugMenuStateChanged"  x34
data.isOpened  (bool, 34/34 records)
    false  x34
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 25 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (25)
- **Intervals:** median 5972.26s (p5 344.33s / p95 231829.72s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 25 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (6); Unit 2 Prod (Refactor) (6); Unit 4 Dev - Dungeon (6); Unit 3 Dev (2); Unit 4 Dev (2); Unit 4 Dev - Anderson Base (2); Transition (1)
- **Intervals:** median 2001.39s (p5 14.03s / p95 232982.92s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationAnswerEvent` — 23 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 1 Dev (3)
- **Intervals:** median 16.12s (p5 2.41s / p95 162854.25s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "submitAnswerEvent"  x23
data.answerSubmitted  (string, 23/23 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 23/23 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 4 - Flooding"  x9
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 33.25s (p5 1.94s / p95 275.57s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x6
    "Bedrock"  x5
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 16/16 records)
    "5"  x11
    "4"  x3
    "3"  x2
data.machine  (string, 16/16 records)
    "1"  x15
    "2"  x1
data.row  (string, 16/16 records)
    "TopRow"  x10
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 5.29s (p5 0.59s / p95 4388.53s, n=14)
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records, 9 empty-string)
    ""  x9
    "cameraPlaced"  x6
data.boxId  (string, 15/15 records)
    "0"  x7
    "1"  x4
    "2"  x4
data.soilType  (string, 15/15 records)
    "Clay"  x8
    "Sand"  x5
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 14 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 4.99s (p5 0.38s / p95 434345.67s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "Close"  x8
    "Open"  x6
data.toolName  (string, 14/14 records, 14 empty-string)
    ""  x14
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 37.37s (p5 0.03s / p95 579754.11s, n=9)
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

### `crash` — 8 records

- **Scenes:** <missing sceneName> (8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 8/8 records)
    true  x8
data.message  (string, 8/8 records)
    "A user gesture is required to request Pointer Lock."  x5
    "Permissions check failed"  x2
    "The root document of this element is not valid for pointer lock."  x1
data.phase  (string, 8/8 records)
    "running"  x8
data.stack  (string, 8/8 records, 6 empty-string)
    ""  x6
    "TypeError: Permissions check failed"  x2
data.type  (string, 8/8 records)
    "unhandled_rejection"  x8
data.unitId  (string, 8/8 records)
    "unit2"  x3
    "unit1"  x2
    "unit4"  x2
    "unit3"  x1
data.workspace  (string, 8/8 records)
    "mhs"  x8
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5)
- **Intervals:** median 1.70s (p5 0.72s / p95 53.96s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 303415.04s (p5 30345.91s / p95 576484.18s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x2
    "Open"  x1
data.chatID  (string, 3/3 records)
    "NA"  x2
    "[18-287, 18-289]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 1037429.26s (p5 1037429.26s / p95 1037429.26s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `WaterChamberEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (10 records)
- `TerasGardenBox` data.actionType: "" (9x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (13x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (18x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*