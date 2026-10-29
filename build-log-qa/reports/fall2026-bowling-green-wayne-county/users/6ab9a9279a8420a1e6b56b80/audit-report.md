# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b80

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b80
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b80.jsonl
- **Records:** 10922 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b80
- **Time span:** 2026-10-05T19:04:43.629000+00:00 .. 2026-10-16T18:59:31.177000+00:00 (263h 54m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b80\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 10922 records, 7 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 86 INFO, 2 NOT_TESTED, 79 PASS.
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
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5361 | 49.08 | 1 | 6 | 0 | 2026-10-05T19:04:57.665000+00:00 | 2026-10-16T18:58:23.261000+00:00 | 263h 53m |
| PuzzlePieceVisibleEvent | 2031 | 18.6 | 1 | 3 | 0 | 2026-10-06T19:01:20.972000+00:00 | 2026-10-16T18:58:21.706000+00:00 | 239h 57m |
| DialogueEvent | 1573 | 14.4 | 1 | 6 | 1023 | 2026-10-05T19:05:14.255000+00:00 | 2026-10-16T18:59:23.202000+00:00 | 263h 54m |
| PlayerPositionEvent | 1355 | 12.41 | 1 | 6 | 0 | 2026-10-05T19:04:54.129000+00:00 | 2026-10-16T18:59:31.177000+00:00 | 263h 54m |
| ObjectInterEvent | 213 | 1.95 | 1 | 6 | 0 | 2026-10-05T19:09:10.165000+00:00 | 2026-10-16T18:58:08.905000+00:00 | 263h 48m |
| argumentationNodeEvent | 101 | 0.92 | 1 | 3 | 0 | 2026-10-06T18:50:46.039000+00:00 | 2026-10-15T21:50:56.890000+00:00 | 219h 0m |
| TopographicMapEvent | 66 | 0.6 | 1 | 2 | 0 | 2026-10-06T19:02:08.466000+00:00 | 2026-10-15T22:08:48.154000+00:00 | 219h 6m |
| Soil Key Puzzle | 62 | 0.57 | 1 | 3 | 0 | 2026-10-06T19:09:08.220000+00:00 | 2026-10-16T18:35:59.653000+00:00 | 239h 26m |
| questEvent | 62 | 0.57 | 1 | 6 | 62 | 2026-10-05T19:05:14.218000+00:00 | 2026-10-16T18:58:02.350000+00:00 | 263h 52m |
| DEBUGMenu | 27 | 0.25 | 1 | 7 | 0 | 2026-10-05T19:04:54.112000+00:00 | 2026-10-16T18:57:58.619000+00:00 | 263h 53m |
| gameWindowFocusEvent | 16 | 0.15 | 1 | 2 | 0 | 2026-10-05T19:04:43.629000+00:00 | 2026-10-16T18:30:06.891000+00:00 | 263h 25m |
| gameStartEvent | 13 | 0.12 | 1 | 1 | 0 | 2026-10-05T19:04:43.630000+00:00 | 2026-10-16T18:30:04.479000+00:00 | 263h 25m |
| argumentationEvent | 9 | 0.08 | 1 | 3 | 0 | 2026-10-06T18:50:57.702000+00:00 | 2026-10-15T21:51:04.199000+00:00 | 219h 0m |
| DaniEvent | 8 | 0.07 | 1 | 2 | 0 | 2026-10-06T19:16:36.343000+00:00 | 2026-10-15T21:38:09.928000+00:00 | 218h 21m |
| gameWindowUnfocusEvent | 8 | 0.07 | 1 | 4 | 0 | 2026-10-05T19:18:01.642000+00:00 | 2026-10-16T18:30:06.506000+00:00 | 263h 12m |
| soilMachine | 8 | 0.07 | 1 | 1 | 0 | 2026-10-16T18:50:32.340000+00:00 | 2026-10-16T18:56:56.806000+00:00 | 6m 24s |
| argumentationAnswerEvent | 4 | 0.04 | 1 | 3 | 0 | 2026-10-06T18:51:14.327000+00:00 | 2026-10-15T21:51:04.145000+00:00 | 218h 59m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-06T18:56:19.003000+00:00 | 2026-10-15T22:13:41.546000+00:00 | 219h 17m |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T18:50:57.615000+00:00 | 2026-10-06T18:50:58.183000+00:00 | 0.6s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 394721.272s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.06s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.961s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 9713.052s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.568s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 42297.005s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 8642.227s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 83707.138s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.037s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
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
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1, 
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
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: D 
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
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 11 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[194] _id=6ac3f65bde269131f9af6aa7 ts=2026-10-05T19:11:22.2830000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[294] _id=6ac3f745de269131f9af6d0d ts=2026-10-05T19:15:16.3580000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[395] _id=6ac3f7dfde269131f9af6fe7 ts=2026-10-05T19:17:50.5150000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1] _id=6ac3f4ccde269131f9af690f ts=2026-10-05T19:04:43.6300000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[421] _id=6ac53eb4de269131f9b679b1 ts=2026-10-06T18:32:18.9100000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1173] _id=6ac544a7de269131f9b71a00 ts=2026-10-06T18:57:41.9140000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[35] _id=6ac3f4ccde269131f9af690d ts=2026-10-05T19:04:43.6290000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[420] _id=6ac53eb4de269131f9b679af ts=2026-10-06T18:32:18.9080000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[463] _id=6ac53eeade269131f9b67e81 ts=2026-10-06T18:33:13.1560000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[418] _id=6ac53eb3de269131f9b679a5 ts=2026-10-05T19:18:01.642Z`; `6ab9a9279a8420a1e6b56b80.jsonl[461] _id=6ac53ee6de269131f9b67e09 ts=2026-10-06T18:33:08.7800000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1102] _id=6ac5440bde269131f9b71133 ts=2026-10-06T18:55:06.3320000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 22 of 66 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1399] _id=6ac545b1de269131f9b72eab ts=2026-10-06T19:02:08.4660000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1426] _id=6ac545e0de269131f9b73247 ts=2026-10-06T19:02:55.7680000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1432] _id=6ac545edde269131f9b73365 ts=2026-10-06T19:03:08.2420000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5360 | 0.0 | 0.365 | 177.24 | 3.834 | 505919.559 | 0.34 | 433 | 11 |
| PuzzlePieceVisibleEvent | 2030 | 0.0 | 0.06 | 425.527 | 1.706 | 615535.176 | 0.14 | 948 | 5 |
| DialogueEvent | 1572 | 0.001 | 3.942 | 604.357 | 31.025 | 505882.936 | 0.1 | 417 | 9 |
| PlayerPositionEvent | 1347 | 9.723 | 10.001 | 650.991 | 10.154 | 505879.398 | 0.09 | 0 | 8 |
| ObjectInterEvent | 212 | 0.005 | 9.198 | 4479.9 | 284.835 | 594755.883 | 0.01 | 2 | 8 |
| argumentationNodeEvent | 100 | 0.022 | 0.48 | 7884.109 | 11.616 | 778499.313 | 0.01 | 11 | 2 |
| TopographicMapEvent | 65 | 0.032 | 3.441 | 12135.38 | 1359.834 | 613915.674 | 0.0 | 4 | 5 |
| Soil Key Puzzle | 61 | 0.036 | 2.961 | 14131.335 | 21.881 | 700814.694 | 0.0 | 1 | 3 |
| questEvent | 61 | 0.002 | 175.668 | 15573.248 | 84125.718 | 505934.166 | 0.0 | 10 | 13 |
| DEBUGMenu | 26 | 9.811 | 1089.561 | 36537.866 | 86246.012 | 505922.546 | 0.0 | 0 | 15 |
| gameWindowFocusEvent | 15 | 2.412 | 8642.227 | 63221.551 | 212279.229 | 505933.948 | 0.0 | 0 | 12 |
| gameStartEvent | 12 | 1124.891 | 42297.005 | 79026.737 | 275205.24 | 505933.948 | 0.0 | 0 | 12 |
| argumentationEvent | 8 | 0.037 | 63.418 | 98550.812 | 509401.803 | 778498.876 | 0.0 | 1 | 2 |
| DaniEvent | 7 | 0.536 | 2.087 | 112299.084 | 550256.507 | 786078.356 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 7 | 1317.552 | 83707.138 | 135360.695 | 441630.455 | 593301.97 | 0.0 | 0 | 7 |
| soilMachine | 7 | 1.244 | 3.037 | 54.924 | 159.125 | 185.246 | 1.09 | 0 | 0 |
| argumentationAnswerEvent | 3 | 105.241 | 9713.052 | 262796.606 | 701685.678 | 778571.525 | 0.0 | 0 | 2 |
| EndOfUnit | 2 | 10840.167 | 394721.272 | 394721.272 | 740214.266 | 778602.376 | 0.0 | 0 | 2 |
| argumentationToolEvent | 1 | 0.568 | 0.568 | 0.568 | 0.568 | 0.568 | 105.63 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 15 group(s), 28 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[2887] _id=6ac693cade269131f9be1202 ts=2026-10-07T18:47:36.7230000Z == 6ab9a9279a8420a1e6b56b80.jsonl[2888] _id=6ac693cade269131f9be1203 ts=2026-10-07T18:47:36.7230000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[2889] _id=6ac693cade269131f9be1204 ts=2026-10-07T18:47:36.7240000Z == 6ab9a9279a8420a1e6b56b80.jsonl[2890] _id=6ac693cade269131f9be1205 ts=2026-10-07T18:47:36.7240000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[3049] _id=6ac694aade269131f9be39fc ts=2026-10-07T18:51:22.6340000Z == 6ab9a9279a8420a1e6b56b80.jsonl[3050] _id=6ac694aade269131f9be39fd ts=2026-10-07T18:51:22.6340000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 105 group(s), 169 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1372] _id=6ac54597de269131f9b72cf5 ts=2026-10-06T19:01:42.4570000Z == 6ab9a9279a8420a1e6b56b80.jsonl[1373] _id=6ac54597de269131f9b72cf7 ts=2026-10-06T19:01:42.4570000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1375] _id=6ac54598de269131f9b72d01 ts=2026-10-06T19:01:42.6170000Z == 6ab9a9279a8420a1e6b56b80.jsonl[1376] _id=6ac54598de269131f9b72d08 ts=2026-10-06T19:01:42.6170000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1384] _id=6ac54599de269131f9b72d33 ts=2026-10-06T19:01:43.7080000Z == 6ab9a9279a8420a1e6b56b80.jsonl[1388] _id=6ac54599de269131f9b72d35 ts=2026-10-06T19:01:43.7080000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b80.jsonl[121] _id=6ac3f5d7de269131f9af6a03 ts=2026-10-05T19:09:10.1650000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[138] _id=6ac3f5d7de269131f9af6a05 ts=2026-10-05T19:09:10.1700000Z`; `5ms: 6ab9a9279a8420a1e6b56b80.jsonl[466] _id=6ac53ef1de269131f9b67f5d ts=2026-10-06T18:33:20.3130000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[467] _id=6ac53ef1de269131f9b67f5f ts=2026-10-06T18:33:20.3180000Z`; `177ms: 6ab9a9279a8420a1e6b56b80.jsonl[695] _id=6ac54143de269131f9b6c4e5 ts=2026-10-06T18:43:14.2620000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[697] _id=6ac54143de269131f9b6c4ed ts=2026-10-06T18:43:14.4390000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 175 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `70ms: 6ab9a9279a8420a1e6b56b80.jsonl[1378] _id=6ac54599de269131f9b72d1d ts=2026-10-06T19:01:42.6170000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[1379] _id=6ac54599de269131f9b72d23 ts=2026-10-06T19:01:42.6870000Z`; `65ms: 6ab9a9279a8420a1e6b56b80.jsonl[1444] _id=6ac54662de269131f9b741e9 ts=2026-10-06T19:04:39.4160000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[1445] _id=6ac54663de269131f9b741ec ts=2026-10-06T19:04:39.4810000Z`; `23ms: 6ab9a9279a8420a1e6b56b80.jsonl[1445] _id=6ac54663de269131f9b741ec ts=2026-10-06T19:04:39.4810000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[1450] _id=6ac54663de269131f9b741f3 ts=2026-10-06T19:04:39.5040000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: 6ab9a9279a8420a1e6b56b80.jsonl[2806] _id=6ac548eede269131f9b78e4b ts=2026-10-06T19:15:56.9090000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[2805] _id=6ac548eede269131f9b78e59 ts=2026-10-06T19:15:56.9410000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6ab9a9279a8420a1e6b56b80.jsonl[7084] _id=6ad14ac9de269131f9e1a5ec ts=2026-10-15T21:51:04.1620000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[7087] _id=6ad14ac9de269131f9e1a5ef ts=2026-10-15T21:51:04.1990000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6ab9a9279a8420a1e6b56b80.jsonl[928] _id=6ac5431ade269131f9b6ff67 ts=2026-10-06T18:51:04.9890000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[939] _id=6ac5431ade269131f9b6ff6c ts=2026-10-06T18:51:05.0160000Z`; `417ms: 6ab9a9279a8420a1e6b56b80.jsonl[6205] _id=6ad12493de269131f9dff590 ts=2026-10-15T19:08:02.3200000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[6253] _id=6ad12493de269131f9dff5a4 ts=2026-10-15T19:08:02.7370000Z`; `923ms: 6ab9a9279a8420a1e6b56b80.jsonl[6261] _id=6ad1249cde269131f9dff6fe ts=2026-10-15T19:08:11.3560000Z ~ 6ab9a9279a8420a1e6b56b80.jsonl[6262] _id=6ad1249dde269131f9dff724 ts=2026-10-15T19:08:12.2790000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 140h 32m 
  - Evidence: 140h 32m: 6ab9a9279a8420a1e6b56b80.jsonl[5118] _id=6ac930e5de269131f9cae5a1 ts=2026-10-09T18:22:28.6970000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5137] _id=6ad0e927de269131f9dbf378 ts=2026-10-15T14:54:31.2430000Z; 24h 0m: 6ab9a9279a8420a1e6b56b80.jsonl[2884] _id=6ac693c1de269131f9be1059 ts=2026-10-07T18:47:29.2590000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3796] _id=6ac7e54cde269131f9c586ca ts=2026-10-08T18:47:40.0710000Z; 23h 49m: 6ab9a9279a8420a1e6b56b80.jsonl[1177] _id=6ac544bade269131f9b71b9d ts=2026-10-06T18:58:01.2370000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2881] _id=6ac693b1de269131f9be0d56 ts=2026-10-07T18:47:12.8470000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 218h 21m 
  - Evidence: 218h 21m: 6ab9a9279a8420a1e6b56b80.jsonl[2835] _id=6ac5491fde269131f9b795b5 ts=2026-10-06T19:16:46.0470000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6526] _id=6ad147bdde269131f9e18e11 ts=2026-10-15T21:38:04.4030000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 140h 31m 
  - Evidence: 140h 31m: 6ab9a9279a8420a1e6b56b80.jsonl[5134] _id=6ac9311dde269131f9cae68c ts=2026-10-09T18:23:24.5630000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5144] _id=6ad0e939de269131f9dbf496 ts=2026-10-15T14:54:47.4990000Z; 23h 31m: 6ab9a9279a8420a1e6b56b80.jsonl[3778] _id=6ac69a7bde269131f9bf1b8a ts=2026-10-07T19:16:10.6400000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3808] _id=6ac7e55dde269131f9c5871d ts=2026-10-08T18:47:54.8310000Z; 23h 30m: 6ab9a9279a8420a1e6b56b80.jsonl[2879] _id=6ac54953de269131f9b79c7f ts=2026-10-06T19:17:38.3440000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2970] _id=6ac693fede269131f9be19fe ts=2026-10-07T18:48:30.0190000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 417 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b80.jsonl[2983] _id=6ac69410de269131f9be1dad ts=2026-10-07T18:48:47.6560000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2984] _id=6ac69410de269131f9be1dae ts=2026-10-07T18:48:47.6570000Z; 1ms: 6ab9a9279a8420a1e6b56b80.jsonl[4725] _id=6ac7e78bde269131f9c5ccb1 ts=2026-10-08T18:57:15.0480000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[4726] _id=6ac7e78bde269131f9c5ccb2 ts=2026-10-08T18:57:15.0490000Z; 1ms: 6ab9a9279a8420a1e6b56b80.jsonl[4867] _id=6ac7e94fde269131f9c615a7 ts=2026-10-08T19:04:46.5980000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[4868] _id=6ac7e94fde269131f9c615a8 ts=2026-10-08T19:04:46.5990000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 216h 16m 
  - Evidence: 216h 16m: 6ab9a9279a8420a1e6b56b80.jsonl[1167] _id=6ac54453de269131f9b715e9 ts=2026-10-06T18:56:19.0030000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6365] _id=6ad125bede269131f9e022c7 ts=2026-10-15T19:13:01.3790000Z; 3h 0m: 6ab9a9279a8420a1e6b56b80.jsonl[6365] _id=6ad125bede269131f9e022c7 ts=2026-10-15T19:13:01.3790000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[8361] _id=6ad15016de269131f9e1cd6e ts=2026-10-15T22:13:41.5460000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 140h 31m 
  - Evidence: 140h 31m: 6ab9a9279a8420a1e6b56b80.jsonl[5126] _id=6ac930f8de269131f9cae618 ts=2026-10-09T18:22:47.9190000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5139] _id=6ad0e939de269131f9dbf492 ts=2026-10-15T14:54:47.4780000Z; 23h 31m: 6ab9a9279a8420a1e6b56b80.jsonl[3769] _id=6ac69a71de269131f9bf1acb ts=2026-10-07T19:16:01.3490000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3805] _id=6ac7e55dde269131f9c5871b ts=2026-10-08T18:47:54.8120000Z; 23h 30m: 6ab9a9279a8420a1e6b56b80.jsonl[2865] _id=6ac5492dde269131f9b79781 ts=2026-10-06T19:17:00.3740000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2886] _id=6ac693cade269131f9be1201 ts=2026-10-07T18:47:36.7190000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 433 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b80.jsonl[10730] _id=6ad27356de269131f9e77b32 ts=2026-10-16T18:56:21.9520000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10731] _id=6ad27356de269131f9e77b33 ts=2026-10-16T18:56:21.9520000Z; 0ms: 6ab9a9279a8420a1e6b56b80.jsonl[10747] _id=6ad27355de269131f9e77b25 ts=2026-10-16T18:56:21.4560000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10748] _id=6ad27355de269131f9e77b26 ts=2026-10-16T18:56:21.4560000Z; 0ms: 6ab9a9279a8420a1e6b56b80.jsonl[10856] _id=6ad273b8de269131f9e78180 ts=2026-10-16T18:57:59.6740000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10857] _id=6ad273b8de269131f9e78181 ts=2026-10-16T18:57:59.6740000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 165h 12m 
  - Evidence: 165h 12m: 6ab9a9279a8420a1e6b56b80.jsonl[4445] _id=6ac7e620de269131f9c59966 ts=2026-10-08T18:51:11.4910000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5266] _id=6ad0f964de269131f9dd224a ts=2026-10-15T16:03:47.3740000Z; 24h 1m: 6ab9a9279a8420a1e6b56b80.jsonl[2629] _id=6ac54755de269131f9b763eb ts=2026-10-06T19:09:08.2250000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3582] _id=6ac6991dde269131f9befda6 ts=2026-10-07T19:10:21.7040000Z; 23h 39m: 6ab9a9279a8420a1e6b56b80.jsonl[3582] _id=6ac6991dde269131f9befda6 ts=2026-10-07T19:10:21.7040000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[4117] _id=6ac7e5edde269131f9c5921e ts=2026-10-08T18:50:20.7820000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b80.jsonl[121] _id=6ac3f5d7de269131f9af6a03 ts=2026-10-05T19:09:10.1650000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[138] _id=6ac3f5d7de269131f9af6a05 ts=2026-10-05T19:09:10.1700000Z; 5ms: 6ab9a9279a8420a1e6b56b80.jsonl[466] _id=6ac53ef1de269131f9b67f5d ts=2026-10-06T18:33:20.3130000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[467] _id=6ac53ef1de269131f9b67f5f ts=2026-10-06T18:33:20.3180000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 140h 31m 
  - Evidence: 140h 31m: 6ab9a9279a8420a1e6b56b80.jsonl[5133] _id=6ac9311cde269131f9cae68a ts=2026-10-09T18:23:23.4850000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5138] _id=6ad0e939de269131f9dbf491 ts=2026-10-15T14:54:42.8830000Z; 23h 30m: 6ab9a9279a8420a1e6b56b80.jsonl[3788] _id=6ac69ab3de269131f9bf2035 ts=2026-10-07T19:17:07.3500000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3804] _id=6ac7e55dde269131f9c5871a ts=2026-10-08T18:47:50.4640000Z; 23h 29m: 6ab9a9279a8420a1e6b56b80.jsonl[2880] _id=6ac54957de269131f9b79c9f ts=2026-10-06T19:17:42.8890000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2885] _id=6ac693cade269131f9be1200 ts=2026-10-07T18:47:29.2770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 170h 58m 
  - Evidence: 170h 58m: 6ab9a9279a8420a1e6b56b80.jsonl[4656] _id=6ac7e75dde269131f9c5c3ac ts=2026-10-08T18:56:28.2280000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[7301] _id=6ad14bcdde269131f9e1acb1 ts=2026-10-15T21:55:23.4040000Z; 24h 7m: 6ab9a9279a8420a1e6b56b80.jsonl[2579] _id=6ac54720de269131f9b760c7 ts=2026-10-06T19:08:13.4090000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3709] _id=6ac69a5ade269131f9bf1819 ts=2026-10-07T19:15:37.6040000Z; 23h 30m: 6ab9a9279a8420a1e6b56b80.jsonl[3790] _id=6ac69ab7de269131f9bf2063 ts=2026-10-07T19:17:10.1270000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3801] _id=6ac7e55dde269131f9c58725 ts=2026-10-08T18:47:55.9740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 948 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b80.jsonl[10858] _id=6ad273bbde269131f9e781de ts=2026-10-16T18:58:01.9530000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10859] _id=6ad273bbde269131f9e781e0 ts=2026-10-16T18:58:01.9530000Z; 0ms: 6ab9a9279a8420a1e6b56b80.jsonl[10859] _id=6ad273bbde269131f9e781e0 ts=2026-10-16T18:58:01.9530000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10869] _id=6ad273bbde269131f9e781e4 ts=2026-10-16T18:58:01.9530000Z; 0ms: 6ab9a9279a8420a1e6b56b80.jsonl[10860] _id=6ad273bcde269131f9e781ec ts=2026-10-16T18:58:01.9530000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10872] _id=6ad273bcde269131f9e781f3 ts=2026-10-16T18:58:01.9530000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 194h 40m 
  - Evidence: 194h 40m: 6ab9a9279a8420a1e6b56b80.jsonl[3644] _id=6ac699e3de269131f9bf0d18 ts=2026-10-07T19:13:39.2820000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[7252] _id=6ad14b72de269131f9e1aa38 ts=2026-10-15T21:53:53.9760000Z; 24h 1m: 6ab9a9279a8420a1e6b56b80.jsonl[2631] _id=6ac54758de269131f9b76407 ts=2026-10-06T19:09:11.2210000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3586] _id=6ac6991dde269131f9befda2 ts=2026-10-07T19:10:21.6950000Z; 20h 41m: 6ab9a9279a8420a1e6b56b80.jsonl[7260] _id=6ad14b8ade269131f9e1aae2 ts=2026-10-15T21:54:17.9200000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[8561] _id=6ad26e7ede269131f9e713a8 ts=2026-10-16T18:35:42.0610000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.036s..0.036s shown 
  - Evidence: 36ms: 6ab9a9279a8420a1e6b56b80.jsonl[3445] _id=6ac69941de269131f9bf0024 ts=2026-10-07T19:10:57.1380000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3597] _id=6ac69941de269131f9bf002a ts=2026-10-07T19:10:57.1740000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 170h 31m 
  - Evidence: 170h 31m: 6ab9a9279a8420a1e6b56b80.jsonl[4906] _id=6ac7e9f7de269131f9c63879 ts=2026-10-08T19:07:34.3170000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6576] _id=6ad14812de269131f9e18fd9 ts=2026-10-15T21:39:29.9910000Z; 23h 58m: 6ab9a9279a8420a1e6b56b80.jsonl[3442] _id=6ac698b5de269131f9bef401 ts=2026-10-07T19:08:37.7920000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[4916] _id=6ac7e9e9de269131f9c63538 ts=2026-10-08T19:07:20.8240000Z; 23h 34m: 6ab9a9279a8420a1e6b56b80.jsonl[2818] _id=6ac548fdde269131f9b7909b ts=2026-10-06T19:16:12.4740000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3013] _id=6ac69486de269131f9be3323 ts=2026-10-07T18:50:45.9910000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.032s..0.038s shown 
  - Evidence: 32ms: 6ab9a9279a8420a1e6b56b80.jsonl[2806] _id=6ac548eede269131f9b78e4b ts=2026-10-06T19:15:56.9090000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2805] _id=6ac548eede269131f9b78e59 ts=2026-10-06T19:15:56.9410000Z; 34ms: 6ab9a9279a8420a1e6b56b80.jsonl[3019] _id=6ac69492de269131f9be35d4 ts=2026-10-07T18:50:58.0530000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3023] _id=6ac69492de269131f9be35d8 ts=2026-10-07T18:50:58.0870000Z; 38ms: 6ab9a9279a8420a1e6b56b80.jsonl[3014] _id=6ac69492de269131f9be35cc ts=2026-10-07T18:50:58.0150000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3019] _id=6ac69492de269131f9be35d4 ts=2026-10-07T18:50:58.0530000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 216h 16m 
  - Evidence: 216h 16m: 6ab9a9279a8420a1e6b56b80.jsonl[988] _id=6ac5438cde269131f9b70701 ts=2026-10-06T18:52:59.5680000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6288] _id=6ad124d8de269131f9e00068 ts=2026-10-15T19:09:11.0930000Z; 2h 41m: 6ab9a9279a8420a1e6b56b80.jsonl[6288] _id=6ad124d8de269131f9e00068 ts=2026-10-15T19:09:11.0930000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[7089] _id=6ad14ac8de269131f9e1a5ea ts=2026-10-15T21:51:04.1450000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 216h 14m 
  - Evidence: 216h 14m: 6ab9a9279a8420a1e6b56b80.jsonl[985] _id=6ac5438cde269131f9b70707 ts=2026-10-06T18:52:59.5970000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6249] _id=6ad1248fde269131f9dff4e3 ts=2026-10-15T19:07:58.4730000Z; 2h 40m: 6ab9a9279a8420a1e6b56b80.jsonl[6289] _id=6ad124d8de269131f9e0006c ts=2026-10-15T19:09:11.1120000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[7045] _id=6ad14a8ade269131f9e1a4c5 ts=2026-10-15T21:50:01.2090000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.037s..0.037s shown 
  - Evidence: 37ms: 6ab9a9279a8420a1e6b56b80.jsonl[7084] _id=6ad14ac9de269131f9e1a5ec ts=2026-10-15T21:51:04.1620000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[7087] _id=6ad14ac9de269131f9e1a5ef ts=2026-10-15T21:51:04.1990000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 216h 14m 
  - Evidence: 216h 14m: 6ab9a9279a8420a1e6b56b80.jsonl[984] _id=6ac5438bde269131f9b706e7 ts=2026-10-06T18:52:58.2380000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6244] _id=6ad1248ede269131f9dff4b1 ts=2026-10-15T19:07:57.5510000Z; 2h 40m: 6ab9a9279a8420a1e6b56b80.jsonl[6285] _id=6ad124d5de269131f9e0002e ts=2026-10-15T19:09:08.5220000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[7022] _id=6ad14a8bde269131f9e1a4d5 ts=2026-10-15T21:50:02.2690000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.022s..0.025s shown 
  - Evidence: 22ms: 6ab9a9279a8420a1e6b56b80.jsonl[6276] _id=6ad124bcde269131f9dffbb3 ts=2026-10-15T19:08:43.0100000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6277] _id=6ad124bcde269131f9dffbc1 ts=2026-10-15T19:08:43.0320000Z; 23ms: 6ab9a9279a8420a1e6b56b80.jsonl[6279] _id=6ad124bede269131f9dffc2b ts=2026-10-15T19:08:45.9910000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6278] _id=6ad124bfde269131f9dffc33 ts=2026-10-15T19:08:46.0140000Z; 25ms: 6ab9a9279a8420a1e6b56b80.jsonl[6265] _id=6ad124a0de269131f9dff7bc ts=2026-10-15T19:08:15.9940000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[6259] _id=6ad124a1de269131f9dff7c5 ts=2026-10-15T19:08:16.0190000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 140h 32m 
  - Evidence: 140h 32m: 6ab9a9279a8420a1e6b56b80.jsonl[5117] _id=6ac930dade269131f9cae560 ts=2026-10-09T18:22:17.6240000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5136] _id=6ad0e927de269131f9dbf37d ts=2026-10-15T14:54:31.5720000Z; 24h 0m: 6ab9a9279a8420a1e6b56b80.jsonl[2883] _id=6ac693b1de269131f9be0d71 ts=2026-10-07T18:47:13.0070000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3798] _id=6ac7e54cde269131f9c586cc ts=2026-10-08T18:47:40.2140000Z; 23h 49m: 6ab9a9279a8420a1e6b56b80.jsonl[1173] _id=6ac544a7de269131f9b71a00 ts=2026-10-06T18:57:41.9140000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2883] _id=6ac693b1de269131f9be0d71 ts=2026-10-07T18:47:13.0070000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 140h 32m 
  - Evidence: 140h 32m: 6ab9a9279a8420a1e6b56b80.jsonl[5116] _id=6ac930dade269131f9cae55f ts=2026-10-09T18:22:17.6240000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5135] _id=6ad0e927de269131f9dbf37c ts=2026-10-15T14:54:31.5720000Z; 24h 0m: 6ab9a9279a8420a1e6b56b80.jsonl[2882] _id=6ac693b1de269131f9be0d70 ts=2026-10-07T18:47:13.0070000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3797] _id=6ac7e54cde269131f9c586cb ts=2026-10-08T18:47:40.2140000Z; 23h 49m: 6ab9a9279a8420a1e6b56b80.jsonl[1172] _id=6ac544a6de269131f9b719fb ts=2026-10-06T18:57:41.9080000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2882] _id=6ac693b1de269131f9be0d70 ts=2026-10-07T18:47:13.0070000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 164h 48m 
  - Evidence: 164h 48m: 6ab9a9279a8420a1e6b56b80.jsonl[5110] _id=6ac930dade269131f9cae55c ts=2026-10-08T19:17:21.891Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5371] _id=6ad11c9ede269131f9deeeb8 ts=2026-10-15T16:05:43.861Z; 24h 22m: 6ab9a9279a8420a1e6b56b80.jsonl[1102] _id=6ac5440bde269131f9b71133 ts=2026-10-06T18:55:06.3320000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3800] _id=6ac7e54cde269131f9c586c6 ts=2026-10-07T19:17:16.585Z; 24h 0m: 6ab9a9279a8420a1e6b56b80.jsonl[3800] _id=6ac7e54cde269131f9c586c6 ts=2026-10-07T19:17:16.585Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5110] _id=6ac930dade269131f9cae55c ts=2026-10-08T19:17:21.891Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 140h 32m 
  - Evidence: 140h 32m: 6ab9a9279a8420a1e6b56b80.jsonl[5115] _id=6ac930eade269131f9cae5ba ts=2026-10-09T18:22:33.3790000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[5146] _id=6ad0e939de269131f9dbf498 ts=2026-10-15T14:54:47.5450000Z; 23h 37m: 6ab9a9279a8420a1e6b56b80.jsonl[3561] _id=6ac69910de269131f9befc82 ts=2026-10-07T19:10:07.9020000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3810] _id=6ac7e55dde269131f9c5871f ts=2026-10-08T18:47:54.8740000Z; 23h 32m: 6ab9a9279a8420a1e6b56b80.jsonl[2793] _id=6ac548d4de269131f9b78a49 ts=2026-10-06T19:15:31.6320000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[2892] _id=6ac693cade269131f9be1207 ts=2026-10-07T18:47:36.7940000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6ab9a9279a8420a1e6b56b80.jsonl[3810] _id=6ac7e55dde269131f9c5871f ts=2026-10-08T18:47:54.8740000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[3811] _id=6ac7e55dde269131f9c58720 ts=2026-10-08T18:47:54.8760000Z; 2ms: 6ab9a9279a8420a1e6b56b80.jsonl[897] _id=6ac542b5de269131f9b6f3d7 ts=2026-10-06T18:49:23.8190000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[881] _id=6ac542b5de269131f9b6f3e4 ts=2026-10-06T18:49:23.8210000Z; 6ms: 6ab9a9279a8420a1e6b56b80.jsonl[10264] _id=6ad27236de269131f9e7645c ts=2026-10-16T18:51:33.9150000Z -> 6ab9a9279a8420a1e6b56b80.jsonl[10265] _id=6ad27236de269131f9e76466 ts=2026-10-16T18:51:33.9210000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[826] _id=6ac5429cde269131f9b6f117 ts=2026-10-06T18:48:59.7350000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[930] _id=6ac543a9de269131f9b70907 ts=2026-10-06T18:53:28.6030000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[3187] _id=6ac697b3de269131f9bed30e ts=2026-10-07T19:04:19.7090000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 40 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1687] _id=6ac5466ade269131f9b743b5 ts=2026-10-06T19:05:07.8270000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1694] _id=6ac5466ade269131f9b743b9 ts=2026-10-06T19:05:08.5190000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1695] _id=6ac5466ade269131f9b743bf ts=2026-10-06T19:05:08.5310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 149 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1460] _id=6ac5465dde269131f9b740ff ts=2026-10-06T19:04:31.2780000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1472] _id=6ac5465dde269131f9b7410b ts=2026-10-06T19:04:31.2780000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1585] _id=6ac5465dde269131f9b7411b ts=2026-10-06T19:04:31.3510000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[7087] _id=6ad14ac9de269131f9e1a5ef ts=2026-10-15T21:51:04.1990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[939] _id=6ac5431ade269131f9b6ff6c ts=2026-10-06T18:51:05.0160000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 108 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1769] _id=6ac5467bde269131f9b7465d ts=2026-10-06T19:05:28.6440000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1817] _id=6ac54688de269131f9b74861 ts=2026-10-06T19:05:42.1030000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1802] _id=6ac54688de269131f9b74863 ts=2026-10-06T19:05:42.9760000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 316 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1373] _id=6ac54597de269131f9b72cf7 ts=2026-10-06T19:01:42.4570000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1375] _id=6ac54598de269131f9b72d01 ts=2026-10-06T19:01:42.6170000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1376] _id=6ac54598de269131f9b72d08 ts=2026-10-06T19:01:42.6170000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[2806] _id=6ac548eede269131f9b78e4b ts=2026-10-06T19:15:56.9090000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[2805] _id=6ac548eede269131f9b78e59 ts=2026-10-06T19:15:56.9410000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[3013] _id=6ac69486de269131f9be3323 ts=2026-10-07T18:50:45.9910000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 280 start, 270 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 28 unmatched 'BecameCameraCentered' (totals: 377 open, 389 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 64 unmatched 'BecameVisible' (totals: 590 open, 675 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 18 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 38 start, 24 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 359 of 10921 adjacent _id pairs reverse in client time; worst 216.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b80.jsonl[1581] _id=6ac5465ade269131f9b740b7 ts=2026-10-06T19:04:57.8130000Z`; `6ab9a9279a8420a1e6b56b80.jsonl[1570] _id=6ac5465bde269131f9b740c7 ts=2026-10-06T19:01:20.9720000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.91s, min -84624.24s, max -0.14s over 10922 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b80\coverage.yaml

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
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `InputEvent` — 5361 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2010); Unit 4 Dev - Dungeon (1337); Unit 3 Dev (650); Unit 1 Dev (596); Unit 3 Dungeon Dev (439); Unit 4 Dev (329)
- **Intervals:** median 0.36s (p5 0.01s / p95 3.83s, n=5360)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5361/5361 records)
    "pressed"  x5361
data.actionType  (string, 5361/5361 records)
    "Move"  x4093
    "Interact"  x516
    "Sprint"  x244
    "Jump"  x221
    "Hoverboard"  x147
    "Ascend"  x118
    "Map"  x14
    "Pause"  x8
data.key  (string, 5361/5361 records, 2 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5361/5361 records)
    "Player"  x4691
    "Drone"  x670
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2031 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1465); Unit 4 Dev (442); Unit 3 Dungeon Dev (124)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.71s, n=2030)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2031/2031 records)
    "BecameInvisible"  x675
    "BecameVisible"  x590
    "BecameCameraUncentered"  x389
    "BecameCameraCentered"  x377
data.pieceId  (string, 2031/2031 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2031/2031 records)
    1226 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1573 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (750); Unit 3 Dev (303); Unit 1 Dev (244); Unit 3 Dungeon Dev (116); Unit 4 Dev - Dungeon (103); Unit 4 Dev (57)
- **eventKey:** present on 1023 of 1573 records
- **Intervals:** median 3.94s (p5 0.01s / p95 31.03s, n=1572)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1023; [conversationId, dialogueEventType] x550
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1573/1573 records)
    numeric range 8 .. 111 (40 unique)
data.dialogueEventType  (string, 1573/1573 records)
    "DialogueNodeEvent"  x1023
    "DialogueStartEvent"  x280
    "DialogueFinishEvent"  x270
data.nodeId  (number, 1023/1573 records)
    numeric range 0 .. 290 (222 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1355 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (720); Unit 1 Dev (222); Unit 3 Dev (174); Unit 4 Dev - Dungeon (111); Unit 3 Dungeon Dev (64); Unit 4 Dev (64)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.15s, n=1347)
- **Fields under `data`:**

```text
data.position  (object, 1355/1355 records)
data.position.x  (number, 1355/1355 records)
    numeric range -677.666 .. 1505.63 (393 unique)
