# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b6f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b6f
- **Game version string(s) in log:** 2.9.6, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b6f.jsonl
- **Records:** 5880 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b6f
- **Time span:** 2026-10-05T18:51:59.288000+00:00 .. 2026-10-16T18:59:06.817000+00:00 (264h 7m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b6f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 5880 records, 3 scenes.
- Findings: **0 FAIL**, **27 WARNING**, 82 INFO, 6 NOT_TESTED, 73 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 1874 | 31.87 | 1 | 1 | 0 | 2026-10-13T18:44:04.574000+00:00 | 2026-10-15T18:59:11.057000+00:00 | 48h 15m |
| InputEvent | 1707 | 29.03 | 1 | 2 | 0 | 2026-10-06T18:54:07.082000+00:00 | 2026-10-16T18:58:56.386000+00:00 | 240h 4m |
| PlayerPositionEvent | 963 | 16.38 | 1 | 2 | 0 | 2026-10-06T18:54:03.685000+00:00 | 2026-10-16T18:59:06.817000+00:00 | 240h 5m |
| DialogueEvent | 913 | 15.53 | 1 | 2 | 634 | 2026-10-06T18:54:23.718000+00:00 | 2026-10-16T18:52:51.926000+00:00 | 239h 58m |
| ObjectInterEvent | 123 | 2.09 | 1 | 2 | 0 | 2026-10-06T19:01:36.110000+00:00 | 2026-10-16T18:45:09.285000+00:00 | 239h 43m |
| Soil Key Puzzle | 80 | 1.36 | 1 | 1 | 0 | 2026-10-14T18:48:35.539000+00:00 | 2026-10-15T18:50:10.704000+00:00 | 24h 1m |
| argumentationNodeEvent | 53 | 0.9 | 1 | 2 | 0 | 2026-10-07T19:01:34.978000+00:00 | 2026-10-16T18:49:01.250000+00:00 | 215h 47m |
| TopographicMapEvent | 44 | 0.75 | 1 | 1 | 0 | 2026-10-13T18:44:45.657000+00:00 | 2026-10-15T19:09:31.336000+00:00 | 48h 24m |
| questEvent | 33 | 0.56 | 1 | 2 | 33 | 2026-10-06T18:54:23.692000+00:00 | 2026-10-16T18:50:40.675000+00:00 | 239h 56m |
| argumentationToolEvent | 28 | 0.48 | 1 | 2 | 0 | 2026-10-07T19:01:27.932000+00:00 | 2026-10-16T18:48:01.299000+00:00 | 215h 46m |
| DEBUGMenu | 16 | 0.27 | 1 | 3 | 0 | 2026-10-06T18:54:03.666000+00:00 | 2026-10-16T18:58:53.955000+00:00 | 240h 4m |
| gameWindowFocusEvent | 13 | 0.22 | 1 | 2 | 0 | 2026-10-05T18:51:59.288000+00:00 | 2026-10-16T18:58:41.552000+00:00 | 264h 6m |
| gameStartEvent | 10 | 0.17 | 1 | 1 | 0 | 2026-10-05T18:51:59.289000+00:00 | 2026-10-16T18:58:41.552000+00:00 | 264h 6m |
| DaniEvent | 6 | 0.1 | 1 | 1 | 0 | 2026-10-15T18:43:51.135000+00:00 | 2026-10-15T18:46:35.876000+00:00 | 2m 44s |
| argumentationEvent | 6 | 0.1 | 1 | 2 | 0 | 2026-10-07T19:01:31.552000+00:00 | 2026-10-16T18:49:05.084000+00:00 | 215h 47m |
| gameWindowUnfocusEvent | 6 | 0.1 | 1 | 3 | 0 | 2026-10-05T18:52:09.344000+00:00 | 2026-10-16T18:42:24.063000+00:00 | 263h 50m |
| argumentationAnswerEvent | 3 | 0.05 | 1 | 2 | 0 | 2026-10-07T19:01:46.427000+00:00 | 2026-10-16T18:49:05.062000+00:00 | 215h 47m |
| EndOfUnit | 1 | 0.02 | 1 | 1 | 0 | 2026-10-07T19:07:09.268000+00:00 | 2026-10-07T19:07:09.268000+00:00 | 0.0s |
| crash | 1 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 197.813s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.08s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.626s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.676s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 388419.318s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 1.228s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.816s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 86004.964s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 43502.542s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 87930.965s median 
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
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; rightShift; upArrow 
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
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 28 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
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

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[343] _id=6ac546a0de269131f9b74c24 ts=2026-10-06T19:06:08.1290000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[406] _id=6ac54792de269131f9b7686d ts=2026-10-06T19:10:09.9940000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[423] _id=6ac5482bde269131f9b77379 ts=2026-10-06T19:12:42.4460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 10 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 10} 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[2] _id=6ac3f1d0de269131f9af67db ts=2026-10-05T18:51:59.2890000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[12] _id=6ac543bcde269131f9b70a79 ts=2026-10-06T18:53:47.7960000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[559] _id=6ac6932ede269131f9bdfbd1 ts=2026-10-07T18:45:01.5280000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[1] _id=6ac3f1d0de269131f9af67d9 ts=2026-10-05T18:51:59.2880000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[11] _id=6ac543bcde269131f9b70a75 ts=2026-10-06T18:53:47.7950000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[558] _id=6ac6932ede269131f9bdfbd0 ts=2026-10-07T18:45:01.5280000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 6 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 6} 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[3] _id=6ac3f1d9de269131f9af67e5 ts=2026-10-05T18:52:09.3440000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[555] _id=6ac6932ede269131f9bdfbbd ts=2026-10-06T19:17:40.309Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1448] _id=6ace7a9dde269131f9d101e2 ts=2026-10-07T19:17:16.785Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 20 of 44 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[1611] _id=6ace7c1ede269131f9d11a10 ts=2026-10-13T18:44:45.6570000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1619] _id=6ace7c36de269131f9d11b09 ts=2026-10-13T18:45:10.4510000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1918] _id=6acfcc0ede269131f9d73946 ts=2026-10-14T18:38:06.1090000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 1873 | 0.0 | 0.08 | 92.742 | 1.797 | 86369.756 | 0.65 | 763 | 2 |
| InputEvent | 1706 | 0.0 | 0.95 | 506.617 | 14.162 | 516204.101 | 0.12 | 33 | 6 |
| PlayerPositionEvent | 961 | 0.0 | 10.003 | 899.273 | 10.116 | 516080.394 | 0.07 | 2 | 5 |
| DialogueEvent | 912 | 0.001 | 4.878 | 947.268 | 35.192 | 516205.484 | 0.06 | 222 | 5 |
| ObjectInterEvent | 122 | 0.004 | 8.734 | 7073.878 | 1173.371 | 516403.204 | 0.01 | 2 | 7 |
| Soil Key Puzzle | 79 | 0.161 | 1.626 | 1094.876 | 12.614 | 84740.699 | 0.05 | 0 | 2 |
| argumentationNodeEvent | 52 | 0.02 | 1.228 | 14939.351 | 17.267 | 776661.538 | 0.0 | 2 | 1 |
| TopographicMapEvent | 43 | 0.016 | 7.676 | 4053.155 | 1326.061 | 85975.658 | 0.01 | 2 | 4 |
| questEvent | 32 | 0.0 | 251.596 | 26993.031 | 85506.552 | 516477.208 | 0.0 | 5 | 8 |
| argumentationToolEvent | 27 | 0.004 | 0.816 | 28770.125 | 84.857 | 776629.964 | 0.0 | 7 | 1 |
| DEBUGMenu | 15 | 9.148 | 197.813 | 57619.353 | 215532.101 | 516571.951 | 0.0 | 0 | 7 |
| gameWindowFocusEvent | 12 | 197.836 | 43502.542 | 79233.522 | 280041.578 | 516581.998 | 0.0 | 0 | 9 |
| gameStartEvent | 9 | 197.836 | 86004.964 | 105644.696 | 344560.036 | 516581.998 | 0.0 | 0 | 8 |
| DaniEvent | 5 | 1.811 | 3.176 | 32.948 | 119.148 | 145.943 | 1.82 | 0 | 0 |
| argumentationEvent | 5 | 26.738 | 58.025 | 155370.706 | 621308.45 | 776608.998 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 5 | 247.231 | 87930.965 | 189962.944 | 516979.597 | 603212.646 | 0.0 | 0 | 4 |
| argumentationAnswerEvent | 2 | 123.369 | 388419.318 | 388419.317 | 737885.671 | 776715.266 | 0.0 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[564] _id=6ac69339de269131f9bdfd99 ts=2026-10-07T18:45:12.1090000Z == 6ab9a9279a8420a1e6b56b6f.jsonl[565] _id=6ac69339de269131f9bdfd9a ts=2026-10-07T18:45:12.1090000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[5466] _id=6ad26e2ade269131f9e70c2c ts=2026-10-16T18:34:16.9250000Z == 6ab9a9279a8420a1e6b56b6f.jsonl[5467] _id=6ad26e2ade269131f9e70c2d ts=2026-10-16T18:34:16.9250000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[5877] _id=6ad273f2de269131f9e785b0 ts=2026-10-16T18:58:56.3860000Z == 6ab9a9279a8420a1e6b56b6f.jsonl[5878] _id=6ad273f2de269131f9e785b1 ts=2026-10-16T18:58:56.3860000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 36 group(s), 50 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[1559] _id=6ace7bfade269131f9d11836 ts=2026-10-13T18:44:08.3050000Z == 6ab9a9279a8420a1e6b56b6f.jsonl[1560] _id=6ace7bfade269131f9d11837 ts=2026-10-13T18:44:08.3050000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1573] _id=6ace7c01de269131f9d11894 ts=2026-10-13T18:44:15.8210000Z == 6ab9a9279a8420a1e6b56b6f.jsonl[1579] _id=6ace7c02de269131f9d11898 ts=2026-10-13T18:44:15.8210000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1593] _id=6ace7c04de269131f9d118ca ts=2026-10-13T18:44:17.9440000Z == 6ab9a9279a8420a1e6b56b6f.jsonl[1567] _id=6ace7c04de269131f9d118cc ts=2026-10-13T18:44:17.9440000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 32 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `827ms: 6ab9a9279a8420a1e6b56b6f.jsonl[183] _id=6ac54590de269131f9b72c47 ts=2026-10-06T19:01:36.1100000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[184] _id=6ac54591de269131f9b72c5b ts=2026-10-06T19:01:36.9370000Z`; `942ms: 6ab9a9279a8420a1e6b56b6f.jsonl[184] _id=6ac54591de269131f9b72c5b ts=2026-10-06T19:01:36.9370000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[189] _id=6ac54592de269131f9b72c6b ts=2026-10-06T19:01:37.8790000Z`; `4ms: 6ab9a9279a8420a1e6b56b6f.jsonl[298] _id=6ac5461ede269131f9b73869 ts=2026-10-06T19:03:58.3990000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[299] _id=6ac5461fde269131f9b73875 ts=2026-10-06T19:03:58.4030000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `303ms: 6ab9a9279a8420a1e6b56b6f.jsonl[920] _id=6ac69764de269131f9bec86d ts=2026-10-07T19:03:00.0140000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[851] _id=6ac69764de269131f9bec877 ts=2026-10-07T19:03:00.3170000Z`; `605ms: 6ab9a9279a8420a1e6b56b6f.jsonl[5768] _id=6ad27169de269131f9e755bd ts=2026-10-16T18:48:09.2130000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[5769] _id=6ad2716ade269131f9e755cd ts=2026-10-16T18:48:09.8180000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `823ms: 6ab9a9279a8420a1e6b56b6f.jsonl[935] _id=6ac69780de269131f9becbf8 ts=2026-10-07T19:03:27.5930000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[937] _id=6ac69781de269131f9becc0b ts=2026-10-07T19:03:28.4160000Z`; `677ms: 6ab9a9279a8420a1e6b56b6f.jsonl[932] _id=6ac69781de269131f9becc03 ts=2026-10-07T19:03:28.4090000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[933] _id=6ac69781de269131f9becc15 ts=2026-10-07T19:03:29.0860000Z`; `680ms: 6ab9a9279a8420a1e6b56b6f.jsonl[937] _id=6ac69781de269131f9becc0b ts=2026-10-07T19:03:28.4160000Z ~ 6ab9a9279a8420a1e6b56b6f.jsonl[934] _id=6ac69781de269131f9becc19 ts=2026-10-07T19:03:29.0960000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 29m 
  - Evidence: 143h 29m: 6ab9a9279a8420a1e6b56b6f.jsonl[1091] _id=6ac698c2de269131f9bef552 ts=2026-10-07T19:08:49.4060000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1449] _id=6ace7a9ede269131f9d101f6 ts=2026-10-13T18:38:21.3570000Z; 24h 1m: 6ab9a9279a8420a1e6b56b6f.jsonl[1856] _id=6acfcb69de269131f9d7234f ts=2026-10-14T18:35:21.2480000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4111] _id=6ad11d5dde269131f9defd3d ts=2026-10-15T18:37:16.2700000Z; 23h 56m: 6ab9a9279a8420a1e6b56b6f.jsonl[1454] _id=6ace7aa9de269131f9d102ab ts=2026-10-13T18:38:32.8990000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1850] _id=6acfcb5ede269131f9d72229 ts=2026-10-14T18:35:09.1770000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 23m 
  - Evidence: 143h 23m: 6ab9a9279a8420a1e6b56b6f.jsonl[1443] _id=6ac69ab9de269131f9bf207a ts=2026-10-07T19:17:12.5330000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1472] _id=6ace7b26de269131f9d10afb ts=2026-10-13T18:40:38.0170000Z; 23h 48m: 6ab9a9279a8420a1e6b56b6f.jsonl[1814] _id=6ace7cadde269131f9d123fd ts=2026-10-13T18:47:09.4410000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1867] _id=6acfcb89de269131f9d72948 ts=2026-10-14T18:35:53.5840000Z; 23h 28m: 6ab9a9279a8420a1e6b56b6f.jsonl[544] _id=6ac54916de269131f9b79463 ts=2026-10-06T19:16:37.8600000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[567] _id=6ac69339de269131f9bdfd9c ts=2026-10-07T18:45:12.3700000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 222 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1069] _id=6ac6983cde269131f9beea87 ts=2026-10-07T19:06:35.7660000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1070] _id=6ac6983cde269131f9beea88 ts=2026-10-07T19:06:35.7670000Z; 1ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1081] _id=6ac69850de269131f9beecb9 ts=2026-10-07T19:06:56.0240000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1082] _id=6ac69850de269131f9beecba ts=2026-10-07T19:06:56.0250000Z; 1ms: 6ab9a9279a8420a1e6b56b6f.jsonl[3696] _id=6acfd04bde269131f9d7bf55 ts=2026-10-14T18:56:10.6690000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[3697] _id=6acfd04bde269131f9d7bf56 ts=2026-10-14T18:56:10.6700000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 23m 
  - Evidence: 143h 23m: 6ab9a9279a8420a1e6b56b6f.jsonl[1439] _id=6ac69aa9de269131f9bf1fa8 ts=2026-10-07T19:16:56.4640000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1465] _id=6ace7b15de269131f9d109f7 ts=2026-10-13T18:40:20.5650000Z; 23h 48m: 6ab9a9279a8420a1e6b56b6f.jsonl[1827] _id=6ace7cbede269131f9d12518 ts=2026-10-13T18:47:25.7170000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1860] _id=6acfcb7dde269131f9d727f9 ts=2026-10-14T18:35:41.1160000Z; 23h 29m: 6ab9a9279a8420a1e6b56b6f.jsonl[535] _id=6ac548f7de269131f9b79002 ts=2026-10-06T19:16:07.1530000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[562] _id=6ac69339de269131f9bdfd97 ts=2026-10-07T18:45:12.1070000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 33 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1025] _id=6ac69807de269131f9bee398 ts=2026-10-07T19:05:42.4530000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1026] _id=6ac69807de269131f9bee399 ts=2026-10-07T19:05:42.4530000Z; 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[5466] _id=6ad26e2ade269131f9e70c2c ts=2026-10-16T18:34:16.9250000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5467] _id=6ad26e2ade269131f9e70c2d ts=2026-10-16T18:34:16.9250000Z; 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[5467] _id=6ad26e2ade269131f9e70c2d ts=2026-10-16T18:34:16.9250000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5468] _id=6ad26e2ade269131f9e70c2e ts=2026-10-16T18:34:16.9250000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 26m 
  - Evidence: 143h 26m: 6ab9a9279a8420a1e6b56b6f.jsonl[1413] _id=6ac69a7fde269131f9bf1bef ts=2026-10-07T19:16:14.7820000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1511] _id=6ace7bb2de269131f9d111f7 ts=2026-10-13T18:42:57.9860000Z; 23h 50m: 6ab9a9279a8420a1e6b56b6f.jsonl[1778] _id=6ace7c97de269131f9d121e1 ts=2026-10-13T18:46:46.8880000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1886] _id=6acfcbc3de269131f9d72f28 ts=2026-10-14T18:36:50.7270000Z; 23h 35m: 6ab9a9279a8420a1e6b56b6f.jsonl[4010] _id=6acfd45dde269131f9d85279 ts=2026-10-14T19:13:33.3380000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4421] _id=6ad1201cde269131f9df5744 ts=2026-10-15T18:48:59.3270000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b6f.jsonl[298] _id=6ac5461ede269131f9b73869 ts=2026-10-06T19:03:58.3990000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[299] _id=6ac5461fde269131f9b73875 ts=2026-10-06T19:03:58.4030000Z; 7ms: 6ab9a9279a8420a1e6b56b6f.jsonl[590] _id=6ac69373de269131f9be0529 ts=2026-10-07T18:46:11.2590000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[591] _id=6ac69374de269131f9be0540 ts=2026-10-07T18:46:11.2660000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 21m 
  - Evidence: 143h 21m: 6ab9a9279a8420a1e6b56b6f.jsonl[1444] _id=6ac69ab9de269131f9bf2078 ts=2026-10-07T19:17:12.5190000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1446] _id=6ace7aaede269131f9d10326 ts=2026-10-13T18:38:32.9130000Z; 23h 46m: 6ab9a9279a8420a1e6b56b6f.jsonl[1853] _id=6acfcb5ede269131f9d72224 ts=2026-10-13T18:49:08.152Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1854] _id=6acfcb6cde269131f9d72388 ts=2026-10-14T18:35:21.2870000Z; 23h 27m: 6ab9a9279a8420a1e6b56b6f.jsonl[551] _id=6ac54953de269131f9b79c7b ts=2026-10-06T19:17:38.5990000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[561] _id=6ac69339de269131f9bdfd96 ts=2026-10-07T18:45:10.5480000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1848] _id=6ace7d24de269131f9d128ab ts=2026-10-13T18:49:08.1520000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1853] _id=6acfcb5ede269131f9d72224 ts=2026-10-13T18:49:08.152Z; 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[4108] _id=6acfd56ede269131f9d8868c ts=2026-10-14T19:18:05.8400000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4110] _id=6ad11d5dde269131f9defd32 ts=2026-10-14T19:18:05.84Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 59m 
  - Evidence: 23h 59m: 6ab9a9279a8420a1e6b56b6f.jsonl[3492] _id=6acfce3ede269131f9d78bfb ts=2026-10-14T18:47:25.3390000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4362] _id=6ad11fa0de269131f9df4828 ts=2026-10-15T18:46:55.0950000Z; 23h 48m: 6ab9a9279a8420a1e6b56b6f.jsonl[1847] _id=6ace7d1ede269131f9d12888 ts=2026-10-13T18:49:01.8520000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1949] _id=6acfcc4dde269131f9d7426f ts=2026-10-14T18:37:47.7420000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 763 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1548] _id=6ace7cbfde269131f9d12520 ts=2026-10-13T18:47:27.0840000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1829] _id=6ace7cbfde269131f9d12522 ts=2026-10-13T18:47:27.0840000Z; 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1559] _id=6ace7bfade269131f9d11836 ts=2026-10-13T18:44:08.3050000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1560] _id=6ace7bfade269131f9d11837 ts=2026-10-13T18:44:08.3050000Z; 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[1564] _id=6ace7bfade269131f9d11834 ts=2026-10-13T18:44:08.3050000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1559] _id=6ace7bfade269131f9d11836 ts=2026-10-13T18:44:08.3050000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 32m 
  - Evidence: 23h 32m: 6ab9a9279a8420a1e6b56b6f.jsonl[4072] _id=6acfd517de269131f9d87812 ts=2026-10-14T19:16:38.6240000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4405] _id=6ad1201cde269131f9df573e ts=2026-10-15T18:48:59.3230000Z; 24m 54s: 6ab9a9279a8420a1e6b56b6f.jsonl[3543] _id=6acfce87de269131f9d79298 ts=2026-10-14T18:48:38.6040000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4009] _id=6acfd45dde269131f9d85273 ts=2026-10-14T19:13:33.3340000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 23h 52m 
  - Evidence: 23h 52m: 6ab9a9279a8420a1e6b56b6f.jsonl[1619] _id=6ace7c36de269131f9d11b09 ts=2026-10-13T18:45:10.4510000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1918] _id=6acfcc0ede269131f9d73946 ts=2026-10-14T18:38:06.1090000Z; 23h 37m: 6ab9a9279a8420a1e6b56b6f.jsonl[3848] _id=6acfd2a0de269131f9d807d7 ts=2026-10-14T19:06:07.5890000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4295] _id=6ad11eebde269131f9df2dad ts=2026-10-15T18:43:54.3200000Z; 22m 23s: 6ab9a9279a8420a1e6b56b6f.jsonl[4344] _id=6ad11f91de269131f9df4654 ts=2026-10-15T18:46:40.4080000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5279] _id=6ad124d0de269131f9dfff54 ts=2026-10-15T19:09:03.8490000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.016s..0.033s shown 
  - Evidence: 16ms: 6ab9a9279a8420a1e6b56b6f.jsonl[3730] _id=6acfd0b9de269131f9d7cbf0 ts=2026-10-14T18:58:01.0660000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[3735] _id=6acfd0b9de269131f9d7cbf4 ts=2026-10-14T18:58:01.0820000Z; 33ms: 6ab9a9279a8420a1e6b56b6f.jsonl[3732] _id=6acfd0b9de269131f9d7cbea ts=2026-10-14T18:58:01.0330000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[3730] _id=6acfd0b9de269131f9d7cbf0 ts=2026-10-14T18:58:01.0660000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 45m 
  - Evidence: 215h 45m: 6ab9a9279a8420a1e6b56b6f.jsonl[955] _id=6ac69796de269131f9bece3e ts=2026-10-07T19:03:49.7960000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5792] _id=6ad271a1de269131f9e75a7d ts=2026-10-16T18:49:05.0620000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 43m 
  - Evidence: 215h 43m: 6ab9a9279a8420a1e6b56b6f.jsonl[956] _id=6ac69796de269131f9bece44 ts=2026-10-07T19:03:49.8300000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5748] _id=6ad27137de269131f9e75105 ts=2026-10-16T18:47:18.8280000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 44m 
  - Evidence: 215h 44m: 6ab9a9279a8420a1e6b56b6f.jsonl[953] _id=6ac69791de269131f9becda1 ts=2026-10-07T19:03:44.7130000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5764] _id=6ad27166de269131f9e7556b ts=2026-10-16T18:48:06.2510000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.030s shown 
  - Evidence: 20ms: 6ab9a9279a8420a1e6b56b6f.jsonl[894] _id=6ac69710de269131f9bec00d ts=2026-10-07T19:01:36.0240000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[895] _id=6ac69710de269131f9bec00e ts=2026-10-07T19:01:36.0440000Z; 30ms: 6ab9a9279a8420a1e6b56b6f.jsonl[952] _id=6ac69791de269131f9becd96 ts=2026-10-07T19:03:44.6830000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[953] _id=6ac69791de269131f9becda1 ts=2026-10-07T19:03:44.7130000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 215h 43m 
  - Evidence: 215h 43m: 6ab9a9279a8420a1e6b56b6f.jsonl[950] _id=6ac6978bde269131f9becd0b ts=2026-10-07T19:03:39.1140000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5749] _id=6ad27141de269131f9e75208 ts=2026-10-16T18:47:29.0780000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b6f.jsonl[941] _id=6ac69787de269131f9becc9a ts=2026-10-07T19:03:34.7290000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[942] _id=6ac69787de269131f9becc9d ts=2026-10-07T19:03:34.7330000Z; 5ms: 6ab9a9279a8420a1e6b56b6f.jsonl[943] _id=6ac69789de269131f9beccc9 ts=2026-10-07T19:03:36.4100000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[936] _id=6ac69789de269131f9beccd0 ts=2026-10-07T19:03:36.4150000Z; 5ms: 6ab9a9279a8420a1e6b56b6f.jsonl[947] _id=6ac69789de269131f9becce1 ts=2026-10-07T19:03:37.0850000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[948] _id=6ac69789de269131f9becce3 ts=2026-10-07T19:03:37.0900000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 29m 
  - Evidence: 143h 29m: 6ab9a9279a8420a1e6b56b6f.jsonl[1089] _id=6ac698b8de269131f9bef426 ts=2026-10-07T19:08:39.6810000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1451] _id=6ace7a9ede269131f9d101f8 ts=2026-10-13T18:38:21.6790000Z; 24h 2m: 6ab9a9279a8420a1e6b56b6f.jsonl[1852] _id=6acfcb5ede269131f9d7222b ts=2026-10-14T18:35:09.3120000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[4113] _id=6ad11d5dde269131f9defd3f ts=2026-10-15T18:37:16.4050000Z; 24h 1m: 6ab9a9279a8420a1e6b56b6f.jsonl[2] _id=6ac3f1d0de269131f9af67db ts=2026-10-05T18:51:59.2890000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[12] _id=6ac543bcde269131f9b70a79 ts=2026-10-06T18:53:47.7960000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 29m 
  - Evidence: 143h 29m: 6ab9a9279a8420a1e6b56b6f.jsonl[1088] _id=6ac698b8de269131f9bef425 ts=2026-10-07T19:08:39.6810000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1450] _id=6ace7a9ede269131f9d101f7 ts=2026-10-13T18:38:21.6790000Z; 24h 1m: 6ab9a9279a8420a1e6b56b6f.jsonl[1] _id=6ac3f1d0de269131f9af67d9 ts=2026-10-05T18:51:59.2880000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[11] _id=6ac543bcde269131f9b70a75 ts=2026-10-06T18:53:47.7950000Z; 23h 56m: 6ab9a9279a8420a1e6b56b6f.jsonl[1450] _id=6ace7a9ede269131f9d101f7 ts=2026-10-13T18:38:21.6790000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1851] _id=6acfcb5ede269131f9d7222a ts=2026-10-14T18:35:09.3120000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 33m 
  - Evidence: 167h 33m: 6ab9a9279a8420a1e6b56b6f.jsonl[1448] _id=6ace7a9dde269131f9d101e2 ts=2026-10-07T19:17:16.785Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[3587] _id=6acfcf0ade269131f9d79f84 ts=2026-10-14T18:50:49.4310000Z; 47h 47m: 6ab9a9279a8420a1e6b56b6f.jsonl[3587] _id=6acfcf0ade269131f9d79f84 ts=2026-10-14T18:50:49.4310000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[5542] _id=6ad26f19de269131f9e727f9 ts=2026-10-16T18:38:16.8320000Z; 24h 25m: 6ab9a9279a8420a1e6b56b6f.jsonl[3] _id=6ac3f1d9de269131f9af67e5 ts=2026-10-05T18:52:09.3440000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[555] _id=6ac6932ede269131f9bdfbbd ts=2026-10-06T19:17:40.309Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 143h 27m 
  - Evidence: 143h 27m: 6ab9a9279a8420a1e6b56b6f.jsonl[1101] _id=6ac69931de269131f9befed5 ts=2026-10-07T19:10:40.5480000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1447] _id=6ace7aaede269131f9d10327 ts=2026-10-13T18:38:37.7560000Z; 23h 56m: 6ab9a9279a8420a1e6b56b6f.jsonl[1447] _id=6ace7aaede269131f9d10327 ts=2026-10-13T18:38:37.7560000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[1855] _id=6acfcb6cde269131f9d72389 ts=2026-10-14T18:35:23.3130000Z; 23h 35m: 6ab9a9279a8420a1e6b56b6f.jsonl[381] _id=6ac54772de269131f9b7662b ts=2026-10-06T19:09:37.4990000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[566] _id=6ac69339de269131f9bdfd9b ts=2026-10-07T18:45:12.1380000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.008s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b6f.jsonl[867] _id=6ac696bfde269131f9beb539 ts=2026-10-07T19:00:14.9540000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[868] _id=6ac696bfde269131f9beb53a ts=2026-10-07T19:00:14.9540000Z; 7ms: 6ab9a9279a8420a1e6b56b6f.jsonl[667] _id=6ac6949bde269131f9be37b9 ts=2026-10-07T18:51:07.3410000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[668] _id=6ac6949cde269131f9be37c4 ts=2026-10-07T18:51:07.3480000Z; 8ms: 6ab9a9279a8420a1e6b56b6f.jsonl[318] _id=6ac5466ade269131f9b743ca ts=2026-10-06T19:05:14.4080000Z -> 6ab9a9279a8420a1e6b56b6f.jsonl[317] _id=6ac5466bde269131f9b743d7 ts=2026-10-06T19:05:14.4160000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[834] _id=6ac696a6de269131f9beb073 ts=2026-10-07T18:59:49.9970000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[967] _id=6ac697afde269131f9bed1f2 ts=2026-10-07T19:04:14.4470000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[3895] _id=6acfd30ede269131f9d81b30 ts=2026-10-14T19:07:58.3680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[5461] _id=6ad26e2ade269131f9e70c36 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 36 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[4662] _id=6ad12162de269131f9df7b3b ts=2026-10-15T18:54:23.6060000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[4664] _id=6ad12162de269131f9df7b51 ts=2026-10-15T18:54:23.6870000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[4665] _id=6ad12162de269131f9df7b52 ts=2026-10-15T18:54:23.8500000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 402 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[1560] _id=6ace7bfade269131f9d11837 ts=2026-10-13T18:44:08.3050000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1579] _id=6ace7c02de269131f9d11898 ts=2026-10-13T18:44:15.8210000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1574] _id=6ace7c02de269131f9d1189a ts=2026-10-13T18:44:15.8210000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 14 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[935] _id=6ac69780de269131f9becbf8 ts=2026-10-07T19:03:27.5930000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[937] _id=6ac69781de269131f9becc0b ts=2026-10-07T19:03:28.4160000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[934] _id=6ac69781de269131f9becc19 ts=2026-10-07T19:03:29.0960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'DialogueStartEvent' (totals: 141 start, 138 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 22 unmatched 'BecameVisible' (totals: 636 open, 614 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 18 open, 10 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 7 unmatched 'questActiveEvent' (totals: 20 start, 13 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 236 of 5878 adjacent _id pairs reverse in client time; worst 118.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b6f.jsonl[1641] _id=6ace7c6bde269131f9d11e4b ts=2026-10-13T18:46:02.5570000Z`; `6ab9a9279a8420a1e6b56b6f.jsonl[1656] _id=6ace7c6cde269131f9d11e55 ts=2026-10-13T18:44:04.5740000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.71s, min -516065.07s, max -0.29s over 5879 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b6f\coverage.yaml

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
  - Observed: 1 records 
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

### `PuzzlePieceVisibleEvent` — 1874 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1874)
- **Intervals:** median 0.08s (p5 0.00s / p95 1.80s, n=1873)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1874/1874 records)
    "BecameVisible"  x636
    "BecameInvisible"  x614
    "BecameCameraCentered"  x312
    "BecameCameraUncentered"  x312
data.pieceId  (string, 1874/1874 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1874/1874 records)
    1380 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 1707 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1264); Unit 1 Dev (443)
- **Intervals:** median 0.95s (p5 0.17s / p95 14.16s, n=1706)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 1707/1707 records)
    "pressed"  x1707
data.actionType  (string, 1707/1707 records)
    "Move"  x1336
    "Interact"  x268
    "Jump"  x54
    "Descend"  x19
    "Ascend"  x15
    "Hoverboard"  x11
    "Sprint"  x4
data.key  (string, 1707/1707 records, 3 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 1707/1707 records)
    "Player"  x1608
    "Drone"  x99
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 963 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (689); Unit 1 Dev (274)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=961)
- **Fields under `data`:**

```text
data.position  (object, 963/963 records)
data.position.x  (number, 963/963 records)
    numeric range -20.3326 .. 1426.91 (305 unique)
