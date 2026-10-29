# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba0

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba0
- **Game version string(s) in log:** 2.9.1, 2.9.6, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba0.jsonl
- **Records:** 7776 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba0
- **Time span:** 2026-10-06T19:48:30.517000+00:00 .. 2026-10-19T16:15:26.940000+00:00 (308h 26m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba0\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 7776 records, 3 scenes.
- Findings: **0 FAIL**, **27 WARNING**, 89 INFO, 6 NOT_TESTED, 72 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3018 | 38.81 | 1 | 2 | 0 | 2026-10-06T19:50:13.956000+00:00 | 2026-10-19T16:14:55.729000+00:00 | 308h 24m |
| PuzzlePieceVisibleEvent | 1805 | 23.21 | 1 | 1 | 0 | 2026-10-08T20:01:30.142000+00:00 | 2026-10-19T14:20:38.998000+00:00 | 258h 19m |
| PlayerPositionEvent | 1334 | 17.16 | 1 | 2 | 0 | 2026-10-06T19:50:10.484000+00:00 | 2026-10-19T16:15:19.363000+00:00 | 308h 25m |
| DialogueEvent | 1066 | 13.71 | 1 | 2 | 747 | 2026-10-06T19:50:30.737000+00:00 | 2026-10-19T16:15:26.940000+00:00 | 308h 24m |
| argumentationNodeEvent | 161 | 2.07 | 1 | 2 | 0 | 2026-10-07T20:05:10.529000+00:00 | 2026-10-19T16:11:43.079000+00:00 | 284h 6m |
| ObjectInterEvent | 103 | 1.32 | 1 | 2 | 0 | 2026-10-07T19:42:48.207000+00:00 | 2026-10-19T16:06:11.901000+00:00 | 284h 23m |
| Soil Key Puzzle | 85 | 1.09 | 1 | 1 | 0 | 2026-10-08T20:09:51.209000+00:00 | 2026-10-19T16:03:28.950000+00:00 | 259h 53m |
| TopographicMapEvent | 54 | 0.69 | 1 | 1 | 0 | 2026-10-08T20:02:59.015000+00:00 | 2026-10-15T19:57:35.793000+00:00 | 167h 54m |
| questEvent | 36 | 0.46 | 1 | 2 | 36 | 2026-10-06T19:50:30.711000+00:00 | 2026-10-19T16:14:08.739000+00:00 | 308h 23m |
| argumentationToolEvent | 23 | 0.3 | 1 | 2 | 0 | 2026-10-07T20:05:02.258000+00:00 | 2026-10-19T16:11:05.639000+00:00 | 284h 6m |
| DEBUGMenu | 22 | 0.28 | 1 | 3 | 0 | 2026-10-06T19:48:30.517000+00:00 | 2026-10-19T15:55:24.186000+00:00 | 308h 6m |
| argumentationAnswerEvent | 18 | 0.23 | 1 | 2 | 0 | 2026-10-07T20:05:28.395000+00:00 | 2026-10-19T16:11:45.032000+00:00 | 284h 6m |
| gameWindowFocusEvent | 15 | 0.19 | 1 | 2 | 0 | 2026-10-06T19:48:31.002000+00:00 | 2026-10-19T15:54:49.315000+00:00 | 308h 6m |
| gameStartEvent | 11 | 0.14 | 1 | 1 | 0 | 2026-10-06T19:48:31.002000+00:00 | 2026-10-19T15:54:49.315000+00:00 | 308h 6m |
| gameWindowUnfocusEvent | 11 | 0.14 | 1 | 2 | 0 | 2026-10-06T20:11:55.213000+00:00 | 2026-10-19T14:18:50.242000+00:00 | 306h 6m |
| argumentationEvent | 9 | 0.12 | 1 | 2 | 0 | 2026-10-07T20:05:02.344000+00:00 | 2026-10-19T16:11:45.050000+00:00 | 284h 6m |
| DaniEvent | 2 | 0.03 | 1 | 1 | 0 | 2026-10-14T19:52:38.520000+00:00 | 2026-10-14T19:52:40.785000+00:00 | 2.3s |
| crash | 2 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-10-08T19:55:11.959000+00:00 | 2026-10-08T19:55:11.959000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 99.944s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.072s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.854s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 24.291s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 138.056s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.781s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 73662.068s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 13586.121s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 71754.69s median 
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
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; h 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,1,; A,D,1,II; D,1,II; D,A,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
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
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[2] _id=6ac5508fde269131f9b7b9a2 ts=2026-10-06T19:48:31.0020000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[443] _id=6ac6a069de269131f9bf27da ts=2026-10-07T19:41:28.7310000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1049] _id=6ac7f1dade269131f9c6b778 ts=2026-10-08T19:41:13.8090000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1] _id=6ac5508fde269131f9b7b9a1 ts=2026-10-06T19:48:31.0020000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[442] _id=6ac6a069de269131f9bf27d9 ts=2026-10-07T19:41:28.7310000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1048] _id=6ac7f1dade269131f9c6b777 ts=2026-10-08T19:41:13.8090000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[444] _id=6ac6a069de269131f9bf27d4 ts=2026-10-06T20:11:55.213Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1046] _id=6ac7f1dade269131f9c6b774 ts=2026-10-07T20:09:13.89Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[2841] _id=6acfd867de269131f9d8c22b ts=2026-10-08T20:11:12.121Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 7 of 54 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1757] _id=6ac7f6f3de269131f9c722e1 ts=2026-10-08T20:02:59.0150000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1760] _id=6ac7f716de269131f9c72684 ts=2026-10-08T20:03:33.6980000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[3010] _id=6acfd915de269131f9d8d691 ts=2026-10-14T19:33:41.7730000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3017 | 0.0 | 0.491 | 368.009 | 7.284 | 516016.181 | 0.16 | 178 | 11 |
| PuzzlePieceVisibleEvent | 1804 | 0.0 | 0.072 | 515.493 | 1.509 | 516106.049 | 0.12 | 812 | 5 |
| PlayerPositionEvent | 1332 | 9.828 | 10.002 | 833.463 | 10.098 | 515995.324 | 0.07 | 0 | 9 |
| DialogueEvent | 1065 | 0.0 | 5.068 | 1042.532 | 46.141 | 516144.409 | 0.06 | 271 | 9 |
| argumentationNodeEvent | 160 | 0.005 | 0.724 | 6392.453 | 24.031 | 937058.755 | 0.01 | 9 | 2 |
| ObjectInterEvent | 102 | 0.005 | 11.929 | 10037.291 | 12227.83 | 516146.583 | 0.01 | 1 | 9 |
| Soil Key Puzzle | 84 | 0.078 | 0.867 | 11138.306 | 284.714 | 516128.122 | 0.01 | 0 | 4 |
| TopographicMapEvent | 53 | 0.02 | 3.854 | 11405.222 | 476.72 | 516608.075 | 0.01 | 2 | 3 |
| questEvent | 35 | 0.001 | 256.061 | 31720.515 | 131002.775 | 516737.407 | 0.0 | 6 | 13 |
| argumentationToolEvent | 22 | 0.007 | 1.781 | 46489.245 | 80696.101 | 937093.667 | 0.0 | 1 | 2 |
| DEBUGMenu | 21 | 9.097 | 99.944 | 52819.699 | 237667.741 | 516805.819 | 0.0 | 0 | 10 |
| argumentationAnswerEvent | 17 | 0.818 | 24.291 | 60163.332 | 255379.213 | 937145.291 | 0.0 | 0 | 2 |
| gameWindowFocusEvent | 14 | 510.504 | 13586.121 | 79227.022 | 335391.498 | 516842.356 | 0.0 | 0 | 12 |
| gameStartEvent | 10 | 931.601 | 73662.068 | 110917.831 | 391222.531 | 516842.356 | 0.0 | 0 | 10 |
| gameWindowUnfocusEvent | 10 | 436.542 | 71754.69 | 110201.503 | 398281.476 | 517590.304 | 0.0 | 0 | 9 |
| argumentationEvent | 8 | 30.335 | 138.056 | 127850.338 | 638814.828 | 937013.855 | 0.0 | 0 | 2 |
| DaniEvent | 1 | 2.265 | 2.265 | 2.265 | 2.265 | 2.265 | 26.49 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 10 group(s), 17 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[7] _id=6ac550f7de269131f9b7bc7d ts=2026-10-06T19:50:13.9570000Z == 6ab9a9439a8420a1e6b56ba0.jsonl[8] _id=6ac550f7de269131f9b7bc7e ts=2026-10-06T19:50:13.9570000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[9] _id=6ac550f7de269131f9b7bc7f ts=2026-10-06T19:50:13.9580000Z == 6ab9a9439a8420a1e6b56ba0.jsonl[10] _id=6ac550f7de269131f9b7bc80 ts=2026-10-06T19:50:13.9580000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[276] _id=6ac5547bde269131f9b82b48 ts=2026-10-06T20:05:14.5440000Z == 6ab9a9439a8420a1e6b56ba0.jsonl[279] _id=6ac5547bde269131f9b82b4b ts=2026-10-06T20:05:14.5440000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 51 group(s), 102 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[2732] _id=6ac7f8cbde269131f9c746fb ts=2026-10-08T20:10:50.7710000Z == 6ab9a9439a8420a1e6b56ba0.jsonl[2733] _id=6ac7f8ccde269131f9c746fd ts=2026-10-08T20:10:50.7710000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[2833] _id=6ac7f8cede269131f9c7471a ts=2026-10-08T20:10:50.9870000Z == 6ab9a9439a8420a1e6b56ba0.jsonl[2735] _id=6ac7f8cede269131f9c7471c ts=2026-10-08T20:10:50.9870000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[2950] _id=6acfd8e5de269131f9d8d213 ts=2026-10-14T19:32:52.2740000Z == 6ab9a9439a8420a1e6b56ba0.jsonl[2957] _id=6acfd8e5de269131f9d8d217 ts=2026-10-14T19:32:52.2740000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[2847] _id=6acfd879de269131f9d8c4b4 ts=? == 6ab9a9439a8420a1e6b56ba0.jsonl[7268] _id=6ad63d71de269131f9e987f7 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba0.jsonl[492] _id=6ac6a0b8de269131f9bf2bfd ts=2026-10-07T19:42:48.2070000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[438] _id=6ac6a0b8de269131f9bf2c02 ts=2026-10-07T19:42:48.2120000Z`; `619ms: 6ab9a9439a8420a1e6b56ba0.jsonl[871] _id=6ac6a545de269131f9bf6dc2 ts=2026-10-07T20:02:12.6250000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[875] _id=6ac6a545de269131f9bf6dcf ts=2026-10-07T20:02:13.2440000Z`; `458ms: 6ab9a9439a8420a1e6b56ba0.jsonl[875] _id=6ac6a545de269131f9bf6dcf ts=2026-10-07T20:02:13.2440000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[876] _id=6ac6a546de269131f9bf6ddf ts=2026-10-07T20:02:13.7020000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `442ms: 6ab9a9439a8420a1e6b56ba0.jsonl[3657] _id=6acfda29de269131f9d8edf2 ts=2026-10-14T19:38:17.3610000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[3659] _id=6acfda29de269131f9d8ee00 ts=2026-10-14T19:38:17.8030000Z`; `679ms: 6ab9a9439a8420a1e6b56ba0.jsonl[3679] _id=6acfda72de269131f9d8f614 ts=2026-10-14T19:39:30.3150000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[3680] _id=6acfda73de269131f9d8f624 ts=2026-10-14T19:39:30.9940000Z`; `591ms: 6ab9a9439a8420a1e6b56ba0.jsonl[3673] _id=6acfda72de269131f9d8f61e ts=2026-10-14T19:39:30.6380000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[3674] _id=6acfda73de269131f9d8f628 ts=2026-10-14T19:39:31.2290000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `818ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1040] _id=6ac6a6bade269131f9bf88a8 ts=2026-10-07T20:08:26.2790000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[1041] _id=6ac6a6bbde269131f9bf88ae ts=2026-10-07T20:08:27.0970000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `974ms: 6ab9a9439a8420a1e6b56ba0.jsonl[977] _id=6ac6a5f7de269131f9bf7777 ts=2026-10-07T20:05:10.5290000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[980] _id=6ac6a5f8de269131f9bf7785 ts=2026-10-07T20:05:11.5030000Z`; `425ms: 6ab9a9439a8420a1e6b56ba0.jsonl[987] _id=6ac6a5fdde269131f9bf77d6 ts=2026-10-07T20:05:16.5380000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[990] _id=6ac6a5fdde269131f9bf77db ts=2026-10-07T20:05:16.9630000Z`; `442ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1183] _id=6ac7f241de269131f9c6c137 ts=2026-10-08T19:42:56.6690000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[1188] _id=6ac7f241de269131f9c6c146 ts=2026-10-08T19:42:57.1110000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `853ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1241] _id=6ac7f2d8de269131f9c6ca4f ts=2026-10-08T19:45:27.9520000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[1246] _id=6ac7f2d9de269131f9c6ca5b ts=2026-10-08T19:45:28.8050000Z`; `592ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1349] _id=6ac7f3ffde269131f9c6e1fe ts=2026-10-08T19:50:22.6710000Z ~ 6ab9a9439a8420a1e6b56ba0.jsonl[1350] _id=6ac7f3ffde269131f9c6e208 ts=2026-10-08T19:50:23.2630000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 33m 
  - Evidence: 143h 33m: 6ab9a9439a8420a1e6b56ba0.jsonl[1571] _id=6ac7f5a2de269131f9c6fcb7 ts=2026-10-08T19:57:21.6220000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2842] _id=6acfd867de269131f9d8c239 ts=2026-10-14T19:30:47.4410000Z; 66h 1m: 6ab9a9439a8420a1e6b56ba0.jsonl[6617] _id=6ad2841ade269131f9e7fcfe ts=2026-10-16T20:07:53.9330000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6684] _id=6ad6247ede269131f9e972e0 ts=2026-10-19T14:09:01.6740000Z; 23h 59m: 6ab9a9439a8420a1e6b56ba0.jsonl[445] _id=6ac6a076de269131f9bf281a ts=2026-10-07T19:41:41.5270000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1047] _id=6ac7f1dade269131f9c6b776 ts=2026-10-08T19:41:13.6730000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 6ab9a9439a8420a1e6b56ba0.jsonl[2682] _id=6ac7f864de269131f9c74148 ts=2026-10-08T20:09:08.0060000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2886] _id=6acfd894de269131f9d8c8c9 ts=2026-10-14T19:31:32.4150000Z; 65h 57m: 6ab9a9439a8420a1e6b56ba0.jsonl[6676] _id=6ad2850bde269131f9e80453 ts=2026-10-16T20:11:54.9470000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6706] _id=6ad624acde269131f9e97370 ts=2026-10-19T14:09:47.3900000Z; 23h 35m: 6ab9a9439a8420a1e6b56ba0.jsonl[1012] _id=6ac6a662de269131f9bf8102 ts=2026-10-07T20:06:57.8270000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1162] _id=6ac7f222de269131f9c6bf86 ts=2026-10-08T19:42:25.7860000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 271 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1311] _id=6ac7f3cade269131f9c6de6f ts=2026-10-08T19:49:30.0060000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1312] _id=6ac7f3cade269131f9c6de70 ts=2026-10-08T19:49:30.0060000Z; 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1359] _id=6ac7f416de269131f9c6e362 ts=2026-10-08T19:50:45.6510000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1360] _id=6ac7f416de269131f9c6e363 ts=2026-10-08T19:50:45.6510000Z; 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[7665] _id=6ad6410ade269131f9e9a633 ts=2026-10-19T16:10:49.0530000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[7666] _id=6ad6410ade269131f9e9a634 ts=2026-10-19T16:10:49.0530000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 143h 20m 
  - Evidence: 143h 20m: 6ab9a9439a8420a1e6b56ba0.jsonl[2825] _id=6ac7f8c9de269131f9c746df ts=2026-10-08T20:10:48.7290000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2849] _id=6acfd879de269131f9d8c4b9 ts=2026-10-14T19:31:04.9100000Z; 65h 58m: 6ab9a9439a8420a1e6b56ba0.jsonl[6650] _id=6ad284bcde269131f9e801e7 ts=2026-10-16T20:10:35.3610000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6694] _id=6ad62499de269131f9e97329 ts=2026-10-19T14:09:28.0090000Z; 23h 38m: 6ab9a9439a8420a1e6b56ba0.jsonl[942] _id=6ac6a562de269131f9bf6fd8 ts=2026-10-07T20:02:41.9170000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1053] _id=6ac7f1e5de269131f9c6b8ce ts=2026-10-08T19:41:24.3990000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 178 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1054] _id=6ac7f1e5de269131f9c6b8cf ts=2026-10-08T19:41:24.4000000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1055] _id=6ac7f1e5de269131f9c6b8d0 ts=2026-10-08T19:41:24.4000000Z; 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1056] _id=6ac7f1e5de269131f9c6b8d1 ts=2026-10-08T19:41:24.4010000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1057] _id=6ac7f1e5de269131f9c6b8d2 ts=2026-10-08T19:41:24.4010000Z; 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1421] _id=6ac7f481de269131f9c6eab4 ts=2026-10-08T19:52:32.7580000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1422] _id=6ac7f481de269131f9c6eab5 ts=2026-10-08T19:52:32.7580000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 6ab9a9439a8420a1e6b56ba0.jsonl[2716] _id=6ac7f88fde269131f9c743e0 ts=2026-10-08T20:09:51.2140000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2913] _id=6acfd8c1de269131f9d8ce61 ts=2026-10-14T19:32:17.7970000Z; 70h 6m: 6ab9a9439a8420a1e6b56ba0.jsonl[6600] _id=6ad24c7ede269131f9e5a5be ts=2026-10-16T16:10:38.4430000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6807] _id=6ad62673de269131f9e97594 ts=2026-10-19T14:17:22.3800000Z; 23h 39m: 6ab9a9439a8420a1e6b56ba0.jsonl[939] _id=6ac6a562de269131f9bf6fda ts=2026-10-07T20:02:42.0440000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1078] _id=6ac7f1fede269131f9c6bb26 ts=2026-10-08T19:41:50.0320000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56ba0.jsonl[492] _id=6ac6a0b8de269131f9bf2bfd ts=2026-10-07T19:42:48.2070000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[438] _id=6ac6a0b8de269131f9bf2c02 ts=2026-10-07T19:42:48.2120000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 19m 
  - Evidence: 143h 19m: 6ab9a9439a8420a1e6b56ba0.jsonl[2810] _id=6ac7f8d9de269131f9c7475e ts=2026-10-08T20:11:04.7170000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2848] _id=6acfd879de269131f9d8c4b8 ts=2026-10-14T19:31:00.0410000Z; 65h 57m: 6ab9a9439a8420a1e6b56ba0.jsonl[6675] _id=6ad2850ede269131f9e80457 ts=2026-10-16T20:11:56.9430000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6693] _id=6ad62499de269131f9e97328 ts=2026-10-19T14:09:25.6200000Z; 23h 32m: 6ab9a9439a8420a1e6b56ba0.jsonl[1045] _id=6ac6a6e1de269131f9bf89f5 ts=2026-10-07T20:09:05.2600000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1052] _id=6ac7f1e5de269131f9c6b8cd ts=2026-10-08T19:41:22.7870000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 6ab9a9439a8420a1e6b56ba0.jsonl[2838] _id=6ac7f8d0de269131f9c74734 ts=2026-10-08T20:10:50.9870000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[3096] _id=6acfd952de269131f9d8dbd9 ts=2026-10-14T19:32:37.0360000Z; 90h 37m: 6ab9a9439a8420a1e6b56ba0.jsonl[5734] _id=6ad12ccede269131f9e0b23a ts=2026-10-15T19:43:08.0920000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6964] _id=6ad62737de269131f9e97765 ts=2026-10-19T14:20:37.5220000Z; 19h 55m: 6ab9a9439a8420a1e6b56ba0.jsonl[4759] _id=6acfe213de269131f9d967bb ts=2026-10-14T20:12:01.3700000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[4785] _id=6ad0fa40de269131f9dd3bb7 ts=2026-10-15T16:07:26.6770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 812 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1734] _id=6ac7f69cde269131f9c719c5 ts=2026-10-08T20:01:31.1220000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1741] _id=6ac7f69dde269131f9c719d4 ts=2026-10-08T20:01:31.1220000Z; 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1770] _id=6ac7f7c3de269131f9c734a3 ts=2026-10-08T20:06:25.8890000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1771] _id=6ac7f7c3de269131f9c734a4 ts=2026-10-08T20:06:25.8890000Z; 0ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1832] _id=6ac7f77ede269131f9c72e41 ts=2026-10-08T20:01:32.4840000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1835] _id=6ac7f77ede269131f9c72e45 ts=2026-10-08T20:01:32.4840000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 22m 
  - Evidence: 143h 22m: 6ab9a9439a8420a1e6b56ba0.jsonl[2717] _id=6ac7f892de269131f9c743fe ts=2026-10-08T20:09:54.1560000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2901] _id=6acfd8b2de269131f9d8cc7a ts=2026-10-14T19:32:02.2780000Z; 92h 15m: 6ab9a9439a8420a1e6b56ba0.jsonl[5857] _id=6ad12dd3de269131f9e0c014 ts=2026-10-15T19:47:30.5600000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[7401] _id=6ad63f4fde269131f9e996c9 ts=2026-10-19T16:03:27.4990000Z; 23h 38m: 6ab9a9439a8420a1e6b56ba0.jsonl[4502] _id=6acfe145de269131f9d95d3a ts=2026-10-14T20:08:36.7970000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[5855] _id=6ad12dd1de269131f9e0c008 ts=2026-10-15T19:47:29.0190000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 30m 
  - Evidence: 143h 30m: 6ab9a9439a8420a1e6b56ba0.jsonl[1760] _id=6ac7f716de269131f9c72684 ts=2026-10-08T20:03:33.6980000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[3010] _id=6acfd915de269131f9d8d691 ts=2026-10-14T19:33:41.7730000Z; 23h 52m: 6ab9a9439a8420a1e6b56ba0.jsonl[4327] _id=6acfe060de269131f9d9526d ts=2026-10-14T20:04:47.9830000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6009] _id=6ad13004de269131f9e0ea3a ts=2026-10-15T19:56:52.0110000Z; 10m 17s: 6ab9a9439a8420a1e6b56ba0.jsonl[3016] _id=6acfd927de269131f9d8d806 ts=2026-10-14T19:33:59.2540000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[3779] _id=6acfdb91de269131f9d90a10 ts=2026-10-14T19:44:17.0380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.023s shown 
  - Evidence: 20ms: 6ab9a9439a8420a1e6b56ba0.jsonl[3963] _id=6acfdd29de269131f9d91f1a ts=2026-10-14T19:51:05.1370000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[3967] _id=6acfdd29de269131f9d91f1e ts=2026-10-14T19:51:05.1570000Z; 23ms: 6ab9a9439a8420a1e6b56ba0.jsonl[3962] _id=6acfdd29de269131f9d91f12 ts=2026-10-14T19:51:05.1140000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[3963] _id=6acfdd29de269131f9d91f1a ts=2026-10-14T19:51:05.1370000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 260h 19m 
  - Evidence: 260h 19m: 6ab9a9439a8420a1e6b56ba0.jsonl[1381] _id=6ac7f43fde269131f9c6e5ec ts=2026-10-08T19:51:26.6240000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[7677] _id=6ad640f8de269131f9e9a560 ts=2026-10-19T16:10:31.9150000Z; 23h 35m: 6ab9a9439a8420a1e6b56ba0.jsonl[1039] _id=6ac6a6bcde269131f9bf88b4 ts=2026-10-07T20:08:28.1560000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1227] _id=6ac7f286de269131f9c6c531 ts=2026-10-08T19:44:05.8500000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 260h 16m 
  - Evidence: 260h 16m: 6ab9a9439a8420a1e6b56ba0.jsonl[1385] _id=6ac7f43fde269131f9c6e5f0 ts=2026-10-08T19:51:26.6470000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[7613] _id=6ad64074de269131f9e9a0a4 ts=2026-10-19T16:08:20.5020000Z; 23h 36m: 6ab9a9439a8420a1e6b56ba0.jsonl[1005] _id=6ac6a65ede269131f9bf808e ts=2026-10-07T20:06:53.6140000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1220] _id=6ac7f276de269131f9c6c467 ts=2026-10-08T19:43:50.2490000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 260h 17m 
  - Evidence: 260h 17m: 6ab9a9439a8420a1e6b56ba0.jsonl[1378] _id=6ac7f437de269131f9c6e569 ts=2026-10-08T19:51:18.4610000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[7624] _id=6ad64099de269131f9e9a16a ts=2026-10-19T16:08:57.2160000Z; 23h 35m: 6ab9a9439a8420a1e6b56ba0.jsonl[1026] _id=6ac6a679de269131f9bf8341 ts=2026-10-07T20:07:20.7330000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1183] _id=6ac7f241de269131f9c6c137 ts=2026-10-08T19:42:56.6690000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.005s..0.020s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1275] _id=6ac7f389de269131f9c6d960 ts=2026-10-08T19:48:25.3100000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1272] _id=6ac7f389de269131f9c6d962 ts=2026-10-08T19:48:25.3150000Z; 17ms: 6ab9a9439a8420a1e6b56ba0.jsonl[974] _id=6ac6a5f8de269131f9bf7794 ts=2026-10-07T20:05:12.0030000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[975] _id=6ac6a5f8de269131f9bf7795 ts=2026-10-07T20:05:12.0200000Z; 20ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1212] _id=6ac7f27bde269131f9c6c4aa ts=2026-10-08T19:43:55.2720000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1213] _id=6ac7f27bde269131f9c6c4ab ts=2026-10-08T19:43:55.2920000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 260h 18m 
  - Evidence: 260h 18m: 6ab9a9439a8420a1e6b56ba0.jsonl[1351] _id=6ac7f401de269131f9c6e22e ts=2026-10-08T19:50:24.9530000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[7618] _id=6ad64086de269131f9e9a103 ts=2026-10-19T16:08:38.6200000Z; 23h 35m: 6ab9a9439a8420a1e6b56ba0.jsonl[1037] _id=6ac6a6b5de269131f9bf8896 ts=2026-10-07T20:08:20.4290000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1207] _id=6ac7f274de269131f9c6c43c ts=2026-10-08T19:43:48.3010000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1352] _id=6ac7f3ffde269131f9c6e202 ts=2026-10-08T19:50:23.2560000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1350] _id=6ac7f3ffde269131f9c6e208 ts=2026-10-08T19:50:23.2630000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 34m 
  - Evidence: 143h 34m: 6ab9a9439a8420a1e6b56ba0.jsonl[1570] _id=6ac7f57dde269131f9c6fa93 ts=2026-10-08T19:56:45.4100000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2844] _id=6acfd867de269131f9d8c23b ts=2026-10-14T19:30:47.7660000Z; 66h 1m: 6ab9a9439a8420a1e6b56ba0.jsonl[6614] _id=6ad28407de269131f9e7fc8b ts=2026-10-16T20:07:34.6490000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6678] _id=6ad6247ede269131f9e972e3 ts=2026-10-19T14:09:01.8380000Z; 23h 59m: 6ab9a9439a8420a1e6b56ba0.jsonl[443] _id=6ac6a069de269131f9bf27da ts=2026-10-07T19:41:28.7310000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1049] _id=6ac7f1dade269131f9c6b778 ts=2026-10-08T19:41:13.8090000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 143h 34m 
  - Evidence: 143h 34m: 6ab9a9439a8420a1e6b56ba0.jsonl[1569] _id=6ac7f57dde269131f9c6fa92 ts=2026-10-08T19:56:45.4100000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2843] _id=6acfd867de269131f9d8c23a ts=2026-10-14T19:30:47.7660000Z; 66h 1m: 6ab9a9439a8420a1e6b56ba0.jsonl[6613] _id=6ad28407de269131f9e7fc8a ts=2026-10-16T20:07:34.6480000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6677] _id=6ad6247ede269131f9e972e2 ts=2026-10-19T14:09:01.8380000Z; 23h 59m: 6ab9a9439a8420a1e6b56ba0.jsonl[442] _id=6ac6a069de269131f9bf27d9 ts=2026-10-07T19:41:28.7310000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1048] _id=6ac7f1dade269131f9c6b777 ts=2026-10-08T19:41:13.8090000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 46m 
  - Evidence: 143h 46m: 6ab9a9439a8420a1e6b56ba0.jsonl[2841] _id=6acfd867de269131f9d8c22b ts=2026-10-08T20:11:12.121Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[4134] _id=6acfdeb6de269131f9d93af3 ts=2026-10-14T19:57:42.4250000Z; 70h 7m: 6ab9a9439a8420a1e6b56ba0.jsonl[6611] _id=6ad28407de269131f9e7fc87 ts=2026-10-16T16:11:10.668Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6854] _id=6ad626cbde269131f9e97637 ts=2026-10-19T14:18:50.2420000Z; 24h 1m: 6ab9a9439a8420a1e6b56ba0.jsonl[1046] _id=6ac7f1dade269131f9c6b774 ts=2026-10-07T20:09:13.89Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2841] _id=6acfd867de269131f9d8c22b ts=2026-10-08T20:11:12.121Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 143h 32m 
  - Evidence: 143h 32m: 6ab9a9439a8420a1e6b56ba0.jsonl[1604] _id=6ac7f5f8de269131f9c70327 ts=2026-10-08T19:58:47.5460000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[2855] _id=6acfd879de269131f9d8c4bf ts=2026-10-14T19:31:04.9530000Z; 66h 1m: 6ab9a9439a8420a1e6b56ba0.jsonl[6616] _id=6ad2841ede269131f9e7fd0c ts=2026-10-16T20:07:56.7310000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[6695] _id=6ad62499de269131f9e9732a ts=2026-10-19T14:09:28.0540000Z; 23h 41m: 6ab9a9439a8420a1e6b56ba0.jsonl[125] _id=6ac55359de269131f9b8001d ts=2026-10-06T20:00:24.4780000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[447] _id=6ac6a078de269131f9bf282f ts=2026-10-07T19:41:43.5890000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56ba0.jsonl[944] _id=6ac6a562de269131f9bf6fdd ts=2026-10-07T20:02:42.0600000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[945] _id=6ac6a562de269131f9bf6fde ts=2026-10-07T20:02:42.0610000Z; 2ms: 6ab9a9439a8420a1e6b56ba0.jsonl[1164] _id=6ac7f222de269131f9c6bf88 ts=2026-10-08T19:42:25.8040000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[1176] _id=6ac7f222de269131f9c6bf89 ts=2026-10-08T19:42:25.8060000Z; 2ms: 6ab9a9439a8420a1e6b56ba0.jsonl[4783] _id=6ad0fa3fde269131f9dd3baa ts=2026-10-15T16:07:25.5500000Z -> 6ab9a9439a8420a1e6b56ba0.jsonl[4784] _id=6ad0fa3fde269131f9dd3bab ts=2026-10-15T16:07:25.5520000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1394] _id=6ac7f465de269131f9c6e8a4 ts=2026-10-08T19:52:04.3220000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[4146] _id=6acfdf1ade269131f9d93ffa ts=2026-10-14T19:59:22.3960000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[5674] _id=6ad12cb8de269131f9e0b0bf ts=2026-10-15T19:42:48.2670000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[2847] _id=6acfd879de269131f9d8c4b4 ts=?`; `6ab9a9439a8420a1e6b56ba0.jsonl[7268] _id=6ad63d71de269131f9e987f7 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 88 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[4706] _id=6acfe208de269131f9d96718 ts=2026-10-14T20:11:49.4760000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[4715] _id=6acfe208de269131f9d9671c ts=2026-10-14T20:11:49.4950000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[4720] _id=6acfe208de269131f9d96721 ts=2026-10-14T20:11:49.5840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 311 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1740] _id=6ac7f69bde269131f9c71990 ts=2026-10-08T20:01:30.3610000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[2733] _id=6ac7f8ccde269131f9c746fd ts=2026-10-08T20:10:50.7710000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[2828] _id=6ac7f8ccde269131f9c74706 ts=2026-10-08T20:10:50.7710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1242] _id=6ac7f2d5de269131f9c6ca26 ts=2026-10-08T19:45:25.2500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 10 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1018] _id=6ac6a66bde269131f9bf81b4 ts=2026-10-07T20:07:06.5580000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1029] _id=6ac6a680de269131f9bf844a ts=2026-10-07T20:07:27.4610000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1036] _id=6ac6a6b3de269131f9bf8890 ts=2026-10-07T20:08:18.9600000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'DialogueStartEvent' (totals: 162 start, 157 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'BecameCameraCentered' (totals: 313 open, 311 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 35 unmatched 'BecameVisible' (totals: 608 open, 573 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 15 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 24 start, 12 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 348 of 7773 adjacent _id pairs reverse in client time; worst 224.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba0.jsonl[1830] _id=6ac7f77dde269131f9c72e21 ts=2026-10-08T20:05:16.9900000Z`; `6ab9a9439a8420a1e6b56ba0.jsonl[1832] _id=6ac7f77ede269131f9c72e41 ts=2026-10-08T20:01:32.4840000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.58s, min -515975.51s, max -0.15s over 7774 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba0\coverage.yaml

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
  - Observed: 2 records 
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

### `InputEvent` — 3018 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2277); Unit 1 Dev (741)
- **Intervals:** median 0.49s (p5 0.04s / p95 7.28s, n=3017)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3018/3018 records)
    "pressed"  x3018
data.actionType  (string, 3018/3018 records)
    "Move"  x2538
    "Interact"  x170
    "Sprint"  x119
    "Jump"  x72
    "Ascend"  x68
    "Descend"  x47
    "Map"  x4
data.key  (string, 3018/3018 records)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3018/3018 records)
    "Player"  x2352
    "Drone"  x666
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 1805 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1805)
- **Intervals:** median 0.07s (p5 0.00s / p95 1.51s, n=1804)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1805/1805 records)
    "BecameVisible"  x608
    "BecameInvisible"  x573
    "BecameCameraCentered"  x313
    "BecameCameraUncentered"  x311
