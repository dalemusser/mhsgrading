# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9dc9a8420a1e6b56bb6

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9dc9a8420a1e6b56bb6
- **Game version string(s) in log:** 2.8.4, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9dc9a8420a1e6b56bb6.jsonl
- **Records:** 13876 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9dc9a8420a1e6b56bb6
- **Time span:** 2026-10-07T18:48:37.190000+00:00 .. 2026-10-19T16:11:00.982000+00:00 (285h 22m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9dc9a8420a1e6b56bb6\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 13876 records, 8 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 98 INFO, 2 NOT_TESTED, 83 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4080 | 29.4 | 1 | 6 | 0 | 2026-10-07T18:49:04.776000+00:00 | 2026-10-19T16:11:00.982000+00:00 | 285h 21m |
| PuzzlePieceVisibleEvent | 3828 | 27.59 | 1 | 3 | 0 | 2026-10-13T19:08:01.443000+00:00 | 2026-10-15T19:06:56.603000+00:00 | 47h 58m |
| PlayerPositionEvent | 2836 | 20.44 | 1 | 6 | 0 | 2026-10-07T18:49:01.288000+00:00 | 2026-10-19T16:10:53.085000+00:00 | 285h 21m |
| DialogueEvent | 1938 | 13.97 | 1 | 6 | 1211 | 2026-10-07T18:49:21.370000+00:00 | 2026-10-19T16:10:07.096000+00:00 | 285h 20m |
| ObjectInterEvent | 421 | 3.03 | 1 | 6 | 0 | 2026-10-07T18:59:15.514000+00:00 | 2026-10-19T16:10:48.432000+00:00 | 285h 11m |
| argumentationNodeEvent | 250 | 1.8 | 1 | 3 | 0 | 2026-10-08T19:11:21.621000+00:00 | 2026-10-14T22:40:19.450000+00:00 | 147h 28m |
| Soil Key Puzzle | 102 | 0.74 | 1 | 3 | 0 | 2026-10-13T19:14:50.015000+00:00 | 2026-10-15T19:03:35.656000+00:00 | 47h 48m |
| TopographicMapEvent | 99 | 0.71 | 1 | 3 | 0 | 2026-10-13T18:38:48.472000+00:00 | 2026-10-14T23:47:32.489000+00:00 | 29h 8m |
| questEvent | 97 | 0.7 | 1 | 6 | 97 | 2026-10-07T18:49:21.332000+00:00 | 2026-10-19T16:09:30.874000+00:00 | 285h 20m |
| soilMachine | 46 | 0.33 | 1 | 1 | 0 | 2026-10-19T00:24:27.363000+00:00 | 2026-10-19T01:45:15.472000+00:00 | 1h 20m |
| DEBUGMenu | 44 | 0.32 | 1 | 7 | 0 | 2026-10-07T18:48:37.190000+00:00 | 2026-10-19T16:09:18.346000+00:00 | 285h 20m |
| gameWindowFocusEvent | 27 | 0.19 | 1 | 3 | 0 | 2026-10-07T18:48:37.525000+00:00 | 2026-10-19T16:09:09.564000+00:00 | 285h 20m |
| argumentationAnswerEvent | 25 | 0.18 | 1 | 3 | 0 | 2026-10-08T19:12:19.564000+00:00 | 2026-10-14T22:40:21.285000+00:00 | 147h 28m |
| gameStartEvent | 21 | 0.15 | 1 | 1 | 0 | 2026-10-07T18:48:37.525000+00:00 | 2026-10-19T16:09:09.564000+00:00 | 285h 20m |
| argumentationToolEvent | 16 | 0.12 | 1 | 3 | 0 | 2026-10-08T19:12:04.106000+00:00 | 2026-10-14T22:39:19.979000+00:00 | 147h 27m |
| gameWindowUnfocusEvent | 15 | 0.11 | 1 | 4 | 0 | 2026-10-08T19:18:09.513000+00:00 | 2026-10-19T01:46:48.633000+00:00 | 246h 28m |
| argumentationEvent | 13 | 0.09 | 1 | 3 | 0 | 2026-10-08T19:12:06.394000+00:00 | 2026-10-14T22:40:21.337000+00:00 | 147h 28m |
| DaniEvent | 12 | 0.09 | 1 | 2 | 0 | 2026-10-13T18:37:41.247000+00:00 | 2026-10-14T16:00:11.814000+00:00 | 21h 22m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-10-13T19:02:47.118000+00:00 | 2026-10-15T00:04:21.515000+00:00 | 29h 1m |
| chatEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-13T18:48:09.024000+00:00 | 2026-10-13T18:48:12.042000+00:00 | 3.0s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 158.587s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 52247.198s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.834s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.407s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.063s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.219s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 2.01s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.639s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3.018s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1908.585s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2021.818s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.7x vs baseline. 
  - Observed: 44 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 30 ft; 60 ft; Jasper's Room; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 25 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,5,II; D,1,II; D,A,1,II 
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
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [31-21, 31-23, 31-24, 31-29, 31-32] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
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
  - Observed: 36; 40; 41; 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 9.2x vs baseline. 
  - Observed: 46 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[4] _id=6ac69406de269131f9be1b78 ts=2026-10-07T18:48:37.5250000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[463] _id=6ac7e5b0de269131f9c58c2b ts=2026-10-08T18:49:19.2920000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1114] _id=6ace7a48de269131f9d0fbd9 ts=2026-10-13T18:36:55.8380000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[3] _id=6ac69406de269131f9be1b77 ts=2026-10-07T18:48:37.5250000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[461] _id=6ac7e5b0de269131f9c58c2a ts=2026-10-08T18:49:19.2920000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1113] _id=6ace7a48de269131f9d0fbd8 ts=2026-10-13T18:36:55.8380000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[1111] _id=6ace7a47de269131f9d0fbd1 ts=2026-10-08T19:18:09.513Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[2956] _id=6aced678de269131f9d28f67 ts=2026-10-13T19:17:47.986Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[4022] _id=6acedca6de269131f9d29781 ts=2026-10-14T01:36:38.1270000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 8 of 99 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[1234] _id=6ace7ab8de269131f9d103c4 ts=2026-10-13T18:38:48.4720000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1240] _id=6ace7ac4de269131f9d104a3 ts=2026-10-13T18:39:00.4370000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1276] _id=6ace7adcde269131f9d106c4 ts=2026-10-13T18:39:24.3280000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4079 | 0.0 | 1.834 | 251.855 | 21.99 | 429575.836 | 0.24 | 92 | 11 |
