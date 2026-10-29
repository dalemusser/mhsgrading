# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f24e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f24e
- **Game version string(s) in log:** 2.8.1, 2.8.9, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f24e.jsonl
- **Records:** 13604 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f24e
- **Time span:** 2026-09-23T16:28:41.084000+00:00 .. 2026-10-07T17:07:29.561000+00:00 (336h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f24e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 13604 records, 5 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 91 INFO, 2 NOT_TESTED, 68 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `soilMachine`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5751 | 42.27 | 1 | 1 | 0 | 2026-09-25T16:47:03.426000+00:00 | 2026-10-05T16:39:35.696000+00:00 | 239h 52m |
| InputEvent | 3824 | 28.11 | 1 | 4 | 0 | 2026-09-23T16:30:41.412000+00:00 | 2026-10-07T17:06:02.958000+00:00 | 336h 35m |
| PlayerPositionEvent | 1899 | 13.96 | 1 | 4 | 0 | 2026-09-23T16:30:36.129000+00:00 | 2026-10-07T17:07:29.561000+00:00 | 336h 36m |
| DialogueEvent | 1235 | 9.08 | 1 | 4 | 828 | 2026-09-23T16:30:58.069000+00:00 | 2026-10-07T17:06:06.290000+00:00 | 336h 35m |
| argumentationNodeEvent | 264 | 1.94 | 1 | 2 | 0 | 2026-09-24T16:42:04.806000+00:00 | 2026-10-06T17:06:37.272000+00:00 | 288h 24m |
| ObjectInterEvent | 191 | 1.4 | 1 | 3 | 0 | 2026-09-23T16:38:09.496000+00:00 | 2026-10-06T16:45:46.930000+00:00 | 312h 7m |
| TopographicMapEvent | 174 | 1.28 | 1 | 3 | 0 | 2026-09-24T16:30:18.177000+00:00 | 2026-10-07T17:04:55.105000+00:00 | 312h 34m |
| questEvent | 59 | 0.43 | 1 | 3 | 59 | 2026-09-23T16:30:58.052000+00:00 | 2026-10-07T16:59:25.966000+00:00 | 336h 28m |
| gameWindowFocusEvent | 48 | 0.35 | 1 | 4 | 0 | 2026-09-23T16:28:41.084000+00:00 | 2026-10-07T17:05:35.836000+00:00 | 336h 36m |
| Soil Key Puzzle | 42 | 0.31 | 1 | 1 | 0 | 2026-09-25T17:00:53.206000+00:00 | 2026-09-30T16:47:39.724000+00:00 | 119h 46m |
| gameWindowUnfocusEvent | 37 | 0.27 | 1 | 4 | 0 | 2026-09-23T16:58:05.117000+00:00 | 2026-10-06T17:06:40.434000+00:00 | 312h 8m |
| DEBUGMenu | 19 | 0.14 | 1 | 5 | 0 | 2026-09-23T16:30:36.121000+00:00 | 2026-10-07T17:05:43.589000+00:00 | 336h 35m |
| DaniEvent | 18 | 0.13 | 1 | 3 | 0 | 2026-09-23T16:56:16.169000+00:00 | 2026-10-06T16:51:50.639000+00:00 | 311h 55m |
| gameStartEvent | 17 | 0.12 | 1 | 1 | 0 | 2026-09-23T16:28:41.084000+00:00 | 2026-10-07T17:05:35.836000+00:00 | 336h 36m |
| argumentationAnswerEvent | 10 | 0.07 | 1 | 2 | 0 | 2026-09-24T16:42:11.287000+00:00 | 2026-10-06T17:06:26.838000+00:00 | 288h 24m |
| argumentationEvent | 9 | 0.07 | 1 | 2 | 0 | 2026-09-24T16:41:31.192000+00:00 | 2026-10-06T17:04:43.332000+00:00 | 288h 23m |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |
| argumentationToolEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-09-24T16:46:05.965000+00:00 | 2026-10-06T17:05:03.444000+00:00 | 288h 18m |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-25T16:39:32.899000+00:00 | 2026-09-25T16:39:32.899000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 43514.655s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.051s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.231s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 77.803s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1037937.479s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84988.035s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 287.417s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 270.37s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
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
  - Observed: 150 ft; 210 ft; 240 ft; 270 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 1,; A,3,II; B,2,I; B,5,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 20 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[220] _id=6ab40122485cab4c954e7366 ts=2026-09-23T16:41:06.6690000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[552] _id=6ab40545485cab4c954e8ca8 ts=2026-09-23T16:58:45.1340000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[694] _id=6ab54c1c485cab4c9552e0eb ts=2026-09-24T16:13:16.1550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[9338] _id=6abe88c5485cab4c95abd8c6 ts=2026-10-01T16:22:29.0210000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[10207] _id=6abe9104485cab4c95ac36d0 ts=2026-10-01T16:57:38.5810000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[10853] _id=6ac3d058de269131f9adb5ad ts=2026-10-05T16:29:09.8300000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[9] _id=6ab3fe39485cab4c954e613e ts=2026-09-23T16:28:41.0840000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[631] _id=6ab54b4a485cab4c9552dda5 ts=2026-09-24T16:09:45.6700000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1024] _id=6ab551aa485cab4c95532251 ts=2026-09-24T16:36:58.4750000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 48 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 48} 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[8] _id=6ab3fe39485cab4c954e613c ts=2026-09-23T16:28:41.0840000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[540] _id=6ab4051d485cab4c954e8b66 ts=2026-09-23T16:58:05.4330000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[544] _id=6ab40520485cab4c954e8b82 ts=2026-09-23T16:58:08.6490000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 37 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 37} 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[538] _id=6ab4051d485cab4c954e8b60 ts=2026-09-23T16:58:05.1170000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[541] _id=6ab4051f485cab4c954e8b7c ts=2026-09-23T16:58:05.5890000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[529] _id=6ab4053e485cab4c954e8c84 ts=2026-09-23T16:58:39.0220000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 35 of 174 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[943] _id=6ab5501a485cab4c95531316 ts=2026-09-24T16:30:18.1770000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[944] _id=6ab5501d485cab4c95531361 ts=2026-09-24T16:30:21.9070000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1720] _id=6ab6a5af485cab4c955c8d9b ts=2026-09-25T16:47:43.5380000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5750 | 0.0 | 0.051 | 150.183 | 1.107 | 343542.941 | 0.4 | 2868 | 6 |