data.position.y  (number, 1355/1355 records)
    numeric range -112.489 .. 157.797 (309 unique)
data.position.z  (number, 1355/1355 records)
    numeric range -1035.6 .. 1901.63 (392 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 213 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (75); Unit 2 Prod (Refactor) (62); Unit 3 Dungeon Dev (32); Unit 1 Dev (24); Unit 3 Dev (11); Unit 4 Dev (9)
- **Intervals:** median 9.20s (p5 0.22s / p95 284.83s, n=212)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 213/213 records)
    30 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 213/213 records)
    80 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 101 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (37); Unit 2 Prod (Refactor) (37); Unit 3 Dev (27)
- **Intervals:** median 0.48s (p5 0.03s / p95 11.62s, n=100)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 101/101 records)
    "argumentationNodeHoverEnd"  x45
    "argumentationNodeHoverStart"  x44
    "argumentationNodeAdd"  x11
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 101/101 records)
    "Unit 2 – Watershed"  x37
    "Unit 3 - Pollution Upstream"  x27
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x18
data.nodeName  (string, 101/101 records)
    "I"  x26
    "1"  x25
    "A"  x20
    "II"  x11
    "B"  x6
    "C"  x4
    "5"  x3
    "2"  x2
    "3"  x2
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 66 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (49); Unit 3 Dev (17)
- **Intervals:** median 3.44s (p5 0.19s / p95 1359.83s, n=65)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, legendName] x22; [actionType, featureUsed, location] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 66/66 records)
    "MapOpenEvent"  x18
    "MapCloseEvent"  x16
    "Selected"  x15
    "Unselected"  x7
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x3
data.featureUsed  (string, 66/66 records)
    "Map"  x34
    "Legend"  x22
    "Waypoint"  x10
