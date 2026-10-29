# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b01

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b01
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b01.jsonl
- **Records:** 17924 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b01
- **Time span:** 2026-10-05T15:16:08.835000+00:00 .. 2026-10-16T15:47:59.966000+00:00 (264h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b01\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 17924 records, 9 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 89 INFO, 2 NOT_TESTED, 72 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 9625 | 53.7 | 1 | 7 | 0 | 2026-10-05T15:17:06.595000+00:00 | 2026-10-16T15:38:10.557000+00:00 | 264h 21m |
| PuzzlePieceVisibleEvent | 3580 | 19.97 | 1 | 3 | 0 | 2026-10-06T15:47:18.912000+00:00 | 2026-10-16T15:30:03.299000+00:00 | 239h 42m |
| DialogueEvent | 1843 | 10.28 | 1 | 7 | 1179 | 2026-10-05T15:17:08.005000+00:00 | 2026-10-16T15:47:48.165000+00:00 | 264h 30m |
| PlayerPositionEvent | 1585 | 8.84 | 1 | 7 | 0 | 2026-10-05T15:16:47.911000+00:00 | 2026-10-16T15:47:59.966000+00:00 | 264h 31m |
| argumentationNodeEvent | 558 | 3.11 | 1 | 4 | 0 | 2026-10-05T15:40:44.735000+00:00 | 2026-10-16T15:47:59.250000+00:00 | 264h 7m |
| ObjectInterEvent | 379 | 2.11 | 1 | 7 | 0 | 2026-10-05T15:22:37.474000+00:00 | 2026-10-16T15:38:14.017000+00:00 | 264h 15m |
| questEvent | 63 | 0.35 | 1 | 7 | 63 | 2026-10-05T15:17:07.977000+00:00 | 2026-10-16T15:34:59.114000+00:00 | 264h 17m |
| Soil Key Puzzle | 53 | 0.3 | 1 | 3 | 0 | 2026-10-07T15:29:46.352000+00:00 | 2026-10-16T15:04:03.090000+00:00 | 215h 34m |
| TopographicMapEvent | 53 | 0.3 | 1 | 3 | 0 | 2026-10-07T15:20:56.123000+00:00 | 2026-10-15T15:46:34.433000+00:00 | 192h 25m |
| argumentationAnswerEvent | 50 | 0.28 | 1 | 4 | 0 | 2026-10-05T15:40:59.765000+00:00 | 2026-10-16T15:47:33.021000+00:00 | 264h 6m |
| DEBUGMenu | 30 | 0.17 | 1 | 8 | 0 | 2026-10-05T15:16:47.890000+00:00 | 2026-10-16T15:34:57.740000+00:00 | 264h 18m |
| gameWindowFocusEvent | 24 | 0.13 | 1 | 5 | 0 | 2026-10-05T15:16:08.835000+00:00 | 2026-10-16T15:42:31.938000+00:00 | 264h 26m |
| soilMachine | 20 | 0.11 | 1 | 1 | 0 | 2026-10-16T15:16:59.769000+00:00 | 2026-10-16T15:26:17.205000+00:00 | 9m 17s |
| gameStartEvent | 16 | 0.09 | 1 | 1 | 0 | 2026-10-05T15:16:08.837000+00:00 | 2026-10-16T14:59:34.362000+00:00 | 263h 43m |
| gameWindowUnfocusEvent | 15 | 0.08 | 1 | 6 | 0 | 2026-10-05T15:47:54.726000+00:00 | 2026-10-16T15:42:29.341000+00:00 | 263h 54m |
| argumentationToolEvent | 14 | 0.08 | 1 | 2 | 0 | 2026-10-05T15:40:38.636000+00:00 | 2026-10-13T15:45:34.623000+00:00 | 192h 4m |
| argumentationEvent | 12 | 0.07 | 1 | 4 | 0 | 2026-10-05T15:40:41.421000+00:00 | 2026-10-16T15:41:44.652000+00:00 | 264h 1m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-10-05T15:47:33.588000+00:00 | 2026-10-15T15:35:11.481000+00:00 | 239h 47m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 431628.946s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 0.218s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.701s median 
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
  - Observed: 9.343s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.17s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 244.283s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 773.521s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2177.741s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.457s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 9625 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightButton; rightShift; tab; upArrow 
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
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.0x vs baseline. 
  - Observed: 50 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,B,2,II; A,C,2,II; A,C,B,2,II; B,1,I; B,1,II; B,3,I; B,C,2,II; B,C,D,2,II; B,D,2,II; C,1,I; C,1,II; C,2,II; C,3,II; C,D,2,II; C,D,B,2,II; D,1,II; D,2,II; D,C,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 558 records 
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
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
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

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[149] _id=6ac3c12fde269131f9ad2137 ts=2026-10-05T15:24:30.7490000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[200] _id=6ac3c206de269131f9ad2e6d ts=2026-10-05T15:28:06.5050000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[220] _id=6ac3c239de269131f9ad319b ts=2026-10-05T15:28:57.3510000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[2] _id=6ac3bf39de269131f9ace76d ts=2026-10-05T15:16:08.8370000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[692] _id=6ac513a3de269131f9b45e53 ts=2026-10-06T15:28:34.6450000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1002] _id=6ac51461de269131f9b46a41 ts=2026-10-06T15:31:44.6410000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[1] _id=6ac3bf39de269131f9ace76b ts=2026-10-05T15:16:08.8350000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[693] _id=6ac513a3de269131f9b45e51 ts=2026-10-06T15:28:34.6440000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1001] _id=6ac51461de269131f9b46a3f ts=2026-10-06T15:31:44.6400000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[691] _id=6ac513a2de269131f9b45e4b ts=2026-10-05T15:47:54.726Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1596] _id=6ac516bbde269131f9b49d3c ts=2026-10-06T15:39:53.629Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1771] _id=6ac662c6de269131f9bb99aa ts=2026-10-06T15:47:33.755Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 9624 | 0.0 | 0.218 | 98.884 | 2.172 | 429756.494 | 0.61 | 1369 | 8 |
| PuzzlePieceVisibleEvent | 3579 | 0.0 | 0.018 | 241.119 | 1.209 | 429774.145 | 0.25 | 1934 | 7 |
| DialogueEvent | 1842 | 0.0 | 3.987 | 516.96 | 28.888 | 429517.231 | 0.12 | 504 | 8 |
| PlayerPositionEvent | 1576 | 9.749 | 10.003 | 604.032 | 10.133 | 429510.391 | 0.1 | 0 | 7 |
| argumentationNodeEvent | 557 | 0.0 | 0.463 | 1707.064 | 13.003 | 691088.869 | 0.04 | 58 | 4 |
| ObjectInterEvent | 378 | 0.0 | 4.566 | 2516.763 | 198.164 | 431733.092 | 0.02 | 3 | 9 |
| questEvent | 62 | 0.002 | 196.858 | 15346.309 | 84813.826 | 429536.627 | 0.0 | 7 | 13 |
| Soil Key Puzzle | 52 | 0.15 | 2.701 | 14924.168 | 86281.577 | 431825.668 | 0.0 | 0 | 6 |
| TopographicMapEvent | 52 | 0.02 | 9.343 | 13321.891 | 85407.651 | 431743.818 | 0.0 | 3 | 6 |
| argumentationAnswerEvent | 49 | 0.515 | 15.17 | 19403.944 | 50900.204 | 691169.205 | 0.0 | 0 | 4 |
| DEBUGMenu | 29 | 8.165 | 415.967 | 32809.995 | 86805.428 | 430975.405 | 0.0 | 0 | 12 |
| gameWindowFocusEvent | 23 | 60.664 | 773.521 | 41390.57 | 86983.652 | 430986.92 | 0.0 | 0 | 12 |
| soilMachine | 19 | 0.623 | 7.457 | 29.339 | 126.535 | 178.974 | 2.05 | 0 | 0 |
| gameStartEvent | 15 | 60.664 | 1692.801 | 63293.702 | 190298.142 | 430986.92 | 0.0 | 0 | 9 |
| gameWindowUnfocusEvent | 14 | 129.637 | 2177.741 | 67862.473 | 236737.129 | 515825.724 | 0.0 | 0 | 9 |
| argumentationToolEvent | 13 | 1.693 | 20.742 | 53191.999 | 276561.917 | 691152.35 | 0.0 | 0 | 1 |
| argumentationEvent | 11 | 0.039 | 244.283 | 86405.748 | 432183.921 | 691081.429 | 0.0 | 1 | 4 |
| EndOfUnit | 2 | 87786.698 | 431628.946 | 431628.946 | 741086.97 | 775471.195 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 14 group(s), 42 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[4530] _id=6ac66708de269131f9bc02c2 ts=2026-10-07T15:36:40.1870000Z == 6ab9a8bc9a8420a1e6b56b01.jsonl[4532] _id=6ac66708de269131f9bc02c4 ts=2026-10-07T15:36:40.1870000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[5118] _id=6ac668b0de269131f9bc1d9c ts=2026-10-07T15:43:43.0840000Z == 6ab9a8bc9a8420a1e6b56b01.jsonl[5119] _id=6ac668b0de269131f9bc1d9d ts=2026-10-07T15:43:43.0840000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[5123] _id=6ac668b0de269131f9bc1da1 ts=2026-10-07T15:43:43.0850000Z == 6ab9a8bc9a8420a1e6b56b01.jsonl[5124] _id=6ac668b0de269131f9bc1da2 ts=2026-10-07T15:43:43.0850000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 46 group(s), 85 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[1855] _id=6ac66342de269131f9bb9d43 ts=2026-10-07T15:20:32.6740000Z == 6ab9a8bc9a8420a1e6b56b01.jsonl[1856] _id=6ac66342de269131f9bb9d47 ts=2026-10-07T15:20:32.6740000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1876] _id=6ac66345de269131f9bb9d72 ts=2026-10-07T15:20:35.7630000Z == 6ab9a8bc9a8420a1e6b56b01.jsonl[1877] _id=6ac66345de269131f9bb9d74 ts=2026-10-07T15:20:35.7630000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1842] _id=6ac6634fde269131f9bb9dcf ts=2026-10-07T15:20:46.4400000Z == 6ab9a8bc9a8420a1e6b56b01.jsonl[1882] _id=6ac66350de269131f9bb9dd1 ts=2026-10-07T15:20:46.4400000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 103 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[111] _id=6ac3c0bdde269131f9ad11db ts=2026-10-05T15:22:37.4740000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[112] _id=6ac3c0bdde269131f9ad11dd ts=2026-10-05T15:22:37.4790000Z`; `306ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[701] _id=6ac513bbde269131f9b45f6b ts=2026-10-06T15:28:58.7930000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[688] _id=6ac513bbde269131f9b45f71 ts=2026-10-06T15:28:59.0990000Z`; `187ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[688] _id=6ac513bbde269131f9b45f71 ts=2026-10-06T15:28:59.0990000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[690] _id=6ac513bbde269131f9b45f77 ts=2026-10-06T15:28:59.2860000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `149ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[1736] _id=6ac51808de269131f9b4bd5d ts=2026-10-06T15:47:18.9120000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[1727] _id=6ac51808de269131f9b4bd5f ts=2026-10-06T15:47:19.0610000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `132ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[12503] _id=6ad0f0a1de269131f9dc8c99 ts=2026-10-15T15:26:25.2170000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[12507] _id=6ad0f0a1de269131f9dc8c9d ts=2026-10-15T15:26:25.3490000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `809ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[8906] _id=6acf9a35de269131f9d44e6a ts=2026-10-14T15:05:24.9190000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[8896] _id=6acf9a36de269131f9d44e76 ts=2026-10-14T15:05:25.7280000Z`; `676ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[8937] _id=6acf9a60de269131f9d451f6 ts=2026-10-14T15:06:07.7960000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[8939] _id=6acf9a61de269131f9d45208 ts=2026-10-14T15:06:08.4720000Z`; `515ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[8940] _id=6acf9a62de269131f9d45227 ts=2026-10-14T15:06:09.6560000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[8941] _id=6acf9a62de269131f9d4522f ts=2026-10-14T15:06:10.1710000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10134] _id=6acfa0d3de269131f9d4bf60 ts=2026-10-14T15:33:38.2000000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[10137] _id=6acfa0d3de269131f9d4bf63 ts=2026-10-14T15:33:38.2390000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 39 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `160ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[400] _id=6ac3c4fdde269131f9ad5bab ts=2026-10-05T15:40:45.1820000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[401] _id=6ac3c4fdde269131f9ad5baf ts=2026-10-05T15:40:45.3420000Z`; `53ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[445] _id=6ac3c507de269131f9ad5c25 ts=2026-10-05T15:40:54.7340000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[413] _id=6ac3c507de269131f9ad5c27 ts=2026-10-05T15:40:54.7870000Z`; `18ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[482] _id=6ac3c5aede269131f9ad6625 ts=2026-10-05T15:43:42.4440000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[486] _id=6ac3c5aede269131f9ad6637 ts=2026-10-05T15:43:42.4620000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `623ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[16519] _id=6ad241dfde269131f9e52f8c ts=2026-10-16T15:25:19.0050000Z ~ 6ab9a8bc9a8420a1e6b56b01.jsonl[16520] _id=6ad241e0de269131f9e52f97 ts=2026-10-16T15:25:19.6280000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5306] _id=6ac7b483de269131f9c382f6 ts=2026-10-08T15:19:30.7710000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7639] _id=6ace4803de269131f9cf00bd ts=2026-10-13T15:02:26.1760000Z; 24h 11m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5] _id=6ac3bf60de269131f9ace899 ts=2026-10-05T15:16:47.8900000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[682] _id=6ac513abde269131f9b45ecd ts=2026-10-06T15:28:43.4900000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7640] _id=6ace4856de269131f9cf0148 ts=2026-10-13T15:03:49.3800000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8818] _id=6acf999ade269131f9d44495 ts=2026-10-14T15:02:49.5500000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7631] _id=6ac7ba8ede269131f9c41ea6 ts=2026-10-08T15:45:17.4300000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7642] _id=6ace485cde269131f9cf0157 ts=2026-10-13T15:03:54.6610000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b01.jsonl[674] _id=6ac3c693de269131f9ad7719 ts=2026-10-05T15:47:31.1960000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[1600] _id=6ac516ccde269131f9b49e81 ts=2026-10-06T15:42:04.3520000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5292] _id=6ac66977de269131f9bc2e0a ts=2026-10-07T15:47:03.0320000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5381] _id=6ac7b4aade269131f9c3866a ts=2026-10-08T15:20:09.9770000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 504 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10090] _id=6acfa09fde269131f9d4bd12 ts=2026-10-14T15:32:46.1360000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10096] _id=6acfa09fde269131f9d4bd13 ts=2026-10-14T15:32:46.1360000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10112] _id=6acfa0b9de269131f9d4be43 ts=2026-10-14T15:33:12.8740000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10113] _id=6acfa0b9de269131f9d4be44 ts=2026-10-14T15:33:12.8740000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[17655] _id=6ad245e4de269131f9e55b5b ts=2026-10-16T15:42:27.0560000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[17656] _id=6ad245e4de269131f9e55b5c ts=2026-10-16T15:42:27.0560000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 24m 
  - Evidence: 215h 24m: 6ab9a8bc9a8420a1e6b56b01.jsonl[673] _id=6ac3c695de269131f9ad773d ts=2026-10-05T15:47:33.5880000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[9125] _id=6acf9bc5de269131f9d4709f ts=2026-10-14T15:12:04.7830000Z; 24h 23m: 6ab9a8bc9a8420a1e6b56b01.jsonl[9125] _id=6acf9bc5de269131f9d4709f ts=2026-10-14T15:12:04.7830000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[13037] _id=6ad0f2afde269131f9dcaf19 ts=2026-10-15T15:35:11.4810000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7555] _id=6ac7b9a6de269131f9c41598 ts=2026-10-08T15:41:25.3250000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7654] _id=6ace4862de269131f9cf017d ts=2026-10-13T15:04:01.8190000Z; 23h 42m: 6ab9a8bc9a8420a1e6b56b01.jsonl[649] _id=6ac3c669de269131f9ad7229 ts=2026-10-05T15:46:49.1180000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[697] _id=6ac513b3de269131f9b45f31 ts=2026-10-06T15:28:51.2410000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5283] _id=6ac6695cde269131f9bc2b61 ts=2026-10-07T15:46:36.0120000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5310] _id=6ac7b489de269131f9c38370 ts=2026-10-08T15:19:36.2580000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1369 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10218] _id=6acfa135de269131f9d4c416 ts=2026-10-14T15:35:16.4960000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10219] _id=6acfa135de269131f9d4c417 ts=2026-10-14T15:35:16.4960000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10284] _id=6acfa151de269131f9d4c67e ts=2026-10-14T15:35:44.2930000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10285] _id=6acfa151de269131f9d4c67f ts=2026-10-14T15:35:44.2930000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10377] _id=6acfa164de269131f9d4c88a ts=2026-10-14T15:36:04.0530000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10378] _id=6acfa164de269131f9d4c88b ts=2026-10-14T15:36:04.0530000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7318] _id=6ac7b8f1de269131f9c40b3f ts=2026-10-08T15:38:25.1180000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8307] _id=6ace4f67de269131f9cf2af4 ts=2026-10-13T15:33:58.2100000Z; 24h 3m: 6ab9a8bc9a8420a1e6b56b01.jsonl[4274] _id=6ac6656ade269131f9bbd8eb ts=2026-10-07T15:29:46.3560000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[6655] _id=6ac7b7c4de269131f9c3ece5 ts=2026-10-08T15:33:23.5580000Z; 23h 42m: 6ab9a8bc9a8420a1e6b56b01.jsonl[652] _id=6ac3c66bde269131f9ad7270 ts=2026-10-05T15:46:51.1660000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[699] _id=6ac513b9de269131f9b45f61 ts=2026-10-06T15:28:56.9060000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[17491] _id=6ad2448bde269131f9e5522a ts=2026-10-16T15:36:42.9320000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[17492] _id=6ad2448bde269131f9e5522b ts=2026-10-16T15:36:42.9320000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[17553] _id=6ad244d6de269131f9e55474 ts=2026-10-16T15:37:57.8330000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[17554] _id=6ad244d6de269131f9e55475 ts=2026-10-16T15:37:57.8330000Z; 5ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[111] _id=6ac3c0bdde269131f9ad11db ts=2026-10-05T15:22:37.4740000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[112] _id=6ac3c0bdde269131f9ad11dd ts=2026-10-05T15:22:37.4790000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7628] _id=6ac7ba8fde269131f9c41eb2 ts=2026-10-08T15:45:19.0010000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7641] _id=6ace485cde269131f9cf0156 ts=2026-10-13T15:03:49.3920000Z; 23h 41m: 6ab9a8bc9a8420a1e6b56b01.jsonl[672] _id=6ac3c68dde269131f9ad76d1 ts=2026-10-05T15:47:25.6180000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[695] _id=6ac513aede269131f9b45ef3 ts=2026-10-06T15:28:43.5060000Z; 23h 32m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5295] _id=6ac66983de269131f9bc2f27 ts=2026-10-07T15:47:14.9780000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5307] _id=6ac7b486de269131f9c3833f ts=2026-10-08T15:19:30.7890000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7466] _id=6ac7b98fde269131f9c41385 ts=2026-10-08T15:41:00.9440000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7647] _id=6ace485cde269131f9cf015d ts=2026-10-13T15:03:55.0890000Z; 24h 34m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7760] _id=6ace4871de269131f9cf0260 ts=2026-10-13T15:04:14.0370000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10477] _id=6acfa1f8de269131f9d4d348 ts=2026-10-14T15:38:30.1670000Z; 24h 7m: 6ab9a8bc9a8420a1e6b56b01.jsonl[4220] _id=6ac66535de269131f9bbd3fd ts=2026-10-07T15:28:52.0450000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[6782] _id=6ac7b85ade269131f9c3f821 ts=2026-10-08T15:35:53.3060000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1934 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10477] _id=6acfa1f8de269131f9d4d348 ts=2026-10-14T15:38:30.1670000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10478] _id=6acfa1f8de269131f9d4d34c ts=2026-10-14T15:38:30.1670000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10486] _id=6acfa1ffde269131f9d4d407 ts=2026-10-14T15:38:38.5040000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10487] _id=6acfa1ffde269131f9d4d409 ts=2026-10-14T15:38:38.5040000Z; 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10488] _id=6acfa200de269131f9d4d415 ts=2026-10-14T15:38:38.5970000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10497] _id=6acfa200de269131f9d4d41b ts=2026-10-14T15:38:38.5970000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 57m 
  - Evidence: 119h 57m: 6ab9a8bc9a8420a1e6b56b01.jsonl[6670] _id=6ac7b7e3de269131f9c3ef2d ts=2026-10-08T15:33:54.6470000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8169] _id=6ace4eb5de269131f9cf239b ts=2026-10-13T15:31:00.3150000Z; 24h 3m: 6ab9a8bc9a8420a1e6b56b01.jsonl[4275] _id=6ac6656dde269131f9bbd931 ts=2026-10-07T15:29:49.3260000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[6654] _id=6ac7b7c4de269131f9c3ece2 ts=2026-10-08T15:33:23.5520000Z; 24h 1m: 6ab9a8bc9a8420a1e6b56b01.jsonl[8354] _id=6ace4fb4de269131f9cf2d8a ts=2026-10-13T15:35:15.4210000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10420] _id=6acfa199de269131f9d4ccd4 ts=2026-10-14T15:36:56.7780000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5712] _id=6ac7b673de269131f9c3befe ts=2026-10-08T15:27:47.0050000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8040] _id=6ace4cf3de269131f9cf164a ts=2026-10-13T15:23:30.8230000Z; 24h 8m: 6ab9a8bc9a8420a1e6b56b01.jsonl[9292] _id=6acf9d27de269131f9d48c34 ts=2026-10-14T15:17:58.2680000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[12489] _id=6ad0f093de269131f9dc8b50 ts=2026-10-15T15:26:11.4980000Z; 23h 53m: 6ab9a8bc9a8420a1e6b56b01.jsonl[8046] _id=6ace4d02de269131f9cf16f3 ts=2026-10-13T15:23:45.3650000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[9254] _id=6acf9ce1de269131f9d486cc ts=2026-10-14T15:16:48.1800000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.020s..0.040s shown 
  - Evidence: 20ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[5259] _id=6ac66941de269131f9bc28c6 ts=2026-10-07T15:46:09.1730000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5263] _id=6ac66941de269131f9bc28ca ts=2026-10-07T15:46:09.1930000Z; 21ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[5436] _id=6ac7b51dde269131f9c39216 ts=2026-10-08T15:22:04.6070000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5443] _id=6ac7b51dde269131f9c3921a ts=2026-10-08T15:22:04.6280000Z; 40ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[5258] _id=6ac66941de269131f9bc28c0 ts=2026-10-07T15:46:09.1330000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5259] _id=6ac66941de269131f9bc28c6 ts=2026-10-07T15:46:09.1730000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 59m 
  - Evidence: 191h 59m: 6ab9a8bc9a8420a1e6b56b01.jsonl[511] _id=6ac3c5dfde269131f9ad6895 ts=2026-10-05T15:44:31.5470000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8677] _id=6ace51c1de269131f9cf413c ts=2026-10-13T15:44:00.7520000Z; 48h 8m: 6ab9a8bc9a8420a1e6b56b01.jsonl[10133] _id=6acfa0d3de269131f9d4bf5e ts=2026-10-14T15:33:38.1620000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[17636] _id=6ad245d4de269131f9e55b06 ts=2026-10-16T15:42:11.5970000Z; 23h 17m: 6ab9a8bc9a8420a1e6b56b01.jsonl[8804] _id=6ace526dde269131f9cf48d6 ts=2026-10-13T15:46:52.2000000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8872] _id=6acf99ecde269131f9d44adb ts=2026-10-14T15:04:12.0750000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 58m 
  - Evidence: 191h 58m: 6ab9a8bc9a8420a1e6b56b01.jsonl[510] _id=6ac3c5dfde269131f9ad6897 ts=2026-10-05T15:44:31.5730000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8623] _id=6ace516ade269131f9cf3dc9 ts=2026-10-13T15:42:33.0020000Z; 48h 8m: 6ab9a8bc9a8420a1e6b56b01.jsonl[10137] _id=6acfa0d3de269131f9d4bf63 ts=2026-10-14T15:33:38.2390000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[17616] _id=6ad245b9de269131f9e55a54 ts=2026-10-16T15:41:44.6520000Z; 23h 16m: 6ab9a8bc9a8420a1e6b56b01.jsonl[8805] _id=6ace526dde269131f9cf48d8 ts=2026-10-13T15:46:52.2200000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8829] _id=6acf99c3de269131f9d4487c ts=2026-10-14T15:03:30.5680000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.039s..0.039s shown 
  - Evidence: 39ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[10134] _id=6acfa0d3de269131f9d4bf60 ts=2026-10-14T15:33:38.2000000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[10137] _id=6acfa0d3de269131f9d4bf63 ts=2026-10-14T15:33:38.2390000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 58m 
  - Evidence: 191h 58m: 6ab9a8bc9a8420a1e6b56b01.jsonl[509] _id=6ac3c5ddde269131f9ad686d ts=2026-10-05T15:44:28.9890000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8627] _id=6ace516ede269131f9cf3dec ts=2026-10-13T15:42:37.8580000Z; 48h 8m: 6ab9a8bc9a8420a1e6b56b01.jsonl[10132] _id=6acfa0d1de269131f9d4bf4a ts=2026-10-14T15:33:36.5750000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[17617] _id=6ad245bcde269131f9e55a60 ts=2026-10-16T15:41:47.5600000Z; 23h 16m: 6ab9a8bc9a8420a1e6b56b01.jsonl[8801] _id=6ace5268de269131f9cf4889 ts=2026-10-13T15:46:47.1950000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8833] _id=6acf99cade269131f9d448ab ts=2026-10-14T15:03:37.5880000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 58 interval(s) ≤ 0.000s..0.018s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[8692] _id=6ace51d6de269131f9cf4223 ts=2026-10-13T15:44:21.6730000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8693] _id=6ace51d6de269131f9cf4224 ts=2026-10-13T15:44:21.6730000Z; 5ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[8747] _id=6ace522cde269131f9cf45ce ts=2026-10-13T15:45:47.7430000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8748] _id=6ace522cde269131f9cf45d0 ts=2026-10-13T15:45:47.7480000Z; 18ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[482] _id=6ac3c5aede269131f9ad6625 ts=2026-10-05T15:43:42.4440000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[486] _id=6ac3c5aede269131f9ad6637 ts=2026-10-05T15:43:42.4620000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 59m 
  - Evidence: 191h 59m: 6ab9a8bc9a8420a1e6b56b01.jsonl[481] _id=6ac3c5a9de269131f9ad6599 ts=2026-10-05T15:43:37.2610000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8635] _id=6ace517ade269131f9cf3e7d ts=2026-10-13T15:42:49.6110000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5304] _id=6ac7b478de269131f9c381df ts=2026-10-08T15:19:19.6460000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7638] _id=6ace4803de269131f9cf00c0 ts=2026-10-13T15:02:26.5660000Z; 24h 12m: 6ab9a8bc9a8420a1e6b56b01.jsonl[2] _id=6ac3bf39de269131f9ace76d ts=2026-10-05T15:16:08.8370000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[692] _id=6ac513a3de269131f9b45e53 ts=2026-10-06T15:28:34.6450000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7638] _id=6ace4803de269131f9cf00c0 ts=2026-10-13T15:02:26.5660000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8820] _id=6acf999ade269131f9d44497 ts=2026-10-14T15:02:49.6980000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5303] _id=6ac7b478de269131f9c381de ts=2026-10-08T15:19:19.6460000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7637] _id=6ace4803de269131f9cf00bf ts=2026-10-13T15:02:26.5660000Z; 24h 12m: 6ab9a8bc9a8420a1e6b56b01.jsonl[1] _id=6ac3bf39de269131f9ace76b ts=2026-10-05T15:16:08.8350000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[693] _id=6ac513a3de269131f9b45e51 ts=2026-10-06T15:28:34.6440000Z; 23h 45m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7955] _id=6ace4b86de269131f9cf0d89 ts=2026-10-13T15:17:25.4630000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[8819] _id=6acf999ade269131f9d44496 ts=2026-10-14T15:02:49.6980000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 17m 
  - Evidence: 143h 17m: 6ab9a8bc9a8420a1e6b56b01.jsonl[5301] _id=6ac7b478de269131f9c381d9 ts=2026-10-07T15:47:22.728Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7810] _id=6ace487dde269131f9cf02db ts=2026-10-13T15:04:28.4520000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b01.jsonl[8817] _id=6acf999ade269131f9d44493 ts=2026-10-13T15:47:18.358Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[11127] _id=6acfa442de269131f9d4f736 ts=2026-10-14T15:48:17.0130000Z; 23h 55m: 6ab9a8bc9a8420a1e6b56b01.jsonl[1771] _id=6ac662c6de269131f9bb99aa ts=2026-10-06T15:47:33.755Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[5107] _id=6ac66887de269131f9bc1bf8 ts=2026-10-07T15:43:02.8940000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8bc9a8420a1e6b56b01.jsonl[7627] _id=6ac7ba7ade269131f9c41dcf ts=2026-10-08T15:44:58.0980000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[7644] _id=6ace485cde269131f9cf0159 ts=2026-10-13T15:03:54.7250000Z; 23h 58m: 6ab9a8bc9a8420a1e6b56b01.jsonl[631] _id=6ac3c66dde269131f9ad72b2 ts=2026-10-05T15:46:53.3540000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[1637] _id=6ac5177fde269131f9b4adcd ts=2026-10-06T15:45:02.9200000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b01.jsonl[1637] _id=6ac5177fde269131f9b4adcd ts=2026-10-06T15:45:02.9200000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[1776] _id=6ac662e1de269131f9bb99fe ts=2026-10-07T15:18:56.8720000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[396] _id=6ac3c4a5de269131f9ad5698 ts=2026-10-05T15:39:17.3030000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[397] _id=6ac3c4a5de269131f9ad569f ts=2026-10-05T15:39:17.3050000Z; 5ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[16071] _id=6ad240dbde269131f9e521d6 ts=2026-10-16T15:20:58.8630000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[16073] _id=6ad240dbde269131f9e521d8 ts=2026-10-16T15:20:58.8680000Z; 6ms: 6ab9a8bc9a8420a1e6b56b01.jsonl[15364] _id=6ad23ec0de269131f9e50749 ts=2026-10-16T15:12:00.0540000Z -> 6ab9a8bc9a8420a1e6b56b01.jsonl[15365] _id=6ad23ec1de269131f9e5074c ts=2026-10-16T15:12:00.0600000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[377] _id=6ac3c49ade269131f9ad556d ts=2026-10-05T15:39:06.3290000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[517] _id=6ac3c5f3de269131f9ad6981 ts=2026-10-05T15:44:51.4800000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[5613] _id=6ac7b64fde269131f9c3b724 ts=2026-10-08T15:27:10.6820000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[1727] _id=6ac51808de269131f9b4bd5f ts=2026-10-06T15:47:19.0610000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1731] _id=6ac51809de269131f9b4bd73 ts=2026-10-06T15:47:19.5250000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[10137] _id=6acfa0d3de269131f9d4bf63 ts=2026-10-14T15:33:38.2390000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[401] _id=6ac3c4fdde269131f9ad5baf ts=2026-10-05T15:40:45.3420000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[413] _id=6ac3c507de269131f9ad5c27 ts=2026-10-05T15:40:54.7870000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[486] _id=6ac3c5aede269131f9ad6637 ts=2026-10-05T15:43:42.4620000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[15364] _id=6ad23ec0de269131f9e50749 ts=2026-10-16T15:12:00.0540000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[5115] _id=6ac668b0de269131f9bc1d98 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 33 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[6850] _id=6ac7b868de269131f9c3fa1f ts=2026-10-08T15:36:07.4040000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[6854] _id=6ac7b86cde269131f9c3faa9 ts=2026-10-08T15:36:09.2820000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[6948] _id=6ac7b8c5de269131f9c403ed ts=2026-10-08T15:37:38.5300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 75 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[1856] _id=6ac66342de269131f9bb9d47 ts=2026-10-07T15:20:32.6740000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1857] _id=6ac66342de269131f9bb9d49 ts=2026-10-07T15:20:32.6740000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1866] _id=6ac66342de269131f9bb9d4e ts=2026-10-07T15:20:32.6740000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[14022] _id=6ad23c9fde269131f9e4cec2 ts=2026-10-16T15:02:54.8070000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[480] _id=6ac3c5a8de269131f9ad6573 ts=2026-10-05T15:43:35.5680000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[8649] _id=6ace5191de269131f9cf3f82 ts=2026-10-13T15:43:12.6190000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[8650] _id=6ace5193de269131f9cf3fa0 ts=2026-10-13T15:43:14.9300000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 335 start, 329 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 1091 open, 1081 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 12 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 37 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 605 of 17922 adjacent _id pairs reverse in client time; worst 90.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b01.jsonl[1947] _id=6ac66392de269131f9bba1b1 ts=2026-10-07T15:21:53.9920000Z`; `6ab9a8bc9a8420a1e6b56b01.jsonl[1945] _id=6ac66393de269131f9bba1c5 ts=2026-10-07T15:20:23.0480000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.86s, min -85240.12s, max -0.18s over 17923 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b01\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
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

### `InputEvent` — 9625 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (3335); Unit 4 Dev (1526); Unit 4 Dev - Dungeon (1323); Unit 3 Dev (1288); Unit 3 Dungeon Dev (1145); Unit 1 Dev (916); Unit 4 Dev - Anderson Base (92)
- **Intervals:** median 0.22s (p5 0.00s / p95 2.17s, n=9624)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 9625/9625 records)
    "pressed"  x9625
data.actionType  (string, 9625/9625 records)
    "Move"  x6887
    "Jump"  x1900
    "Interact"  x595
    "Ascend"  x116
    "Hoverboard"  x91
    "Descend"  x14
    "Map"  x8
    "Sprint"  x7
    "SkipCinematic"  x5
    "Pause"  x2
data.key  (string, 9625/9625 records, 3 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 9625/9625 records)
    "Player"  x9072
    "Drone"  x553
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3580 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2318); Unit 4 Dev (878); Unit 3 Dungeon Dev (384)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.21s, n=3579)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3580/3580 records)
    "BecameVisible"  x1091
    "BecameInvisible"  x1081
    "BecameCameraCentered"  x704
    "BecameCameraUncentered"  x704
data.pieceId  (string, 3580/3580 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3580/3580 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1843 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (775); Unit 3 Dev (321); Unit 1 Dev (221); Unit 3 Dungeon Dev (191); Unit 4 Dev (124); Unit 4 Dev - Anderson Base (124); Unit 4 Dev - Dungeon (87)
- **eventKey:** present on 1179 of 1843 records
- **Intervals:** median 3.99s (p5 0.00s / p95 28.89s, n=1842)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1179; [conversationId, dialogueEventType] x664
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1843/1843 records)
    numeric range 8 .. 107 (42 unique)
data.dialogueEventType  (string, 1843/1843 records)
    "DialogueNodeEvent"  x1179
    "DialogueStartEvent"  x335
    "DialogueFinishEvent"  x329
data.nodeId  (number, 1179/1843 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1585 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (622); Unit 1 Dev (242); Unit 3 Dev (213); Unit 3 Dungeon Dev (165); Unit 4 Dev (152); Unit 4 Dev - Dungeon (112); Unit 4 Dev - Anderson Base (79)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=1576)
- **Fields under `data`:**

```text
data.position  (object, 1585/1585 records)
data.position.x  (number, 1585/1585 records)
    numeric range -655.206 .. 1464.69 (556 unique)