data.pieceId  (string, 1805/1805 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1805/1805 records)
    1284 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1334 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (956); Unit 1 Dev (378)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.10s, n=1332)
- **Fields under `data`:**

```text
data.position  (object, 1334/1334 records)
data.position.x  (number, 1334/1334 records)
    numeric range -24.0473 .. 1426.97 (264 unique)
data.position.y  (number, 1334/1334 records)
    numeric range -5.58009 .. 155.92 (164 unique)
data.position.z  (number, 1334/1334 records)
    numeric range -130.016 .. 1810.7 (264 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1066 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (808); Unit 1 Dev (258)
- **eventKey:** present on 747 of 1066 records
- **Intervals:** median 5.07s (p5 0.01s / p95 46.14s, n=1065)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x747; [conversationId, dialogueEventType] x319
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1066/1066 records)
    numeric range 8 .. 103 (24 unique)
data.dialogueEventType  (string, 1066/1066 records)
    "DialogueNodeEvent"  x747
    "DialogueStartEvent"  x162
    "DialogueFinishEvent"  x157
data.nodeId  (number, 747/1066 records)
    numeric range 0 .. 290 (186 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 161 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (100); Unit 2 Prod (Refactor) (61)
- **Intervals:** median 0.72s (p5 0.05s / p95 24.03s, n=160)
- **Fields under `data`:**

```text
data.actionType  (string, 161/161 records)
    "argumentationNodeHoverEnd"  x69
    "argumentationNodeHoverStart"  x69
    "argumentationNodeAdd"  x18
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 161/161 records)
    "Unit 1 - Freshwater"  x63
    "Unit 2 – Watershed"  x61
    "Unit 1 - Argumentation Tutorial"  x37