data.position.y  (number, 963/963 records)
    numeric range -5.58007 .. 161.109 (196 unique)
data.position.z  (number, 963/963 records)
    numeric range -117.207 .. 2224.98 (307 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 913 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (652); Unit 1 Dev (261)
- **eventKey:** present on 634 of 913 records
- **Intervals:** median 4.88s (p5 0.01s / p95 35.19s, n=912)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x634; [conversationId, dialogueEventType] x279
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 913/913 records)
    numeric range 8 .. 103 (23 unique)
data.dialogueEventType  (string, 913/913 records)
    "DialogueNodeEvent"  x634
    "DialogueStartEvent"  x141
    "DialogueFinishEvent"  x138
data.nodeId  (number, 634/913 records)
    numeric range 0 .. 290 (178 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 123 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (102); Unit 1 Dev (21)
- **Intervals:** median 8.73s (p5 0.29s / p95 1173.37s, n=122)
- **Fields under `data`:**

```text
data.actionType  (string, 123/123 records)
    "Press E to Install"  x37
    "Press E to Place"  x26
    "Press E to Pick up"  x21
    "TalkTo"  x11
    "Press E to Scan"  x10
    "E to Talk"  x4
    "Press E to Insert"  x4
    "Press E to Open Locker"  x4
    "Press E to Operate"  x3
    "Inspect Alien Glyph"  x1
    "Press E to Collect"  x1
    "Press [E/Action button] to enter escape pod "  x1
data.objectName  (string, 123/123 records)
    38 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 80 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (80)
- **Intervals:** median 1.63s (p5 0.33s / p95 12.61s, n=79)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x74; [Soil Key Puzzle Status, Unit] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/80 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/80 records)
    "Unit 2 Prod (Refactor)"  x6
data.actionType  (string, 74/80 records)
    "RightDrag"  x41
    "LeftDrag"  x33
data.currentSoilType  (string, 74/80 records)
    "SAND"  x20
    "CLAYSAND"  x15
    "SANDGRAVEL"  x13
    "CLAY"  x11
    "CLAYROCK"  x9
    "BEDROCK"  x3
    "GRAVEL"  x3
data.isCorrectSelection  (string, 74/80 records)
    "false"  x54
    "true"  x20
data.waterLevelStatus  (string, 74/80 records)
    "TooHigh"  x46
    "Proper"  x26
    "TooLow"  x2
data.waterRetentionChange  (string, 74/80 records)
    "Increase"  x38
    "NoChange"  x20
    "Decrease"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationNodeEvent` — 53 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (28); Unit 2 Prod (Refactor) (25)
- **Intervals:** median 1.23s (p5 0.05s / p95 17.27s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "argumentationNodeHoverEnd"  x22
    "argumentationNodeHoverStart"  x22
    "argumentationNodeAdd"  x9
data.argumentationTitle  (string, 53/53 records)
    "Unit 2 – Watershed"  x25
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x9
data.nodeName  (string, 53/53 records)
    "A"  x15
    "II"  x13
    "1"  x11
    "I"  x6
    "B"  x4
    "C"  x2
    "D"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 44 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (44)
- **Intervals:** median 7.68s (p5 0.95s / p95 1326.06s, n=43)
- **`data` key-set variants:** [actionType, featureUsed, legendName] x20; [actionType, featureUsed] x18; [actionType, featureUsed, location] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "Selected"  x17
    "MapCloseEvent"  x9
    "MapOpenEvent"  x9
    "WaypointSetEvent"  x4
    "Unselected"  x3
    "WaypointMoveEvent"  x2
data.featureUsed  (string, 44/44 records)
    "Legend"  x20
    "Map"  x18
    "Waypoint"  x6
data.legendName  (string, 20/44 records)
    "0 ft"  x6
    "Water"  x3
    "330 ft"  x2
    "360 ft"  x2
    "90 ft"  x2
    "120 ft"  x1
    "270 ft"  x1
    "30 ft"  x1
    "300 ft"  x1
    "60 ft"  x1
data.location  (object, 6/44 records)
data.location.x  (number, 6/44 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 6/44 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 6/44 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 33 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (16)
- **eventKey:** present on 33 of 33 records
- **Intervals:** median 251.60s (p5 0.01s / p95 85506.55s, n=32)
- **`data` key-set variants:** [questEventType, questID, questName] x20; [questEventType, questID, questName, questSuccessOrFailure] x13
- **Fields under `data`:**

```text
data.questEventType  (string, 33/33 records)
    "questActiveEvent"  x20
    "questFinishEvent"  x13
data.questID  (string, 33/33 records)
    "21"  x4
    "29"  x4
    "31"  x4
    "22"  x3
    "24"  x3
    "25"  x3
    "32"  x3
    "23"  x2
    "28"  x2
    "33"  x2
    "34"  x2
    "54"  x1
data.questName  (string, 33/33 records)
    "Escape the Ruin"  x4
    "Gear Up"  x4
    "TK, Reporting In!"  x4
    "Getting the Band Back Together"  x3
    "Info and Intros"  x3
    "Investigate the Temple"  x3
    "Which Watershed?"  x3
    "Defend the Expedition"  x2
    "Foraged Forging"  x2
    "Getting Your Space Legs"  x2
    "What Was That?"  x2
    "Claim of Command"  x1
data.questSuccessOrFailure  (string, 13/33 records)
    "Succeeded"  x13
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationToolEvent` — 28 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (21); Unit 2 Prod (Refactor) (7)
- **Intervals:** median 0.82s (p5 0.01s / p95 84.86s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "argumentationToolOpen"  x18
    "argumentationToolClose"  x10
data.argumentationTitle  (string, 28/28 records)
    "Unit 1 - Freshwater"  x19
    "Unit 2 – Watershed"  x7
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 28/28 records)
    "BackingInfoPanel - "  x19
    "BackingInfoPanel - Waterfall Data"  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DEBUGMenu` — 16 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (8); Unit 2 Prod (Refactor) (6); Unit 1 Dev (2)
- **Intervals:** median 197.81s (p5 9.66s / p95 215532.10s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "DebugMenuStateChanged"  x16
data.isOpened  (bool, 16/16 records)
    false  x16
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 13 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 43502.54s (p5 225.77s / p95 280041.58s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 10 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (10)
- **Intervals:** median 86004.96s (p5 685.96s / p95 344560.04s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 10/10 records)
    true  x10
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (6)
- **Intervals:** median 3.18s (p5 1.82s / p95 119.15s, n=5)
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

- **Scenes:** Unit 1 Dev (4); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 58.02s (p5 32.09s / p95 621308.45s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationSessionClose"  x3
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 6/6 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 6 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); MainMenu (1); Unit 1 Dev (1)
- **Intervals:** median 87930.96s (p5 17473.08s / p95 516979.60s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 6/6 records)
    false  x6
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationAnswerEvent` — 3 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 388419.32s (p5 38952.96s / p95 737885.67s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "submitAnswerEvent"  x3
data.answerSubmitted  (string, 3/3 records)
    "A,1,I"  x2
    "A,1,II"  x1
data.argumentationTitle  (string, 3/3 records)
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
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
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationNodeEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (80 records)
- `TopographicMapEvent` data.actionType: "Selected" (17x); "Unselected" (3x); "WaypointMoveEvent" (2x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (20x); "Waypoint" (6x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 3 Dev' has no records of this event
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*