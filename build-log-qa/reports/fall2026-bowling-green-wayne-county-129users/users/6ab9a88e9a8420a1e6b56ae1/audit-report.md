# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae1

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56ae1
- **Game version string(s) in log:** 2.9.0, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae1.jsonl
- **Records:** 27385 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae1
- **Time span:** 2026-10-06T13:24:31.735000+00:00 .. 2026-10-16T13:59:14.430000+00:00 (240h 34m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae1\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **19 event types**, 27385 records, 3 scenes.
- Findings: **0 FAIL**, **25 WARNING**, 94 INFO, 6 NOT_TESTED, 75 PASS.
- Top items needing attention:
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 14622 | 53.39 | 1 | 1 | 0 | 2026-10-14T16:42:41.883000+00:00 | 2026-10-16T13:42:59.522000+00:00 | 45h 0m |
| InputEvent | 8707 | 31.79 | 1 | 2 | 0 | 2026-10-06T13:29:20.047000+00:00 | 2026-10-16T13:58:51.243000+00:00 | 240h 29m |
| PlayerPositionEvent | 2256 | 8.24 | 1 | 2 | 0 | 2026-10-06T13:24:40.491000+00:00 | 2026-10-16T13:59:14.430000+00:00 | 240h 34m |
| DialogueEvent | 871 | 3.18 | 1 | 2 | 562 | 2026-10-06T13:24:58.374000+00:00 | 2026-10-16T13:52:47.499000+00:00 | 240h 27m |
| ObjectInterEvent | 469 | 1.71 | 1 | 2 | 0 | 2026-10-06T13:34:22.579000+00:00 | 2026-10-16T13:47:02.078000+00:00 | 240h 12m |
| TopographicMapEvent | 122 | 0.45 | 1 | 1 | 0 | 2026-10-14T16:09:26.779000+00:00 | 2026-10-16T13:14:42.595000+00:00 | 45h 5m |
| DaniEvent | 78 | 0.28 | 1 | 2 | 0 | 2026-10-14T13:56:49.082000+00:00 | 2026-10-16T04:09:14.701000+00:00 | 38h 12m |
| argumentationNodeEvent | 78 | 0.28 | 1 | 2 | 0 | 2026-10-14T13:53:52.110000+00:00 | 2026-10-16T03:10:28.477000+00:00 | 37h 16m |
| questEvent | 46 | 0.17 | 1 | 2 | 46 | 2026-10-06T13:24:58.354000+00:00 | 2026-10-16T13:52:39.366000+00:00 | 240h 27m |
| gameWindowFocusEvent | 34 | 0.12 | 1 | 3 | 0 | 2026-10-06T13:24:31.735000+00:00 | 2026-10-16T13:59:13.004000+00:00 | 240h 34m |
| DEBUGMenu | 30 | 0.11 | 1 | 3 | 0 | 2026-10-06T13:24:40.478000+00:00 | 2026-10-16T13:11:42.888000+00:00 | 239h 47m |
| gameWindowUnfocusEvent | 25 | 0.09 | 1 | 2 | 0 | 2026-10-06T13:58:10.719000+00:00 | 2026-10-16T13:59:10.155000+00:00 | 240h 0m |
| gameStartEvent | 15 | 0.05 | 1 | 1 | 0 | 2026-10-06T13:24:31.736000+00:00 | 2026-10-16T13:11:36.120000+00:00 | 239h 47m |
| chatEvent | 10 | 0.04 | 1 | 1 | 0 | 2026-10-15T13:34:48.997000+00:00 | 2026-10-16T03:24:27.662000+00:00 | 13h 49m |
| argumentationEvent | 8 | 0.03 | 1 | 1 | 0 | 2026-10-14T13:52:16.812000+00:00 | 2026-10-14T15:58:48.607000+00:00 | 2h 6m |
| Soil Key Puzzle | 6 | 0.02 | 1 | 1 | 0 | 2026-10-14T16:49:38.990000+00:00 | 2026-10-16T13:47:05.021000+00:00 | 44h 57m |
| crash | 5 | 0.02 | 1 | 1 | 0 |  |  | ? |
| argumentationAnswerEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-14T13:54:28.744000+00:00 | 2026-10-14T15:58:48.588000+00:00 | 2h 4m |
| EndOfUnit | 1 | 0.0 | 1 | 1 | 0 | 2026-10-14T16:03:41.407000+00:00 | 2026-10-14T16:03:41.407000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 24.882s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 0.776s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.085s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.98s median 
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
  - Observed: 7459.844s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 0.951s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 14.705s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 21646.768s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 675.601s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 474.726s median 
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
  - Observed: 78 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 8707 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Insert; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 6 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: RightDrag 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK; CLAYSAND; GRAVEL; SAND; SANDGRAVEL 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.isCorrectSelection` — baseline categorical value(s) not seen this build. 
  - Observed: true 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.waterLevelStatus` — baseline categorical value(s) not seen this build. 
  - Observed: TooHigh; TooLow 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.waterRetentionChange` — baseline categorical value(s) not seen this build. 
  - Observed: Decrease; NoChange 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 10 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-179, 68-1, 68-2, 68-3, 68-5, 68-10]; [18-271, 18-273, 18-179, 68-1, 68-2, 68-3]; [18-273, 18-179, 68-1, 68-2, 68-3]; [68-1, 68-2, 68-3, 68-5, 68-10] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 22; 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[2] _id=6ac4f690de269131f9b06f94 ts=2026-10-06T13:24:31.7360000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[718] _id=6ac647f2de269131f9b8e0e1 ts=2026-10-07T13:24:01.0530000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[776] _id=6ac6486dde269131f9b8f935 ts=2026-10-07T13:26:05.6660000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 34 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 34} 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[1] _id=6ac4f690de269131f9b06f8c ts=2026-10-06T13:24:31.7350000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[717] _id=6ac647f2de269131f9b8e0e0 ts=2026-10-07T13:24:01.0530000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[775] _id=6ac6486dde269131f9b8f934 ts=2026-10-07T13:26:05.6660000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[715] _id=6ac647f2de269131f9b8e0bf ts=2026-10-06T13:58:10.719Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[2099] _id=6ac79aa0de269131f9c03852 ts=2026-10-07T13:59:47.023Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[2948] _id=6ace2f54de269131f9ce8f67 ts=2026-10-08T13:58:16.741Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 82 of 122 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[5247] _id=6acfa937de269131f9d53fd5 ts=2026-10-14T16:09:26.7790000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[5256] _id=6acfa940de269131f9d540a3 ts=2026-10-14T16:09:36.1580000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[5439] _id=6acfb114de269131f9d5b904 ts=2026-10-14T16:42:59.7360000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 14621 | 0.0 | 0.085 | 11.081 | 2.049 | 73550.262 | 5.41 | 5815 | 5 |
| InputEvent | 8706 | 0.0 | 0.816 | 99.445 | 7.717 | 429608.692 | 0.6 | 77 | 10 |
| PlayerPositionEvent | 2254 | 9.827 | 10.0 | 384.2 | 10.033 | 429547.193 | 0.16 | 0 | 10 |
| DialogueEvent | 870 | 0.001 | 4.492 | 995.022 | 83.444 | 429810.888 | 0.06 | 212 | 13 |
| ObjectInterEvent | 468 | 0.003 | 0.776 | 1847.777 | 319.008 | 429948.631 | 0.03 | 7 | 13 |
| TopographicMapEvent | 121 | 0.133 | 1.083 | 1341.453 | 1072.622 | 73637.774 | 0.04 | 0 | 9 |
| DaniEvent | 77 | 0.003 | 3.526 | 1786.307 | 726.758 | 85074.141 | 0.03 | 12 | 5 |
| argumentationNodeEvent | 77 | 0.019 | 0.951 | 1742.81 | 55.228 | 86841.323 | 0.03 | 13 | 3 |
| questEvent | 45 | 0.001 | 264.358 | 19236.911 | 85392.087 | 430549.458 | 0.0 | 11 | 18 |
| gameWindowFocusEvent | 33 | 1.597 | 675.601 | 26244.887 | 86453.017 | 431283.588 | 0.0 | 0 | 17 |
| DEBUGMenu | 29 | 3.277 | 24.882 | 29766.29 | 86488.471 | 431277.962 | 0.0 | 0 | 13 |
| gameWindowUnfocusEvent | 24 | 0.0 | 474.726 | 36002.476 | 87345.944 | 430417.834 | 0.0 | 1 | 11 |
| gameStartEvent | 14 | 124.613 | 21646.768 | 61658.885 | 207225.324 | 431283.588 | 0.0 | 0 | 13 |
| chatEvent | 9 | 1.391 | 14.705 | 5530.963 | 29668.035 | 48929.887 | 0.01 | 0 | 2 |
| argumentationEvent | 7 | 35.836 | 42.945 | 1084.542 | 5148.802 | 7332.645 | 0.06 | 0 | 1 |
| Soil Key Puzzle | 5 | 0.6 | 2.98 | 32369.206 | 108044.748 | 126128.078 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationAnswerEvent | 1 | 7459.844 | 7459.844 | 7459.844 | 7459.844 | 7459.844 | 0.01 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[2105] _id=6ac79aa7de269131f9c03904 ts=2026-10-08T13:29:10.2100000Z == 6ab9a88e9a8420a1e6b56ae1.jsonl[2106] _id=6ac79aa7de269131f9c03905 ts=2026-10-08T13:29:10.2100000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[6179] _id=6acfb48fde269131f9d6171f ts=2026-10-14T16:57:50.4860000Z == 6ab9a88e9a8420a1e6b56ae1.jsonl[6180] _id=6acfb48fde269131f9d61720 ts=2026-10-14T16:57:50.4860000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 18 group(s), 42 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[6310] _id=6acfb58fde269131f9d6383d ts=2026-10-14T17:02:06.7890000Z == 6ab9a88e9a8420a1e6b56ae1.jsonl[6311] _id=6acfb590de269131f9d63841 ts=2026-10-14T17:02:06.7890000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[6332] _id=6acfb59bde269131f9d6396c ts=2026-10-14T17:02:16.7840000Z == 6ab9a88e9a8420a1e6b56ae1.jsonl[6333] _id=6acfb59bde269131f9d6396d ts=2026-10-14T17:02:16.7840000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[6625] _id=6ad0d4f5de269131f9da93d3 ts=2026-10-15T13:28:20.9720000Z == 6ab9a88e9a8420a1e6b56ae1.jsonl[6628] _id=6ad0d4f5de269131f9da93db ts=2026-10-15T13:28:20.9720000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[781] _id=6ac64878de269131f9b8fb80 ts=? == 6ab9a88e9a8420a1e6b56ae1.jsonl[4618] _id=6acf89b7de269131f9d39bbd ts=?`; `6ab9a88e9a8420a1e6b56ae1.jsonl[5285] _id=6acfb040de269131f9d5a8e7 ts=? == 6ab9a88e9a8420a1e6b56ae1.jsonl[10508] _id=6ad0f73bde269131f9dced32 ts=?`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `836ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[22476] _id=6ad1a1adde269131f9e32317 ts=2026-10-16T04:01:48.8170000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[22491] _id=6ad1a1aede269131f9e3231e ts=2026-10-16T04:01:49.6530000Z`; `969ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[22749] _id=6ad1a232de269131f9e32559 ts=2026-10-16T04:04:01.5830000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[22740] _id=6ad1a233de269131f9e32563 ts=2026-10-16T04:04:02.5520000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 247 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `317ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[193] _id=6ac4f8e1de269131f9b0d0a9 ts=2026-10-06T13:34:24.8450000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[198] _id=6ac4f8e1de269131f9b0d0b6 ts=2026-10-06T13:34:25.1620000Z`; `167ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[198] _id=6ac4f8e1de269131f9b0d0b6 ts=2026-10-06T13:34:25.1620000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[195] _id=6ac4f8e1de269131f9b0d0bd ts=2026-10-06T13:34:25.3290000Z`; `467ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[195] _id=6ac4f8e1de269131f9b0d0bd ts=2026-10-06T13:34:25.3290000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[199] _id=6ac4f8e2de269131f9b0d0cb ts=2026-10-06T13:34:25.7960000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `249ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[8998] _id=6ad0d892de269131f9daf2e4 ts=2026-10-15T13:43:46.4250000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[8997] _id=6ad0d892de269131f9daf2ea ts=2026-10-15T13:43:46.6740000Z`; `916ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[11587] _id=6ad0fa59de269131f9dd3e8b ts=2026-10-15T16:07:52.5240000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[11590] _id=6ad0fa5ade269131f9dd3ea9 ts=2026-10-15T16:07:53.4400000Z`; `400ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[11589] _id=6ad0fa5cde269131f9dd3ecd ts=2026-10-15T16:07:55.1400000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[11594] _id=6ad0fa5cde269131f9dd3ed7 ts=2026-10-15T16:07:55.5400000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `332ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4867] _id=6acfa63dde269131f9d504a9 ts=2026-10-14T15:56:44.4880000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[4860] _id=6acfa63dde269131f9d504b1 ts=2026-10-14T15:56:44.8200000Z`; `333ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4902] _id=6acfa6aade269131f9d50a42 ts=2026-10-14T15:58:34.1370000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[4906] _id=6acfa6abde269131f9d50a57 ts=2026-10-14T15:58:34.4700000Z`; `965ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[11521] _id=6ad0f9efde269131f9dd315c ts=2026-10-15T16:06:06.5930000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[11524] _id=6ad0f9f0de269131f9dd317a ts=2026-10-15T16:06:07.5580000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4773] _id=6acf8abfde269131f9d3c730 ts=2026-10-14T13:59:27.1350000Z ~ 6ab9a88e9a8420a1e6b56ae1.jsonl[4776] _id=6acfa586de269131f9d4fcf1 ts=2026-10-14T13:59:27.135Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2103] _id=6ac79aa6de269131f9c038ef ts=2026-10-08T13:29:09.7980000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2949] _id=6ace2f54de269131f9ce8f6b ts=2026-10-13T13:17:07.7600000Z; 24h 2m: 6ab9a88e9a8420a1e6b56ae1.jsonl[778] _id=6ac64872de269131f9b8fa6e ts=2026-10-07T13:26:10.4030000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2100] _id=6ac79aa0de269131f9c0385b ts=2026-10-08T13:29:04.1810000Z; 23h 59m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3] _id=6ac4f698de269131f9b071fa ts=2026-10-06T13:24:40.4780000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[716] _id=6ac647f2de269131f9b8e0df ts=2026-10-07T13:24:00.9880000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 23h 37m 
  - Evidence: 23h 37m: 6ab9a88e9a8420a1e6b56ae1.jsonl[4678] _id=6acf8a23de269131f9d3a742 ts=2026-10-14T13:56:51.2650000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[7311] _id=6ad0d675de269131f9dab7a4 ts=2026-10-15T13:34:45.4060000Z; 11h 3m: 6ab9a88e9a8420a1e6b56ae1.jsonl[11532] _id=6ad0f9fade269131f9dd328e ts=2026-10-15T16:06:17.2910000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[14602] _id=6ad1957bde269131f9e2de85 ts=2026-10-16T03:09:46.8290000Z; 2h 22m: 6ab9a88e9a8420a1e6b56ae1.jsonl[8993] _id=6ad0d86bde269131f9daee64 ts=2026-10-15T13:43:07.3510000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[11519] _id=6ad0f9e6de269131f9dd30cb ts=2026-10-15T16:05:57.5650000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.003s..0.004s shown 
  - Evidence: 3ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[19566] _id=6ad19d61de269131f9e30ada ts=2026-10-16T03:43:28.7900000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[19568] _id=6ad19d61de269131f9e30adc ts=2026-10-16T03:43:28.7930000Z; 4ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[20658] _id=6ad19f17de269131f9e31466 ts=2026-10-16T03:50:46.6260000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[20659] _id=6ad19f17de269131f9e31468 ts=2026-10-16T03:50:46.6300000Z; 4ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[22113] _id=6ad1a15ade269131f9e3206e ts=2026-10-16T04:00:25.6720000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[22139] _id=6ad1a15ade269131f9e32070 ts=2026-10-16T04:00:25.6760000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2910] _id=6ac7a11fde269131f9c14df2 ts=2026-10-08T13:56:47.6640000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3072] _id=6ace3013de269131f9ce9661 ts=2026-10-13T13:20:18.5520000Z; 23h 47m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3398] _id=6ace328bde269131f9ceaca5 ts=2026-10-13T13:30:50.1740000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3532] _id=6acf811fde269131f9d2e200 ts=2026-10-14T13:18:23.2340000Z; 23h 41m: 6ab9a88e9a8420a1e6b56ae1.jsonl[1494] _id=6ac64df8de269131f9b9fd43 ts=2026-10-07T13:49:44.4840000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2174] _id=6ac79b12de269131f9c04627 ts=2026-10-08T13:30:57.9340000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 212 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[11958] _id=6ad18eaede269131f9e2c268 ts=2026-10-16T02:40:46.1010000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[11959] _id=6ad18eaede269131f9e2c269 ts=2026-10-16T02:40:46.1020000Z; 1ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[27138] _id=6ad22b5ade269131f9e40858 ts=2026-10-16T13:49:14.3110000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[27139] _id=6ad22b5ade269131f9e40859 ts=2026-10-16T13:49:14.3120000Z; 1ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4667] _id=6acf8a02de269131f9d3a2f0 ts=2026-10-14T13:56:17.7860000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4668] _id=6acf8a02de269131f9d3a2f1 ts=2026-10-14T13:56:17.7870000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2938] _id=6ac7a144de269131f9c15196 ts=2026-10-08T13:57:23.9310000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2952] _id=6ace2f6dde269131f9ce8fd5 ts=2026-10-13T13:17:32.6230000Z; 23h 45m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3393] _id=6ace3281de269131f9ceac73 ts=2026-10-13T13:30:40.4230000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3417] _id=6acf80a4de269131f9d2db30 ts=2026-10-14T13:16:20.0070000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2096] _id=6ac65051de269131f9ba3c4a ts=2026-10-07T13:59:45.6100000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2105] _id=6ac79aa7de269131f9c03904 ts=2026-10-08T13:29:10.2100000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 77 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[19925] _id=6ad19dcdde269131f9e30e6b ts=2026-10-16T03:45:16.7790000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[19926] _id=6ad19dcdde269131f9e30e6c ts=2026-10-16T03:45:16.7790000Z; 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[19932] _id=6ad19db5de269131f9e30d94 ts=2026-10-16T03:44:52.9640000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[19933] _id=6ad19db5de269131f9e30d95 ts=2026-10-16T03:44:52.9640000Z; 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[2105] _id=6ac79aa7de269131f9c03904 ts=2026-10-08T13:29:10.2100000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2106] _id=6ac79aa7de269131f9c03905 ts=2026-10-08T13:29:10.2100000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2937] _id=6ac7a144de269131f9c15192 ts=2026-10-08T13:57:23.9240000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3203] _id=6ace30c1de269131f9ce9ba5 ts=2026-10-13T13:23:12.5550000Z; 23h 46m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3395] _id=6ace328ade269131f9ceaca0 ts=2026-10-13T13:30:50.1560000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3479] _id=6acf80e3de269131f9d2dee9 ts=2026-10-14T13:17:23.2880000Z; 23h 43m: 6ab9a88e9a8420a1e6b56ae1.jsonl[614] _id=6ac4fd31de269131f9b1c2b9 ts=2026-10-06T13:52:49.2360000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[1087] _id=6ac64ac3de269131f9b992bc ts=2026-10-07T13:36:03.1100000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.003s..0.004s shown 
  - Evidence: 3ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[1087] _id=6ac64ac3de269131f9b992bc ts=2026-10-07T13:36:03.1100000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[1084] _id=6ac64ac3de269131f9b992d0 ts=2026-10-07T13:36:03.1130000Z; 3ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[2330] _id=6ac79c3dde269131f9c07a5e ts=2026-10-08T13:35:57.6730000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2331] _id=6ac79c3ede269131f9c07a67 ts=2026-10-08T13:35:57.6760000Z; 4ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[3203] _id=6ace30c1de269131f9ce9ba5 ts=2026-10-13T13:23:12.5550000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3204] _id=6ace30c1de269131f9ce9ba7 ts=2026-10-13T13:23:12.5590000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2943] _id=6ac7a173de269131f9c155a2 ts=2026-10-08T13:58:11.1900000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2946] _id=6ace2f61de269131f9ce8f96 ts=2026-10-13T13:17:18.3830000Z; 23h 44m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3409] _id=6ace32d1de269131f9ceaefc ts=2026-10-13T13:32:00.3560000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3415] _id=6acf809dde269131f9d2dada ts=2026-10-14T13:16:10.9090000Z; 23h 29m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2094] _id=6ac6504ede269131f9ba3c1c ts=2026-10-07T13:59:42.2960000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2104] _id=6ac79aa7de269131f9c03903 ts=2026-10-08T13:29:09.8070000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 20h 25m 
  - Evidence: 20h 25m: 6ab9a88e9a8420a1e6b56ae1.jsonl[6354] _id=6acfb5a8de269131f9d63a88 ts=2026-10-14T17:02:30.7100000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[6625] _id=6ad0d4f5de269131f9da93d3 ts=2026-10-15T13:28:20.9720000Z; 10h 32m: 6ab9a88e9a8420a1e6b56ae1.jsonl[11908] _id=6ad0faf0de269131f9dd505f ts=2026-10-15T16:10:23.0390000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[12039] _id=6ad18f64de269131f9e2c44d ts=2026-10-16T02:42:24.4800000Z; 9h 3m: 6ab9a88e9a8420a1e6b56ae1.jsonl[23931] _id=6ad1a3afde269131f9e330c1 ts=2026-10-16T04:10:21.9870000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[24145] _id=6ad223dfde269131f9e36ba3 ts=2026-10-16T13:13:52.7800000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5815 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[10056] _id=6ad0dabede269131f9db38ae ts=2026-10-15T13:53:01.7820000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[9901] _id=6ad0dabede269131f9db38b6 ts=2026-10-15T13:53:01.7820000Z; 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[10139] _id=6ad0db2fde269131f9db46b4 ts=2026-10-15T13:54:54.6380000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[10137] _id=6ad0db2fde269131f9db46b6 ts=2026-10-15T13:54:54.6380000Z; 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[10265] _id=6ad0db82de269131f9db4fe5 ts=2026-10-15T13:56:17.0160000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[10153] _id=6ad0db82de269131f9db4fe7 ts=2026-10-15T13:56:17.0160000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 35h 2m 
  - Evidence: 35h 2m: 6ab9a88e9a8420a1e6b56ae1.jsonl[6100] _id=6acfb2a6de269131f9d5e85b ts=2026-10-14T16:49:41.9700000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[20725] _id=6ad19f56de269131f9e31515 ts=2026-10-16T03:51:50.0480000Z; 9h 55m: 6ab9a88e9a8420a1e6b56ae1.jsonl[20728] _id=6ad19f57de269131f9e31517 ts=2026-10-16T03:51:50.6480000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[27077] _id=6ad22ad6de269131f9e3f7c8 ts=2026-10-16T13:47:02.0750000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 20h 27m 
  - Evidence: 20h 27m: 6ab9a88e9a8420a1e6b56ae1.jsonl[6293] _id=6acfb568de269131f9d633e5 ts=2026-10-14T17:01:27.9820000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[6650] _id=6ad0d50dde269131f9da9678 ts=2026-10-15T13:28:45.7560000Z; 10h 34m: 6ab9a88e9a8420a1e6b56ae1.jsonl[11626] _id=6ad0fa67de269131f9dd405a ts=2026-10-15T16:08:06.2440000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[11936] _id=6ad18f25de269131f9e2c39e ts=2026-10-16T02:42:44.3290000Z; 9h 20m: 6ab9a88e9a8420a1e6b56ae1.jsonl[20854] _id=6ad19fdede269131f9e3163f ts=2026-10-16T03:54:05.5520000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[24013] _id=6ad22333de269131f9e35f7b ts=2026-10-16T13:14:27.6820000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 4m 
  - Evidence: 2h 4m: 6ab9a88e9a8420a1e6b56ae1.jsonl[4609] _id=6acf8994de269131f9d39895 ts=2026-10-14T13:54:28.7440000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4855] _id=6acfa6b9de269131f9d50b9b ts=2026-10-14T15:58:48.5880000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 2m 
  - Evidence: 2h 2m: 6ab9a88e9a8420a1e6b56ae1.jsonl[4605] _id=6acf8995de269131f9d39897 ts=2026-10-14T13:54:28.7600000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4865] _id=6acfa63ade269131f9d50477 ts=2026-10-14T15:56:41.4050000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 24h 7m 
  - Evidence: 24h 7m: 6ab9a88e9a8420a1e6b56ae1.jsonl[4918] _id=6acfa6b5de269131f9d50b57 ts=2026-10-14T15:58:45.2700000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[11521] _id=6ad0f9efde269131f9dd315c ts=2026-10-15T16:06:06.5930000Z; 11h 3m: 6ab9a88e9a8420a1e6b56ae1.jsonl[11527] _id=6ad0f9f5de269131f9dd3214 ts=2026-10-15T16:06:12.1420000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[14608] _id=6ad1958cde269131f9e2de99 ts=2026-10-16T03:10:03.2470000Z; 2h 1m: 6ab9a88e9a8420a1e6b56ae1.jsonl[4602] _id=6acf8990de269131f9d39809 ts=2026-10-14T13:54:24.2260000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4841] _id=6acfa602de269131f9d50213 ts=2026-10-14T15:55:45.9050000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.019s..0.023s shown 
  - Evidence: 19ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4598] _id=6acf8989de269131f9d39751 ts=2026-10-14T13:54:17.6420000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4599] _id=6acf8989de269131f9d39754 ts=2026-10-14T13:54:17.6610000Z; 20ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[11521] _id=6ad0f9efde269131f9dd315c ts=2026-10-15T16:06:06.5930000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[11522] _id=6ad0f9efde269131f9dd3160 ts=2026-10-15T16:06:06.6130000Z; 23ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[14608] _id=6ad1958cde269131f9e2de99 ts=2026-10-16T03:10:03.2470000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[14609] _id=6ad1958cde269131f9e2de9b ts=2026-10-16T03:10:03.2700000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 13h 35m 
  - Evidence: 13h 35m: 6ab9a88e9a8420a1e6b56ae1.jsonl[7317] _id=6ad0d687de269131f9dab917 ts=2026-10-15T13:35:03.7020000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[14618] _id=6ad195aade269131f9e2dece ts=2026-10-16T03:10:33.5890000Z; 12m 55s: 6ab9a88e9a8420a1e6b56ae1.jsonl[14621] _id=6ad195b9de269131f9e2dede ts=2026-10-16T03:10:48.6290000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[16410] _id=6ad198c0de269131f9e2efe2 ts=2026-10-16T03:23:43.8850000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2102] _id=6ac79aa0de269131f9c0385d ts=2026-10-08T13:29:04.2320000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2951] _id=6ace2f54de269131f9ce8f6d ts=2026-10-13T13:17:07.8200000Z; 24h 2m: 6ab9a88e9a8420a1e6b56ae1.jsonl[776] _id=6ac6486dde269131f9b8f935 ts=2026-10-07T13:26:05.6660000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2102] _id=6ac79aa0de269131f9c0385d ts=2026-10-08T13:29:04.2320000Z; 23h 59m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2] _id=6ac4f690de269131f9b06f94 ts=2026-10-06T13:24:31.7360000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[718] _id=6ac647f2de269131f9b8e0e1 ts=2026-10-07T13:24:01.0530000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2101] _id=6ac79aa0de269131f9c0385c ts=2026-10-08T13:29:04.2320000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2950] _id=6ace2f54de269131f9ce8f6c ts=2026-10-13T13:17:07.8200000Z; 24h 2m: 6ab9a88e9a8420a1e6b56ae1.jsonl[775] _id=6ac6486dde269131f9b8f934 ts=2026-10-07T13:26:05.6660000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2101] _id=6ac79aa0de269131f9c0385c ts=2026-10-08T13:29:04.2320000Z; 23h 59m: 6ab9a88e9a8420a1e6b56ae1.jsonl[1] _id=6ac4f690de269131f9b06f8c ts=2026-10-06T13:24:31.7350000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[717] _id=6ac647f2de269131f9b8e0e0 ts=2026-10-07T13:24:01.0530000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 33m 
  - Evidence: 119h 33m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2948] _id=6ace2f54de269131f9ce8f67 ts=2026-10-08T13:58:16.741Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3407] _id=6ace32cbde269131f9ceaec5 ts=2026-10-13T13:31:54.5750000Z; 24h 18m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3407] _id=6ace32cbde269131f9ceaec5 ts=2026-10-13T13:31:54.5750000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4497] _id=6acf8892de269131f9d374f1 ts=2026-10-14T13:50:10.4550000Z; 24h 1m: 6ab9a88e9a8420a1e6b56ae1.jsonl[715] _id=6ac647f2de269131f9b8e0bf ts=2026-10-06T13:58:10.719Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2099] _id=6ac79aa0de269131f9c03852 ts=2026-10-07T13:59:47.023Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4773] _id=6acf8abfde269131f9d3c730 ts=2026-10-14T13:59:27.1350000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4776] _id=6acfa586de269131f9d4fcf1 ts=2026-10-14T13:59:27.135Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 35m 
  - Evidence: 119h 35m: 6ab9a88e9a8420a1e6b56ae1.jsonl[2430] _id=6ac79d8bde269131f9c0b5eb ts=2026-10-08T13:41:30.7460000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2947] _id=6ace2f61de269131f9ce8f97 ts=2026-10-13T13:17:20.2040000Z; 23h 47m: 6ab9a88e9a8420a1e6b56ae1.jsonl[3307] _id=6ace3206de269131f9cea784 ts=2026-10-13T13:28:37.9140000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[3416] _id=6acf809dde269131f9d2dadb ts=2026-10-14T13:16:13.0270000Z; 23h 46m: 6ab9a88e9a8420a1e6b56ae1.jsonl[1277] _id=6ac64c6dde269131f9b9ddec ts=2026-10-07T13:43:09.0060000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2107] _id=6ac79aa7de269131f9c03906 ts=2026-10-08T13:29:10.3330000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4529] _id=6acf88bdde269131f9d37b3b ts=2026-10-14T13:50:53.3590000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4530] _id=6acf88bdde269131f9d37b3c ts=2026-10-14T13:50:53.3600000Z; 1ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[4830] _id=6acfa5e2de269131f9d500b2 ts=2026-10-14T15:55:14.1320000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[4831] _id=6acfa5e2de269131f9d500b3 ts=2026-10-14T15:55:14.1330000Z; 4ms: 6ab9a88e9a8420a1e6b56ae1.jsonl[2427] _id=6ac79d8bde269131f9c0b5e9 ts=2026-10-08T13:41:30.7420000Z -> 6ab9a88e9a8420a1e6b56ae1.jsonl[2430] _id=6ac79d8bde269131f9c0b5eb ts=2026-10-08T13:41:30.7460000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[4399] _id=6acf8806de269131f9d36305 ts=2026-10-14T13:47:50.1480000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[4617] _id=6acf89a7de269131f9d39a72 ts=2026-10-14T13:54:47.3340000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[4924] _id=6acfa6cede269131f9d50d28 ts=2026-10-14T15:59:10.1210000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[781] _id=6ac64878de269131f9b8fb80 ts=?`; `6ab9a88e9a8420a1e6b56ae1.jsonl[4618] _id=6acf89b7de269131f9d39bbd ts=?`; `6ab9a88e9a8420a1e6b56ae1.jsonl[5285] _id=6acfb040de269131f9d5a8e7 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 5248 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[6311] _id=6acfb590de269131f9d63841 ts=2026-10-14T17:02:06.7890000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[6315] _id=6acfb590de269131f9d63843 ts=2026-10-14T17:02:06.7890000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[6312] _id=6acfb590de269131f9d63847 ts=2026-10-14T17:02:06.7890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 6 unmatched 'DialogueStartEvent' (totals: 156 start, 153 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 28 unmatched 'BecameVisible' (totals: 5525 open, 5497 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'questActiveEvent' (totals: 29 start, 17 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 1586 of 27379 adjacent _id pairs reverse in client time; worst 205.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae1.jsonl[24144] _id=6ad223dede269131f9e36b96 ts=2026-10-16T13:17:18.4030000Z`; `6ab9a88e9a8420a1e6b56ae1.jsonl[24145] _id=6ad223dfde269131f9e36ba3 ts=2026-10-16T13:13:52.7800000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.93s, min -429531.87s, max -0.14s over 27380 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56ae1\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | skipped |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
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

### `PuzzlePieceVisibleEvent` — 14622 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (14622)
- **Intervals:** median 0.09s (p5 0.00s / p95 2.05s, n=14621)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14622/14622 records)
    "BecameVisible"  x5525
    "BecameInvisible"  x5497
    "BecameCameraCentered"  x1800
    "BecameCameraUncentered"  x1800
data.pieceId  (string, 14622/14622 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 14622/14622 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 8707 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (5316); Unit 1 Dev (3391)
- **Intervals:** median 0.82s (p5 0.17s / p95 7.72s, n=8706)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 8707/8707 records)
    "pressed"  x8707
data.actionType  (string, 8707/8707 records)
    "Move"  x7208
    "Interact"  x1146
    "Jump"  x159
    "Sprint"  x116
    "Hoverboard"  x43
    "Pause"  x30
    "Map"  x4
    "SkipCinematic"  x1
data.key  (string, 8707/8707 records)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 8707/8707 records)
    "Player"  x8707
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2256 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1259); Unit 1 Dev (997)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2254)
- **Fields under `data`:**

