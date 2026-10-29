# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1fc

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1fc
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1fc.jsonl
- **Records:** 9193 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1fc
- **Time span:** 2026-09-24T13:29:58.772000+00:00 .. 2026-10-07T15:13:52.979000+00:00 (313h 43m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1fc\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 9193 records, 6 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 97 INFO, 2 NOT_TESTED, 73 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3836 | 41.73 | 1 | 2 | 0 | 2026-09-30T13:39:32.302000+00:00 | 2026-10-07T15:13:52.979000+00:00 | 169h 34m |
| InputEvent | 2072 | 22.54 | 1 | 4 | 0 | 2026-09-28T13:02:19.265000+00:00 | 2026-10-07T15:13:43.480000+00:00 | 218h 11m |
| PlayerPositionEvent | 1712 | 18.62 | 1 | 4 | 0 | 2026-09-24T13:30:10.043000+00:00 | 2026-10-07T15:13:50.451000+00:00 | 313h 43m |
| DialogueEvent | 1011 | 11.0 | 1 | 4 | 670 | 2026-09-24T16:06:37.600000+00:00 | 2026-10-07T15:11:32.608000+00:00 | 311h 4m |
| ObjectInterEvent | 157 | 1.71 | 1 | 3 | 0 | 2026-09-28T13:08:38.061000+00:00 | 2026-10-07T15:11:53.666000+00:00 | 218h 3m |
| argumentationNodeEvent | 156 | 1.7 | 1 | 1 | 0 | 2026-09-28T13:35:19.184000+00:00 | 2026-09-30T13:27:22.617000+00:00 | 47h 52m |
| TopographicMapEvent | 59 | 0.64 | 1 | 2 | 0 | 2026-09-30T13:40:45.395000+00:00 | 2026-10-07T13:30:37.634000+00:00 | 167h 49m |
| questEvent | 44 | 0.48 | 1 | 4 | 44 | 2026-09-24T16:06:37.588000+00:00 | 2026-10-07T15:07:25.201000+00:00 | 311h 0m |
| Soil Key Puzzle | 28 | 0.3 | 1 | 2 | 0 | 2026-10-01T13:16:05.566000+00:00 | 2026-10-07T15:12:17.721000+00:00 | 145h 56m |
| gameWindowFocusEvent | 28 | 0.3 | 1 | 4 | 0 | 2026-09-24T13:29:58.772000+00:00 | 2026-10-07T15:07:19.159000+00:00 | 313h 37m |
| DEBUGMenu | 16 | 0.17 | 1 | 5 | 0 | 2026-09-24T13:30:10.036000+00:00 | 2026-10-07T15:07:20.141000+00:00 | 313h 37m |
| DaniEvent | 16 | 0.17 | 1 | 3 | 0 | 2026-09-29T13:11:55.068000+00:00 | 2026-10-07T13:22:06.280000+00:00 | 192h 10m |
| gameWindowUnfocusEvent | 16 | 0.17 | 1 | 4 | 0 | 2026-09-24T13:30:17.834000+00:00 | 2026-10-07T15:07:16.891000+00:00 | 313h 36m |
| gameStartEvent | 14 | 0.15 | 1 | 1 | 0 | 2026-09-24T13:29:58.773000+00:00 | 2026-10-07T15:07:10.058000+00:00 | 313h 37m |
| argumentationEvent | 8 | 0.09 | 1 | 1 | 0 | 2026-09-28T13:35:11.875000+00:00 | 2026-09-30T13:27:27.796000+00:00 | 47h 52m |
| argumentationToolEvent | 7 | 0.08 | 1 | 1 | 0 | 2026-09-28T13:35:08.090000+00:00 | 2026-09-30T13:25:47.891000+00:00 | 47h 50m |
| argumentationAnswerEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-09-28T13:35:33.744000+00:00 | 2026-09-30T13:27:27.766000+00:00 | 47h 51m |
| chatEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-07T13:21:44.931000+00:00 | 2026-10-07T13:21:57.073000+00:00 | 12.1s |
| crash | 3 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.02 | 1 | 1 | 0 | 2026-09-28T13:41:04.760000+00:00 | 2026-09-30T13:30:24.343000+00:00 | 47h 49m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 7116.616s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 172159.583s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.747s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.83s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.571s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 139.419s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 41.318s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3.57s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 79655.073s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1153.892s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1158.107s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 16 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 180 ft; 30 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 36; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 22 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[208] _id=6aba6817485cab4c9567bc13 ts=2026-09-28T13:13:59.2830000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[256] _id=6aba6985485cab4c9567d5d1 ts=2026-09-28T13:20:05.2600000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[329] _id=6aba6ab1485cab4c9567f24d ts=2026-09-28T13:25:05.7100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[6259] _id=6ac4f184de269131f9b00953 ts=2026-10-06T13:02:58.1850000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[1] _id=6ab525d7485cab4c95511441 ts=2026-09-24T13:29:58.7730000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[32] _id=6aba6547485cab4c95679ae7 ts=2026-09-28T13:01:59.0150000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[765] _id=6abbb7cb485cab4c957c21c8 ts=2026-09-29T13:06:18.8040000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[0] _id=6ab525d6485cab4c9551143b ts=2026-09-24T13:29:58.7720000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[4] _id=6ab525e9485cab4c955117e5 ts=2026-09-24T13:30:17.9010000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[7] _id=6ab54aab485cab4c9552dd01 ts=2026-09-24T16:06:27.5310000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[5] _id=6ab525e9485cab4c955117e3 ts=2026-09-24T13:30:17.8340000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[11] _id=6ab54aab485cab4c9552dcff ts=2026-09-24T16:06:26.9360000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[26] _id=6ab54b1a485cab4c9552dd71 ts=2026-09-24T16:08:58.5760000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 8 of 59 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2070] _id=6abd115d485cab4c9588f166 ts=2026-09-30T13:40:45.3950000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2071] _id=6abd115f485cab4c9588f1bd ts=2026-09-30T13:40:47.3750000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2073] _id=6abd1163485cab4c9588f265 ts=2026-09-30T13:40:51.0750000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3835 | 0.0 | 0.03 | 159.181 | 1.274 | 347038.292 | 0.38 | 2321 | 5 |
| InputEvent | 2071 | 0.0 | 1.747 | 379.278 | 28.309 | 343109.678 | 0.16 | 70 | 9 |
| PlayerPositionEvent | 1708 | 9.591 | 10.0 | 661.133 | 10.019 | 343107.412 | 0.09 | 0 | 10 |
| DialogueEvent | 1010 | 0.001 | 5.001 | 1108.807 | 72.671 | 343468.228 | 0.05 | 284 | 10 |
| ObjectInterEvent | 156 | 0.006 | 6.515 | 5032.023 | 484.601 | 346762.971 | 0.01 | 3 | 7 |
| argumentationNodeEvent | 155 | 0.002 | 0.341 | 1111.764 | 6.624 | 172032.241 | 0.05 | 46 | 1 |
| TopographicMapEvent | 58 | 0.263 | 4.571 | 10417.108 | 84122.043 | 343552.73 | 0.01 | 0 | 5 |
| questEvent | 43 | 0.003 | 295.933 | 26038.317 | 85218.032 | 343996.138 | 0.0 | 9 | 14 |
| Soil Key Puzzle | 27 | 0.29 | 2.83 | 19458.228 | 122710.525 | 346759.985 | 0.0 | 0 | 3 |
| gameWindowFocusEvent | 27 | 0.611 | 1153.892 | 41816.311 | 260169.975 | 345832.033 | 0.0 | 0 | 16 |
| DEBUGMenu | 15 | 8.156 | 7116.616 | 75268.674 | 344495.385 | 345828.87 | 0.0 | 0 | 11 |
| DaniEvent | 15 | 0.678 | 2.621 | 46120.747 | 225246.988 | 343456.605 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 15 | 0.487 | 1158.107 | 75267.937 | 365881.367 | 433921.38 | 0.0 | 0 | 9 |
| gameStartEvent | 13 | 67.01 | 79655.073 | 86848.56 | 344684.959 | 345832.034 | 0.0 | 0 | 11 |
| argumentationEvent | 7 | 29.186 | 40.215 | 24619.417 | 120479.089 | 172074.752 | 0.0 | 0 | 1 |
| argumentationToolEvent | 6 | 1.407 | 41.318 | 28706.633 | 129074.334 | 172072.469 | 0.0 | 0 | 1 |
| argumentationAnswerEvent | 3 | 76.871 | 139.419 | 57438.007 | 154901.901 | 172097.732 | 0.0 | 0 | 1 |
| chatEvent | 3 | 2.421 | 3.57 | 4.047 | 5.893 | 6.151 | 14.82 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 172159.583 | 172159.583 | 172159.583 | 172159.583 | 172159.583 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 11 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[7733] _id=6ac50e37de269131f9b42b4c ts=2026-10-06T15:05:27.0150000Z == 6aa413b141b41dbac0c7f1fc.jsonl[7728] _id=6ac50e37de269131f9b42b4e ts=2026-10-06T15:05:27.0150000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[7736] _id=6ac50e38de269131f9b42b5c ts=2026-10-06T15:05:27.0180000Z == 6aa413b141b41dbac0c7f1fc.jsonl[7737] _id=6ac50e38de269131f9b42b60 ts=2026-10-06T15:05:27.0180000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[8901] _id=6ac6602dde269131f9bb8053 ts=2026-10-07T15:07:25.1790000Z == 6aa413b141b41dbac0c7f1fc.jsonl[8902] _id=6ac6602dde269131f9bb8054 ts=2026-10-07T15:07:25.1790000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 101 group(s), 143 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2003] _id=6abd1115485cab4c9588e481 ts=2026-09-30T13:39:32.4940000Z == 6aa413b141b41dbac0c7f1fc.jsonl[2010] _id=6abd1116485cab4c9588e490 ts=2026-09-30T13:39:32.4940000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2006] _id=6abd1116485cab4c9588e497 ts=2026-09-30T13:39:32.7400000Z == 6aa413b141b41dbac0c7f1fc.jsonl[1998] _id=6abd1116485cab4c9588e4a5 ts=2026-09-30T13:39:32.7400000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2049] _id=6abd112f485cab4c9588ea31 ts=2026-09-30T13:39:58.6840000Z == 6aa413b141b41dbac0c7f1fc.jsonl[2045] _id=6abd112f485cab4c9588ea39 ts=2026-09-30T13:39:58.6840000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2099] _id=6abe5884485cab4c95a4027f ts=? == 6aa413b141b41dbac0c7f1fc.jsonl[6244] _id=6ac4f182de269131f9b0092f ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 50 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6aa413b141b41dbac0c7f1fc.jsonl[147] _id=6aba66d6485cab4c9567a731 ts=2026-09-28T13:08:38.0610000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[143] _id=6aba66d6485cab4c9567a733 ts=2026-09-28T13:08:38.0700000Z`; `139ms: 6aa413b141b41dbac0c7f1fc.jsonl[795] _id=6abbb856485cab4c957c28bc ts=2026-09-29T13:08:38.7250000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[798] _id=6abbb856485cab4c957c28c7 ts=2026-09-29T13:08:38.8640000Z`; `223ms: 6aa413b141b41dbac0c7f1fc.jsonl[824] _id=6abbb8f2485cab4c957c3cca ts=2026-09-29T13:11:14.6680000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[834] _id=6abbb8f3485cab4c957c3cdd ts=2026-09-29T13:11:14.8910000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 429 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `246ms: 6aa413b141b41dbac0c7f1fc.jsonl[2010] _id=6abd1116485cab4c9588e490 ts=2026-09-30T13:39:32.4940000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[2006] _id=6abd1116485cab4c9588e497 ts=2026-09-30T13:39:32.7400000Z`; `62ms: 6aa413b141b41dbac0c7f1fc.jsonl[2012] _id=6abd1116485cab4c9588e4ab ts=2026-09-30T13:39:32.7400000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[1994] _id=6abd1116485cab4c9588e4af ts=2026-09-30T13:39:32.8020000Z`; `16ms: 6aa413b141b41dbac0c7f1fc.jsonl[2021] _id=6abd111f485cab4c9588e6f7 ts=2026-09-30T13:39:42.1170000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[2005] _id=6abd111f485cab4c9588e6f9 ts=2026-09-30T13:39:42.1330000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `806ms: 6aa413b141b41dbac0c7f1fc.jsonl[8241] _id=6ac6490fde269131f9b9215a ts=2026-10-07T13:28:47.8480000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[8245] _id=6ac64910de269131f9b92180 ts=2026-10-07T13:28:48.6540000Z`; `766ms: 6aa413b141b41dbac0c7f1fc.jsonl[8244] _id=6ac64910de269131f9b9216f ts=2026-10-07T13:28:48.2140000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[8250] _id=6ac64911de269131f9b9218e ts=2026-10-07T13:28:48.9800000Z`; `697ms: 6aa413b141b41dbac0c7f1fc.jsonl[8245] _id=6ac64910de269131f9b92180 ts=2026-10-07T13:28:48.6540000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[8247] _id=6ac64911de269131f9b921a2 ts=2026-10-07T13:28:49.3510000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 45 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa413b141b41dbac0c7f1fc.jsonl[530] _id=6aba6d17485cab4c95680a90 ts=2026-09-28T13:35:19.2150000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[531] _id=6aba6d17485cab4c95680a93 ts=2026-09-28T13:35:19.2170000Z`; `31ms: 6aa413b141b41dbac0c7f1fc.jsonl[531] _id=6aba6d17485cab4c95680a93 ts=2026-09-28T13:35:19.2170000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[532] _id=6aba6d17485cab4c95680a97 ts=2026-09-28T13:35:19.2480000Z`; `912ms: 6aa413b141b41dbac0c7f1fc.jsonl[532] _id=6aba6d17485cab4c95680a97 ts=2026-09-28T13:35:19.2480000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[533] _id=6aba6d18485cab4c95680aa5 ts=2026-09-28T13:35:20.1600000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `611ms: 6aa413b141b41dbac0c7f1fc.jsonl[7606] _id=6ac4f936de269131f9b0dc01 ts=2026-10-06T13:35:50.0790000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[7607] _id=6ac4f936de269131f9b0dc15 ts=2026-10-06T13:35:50.6900000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `725ms: 6aa413b141b41dbac0c7f1fc.jsonl[1138] _id=6abbbce7485cab4c957d0596 ts=2026-09-29T13:28:07.5870000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[1136] _id=6abbbce8485cab4c957d05bc ts=2026-09-29T13:28:08.3120000Z`; `487ms: 6aa413b141b41dbac0c7f1fc.jsonl[7608] _id=6ac4f935de269131f9b0dbfb ts=2026-10-06T13:35:49.8990000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[7604] _id=6ac4f936de269131f9b0dc0d ts=2026-10-06T13:35:50.3860000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa413b141b41dbac0c7f1fc.jsonl[6259] _id=6ac4f184de269131f9b00953 ts=2026-10-06T13:02:58.1850000Z ~ 6aa413b141b41dbac0c7f1fc.jsonl[6265] _id=6ac4f184de269131f9b00957 ts=2026-10-06T13:02:58.1880000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1fc.jsonl[2098] _id=6abe587d485cab4c95a4024d ts=2026-10-01T12:56:29.6230000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5032] _id=6ac39f62de269131f9a840a2 ts=2026-10-05T13:00:18.4930000Z; 95h 32m: 6aa413b141b41dbac0c7f1fc.jsonl[2] _id=6ab525e2485cab4c9551160e ts=2026-09-24T13:30:10.0360000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[33] _id=6aba6555485cab4c95679b0b ts=2026-09-28T13:02:13.9280000Z; 24h 4m: 6aa413b141b41dbac0c7f1fc.jsonl[33] _id=6aba6555485cab4c95679b0b ts=2026-09-28T13:02:13.9280000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[767] _id=6abbb7d3485cab4c957c2242 ts=2026-09-29T13:06:27.9300000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa413b141b41dbac0c7f1fc.jsonl[5016] _id=6abe631c485cab4c95a685cf ts=2026-10-01T13:41:48.1110000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5124] _id=6ac3a0bcde269131f9a85525 ts=2026-10-05T13:06:04.7160000Z; 48h 29m: 6aa413b141b41dbac0c7f1fc.jsonl[908] _id=6abbb921485cab4c957c4230 ts=2026-09-29T13:12:00.9330000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5017] _id=6abe631a485cab4c95a68593 ts=2026-10-01T13:41:46.6570000Z; 48h 15m: 6aa413b141b41dbac0c7f1fc.jsonl[5125] _id=6ac3a0bfde269131f9a85550 ts=2026-10-05T13:06:07.0660000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8106] _id=6ac64765de269131f9b8cfd6 ts=2026-10-07T13:21:41.3900000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa413b141b41dbac0c7f1fc.jsonl[4980] _id=6abe62a2485cab4c95a66d09 ts=2026-10-01T13:39:46.1890000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5101] _id=6ac3a04ede269131f9a84c2c ts=2026-10-05T13:04:14.4170000Z; 92h 55m: 6aa413b141b41dbac0c7f1fc.jsonl[9] _id=6ab54aac485cab4c9552dd09 ts=2026-09-24T16:06:37.6090000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[50] _id=6aba656c485cab4c95679b57 ts=2026-09-28T13:02:35.9770000Z; 23h 37m: 6aa413b141b41dbac0c7f1fc.jsonl[761] _id=6aba6e6e485cab4c956818e3 ts=2026-09-28T13:41:02.3290000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1023] _id=6abbbaaf485cab4c957c8472 ts=2026-09-29T13:18:39.7550000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 284 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fc.jsonl[4710] _id=6abe5f2c485cab4c95a560b3 ts=2026-10-01T13:25:00.4240000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[4712] _id=6abe5f2c485cab4c95a560bf ts=2026-10-01T13:25:00.4250000Z; 1ms: 6aa413b141b41dbac0c7f1fc.jsonl[7307] _id=6ac4f41bde269131f9b02dae ts=2026-10-06T13:14:03.5170000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[7271] _id=6ac4f41bde269131f9b02db2 ts=2026-10-06T13:14:03.5180000Z; 1ms: 6aa413b141b41dbac0c7f1fc.jsonl[7421] _id=6ac4f629de269131f9b057fc ts=2026-10-06T13:22:49.0550000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[7424] _id=6ac4f629de269131f9b05804 ts=2026-10-06T13:22:49.0560000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 49m 
  - Evidence: 47h 49m: 6aa413b141b41dbac0c7f1fc.jsonl[762] _id=6aba6e70485cab4c95681907 ts=2026-09-28T13:41:04.7600000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1856] _id=6abd0ef0485cab4c95881710 ts=2026-09-30T13:30:24.3430000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1fc.jsonl[5025] _id=6abe6322485cab4c95a686c1 ts=2026-10-01T13:41:54.6260000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5033] _id=6ac39f69de269131f9a840d2 ts=2026-10-05T13:00:24.3040000Z; 23h 27m: 6aa413b141b41dbac0c7f1fc.jsonl[736] _id=6aba6e43485cab4c95681751 ts=2026-09-28T13:40:19.8920000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[772] _id=6abbb825485cab4c957c256c ts=2026-09-29T13:07:49.1270000Z; 23h 22m: 6aa413b141b41dbac0c7f1fc.jsonl[1253] _id=6abbbf2c485cab4c957d7e64 ts=2026-09-29T13:37:48.4570000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1295] _id=6abd07df485cab4c958679d1 ts=2026-09-30T13:00:17.5010000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 70 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fc.jsonl[7733] _id=6ac50e37de269131f9b42b4c ts=2026-10-06T15:05:27.0150000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[7728] _id=6ac50e37de269131f9b42b4e ts=2026-10-06T15:05:27.0150000Z; 0ms: 6aa413b141b41dbac0c7f1fc.jsonl[7736] _id=6ac50e38de269131f9b42b5c ts=2026-10-06T15:05:27.0180000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[7737] _id=6ac50e38de269131f9b42b60 ts=2026-10-06T15:05:27.0180000Z; 0ms: 6aa413b141b41dbac0c7f1fc.jsonl[8892] _id=6ac6602dde269131f9bb805b ts=2026-10-07T15:07:25.1800000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8893] _id=6ac6602dde269131f9bb805c ts=2026-10-07T15:07:25.1800000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 19m 
  - Evidence: 96h 19m: 6aa413b141b41dbac0c7f1fc.jsonl[4567] _id=6abe5d15485cab4c95a4978f ts=2026-10-01T13:16:05.5680000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5682] _id=6ac3a7a0de269131f9a95e01 ts=2026-10-05T13:35:28.5390000Z; 24h 30m: 6aa413b141b41dbac0c7f1fc.jsonl[7168] _id=6ac4f292de269131f9b01b1b ts=2026-10-06T13:07:30.8010000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8394] _id=6ac64b2cde269131f9b9a695 ts=2026-10-07T13:37:48.1130000Z; 23h 29m: 6aa413b141b41dbac0c7f1fc.jsonl[5682] _id=6ac3a7a0de269131f9a95e01 ts=2026-10-05T13:35:28.5390000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[6456] _id=6ac4f212de269131f9b00fe6 ts=2026-10-06T13:05:22.2340000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.006s..0.009s shown 
  - Evidence: 6ms: 6aa413b141b41dbac0c7f1fc.jsonl[1364] _id=6abd088c485cab4c958687f3 ts=2026-09-30T13:03:11.0040000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1362] _id=6abd088c485cab4c958687f7 ts=2026-09-30T13:03:11.0100000Z; 8ms: 6aa413b141b41dbac0c7f1fc.jsonl[1022] _id=6abbbaaf485cab4c957c8466 ts=2026-09-29T13:18:39.7270000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1024] _id=6abbbaaf485cab4c957c846c ts=2026-09-29T13:18:39.7350000Z; 9ms: 6aa413b141b41dbac0c7f1fc.jsonl[147] _id=6aba66d6485cab4c9567a731 ts=2026-09-28T13:08:38.0610000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[143] _id=6aba66d6485cab4c9567a733 ts=2026-09-28T13:08:38.0700000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1fc.jsonl[5018] _id=6abe631f485cab4c95a68629 ts=2026-10-01T13:41:51.0870000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5035] _id=6ac39f69de269131f9a840d0 ts=2026-10-05T13:00:18.4990000Z; 92h 53m: 6aa413b141b41dbac0c7f1fc.jsonl[25] _id=6ab54b13485cab4c9552dd5f ts=2026-09-24T16:08:51.5890000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[36] _id=6aba655b485cab4c95679b1f ts=2026-09-28T13:02:13.9340000Z; 23h 25m: 6aa413b141b41dbac0c7f1fc.jsonl[755] _id=6aba6e6e485cab4c956818e1 ts=2026-09-28T13:41:02.0460000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[768] _id=6abbb7d4485cab4c957c224c ts=2026-09-29T13:06:27.9390000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6aa413b141b41dbac0c7f1fc.jsonl[4517] _id=6abe5c64485cab4c95a47b4c ts=2026-10-01T13:13:07.8030000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5732] _id=6ac3a802de269131f9a96fb9 ts=2026-10-05T13:37:06.0950000Z; 24h 27m: 6aa413b141b41dbac0c7f1fc.jsonl[7268] _id=6ac4f381de269131f9b0244f ts=2026-10-06T13:11:28.7010000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8408] _id=6ac64b56de269131f9b9af02 ts=2026-10-07T13:38:30.4030000Z; 23h 22m: 6aa413b141b41dbac0c7f1fc.jsonl[6200] _id=6ac3a8d9de269131f9a9981d ts=2026-10-05T13:40:41.1950000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[6261] _id=6ac4f184de269131f9b0095d ts=2026-10-06T13:02:58.5360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2321 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fc.jsonl[1988] _id=6abd1115485cab4c9588e463 ts=2026-09-30T13:39:32.4940000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[2003] _id=6abd1115485cab4c9588e481 ts=2026-09-30T13:39:32.4940000Z; 0ms: 6aa413b141b41dbac0c7f1fc.jsonl[1997] _id=6abd1115485cab4c9588e45b ts=2026-09-30T13:39:32.4940000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1988] _id=6abd1115485cab4c9588e463 ts=2026-09-30T13:39:32.4940000Z; 0ms: 6aa413b141b41dbac0c7f1fc.jsonl[1998] _id=6abd1116485cab4c9588e4a5 ts=2026-09-30T13:39:32.7400000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[2012] _id=6abd1116485cab4c9588e4ab ts=2026-09-30T13:39:32.7400000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 19m 
  - Evidence: 96h 19m: 6aa413b141b41dbac0c7f1fc.jsonl[4566] _id=6abe5d18485cab4c95a497e5 ts=2026-10-01T13:16:08.5510000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5683] _id=6ac3a7a0de269131f9a95dfd ts=2026-10-05T13:35:28.5360000Z; 48h 1m: 6aa413b141b41dbac0c7f1fc.jsonl[5706] _id=6ac3a7cade269131f9a965c7 ts=2026-10-05T13:36:10.1590000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8393] _id=6ac64b2cde269131f9b9a691 ts=2026-10-07T13:37:48.1090000Z; 1h 33m: 6aa413b141b41dbac0c7f1fc.jsonl[8402] _id=6ac64b53de269131f9b9ae39 ts=2026-10-07T13:38:27.1280000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8998] _id=6ac66139de269131f9bb9051 ts=2026-10-07T15:11:53.6620000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa413b141b41dbac0c7f1fc.jsonl[4984] _id=6abe62ab485cab4c95a6704d ts=2026-10-01T13:39:55.6370000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5122] _id=6ac3a0acde269131f9a85366 ts=2026-10-05T13:05:48.3670000Z; 24h 15m: 6aa413b141b41dbac0c7f1fc.jsonl[5270] _id=6ac3a2d5de269131f9a87bda ts=2026-10-05T13:15:01.5120000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[7537] _id=6ac4f802de269131f9b0b2fa ts=2026-10-06T13:30:42.4890000Z; 23h 44m: 6aa413b141b41dbac0c7f1fc.jsonl[7543] _id=6ac4f813de269131f9b0b605 ts=2026-10-06T13:30:59.3770000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[7975] _id=6ac645dede269131f9b8bd95 ts=2026-10-07T13:15:09.9190000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 48m 
  - Evidence: 47h 48m: 6aa413b141b41dbac0c7f1fc.jsonl[652] _id=6aba6db1485cab4c95681091 ts=2026-09-28T13:37:53.1630000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1723] _id=6abd0df2485cab4c9587a2e8 ts=2026-09-30T13:26:10.8950000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 47m 
  - Evidence: 47h 47m: 6aa413b141b41dbac0c7f1fc.jsonl[613] _id=6aba6db1485cab4c95681093 ts=2026-09-28T13:37:53.1820000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1702] _id=6abd0ddc485cab4c95879953 ts=2026-09-30T13:25:47.9340000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 47m 
  - Evidence: 47h 47m: 6aa413b141b41dbac0c7f1fc.jsonl[647] _id=6aba6dab485cab4c95681065 ts=2026-09-28T13:37:47.3220000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1680] _id=6abd0dab485cab4c95877f5c ts=2026-09-30T13:24:59.5630000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 46 interval(s) ≤ 0.002s..0.018s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1fc.jsonl[530] _id=6aba6d17485cab4c95680a90 ts=2026-09-28T13:35:19.2150000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[531] _id=6aba6d17485cab4c95680a93 ts=2026-09-28T13:35:19.2170000Z; 16ms: 6aa413b141b41dbac0c7f1fc.jsonl[1720] _id=6abd0ded485cab4c9587a07a ts=2026-09-30T13:26:04.0730000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1729] _id=6abd0dee485cab4c9587a0a1 ts=2026-09-30T13:26:04.0890000Z; 18ms: 6aa413b141b41dbac0c7f1fc.jsonl[1728] _id=6abd0df1485cab4c9587a21b ts=2026-09-30T13:26:09.0210000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1731] _id=6abd0df1485cab4c9587a239 ts=2026-09-30T13:26:09.0390000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 47m 
  - Evidence: 47h 47m: 6aa413b141b41dbac0c7f1fc.jsonl[651] _id=6aba6db0485cab4c95681087 ts=2026-09-28T13:37:52.0610000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1704] _id=6abd0dd8485cab4c958797bf ts=2026-09-30T13:25:44.5300000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1fc.jsonl[2094] _id=6abe5874485cab4c95a401eb ts=2026-10-01T12:56:20.1890000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5029] _id=6ac39f5cde269131f9a8405a ts=2026-10-05T13:00:12.2230000Z; 95h 32m: 6aa413b141b41dbac0c7f1fc.jsonl[1] _id=6ab525d7485cab4c95511441 ts=2026-09-24T13:29:58.7730000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[32] _id=6aba6547485cab4c95679ae7 ts=2026-09-28T13:01:59.0150000Z; 24h 4m: 6aa413b141b41dbac0c7f1fc.jsonl[32] _id=6aba6547485cab4c95679ae7 ts=2026-09-28T13:01:59.0150000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[765] _id=6abbb7cb485cab4c957c21c8 ts=2026-09-29T13:06:18.8040000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1fc.jsonl[2096] _id=6abe5874485cab4c95a401e7 ts=2026-10-01T12:56:20.1880000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5031] _id=6ac39f5cde269131f9a84056 ts=2026-10-05T13:00:12.2210000Z; 92h 55m: 6aa413b141b41dbac0c7f1fc.jsonl[7] _id=6ab54aab485cab4c9552dd01 ts=2026-09-24T16:06:27.5310000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[37] _id=6aba6547485cab4c95679ae3 ts=2026-09-28T13:01:59.0150000Z; 24h 4m: 6aa413b141b41dbac0c7f1fc.jsonl[37] _id=6aba6547485cab4c95679ae3 ts=2026-09-28T13:01:59.0150000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[764] _id=6abbb7ca485cab4c957c21c4 ts=2026-09-29T13:06:18.8030000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 32m 
  - Evidence: 120h 32m: 6aa413b141b41dbac0c7f1fc.jsonl[1292] _id=6abd07c2485cab4c9586787d ts=2026-09-30T12:59:47.8250000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5627] _id=6ac3a6c5de269131f9a93b2d ts=2026-10-05T13:31:49.2050000Z; 93h 32m: 6aa413b141b41dbac0c7f1fc.jsonl[26] _id=6ab54b1a485cab4c9552dd71 ts=2026-09-24T16:08:58.5760000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[760] _id=6aba6e6b485cab4c956818d1 ts=2026-09-28T13:40:59.9380000Z; 25h 31m: 6aa413b141b41dbac0c7f1fc.jsonl[7609] _id=6ac4f93ade269131f9b0dc9f ts=2026-10-06T13:35:54.5480000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[8898] _id=6ac66024de269131f9bb8010 ts=2026-10-07T15:07:16.8910000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 6aa413b141b41dbac0c7f1fc.jsonl[4748] _id=6abe5fac485cab4c95a589fd ts=2026-10-01T13:27:08.2330000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[5041] _id=6ac39f6ade269131f9a840ea ts=2026-10-05T13:00:24.3710000Z; 92h 55m: 6aa413b141b41dbac0c7f1fc.jsonl[13] _id=6ab54aac485cab4c9552dd05 ts=2026-09-24T16:06:37.5880000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[46] _id=6aba656b485cab4c95679b55 ts=2026-09-28T13:02:35.9590000Z; 23h 40m: 6aa413b141b41dbac0c7f1fc.jsonl[738] _id=6aba6e49485cab4c95681793 ts=2026-09-28T13:40:25.4410000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1049] _id=6abbbb50485cab4c957caa8a ts=2026-09-29T13:21:20.1230000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 6aa413b141b41dbac0c7f1fc.jsonl[1670] _id=6abd0d78485cab4c958760ef ts=2026-09-30T13:24:07.3210000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[1671] _id=6abd0d78485cab4c9587610a ts=2026-09-30T13:24:07.3240000Z; 3ms: 6aa413b141b41dbac0c7f1fc.jsonl[500] _id=6aba6cbd485cab4c95680785 ts=2026-09-28T13:33:49.4430000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[501] _id=6aba6cbd485cab4c95680787 ts=2026-09-28T13:33:49.4460000Z; 3ms: 6aa413b141b41dbac0c7f1fc.jsonl[6259] _id=6ac4f184de269131f9b00953 ts=2026-10-06T13:02:58.1850000Z -> 6aa413b141b41dbac0c7f1fc.jsonl[6265] _id=6ac4f184de269131f9b00957 ts=2026-10-06T13:02:58.1880000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[654] _id=6aba6dc4485cab4c95681167 ts=2026-09-28T13:38:12.3860000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[1639] _id=6abd0d5a485cab4c95875489 ts=2026-09-30T13:23:38.1340000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[1763] _id=6abd0e55485cab4c9587cc36 ts=2026-09-30T13:27:49.3380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 58 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2182] _id=6abe5a41485cab4c95a42521 ts=2026-10-01T13:03:34.5670000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2546] _id=6abe5a47485cab4c95a425bf ts=2026-10-01T13:03:52.0240000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2590] _id=6abe5a49485cab4c95a4263f ts=2026-10-01T13:03:56.4120000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 182 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[1996] _id=6abd1115485cab4c9588e457 ts=2026-09-30T13:39:32.4440000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2010] _id=6abd1116485cab4c9588e490 ts=2026-09-30T13:39:32.4940000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2006] _id=6abd1116485cab4c9588e497 ts=2026-09-30T13:39:32.7400000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 17 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[530] _id=6aba6d17485cab4c95680a90 ts=2026-09-28T13:35:19.2150000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[531] _id=6aba6d17485cab4c95680a93 ts=2026-09-28T13:35:19.2170000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[532] _id=6aba6d17485cab4c95680a97 ts=2026-09-28T13:35:19.2480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[1049] _id=6abbbb50485cab4c957caa8a ts=2026-09-29T13:21:20.1230000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[1384] _id=6abd08ca485cab4c95868b3d ts=2026-09-30T13:04:12.3240000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2099] _id=6abe5884485cab4c95a4027f ts=?`; `6aa413b141b41dbac0c7f1fc.jsonl[6244] _id=6ac4f182de269131f9b0092f ts=?`; `6aa413b141b41dbac0c7f1fc.jsonl[8890] _id=6ac6602dde269131f9bb804f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 391 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2705] _id=6abe5a66485cab4c95a428cd ts=2026-10-01T13:04:37.3210000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2757] _id=6abe5a72485cab4c95a42a07 ts=2026-10-01T13:04:50.0900000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2819] _id=6abe5a97485cab4c95a42e24 ts=2026-10-01T13:05:27.1560000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 816 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2342] _id=6abe5a31485cab4c95a42311 ts=2026-10-01T12:58:49.6630000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2348] _id=6abe5a32485cab4c95a4232f ts=2026-10-01T13:01:44.0320000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2357] _id=6abe5a32485cab4c95a42337 ts=2026-10-01T13:01:44.0590000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[541] _id=6aba6d22485cab4c95680aef ts=2026-09-28T13:35:29.9790000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[1688] _id=6abd0db2485cab4c958782b9 ts=2026-09-30T13:25:05.8770000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[1713] _id=6abd0de3485cab4c95879d02 ts=2026-09-30T13:25:55.8590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[648] _id=6aba6dae485cab4c95681077 ts=2026-09-28T13:37:50.6540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'DialogueStartEvent' (totals: 173 start, 168 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 67 unmatched 'BecameCameraCentered' (totals: 652 open, 643 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 87 unmatched 'BecameVisible' (totals: 1223 open, 1318 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 62 open, 78 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 27 start, 17 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 245 of 9189 adjacent _id pairs reverse in client time; worst 295.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1fc.jsonl[2270] _id=6abe5a30485cab4c95a422ff ts=2026-10-01T13:03:44.4230000Z`; `6aa413b141b41dbac0c7f1fc.jsonl[2271] _id=6abe5a31485cab4c95a4230b ts=2026-10-01T12:58:48.9770000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.15s, min -296.54s, max +2.10s over 9190 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1fc\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
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

### `PuzzlePieceVisibleEvent` — 3836 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3296); Unit 4 Dev (540)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.27s, n=3835)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3836/3836 records)
    "BecameInvisible"  x1318
    "BecameVisible"  x1223
    "BecameCameraCentered"  x652
    "BecameCameraUncentered"  x643
data.pieceId  (string, 3836/3836 records)
    27 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3836/3836 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2072 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1015); Unit 1 Dev (514); Unit 3 Dev (337); Unit 4 Dev (206)
- **Intervals:** median 1.75s (p5 0.12s / p95 28.31s, n=2071)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2072/2072 records)
    "pressed"  x2072
data.actionType  (string, 2072/2072 records)
    "Move"  x1531
    "Interact"  x324
    "Jump"  x107
    "Sprint"  x42
    "Pause"  x29
    "Map"  x24
    "Hoverboard"  x12
    "SkipCinematic"  x3
data.key  (string, 2072/2072 records, 2 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2072/2072 records)
    "Player"  x2072
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1712 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (815); Unit 1 Dev (642); Unit 3 Dev (158); Unit 4 Dev (97)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.02s, n=1708)
- **Fields under `data`:**

