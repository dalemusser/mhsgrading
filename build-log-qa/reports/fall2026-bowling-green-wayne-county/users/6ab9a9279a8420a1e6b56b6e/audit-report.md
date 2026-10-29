# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b6e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b6e
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b6e.jsonl
- **Records:** 10422 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b6e
- **Time span:** 2026-10-06T18:31:58.107000+00:00 .. 2026-10-19T16:08:11.427000+00:00 (309h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b6e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **18 event types**, 10422 records, 6 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 91 INFO, 2 NOT_TESTED, 70 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3896 | 37.38 | 1 | 5 | 0 | 2026-10-06T18:32:11.029000+00:00 | 2026-10-16T18:56:59.899000+00:00 | 240h 24m |
| PuzzlePieceVisibleEvent | 2862 | 27.46 | 1 | 2 | 0 | 2026-10-06T19:11:32.066000+00:00 | 2026-10-16T18:35:10.979000+00:00 | 239h 23m |
| DialogueEvent | 1567 | 15.04 | 1 | 5 | 999 | 2026-10-06T18:32:27.570000+00:00 | 2026-10-19T16:05:26.233000+00:00 | 309h 32m |
| PlayerPositionEvent | 1443 | 13.85 | 1 | 5 | 0 | 2026-10-06T18:32:07.585000+00:00 | 2026-10-19T16:08:11.427000+00:00 | 309h 36m |
| ObjectInterEvent | 186 | 1.78 | 1 | 4 | 0 | 2026-10-06T18:39:14.903000+00:00 | 2026-10-16T18:56:16.941000+00:00 | 240h 17m |
| argumentationNodeEvent | 174 | 1.67 | 1 | 3 | 0 | 2026-10-06T18:59:28.027000+00:00 | 2026-10-15T19:04:46.981000+00:00 | 216h 5m |
| TopographicMapEvent | 72 | 0.69 | 1 | 2 | 0 | 2026-10-06T19:12:06.773000+00:00 | 2026-10-16T18:51:22.447000+00:00 | 239h 39m |
| questEvent | 52 | 0.5 | 1 | 4 | 52 | 2026-10-06T18:32:27.546000+00:00 | 2026-10-16T18:56:25.101000+00:00 | 240h 23m |
| Soil Key Puzzle | 50 | 0.48 | 1 | 2 | 0 | 2026-10-08T19:01:34.877000+00:00 | 2026-10-15T19:08:36.941000+00:00 | 168h 7m |
| DEBUGMenu | 32 | 0.31 | 1 | 6 | 0 | 2026-10-06T18:32:07.567000+00:00 | 2026-10-19T16:05:09.630000+00:00 | 309h 33m |
| gameWindowFocusEvent | 17 | 0.16 | 1 | 2 | 0 | 2026-10-06T18:31:58.107000+00:00 | 2026-10-19T16:04:59.528000+00:00 | 309h 33m |
| argumentationAnswerEvent | 16 | 0.15 | 1 | 3 | 0 | 2026-10-06T18:59:39.097000+00:00 | 2026-10-15T19:04:48.411000+00:00 | 216h 5m |
| gameStartEvent | 16 | 0.15 | 1 | 1 | 0 | 2026-10-06T18:31:58.108000+00:00 | 2026-10-19T16:04:59.528000+00:00 | 309h 33m |
| DaniEvent | 14 | 0.13 | 1 | 2 | 0 | 2026-10-08T18:54:47.067000+00:00 | 2026-10-16T18:49:53.624000+00:00 | 191h 55m |
| argumentationEvent | 9 | 0.09 | 1 | 3 | 0 | 2026-10-06T18:59:24.758000+00:00 | 2026-10-15T19:04:48.473000+00:00 | 216h 5m |
| argumentationToolEvent | 7 | 0.07 | 1 | 1 | 0 | 2026-10-06T18:59:17.275000+00:00 | 2026-10-06T19:01:28.259000+00:00 | 2m 10s |
| gameWindowUnfocusEvent | 6 | 0.06 | 1 | 3 | 0 | 2026-10-06T19:17:46.051000+00:00 | 2026-10-16T16:09:15.979000+00:00 | 236h 51m |
| EndOfUnit | 3 | 0.03 | 1 | 3 | 0 | 2026-10-06T19:04:46.127000+00:00 | 2026-10-16T18:56:33.039000+00:00 | 239h 51m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 431753.456s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.078s median 
  - Expected: 0.018s in 09-23-26 
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
  - Observed: 23.172s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.971s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 17675.761s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 13231.359s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 84239.24s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 14 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.waterLevelStatus` — baseline categorical value(s) not seen this build. 
  - Observed: TooLow 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,3,I; B,1,I; C,1,I; D,1,II; D,C,1,I 
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
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[180] _id=6ac540e2de269131f9b6b989 ts=2026-10-06T18:41:37.8880000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[2] _id=6ac54226de269131f9b6e15c ts=2026-10-06T18:47:01.8510000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[263] _id=6ac54271de269131f9b6eb31 ts=2026-10-06T18:48:16.2470000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[4] _id=6ac53e9ede269131f9b67843 ts=2026-10-06T18:31:58.1080000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[587] _id=6ac546a3de269131f9b74cab ts=2026-10-06T19:06:10.5440000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[1208] _id=6ac54902de269131f9b79119 ts=2026-10-06T19:16:17.0320000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[5] _id=6ac53e9ede269131f9b67841 ts=2026-10-06T18:31:58.1070000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[589] _id=6ac546a3de269131f9b74ca5 ts=2026-10-06T19:06:10.5430000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[1207] _id=6ac54901de269131f9b79116 ts=2026-10-06T19:16:17.0290000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[1244] _id=6ac693f5de269131f9be186c ts=2026-10-06T19:17:46.051Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[2866] _id=6ac7e576de269131f9c588a0 ts=2026-10-07T19:17:16.18Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[5528] _id=6acfd55fde269131f9d8849f ts=2026-10-14T19:17:50.2820000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 6 of 72 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[715] _id=6ac54807de269131f9b77059 ts=2026-10-06T19:12:06.7730000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[730] _id=6ac54839de269131f9b77509 ts=2026-10-06T19:12:56.9500000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[1326] _id=6ac694c0de269131f9be3e37 ts=2026-10-07T18:51:43.3460000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3895 | 0.0 | 0.422 | 222.205 | 10.422 | 498538.476 | 0.27 | 277 | 8 |
| PuzzlePieceVisibleEvent | 2861 | 0.0 | 0.078 | 301.23 | 2.022 | 498733.704 | 0.2 | 1140 | 8 |
| DialogueEvent | 1566 | 0.0 | 3.739 | 711.608 | 27.876 | 498436.4 | 0.08 | 444 | 10 |
| PlayerPositionEvent | 1435 | 9.825 | 10.002 | 741.428 | 10.156 | 498336.6 | 0.08 | 0 | 8 |
| ObjectInterEvent | 185 | 0.006 | 9.889 | 4675.795 | 378.089 | 516925.976 | 0.01 | 1 | 9 |
| argumentationNodeEvent | 173 | 0.007 | 0.657 | 4496.641 | 13.688 | 690867.931 | 0.01 | 14 | 2 |
| TopographicMapEvent | 71 | 0.021 | 3.326 | 12151.488 | 84932.789 | 500263.854 | 0.0 | 1 | 7 |
| questEvent | 51 | 0.002 | 257.468 | 16969.364 | 84269.251 | 498504.234 | 0.0 | 3 | 15 |
| Soil Key Puzzle | 49 | 0.005 | 1.145 | 12351.471 | 11.52 | 605097.655 | 0.0 | 1 | 1 |
| DEBUGMenu | 31 | 8.849 | 759.028 | 35947.808 | 166960.47 | 500092.693 | 0.0 | 0 | 18 |
| gameWindowFocusEvent | 16 | 537.009 | 13231.359 | 69648.839 | 311693.302 | 500104.074 | 0.0 | 0 | 15 |
| argumentationAnswerEvent | 15 | 3.306 | 23.172 | 51860.621 | 267947.964 | 690905.429 | 0.0 | 0 | 2 |
| gameStartEvent | 15 | 606.488 | 17675.761 | 74292.095 | 324254.021 | 500104.074 | 0.0 | 0 | 15 |
| DaniEvent | 13 | 0.006 | 3.553 | 53146.658 | 293321.964 | 604019.777 | 0.0 | 2 | 2 |
| argumentationEvent | 8 | 0.045 | 99.356 | 97240.464 | 479387.61 | 690867.261 | 0.0 | 1 | 2 |
| argumentationToolEvent | 6 | 0.009 | 0.971 | 21.831 | 92.399 | 120.731 | 2.75 | 1 | 0 |
| gameWindowUnfocusEvent | 5 | 26739.775 | 84239.24 | 170537.986 | 501141.307 | 604834.102 | 0.0 | 0 | 5 |
| EndOfUnit | 2 | 172429.522 | 431753.456 | 431753.456 | 665144.997 | 691077.39 | 0.0 | 0 | 2 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 15 group(s), 35 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[1247] _id=6ac69409de269131f9be1c55 ts=2026-10-07T18:48:40.0310000Z == 6ab9a9279a8420a1e6b56b6e.jsonl[1248] _id=6ac69409de269131f9be1c56 ts=2026-10-07T18:48:40.0310000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[2869] _id=6ac7e586de269131f9c5898e ts=2026-10-08T18:48:35.7630000Z == 6ab9a9279a8420a1e6b56b6e.jsonl[2870] _id=6ac7e586de269131f9c5898f ts=2026-10-08T18:48:35.7630000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[2875] _id=6ac7e586de269131f9c58994 ts=2026-10-08T18:48:35.7640000Z == 6ab9a9279a8420a1e6b56b6e.jsonl[2876] _id=6ac7e586de269131f9c58995 ts=2026-10-08T18:48:35.7640000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 59 group(s), 91 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[685] _id=6ac547e4de269131f9b76ded ts=2026-10-06T19:11:32.0660000Z == 6ab9a9279a8420a1e6b56b6e.jsonl[686] _id=6ac547e5de269131f9b76df1 ts=2026-10-06T19:11:32.0660000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[687] _id=6ac547e5de269131f9b76dff ts=2026-10-06T19:11:32.0660000Z == 6ab9a9279a8420a1e6b56b6e.jsonl[688] _id=6ac547e5de269131f9b76e05 ts=2026-10-06T19:11:32.0660000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[689] _id=6ac547e6de269131f9b76e1b ts=2026-10-06T19:11:33.2440000Z == 6ab9a9279a8420a1e6b56b6e.jsonl[680] _id=6ac547e6de269131f9b76e21 ts=2026-10-06T19:11:33.2440000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 20 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a9279a8420a1e6b56b6e.jsonl[127] _id=6ac54053de269131f9b6a9c7 ts=2026-10-06T18:39:14.9030000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[129] _id=6ac54053de269131f9b6a9d1 ts=2026-10-06T18:39:14.9090000Z`; `611ms: 6ab9a9279a8420a1e6b56b6e.jsonl[1288] _id=6ac6947cde269131f9be316e ts=2026-10-07T18:50:35.9980000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[1296] _id=6ac6947dde269131f9be3186 ts=2026-10-07T18:50:36.6090000Z`; `349ms: 6ab9a9279a8420a1e6b56b6e.jsonl[1296] _id=6ac6947dde269131f9be3186 ts=2026-10-07T18:50:36.6090000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[1273] _id=6ac6947dde269131f9be3198 ts=2026-10-07T18:50:36.9580000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 74 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `132ms: 6ab9a9279a8420a1e6b56b6e.jsonl[692] _id=6ac547ecde269131f9b76e89 ts=2026-10-06T19:11:39.3190000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[693] _id=6ac547edde269131f9b76e8d ts=2026-10-06T19:11:39.4510000Z`; `18ms: 6ab9a9279a8420a1e6b56b6e.jsonl[705] _id=6ac547efde269131f9b76ec7 ts=2026-10-06T19:11:40.0920000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[709] _id=6ac547efde269131f9b76ec9 ts=2026-10-06T19:11:40.1100000Z`; `30ms: 6ab9a9279a8420a1e6b56b6e.jsonl[894] _id=6ac54887de269131f9b77e93 ts=2026-10-06T19:11:51.2000000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[895] _id=6ac54887de269131f9b77e95 ts=2026-10-06T19:11:51.2300000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `613ms: 6ab9a9279a8420a1e6b56b6e.jsonl[2808] _id=6ac699f4de269131f9bf0f1b ts=2026-10-07T19:13:55.8790000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[2800] _id=6ac699f5de269131f9bf0f2a ts=2026-10-07T19:13:56.4920000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6ab9a9279a8420a1e6b56b6e.jsonl[8023] _id=6ad123d1de269131f9dfd770 ts=2026-10-15T19:04:48.4280000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[8026] _id=6ad123d1de269131f9dfd773 ts=2026-10-15T19:04:48.4730000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `460ms: 6ab9a9279a8420a1e6b56b6e.jsonl[423] _id=6ac54510de269131f9b72129 ts=2026-10-06T18:59:28.0990000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[412] _id=6ac54511de269131f9b7213d ts=2026-10-06T18:59:28.5590000Z`; `824ms: 6ab9a9279a8420a1e6b56b6e.jsonl[414] _id=6ac54510de269131f9b72131 ts=2026-10-06T18:59:28.1630000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[425] _id=6ac54511de269131f9b7214d ts=2026-10-06T18:59:28.9870000Z`; `35ms: 6ab9a9279a8420a1e6b56b6e.jsonl[425] _id=6ac54511de269131f9b7214d ts=2026-10-06T18:59:28.9870000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[395] _id=6ac54511de269131f9b7214f ts=2026-10-06T18:59:29.0220000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `907ms: 6ab9a9279a8420a1e6b56b6e.jsonl[494] _id=6ac54587de269131f9b72ba3 ts=2026-10-06T19:01:26.4250000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[496] _id=6ac54588de269131f9b72bb7 ts=2026-10-06T19:01:27.3320000Z`; `936ms: 6ab9a9279a8420a1e6b56b6e.jsonl[488] _id=6ac54588de269131f9b72bb1 ts=2026-10-06T19:01:27.3230000Z ~ 6ab9a9279a8420a1e6b56b6e.jsonl[497] _id=6ac54588de269131f9b72bc9 ts=2026-10-06T19:01:28.2590000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 138h 54m 
  - Evidence: 138h 54m: 6ab9a9279a8420a1e6b56b6e.jsonl[2862] _id=6ac7e581de269131f9c58928 ts=2026-10-08T18:48:32.8870000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4110] _id=6acf86fdde269131f9d34c84 ts=2026-10-14T13:43:25.5800000Z; 69h 8m: 6ab9a9279a8420a1e6b56b6e.jsonl[10377] _id=6ad2737bde269131f9e77d75 ts=2026-10-16T18:56:58.5140000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10398] _id=6ad63fabde269131f9e99a1c ts=2026-10-19T16:04:59.3750000Z; 23h 37m: 6ab9a9279a8420a1e6b56b6e.jsonl[2732] _id=6ac69946de269131f9bf0064 ts=2026-10-07T19:11:01.6270000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2863] _id=6ac7e576de269131f9c588a2 ts=2026-10-08T18:48:21.7060000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 46m 
  - Evidence: 167h 46m: 6ab9a9279a8420a1e6b56b6e.jsonl[3022] _id=6ac7e6f9de269131f9c5b4a7 ts=2026-10-08T18:54:49.6510000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[6286] _id=6ad11e6ede269131f9df1991 ts=2026-10-15T18:41:49.4280000Z; 23h 56m: 6ab9a9279a8420a1e6b56b6e.jsonl[7678] _id=6ad12121de269131f9df7323 ts=2026-10-15T18:53:20.8520000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10230] _id=6ad271cfde269131f9e75d49 ts=2026-10-16T18:49:50.9410000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.006s..0.007s shown 
  - Evidence: 6ms: 6ab9a9279a8420a1e6b56b6e.jsonl[6659] _id=6ad11efcde269131f9df3156 ts=2026-10-15T18:44:12.3140000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[6656] _id=6ad11efdde269131f9df3161 ts=2026-10-15T18:44:12.3200000Z; 7ms: 6ab9a9279a8420a1e6b56b6e.jsonl[6654] _id=6ad11ef5de269131f9df2ff8 ts=2026-10-15T18:44:05.2890000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[6655] _id=6ad11ef5de269131f9df2ffe ts=2026-10-15T18:44:05.2960000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 138h 27m 
  - Evidence: 138h 27m: 6ab9a9279a8420a1e6b56b6e.jsonl[4105] _id=6ac7ec5ade269131f9c68769 ts=2026-10-08T19:17:45.8960000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4297] _id=6acf875ede269131f9d35432 ts=2026-10-14T13:45:02.2960000Z; 69h 8m: 6ab9a9279a8420a1e6b56b6e.jsonl[10383] _id=6ad2738cde269131f9e77e72 ts=2026-10-16T18:57:15.4840000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10404] _id=6ad63fc6de269131f9e99af6 ts=2026-10-19T16:05:26.1410000Z; 23h 32m: 6ab9a9279a8420a1e6b56b6e.jsonl[2861] _id=6ac69ab8de269131f9bf206b ts=2026-10-07T19:17:11.4440000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2923] _id=6ac7e5c2de269131f9c58dbf ts=2026-10-08T18:49:38.6250000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 444 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[5160] _id=6acfd0a4de269131f9d7c964 ts=2026-10-14T18:57:39.0380000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[5161] _id=6acfd0a4de269131f9d7c965 ts=2026-10-14T18:57:39.0380000Z; 1ms: 6ab9a9279a8420a1e6b56b6e.jsonl[10108] _id=6ad27095de269131f9e74418 ts=2026-10-16T18:44:37.2080000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10109] _id=6ad27095de269131f9e74419 ts=2026-10-16T18:44:37.2090000Z; 1ms: 6ab9a9279a8420a1e6b56b6e.jsonl[10145] _id=6ad270dfde269131f9e74a3f ts=2026-10-16T18:45:51.1070000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10146] _id=6ad270dfde269131f9e74a40 ts=2026-10-16T18:45:51.1080000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 57m 
  - Evidence: 191h 57m: 6ab9a9279a8420a1e6b56b6e.jsonl[585] _id=6ac5464ede269131f9b73f95 ts=2026-10-06T19:04:46.1270000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[5239] _id=6acfd1d4de269131f9d7eef7 ts=2026-10-14T19:02:43.5170000Z; 47h 53m: 6ab9a9279a8420a1e6b56b6e.jsonl[5239] _id=6acfd1d4de269131f9d7eef7 ts=2026-10-14T19:02:43.5170000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10374] _id=6ad27361de269131f9e77bee ts=2026-10-16T18:56:33.0390000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 138h 28m 
  - Evidence: 138h 28m: 6ab9a9279a8420a1e6b56b6e.jsonl[4048] _id=6ac7eba4de269131f9c672e5 ts=2026-10-08T19:14:43.9630000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4115] _id=6acf8710de269131f9d34dcc ts=2026-10-14T13:43:42.4390000Z; 23h 33m: 6ab9a9279a8420a1e6b56b6e.jsonl[2825] _id=6ac69a1dde269131f9bf12a7 ts=2026-10-07T19:14:36.4970000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2868] _id=6ac7e586de269131f9c5898d ts=2026-10-08T18:48:35.7610000Z; 23h 31m: 6ab9a9279a8420a1e6b56b6e.jsonl[1229] _id=6ac5493ade269131f9b799a1 ts=2026-10-06T19:17:14.0120000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1246] _id=6ac69409de269131f9be1c54 ts=2026-10-07T18:48:40.0290000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 277 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[10141] _id=6ad270dbde269131f9e749b3 ts=2026-10-16T18:45:46.7250000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10142] _id=6ad270dbde269131f9e749b4 ts=2026-10-16T18:45:46.7250000Z; 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[10142] _id=6ad270dbde269131f9e749b4 ts=2026-10-16T18:45:46.7250000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10143] _id=6ad270dbde269131f9e749b5 ts=2026-10-16T18:45:46.7250000Z; 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[1205] _id=6ac548eade269131f9b78da9 ts=2026-10-06T19:15:52.7690000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1206] _id=6ac54901de269131f9b7910a ts=2026-10-06T19:15:52.769Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 35m 
  - Evidence: 143h 35m: 6ab9a9279a8420a1e6b56b6e.jsonl[3887] _id=6ac7ea2cde269131f9c64477 ts=2026-10-08T19:08:28.5380000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4610] _id=6acfcd6bde269131f9d76f34 ts=2026-10-14T18:43:54.5140000Z; 24h 1m: 6ab9a9279a8420a1e6b56b6e.jsonl[2563] _id=6ac6969fde269131f9beaefe ts=2026-10-07T18:59:42.6230000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[3175] _id=6ac7e88fde269131f9c5f37b ts=2026-10-08T19:01:34.8830000Z; 23h 34m: 6ab9a9279a8420a1e6b56b6e.jsonl[1060] _id=6ac548e2de269131f9b78ca1 ts=2026-10-06T19:15:46.1350000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1279] _id=6ac69473de269131f9be2f91 ts=2026-10-07T18:50:26.8180000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 6ab9a9279a8420a1e6b56b6e.jsonl[127] _id=6ac54053de269131f9b6a9c7 ts=2026-10-06T18:39:14.9030000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[129] _id=6ac54053de269131f9b6a9d1 ts=2026-10-06T18:39:14.9090000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 138h 25m 
  - Evidence: 138h 25m: 6ab9a9279a8420a1e6b56b6e.jsonl[4101] _id=6ac7ec69de269131f9c68890 ts=2026-10-08T19:18:00.8090000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4114] _id=6acf8710de269131f9d34dcb ts=2026-10-14T13:43:37.4090000Z; 69h 5m: 6ab9a9279a8420a1e6b56b6e.jsonl[10395] _id=6ad273ffde269131f9e78616 ts=2026-10-16T18:59:10.7490000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10401] _id=6ad63fb8de269131f9e99a91 ts=2026-10-19T16:05:09.6420000Z; 23h 31m: 6ab9a9279a8420a1e6b56b6e.jsonl[2860] _id=6ac69ab3de269131f9bf2039 ts=2026-10-07T19:17:07.0520000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2867] _id=6ac7e586de269131f9c5898c ts=2026-10-08T18:48:32.8990000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 138h 32m 
  - Evidence: 138h 32m: 6ab9a9279a8420a1e6b56b6e.jsonl[3961] _id=6ac7eae2de269131f9c65cf5 ts=2026-10-08T19:11:29.2380000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4112] _id=6acf8710de269131f9d34dd8 ts=2026-10-14T13:43:42.9420000Z; 24h 23m: 6ab9a9279a8420a1e6b56b6e.jsonl[4760] _id=6acfcdffde269131f9d782e2 ts=2026-10-14T18:46:21.6460000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[8174] _id=6ad124e4de269131f9e00217 ts=2026-10-15T19:09:22.8310000Z; 24h 5m: 6ab9a9279a8420a1e6b56b6e.jsonl[2553] _id=6ac6967fde269131f9bea8e5 ts=2026-10-07T18:59:09.2880000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[3239] _id=6ac7e92ade269131f9c60dd5 ts=2026-10-08T19:04:09.6520000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1140 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[1004] _id=6ac548aade269131f9b78393 ts=2026-10-06T19:14:49.4310000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1005] _id=6ac548aade269131f9b78395 ts=2026-10-06T19:14:49.4310000Z; 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[1009] _id=6ac548acde269131f9b783e1 ts=2026-10-06T19:14:51.3460000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[840] _id=6ac548acde269131f9b783e3 ts=2026-10-06T19:14:51.3460000Z; 0ms: 6ab9a9279a8420a1e6b56b6e.jsonl[1031] _id=6ac548b3de269131f9b7853d ts=2026-10-06T19:14:58.0600000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1039] _id=6ac548b4de269131f9b78550 ts=2026-10-06T19:14:58.0600000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 168h 4m 
  - Evidence: 168h 4m: 6ab9a9279a8420a1e6b56b6e.jsonl[3208] _id=6ac7e8e1de269131f9c60025 ts=2026-10-08T19:02:57.1780000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[8122] _id=6ad1248bde269131f9dff426 ts=2026-10-15T19:07:54.8330000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b6e.jsonl[8132] _id=6ad12497de269131f9dff632 ts=2026-10-15T19:08:06.4900000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[8133] _id=6ad12497de269131f9dff646 ts=2026-10-15T19:08:06.4950000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 138h 57m 
  - Evidence: 138h 57m: 6ab9a9279a8420a1e6b56b6e.jsonl[3026] _id=6ac7e700de269131f9c5b561 ts=2026-10-08T18:54:55.9230000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4438] _id=6acf8927de269131f9d38840 ts=2026-10-14T13:52:39.7770000Z; 23h 54m: 6ab9a9279a8420a1e6b56b6e.jsonl[7692] _id=6ad12133de269131f9df74fc ts=2026-10-15T18:53:38.8170000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10190] _id=6ad2717dde269131f9e757a6 ts=2026-10-16T18:48:29.1150000Z; 23h 38m: 6ab9a9279a8420a1e6b56b6e.jsonl[730] _id=6ac54839de269131f9b77509 ts=2026-10-06T19:12:56.9500000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1326] _id=6ac694c0de269131f9be3e37 ts=2026-10-07T18:51:43.3460000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.021s..0.021s shown 
  - Evidence: 21ms: 6ab9a9279a8420a1e6b56b6e.jsonl[2802] _id=6ac699f1de269131f9bf0ef4 ts=2026-10-07T19:13:53.3300000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2806] _id=6ac699f1de269131f9bf0ef8 ts=2026-10-07T19:13:53.3510000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 55m 
  - Evidence: 191h 55m: 6ab9a9279a8420a1e6b56b6e.jsonl[489] _id=6ac54589de269131f9b72bd9 ts=2026-10-06T19:01:29.1830000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[5112] _id=6acfd063de269131f9d7c25f ts=2026-10-14T18:56:34.6120000Z; 24h 4m: 6ab9a9279a8420a1e6b56b6e.jsonl[5196] _id=6acfd0d7de269131f9d7cf07 ts=2026-10-14T18:58:30.6420000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[7955] _id=6ad1236fde269131f9dfc3f4 ts=2026-10-15T19:03:11.1210000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 54m 
  - Evidence: 191h 54m: 6ab9a9279a8420a1e6b56b6e.jsonl[478] _id=6ac5458ade269131f9b72be1 ts=2026-10-06T19:01:29.2140000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[5087] _id=6acfd03dde269131f9d7bdcc ts=2026-10-14T18:55:56.4750000Z; 24h 3m: 6ab9a9279a8420a1e6b56b6e.jsonl[5197] _id=6acfd0d7de269131f9d7cf0a ts=2026-10-14T18:58:30.6670000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[7917] _id=6ad12346de269131f9dfbdcb ts=2026-10-15T19:02:30.3550000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.045s..0.045s shown 
  - Evidence: 45ms: 6ab9a9279a8420a1e6b56b6e.jsonl[8023] _id=6ad123d1de269131f9dfd770 ts=2026-10-15T19:04:48.4280000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[8026] _id=6ad123d1de269131f9dfd773 ts=2026-10-15T19:04:48.4730000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 191h 54m 
  - Evidence: 191h 54m: 6ab9a9279a8420a1e6b56b6e.jsonl[492] _id=6ac54583de269131f9b72b34 ts=2026-10-06T19:01:22.6010000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[5082] _id=6acfd037de269131f9d7bd0e ts=2026-10-14T18:55:50.5320000Z; 24h 4m: 6ab9a9279a8420a1e6b56b6e.jsonl[5195] _id=6acfd0d5de269131f9d7ceda ts=2026-10-14T18:58:28.7770000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[7924] _id=6ad1234bde269131f9dfbe7c ts=2026-10-15T19:02:34.6570000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.007s..0.021s shown 
  - Evidence: 7ms: 6ab9a9279a8420a1e6b56b6e.jsonl[8020] _id=6ad123cede269131f9dfd6e6 ts=2026-10-15T19:04:46.0130000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[8021] _id=6ad123cede269131f9dfd6ed ts=2026-10-15T19:04:46.0200000Z; 8ms: 6ab9a9279a8420a1e6b56b6e.jsonl[422] _id=6ac54510de269131f9b72127 ts=2026-10-06T18:59:28.0910000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[423] _id=6ac54510de269131f9b72129 ts=2026-10-06T18:59:28.0990000Z; 21ms: 6ab9a9279a8420a1e6b56b6e.jsonl[433] _id=6ac54519de269131f9b721ff ts=2026-10-06T18:59:36.4520000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[420] _id=6ac54519de269131f9b72201 ts=2026-10-06T18:59:36.4730000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.009s..0.009s shown 
  - Evidence: 9ms: 6ab9a9279a8420a1e6b56b6e.jsonl[488] _id=6ac54588de269131f9b72bb1 ts=2026-10-06T19:01:27.3230000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[496] _id=6ac54588de269131f9b72bb7 ts=2026-10-06T19:01:27.3320000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 138h 55m 
  - Evidence: 138h 55m: 6ab9a9279a8420a1e6b56b6e.jsonl[2865] _id=6ac7e576de269131f9c588a4 ts=2026-10-08T18:48:21.8400000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4109] _id=6acf86fede269131f9d34c8f ts=2026-10-14T13:43:25.9140000Z; 69h 8m: 6ab9a9279a8420a1e6b56b6e.jsonl[10350] _id=6ad27372de269131f9e77ced ts=2026-10-16T18:56:49.8160000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10397] _id=6ad63facde269131f9e99a21 ts=2026-10-19T16:04:59.5280000Z; 23h 37m: 6ab9a9279a8420a1e6b56b6e.jsonl[2731] _id=6ac6993ade269131f9beffa5 ts=2026-10-07T19:10:49.6380000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2865] _id=6ac7e576de269131f9c588a4 ts=2026-10-08T18:48:21.8400000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 138h 55m 
  - Evidence: 138h 55m: 6ab9a9279a8420a1e6b56b6e.jsonl[2864] _id=6ac7e576de269131f9c588a3 ts=2026-10-08T18:48:21.8400000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4108] _id=6acf86fede269131f9d34c8e ts=2026-10-14T13:43:25.9140000Z; 69h 8m: 6ab9a9279a8420a1e6b56b6e.jsonl[10349] _id=6ad27372de269131f9e77cec ts=2026-10-16T18:56:49.8160000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[10396] _id=6ad63facde269131f9e99a20 ts=2026-10-19T16:04:59.5280000Z; 23h 37m: 6ab9a9279a8420a1e6b56b6e.jsonl[2728] _id=6ac6993ade269131f9beffa4 ts=2026-10-07T19:10:49.6380000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2864] _id=6ac7e576de269131f9c588a3 ts=2026-10-08T18:48:21.8400000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 168h 0m 
  - Evidence: 168h 0m: 6ab9a9279a8420a1e6b56b6e.jsonl[2866] _id=6ac7e576de269131f9c588a0 ts=2026-10-07T19:17:16.18Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[5528] _id=6acfd55fde269131f9d8849f ts=2026-10-14T19:17:50.2820000Z; 23h 59m: 6ab9a9279a8420a1e6b56b6e.jsonl[1244] _id=6ac693f5de269131f9be186c ts=2026-10-06T19:17:46.051Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2866] _id=6ac7e576de269131f9c588a0 ts=2026-10-07T19:17:16.18Z; 23h 23m: 6ab9a9279a8420a1e6b56b6e.jsonl[5528] _id=6acfd55fde269131f9d8849f ts=2026-10-14T19:17:50.2820000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[6288] _id=6ad11e6ede269131f9df1998 ts=2026-10-15T18:41:49.5220000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 138h 28m 
  - Evidence: 138h 28m: 6ab9a9279a8420a1e6b56b6e.jsonl[4062] _id=6ac7ebc6de269131f9c67632 ts=2026-10-08T19:15:18.2570000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[4122] _id=6acf8710de269131f9d34dd3 ts=2026-10-14T13:43:42.4910000Z; 23h 35m: 6ab9a9279a8420a1e6b56b6e.jsonl[2792] _id=6ac699d1de269131f9bf0bc3 ts=2026-10-07T19:13:20.4910000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[2882] _id=6ac7e586de269131f9c5899b ts=2026-10-08T18:48:35.8040000Z; 23h 32m: 6ab9a9279a8420a1e6b56b6e.jsonl[1213] _id=6ac54910de269131f9b79366 ts=2026-10-06T19:16:29.5240000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[1249] _id=6ac69409de269131f9be1c57 ts=2026-10-07T18:48:40.0680000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.007s shown 
  - Evidence: 2ms: 6ab9a9279a8420a1e6b56b6e.jsonl[389] _id=6ac544b6de269131f9b71b5f ts=2026-10-06T18:57:56.6830000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[390] _id=6ac544b6de269131f9b71b61 ts=2026-10-06T18:57:56.6850000Z; 7ms: 6ab9a9279a8420a1e6b56b6e.jsonl[141] _id=6ac54098de269131f9b6b0dd ts=2026-10-06T18:40:23.8120000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[142] _id=6ac54098de269131f9b6b0e3 ts=2026-10-06T18:40:23.8190000Z; 7ms: 6ab9a9279a8420a1e6b56b6e.jsonl[222] _id=6ac541d9de269131f9b6d5f7 ts=2026-10-06T18:45:45.0110000Z -> 6ab9a9279a8420a1e6b56b6e.jsonl[224] _id=6ac541d9de269131f9b6d5fb ts=2026-10-06T18:45:45.0180000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[378] _id=6ac544a0de269131f9b71999 ts=2026-10-06T18:57:35.3720000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[502] _id=6ac545acde269131f9b72e57 ts=2026-10-06T19:02:03.8180000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[2974] _id=6ac7e669de269131f9c5a38b ts=2026-10-08T18:52:24.8060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[982] _id=6ac548a3de269131f9b78289 ts=2026-10-06T19:14:40.9560000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[994] _id=6ac548a4de269131f9b782b3 ts=2026-10-06T19:14:43.0750000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[1119] _id=6ac548cfde269131f9b7896b ts=2026-10-06T19:15:25.5850000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 63 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[681] _id=6ac547e6de269131f9b76e2d ts=2026-10-06T19:11:33.2670000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[682] _id=6ac547e7de269131f9b76e33 ts=2026-10-06T19:11:33.2670000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[697] _id=6ac547eade269131f9b76e5f ts=2026-10-06T19:11:36.7340000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[8026] _id=6ad123d1de269131f9dfd773 ts=2026-10-15T19:04:48.4730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[395] _id=6ac54511de269131f9b7214f ts=2026-10-06T18:59:29.0220000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[418] _id=6ac54518de269131f9b721e9 ts=2026-10-06T18:59:35.4600000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[420] _id=6ac54519de269131f9b72201 ts=2026-10-06T18:59:36.4730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 197 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[978] _id=6ac548a1de269131f9b78217 ts=2026-10-06T19:14:40.5130000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[1011] _id=6ac548afde269131f9b7844d ts=2026-10-06T19:14:54.1380000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[1034] _id=6ac548b0de269131f9b78488 ts=2026-10-06T19:14:54.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 524 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[686] _id=6ac547e5de269131f9b76df1 ts=2026-10-06T19:11:32.0660000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[688] _id=6ac547e5de269131f9b76e05 ts=2026-10-06T19:11:32.0660000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[690] _id=6ac547e5de269131f9b76e0d ts=2026-10-06T19:11:32.0660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[494] _id=6ac54587de269131f9b72ba3 ts=2026-10-06T19:01:26.4250000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[496] _id=6ac54588de269131f9b72bb7 ts=2026-10-06T19:01:27.3320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 290 start, 278 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 19 unmatched 'BecameCameraCentered' (totals: 537 open, 521 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 61 unmatched 'BecameVisible' (totals: 901 open, 903 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 10 unmatched 'questActiveEvent' (totals: 31 start, 21 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 240 of 10421 adjacent _id pairs reverse in client time; worst 146.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b6e.jsonl[726] _id=6ac5487ede269131f9b77d4b ts=2026-10-06T19:14:06.1300000Z`; `6ab9a9279a8420a1e6b56b6e.jsonl[809] _id=6ac5487fde269131f9b77d53 ts=2026-10-06T19:11:39.8950000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.71s, min -84666.02s, max -0.10s over 10422 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b6e\coverage.yaml

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
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `InputEvent` — 3896 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2261); Unit 2 Prod (Refactor) (952); Unit 3 Dungeon Dev (580); Unit 1 Dev (102); Unit 4 Dev (1)
- **Intervals:** median 0.42s (p5 0.03s / p95 10.42s, n=3895)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3896/3896 records)
    "pressed"  x3896
data.actionType  (string, 3896/3896 records)
    "Move"  x2264
    "Interact"  x1254
    "Jump"  x145
    "Ascend"  x123
    "Sprint"  x64
    "Hoverboard"  x39
    "Map"  x5
    "Pause"  x1
    "ToggleDebug"  x1
data.key  (string, 3896/3896 records, 9 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3896/3896 records)
    "Drone"  x2230
    "Player"  x1666
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2862 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2156); Unit 3 Dungeon Dev (706)
- **Intervals:** median 0.08s (p5 0.00s / p95 2.02s, n=2861)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2862/2862 records)
    "BecameInvisible"  x903
    "BecameVisible"  x901
    "BecameCameraCentered"  x537
    "BecameCameraUncentered"  x521
data.pieceId  (string, 2862/2862 records)
    24 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2862/2862 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 1567 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (705); Unit 3 Dev (346); Unit 3 Dungeon Dev (310); Unit 1 Dev (200); Unit 4 Dev (6)
- **eventKey:** present on 999 of 1567 records
- **Intervals:** median 3.74s (p5 0.00s / p95 27.88s, n=1566)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x999; [conversationId, dialogueEventType] x568
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1567/1567 records)
    numeric range 8 .. 104 (37 unique)
data.dialogueEventType  (string, 1567/1567 records)
    "DialogueNodeEvent"  x999
    "DialogueStartEvent"  x290
    "DialogueFinishEvent"  x278
data.nodeId  (number, 999/1567 records)
    numeric range 0 .. 290 (215 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1443 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (624); Unit 3 Dev (354); Unit 3 Dungeon Dev (236); Unit 1 Dev (196); Unit 4 Dev (33)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.16s, n=1435)
- **Fields under `data`:**

```text
data.position  (object, 1443/1443 records)
data.position.x  (number, 1443/1443 records)
    numeric range -665.301 .. 1426.26 (457 unique)
data.position.y  (number, 1443/1443 records)
    numeric range -114.326 .. 163.972 (294 unique)
data.position.z  (number, 1443/1443 records)
    numeric range -1040.44 .. 2018.96 (457 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 186 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (94); Unit 2 Prod (Refactor) (70); Unit 3 Dev (12); Unit 1 Dev (10)
- **Intervals:** median 9.89s (p5 0.28s / p95 378.09s, n=185)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 186/186 records)
    20 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 186/186 records)
    52 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 174 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (65); Unit 3 Dev (59); Unit 1 Dev (50)
