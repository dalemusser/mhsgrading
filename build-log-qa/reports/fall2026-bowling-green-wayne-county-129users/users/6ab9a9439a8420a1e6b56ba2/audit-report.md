# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba2

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba2
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba2.jsonl
- **Records:** 10848 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba2
- **Time span:** 2026-10-05T19:58:16.319000+00:00 .. 2026-10-16T20:12:08.458000+00:00 (264h 13m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba2\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 10848 records, 10 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 92 INFO, 2 NOT_TESTED, 82 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4737 | 43.67 | 1 | 7 | 0 | 2026-10-05T19:58:31.573000+00:00 | 2026-10-16T20:08:13.188000+00:00 | 264h 9m |
| PuzzlePieceVisibleEvent | 2139 | 19.72 | 1 | 3 | 0 | 2026-10-06T19:48:47.733000+00:00 | 2026-10-15T19:57:24.357000+00:00 | 216h 8m |
| DialogueEvent | 1637 | 15.09 | 1 | 7 | 1056 | 2026-10-05T19:58:48.145000+00:00 | 2026-10-16T20:12:04.300000+00:00 | 264h 13m |
| PlayerPositionEvent | 1248 | 11.5 | 1 | 7 | 0 | 2026-10-05T19:58:28.038000+00:00 | 2026-10-16T20:11:59.720000+00:00 | 264h 13m |
| Soil Key Puzzle | 315 | 2.9 | 1 | 3 | 0 | 2026-10-06T19:53:48.776000+00:00 | 2026-10-15T19:36:42.725000+00:00 | 215h 42m |
| argumentationNodeEvent | 291 | 2.68 | 1 | 4 | 0 | 2026-10-06T19:38:56.209000+00:00 | 2026-10-16T20:12:02.829000+00:00 | 240h 33m |
| ObjectInterEvent | 197 | 1.82 | 1 | 7 | 0 | 2026-10-05T20:03:23.585000+00:00 | 2026-10-16T20:08:15.750000+00:00 | 264h 4m |
| TopographicMapEvent | 81 | 0.75 | 1 | 2 | 0 | 2026-10-06T19:49:06.242000+00:00 | 2026-10-14T20:05:12.820000+00:00 | 192h 16m |
| questEvent | 66 | 0.61 | 1 | 7 | 66 | 2026-10-05T19:58:48.120000+00:00 | 2026-10-16T20:05:49.403000+00:00 | 264h 7m |
| DEBUGMenu | 33 | 0.3 | 1 | 8 | 0 | 2026-10-05T19:58:28.025000+00:00 | 2026-10-16T20:05:48.112000+00:00 | 264h 7m |
| gameWindowFocusEvent | 23 | 0.21 | 1 | 6 | 0 | 2026-10-05T19:58:16.319000+00:00 | 2026-10-16T20:05:36.206000+00:00 | 264h 7m |
| argumentationAnswerEvent | 19 | 0.18 | 1 | 4 | 0 | 2026-10-06T19:40:01.044000+00:00 | 2026-10-16T20:12:04.236000+00:00 | 240h 32m |
| gameStartEvent | 15 | 0.14 | 1 | 1 | 0 | 2026-10-05T19:58:16.320000+00:00 | 2026-10-16T20:05:36.206000+00:00 | 264h 7m |
| argumentationEvent | 13 | 0.12 | 1 | 4 | 0 | 2026-10-06T19:39:45.689000+00:00 | 2026-10-16T20:12:04.298000+00:00 | 240h 32m |
| gameWindowUnfocusEvent | 10 | 0.09 | 1 | 6 | 0 | 2026-10-05T19:59:17.181000+00:00 | 2026-10-16T20:12:08.458000+00:00 | 264h 12m |
| argumentationToolEvent | 8 | 0.07 | 1 | 3 | 0 | 2026-10-06T19:39:41.993000+00:00 | 2026-10-14T19:43:04.979000+00:00 | 192h 3m |
| soilMachine | 7 | 0.06 | 1 | 1 | 0 | 2026-10-15T19:50:05.447000+00:00 | 2026-10-15T19:54:03.217000+00:00 | 3m 57s |
| DaniEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-14T19:37:50.234000+00:00 | 2026-10-14T19:37:58.042000+00:00 | 7.8s |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-06T19:43:58.473000+00:00 | 2026-10-15T19:30:55.112000+00:00 | 215h 46m |
| chatEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-14T19:37:53.607000+00:00 | 2026-10-14T19:37:55.350000+00:00 | 1.7s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 218.664s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 388408.319s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.042s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 0.297s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.848s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 23.981s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 1.743s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 750.901s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1025.65s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 19.627s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: PodsEscapingCopernicus Cutscene 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 8.3x vs baseline. 
  - Observed: 315 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; B,1,II; B,2,II; B,C,2,II; B,C,A,2,II; C,2,II; C,A,D,2,II; D,1,II; D,2,II 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-218, 11-224, 11-226, 11-23, 11-24] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 10 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[163] _id=6ac40304de269131f9af8f1b ts=2026-10-05T20:05:23.6860000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[248] _id=6ac403ebde269131f9af942d ts=2026-10-05T20:09:14.0580000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[275] _id=6ac4041bde269131f9af95a7 ts=2026-10-05T20:10:02.5590000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[1] _id=6ac40159de269131f9af884d ts=2026-10-05T19:58:16.3200000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[314] _id=6ac54ae7de269131f9b79d58 ts=2026-10-06T19:24:22.7870000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[310] _id=6ac54b36de269131f9b79dad ts=2026-10-06T19:25:41.2890000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[0] _id=6ac40159de269131f9af8849 ts=2026-10-05T19:58:16.3190000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[15] _id=6ac40196de269131f9af88db ts=2026-10-05T19:59:17.4050000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[313] _id=6ac54ae7de269131f9b79d57 ts=2026-10-06T19:24:22.7870000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[12] _id=6ac40196de269131f9af88d9 ts=2026-10-05T19:59:17.1810000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[866] _id=6ac54f82de269131f9b7b1db ts=2026-10-06T19:44:01.7120000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[2136] _id=6ac552c8de269131f9b7e373 ts=2026-10-06T19:58:00.1000000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4736 | 0.0 | 0.467 | 200.798 | 4.714 | 515705.715 | 0.3 | 238 | 7 |