```text
data.position  (object, 1712/1712 records)
data.position.x  (number, 1712/1712 records)
    numeric range -106.953 .. 1421.19 (592 unique)
data.position.y  (number, 1712/1712 records)
    numeric range -113.991 .. 157.661 (493 unique)
data.position.z  (number, 1712/1712 records)
    numeric range -640.379 .. 2032.84 (597 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1011 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (536); Unit 1 Dev (410); Unit 4 Dev (40); Unit 3 Dev (25)
- **eventKey:** present on 670 of 1011 records
- **Intervals:** median 5.00s (p5 0.00s / p95 72.67s, n=1010)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x670; [conversationId, dialogueEventType] x341
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1011/1011 records)
    numeric range 8 .. 102 (25 unique)
data.dialogueEventType  (string, 1011/1011 records)
    "DialogueNodeEvent"  x670
    "DialogueStartEvent"  x173
    "DialogueFinishEvent"  x168
data.nodeId  (number, 670/1011 records)
    numeric range 0 .. 290 (163 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 157 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (86); Unit 2 Prod (Refactor) (69); Unit 4 Dev (2)
- **Intervals:** median 6.51s (p5 0.14s / p95 484.60s, n=156)
- **Fields under `data`:**

```text
data.actionType  (string, 157/157 records)
    "TalkTo"  x64
    "Press E to Pick up"  x26
    "Press E to Place"  x23
    "E to Talk"  x12
    "Press E to Install"  x10
    "Press E to Insert"  x7
    "Press E to Open Locker"  x6
    "Press E to Operate"  x4
    "Inspect Alien Glyph"  x2
    "Press [E/Action button] to enter escape pod "  x2
    "Press E to Collect"  x1