```text
data.position  (object, 2256/2256 records)
data.position.x  (number, 2256/2256 records)
    numeric range -24.4419 .. 1099.84 (1403 unique)
data.position.y  (number, 2256/2256 records)
    numeric range -5.58004 .. 157.999 (608 unique)
data.position.z  (number, 2256/2256 records)
    numeric range -130.3 .. 1403.15 (1407 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 871 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (456); Unit 2 Prod (Refactor) (415)
- **eventKey:** present on 562 of 871 records
- **Intervals:** median 4.49s (p5 0.00s / p95 83.44s, n=870)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x562; [conversationId, dialogueEventType] x309
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 871/871 records)
    12 unique values (see csv/event_unique_values.csv)
data.dialogueEventType  (string, 871/871 records)
    "DialogueNodeEvent"  x562
    "DialogueStartEvent"  x156
    "DialogueFinishEvent"  x153
data.nodeId  (number, 562/871 records)
    numeric range 0 .. 283 (110 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 469 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (366); Unit 1 Dev (103)
- **Intervals:** median 0.78s (p5 0.15s / p95 319.01s, n=468)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 469/469 records)
    "Press E to Place"  x241
    "TalkTo"  x70
    "Press E to Install"  x68
    "Press E to Pick up"  x53
    "E to Talk"  x20
    "Press E to Open Locker"  x10
    "Inspect Alien Glyph"  x2
    "Press E to Collect"  x2
    "Press E to Operate"  x2
    "Press [E/Action button] to enter escape pod "  x1
data.objectName  (string, 469/469 records)
    24 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 122 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (122)
- **Intervals:** median 1.08s (p5 0.17s / p95 1072.62s, n=121)
- **`data` key-set variants:** [actionType, featureUsed, legendName] x82; [actionType, featureUsed] x30; [actionType, featureUsed, location] x10
- **Fields under `data`:**

```text
data.actionType  (string, 122/122 records)
    "Selected"  x52
    "Unselected"  x30
    "MapCloseEvent"  x15
    "MapOpenEvent"  x15
    "WaypointMoveEvent"  x6
    "WaypointSetEvent"  x4