| PuzzlePieceVisibleEvent | 3827 | 0.0 | 0.063 | 45.136 | 2.394 | 71950.81 | 1.33 | 1744 | 7 |
| PlayerPositionEvent | 2829 | 2.137 | 10.001 | 339.033 | 10.087 | 429545.766 | 0.18 | 0 | 9 |
| DialogueEvent | 1937 | 0.0 | 4.414 | 530.328 | 62.654 | 429717.847 | 0.11 | 522 | 12 |
| ObjectInterEvent | 420 | 0.0 | 12.407 | 2444.507 | 300.901 | 429593.288 | 0.02 | 4 | 15 |
| argumentationNodeEvent | 249 | 0.004 | 0.7 | 2132.28 | 9.522 | 430920.737 | 0.03 | 21 | 3 |
| Soil Key Puzzle | 101 | 0.002 | 0.965 | 1704.214 | 8.614 | 74820.284 | 0.04 | 2 | 3 |
| TopographicMapEvent | 98 | 0.016 | 4.219 | 1070.653 | 1580.704 | 50504.617 | 0.06 | 4 | 7 |
| questEvent | 96 | 0.001 | 234.012 | 10700.099 | 50916.015 | 429923.127 | 0.01 | 23 | 23 |
| soilMachine | 45 | 3.372 | 36.529 | 107.736 | 396.573 | 816.077 | 0.56 | 0 | 1 |
| DEBUGMenu | 43 | 7.053 | 158.587 | 23889.329 | 84809.597 | 431242.278 | 0.0 | 0 | 19 |
| gameWindowFocusEvent | 26 | 0.368 | 1908.585 | 39508.925 | 210396.777 | 431256.546 | 0.0 | 0 | 19 |
| argumentationAnswerEvent | 24 | 0.136 | 2.01 | 22120.072 | 75096.706 | 430966.729 | 0.0 | 0 | 3 |
| gameStartEvent | 20 | 82.324 | 4594.757 | 51361.602 | 261811.666 | 431256.546 | 0.0 | 0 | 17 |
| argumentationToolEvent | 15 | 1.069 | 3.639 | 35389.058 | 189539.905 | 431037.747 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 14 | 0.351 | 2021.818 | 63379.937 | 330106.312 | 431978.473 | 0.0 | 0 | 11 |
| argumentationEvent | 12 | 0.034 | 98.26 | 44241.245 | 241144.022 | 430955.869 | 0.0 | 1 | 3 |
| DaniEvent | 11 | 1.306 | 5.319 | 6995.506 | 38386.79 | 76229.533 | 0.01 | 0 | 1 |
| EndOfUnit | 2 | 18290.613 | 52247.198 | 52247.198 | 82808.125 | 86203.784 | 0.0 | 0 | 2 |
| chatEvent | 1 | 3.018 | 3.018 | 3.018 | 3.018 | 3.018 | 19.88 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 9 group(s), 20 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[1118] _id=6ace7a55de269131f9d0fc43 ts=2026-10-13T18:37:08.1350000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[1119] _id=6ace7a55de269131f9d0fc44 ts=2026-10-13T18:37:08.1350000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1122] _id=6ace7a55de269131f9d0fc47 ts=2026-10-13T18:37:08.1360000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[1123] _id=6ace7a55de269131f9d0fc48 ts=2026-10-13T18:37:08.1360000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1843] _id=6ace80bfde269131f9d14fef ts=2026-10-13T19:04:30.0090000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[1844] _id=6ace80bfde269131f9d14ff0 ts=2026-10-13T19:04:30.0090000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[4954] _id=6acfa8e5de269131f9d53812 ts=2026-10-14T16:08:04.7320000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[4956] _id=6acfa8e5de269131f9d53814 ts=2026-10-14T16:08:04.7320000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 123 group(s), 193 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[1939] _id=6ace8194de269131f9d16728 ts=2026-10-13T19:08:04.4550000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[1936] _id=6ace8195de269131f9d1672c ts=2026-10-13T19:08:04.4550000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1945] _id=6ace8196de269131f9d1674a ts=2026-10-13T19:08:04.6630000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[1946] _id=6ace8196de269131f9d16750 ts=2026-10-13T19:08:04.6630000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1947] _id=6ace8196de269131f9d16758 ts=2026-10-13T19:08:04.9730000Z == 6ab9a9dc9a8420a1e6b56bb6.jsonl[1942] _id=6ace8196de269131f9d1675e ts=2026-10-13T19:08:04.9730000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 72 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[195] _id=6ac69684de269131f9bea9df ts=2026-10-07T18:59:15.5140000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[196] _id=6ac69684de269131f9bea9f2 ts=2026-10-07T18:59:15.5180000Z`; `15ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[499] _id=6ac7e620de269131f9c59982 ts=2026-10-08T18:51:11.8260000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[500] _id=6ac7e620de269131f9c5998e ts=2026-10-08T18:51:11.8410000Z`; `276ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1124] _id=6ace7a71de269131f9d0fd57 ts=2026-10-13T18:37:37.2660000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[1125] _id=6ace7a71de269131f9d0fd63 ts=2026-10-13T18:37:37.5420000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `380ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[979] _id=6ac7ebb0de269131f9c673dc ts=2026-10-08T19:14:55.2990000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[981] _id=6ac7ebb0de269131f9c673f3 ts=2026-10-08T19:14:55.6790000Z`; `144ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[981] _id=6ac7ebb0de269131f9c673f3 ts=2026-10-08T19:14:55.6790000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[984] _id=6ac7ebb0de269131f9c673f9 ts=2026-10-08T19:14:55.8230000Z`; `237ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[984] _id=6ac7ebb0de269131f9c673f9 ts=2026-10-08T19:14:55.8230000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[982] _id=6ac7ebb1de269131f9c67403 ts=2026-10-08T19:14:56.0600000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[9224] _id=6ad004d6de269131f9d99941 ts=2026-10-14T22:40:21.3030000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[9227] _id=6ad004d6de269131f9d99944 ts=2026-10-14T22:40:21.3370000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 20 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `514ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[948] _id=6ac7eb8cde269131f9c66fe4 ts=2026-10-08T19:14:19.7720000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[951] _id=6ac7eb8dde269131f9c66ff8 ts=2026-10-08T19:14:20.2860000Z`; `761ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[950] _id=6ac7eb8cde269131f9c66fea ts=2026-10-08T19:14:19.9130000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[949] _id=6ac7eb8dde269131f9c67004 ts=2026-10-08T19:14:20.6740000Z`; `879ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[957] _id=6ac7eb99de269131f9c671ad ts=2026-10-08T19:14:32.3300000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[959] _id=6ac7eb9ade269131f9c671ca ts=2026-10-08T19:14:33.2090000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `368ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4023] _id=6acedca7de269131f9d29787 ts=2026-10-14T01:36:39.6070000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[4018] _id=6acedca8de269131f9d2978b ts=2026-10-14T01:36:39.9750000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `351ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4016] _id=6acedca7de269131f9d29785 ts=2026-10-14T01:36:39.2700000Z ~ 6ab9a9dc9a8420a1e6b56bb6.jsonl[4017] _id=6acedca7de269131f9d29789 ts=2026-10-14T01:36:39.6210000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[464] _id=6ac7e5bede269131f9c58d40 ts=2026-10-08T18:49:33.2250000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1112] _id=6ace7a48de269131f9d0fbd7 ts=2026-10-13T18:36:55.5030000Z; 70h 5m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11418] _id=6ad12469de269131f9dfef6a ts=2026-10-15T19:07:19.2220000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11706] _id=6ad4fe05de269131f9e8b406 ts=2026-10-18T17:12:37.4030000Z; 24h 0m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[5] _id=6ac6941dde269131f9be208e ts=2026-10-07T18:49:01.2730000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[462] _id=6ac7e5b0de269131f9c58c1f ts=2026-10-08T18:49:18.9600000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21h 10m 
  - Evidence: 21h 10m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1427] _id=6ace7ce8de269131f9d1268e ts=2026-10-13T18:48:08.8380000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4493] _id=6acfa6afde269131f9d50ac5 ts=2026-10-14T15:58:38.3710000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1106] _id=6ac7ec6fde269131f9c688ca ts=2026-10-08T19:18:05.7660000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1298] _id=6ace7b03de269131f9d10907 ts=2026-10-13T18:40:03.6130000Z; 76h 14m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11698] _id=6ad126bbde269131f9e044ea ts=2026-10-15T19:17:14.7120000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11909] _id=6ad556c6de269131f9e8dea2 ts=2026-10-18T23:31:18.4600000Z; 23h 32m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[457] _id=6ac69aafde269131f9bf1fe0 ts=2026-10-07T19:17:02.4860000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[472] _id=6ac7e5d1de269131f9c58f12 ts=2026-10-08T18:49:53.0070000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 522 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7907] _id=6acfcf5ede269131f9d7a657 ts=2026-10-14T18:52:13.3430000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[7908] _id=6acfcf5ede269131f9d7a658 ts=2026-10-14T18:52:13.3430000Z; 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[8810] _id=6acfd56ade269131f9d88633 ts=2026-10-14T19:18:01.8640000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[8816] _id=6ad00132de269131f9d9943a ts=2026-10-14T19:18:01.864Z; 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[9201] _id=6ad004cbde269131f9d99923 ts=2026-10-14T22:40:10.0070000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9215] _id=6ad004cbde269131f9d99924 ts=2026-10-14T22:40:10.0070000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 56m 
  - Evidence: 23h 56m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1839] _id=6ace8057de269131f9d145b1 ts=2026-10-13T19:02:47.1180000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[8174] _id=6acfd113de269131f9d7d63a ts=2026-10-14T18:59:30.9020000Z; 5h 4m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[8174] _id=6acfd113de269131f9d7d63a ts=2026-10-14T18:59:30.9020000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[10876] _id=6ad01886de269131f9d9b86a ts=2026-10-15T00:04:21.5150000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1082] _id=6ac7ec4dde269131f9c68641 ts=2026-10-08T19:17:32.2970000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1117] _id=6ace7a55de269131f9d0fc42 ts=2026-10-13T18:37:08.1330000Z; 76h 14m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11696] _id=6ad126b8de269131f9e0448e ts=2026-10-15T19:17:11.7700000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11904] _id=6ad556c1de269131f9e8de92 ts=2026-10-18T23:31:12.9180000Z; 23h 35m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[426] _id=6ac69a1bde269131f9bf1293 ts=2026-10-07T19:14:35.3020000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[466] _id=6ac7e5c2de269131f9c58db2 ts=2026-10-08T18:49:36.8140000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 92 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1016] _id=6ac7ebebde269131f9c67a03 ts=2026-10-08T19:15:54.8200000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1017] _id=6ac7ebebde269131f9c67a04 ts=2026-10-08T19:15:54.8200000Z; 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1118] _id=6ace7a55de269131f9d0fc43 ts=2026-10-13T18:37:08.1350000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1119] _id=6ace7a55de269131f9d0fc44 ts=2026-10-13T18:37:08.1350000Z; 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1119] _id=6ace7a55de269131f9d0fc44 ts=2026-10-13T18:37:08.1350000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1120] _id=6ace7a55de269131f9d0fc45 ts=2026-10-13T18:37:08.1350000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1085] _id=6ac7ec50de269131f9c68693 ts=2026-10-08T19:17:35.4910000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1130] _id=6ace7a68de269131f9d0fd0d ts=2026-10-13T18:37:28.7790000Z; 76h 14m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11699] _id=6ad126bbde269131f9e044eb ts=2026-10-15T19:17:14.7150000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11919] _id=6ad556c6de269131f9e8dea5 ts=2026-10-18T23:31:18.4910000Z; 23h 36m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[435] _id=6ac69a1fde269131f9bf12bf ts=2026-10-07T19:14:38.9170000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[499] _id=6ac7e620de269131f9c59982 ts=2026-10-08T18:51:11.8260000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4954] _id=6acfa8e5de269131f9d53812 ts=2026-10-14T16:08:04.7320000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4956] _id=6acfa8e5de269131f9d53814 ts=2026-10-14T16:08:04.7320000Z; 4ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[195] _id=6ac69684de269131f9bea9df ts=2026-10-07T18:59:15.5140000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[196] _id=6ac69684de269131f9bea9f2 ts=2026-10-07T18:59:15.5180000Z; 5ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1294] _id=6ace7b03de269131f9d10902 ts=2026-10-13T18:40:03.5960000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1297] _id=6ace7b03de269131f9d10906 ts=2026-10-13T18:40:03.6010000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1091] _id=6ac7ec67de269131f9c6888b ts=2026-10-08T19:17:58.8910000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1116] _id=6ace7a55de269131f9d0fc41 ts=2026-10-13T18:37:04.6570000Z; 76h 13m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11704] _id=6ad126dede269131f9e046e3 ts=2026-10-15T19:17:49.8580000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11916] _id=6ad556adde269131f9e8de74 ts=2026-10-18T23:30:51.5610000Z; 23h 32m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[460] _id=6ac69abcde269131f9bf2098 ts=2026-10-07T19:17:15.8490000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[465] _id=6ac7e5c2de269131f9c58db1 ts=2026-10-08T18:49:33.2420000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 19h 59m 
  - Evidence: 19h 59m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[10000] _id=6ad00a7ede269131f9d9a036 ts=2026-10-14T23:04:28.0490000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11013] _id=6ad1238cde269131f9dfc871 ts=2026-10-15T19:03:38.8590000Z; 14h 44m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[3708] _id=6aced8a6de269131f9d29514 ts=2026-10-14T01:19:32.3520000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4708] _id=6acfa7eede269131f9d52369 ts=2026-10-14T16:03:57.1800000Z; 5h 59m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[2746] _id=6ace82eade269131f9d1a17b ts=2026-10-13T19:13:44.0030000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[3098] _id=6aced7acde269131f9d29078 ts=2026-10-14T01:13:33.9850000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1744 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[10908] _id=6ad1238cde269131f9dfc879 ts=2026-10-15T19:03:38.8590000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11014] _id=6ad1238cde269131f9dfc87f ts=2026-10-15T19:03:38.8590000Z; 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[10912] _id=6ad1238dde269131f9dfc897 ts=2026-10-15T19:03:38.8590000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[10913] _id=6ad1238dde269131f9dfc898 ts=2026-10-15T19:03:38.8590000Z; 0ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[10913] _id=6ad1238dde269131f9dfc898 ts=2026-10-15T19:03:38.8590000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[10910] _id=6ad1238dde269131f9dfc89c ts=2026-10-15T19:03:38.8590000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 20h 47m 
  - Evidence: 20h 47m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[2874] _id=6ace832dde269131f9d1ab32 ts=2026-10-13T19:14:52.9750000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4614] _id=6acfa771de269131f9d51acf ts=2026-10-14T16:01:53.2590000Z; 20h 14m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[9437] _id=6ad006ebde269131f9d99c09 ts=2026-10-14T22:49:14.7200000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11002] _id=6ad12378de269131f9dfc556 ts=2026-10-15T19:03:19.8340000Z; 6h 45m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4705] _id=6acfa7e2de269131f9d522ed ts=2026-10-14T16:03:45.7250000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9432] _id=6ad006d3de269131f9d99bef ts=2026-10-14T22:48:50.5240000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.002s..0.010s shown 
  - Evidence: 2ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4661] _id=6acfa7bdde269131f9d51fec ts=2026-10-14T16:03:08.8010000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4662] _id=6acfa7bdde269131f9d51fed ts=2026-10-14T16:03:08.8030000Z; 10ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4660] _id=6acfa7bdde269131f9d51fe2 ts=2026-10-14T16:03:08.7910000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4661] _id=6acfa7bdde269131f9d51fec ts=2026-10-14T16:03:08.8010000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 14h 1m 
  - Evidence: 14h 1m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[3960] _id=6acedc0ade269131f9d296fe ts=2026-10-14T01:34:02.5660000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4103] _id=6acfa153de269131f9d4c6c5 ts=2026-10-14T15:35:47.1830000Z; 6h 5m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1966] _id=6ace81b6de269131f9d16ae0 ts=2026-10-13T19:08:38.5290000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[3053] _id=6aced755de269131f9d29019 ts=2026-10-14T01:13:56.9380000Z; 4h 23m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[8255] _id=6acfd234de269131f9d7fac8 ts=2026-10-14T19:04:19.3120000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[10435] _id=6ad00ffdde269131f9d9a67e ts=2026-10-14T23:27:56.8350000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.016s..0.023s shown 
  - Evidence: 16ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4106] _id=6acfa15fde269131f9d4c7f2 ts=2026-10-14T15:35:59.5450000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4108] _id=6acfa15fde269131f9d4c7f6 ts=2026-10-14T15:35:59.5610000Z; 23ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[3935] _id=6acedbeede269131f9d296e6 ts=2026-10-14T01:33:34.1860000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[3939] _id=6acedbeede269131f9d296ea ts=2026-10-14T01:33:34.2090000Z; 23ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4108] _id=6acfa15fde269131f9d4c7f6 ts=2026-10-14T15:35:59.5610000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[4112] _id=6acfa15fde269131f9d4c7fa ts=2026-10-14T15:35:59.5840000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[980] _id=6ac7ebb5de269131f9c67491 ts=2026-10-08T19:15:00.8510000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1677] _id=6ace7f2bde269131f9d13537 ts=2026-10-13T18:57:47.5800000Z; 23h 52m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1705] _id=6ace7fa5de269131f9d139fa ts=2026-10-13T18:59:49.0460000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[7906] _id=6acfcf5ede269131f9d7a64a ts=2026-10-14T18:52:13.3110000Z; 3h 47m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7943] _id=6acfcf8fde269131f9d7abaf ts=2026-10-14T18:53:02.7770000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9200] _id=6ad004cade269131f9d99921 ts=2026-10-14T22:40:09.9830000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[918] _id=6ac7ebb6de269131f9c6749e ts=2026-10-08T19:15:00.8840000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1656] _id=6ace7f20de269131f9d134db ts=2026-10-13T18:57:36.7530000Z; 23h 50m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1706] _id=6ace7fa5de269131f9d139fc ts=2026-10-13T18:59:49.0700000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[7844] _id=6acfcef9de269131f9d79df2 ts=2026-10-14T18:50:32.4900000Z; 3h 44m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7946] _id=6acfcf8fde269131f9d7abb1 ts=2026-10-14T18:53:02.8020000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9116] _id=6ad0043ade269131f9d9980d ts=2026-10-14T22:37:45.3300000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.034s..0.034s shown 
  - Evidence: 34ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[9224] _id=6ad004d6de269131f9d99941 ts=2026-10-14T22:40:21.3030000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9227] _id=6ad004d6de269131f9d99944 ts=2026-10-14T22:40:21.3370000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[973] _id=6ac7ebabde269131f9c67376 ts=2026-10-08T19:14:50.8580000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1639] _id=6ace7ef3de269131f9d133c4 ts=2026-10-13T18:56:51.5950000Z; 23h 50m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1715] _id=6ace7f9bde269131f9d139a1 ts=2026-10-13T18:59:39.7200000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[7841] _id=6acfcefbde269131f9d79e25 ts=2026-10-14T18:50:34.5290000Z; 3h 44m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7949] _id=6acfcf8dde269131f9d7ab7f ts=2026-10-14T18:53:00.9430000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9123] _id=6ad00434de269131f9d997ff ts=2026-10-14T22:37:39.5720000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 21 interval(s) ≤ 0.004s..0.006s shown 
  - Evidence: 4ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[9143] _id=6ad0046ede269131f9d99857 ts=2026-10-14T22:38:37.3820000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9134] _id=6ad0046ede269131f9d99859 ts=2026-10-14T22:38:37.3860000Z; 5ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[9156] _id=6ad00480de269131f9d9987e ts=2026-10-14T22:38:55.1350000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9161] _id=6ad00480de269131f9d99880 ts=2026-10-14T22:38:55.1400000Z; 6ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7918] _id=6acfcf6dde269131f9d7a807 ts=2026-10-14T18:52:28.4500000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[7919] _id=6acfcf6dde269131f9d7a80b ts=2026-10-14T18:52:28.4560000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 43m 
  - Evidence: 119h 43m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[904] _id=6ac7eb62de269131f9c66ab0 ts=2026-10-08T19:13:37.1360000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1651] _id=6ace7f1fde269131f9d134ca ts=2026-10-13T18:57:34.8830000Z; 23h 54m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1654] _id=6ace7f20de269131f9d134d8 ts=2026-10-13T18:57:36.6790000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[7886] _id=6acfcf3ade269131f9d7a3c1 ts=2026-10-14T18:51:37.5090000Z; 3h 47m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7894] _id=6acfcf4cde269131f9d7a4e6 ts=2026-10-14T18:51:55.3750000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[9160] _id=6ad0048cde269131f9d9988f ts=2026-10-14T22:39:07.4760000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[463] _id=6ac7e5b0de269131f9c58c2b ts=2026-10-08T18:49:19.2920000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1114] _id=6ace7a48de269131f9d0fbd9 ts=2026-10-13T18:36:55.8380000Z; 70h 14m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[10881] _id=6ad1222ade269131f9df9698 ts=2026-10-15T18:57:44.0490000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11707] _id=6ad4fe05de269131f9e8b409 ts=2026-10-18T17:12:37.5630000Z; 24h 0m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[4] _id=6ac69406de269131f9be1b78 ts=2026-10-07T18:48:37.5250000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[463] _id=6ac7e5b0de269131f9c58c2b ts=2026-10-08T18:49:19.2920000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[461] _id=6ac7e5b0de269131f9c58c2a ts=2026-10-08T18:49:19.2920000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1113] _id=6ace7a48de269131f9d0fbd8 ts=2026-10-13T18:36:55.8380000Z; 69h 55m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11695] _id=6ad126c3de269131f9e0458b ts=2026-10-15T19:17:22.4500000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11705] _id=6ad4fe05de269131f9e8b408 ts=2026-10-18T17:12:37.5630000Z; 24h 0m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[3] _id=6ac69406de269131f9be1b77 ts=2026-10-07T18:48:37.5250000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[461] _id=6ac7e5b0de269131f9c58c2a ts=2026-10-08T18:49:19.2920000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1111] _id=6ace7a47de269131f9d0fbd1 ts=2026-10-08T19:18:09.513Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[2956] _id=6aced678de269131f9d28f67 ts=2026-10-13T19:17:47.986Z; 76h 27m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11702] _id=6ad126c3de269131f9e04581 ts=2026-10-15T19:17:22.3200000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[12019] _id=6ad559f6de269131f9e8e7b9 ts=2026-10-18T23:44:54.3910000Z; 26h 13m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[7444] _id=6acfb5efde269131f9d64071 ts=2026-10-14T17:03:41.6780000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11702] _id=6ad126c3de269131f9e04581 ts=2026-10-15T19:17:22.3200000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 119h 25m 
  - Evidence: 119h 25m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1088] _id=6ac7ec52de269131f9c686ca ts=2026-10-08T19:17:37.7590000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1324] _id=6ace7bb5de269131f9d1121f ts=2026-10-13T18:43:00.8860000Z; 76h 16m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[11632] _id=6ad12629de269131f9e0318e ts=2026-10-15T19:14:48.2780000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[11917] _id=6ad556adde269131f9e8de75 ts=2026-10-18T23:30:53.2580000Z; 23h 44m: 6ab9a9dc9a8420a1e6b56bb6.jsonl[272] _id=6ac697cdde269131f9bed846 ts=2026-10-07T19:04:44.9600000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[467] _id=6ac7e5c2de269131f9c58db3 ts=2026-10-08T18:49:36.8450000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 23 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[1620] _id=6ace7ed9de269131f9d1333c ts=2026-10-13T18:56:25.6560000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[1621] _id=6ace7ed9de269131f9d1333d ts=2026-10-13T18:56:25.6570000Z; 1ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[5759] _id=6acfaf7ade269131f9d59698 ts=2026-10-14T16:36:08.6040000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[5760] _id=6acfaf7ade269131f9d59699 ts=2026-10-14T16:36:08.6050000Z; 1ms: 6ab9a9dc9a8420a1e6b56bb6.jsonl[838] _id=6ac7eabede269131f9c65954 ts=2026-10-08T19:10:53.2280000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[839] _id=6ac7eabede269131f9c65955 ts=2026-10-08T19:10:53.2290000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 13m 36s 
  - Evidence: 13m 36s: 6ab9a9dc9a8420a1e6b56bb6.jsonl[13129] _id=6ad56dddde269131f9e90bca ts=2026-10-19T01:09:48.8320000Z -> 6ab9a9dc9a8420a1e6b56bb6.jsonl[13329] _id=6ad5710dde269131f9e912ef ts=2026-10-19T01:23:24.9090000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[819] _id=6ac7ea9fde269131f9c6561f ts=2026-10-08T19:10:22.5860000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1000] _id=6ac7ebd2de269131f9c67774 ts=2026-10-08T19:15:29.9030000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1607] _id=6ace7ebfde269131f9d132c0 ts=2026-10-13T18:55:59.6870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[9227] _id=6ad004d6de269131f9d99944 ts=2026-10-14T22:40:21.3370000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[1324] _id=6ace7bb5de269131f9d1121f ts=2026-10-13T18:43:00.8860000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[13157] _id=6ad56e5fde269131f9e90d20 ts=2026-10-19T01:11:59.4710000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[13200] _id=6ad56f13de269131f9e90eac ts=2026-10-19T01:14:59.6470000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[10885] _id=6ad12248de269131f9df9b6f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 312 occurrence(s) 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[4896] _id=6acfa8c3de269131f9d53485 ts=2026-10-14T16:07:26.4070000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[4898] _id=6acfa8c3de269131f9d53487 ts=2026-10-14T16:07:26.4070000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[4901] _id=6acfa8c3de269131f9d5348a ts=2026-10-14T16:07:26.5670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 698 occurrence(s) 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[1936] _id=6ace8195de269131f9d1672c ts=2026-10-13T19:08:04.4550000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1940] _id=6ace8195de269131f9d16730 ts=2026-10-13T19:08:04.4550000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[1945] _id=6ace8196de269131f9d1674a ts=2026-10-13T19:08:04.6630000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[902] _id=6ac7eb60de269131f9c66a76 ts=2026-10-08T19:13:35.0930000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[7890] _id=6acfcf3ede269131f9d7a3f5 ts=2026-10-14T18:51:41.1480000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[7894] _id=6acfcf4cde269131f9d7a4e6 ts=2026-10-14T18:51:55.3750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 368 start, 359 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 15 unmatched 'BecameCameraCentered' (totals: 748 open, 733 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 47 unmatched 'BecameVisible' (totals: 1197 open, 1150 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 13 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 25 unmatched 'questActiveEvent' (totals: 59 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 299 of 13874 adjacent _id pairs reverse in client time; worst 109.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9dc9a8420a1e6b56bb6.jsonl[3097] _id=6aced7abde269131f9d29076 ts=2026-10-14T01:15:23.2110000Z`; `6ab9a9dc9a8420a1e6b56bb6.jsonl[3098] _id=6aced7acde269131f9d29078 ts=2026-10-14T01:13:33.9850000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.97s, min -429526.16s, max -0.12s over 13875 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9dc9a8420a1e6b56bb6\coverage.yaml

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
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
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

### `InputEvent` — 4080 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1230); Unit 4 Dev - Dungeon (1056); Unit 3 Dev (742); Unit 1 Dev (640); Unit 3 Dungeon Dev (331); Unit 4 Dev (81)
- **Intervals:** median 1.83s (p5 0.15s / p95 21.99s, n=4079)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4080/4080 records)
    "pressed"  x4080
data.actionType  (string, 4080/4080 records)
    "Move"  x2857
    "Interact"  x667
    "Sprint"  x191
    "Jump"  x179
    "Ascend"  x109
    "Hoverboard"  x55
    "Map"  x9
    "SkipCinematic"  x8
    "Descend"  x3
    "Pause"  x2
data.key  (string, 4080/4080 records, 7 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4080/4080 records)
    "Player"  x3512
    "Drone"  x568
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3828 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3272); Unit 4 Dev (340); Unit 3 Dungeon Dev (216)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.39s, n=3827)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3828/3828 records)
    "BecameVisible"  x1197
    "BecameInvisible"  x1150
    "BecameCameraCentered"  x748
    "BecameCameraUncentered"  x733
