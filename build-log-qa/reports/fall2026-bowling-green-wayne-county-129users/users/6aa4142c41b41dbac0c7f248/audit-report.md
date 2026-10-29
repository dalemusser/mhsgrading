# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f248

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4142c41b41dbac0c7f248
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f248.jsonl
- **Records:** 9705 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f248
- **Time span:** 2026-09-23T16:33:16.454000+00:00 .. 2026-10-07T17:07:44.441000+00:00 (336h 34m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f248\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 9705 records, 7 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 99 INFO, 2 NOT_TESTED, 78 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3406 | 35.1 | 1 | 2 | 0 | 2026-09-25T16:43:01.681000+00:00 | 2026-10-07T16:52:05.615000+00:00 | 288h 9m |
| InputEvent | 3005 | 30.96 | 1 | 6 | 0 | 2026-09-23T16:33:41.856000+00:00 | 2026-10-07T17:02:15.244000+00:00 | 336h 28m |
| PlayerPositionEvent | 1528 | 15.74 | 1 | 6 | 0 | 2026-09-23T16:33:36.733000+00:00 | 2026-10-07T17:07:44.441000+00:00 | 336h 34m |
| DialogueEvent | 1150 | 11.85 | 1 | 6 | 727 | 2026-09-23T16:33:58.485000+00:00 | 2026-10-07T17:07:30.508000+00:00 | 336h 33m |
| ObjectInterEvent | 177 | 1.82 | 1 | 6 | 0 | 2026-09-23T16:38:35.958000+00:00 | 2026-10-07T17:02:17.131000+00:00 | 336h 23m |
| argumentationNodeEvent | 108 | 1.11 | 1 | 2 | 0 | 2026-09-23T17:00:43.977000+00:00 | 2026-10-07T17:07:29.209000+00:00 | 336h 6m |
| Soil Key Puzzle | 68 | 0.7 | 1 | 2 | 0 | 2026-09-25T16:55:54.598000+00:00 | 2026-10-05T16:27:29.513000+00:00 | 239h 31m |
| questEvent | 56 | 0.58 | 1 | 6 | 56 | 2026-09-23T16:33:58.461000+00:00 | 2026-10-07T16:56:18.794000+00:00 | 336h 22m |
| TopographicMapEvent | 46 | 0.47 | 1 | 3 | 0 | 2026-09-25T16:36:27.696000+00:00 | 2026-09-30T17:03:52.003000+00:00 | 120h 27m |
| gameWindowFocusEvent | 27 | 0.28 | 1 | 4 | 0 | 2026-09-23T16:33:16.454000+00:00 | 2026-10-07T16:58:40.347000+00:00 | 336h 25m |
| soilMachine | 26 | 0.27 | 1 | 1 | 0 | 2026-10-07T16:41:07.069000+00:00 | 2026-10-07T16:48:48.404000+00:00 | 7m 41s |
| DEBUGMenu | 25 | 0.26 | 1 | 7 | 0 | 2026-09-23T16:33:36.727000+00:00 | 2026-10-07T16:56:17.605000+00:00 | 336h 22m |
| argumentationAnswerEvent | 25 | 0.26 | 1 | 2 | 0 | 2026-09-23T17:03:52.931000+00:00 | 2026-10-07T17:07:30.904000+00:00 | 336h 3m |
| gameStartEvent | 18 | 0.19 | 1 | 1 | 0 | 2026-09-23T16:33:16.454000+00:00 | 2026-10-07T16:37:16.353000+00:00 | 336h 3m |
| gameWindowUnfocusEvent | 15 | 0.15 | 1 | 5 | 0 | 2026-09-23T18:05:14.749000+00:00 | 2026-10-07T16:58:27.251000+00:00 | 334h 53m |
| argumentationEvent | 8 | 0.08 | 1 | 2 | 0 | 2026-09-23T17:01:33.521000+00:00 | 2026-10-07T17:05:51.075000+00:00 | 336h 4m |
| crash | 7 | 0.07 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 6 | 0.06 | 1 | 2 | 0 | 2026-09-30T16:41:58.774000+00:00 | 2026-10-07T16:59:28.746000+00:00 | 168h 17m |
| argumentationToolEvent | 3 | 0.03 | 1 | 1 | 0 | 2026-09-23T17:01:29.619000+00:00 | 2026-09-24T16:44:05.006000+00:00 | 23h 42m |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-24T16:47:12.345000+00:00 | 2026-09-24T16:47:12.345000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 15.285s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 0.427s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 42677.693s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1113.493s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 20981.121s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.478s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev; Unit 5 Dev; Unit 5 Dev - Dungeon 
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
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Place Cameras; Press E To Place Glyph; Press E To Return To Base; Press E to Plant Seed; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Teleporter Room; Toppo's Room 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 25 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,1,; B,C,D,2,I; C,D,B,2,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 27 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 41; 43; 44; 45; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 13 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[123] _id=6ab4012d485cab4c954e7394 ts=2026-09-23T16:41:17.9690000Z`; `6aa4142c41b41dbac0c7f248.jsonl[166] _id=6ab40222485cab4c954e7814 ts=2026-09-23T16:45:21.9820000Z`; `6aa4142c41b41dbac0c7f248.jsonl[221] _id=6ab4035a485cab4c954e7dd6 ts=2026-09-23T16:50:34.9510000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[3] _id=6ab3ff4c485cab4c954e65a0 ts=2026-09-23T16:33:16.4540000Z`; `6aa4142c41b41dbac0c7f248.jsonl[423] _id=6ab5522b485cab4c955329ab ts=2026-09-24T16:39:07.6970000Z`; `6aa4142c41b41dbac0c7f248.jsonl[689] _id=6ab6a1ae485cab4c9559f757 ts=2026-09-25T16:30:38.3530000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[2] _id=6ab3ff4c485cab4c954e659e ts=2026-09-23T16:33:16.4540000Z`; `6aa4142c41b41dbac0c7f248.jsonl[424] _id=6ab5522b485cab4c955329a3 ts=2026-09-24T16:39:07.6960000Z`; `6aa4142c41b41dbac0c7f248.jsonl[688] _id=6ab6a1ae485cab4c9559f74e ts=2026-09-25T16:30:38.3520000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[416] _id=6ab414da485cab4c954f3638 ts=2026-09-23T18:05:14.7490000Z`; `6aa4142c41b41dbac0c7f248.jsonl[868] _id=6ab6a37b485cab4c955b23e3 ts=2026-09-25T16:38:20.1110000Z`; `6aa4142c41b41dbac0c7f248.jsonl[2565] _id=6aba95d2485cab4c956a962d ts=2026-09-28T16:29:06.5080000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 46 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[828] _id=6ab6a30b485cab4c955adcd0 ts=2026-09-25T16:36:27.6960000Z`; `6aa4142c41b41dbac0c7f248.jsonl[831] _id=6ab6a321485cab4c955aea26 ts=2026-09-25T16:36:49.2740000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1025] _id=6ab6a4d1485cab4c955c07d7 ts=2026-09-25T16:44:01.5090000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3405 | 0.0 | 0.024 | 304.653 | 1.043 | 345431.906 | 0.2 | 2217 | 5 |
| InputEvent | 3004 | 0.0 | 0.623 | 403.233 | 13.374 | 344207.902 | 0.15 | 189 | 11 |
| PlayerPositionEvent | 1519 | 9.68 | 9.999 | 571.058 | 10.691 | 257055.154 | 0.11 | 0 | 10 |
| DialogueEvent | 1149 | 0.0 | 5.679 | 1054.493 | 50.031 | 345153.467 | 0.06 | 322 | 9 |
| ObjectInterEvent | 176 | 0.0 | 6.802 | 6880.802 | 468.625 | 345284.676 | 0.01 | 3 | 8 |
| argumentationNodeEvent | 107 | 0.016 | 0.312 | 11308.46 | 41.27 | 1124501.394 | 0.01 | 28 | 2 |
| Soil Key Puzzle | 67 | 0.157 | 0.666 | 12870.073 | 506.412 | 345566.031 | 0.0 | 0 | 4 |
| questEvent | 55 | 0.003 | 225.609 | 22017.097 | 110952.102 | 344758.35 | 0.0 | 8 | 17 |
| TopographicMapEvent | 45 | 0.015 | 15.285 | 9636.54 | 68731.15 | 257399.423 | 0.01 | 2 | 5 |
| gameWindowFocusEvent | 26 | 13.153 | 1113.493 | 46581.688 | 236163.108 | 344749.453 | 0.0 | 0 | 18 |
| soilMachine | 25 | 0.601 | 3.478 | 18.453 | 74.365 | 199.821 | 3.25 | 0 | 0 |
| DEBUGMenu | 24 | 5.974 | 816.966 | 50456.703 | 245266.104 | 344317.864 | 0.0 | 0 | 15 |
| argumentationAnswerEvent | 24 | 0.112 | 0.427 | 50409.082 | 72356.792 | 1124514.779 | 0.0 | 0 | 2 |
| gameStartEvent | 17 | 82.837 | 3031.979 | 71167.053 | 275802.866 | 344749.452 | 0.0 | 0 | 13 |
| gameWindowUnfocusEvent | 14 | 0.468 | 20981.121 | 86113.75 | 318684.082 | 430182.64 | 0.0 | 0 | 11 |
| argumentationEvent | 7 | 16.408 | 75.238 | 172836.793 | 812680.649 | 1124500.567 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 5 | 0.89 | 1.737 | 121169.994 | 484031.885 | 604771.152 | 0.0 | 0 | 2 |
| argumentationToolEvent | 2 | 3.869 | 42677.693 | 42677.694 | 81084.136 | 85351.518 | 0.0 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 15 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[7315] _id=6ac3cbacde269131f9ad94f3 ts=2026-10-05T16:09:15.4900000Z == 6aa4142c41b41dbac0c7f248.jsonl[7334] _id=6ac3cbacde269131f9ad94f5 ts=2026-10-05T16:09:15.4900000Z`; `6aa4142c41b41dbac0c7f248.jsonl[8498] _id=6ac6744dde269131f9bc904e ts=2026-10-07T16:33:17.6690000Z == 6aa4142c41b41dbac0c7f248.jsonl[8499] _id=6ac6744dde269131f9bc904f ts=2026-10-07T16:33:17.6690000Z`; `6aa4142c41b41dbac0c7f248.jsonl[8578] _id=6ac67547de269131f9bcb8de ts=2026-10-07T16:37:27.3030000Z == 6aa4142c41b41dbac0c7f248.jsonl[8579] _id=6ac67547de269131f9bcb8df ts=2026-10-07T16:37:27.3030000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 107 group(s), 151 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[1139] _id=6ab6a640485cab4c955cd6e3 ts=2026-09-25T16:49:50.3310000Z == 6aa4142c41b41dbac0c7f248.jsonl[1140] _id=6ab6a640485cab4c955cd6e7 ts=2026-09-25T16:49:50.3310000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1168] _id=6ab6a641485cab4c955cd71b ts=2026-09-25T16:50:00.6760000Z == 6aa4142c41b41dbac0c7f248.jsonl[1169] _id=6ab6a641485cab4c955cd721 ts=2026-09-25T16:50:00.6760000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1179] _id=6ab6a641485cab4c955cd72a ts=2026-09-25T16:50:01.2710000Z == 6aa4142c41b41dbac0c7f248.jsonl[1180] _id=6ab6a642485cab4c955cd72d ts=2026-09-25T16:50:01.2710000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[2537] _id=6aba95b8485cab4c956a9211 ts=? == 6aa4142c41b41dbac0c7f248.jsonl[4420] _id=6abbee2f485cab4c95828e96 ts=?`; `6aa4142c41b41dbac0c7f248.jsonl[8462] _id=6ac66879de269131f9bc1b62 ts=? == 6aa4142c41b41dbac0c7f248.jsonl[8494] _id=6ac6744dde269131f9bc9047 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4142c41b41dbac0c7f248.jsonl[86] _id=6ab4008b485cab4c954e701e ts=2026-09-23T16:38:35.9580000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[87] _id=6ab4008b485cab4c954e7020 ts=2026-09-23T16:38:35.9630000Z`; `670ms: 6aa4142c41b41dbac0c7f248.jsonl[8958] _id=6ac677afde269131f9bd2b70 ts=2026-10-07T16:47:42.9500000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[8965] _id=6ac677afde269131f9bd2b8e ts=2026-10-07T16:47:43.6200000Z`; `606ms: 6aa4142c41b41dbac0c7f248.jsonl[8965] _id=6ac677afde269131f9bd2b8e ts=2026-10-07T16:47:43.6200000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[8971] _id=6ac677b0de269131f9bd2ba3 ts=2026-10-07T16:47:44.2260000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 367 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: 6aa4142c41b41dbac0c7f248.jsonl[1006] _id=6ab6a4af485cab4c955bf2ec ts=2026-09-25T16:43:26.0790000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[1009] _id=6ab6a4af485cab4c955bf2f9 ts=2026-09-25T16:43:26.0930000Z`; `18ms: 6aa4142c41b41dbac0c7f248.jsonl[1147] _id=6ab6a640485cab4c955cd6dd ts=2026-09-25T16:49:50.3130000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[1139] _id=6ab6a640485cab4c955cd6e3 ts=2026-09-25T16:49:50.3310000Z`; `16ms: 6aa4142c41b41dbac0c7f248.jsonl[1174] _id=6ab6a640485cab4c955cd6f1 ts=2026-09-25T16:49:54.8760000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[1175] _id=6ab6a640485cab4c955cd6f5 ts=2026-09-25T16:49:54.8920000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `534ms: 6aa4142c41b41dbac0c7f248.jsonl[3190] _id=6abbe78c485cab4c9580c786 ts=2026-09-29T16:30:04.0540000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[3189] _id=6abbe78c485cab4c9580c78c ts=2026-09-29T16:30:04.5880000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `24ms: 6aa4142c41b41dbac0c7f248.jsonl[2664] _id=6aba9742485cab4c956ab85d ts=2026-09-28T16:35:14.5810000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[2670] _id=6aba9743485cab4c956ab865 ts=2026-09-28T16:35:14.6050000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `423ms: 6aa4142c41b41dbac0c7f248.jsonl[408] _id=6ab40680485cab4c954e93b8 ts=2026-09-23T17:04:00.1810000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[389] _id=6ab40680485cab4c954e93ba ts=2026-09-23T17:04:00.6040000Z`; `491ms: 6aa4142c41b41dbac0c7f248.jsonl[389] _id=6ab40680485cab4c954e93ba ts=2026-09-23T17:04:00.6040000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[411] _id=6ab40681485cab4c954e93bc ts=2026-09-23T17:04:01.0950000Z`; `136ms: 6aa4142c41b41dbac0c7f248.jsonl[411] _id=6ab40681485cab4c954e93bc ts=2026-09-23T17:04:01.0950000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[390] _id=6ab40681485cab4c954e93be ts=2026-09-23T17:04:01.2310000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 20 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `398ms: 6aa4142c41b41dbac0c7f248.jsonl[343] _id=6ab405bb485cab4c954e8f34 ts=2026-09-23T17:00:43.9770000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[357] _id=6ab405bc485cab4c954e8f40 ts=2026-09-23T17:00:44.3750000Z`; `39ms: 6aa4142c41b41dbac0c7f248.jsonl[348] _id=6ab405bc485cab4c954e8f44 ts=2026-09-23T17:00:44.4110000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[358] _id=6ab405bc485cab4c954e8f46 ts=2026-09-23T17:00:44.4500000Z`; `18ms: 6aa4142c41b41dbac0c7f248.jsonl[351] _id=6ab405bd485cab4c954e8f58 ts=2026-09-23T17:00:45.8100000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[352] _id=6ab405bd485cab4c954e8f5a ts=2026-09-23T17:00:45.8280000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `468ms: 6aa4142c41b41dbac0c7f248.jsonl[4411] _id=6abbee0c485cab4c95828c91 ts=2026-09-29T16:57:48.9430000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[4413] _id=6abbee0e485cab4c95828ce9 ts=2026-09-29T16:57:49.4110000Z`; `786ms: 6aa4142c41b41dbac0c7f248.jsonl[9402] _id=6ac67a32de269131f9bd68b1 ts=2026-10-07T16:58:26.4650000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[9400] _id=6ac67a33de269131f9bd68de ts=2026-10-07T16:58:27.2510000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `671ms: 6aa4142c41b41dbac0c7f248.jsonl[8957] _id=6ac677aede269131f9bd2b6e ts=2026-10-07T16:47:42.9450000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[8960] _id=6ac677afde269131f9bd2b8a ts=2026-10-07T16:47:43.6160000Z`; `606ms: 6aa4142c41b41dbac0c7f248.jsonl[8960] _id=6ac677afde269131f9bd2b8a ts=2026-10-07T16:47:43.6160000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[8967] _id=6ac677b0de269131f9bd2b9f ts=2026-10-07T16:47:44.2220000Z`; `601ms: 6aa4142c41b41dbac0c7f248.jsonl[8977] _id=6ac677b4de269131f9bd2c35 ts=2026-10-07T16:47:48.7540000Z ~ 6aa4142c41b41dbac0c7f248.jsonl[8978] _id=6ac677b5de269131f9bd2c3e ts=2026-10-07T16:47:49.3550000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa4142c41b41dbac0c7f248.jsonl[7235] _id=6abe8aa8485cab4c95ac0424 ts=2026-10-01T16:30:32.4210000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7324] _id=6ac3cba6de269131f9ad949b ts=2026-10-05T16:09:10.2850000Z; 71h 49m: 6aa4142c41b41dbac0c7f248.jsonl[871] _id=6ab6a3a1485cab4c955b3e26 ts=2026-09-25T16:38:57.3220000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2535] _id=6aba95b1485cab4c956a914a ts=2026-09-28T16:28:33.9570000Z; 47h 10m: 6aa4142c41b41dbac0c7f248.jsonl[8179] _id=6ac3d0fade269131f9adc0f5 ts=2026-10-05T16:31:54.6850000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8458] _id=6ac6686ade269131f9bc1aa7 ts=2026-10-07T15:42:34.4450000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 59m 
  - Evidence: 167h 59m: 6aa4142c41b41dbac0c7f248.jsonl[5435] _id=6abd400c485cab4c958edace ts=2026-09-30T16:59:56.2200000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9473] _id=6ac67a6fde269131f9bd6fa7 ts=2026-10-07T16:59:27.3720000Z; 17m 54s: 6aa4142c41b41dbac0c7f248.jsonl[4632] _id=6abd3bd8485cab4c958e56eb ts=2026-09-30T16:42:00.5110000Z -> 6aa4142c41b41dbac0c7f248.jsonl[5432] _id=6abd400b485cab4c958edab5 ts=2026-09-30T16:59:55.3300000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa4142c41b41dbac0c7f248.jsonl[7270] _id=6abe8afb485cab4c95ac09e1 ts=2026-10-01T16:31:55.1690000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7577] _id=6ac3cf3cde269131f9ada56f ts=2026-10-05T16:24:28.6360000Z; 71h 26m: 6aa4142c41b41dbac0c7f248.jsonl[2526] _id=6ab6a98f485cab4c955d3499 ts=2026-09-25T17:04:15.9860000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2602] _id=6aba963c485cab4c956aa1bb ts=2026-09-28T16:30:52.2280000Z; 46h 56m: 6aa4142c41b41dbac0c7f248.jsonl[8451] _id=6ac3d463de269131f9ae0ad5 ts=2026-10-05T16:46:27.0730000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8467] _id=6ac66879de269131f9bc1b6a ts=2026-10-07T15:42:49.5560000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 322 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f248.jsonl[9674] _id=6ac67c0fde269131f9bd94b9 ts=2026-10-07T17:06:23.4600000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9675] _id=6ac67c0fde269131f9bd94ba ts=2026-10-07T17:06:23.4600000Z; 0ms: 6aa4142c41b41dbac0c7f248.jsonl[9686] _id=6ac67c25de269131f9bd94f3 ts=2026-10-07T17:06:45.0170000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9687] _id=6ac67c25de269131f9bd94f4 ts=2026-10-07T17:06:45.0170000Z; 0ms: 6aa4142c41b41dbac0c7f248.jsonl[9699] _id=6ac67c52de269131f9bd9576 ts=2026-10-07T17:07:30.4850000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9700] _id=6ac67c52de269131f9bd9577 ts=2026-10-07T17:07:30.4850000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 36m 
  - Evidence: 95h 36m: 6aa4142c41b41dbac0c7f248.jsonl[7277] _id=6abe8b1b485cab4c95ac0c70 ts=2026-10-01T16:32:27.5870000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7326] _id=6ac3cbacde269131f9ad94ee ts=2026-10-05T16:09:15.4890000Z; 71h 26m: 6aa4142c41b41dbac0c7f248.jsonl[2488] _id=6ab6a906485cab4c955d223d ts=2026-09-25T17:01:58.1900000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2549] _id=6aba95b8485cab4c956a921b ts=2026-09-28T16:28:40.4850000Z; 46h 56m: 6aa4142c41b41dbac0c7f248.jsonl[8455] _id=6ac3d46dde269131f9ae0c3f ts=2026-10-05T16:46:37.1840000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8464] _id=6ac66879de269131f9bc1b67 ts=2026-10-07T15:42:49.4070000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 189 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f248.jsonl[7315] _id=6ac3cbacde269131f9ad94f3 ts=2026-10-05T16:09:15.4900000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7334] _id=6ac3cbacde269131f9ad94f5 ts=2026-10-05T16:09:15.4900000Z; 0ms: 6aa4142c41b41dbac0c7f248.jsonl[8498] _id=6ac6744dde269131f9bc904e ts=2026-10-07T16:33:17.6690000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8499] _id=6ac6744dde269131f9bc904f ts=2026-10-07T16:33:17.6690000Z; 0ms: 6aa4142c41b41dbac0c7f248.jsonl[8578] _id=6ac67547de269131f9bcb8de ts=2026-10-07T16:37:27.3030000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8579] _id=6ac67547de269131f9bcb8df ts=2026-10-07T16:37:27.3030000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 54m 
  - Evidence: 95h 54m: 6aa4142c41b41dbac0c7f248.jsonl[7280] _id=6abe8b18485cab4c95ac0c40 ts=2026-10-01T16:32:24.0210000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7630] _id=6ac3cfdcde269131f9ada8f7 ts=2026-10-05T16:27:08.6970000Z; 95h 34m: 6aa4142c41b41dbac0c7f248.jsonl[2359] _id=6ab6a79a485cab4c955d01a5 ts=2026-09-25T16:55:54.6030000Z -> 6aa4142c41b41dbac0c7f248.jsonl[3180] _id=6abbe782485cab4c9580c681 ts=2026-09-29T16:29:54.6420000Z; 47h 47m: 6aa4142c41b41dbac0c7f248.jsonl[8444] _id=6ac3d44bde269131f9ae07af ts=2026-10-05T16:46:03.0550000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8515] _id=6ac6747ade269131f9bc947f ts=2026-10-07T16:34:02.7250000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f248.jsonl[9574] _id=6ac67b01de269131f9bd8140 ts=2026-10-07T17:01:53.3370000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9575] _id=6ac67b01de269131f9bd8141 ts=2026-10-07T17:01:53.3370000Z; 1ms: 6aa4142c41b41dbac0c7f248.jsonl[9543] _id=6ac67ac7de269131f9bd7a0e ts=2026-10-07T17:00:55.5460000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9544] _id=6ac67ac7de269131f9bd7a0f ts=2026-10-07T17:00:55.5470000Z; 5ms: 6aa4142c41b41dbac0c7f248.jsonl[86] _id=6ab4008b485cab4c954e701e ts=2026-09-23T16:38:35.9580000Z -> 6aa4142c41b41dbac0c7f248.jsonl[87] _id=6ab4008b485cab4c954e7020 ts=2026-09-23T16:38:35.9630000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 71h 24m 
  - Evidence: 71h 24m: 6aa4142c41b41dbac0c7f248.jsonl[2528] _id=6ab6a992485cab4c955d34c9 ts=2026-09-25T17:04:18.8120000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2538] _id=6aba95b8485cab4c956a9217 ts=2026-09-28T16:28:33.9660000Z; 46h 56m: 6aa4142c41b41dbac0c7f248.jsonl[8454] _id=6ac3d46ade269131f9ae0bdf ts=2026-10-05T16:46:34.8030000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8463] _id=6ac66879de269131f9bc1b66 ts=2026-10-07T15:42:44.1980000Z; 23h 46m: 6aa4142c41b41dbac0c7f248.jsonl[686] _id=6ab55409485cab4c95534c95 ts=2026-09-24T16:47:05.7570000Z -> 6aa4142c41b41dbac0c7f248.jsonl[691] _id=6ab6a250485cab4c955a628d ts=2026-09-25T16:33:19.8070000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4142c41b41dbac0c7f248.jsonl[7232] _id=6abe8a9e485cab4c95ac032e ts=2026-10-01T16:30:19.8710000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7666] _id=6ac3cff4de269131f9adaa09 ts=2026-10-05T16:27:31.7770000Z; 95h 34m: 6aa4142c41b41dbac0c7f248.jsonl[2354] _id=6ab6a792485cab4c955d011b ts=2026-09-25T16:55:45.2090000Z -> 6aa4142c41b41dbac0c7f248.jsonl[3205] _id=6abbe79b485cab4c9580c9e1 ts=2026-09-29T16:30:18.8800000Z; 48h 19m: 6aa4142c41b41dbac0c7f248.jsonl[8162] _id=6ac3d07bde269131f9adb797 ts=2026-10-05T16:29:46.5330000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9016] _id=6ac6781ade269131f9bd34a3 ts=2026-10-07T16:49:29.1110000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2217 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f248.jsonl[1002] _id=6ab6a4ad485cab4c955bf20a ts=2026-09-25T16:43:25.5070000Z -> 6aa4142c41b41dbac0c7f248.jsonl[1004] _id=6ab6a4ad485cab4c955bf213 ts=2026-09-25T16:43:25.5070000Z; 0ms: 6aa4142c41b41dbac0c7f248.jsonl[1004] _id=6ab6a4ad485cab4c955bf213 ts=2026-09-25T16:43:25.5070000Z -> 6aa4142c41b41dbac0c7f248.jsonl[1003] _id=6ab6a4ad485cab4c955bf21c ts=2026-09-25T16:43:25.5070000Z; 0ms: 6aa4142c41b41dbac0c7f248.jsonl[1068] _id=6ab6a63c485cab4c955cd609 ts=2026-09-25T16:43:27.9070000Z -> 6aa4142c41b41dbac0c7f248.jsonl[1117] _id=6ab6a63c485cab4c955cd60d ts=2026-09-25T16:43:27.9070000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 59m 
  - Evidence: 95h 59m: 6aa4142c41b41dbac0c7f248.jsonl[6563] _id=6abe89fe485cab4c95abed26 ts=2026-10-01T16:27:42.6630000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7623] _id=6ac3cfdcde269131f9ada8f5 ts=2026-10-05T16:27:08.6940000Z; 95h 33m: 6aa4142c41b41dbac0c7f248.jsonl[2361] _id=6ab6a79d485cab4c955d01b5 ts=2026-09-25T16:55:57.5760000Z -> 6aa4142c41b41dbac0c7f248.jsonl[3184] _id=6abbe782485cab4c9580c67d ts=2026-09-29T16:29:54.6360000Z; 47h 44m: 6aa4142c41b41dbac0c7f248.jsonl[3200] _id=6abbe797485cab4c9580c987 ts=2026-09-29T16:30:15.2070000Z -> 6aa4142c41b41dbac0c7f248.jsonl[5768] _id=6abe8704485cab4c95abcd2e ts=2026-10-01T16:15:00.8540000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 71h 29m 
  - Evidence: 71h 29m: 6aa4142c41b41dbac0c7f248.jsonl[2529] _id=6ab6a990485cab4c955d349f ts=2026-09-25T17:04:16.0080000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2651] _id=6aba9707485cab4c956ab5c4 ts=2026-09-28T16:34:15.4310000Z; 24h 0m: 6aa4142c41b41dbac0c7f248.jsonl[2926] _id=6aba9b24485cab4c956ad7a7 ts=2026-09-28T16:51:48.6200000Z -> 6aa4142c41b41dbac0c7f248.jsonl[4277] _id=6abbecaa485cab4c9581f8ce ts=2026-09-29T16:51:54.8100000Z; 23h 48m: 6aa4142c41b41dbac0c7f248.jsonl[4282] _id=6abbecba485cab4c9581ff87 ts=2026-09-29T16:52:10.0950000Z -> 6aa4142c41b41dbac0c7f248.jsonl[4603] _id=6abd3b6e485cab4c958e31d3 ts=2026-09-30T16:40:14.7260000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.015s..0.024s shown 
  - Evidence: 15ms: 6aa4142c41b41dbac0c7f248.jsonl[2667] _id=6aba9742485cab4c956ab85b ts=2026-09-28T16:35:14.5660000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2664] _id=6aba9742485cab4c956ab85d ts=2026-09-28T16:35:14.5810000Z; 24ms: 6aa4142c41b41dbac0c7f248.jsonl[2664] _id=6aba9742485cab4c956ab85d ts=2026-09-28T16:35:14.5810000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2670] _id=6aba9743485cab4c956ab865 ts=2026-09-28T16:35:14.6050000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 312h 21m 
  - Evidence: 312h 21m: 6aa4142c41b41dbac0c7f248.jsonl[572] _id=6ab5535a485cab4c9553452b ts=2026-09-24T16:44:10.4900000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9668] _id=6ac67bfdde269131f9bd9415 ts=2026-10-07T17:06:05.2690000Z; 23h 38m: 6aa4142c41b41dbac0c7f248.jsonl[395] _id=6ab40682485cab4c954e93d4 ts=2026-09-23T17:04:02.7140000Z -> 6aa4142c41b41dbac0c7f248.jsonl[521] _id=6ab552f7485cab4c95533e27 ts=2026-09-24T16:42:31.5120000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 312h 21m 
  - Evidence: 312h 21m: 6aa4142c41b41dbac0c7f248.jsonl[569] _id=6ab5535a485cab4c9553452d ts=2026-09-24T16:44:10.5080000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9647] _id=6ac67befde269131f9bd9378 ts=2026-10-07T17:05:51.0750000Z; 23h 38m: 6aa4142c41b41dbac0c7f248.jsonl[406] _id=6ab40676485cab4c954e938a ts=2026-09-23T17:03:50.5590000Z -> 6aa4142c41b41dbac0c7f248.jsonl[499] _id=6ab552e3485cab4c95533c23 ts=2026-09-24T16:42:11.3980000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 312h 21m 
  - Evidence: 312h 21m: 6aa4142c41b41dbac0c7f248.jsonl[566] _id=6ab55353485cab4c955344ad ts=2026-09-24T16:44:03.6950000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9643] _id=6ac67be9de269131f9bd9327 ts=2026-10-07T17:05:45.0890000Z; 23h 38m: 6aa4142c41b41dbac0c7f248.jsonl[382] _id=6ab40629485cab4c954e924c ts=2026-09-23T17:02:33.6310000Z -> 6aa4142c41b41dbac0c7f248.jsonl[470] _id=6ab552b3485cab4c955337eb ts=2026-09-24T16:41:23.4410000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 28 interval(s) ≤ 0.016s..0.018s shown 
  - Evidence: 16ms: 6aa4142c41b41dbac0c7f248.jsonl[508] _id=6ab552f1485cab4c95533da9 ts=2026-09-24T16:42:25.7920000Z -> 6aa4142c41b41dbac0c7f248.jsonl[514] _id=6ab552f1485cab4c95533dab ts=2026-09-24T16:42:25.8080000Z; 18ms: 6aa4142c41b41dbac0c7f248.jsonl[351] _id=6ab405bd485cab4c954e8f58 ts=2026-09-23T17:00:45.8100000Z -> 6aa4142c41b41dbac0c7f248.jsonl[352] _id=6ab405bd485cab4c954e8f5a ts=2026-09-23T17:00:45.8280000Z; 18ms: 6aa4142c41b41dbac0c7f248.jsonl[512] _id=6ab552f0485cab4c95533d8a ts=2026-09-24T16:42:24.8100000Z -> 6aa4142c41b41dbac0c7f248.jsonl[510] _id=6ab552f0485cab4c95533d8d ts=2026-09-24T16:42:24.8280000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 42m 
  - Evidence: 23h 42m: 6aa4142c41b41dbac0c7f248.jsonl[366] _id=6ab405ed485cab4c954e90ea ts=2026-09-23T17:01:33.4880000Z -> 6aa4142c41b41dbac0c7f248.jsonl[539] _id=6ab55355485cab4c955344c1 ts=2026-09-24T16:44:05.0060000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 45m 
  - Evidence: 95h 45m: 6aa4142c41b41dbac0c7f248.jsonl[6355] _id=6abe88e8485cab4c95abdae2 ts=2026-10-01T16:23:03.8990000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7318] _id=6ac3cb95de269131f9ad9429 ts=2026-10-05T16:08:53.3510000Z; 71h 49m: 6aa4142c41b41dbac0c7f248.jsonl[870] _id=6ab6a39b485cab4c955b3a7f ts=2026-09-25T16:38:51.6350000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2533] _id=6aba95a1485cab4c956a8f50 ts=2026-09-28T16:28:17.8540000Z; 47h 21m: 6aa4142c41b41dbac0c7f248.jsonl[7535] _id=6ac3ce80de269131f9ada383 ts=2026-10-05T16:21:20.2230000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8460] _id=6ac6686ade269131f9bc1ab3 ts=2026-10-07T15:42:34.8830000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 45m 
  - Evidence: 95h 45m: 6aa4142c41b41dbac0c7f248.jsonl[6354] _id=6abe88e7485cab4c95abdae0 ts=2026-10-01T16:23:03.8980000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7317] _id=6ac3cb95de269131f9ad9425 ts=2026-10-05T16:08:53.3510000Z; 71h 49m: 6aa4142c41b41dbac0c7f248.jsonl[869] _id=6ab6a39b485cab4c955b3a59 ts=2026-09-25T16:38:51.6330000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2534] _id=6aba95a1485cab4c956a8f4c ts=2026-09-28T16:28:17.8530000Z; 46h 55m: 6aa4142c41b41dbac0c7f248.jsonl[8457] _id=6ac3d471de269131f9ae0cb7 ts=2026-10-05T16:46:41.1100000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8459] _id=6ac6686ade269131f9bc1ab2 ts=2026-10-07T15:42:34.8830000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 29m 
  - Evidence: 119h 29m: 6aa4142c41b41dbac0c7f248.jsonl[5648] _id=6abd4193485cab4c958ef90c ts=2026-09-30T17:06:27.4470000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8258] _id=6ac3d1fade269131f9add71d ts=2026-10-05T16:36:10.0870000Z; 71h 50m: 6aa4142c41b41dbac0c7f248.jsonl[868] _id=6ab6a37b485cab4c955b23e3 ts=2026-09-25T16:38:20.1110000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2565] _id=6aba95d2485cab4c956a962d ts=2026-09-28T16:29:06.5080000Z; 48h 11m: 6aa4142c41b41dbac0c7f248.jsonl[8456] _id=6ac3d471de269131f9ae0cb4 ts=2026-10-05T16:46:41.0290000Z -> 6aa4142c41b41dbac0c7f248.jsonl[9402] _id=6ac67a32de269131f9bd68b1 ts=2026-10-07T16:58:26.4650000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 45m 
  - Evidence: 95h 45m: 6aa4142c41b41dbac0c7f248.jsonl[6391] _id=6abe88f8485cab4c95abdbf6 ts=2026-10-01T16:23:17.1940000Z -> 6aa4142c41b41dbac0c7f248.jsonl[7331] _id=6ac3cbadde269131f9ad9537 ts=2026-10-05T16:09:15.5440000Z; 71h 25m: 6aa4142c41b41dbac0c7f248.jsonl[2520] _id=6ab6a96c485cab4c955d3131 ts=2026-09-25T17:03:40.2160000Z -> 6aa4142c41b41dbac0c7f248.jsonl[2553] _id=6aba95ba485cab4c956a925b ts=2026-09-28T16:28:40.5360000Z; 46h 57m: 6aa4142c41b41dbac0c7f248.jsonl[8440] _id=6ac3d43bde269131f9ae0595 ts=2026-10-05T16:45:47.1030000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8466] _id=6ac66879de269131f9bc1b69 ts=2026-10-07T15:42:49.4300000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.003s..0.005s shown 
  - Evidence: 3ms: 6aa4142c41b41dbac0c7f248.jsonl[334] _id=6ab4058a485cab4c954e8e1e ts=2026-09-23T16:59:53.9780000Z -> 6aa4142c41b41dbac0c7f248.jsonl[331] _id=6ab4058a485cab4c954e8e20 ts=2026-09-23T16:59:53.9810000Z; 3ms: 6aa4142c41b41dbac0c7f248.jsonl[456] _id=6ab55284485cab4c955333f9 ts=2026-09-24T16:40:36.3950000Z -> 6aa4142c41b41dbac0c7f248.jsonl[457] _id=6ab55284485cab4c955333fb ts=2026-09-24T16:40:36.3980000Z; 5ms: 6aa4142c41b41dbac0c7f248.jsonl[8870] _id=6ac67738de269131f9bd15b8 ts=2026-10-07T16:45:44.5930000Z -> 6aa4142c41b41dbac0c7f248.jsonl[8871] _id=6ac67738de269131f9bd15ba ts=2026-10-07T16:45:44.5980000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[325] _id=6ab40569485cab4c954e8d64 ts=2026-09-23T16:59:21.2990000Z`; `6aa4142c41b41dbac0c7f248.jsonl[580] _id=6ab55376485cab4c95534729 ts=2026-09-24T16:44:37.9240000Z`; `6aa4142c41b41dbac0c7f248.jsonl[2930] _id=6aba9b23485cab4c956ad79e ts=2026-09-28T16:51:47.4600000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 58 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[1335] _id=6ab6a66e485cab4c955cdbdf ts=2026-09-25T16:50:53.3980000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1617] _id=6ab6a698485cab4c955ce355 ts=2026-09-25T16:51:35.7820000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1614] _id=6ab6a698485cab4c955ce35b ts=2026-09-25T16:51:35.8060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 239 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[1104] _id=6ab6a63b485cab4c955cd5cf ts=2026-09-25T16:43:01.7330000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1009] _id=6ab6a4af485cab4c955bf2f9 ts=2026-09-25T16:43:26.0930000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1117] _id=6ab6a63c485cab4c955cd60d ts=2026-09-25T16:43:27.9070000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[510] _id=6ab552f0485cab4c95533d8d ts=2026-09-24T16:42:24.8280000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[8317] _id=6ac3d2ffde269131f9adec75 ts=2026-10-05T16:40:31.6920000Z`; `6aa4142c41b41dbac0c7f248.jsonl[8477] _id=6ac668adde269131f9bc1d7a ts=2026-10-07T15:43:41.9310000Z`; `6aa4142c41b41dbac0c7f248.jsonl[8508] _id=6ac6746ade269131f9bc92dd ts=2026-10-07T16:33:46.6760000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 7 records 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[2537] _id=6aba95b8485cab4c956a9211 ts=?`; `6aa4142c41b41dbac0c7f248.jsonl[3086] _id=6abbe6fa485cab4c9580c045 ts=?`; `6aa4142c41b41dbac0c7f248.jsonl[4420] _id=6abbee2f485cab4c95828e96 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 511 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[1264] _id=6ab6a661485cab4c955cda5f ts=2026-09-25T16:50:41.1630000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1259] _id=6ab6a661485cab4c955cda7b ts=2026-09-25T16:50:41.4690000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1275] _id=6ab6a663485cab4c955cdaa5 ts=2026-09-25T16:50:42.5130000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 618 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[1106] _id=6ab6a63b485cab4c955cd5e0 ts=2026-09-25T16:43:02.2370000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1004] _id=6ab6a4ad485cab4c955bf213 ts=2026-09-25T16:43:25.5070000Z`; `6aa4142c41b41dbac0c7f248.jsonl[1127] _id=6ab6a63c485cab4c955cd61d ts=2026-09-25T16:43:28.2160000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 18 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[2651] _id=6aba9707485cab4c956ab5c4 ts=2026-09-28T16:34:15.4310000Z`; `6aa4142c41b41dbac0c7f248.jsonl[2664] _id=6aba9742485cab4c956ab85d ts=2026-09-28T16:35:14.5810000Z`; `6aa4142c41b41dbac0c7f248.jsonl[2670] _id=6aba9743485cab4c956ab865 ts=2026-09-28T16:35:14.6050000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[548] _id=6ab5534a485cab4c95534415 ts=2026-09-24T16:43:54.1000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 25 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[358] _id=6ab405bc485cab4c954e8f46 ts=2026-09-23T17:00:44.4500000Z`; `6aa4142c41b41dbac0c7f248.jsonl[350] _id=6ab405bd485cab4c954e8f54 ts=2026-09-23T17:00:45.7740000Z`; `6aa4142c41b41dbac0c7f248.jsonl[351] _id=6ab405bd485cab4c954e8f58 ts=2026-09-23T17:00:45.8100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'DialogueStartEvent' (totals: 214 start, 209 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 106 unmatched 'BecameCameraCentered' (totals: 677 open, 629 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 99 unmatched 'BecameVisible' (totals: 980 open, 1120 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 21 open, 18 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 5 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 51 open, 49 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 35 start, 21 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 232 of 9697 adjacent _id pairs reverse in client time; worst 43252.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f248.jsonl[4434] _id=6abbef9f485cab4c9582b22f ts=2026-09-29T17:04:29.5330000Z`; `6aa4142c41b41dbac0c7f248.jsonl[4439] _id=6abd3817485cab4c958d9cfa ts=2026-09-29T05:03:37.562Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -127341.73s, max +0.20s over 9698 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4142c41b41dbac0c7f248\coverage.yaml

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
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 7 records 
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

### `PuzzlePieceVisibleEvent` — 3406 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1782); Unit 4 Dev (1624)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.04s, n=3405)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3406/3406 records)
    "BecameInvisible"  x1120
    "BecameVisible"  x980
    "BecameCameraCentered"  x677
    "BecameCameraUncentered"  x629
data.pieceId  (string, 3406/3406 records)
    27 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3406/3406 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3005 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (804); Unit 2 Prod (Refactor) (679); Unit 4 Dev (640); Unit 4 Dev - Dungeon (425); Unit 1 Dev (249); Unit 4 Dev - Anderson Base (208)
- **Intervals:** median 0.62s (p5 0.03s / p95 13.37s, n=3004)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3005/3005 records)
    "pressed"  x3005
data.actionType  (string, 3005/3005 records)
    "Move"  x1596
    "Jump"  x917
    "Interact"  x305
    "Ascend"  x75
    "Sprint"  x54
    "Hoverboard"  x39
    "Map"  x13
    "Pause"  x3
    "Descend"  x2
    "ToggleDebug"  x1
data.key  (string, 3005/3005 records, 8 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3005/3005 records)
    "Player"  x2155
    "Drone"  x850
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1528 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (555); Unit 1 Dev (255); Unit 4 Dev - Dungeon (233); Unit 4 Dev (223); Unit 3 Dev (193); Unit 4 Dev - Anderson Base (69)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.69s, n=1519)
- **Fields under `data`:**

```text
data.position  (object, 1528/1528 records)
data.position.x  (number, 1528/1528 records)
    numeric range -112.353 .. 1587.08 (447 unique)
data.position.y  (number, 1528/1528 records)
    numeric range -115.417 .. 160.085 (359 unique)
data.position.z  (number, 1528/1528 records)
    numeric range -720.927 .. 1964.78 (448 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1150 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (466); Unit 1 Dev (215); Unit 4 Dev (149); Unit 4 Dev - Dungeon (126); Unit 3 Dev (121); Unit 4 Dev - Anderson Base (73)
- **eventKey:** present on 727 of 1150 records
- **Intervals:** median 5.68s (p5 0.00s / p95 50.03s, n=1149)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x727; [conversationId, dialogueEventType] x423
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1150/1150 records)
    numeric range 8 .. 107 (30 unique)
data.dialogueEventType  (string, 1150/1150 records)
    "DialogueNodeEvent"  x727
    "DialogueStartEvent"  x214
    "DialogueFinishEvent"  x209
data.nodeId  (number, 727/1150 records)
    numeric range 0 .. 290 (175 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 177 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (94); Unit 2 Prod (Refactor) (48); Unit 1 Dev (11); Unit 4 Dev (10); Unit 4 Dev - Anderson Base (9); Unit 3 Dev (5)
- **Intervals:** median 6.80s (p5 1.11s / p95 468.62s, n=176)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 177/177 records)
    28 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 177/177 records)
    70 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 108 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (75); Unit 4 Dev - Anderson Base (33)
- **Intervals:** median 0.31s (p5 0.02s / p95 41.27s, n=107)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 108/108 records)
    "argumentationNodeHoverStart"  x51
    "argumentationNodeHoverEnd"  x49
    "argumentationNodeAdd"  x8
data.argumentationTitle  (string, 108/108 records)
    "Unit 1 - Argumentation Tutorial"  x58
    "Unit 4 - Flooding"  x33
    "Unit 1 - Freshwater"  x17
data.nodeName  (string, 108/108 records)
    "I"  x32
    "1"  x24
    "A"  x18
    "B"  x9
    "C"  x9
    "II"  x6
    "2"  x5
    "D"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 68 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (52); Unit 2 Prod (Refactor) (16)
- **Intervals:** median 0.67s (p5 0.18s / p95 506.41s, n=67)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/68 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/68 records)
    "Unit 4 Dev"  x6
    "Unit 2 Prod (Refactor)"  x4
data.actionType  (string, 58/68 records)
    "RightDrag"  x31
    "LeftDrag"  x27
data.currentSoilType  (string, 58/68 records)
    "SAND"  x12
    "CLAYSAND"  x11
    "CLAY"  x9
    "CLAYROCK"  x9
    "SANDGRAVEL"  x8
    "GRAVEL"  x5
    "BEDROCK"  x4
data.isCorrectSelection  (string, 58/68 records)
    "false"  x45
    "true"  x13
data.waterLevelStatus  (string, 58/68 records)
    "Proper"  x25
    "TooLow"  x23
    "TooHigh"  x10
data.waterRetentionChange  (string, 58/68 records)
    "Increase"  x23
    "Decrease"  x22
    "NoChange"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 56 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (15); Unit 2 Prod (Refactor) (15); Unit 4 Dev - Dungeon (14); Unit 4 Dev (7); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 56 of 56 records
- **Intervals:** median 225.61s (p5 0.01s / p95 110952.10s, n=55)
- **`data` key-set variants:** [questEventType, questID, questName] x35; [questEventType, questID, questName, questSuccessOrFailure] x21
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 56/56 records)
    "questActiveEvent"  x35
    "questFinishEvent"  x21
data.questID  (string, 56/56 records)
    21 unique values (see csv/event_unique_values.csv)
data.questName  (string, 56/56 records)
    21 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 21/56 records)
    "Succeeded"  x21
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 46 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (27); Unit 2 Prod (Refactor) (15); Unit 1 Dev (4)
- **Intervals:** median 15.29s (p5 0.73s / p95 68731.15s, n=45)
- **`data` key-set variants:** [actionType, featureUsed] x39; [actionType, featureUsed, location] x5; [actionType, featureUsed, legendName] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "MapOpenEvent"  x21
    "MapCloseEvent"  x18
    "Selected"  x2
    "WaypointMoveEvent"  x2
    "WaypointSetEvent"  x2
    "WaypointResetEvent"  x1
data.featureUsed  (string, 46/46 records)
    "Map"  x39
    "Waypoint"  x5
    "Legend"  x2
data.legendName  (string, 2/46 records)
    "Teleporter Room"  x1
    "Toppo's Room"  x1
data.location  (object, 5/46 records)
data.location.x  (number, 5/46 records)
    4 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/46 records)
    4 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/46 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 27 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (5); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1113.49s (p5 35.02s / p95 236163.11s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    true  x27
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 3.48s (p5 0.61s / p95 74.36s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Bedrock"  x10
    "Clay"  x10
    "Gravel"  x3
    "Sand"  x3
data.floor  (string, 26/26 records)
    "5"  x19
    "4"  x6
    "3"  x1
data.machine  (string, 26/26 records)
    "1"  x24
    "2"  x2
data.row  (string, 26/26 records)
    "TopRow"  x19
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 25 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (6); Unit 2 Prod (Refactor) (5); Unit 4 Dev - Dungeon (5); MainMenu (3); Unit 1 Dev (3); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 816.97s (p5 6.74s / p95 245266.10s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "DebugMenuStateChanged"  x25
data.isOpened  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 25 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (18); Unit 4 Dev - Anderson Base (7)
- **Intervals:** median 0.43s (p5 0.12s / p95 72356.79s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "submitAnswerEvent"  x25
data.answerSubmitted  (string, 25/25 records, 14 empty-string)
    ""  x14
    "B,C,D,2,I"  x6
    "A,1,I"  x3
    "A,1,"  x1
    "C,D,B,2,I"  x1
data.argumentationTitle  (string, 25/25 records)
    "Unit 1 - Freshwater"  x17
    "Unit 4 - Flooding"  x7
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 3031.98s (p5 216.16s / p95 275802.87s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 4 Dev (1)
- **Intervals:** median 20981.12s (p5 0.67s / p95 318684.08s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 75.24s (p5 19.72s / p95 812680.65s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionOpen"  x5
    "argumentationSessionClose"  x3
data.argumentationDescription  (string, 8/8 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 7 records

- **Scenes:** <missing sceneName> (7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 7/7 records)
    true  x7
data.message  (string, 7/7 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x3
data.phase  (string, 7/7 records)
    "running"  x7
data.stack  (string, 7/7 records, 4 empty-string)
    ""  x4
    "TypeError: Permissions check failed"  x3
data.type  (string, 7/7 records)
    "unhandled_rejection"  x7
data.unitId  (string, 7/7 records)
    "unit2"  x3
    "unit4"  x3
    "unit3"  x1
data.workspace  (string, 7/7 records)
    "mhs"  x7
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 1.74s (p5 0.99s / p95 484031.89s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3)
- **Intervals:** median 42677.69s (p5 4271.25s / p95 81084.14s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationToolOpen"  x2
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 3/3 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 3/3 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
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
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (16 records)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (2x); "WaypointResetEvent" (1x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (5x)
- `soilMachine` data.canisterType: "Bedrock" (10x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*