data.position.y  (number, 1585/1585 records)
    numeric range -112.489 .. 164.671 (431 unique)
data.position.z  (number, 1585/1585 records)
    numeric range -1039.11 .. 1869.07 (555 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 558 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (256); Unit 4 Dev - Anderson Base (187); Unit 3 Dev (71); Unit 1 Dev (44)
- **Intervals:** median 0.46s (p5 0.04s / p95 13.00s, n=557)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 558/558 records)
    "argumentationNodeHoverEnd"  x236
    "argumentationNodeHoverStart"  x233
    "argumentationNodeAdd"  x53
    "argumentationNodeRemove"  x36
data.argumentationTitle  (string, 558/558 records)
    "Unit 2 – Watershed"  x256
    "Unit 4 - Flooding"  x187
    "Unit 3 - Pollution Upstream"  x71
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x19
data.nodeName  (string, 558/558 records)
    "B"  x101
    "C"  x89
    "A"  x83
    "1"  x76
    "II"  x65
    "I"  x47
    "D"  x41
    "2"  x25
    "3"  x20
    "5"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 379 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (133); Unit 4 Dev - Dungeon (83); Unit 2 Prod (Refactor) (77); Unit 3 Dungeon Dev (57); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 4 Dev (8)
- **Intervals:** median 4.57s (p5 0.18s / p95 198.16s, n=378)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 379/379 records)
    33 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 379/379 records)
    90 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 63 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev - Dungeon (8); Unit 4 Dev (6); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 63 of 63 records