data.featureUsed  (string, 122/122 records)
    "Legend"  x82
    "Map"  x30
    "Waypoint"  x10
data.legendName  (string, 82/122 records)
    13 unique values (see csv/event_unique_values.csv)
data.location  (object, 10/122 records)
data.location.x  (number, 10/122 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 10/122 records)
    8 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 10/122 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DaniEvent` — 78 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (76); Unit 1 Dev (2)
- **Intervals:** median 3.53s (p5 0.00s / p95 726.76s, n=77)
- **Fields under `data`:**

```text
data.actionType  (string, 78/78 records)
    "Close"  x39
    "Open"  x39
data.toolName  (string, 78/78 records, 66 empty-string)
    ""  x66
    "Settings"  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationNodeEvent` — 78 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (60); Unit 2 Prod (Refactor) (18)
- **Intervals:** median 0.95s (p5 0.03s / p95 55.23s, n=77)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 78/78 records)
    "argumentationNodeHoverEnd"  x36
    "argumentationNodeHoverStart"  x36
    "argumentationNodeAdd"  x6
data.argumentationTitle  (string, 78/78 records)
    "Unit 1 - Freshwater"  x46
    "Unit 2 – Watershed"  x18
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 78/78 records)
    "1"  x28
    "I"  x20
    "A"  x12
    "C"  x6
    "II"  x6
    "D"  x4
    "B"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 46 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (35); Unit 2 Prod (Refactor) (11)
- **eventKey:** present on 46 of 46 records
- **Intervals:** median 264.36s (p5 0.00s / p95 85392.09s, n=45)
- **`data` key-set variants:** [questEventType, questID, questName] x29; [questEventType, questID, questName, questSuccessOrFailure] x17
- **Fields under `data`:**

```text
data.questEventType  (string, 46/46 records)
    "questActiveEvent"  x29
    "questFinishEvent"  x17