| InputEvent | 3823 | 0.0 | 0.602 | 316.956 | 11.109 | 343542.032 | 0.19 | 160 | 13 |
| PlayerPositionEvent | 1895 | 9.853 | 10.0 | 639.364 | 10.032 | 339903.924 | 0.09 | 0 | 12 |
| DialogueEvent | 1234 | 0.001 | 6.271 | 981.935 | 64.601 | 343307.964 | 0.06 | 336 | 11 |
| argumentationNodeEvent | 263 | 0.006 | 0.39 | 3947.804 | 9.655 | 952100.001 | 0.02 | 67 | 2 |
| ObjectInterEvent | 190 | 0.005 | 6.996 | 5913.986 | 504.211 | 343708.053 | 0.01 | 2 | 9 |
| TopographicMapEvent | 173 | 0.023 | 4.231 | 6504.491 | 662.923 | 432489.236 | 0.01 | 2 | 10 |
| questEvent | 58 | 0.001 | 257.202 | 20884.619 | 85622.254 | 343518.383 | 0.0 | 10 | 17 |
| gameWindowFocusEvent | 47 | 1.474 | 287.417 | 25783.293 | 87597.022 | 343894.078 | 0.0 | 0 | 16 |
| Soil Key Puzzle | 41 | 0.025 | 0.628 | 10517.232 | 7.057 | 431145.32 | 0.01 | 1 | 1 |
| gameWindowUnfocusEvent | 36 | 0.472 | 270.37 | 31214.314 | 148698.46 | 345707.009 | 0.0 | 0 | 13 |
| DEBUGMenu | 18 | 7.815 | 43514.655 | 67317.082 | 270975.63 | 343890.265 | 0.0 | 0 | 13 |
| DaniEvent | 17 | 0.86 | 8.25 | 66054.969 | 397118.419 | 605034.29 | 0.0 | 0 | 4 |
| gameStartEvent | 16 | 287.417 | 84988.035 | 75738.422 | 279555.182 | 343894.079 | 0.0 | 0 | 13 |
| argumentationAnswerEvent | 9 | 18.912 | 77.803 | 115361.728 | 605535.894 | 952134.623 | 0.0 | 0 | 2 |
| argumentationEvent | 8 | 50.266 | 86.872 | 129774.018 | 648828.356 | 952112.335 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationToolEvent | 1 | 1037937.479 | 1037937.479 | 1037937.479 | 1037937.479 | 1037937.479 | 0.0 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[13583] _id=6ac67be8de269131f9bd9322 ts=2026-10-07T17:05:44.2520000Z == 6aa4142c41b41dbac0c7f24e.jsonl[13584] _id=6ac67be8de269131f9bd9323 ts=2026-10-07T17:05:44.2520000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 151 group(s), 210 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[1694] _id=6ab6a59c485cab4c955c81ff ts=2026-09-25T16:47:24.7440000Z == 6aa4142c41b41dbac0c7f24e.jsonl[1700] _id=6ab6a59d485cab4c955c821b ts=2026-09-25T16:47:24.7440000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1698] _id=6ab6a59d485cab4c955c824b ts=2026-09-25T16:47:24.7440000Z == 6aa4142c41b41dbac0c7f24e.jsonl[1697] _id=6ab6a59d485cab4c955c825d ts=2026-09-25T16:47:24.7440000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1715] _id=6ab6a59f485cab4c955c8383 ts=2026-09-25T16:47:25.1390000Z == 6aa4142c41b41dbac0c7f24e.jsonl[1711] _id=6ab6a59f485cab4c955c8395 ts=2026-09-25T16:47:25.1390000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 47 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f24e.jsonl[189] _id=6ab40071485cab4c954e6f84 ts=2026-09-23T16:38:09.4960000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[185] _id=6ab40071485cab4c954e6f88 ts=2026-09-23T16:38:09.5020000Z`; `168ms: 6aa4142c41b41dbac0c7f24e.jsonl[364] _id=6ab4043a485cab4c954e83ae ts=2026-09-23T16:54:18.3210000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[370] _id=6ab4043a485cab4c954e83b4 ts=2026-09-23T16:54:18.4890000Z`; `158ms: 6aa4142c41b41dbac0c7f24e.jsonl[370] _id=6ab4043a485cab4c954e83b4 ts=2026-09-23T16:54:18.4890000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[371] _id=6ab4043a485cab4c954e83b8 ts=2026-09-23T16:54:18.6470000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 937 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `15ms: 6aa4142c41b41dbac0c7f24e.jsonl[1714] _id=6ab6a59f485cab4c955c8379 ts=2026-09-25T16:47:25.1240000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1715] _id=6ab6a59f485cab4c955c8383 ts=2026-09-25T16:47:25.1390000Z`; `18ms: 6aa4142c41b41dbac0c7f24e.jsonl[1711] _id=6ab6a59f485cab4c955c8395 ts=2026-09-25T16:47:25.1390000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1709] _id=6ab6a59f485cab4c955c83a6 ts=2026-09-25T16:47:25.1570000Z`; `391ms: 6aa4142c41b41dbac0c7f24e.jsonl[1779] _id=6ab6a619485cab4c955cc8ea ts=2026-09-25T16:49:27.9440000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1787] _id=6ab6a619485cab4c955cc8f7 ts=2026-09-25T16:49:28.3350000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `991ms: 6aa4142c41b41dbac0c7f24e.jsonl[1731] _id=6ab6a5c3485cab4c955c9902 ts=2026-09-25T16:48:03.5980000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1734] _id=6ab6a5c4485cab4c955c9974 ts=2026-09-25T16:48:04.5890000Z`; `209ms: 6aa4142c41b41dbac0c7f24e.jsonl[4464] _id=6aba958c485cab4c956a8d10 ts=2026-09-28T16:27:56.8920000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[4458] _id=6aba958d485cab4c956a8d1a ts=2026-09-28T16:27:57.1010000Z`; `206ms: 6aa4142c41b41dbac0c7f24e.jsonl[4458] _id=6aba958d485cab4c956a8d1a ts=2026-09-28T16:27:57.1010000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[4468] _id=6aba958d485cab4c956a8d24 ts=2026-09-28T16:27:57.3070000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 37 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `250ms: 6aa4142c41b41dbac0c7f24e.jsonl[1084] _id=6ab552dc485cab4c95533b2d ts=2026-09-24T16:42:04.8060000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1089] _id=6ab552dc485cab4c95533b33 ts=2026-09-24T16:42:05.0560000Z`; `983ms: 6aa4142c41b41dbac0c7f24e.jsonl[1088] _id=6ab552dc485cab4c95533b2f ts=2026-09-24T16:42:04.8600000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1085] _id=6ab552dd485cab4c95533b55 ts=2026-09-24T16:42:05.8430000Z`; `34ms: 6aa4142c41b41dbac0c7f24e.jsonl[1086] _id=6ab552dd485cab4c95533b5c ts=2026-09-24T16:42:05.8770000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[1087] _id=6ab552dd485cab4c95533b61 ts=2026-09-24T16:42:05.9110000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `472ms: 6aa4142c41b41dbac0c7f24e.jsonl[538] _id=6ab4051d485cab4c954e8b60 ts=2026-09-23T16:58:05.1170000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[541] _id=6ab4051f485cab4c954e8b7c ts=2026-09-23T16:58:05.5890000Z`; `567ms: 6aa4142c41b41dbac0c7f24e.jsonl[10173] _id=6abe8be4485cab4c95ac12fa ts=2026-10-01T16:35:48.7240000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[10176] _id=6abe8be5485cab4c95ac1304 ts=2026-10-01T16:35:49.2910000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4142c41b41dbac0c7f24e.jsonl[9338] _id=6abe88c5485cab4c95abd8c6 ts=2026-10-01T16:22:29.0210000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[9330] _id=6abe88c5485cab4c95abd8ca ts=2026-10-01T16:22:29.0240000Z`; `3ms: 6aa4142c41b41dbac0c7f24e.jsonl[10207] _id=6abe9104485cab4c95ac36d0 ts=2026-10-01T16:57:38.5810000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[10218] _id=6abe9104485cab4c95ac36d4 ts=2026-10-01T16:57:38.5840000Z`; `3ms: 6aa4142c41b41dbac0c7f24e.jsonl[10853] _id=6ac3d058de269131f9adb5ad ts=2026-10-05T16:29:09.8300000Z ~ 6aa4142c41b41dbac0c7f24e.jsonl[10854] _id=6ac3d058de269131f9adb5af ts=2026-10-05T16:29:09.8330000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 6aa4142c41b41dbac0c7f24e.jsonl[10214] _id=6abe90fc485cab4c95ac3684 ts=2026-10-01T16:57:32.6430000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10833] _id=6ac3d04ede269131f9adb4a1 ts=2026-10-05T16:29:02.9080000Z; 71h 41m: 6aa4142c41b41dbac0c7f24e.jsonl[1572] _id=6ab6a41d485cab4c955b941c ts=2026-09-25T16:41:02.1320000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4353] _id=6aba945a485cab4c956a6ae7 ts=2026-09-28T16:22:50.4740000Z; 24h 30m: 6aa4142c41b41dbac0c7f24e.jsonl[11877] _id=6ac521a2de269131f9b501c7 ts=2026-10-06T16:28:18.9050000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13441] _id=6ac67a5dde269131f9bd6db2 ts=2026-10-07T16:59:09.7190000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 3m 
  - Evidence: 168h 3m: 6aa4142c41b41dbac0c7f24e.jsonl[6963] _id=6abbeb32485cab4c95815527 ts=2026-09-29T16:45:38.6560000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[12742] _id=6ac5269cde269131f9b561df ts=2026-10-06T16:49:32.9460000Z; 95h 52m: 6aa4142c41b41dbac0c7f24e.jsonl[2325] _id=6ab6a6a2485cab4c955ce465 ts=2026-09-25T16:51:46.6570000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[6927] _id=6abbead6485cab4c95812d44 ts=2026-09-29T16:44:06.1080000Z; 24h 21m: 6aa4142c41b41dbac0c7f24e.jsonl[913] _id=6ab5501e485cab4c9553137f ts=2026-09-24T16:30:22.7770000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[2311] _id=6ab6a697485cab4c955ce30d ts=2026-09-25T16:51:35.4420000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 6aa4142c41b41dbac0c7f24e.jsonl[10800] _id=6abe9349485cab4c95ac42dc ts=2026-10-01T17:07:21.3340000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10860] _id=6ac3d058de269131f9adb5a7 ts=2026-10-05T16:29:09.2980000Z; 71h 22m: 6aa4142c41b41dbac0c7f24e.jsonl[4336] _id=6ab6a92e485cab4c955d2681 ts=2026-09-25T17:02:38.7760000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4386] _id=6aba94e2485cab4c956a7c45 ts=2026-09-28T16:25:06.2910000Z; 23h 59m: 6aa4142c41b41dbac0c7f24e.jsonl[13434] _id=6ac52a99de269131f9b613b3 ts=2026-10-06T17:06:33.6060000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13592] _id=6ac67bfbde269131f9bd93f3 ts=2026-10-07T17:06:03.5890000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 336 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[10150] _id=6abe8ba9485cab4c95ac11f2 ts=2026-10-01T16:34:49.5390000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10151] _id=6abe8ba9485cab4c95ac11f4 ts=2026-10-01T16:34:49.5400000Z; 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[10157] _id=6abe8bbf485cab4c95ac1267 ts=2026-10-01T16:35:11.2820000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10160] _id=6abe8bbf485cab4c95ac126a ts=2026-10-01T16:35:11.2830000Z; 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[10167] _id=6abe8bd3485cab4c95ac12be ts=2026-10-01T16:35:31.6810000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10168] _id=6abe8bd3485cab4c95ac12c0 ts=2026-10-01T16:35:31.6820000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4142c41b41dbac0c7f24e.jsonl[10763] _id=6abe925f485cab4c95ac4016 ts=2026-10-01T17:03:27.2100000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10838] _id=6ac3d056de269131f9adb555 ts=2026-10-05T16:29:09.2420000Z; 71h 20m: 6aa4142c41b41dbac0c7f24e.jsonl[4329] _id=6ab6a917485cab4c955d247d ts=2026-09-25T17:02:15.1450000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4355] _id=6aba9461485cab4c956a6b7e ts=2026-09-28T16:22:56.6720000Z; 24h 0m: 6aa4142c41b41dbac0c7f24e.jsonl[13222] _id=6ac528cfde269131f9b5cd63 ts=2026-10-06T16:58:55.7210000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13454] _id=6ac67a8bde269131f9bd72b6 ts=2026-10-07T16:59:55.5220000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 160 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24e.jsonl[13583] _id=6ac67be8de269131f9bd9322 ts=2026-10-07T17:05:44.2520000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13584] _id=6ac67be8de269131f9bd9323 ts=2026-10-07T17:05:44.2520000Z; 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[10838] _id=6ac3d056de269131f9adb555 ts=2026-10-05T16:29:09.2420000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10839] _id=6ac3d056de269131f9adb557 ts=2026-10-05T16:29:09.2430000Z; 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[10839] _id=6ac3d056de269131f9adb557 ts=2026-10-05T16:29:09.2430000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10850] _id=6ac3d056de269131f9adb559 ts=2026-10-05T16:29:09.2440000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4142c41b41dbac0c7f24e.jsonl[10730] _id=6abe925a485cab4c95ac3ff2 ts=2026-10-01T17:03:22.4360000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10988] _id=6ac3d0f6de269131f9adc063 ts=2026-10-05T16:31:50.4890000Z; 71h 25m: 6aa4142c41b41dbac0c7f24e.jsonl[4268] _id=6ab6a8c5485cab4c955d183f ts=2026-09-25T17:00:53.2090000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4409] _id=6aba951d485cab4c956a814c ts=2026-09-28T16:26:05.5170000Z; 48h 9m: 6aa4142c41b41dbac0c7f24e.jsonl[6014] _id=6aba97ec485cab4c956abdbf ts=2026-09-28T16:38:04.9050000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[7910] _id=6abd3d14485cab4c958e9acc ts=2026-09-30T16:47:16.2120000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.005s..0.006s shown 
  - Evidence: 5ms: 6aa4142c41b41dbac0c7f24e.jsonl[666] _id=6ab54bad485cab4c9552dee9 ts=2026-09-24T16:11:24.9340000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[667] _id=6ab54bad485cab4c9552deeb ts=2026-09-24T16:11:24.9390000Z; 6ms: 6aa4142c41b41dbac0c7f24e.jsonl[189] _id=6ab40071485cab4c954e6f84 ts=2026-09-23T16:38:09.4960000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[185] _id=6ab40071485cab4c954e6f88 ts=2026-09-23T16:38:09.5020000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 94h 25m 
  - Evidence: 94h 25m: 6aa4142c41b41dbac0c7f24e.jsonl[11837] _id=6ac5206bde269131f9b4f3a3 ts=2026-10-01T18:03:58.992Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10849] _id=6ac3d056de269131f9adb553 ts=2026-10-05T16:29:02.9160000Z; 71h 18m: 6aa4142c41b41dbac0c7f24e.jsonl[4346] _id=6ab6a996485cab4c955d34f3 ts=2026-09-25T17:04:22.1360000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4357] _id=6aba9461485cab4c956a6b7a ts=2026-09-28T16:22:50.4810000Z; 23h 52m: 6aa4142c41b41dbac0c7f24e.jsonl[13439] _id=6ac52a9bde269131f9b613cb ts=2026-10-06T17:06:35.1640000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13446] _id=6ac67a6ede269131f9bd6f86 ts=2026-10-07T16:59:21.1970000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4142c41b41dbac0c7f24e.jsonl[10768] _id=6abe925f485cab4c95ac4022 ts=2026-10-01T17:03:26.3900000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10861] _id=6ac3d058de269131f9adb5b1 ts=2026-10-05T16:29:09.3310000Z; 71h 27m: 6aa4142c41b41dbac0c7f24e.jsonl[4182] _id=6ab6a869485cab4c955d0ebf ts=2026-09-25T16:59:20.9070000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4530] _id=6aba95d2485cab4c956a963d ts=2026-09-28T16:26:46.6190000Z; 48h 0m: 6aa4142c41b41dbac0c7f24e.jsonl[5977] _id=6aba97c2485cab4c956abc97 ts=2026-09-28T16:37:21.7120000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[7612] _id=6abd3ad7485cab4c958e0a3c ts=2026-09-30T16:37:43.5970000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2868 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24e.jsonl[10061] _id=6abe8b06485cab4c95ac0a9c ts=2026-10-01T16:32:05.9520000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10062] _id=6abe8b06485cab4c95ac0a9e ts=2026-10-01T16:32:05.9520000Z; 0ms: 6aa4142c41b41dbac0c7f24e.jsonl[10066] _id=6abe8b06485cab4c95ac0aaa ts=2026-10-01T16:32:06.3140000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10069] _id=6abe8b06485cab4c95ac0aac ts=2026-10-01T16:32:06.3140000Z; 0ms: 6aa4142c41b41dbac0c7f24e.jsonl[10209] _id=6abe9104485cab4c95ac36dc ts=2026-10-01T16:57:38.9090000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10220] _id=6abe9104485cab4c95ac36de ts=2026-10-01T16:57:38.9090000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6aa4142c41b41dbac0c7f24e.jsonl[4292] _id=6ab6a8ea485cab4c955d1d65 ts=2026-09-25T17:01:30.8900000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[7912] _id=6abd3d14485cab4c958e9ac8 ts=2026-09-30T16:47:16.2100000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.025s..0.025s shown 
  - Evidence: 25ms: 6aa4142c41b41dbac0c7f24e.jsonl[4263] _id=6ab6a8c5485cab4c955d1839 ts=2026-09-25T17:00:53.2060000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4270] _id=6ab6a8c5485cab4c955d1843 ts=2026-09-25T17:00:53.2310000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 120h 8m 
  - Evidence: 120h 8m: 6aa4142c41b41dbac0c7f24e.jsonl[7872] _id=6abd3cc5485cab4c958e9420 ts=2026-09-30T16:45:57.4930000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[11693] _id=6ac3d62ede269131f9ae349d ts=2026-10-05T16:54:06.7290000Z; 71h 32m: 6aa4142c41b41dbac0c7f24e.jsonl[3512] _id=6ab6a78a485cab4c955d0057 ts=2026-09-25T16:55:38.0660000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4466] _id=6aba958b485cab4c956a8cec ts=2026-09-28T16:27:55.6000000Z; 24h 17m: 6aa4142c41b41dbac0c7f24e.jsonl[944] _id=6ab5501d485cab4c95531361 ts=2026-09-24T16:30:21.9070000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1720] _id=6ab6a5af485cab4c955c8d9b ts=2026-09-25T16:47:43.5380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.042s shown 
  - Evidence: 23ms: 6aa4142c41b41dbac0c7f24e.jsonl[6867] _id=6abbea63485cab4c958102ee ts=2026-09-29T16:42:10.9680000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[6868] _id=6abbea63485cab4c958102f5 ts=2026-09-29T16:42:10.9910000Z; 42ms: 6aa4142c41b41dbac0c7f24e.jsonl[6868] _id=6abbea63485cab4c958102f5 ts=2026-09-29T16:42:10.9910000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[6866] _id=6abbea63485cab4c95810309 ts=2026-09-29T16:42:11.0330000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 264h 28m 
  - Evidence: 264h 28m: 6aa4142c41b41dbac0c7f24e.jsonl[1451] _id=6ab6a2fa485cab4c955ad162 ts=2026-09-25T16:36:10.9750000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13325] _id=6ac52a41de269131f9b60f17 ts=2026-10-06T17:05:05.5980000Z; 23h 47m: 6aa4142c41b41dbac0c7f24e.jsonl[1240] _id=6ab553d3485cab4c95534a97 ts=2026-09-24T16:46:11.8740000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1391] _id=6ab6a259485cab4c955a692f ts=2026-09-25T16:33:29.6750000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 264h 28m 
  - Evidence: 264h 28m: 6aa4142c41b41dbac0c7f24e.jsonl[1453] _id=6ab6a2fa485cab4c955ad171 ts=2026-09-25T16:36:10.9970000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13311] _id=6ac52a2bde269131f9b60ced ts=2026-10-06T17:04:43.3320000Z; 23h 46m: 6aa4142c41b41dbac0c7f24e.jsonl[1241] _id=6ab553d3485cab4c95534a99 ts=2026-09-24T16:46:11.8950000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1371] _id=6ab6a226485cab4c955a455a ts=2026-09-25T16:32:38.5770000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 264h 28m 
  - Evidence: 264h 28m: 6aa4142c41b41dbac0c7f24e.jsonl[1450] _id=6ab6a2f9485cab4c955ad091 ts=2026-09-25T16:36:09.9510000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13282] _id=6ac52a1dde269131f9b60ba7 ts=2026-10-06T17:04:29.9520000Z; 23h 44m: 6aa4142c41b41dbac0c7f24e.jsonl[1239] _id=6ab553d2485cab4c95534a8d ts=2026-09-24T16:46:10.5360000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1351] _id=6ab6a1a7485cab4c9559f36e ts=2026-09-25T16:30:31.7480000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 67 interval(s) ≤ 0.006s..0.020s shown 
  - Evidence: 6ms: 6aa4142c41b41dbac0c7f24e.jsonl[13298] _id=6ac52a20de269131f9b60bd9 ts=2026-10-06T17:04:32.4540000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13299] _id=6ac52a20de269131f9b60bdb ts=2026-10-06T17:04:32.4600000Z; 16ms: 6aa4142c41b41dbac0c7f24e.jsonl[1382] _id=6ab6a252485cab4c955a6421 ts=2026-09-25T16:33:22.8880000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1383] _id=6ab6a252485cab4c955a642d ts=2026-09-25T16:33:22.9040000Z; 20ms: 6aa4142c41b41dbac0c7f24e.jsonl[1186] _id=6ab55380485cab4c955347c1 ts=2026-09-24T16:44:49.1040000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1180] _id=6ab55381485cab4c955347c3 ts=2026-09-24T16:44:49.1240000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 288h 18m 
  - Evidence: 288h 18m: 6aa4142c41b41dbac0c7f24e.jsonl[1234] _id=6ab553cd485cab4c95534a49 ts=2026-09-24T16:46:05.9650000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13339] _id=6ac52a3fde269131f9b60eff ts=2026-10-06T17:05:03.4440000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 6aa4142c41b41dbac0c7f24e.jsonl[10212] _id=6abe90f0485cab4c95ac3658 ts=2026-10-01T16:57:20.7630000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10832] _id=6ac3d046de269131f9adb434 ts=2026-10-05T16:28:54.8420000Z; 71h 41m: 6aa4142c41b41dbac0c7f24e.jsonl[1571] _id=6ab6a413485cab4c955b8d5f ts=2026-09-25T16:40:52.0390000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4351] _id=6aba9451485cab4c956a6a26 ts=2026-09-28T16:22:40.9220000Z; 24h 31m: 6aa4142c41b41dbac0c7f24e.jsonl[11871] _id=6ac5218bde269131f9b50107 ts=2026-10-06T16:27:54.9590000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13443] _id=6ac67a5ede269131f9bd6dbb ts=2026-10-07T16:59:10.1930000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 6aa4142c41b41dbac0c7f24e.jsonl[10213] _id=6abe90f0485cab4c95ac3656 ts=2026-10-01T16:57:20.7630000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10831] _id=6ac3d046de269131f9adb42f ts=2026-10-05T16:28:54.8410000Z; 71h 41m: 6aa4142c41b41dbac0c7f24e.jsonl[1570] _id=6ab6a413485cab4c955b8d53 ts=2026-09-25T16:40:52.0370000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4352] _id=6aba9450485cab4c956a6a20 ts=2026-09-28T16:22:40.9210000Z; 24h 29m: 6aa4142c41b41dbac0c7f24e.jsonl[11904] _id=6ac52211de269131f9b507db ts=2026-10-06T16:30:09.2390000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13442] _id=6ac67a5ede269131f9bd6dba ts=2026-10-07T16:59:10.1930000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa4142c41b41dbac0c7f24e.jsonl[1051] _id=6ab55229485cab4c9553291f ts=2026-09-24T16:39:05.3950000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[6059] _id=6aba9894485cab4c956ac284 ts=2026-09-28T16:40:52.4040000Z; 94h 32m: 6aa4142c41b41dbac0c7f24e.jsonl[11836] _id=6ac5206bde269131f9b4f3a1 ts=2026-10-01T18:03:57.166Z -> 6aa4142c41b41dbac0c7f24e.jsonl[11320] _id=6ac3d204de269131f9add7fd ts=2026-10-05T16:36:20.1630000Z; 23h 33m: 6aa4142c41b41dbac0c7f24e.jsonl[6479] _id=6aba9deb485cab4c956baf47 ts=2026-09-28T17:03:39.6050000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[6664] _id=6abbe93c485cab4c9580eaf9 ts=2026-09-29T16:37:16.5530000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 25m 
  - Evidence: 95h 25m: 6aa4142c41b41dbac0c7f24e.jsonl[10771] _id=6abe9277485cab4c95ac4072 ts=2026-10-01T17:03:51.4470000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[10853] _id=6ac3d058de269131f9adb5ad ts=2026-10-05T16:29:09.8300000Z; 71h 21m: 6aa4142c41b41dbac0c7f24e.jsonl[4316] _id=6ab6a900485cab4c955d2155 ts=2026-09-25T17:01:52.7870000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[4360] _id=6aba9461485cab4c956a6b8c ts=2026-09-28T16:22:56.6930000Z; 24h 16m: 6aa4142c41b41dbac0c7f24e.jsonl[12231] _id=6ac524f8de269131f9b52aa9 ts=2026-10-06T16:42:32.1750000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[13447] _id=6ac67a6ede269131f9bd6f87 ts=2026-10-07T16:59:25.9660000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[1046] _id=6ab55213485cab4c955327c9 ts=2026-09-24T16:38:44.1100000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1047] _id=6ab55214485cab4c955327cb ts=2026-09-24T16:38:44.1110000Z; 1ms: 6aa4142c41b41dbac0c7f24e.jsonl[1332] _id=6ab6a147485cab4c9559b6b2 ts=2026-09-25T16:28:54.9870000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[1330] _id=6ab6a147485cab4c9559b6be ts=2026-09-25T16:28:54.9880000Z; 2ms: 6aa4142c41b41dbac0c7f24e.jsonl[919] _id=6ab54fd4485cab4c95530e4d ts=2026-09-24T16:29:08.4200000Z -> 6aa4142c41b41dbac0c7f24e.jsonl[873] _id=6ab54fd4485cab4c95530e4f ts=2026-09-24T16:29:08.4220000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[908] _id=6ab54fbf485cab4c95530cdd ts=2026-09-24T16:28:47.6590000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1250] _id=6ab553ea485cab4c95534b67 ts=2026-09-24T16:46:34.8130000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1464] _id=6ab6a324485cab4c955aec60 ts=2026-09-25T16:36:52.7880000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 128 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[2180] _id=6ab6a66b485cab4c955cdb8d ts=2026-09-25T16:50:50.5200000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[2183] _id=6ab6a66c485cab4c955cdba2 ts=2026-09-25T16:50:51.4860000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[2249] _id=6ab6a678485cab4c955cddbc ts=2026-09-25T16:51:03.3000000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 387 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[1818] _id=6ab6a63a485cab4c955cd5a0 ts=2026-09-25T16:47:21.8260000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1907] _id=6ab6a63a485cab4c955cd5b8 ts=2026-09-25T16:47:21.9150000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1894] _id=6ab6a63b485cab4c955cd5c3 ts=2026-09-25T16:47:21.9460000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[1086] _id=6ab552dd485cab4c95533b5c ts=2026-09-24T16:42:05.8770000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1087] _id=6ab552dd485cab4c95533b61 ts=2026-09-24T16:42:05.9110000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1095] _id=6ab552de485cab4c95533b91 ts=2026-09-24T16:42:07.1500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[545] _id=6ab4053e485cab4c954e8c82 ts=?`; `6aa4142c41b41dbac0c7f24e.jsonl[4354] _id=6aba9460485cab4c956a6b76 ts=?`; `6aa4142c41b41dbac0c7f24e.jsonl[10215] _id=6abe9102485cab4c95ac36ba ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 519 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[2113] _id=6ab6a655485cab4c955cd955 ts=2026-09-25T16:50:28.8030000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[2141] _id=6ab6a65c485cab4c955cd9f9 ts=2026-09-25T16:50:36.4510000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[2146] _id=6ab6a65d485cab4c955cd9fb ts=2026-09-25T16:50:36.4750000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1587 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[1860] _id=6ab6a638485cab4c955cd565 ts=2026-09-25T16:47:03.5630000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1878] _id=6ab6a638485cab4c955cd575 ts=2026-09-25T16:47:03.5900000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[1854] _id=6ab6a639485cab4c955cd57b ts=2026-09-25T16:47:05.8040000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 45 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[6864] _id=6abbea5e485cab4c95810267 ts=2026-09-29T16:42:06.3830000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[6868] _id=6abbea63485cab4c958102f5 ts=2026-09-29T16:42:10.9910000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[6866] _id=6abbea63485cab4c95810309 ts=2026-09-29T16:42:11.0330000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[13438] _id=6ac52a9ade269131f9b613c5 ts=2026-10-06T17:06:34.5710000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[13435] _id=6ac52a9bde269131f9b613d7 ts=2026-10-06T17:06:35.8460000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 208 start, 199 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 88 unmatched 'BecameCameraCentered' (totals: 731 open, 771 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 152 unmatched 'BecameVisible' (totals: 2007 open, 2242 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 55 open, 52 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 111 open, 117 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 36 start, 23 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 468 of 13599 adjacent _id pairs reverse in client time; worst 347194.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f24e.jsonl[11812] _id=6ac3d8fbde269131f9ae779f ts=2026-10-05T17:06:02.9800000Z`; `6aa4142c41b41dbac0c7f24e.jsonl[11835] _id=6ac5206bde269131f9b4f399 ts=2026-10-01T16:39:28.077Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.07s, min -431018.98s, max +0.54s over 13600 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f24e\coverage.yaml

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
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
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

### `PuzzlePieceVisibleEvent` — 5751 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (5751)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.11s, n=5750)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5751/5751 records)
    "BecameInvisible"  x2242
    "BecameVisible"  x2007
    "BecameCameraUncentered"  x771
    "BecameCameraCentered"  x731
data.pieceId  (string, 5751/5751 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5751/5751 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3824 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2281); Unit 3 Dev (1119); Unit 1 Dev (415); Unit 4 Dev (9)
- **Intervals:** median 0.60s (p5 0.07s / p95 11.11s, n=3823)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3824/3824 records)
    "pressed"  x3824
data.actionType  (string, 3824/3824 records)
    "Move"  x2221
    "Jump"  x980
    "Interact"  x389
    "Sprint"  x80
    "Ascend"  x63
    "Hoverboard"  x51
    "Map"  x27
    "Pause"  x6
    "ToggleDebug"  x6
    "SkipCinematic"  x1
data.key  (string, 3824/3824 records, 38 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3824/3824 records)
    "Player"  x2978
    "Drone"  x846
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1899 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1156); Unit 1 Dev (480); Unit 3 Dev (252); Unit 4 Dev (11)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.03s, n=1895)
- **Fields under `data`:**

