# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f225

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f225
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f225.jsonl
- **Records:** 18827 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f225
- **Time span:** 2026-09-23T13:53:34+00:00 .. 2026-10-06T15:57:27.131000+00:00 (314h 3m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f225\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 18827 records, 9 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 119 INFO, 0 NOT_TESTED, 92 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 9930 | 52.74 | 1 | 8 | 0 | 2026-09-23T13:59:09.696000+00:00 | 2026-10-06T15:44:00.806000+00:00 | 313h 44m |
| PuzzlePieceVisibleEvent | 3612 | 19.19 | 1 | 3 | 0 | 2026-09-25T13:52:13.855000+00:00 | 2026-10-06T14:19:26.415000+00:00 | 264h 27m |
| PlayerPositionEvent | 2152 | 11.43 | 1 | 8 | 0 | 2026-09-23T13:53:48.917000+00:00 | 2026-10-06T15:57:27.131000+00:00 | 314h 3m |
| DialogueEvent | 1623 | 8.62 | 1 | 8 | 1010 | 2026-09-23T13:54:11.005000+00:00 | 2026-10-06T15:51:52.221000+00:00 | 313h 57m |
| argumentationNodeEvent | 703 | 3.73 | 1 | 3 | 0 | 2026-09-24T14:04:43.668000+00:00 | 2026-10-06T15:51:20.369000+00:00 | 289h 46m |
| ObjectInterEvent | 232 | 1.23 | 1 | 7 | 0 | 2026-09-23T14:00:36.046000+00:00 | 2026-10-06T15:42:15.155000+00:00 | 313h 41m |
| Soil Key Puzzle | 144 | 0.76 | 1 | 2 | 0 | 2026-09-28T14:06:03.973000+00:00 | 2026-10-01T14:00:51.022000+00:00 | 71h 54m |
| WaterChamberEvent | 82 | 0.44 | 1 | 1 | 0 | 2026-10-06T13:57:23.004000+00:00 | 2026-10-06T14:24:24.702000+00:00 | 27m 1s |
| questEvent | 75 | 0.4 | 1 | 8 | 75 | 2026-09-23T13:54:10.988000+00:00 | 2026-10-06T15:38:54.060000+00:00 | 313h 44m |
| argumentationAnswerEvent | 68 | 0.36 | 1 | 3 | 0 | 2026-09-24T14:06:09.002000+00:00 | 2026-10-06T15:51:21.526000+00:00 | 289h 45m |
| gameWindowFocusEvent | 52 | 0.28 | 1 | 9 | 0 | 2026-09-23T13:53:34+00:00 | 2026-10-06T15:39:04.008000+00:00 | 313h 45m |
| TopographicMapEvent | 38 | 0.2 | 1 | 3 | 0 | 2026-09-25T13:52:35.087000+00:00 | 2026-10-06T13:50:05.798000+00:00 | 263h 57m |
| gameWindowUnfocusEvent | 38 | 0.2 | 1 | 8 | 0 | 2026-09-23T14:18:56.633000+00:00 | 2026-10-06T15:52:56.181000+00:00 | 313h 33m |
| DEBUGMenu | 24 | 0.13 | 1 | 7 | 0 | 2026-09-23T13:53:48.908000+00:00 | 2026-10-06T14:11:16.035000+00:00 | 312h 17m |
| gameStartEvent | 21 | 0.11 | 1 | 1 | 0 | 2026-09-23T13:53:34.001000+00:00 | 2026-10-06T15:38:37.922000+00:00 | 313h 45m |
| argumentationEvent | 8 | 0.04 | 1 | 3 | 0 | 2026-09-24T14:05:40.251000+00:00 | 2026-10-06T15:45:21.245000+00:00 | 289h 39m |
| argumentationToolEvent | 7 | 0.04 | 1 | 1 | 0 | 2026-09-24T14:05:33.751000+00:00 | 2026-09-24T14:07:24.575000+00:00 | 1m 50s |
| chatEvent | 5 | 0.03 | 1 | 2 | 0 | 2026-10-06T13:52:53.554000+00:00 | 2026-10-06T15:38:45.986000+00:00 | 1h 45m |
| TerasGardenBox | 4 | 0.02 | 1 | 1 | 0 | 2026-10-05T14:22:11.898000+00:00 | 2026-10-05T14:22:57.395000+00:00 | 45.5s |
| crash | 4 | 0.02 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-09-23T14:36:59.916000+00:00 | 2026-09-25T13:56:35.192000+00:00 | 47h 19m |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-24T14:10:52.060000+00:00 | 2026-09-24T14:10:52.060000+00:00 | 0.0s |
| soilMachine | 1 | 0.01 | 1 | 1 | 0 | 2026-10-01T15:59:44.142000+00:00 | 2026-10-01T15:59:44.142000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 18.698s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.location; data.location.x; data.location.y; data.location.z 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.26s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.598s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.001s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 5.994s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 309.314s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 823.573s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 4.1x vs baseline. 
  - Observed: 9930 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; backquote; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: E to Talk; Inspect Alien Glyph; Place Cube; Press E; Press E To Change Direction; Press E To Pick Up; Press E To Place Glyph; Press E To Return To Base; Press E to Plant Seed; Press E to Switch Canister; Press E to place; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Topography Piece 1; Topography Piece 2; Topography Piece 3; Topography Piece 4; Topography Piece 5; Topography Piece 6; Topography Slot 1; Topography Slot 2; Topography Slot 3; Topography Slot 4; Topography Slot 5; Topography Slot 6 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.8x vs baseline. 
  - Observed: 144 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 4.1x vs baseline. 
  - Observed: 82 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 13.6x vs baseline. 
  - Observed: 68 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 4,I; A,2,II; A,3,II; A,4,II; A,B,2,I; A,B,2,II; A,C,2,II; A,C,B,2,II; B,2,II; B,3,II; B,4,I; B,4,II; B,C,4,II; C,2,4,II; C,2,II; C,3,II; C,4,II; C,D,2,II; C,D,4,I; C,D,B,4,I; D,1,I; D,2,II; D,3,II; D,4,I; D,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit; U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 703 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationToolOpen 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 33; 45; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Defend the Expedition; Forsaken Facility; Guru of Arguments; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 325 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[286] _id=6ab3dd1e485cab4c954cf93d ts=2026-09-23T14:07:26.6870000Z`; `6aa4140b41b41dbac0c7f225.jsonl[1201] _id=6aba7043485cab4c95681d81 ts=2026-09-24T13:36:26.483Z`; `6aa4140b41b41dbac0c7f225.jsonl[1133] _id=6aba70a3485cab4c95682533 ts=2026-09-24T13:43:13.147Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 14 mismatch(es); e.g. 'questActiveEvent:29' vs expected 'questActiveEvent:34' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[1188] _id=6aba703d485cab4c95681d39 ts=2026-09-24T13:36:07.148Z`; `6aa4140b41b41dbac0c7f225.jsonl[1621] _id=6aba70a8485cab4c956825a3 ts=2026-09-24T13:45:12.596Z`; `6aa4140b41b41dbac0c7f225.jsonl[1694] _id=6aba70a8485cab4c956825a5 ts=2026-09-24T13:45:12.655Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[78] _id=6ab3d9de485cab4c954ce26d ts=2026-09-23T13:53:34.0010000Z`; `6aa4140b41b41dbac0c7f225.jsonl[90] _id=6ab3da23485cab4c954ce301 ts=2026-09-23T13:54:43.2020000Z`; `6aa4140b41b41dbac0c7f225.jsonl[1153] _id=6aba703c485cab4c95681d2b ts=2026-09-24T13:35:56.85Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 52 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 52} 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[74] _id=6ab3d9dd485cab4c954ce26b ts=2026-09-23T13:53:34.0000000Z`; `6aa4140b41b41dbac0c7f225.jsonl[85] _id=6ab3da23485cab4c954ce2ff ts=2026-09-23T13:54:43.2000000Z`; `6aa4140b41b41dbac0c7f225.jsonl[612] _id=6ab3dfd4485cab4c954d1251 ts=2026-09-23T14:18:59.9910000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 38 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 38} 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[640] _id=6ab3dfd0485cab4c954d1235 ts=2026-09-23T14:18:56.6330000Z`; `6aa4140b41b41dbac0c7f225.jsonl[1082] _id=6ab3e0ae485cab4c954d1def ts=2026-09-23T14:22:38.1900000Z`; `6aa4140b41b41dbac0c7f225.jsonl[1125] _id=6ab3e0ca485cab4c954d1f7d ts=2026-09-23T14:23:06.6800000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 10 of 38 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2600] _id=6aba712f485cab4c956833b5 ts=2026-09-25T13:52:35.087Z`; `6aa4140b41b41dbac0c7f225.jsonl[2627] _id=6aba7131485cab4c956833e7 ts=2026-09-25T13:54:11.952Z`; `6aa4140b41b41dbac0c7f225.jsonl[3006] _id=6aba715a485cab4c95683a09 ts=2026-09-25T13:56:35.27Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 9929 | 0.0 | 0.378 | 113.757 | 2.764 | 337143.862 | 0.53 | 691 | 14 |
