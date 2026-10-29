# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f8

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f8
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f8.jsonl
- **Records:** 11047 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f8
- **Time span:** 2026-09-23T13:08:45.118000+00:00 .. 2026-10-07T18:47:28.023000+00:00 (341h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f8\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **18 event types**, 11047 records, 4 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 79 INFO, 4 NOT_TESTED, 58 PASS.
- Top items needing attention:
  - WARNING/Medium `Soil Key Puzzle`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5044 | 45.66 | 1 | 3 | 0 | 2026-09-23T13:10:00.563000+00:00 | 2026-10-07T18:47:21.960000+00:00 | 341h 37m |
| PuzzlePieceVisibleEvent | 2178 | 19.72 | 1 | 1 | 0 | 2026-09-30T14:59:51.571000+00:00 | 2026-10-06T14:51:26.855000+00:00 | 143h 51m |
| PlayerPositionEvent | 2136 | 19.34 | 1 | 3 | 0 | 2026-09-23T13:09:55.239000+00:00 | 2026-10-07T18:47:28.023000+00:00 | 341h 37m |
| DialogueEvent | 1014 | 9.18 | 1 | 3 | 671 | 2026-09-23T13:10:17.268000+00:00 | 2026-10-07T15:14:19.554000+00:00 | 338h 4m |
| ObjectInterEvent | 204 | 1.85 | 1 | 3 | 0 | 2026-09-23T13:16:35.023000+00:00 | 2026-10-07T14:57:47.604000+00:00 | 337h 41m |
| argumentationNodeEvent | 172 | 1.56 | 1 | 1 | 0 | 2026-09-28T18:41:33.615000+00:00 | 2026-09-29T18:38:31.722000+00:00 | 23h 56m |
| TopographicMapEvent | 133 | 1.2 | 1 | 2 | 0 | 2026-09-30T14:57:46.381000+00:00 | 2026-10-07T15:15:23.050000+00:00 | 168h 17m |
| questEvent | 52 | 0.47 | 1 | 3 | 52 | 2026-09-23T13:10:17.246000+00:00 | 2026-10-07T18:46:37.990000+00:00 | 341h 36m |
| gameWindowFocusEvent | 28 | 0.25 | 1 | 3 | 0 | 2026-09-23T13:08:45.118000+00:00 | 2026-10-07T18:46:25.757000+00:00 | 341h 37m |
| gameWindowUnfocusEvent | 23 | 0.21 | 1 | 3 | 0 | 2026-09-23T13:41:53.184000+00:00 | 2026-10-07T18:47:27.643000+00:00 | 341h 5m |
| DEBUGMenu | 18 | 0.16 | 1 | 4 | 0 | 2026-09-23T13:09:55.233000+00:00 | 2026-10-07T18:46:33.489000+00:00 | 341h 36m |
| gameStartEvent | 16 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:08:45.119000+00:00 | 2026-10-07T18:46:25.757000+00:00 | 341h 37m |
| argumentationToolEvent | 7 | 0.06 | 1 | 1 | 0 | 2026-09-28T18:46:52.953000+00:00 | 2026-09-29T18:38:39.634000+00:00 | 23h 51m |
| DaniEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-09-30T14:57:40.901000+00:00 | 2026-10-07T15:15:20.215000+00:00 | 168h 17m |
| argumentationEvent | 6 | 0.05 | 1 | 1 | 0 | 2026-09-28T18:47:04.212000+00:00 | 2026-09-29T18:38:39.851000+00:00 | 23h 51m |
| crash | 6 | 0.05 | 1 | 1 | 0 |  |  | ? |
| argumentationAnswerEvent | 3 | 0.03 | 1 | 1 | 0 | 2026-09-28T18:47:20.898000+00:00 | 2026-09-29T18:38:39.821000+00:00 | 23h 51m |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-29T18:41:38.593000+00:00 | 2026-09-29T18:41:38.593000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 72852.897s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.043s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 38 records in baseline; check coverage before treating as a logging regression
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
  - Observed: 9.162s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 42939.461s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 73891.497s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1628.639s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 6305.503s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 445.261s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Insert; Press E to Operate; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
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
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 20 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[756] _id=6ab3d4b4485cab4c954c61a4 ts=2026-09-23T13:31:32.7200000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[876] _id=6ab3d5e9485cab4c954c9199 ts=2026-09-23T13:36:41.0350000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[890] _id=6ab3d619485cab4c954c96a8 ts=2026-09-23T13:37:29.3160000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[1] _id=6ab3cf5d485cab4c954b87d6 ts=2026-09-23T13:08:45.1190000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[935] _id=6ab51e1d485cab4c954fd3b5 ts=2026-09-24T12:57:01.5740000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[1559] _id=6ab6719d485cab4c955468f1 ts=2026-09-25T13:05:33.8550000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[0] _id=6ab3cf5d485cab4c954b87d4 ts=2026-09-23T13:08:45.1180000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[938] _id=6ab51e1d485cab4c954fd3ad ts=2026-09-24T12:57:01.5740000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[1558] _id=6ab6719d485cab4c955468ef ts=2026-09-25T13:05:33.8550000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[932] _id=6ab3d721485cab4c954cb6e3 ts=2026-09-23T13:41:53.1840000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[1551] _id=6ab52606485cab4c95511cc5 ts=2026-09-24T13:30:46.1260000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[1857] _id=6ab6776e485cab4c95550cfa ts=2026-09-25T13:30:22.6870000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5043 | 0.0 | 0.68 | 243.871 | 10.163 | 344456.617 | 0.25 | 201 | 16 |
| PuzzlePieceVisibleEvent | 2177 | 0.0 | 0.043 | 237.894 | 1.557 | 358156.085 | 0.25 | 1176 | 4 |
| PlayerPositionEvent | 2133 | 8.182 | 9.999 | 571.493 | 10.14 | 344263.398 | 0.1 | 0 | 12 |
| DialogueEvent | 1013 | 0.001 | 6.451 | 1201.424 | 81.516 | 344330.233 | 0.05 | 240 | 12 |
| ObjectInterEvent | 203 | 0.004 | 3.791 | 5988.535 | 554.693 | 518220.008 | 0.01 | 4 | 10 |
| argumentationNodeEvent | 171 | 0.013 | 0.41 | 504.199 | 12.468 | 85332.175 | 0.12 | 25 | 1 |
| TopographicMapEvent | 132 | 0.37 | 9.162 | 4589.823 | 5566.153 | 345196.428 | 0.01 | 0 | 11 |
| questEvent | 51 | 0.001 | 445.261 | 24113.348 | 85680.109 | 345603.689 | 0.0 | 10 | 22 |
| gameWindowFocusEvent | 27 | 0.045 | 1628.639 | 45550.394 | 220465.851 | 345805.301 | 0.0 | 1 | 17 |
| gameWindowUnfocusEvent | 22 | 0.462 | 6305.503 | 55815.203 | 331987.936 | 364704.322 | 0.0 | 0 | 11 |
| DEBUGMenu | 17 | 7.395 | 72852.897 | 72341.074 | 291132.408 | 345853.054 | 0.0 | 0 | 15 |
| gameStartEvent | 15 | 920.702 | 73891.497 | 81990.709 | 297968.652 | 345805.301 | 0.0 | 0 | 15 |
| argumentationToolEvent | 6 | 3.653 | 20.462 | 14317.78 | 64170.441 | 85411.809 | 0.0 | 0 | 1 |
| DaniEvent | 5 | 1.127 | 5.471 | 121171.863 | 484675.466 | 605842.614 | 0.0 | 0 | 1 |
| argumentationEvent | 5 | 26.833 | 42.833 | 17179.128 | 68390.569 | 85388.924 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationAnswerEvent | 2 | 444.057 | 42939.461 | 42939.461 | 81185.326 | 85434.866 | 0.0 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[9246] _id=6ac65ad5de269131f9bb0cec ts=2026-10-07T14:44:38.3940000Z == 6aa413b141b41dbac0c7f1f8.jsonl[9247] _id=6ac65ad5de269131f9bb0ced ts=2026-10-07T14:44:38.3940000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[10228] _id=6ac65faede269131f9bb785f ts=2026-10-07T15:05:18.5860000Z == 6aa413b141b41dbac0c7f1f8.jsonl[10229] _id=6ac65faede269131f9bb7860 ts=2026-10-07T15:05:18.5860000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 33 group(s), 40 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[3105] _id=6abd23eb485cab4c958b9d27 ts=2026-09-30T14:59:55.1840000Z == 6aa413b141b41dbac0c7f1f8.jsonl[3089] _id=6abd23eb485cab4c958b9d2e ts=2026-09-30T14:59:55.1840000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3172] _id=6abd23fa485cab4c958b9e10 ts=2026-09-30T14:59:59.8830000Z == 6aa413b141b41dbac0c7f1f8.jsonl[3081] _id=6abd23fa485cab4c958b9e17 ts=2026-09-30T14:59:59.8830000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3199] _id=6abd23fa485cab4c958b9e1d ts=2026-09-30T14:59:59.9360000Z == 6aa413b141b41dbac0c7f1f8.jsonl[3179] _id=6abd23fa485cab4c958b9e20 ts=2026-09-30T14:59:59.9360000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[3015] _id=6abd235d485cab4c958b9668 ts=? == 6aa413b141b41dbac0c7f1f8.jsonl[6022] _id=6abe72e0485cab4c95a95fee ts=?`; `6aa413b141b41dbac0c7f1f8.jsonl[4515] _id=6abd518d485cab4c95910571 ts=? == 6aa413b141b41dbac0c7f1f8.jsonl[6583] _id=6ac3b9dade269131f9acb4c1 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 82 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `838ms: 6aa413b141b41dbac0c7f1f8.jsonl[245] _id=6ab3d1de485cab4c954bdc50 ts=2026-09-23T13:19:26.9040000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[247] _id=6ab3d1df485cab4c954bdc5c ts=2026-09-23T13:19:27.7420000Z`; `661ms: 6aa413b141b41dbac0c7f1f8.jsonl[247] _id=6ab3d1df485cab4c954bdc5c ts=2026-09-23T13:19:27.7420000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[263] _id=6ab3d1e0485cab4c954bdc70 ts=2026-09-23T13:19:28.4030000Z`; `386ms: 6aa413b141b41dbac0c7f1f8.jsonl[263] _id=6ab3d1e0485cab4c954bdc70 ts=2026-09-23T13:19:28.4030000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[259] _id=6ab3d1e0485cab4c954bdc7e ts=2026-09-23T13:19:28.7890000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 247 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `206ms: 6aa413b141b41dbac0c7f1f8.jsonl[3467] _id=6abd25c8485cab4c958bb9ff ts=2026-09-30T14:59:52.4130000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[3468] _id=6abd25c8485cab4c958bba01 ts=2026-09-30T14:59:52.6190000Z`; `12ms: 6aa413b141b41dbac0c7f1f8.jsonl[3116] _id=6abd23ec485cab4c958b9d49 ts=2026-09-30T14:59:55.3850000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[3097] _id=6abd23ec485cab4c958b9d4b ts=2026-09-30T14:59:55.3970000Z`; `32ms: 6aa413b141b41dbac0c7f1f8.jsonl[3081] _id=6abd23fa485cab4c958b9e17 ts=2026-09-30T14:59:59.8830000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[3165] _id=6abd23fa485cab4c958b9e1a ts=2026-09-30T14:59:59.9150000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `958ms: 6aa413b141b41dbac0c7f1f8.jsonl[2458] _id=6abab4dd485cab4c95704703 ts=2026-09-28T18:41:33.6150000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[2456] _id=6abab4de485cab4c95704727 ts=2026-09-28T18:41:34.5730000Z`; `196ms: 6aa413b141b41dbac0c7f1f8.jsonl[2469] _id=6abab4e0485cab4c95704751 ts=2026-09-28T18:41:36.1130000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[2466] _id=6abab4e0485cab4c9570475b ts=2026-09-28T18:41:36.3090000Z`; `774ms: 6aa413b141b41dbac0c7f1f8.jsonl[2465] _id=6abab4e0485cab4c95704757 ts=2026-09-28T18:41:36.1410000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[2467] _id=6abab4e1485cab4c95704761 ts=2026-09-28T18:41:36.9150000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6aa413b141b41dbac0c7f1f8.jsonl[6857] _id=6ac3bc6ede269131f9acccf1 ts=2026-10-05T15:04:14.2480000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[6859] _id=6ac3bc6ede269131f9acccf7 ts=2026-10-05T15:04:14.2930000Z`; `639ms: 6aa413b141b41dbac0c7f1f8.jsonl[10695] _id=6ac6612ade269131f9bb8f6f ts=2026-10-07T15:11:38.8460000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[10697] _id=6ac6612bde269131f9bb8f75 ts=2026-10-07T15:11:39.4850000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `462ms: 6aa413b141b41dbac0c7f1f8.jsonl[10692] _id=6ac66129de269131f9bb8f61 ts=2026-10-07T15:11:37.3840000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[10694] _id=6ac66129de269131f9bb8f6b ts=2026-10-07T15:11:37.8460000Z`; `636ms: 6aa413b141b41dbac0c7f1f8.jsonl[10696] _id=6ac6612ade269131f9bb8f71 ts=2026-10-07T15:11:38.8550000Z ~ 6aa413b141b41dbac0c7f1f8.jsonl[10698] _id=6ac6612bde269131f9bb8f7a ts=2026-10-07T15:11:39.4910000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 6aa413b141b41dbac0c7f1f8.jsonl[6021] _id=6abe72da485cab4c95a95f08 ts=2026-10-01T14:48:58.1270000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6561] _id=6ac3b9d4de269131f9acb495 ts=2026-10-05T14:53:11.1810000Z; 77h 4m: 6aa413b141b41dbac0c7f1f8.jsonl[1560] _id=6ab671ba485cab4c955469bf ts=2026-09-25T13:06:02.3570000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1860] _id=6abaad86485cab4c956f87c6 ts=2026-09-28T18:10:14.6040000Z; 24h 17m: 6aa413b141b41dbac0c7f1f8.jsonl[1860] _id=6abaad86485cab4c956f87c6 ts=2026-09-28T18:10:14.6040000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2623] _id=6abc032e485cab4c95847221 ts=2026-09-29T18:27:58.0130000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 168h 17m 
  - Evidence: 168h 17m: 6aa413b141b41dbac0c7f1f8.jsonl[3040] _id=6abd2372485cab4c958b97d3 ts=2026-09-30T14:57:54.3710000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[10926] _id=6ac66205de269131f9bb97c2 ts=2026-10-07T15:15:16.9850000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa413b141b41dbac0c7f1f8.jsonl[6530] _id=6abe790b485cab4c95a9fe61 ts=2026-10-01T15:15:23.6400000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6628] _id=6ac3ba14de269131f9acb65b ts=2026-10-05T14:54:13.8730000Z; 76h 43m: 6aa413b141b41dbac0c7f1f8.jsonl[1855] _id=6ab67764485cab4c95550c08 ts=2026-09-25T13:30:12.5330000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1959] _id=6abaae3f485cab4c956fa1eb ts=2026-09-28T18:13:19.5130000Z; 23h 41m: 6aa413b141b41dbac0c7f1f8.jsonl[2609] _id=6abab652485cab4c9570697f ts=2026-09-28T18:47:46.6450000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2651] _id=6abc036d485cab4c95847955 ts=2026-09-29T18:29:01.0750000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 240 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f8.jsonl[2880] _id=6abc063b485cab4c9584a9f1 ts=2026-09-29T18:40:59.3310000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2873] _id=6abc063b485cab4c9584a9f5 ts=2026-09-29T18:40:59.3320000Z; 2ms: 6aa413b141b41dbac0c7f1f8.jsonl[2805] _id=6abc05b0485cab4c95849df5 ts=2026-09-29T18:38:39.8640000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2804] _id=6abc05b0485cab4c95849df7 ts=2026-09-29T18:38:39.8660000Z; 2ms: 6aa413b141b41dbac0c7f1f8.jsonl[2847] _id=6abc05ff485cab4c9584a50d ts=2026-09-29T18:39:59.3900000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2848] _id=6abc05ff485cab4c9584a511 ts=2026-09-29T18:39:59.3920000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 6aa413b141b41dbac0c7f1f8.jsonl[6497] _id=6abe784e485cab4c95a9e7ff ts=2026-10-01T15:12:14.5830000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6587] _id=6ac3b9dade269131f9acb4c7 ts=2026-10-05T14:53:11.2000000Z; 76h 42m: 6aa413b141b41dbac0c7f1f8.jsonl[1826] _id=6ab676f3485cab4c9554f98a ts=2026-09-25T13:28:19.6400000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1863] _id=6abaad8c485cab4c956f889b ts=2026-09-28T18:10:20.0060000Z; 23h 43m: 6aa413b141b41dbac0c7f1f8.jsonl[2531] _id=6abab5a5485cab4c95705531 ts=2026-09-28T18:44:53.8270000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2630] _id=6abc0343485cab4c958473cf ts=2026-09-29T18:28:19.8740000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 201 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f8.jsonl[10228] _id=6ac65faede269131f9bb785f ts=2026-10-07T15:05:18.5860000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[10229] _id=6ac65faede269131f9bb7860 ts=2026-10-07T15:05:18.5860000Z; 0ms: 6aa413b141b41dbac0c7f1f8.jsonl[9246] _id=6ac65ad5de269131f9bb0cec ts=2026-10-07T14:44:38.3940000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[9247] _id=6ac65ad5de269131f9bb0ced ts=2026-10-07T14:44:38.3940000Z; 0ms: 6aa413b141b41dbac0c7f1f8.jsonl[9247] _id=6ac65ad5de269131f9bb0ced ts=2026-10-07T14:44:38.3940000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[9248] _id=6ac65ad5de269131f9bb0cee ts=2026-10-07T14:44:38.3940000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 6aa413b141b41dbac0c7f1f8.jsonl[5700] _id=6abd5435485cab4c95916d95 ts=2026-09-30T18:25:57.7290000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[8063] _id=6ac53c81de269131f9b65523 ts=2026-10-06T18:22:57.7370000Z; 76h 47m: 6aa413b141b41dbac0c7f1f8.jsonl[1835] _id=6ab676f6485cab4c9554fa32 ts=2026-09-25T13:28:23.1730000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2014] _id=6abaaeec485cab4c956fb229 ts=2026-09-28T18:16:12.4630000Z; 23h 48m: 6aa413b141b41dbac0c7f1f8.jsonl[2439] _id=6abab4a2485cab4c95704083 ts=2026-09-28T18:40:34.0470000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2650] _id=6abc036d485cab4c9584794f ts=2026-09-29T18:29:01.0600000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6aa413b141b41dbac0c7f1f8.jsonl[1605] _id=6ab67232485cab4c95546f83 ts=2026-09-25T13:08:03.2180000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1556] _id=6ab67233485cab4c95546f86 ts=2026-09-25T13:08:03.2220000Z; 4ms: 6aa413b141b41dbac0c7f1f8.jsonl[599] _id=6ab3d419485cab4c954c3cd1 ts=2026-09-23T13:28:57.3780000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[600] _id=6ab3d419485cab4c954c3cd5 ts=2026-09-23T13:28:57.3820000Z; 5ms: 6aa413b141b41dbac0c7f1f8.jsonl[2014] _id=6abaaeec485cab4c956fb229 ts=2026-09-28T18:16:12.4630000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2009] _id=6abaaeec485cab4c956fb22d ts=2026-09-28T18:16:12.4680000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa413b141b41dbac0c7f1f8.jsonl[6526] _id=6abe790f485cab4c95a9fefc ts=2026-10-01T15:15:27.7900000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6560] _id=6ac3b9dade269131f9acb4c5 ts=2026-10-05T14:53:11.1880000Z; 76h 39m: 6aa413b141b41dbac0c7f1f8.jsonl[1856] _id=6ab67769485cab4c95550c7c ts=2026-09-25T13:30:17.3810000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1862] _id=6abaad8c485cab4c956f8897 ts=2026-09-28T18:10:14.6100000Z; 23h 40m: 6aa413b141b41dbac0c7f1f8.jsonl[2612] _id=6abab658485cab4c95706b2d ts=2026-09-28T18:47:52.4580000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2624] _id=6abc032e485cab4c9584722b ts=2026-09-29T18:27:58.0180000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 99h 29m 
  - Evidence: 99h 29m: 6aa413b141b41dbac0c7f1f8.jsonl[6491] _id=6abe7837485cab4c95a9e4f4 ts=2026-10-01T15:11:51.3840000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[7312] _id=6ac3ef44de269131f9af43cf ts=2026-10-05T18:41:07.4690000Z; 20h 46m: 6aa413b141b41dbac0c7f1f8.jsonl[5380] _id=6abd540e485cab4c959168bd ts=2026-09-30T18:25:17.3540000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6475] _id=6abe7831485cab4c95a9e417 ts=2026-10-01T15:11:44.1740000Z; 20h 9m: 6aa413b141b41dbac0c7f1f8.jsonl[7321] _id=6ac3ef4bde269131f9af4439 ts=2026-10-05T18:41:14.2340000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[7517] _id=6ac50adade269131f9b3ff4f ts=2026-10-06T14:51:05.5490000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1176 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f8.jsonl[3007] _id=6abd23fc485cab4c958b9e75 ts=2026-09-30T15:00:02.5280000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[3008] _id=6abd23fd485cab4c958b9e7b ts=2026-09-30T15:00:02.5280000Z; 0ms: 6aa413b141b41dbac0c7f1f8.jsonl[3099] _id=6abd23ee485cab4c958b9d65 ts=2026-09-30T14:59:55.9610000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[3109] _id=6abd23ee485cab4c958b9d67 ts=2026-09-30T14:59:55.9610000Z; 0ms: 6aa413b141b41dbac0c7f1f8.jsonl[3101] _id=6abd23eb485cab4c958b9d33 ts=2026-09-30T14:59:55.1900000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[3090] _id=6abd23eb485cab4c958b9d35 ts=2026-09-30T14:59:55.1900000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa413b141b41dbac0c7f1f8.jsonl[6389] _id=6abe772b485cab4c95a9b433 ts=2026-10-01T15:07:23.1090000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6767] _id=6ac3bb97de269131f9acc311 ts=2026-10-05T15:00:39.5370000Z; 20h 24m: 6aa413b141b41dbac0c7f1f8.jsonl[9222] _id=6ac542d6de269131f9b6f877 ts=2026-10-06T18:49:58.1350000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[10854] _id=6ac661d2de269131f9bb96e6 ts=2026-10-07T15:14:26.5740000Z; 20h 16m: 6aa413b141b41dbac0c7f1f8.jsonl[6002] _id=6abd56c5485cab4c9591cf4f ts=2026-09-30T18:36:53.3950000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6104] _id=6abe73ea485cab4c95a97404 ts=2026-10-01T14:53:30.2600000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 43m 
  - Evidence: 23h 43m: 6aa413b141b41dbac0c7f1f8.jsonl[2603] _id=6abab638485cab4c957061cb ts=2026-09-28T18:47:20.8980000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2715] _id=6abc03f3485cab4c95848397 ts=2026-09-29T18:31:15.7640000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 43m 
  - Evidence: 23h 43m: 6aa413b141b41dbac0c7f1f8.jsonl[2608] _id=6abab643485cab4c957064d2 ts=2026-09-28T18:47:31.0450000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2695] _id=6abc03d0485cab4c95848238 ts=2026-09-29T18:30:39.9690000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 42m 
  - Evidence: 23h 42m: 6aa413b141b41dbac0c7f1f8.jsonl[2601] _id=6abab636485cab4c957060f7 ts=2026-09-28T18:47:18.4650000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2661] _id=6abc038a485cab4c95847d77 ts=2026-09-29T18:29:30.6400000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 25 interval(s) ≤ 0.013s..0.019s shown 
  - Evidence: 13ms: 6aa413b141b41dbac0c7f1f8.jsonl[2588] _id=6abab634485cab4c957060af ts=2026-09-28T18:47:16.7020000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2598] _id=6abab634485cab4c957060b3 ts=2026-09-28T18:47:16.7150000Z; 16ms: 6aa413b141b41dbac0c7f1f8.jsonl[2592] _id=6abab62a485cab4c95705fed ts=2026-09-28T18:47:06.7450000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2597] _id=6abab62a485cab4c95705fef ts=2026-09-28T18:47:06.7610000Z; 19ms: 6aa413b141b41dbac0c7f1f8.jsonl[2602] _id=6abab636485cab4c957060f0 ts=2026-09-28T18:47:18.4460000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2601] _id=6abab636485cab4c957060f7 ts=2026-09-28T18:47:18.4650000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 43m 
  - Evidence: 23h 43m: 6aa413b141b41dbac0c7f1f8.jsonl[2594] _id=6abab628485cab4c95705fad ts=2026-09-28T18:47:04.1760000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2689] _id=6abc03cc485cab4c95848211 ts=2026-09-29T18:30:35.9850000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1f8.jsonl[6020] _id=6abe72ce485cab4c95a95d90 ts=2026-10-01T14:48:46.3880000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6555] _id=6ac3b997de269131f9acb395 ts=2026-10-05T14:52:11.6890000Z; 77h 4m: 6aa413b141b41dbac0c7f1f8.jsonl[1559] _id=6ab6719d485cab4c955468f1 ts=2026-09-25T13:05:33.8550000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1859] _id=6abaad79485cab4c956f8603 ts=2026-09-28T18:10:01.0860000Z; 24h 17m: 6aa413b141b41dbac0c7f1f8.jsonl[1859] _id=6abaad79485cab4c956f8603 ts=2026-09-28T18:10:01.0860000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2621] _id=6abc031f485cab4c958470c3 ts=2026-09-29T18:27:43.7210000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1f8.jsonl[6019] _id=6abe72ce485cab4c95a95d8a ts=2026-10-01T14:48:46.3870000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6559] _id=6ac3b997de269131f9acb393 ts=2026-10-05T14:52:11.6880000Z; 77h 4m: 6aa413b141b41dbac0c7f1f8.jsonl[1558] _id=6ab6719d485cab4c955468ef ts=2026-09-25T13:05:33.8550000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1858] _id=6abaad79485cab4c956f85fc ts=2026-09-28T18:10:01.0850000Z; 24h 17m: 6aa413b141b41dbac0c7f1f8.jsonl[1858] _id=6abaad79485cab4c956f85fc ts=2026-09-28T18:10:01.0850000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2620] _id=6abc031f485cab4c958470c1 ts=2026-09-29T18:27:43.7200000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.045s..0.045s shown 
  - Evidence: 45ms: 6aa413b141b41dbac0c7f1f8.jsonl[6857] _id=6ac3bc6ede269131f9acccf1 ts=2026-10-05T15:04:14.2480000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6859] _id=6ac3bc6ede269131f9acccf7 ts=2026-10-05T15:04:14.2930000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 101h 18m 
  - Evidence: 101h 18m: 6aa413b141b41dbac0c7f1f8.jsonl[1857] _id=6ab6776e485cab4c95550cfa ts=2026-09-25T13:30:22.6870000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2980] _id=6abc080f485cab4c9584caa1 ts=2026-09-29T18:48:47.0090000Z; 95h 48m: 6aa413b141b41dbac0c7f1f8.jsonl[6527] _id=6abe790f485cab4c95a9fede ts=2026-10-01T15:15:27.2190000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6856] _id=6ac3bc62de269131f9accc93 ts=2026-10-05T15:04:02.0700000Z; 23h 59m: 6aa413b141b41dbac0c7f1f8.jsonl[1551] _id=6ab52606485cab4c95511cc5 ts=2026-09-24T13:30:46.1260000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1857] _id=6ab6776e485cab4c95550cfa ts=2026-09-25T13:30:22.6870000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 6aa413b141b41dbac0c7f1f8.jsonl[6099] _id=6abe73d9485cab4c95a97314 ts=2026-10-01T14:53:13.5590000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[6580] _id=6ac3b9dcde269131f9acb4ed ts=2026-10-05T14:53:17.2480000Z; 76h 49m: 6aa413b141b41dbac0c7f1f8.jsonl[1713] _id=6ab67516485cab4c9554b4ae ts=2026-09-25T13:20:22.8270000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1866] _id=6abaad8d485cab4c956f88bf ts=2026-09-28T18:10:20.3890000Z; 23h 48m: 6aa413b141b41dbac0c7f1f8.jsonl[1378] _id=6ab522eb485cab4c95506bce ts=2026-09-24T13:17:30.9390000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1567] _id=6ab671bf485cab4c955469f1 ts=2026-09-25T13:06:06.5120000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f8.jsonl[2440] _id=6abab4a2485cab4c9570408b ts=2026-09-28T18:40:34.0930000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2443] _id=6abab4a2485cab4c9570408d ts=2026-09-28T18:40:34.0940000Z; 2ms: 6aa413b141b41dbac0c7f1f8.jsonl[2649] _id=6abc036d485cab4c95847960 ts=2026-09-29T18:29:01.0910000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[2647] _id=6abc036d485cab4c95847965 ts=2026-09-29T18:29:01.0930000Z; 4ms: 6aa413b141b41dbac0c7f1f8.jsonl[1624] _id=6ab67297485cab4c95547743 ts=2026-09-25T13:09:43.6830000Z -> 6aa413b141b41dbac0c7f1f8.jsonl[1625] _id=6ab67297485cab4c95547745 ts=2026-09-25T13:09:43.6870000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[2256] _id=6abab2ff485cab4c95701a0d ts=2026-09-28T18:33:35.8660000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[7024] _id=6ac3eb09de269131f9aef0dd ts=2026-10-05T18:23:05.7600000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[8141] _id=6ac53da9de269131f9b66981 ts=2026-10-06T18:27:53.4660000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 21 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[3973] _id=6abd261b485cab4c958bc27d ts=2026-09-30T15:09:14.8480000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[4040] _id=6abd2625485cab4c958bc381 ts=2026-09-30T15:09:23.2990000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[4044] _id=6abd2625485cab4c958bc385 ts=2026-09-30T15:09:23.6290000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 124 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[3443] _id=6abd25c8485cab4c958bb9eb ts=2026-09-30T14:59:51.6180000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3097] _id=6abd23ec485cab4c958b9d4b ts=2026-09-30T14:59:55.3970000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3120] _id=6abd23ee485cab4c958b9d7b ts=2026-09-30T14:59:57.7290000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[2597] _id=6abab62a485cab4c95705fef ts=2026-09-28T18:47:06.7610000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[2598] _id=6abab634485cab4c957060b3 ts=2026-09-28T18:47:16.7150000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[2601] _id=6abab636485cab4c957060f7 ts=2026-09-28T18:47:18.4650000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[942] _id=6ab51e3b485cab4c954fd80d ts=?`; `6aa413b141b41dbac0c7f1f8.jsonl[3015] _id=6abd235d485cab4c958b9668 ts=?`; `6aa413b141b41dbac0c7f1f8.jsonl[4515] _id=6abd518d485cab4c95910571 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 106 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[4056] _id=6abd2625485cab4c958bc3c1 ts=2026-09-30T15:09:24.2690000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[4051] _id=6abd2625485cab4c958bc3c5 ts=2026-09-30T15:09:24.4800000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[4060] _id=6abd2627485cab4c958bc3f6 ts=2026-09-30T15:09:26.1950000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 638 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[3461] _id=6abd25c8485cab4c958bb9fd ts=2026-09-30T14:59:52.4130000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3105] _id=6abd23eb485cab4c958b9d27 ts=2026-09-30T14:59:55.1840000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3089] _id=6abd23eb485cab4c958b9d2e ts=2026-09-30T14:59:55.1840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 60 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[6104] _id=6abe73ea485cab4c95a97404 ts=2026-10-01T14:53:30.2600000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[6120] _id=6abe7412485cab4c95a97666 ts=2026-10-01T14:54:10.6730000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[6180] _id=6abe7464485cab4c95a97bc8 ts=2026-10-01T14:55:32.8760000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[2800] _id=6abc05ac485cab4c95849d9d ts=2026-09-29T18:38:35.9810000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'DialogueStartEvent' (totals: 176 start, 167 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 35 unmatched 'BecameCameraCentered' (totals: 199 open, 185 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 100 unmatched 'BecameVisible' (totals: 885 open, 909 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 65 open, 63 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 33 start, 19 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 95 of 11040 adjacent _id pairs reverse in client time; worst 479.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f8.jsonl[3447] _id=6abd25c6485cab4c958bb9d7 ts=2026-09-30T15:07:50.6180000Z`; `6aa413b141b41dbac0c7f1f8.jsonl[3448] _id=6abd25c7485cab4c958bb9db ts=2026-09-30T14:59:51.5710000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -480.49s, max +4.62s over 11041 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f8\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `Soil Key Puzzle` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [3, 4] 
  - Evidence: coverage: Unit3=partial, Unit4=skipped 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
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

### `InputEvent` — 5044 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2500); Unit 2 Prod (Refactor) (1311); Unit 1 Dev (1233)
- **Intervals:** median 0.68s (p5 0.07s / p95 10.16s, n=5043)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5044/5044 records)
    "pressed"  x5044
data.actionType  (string, 5044/5044 records)
    "Move"  x4030
    "Jump"  x293
    "Interact"  x260
    "Sprint"  x199
    "Ascend"  x141
    "Hoverboard"  x56
    "ToggleDebug"  x32
    "Descend"  x22
    "Map"  x7
    "Pause"  x4
data.key  (string, 5044/5044 records, 83 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5044/5044 records)
    "Player"  x2662
    "Drone"  x2382
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2178 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2178)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.56s, n=2177)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2178/2178 records)
    "BecameInvisible"  x909
    "BecameVisible"  x885
    "BecameCameraCentered"  x199
    "BecameCameraUncentered"  x185