- **Intervals:** median 196.86s (p5 0.01s / p95 84813.83s, n=62)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 63/63 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x26
data.questID  (string, 63/63 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 63/63 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/63 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 53 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 4 Dev (20); Unit 3 Dev (11)
- **Intervals:** median 2.70s (p5 0.15s / p95 86281.58s, n=52)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/53 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/53 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x3
    "Unit 3 Dev"  x2
data.actionType  (string, 44/53 records)
    "RightDrag"  x25
    "LeftDrag"  x19
data.currentSoilType  (string, 44/53 records)
    "CLAYROCK"  x9
    "SAND"  x8
    "CLAY"  x7
    "CLAYSAND"  x7
    "SANDGRAVEL"  x6
    "BEDROCK"  x4
    "GRAVEL"  x3
data.isCorrectSelection  (string, 44/53 records)
    "false"  x34
    "true"  x10
data.waterLevelStatus  (string, 44/53 records)
    "TooHigh"  x23
    "TooLow"  x12
    "Proper"  x9
data.waterRetentionChange  (string, 44/53 records)
    "Increase"  x19
    "Decrease"  x15
    "NoChange"  x10
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 53 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (29); Unit 3 Dev (22); Unit 4 Dev (2)
- **Intervals:** median 9.34s (p5 0.05s / p95 85407.65s, n=52)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, location] x13
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x1
data.featureUsed  (string, 53/53 records)
    "Map"  x40
    "Waypoint"  x13