| PuzzlePieceVisibleEvent | 3611 | 0.0 | 0.026 | 263.648 | 0.864 | 424110.003 | 0.23 | 2324 | 8 |
| PlayerPositionEvent | 2136 | 3.618 | 9.999 | 526.705 | 10.079 | 337108.275 | 0.11 | 0 | 10 |
| DialogueEvent | 1622 | 0.0 | 4.702 | 696.832 | 47.89 | 337134.371 | 0.09 | 416 | 10 |
| argumentationNodeEvent | 702 | 0.002 | 0.285 | 1486.035 | 12.626 | 949779.419 | 0.04 | 178 | 2 |
| ObjectInterEvent | 231 | 0.001 | 6.926 | 4888.741 | 649.855 | 337194.287 | 0.01 | 3 | 12 |
| Soil Key Puzzle | 143 | 0.132 | 0.767 | 1810.399 | 11.535 | 258498.119 | 0.03 | 0 | 1 |
| WaterChamberEvent | 81 | 0.305 | 5.598 | 20.021 | 74.259 | 134.817 | 3.0 | 0 | 0 |
| questEvent | 74 | 0.001 | 284.291 | 15263.285 | 84560.835 | 337191.037 | 0.0 | 14 | 19 |
| argumentationAnswerEvent | 67 | 0.206 | 15.001 | 15568.844 | 100.801 | 949759.941 | 0.0 | 0 | 2 |
| gameWindowFocusEvent | 51 | 0.0 | 309.314 | 22147.647 | 127843.554 | 338241.888 | 0.0 | 1 | 20 |
| TopographicMapEvent | 37 | 0.383 | 10.26 | 25682.452 | 189508.28 | 432010.306 | 0.0 | 0 | 6 |
| gameWindowUnfocusEvent | 37 | 0.095 | 823.573 | 30509.177 | 188382.069 | 337148.434 | 0.0 | 0 | 20 |
| DEBUGMenu | 23 | 63.416 | 1482.598 | 48880.31 | 250490.352 | 337188.502 | 0.0 | 0 | 16 |
| gameStartEvent | 20 | 69.201 | 3317.322 | 56475.196 | 263105.784 | 338904.965 | 0.0 | 0 | 14 |
| argumentationEvent | 7 | 0.02 | 56.481 | 148968.713 | 692403.45 | 949745.325 | 0.0 | 1 | 3 |
| argumentationToolEvent | 6 | 0.986 | 5.994 | 18.471 | 66.212 | 85.5 | 3.25 | 0 | 0 |
| chatEvent | 4 | 65.476 | 944.292 | 1588.108 | 3894.163 | 4398.372 | 0.04 | 0 | 3 |
| TerasGardenBox | 3 | 0.264 | 18.698 | 15.166 | 25.751 | 26.535 | 3.96 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 2 | 2.555 | 85187.638 | 85187.638 | 161854.213 | 170372.721 | 0.0 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| soilMachine | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[10686] _id=6abe6e7f485cab4c95a8a2e5 ts=2026-10-01T14:04:26.489Z == 6aa4140b41b41dbac0c7f225.jsonl[14064] _id=6ac4fb9ade269131f9b156fb ts=2026-10-01T14:04:26.489Z`; `6aa4140b41b41dbac0c7f225.jsonl[10690] _id=6abe6e80485cab4c95a8a2ee ts=2026-10-01T14:04:27.178Z == 6aa4140b41b41dbac0c7f225.jsonl[14037] _id=6ac4fb9ade269131f9b15711 ts=2026-10-01T14:04:27.178Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 425 group(s), 731 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2775] _id=6aba7143485cab4c9568366d ts=2026-09-25T13:52:14.833Z == 6aa4140b41b41dbac0c7f225.jsonl[2770] _id=6aba7143485cab4c95683671 ts=2026-09-25T13:52:14.833Z`; `6aa4140b41b41dbac0c7f225.jsonl[2788] _id=6aba7143485cab4c95683687 ts=2026-09-25T13:52:14.984Z == 6aa4140b41b41dbac0c7f225.jsonl[2789] _id=6aba7143485cab4c9568368f ts=2026-09-25T13:52:14.984Z`; `6aa4140b41b41dbac0c7f225.jsonl[2791] _id=6aba7144485cab4c9568369f ts=2026-09-25T13:52:15.177Z == 6aa4140b41b41dbac0c7f225.jsonl[2772] _id=6aba7144485cab4c956836a3 ts=2026-09-25T13:52:15.177Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[1222] _id=6aba704f485cab4c95681e11 ts=? == 6aa4140b41b41dbac0c7f225.jsonl[6860] _id=6abd1347485cab4c95894c37 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa4140b41b41dbac0c7f225.jsonl[203] _id=6ab3db84485cab4c954cebab ts=2026-09-23T14:00:36.0460000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[204] _id=6ab3db84485cab4c954cebad ts=2026-09-23T14:00:36.0530000Z`; `54ms: 6aa4140b41b41dbac0c7f225.jsonl[1708] _id=6aba70a4485cab4c95682555 ts=2026-09-24T13:43:27.184Z ~ 6aa4140b41b41dbac0c7f225.jsonl[1156] _id=6aba70a4485cab4c9568255b ts=2026-09-24T13:43:27.238Z`; `122ms: 6aa4140b41b41dbac0c7f225.jsonl[1920] _id=6aba70ce485cab4c956828fd ts=2026-09-24T13:54:29.778Z ~ 6aa4140b41b41dbac0c7f225.jsonl[1944] _id=6aba70ce485cab4c95682904 ts=2026-09-24T13:54:29.9Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1312 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `43ms: 6aa4140b41b41dbac0c7f225.jsonl[2768] _id=6aba7142485cab4c95683640 ts=2026-09-25T13:52:13.855Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2769] _id=6aba7142485cab4c95683645 ts=2026-09-25T13:52:13.898Z`; `58ms: 6aa4140b41b41dbac0c7f225.jsonl[2769] _id=6aba7142485cab4c95683645 ts=2026-09-25T13:52:13.898Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2742] _id=6aba7142485cab4c9568364e ts=2026-09-25T13:52:13.956Z`; `43ms: 6aa4140b41b41dbac0c7f225.jsonl[2742] _id=6aba7142485cab4c9568364e ts=2026-09-25T13:52:13.956Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2761] _id=6aba7142485cab4c95683653 ts=2026-09-25T13:52:13.999Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `517ms: 6aa4140b41b41dbac0c7f225.jsonl[10219] _id=6abe6e37485cab4c95a8904d ts=2026-10-01T14:00:12.756Z ~ 6aa4140b41b41dbac0c7f225.jsonl[10220] _id=6abe6e37485cab4c95a89057 ts=2026-10-01T14:00:13.273Z`; `589ms: 6aa4140b41b41dbac0c7f225.jsonl[10220] _id=6abe6e37485cab4c95a89057 ts=2026-10-01T14:00:13.273Z ~ 6aa4140b41b41dbac0c7f225.jsonl[10225] _id=6abe6e37485cab4c95a89068 ts=2026-10-01T14:00:13.862Z`; `534ms: 6aa4140b41b41dbac0c7f225.jsonl[10228] _id=6abe6e38485cab4c95a89080 ts=2026-10-01T14:00:21.117Z ~ 6aa4140b41b41dbac0c7f225.jsonl[10229] _id=6abe6e38485cab4c95a89087 ts=2026-10-01T14:00:21.651Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `264ms: 6aa4140b41b41dbac0c7f225.jsonl[13877] _id=6ac3b293de269131f9ab8181 ts=2026-10-05T14:22:11.8980000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[13876] _id=6ac3b294de269131f9ab8191 ts=2026-10-05T14:22:12.1620000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `383ms: 6aa4140b41b41dbac0c7f225.jsonl[2988] _id=6aba715b485cab4c95683a13 ts=2026-09-25T13:56:58.215Z ~ 6aa4140b41b41dbac0c7f225.jsonl[3008] _id=6aba715b485cab4c95683a17 ts=2026-09-25T13:56:58.598Z`; `700ms: 6aa4140b41b41dbac0c7f225.jsonl[3008] _id=6aba715b485cab4c95683a17 ts=2026-09-25T13:56:58.598Z ~ 6aa4140b41b41dbac0c7f225.jsonl[3009] _id=6aba715b485cab4c95683a1b ts=2026-09-25T13:56:59.298Z`; `516ms: 6aa4140b41b41dbac0c7f225.jsonl[3009] _id=6aba715b485cab4c95683a1b ts=2026-09-25T13:56:59.298Z ~ 6aa4140b41b41dbac0c7f225.jsonl[3003] _id=6aba715b485cab4c95683a21 ts=2026-09-25T13:56:59.814Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `783ms: 6aa4140b41b41dbac0c7f225.jsonl[17138] _id=6ac50202de269131f9b276c8 ts=2026-10-06T14:13:22.4320000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[17139] _id=6ac50203de269131f9b276e6 ts=2026-10-06T14:13:23.2150000Z`; `840ms: 6aa4140b41b41dbac0c7f225.jsonl[17822] _id=6ac50400de269131f9b2d343 ts=2026-10-06T14:21:52.1100000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[17840] _id=6ac50400de269131f9b2d369 ts=2026-10-06T14:21:52.9500000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `664ms: 6aa4140b41b41dbac0c7f225.jsonl[13368] _id=6ac3aec0de269131f9aa959a ts=2026-10-05T14:05:52.8610000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[13370] _id=6ac3aec1de269131f9aa95c0 ts=2026-10-05T14:05:53.5250000Z`; `813ms: 6aa4140b41b41dbac0c7f225.jsonl[18597] _id=6ac517afde269131f9b4b4fd ts=2026-10-06T15:45:51.3850000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[18599] _id=6ac517b0de269131f9b4b52b ts=2026-10-06T15:45:52.1980000Z`; `884ms: 6aa4140b41b41dbac0c7f225.jsonl[18610] _id=6ac517bcde269131f9b4b6a1 ts=2026-10-06T15:46:04.1550000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[18600] _id=6ac517bdde269131f9b4b6c6 ts=2026-10-06T15:46:05.0390000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa4140b41b41dbac0c7f225.jsonl[13725] _id=6ac3b06ede269131f9aaea26 ts=2026-10-05T14:13:02.1490000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[13729] _id=6ac3b06ede269131f9aaea36 ts=2026-10-05T14:13:02.1690000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 127 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `906ms: 6aa4140b41b41dbac0c7f225.jsonl[2189] _id=6aba70fa485cab4c95682da5 ts=2026-09-24T14:04:44.919Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2190] _id=6aba70fb485cab4c95682dab ts=2026-09-24T14:04:45.825Z`; `515ms: 6aa4140b41b41dbac0c7f225.jsonl[2190] _id=6aba70fb485cab4c95682dab ts=2026-09-24T14:04:45.825Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2191] _id=6aba70fb485cab4c95682dad ts=2026-09-24T14:04:46.34Z`; `544ms: 6aa4140b41b41dbac0c7f225.jsonl[2212] _id=6aba70fb485cab4c95682db5 ts=2026-09-24T14:04:48.515Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2226] _id=6aba70fb485cab4c95682db7 ts=2026-09-24T14:04:49.059Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `986ms: 6aa4140b41b41dbac0c7f225.jsonl[2269] _id=6aba7104485cab4c95682ea3 ts=2026-09-24T14:07:05.602Z ~ 6aa4140b41b41dbac0c7f225.jsonl[2276] _id=6aba7104485cab4c95682ea7 ts=2026-09-24T14:07:06.588Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4140b41b41dbac0c7f225.jsonl[8456] _id=6abd323c485cab4c958d2fda ts=2026-09-30T16:01:00.8150000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[8487] _id=6abd324b485cab4c958d30a8 ts=2026-09-30T16:01:00.815Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `153ms: 6aa4140b41b41dbac0c7f225.jsonl[6847] _id=6aba78a4485cab4c9568d441 ts=2026-09-28T14:24:36.3870000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[6851] _id=6aba78a4485cab4c9568d448 ts=2026-09-28T14:24:36.5400000Z`; `95ms: 6aa4140b41b41dbac0c7f225.jsonl[8025] _id=6abd19ce485cab4c958ad12e ts=2026-09-30T14:16:46.6230000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[7996] _id=6abd19ce485cab4c958ad13a ts=2026-09-30T14:16:46.7180000Z`; `534ms: 6aa4140b41b41dbac0c7f225.jsonl[17023] _id=6ac5016ede269131f9b264ba ts=2026-10-06T14:10:54.4530000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[17019] _id=6ac5016fde269131f9b264cb ts=2026-10-06T14:10:54.9870000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4140b41b41dbac0c7f225.jsonl[6862] _id=6abd1345485cab4c95894bb9 ts=2026-09-30T13:48:52.6030000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[6858] _id=6abd1345485cab4c95894bbd ts=2026-09-30T13:48:52.6060000Z`; `10ms: 6aa4140b41b41dbac0c7f225.jsonl[17525] _id=6ac50326de269131f9b2a5f0 ts=2026-10-06T14:18:14.4130000Z ~ 6aa4140b41b41dbac0c7f225.jsonl[17509] _id=6ac50326de269131f9b2a5f8 ts=2026-10-06T14:18:14.4230000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 93h 39m 
  - Evidence: 93h 39m: 6aa4140b41b41dbac0c7f225.jsonl[12740] _id=6abe85e8485cab4c95abc488 ts=2026-10-01T16:10:16.5500000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12776] _id=6ac3ab0dde269131f9a9e3e8 ts=2026-10-05T13:50:05.0520000Z; 71h 58m: 6aa4140b41b41dbac0c7f225.jsonl[2516] _id=6aba7124485cab4c95683281 ts=2026-09-25T13:50:11.006Z -> 6aa4140b41b41dbac0c7f225.jsonl[4524] _id=6aba71ff485cab4c956854b7 ts=2026-09-28T13:48:53.8500000Z; 47h 59m: 6aa4140b41b41dbac0c7f225.jsonl[4524] _id=6aba71ff485cab4c956854b7 ts=2026-09-28T13:48:53.8500000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6857] _id=6abd1343485cab4c95894b87 ts=2026-09-30T13:48:51.7720000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 19m 
  - Evidence: 47h 19m: 6aa4140b41b41dbac0c7f225.jsonl[1151] _id=6aba703c485cab4c95681d25 ts=2026-09-23T14:36:59.916Z -> 6aa4140b41b41dbac0c7f225.jsonl[2968] _id=6aba715a485cab4c95683a01 ts=2026-09-25T13:56:32.637Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 93h 38m 
  - Evidence: 93h 38m: 6aa4140b41b41dbac0c7f225.jsonl[12758] _id=6abe8623485cab4c95abc660 ts=2026-10-01T16:11:15.5550000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12777] _id=6ac3ab11de269131f9a9e4ec ts=2026-10-05T13:50:09.9260000Z; 71h 27m: 6aa4140b41b41dbac0c7f225.jsonl[4497] _id=6aba71fe485cab4c95685485 ts=2026-09-25T14:23:49.688Z -> 6aa4140b41b41dbac0c7f225.jsonl[4579] _id=6aba7205485cab4c956855a7 ts=2026-09-28T13:51:00.0820000Z; 47h 11m: 6aa4140b41b41dbac0c7f225.jsonl[6855] _id=6abd131d485cab4c9589459d ts=2026-09-28T14:37:50.04Z -> 6aa4140b41b41dbac0c7f225.jsonl[6928] _id=6abd1358485cab4c95894de5 ts=2026-09-30T13:49:11.9230000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 416 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f225.jsonl[13517] _id=6ac3af58de269131f9aab429 ts=2026-10-05T14:08:24.0360000Z -> 6aa4140b41b41dbac0c7f225.jsonl[13518] _id=6ac3af58de269131f9aab433 ts=2026-10-05T14:08:24.0360000Z; 0ms: 6aa4140b41b41dbac0c7f225.jsonl[7679] _id=6abd16e6485cab4c9589dcbd ts=2026-09-30T14:04:22.8590000Z -> 6aa4140b41b41dbac0c7f225.jsonl[7693] _id=6abd16e7485cab4c9589dcd4 ts=2026-09-30T14:04:22.8590000Z; 1ms: 6aa4140b41b41dbac0c7f225.jsonl[12938] _id=6ac3ad39de269131f9aa5bdc ts=2026-10-05T13:59:21.4610000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12939] _id=6ac3ad39de269131f9aa5be0 ts=2026-10-05T13:59:21.4620000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 93h 39m 
  - Evidence: 93h 39m: 6aa4140b41b41dbac0c7f225.jsonl[12753] _id=6abe8618485cab4c95abc624 ts=2026-10-01T16:11:04.8960000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12769] _id=6ac3ab11de269131f9a9e4ba ts=2026-10-05T13:50:08.7580000Z; 71h 24m: 6aa4140b41b41dbac0c7f225.jsonl[4522] _id=6aba71ff485cab4c956854a7 ts=2026-09-25T14:24:00.219Z -> 6aa4140b41b41dbac0c7f225.jsonl[4525] _id=6aba71ff485cab4c956854bb ts=2026-09-28T13:48:59.5840000Z; 47h 27m: 6aa4140b41b41dbac0c7f225.jsonl[6798] _id=6aba7803485cab4c9568cc2d ts=2026-09-28T14:21:55.9840000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6919] _id=6abd1356485cab4c95894db3 ts=2026-09-30T13:49:09.9490000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 691 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f225.jsonl[10686] _id=6abe6e7f485cab4c95a8a2e5 ts=2026-10-01T14:04:26.489Z -> 6aa4140b41b41dbac0c7f225.jsonl[14064] _id=6ac4fb9ade269131f9b156fb ts=2026-10-01T14:04:26.489Z; 0ms: 6aa4140b41b41dbac0c7f225.jsonl[10690] _id=6abe6e80485cab4c95a8a2ee ts=2026-10-01T14:04:27.178Z -> 6aa4140b41b41dbac0c7f225.jsonl[14037] _id=6ac4fb9ade269131f9b15711 ts=2026-10-01T14:04:27.178Z; 1ms: 6aa4140b41b41dbac0c7f225.jsonl[10127] _id=6abe6701485cab4c95a7700f ts=2026-10-01T13:58:25.8510000Z -> 6aa4140b41b41dbac0c7f225.jsonl[10114] _id=6abe6702485cab4c95a77015 ts=2026-10-01T13:58:25.8520000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 93h 39m 
  - Evidence: 93h 39m: 6aa4140b41b41dbac0c7f225.jsonl[12755] _id=6abe8619485cab4c95abc62e ts=2026-10-01T16:11:05.8590000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12799] _id=6ac3ab44de269131f9a9ee16 ts=2026-10-05T13:51:00.1460000Z; 72h 6m: 6aa4140b41b41dbac0c7f225.jsonl[3783] _id=6aba71af485cab4c9568475e ts=2026-09-25T13:59:49.824Z -> 6aa4140b41b41dbac0c7f225.jsonl[5245] _id=6aba744c485cab4c95687b43 ts=2026-09-28T14:06:03.9770000Z; 47h 33m: 6aa4140b41b41dbac0c7f225.jsonl[6530] _id=6aba76d9485cab4c9568b7b5 ts=2026-09-28T14:16:57.5280000Z -> 6aa4140b41b41dbac0c7f225.jsonl[7031] _id=6abd13ab485cab4c95895131 ts=2026-09-30T13:50:35.8670000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.007s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f225.jsonl[12837] _id=6ac3ab84de269131f9a9fe28 ts=2026-10-05T13:52:04.2110000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12831] _id=6ac3ab84de269131f9a9fe36 ts=2026-10-05T13:52:04.2120000Z; 2ms: 6aa4140b41b41dbac0c7f225.jsonl[12865] _id=6ac3abbbde269131f9aa0aaa ts=2026-10-05T13:52:59.6930000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12869] _id=6ac3abbbde269131f9aa0ab3 ts=2026-10-05T13:52:59.6950000Z; 7ms: 6aa4140b41b41dbac0c7f225.jsonl[203] _id=6ab3db84485cab4c954cebab ts=2026-09-23T14:00:36.0460000Z -> 6aa4140b41b41dbac0c7f225.jsonl[204] _id=6ab3db84485cab4c954cebad ts=2026-09-23T14:00:36.0530000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 93h 38m 
  - Evidence: 93h 38m: 6aa4140b41b41dbac0c7f225.jsonl[12229] _id=6abe8638485cab4c95abc6e8 ts=2026-10-01T16:11:36.7810000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12772] _id=6ac3ab11de269131f9a9e4b2 ts=2026-10-05T13:50:05.0560000Z; 71h 24m: 6aa4140b41b41dbac0c7f225.jsonl[4443] _id=6aba71ff485cab4c9568549e ts=2026-09-25T14:23:59.52Z -> 6aa4140b41b41dbac0c7f225.jsonl[4505] _id=6aba71ff485cab4c956854b9 ts=2026-09-28T13:48:53.9460000Z; 47h 24m: 6aa4140b41b41dbac0c7f225.jsonl[6849] _id=6aba78a1485cab4c9568d42f ts=2026-09-28T14:24:33.7920000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6861] _id=6abd1344485cab4c95894bb3 ts=2026-09-30T13:48:51.7780000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 117h 48m 
  - Evidence: 117h 48m: 6aa4140b41b41dbac0c7f225.jsonl[12422] _id=6abe848e485cab4c95abb41a ts=2026-10-01T16:04:29.1010000Z -> 6aa4140b41b41dbac0c7f225.jsonl[15852] _id=6ac4fd3bde269131f9b1c584 ts=2026-10-06T13:52:59.1040000Z; 71h 34m: 6aa4140b41b41dbac0c7f225.jsonl[4441] _id=6aba71fd485cab4c9568546d ts=2026-09-25T14:23:22.303Z -> 6aa4140b41b41dbac0c7f225.jsonl[4799] _id=6aba725c485cab4c95685ca3 ts=2026-09-28T13:57:47.7310000Z; 47h 27m: 6aa4140b41b41dbac0c7f225.jsonl[6769] _id=6aba77f3485cab4c9568cb4b ts=2026-09-28T14:21:38.4180000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6870] _id=6abd1345485cab4c95894bcf ts=2026-09-30T13:48:52.9110000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2324 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f225.jsonl[10231] _id=6abe6e3c485cab4c95a8916d ts=2026-10-01T14:01:00.418Z -> 6aa4140b41b41dbac0c7f225.jsonl[10257] _id=6abe6e3c485cab4c95a89173 ts=2026-10-01T14:01:00.418Z; 0ms: 6aa4140b41b41dbac0c7f225.jsonl[10245] _id=6abe6e45485cab4c95a893f1 ts=2026-10-01T14:01:12.455Z -> 6aa4140b41b41dbac0c7f225.jsonl[10198] _id=6abe6e45485cab4c95a89415 ts=2026-10-01T14:01:12.455Z; 0ms: 6aa4140b41b41dbac0c7f225.jsonl[10249] _id=6abe6e3b485cab4c95a89160 ts=2026-10-01T14:01:00.418Z -> 6aa4140b41b41dbac0c7f225.jsonl[10231] _id=6abe6e3c485cab4c95a8916d ts=2026-10-01T14:01:00.418Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 71h 48m 
  - Evidence: 71h 48m: 6aa4140b41b41dbac0c7f225.jsonl[5354] _id=6aba7545485cab4c95688821 ts=2026-09-28T14:10:13.7190000Z -> 6aa4140b41b41dbac0c7f225.jsonl[10156] _id=6abe6707485cab4c95a77121 ts=2026-10-01T13:58:31.8380000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6aa4140b41b41dbac0c7f225.jsonl[9798] _id=6abe64ff485cab4c95a6f4fd ts=2026-10-01T13:49:51.6600000Z -> 6aa4140b41b41dbac0c7f225.jsonl[15824] _id=6ac4fc8bde269131f9b1978f ts=2026-10-06T13:50:01.9660000Z; 71h 31m: 6aa4140b41b41dbac0c7f225.jsonl[4418] _id=6aba71f4485cab4c95685313 ts=2026-09-25T14:21:33.122Z -> 6aa4140b41b41dbac0c7f225.jsonl[4581] _id=6aba7207485cab4c95685619 ts=2026-09-28T13:53:32.9190000Z; 47h 55m: 6aa4140b41b41dbac0c7f225.jsonl[5366] _id=6aba7555485cab4c95688a8d ts=2026-09-28T14:10:29.7760000Z -> 6aa4140b41b41dbac0c7f225.jsonl[7719] _id=6abd172f485cab4c958a093c ts=2026-09-30T14:05:35.1770000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 263h 49m 
  - Evidence: 263h 49m: 6aa4140b41b41dbac0c7f225.jsonl[2306] _id=6aba7108485cab4c95682f23 ts=2026-09-24T14:07:52.155Z -> 6aa4140b41b41dbac0c7f225.jsonl[12946] _id=6ac3acb8de269131f9aa4393 ts=2026-10-05T13:57:12.0960000Z; 25h 32m: 6aa4140b41b41dbac0c7f225.jsonl[13730] _id=6ac3b06ede269131f9aaea1e ts=2026-10-05T14:13:02.1300000Z -> 6aa4140b41b41dbac0c7f225.jsonl[18590] _id=6ac517a8de269131f9b4b401 ts=2026-10-06T15:45:44.6420000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 263h 49m 
  - Evidence: 263h 49m: 6aa4140b41b41dbac0c7f225.jsonl[2296] _id=6aba7108485cab4c95682f27 ts=2026-09-24T14:07:52.252Z -> 6aa4140b41b41dbac0c7f225.jsonl[12931] _id=6ac3aca9de269131f9aa403a ts=2026-10-05T13:56:57.5770000Z; 25h 32m: 6aa4140b41b41dbac0c7f225.jsonl[13729] _id=6ac3b06ede269131f9aaea36 ts=2026-10-05T14:13:02.1690000Z -> 6aa4140b41b41dbac0c7f225.jsonl[18560] _id=6ac51791de269131f9b4b061 ts=2026-10-06T15:45:21.2450000Z; 16m 4s: 6aa4140b41b41dbac0c7f225.jsonl[12931] _id=6ac3aca9de269131f9aa403a ts=2026-10-05T13:56:57.5770000Z -> 6aa4140b41b41dbac0c7f225.jsonl[13725] _id=6ac3b06ede269131f9aaea26 ts=2026-10-05T14:13:02.1490000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.020s..0.020s shown 
  - Evidence: 20ms: 6aa4140b41b41dbac0c7f225.jsonl[13725] _id=6ac3b06ede269131f9aaea26 ts=2026-10-05T14:13:02.1490000Z -> 6aa4140b41b41dbac0c7f225.jsonl[13729] _id=6ac3b06ede269131f9aaea36 ts=2026-10-05T14:13:02.1690000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 263h 49m 
  - Evidence: 263h 49m: 6aa4140b41b41dbac0c7f225.jsonl[2304] _id=6aba7108485cab4c95682f11 ts=2026-09-24T14:07:37.236Z -> 6aa4140b41b41dbac0c7f225.jsonl[12947] _id=6ac3acbcde269131f9aa4484 ts=2026-10-05T13:57:16.6550000Z; 25h 32m: 6aa4140b41b41dbac0c7f225.jsonl[13720] _id=6ac3b06cde269131f9aae9f7 ts=2026-10-05T14:13:00.6950000Z -> 6aa4140b41b41dbac0c7f225.jsonl[18563] _id=6ac5179ede269131f9b4b24d ts=2026-10-06T15:45:34.5130000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 178 interval(s) ≤ 0.002s..0.018s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f225.jsonl[13583] _id=6ac3afacde269131f9aac92f ts=2026-10-05T14:09:48.0290000Z -> 6aa4140b41b41dbac0c7f225.jsonl[13584] _id=6ac3afacde269131f9aac933 ts=2026-10-05T14:09:48.0310000Z; 17ms: 6aa4140b41b41dbac0c7f225.jsonl[13191] _id=6ac3adc2de269131f9aa6e8a ts=2026-10-05T14:01:38.9010000Z -> 6aa4140b41b41dbac0c7f225.jsonl[13192] _id=6ac3adc2de269131f9aa6e8c ts=2026-10-05T14:01:38.9180000Z; 18ms: 6aa4140b41b41dbac0c7f225.jsonl[13010] _id=6ac3ad17de269131f9aa559e ts=2026-10-05T13:58:47.5280000Z -> 6aa4140b41b41dbac0c7f225.jsonl[13011] _id=6ac3ad17de269131f9aa55a0 ts=2026-10-05T13:58:47.5460000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 1h 13m 
  - Evidence: 1h 13m: 6aa4140b41b41dbac0c7f225.jsonl[18194] _id=6ac504d7de269131f9b2f759 ts=2026-10-06T14:25:27.6140000Z -> 6aa4140b41b41dbac0c7f225.jsonl[18319] _id=6ac51606de269131f9b48c0e ts=2026-10-06T15:38:45.9860000Z; 17m 16s: 6aa4140b41b41dbac0c7f225.jsonl[15845] _id=6ac4fd35de269131f9b1c3f9 ts=2026-10-06T13:52:53.5540000Z -> 6aa4140b41b41dbac0c7f225.jsonl[17010] _id=6ac50142de269131f9b2615c ts=2026-10-06T14:10:10.5300000Z; 14m 11s: 6aa4140b41b41dbac0c7f225.jsonl[17028] _id=6ac50184de269131f9b26602 ts=2026-10-06T14:11:16.0060000Z -> 6aa4140b41b41dbac0c7f225.jsonl[18194] _id=6ac504d7de269131f9b2f759 ts=2026-10-06T14:25:27.6140000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 8m 
  - Evidence: 94h 8m: 6aa4140b41b41dbac0c7f225.jsonl[10694] _id=6abe7f2e485cab4c95ab23b8 ts=2026-10-01T15:41:34.4890000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12767] _id=6ac3ab07de269131f9a9e2d6 ts=2026-10-05T13:49:59.4540000Z; 71h 58m: 6aa4140b41b41dbac0c7f225.jsonl[2507] _id=6aba7124485cab4c9568327f ts=2026-09-25T13:50:05.116Z -> 6aa4140b41b41dbac0c7f225.jsonl[4523] _id=6aba71ff485cab4c956854b1 ts=2026-09-28T13:48:41.4690000Z; 47h 59m: 6aa4140b41b41dbac0c7f225.jsonl[4523] _id=6aba71ff485cab4c956854b1 ts=2026-09-28T13:48:41.4690000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6854] _id=6abd131d485cab4c958945ac ts=2026-09-30T13:48:13.1170000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 93h 57m 
  - Evidence: 93h 57m: 6aa4140b41b41dbac0c7f225.jsonl[11594] _id=6abe81c5485cab4c95ab8b94 ts=2026-10-01T15:52:37.5650000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12766] _id=6ac3ab07de269131f9a9e2ca ts=2026-10-05T13:49:59.4530000Z; 71h 57m: 6aa4140b41b41dbac0c7f225.jsonl[2547] _id=6aba7127485cab4c956832e5 ts=2026-09-25T13:50:43.175Z -> 6aa4140b41b41dbac0c7f225.jsonl[4504] _id=6aba71ff485cab4c956854af ts=2026-09-28T13:48:41.3470000Z; 47h 23m: 6aa4140b41b41dbac0c7f225.jsonl[6856] _id=6abd131d485cab4c95894591 ts=2026-09-28T14:24:37.966Z -> 6aa4140b41b41dbac0c7f225.jsonl[6853] _id=6abd131d485cab4c958945a7 ts=2026-09-30T13:48:13.1160000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f225.jsonl[8456] _id=6abd323c485cab4c958d2fda ts=2026-09-30T16:01:00.8150000Z -> 6aa4140b41b41dbac0c7f225.jsonl[8487] _id=6abd324b485cab4c958d30a8 ts=2026-09-30T16:01:00.815Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 93h 39m 
  - Evidence: 93h 39m: 6aa4140b41b41dbac0c7f225.jsonl[12691] _id=6abe8635485cab4c95abc6da ts=2026-10-01T16:11:33.4230000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12789] _id=6ac3ab31de269131f9a9ead8 ts=2026-10-05T13:50:41.8570000Z; 72h 0m: 6aa4140b41b41dbac0c7f225.jsonl[2536] _id=6aba7127485cab4c956832dd ts=2026-09-25T13:50:37.625Z -> 6aa4140b41b41dbac0c7f225.jsonl[4566] _id=6aba7205485cab4c956855b1 ts=2026-09-28T13:51:15.0680000Z; 47h 24m: 6aa4140b41b41dbac0c7f225.jsonl[6851] _id=6aba78a4485cab4c9568d448 ts=2026-09-28T14:24:36.5400000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6897] _id=6abd1350485cab4c95894d55 ts=2026-09-30T13:49:04.7660000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 93h 39m 
  - Evidence: 93h 39m: 6aa4140b41b41dbac0c7f225.jsonl[12743] _id=6abe85e9485cab4c95abc49a ts=2026-10-01T16:10:17.7530000Z -> 6aa4140b41b41dbac0c7f225.jsonl[12773] _id=6ac3ab11de269131f9a9e4be ts=2026-10-05T13:50:08.7900000Z; 71h 37m: 6aa4140b41b41dbac0c7f225.jsonl[4131] _id=6aba71da485cab4c95684ed1 ts=2026-09-25T14:11:07.621Z -> 6aa4140b41b41dbac0c7f225.jsonl[4537] _id=6aba7202485cab4c9568551b ts=2026-09-28T13:49:02.6360000Z; 47h 26m: 6aa4140b41b41dbac0c7f225.jsonl[6800] _id=6aba780b485cab4c9568cc7d ts=2026-09-28T14:22:03.4240000Z -> 6aa4140b41b41dbac0c7f225.jsonl[6862] _id=6abd1345485cab4c95894bb9 ts=2026-09-30T13:48:52.6030000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f225.jsonl[17509] _id=6ac50326de269131f9b2a5f8 ts=2026-10-06T14:18:14.4230000Z -> 6aa4140b41b41dbac0c7f225.jsonl[17528] _id=6ac50326de269131f9b2a602 ts=2026-10-06T14:18:14.4240000Z; 2ms: 6aa4140b41b41dbac0c7f225.jsonl[16627] _id=6ac4fefbde269131f9b23bc3 ts=2026-10-06T14:00:27.2730000Z -> 6aa4140b41b41dbac0c7f225.jsonl[16620] _id=6ac4fefbde269131f9b23bc5 ts=2026-10-06T14:00:27.2750000Z; 3ms: 6aa4140b41b41dbac0c7f225.jsonl[10999] _id=6abe8005485cab4c95ab5650 ts=2026-10-01T15:45:09.4870000Z -> 6aa4140b41b41dbac0c7f225.jsonl[11000] _id=6abe8005485cab4c95ab5658 ts=2026-10-01T15:45:09.4900000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[3002] _id=6aba715a485cab4c95683a03 ts=2026-09-25T13:56:35.192Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[6740] _id=6aba77ea485cab4c9568ca93 ts=2026-09-28T14:21:30.4290000Z`; `6aa4140b41b41dbac0c7f225.jsonl[7419] _id=6abd1443485cab4c958959a9 ts=2026-09-30T13:53:07.2020000Z`; `6aa4140b41b41dbac0c7f225.jsonl[7583] _id=6abd15ec485cab4c95897ae1 ts=2026-09-30T14:00:11.5750000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 49 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[5524] _id=6aba765e485cab4c9568a90f ts=2026-09-28T14:14:54.0090000Z`; `6aa4140b41b41dbac0c7f225.jsonl[5631] _id=6aba7677485cab4c9568abbd ts=2026-09-28T14:15:18.7730000Z`; `6aa4140b41b41dbac0c7f225.jsonl[5632] _id=6aba7677485cab4c9568abc1 ts=2026-09-28T14:15:18.7730000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 1796 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2768] _id=6aba7142485cab4c95683640 ts=2026-09-25T13:52:13.855Z`; `6aa4140b41b41dbac0c7f225.jsonl[2769] _id=6aba7142485cab4c95683645 ts=2026-09-25T13:52:13.898Z`; `6aa4140b41b41dbac0c7f225.jsonl[2742] _id=6aba7142485cab4c9568364e ts=2026-09-25T13:52:13.956Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2600] _id=6aba712f485cab4c956833b5 ts=2026-09-25T13:52:35.087Z`; `6aa4140b41b41dbac0c7f225.jsonl[2627] _id=6aba7131485cab4c956833e7 ts=2026-09-25T13:54:11.952Z`; `6aa4140b41b41dbac0c7f225.jsonl[3006] _id=6aba715a485cab4c95683a09 ts=2026-09-25T13:56:35.27Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2206] _id=6aba70fe485cab4c95682df1 ts=2026-09-24T14:05:40.251Z`; `6aa4140b41b41dbac0c7f225.jsonl[2209] _id=6aba7101485cab4c95682e4d ts=2026-09-24T14:06:12.325Z`; `6aa4140b41b41dbac0c7f225.jsonl[2239] _id=6aba7103485cab4c95682e89 ts=2026-09-24T14:06:55.771Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 56 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2188] _id=6aba70fa485cab4c95682da1 ts=2026-09-24T14:04:43.668Z`; `6aa4140b41b41dbac0c7f225.jsonl[2189] _id=6aba70fa485cab4c95682da5 ts=2026-09-24T14:04:44.919Z`; `6aa4140b41b41dbac0c7f225.jsonl[2190] _id=6aba70fb485cab4c95682dab ts=2026-09-24T14:04:45.825Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[2222] _id=6aba70fd485cab4c95682de3 ts=2026-09-24T14:05:33.751Z`; `6aa4140b41b41dbac0c7f225.jsonl[2224] _id=6aba70fe485cab4c95682de9 ts=2026-09-24T14:05:40.102Z`; `6aa4140b41b41dbac0c7f225.jsonl[2269] _id=6aba7104485cab4c95682ea3 ts=2026-09-24T14:07:05.602Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[15845] _id=6ac4fd35de269131f9b1c3f9 ts=2026-10-06T13:52:53.5540000Z`; `6aa4140b41b41dbac0c7f225.jsonl[17010] _id=6ac50142de269131f9b2615c ts=2026-10-06T14:10:10.5300000Z`; `6aa4140b41b41dbac0c7f225.jsonl[17028] _id=6ac50184de269131f9b26602 ts=2026-10-06T14:11:16.0060000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[3811] _id=6aba71b1485cab4c956847b9 ts=2026-09-25T14:00:21.609Z`; `6aa4140b41b41dbac0c7f225.jsonl[4152] _id=6aba71da485cab4c95684ec3 ts=2026-09-25T14:10:30.236Z`; `6aa4140b41b41dbac0c7f225.jsonl[15185] _id=6ac4fc51de269131f9b1860e ts=2026-10-01T14:21:48.748Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[75] _id=6ab3d9f2485cab4c954ce277 ts=?`; `6aa4140b41b41dbac0c7f225.jsonl[1222] _id=6aba704f485cab4c95681e11 ts=?`; `6aa4140b41b41dbac0c7f225.jsonl[6860] _id=6abd1347485cab4c95894c37 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 287 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[5594] _id=6aba765e485cab4c9568a915 ts=2026-09-28T14:14:54.1440000Z`; `6aa4140b41b41dbac0c7f225.jsonl[5640] _id=6aba7670485cab4c9568aa73 ts=2026-09-28T14:15:11.4080000Z`; `6aa4140b41b41dbac0c7f225.jsonl[5658] _id=6aba7673485cab4c9568ab1b ts=2026-09-28T14:15:13.5440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 379 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[5481] _id=6aba75fa485cab4c9568a181 ts=2026-09-28T14:13:13.8570000Z`; `6aa4140b41b41dbac0c7f225.jsonl[5492] _id=6aba75fb485cab4c9568a189 ts=2026-09-28T14:13:14.1300000Z`; `6aa4140b41b41dbac0c7f225.jsonl[5482] _id=6aba75fb485cab4c9568a18b ts=2026-09-28T14:13:14.1580000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 12 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[13597] _id=6ac3afd0de269131f9aacfc3 ts=2026-10-05T14:10:24.0260000Z`; `6aa4140b41b41dbac0c7f225.jsonl[13602] _id=6ac3afd0de269131f9aacfd3 ts=2026-10-05T14:10:24.1960000Z`; `6aa4140b41b41dbac0c7f225.jsonl[13646] _id=6ac3affede269131f9aad8fb ts=2026-10-05T14:11:10.2640000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 PlayerPositionEvent record in 'Unit 5 Dev' inside a 'Unit 5 Dev - Dungeon' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[17076] _id=6ac501a4de269131f9b26824 ts=2026-10-06T14:11:48.4470000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'DialogueStartEvent' (totals: 310 start, 303 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 52 unmatched 'BecameCameraCentered' (totals: 380 open, 377 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 55 unmatched 'BecameVisible' (totals: 557 open, 2298 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 2 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 270 open, 325 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'questActiveEvent' (totals: 48 start, 27 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 509 of 18822 adjacent _id pairs reverse in client time; worst 347281.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f225.jsonl[13999] _id=6ac3b4fbde269131f9abf434 ts=2026-10-05T14:32:27.6540000Z`; `6aa4140b41b41dbac0c7f225.jsonl[14064] _id=6ac4fb9ade269131f9b156fb ts=2026-10-01T14:04:26.489Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.09s, min -430917.96s, max +0.07s over 18823 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f225\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 9930 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1907); Unit 1 Dev (1695); Unit 4 Dev - Dungeon (1650); Unit 3 Dev (1524); Unit 5 Dev - Dungeon (1523); Unit 4 Dev (1362); Unit 5 Dev (209); Unit 4 Dev - Anderson Base (60)
- **Intervals:** median 0.38s (p5 0.04s / p95 2.76s, n=9929)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 9930/9930 records)
    "pressed"  x9930
data.actionType  (string, 9930/9930 records)
    "Move"  x5493
    "Interact"  x1785
    "Jump"  x1484
    "Sprint"  x908
    "Hoverboard"  x138
    "Ascend"  x65
    "Descend"  x34
    "Pause"  x12
    "Map"  x4
    "SkipCinematic"  x4
    "ToggleDebug"  x3
data.key  (string, 9930/9930 records, 22 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 9930/9930 records)
    "Player"  x9711
    "Drone"  x219
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3612 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2296); Unit 4 Dev (916); Unit 5 Dev - Dungeon (400)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.86s, n=3611)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3612/3612 records)
    "BecameInvisible"  x2298
    "BecameVisible"  x557
    "BecameCameraCentered"  x380
    "BecameCameraUncentered"  x377
data.pieceId  (string, 3612/3612 records)
    23 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3612/3612 records)
    1118 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2152 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (610); Unit 1 Dev (386); Unit 4 Dev (334); Unit 4 Dev - Dungeon (193); Unit 5 Dev - Dungeon (185); Unit 3 Dev (160); Unit 4 Dev - Anderson Base (154); Unit 5 Dev (130)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.08s, n=2136)
- **Fields under `data`:**

```text
data.position  (object, 2152/2152 records)
data.position.x  (number, 2152/2152 records)
    numeric range -336.71 .. 1555.68 (517 unique)
