# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56b9e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56b9e
- **Game version string(s) in log:** 2.8.9, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56b9e.jsonl
- **Records:** 10455 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56b9e
- **Time span:** 2026-10-05T20:04:15.510000+00:00 .. 2026-10-16T20:11:21.938000+00:00 (264h 7m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56b9e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 10455 records, 8 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 91 INFO, 2 NOT_TESTED, 80 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3187 | 30.48 | 1 | 6 | 0 | 2026-10-05T20:04:31.274000+00:00 | 2026-10-16T20:11:19.397000+00:00 | 264h 6m |
| PuzzlePieceVisibleEvent | 2908 | 27.81 | 1 | 3 | 0 | 2026-10-06T19:56:17.980000+00:00 | 2026-10-16T20:11:15.836000+00:00 | 240h 14m |
| DialogueEvent | 1861 | 17.8 | 1 | 6 | 1157 | 2026-10-05T20:04:48.065000+00:00 | 2026-10-16T20:11:09.099000+00:00 | 264h 6m |
| PlayerPositionEvent | 1602 | 15.32 | 1 | 6 | 0 | 2026-10-05T20:04:27.688000+00:00 | 2026-10-16T20:11:21.938000+00:00 | 264h 6m |
| ObjectInterEvent | 309 | 2.96 | 1 | 6 | 0 | 2026-10-05T20:10:16.051000+00:00 | 2026-10-16T20:07:49.144000+00:00 | 263h 57m |
| argumentationNodeEvent | 195 | 1.87 | 1 | 3 | 0 | 2026-10-06T19:43:41.254000+00:00 | 2026-10-14T19:50:23.600000+00:00 | 192h 6m |
| Soil Key Puzzle | 101 | 0.97 | 1 | 3 | 0 | 2026-10-06T19:56:04.564000+00:00 | 2026-10-15T19:54:00.726000+00:00 | 215h 57m |
| TopographicMapEvent | 78 | 0.75 | 1 | 3 | 0 | 2026-10-06T19:57:43.905000+00:00 | 2026-10-16T18:02:19.341000+00:00 | 238h 4m |
| questEvent | 69 | 0.66 | 1 | 6 | 69 | 2026-10-05T20:04:48.045000+00:00 | 2026-10-16T20:11:06.265000+00:00 | 264h 6m |
| DEBUGMenu | 31 | 0.3 | 1 | 7 | 0 | 2026-10-05T20:04:27.672000+00:00 | 2026-10-16T20:07:38.858000+00:00 | 264h 3m |
| soilMachine | 20 | 0.19 | 1 | 1 | 0 | 2026-10-15T20:07:21.631000+00:00 | 2026-10-16T18:11:55.829000+00:00 | 22h 4m |
| gameWindowFocusEvent | 19 | 0.18 | 1 | 5 | 0 | 2026-10-05T20:04:15.510000+00:00 | 2026-10-16T20:07:29.006000+00:00 | 264h 3m |
| argumentationToolEvent | 18 | 0.17 | 1 | 3 | 0 | 2026-10-06T19:44:07.366000+00:00 | 2026-10-14T19:49:01.817000+00:00 | 192h 4m |
| argumentationAnswerEvent | 14 | 0.13 | 1 | 3 | 0 | 2026-10-06T19:44:23.323000+00:00 | 2026-10-14T19:50:27.178000+00:00 | 192h 6m |
| gameStartEvent | 14 | 0.13 | 1 | 1 | 0 | 2026-10-05T20:04:15.511000+00:00 | 2026-10-16T20:07:29.007000+00:00 | 264h 3m |
| argumentationEvent | 9 | 0.09 | 1 | 3 | 0 | 2026-10-06T19:44:07.507000+00:00 | 2026-10-14T19:50:27.226000+00:00 | 192h 6m |
| DaniEvent | 8 | 0.08 | 1 | 2 | 0 | 2026-10-14T19:42:03.542000+00:00 | 2026-10-16T16:10:25.887000+00:00 | 44h 28m |
| gameWindowUnfocusEvent | 8 | 0.08 | 1 | 6 | 0 | 2026-10-05T20:11:23.959000+00:00 | 2026-10-16T18:20:43.277000+00:00 | 262h 9m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-06T19:50:25.545000+00:00 | 2026-10-15T19:48:03.059000+00:00 | 215h 57m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 388728.757s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.067s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.601s median 
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
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.644s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.11s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 72744.637s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 7299.636s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86513.429s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 8.663s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,I; A,3,I; A,4,I; B,1,I; C,1,I; C,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding; Unit 5 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[3] _id=6ac402c0de269131f9af8ddd ts=2026-10-05T20:04:15.5110000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[125] _id=6ac54b91de269131f9b79f03 ts=2026-10-06T19:27:13.0100000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[587] _id=6ac55174de269131f9b7c535 ts=2026-10-06T19:52:20.6520000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[2] _id=6ac402c0de269131f9af8ddb ts=2026-10-05T20:04:15.5100000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[124] _id=6ac54b91de269131f9b79f02 ts=2026-10-06T19:27:13.0100000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[586] _id=6ac55174de269131f9b7c534 ts=2026-10-06T19:52:20.6520000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[129] _id=6ac54b91de269131f9b79eff ts=2026-10-05T20:11:23.959Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[3295] _id=6ac7f149de269131f9c6acbb ts=2026-10-07T20:09:48.621Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[4405] _id=6ace8a31de269131f9d21822 ts=2026-10-13T19:44:48.1110000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3186 | 0.0 | 0.799 | 298.433 | 14.958 | 430248.303 | 0.2 | 102 | 11 |
| PuzzlePieceVisibleEvent | 2907 | 0.0 | 0.067 | 297.522 | 1.906 | 519019.965 | 0.2 | 1264 | 8 |
| DialogueEvent | 1860 | 0.0 | 3.965 | 511.173 | 29.195 | 430317.046 | 0.12 | 511 | 10 |
| PlayerPositionEvent | 1592 | 0.0 | 10.001 | 537.075 | 10.14 | 430234.031 | 0.11 | 2 | 8 |
| ObjectInterEvent | 308 | 0.004 | 9.204 | 3085.237 | 326.299 | 431067.052 | 0.02 | 2 | 12 |
| argumentationNodeEvent | 194 | 0.024 | 0.481 | 3564.961 | 9.826 | 605754.447 | 0.02 | 19 | 2 |
| Soil Key Puzzle | 100 | 0.001 | 1.601 | 7774.762 | 5255.281 | 432919.017 | 0.01 | 7 | 6 |
| TopographicMapEvent | 77 | 0.006 | 1.993 | 11130.85 | 75965.104 | 516631.525 | 0.01 | 3 | 8 |
| questEvent | 68 | 0.001 | 184.771 | 13982.033 | 83957.892 | 431200.476 | 0.0 | 10 | 15 |
| DEBUGMenu | 30 | 7.02 | 695.207 | 31686.373 | 86023.451 | 432081.297 | 0.0 | 0 | 16 |
| soilMachine | 19 | 0.936 | 8.663 | 4182.853 | 13526.075 | 71910.811 | 0.01 | 0 | 2 |
| gameWindowFocusEvent | 18 | 39.64 | 7299.636 | 52810.75 | 138267.315 | 432095.38 | 0.0 | 0 | 13 |
| argumentationToolEvent | 17 | 0.496 | 7.11 | 40676.144 | 189595.119 | 605776.006 | 0.0 | 0 | 2 |
| argumentationAnswerEvent | 13 | 2.23 | 15.644 | 53197.22 | 293628.788 | 605821.866 | 0.0 | 0 | 2 |
| gameStartEvent | 13 | 1307.034 | 72744.637 | 73122.577 | 224687.334 | 432095.38 | 0.0 | 0 | 13 |
| argumentationEvent | 8 | 0.033 | 78.403 | 86447.465 | 423648.022 | 605755.097 | 0.0 | 1 | 2 |
| DaniEvent | 7 | 0.572 | 4.923 | 22871.764 | 111750.378 | 159310.203 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 7 | 81.731 | 86513.429 | 134822.76 | 413641.042 | 516899.49 | 0.0 | 0 | 5 |
| EndOfUnit | 2 | 171504.818 | 388728.757 | 388728.757 | 584230.302 | 605952.696 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 9 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[1886] _id=6ac69fccde269131f9bf2392 ts=2026-10-07T19:38:49.5680000Z == 6ab9a9439a8420a1e6b56b9e.jsonl[1887] _id=6ac69fccde269131f9bf2393 ts=2026-10-07T19:38:49.5680000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[7731] _id=6ad128f0de269131f9e05abe ts=2026-10-15T19:26:37.6630000Z == 6ab9a9439a8420a1e6b56b9e.jsonl[7732] _id=6ad128f0de269131f9e05abf ts=2026-10-15T19:26:37.6630000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[10139] _id=6ad26924de269131f9e6fa16 ts=2026-10-16T18:12:52.3530000Z == 6ab9a9439a8420a1e6b56b9e.jsonl[10140] _id=6ad26924de269131f9e6fa17 ts=2026-10-16T18:12:52.3530000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 21 group(s), 35 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[669] _id=6ac55263de269131f9b7d727 ts=2026-10-06T19:56:18.2470000Z == 6ab9a9439a8420a1e6b56b9e.jsonl[670] _id=6ac55263de269131f9b7d72d ts=2026-10-06T19:56:18.2470000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[3482] _id=6ac7f2acde269131f9c6c7ca ts=2026-10-08T19:44:42.4510000Z == 6ab9a9439a8420a1e6b56b9e.jsonl[3484] _id=6ac7f2acde269131f9c6c7ce ts=2026-10-08T19:44:42.4510000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[3496] _id=6ac7f2e6de269131f9c6cb00 ts=2026-10-08T19:45:41.4310000Z == 6ab9a9439a8420a1e6b56b9e.jsonl[3501] _id=6ac7f2e6de269131f9c6cb02 ts=2026-10-08T19:45:41.4310000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9439a8420a1e6b56b9e.jsonl[106] _id=6ac40428de269131f9af95e9 ts=2026-10-05T20:10:16.0510000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[108] _id=6ac40428de269131f9af95eb ts=2026-10-05T20:10:16.0550000Z`; `5ms: 6ab9a9439a8420a1e6b56b9e.jsonl[140] _id=6ac54bc3de269131f9b79fd7 ts=2026-10-06T19:28:03.4030000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[144] _id=6ac54bc3de269131f9b79fd9 ts=2026-10-06T19:28:03.4080000Z`; `784ms: 6ab9a9439a8420a1e6b56b9e.jsonl[2336] _id=6ac6a144de269131f9bf37ac ts=2026-10-07T19:45:07.6890000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[2346] _id=6ac6a145de269131f9bf37bd ts=2026-10-07T19:45:08.4730000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `322ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3333] _id=6ac7f1e9de269131f9c6b929 ts=2026-10-08T19:41:28.8750000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[3340] _id=6ac7f1eade269131f9c6b93c ts=2026-10-08T19:41:29.1970000Z`; `168ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3334] _id=6ac7f1e9de269131f9c6b934 ts=2026-10-08T19:41:29.1870000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[3335] _id=6ac7f1eade269131f9c6b943 ts=2026-10-08T19:41:29.3550000Z`; `159ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3340] _id=6ac7f1eade269131f9c6b93c ts=2026-10-08T19:41:29.1970000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[3336] _id=6ac7f1eade269131f9c6b944 ts=2026-10-08T19:41:29.3560000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `387ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9669] _id=6ad266a4de269131f9e6f32a ts=2026-10-16T18:02:12.4320000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[9673] _id=6ad266a5de269131f9e6f333 ts=2026-10-16T18:02:12.8190000Z`; `409ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9651] _id=6ad266a4de269131f9e6f32d ts=2026-10-16T18:02:12.5960000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[9676] _id=6ad266a5de269131f9e6f336 ts=2026-10-16T18:02:13.0050000Z`; `414ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9673] _id=6ad266a5de269131f9e6f333 ts=2026-10-16T18:02:12.8190000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[9682] _id=6ad266a5de269131f9e6f33d ts=2026-10-16T18:02:13.2330000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `33ms: 6ab9a9439a8420a1e6b56b9e.jsonl[6156] _id=6acfdd04de269131f9d91cda ts=2026-10-14T19:50:27.1930000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[6159] _id=6acfdd04de269131f9d91cdd ts=2026-10-14T19:50:27.2260000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `917ms: 6ab9a9439a8420a1e6b56b9e.jsonl[341] _id=6ac54f6dde269131f9b7b156 ts=2026-10-06T19:43:41.2540000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[355] _id=6ac54f6ede269131f9b7b15c ts=2026-10-06T19:43:42.1710000Z`; `438ms: 6ab9a9439a8420a1e6b56b9e.jsonl[355] _id=6ac54f6ede269131f9b7b15c ts=2026-10-06T19:43:42.1710000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[342] _id=6ac54f6ede269131f9b7b160 ts=2026-10-06T19:43:42.6090000Z`; `678ms: 6ab9a9439a8420a1e6b56b9e.jsonl[397] _id=6ac54f8dde269131f9b7b22c ts=2026-10-06T19:44:13.6140000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[395] _id=6ac54f8ede269131f9b7b234 ts=2026-10-06T19:44:14.2920000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `496ms: 6ab9a9439a8420a1e6b56b9e.jsonl[4813] _id=6ace8e80de269131f9d2458c ts=2026-10-13T20:03:11.4240000Z ~ 6ab9a9439a8420a1e6b56b9e.jsonl[4823] _id=6ace8e80de269131f9d24592 ts=2026-10-13T20:03:11.9200000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a9439a8420a1e6b56b9e.jsonl[3299] _id=6ac7f157de269131f9c6ad9d ts=2026-10-08T19:39:02.6680000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4364] _id=6ace8929de269131f9d20f5f ts=2026-10-13T19:40:23.9650000Z; 24h 0m: 6ab9a9439a8420a1e6b56b9e.jsonl[1883] _id=6ac69fc8de269131f9bf2376 ts=2026-10-07T19:38:47.0940000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3296] _id=6ac7f14ade269131f9c6acc3 ts=2026-10-08T19:38:48.7470000Z; 23h 46m: 6ab9a9439a8420a1e6b56b9e.jsonl[584] _id=6ac55180de269131f9b7c62e ts=2026-10-06T19:52:32.2170000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1882] _id=6ac69fbade269131f9bf232e ts=2026-10-07T19:38:33.4220000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 44h 15m 
  - Evidence: 44h 15m: 6ab9a9439a8420a1e6b56b9e.jsonl[6399] _id=6acfde1ede269131f9d93171 ts=2026-10-14T19:55:09.1110000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9536] _id=6ad24c6cde269131f9e5a47b ts=2026-10-16T16:10:19.3140000Z; 12m 57s: 6ab9a9439a8420a1e6b56b9e.jsonl[5637] _id=6acfdb11de269131f9d90268 ts=2026-10-14T19:42:08.7570000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6398] _id=6acfde1bde269131f9d9314b ts=2026-10-14T19:55:06.2100000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a9439a8420a1e6b56b9e.jsonl[4346] _id=6ac7f868de269131f9c74177 ts=2026-10-08T20:09:11.3910000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4359] _id=6ace8955de269131f9d210c8 ts=2026-10-13T19:41:08.4370000Z; 23h 32m: 6ab9a9439a8420a1e6b56b9e.jsonl[3230] _id=6ac6a660de269131f9bf80d8 ts=2026-10-07T20:06:55.8990000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3292] _id=6ac7f15ade269131f9c6adcf ts=2026-10-08T19:39:04.9700000Z; 23h 30m: 6ab9a9439a8420a1e6b56b9e.jsonl[1868] _id=6ac555acde269131f9b8507c ts=2026-10-06T20:10:20.0400000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1928] _id=6ac6a05ade269131f9bf277e ts=2026-10-07T19:41:13.4500000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 511 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[431] _id=6ac54fe4de269131f9b7b496 ts=2026-10-06T19:45:39.9640000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[432] _id=6ac54fe4de269131f9b7b497 ts=2026-10-06T19:45:39.9640000Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[4842] _id=6ace8e90de269131f9d24616 ts=2026-10-13T20:03:27.9100000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4843] _id=6ace8e90de269131f9d24617 ts=2026-10-13T20:03:27.9100000Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[4899] _id=6ace8ed2de269131f9d2493b ts=2026-10-13T20:04:33.0970000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4900] _id=6ace8ed2de269131f9d2493c ts=2026-10-13T20:04:33.0970000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 19m 
  - Evidence: 168h 19m: 6ab9a9439a8420a1e6b56b9e.jsonl[583] _id=6ac55101de269131f9b7bcf2 ts=2026-10-06T19:50:25.5450000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4993] _id=6ace9003de269131f9d25330 ts=2026-10-13T20:09:38.2410000Z; 47h 38m: 6ab9a9439a8420a1e6b56b9e.jsonl[4993] _id=6ace9003de269131f9d25330 ts=2026-10-13T20:09:38.2410000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[8483] _id=6ad12df3de269131f9e0c265 ts=2026-10-15T19:48:03.0590000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a9439a8420a1e6b56b9e.jsonl[4357] _id=6ac7f892de269131f9c74404 ts=2026-10-08T20:09:54.2220000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4369] _id=6ace893cde269131f9d21015 ts=2026-10-13T19:40:42.5250000Z; 23h 32m: 6ab9a9439a8420a1e6b56b9e.jsonl[1809] _id=6ac554d8de269131f9b8369b ts=2026-10-06T20:06:48.0790000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1885] _id=6ac69fccde269131f9bf2391 ts=2026-10-07T19:38:49.5660000Z; 23h 29m: 6ab9a9439a8420a1e6b56b9e.jsonl[3279] _id=6ac6a6f7de269131f9bf8a8e ts=2026-10-07T20:09:26.2060000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3304] _id=6ac7f167de269131f9c6aec5 ts=2026-10-08T19:39:18.7660000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 102 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[10139] _id=6ad26924de269131f9e6fa16 ts=2026-10-16T18:12:52.3530000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[10140] _id=6ad26924de269131f9e6fa17 ts=2026-10-16T18:12:52.3530000Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[10350] _id=6ad2840ede269131f9e7fcad ts=2026-10-16T20:07:40.4080000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[10351] _id=6ad2840ede269131f9e7fcae ts=2026-10-16T20:07:40.4080000Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[10351] _id=6ad2840ede269131f9e7fcae ts=2026-10-16T20:07:40.4080000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[10352] _id=6ad2840ede269131f9e7fcaf ts=2026-10-16T20:07:40.4080000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a9439a8420a1e6b56b9e.jsonl[4344] _id=6ac7f868de269131f9c74172 ts=2026-10-08T20:09:11.3690000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4495] _id=6ace8c43de269131f9d23256 ts=2026-10-13T19:53:38.4210000Z; 23h 52m: 6ab9a9439a8420a1e6b56b9e.jsonl[2931] _id=6ac6a1fade269131f9bf44f3 ts=2026-10-07T19:48:09.7120000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3324] _id=6ac7f1aade269131f9c6b385 ts=2026-10-08T19:40:25.5470000Z; 23h 37m: 6ab9a9439a8420a1e6b56b9e.jsonl[1773] _id=6ac55448de269131f9b82336 ts=2026-10-06T20:04:24.4760000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1939] _id=6ac6a07ede269131f9bf2859 ts=2026-10-07T19:41:49.9680000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a9439a8420a1e6b56b9e.jsonl[106] _id=6ac40428de269131f9af95e9 ts=2026-10-05T20:10:16.0510000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[108] _id=6ac40428de269131f9af95eb ts=2026-10-05T20:10:16.0550000Z; 5ms: 6ab9a9439a8420a1e6b56b9e.jsonl[140] _id=6ac54bc3de269131f9b79fd7 ts=2026-10-06T19:28:03.4030000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[144] _id=6ac54bc3de269131f9b79fd9 ts=2026-10-06T19:28:03.4080000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a9439a8420a1e6b56b9e.jsonl[4362] _id=6ace8928de269131f9d20f53 ts=2026-10-08T20:10:03.444Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4368] _id=6ace893cde269131f9d21014 ts=2026-10-13T19:40:37.4750000Z; 23h 29m: 6ab9a9439a8420a1e6b56b9e.jsonl[3287] _id=6ac6a70bde269131f9bf8ac8 ts=2026-10-07T20:09:46.3730000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3291] _id=6ac7f15ade269131f9c6adce ts=2026-10-08T19:39:02.6940000Z; 23h 28m: 6ab9a9439a8420a1e6b56b9e.jsonl[1870] _id=6ac555bdde269131f9b851bf ts=2026-10-06T20:10:36.8180000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1884] _id=6ac69fccde269131f9bf2390 ts=2026-10-07T19:38:47.1080000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[4358] _id=6ac7f89cde269131f9c74495 ts=2026-10-08T20:10:03.4440000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4362] _id=6ace8928de269131f9d20f53 ts=2026-10-08T20:10:03.444Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9308] _id=6ad13352de269131f9e11ff5 ts=2026-10-15T20:10:57.8840000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9313] _id=6ad24a29de269131f9e57d7d ts=2026-10-15T20:10:57.884Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 144h 10m 
  - Evidence: 144h 10m: 6ab9a9439a8420a1e6b56b9e.jsonl[3946] _id=6ac7f3edde269131f9c6e0f6 ts=2026-10-08T19:50:02.5880000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6636] _id=6acfdf58de269131f9d9432f ts=2026-10-14T20:00:22.5530000Z; 23h 56m: 6ab9a9439a8420a1e6b56b9e.jsonl[2901] _id=6ac6a1ccde269131f9bf424e ts=2026-10-07T19:47:21.3890000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3427] _id=6ac7f25cde269131f9c6c2d3 ts=2026-10-08T19:43:22.5750000Z; 23h 39m: 6ab9a9439a8420a1e6b56b9e.jsonl[1751] _id=6ac5540ade269131f9b8189a ts=2026-10-06T20:03:20.7920000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[2012] _id=6ac6a0fede269131f9bf30b7 ts=2026-10-07T19:42:38.6320000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1264 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[10098] _id=6ad26935de269131f9e6fa45 ts=2026-10-16T18:13:06.4400000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[10159] _id=6ad26935de269131f9e6fa47 ts=2026-10-16T18:13:06.4400000Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[10099] _id=6ad26936de269131f9e6fa49 ts=2026-10-16T18:13:06.4400000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[10100] _id=6ad26936de269131f9e6fa4a ts=2026-10-16T18:13:06.4400000Z; 0ms: 6ab9a9439a8420a1e6b56b9e.jsonl[10100] _id=6ad26936de269131f9e6fa4a ts=2026-10-16T18:13:06.4400000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[10167] _id=6ad26937de269131f9e6fa4c ts=2026-10-16T18:13:06.4400000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 15m 
  - Evidence: 120h 15m: 6ab9a9439a8420a1e6b56b9e.jsonl[3438] _id=6ac7f273de269131f9c6c430 ts=2026-10-08T19:43:47.0140000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4725] _id=6ace8d8ade269131f9d23ef9 ts=2026-10-13T19:59:06.0310000Z; 24h 0m: 6ab9a9439a8420a1e6b56b9e.jsonl[4726] _id=6ace8d8cde269131f9d23f01 ts=2026-10-13T19:59:07.5190000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6478] _id=6acfdf16de269131f9d93fc5 ts=2026-10-14T19:59:16.9860000Z; 23h 51m: 6ab9a9439a8420a1e6b56b9e.jsonl[6613] _id=6acfdf30de269131f9d94142 ts=2026-10-14T19:59:43.0960000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[8517] _id=6ad12ec2de269131f9e0ce26 ts=2026-10-15T19:51:30.0110000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3335] _id=6ac7f1eade269131f9c6b943 ts=2026-10-08T19:41:29.3550000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3336] _id=6ac7f1eade269131f9c6b944 ts=2026-10-08T19:41:29.3560000Z; 1ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3337] _id=6ac7f1eade269131f9c6b950 ts=2026-10-08T19:41:29.5300000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3345] _id=6ac7f1eade269131f9c6b951 ts=2026-10-08T19:41:29.5310000Z; 1ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3341] _id=6ac7f1eade269131f9c6b958 ts=2026-10-08T19:41:29.8520000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3342] _id=6ac7f1eade269131f9c6b959 ts=2026-10-08T19:41:29.8530000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a9439a8420a1e6b56b9e.jsonl[4158] _id=6ac7f67dde269131f9c715ce ts=2026-10-08T20:01:01.2080000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[5072] _id=6acfd895de269131f9d8c8fe ts=2026-10-14T19:31:32.7330000Z; 24h 6m: 6ab9a9439a8420a1e6b56b9e.jsonl[5149] _id=6acfd938de269131f9d8d962 ts=2026-10-14T19:34:15.0670000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[8315] _id=6ad12c2ede269131f9e0a854 ts=2026-10-15T19:40:29.7980000Z; 23h 44m: 6ab9a9439a8420a1e6b56b9e.jsonl[749] _id=6ac552cede269131f9b7e439 ts=2026-10-06T19:58:05.8200000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1971] _id=6ac6a0c3de269131f9bf2c85 ts=2026-10-07T19:42:58.3170000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.006s..0.029s shown 
  - Evidence: 6ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9674] _id=6ad266a5de269131f9e6f334 ts=2026-10-16T18:02:12.9990000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9676] _id=6ad266a5de269131f9e6f336 ts=2026-10-16T18:02:13.0050000Z; 22ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3081] _id=6ac6a433de269131f9bf5b6b ts=2026-10-07T19:57:38.8600000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3088] _id=6ac6a433de269131f9bf5b6f ts=2026-10-07T19:57:38.8820000Z; 29ms: 6ab9a9439a8420a1e6b56b9e.jsonl[3083] _id=6ac6a433de269131f9bf5b69 ts=2026-10-07T19:57:38.8310000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3081] _id=6ac6a433de269131f9bf5b6b ts=2026-10-07T19:57:38.8600000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 17m 
  - Evidence: 168h 17m: 6ab9a9439a8420a1e6b56b9e.jsonl[480] _id=6ac55012de269131f9b7b60a ts=2026-10-06T19:46:26.0050000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4848] _id=6ace8e90de269131f9d24614 ts=2026-10-13T20:03:27.8710000Z; 23h 45m: 6ab9a9439a8420a1e6b56b9e.jsonl[4911] _id=6ace8ee3de269131f9d249d7 ts=2026-10-13T20:04:50.8660000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6104] _id=6acfdce0de269131f9d91af5 ts=2026-10-14T19:49:50.9360000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 15m 
  - Evidence: 168h 15m: 6ab9a9439a8420a1e6b56b9e.jsonl[481] _id=6ac55012de269131f9b7b60b ts=2026-10-06T19:46:26.0230000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4801] _id=6ace8e4ede269131f9d243c0 ts=2026-10-13T20:02:21.1200000Z; 23h 44m: 6ab9a9439a8420a1e6b56b9e.jsonl[4915] _id=6ace8ee3de269131f9d249e1 ts=2026-10-13T20:04:50.9200000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6062] _id=6acfdcadde269131f9d916e9 ts=2026-10-14T19:49:00.0880000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.033s..0.033s shown 
  - Evidence: 33ms: 6ab9a9439a8420a1e6b56b9e.jsonl[6156] _id=6acfdd04de269131f9d91cda ts=2026-10-14T19:50:27.1930000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6159] _id=6acfdd04de269131f9d91cdd ts=2026-10-14T19:50:27.2260000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 15m 
  - Evidence: 168h 15m: 6ab9a9439a8420a1e6b56b9e.jsonl[476] _id=6ac5500bde269131f9b7b5d1 ts=2026-10-06T19:46:19.2640000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4796] _id=6ace8e46de269131f9d2437e ts=2026-10-13T20:02:13.7110000Z; 23h 44m: 6ab9a9439a8420a1e6b56b9e.jsonl[4909] _id=6ace8eddde269131f9d2499f ts=2026-10-13T20:04:45.0530000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6064] _id=6acfdcb6de269131f9d91783 ts=2026-10-14T19:49:09.5780000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.024s..0.026s shown 
  - Evidence: 24ms: 6ab9a9439a8420a1e6b56b9e.jsonl[6128] _id=6acfdcf1de269131f9d91c13 ts=2026-10-14T19:50:08.7190000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6129] _id=6acfdcf1de269131f9d91c15 ts=2026-10-14T19:50:08.7430000Z; 24ms: 6ab9a9439a8420a1e6b56b9e.jsonl[6135] _id=6acfdcf5de269131f9d91c31 ts=2026-10-14T19:50:12.1560000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6132] _id=6acfdcf5de269131f9d91c33 ts=2026-10-14T19:50:12.1800000Z; 26ms: 6ab9a9439a8420a1e6b56b9e.jsonl[6072] _id=6acfdcc3de269131f9d91894 ts=2026-10-14T19:49:22.8620000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6073] _id=6acfdcc4de269131f9d91896 ts=2026-10-14T19:49:22.8880000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 16m 
  - Evidence: 168h 16m: 6ab9a9439a8420a1e6b56b9e.jsonl[460] _id=6ac55002de269131f9b7b578 ts=2026-10-06T19:46:10.2700000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4546] _id=6ace8e53de269131f9d24406 ts=2026-10-13T20:02:26.2760000Z; 23h 45m: 6ab9a9439a8420a1e6b56b9e.jsonl[4823] _id=6ace8e80de269131f9d24592 ts=2026-10-13T20:03:11.9200000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[6061] _id=6acfdcaede269131f9d91700 ts=2026-10-14T19:49:01.8170000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a9439a8420a1e6b56b9e.jsonl[3298] _id=6ac7f14ade269131f9c6acc5 ts=2026-10-08T19:38:48.8960000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4366] _id=6ace8929de269131f9d20f61 ts=2026-10-13T19:40:24.2760000Z; 24h 0m: 6ab9a9439a8420a1e6b56b9e.jsonl[1881] _id=6ac69fbade269131f9bf2331 ts=2026-10-07T19:38:33.5920000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3298] _id=6ac7f14ade269131f9c6acc5 ts=2026-10-08T19:38:48.8960000Z; 23h 46m: 6ab9a9439a8420a1e6b56b9e.jsonl[587] _id=6ac55174de269131f9b7c535 ts=2026-10-06T19:52:20.6520000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1881] _id=6ac69fbade269131f9bf2331 ts=2026-10-07T19:38:33.5920000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a9439a8420a1e6b56b9e.jsonl[3297] _id=6ac7f14ade269131f9c6acc4 ts=2026-10-08T19:38:48.8960000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4365] _id=6ace8929de269131f9d20f60 ts=2026-10-13T19:40:24.2760000Z; 24h 0m: 6ab9a9439a8420a1e6b56b9e.jsonl[1880] _id=6ac69fbade269131f9bf2330 ts=2026-10-07T19:38:33.5920000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3297] _id=6ac7f14ade269131f9c6acc4 ts=2026-10-08T19:38:48.8960000Z; 23h 46m: 6ab9a9439a8420a1e6b56b9e.jsonl[586] _id=6ac55174de269131f9b7c534 ts=2026-10-06T19:52:20.6520000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1880] _id=6ac69fbade269131f9bf2330 ts=2026-10-07T19:38:33.5920000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 34m 
  - Evidence: 143h 34m: 6ab9a9439a8420a1e6b56b9e.jsonl[3295] _id=6ac7f149de269131f9c6acbb ts=2026-10-07T20:09:48.621Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4405] _id=6ace8a31de269131f9d21822 ts=2026-10-13T19:44:48.1110000Z; 47h 58m: 6ab9a9439a8420a1e6b56b9e.jsonl[129] _id=6ac54b91de269131f9b79eff ts=2026-10-05T20:11:23.959Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3295] _id=6ac7f149de269131f9c6acbb ts=2026-10-07T20:09:48.621Z; 44h 10m: 6ab9a9439a8420a1e6b56b9e.jsonl[4405] _id=6ace8a31de269131f9d21822 ts=2026-10-13T19:44:48.1110000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[7172] _id=6ad0f770de269131f9dcf09a ts=2026-10-15T15:55:27.8950000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a9439a8420a1e6b56b9e.jsonl[4025] _id=6ac7f4dade269131f9c6f0aa ts=2026-10-08T19:54:02.0900000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[4370] _id=6ace893cde269131f9d21016 ts=2026-10-13T19:40:42.5660000Z; 23h 42m: 6ab9a9439a8420a1e6b56b9e.jsonl[3072] _id=6ac6a406de269131f9bf5999 ts=2026-10-07T19:56:53.1130000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[3294] _id=6ac7f15ade269131f9c6add1 ts=2026-10-08T19:39:05.0470000Z; 23h 31m: 6ab9a9439a8420a1e6b56b9e.jsonl[1811] _id=6ac554e3de269131f9b837d5 ts=2026-10-06T20:06:59.4980000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[1893] _id=6ac69fccde269131f9bf2399 ts=2026-10-07T19:38:49.6000000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56b9e.jsonl[368] _id=6ac54f38de269131f9b7b003 ts=2026-10-06T19:42:47.7670000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[369] _id=6ac54f38de269131f9b7b004 ts=2026-10-06T19:42:47.7680000Z; 4ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9169] _id=6ad131c1de269131f9e105ef ts=2026-10-15T20:04:16.7850000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9167] _id=6ad131c1de269131f9e105f1 ts=2026-10-15T20:04:16.7890000Z; 4ms: 6ab9a9439a8420a1e6b56b9e.jsonl[9427] _id=6ad24b97de269131f9e595b7 ts=2026-10-16T16:06:47.1420000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9425] _id=6ad24b97de269131f9e595b9 ts=2026-10-16T16:06:47.1460000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 19h 58m 
  - Evidence: 19h 58m: 6ab9a9439a8420a1e6b56b9e.jsonl[9269] _id=6ad1327ade269131f9e1135d ts=2026-10-15T20:07:21.6310000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9388] _id=6ad24b61de269131f9e59299 ts=2026-10-16T16:05:52.4420000Z; 1h 57m: 6ab9a9439a8420a1e6b56b9e.jsonl[9466] _id=6ad24bd8de269131f9e59adf ts=2026-10-16T16:07:51.3510000Z -> 6ab9a9439a8420a1e6b56b9e.jsonl[9831] _id=6ad26756de269131f9e6f48e ts=2026-10-16T18:05:10.2330000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[496] _id=6ac55032de269131f9b7b6b6 ts=2026-10-06T19:46:57.6880000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[3909] _id=6ac7f3e3de269131f9c6e015 ts=2026-10-08T19:49:55.0050000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[4060] _id=6ac7f555de269131f9c6f811 ts=2026-10-08T19:56:04.6860000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[6159] _id=6acfdd04de269131f9d91cdd ts=2026-10-14T19:50:27.2260000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[9325] _id=6ad24a3cde269131f9e57f56 ts=2026-10-16T16:00:59.6130000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[9586] _id=6ad26690de269131f9e6f2a3 ts=2026-10-16T18:01:52.3040000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[7176] _id=6ad0f7c3de269131f9dcf551 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 34 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[3562] _id=6ac7f300de269131f9c6ccdf ts=2026-10-08T19:46:05.1060000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[3563] _id=6ac7f300de269131f9c6cce0 ts=2026-10-08T19:46:05.1060000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[3558] _id=6ac7f300de269131f9c6cce2 ts=2026-10-08T19:46:05.1060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 297 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[666] _id=6ac55262de269131f9b7d719 ts=2026-10-06T19:56:18.1690000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[2012] _id=6ac6a0fede269131f9bf30b7 ts=2026-10-07T19:42:38.6320000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[2013] _id=6ac6a0fede269131f9bf30bd ts=2026-10-07T19:42:38.6320000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[436] _id=6ac54fdede269131f9b7b44a ts=2026-10-06T19:45:34.1500000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[447] _id=6ac54fedde269131f9b7b4cf ts=2026-10-06T19:45:49.0690000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[467] _id=6ac55000de269131f9b7b569 ts=2026-10-06T19:46:08.6350000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 355 start, 349 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 24 unmatched 'BecameVisible' (totals: 912 open, 888 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 14 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 39 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 230 of 10453 adjacent _id pairs reverse in client time; worst 144.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56b9e.jsonl[777] _id=6ac552fbde269131f9b7f0e1 ts=2026-10-06T19:58:51.5550000Z`; `6ab9a9439a8420a1e6b56b9e.jsonl[782] _id=6ac552fcde269131f9b7f0fc ts=2026-10-06T19:56:27.3880000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.97s, min -430221.46s, max -0.12s over 10454 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56b9e\coverage.yaml

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

### `InputEvent` — 3187 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1142); Unit 2 Prod (Refactor) (682); Unit 4 Dev - Dungeon (624); Unit 3 Dungeon Dev (528); Unit 4 Dev (129); Unit 1 Dev (82)
- **Intervals:** median 0.80s (p5 0.09s / p95 14.96s, n=3186)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3187/3187 records)
    "pressed"  x3187
data.actionType  (string, 3187/3187 records)
    "Move"  x2178
    "Jump"  x368
    "Interact"  x338
    "Hoverboard"  x140
    "Ascend"  x87
    "Map"  x41
    "Sprint"  x29
    "Pause"  x4
    "SkipCinematic"  x2
data.key  (string, 3187/3187 records, 4 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3187/3187 records)
    "Player"  x2225
    "Drone"  x962
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2908 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2086); Unit 3 Dungeon Dev (438); Unit 4 Dev (384)
- **Intervals:** median 0.07s (p5 0.00s / p95 1.91s, n=2907)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2908/2908 records)
    "BecameVisible"  x912
    "BecameInvisible"  x888
    "BecameCameraCentered"  x554
    "BecameCameraUncentered"  x554
data.pieceId  (string, 2908/2908 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2908/2908 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1861 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (716); Unit 3 Dev (335); Unit 3 Dungeon Dev (325); Unit 1 Dev (211); Unit 4 Dev - Dungeon (172); Unit 4 Dev (102)
- **eventKey:** present on 1157 of 1861 records
- **Intervals:** median 3.96s (p5 0.01s / p95 29.20s, n=1860)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1157; [conversationId, dialogueEventType] x704
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1861/1861 records)
    numeric range 8 .. 111 (41 unique)
data.dialogueEventType  (string, 1861/1861 records)
    "DialogueNodeEvent"  x1157
    "DialogueStartEvent"  x355
    "DialogueFinishEvent"  x349
data.nodeId  (number, 1157/1861 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1602 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (625); Unit 3 Dev (256); Unit 3 Dungeon Dev (220); Unit 4 Dev - Dungeon (200); Unit 1 Dev (180); Unit 4 Dev (121)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.14s, n=1592)
- **Fields under `data`:**

```text
data.position  (object, 1602/1602 records)
data.position.x  (number, 1602/1602 records)
    numeric range -683.781 .. 1438.7 (568 unique)