data.pieceId  (string, 3828/3828 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3828/3828 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2836 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 4 Dev - Dungeon (842); Unit 2 Prod (Refactor) (756); Unit 1 Dev (492); Unit 3 Dev (478); Unit 3 Dungeon Dev (212); Unit 4 Dev (56)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.09s, n=2829)
- **Fields under `data`:**

```text
data.position  (object, 2836/2836 records)
data.position.x  (number, 2836/2836 records)
    numeric range -708.333 .. 1551.3 (1052 unique)
data.position.y  (number, 2836/2836 records)
    numeric range -115.127 .. 170.992 (575 unique)
data.position.z  (number, 2836/2836 records)
    numeric range -1241.1 .. 2060.57 (1051 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1938 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (699); Unit 1 Dev (433); Unit 3 Dev (381); Unit 4 Dev - Dungeon (266); Unit 3 Dungeon Dev (122); Unit 4 Dev (37)
- **eventKey:** present on 1211 of 1938 records
- **Intervals:** median 4.41s (p5 0.01s / p95 62.65s, n=1937)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1211; [conversationId, dialogueEventType] x727
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1938/1938 records)
    numeric range 8 .. 111 (40 unique)
data.dialogueEventType  (string, 1938/1938 records)
    "DialogueNodeEvent"  x1211
    "DialogueStartEvent"  x368
    "DialogueFinishEvent"  x359
data.nodeId  (number, 1211/1938 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 421 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (192); Unit 2 Prod (Refactor) (81); Unit 1 Dev (75); Unit 3 Dungeon Dev (57); Unit 3 Dev (12); Unit 4 Dev (4)
- **Intervals:** median 12.41s (p5 0.16s / p95 300.90s, n=420)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 421/421 records)
    30 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 421/421 records)
    82 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 250 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (110); Unit 3 Dev (71); Unit 2 Prod (Refactor) (69)
- **Intervals:** median 0.70s (p5 0.03s / p95 9.52s, n=249)
- **Fields under `data`:**

```text
data.actionType  (string, 250/250 records)
    "argumentationNodeHoverEnd"  x108
    "argumentationNodeHoverStart"  x108
    "argumentationNodeAdd"  x26
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 250/250 records)
    "Unit 1 - Freshwater"  x72
    "Unit 3 - Pollution Upstream"  x71
    "Unit 2 – Watershed"  x69
    "Unit 1 - Argumentation Tutorial"  x38