data.nodeName  (string, 161/161 records)
    "A"  x40
    "I"  x39
    "1"  x37
    "II"  x19
    "C"  x16
    "D"  x8
    "B"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 103 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (82); Unit 1 Dev (21)
- **Intervals:** median 11.93s (p5 0.38s / p95 12227.83s, n=102)
- **Fields under `data`:**

```text
data.actionType  (string, 103/103 records)
    "Press E to Place"  x21
    "Press E to Scan"  x19
    "Press E to Pick up"  x16
    "E to Talk"  x12
    "Press E to Install"  x12
    "Press E to Insert"  x9
    "TalkTo"  x5
    "Press E to Operate"  x3
    "Press E to Collect"  x2
    "Press E to Open Locker"  x2
    "Inspect Alien Glyph"  x1
    "Press [E/Action button] to enter escape pod "  x1
data.objectName  (string, 103/103 records)
    39 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 85 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (85)
- **Intervals:** median 0.87s (p5 0.13s / p95 284.71s, n=84)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x79; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/85 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/85 records)
    "Unit 2 Prod (Refactor)"  x6
data.actionType  (string, 79/85 records)
    "LeftDrag"  x43
    "RightDrag"  x36
data.currentSoilType  (string, 79/85 records)
    "CLAY"  x16
    "CLAYSAND"  x14
    "SAND"  x14
    "SANDGRAVEL"  x13
    "CLAYROCK"  x11
    "GRAVEL"  x6
    "BEDROCK"  x5
data.isCorrectSelection  (string, 79/85 records)
    "false"  x65
    "true"  x14
data.waterLevelStatus  (string, 79/85 records)
    "TooHigh"  x34
    "TooLow"  x23
    "Proper"  x22
data.waterRetentionChange  (string, 79/85 records)
    "Increase"  x35
    "Decrease"  x30
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 54 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (54)
- **Intervals:** median 3.85s (p5 0.75s / p95 476.72s, n=53)
- **`data` key-set variants:** [actionType, featureUsed, location] x27; [actionType, featureUsed] x20; [actionType, featureUsed, legendName] x7
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "WaypointMoveEvent"  x25
    "MapCloseEvent"  x10
    "MapOpenEvent"  x10
    "Selected"  x5
    "Unselected"  x2
    "WaypointSetEvent"  x2
data.featureUsed  (string, 54/54 records)
    "Waypoint"  x27
    "Map"  x20
    "Legend"  x7
data.legendName  (string, 7/54 records)
    "360 ft"  x4
    "Water"  x3
data.location  (object, 27/54 records)
data.location.x  (number, 27/54 records)
    numeric range -310.994 .. 106.578 (23 unique)
data.location.y  (number, 27/54 records)
    numeric range -146.327 .. 127.508 (24 unique)
data.location.z  (number, 27/54 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 36 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (16)
- **eventKey:** present on 36 of 36 records
- **Intervals:** median 256.06s (p5 0.00s / p95 131002.77s, n=35)
- **`data` key-set variants:** [questEventType, questID, questName] x24; [questEventType, questID, questName, questSuccessOrFailure] x12
- **Fields under `data`:**

```text
data.questEventType  (string, 36/36 records)
    "questActiveEvent"  x24
    "questFinishEvent"  x12
