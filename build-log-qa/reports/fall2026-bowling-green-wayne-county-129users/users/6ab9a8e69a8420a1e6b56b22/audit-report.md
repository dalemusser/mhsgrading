# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b22

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b22
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b22.jsonl
- **Records:** 10438 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b22
- **Time span:** 2026-10-05T16:31:52.959000+00:00 .. 2026-10-19T16:11:13.162000+00:00 (335h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b22\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 10438 records, 9 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 97 INFO, 2 NOT_TESTED, 85 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2709 | 25.95 | 1 | 7 | 0 | 2026-10-05T16:32:07.959000+00:00 | 2026-10-19T16:09:49.838000+00:00 | 335h 37m |
| PuzzlePieceVisibleEvent | 2558 | 24.51 | 1 | 3 | 0 | 2026-10-06T16:56:40.714000+00:00 | 2026-10-16T16:53:16.230000+00:00 | 239h 56m |
| DialogueEvent | 2142 | 20.52 | 1 | 7 | 1344 | 2026-10-05T16:32:24.562000+00:00 | 2026-10-19T16:11:09.139000+00:00 | 335h 38m |
| PlayerPositionEvent | 1828 | 17.51 | 1 | 7 | 0 | 2026-10-05T16:32:04.147000+00:00 | 2026-10-19T16:11:13.162000+00:00 | 335h 39m |
| argumentationNodeEvent | 395 | 3.78 | 1 | 4 | 0 | 2026-10-05T16:53:58.111000+00:00 | 2026-10-16T21:06:52.387000+00:00 | 268h 12m |
| ObjectInterEvent | 286 | 2.74 | 1 | 7 | 0 | 2026-10-05T16:37:40.837000+00:00 | 2026-10-19T16:07:43.932000+00:00 | 335h 30m |
| Soil Key Puzzle | 105 | 1.01 | 1 | 3 | 0 | 2026-10-07T16:41:31.122000+00:00 | 2026-10-16T16:27:59.367000+00:00 | 215h 46m |
| TopographicMapEvent | 94 | 0.9 | 1 | 3 | 0 | 2026-10-06T16:57:02.716000+00:00 | 2026-10-16T21:40:53.092000+00:00 | 244h 43m |
| questEvent | 70 | 0.67 | 1 | 7 | 70 | 2026-10-05T16:32:24.538000+00:00 | 2026-10-19T16:09:37.084000+00:00 | 335h 37m |
| gameWindowFocusEvent | 44 | 0.42 | 1 | 7 | 0 | 2026-10-05T16:31:52.959000+00:00 | 2026-10-19T16:04:56.844000+00:00 | 335h 33m |
| DaniEvent | 41 | 0.39 | 1 | 3 | 0 | 2026-10-07T16:40:33.894000+00:00 | 2026-10-16T21:41:39.009000+00:00 | 221h 1m |
| DEBUGMenu | 35 | 0.34 | 1 | 8 | 0 | 2026-10-05T16:32:04.132000+00:00 | 2026-10-19T16:05:10.924000+00:00 | 335h 33m |
| gameWindowUnfocusEvent | 35 | 0.34 | 1 | 6 | 0 | 2026-10-05T16:53:31.290000+00:00 | 2026-10-16T21:37:28.433000+00:00 | 268h 43m |
| TerasGardenBox | 18 | 0.17 | 1 | 1 | 0 | 2026-10-16T21:11:50.216000+00:00 | 2026-10-19T16:07:07.237000+00:00 | 66h 55m |
| argumentationToolEvent | 18 | 0.17 | 1 | 3 | 0 | 2026-10-05T16:54:41.980000+00:00 | 2026-10-14T16:29:37.728000+00:00 | 215h 34m |
| gameStartEvent | 16 | 0.15 | 1 | 1 | 0 | 2026-10-05T16:31:52.960000+00:00 | 2026-10-19T16:04:56.844000+00:00 | 335h 33m |
| argumentationEvent | 13 | 0.12 | 1 | 4 | 0 | 2026-10-05T16:54:46.094000+00:00 | 2026-10-16T21:06:54.269000+00:00 | 268h 12m |
| soilMachine | 12 | 0.11 | 1 | 1 | 0 | 2026-10-16T16:41:34.621000+00:00 | 2026-10-16T16:49:37.021000+00:00 | 8m 2s |
| argumentationAnswerEvent | 11 | 0.11 | 1 | 4 | 0 | 2026-10-05T16:55:08.347000+00:00 | 2026-10-16T21:06:54.220000+00:00 | 268h 11m |
| chatEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-16T21:40:04.365000+00:00 | 2026-10-16T21:40:46.115000+00:00 | 41.8s |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-05T17:00:45.298000+00:00 | 2026-10-16T16:19:31.661000+00:00 | 263h 18m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 473963.182s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.373s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.058s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.72s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.304s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 263.908s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.082s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 7.802s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84682.572s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.632s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 41 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
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
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,C,2,II; B,5,I; C,2,II; D,2,II; D,A,C,2,II 
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
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [92-33, 92-61, 92-61, 92-61, 92-38, 92-64, 92-39]; [92-61, 92-61, 92-38, 92-64, 92-39] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[159] _id=6ac3d2d7de269131f9ade995 ts=2026-10-05T16:39:50.8670000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[187] _id=6ac3d3c5de269131f9adfa52 ts=2026-10-05T16:43:48.1860000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[253] _id=6ac3d44dde269131f9ae07e7 ts=2026-10-05T16:46:04.3830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[18] _id=6ac3d0f9de269131f9adc0e1 ts=2026-10-05T16:31:52.9600000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[633] _id=6ac3d81cde269131f9ae690b ts=2026-10-05T17:02:19.7830000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[656] _id=6ac527c4de269131f9b58e1d ts=2026-10-06T16:54:27.8710000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 44 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 44} 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[17] _id=6ac3d0f9de269131f9adc0db ts=2026-10-05T16:31:52.9590000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[396] _id=6ac3d60dde269131f9ae3087 ts=2026-10-05T16:53:32.1660000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[592] _id=6ac3d81cde269131f9ae6909 ts=2026-10-05T17:02:19.7820000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 35 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 35} 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[395] _id=6ac3d60cde269131f9ae3079 ts=2026-10-05T16:53:31.2900000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[654] _id=6ac527c4de269131f9b58df2 ts=2026-10-05T17:04:41.873Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[1468] _id=6ac67418de269131f9bc8bd1 ts=2026-10-06T17:04:26.477Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 17 of 94 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[721] _id=6ac5285fde269131f9b5b28c ts=2026-10-06T16:57:02.7160000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[726] _id=6ac52862de269131f9b5b329 ts=2026-10-06T16:57:05.8780000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[728] _id=6ac52865de269131f9b5b3a9 ts=2026-10-06T16:57:09.4250000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2708 | 0.0 | 1.373 | 446.182 | 24.217 | 429348.495 | 0.13 | 59 | 10 |
| PuzzlePieceVisibleEvent | 2557 | 0.0 | 0.058 | 337.816 | 1.835 | 518282.017 | 0.18 | 1217 | 7 |
| DialogueEvent | 2141 | 0.0 | 3.785 | 564.374 | 29.666 | 429387.737 | 0.11 | 593 | 9 |
| PlayerPositionEvent | 1818 | 9.7 | 10.003 | 664.468 | 10.382 | 429321.781 | 0.09 | 0 | 9 |
| argumentationNodeEvent | 394 | 0.004 | 0.75 | 2450.696 | 11.509 | 689798.118 | 0.02 | 37 | 4 |
| ObjectInterEvent | 285 | 0.0 | 11.552 | 4237.906 | 764.505 | 429939.218 | 0.01 | 5 | 15 |
| Soil Key Puzzle | 104 | 0.143 | 1.72 | 7469.118 | 27.445 | 518645.055 | 0.01 | 0 | 4 |
| TopographicMapEvent | 93 | 0.027 | 4.304 | 9473.445 | 44868.345 | 430657.643 | 0.01 | 2 | 8 |
| questEvent | 69 | 0.002 | 228.478 | 17510.617 | 85422.462 | 429424.107 | 0.0 | 9 | 17 |
| gameWindowFocusEvent | 43 | 2.076 | 105.518 | 28092.648 | 86212.575 | 429422.95 | 0.0 | 0 | 14 |
| DaniEvent | 40 | 0.007 | 2.466 | 19891.628 | 106412.801 | 429866.365 | 0.0 | 9 | 4 |
| DEBUGMenu | 34 | 8.049 | 866.564 | 35529.023 | 139944.335 | 429414.146 | 0.0 | 0 | 19 |
| gameWindowUnfocusEvent | 34 | 2.425 | 85.832 | 28454.034 | 118328.733 | 432058.254 | 0.0 | 0 | 9 |
| TerasGardenBox | 17 | 1.011 | 2.887 | 14171.589 | 48782.971 | 239455.821 | 0.0 | 0 | 2 |
| argumentationToolEvent | 17 | 0.072 | 4.082 | 45652.691 | 206797.703 | 689852.699 | 0.0 | 0 | 2 |
| gameStartEvent | 15 | 179.75 | 84682.572 | 80532.259 | 296626.93 | 429422.951 | 0.0 | 0 | 14 |
| argumentationEvent | 12 | 0.031 | 133.185 | 80460.681 | 406467.77 | 689778.628 | 0.0 | 1 | 4 |
| soilMachine | 11 | 0.906 | 4.632 | 43.855 | 145.312 | 168.192 | 1.37 | 0 | 0 |
| argumentationAnswerEvent | 10 | 3.674 | 263.908 | 96550.587 | 458084.433 | 689897.752 | 0.0 | 0 | 4 |
| chatEvent | 3 | 0.659 | 7.802 | 13.917 | 30.74 | 33.289 | 4.31 | 0 | 0 |
| EndOfUnit | 2 | 257926.617 | 473963.182 | 473963.182 | 668396.09 | 689999.746 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 15 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[1476] _id=6ac67428de269131f9bc8d14 ts=2026-10-07T16:32:38.7180000Z == 6ab9a8e69a8420a1e6b56b22.jsonl[1477] _id=6ac67428de269131f9bc8d15 ts=2026-10-07T16:32:38.7180000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[1482] _id=6ac67428de269131f9bc8d1a ts=2026-10-07T16:32:38.7190000Z == 6ab9a8e69a8420a1e6b56b22.jsonl[1483] _id=6ac67428de269131f9bc8d1b ts=2026-10-07T16:32:38.7190000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[5708] _id=6acfaee3de269131f9d58af7 ts=2026-10-14T16:33:38.3920000Z == 6ab9a8e69a8420a1e6b56b22.jsonl[5744] _id=6acfaee3de269131f9d58af8 ts=2026-10-14T16:33:38.3920000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 54 group(s), 86 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[745] _id=6ac52895de269131f9b5c02f ts=2026-10-06T16:57:56.4040000Z == 6ab9a8e69a8420a1e6b56b22.jsonl[754] _id=6ac52895de269131f9b5c035 ts=2026-10-06T16:57:56.4040000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[751] _id=6ac52895de269131f9b5c049 ts=2026-10-06T16:57:56.6210000Z == 6ab9a8e69a8420a1e6b56b22.jsonl[752] _id=6ac52895de269131f9b5c04d ts=2026-10-06T16:57:56.6210000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[764] _id=6ac52899de269131f9b5c11c ts=2026-10-06T16:58:00.1500000Z == 6ab9a8e69a8420a1e6b56b22.jsonl[738] _id=6ac5289ade269131f9b5c129 ts=2026-10-06T16:58:00.1500000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b22.jsonl[119] _id=6ac3d255de269131f9adde7d ts=2026-10-05T16:37:40.8370000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[116] _id=6ac3d255de269131f9adde83 ts=2026-10-05T16:37:40.8410000Z`; `174ms: 6ab9a8e69a8420a1e6b56b22.jsonl[357] _id=6ac3d5ecde269131f9ae2dc8 ts=2026-10-05T16:52:59.3560000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[358] _id=6ac3d5ecde269131f9ae2dd7 ts=2026-10-05T16:52:59.5300000Z`; `194ms: 6ab9a8e69a8420a1e6b56b22.jsonl[358] _id=6ac3d5ecde269131f9ae2dd7 ts=2026-10-05T16:52:59.5300000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[360] _id=6ac3d5edde269131f9ae2ddd ts=2026-10-05T16:52:59.7240000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 113 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `569ms: 6ab9a8e69a8420a1e6b56b22.jsonl[761] _id=6ac52897de269131f9b5c0b1 ts=2026-10-06T16:57:57.4870000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[743] _id=6ac52897de269131f9b5c0b3 ts=2026-10-06T16:57:58.0560000Z`; `17ms: 6ab9a8e69a8420a1e6b56b22.jsonl[743] _id=6ac52897de269131f9b5c0b3 ts=2026-10-06T16:57:58.0560000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[762] _id=6ac52898de269131f9b5c0bb ts=2026-10-06T16:57:58.0730000Z`; `15ms: 6ab9a8e69a8420a1e6b56b22.jsonl[829] _id=6ac528a8de269131f9b5c45b ts=2026-10-06T16:58:01.1050000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[822] _id=6ac528a8de269131f9b5c465 ts=2026-10-06T16:58:01.1200000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `68ms: 6ab9a8e69a8420a1e6b56b22.jsonl[5680] _id=6acfae5ade269131f9d581e5 ts=2026-10-14T16:31:22.3890000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[5683] _id=6acfae5ade269131f9d581e8 ts=2026-10-14T16:31:22.4570000Z`; `31ms: 6ab9a8e69a8420a1e6b56b22.jsonl[9669] _id=6ad291eede269131f9e8261a ts=2026-10-16T21:06:54.2380000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[9686] _id=6ad291eede269131f9e8261d ts=2026-10-16T21:06:54.2690000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `791ms: 6ab9a8e69a8420a1e6b56b22.jsonl[478] _id=6ac3d6b9de269131f9ae44f7 ts=2026-10-05T16:56:24.9820000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[482] _id=6ac3d6bade269131f9ae450e ts=2026-10-05T16:56:25.7730000Z`; `608ms: 6ab9a8e69a8420a1e6b56b22.jsonl[4567] _id=6ace5d7cde269131f9cf8065 ts=2026-10-13T16:34:04.3310000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[4570] _id=6ace5d7dde269131f9cf806d ts=2026-10-13T16:34:04.9390000Z`; `352ms: 6ab9a8e69a8420a1e6b56b22.jsonl[4635] _id=6ace5de3de269131f9cf87e5 ts=2026-10-13T16:35:47.0820000Z ~ 6ab9a8e69a8420a1e6b56b22.jsonl[4633] _id=6ace5de4de269131f9cf87f5 ts=2026-10-13T16:35:47.4340000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b22.jsonl[4208] _id=6ac7ccaade269131f9c4da7e ts=2026-10-08T17:02:33.4850000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4239] _id=6ace5a10de269131f9cf59d0 ts=2026-10-13T16:19:27.6310000Z; 66h 34m: 6ab9a8e69a8420a1e6b56b22.jsonl[10022] _id=6ad29757de269131f9e83187 ts=2026-10-16T21:29:59.6300000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10274] _id=6ad63fa9de269131f9e99a08 ts=2026-10-19T16:04:56.6750000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b22.jsonl[1472] _id=6ac67425de269131f9bc8cb7 ts=2026-10-07T16:32:35.9900000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[3175] _id=6ac7c4fcde269131f9c42afc ts=2026-10-08T16:29:47.3270000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 24m 
  - Evidence: 119h 24m: 6ab9a8e69a8420a1e6b56b22.jsonl[4230] _id=6ac7ccf0de269131f9c4de0c ts=2026-10-08T17:03:43.8720000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4425] _id=6ace5c1ade269131f9cf6f25 ts=2026-10-13T16:28:10.2370000Z; 48h 30m: 6ab9a8e69a8420a1e6b56b22.jsonl[4433] _id=6ace5c2bde269131f9cf6fd7 ts=2026-10-13T16:28:26.6880000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[7456] _id=6ad1063cde269131f9de23d7 ts=2026-10-15T16:58:35.3240000Z; 28h 33m: 6ab9a8e69a8420a1e6b56b22.jsonl[7572] _id=6ad10729de269131f9de3bf7 ts=2026-10-15T17:02:32.5200000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10165] _id=6ad298d0de269131f9e83547 ts=2026-10-16T21:36:16.0670000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.007s..0.008s shown 
  - Evidence: 7ms: 6ab9a8e69a8420a1e6b56b22.jsonl[4229] _id=6ac7cceede269131f9c4ddf0 ts=2026-10-08T17:03:42.1180000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4228] _id=6ac7cceede269131f9c4ddf2 ts=2026-10-08T17:03:42.1250000Z; 7ms: 6ab9a8e69a8420a1e6b56b22.jsonl[4431] _id=6ace5c29de269131f9cf6fb7 ts=2026-10-13T16:28:25.0640000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4432] _id=6ace5c29de269131f9cf6fb9 ts=2026-10-13T16:28:25.0710000Z; 8ms: 6ab9a8e69a8420a1e6b56b22.jsonl[4428] _id=6ace5c1ede269131f9cf6f66 ts=2026-10-13T16:28:13.6160000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4426] _id=6ace5c1ede269131f9cf6f69 ts=2026-10-13T16:28:13.6240000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b22.jsonl[4218] _id=6ac7ccd3de269131f9c4dca7 ts=2026-10-08T17:03:14.7290000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4244] _id=6ace5a20de269131f9cf5a49 ts=2026-10-13T16:19:42.4660000Z; 66h 28m: 6ab9a8e69a8420a1e6b56b22.jsonl[10138] _id=6ad298ebde269131f9e8356a ts=2026-10-16T21:36:43.3500000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10282] _id=6ad63fc5de269131f9e99ae9 ts=2026-10-19T16:05:23.9970000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b22.jsonl[649] _id=6ac3d888de269131f9ae7179 ts=2026-10-05T17:04:07.2470000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[669] _id=6ac527ecde269131f9b59797 ts=2026-10-06T16:55:08.6230000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 593 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[5668] _id=6acfae4fde269131f9d58155 ts=2026-10-14T16:31:11.1020000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5669] _id=6acfae4fde269131f9d58156 ts=2026-10-14T16:31:11.1020000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[9644] _id=6ad291d8de269131f9e82594 ts=2026-10-16T21:06:31.9570000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9645] _id=6ad291d8de269131f9e82595 ts=2026-10-16T21:06:31.9570000Z; 1ms: 6ab9a8e69a8420a1e6b56b22.jsonl[2746] _id=6ac67774de269131f9bd20dd ts=2026-10-07T16:46:43.3000000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[2747] _id=6ac67774de269131f9bd20de ts=2026-10-07T16:46:43.3010000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 39m 
  - Evidence: 191h 39m: 6ab9a8e69a8420a1e6b56b22.jsonl[630] _id=6ac3d7bede269131f9ae5f1a ts=2026-10-05T17:00:45.2980000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4728] _id=6ace5f0dde269131f9cfa08e ts=2026-10-13T16:40:45.0440000Z; 71h 38m: 6ab9a8e69a8420a1e6b56b22.jsonl[4728] _id=6ace5f0dde269131f9cfa08e ts=2026-10-13T16:40:45.0440000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[7681] _id=6ad24e93de269131f9e5b5c4 ts=2026-10-16T16:19:31.6610000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b22.jsonl[4233] _id=6ac7ccfade269131f9c4de86 ts=2026-10-08T17:03:53.9470000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4243] _id=6ace5a20de269131f9cf5a48 ts=2026-10-13T16:19:42.4420000Z; 66h 23m: 6ab9a8e69a8420a1e6b56b22.jsonl[10269] _id=6ad29a13de269131f9e837e8 ts=2026-10-16T21:41:39.1430000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10278] _id=6ad63fbade269131f9e99aa8 ts=2026-10-19T16:05:12.4830000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b22.jsonl[635] _id=6ac3d854de269131f9ae6d40 ts=2026-10-05T17:03:15.3780000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[658] _id=6ac527d3de269131f9b5919d ts=2026-10-06T16:54:40.9140000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 59 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[10279] _id=6ad63fbade269131f9e99aa9 ts=2026-10-19T16:05:12.4840000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10280] _id=6ad63fbade269131f9e99aaa ts=2026-10-19T16:05:12.4840000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[1476] _id=6ac67428de269131f9bc8d14 ts=2026-10-07T16:32:38.7180000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[1477] _id=6ac67428de269131f9bc8d15 ts=2026-10-07T16:32:38.7180000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[1477] _id=6ac67428de269131f9bc8d15 ts=2026-10-07T16:32:38.7180000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[1478] _id=6ac67428de269131f9bc8d16 ts=2026-10-07T16:32:38.7180000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a8e69a8420a1e6b56b22.jsonl[4178] _id=6ac7cc3ede269131f9c4d396 ts=2026-10-08T17:00:45.2510000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4363] _id=6ace5bb1de269131f9cf699b ts=2026-10-13T16:26:24.4690000Z; 66h 29m: 6ab9a8e69a8420a1e6b56b22.jsonl[10146] _id=6ad298c2de269131f9e83522 ts=2026-10-16T21:36:02.3440000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10298] _id=6ad63fd6de269131f9e99b7b ts=2026-10-19T16:05:41.6540000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b22.jsonl[591] _id=6ac3d796de269131f9ae5ac3 ts=2026-10-05T17:00:01.8720000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[686] _id=6ac52817de269131f9b59fcb ts=2026-10-06T16:55:51.1030000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[9239] _id=6ad25824de269131f9e65387 ts=2026-10-16T17:00:20.4940000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9240] _id=6ad25824de269131f9e65388 ts=2026-10-16T17:00:20.4940000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[9385] _id=6ad28ec8de269131f9e820b3 ts=2026-10-16T20:53:27.9010000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9386] _id=6ad28ec8de269131f9e820b4 ts=2026-10-16T20:53:27.9010000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[9423] _id=6ad28e89de269131f9e8203c ts=2026-10-16T20:52:25.2490000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9424] _id=6ad28e89de269131f9e8203d ts=2026-10-16T20:52:25.2490000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 15m 
  - Evidence: 119h 15m: 6ab9a8e69a8420a1e6b56b22.jsonl[4236] _id=6ac7cd10de269131f9c4df5c ts=2026-10-08T17:04:16.0890000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4242] _id=6ace5a20de269131f9cf5a47 ts=2026-10-13T16:19:37.8700000Z; 66h 23m: 6ab9a8e69a8420a1e6b56b22.jsonl[10241] _id=6ad29a13de269131f9e837e1 ts=2026-10-16T21:41:38.8160000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10277] _id=6ad63fbade269131f9e99aa7 ts=2026-10-19T16:05:10.9340000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b22.jsonl[652] _id=6ac3d8a1de269131f9ae7318 ts=2026-10-05T17:04:32.2050000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[660] _id=6ac527d2de269131f9b5916b ts=2026-10-06T16:54:38.6580000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 58m 
  - Evidence: 143h 58m: 6ab9a8e69a8420a1e6b56b22.jsonl[3783] _id=6ac7c786de269131f9c47b40 ts=2026-10-08T16:40:35.0310000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[6004] _id=6acfb00ede269131f9d5a236 ts=2026-10-14T16:38:37.0480000Z; 23h 54m: 6ab9a8e69a8420a1e6b56b22.jsonl[2584] _id=6ac675d7de269131f9bcdb96 ts=2026-10-07T16:39:48.9770000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[3284] _id=6ac7c602de269131f9c446c2 ts=2026-10-08T16:34:08.9190000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b22.jsonl[6745] _id=6acfb4d8de269131f9d61f0b ts=2026-10-14T16:59:03.1190000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[6953] _id=6ad1032fde269131f9ddd311 ts=2026-10-15T16:45:33.2450000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1217 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[1008] _id=6ac528edde269131f9b5d33e ts=2026-10-06T16:59:24.3490000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[1009] _id=6ac528edde269131f9b5d348 ts=2026-10-06T16:59:24.3490000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[1010] _id=6ac528efde269131f9b5d393 ts=2026-10-06T16:59:25.3380000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[1007] _id=6ac528efde269131f9b5d3a9 ts=2026-10-06T16:59:25.3380000Z; 0ms: 6ab9a8e69a8420a1e6b56b22.jsonl[1016] _id=6ac528ffde269131f9b5d6d6 ts=2026-10-06T16:59:41.4700000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[1055] _id=6ac528ffde269131f9b5d6df ts=2026-10-06T16:59:41.4700000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 4m 
  - Evidence: 144h 4m: 6ab9a8e69a8420a1e6b56b22.jsonl[3246] _id=6ac7c5a5de269131f9c43a87 ts=2026-10-08T16:32:36.7790000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5953] _id=6acfaf9ade269131f9d599a9 ts=2026-10-14T16:36:41.8340000Z; 47h 47m: 6ab9a8e69a8420a1e6b56b22.jsonl[5988] _id=6acfafe4de269131f9d59ec3 ts=2026-10-14T16:37:55.8580000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[7758] _id=6ad24fe5de269131f9e5cdaa ts=2026-10-16T16:25:08.9680000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b22.jsonl[3165] _id=6ac67b91de269131f9bd8f63 ts=2026-10-07T17:04:16.0530000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[3202] _id=6ac7c574de269131f9c43556 ts=2026-10-08T16:31:47.5220000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 66h 30m 
  - Evidence: 66h 30m: 6ab9a8e69a8420a1e6b56b22.jsonl[10119] _id=6ad2989dde269131f9e834e3 ts=2026-10-16T21:35:25.3670000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10312] _id=6ad63ffede269131f9e99ce4 ts=2026-10-19T16:06:21.1880000Z; 18m 34s: 6ab9a8e69a8420a1e6b56b22.jsonl[9839] _id=6ad29355de269131f9e82937 ts=2026-10-16T21:12:52.8630000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10072] _id=6ad297afde269131f9e832f8 ts=2026-10-16T21:31:27.6210000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 37m 
  - Evidence: 119h 37m: 6ab9a8e69a8420a1e6b56b22.jsonl[3963] _id=6ac7c9d7de269131f9c4ad75 ts=2026-10-08T16:50:30.6480000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4422] _id=6ace5c18de269131f9cf6eed ts=2026-10-13T16:28:08.2910000Z; 47h 52m: 6ab9a8e69a8420a1e6b56b22.jsonl[5255] _id=6ace64bede269131f9d01267 ts=2026-10-13T17:05:01.5690000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[7447] _id=6ad1060dde269131f9de1f33 ts=2026-10-15T16:57:49.4230000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b22.jsonl[2995] _id=6ac67a60de269131f9bd6dff ts=2026-10-07T16:59:11.1810000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[3956] _id=6ac7c9c9de269131f9c4acf9 ts=2026-10-08T16:50:16.9420000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.035s shown 
  - Evidence: 27ms: 6ab9a8e69a8420a1e6b56b22.jsonl[2782] _id=6ac677cfde269131f9bd2f32 ts=2026-10-07T16:48:14.5150000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[2786] _id=6ac677cfde269131f9bd2f36 ts=2026-10-07T16:48:14.5420000Z; 35ms: 6ab9a8e69a8420a1e6b56b22.jsonl[2789] _id=6ac677cfde269131f9bd2f2d ts=2026-10-07T16:48:14.4800000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[2782] _id=6ac677cfde269131f9bd2f32 ts=2026-10-07T16:48:14.5150000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 38m 
  - Evidence: 191h 38m: 6ab9a8e69a8420a1e6b56b22.jsonl[516] _id=6ac3d6fcde269131f9ae4b93 ts=2026-10-05T16:57:31.9440000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4639] _id=6ace5de6de269131f9cf8827 ts=2026-10-13T16:35:49.6960000Z; 48h 32m: 6ab9a8e69a8420a1e6b56b22.jsonl[5679] _id=6acfae5ade269131f9d581e1 ts=2026-10-14T16:31:22.3740000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9331] _id=6ad258ffde269131f9e65f40 ts=2026-10-16T17:03:59.4170000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b22.jsonl[4639] _id=6ace5de6de269131f9cf8827 ts=2026-10-13T16:35:49.6960000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5660] _id=6acfae4fde269131f9d5814d ts=2026-10-14T16:31:11.0810000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 36m 
  - Evidence: 191h 36m: 6ab9a8e69a8420a1e6b56b22.jsonl[517] _id=6ac3d6fcde269131f9ae4b97 ts=2026-10-05T16:57:31.9780000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4559] _id=6ace5d6fde269131f9cf7f9e ts=2026-10-13T16:33:50.6060000Z; 48h 31m: 6ab9a8e69a8420a1e6b56b22.jsonl[5683] _id=6acfae5ade269131f9d581e8 ts=2026-10-14T16:31:22.4570000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9283] _id=6ad258a6de269131f9e659e1 ts=2026-10-16T17:02:30.4350000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b22.jsonl[4621] _id=6ace5de6de269131f9cf882c ts=2026-10-13T16:35:49.7220000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5587] _id=6acfadc7de269131f9d57901 ts=2026-10-14T16:28:55.1350000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.031s..0.031s shown 
  - Evidence: 31ms: 6ab9a8e69a8420a1e6b56b22.jsonl[9669] _id=6ad291eede269131f9e8261a ts=2026-10-16T21:06:54.2380000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9686] _id=6ad291eede269131f9e8261d ts=2026-10-16T21:06:54.2690000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 36m 
  - Evidence: 191h 36m: 6ab9a8e69a8420a1e6b56b22.jsonl[509] _id=6ac3d6ecde269131f9ae4a19 ts=2026-10-05T16:57:15.6220000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4563] _id=6ace5d72de269131f9cf7fcb ts=2026-10-13T16:33:53.7400000Z; 48h 31m: 6ab9a8e69a8420a1e6b56b22.jsonl[5676] _id=6acfae55de269131f9d5819a ts=2026-10-14T16:31:16.8320000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[9280] _id=6ad258a1de269131f9e6599d ts=2026-10-16T17:02:25.1560000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b22.jsonl[4637] _id=6ace5de4de269131f9cf87fd ts=2026-10-13T16:35:47.7930000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5546] _id=6acfadabde269131f9d57740 ts=2026-10-14T16:28:26.8030000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 37 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6ab9a8e69a8420a1e6b56b22.jsonl[5553] _id=6acfadafde269131f9d57793 ts=2026-10-14T16:28:31.4590000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5549] _id=6acfadafde269131f9d57795 ts=2026-10-14T16:28:31.4630000Z; 5ms: 6ab9a8e69a8420a1e6b56b22.jsonl[5551] _id=6acfadafde269131f9d57789 ts=2026-10-14T16:28:30.6240000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5552] _id=6acfadafde269131f9d5778b ts=2026-10-14T16:28:30.6290000Z; 7ms: 6ab9a8e69a8420a1e6b56b22.jsonl[5641] _id=6acfae3ade269131f9d57fe0 ts=2026-10-14T16:30:49.6280000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5643] _id=6acfae3ade269131f9d57fe2 ts=2026-10-14T16:30:49.6350000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 37m 
  - Evidence: 191h 37m: 6ab9a8e69a8420a1e6b56b22.jsonl[518] _id=6ac3d6fade269131f9ae4b39 ts=2026-10-05T16:57:29.1980000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4600] _id=6ace5db6de269131f9cf8483 ts=2026-10-13T16:35:01.8970000Z; 23h 53m: 6ab9a8e69a8420a1e6b56b22.jsonl[4608] _id=6ace5dcede269131f9cf85e5 ts=2026-10-13T16:35:25.4380000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5544] _id=6acfaddfde269131f9d57a5c ts=2026-10-14T16:29:19.3920000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b22.jsonl[4206] _id=6ac7cca1de269131f9c4da1a ts=2026-10-08T17:02:24.8250000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4241] _id=6ace5a10de269131f9cf59d2 ts=2026-10-13T16:19:27.7760000Z; 66h 35m: 6ab9a8e69a8420a1e6b56b22.jsonl[10019] _id=6ad29746de269131f9e83133 ts=2026-10-16T21:29:42.4950000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10273] _id=6ad63fa9de269131f9e99a0b ts=2026-10-19T16:04:56.8440000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b22.jsonl[1471] _id=6ac67418de269131f9bc8bd7 ts=2026-10-07T16:32:23.2930000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[3177] _id=6ac7c4fcde269131f9c42b04 ts=2026-10-08T16:29:47.4780000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b22.jsonl[4205] _id=6ac7cca1de269131f9c4da19 ts=2026-10-08T17:02:24.8250000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4240] _id=6ace5a10de269131f9cf59d1 ts=2026-10-13T16:19:27.7750000Z; 66h 25m: 6ab9a8e69a8420a1e6b56b22.jsonl[10210] _id=6ad29981de269131f9e836da ts=2026-10-16T21:39:12.8580000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10272] _id=6ad63fa9de269131f9e99a0a ts=2026-10-19T16:04:56.8440000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b22.jsonl[1470] _id=6ac67418de269131f9bc8bd6 ts=2026-10-07T16:32:23.2930000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[3176] _id=6ac7c4fcde269131f9c42b03 ts=2026-10-08T16:29:47.4780000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6ab9a8e69a8420a1e6b56b22.jsonl[4238] _id=6ace5a10de269131f9cf59ce ts=2026-10-08T17:04:22.797Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[5279] _id=6acfab84de269131f9d54e2c ts=2026-10-13T17:05:21.051Z; 47h 55m: 6ab9a8e69a8420a1e6b56b22.jsonl[1468] _id=6ac67418de269131f9bc8bd1 ts=2026-10-06T17:04:26.477Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4165] _id=6ac7cc28de269131f9c4d125 ts=2026-10-08T17:00:23.0860000Z; 24h 45m: 6ab9a8e69a8420a1e6b56b22.jsonl[5286] _id=6acfaba8de269131f9d5506d ts=2026-10-14T16:19:52.2520000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[7625] _id=6ad107d1de269131f9de4b20 ts=2026-10-15T17:05:21.3600000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b22.jsonl[4214] _id=6ac7ccb0de269131f9c4daba ts=2026-10-08T17:02:38.4110000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[4247] _id=6ace5a20de269131f9cf5a4b ts=2026-10-13T16:19:42.5180000Z; 66h 35m: 6ab9a8e69a8420a1e6b56b22.jsonl[10025] _id=6ad2975ade269131f9e8318d ts=2026-10-16T21:30:01.5940000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[10281] _id=6ad63fbade269131f9e99aab ts=2026-10-19T16:05:12.5660000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b22.jsonl[648] _id=6ac3d888de269131f9ae7171 ts=2026-10-05T17:04:07.1380000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[659] _id=6ac527d3de269131f9b591a5 ts=2026-10-06T16:54:40.9470000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.002s..0.007s shown 
  - Evidence: 2ms: 6ab9a8e69a8420a1e6b56b22.jsonl[389] _id=6ac3d605de269131f9ae2fda ts=2026-10-05T16:53:23.9900000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[393] _id=6ac3d605de269131f9ae2fdf ts=2026-10-05T16:53:23.9920000Z; 6ms: 6ab9a8e69a8420a1e6b56b22.jsonl[8732] _id=6ad254e1de269131f9e61422 ts=2026-10-16T16:46:25.0690000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[8734] _id=6ad254e1de269131f9e61426 ts=2026-10-16T16:46:25.0750000Z; 7ms: 6ab9a8e69a8420a1e6b56b22.jsonl[8621] _id=6ad25409de269131f9e609ab ts=2026-10-16T16:42:49.0270000Z -> 6ab9a8e69a8420a1e6b56b22.jsonl[8622] _id=6ad25409de269131f9e609af ts=2026-10-16T16:42:49.0340000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[355] _id=6ac3d5d7de269131f9ae2c05 ts=2026-10-05T16:52:38.7490000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[527] _id=6ac3d716de269131f9ae4df8 ts=2026-10-05T16:57:57.8480000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[3713] _id=6ac7c775de269131f9c478ea ts=2026-10-08T16:40:20.7890000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[878] _id=6ac528b1de269131f9b5c639 ts=2026-10-06T16:58:22.4970000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[879] _id=6ac528b1de269131f9b5c645 ts=2026-10-06T16:58:22.5000000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[846] _id=6ac528b1de269131f9b5c651 ts=2026-10-06T16:58:22.6120000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 53 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[822] _id=6ac528a8de269131f9b5c465 ts=2026-10-06T16:58:01.1200000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[824] _id=6ac528a8de269131f9b5c472 ts=2026-10-06T16:58:01.9530000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[850] _id=6ac528abde269131f9b5c51a ts=2026-10-06T16:58:09.5450000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[5683] _id=6acfae5ade269131f9d581e8 ts=2026-10-14T16:31:22.4570000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[617] _id=6ac3d843de269131f9ae6bed ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 177 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[863] _id=6ac528adde269131f9b5c583 ts=2026-10-06T16:58:10.4280000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[854] _id=6ac528aede269131f9b5c595 ts=2026-10-06T16:58:10.6030000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[855] _id=6ac528aede269131f9b5c59a ts=2026-10-06T16:58:10.6030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 470 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[816] _id=6ac528a5de269131f9b5c3af ts=2026-10-06T16:56:41.1760000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[821] _id=6ac528a7de269131f9b5c3e8 ts=2026-10-06T16:56:41.3920000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[813] _id=6ac528a7de269131f9b5c3ef ts=2026-10-06T16:56:41.4720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[3202] _id=6ac7c574de269131f9c43556 ts=2026-10-08T16:31:47.5220000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[7447] _id=6ad1060dde269131f9de1f33 ts=2026-10-15T16:57:49.4230000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[7451] _id=6ad10615de269131f9de200d ts=2026-10-15T16:57:57.0210000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[7480] _id=6ad10671de269131f9de2a8f ts=2026-10-15T16:59:28.4240000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[9507] _id=6ad28ffade269131f9e822af ts=2026-10-16T20:58:33.5020000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[512] _id=6ac3d6f7de269131f9ae4af5 ts=2026-10-05T16:57:26.5170000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[514] _id=6ac3d6f8de269131f9ae4b0b ts=2026-10-05T16:57:27.9610000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[4604] _id=6ace5dc7de269131f9cf855e ts=2026-10-13T16:35:18.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 21 open, 20 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 402 start, 396 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 38 unmatched 'BecameCameraCentered' (totals: 497 open, 472 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 60 unmatched 'BecameVisible' (totals: 798 open, 791 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 22 open, 21 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'argumentationToolOpen' (totals: 15 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 44 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 238 of 10436 adjacent _id pairs reverse in client time; worst 90.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b22.jsonl[782] _id=6ac528a3de269131f9b5c32f ts=2026-10-06T16:58:11.4330000Z`; `6ab9a8e69a8420a1e6b56b22.jsonl[783] _id=6ac528a4de269131f9b5c341 ts=2026-10-06T16:56:40.7140000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.70s, min -429305.49s, max -0.30s over 10437 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b22\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
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

### `InputEvent` — 2709 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (776); Unit 3 Dev (626); Unit 3 Dungeon Dev (563); Unit 4 Dev (286); Unit 4 Dev - Dungeon (273); Unit 1 Dev (128); Unit 4 Dev - Anderson Base (57)
- **Intervals:** median 1.37s (p5 0.15s / p95 24.22s, n=2708)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2709/2709 records)
    "pressed"  x2709
data.actionType  (string, 2709/2709 records)
    "Move"  x1767
    "Jump"  x390
    "Interact"  x321
    "Hoverboard"  x95
    "Ascend"  x78
    "Descend"  x25
    "Map"  x16
    "Pause"  x10
    "Sprint"  x4
    "SkipCinematic"  x3
data.key  (string, 2709/2709 records, 5 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2709/2709 records)
    "Player"  x2188
    "Drone"  x521
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2558 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1822); Unit 4 Dev (470); Unit 3 Dungeon Dev (266)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.84s, n=2557)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2558/2558 records)
    "BecameVisible"  x798
    "BecameInvisible"  x791
    "BecameCameraCentered"  x497
    "BecameCameraUncentered"  x472
data.pieceId  (string, 2558/2558 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2558/2558 records)
    1653 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2142 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (663); Unit 3 Dev (393); Unit 4 Dev (373); Unit 3 Dungeon Dev (277); Unit 1 Dev (195); Unit 4 Dev - Anderson Base (142); Unit 4 Dev - Dungeon (99)
- **eventKey:** present on 1344 of 2142 records
- **Intervals:** median 3.79s (p5 0.01s / p95 29.67s, n=2141)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1344; [conversationId, dialogueEventType] x798
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2142/2142 records)
    numeric range 8 .. 114 (45 unique)
data.dialogueEventType  (string, 2142/2142 records)
    "DialogueNodeEvent"  x1344
    "DialogueStartEvent"  x402
    "DialogueFinishEvent"  x396
data.nodeId  (number, 1344/2142 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1828 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (578); Unit 3 Dev (306); Unit 4 Dev (287); Unit 3 Dungeon Dev (219); Unit 1 Dev (172); Unit 4 Dev - Anderson Base (149); Unit 4 Dev - Dungeon (117)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.38s, n=1818)
- **Fields under `data`:**

```text
data.position  (object, 1828/1828 records)
data.position.x  (number, 1828/1828 records)
    numeric range -677.829 .. 1557.46 (636 unique)