data.objectName  (string, 157/157 records)
    31 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 156 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (156)
- **Intervals:** median 0.34s (p5 0.02s / p95 6.62s, n=155)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 156/156 records)
    "argumentationNodeHoverEnd"  x78
    "argumentationNodeHoverStart"  x62
    "argumentationNodeAdd"  x11
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 156/156 records)
    "Unit 1 - Freshwater"  x116
    "Unit 1 - Argumentation Tutorial"  x40
data.nodeName  (string, 156/156 records)
    "1"  x65
    "A"  x62
    "I"  x24
    "II"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 59 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (35); Unit 2 Prod (Refactor) (24)
- **Intervals:** median 4.57s (p5 0.36s / p95 84122.04s, n=58)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, location] x11; [actionType, featureUsed, legendName] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 59/59 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
    "Selected"  x8
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x3
    "WaypointMoveEvent"  x2
data.featureUsed  (string, 59/59 records)
    "Map"  x40
    "Waypoint"  x11
    "Legend"  x8
data.legendName  (string, 8/59 records)
    "180 ft"  x2
    "360 ft"  x2
    "150 ft"  x1
    "30 ft"  x1
    "90 ft"  x1
    "Water"  x1
data.location  (object, 11/59 records)
data.location.x  (number, 11/59 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 11/59 records)
    8 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 11/59 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 44 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (26); Unit 2 Prod (Refactor) (14); Unit 3 Dev (2); Unit 4 Dev (2)