- **Intervals:** median 0.66s (p5 0.03s / p95 13.69s, n=173)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 174/174 records)
    "argumentationNodeHoverEnd"  x74
    "argumentationNodeHoverStart"  x71
    "argumentationNodeAdd"  x19
    "argumentationNodeRemove"  x10
data.argumentationTitle  (string, 174/174 records)
    "Unit 2 – Watershed"  x65
    "Unit 3 - Pollution Upstream"  x59
    "Unit 1 - Freshwater"  x33
    "Unit 1 - Argumentation Tutorial"  x17
data.nodeName  (string, 174/174 records)
    "I"  x39
    "1"  x37
    "II"  x23
    "B"  x22
    "A"  x16
    "2"  x10
    "3"  x8
    "C"  x8
    "D"  x6
    "5"  x3
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 72 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (39); Unit 2 Prod (Refactor) (33)
- **Intervals:** median 3.33s (p5 0.43s / p95 84932.79s, n=71)
- **`data` key-set variants:** [actionType, featureUsed] x36; [actionType, featureUsed, location] x30; [actionType, featureUsed, legendName] x6
- **Fields under `data`:**

```text
data.actionType  (string, 72/72 records)
    "WaypointMoveEvent"  x24
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
    "WaypointSetEvent"  x6
    "Selected"  x4
    "Unselected"  x2
data.featureUsed  (string, 72/72 records)
    "Map"  x36
    "Waypoint"  x30
    "Legend"  x6
data.legendName  (string, 6/72 records)
    "360 ft"  x2
    "Water"  x2
    "330 ft"  x1
    "90 ft"  x1
data.location  (object, 30/72 records)
data.location.x  (number, 30/72 records)
    numeric range -271.611 .. 276.693 (26 unique)
data.location.y  (number, 30/72 records)
    numeric range -219.751 .. 197.847 (26 unique)
data.location.z  (number, 30/72 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 52 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 3 Dev (14); Unit 1 Dev (12); Unit 3 Dungeon Dev (6)
- **eventKey:** present on 52 of 52 records
- **Intervals:** median 257.47s (p5 1.81s / p95 84269.25s, n=51)
- **`data` key-set variants:** [questEventType, questID, questName] x31; [questEventType, questID, questName, questSuccessOrFailure] x21
- **Fields under `data`:**

```text
data.questEventType  (string, 52/52 records)
    "questActiveEvent"  x31
    "questFinishEvent"  x21
