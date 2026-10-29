# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f1

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f1
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f1.jsonl
- **Records:** 9198 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f1
- **Time span:** 2026-09-23T13:05:17.951000+00:00 .. 2026-10-07T15:13:55.803000+00:00 (338h 8m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f1\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **13 event types**, 9198 records, 6 scenes.
- Findings: **0 FAIL**, **42 WARNING**, 59 INFO, 2 NOT_TESTED, 44 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `EndOfUnit`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationNodeEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4016 | 43.66 | 1 | 2 | 0 | 2026-09-25T13:28:04.581000+00:00 | 2026-10-07T15:05:55.837000+00:00 | 289h 37m |
| InputEvent | 2058 | 22.37 | 1 | 5 | 0 | 2026-09-23T13:12:46.643000+00:00 | 2026-10-07T15:11:37.216000+00:00 | 337h 58m |
| PlayerPositionEvent | 2014 | 21.9 | 1 | 5 | 0 | 2026-09-23T13:07:00.473000+00:00 | 2026-10-07T15:13:55.803000+00:00 | 338h 6m |
| DialogueEvent | 789 | 8.58 | 1 | 5 | 524 | 2026-09-23T13:07:22.382000+00:00 | 2026-10-07T15:13:16.108000+00:00 | 338h 5m |
| ObjectInterEvent | 76 | 0.83 | 1 | 4 | 0 | 2026-09-23T13:17:38.241000+00:00 | 2026-10-07T15:11:37.587000+00:00 | 337h 53m |
| TopographicMapEvent | 47 | 0.51 | 1 | 3 | 0 | 2026-09-25T13:28:23.461000+00:00 | 2026-10-07T14:52:46.526000+00:00 | 289h 24m |
| questEvent | 45 | 0.49 | 1 | 4 | 45 | 2026-09-23T13:07:22.355000+00:00 | 2026-10-07T14:45:11.209000+00:00 | 337h 37m |
| gameWindowFocusEvent | 43 | 0.47 | 1 | 5 | 0 | 2026-09-23T13:05:17.951000+00:00 | 2026-10-07T14:49:31.852000+00:00 | 337h 44m |
| Soil Key Puzzle | 32 | 0.35 | 1 | 2 | 0 | 2026-10-01T13:36:45.859000+00:00 | 2026-10-07T14:57:14.785000+00:00 | 145h 20m |
| gameWindowUnfocusEvent | 27 | 0.29 | 1 | 4 | 0 | 2026-09-23T13:08:09.091000+00:00 | 2026-10-07T14:45:24.702000+00:00 | 337h 37m |
| DEBUGMenu | 23 | 0.25 | 1 | 6 | 0 | 2026-09-23T13:07:00.454000+00:00 | 2026-10-07T15:07:55.533000+00:00 | 338h 0m |
| gameStartEvent | 19 | 0.21 | 1 | 1 | 0 | 2026-09-23T13:05:17.951000+00:00 | 2026-10-07T14:42:38.817000+00:00 | 337h 37m |
| crash | 9 | 0.1 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 2815.61s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.584s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 14 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 140 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6310.87s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 459.369s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 544.851s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 363.858s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 76 records 
  - Expected: 235 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Collect; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to place canister; Press [E/Action button] to enter escape pod ; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 9 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 28; 33; 34; 36; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Defend the Expedition; Desert Delicacies; Forsaken Facility; Getting Your Space Legs; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; What Was That? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 97 mismatch(es); e.g. 'DialogueNodeEvent:30:1' vs expected 'DialogueNodeEvent:31:64' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[312] _id=6abbb844485cab4c957c2720 ts=2026-09-23T13:07:22.382Z`; `6aa413b141b41dbac0c7f1f1.jsonl[319] _id=6abbb844485cab4c957c2728 ts=2026-09-23T13:07:32.497Z`; `6aa413b141b41dbac0c7f1f1.jsonl[323] _id=6abbb846485cab4c957c2746 ts=2026-09-23T13:08:15.443Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 14 mismatch(es); e.g. 'questActiveEvent:28' vs expected 'questActiveEvent:31' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[317] _id=6abbb843485cab4c957c2712 ts=2026-09-23T13:07:22.355Z`; `6aa413b141b41dbac0c7f1f1.jsonl[657] _id=6abbb871485cab4c957c2bb2 ts=2026-09-23T13:22:30.494Z`; `6aa413b141b41dbac0c7f1f1.jsonl[659] _id=6abbb872485cab4c957c2bba ts=2026-09-23T13:22:35.697Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[0] _id=6ab3ce8e485cab4c954b84fe ts=2026-09-23T13:05:17.9510000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[896] _id=6abbb88c485cab4c957c2ef6 ts=2026-09-24T12:55:33.069Z`; `6aa413b141b41dbac0c7f1f1.jsonl[839] _id=6abbb88c485cab4c957c2f04 ts=2026-09-24T12:56:40.745Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 43 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 43} 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[1] _id=6ab3ce8d485cab4c954b84fc ts=2026-09-23T13:05:17.9510000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[322] _id=6abbb845485cab4c957c273a ts=2026-09-23T13:08:09.916Z`; `6aa413b141b41dbac0c7f1f1.jsonl[627] _id=6abbb872485cab4c957c2bc6 ts=2026-09-23T13:22:43.549Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[328] _id=6abbb845485cab4c957c2736 ts=2026-09-23T13:08:09.091Z`; `6aa413b141b41dbac0c7f1f1.jsonl[626] _id=6abbb872485cab4c957c2bc4 ts=2026-09-23T13:22:42.436Z`; `6aa413b141b41dbac0c7f1f1.jsonl[21] _id=6ab6718d485cab4c9554682b ts=2026-09-25T13:05:17.1690000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 47 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[287] _id=6ab676f7485cab4c9554fa51 ts=2026-09-25T13:28:23.4610000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[1469] _id=6abbba5b485cab4c957c71ae ts=2026-09-29T13:17:15.0680000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[1475] _id=6abbba76485cab4c957c77ea ts=2026-09-29T13:17:42.2160000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4015 | 0.0 | 0.034 | 259.694 | 1.056 | 344652.923 | 0.23 | 2375 | 6 |