data.position.y  (number, 2152/2152 records)
    numeric range -115.021 .. 224.703 (413 unique)
data.position.z  (number, 2152/2152 records)
    numeric range -721.33 .. 2161.43 (516 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1623 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (583); Unit 1 Dev (238); Unit 4 Dev - Anderson Base (218); Unit 4 Dev (197); Unit 4 Dev - Dungeon (129); Unit 5 Dev (124); Unit 5 Dev - Dungeon (106); Unit 3 Dev (28)
- **eventKey:** present on 1010 of 1623 records
- **Intervals:** median 4.70s (p5 0.00s / p95 47.89s, n=1622)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1010; [conversationId, dialogueEventType] x613
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1623/1623 records)
    numeric range 8 .. 116 (28 unique)
data.dialogueEventType  (string, 1623/1623 records)
    "DialogueNodeEvent"  x1010
    "DialogueStartEvent"  x310
    "DialogueFinishEvent"  x303
data.nodeId  (number, 1010/1623 records)
    numeric range 0 .. 290 (161 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 703 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (527); Unit 5 Dev (131); Unit 1 Dev (45)
- **Intervals:** median 0.28s (p5 0.03s / p95 12.63s, n=702)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 703/703 records)
    "argumentationNodeHoverEnd"  x325
    "argumentationNodeHoverStart"  x270
    "argumentationNodeAdd"  x58
    "argumentationNodeRemove"  x50