data.legendName  (string, 22/66 records)
    "0 ft"  x4
    "Water"  x4
    "120 ft"  x2
    "210 ft"  x2
    "30 ft"  x2
    "330 ft"  x2
    "360 ft"  x2
    "180 ft"  x1
    "240 ft"  x1
    "270 ft"  x1
    "90 ft"  x1
data.location  (object, 10/66 records)
data.location.x  (number, 10/66 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 10/66 records)
    9 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 10/66 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 62 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (48); Unit 3 Dev (8); Unit 4 Dev (6)
- **Intervals:** median 2.96s (p5 0.17s / p95 21.88s, n=61)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x54; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/62 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/62 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 54/62 records)
    "RightDrag"  x30
    "LeftDrag"  x24
data.currentSoilType  (string, 54/62 records)
    "SAND"  x12
    "CLAYSAND"  x11
    "CLAY"  x10
    "SANDGRAVEL"  x9
    "CLAYROCK"  x7
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 54/62 records)
    "false"  x40
    "true"  x14
data.waterLevelStatus  (string, 54/62 records)
    "TooHigh"  x27
    "Proper"  x15
    "TooLow"  x12
data.waterRetentionChange  (string, 54/62 records)
    "Increase"  x25
    "Decrease"  x15
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 62 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 1 Dev (17); Unit 3 Dev (10); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (2); Unit 4 Dev (2)
- **eventKey:** present on 62 of 62 records
- **Intervals:** median 175.67s (p5 0.01s / p95 84125.72s, n=61)
- **`data` key-set variants:** [questEventType, questID, questName] x38; [questEventType, questID, questName, questSuccessOrFailure] x24
- **Fields under `data`:**