| PuzzlePieceVisibleEvent | 2138 | 0.0 | 0.042 | 363.946 | 1.317 | 519005.859 | 0.16 | 1111 | 5 |
| DialogueEvent | 1636 | 0.0 | 3.817 | 581.416 | 25.627 | 515699.172 | 0.1 | 454 | 6 |
| PlayerPositionEvent | 1239 | 0.0 | 10.003 | 767.55 | 10.373 | 515651.871 | 0.08 | 2 | 6 |
| Soil Key Puzzle | 314 | 0.0 | 0.297 | 2473.165 | 6.873 | 603814.159 | 0.02 | 31 | 3 |
| argumentationNodeEvent | 290 | 0.001 | 0.757 | 2986.161 | 10.205 | 517037.045 | 0.02 | 38 | 4 |
| ObjectInterEvent | 196 | 0.0 | 11.52 | 4850.47 | 300.175 | 516539.721 | 0.01 | 6 | 7 |
| TopographicMapEvent | 80 | 0.02 | 8.848 | 8652.082 | 686.311 | 517068.511 | 0.01 | 6 | 5 |
| questEvent | 65 | 0.004 | 171.961 | 14628.02 | 84327.382 | 515893.375 | 0.0 | 9 | 10 |
| DEBUGMenu | 32 | 7.431 | 218.664 | 29713.753 | 86367.816 | 515561.43 | 0.0 | 0 | 12 |
| gameWindowFocusEvent | 22 | 6.824 | 750.901 | 43219.995 | 86586.973 | 515570.968 | 0.0 | 0 | 12 |
| argumentationAnswerEvent | 18 | 1.082 | 23.981 | 48106.844 | 225604.348 | 517100.574 | 0.0 | 0 | 4 |
| gameStartEvent | 14 | 41.141 | 2050.322 | 67917.135 | 236810.57 | 515570.968 | 0.0 | 0 | 10 |
| argumentationEvent | 12 | 0.041 | 89.193 | 72161.551 | 328427.153 | 517045.561 | 0.0 | 2 | 4 |
| gameWindowUnfocusEvent | 9 | 4.026 | 1025.65 | 105685.697 | 431029.497 | 602666.879 | 0.0 | 0 | 6 |
| argumentationToolEvent | 7 | 3.332 | 10.169 | 98771.855 | 414239.774 | 517140.105 | 0.0 | 0 | 2 |
| soilMachine | 6 | 3.089 | 19.627 | 39.628 | 115.974 | 136.223 | 1.51 | 0 | 0 |
| DaniEvent | 3 | 1.099 | 3.128 | 2.603 | 3.536 | 3.581 | 23.05 | 0 | 0 |
| EndOfUnit | 2 | 174279.665 | 388408.319 | 388408.32 | 581124.109 | 602536.974 | 0.0 | 0 | 2 |
| chatEvent | 1 | 1.743 | 1.743 | 1.743 | 1.743 | 1.743 | 34.42 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 7 group(s), 13 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[2522] _id=6ac69f06de269131f9bf211a ts=2026-10-07T19:35:32.3540000Z == 6ab9a9439a8420a1e6b56ba2.jsonl[2523] _id=6ac69f06de269131f9bf211b ts=2026-10-07T19:35:32.3540000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[2524] _id=6ac69f06de269131f9bf211c ts=2026-10-07T19:35:32.3550000Z == 6ab9a9439a8420a1e6b56ba2.jsonl[2525] _id=6ac69f06de269131f9bf211d ts=2026-10-07T19:35:32.3550000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[3939] _id=6ac6a5c2de269131f9bf7534 ts=2026-10-07T20:04:17.2610000Z == 6ab9a9439a8420a1e6b56ba2.jsonl[3941] _id=6ac6a5c2de269131f9bf7536 ts=2026-10-07T20:04:17.2610000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 71 group(s), 115 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[1019] _id=6ac550eade269131f9b7bbb8 ts=2026-10-06T19:50:00.3040000Z == 6ab9a9439a8420a1e6b56ba2.jsonl[1001] _id=6ac550eade269131f9b7bbbc ts=2026-10-06T19:50:00.3040000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[1026] _id=6ac550ecde269131f9b7bbd9 ts=2026-10-06T19:50:02.6510000Z == 6ab9a9439a8420a1e6b56ba2.jsonl[1031] _id=6ac550ecde269131f9b7bbdb ts=2026-10-06T19:50:02.6510000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[1035] _id=6ac550ecde269131f9b7bbe7 ts=2026-10-06T19:50:02.8930000Z == 6ab9a9439a8420a1e6b56ba2.jsonl[1036] _id=6ac550edde269131f9b7bbe9 ts=2026-10-06T19:50:02.8930000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6ab9a9439a8420a1e6b56ba2.jsonl[50] _id=6ac4028cde269131f9af8cff ts=2026-10-05T20:03:23.5850000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[116] _id=6ac4028cde269131f9af8d01 ts=2026-10-05T20:03:23.5940000Z`; `10ms: 6ab9a9439a8420a1e6b56ba2.jsonl[339] _id=6ac54b66de269131f9b79e44 ts=2026-10-06T19:26:29.7100000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[348] _id=6ac54b66de269131f9b79e46 ts=2026-10-06T19:26:29.7200000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 32 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `307ms: 6ab9a9439a8420a1e6b56ba2.jsonl[3683] _id=6ac6a52dde269131f9bf6b8a ts=2026-10-07T20:01:48.1090000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[3686] _id=6ac6a52dde269131f9bf6b8d ts=2026-10-07T20:01:48.4160000Z`; `169ms: 6ab9a9439a8420a1e6b56ba2.jsonl[3685] _id=6ac6a52dde269131f9bf6b8c ts=2026-10-07T20:01:48.4150000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[3684] _id=6ac6a52dde269131f9bf6b93 ts=2026-10-07T20:01:48.5840000Z`; `169ms: 6ab9a9439a8420a1e6b56ba2.jsonl[3686] _id=6ac6a52dde269131f9bf6b8d ts=2026-10-07T20:01:48.4160000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[3692] _id=6ac6a52dde269131f9bf6b94 ts=2026-10-07T20:01:48.5850000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `41ms: 6ab9a9439a8420a1e6b56ba2.jsonl[6546] _id=6acfdb93de269131f9d90a41 ts=2026-10-14T19:44:19.0900000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[6549] _id=6acfdb93de269131f9d90a44 ts=2026-10-14T19:44:19.1310000Z`; `46ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10844] _id=6ad28515de269131f9e8046f ts=2026-10-16T20:12:04.2520000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[10834] _id=6ad28515de269131f9e80473 ts=2026-10-16T20:12:04.2980000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `557ms: 6ab9a9439a8420a1e6b56ba2.jsonl[716] _id=6ac54e88de269131f9b7ab06 ts=2026-10-06T19:39:52.3160000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[655] _id=6ac54e89de269131f9b7ab0a ts=2026-10-06T19:39:52.8730000Z`; `649ms: 6ab9a9439a8420a1e6b56ba2.jsonl[6448] _id=6acfdb13de269131f9d90272 ts=2026-10-14T19:42:10.6520000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[6451] _id=6acfdb14de269131f9d9027f ts=2026-10-14T19:42:11.3010000Z`; `845ms: 6ab9a9439a8420a1e6b56ba2.jsonl[6461] _id=6acfdb1fde269131f9d90369 ts=2026-10-14T19:42:23.2570000Z ~ 6ab9a9439a8420a1e6b56ba2.jsonl[6462] _id=6acfdb20de269131f9d9037b ts=2026-10-14T19:42:24.1020000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 12m 
  - Evidence: 143h 12m: 6ab9a9439a8420a1e6b56ba2.jsonl[5709] _id=6ac7f866de269131f9c7416a ts=2026-10-08T20:09:09.9270000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5721] _id=6acfd650de269131f9d897e7 ts=2026-10-14T19:21:51.3570000Z; 24h 2m: 6ab9a9439a8420a1e6b56ba2.jsonl[2519] _id=6ac69f00de269131f9bf2116 ts=2026-10-07T19:35:27.5700000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4791] _id=6ac7f12fde269131f9c6ab13 ts=2026-10-08T19:38:22.3420000Z; 23h 56m: 6ab9a9439a8420a1e6b56ba2.jsonl[10598] _id=6ad132dade269131f9e11b39 ts=2026-10-15T20:08:57.5620000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10645] _id=6ad28391de269131f9e7fa85 ts=2026-10-16T20:05:36.0500000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 14m 
  - Evidence: 143h 14m: 6ab9a9439a8420a1e6b56ba2.jsonl[5689] _id=6ac7f877de269131f9c7428a ts=2026-10-08T20:09:26.4600000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5742] _id=6acfd6eade269131f9d8a022 ts=2026-10-14T19:24:25.6320000Z; 23h 55m: 6ab9a9439a8420a1e6b56ba2.jsonl[10612] _id=6ad13324de269131f9e11eb2 ts=2026-10-15T20:10:11.3980000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10651] _id=6ad2839fde269131f9e7fad2 ts=2026-10-16T20:05:50.6740000Z; 23h 28m: 6ab9a9439a8420a1e6b56ba2.jsonl[4781] _id=6ac6a72fde269131f9bf8b20 ts=2026-10-07T20:10:22.2590000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4964] _id=6ac7f16ade269131f9c6af00 ts=2026-10-08T19:39:22.1630000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 454 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10548] _id=6ad1327fde269131f9e113ae ts=2026-10-15T20:07:26.1610000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10549] _id=6ad1327fde269131f9e113af ts=2026-10-15T20:07:26.1610000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10584] _id=6ad132b1de269131f9e11815 ts=2026-10-15T20:08:16.5820000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10587] _id=6ad132b1de269131f9e11816 ts=2026-10-15T20:08:16.5820000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[2511] _id=6ac555a8de269131f9b85028 ts=2026-10-06T20:10:16.2660000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[2539] _id=6ac69ee0de269131f9bf2110 ts=2026-10-06T20:10:16.266Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 22m 
  - Evidence: 167h 22m: 6ab9a9439a8420a1e6b56ba2.jsonl[5706] _id=6ac7f846de269131f9c73fd2 ts=2026-10-08T20:08:38.1380000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[8223] _id=6ad129efde269131f9e071a1 ts=2026-10-15T19:30:55.1120000Z; 48h 24m: 6ab9a9439a8420a1e6b56ba2.jsonl[863] _id=6ac54f7ede269131f9b7b1c1 ts=2026-10-06T19:43:58.4730000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5706] _id=6ac7f846de269131f9c73fd2 ts=2026-10-08T20:08:38.1380000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 15m 
  - Evidence: 143h 15m: 6ab9a9439a8420a1e6b56ba2.jsonl[5713] _id=6ac7f868de269131f9c74185 ts=2026-10-08T20:09:11.6290000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5729] _id=6acfd6e2de269131f9d89f89 ts=2026-10-14T19:24:17.3440000Z; 23h 55m: 6ab9a9439a8420a1e6b56ba2.jsonl[10631] _id=6ad13335de269131f9e11f23 ts=2026-10-15T20:10:28.4800000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10647] _id=6ad2839fde269131f9e7facd ts=2026-10-16T20:05:48.3130000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba2.jsonl[4717] _id=6ac6a6a2de269131f9bf8810 ts=2026-10-07T20:08:00.7210000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4802] _id=6ac7f140de269131f9c6abcc ts=2026-10-08T19:38:39.0340000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 238 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10153] _id=6ad13029de269131f9e0ed7d ts=2026-10-15T19:57:28.8880000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10154] _id=6ad13029de269131f9e0ed7e ts=2026-10-15T19:57:28.8880000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[1041] _id=6ac550eede269131f9b7bbfb ts=2026-10-06T19:50:05.3350000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[1042] _id=6ac550eede269131f9b7bbfc ts=2026-10-06T19:50:05.3350000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[1980] _id=6ac551a1de269131f9b7c780 ts=2026-10-06T19:53:05.2300000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[1981] _id=6ac551a1de269131f9b7c781 ts=2026-10-06T19:53:05.2300000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 28m 
  - Evidence: 143h 28m: 6ab9a9439a8420a1e6b56ba2.jsonl[5513] _id=6ac7f68bde269131f9c71752 ts=2026-10-08T20:01:14.7570000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5916] _id=6acfd847de269131f9d8bdec ts=2026-10-14T19:30:14.4780000Z; 24h 3m: 6ab9a9439a8420a1e6b56ba2.jsonl[2037] _id=6ac551cdde269131f9b7c9eb ts=2026-10-06T19:53:48.7840000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[3562] _id=6ac6a40ede269131f9bf5a0f ts=2026-10-07T19:57:01.0690000Z; 23h 56m: 6ab9a9439a8420a1e6b56ba2.jsonl[10625] _id=6ad13313de269131f9e11e15 ts=2026-10-15T20:09:54.5470000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10667] _id=6ad283bade269131f9e7fb23 ts=2026-10-16T20:06:17.4200000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10380] _id=6ad13193de269131f9e10361 ts=2026-10-15T20:03:31.0270000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10386] _id=6ad13193de269131f9e10362 ts=2026-10-15T20:03:31.0270000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10442] _id=6ad131d0de269131f9e106cf ts=2026-10-15T20:04:31.1910000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10445] _id=6ad131d0de269131f9e106d0 ts=2026-10-15T20:04:31.1910000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10688] _id=6ad283e9de269131f9e7fb9e ts=2026-10-16T20:07:04.1400000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10689] _id=6ad283e9de269131f9e7fb9f ts=2026-10-16T20:07:04.1400000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 14m 
  - Evidence: 143h 14m: 6ab9a9439a8420a1e6b56ba2.jsonl[5720] _id=6acfd650de269131f9d897dd ts=2026-10-08T20:10:01.65Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5728] _id=6acfd6e2de269131f9d89f88 ts=2026-10-14T19:24:13.5210000Z; 23h 55m: 6ab9a9439a8420a1e6b56ba2.jsonl[10632] _id=6ad13335de269131f9e11f2b ts=2026-10-15T20:10:28.8920000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10646] _id=6ad2839fde269131f9e7facc ts=2026-10-16T20:05:48.1210000Z; 23h 28m: 6ab9a9439a8420a1e6b56ba2.jsonl[4780] _id=6ac6a72ede269131f9bf8b18 ts=2026-10-07T20:10:21.0330000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4801] _id=6ac7f140de269131f9c6abcb ts=2026-10-08T19:38:34.1160000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[2344] _id=6ac55469de269131f9b828a9 ts=2026-10-06T20:04:56.4860000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[2348] _id=6ac554d2de269131f9b835eb ts=2026-10-06T20:04:56.486Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[5719] _id=6ac7f89ade269131f9c74475 ts=2026-10-08T20:10:01.6500000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5720] _id=6acfd650de269131f9d897dd ts=2026-10-08T20:10:01.65Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 10m 
  - Evidence: 144h 10m: 6ab9a9439a8420a1e6b56ba2.jsonl[4919] _id=6ac7f14fde269131f9c6ad43 ts=2026-10-08T19:38:52.5930000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6886] _id=6acfdcacde269131f9d916d7 ts=2026-10-14T19:48:58.4520000Z; 24h 10m: 6ab9a9439a8420a1e6b56ba2.jsonl[1944] _id=6ac55185de269131f9b7c69b ts=2026-10-06T19:52:35.0240000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[3842] _id=6ac6a57fde269131f9bf70e0 ts=2026-10-07T20:03:09.0090000Z; 23h 45m: 6ab9a9439a8420a1e6b56ba2.jsonl[7264] _id=6acfdd40de269131f9d9217b ts=2026-10-14T19:51:24.5990000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[8358] _id=6ad12b4fde269131f9e08dc3 ts=2026-10-15T19:36:45.9270000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1111 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10018] _id=6ad12f9bde269131f9e0e12b ts=2026-10-15T19:55:03.9490000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10019] _id=6ad12f9bde269131f9e0e12c ts=2026-10-15T19:55:03.9490000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[1001] _id=6ac550eade269131f9b7bbbc ts=2026-10-06T19:50:00.3040000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[1002] _id=6ac550eade269131f9b7bbbd ts=2026-10-06T19:50:00.3040000Z; 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10029] _id=6ad12f9ede269131f9e0e170 ts=2026-10-15T19:55:07.0070000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10050] _id=6ad12f9ede269131f9e0e17e ts=2026-10-15T19:55:07.0070000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 43m 
  - Evidence: 167h 43m: 6ab9a9439a8420a1e6b56ba2.jsonl[3897] _id=6ac6a59ede269131f9bf7288 ts=2026-10-07T20:03:41.7240000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6738] _id=6acfdc44de269131f9d911e3 ts=2026-10-14T19:47:15.8830000Z; 24h 3m: 6ab9a9439a8420a1e6b56ba2.jsonl[2043] _id=6ac551d0de269131f9b7ca36 ts=2026-10-06T19:53:51.8540000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[3561] _id=6ac6a40ede269131f9bf5a0d ts=2026-10-07T19:57:01.0640000Z; 23h 47m: 6ab9a9439a8420a1e6b56ba2.jsonl[6861] _id=6acfdc83de269131f9d914c9 ts=2026-10-14T19:48:18.6390000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[8327] _id=6ad12b2cde269131f9e08b24 ts=2026-10-15T19:36:11.3660000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 31 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba2.jsonl[3701] _id=6ac6a52fde269131f9bf6bbe ts=2026-10-07T20:01:50.5350000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[3702] _id=6ac6a52fde269131f9bf6bbf ts=2026-10-07T20:01:50.5350000Z; 1ms: 6ab9a9439a8420a1e6b56ba2.jsonl[3614] _id=6ac6a53cde269131f9bf6cf7 ts=2026-10-07T20:02:03.3990000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[3615] _id=6ac6a53cde269131f9bf6cf8 ts=2026-10-07T20:02:03.4000000Z; 1ms: 6ab9a9439a8420a1e6b56ba2.jsonl[3682] _id=6ac6a52dde269131f9bf6b89 ts=2026-10-07T20:01:48.1080000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[3683] _id=6ac6a52dde269131f9bf6b8a ts=2026-10-07T20:01:48.1090000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a9439a8420a1e6b56ba2.jsonl[5150] _id=6ac7f3cfde269131f9c6dea7 ts=2026-10-08T19:49:34.5220000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5808] _id=6acfd79bde269131f9d8ae8d ts=2026-10-14T19:27:23.0330000Z; 23h 53m: 6ab9a9439a8420a1e6b56ba2.jsonl[3478] _id=6ac6a3bdde269131f9bf560d ts=2026-10-07T19:55:40.5070000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5146] _id=6ac7f3c1de269131f9c6dddb ts=2026-10-08T19:49:20.5840000Z; 23h 29m: 6ab9a9439a8420a1e6b56ba2.jsonl[2479] _id=6ac5558bde269131f9b84d0d ts=2026-10-06T20:09:46.8450000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[2675] _id=6ac69ff5de269131f9bf2499 ts=2026-10-07T19:39:31.9040000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.020s..0.024s shown 
  - Evidence: 20ms: 6ab9a9439a8420a1e6b56ba2.jsonl[2227] _id=6ac5535ade269131f9b8004a ts=2026-10-06T20:00:26.1010000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[2231] _id=6ac5535ade269131f9b8004e ts=2026-10-06T20:00:26.1210000Z; 20ms: 6ab9a9439a8420a1e6b56ba2.jsonl[2666] _id=6ac69ff9de269131f9bf24a7 ts=2026-10-07T19:39:36.1340000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[2670] _id=6ac69ff9de269131f9bf24ab ts=2026-10-07T19:39:36.1540000Z; 24ms: 6ab9a9439a8420a1e6b56ba2.jsonl[2471] _id=6ac5556fde269131f9b84a00 ts=2026-10-06T20:09:19.4100000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[2475] _id=6ac5556fde269131f9b84a04 ts=2026-10-06T20:09:19.4340000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 38m 
  - Evidence: 143h 38m: 6ab9a9439a8420a1e6b56ba2.jsonl[5626] _id=6ac7f763de269131f9c72c8a ts=2026-10-08T20:04:50.2930000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6492] _id=6acfdb4fde269131f9d906b6 ts=2026-10-14T19:43:10.8670000Z; 48h 22m: 6ab9a9439a8420a1e6b56ba2.jsonl[769] _id=6ac54ee6de269131f9b7ad3c ts=2026-10-06T19:41:25.7960000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5589] _id=6ac7f73ade269131f9c7297b ts=2026-10-08T20:04:09.6330000Z; 24h 22m: 6ab9a9439a8420a1e6b56ba2.jsonl[6545] _id=6acfdb93de269131f9d90a3d ts=2026-10-14T19:44:19.0630000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10522] _id=6ad13266de269131f9e1121a ts=2026-10-15T20:07:01.8200000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a9439a8420a1e6b56ba2.jsonl[5629] _id=6ac7f763de269131f9c72c90 ts=2026-10-08T20:04:50.3160000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6453] _id=6acfdb18de269131f9d902d2 ts=2026-10-14T19:42:15.8770000Z; 48h 21m: 6ab9a9439a8420a1e6b56ba2.jsonl[761] _id=6ac54ee6de269131f9b7ad40 ts=2026-10-06T19:41:25.8260000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5564] _id=6ac7f6fdde269131f9c723f3 ts=2026-10-08T20:03:08.8270000Z; 24h 22m: 6ab9a9439a8420a1e6b56ba2.jsonl[6549] _id=6acfdb93de269131f9d90a44 ts=2026-10-14T19:44:19.1310000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10492] _id=6ad13246de269131f9e10f86 ts=2026-10-15T20:06:30.1270000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.041s..0.046s shown 
  - Evidence: 41ms: 6ab9a9439a8420a1e6b56ba2.jsonl[6546] _id=6acfdb93de269131f9d90a41 ts=2026-10-14T19:44:19.0900000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6549] _id=6acfdb93de269131f9d90a44 ts=2026-10-14T19:44:19.1310000Z; 46ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10844] _id=6ad28515de269131f9e8046f ts=2026-10-16T20:12:04.2520000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10834] _id=6ad28515de269131f9e80473 ts=2026-10-16T20:12:04.2980000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 37m 
  - Evidence: 143h 37m: 6ab9a9439a8420a1e6b56ba2.jsonl[5618] _id=6ac7f761de269131f9c72c69 ts=2026-10-08T20:04:48.4690000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6441] _id=6acfdb0ede269131f9d9022a ts=2026-10-14T19:42:05.5140000Z; 48h 21m: 6ab9a9439a8420a1e6b56ba2.jsonl[764] _id=6ac54edfde269131f9b7ad01 ts=2026-10-06T19:41:18.6580000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5559] _id=6ac7f6fade269131f9c7239a ts=2026-10-08T20:03:06.1410000Z; 24h 22m: 6ab9a9439a8420a1e6b56ba2.jsonl[6544] _id=6acfdb8fde269131f9d909fc ts=2026-10-14T19:44:14.8340000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10491] _id=6ad13244de269131f9e10f58 ts=2026-10-15T20:06:27.5890000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 38 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56ba2.jsonl[6444] _id=6acfdb0ede269131f9d9022c ts=2026-10-14T19:42:05.5460000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6445] _id=6acfdb0ede269131f9d9022d ts=2026-10-14T19:42:05.5470000Z; 5ms: 6ab9a9439a8420a1e6b56ba2.jsonl[10533] _id=6ad13272de269131f9e112da ts=2026-10-15T20:07:13.3400000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10527] _id=6ad13272de269131f9e112de ts=2026-10-15T20:07:13.3450000Z; 6ms: 6ab9a9439a8420a1e6b56ba2.jsonl[693] _id=6ac54e57de269131f9b7aa5e ts=2026-10-06T19:39:03.5300000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[694] _id=6ac54e58de269131f9b7aa60 ts=2026-10-06T19:39:03.5360000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 39m 
  - Evidence: 143h 39m: 6ab9a9439a8420a1e6b56ba2.jsonl[5580] _id=6ac7f721de269131f9c7276f ts=2026-10-08T20:03:45.2180000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6483] _id=6acfdb35de269131f9d90520 ts=2026-10-14T19:42:45.3230000Z; 48h 22m: 6ab9a9439a8420a1e6b56ba2.jsonl[768] _id=6ac54ee3de269131f9b7ad17 ts=2026-10-06T19:41:22.8840000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5579] _id=6ac7f71ede269131f9c72724 ts=2026-10-08T20:03:41.8860000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 12m 
  - Evidence: 143h 12m: 6ab9a9439a8420a1e6b56ba2.jsonl[5692] _id=6ac7f85dde269131f9c740ea ts=2026-10-08T20:09:00.6990000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5723] _id=6acfd650de269131f9d897e9 ts=2026-10-14T19:21:51.6670000Z; 24h 5m: 6ab9a9439a8420a1e6b56ba2.jsonl[5725] _id=6acfd679de269131f9d89ad7 ts=2026-10-14T19:22:32.8080000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[8163] _id=6ad1292ede269131f9e05edf ts=2026-10-15T19:27:41.6260000Z; 24h 3m: 6ab9a9439a8420a1e6b56ba2.jsonl[2542] _id=6ac69ee0de269131f9bf2114 ts=2026-10-07T19:34:55.4500000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4793] _id=6ac7f12fde269131f9c6ab15 ts=2026-10-08T19:38:22.4750000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 12m 
  - Evidence: 143h 12m: 6ab9a9439a8420a1e6b56ba2.jsonl[5691] _id=6ac7f85dde269131f9c740e9 ts=2026-10-08T20:09:00.6990000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5722] _id=6acfd650de269131f9d897e8 ts=2026-10-14T19:21:51.6670000Z; 24h 3m: 6ab9a9439a8420a1e6b56ba2.jsonl[2541] _id=6ac69ee0de269131f9bf2113 ts=2026-10-07T19:34:55.4490000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4792] _id=6ac7f12fde269131f9c6ab14 ts=2026-10-08T19:38:22.4750000Z; 23h 56m: 6ab9a9439a8420a1e6b56ba2.jsonl[10594] _id=6ad132d3de269131f9e11ac8 ts=2026-10-15T20:08:50.2500000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10643] _id=6ad28391de269131f9e7fa87 ts=2026-10-16T20:05:36.2060000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 167h 24m 
  - Evidence: 167h 24m: 6ab9a9439a8420a1e6b56ba2.jsonl[4790] _id=6ac7f12fde269131f9c6ab11 ts=2026-10-07T20:10:25.494Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[6108] _id=6acfd95dde269131f9d8dceb ts=2026-10-14T19:34:52.3730000Z; 48h 12m: 6ab9a9439a8420a1e6b56ba2.jsonl[7450] _id=6acfdf13de269131f9d93faa ts=2026-10-14T19:59:15.0330000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10847] _id=6ad28519de269131f9e80478 ts=2026-10-16T20:12:08.4580000Z; 24h 7m: 6ab9a9439a8420a1e6b56ba2.jsonl[2334] _id=6ac5540ade269131f9b8187e ts=2026-10-06T20:03:21.3530000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4790] _id=6ac7f12fde269131f9c6ab11 ts=2026-10-07T20:10:25.494Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 18m 
  - Evidence: 143h 18m: 6ab9a9439a8420a1e6b56ba2.jsonl[5704] _id=6ac7f840de269131f9c73f72 ts=2026-10-08T20:08:31.8550000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[5771] _id=6acfd775de269131f9d8aac9 ts=2026-10-14T19:26:45.2300000Z; 23h 56m: 6ab9a9439a8420a1e6b56ba2.jsonl[10600] _id=6ad132dbde269131f9e11b50 ts=2026-10-15T20:08:58.7120000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[10649] _id=6ad2839fde269131f9e7facf ts=2026-10-16T20:05:49.4030000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba2.jsonl[4748] _id=6ac6a6b5de269131f9bf889a ts=2026-10-07T20:08:20.6240000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[4803] _id=6ac7f140de269131f9c6abcd ts=2026-10-08T19:38:39.0740000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a9439a8420a1e6b56ba2.jsonl[659] _id=6ac54e35de269131f9b7a9de ts=2026-10-06T19:38:28.8100000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[660] _id=6ac54e35de269131f9b7a9df ts=2026-10-06T19:38:28.8140000Z; 4ms: 6ab9a9439a8420a1e6b56ba2.jsonl[9303] _id=6ad12d73de269131f9e0bac8 ts=2026-10-15T19:45:54.2560000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[9305] _id=6ad12d73de269131f9e0bacc ts=2026-10-15T19:45:54.2600000Z; 5ms: 6ab9a9439a8420a1e6b56ba2.jsonl[9576] _id=6ad12e34de269131f9e0c5e7 ts=2026-10-15T19:49:07.2160000Z -> 6ab9a9439a8420a1e6b56ba2.jsonl[9572] _id=6ad12e34de269131f9e0c5eb ts=2026-10-15T19:49:07.2210000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[776] _id=6ac54ef8de269131f9b7ae01 ts=2026-10-06T19:41:43.8150000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[2825] _id=6ac6a126de269131f9bf3462 ts=2026-10-07T19:44:37.4940000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[4781] _id=6ac6a72fde269131f9bf8b20 ts=2026-10-07T20:10:22.2590000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[6549] _id=6acfdb93de269131f9d90a44 ts=2026-10-14T19:44:19.1310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 56 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[4020] _id=6ac6a61ede269131f9bf7a2f ts=2026-10-07T20:05:47.4120000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[4012] _id=6ac6a61ede269131f9bf7a33 ts=2026-10-07T20:05:47.4120000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[4024] _id=6ac6a620de269131f9bf7a74 ts=2026-10-07T20:05:50.7200000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 141 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[1001] _id=6ac550eade269131f9b7bbbc ts=2026-10-06T19:50:00.3040000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[1002] _id=6ac550eade269131f9b7bbbd ts=2026-10-06T19:50:00.3040000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[1004] _id=6ac550eade269131f9b7bbc0 ts=2026-10-06T19:50:00.3040000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[10800] _id=6ad284c8de269131f9e8029f ts=2026-10-16T20:10:47.3550000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[6484] _id=6acfdb40de269131f9d905c6 ts=2026-10-14T19:42:55.4920000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[6486] _id=6acfdb49de269131f9d9067e ts=2026-10-14T19:43:04.9790000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 295 start, 286 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'BecameCameraCentered' (totals: 415 open, 414 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 22 unmatched 'BecameVisible' (totals: 666 open, 644 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 7 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 40 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 382 of 10847 adjacent _id pairs reverse in client time; worst 97.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba2.jsonl[1151] _id=6ac55104de269131f9b7bd3e ts=2026-10-06T19:50:28.1640000Z`; `6ab9a9439a8420a1e6b56ba2.jsonl[1152] _id=6ac55104de269131f9b7bd3f ts=2026-10-06T19:48:50.3770000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.83s, min -515510.36s, max -0.41s over 10848 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba2\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `InputEvent` — 4737 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1809); Unit 4 Dev - Dungeon (899); Unit 3 Dev (711); Unit 3 Dungeon Dev (545); Unit 1 Dev (324); Unit 4 Dev (318); Unit 4 Dev - Anderson Base (131)
- **Intervals:** median 0.47s (p5 0.05s / p95 4.71s, n=4736)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4737/4737 records)
    "pressed"  x4737
data.actionType  (string, 4737/4737 records)
    "Move"  x3945
    "Interact"  x290
    "Sprint"  x218
    "Jump"  x180
    "Ascend"  x33
    "Hoverboard"  x33
    "Map"  x12
    "Descend"  x11
    "Pause"  x7
    "SkipCinematic"  x4
    "ToggleDebug"  x4
data.key  (string, 4737/4737 records, 17 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4737/4737 records)
    "Player"  x4210
    "Drone"  x527
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2139 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1513); Unit 4 Dev (376); Unit 3 Dungeon Dev (250)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.32s, n=2138)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2139/2139 records)
    "BecameVisible"  x666
    "BecameInvisible"  x644
    "BecameCameraCentered"  x415
    "BecameCameraUncentered"  x414
data.pieceId  (string, 2139/2139 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2139/2139 records)
    1375 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1637 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (618); Unit 3 Dev (312); Unit 1 Dev (247); Unit 4 Dev - Anderson Base (150); Unit 3 Dungeon Dev (116); Unit 4 Dev - Dungeon (99); Unit 4 Dev (95)
- **eventKey:** present on 1056 of 1637 records
- **Intervals:** median 3.82s (p5 0.00s / p95 25.63s, n=1636)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1056; [conversationId, dialogueEventType] x581
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1637/1637 records)
    numeric range 8 .. 111 (42 unique)
data.dialogueEventType  (string, 1637/1637 records)
    "DialogueNodeEvent"  x1056
    "DialogueStartEvent"  x295
    "DialogueFinishEvent"  x286
data.nodeId  (number, 1056/1637 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1248 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (508); Unit 3 Dev (211); Unit 1 Dev (188); Unit 4 Dev - Dungeon (92); Unit 4 Dev (91); Unit 4 Dev - Anderson Base (88); Unit 3 Dungeon Dev (70)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.37s, n=1239)
- **Fields under `data`:**

```text
data.position  (object, 1248/1248 records)
data.position.x  (number, 1248/1248 records)
    numeric range -699.017 .. 1746.68 (406 unique)