data.argumentationTitle  (string, 703/703 records)
    "Unit 4 - Flooding"  x527
    "Unit 5"  x131
    "Unit 1 - Freshwater"  x45
data.nodeName  (string, 703/703 records)
    "C"  x120
    "B"  x116
    "D"  x96
    "II"  x93
    "4"  x88
    "A"  x71
    "2"  x46
    "I"  x28
    "3"  x27
    "1"  x18
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 232 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (108); Unit 2 Prod (Refactor) (51); Unit 4 Dev (24); Unit 5 Dev - Dungeon (19); Unit 1 Dev (15); Unit 4 Dev - Anderson Base (10); Unit 5 Dev (5)
- **Intervals:** median 6.93s (p5 0.42s / p95 649.86s, n=231)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 232/232 records)
    28 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 232/232 records)
    61 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 144 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (90); Unit 4 Dev (54)
- **Intervals:** median 0.77s (p5 0.18s / p95 11.53s, n=143)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x140; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/144 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/144 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 140/144 records)
    "LeftDrag"  x79
    "RightDrag"  x61
data.currentSoilType  (string, 140/144 records)
    "CLAYSAND"  x44
    "SAND"  x25
    "SANDGRAVEL"  x23
    "CLAY"  x21
    "CLAYROCK"  x12
    "GRAVEL"  x10
    "BEDROCK"  x5
