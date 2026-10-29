# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f4

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f4
- **Game version string(s) in log:** 2.8.1, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f4.jsonl
- **Records:** 6585 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f4
- **Time span:** 2026-09-23T13:04:47.495000+00:00 .. 2026-10-07T15:13:49.967000+00:00 (338h 9m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f4\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 6585 records, 3 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 86 INFO, 6 NOT_TESTED, 69 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1903 | 28.9 | 1 | 2 | 0 | 2026-09-23T13:06:52.871000+00:00 | 2026-10-07T15:13:36.221000+00:00 | 338h 6m |
| PlayerPositionEvent | 1609 | 24.43 | 1 | 2 | 0 | 2026-09-23T13:06:31.033000+00:00 | 2026-10-07T15:13:49.967000+00:00 | 338h 7m |
| PuzzlePieceVisibleEvent | 1552 | 23.57 | 1 | 1 | 0 | 2026-10-01T13:02:54.381000+00:00 | 2026-10-07T13:24:56.927000+00:00 | 144h 22m |
| DialogueEvent | 956 | 14.52 | 1 | 2 | 674 | 2026-09-23T13:06:53.361000+00:00 | 2026-10-07T15:12:46.560000+00:00 | 338h 5m |
| ObjectInterEvent | 191 | 2.9 | 1 | 2 | 0 | 2026-09-23T13:12:25.461000+00:00 | 2026-10-07T15:10:51.045000+00:00 | 337h 58m |
| argumentationNodeEvent | 106 | 1.61 | 1 | 1 | 0 | 2026-09-25T13:29:43.754000+00:00 | 2026-09-29T13:17:18.280000+00:00 | 95h 47m |
| Soil Key Puzzle | 82 | 1.25 | 1 | 1 | 0 | 2026-10-05T13:23:26.404000+00:00 | 2026-10-07T13:16:55.414000+00:00 | 47h 53m |
| TopographicMapEvent | 54 | 0.82 | 1 | 1 | 0 | 2026-09-29T13:35:41.278000+00:00 | 2026-10-07T13:35:29.855000+00:00 | 191h 59m |
| questEvent | 42 | 0.64 | 1 | 2 | 42 | 2026-09-23T13:06:53.334000+00:00 | 2026-10-07T14:48:36.366000+00:00 | 337h 41m |
| gameWindowFocusEvent | 20 | 0.3 | 1 | 3 | 0 | 2026-09-23T13:04:47.495000+00:00 | 2026-10-07T14:53:11.270000+00:00 | 337h 48m |
| DEBUGMenu | 14 | 0.21 | 1 | 3 | 0 | 2026-09-23T13:06:31.025000+00:00 | 2026-10-07T14:48:29.240000+00:00 | 337h 41m |
| gameStartEvent | 13 | 0.2 | 1 | 1 | 0 | 2026-09-23T13:04:47.497000+00:00 | 2026-10-07T14:47:05.195000+00:00 | 337h 42m |
| crash | 9 | 0.14 | 1 | 1 | 0 |  |  | ? |
| argumentationEvent | 8 | 0.12 | 1 | 1 | 0 | 2026-09-25T13:27:39.440000+00:00 | 2026-09-29T13:17:25.034000+00:00 | 95h 49m |
| gameWindowUnfocusEvent | 8 | 0.12 | 1 | 3 | 0 | 2026-09-23T13:05:45.605000+00:00 | 2026-10-07T14:52:51.574000+00:00 | 337h 47m |
| argumentationAnswerEvent | 7 | 0.11 | 1 | 1 | 0 | 2026-09-25T13:29:31.066000+00:00 | 2026-09-29T13:17:25.009000+00:00 | 95h 47m |
| argumentationToolEvent | 6 | 0.09 | 1 | 1 | 0 | 2026-09-25T13:29:37.939000+00:00 | 2026-09-29T13:17:21.724000+00:00 | 95h 47m |
| DaniEvent | 4 | 0.06 | 1 | 1 | 0 | 2026-10-05T13:41:43.585000+00:00 | 2026-10-05T13:41:45.711000+00:00 | 2.1s |
| EndOfUnit | 1 | 0.02 | 1 | 1 | 0 | 2026-09-29T13:21:23.704000+00:00 | 2026-09-29T13:21:23.704000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 6383.571s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 0.218s median 
  - Expected: 5.979s in 09-23-26 
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
  - Observed: 17.462s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.91s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 46068.465s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1180.774s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85082.352s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dev; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 1552 records 
  - Expected: 5172 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointMoveEvent; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; B; C; D 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 9 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 19 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[143] _id=6ab3d114485cab4c954bb4ba ts=2026-09-23T13:16:04.6610000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[254] _id=6ab3d3e9485cab4c954c31d0 ts=2026-09-23T13:28:09.5760000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[316] _id=6ab3d4fd485cab4c954c6c53 ts=2026-09-23T13:32:44.9840000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[5] _id=6ab3ce6e485cab4c954b84ca ts=2026-09-23T13:04:47.4970000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[400] _id=6ab51d70485cab4c954fbf4d ts=2026-09-24T12:54:09.3350000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[769] _id=6ab670b9485cab4c955455a0 ts=2026-09-25T13:01:45.6720000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[4] _id=6ab3ce6e485cab4c954b84c8 ts=2026-09-23T13:04:47.4950000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[7] _id=6ab3cecb485cab4c954b859e ts=2026-09-23T13:06:19.5040000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[399] _id=6ab51d70485cab4c954fbf49 ts=2026-09-24T12:54:09.3340000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[8] _id=6ab3cea9485cab4c954b853e ts=2026-09-23T13:05:45.6050000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[763] _id=6ab52661485cab4c955121ed ts=2026-09-24T13:32:17.8010000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[765] _id=6ab5266c485cab4c95512369 ts=2026-09-24T13:32:27.9310000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 1902 | 0.0 | 1.1 | 639.96 | 20.989 | 344541.519 | 0.09 | 61 | 9 |
| PlayerPositionEvent | 1607 | 9.709 | 10.0 | 757.402 | 10.026 | 344263.186 | 0.08 | 0 | 8 |
| PuzzlePieceVisibleEvent | 1551 | 0.0 | 0.035 | 335.089 | 1.295 | 346325.224 | 0.18 | 875 | 2 |
| DialogueEvent | 955 | 0.0 | 6.636 | 1274.506 | 65.052 | 344426.03 | 0.05 | 230 | 8 |
| ObjectInterEvent | 190 | 0.003 | 0.218 | 6403.714 | 581.478 | 346073.211 | 0.01 | 3 | 10 |
| argumentationNodeEvent | 105 | 0.015 | 0.472 | 3284.329 | 14.662 | 344467.866 | 0.02 | 27 | 1 |
| Soil Key Puzzle | 81 | 0.142 | 0.999 | 2128.506 | 17.916 | 172138.157 | 0.03 | 0 | 1 |
| TopographicMapEvent | 53 | 0.015 | 2.731 | 13041.294 | 69237.911 | 343271.0 | 0.0 | 3 | 7 |
| questEvent | 41 | 0.003 | 269.715 | 29651.293 | 170690.359 | 344530.469 | 0.0 | 8 | 13 |
| gameWindowFocusEvent | 19 | 0.607 | 1180.774 | 64005.462 | 344517.832 | 345769.347 | 0.0 | 0 | 13 |
| DEBUGMenu | 13 | 6.331 | 6383.571 | 93516.786 | 345814.298 | 345903.359 | 0.0 | 0 | 10 |
| gameStartEvent | 12 | 441.253 | 46068.465 | 101311.475 | 345855.983 | 345961.871 | 0.0 | 0 | 11 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationEvent | 7 | 39.307 | 67.945 | 49283.656 | 241268.947 | 344635.698 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 7 | 0.944 | 85082.352 | 173717.996 | 660120.97 | 868888.141 | 0.0 | 0 | 5 |
| argumentationAnswerEvent | 6 | 3.124 | 17.462 | 57478.991 | 258606.603 | 344799.755 | 0.0 | 0 | 1 |
| argumentationToolEvent | 5 | 0.857 | 1.91 | 68972.757 | 275769.74 | 344663.052 | 0.0 | 0 | 1 |
| DaniEvent | 3 | 0.264 | 0.669 | 0.709 | 1.141 | 1.193 | 84.67 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[5069] _id=6ac644b8de269131f9b8b75d ts=2026-10-07T13:10:15.9530000Z == 6aa413b141b41dbac0c7f1f4.jsonl[5070] _id=6ac644b8de269131f9b8b75e ts=2026-10-07T13:10:15.9530000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 49 group(s), 75 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2330] _id=6abe5a03485cab4c95a41f5b ts=2026-10-01T13:02:58.9020000Z == 6aa413b141b41dbac0c7f1f4.jsonl[2322] _id=6abe5a03485cab4c95a41f5f ts=2026-10-01T13:02:58.9020000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2331] _id=6abe5a03485cab4c95a41f69 ts=2026-10-01T13:02:58.9020000Z == 6aa413b141b41dbac0c7f1f4.jsonl[2332] _id=6abe5a03485cab4c95a41f6b ts=2026-10-01T13:02:58.9020000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2414] _id=6abe5b85485cab4c95a45188 ts=2026-10-01T13:09:24.6260000Z == 6aa413b141b41dbac0c7f1f4.jsonl[2408] _id=6abe5b85485cab4c95a45193 ts=2026-10-01T13:09:24.6260000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[15] _id=6ab3cedc485cab4c954b85ce ts=? == 6aa413b141b41dbac0c7f1f4.jsonl[401] _id=6ab51d94485cab4c954fc27d ts=?`; `6aa413b141b41dbac0c7f1f4.jsonl[2196] _id=6abe58f5485cab4c95a40809 ts=? == 6aa413b141b41dbac0c7f1f4.jsonl[4091] _id=6ac39f90de269131f9a8420a ts=?`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `264ms: 6aa413b141b41dbac0c7f1f4.jsonl[5011] _id=6ac3a91ade269131f9a99f7d ts=2026-10-05T13:41:45.4470000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[5020] _id=6ac3a91ade269131f9a99f9e ts=2026-10-05T13:41:45.7110000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 120 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa413b141b41dbac0c7f1f4.jsonl[99] _id=6ab3d039485cab4c954b9290 ts=2026-09-23T13:12:25.4610000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[94] _id=6ab3d039485cab4c954b9294 ts=2026-09-23T13:12:25.4670000Z`; `3ms: 6aa413b141b41dbac0c7f1f4.jsonl[429] _id=6ab51dd8485cab4c954fcadc ts=2026-09-24T12:55:53.1670000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[417] _id=6ab51dd8485cab4c954fcae1 ts=2026-09-24T12:55:53.1700000Z`; `8ms: 6aa413b141b41dbac0c7f1f4.jsonl[807] _id=6ab67140485cab4c955460ef ts=2026-09-25T13:04:00.6030000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[783] _id=6ab67140485cab4c955460f5 ts=2026-09-25T13:04:00.6110000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 166 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa413b141b41dbac0c7f1f4.jsonl[2506] _id=6abe5b94485cab4c95a454ed ts=2026-10-01T13:02:56.0410000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[2503] _id=6abe5b94485cab4c95a454f1 ts=2026-10-01T13:02:56.0580000Z`; `17ms: 6aa413b141b41dbac0c7f1f4.jsonl[2344] _id=6abe5a05485cab4c95a41fa2 ts=2026-10-01T13:03:00.5730000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[2315] _id=6abe5a05485cab4c95a41fa6 ts=2026-10-01T13:03:00.5900000Z`; `16ms: 6aa413b141b41dbac0c7f1f4.jsonl[2315] _id=6abe5a05485cab4c95a41fa6 ts=2026-10-01T13:03:00.5900000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[2345] _id=6abe5a05485cab4c95a41fae ts=2026-10-01T13:03:00.6060000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `206ms: 6aa413b141b41dbac0c7f1f4.jsonl[2093] _id=6abbbeae485cab4c957d6ada ts=2026-09-29T13:35:41.2780000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[2095] _id=6abbbeaf485cab4c957d6ae6 ts=2026-09-29T13:35:41.4840000Z`; `412ms: 6aa413b141b41dbac0c7f1f4.jsonl[2085] _id=6abbbeaf485cab4c957d6b01 ts=2026-09-29T13:35:41.7160000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[2097] _id=6abbbeaf485cab4c957d6b0f ts=2026-09-29T13:35:42.1280000Z`; `363ms: 6aa413b141b41dbac0c7f1f4.jsonl[2102] _id=6abbbeb4485cab4c957d6be2 ts=2026-09-29T13:35:48.6480000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[2107] _id=6abbbeb5485cab4c957d6c00 ts=2026-09-29T13:35:49.0110000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `631ms: 6aa413b141b41dbac0c7f1f4.jsonl[1236] _id=6ab6774a485cab4c955508e0 ts=2026-09-25T13:29:46.8850000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[1240] _id=6ab6774b485cab4c955508f2 ts=2026-09-25T13:29:47.5160000Z`; `541ms: 6aa413b141b41dbac0c7f1f4.jsonl[1237] _id=6ab6774a485cab4c955508e2 ts=2026-09-25T13:29:47.0090000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[1229] _id=6ab6774b485cab4c955508f4 ts=2026-09-25T13:29:47.5500000Z`; `283ms: 6aa413b141b41dbac0c7f1f4.jsonl[1240] _id=6ab6774b485cab4c955508f2 ts=2026-09-25T13:29:47.5160000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[1230] _id=6ab6774b485cab4c955508fe ts=2026-09-25T13:29:47.7990000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `607ms: 6aa413b141b41dbac0c7f1f4.jsonl[892] _id=6ab672c6485cab4c95547c31 ts=2026-09-25T13:10:30.7170000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[891] _id=6ab672c7485cab4c95547c4b ts=2026-09-25T13:10:31.3240000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `944ms: 6aa413b141b41dbac0c7f1f4.jsonl[890] _id=6ab672c6485cab4c95547c1f ts=2026-09-25T13:10:30.2830000Z ~ 6aa413b141b41dbac0c7f1f4.jsonl[894] _id=6ab672c7485cab4c95547c49 ts=2026-09-25T13:10:31.2270000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 96h 5m 
  - Evidence: 96h 5m: 6aa413b141b41dbac0c7f1f4.jsonl[771] _id=6ab670fd485cab4c95545d0d ts=2026-09-25T13:02:53.8640000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1272] _id=6abbb82d485cab4c957c25ce ts=2026-09-29T13:07:57.2230000Z; 96h 2m: 6aa413b141b41dbac0c7f1f4.jsonl[2195] _id=6abe58ef485cab4c95a4074d ts=2026-10-01T12:58:23.2010000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4090] _id=6ac39f8ade269131f9a841d8 ts=2026-10-05T13:00:58.1250000Z; 47h 24m: 6aa413b141b41dbac0c7f1f4.jsonl[1952] _id=6abbbe32485cab4c957d5318 ts=2026-09-29T13:33:38.0540000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2195] _id=6abe58ef485cab4c95a4074d ts=2026-10-01T12:58:23.2010000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 6aa413b141b41dbac0c7f1f4.jsonl[1262] _id=6ab6775f485cab4c95550b82 ts=2026-09-25T13:30:07.2730000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1341] _id=6abbb8c9485cab4c957c3844 ts=2026-09-29T13:10:33.3030000Z; 95h 20m: 6aa413b141b41dbac0c7f1f4.jsonl[4076] _id=6abe62e0485cab4c95a67ad3 ts=2026-10-01T13:40:48.5980000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4106] _id=6ac39fb7de269131f9a84382 ts=2026-10-05T13:01:43.2520000Z; 47h 23m: 6aa413b141b41dbac0c7f1f4.jsonl[1965] _id=6abbbe8e485cab4c957d6504 ts=2026-09-29T13:35:10.7990000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2206] _id=6abe5907485cab4c95a40a73 ts=2026-10-01T12:58:47.4070000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 230 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f4.jsonl[5862] _id=6ac648aade269131f9b9078e ts=2026-10-07T13:27:06.5530000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5863] _id=6ac648aade269131f9b9078f ts=2026-10-07T13:27:06.5530000Z; 1ms: 6aa413b141b41dbac0c7f1f4.jsonl[1486] _id=6abbba57485cab4c957c70ca ts=2026-09-29T13:17:11.3520000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1487] _id=6abbba57485cab4c957c70d4 ts=2026-09-29T13:17:11.3530000Z; 1ms: 6aa413b141b41dbac0c7f1f4.jsonl[1572] _id=6abbbaf7485cab4c957c92a3 ts=2026-09-29T13:19:51.2750000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1573] _id=6abbbaf7485cab4c957c92aa ts=2026-09-29T13:19:51.2760000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 6aa413b141b41dbac0c7f1f4.jsonl[1169] _id=6ab6765f485cab4c9554e254 ts=2026-09-25T13:25:51.4250000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1274] _id=6abbb83c485cab4c957c2688 ts=2026-09-29T13:08:12.9440000Z; 95h 19m: 6aa413b141b41dbac0c7f1f4.jsonl[4085] _id=6abe6313485cab4c95a68481 ts=2026-10-01T13:41:39.4030000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4094] _id=6ac39f93de269131f9a8423a ts=2026-10-05T13:01:07.3200000Z; 47h 28m: 6aa413b141b41dbac0c7f1f4.jsonl[5018] _id=6ac3a91bde269131f9a99fbd ts=2026-10-05T13:41:46.6070000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5068] _id=6ac644b8de269131f9b8b75c ts=2026-10-07T13:10:15.9520000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 61 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f4.jsonl[5069] _id=6ac644b8de269131f9b8b75d ts=2026-10-07T13:10:15.9530000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5070] _id=6ac644b8de269131f9b8b75e ts=2026-10-07T13:10:15.9530000Z; 1ms: 6aa413b141b41dbac0c7f1f4.jsonl[1944] _id=6abbbe33485cab4c957d5362 ts=2026-09-29T13:33:38.8050000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1947] _id=6abbbe33485cab4c957d5364 ts=2026-09-29T13:33:38.8060000Z; 1ms: 6aa413b141b41dbac0c7f1f4.jsonl[5068] _id=6ac644b8de269131f9b8b75c ts=2026-10-07T13:10:15.9520000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5069] _id=6ac644b8de269131f9b8b75d ts=2026-10-07T13:10:15.9530000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 96h 7m 
  - Evidence: 96h 7m: 6aa413b141b41dbac0c7f1f4.jsonl[3625] _id=6abe5cf5485cab4c95a492e7 ts=2026-10-01T13:15:33.1960000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4483] _id=6ac3a4cede269131f9a8d053 ts=2026-10-05T13:23:26.4070000Z; 95h 43m: 6aa413b141b41dbac0c7f1f4.jsonl[1173] _id=6ab67660485cab4c9554e282 ts=2026-09-25T13:25:52.5520000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1326] _id=6abbb89b485cab4c957c318e ts=2026-09-29T13:09:47.4290000Z; 47h 51m: 6aa413b141b41dbac0c7f1f4.jsonl[4483] _id=6ac3a4cede269131f9a8d053 ts=2026-10-05T13:23:26.4070000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5160] _id=6ac645d8de269131f9b8bd83 ts=2026-10-07T13:15:04.8840000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.003s..0.008s shown 
  - Evidence: 3ms: 6aa413b141b41dbac0c7f1f4.jsonl[429] _id=6ab51dd8485cab4c954fcadc ts=2026-09-24T12:55:53.1670000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[417] _id=6ab51dd8485cab4c954fcae1 ts=2026-09-24T12:55:53.1700000Z; 6ms: 6aa413b141b41dbac0c7f1f4.jsonl[99] _id=6ab3d039485cab4c954b9290 ts=2026-09-23T13:12:25.4610000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[94] _id=6ab3d039485cab4c954b9294 ts=2026-09-23T13:12:25.4670000Z; 8ms: 6aa413b141b41dbac0c7f1f4.jsonl[807] _id=6ab67140485cab4c955460ef ts=2026-09-25T13:04:00.6030000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[783] _id=6ab67140485cab4c955460f5 ts=2026-09-25T13:04:00.6110000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa413b141b41dbac0c7f1f4.jsonl[1267] _id=6ab67765485cab4c95550c2c ts=2026-09-25T13:30:14.0440000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1269] _id=6abbb833485cab4c957c2610 ts=2026-09-29T13:07:57.2300000Z; 95h 19m: 6aa413b141b41dbac0c7f1f4.jsonl[4086] _id=6abe6318485cab4c95a6853d ts=2026-10-01T13:41:44.2490000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4092] _id=6ac39f91de269131f9a84210 ts=2026-10-05T13:00:58.1310000Z; 47h 17m: 6aa413b141b41dbac0c7f1f4.jsonl[2183] _id=6abbbfd0485cab4c957d9bc4 ts=2026-09-29T13:40:32.5500000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2197] _id=6abe58f5485cab4c95a4080f ts=2026-10-01T12:58:23.2070000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 6aa413b141b41dbac0c7f1f4.jsonl[3606] _id=6abe5cd8485cab4c95a48f77 ts=2026-10-01T13:15:00.6180000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4563] _id=6ac3a5aade269131f9a904d3 ts=2026-10-05T13:27:05.8420000Z; 47h 49m: 6aa413b141b41dbac0c7f1f4.jsonl[4668] _id=6ac3a5f8de269131f9a91365 ts=2026-10-05T13:28:21.9490000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5242] _id=6ac64669de269131f9b8c04d ts=2026-10-07T13:17:28.9110000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 875 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f4.jsonl[2321] _id=6abe5a03485cab4c95a41f57 ts=2026-10-01T13:02:58.9020000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2330] _id=6abe5a03485cab4c95a41f5b ts=2026-10-01T13:02:58.9020000Z; 0ms: 6aa413b141b41dbac0c7f1f4.jsonl[2322] _id=6abe5a03485cab4c95a41f5f ts=2026-10-01T13:02:58.9020000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2323] _id=6abe5a03485cab4c95a41f66 ts=2026-10-01T13:02:58.9020000Z; 0ms: 6aa413b141b41dbac0c7f1f4.jsonl[2323] _id=6abe5a03485cab4c95a41f66 ts=2026-10-01T13:02:58.9020000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2331] _id=6abe5a03485cab4c95a41f69 ts=2026-10-01T13:02:58.9020000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 48m 
  - Evidence: 47h 48m: 6aa413b141b41dbac0c7f1f4.jsonl[4543] _id=6ac3a56ede269131f9a8fabb ts=2026-10-05T13:26:06.7220000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5061] _id=6ac645d8de269131f9b8bd81 ts=2026-10-07T13:15:04.8790000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 6aa413b141b41dbac0c7f1f4.jsonl[4064] _id=6abe62b4485cab4c95a671bd ts=2026-10-01T13:40:03.9360000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4098] _id=6ac39f9ade269131f9a84286 ts=2026-10-05T13:01:14.9360000Z; 47h 31m: 6aa413b141b41dbac0c7f1f4.jsonl[2114] _id=6abbbeb7485cab4c957d6c6e ts=2026-09-29T13:35:51.0080000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2383] _id=6abe5b08485cab4c95a43d97 ts=2026-10-01T13:07:20.8820000Z; 47h 30m: 6aa413b141b41dbac0c7f1f4.jsonl[5017] _id=6ac3a91bde269131f9a99fb9 ts=2026-10-05T13:41:46.6030000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5103] _id=6ac64533de269131f9b8b8d6 ts=2026-10-07T13:12:19.1500000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.015s..0.028s shown 
  - Evidence: 15ms: 6aa413b141b41dbac0c7f1f4.jsonl[4042] _id=6abe62a8485cab4c95a66f23 ts=2026-10-01T13:39:51.6460000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4044] _id=6abe62a8485cab4c95a66f44 ts=2026-10-01T13:39:51.6610000Z; 22ms: 6aa413b141b41dbac0c7f1f4.jsonl[4041] _id=6abe62a7485cab4c95a66f12 ts=2026-10-01T13:39:51.6240000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4042] _id=6abe62a8485cab4c95a66f23 ts=2026-10-01T13:39:51.6460000Z; 28ms: 6aa413b141b41dbac0c7f1f4.jsonl[4040] _id=6abe62a7485cab4c95a66ef8 ts=2026-10-01T13:39:51.5960000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4041] _id=6abe62a7485cab4c95a66f12 ts=2026-10-01T13:39:51.6240000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 46m 
  - Evidence: 95h 46m: 6aa413b141b41dbac0c7f1f4.jsonl[1256] _id=6ab6775e485cab4c95550b62 ts=2026-09-25T13:30:07.2070000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1447] _id=6abbba3e485cab4c957c69c2 ts=2026-09-29T13:16:46.9620000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 43m 
  - Evidence: 95h 43m: 6aa413b141b41dbac0c7f1f4.jsonl[1265] _id=6ab6775f485cab4c95550b6a ts=2026-09-25T13:30:07.2370000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1398] _id=6abbb99b485cab4c957c5061 ts=2026-09-29T13:14:02.9350000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 41m 
  - Evidence: 95h 41m: 6aa413b141b41dbac0c7f1f4.jsonl[1263] _id=6ab6775e485cab4c95550b3d ts=2026-09-25T13:30:05.8150000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1356] _id=6abbb8f1485cab4c957c3cb1 ts=2026-09-29T13:11:13.6810000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 27 interval(s) ≤ 0.015s..0.021s shown 
  - Evidence: 15ms: 6aa413b141b41dbac0c7f1f4.jsonl[1387] _id=6abbba36485cab4c957c67ba ts=2026-09-29T13:16:38.4040000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1391] _id=6abbba36485cab4c957c67bc ts=2026-09-29T13:16:38.4190000Z; 20ms: 6aa413b141b41dbac0c7f1f4.jsonl[1479] _id=6abbba54485cab4c957c6ff0 ts=2026-09-29T13:17:08.5990000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1482] _id=6abbba54485cab4c957c6ff8 ts=2026-09-29T13:17:08.6190000Z; 21ms: 6aa413b141b41dbac0c7f1f4.jsonl[1363] _id=6abbb915485cab4c957c4166 ts=2026-09-29T13:11:49.0400000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1362] _id=6abbb915485cab4c957c4168 ts=2026-09-29T13:11:49.0610000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 6aa413b141b41dbac0c7f1f4.jsonl[1227] _id=6ab67741485cab4c9555080e ts=2026-09-25T13:29:37.9390000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1394] _id=6abbb998485cab4c957c5018 ts=2026-09-29T13:14:00.9910000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa413b141b41dbac0c7f1f4.jsonl[769] _id=6ab670b9485cab4c955455a0 ts=2026-09-25T13:01:45.6720000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1268] _id=6abbb823485cab4c957c2568 ts=2026-09-29T13:07:47.5430000Z; 96h 2m: 6aa413b141b41dbac0c7f1f4.jsonl[2194] _id=6abe58d8485cab4c95a40602 ts=2026-10-01T12:58:00.0490000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4089] _id=6ac39f81de269131f9a8419c ts=2026-10-05T13:00:49.3960000Z; 47h 24m: 6aa413b141b41dbac0c7f1f4.jsonl[1949] _id=6abbbe11485cab4c957d4d5b ts=2026-09-29T13:33:05.2980000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2194] _id=6abe58d8485cab4c95a40602 ts=2026-10-01T12:58:00.0490000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa413b141b41dbac0c7f1f4.jsonl[2193] _id=6abe58d7485cab4c95a405fb ts=2026-10-01T12:58:00.0480000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4088] _id=6ac39f81de269131f9a84199 ts=2026-10-05T13:00:49.3950000Z; 95h 39m: 6aa413b141b41dbac0c7f1f4.jsonl[1201] _id=6ab676e8485cab4c9554f7bd ts=2026-09-25T13:28:08.7670000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1271] _id=6abbb823485cab4c957c2566 ts=2026-09-29T13:07:47.5420000Z; 47h 24m: 6aa413b141b41dbac0c7f1f4.jsonl[1948] _id=6abbbe11485cab4c957d4d56 ts=2026-09-29T13:33:05.2970000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2193] _id=6abe58d7485cab4c95a405fb ts=2026-10-01T12:58:00.0480000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 241h 21m 
  - Evidence: 241h 21m: 6aa413b141b41dbac0c7f1f4.jsonl[1200] _id=6ab676e5485cab4c9554f72a ts=2026-09-25T13:28:05.8630000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[5043] _id=6ac3b8fede269131f9aca7c4 ts=2026-10-05T14:49:34.0040000Z; 48h 3m: 6aa413b141b41dbac0c7f1f4.jsonl[5043] _id=6ac3b8fede269131f9aca7c4 ts=2026-10-05T14:49:34.0040000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[6147] _id=6ac65cc3de269131f9bb3238 ts=2026-10-07T14:52:51.5740000Z; 24h 26m: 6aa413b141b41dbac0c7f1f4.jsonl[8] _id=6ab3cea9485cab4c954b853e ts=2026-09-23T13:05:45.6050000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[763] _id=6ab52661485cab4c955121ed ts=2026-09-24T13:32:17.8010000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 6aa413b141b41dbac0c7f1f4.jsonl[1171] _id=6ab67660485cab4c9554e296 ts=2026-09-25T13:25:52.6090000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1270] _id=6abbb833485cab4c957c2616 ts=2026-09-29T13:08:03.0780000Z; 95h 35m: 6aa413b141b41dbac0c7f1f4.jsonl[3830] _id=6abe5f54485cab4c95a56e7d ts=2026-10-01T13:25:40.2060000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[4093] _id=6ac39f91de269131f9a84216 ts=2026-10-05T13:01:04.6790000Z; 47h 24m: 6aa413b141b41dbac0c7f1f4.jsonl[1953] _id=6abbbe33485cab4c957d5374 ts=2026-09-29T13:33:38.8530000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[2198] _id=6abe58f5485cab4c95a40815 ts=2026-10-01T12:58:29.2120000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6aa413b141b41dbac0c7f1f4.jsonl[1345] _id=6abbb8c9485cab4c957c384a ts=2026-09-29T13:10:33.3260000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1343] _id=6abbb8c9485cab4c957c384c ts=2026-09-29T13:10:33.3290000Z; 5ms: 6aa413b141b41dbac0c7f1f4.jsonl[1170] _id=6ab67660485cab4c9554e294 ts=2026-09-25T13:25:52.6040000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[1171] _id=6ab67660485cab4c9554e296 ts=2026-09-25T13:25:52.6090000Z; 5ms: 6aa413b141b41dbac0c7f1f4.jsonl[896] _id=6ab672d0485cab4c95547d09 ts=2026-09-25T13:10:40.9790000Z -> 6aa413b141b41dbac0c7f1f4.jsonl[897] _id=6ab672d0485cab4c95547d0f ts=2026-09-25T13:10:40.9840000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[5011] _id=6ac3a91ade269131f9a99f7d ts=2026-10-05T13:41:45.4470000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[5020] _id=6ac3a91ade269131f9a99f9e ts=2026-10-05T13:41:45.7110000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[1139] _id=6ab67628485cab4c9554d95a ts=2026-09-25T13:24:56.4370000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[1519] _id=6abbba92485cab4c957c7d98 ts=2026-09-29T13:18:10.1140000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[4035] _id=6abe629d485cab4c95a66b49 ts=2026-10-01T13:39:41.7520000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 16 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2786] _id=6abe5bc2485cab4c95a45fb7 ts=2026-10-01T13:10:24.7290000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2730] _id=6abe5bc2485cab4c95a45fc5 ts=2026-10-01T13:10:24.9090000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2731] _id=6abe5bc2485cab4c95a45fc9 ts=2026-10-01T13:10:24.9590000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 109 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2502] _id=6abe5b93485cab4c95a454d7 ts=2026-10-01T13:02:56.0070000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2342] _id=6abe5a05485cab4c95a41f98 ts=2026-10-01T13:03:00.5140000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2343] _id=6abe5a05485cab4c95a41f9f ts=2026-10-01T13:03:00.5390000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2093] _id=6abbbeae485cab4c957d6ada ts=2026-09-29T13:35:41.2780000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2095] _id=6abbbeaf485cab4c957d6ae6 ts=2026-09-29T13:35:41.4840000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[1257] _id=6ab6775d485cab4c95550ae3 ts=2026-09-25T13:30:03.0290000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[1260] _id=6ab6775e485cab4c95550b1d ts=2026-09-25T13:30:04.5810000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[1258] _id=6ab6775e485cab4c95550b2a ts=2026-09-25T13:30:04.6120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 9 records 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[15] _id=6ab3cedc485cab4c954b85ce ts=?`; `6aa413b141b41dbac0c7f1f4.jsonl[401] _id=6ab51d94485cab4c954fc27d ts=?`; `6aa413b141b41dbac0c7f1f4.jsonl[773] _id=6ab67103485cab4c95545dad ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 93 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2710] _id=6abe5bab485cab4c95a45c6a ts=2026-10-01T13:10:02.2900000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2699] _id=6abe5bab485cab4c95a45c70 ts=2026-10-01T13:10:02.3250000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2712] _id=6abe5bab485cab4c95a45c7d ts=2026-10-01T13:10:02.3910000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 364 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2506] _id=6abe5b94485cab4c95a454ed ts=2026-10-01T13:02:56.0410000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2503] _id=6abe5b94485cab4c95a454f1 ts=2026-10-01T13:02:56.0580000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2322] _id=6abe5a03485cab4c95a41f5f ts=2026-10-01T13:02:58.9020000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 28 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2097] _id=6abbbeaf485cab4c957d6b0f ts=2026-09-29T13:35:42.1280000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2086] _id=6abbbeaf485cab4c957d6b1a ts=2026-09-29T13:35:43.2150000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2104] _id=6abbbeb3485cab4c957d6ba3 ts=2026-09-29T13:35:47.2610000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[1477] _id=6abbba50485cab4c957c6eef ts=2026-09-29T13:17:04.3580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[1500] _id=6abbba5f485cab4c957c72e2 ts=2026-09-29T13:17:19.3940000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[1501] _id=6abbba60485cab4c957c7349 ts=2026-09-29T13:17:20.8670000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'DialogueStartEvent' (totals: 143 start, 139 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 21 unmatched 'BecameCameraCentered' (totals: 177 open, 172 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 60 unmatched 'BecameVisible' (totals: 577 open, 626 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'MapOpenEvent' (totals: 29 open, 24 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 4 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 27 start, 15 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 124 of 6575 adjacent _id pairs reverse in client time; worst 403.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f4.jsonl[2507] _id=6abe5b94485cab4c95a454f3 ts=2026-10-01T13:09:39.6820000Z`; `6aa413b141b41dbac0c7f1f4.jsonl[2508] _id=6abe5b94485cab4c95a454f7 ts=2026-10-01T13:02:56.0580000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -404.32s, max +1.00s over 6576 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f4\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | skipped |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 9 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `TerasGardenBox` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **NOT_TESTED / NotTested** `soilMachine` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md

## 9. Event-Type Details

### `InputEvent` — 1903 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1515); Unit 1 Dev (388)
- **Intervals:** median 1.10s (p5 0.10s / p95 20.99s, n=1902)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1903/1903 records)
    "pressed"  x1903
data.actionType  (string, 1903/1903 records)
    "Move"  x1348
    "Interact"  x271
    "Jump"  x129
    "Map"  x61
    "Sprint"  x34
    "Hoverboard"  x27
    "Ascend"  x21
    "Descend"  x5
    "SkipCinematic"  x3
    "ToggleDebug"  x3
    "Pause"  x1
data.key  (string, 1903/1903 records, 16 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1903/1903 records)
    "Player"  x1661
    "Drone"  x242
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1609 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (945); Unit 1 Dev (664)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1607)
- **Fields under `data`:**

```text
data.position  (object, 1609/1609 records)
data.position.x  (number, 1609/1609 records)
    numeric range -22.4637 .. 1701.94 (412 unique)
data.position.y  (number, 1609/1609 records)
    numeric range -5.12663 .. 160.6 (323 unique)
data.position.z  (number, 1609/1609 records)
    numeric range -101.115 .. 1995.36 (412 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 1552 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1552)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.29s, n=1551)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1552/1552 records)
    "BecameInvisible"  x626
    "BecameVisible"  x577
    "BecameCameraCentered"  x177
    "BecameCameraUncentered"  x172
data.pieceId  (string, 1552/1552 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1552/1552 records)
    1146 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 956 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (567); Unit 1 Dev (389)
- **eventKey:** present on 674 of 956 records
- **Intervals:** median 6.64s (p5 0.01s / p95 65.05s, n=955)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x674; [conversationId, dialogueEventType] x282
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 956/956 records)
    numeric range 8 .. 74 (21 unique)
data.dialogueEventType  (string, 956/956 records)
    "DialogueNodeEvent"  x674
    "DialogueStartEvent"  x143
    "DialogueFinishEvent"  x139
data.nodeId  (number, 674/956 records)
    numeric range 0 .. 290 (167 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 191 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (161); Unit 1 Dev (30)
- **Intervals:** median 0.22s (p5 0.15s / p95 581.48s, n=190)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 191/191 records)
    "Press E to Install"  x131
    "TalkTo"  x15
    "Press E to Pick up"  x11
    "E to Talk"  x7
    "Press E to Place"  x7
    "Press E to Open Locker"  x6
    "Press E to Scan"  x5
    "Press E to Insert"  x4
    "Press E to Operate"  x2
    "Inspect Alien Glyph"  x1
    "Press E to Collect"  x1
    "Press [E/Action button] to enter escape pod "  x1
data.objectName  (string, 191/191 records)
    33 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 106 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (106)
- **Intervals:** median 0.47s (p5 0.03s / p95 14.66s, n=105)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 106/106 records)
    "argumentationNodeHoverEnd"  x50
    "argumentationNodeHoverStart"  x43
    "argumentationNodeAdd"  x9
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 106/106 records)
    "Unit 1 - Freshwater"  x80
    "Unit 1 - Argumentation Tutorial"  x26
data.nodeName  (string, 106/106 records)
    "A"  x49
    "1"  x26
    "II"  x16
    "I"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 82 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (82)
- **Intervals:** median 1.00s (p5 0.17s / p95 17.92s, n=81)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x78; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/82 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/82 records)
    "Unit 2 Prod (Refactor)"  x4
data.actionType  (string, 78/82 records)
    "RightDrag"  x43
    "LeftDrag"  x35
data.currentSoilType  (string, 78/82 records)
    "SAND"  x16
    "SANDGRAVEL"  x15
    "CLAYSAND"  x14
    "CLAY"  x12
    "CLAYROCK"  x10
    "GRAVEL"  x7
    "BEDROCK"  x4
data.isCorrectSelection  (string, 78/82 records)
    "false"  x62
    "true"  x16
data.waterLevelStatus  (string, 78/82 records)
    "TooHigh"  x47
    "Proper"  x19
    "TooLow"  x12
data.waterRetentionChange  (string, 78/82 records)
    "Increase"  x40
    "Decrease"  x22
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 54 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (54)
- **Intervals:** median 2.73s (p5 0.10s / p95 69237.91s, n=53)
- **`data` key-set variants:** [actionType, featureUsed] x53; [actionType, featureUsed, location] x1
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "MapOpenEvent"  x29
    "MapCloseEvent"  x24
    "WaypointSetEvent"  x1
data.featureUsed  (string, 54/54 records)
    "Map"  x53
    "Waypoint"  x1
data.location  (object, 1/54 records)
data.location.x  (number, 1/54 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 1/54 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 1/54 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 42 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (25); Unit 2 Prod (Refactor) (17)
- **eventKey:** present on 42 of 42 records
- **Intervals:** median 269.71s (p5 0.01s / p95 170690.36s, n=41)
- **`data` key-set variants:** [questEventType, questID, questName] x27; [questEventType, questID, questName, questSuccessOrFailure] x15
- **Fields under `data`:**

```text
data.questEventType  (string, 42/42 records)
    "questActiveEvent"  x27
    "questFinishEvent"  x15
data.questID  (string, 42/42 records)
    "22"  x6
    "29"  x6
    "31"  x6
    "32"  x6
    "21"  x4
    "24"  x3
    "33"  x3
    "23"  x2
    "25"  x2
    "28"  x2
    "34"  x2
data.questName  (string, 42/42 records)
    "Gear Up"  x6
    "Getting the Band Back Together"  x6
    "Info and Intros"  x6
    "TK, Reporting In!"  x6
    "Escape the Ruin"  x4
    "Defend the Expedition"  x3
    "Investigate the Temple"  x3
    "Foraged Forging"  x2
    "Getting Your Space Legs"  x2
    "What Was That?"  x2
    "Which Watershed?"  x2
data.questSuccessOrFailure  (string, 15/42 records)
    "Succeeded"  x15
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 1 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1180.77s (p5 82.87s / p95 344517.83s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 14 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (4); MainMenu (2)
- **Intervals:** median 6383.57s (p5 53.30s / p95 345814.30s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "DebugMenuStateChanged"  x14
data.isOpened  (bool, 14/14 records)
    false  x14
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 46068.46s (p5 541.01s / p95 345855.98s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `crash` — 9 records

- **Scenes:** <missing sceneName> (9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 9/9 records)
    true  x9
data.message  (string, 9/9 records)
    "A user gesture is required to request Pointer Lock."  x8
    "Permissions check failed"  x1
data.phase  (string, 9/9 records)
    "running"  x9
data.stack  (string, 9/9 records, 8 empty-string)
    ""  x8
    "TypeError: Permissions check failed"  x1
data.type  (string, 9/9 records)
    "unhandled_rejection"  x9
data.unitId  (string, 9/9 records)
    "unit2"  x5
    "unit1"  x4
data.workspace  (string, 9/9 records)
    "mhs"  x9
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8)
- **Intervals:** median 67.94s (p5 39.68s / p95 241268.95s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 8/8 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (5); Unit 2 Prod (Refactor) (2); MainMenu (1)
- **Intervals:** median 85082.35s (p5 3.70s / p95 660120.97s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationAnswerEvent` — 7 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 17.46s (p5 4.59s / p95 258606.60s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "submitAnswerEvent"  x7
data.answerSubmitted  (string, 7/7 records, 2 empty-string)
    "A,1,I"  x4
    ""  x2
    "A,1,II"  x1
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x7
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (6)
- **Intervals:** median 1.91s (p5 0.98s / p95 275769.74s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Freshwater"  x4
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4)
- **Intervals:** median 0.67s (p5 0.30s / p95 1.14s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x3
    "Open"  x1
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "1"  x1
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
- `ObjectInterEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (82 records)
- `TopographicMapEvent` data.actionType: "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (1x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 3 Dev' has no records of this event
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*