data.nodeName  (string, 250/250 records)
    "I"  x71
    "A"  x56
    "1"  x49
    "II"  x31
    "B"  x14
    "D"  x8
    "C"  x6
    "5"  x5
    "2"  x4
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 102 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (84); Unit 3 Dev (10); Unit 4 Dev (8)
- **Intervals:** median 0.96s (p5 0.16s / p95 8.61s, n=101)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x94; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/102 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/102 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 94/102 records)
    "RightDrag"  x50
    "LeftDrag"  x44
data.currentSoilType  (string, 94/102 records)
    "CLAYSAND"  x18
    "SAND"  x18
    "SANDGRAVEL"  x17
    "CLAY"  x16
    "CLAYROCK"  x12
    "GRAVEL"  x9
    "BEDROCK"  x4
data.isCorrectSelection  (string, 94/102 records)
    "false"  x73
    "true"  x21
data.waterLevelStatus  (string, 94/102 records)
    "TooHigh"  x47
    "Proper"  x36
    "TooLow"  x11
data.waterRetentionChange  (string, 94/102 records)
    "Increase"  x42
    "Decrease"  x31
    "NoChange"  x21
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 99 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (54); Unit 3 Dev (38); Unit 1 Dev (7)
- **Intervals:** median 4.22s (p5 0.56s / p95 1580.70s, n=98)
- **`data` key-set variants:** [actionType, featureUsed] x48; [actionType, featureUsed, location] x43; [actionType, featureUsed, legendName] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 99/99 records)
    "WaypointMoveEvent"  x37
    "MapCloseEvent"  x24
    "MapOpenEvent"  x24
    "Selected"  x6
    "WaypointSetEvent"  x6
    "Unselected"  x2