data.position.y  (number, 1828/1828 records)
    numeric range -113.606 .. 164.364 (444 unique)
data.position.z  (number, 1828/1828 records)
    numeric range -1218.14 .. 1938.82 (636 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 395 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (169); Unit 3 Dev (101); Unit 1 Dev (68); Unit 2 Prod (Refactor) (57)
- **Intervals:** median 0.75s (p5 0.03s / p95 11.51s, n=394)
- **Fields under `data`:**

```text
data.actionType  (string, 395/395 records)
    "argumentationNodeHoverEnd"  x177
    "argumentationNodeHoverStart"  x177
    "argumentationNodeAdd"  x30
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 395/395 records)
    "Unit 4 - Flooding"  x169
    "Unit 3 - Pollution Upstream"  x101
    "Unit 2 – Watershed"  x57
    "Unit 1 - Freshwater"  x47
    "Unit 1 - Argumentation Tutorial"  x21
data.nodeName  (string, 395/395 records)
    "A"  x65
    "II"  x57
    "1"  x49
    "I"  x49
    "C"  x39
    "B"  x38
    "2"  x24
    "4"  x24
    "D"  x23
    "3"  x16
    "5"  x11
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 286 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (73); Unit 2 Prod (Refactor) (64); Unit 3 Dungeon Dev (63); Unit 4 Dev (38); Unit 4 Dev - Anderson Base (18); Unit 1 Dev (17); Unit 3 Dev (13)
- **Intervals:** median 11.55s (p5 1.86s / p95 764.50s, n=285)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 286/286 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 286/286 records)
    97 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 105 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (54); Unit 3 Dev (28); Unit 2 Prod (Refactor) (23)
- **Intervals:** median 1.72s (p5 0.15s / p95 27.45s, n=104)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x96; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/105 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/105 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 96/105 records)
    "RightDrag"  x54
    "LeftDrag"  x42
data.currentSoilType  (string, 96/105 records)
    "CLAY"  x22
    "CLAYSAND"  x21
    "SAND"  x18
    "CLAYROCK"  x16
    "SANDGRAVEL"  x11
    "BEDROCK"  x4
    "GRAVEL"  x4
data.isCorrectSelection  (string, 96/105 records)
    "false"  x73
    "true"  x23
data.waterLevelStatus  (string, 96/105 records)
    "TooHigh"  x47
    "Proper"  x40
    "TooLow"  x9
data.waterRetentionChange  (string, 96/105 records)
    "Increase"  x38
    "Decrease"  x35
    "NoChange"  x23
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 94 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (51); Unit 3 Dev (36); Unit 4 Dev (7)
- **Intervals:** median 4.30s (p5 0.84s / p95 44868.35s, n=93)
- **`data` key-set variants:** [actionType, featureUsed] x43; [actionType, featureUsed, location] x34; [actionType, featureUsed, legendName] x17
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 94/94 records)
    "WaypointMoveEvent"  x27
    "MapOpenEvent"  x22
    "MapCloseEvent"  x21
    "Selected"  x17
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x1
data.featureUsed  (string, 94/94 records)
    "Map"  x43
    "Waypoint"  x34
    "Legend"  x17
data.legendName  (string, 17/94 records)
    "Water"  x3
    "0 ft"  x2
    "210 ft"  x2
    "90 ft"  x2
    "150 ft"  x1
    "180 ft"  x1
    "240 ft"  x1
    "270 ft"  x1
    "30 ft"  x1
    "300 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
data.location  (object, 34/94 records)
data.location.x  (number, 34/94 records)
    numeric range -355.965 .. 511.48 (31 unique)
data.location.y  (number, 34/94 records)
    numeric range -364.56 .. 310.139 (31 unique)
data.location.z  (number, 34/94 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 70 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev (11); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 70 of 70 records
- **Intervals:** median 228.48s (p5 0.01s / p95 85422.46s, n=69)
- **`data` key-set variants:** [questEventType, questID, questName] x44; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Fields under `data`:**

```text
data.questEventType  (string, 70/70 records)
    "questActiveEvent"  x44
    "questFinishEvent"  x26
data.questID  (string, 70/70 records)
    27 unique values (see csv/event_unique_values.csv)
data.questName  (string, 70/70 records)
    27 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/70 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 44 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 4 Dev (19); MainMenu (16); Unit 4 Dev - Anderson Base (5); Transition (1); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 105.52s (p5 7.46s / p95 86212.58s, n=43)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 44/44 records)
    true  x44
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 41 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 4 Dev (7); Unit 3 Dev (6)
- **Intervals:** median 2.47s (p5 0.01s / p95 106412.80s, n=40)
- **Fields under `data`:**