| InputEvent | 2057 | 0.0 | 1.089 | 591.507 | 17.447 | 344428.195 | 0.1 | 127 | 16 |
| PlayerPositionEvent | 2007 | 9.291 | 9.999 | 521.629 | 10.027 | 344269.165 | 0.12 | 0 | 10 |
| DialogueEvent | 788 | 0.001 | 6.47 | 1544.611 | 114.351 | 344392.5 | 0.04 | 202 | 12 |
| ObjectInterEvent | 75 | 0.035 | 10.043 | 16219.191 | 86797.46 | 344767.49 | 0.0 | 2 | 9 |
| TopographicMapEvent | 46 | 0.02 | 10.584 | 22649.197 | 89778.033 | 346390.347 | 0.0 | 3 | 7 |
| questEvent | 44 | 0.002 | 363.858 | 27624.292 | 86587.985 | 345237.722 | 0.0 | 6 | 20 |
| gameWindowFocusEvent | 42 | 1.863 | 459.369 | 28948.902 | 85980.318 | 345356.173 | 0.0 | 0 | 18 |
| Soil Key Puzzle | 31 | 0.211 | 0.892 | 16878.352 | 18.632 | 523150.704 | 0.0 | 0 | 1 |
| gameWindowUnfocusEvent | 26 | 1.273 | 544.851 | 46747.524 | 296423.795 | 345391.981 | 0.0 | 0 | 13 |
| DEBUGMenu | 22 | 10.474 | 2815.61 | 55311.594 | 326572.054 | 345803.133 | 0.0 | 0 | 16 |
| gameStartEvent | 18 | 67.676 | 6310.87 | 67524.493 | 340195.494 | 345809.473 | 0.0 | 0 | 15 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[16] _id=6ab67187485cab4c95546809 ts=2026-09-25T13:05:11.0480000Z == 6aa413b141b41dbac0c7f1f1.jsonl[17] _id=6ab67187485cab4c95546811 ts=2026-09-25T13:05:11.0480000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[5385] _id=6abe72cc485cab4c95a95d28 ts=2026-10-01T14:48:43.5450000Z == 6aa413b141b41dbac0c7f1f1.jsonl[5366] _id=6abe72cd485cab4c95a95d2e ts=2026-10-01T14:48:43.5450000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 118 group(s), 180 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[222] _id=6ab676e5485cab4c9554f722 ts=2026-09-25T13:28:04.5810000Z == 6aa413b141b41dbac0c7f1f1.jsonl[260] _id=6ab676e5485cab4c9554f724 ts=2026-09-25T13:28:04.5810000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[283] _id=6ab676e8485cab4c9554f7d4 ts=2026-09-25T13:28:07.9660000Z == 6aa413b141b41dbac0c7f1f1.jsonl[284] _id=6ab676e9485cab4c9554f7da ts=2026-09-25T13:28:07.9660000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[269] _id=6ab676f3485cab4c9554f99f ts=2026-09-25T13:28:18.7250000Z == 6aa413b141b41dbac0c7f1f1.jsonl[259] _id=6ab676f3485cab4c9554f9a6 ts=2026-09-25T13:28:18.7250000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[12] _id=6ab67187485cab4c955467ff ts=? == 6aa413b141b41dbac0c7f1f1.jsonl[4257] _id=6abe5a72485cab4c95a429e6 ts=?`; `6aa413b141b41dbac0c7f1f1.jsonl[3955] _id=6abd21ea485cab4c958b815d ts=? == 6aa413b141b41dbac0c7f1f1.jsonl[5380] _id=6abe72cb485cab4c95a95cfc ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `917ms: 6aa413b141b41dbac0c7f1f1.jsonl[452] _id=6abbb85f485cab4c957c29a4 ts=2026-09-23T13:17:41.544Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[453] _id=6abbb85f485cab4c957c29aa ts=2026-09-23T13:17:42.461Z`; `35ms: 6aa413b141b41dbac0c7f1f1.jsonl[769] _id=6abbb87f485cab4c957c2d2c ts=2026-09-23T13:25:06.07Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[760] _id=6abbb87f485cab4c957c2d30 ts=2026-09-23T13:25:06.105Z`; `64ms: 6aa413b141b41dbac0c7f1f1.jsonl[1012] _id=6abbb896485cab4c957c307c ts=2026-09-24T12:58:58.932Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[1009] _id=6abbb896485cab4c957c3086 ts=2026-09-24T12:58:58.996Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 453 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `263ms: 6aa413b141b41dbac0c7f1f1.jsonl[254] _id=6ab676e6485cab4c9554f762 ts=2026-09-25T13:28:05.2050000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[255] _id=6ab676e6485cab4c9554f764 ts=2026-09-25T13:28:05.4680000Z`; `26ms: 6aa413b141b41dbac0c7f1f1.jsonl[255] _id=6ab676e6485cab4c9554f764 ts=2026-09-25T13:28:05.4680000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[256] _id=6ab676e6485cab4c9554f768 ts=2026-09-25T13:28:05.4940000Z`; `770ms: 6aa413b141b41dbac0c7f1f1.jsonl[279] _id=6ab676e7485cab4c9554f7a2 ts=2026-09-25T13:28:05.9720000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[280] _id=6ab676e7485cab4c9554f7ab ts=2026-09-25T13:28:06.7420000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa413b141b41dbac0c7f1f1.jsonl[3864] _id=6abd0f3e485cab4c95883679 ts=2026-09-30T13:31:41.9430000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[3871] _id=6abd0f3e485cab4c958836a7 ts=2026-09-30T13:31:41.9630000Z`; `52ms: 6aa413b141b41dbac0c7f1f1.jsonl[4371] _id=6abe5bb5485cab4c95a45de5 ts=2026-10-01T13:10:13.5490000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[4369] _id=6abe5bb6485cab4c95a45e01 ts=2026-10-01T13:10:13.6010000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6aa413b141b41dbac0c7f1f1.jsonl[3958] _id=6abd21ea485cab4c958b81a9 ts=2026-09-30T14:51:21.7220000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[3959] _id=6abd21eb485cab4c958b81ae ts=2026-09-30T14:51:21.7570000Z`; `46ms: 6aa413b141b41dbac0c7f1f1.jsonl[4251] _id=6abe5a6c485cab4c95a42941 ts=2026-10-01T13:04:46.4860000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[4252] _id=6abe5a6c485cab4c95a42949 ts=2026-10-01T13:04:46.5320000Z`; `3ms: 6aa413b141b41dbac0c7f1f1.jsonl[5393] _id=6abe72cd485cab4c95a95d44 ts=2026-10-01T14:48:43.5710000Z ~ 6aa413b141b41dbac0c7f1f1.jsonl[5394] _id=6abe72cd485cab4c95a95d46 ts=2026-10-01T14:48:43.5740000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1f1.jsonl[9] _id=6ab67180485cab4c955467c3 ts=2026-09-25T13:05:04.9350000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1381] _id=6abbb8b1485cab4c957c360c ts=2026-09-29T13:08:28.0680000Z; 94h 13m: 6aa413b141b41dbac0c7f1f1.jsonl[5377] _id=6abe72c5485cab4c95a95c58 ts=2026-10-01T14:48:37.8580000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5612] _id=6ac39fd5de269131f9a84470 ts=2026-10-05T13:02:14.1990000Z; 23h 58m: 6aa413b141b41dbac0c7f1f1.jsonl[5612] _id=6ac39fd5de269131f9a84470 ts=2026-10-05T13:02:14.1990000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7372] _id=6ac4f111de269131f9b001dc ts=2026-10-06T13:01:04.7960000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 39m 
  - Evidence: 95h 39m: 6aa413b141b41dbac0c7f1f1.jsonl[294] _id=6ab67733485cab4c9555055e ts=2026-09-25T13:29:23.6530000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1388] _id=6abbb8b3485cab4c957c366a ts=2026-09-29T13:09:16.1530000Z; 94h 13m: 6aa413b141b41dbac0c7f1f1.jsonl[5378] _id=6abe733c485cab4c95a96c52 ts=2026-10-01T14:50:36.7940000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5750] _id=6ac3a039de269131f9a84aaf ts=2026-10-05T13:03:54.3280000Z; 23h 49m: 6aa413b141b41dbac0c7f1f1.jsonl[7742] _id=6ac4fa03de269131f9b10571 ts=2026-10-06T13:39:15.7970000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7776] _id=6ac64921de269131f9b9253e ts=2026-10-07T13:29:05.7170000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 202 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f1.jsonl[4149] _id=6abd2621485cab4c958bc307 ts=2026-09-30T15:09:21.4080000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[4150] _id=6abd2621485cab4c958bc30b ts=2026-09-30T15:09:21.4090000Z; 1ms: 6aa413b141b41dbac0c7f1f1.jsonl[7138] _id=6ac3a43ede269131f9a8b179 ts=2026-10-05T13:21:02.3700000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7137] _id=6ac3a43ede269131f9a8b182 ts=2026-10-05T13:21:02.3710000Z; 2ms: 6aa413b141b41dbac0c7f1f1.jsonl[139] _id=6ab673eb485cab4c955490f9 ts=2026-09-25T13:15:23.6310000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[140] _id=6ab673eb485cab4c955490fd ts=2026-09-25T13:15:23.6330000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 6aa413b141b41dbac0c7f1f1.jsonl[253] _id=6ab676e6485cab4c9554f756 ts=2026-09-25T13:28:06.2260000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1325] _id=6abbb8b1485cab4c957c3614 ts=2026-09-29T13:08:34.4210000Z; 94h 13m: 6aa413b141b41dbac0c7f1f1.jsonl[5458] _id=6abe72e1485cab4c95a96024 ts=2026-10-01T14:49:05.5740000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5622] _id=6ac39ff0de269131f9a84632 ts=2026-10-05T13:02:40.7730000Z; 23h 56m: 6aa413b141b41dbac0c7f1f1.jsonl[7734] _id=6ac4f978de269131f9b0ea3e ts=2026-10-06T13:36:56.6490000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7813] _id=6ac64a2ade269131f9b96bdc ts=2026-10-07T13:33:30.2510000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 127 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f1.jsonl[16] _id=6ab67187485cab4c95546809 ts=2026-09-25T13:05:11.0480000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[17] _id=6ab67187485cab4c95546811 ts=2026-09-25T13:05:11.0480000Z; 0ms: 6aa413b141b41dbac0c7f1f1.jsonl[5385] _id=6abe72cc485cab4c95a95d28 ts=2026-10-01T14:48:43.5450000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5366] _id=6abe72cd485cab4c95a95d2e ts=2026-10-01T14:48:43.5450000Z; 1ms: 6aa413b141b41dbac0c7f1f1.jsonl[10] _id=6ab67187485cab4c95546807 ts=2026-09-25T13:05:11.0470000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[16] _id=6ab67187485cab4c95546809 ts=2026-09-25T13:05:11.0480000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 46m 
  - Evidence: 95h 46m: 6aa413b141b41dbac0c7f1f1.jsonl[218] _id=6ab67658485cab4c9554e182 ts=2026-09-25T13:25:44.2230000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1418] _id=6abbb917485cab4c957c4198 ts=2026-09-29T13:11:51.7130000Z; 95h 34m: 6aa413b141b41dbac0c7f1f1.jsonl[5233] _id=6abe6284485cab4c95a66057 ts=2026-10-01T13:39:16.2390000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[6148] _id=6ac3a27bde269131f9a872f8 ts=2026-10-05T13:13:31.4710000Z; 49h 40m: 6aa413b141b41dbac0c7f1f1.jsonl[7003] _id=6ac3a301de269131f9a8828a ts=2026-10-05T13:15:45.6280000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7977] _id=6ac65da9de269131f9bb4203 ts=2026-10-07T14:56:41.4160000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.035s..0.047s shown 
  - Evidence: 35ms: 6aa413b141b41dbac0c7f1f1.jsonl[769] _id=6abbb87f485cab4c957c2d2c ts=2026-09-23T13:25:06.07Z -> 6aa413b141b41dbac0c7f1f1.jsonl[760] _id=6abbb87f485cab4c957c2d30 ts=2026-09-23T13:25:06.105Z; 47ms: 6aa413b141b41dbac0c7f1f1.jsonl[1104] _id=6abbb89c485cab4c957c31e8 ts=2026-09-24T13:07:09.989Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1105] _id=6abbb89c485cab4c957c31ec ts=2026-09-24T13:07:10.036Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa413b141b41dbac0c7f1f1.jsonl[302] _id=6ab6777e485cab4c95550dfe ts=2026-09-25T13:30:38.9420000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1382] _id=6abbb8b1485cab4c957c3610 ts=2026-09-29T13:08:28.1070000Z; 93h 46m: 6aa413b141b41dbac0c7f1f1.jsonl[5583] _id=6abe7914485cab4c95a9ff96 ts=2026-10-01T15:15:32.0690000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5618] _id=6ac39fdcde269131f9a84500 ts=2026-10-05T13:02:14.2070000Z; 23h 20m: 6aa413b141b41dbac0c7f1f1.jsonl[7369] _id=6ac3a8d8de269131f9a997f1 ts=2026-10-05T13:40:40.2990000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7373] _id=6ac4f112de269131f9b001e0 ts=2026-10-06T13:01:04.8020000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 6aa413b141b41dbac0c7f1f1.jsonl[264] _id=6ab676f3485cab4c9554f9bc ts=2026-09-25T13:28:18.7250000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1630] _id=6abbbb40485cab4c957ca53f ts=2026-09-29T13:12:31.6480000Z; 94h 11m: 6aa413b141b41dbac0c7f1f1.jsonl[5356] _id=6abe732e485cab4c95a96a8a ts=2026-10-01T14:50:21.4430000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5621] _id=6ac39fddde269131f9a8450a ts=2026-10-05T13:02:20.5470000Z; 49h 37m: 6aa413b141b41dbac0c7f1f1.jsonl[7102] _id=6ac3a3dfde269131f9a89d58 ts=2026-10-05T13:19:27.4420000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7999] _id=6ac65dd2de269131f9bb46c5 ts=2026-10-07T14:57:22.5360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2375 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f1.jsonl[1499] _id=6abbbb2e485cab4c957c9f94 ts=2026-09-29T13:20:45.5780000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1512] _id=6abbbb2e485cab4c957c9f9a ts=2026-09-29T13:20:45.5780000Z; 0ms: 6aa413b141b41dbac0c7f1f1.jsonl[1500] _id=6abbbb2f485cab4c957c9fba ts=2026-09-29T13:20:45.7390000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1517] _id=6abbbb2f485cab4c957c9fbe ts=2026-09-29T13:20:45.7390000Z; 0ms: 6aa413b141b41dbac0c7f1f1.jsonl[1502] _id=6abbbb2e485cab4c957c9f92 ts=2026-09-29T13:20:45.5780000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1499] _id=6abbbb2e485cab4c957c9f94 ts=2026-09-29T13:20:45.5780000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 145h 19m 
  - Evidence: 145h 19m: 6aa413b141b41dbac0c7f1f1.jsonl[5086] _id=6abe621a485cab4c95a640f1 ts=2026-10-01T13:37:30.7070000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7976] _id=6ac65da9de269131f9bb41ff ts=2026-10-07T14:56:41.4110000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 13m 
  - Evidence: 96h 13m: 6aa413b141b41dbac0c7f1f1.jsonl[4798] _id=6abe5e94485cab4c95a51d1a ts=2026-10-01T13:22:28.4290000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7317] _id=6ac3a7aade269131f9a96031 ts=2026-10-05T13:35:38.7760000Z; 95h 48m: 6aa413b141b41dbac0c7f1f1.jsonl[287] _id=6ab676f7485cab4c9554fa51 ts=2026-09-25T13:28:23.4610000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1469] _id=6abbba5b485cab4c957c71ae ts=2026-09-29T13:17:15.0680000Z; 25h 16m: 6aa413b141b41dbac0c7f1f1.jsonl[7714] _id=6ac4f961de269131f9b0e365 ts=2026-10-06T13:36:33.0580000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7925] _id=6ac65cbcde269131f9bb3163 ts=2026-10-07T14:52:44.4470000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.020s..0.039s shown 
  - Evidence: 20ms: 6aa413b141b41dbac0c7f1f1.jsonl[3864] _id=6abd0f3e485cab4c95883679 ts=2026-09-30T13:31:41.9430000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[3871] _id=6abd0f3e485cab4c958836a7 ts=2026-09-30T13:31:41.9630000Z; 34ms: 6aa413b141b41dbac0c7f1f1.jsonl[3847] _id=6abd0f3d485cab4c9588366e ts=2026-09-30T13:31:41.9090000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[3864] _id=6abd0f3e485cab4c95883679 ts=2026-09-30T13:31:41.9430000Z; 39ms: 6aa413b141b41dbac0c7f1f1.jsonl[4370] _id=6abe5bb5485cab4c95a45ddf ts=2026-10-01T13:10:13.5100000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[4371] _id=6abe5bb5485cab4c95a45de5 ts=2026-10-01T13:10:13.5490000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1f1.jsonl[7] _id=6ab67172485cab4c955466de ts=2026-09-25T13:04:50.5050000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1380] _id=6abbb8b1485cab4c957c360a ts=2026-09-29T13:08:19.9780000Z; 94h 13m: 6aa413b141b41dbac0c7f1f1.jsonl[5365] _id=6abe72bd485cab4c95a95b45 ts=2026-10-01T14:48:29.5430000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5607] _id=6ac39fc2de269131f9a843ca ts=2026-10-05T13:01:54.3350000Z; 23h 55m: 6aa413b141b41dbac0c7f1f1.jsonl[5607] _id=6ac39fc2de269131f9a843ca ts=2026-10-05T13:01:54.3350000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7371] _id=6ac4f03bde269131f9affe07 ts=2026-10-06T12:57:31.0000000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 6aa413b141b41dbac0c7f1f1.jsonl[105] _id=6ab67337485cab4c9554855f ts=2026-09-25T13:12:23.7520000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1379] _id=6abbb8b1485cab4c957c3605 ts=2026-09-29T13:08:19.9250000Z; 93h 46m: 6aa413b141b41dbac0c7f1f1.jsonl[5585] _id=6abe7916485cab4c95a9ffe2 ts=2026-10-01T15:15:34.4160000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5609] _id=6ac39fc1de269131f9a843c8 ts=2026-10-05T13:01:54.3340000Z; 23h 53m: 6aa413b141b41dbac0c7f1f1.jsonl[5755] _id=6ac3a04ede269131f9a84c4a ts=2026-10-05T13:04:15.3630000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7370] _id=6ac4f03bde269131f9affe05 ts=2026-10-06T12:57:30.9990000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 6aa413b141b41dbac0c7f1f1.jsonl[104] _id=6ab6732a485cab4c955484a6 ts=2026-09-25T13:12:10.2430000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1368] _id=6abbb8b2485cab4c957c361b ts=2026-09-29T13:08:42.2240000Z; 93h 53m: 6aa413b141b41dbac0c7f1f1.jsonl[5578] _id=6abe780d485cab4c95a9e01f ts=2026-10-01T15:11:09.4790000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5753] _id=6ac3a049de269131f9a84bbe ts=2026-10-05T13:04:09.6280000Z; 47h 42m: 6aa413b141b41dbac0c7f1f1.jsonl[626] _id=6abbb872485cab4c957c2bc4 ts=2026-09-23T13:22:42.436Z -> 6aa413b141b41dbac0c7f1f1.jsonl[21] _id=6ab6718d485cab4c9554682b ts=2026-09-25T13:05:17.1690000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa413b141b41dbac0c7f1f1.jsonl[122] _id=6ab673bc485cab4c95548e87 ts=2026-09-25T13:14:36.7970000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[1367] _id=6abbb8b2485cab4c957c3617 ts=2026-09-29T13:08:34.5190000Z; 94h 13m: 6aa413b141b41dbac0c7f1f1.jsonl[5372] _id=6abe72cd485cab4c95a95d4d ts=2026-10-01T14:48:43.5760000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5617] _id=6ac39fddde269131f9a84502 ts=2026-10-05T13:02:20.1360000Z; 24h 5m: 6aa413b141b41dbac0c7f1f1.jsonl[7511] _id=6ac4f72ade269131f9b08872 ts=2026-10-06T13:27:10.1530000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[7802] _id=6ac649e3de269131f9b95709 ts=2026-10-07T13:32:19.2070000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1f1.jsonl[5394] _id=6abe72cd485cab4c95a95d46 ts=2026-10-01T14:48:43.5740000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5372] _id=6abe72cd485cab4c95a95d4d ts=2026-10-01T14:48:43.5760000Z; 3ms: 6aa413b141b41dbac0c7f1f1.jsonl[5393] _id=6abe72cd485cab4c95a95d44 ts=2026-10-01T14:48:43.5710000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5394] _id=6abe72cd485cab4c95a95d46 ts=2026-10-01T14:48:43.5740000Z; 3ms: 6aa413b141b41dbac0c7f1f1.jsonl[5619] _id=6ac39fddde269131f9a84504 ts=2026-10-05T13:02:20.1400000Z -> 6aa413b141b41dbac0c7f1f1.jsonl[5620] _id=6ac39fddde269131f9a84508 ts=2026-10-05T13:02:20.1430000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[7060] _id=6ac3a3c7de269131f9a898da ts=2026-10-05T13:19:03.2240000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[7210] _id=6ac3a5bcde269131f9a906c9 ts=2026-10-05T13:27:24.8940000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 70 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[1937] _id=6abbbbec485cab4c957cd23e ts=2026-09-29T13:23:53.7080000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[2242] _id=6abbbc6c485cab4c957ce9ca ts=2026-09-29T13:26:03.2660000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[2364] _id=6abbbc72485cab4c957cebc4 ts=2026-09-29T13:26:07.6290000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 195 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[255] _id=6ab676e6485cab4c9554f764 ts=2026-09-25T13:28:05.4680000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[256] _id=6ab676e6485cab4c9554f768 ts=2026-09-25T13:28:05.4940000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[274] _id=6ab676e9485cab4c9554f7ea ts=2026-09-25T13:28:07.9660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[657] _id=6abbb871485cab4c957c2bb2 ts=2026-09-23T13:22:30.494Z`; `6aa413b141b41dbac0c7f1f1.jsonl[784] _id=6abbb881485cab4c957c2d94 ts=2026-09-23T13:27:40.684Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 9 records 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[3] _id=6ab3cef9485cab4c954b8628 ts=?`; `6aa413b141b41dbac0c7f1f1.jsonl[12] _id=6ab67187485cab4c955467ff ts=?`; `6aa413b141b41dbac0c7f1f1.jsonl[3955] _id=6abd21ea485cab4c958b815d ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 324 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[2188] _id=6abbbc69485cab4c957ce8dc ts=2026-09-29T13:26:00.7620000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[2232] _id=6abbbc6b485cab4c957ce933 ts=2026-09-29T13:26:01.2310000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[2227] _id=6abbbc6b485cab4c957ce941 ts=2026-09-29T13:26:01.6630000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 716 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[260] _id=6ab676e5485cab4c9554f724 ts=2026-09-25T13:28:04.5810000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[240] _id=6ab676e5485cab4c9554f735 ts=2026-09-25T13:28:04.9450000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[261] _id=6ab676e5485cab4c9554f73a ts=2026-09-25T13:28:04.9810000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 22 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[1469] _id=6abbba5b485cab4c957c71ae ts=2026-09-29T13:17:15.0680000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[2678] _id=6abd093d485cab4c95868fa1 ts=2026-09-30T13:06:05.5770000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[3844] _id=6abd0f3b485cab4c9588353e ts=2026-09-30T13:31:39.2100000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'DialogueStartEvent' (totals: 137 start, 128 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 84 unmatched 'BecameCameraCentered' (totals: 724 open, 710 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 107 unmatched 'BecameVisible' (totals: 1247 open, 1335 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'MapOpenEvent' (totals: 23 open, 18 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 27 unmatched 'questActiveEvent' (totals: 35 start, 10 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 295 of 9188 adjacent _id pairs reverse in client time; worst 174196.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f1.jsonl[302] _id=6ab6777e485cab4c95550dfe ts=2026-09-25T13:30:38.9420000Z`; `6aa413b141b41dbac0c7f1f1.jsonl[317] _id=6abbb843485cab4c957c2712 ts=2026-09-23T13:07:22.355Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.83s, min -518457.92s, max +3.65s over 9189 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f1\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `EndOfUnit` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=partial, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 9 records 
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

### `PuzzlePieceVisibleEvent` — 4016 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3066); Unit 4 Dev (950)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.06s, n=4015)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4016/4016 records)
    "BecameInvisible"  x1335
    "BecameVisible"  x1247
    "BecameCameraCentered"  x724
    "BecameCameraUncentered"  x710
data.pieceId  (string, 4016/4016 records)
    27 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4016/4016 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2058 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1229); Unit 1 Dev (480); Unit 4 Dev (169); Unit 3 Dev (158); Unit 4 Dev - Dungeon (22)
- **Intervals:** median 1.09s (p5 0.04s / p95 17.45s, n=2057)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2058/2058 records)
    "pressed"  x2058
data.actionType  (string, 2058/2058 records)
    "Move"  x1687
    "Interact"  x176
    "Jump"  x137
    "Hoverboard"  x27
    "Sprint"  x19
    "Map"  x10
    "SkipCinematic"  x2
data.key  (string, 2058/2058 records, 1 empty-string)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2058/2058 records)
    "Player"  x2058
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2014 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1300); Unit 1 Dev (399); Unit 4 Dev (162); Unit 3 Dev (116); Unit 4 Dev - Dungeon (37)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2007)
- **Fields under `data`:**