data.featureUsed  (string, 99/99 records)
    "Map"  x48
    "Waypoint"  x43
    "Legend"  x8
data.legendName  (string, 8/99 records)
    "0 ft"  x2
    "60 ft"  x2
    "30 ft"  x1
    "90 ft"  x1
    "Jasper's Room"  x1
    "Water"  x1
data.location  (object, 43/99 records)
data.location.x  (number, 43/99 records)
    numeric range -542.951 .. 293.564 (38 unique)
data.location.y  (number, 43/99 records)
    numeric range -131.179 .. 358.076 (40 unique)
data.location.z  (number, 43/99 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 97 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (29); Unit 4 Dev - Dungeon (27); Unit 1 Dev (26); Unit 3 Dev (12); Unit 3 Dungeon Dev (2); Unit 4 Dev (1)
- **eventKey:** present on 97 of 97 records
- **Intervals:** median 234.01s (p5 0.00s / p95 50916.02s, n=96)
- **`data` key-set variants:** [questEventType, questID, questName] x59; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 97/97 records)
    "questActiveEvent"  x59
    "questFinishEvent"  x38
data.questID  (string, 97/97 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 97/97 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/97 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 46 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (46)
- **Intervals:** median 36.53s (p5 4.75s / p95 396.57s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "ChangeCanister"  x46
data.canisterType  (string, 46/46 records)
    "Clay"  x19
    "Bedrock"  x14
    "Gravel"  x7
    "Sand"  x6
data.floor  (string, 46/46 records)
    "5"  x33
    "4"  x9
    "3"  x4
data.machine  (string, 46/46 records)
    "1"  x43
    "2"  x3
data.row  (string, 46/46 records)
    "TopRow"  x34
    "BottomRow"  x12
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 44 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (21); Unit 2 Prod (Refactor) (8); Unit 4 Dev - Dungeon (7); Unit 1 Dev (3); Unit 3 Dev (3); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 158.59s (p5 8.30s / p95 84809.60s, n=43)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "DebugMenuStateChanged"  x44
data.isOpened  (bool, 44/44 records)
    false  x44
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 27 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21); Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1908.59s (p5 21.53s / p95 210396.78s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    true  x27
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 25 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (20); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2)
- **Intervals:** median 2.01s (p5 0.15s / p95 75096.71s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "submitAnswerEvent"  x25
data.answerSubmitted  (string, 25/25 records, 2 empty-string)
    "A,1,I"  x18
    ""  x2
    "A,1,II"  x1
    "A,5,I"  x1
    "A,5,II"  x1
    "D,1,II"  x1
    "D,A,1,II"  x1
data.argumentationTitle  (string, 25/25 records)
    "Unit 1 - Freshwater"  x18
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 4594.76s (p5 161.27s / p95 261811.67s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (6); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 3.64s (p5 1.28s / p95 189539.91s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 16/16 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 2 – Watershed"  x3
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Graph"  x3
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 4 Dev - Dungeon (4); Transition (2); Unit 1 Dev (1)
- **Intervals:** median 2021.82s (p5 0.87s / p95 330106.31s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 98.26s (p5 9.26s / p95 241144.02s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (6); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 5.32s (p5 2.17s / p95 38386.79s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 52247.20s (p5 21686.27s / p95 82808.13s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 3.02s (p5 3.02s / p95 3.02s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[31-21, 31-23, 31-24, 31-29, 31-32]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

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
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (84 records)
- `TopographicMapEvent` data.actionType: "Selected" (6x); "Unselected" (2x); "WaypointMoveEvent" (37x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (8x); "Waypoint" (43x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (14x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*