```text
data.actionType  (string, 41/41 records)
    "Open"  x21
    "Close"  x20
data.toolName  (string, 41/41 records, 33 empty-string)
    ""  x33
    "Settings"  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `DEBUGMenu` — 35 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (6); Unit 4 Dev (5); Unit 3 Dev (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 866.56s (p5 8.93s / p95 139944.33s, n=34)
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "DebugMenuStateChanged"  x35
data.isOpened  (bool, 35/35 records)
    false  x35
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 35 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (19); Unit 4 Dev - Anderson Base (6); Unit 2 Prod (Refactor) (5); Unit 3 Dev (3); Transition (1); Unit 1 Dev (1)
- **Intervals:** median 85.83s (p5 4.15s / p95 118328.73s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 35/35 records)
    false  x35
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 18 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (18)
- **Intervals:** median 2.89s (p5 1.18s / p95 48782.97s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records, 9 empty-string)
    ""  x9
    "cameraPlaced"  x9
data.boxId  (string, 18/18 records)
    "0"  x6
    "1"  x6
    "2"  x6
data.soilType  (string, 18/18 records)
    "Clay"  x6
    "Gravel"  x6
    "Sand"  x6
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 18 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (6); Unit 3 Dev (5)
- **Intervals:** median 4.08s (p5 0.69s / p95 206797.70s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationToolOpen"  x15
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 18/18 records)
    "Unit 2 – Watershed"  x6
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 18/18 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Waterfall Data"  x5
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 84682.57s (p5 1039.90s / p95 296626.93s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 133.19s (p5 0.05s / p95 406467.77s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 12 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (12)
- **Intervals:** median 4.63s (p5 1.21s / p95 145.31s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "ChangeCanister"  x12
data.canisterType  (string, 12/12 records)
    "Clay"  x4
    "Bedrock"  x3
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 12/12 records)
    "5"  x7
    "4"  x4
    "3"  x1
data.machine  (string, 12/12 records)
    "1"  x11
    "2"  x1
data.row  (string, 12/12 records)
    "TopRow"  x7
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 11 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (5); Unit 3 Dev (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 263.91s (p5 5.45s / p95 458084.43s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "submitAnswerEvent"  x11
data.answerSubmitted  (string, 11/11 records)
    "A,1,I"  x2
    "A,5,I"  x2
    "A,1,II"  x1
    "A,2,II"  x1
    "A,C,2,II"  x1
    "B,5,I"  x1
    "C,2,II"  x1
    "D,2,II"  x1
    "D,A,C,2,II"  x1
data.argumentationTitle  (string, 11/11 records)
    "Unit 4 - Flooding"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 4 Dev (4)
- **Intervals:** median 7.80s (p5 1.37s / p95 30.74s, n=3)
- **`data` key-set variants:** [actionType, chatID] x3; [actionKey, chatID] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 1/4 records)
    "ScrollStop"  x1
data.actionType  (string, 3/4 records)
    "Close"  x1
    "Open"  x1
    "ScrollStart"  x1
data.chatID  (string, 4/4 records)
    "NA"  x2
    "[92-33, 92-61, 92-61, 92-61, 92-38, 92-64, 92-39]"  x1
    "[92-61, 92-61, 92-38, 92-64, 92-39]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 473963.18s (p5 279530.27s / p95 668396.09s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

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
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (23 records)
- `TerasGardenBox` data.actionType: "" (9x)
- `TopographicMapEvent` data.actionType: "Selected" (17x); "WaypointMoveEvent" (27x); "WaypointResetEvent" (1x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (17x); "Waypoint" (34x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (3x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*