data.position.y  (number, 1248/1248 records)
    numeric range -114.377 .. 159.178 (340 unique)
data.position.z  (number, 1248/1248 records)
    numeric range -1070.96 .. 2280.41 (406 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Soil Key Puzzle` — 315 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (195); Unit 3 Dev (102); Unit 4 Dev (18)
- **Intervals:** median 0.30s (p5 0.01s / p95 6.87s, n=314)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x307; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/315 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/315 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 307/315 records)
    "RightDrag"  x155
    "LeftDrag"  x152
data.currentSoilType  (string, 307/315 records)
    "SAND"  x64
    "SANDGRAVEL"  x63
    "CLAYSAND"  x55
    "CLAY"  x41
    "CLAYROCK"  x36
    "GRAVEL"  x32
    "BEDROCK"  x16
data.isCorrectSelection  (string, 307/315 records)
    "false"  x244
    "true"  x63
data.waterLevelStatus  (string, 307/315 records)
    "Proper"  x206
    "TooLow"  x68
    "TooHigh"  x33
data.waterRetentionChange  (string, 307/315 records)
    "Decrease"  x132
    "Increase"  x112
    "NoChange"  x63
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 291 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (117); Unit 3 Dev (79); Unit 2 Prod (Refactor) (51); Unit 1 Dev (44)
- **Intervals:** median 0.76s (p5 0.03s / p95 10.20s, n=290)
- **Fields under `data`:**

```text
data.actionType  (string, 291/291 records)
    "argumentationNodeHoverEnd"  x123
    "argumentationNodeHoverStart"  x123
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x13
data.argumentationTitle  (string, 291/291 records)
    "Unit 4 - Flooding"  x117
    "Unit 3 - Pollution Upstream"  x79
    "Unit 2 – Watershed"  x51
    "Unit 1 - Freshwater"  x23
    "Unit 1 - Argumentation Tutorial"  x21
data.nodeName  (string, 291/291 records)
    "A"  x51
    "1"  x39
    "2"  x38
    "B"  x34
    "I"  x33
    "II"  x25
    "D"  x19
    "C"  x17
    "3"  x14
    "4"  x14
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 197 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (69); Unit 2 Prod (Refactor) (42); Unit 3 Dungeon Dev (29); Unit 4 Dev - Anderson Base (20); Unit 1 Dev (16); Unit 3 Dev (11); Unit 4 Dev (10)
- **Intervals:** median 11.52s (p5 1.36s / p95 300.18s, n=196)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 197/197 records)
    33 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 197/197 records)
    90 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 81 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (48); Unit 3 Dev (33)