- **eventKey:** present on 44 of 44 records
- **Intervals:** median 295.93s (p5 0.00s / p95 85218.03s, n=43)
- **`data` key-set variants:** [questEventType, questID, questName] x27; [questEventType, questID, questName, questSuccessOrFailure] x17
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 44/44 records)
    "questActiveEvent"  x27
    "questFinishEvent"  x17
data.questID  (string, 44/44 records)
    13 unique values (see csv/event_unique_values.csv)
data.questName  (string, 44/44 records)
    13 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 17/44 records)
    "Succeeded"  x17
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 28 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev (8)
- **Intervals:** median 2.83s (p5 0.48s / p95 122710.53s, n=27)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x20; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/28 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/28 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
data.actionType  (string, 20/28 records)
    "RightDrag"  x12
    "LeftDrag"  x8
data.currentSoilType  (string, 20/28 records)
    "CLAYSAND"  x5
    "SAND"  x5
    "SANDGRAVEL"  x4
    "CLAY"  x3
    "GRAVEL"  x2
    "CLAYROCK"  x1
data.isCorrectSelection  (string, 20/28 records)
    "false"  x13
    "true"  x7
data.waterLevelStatus  (string, 20/28 records)
    "Proper"  x10
    "TooHigh"  x8
    "TooLow"  x2