data.position.y  (number, 1602/1602 records)
    numeric range -112.699 .. 178.782 (386 unique)
data.position.z  (number, 1602/1602 records)
    numeric range -1318.74 .. 2107.58 (569 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 309 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (116); Unit 3 Dungeon Dev (87); Unit 2 Prod (Refactor) (74); Unit 1 Dev (14); Unit 3 Dev (11); Unit 4 Dev (7)
- **Intervals:** median 9.20s (p5 1.54s / p95 326.30s, n=308)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 309/309 records)
    30 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 309/309 records)
    79 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 195 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (73); Unit 3 Dev (65); Unit 1 Dev (57)
- **Intervals:** median 0.48s (p5 0.03s / p95 9.83s, n=194)
- **Fields under `data`:**

```text
data.actionType  (string, 195/195 records)
    "argumentationNodeHoverEnd"  x84
    "argumentationNodeHoverStart"  x84
    "argumentationNodeAdd"  x19
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 195/195 records)
    "Unit 2 – Watershed"  x73
    "Unit 3 - Pollution Upstream"  x65
    "Unit 1 - Freshwater"  x31
    "Unit 1 - Argumentation Tutorial"  x26
data.nodeName  (string, 195/195 records)
    "I"  x49
    "A"  x35
    "1"  x27
    "2"  x18
    "B"  x16
    "C"  x16
    "II"  x11
    "4"  x10
    "3"  x8
    "5"  x3
    "D"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 101 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (81); Unit 4 Dev (12); Unit 3 Dev (8)
- **Intervals:** median 1.60s (p5 0.01s / p95 5255.28s, n=100)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x91; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/101 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/101 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 91/101 records)
    "LeftDrag"  x48
    "RightDrag"  x43
data.currentSoilType  (string, 91/101 records)
    "CLAY"  x19
    "CLAYROCK"  x18
    "CLAYSAND"  x17
    "SAND"  x13
    "BEDROCK"  x11
    "SANDGRAVEL"  x9
    "GRAVEL"  x4
data.isCorrectSelection  (string, 91/101 records)
    "false"  x77
    "true"  x14
data.waterLevelStatus  (string, 91/101 records)
    "TooHigh"  x56
    "Proper"  x22
    "TooLow"  x13
data.waterRetentionChange  (string, 91/101 records)
    "Increase"  x54
    "Decrease"  x23
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 78 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 4 Dev - Dungeon (37); Unit 2 Prod (Refactor) (24); Unit 3 Dev (17)
- **Intervals:** median 1.99s (p5 0.14s / p95 75965.10s, n=77)
- **`data` key-set variants:** [actionType, featureUsed] x64; [actionType, featureUsed, location] x14
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 78/78 records)
    "MapCloseEvent"  x32
    "MapOpenEvent"  x32
    "WaypointMoveEvent"  x6
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x2
data.featureUsed  (string, 78/78 records)
    "Map"  x64
    "Waypoint"  x14
data.location  (object, 14/78 records)
data.location.x  (number, 14/78 records)
    11 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 14/78 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 14/78 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 69 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (19); Unit 2 Prod (Refactor) (16); Unit 1 Dev (13); Unit 3 Dev (9); Unit 4 Dev (7); Unit 3 Dungeon Dev (5)
- **eventKey:** present on 69 of 69 records
- **Intervals:** median 184.77s (p5 0.01s / p95 83957.89s, n=68)
- **`data` key-set variants:** [questEventType, questID, questName] x39; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 69/69 records)
    "questActiveEvent"  x39
    "questFinishEvent"  x30
data.questID  (string, 69/69 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 69/69 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/69 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 31 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 3 Dungeon Dev (3); Unit 4 Dev (3); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2)
- **Intervals:** median 695.21s (p5 8.20s / p95 86023.45s, n=30)
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "DebugMenuStateChanged"  x31
data.isOpened  (bool, 31/31 records)
    false  x31
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 20 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (20)
- **Intervals:** median 8.66s (p5 1.28s / p95 13526.07s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "ChangeCanister"  x20
data.canisterType  (string, 20/20 records)
    "Gravel"  x7
    "Clay"  x5
    "Sand"  x5
    "Bedrock"  x3
data.floor  (string, 20/20 records)
    "4"  x13
    "5"  x4
    "3"  x3
data.machine  (string, 20/20 records)
    "1"  x18
    "2"  x2
data.row  (string, 20/20 records)
    "TopRow"  x19
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 19 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 3 Dungeon Dev (2); Transition (1); Unit 2 Prod (Refactor) (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 7299.64s (p5 77.49s / p95 138267.32s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationToolEvent` — 18 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 2 Prod (Refactor) (8); Unit 3 Dev (1)
- **Intervals:** median 7.11s (p5 1.41s / p95 189595.12s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationToolOpen"  x14
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 18/18 records)
    "Unit 2 – Watershed"  x8
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 18/18 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Waterfall Data"  x7
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationAnswerEvent` — 14 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 1 Dev (4)
- **Intervals:** median 15.64s (p5 3.27s / p95 293628.79s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "submitAnswerEvent"  x14
data.answerSubmitted  (string, 14/14 records)
    "A,1,II"  x3
    "A,1,I"  x2
    "A,4,I"  x2
    "1,I"  x1
    "A,2,I"  x1
    "A,3,I"  x1
    "A,5,I"  x1
    "B,1,I"  x1
    "C,1,I"  x1
    "C,1,II"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 72744.64s (p5 1427.40s / p95 224687.33s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 78.40s (p5 6.60s / p95 423648.02s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4); Unit 4 Dev - Dungeon (4)
- **Intervals:** median 4.92s (p5 0.72s / p95 111750.38s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 8 empty-string)
    ""  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 3 Dungeon Dev (2); Transition (1); Unit 1 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 86513.43s (p5 109.11s / p95 413641.04s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 388728.76s (p5 193227.21s / p95 584230.30s, n=2)
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
    "The root document of this element is not valid for pointer lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit3"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (81 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (6x); "WaypointResetEvent" (2x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (3x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*