data.isCorrectSelection  (string, 140/144 records)
    "false"  x94
    "true"  x46
data.waterLevelStatus  (string, 140/144 records)
    "TooHigh"  x64
    "Proper"  x51
    "TooLow"  x25
data.waterRetentionChange  (string, 140/144 records)
    "Increase"  x56
    "NoChange"  x46
    "Decrease"  x38
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 82 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (82)
- **Intervals:** median 5.60s (p5 0.43s / p95 74.26s, n=81)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 82/82 records)
    "On"  x50
    "Off"  x32
data.floor  (string, 82/82 records)
    "4"  x38
    "3"  x35
    "1"  x6
    "2"  x3
data.machineNumber  (string, 82/82 records)
    "One"  x78
    "Two"  x4
data.machineType  (string, 82/82 records)
    "Condenser"  x43
    "Evaporator"  x27
    "DualChamber_Condenser"  x4
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x4
data.room  (string, 82/82 records)
    "3"  x32
    "2"  x22
    "1"  x20
    "4"  x8
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `questEvent` — 75 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (18); Unit 2 Prod (Refactor) (16); Unit 4 Dev - Dungeon (13); Unit 5 Dev - Dungeon (12); Unit 4 Dev (6); Unit 3 Dev (5); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **eventKey:** present on 75 of 75 records
- **Intervals:** median 284.29s (p5 0.00s / p95 84560.84s, n=74)
- **`data` key-set variants:** [questEventType, questID, questName] x48; [questEventType, questID, questName, questSuccessOrFailure] x27
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 75/75 records)
    "questActiveEvent"  x48
    "questFinishEvent"  x27