```text
data.position  (object, 1899/1899 records)
data.position.x  (number, 1899/1899 records)
    numeric range -26.6881 .. 1422.59 (560 unique)
data.position.y  (number, 1899/1899 records)
    numeric range -115.127 .. 169.271 (385 unique)
data.position.z  (number, 1899/1899 records)
    numeric range -639.68 .. 1911.8 (562 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1235 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (732); Unit 1 Dev (350); Unit 3 Dev (149); Unit 4 Dev (4)
- **eventKey:** present on 828 of 1235 records
- **Intervals:** median 6.27s (p5 0.00s / p95 64.60s, n=1234)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x828; [conversationId, dialogueEventType] x407
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1235/1235 records)
    numeric range 8 .. 101 (26 unique)
data.dialogueEventType  (string, 1235/1235 records)
    "DialogueNodeEvent"  x828
    "DialogueStartEvent"  x208
    "DialogueFinishEvent"  x199
data.nodeId  (number, 828/1235 records)
    numeric range 0 .. 290 (167 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 264 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (147); Unit 3 Dev (117)
- **Intervals:** median 0.39s (p5 0.02s / p95 9.66s, n=263)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 264/264 records)
    "argumentationNodeHoverEnd"  x117
    "argumentationNodeHoverStart"  x111
    "argumentationNodeAdd"  x21
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 264/264 records)
    "Unit 3 - Pollution Upstream"  x117
    "Unit 1 - Freshwater"  x110
    "Unit 1 - Argumentation Tutorial"  x37
data.nodeName  (string, 264/264 records)
    "1"  x67
    "A"  x54
    "I"  x38
    "II"  x30
    "3"  x22
    "B"  x16
    "4"  x14
    "2"  x13
    "5"  x10
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 191 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (106); Unit 1 Dev (80); Unit 3 Dev (5)
- **Intervals:** median 7.00s (p5 0.14s / p95 504.21s, n=190)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 191/191 records)
    14 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 191/191 records)
    33 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 174 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (128); Unit 3 Dev (44); Unit 1 Dev (2)
- **Intervals:** median 4.23s (p5 0.41s / p95 662.92s, n=173)
- **`data` key-set variants:** [actionType, featureUsed] x107; [actionType, featureUsed, legendName] x35; [actionType, featureUsed, location] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 174/174 records)
    "MapOpenEvent"  x55
    "MapCloseEvent"  x52
    "Selected"  x28
    "WaypointMoveEvent"  x25
    "Unselected"  x7
    "WaypointSetEvent"  x7
data.featureUsed  (string, 174/174 records)
    "Map"  x107
    "Legend"  x35
    "Waypoint"  x32
data.legendName  (string, 35/174 records)
    "360 ft"  x6
    "90 ft"  x6
    "270 ft"  x4
    "330 ft"  x4
    "240 ft"  x3
    "300 ft"  x3
    "0 ft"  x2
    "210 ft"  x2
    "60 ft"  x2
    "Water"  x2
    "150 ft"  x1
data.location  (object, 32/174 records)
data.location.x  (number, 32/174 records)
    numeric range -503.09 .. 282.91 (28 unique)
data.location.y  (number, 32/174 records)
    numeric range -345.5 .. 272.5 (25 unique)
data.location.z  (number, 32/174 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 59 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 1 Dev (25); Unit 3 Dev (4)
- **eventKey:** present on 59 of 59 records
- **Intervals:** median 257.20s (p5 0.00s / p95 85622.25s, n=58)
- **`data` key-set variants:** [questEventType, questID, questName] x36; [questEventType, questID, questName, questSuccessOrFailure] x23
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 59/59 records)
    "questActiveEvent"  x36
    "questFinishEvent"  x23
data.questID  (string, 59/59 records)
    13 unique values (see csv/event_unique_values.csv)
data.questName  (string, 59/59 records)
    13 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 23/59 records)
    "Succeeded"  x23
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 48 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (22); MainMenu (18); Unit 1 Dev (7); Unit 3 Dev (1)
- **Intervals:** median 287.42s (p5 2.04s / p95 87597.02s, n=47)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 48/48 records)
    true  x48
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 42 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (42)
- **Intervals:** median 0.63s (p5 0.16s / p95 7.06s, n=41)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x38; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/42 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/42 records)
    "Unit 2 Prod (Refactor)"  x4
data.actionType  (string, 38/42 records)
    "RightDrag"  x21
    "LeftDrag"  x17
data.currentSoilType  (string, 38/42 records)
    "SAND"  x10
    "SANDGRAVEL"  x10
    "CLAYSAND"  x6
    "CLAY"  x4
    "GRAVEL"  x4
    "CLAYROCK"  x3
    "BEDROCK"  x1
data.isCorrectSelection  (string, 38/42 records)
    "false"  x28
    "true"  x10
data.waterLevelStatus  (string, 38/42 records)
    "TooHigh"  x20
    "Proper"  x14
    "TooLow"  x4
data.waterRetentionChange  (string, 38/42 records)
    "Decrease"  x18
    "Increase"  x10
    "NoChange"  x10
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowUnfocusEvent` — 37 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 1 Dev (9); Unit 3 Dev (2); MainMenu (1)
- **Intervals:** median 270.37s (p5 7.03s / p95 148698.46s, n=36)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 37/37 records)
    false  x37
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 19 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 1 Dev (4); MainMenu (2); Unit 3 Dev (2); Unit 4 Dev (1)
- **Intervals:** median 43514.66s (p5 10.92s / p95 270975.63s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "DebugMenuStateChanged"  x19
data.isOpened  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 1 Dev (4); Unit 3 Dev (4)
- **Intervals:** median 8.25s (p5 0.95s / p95 397118.42s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 18 empty-string)
    ""  x18
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 84988.04s (p5 297.60s / p95 279555.18s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 10 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (4)
- **Intervals:** median 77.80s (p5 21.41s / p95 605535.89s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "submitAnswerEvent"  x10
data.answerSubmitted  (string, 10/10 records, 2 empty-string)
    ""  x2
    "A,1,I"  x2
    "B,5,I"  x2
    "1,"  x1
    "A,1,II"  x1
    "A,3,II"  x1
    "B,2,I"  x1
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (1)
- **Intervals:** median 86.87s (p5 52.41s / p95 648828.36s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionOpen"  x5
    "argumentationSessionClose"  x4
data.argumentationDescription  (string, 9/9 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x2
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x2
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x2
    "unit1"  x1
    "unit3"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 1037937.48s (p5 1037937.48s / p95 1037937.48s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (42 records)
- `TopographicMapEvent` data.actionType: "Selected" (28x); "Unselected" (7x); "WaypointMoveEvent" (25x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (35x); "Waypoint" (32x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*