data.location  (object, 13/53 records)
data.location.x  (number, 13/53 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 13/53 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 13/53 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 50 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 4 Dev - Anderson Base (19); Unit 3 Dev (6); Unit 1 Dev (2)
- **Intervals:** median 15.17s (p5 0.90s / p95 50900.20s, n=49)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "submitAnswerEvent"  x50
data.answerSubmitted  (string, 50/50 records)
    23 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 50/50 records)
    "Unit 2 – Watershed"  x23
    "Unit 4 - Flooding"  x19
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (6); Unit 1 Dev (4); Unit 4 Dev (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 415.97s (p5 10.19s / p95 86805.43s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 24 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 4 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 773.52s (p5 108.94s / p95 86983.65s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 20 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (20)
- **Intervals:** median 7.46s (p5 1.18s / p95 126.53s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "ChangeCanister"  x20
data.canisterType  (string, 20/20 records)
    "Clay"  x8
    "Bedrock"  x7
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 20/20 records)
    "5"  x14
    "4"  x4
    "3"  x2
data.machine  (string, 20/20 records)
    "1"  x19
    "2"  x1
data.row  (string, 20/20 records)
    "TopRow"  x12
    "BottomRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 1692.80s (p5 151.20s / p95 190298.14s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev (4); Unit 3 Dungeon Dev (2); Transition (1); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 2177.74s (p5 173.34s / p95 236737.13s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 1 Dev (5)
- **Intervals:** median 20.74s (p5 1.83s / p95 276561.92s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x12
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 2 – Watershed"  x9
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - Waterfall Data"  x7
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 244.28s (p5 14.65s / p95 432183.92s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 12/12 records)
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 2 – Watershed"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 431628.95s (p5 122170.92s / p95 741086.97s, n=2)
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
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointResetEvent" (1x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (36x)
- `soilMachine` data.canisterType: "Bedrock" (7x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*