data.questID  (string, 46/46 records)
    "21"  x10
    "29"  x10
    "31"  x9
    "32"  x7
    "33"  x4
    "34"  x3
    "28"  x2
    "23"  x1
data.questName  (string, 46/46 records)
    "Escape the Ruin"  x10
    "Gear Up"  x10
    "TK, Reporting In!"  x9
    "Info and Intros"  x7
    "Defend the Expedition"  x4
    "What Was That?"  x3
    "Getting Your Space Legs"  x2
    "Foraged Forging"  x1
data.questSuccessOrFailure  (string, 17/46 records)
    "Succeeded"  x17
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 34 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (14); Unit 1 Dev (5)
- **Intervals:** median 675.60s (p5 21.98s / p95 86453.02s, n=33)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 34/34 records)
    true  x34
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (14); Unit 1 Dev (8); Unit 2 Prod (Refactor) (8)
- **Intervals:** median 24.88s (p5 5.05s / p95 86488.47s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 25 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (9)
- **Intervals:** median 474.73s (p5 1.97s / p95 87345.94s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 21646.77s (p5 482.76s / p95 207225.32s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `chatEvent` — 10 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (10)
- **Intervals:** median 14.71s (p5 1.55s / p95 29668.03s, n=9)
- **`data` key-set variants:** [actionType, chatID] x8; [actionKey, chatID] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/10 records)
    "ScrollStop"  x2
data.actionType  (string, 8/10 records)
    "Close"  x3
    "Open"  x3
    "ScrollStart"  x2
data.chatID  (string, 10/10 records)
    "NA"  x5
    "[68-1, 68-2, 68-3, 68-5, 68-10]"  x2
    "[18-179, 68-1, 68-2, 68-3, 68-5, 68-10]"  x1
    "[18-271, 18-273, 18-179, 68-1, 68-2, 68-3]"  x1
    "[18-273, 18-179, 68-1, 68-2, 68-3]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8)
- **Intervals:** median 42.95s (p5 36.01s / p95 5148.80s, n=7)
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

### `Soil Key Puzzle` — 6 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6)
- **Intervals:** median 2.98s (p5 1.07s / p95 108044.75s, n=5)
- **`data` key-set variants:** [Soil Key Puzzle Status, Unit] x4; [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/6 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/6 records)
    "Unit 2 Prod (Refactor)"  x4
data.actionType  (string, 2/6 records)
    "LeftDrag"  x2
data.currentSoilType  (string, 2/6 records)
    "CLAY"  x1
    "CLAYROCK"  x1
data.isCorrectSelection  (string, 2/6 records)
    "false"  x2
data.waterLevelStatus  (string, 2/6 records)
    "Proper"  x2
data.waterRetentionChange  (string, 2/6 records)
    "Increase"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x1
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 4 empty-string)
    ""  x4
    "TypeError: Permissions check failed"  x1
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit2"  x3
    "unit1"  x2
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationAnswerEvent` — 2 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 7459.84s (p5 7459.84s / p95 7459.84s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "submitAnswerEvent"  x2
data.answerSubmitted  (string, 2/2 records)
    "A,1,I"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Freshwater"  x2
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
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationNodeEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now
- `chatEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "Selected" (52x); "Unselected" (30x); "WaypointMoveEvent" (6x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (82x); "Waypoint" (10x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 3 Dev' has no records of this event
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*