- **Intervals:** median 8.85s (p5 0.03s / p95 686.31s, n=80)
- **`data` key-set variants:** [actionType, featureUsed] x64; [actionType, featureUsed, location] x17
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 81/81 records)
    "MapCloseEvent"  x32
    "MapOpenEvent"  x32
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x7
    "WaypointResetEvent"  x3
data.featureUsed  (string, 81/81 records)
    "Map"  x64
    "Waypoint"  x17
data.location  (object, 17/81 records)
data.location.x  (number, 17/81 records)
    numeric range -313.788 .. 164.221 (14 unique)
data.location.y  (number, 17/81 records)
    numeric range -281.611 .. 218.892 (14 unique)
data.location.z  (number, 17/81 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 66 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (18); Unit 3 Dev (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 66 of 66 records
- **Intervals:** median 171.96s (p5 0.01s / p95 84327.38s, n=65)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Fields under `data`:**

```text
data.questEventType  (string, 66/66 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x26
data.questID  (string, 66/66 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 66/66 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/66 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 33 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (14); Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 1 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 4 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 218.66s (p5 8.49s / p95 86367.82s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "DebugMenuStateChanged"  x33
data.isOpened  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 23 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); PodsEscapingCopernicus Cutscene (1); Unit 1 Dev (1)
- **Intervals:** median 750.90s (p5 42.14s / p95 86586.97s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 19 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (8); Unit 3 Dev (6); Unit 2 Prod (Refactor) (3); Unit 1 Dev (2)
- **Intervals:** median 23.98s (p5 4.05s / p95 225604.35s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "submitAnswerEvent"  x19
data.answerSubmitted  (string, 19/19 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 19/19 records)
    "Unit 4 - Flooding"  x8
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 2050.32s (p5 65.43s / p95 236810.57s, n=14)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 89.19s (p5 0.04s / p95 328427.15s, n=12)
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

### `gameWindowUnfocusEvent` — 10 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Transition (1); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1025.65s (p5 130.92s / p95 431029.50s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    false  x10
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 10.17s (p5 3.40s / p95 414239.77s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x7
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 7 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (7)
- **Intervals:** median 19.63s (p5 3.31s / p95 115.97s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "ChangeCanister"  x7
data.canisterType  (string, 7/7 records)
    "Clay"  x3
    "Gravel"  x2
    "Bedrock"  x1
    "Sand"  x1
data.floor  (string, 7/7 records)
    "4"  x4
    "5"  x3
data.machine  (string, 7/7 records)
    "1"  x6
    "2"  x1
data.row  (string, 7/7 records)
    "TopRow"  x6
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 3.13s (p5 1.30s / p95 3.54s, n=3)
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
- **Intervals:** median 388408.32s (p5 195692.53s / p95 581124.11s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 1.74s (p5 1.74s / p95 1.74s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[10-218, 11-224, 11-226, 11-23, 11-24]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (195 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointResetEvent" (3x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (13x)
- `soilMachine` data.canisterType: "Bedrock" (1x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*