data.waterRetentionChange  (string, 20/28 records)
    "Increase"  x7
    "NoChange"  x7
    "Decrease"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (7); Unit 1 Dev (5); Transition (1)
- **Intervals:** median 1153.89s (p5 1.97s / p95 260169.98s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 16 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 1 Dev (4); MainMenu (3); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 7116.62s (p5 9.85s / p95 344495.39s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "DebugMenuStateChanged"  x16
data.isOpened  (bool, 16/16 records)
    false  x16
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 16 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (8); Unit 1 Dev (4); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 2.62s (p5 1.22s / p95 225246.99s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "Close"  x8
    "Open"  x8
data.toolName  (string, 16/16 records, 16 empty-string)
    ""  x16
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowUnfocusEvent` — 16 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (7); MainMenu (1); Transition (1)
- **Intervals:** median 1158.11s (p5 0.65s / p95 365881.37s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    false  x16
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 79655.07s (p5 166.58s / p95 344684.96s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8)
- **Intervals:** median 40.22s (p5 29.40s / p95 120479.09s, n=7)
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

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 41.32s (p5 1.90s / p95 129074.33s, n=6)
- **Open findings:** 2 — see sections 5-8
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

### `argumentationAnswerEvent` — 4 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 139.42s (p5 83.13s / p95 154901.90s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "submitAnswerEvent"  x4
data.answerSubmitted  (string, 4/4 records)
    "A,1,I"  x4
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 3.57s (p5 2.54s / p95 5.89s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.chatID  (string, 4/4 records)
    "NA"  x2
    "[]"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x2
    "unit4"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 172159.58s (p5 172159.58s / p95 172159.58s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x2
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TopographicMapEvent` data.actionType: "Selected" (8x); "WaypointMoveEvent" (2x); "WaypointResetEvent" (3x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (8x); "Waypoint" (11x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*