data.questID  (string, 52/52 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 52/52 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 21/52 records)
    "Succeeded"  x21
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 50 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 3 Dev (22)
- **Intervals:** median 1.15s (p5 0.17s / p95 11.52s, n=49)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x46; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/50 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/50 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
data.actionType  (string, 46/50 records)
    "RightDrag"  x26
    "LeftDrag"  x20
data.currentSoilType  (string, 46/50 records)
    "CLAY"  x10
    "CLAYSAND"  x10
    "SAND"  x10
    "CLAYROCK"  x7
    "SANDGRAVEL"  x6
    "BEDROCK"  x2
    "GRAVEL"  x1
data.isCorrectSelection  (string, 46/50 records)
    "false"  x31
    "true"  x15
data.waterLevelStatus  (string, 46/50 records)
    "TooHigh"  x33
    "Proper"  x13
data.waterRetentionChange  (string, 46/50 records)
    "Increase"  x17
    "NoChange"  x15
    "Decrease"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 32 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (7); Unit 3 Dev (5); Unit 3 Dungeon Dev (4); Unit 4 Dev (2); Unit 1 Dev (1)
- **Intervals:** median 759.03s (p5 9.09s / p95 166960.47s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "DebugMenuStateChanged"  x32
data.isOpened  (bool, 32/32 records)
    false  x32
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 17 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 3 Dev (1)
- **Intervals:** median 13231.36s (p5 589.12s / p95 311693.30s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 16 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (6); Unit 1 Dev (2)
- **Intervals:** median 23.17s (p5 3.42s / p95 267947.96s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "submitAnswerEvent"  x16
data.answerSubmitted  (string, 16/16 records)
    "A,1,I"  x4
    "C,1,I"  x3
    "B,1,I"  x2
    "D,C,1,I"  x2
    "A,1,II"  x1
    "A,2,I"  x1
    "A,3,I"  x1
    "A,5,I"  x1
    "D,1,II"  x1
data.argumentationTitle  (string, 16/16 records)
    "Unit 2 – Watershed"  x8
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 17675.76s (p5 1126.13s / p95 324254.02s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 14 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (12); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 3.55s (p5 0.01s / p95 293321.96s, n=13)
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "Close"  x7
    "Open"  x7
data.toolName  (string, 14/14 records, 12 empty-string)
    ""  x12
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 99.36s (p5 6.76s / p95 479387.61s, n=8)
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

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 0.97s (p5 0.23s / p95 92.40s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 6 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 84239.24s (p5 31493.16s / p95 501141.31s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    false  x6
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 431753.46s (p5 198361.92s / p95 665145.00s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (28 records)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "Unselected" (2x); "WaypointMoveEvent" (24x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (6x); "Waypoint" (30x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (10x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*