```text
data.questEventType  (string, 62/62 records)
    "questActiveEvent"  x38
    "questFinishEvent"  x24
data.questID  (string, 62/62 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 62/62 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 24/62 records)
    "Succeeded"  x24
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 27 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (8); Unit 3 Dev (3); Unit 1 Dev (2); Unit 4 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1089.56s (p5 10.59s / p95 86246.01s, n=26)
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "DebugMenuStateChanged"  x27
data.isOpened  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 16 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 1 Dev (2)
- **Intervals:** median 8642.23s (p5 38.70s / p95 212279.23s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 42297.00s (p5 1181.57s / p95 275205.24s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 63.42s (p5 7.21s / p95 509401.80s, n=8)
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

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (2)
- **Intervals:** median 2.09s (p5 0.54s / p95 550256.51s, n=7)
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

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (3); MainMenu (1); Unit 3 Dev (1)
- **Intervals:** median 83707.14s (p5 4373.57s / p95 441630.45s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 3.04s (p5 1.30s / p95 159.13s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Gravel"  x4
    "Clay"  x2
    "Sand"  x2
data.floor  (string, 8/8 records)
    "4"  x5
    "5"  x2
    "3"  x1
data.machine  (string, 8/8 records)
    "1"  x7
    "2"  x1
data.row  (string, 8/8 records)
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 4 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 9713.05s (p5 1066.02s / p95 701685.68s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "submitAnswerEvent"  x4
data.answerSubmitted  (string, 4/4 records)
    "A,1,"  x1
    "A,1,I"  x1
    "A,1,II"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 394721.27s (p5 49228.28s / p95 740214.27s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 0.57s (p5 0.57s / p95 0.57s, n=1)
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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (48 records)
- `TopographicMapEvent` data.actionType: "Selected" (15x); "Unselected" (7x); "WaypointMoveEvent" (7x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (22x); "Waypoint" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*