data.pieceId  (string, 2178/2178 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2178/2178 records)
    1622 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2136 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (877); Unit 1 Dev (846); Unit 3 Dev (413)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.14s, n=2133)
- **Fields under `data`:**

```text
data.position  (object, 2136/2136 records)
data.position.x  (number, 2136/2136 records)
    numeric range -38.1751 .. 3416.3 (723 unique)
data.position.y  (number, 2136/2136 records)
    numeric range -69433.8 .. 170.599 (569 unique)
data.position.z  (number, 2136/2136 records)
    numeric range -592.152 .. 2602.85 (723 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1014 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (434); Unit 2 Prod (Refactor) (426); Unit 3 Dev (154)
- **eventKey:** present on 671 of 1014 records
- **Intervals:** median 6.45s (p5 0.00s / p95 81.52s, n=1013)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x671; [conversationId, dialogueEventType] x343
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1014/1014 records)
    numeric range 10 .. 70 (19 unique)
data.dialogueEventType  (string, 1014/1014 records)
    "DialogueNodeEvent"  x671
    "DialogueStartEvent"  x176
    "DialogueFinishEvent"  x167
data.nodeId  (number, 671/1014 records)
    numeric range 0 .. 283 (136 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 204 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (151); Unit 2 Prod (Refactor) (47); Unit 3 Dev (6)
- **Intervals:** median 3.79s (p5 0.18s / p95 554.69s, n=203)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 204/204 records)
    "TalkTo"  x96
    "E to Talk"  x45
    "Press E to Pick up"  x22
    "Press E to Place"  x20
    "Press E to Open Locker"  x8
    "Press E to Install"  x3
    "Push E To Grab Crate"  x3
    "Press E To Pick Up"  x2
    "Press E to Collect"  x2
    "Inspect Alien Glyph"  x1
    "Press [E/Action button] to enter escape pod "  x1
    "Push E To Place Crate On Hoverboard"  x1
data.objectName  (string, 204/204 records)
    26 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 172 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (172)
- **Intervals:** median 0.41s (p5 0.03s / p95 12.47s, n=171)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 172/172 records)
    "argumentationNodeHoverEnd"  x86
    "argumentationNodeHoverStart"  x83
    "argumentationNodeAdd"  x3
data.argumentationTitle  (string, 172/172 records)
    "Unit 1 - Argumentation Tutorial"  x145
    "Unit 1 - Freshwater"  x27
data.nodeName  (string, 172/172 records)
    "1"  x70
    "I"  x48
    "A"  x46
    "II"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 133 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (115); Unit 3 Dev (18)
- **Intervals:** median 9.16s (p5 1.10s / p95 5566.15s, n=132)
- **`data` key-set variants:** [actionType, featureUsed] x128; [actionType, featureUsed, location] x5
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 133/133 records)
    "MapOpenEvent"  x65
    "MapCloseEvent"  x63
    "WaypointMoveEvent"  x4
    "WaypointSetEvent"  x1
data.featureUsed  (string, 133/133 records)
    "Map"  x128
    "Waypoint"  x5
data.location  (object, 5/133 records)
data.location.x  (number, 5/133 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/133 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/133 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 52 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (30); Unit 2 Prod (Refactor) (15); Unit 3 Dev (7)
- **eventKey:** present on 52 of 52 records
- **Intervals:** median 445.26s (p5 0.00s / p95 85680.11s, n=51)
- **`data` key-set variants:** [questEventType, questID, questName] x33; [questEventType, questID, questName, questSuccessOrFailure] x19
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 52/52 records)
    "questActiveEvent"  x33
    "questFinishEvent"  x19
data.questID  (string, 52/52 records)
    "29"  x8
    "31"  x8
    "32"  x7
    "22"  x6
    "16"  x5
    "21"  x5
    "23"  x4
    "33"  x3
    "17"  x2
    "28"  x2
    "34"  x2
data.questName  (string, 52/52 records)
    "Gear Up"  x8
    "TK, Reporting In!"  x8
    "Info and Intros"  x7
    "Getting the Band Back Together"  x6
    "Escape the Ruin"  x5
    "Supply Run"  x5
    "Foraged Forging"  x4
    "Defend the Expedition"  x3
    "Getting Your Space Legs"  x2
    "Pollution Solution"  x2
    "What Was That?"  x2
data.questSuccessOrFailure  (string, 19/52 records)
    "Succeeded"  x19
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 3 Dev (8); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 1628.64s (p5 0.75s / p95 220465.85s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 23 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (11); Unit 2 Prod (Refactor) (9); Unit 1 Dev (3)
- **Intervals:** median 6305.50s (p5 0.65s / p95 331987.94s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 18 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (5); Unit 3 Dev (3); MainMenu (2)
- **Intervals:** median 72852.90s (p5 8.01s / p95 291132.41s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "DebugMenuStateChanged"  x18
data.isOpened  (bool, 18/18 records)
    false  x18
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 73891.50s (p5 1177.60s / p95 297968.65s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 20.46s (p5 3.73s / p95 64170.44s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - "  x3
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (2)
- **Intervals:** median 5.47s (p5 1.55s / p95 484675.47s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 6 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6)
- **Intervals:** median 42.83s (p5 29.45s / p95 68390.57s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationSessionClose"  x3
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 6/6 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x3
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x3
data.type  (string, 6/6 records)
    "unhandled_rejection"  x6
data.unitId  (string, 6/6 records)
    "unit2"  x5
    "unit1"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationAnswerEvent` — 3 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (3)
- **Intervals:** median 42939.46s (p5 4693.60s / p95 81185.33s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "submitAnswerEvent"  x3
data.answerSubmitted  (string, 3/3 records, 1 empty-string)
    "A,1,I"  x2
    ""  x1
data.argumentationTitle  (string, 3/3 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

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
- `Soil Key Puzzle` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : event type present in baseline 09-23-26 but absent now
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (4x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*