```text
data.position  (object, 2014/2014 records)
data.position.x  (number, 2014/2014 records)
    numeric range -106.241 .. 1669.09 (383 unique)
data.position.y  (number, 2014/2014 records)
    numeric range -85.415 .. 171.241 (278 unique)
data.position.z  (number, 2014/2014 records)
    numeric range -639.68 .. 1872.47 (383 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 789 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (567); Unit 1 Dev (134); Unit 4 Dev (45); Unit 3 Dev (24); Unit 4 Dev - Dungeon (19)
- **eventKey:** present on 524 of 789 records
- **Intervals:** median 6.47s (p5 0.01s / p95 114.35s, n=788)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x524; [conversationId, dialogueEventType] x265
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 789/789 records)
    numeric range 8 .. 102 (19 unique)
data.dialogueEventType  (string, 789/789 records)
    "DialogueNodeEvent"  x524
    "DialogueStartEvent"  x137
    "DialogueFinishEvent"  x128
data.nodeId  (number, 524/789 records)
    numeric range 0 .. 290 (136 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 76 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (51); Unit 1 Dev (12); Unit 4 Dev (8); Unit 4 Dev - Dungeon (5)
- **Intervals:** median 10.04s (p5 1.45s / p95 86797.46s, n=75)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "Press E to Pick up"  x20
    "Press E to Place"  x17
    "Press E to Insert"  x10
    "Press E to place"  x6
    "TalkTo"  x6
    "Press E to inspect "  x5
    "E to Talk"  x4
    "Press E to Install"  x3
    "Press E to Open Locker"  x2
    "Press E to Operate"  x2
    "Press E to use"  x1
data.objectName  (string, 76/76 records)
    30 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 47 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 3 Dev (18); Unit 4 Dev (2)
- **Intervals:** median 10.58s (p5 0.04s / p95 89778.03s, n=46)
- **`data` key-set variants:** [actionType, featureUsed] x41; [actionType, featureUsed, location] x5; [actionType, featureUsed, legendName] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "MapOpenEvent"  x23
    "MapCloseEvent"  x18
    "WaypointSetEvent"  x4
    "Selected"  x1
    "WaypointMoveEvent"  x1
data.featureUsed  (string, 47/47 records)
    "Map"  x41
    "Waypoint"  x5
    "Legend"  x1
data.legendName  (string, 1/47 records)
    "150 ft"  x1
data.location  (object, 5/47 records)
data.location.x  (number, 5/47 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/47 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/47 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 45 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 1 Dev (15); Unit 4 Dev (3); Unit 3 Dev (2)
- **eventKey:** present on 45 of 45 records
- **Intervals:** median 363.86s (p5 0.00s / p95 86587.98s, n=44)
- **`data` key-set variants:** [questEventType, questID, questName] x35; [questEventType, questID, questName, questSuccessOrFailure] x10
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 45/45 records)
    "questActiveEvent"  x35
    "questFinishEvent"  x10
data.questID  (string, 45/45 records)
    "23"  x8
    "24"  x8
    "31"  x7
    "21"  x5
    "29"  x5
    "22"  x3
    "32"  x3
    "39"  x3
    "16"  x2
    "25"  x1
data.questName  (string, 45/45 records)
    "Foraged Forging"  x8
    "Investigate the Temple"  x8
    "TK, Reporting In!"  x7
    "Escape the Ruin"  x5
    "Gear Up"  x5
    "Getting the Band Back Together"  x3
    "Info and Intros"  x3
    "Well, What Have We Here?"  x3
    "Supply Run"  x2
    "Which Watershed?"  x1
data.questSuccessOrFailure  (string, 10/45 records)
    "Succeeded"  x10
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 43 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (14); Unit 3 Dev (4); Unit 4 Dev (4); Unit 1 Dev (2)
- **Intervals:** median 459.37s (p5 4.30s / p95 85980.32s, n=42)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 43/43 records)
    true  x43
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 32 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 4 Dev (8)
- **Intervals:** median 0.89s (p5 0.25s / p95 18.63s, n=31)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x28; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/32 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/32 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 28/32 records)
    "RightDrag"  x16
    "LeftDrag"  x12
data.currentSoilType  (string, 28/32 records)
    "CLAY"  x5
    "CLAYROCK"  x5
    "CLAYSAND"  x5
    "SAND"  x5
    "SANDGRAVEL"  x4
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 28/32 records)
    "false"  x22
    "true"  x6
data.waterLevelStatus  (string, 28/32 records)
    "TooHigh"  x16
    "Proper"  x9
    "TooLow"  x3
data.waterRetentionChange  (string, 28/32 records)
    "Increase"  x16
    "Decrease"  x6
    "NoChange"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowUnfocusEvent` — 27 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (5); Unit 4 Dev (5); Unit 1 Dev (2)
- **Intervals:** median 544.85s (p5 2.88s / p95 296423.79s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    false  x27
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (5); Unit 4 Dev (4); MainMenu (3); Unit 3 Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2815.61s (p5 18.47s / p95 326572.05s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 6310.87s (p5 367.13s / p95 340195.49s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
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
    "A user gesture is required to request Pointer Lock."  x6
    "Permissions check failed"  x3
data.phase  (string, 9/9 records)
    "running"  x9
data.stack  (string, 9/9 records, 6 empty-string)
    ""  x6
    "TypeError: Permissions check failed"  x3
data.type  (string, 9/9 records)
    "unhandled_rejection"  x9
data.unitId  (string, 9/9 records)
    "unit2"  x5
    "unit4"  x2
    "unit1"  x1
    "unit3"  x1
data.workspace  (string, 9/9 records)
    "mhs"  x9
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `EndOfUnit` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationNodeEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : event type present in baseline 09-23-26 but absent now
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (24 records)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (1x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (5x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*