data.questID  (string, 75/75 records)
    25 unique values (see csv/event_unique_values.csv)
data.questName  (string, 75/75 records)
    25 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 27/75 records)
    "Succeeded"  x27
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 68 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (36); Unit 5 Dev (28); Unit 1 Dev (4)
- **Intervals:** median 15.00s (p5 0.71s / p95 100.80s, n=67)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "submitAnswerEvent"  x68
data.answerSubmitted  (string, 68/68 records, 1 empty-string)
    28 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 68/68 records)
    "Unit 4 - Flooding"  x36
    "Unit 5"  x28
    "Unit 1 - Freshwater"  x4
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 52 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21); Unit 2 Prod (Refactor) (9); Unit 5 Dev (6); Unit 1 Dev (5); Unit 5 Dev - Dungeon (4); Unit 4 Dev (3); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 309.31s (p5 1.50s / p95 127843.55s, n=51)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 52/52 records)
    true  x52
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TopographicMapEvent` — 38 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 3 Dev (4); Unit 4 Dev (2)
- **Intervals:** median 10.26s (p5 0.61s / p95 189508.28s, n=37)
- **`data` key-set variants:** [actionType, featureUsed] x28; [actionType, featureUsed, legendName] x10
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "MapCloseEvent"  x20
    "Unselected"  x10
    "MapOpenEvent"  x8
data.featureUsed  (string, 38/38 records)
    "Map"  x28
    "Legend"  x10
data.legendName  (string, 10/38 records)
    "150 ft"  x10
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowUnfocusEvent` — 38 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 5 Dev (8); Unit 1 Dev (4); Unit 4 Dev (4); Unit 5 Dev - Dungeon (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 823.57s (p5 0.46s / p95 188382.07s, n=37)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 38/38 records)
    false  x38
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 24 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev (4); Unit 1 Dev (3); Unit 4 Dev - Dungeon (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 1482.60s (p5 147.37s / p95 250490.35s, n=23)
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "DebugMenuStateChanged"  x24
data.isOpened  (bool, 24/24 records)
    false  x24
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 3317.32s (p5 127.61s / p95 263105.78s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 8 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (1)
- **Intervals:** median 56.48s (p5 9.64s / p95 692403.45s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 8/8 records)
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x4
    "Unit 4 - Flooding"  x3
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 5.99s (p5 1.74s / p95 66.21s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolClose"  x7
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x7
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - "  x7
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 944.29s (p5 183.40s / p95 3894.16s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x5
data.chatID  (string, 5/5 records)
    "NA"  x5
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `TerasGardenBox` — 4 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (4)
- **Intervals:** median 18.70s (p5 2.11s / p95 25.75s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "cameraPlaced"  x4
data.boxId  (string, 4/4 records)
    "0"  x2
    "1"  x1
    "2"  x1
data.soilType  (string, 4/4 records)
    "None"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x1
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x2
    "unit1"  x1
    "unit5"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 3 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2); Unit 1 Dev (1)
- **Intervals:** median 85187.64s (p5 8521.06s / p95 161854.21s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x2
    "Open"  x1
data.toolName  (string, 3/3 records, 3 empty-string)
    ""  x3
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

### `soilMachine` — 1 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "ChangeCanister"  x1
data.canisterType  (string, 1/1 records)
    "Gravel"  x1
data.floor  (string, 1/1 records)
    "5"  x1
data.machine  (string, 1/1 records)
    "2"  x1
data.row  (string, 1/1 records)
    "TopRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (90 records)
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "Unselected" (10x)
- `TopographicMapEvent` data.featureUsed: "Legend" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (50x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*