data.questID  (string, 36/36 records)
    "25"  x6
    "22"  x4
    "24"  x4
    "32"  x4
    "21"  x3
    "29"  x3
    "33"  x3
    "23"  x2
    "28"  x2
    "31"  x2
    "34"  x2
    "54"  x1
data.questName  (string, 36/36 records)
    "Which Watershed?"  x6
    "Getting the Band Back Together"  x4
    "Info and Intros"  x4
    "Investigate the Temple"  x4
    "Defend the Expedition"  x3
    "Escape the Ruin"  x3
    "Gear Up"  x3
    "Foraged Forging"  x2
    "Getting Your Space Legs"  x2
    "TK, Reporting In!"  x2
    "What Was That?"  x2
    "Claim of Command"  x1
data.questSuccessOrFailure  (string, 12/36 records)
    "Succeeded"  x12
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 23 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (18); Unit 2 Prod (Refactor) (5)
- **Intervals:** median 1.78s (p5 0.54s / p95 80696.10s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "argumentationToolOpen"  x15
    "argumentationToolClose"  x8
data.argumentationTitle  (string, 23/23 records)
    "Unit 1 - Freshwater"  x14
    "Unit 2 – Watershed"  x5
    "Unit 1 - Argumentation Tutorial"  x4
data.toolName  (string, 23/23 records)
    "BackingInfoPanel - "  x14
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Watershed Graph"  x3
    "BackingInfoPanel - Waterfall Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DEBUGMenu` — 22 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (8); Unit 1 Dev (3)
- **Intervals:** median 99.94s (p5 12.09s / p95 237667.74s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "DebugMenuStateChanged"  x22
data.isOpened  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (13); Unit 2 Prod (Refactor) (5)
- **Intervals:** median 24.29s (p5 1.01s / p95 255379.21s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    "A,1,II"  x7
    "1,I"  x4
    "A,1,I"  x2
    "A,D,1,II"  x2
    "A,1,"  x1
    "D,1,II"  x1
    "D,A,1,II"  x1
data.argumentationTitle  (string, 18/18 records)
    "Unit 1 - Freshwater"  x11
    "Unit 2 – Watershed"  x5
    "Unit 1 - Argumentation Tutorial"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 15 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 13586.12s (p5 562.45s / p95 335391.50s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 11 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (11)
- **Intervals:** median 73662.07s (p5 3368.75s / p95 391222.53s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    true  x11
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 1 Dev (2)
- **Intervals:** median 71754.69s (p5 611.14s / p95 398281.48s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 138.06s (p5 33.61s / p95 638814.83s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionOpen"  x5
    "argumentationSessionClose"  x4
data.argumentationDescription  (string, 9/9 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.27s (p5 2.27s / p95 2.27s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x2
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

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
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (85 records)
- `TopographicMapEvent` data.actionType: "Selected" (5x); "Unselected" (2x); "WaypointMoveEvent" (25x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (7x); "Waypoint" (27x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 3 Dev' has no records of this event
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*