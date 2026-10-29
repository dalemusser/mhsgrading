# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f24d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f24d
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f24d.jsonl
- **Records:** 13126 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f24d
- **Time span:** 2026-09-23T16:27:21.491000+00:00 .. 2026-10-07T17:06:32.533000+00:00 (336h 39m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f24d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13126 records, 10 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 105 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4430 | 33.75 | 1 | 3 | 0 | 2026-09-25T16:33:05.361000+00:00 | 2026-10-06T17:04:47.710000+00:00 | 264h 31m |
| InputEvent | 4011 | 30.56 | 1 | 8 | 0 | 2026-09-23T16:27:45.978000+00:00 | 2026-10-07T17:06:22.858000+00:00 | 336h 38m |
| PlayerPositionEvent | 2121 | 16.16 | 1 | 8 | 0 | 2026-09-23T16:27:40.769000+00:00 | 2026-10-07T17:06:15.793000+00:00 | 336h 38m |
| DialogueEvent | 1744 | 13.29 | 1 | 8 | 1112 | 2026-09-23T16:28:02.705000+00:00 | 2026-10-07T17:06:19.372000+00:00 | 336h 38m |
| ObjectInterEvent | 249 | 1.9 | 1 | 8 | 0 | 2026-09-23T16:35:16.519000+00:00 | 2026-10-07T17:06:22.858000+00:00 | 336h 31m |
| argumentationNodeEvent | 187 | 1.42 | 1 | 3 | 0 | 2026-09-23T17:00:49.582000+00:00 | 2026-10-07T16:51:07.105000+00:00 | 335h 50m |
| TopographicMapEvent | 76 | 0.58 | 1 | 2 | 0 | 2026-09-25T16:33:47.731000+00:00 | 2026-09-30T17:03:47.047000+00:00 | 120h 29m |
| questEvent | 76 | 0.58 | 1 | 8 | 76 | 2026-09-23T16:28:02.682000+00:00 | 2026-10-07T17:01:18.414000+00:00 | 336h 33m |
| Soil Key Puzzle | 42 | 0.32 | 1 | 2 | 0 | 2026-09-25T16:42:38.374000+00:00 | 2026-10-01T16:30:24.579000+00:00 | 143h 47m |
| WaterChamberEvent | 40 | 0.3 | 1 | 1 | 0 | 2026-10-06T17:03:08.646000+00:00 | 2026-10-07T16:41:57.361000+00:00 | 23h 38m |
| gameWindowFocusEvent | 27 | 0.21 | 1 | 5 | 0 | 2026-09-23T16:27:21.491000+00:00 | 2026-10-07T17:06:32.533000+00:00 | 336h 39m |
| DEBUGMenu | 20 | 0.15 | 1 | 8 | 0 | 2026-09-23T16:27:40.764000+00:00 | 2026-10-07T16:36:10.447000+00:00 | 336h 8m |
| SolarStillDesignEvent | 17 | 0.13 | 1 | 1 | 0 | 2026-10-07T16:56:53.485000+00:00 | 2026-10-07T16:58:04.188000+00:00 | 1m 10s |
| gameStartEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-09-23T16:27:21.492000+00:00 | 2026-10-07T16:35:53.739000+00:00 | 336h 8m |
| TerasGardenBox | 12 | 0.09 | 1 | 1 | 0 | 2026-10-06T16:40:34.251000+00:00 | 2026-10-06T16:42:23.685000+00:00 | 1m 49s |
| argumentationEvent | 12 | 0.09 | 1 | 3 | 0 | 2026-09-23T17:02:39.310000+00:00 | 2026-10-07T16:51:09.458000+00:00 | 335h 48m |
| gameWindowUnfocusEvent | 12 | 0.09 | 1 | 5 | 0 | 2026-09-25T16:27:02.013000+00:00 | 2026-10-07T17:06:23.550000+00:00 | 288h 39m |
| soilMachine | 11 | 0.08 | 1 | 1 | 0 | 2026-10-05T16:44:23.231000+00:00 | 2026-10-05T16:54:32.472000+00:00 | 10m 9s |
| argumentationAnswerEvent | 6 | 0.05 | 1 | 3 | 0 | 2026-09-24T16:42:52.549000+00:00 | 2026-10-07T16:51:09.430000+00:00 | 312h 8m |
| DaniEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-09-30T16:34:39.441000+00:00 | 2026-09-30T17:03:53.144000+00:00 | 29m 13s |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-24T16:47:56.249000+00:00 | 2026-10-07T17:06:22.826000+00:00 | 312h 18m |
| argumentationToolEvent | 3 | 0.02 | 1 | 1 | 0 | 2026-09-23T17:02:28.158000+00:00 | 2026-09-23T17:05:15.963000+00:00 | 2m 47s |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-06T16:58:09.561000+00:00 | 2026-10-07T16:42:46.339000+00:00 | 23h 44m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 2113.709s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 562153.289s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.247s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.7s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 98.863s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 83.903s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 42738.389s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84432.746s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1373.329s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 3844.157s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: d 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E To Change Direction; Press E To Place Glyph; Press E to Plant Seed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: C,A,D,2,II; C,D,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
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
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 27 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 54; 55 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Forsaken Facility; Leader of Evidence; Part of a Balanced Ecosystem 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 15 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[323] _id=6ab40116485cab4c954e7326 ts=2026-09-23T16:40:54.6720000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[422] _id=6ab40206485cab4c954e7784 ts=2026-09-23T16:44:54.3450000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[479] _id=6ab40311485cab4c954e7c20 ts=2026-09-23T16:49:21.3100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[5660] _id=6abbe77e485cab4c9580c60d ts=2026-09-29T16:29:48.3960000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[8] _id=6ab3fde9485cab4c954e60da ts=2026-09-23T16:27:21.4920000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[801] _id=6ab551a4485cab4c95532227 ts=2026-09-24T16:36:52.0980000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1079] _id=6ab6a09d485cab4c95594685 ts=2026-09-25T16:26:05.5260000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[7] _id=6ab3fde9485cab4c954e60d8 ts=2026-09-23T16:27:21.4910000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[800] _id=6ab551a4485cab4c95532225 ts=2026-09-24T16:36:52.0980000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1080] _id=6ab6a09d485cab4c95594661 ts=2026-09-25T16:26:05.5240000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1084] _id=6ab6a0d6485cab4c95596ccb ts=2026-09-25T16:27:02.0130000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1488] _id=6ab6a330485cab4c955af35c ts=2026-09-25T16:37:05.0160000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[2784] _id=6ab6a6d4485cab4c955cea75 ts=2026-09-25T16:52:36.3670000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 76 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1250] _id=6ab6a26b485cab4c955a75f8 ts=2026-09-25T16:33:47.7310000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1251] _id=6ab6a26d485cab4c955a7734 ts=2026-09-25T16:33:49.3980000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1252] _id=6ab6a26f485cab4c955a7882 ts=2026-09-25T16:33:51.1340000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4429 | 0.0 | 0.025 | 215.015 | 1.258 | 346982.487 | 0.28 | 2822 | 6 |
| InputEvent | 4010 | 0.0 | 0.925 | 302.224 | 14.256 | 343417.225 | 0.2 | 113 | 12 |
| PlayerPositionEvent | 2111 | 8.088 | 10.0 | 493.966 | 10.023 | 343416.732 | 0.12 | 0 | 7 |
| DialogueEvent | 1743 | 0.0 | 5.165 | 695.294 | 43.295 | 343454.622 | 0.09 | 494 | 10 |
| ObjectInterEvent | 248 | 0.001 | 10.78 | 4884.945 | 558.161 | 343444.199 | 0.01 | 5 | 12 |
| argumentationNodeEvent | 186 | 0.005 | 0.362 | 6500.094 | 7.853 | 1036112.164 | 0.01 | 45 | 3 |
| TopographicMapEvent | 75 | 0.026 | 7.247 | 5783.991 | 898.653 | 257593.826 | 0.01 | 2 | 5 |
| questEvent | 75 | 0.0 | 234.504 | 16154.61 | 85118.394 | 343916.427 | 0.0 | 18 | 17 |
| Soil Key Puzzle | 41 | 0.173 | 0.803 | 12626.005 | 11.979 | 259831.672 | 0.0 | 0 | 2 |
| WaterChamberEvent | 39 | 0.65 | 5.7 | 2182.788 | 76.72 | 84531.523 | 0.03 | 0 | 1 |
| gameWindowFocusEvent | 26 | 1.533 | 1373.329 | 46613.502 | 215373.392 | 345843.724 | 0.0 | 0 | 18 |
| DEBUGMenu | 19 | 17.206 | 2113.709 | 63689.983 | 268280.286 | 345222.307 | 0.0 | 0 | 15 |
| SolarStillDesignEvent | 16 | 0.001 | 1.857 | 4.419 | 18.37 | 35.243 | 13.58 | 2 | 0 |
| gameStartEvent | 15 | 79.266 | 84432.746 | 80674.15 | 285590.015 | 345843.725 | 0.0 | 0 | 12 |
| TerasGardenBox | 11 | 0.746 | 3.875 | 9.949 | 35.526 | 53.947 | 6.03 | 0 | 0 |
| argumentationEvent | 11 | 0.026 | 54.534 | 109900.923 | 561757.677 | 1036109.649 | 0.0 | 1 | 3 |
| gameWindowUnfocusEvent | 11 | 1.141 | 3844.157 | 94469.231 | 385277.799 | 512078.66 | 0.0 | 0 | 9 |
| soilMachine | 10 | 1.054 | 42.843 | 60.924 | 181.166 | 226.878 | 0.98 | 0 | 0 |
| argumentationAnswerEvent | 5 | 3.392 | 98.863 | 224739.376 | 846394.612 | 1036131.003 | 0.0 | 0 | 2 |
| DaniEvent | 3 | 3.521 | 6.09 | 584.568 | 1570.292 | 1744.092 | 0.1 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 2 | 86917.82 | 562153.289 | 562153.289 | 989865.21 | 1037388.757 | 0.0 | 0 | 2 |
| argumentationToolEvent | 2 | 11.117 | 83.903 | 83.902 | 149.409 | 156.688 | 0.72 | 0 | 0 |
| chatEvent | 2 | 395.961 | 42738.389 | 42738.389 | 80846.574 | 85080.817 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 7 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[10487] _id=6ac51acbde269131f9b4d2b7 ts=2026-10-06T15:59:07.5320000Z == 6aa4142c41b41dbac0c7f24d.jsonl[10474] _id=6ac51acbde269131f9b4d2b9 ts=2026-10-06T15:59:07.5320000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[11099] _id=6ac5213dde269131f9b4fd1b ts=2026-10-06T16:26:36.9440000Z == 6aa4142c41b41dbac0c7f24d.jsonl[11100] _id=6ac5213dde269131f9b4fd1f ts=2026-10-06T16:26:36.9440000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[12424] _id=6ac67500de269131f9bca909 ts=2026-10-07T16:36:15.2960000Z == 6aa4142c41b41dbac0c7f24d.jsonl[12425] _id=6ac67500de269131f9bca90a ts=2026-10-07T16:36:15.2960000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 231 group(s), 325 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1188] _id=6ab6a253485cab4c955a6469 ts=2026-09-25T16:33:22.4350000Z == 6aa4142c41b41dbac0c7f24d.jsonl[1191] _id=6ab6a253485cab4c955a6483 ts=2026-09-25T16:33:22.4350000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1199] _id=6ab6a254485cab4c955a6542 ts=2026-09-25T16:33:22.5360000Z == 6aa4142c41b41dbac0c7f24d.jsonl[1184] _id=6ab6a254485cab4c955a655e ts=2026-09-25T16:33:22.5360000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1197] _id=6ab6a254485cab4c955a657e ts=2026-09-25T16:33:22.5490000Z == 6aa4142c41b41dbac0c7f24d.jsonl[1200] _id=6ab6a254485cab4c955a6596 ts=2026-09-25T16:33:22.5490000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[3123] _id=6aba976f485cab4c956ab94a ts=? == 6aa4142c41b41dbac0c7f24d.jsonl[5648] _id=6abbe77c485cab4c9580c5c9 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[12892] _id=6ac678c8de269131f9bd4915 ts=2026-10-07T16:52:24.0070000Z == 6aa4142c41b41dbac0c7f24d.jsonl[12893] _id=6ac678c8de269131f9bd4916 ts=2026-10-07T16:52:24.0070000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 34 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `204ms: 6aa4142c41b41dbac0c7f24d.jsonl[152] _id=6ab3ffd1485cab4c954e6a96 ts=2026-09-23T16:35:29.4930000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[153] _id=6ab3ffd1485cab4c954e6a9a ts=2026-09-23T16:35:29.6970000Z`; `230ms: 6aa4142c41b41dbac0c7f24d.jsonl[153] _id=6ab3ffd1485cab4c954e6a9a ts=2026-09-23T16:35:29.6970000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[154] _id=6ab3ffd1485cab4c954e6a9e ts=2026-09-23T16:35:29.9270000Z`; `162ms: 6aa4142c41b41dbac0c7f24d.jsonl[154] _id=6ab3ffd1485cab4c954e6a9e ts=2026-09-23T16:35:29.9270000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[121] _id=6ab3ffd2485cab4c954e6aa4 ts=2026-09-23T16:35:30.0890000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 585 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa4142c41b41dbac0c7f24d.jsonl[1198] _id=6ab6a253485cab4c955a64da ts=2026-09-25T16:33:22.4970000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[1196] _id=6ab6a253485cab4c955a64f3 ts=2026-09-25T16:33:22.5190000Z`; `13ms: 6aa4142c41b41dbac0c7f24d.jsonl[1185] _id=6ab6a254485cab4c955a6574 ts=2026-09-25T16:33:22.5360000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[1197] _id=6ab6a254485cab4c955a657e ts=2026-09-25T16:33:22.5490000Z`; `74ms: 6aa4142c41b41dbac0c7f24d.jsonl[1217] _id=6ab6a256485cab4c955a676d ts=2026-09-25T16:33:24.2920000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[1219] _id=6ab6a257485cab4c955a6781 ts=2026-09-25T16:33:24.3660000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6aa4142c41b41dbac0c7f24d.jsonl[2947] _id=6ab6a81c485cab4c955d09d1 ts=2026-09-25T16:58:04.7360000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[2950] _id=6ab6a81d485cab4c955d09d9 ts=2026-09-25T16:58:04.7700000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6aa4142c41b41dbac0c7f24d.jsonl[11357] _id=6ac522e4de269131f9b51377 ts=2026-10-06T16:33:40.3950000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[11354] _id=6ac522e4de269131f9b51383 ts=2026-10-06T16:33:40.4210000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 42 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `314ms: 6aa4142c41b41dbac0c7f24d.jsonl[680] _id=6ab405c1485cab4c954e8f82 ts=2026-09-23T17:00:49.5820000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[676] _id=6ab405c1485cab4c954e8f86 ts=2026-09-23T17:00:49.8960000Z`; `539ms: 6aa4142c41b41dbac0c7f24d.jsonl[681] _id=6ab405c1485cab4c954e8f84 ts=2026-09-23T17:00:49.6680000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[677] _id=6ab405c2485cab4c954e8f8a ts=2026-09-23T17:00:50.2070000Z`; `860ms: 6aa4142c41b41dbac0c7f24d.jsonl[676] _id=6ab405c1485cab4c954e8f86 ts=2026-09-23T17:00:49.8960000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[678] _id=6ab405c2485cab4c954e8f8e ts=2026-09-23T17:00:50.7560000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4142c41b41dbac0c7f24d.jsonl[5660] _id=6abbe77e485cab4c9580c60d ts=2026-09-29T16:29:48.3960000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[5661] _id=6abbe77e485cab4c9580c611 ts=2026-09-29T16:29:48.4020000Z`; `5ms: 6aa4142c41b41dbac0c7f24d.jsonl[13016] _id=6ac67a60de269131f9bd6e0b ts=2026-10-07T16:59:12.7840000Z ~ 6aa4142c41b41dbac0c7f24d.jsonl[13017] _id=6ac67a60de269131f9bd6e0d ts=2026-10-07T16:59:12.7890000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa4142c41b41dbac0c7f24d.jsonl[8778] _id=6abe8b79485cab4c95ac104c ts=2026-10-01T16:34:01.4650000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9135] _id=6ac3cff5de269131f9adaa41 ts=2026-10-05T16:27:43.7720000Z; 72h 8m: 6aa4142c41b41dbac0c7f24d.jsonl[1081] _id=6ab6a0d3485cab4c95596b2d ts=2026-09-25T16:26:59.2480000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3114] _id=6aba9766485cab4c956ab91e ts=2026-09-28T16:35:50.4210000Z; 24h 9m: 6aa4142c41b41dbac0c7f24d.jsonl[18] _id=6ab3fdfc485cab4c954e60e2 ts=2026-09-23T16:27:40.7640000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[804] _id=6ab551ae485cab4c9553229d ts=2026-09-24T16:37:02.5280000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 29m 4s 
  - Evidence: 29m 4s: 6aa4142c41b41dbac0c7f24d.jsonl[7089] _id=6abd3a22485cab4c958dd6b8 ts=2026-09-30T16:34:42.9620000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[8174] _id=6abd40f3485cab4c958eeeb8 ts=2026-09-30T17:03:47.0540000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4142c41b41dbac0c7f24d.jsonl[9112] _id=6abe9277485cab4c95ac4076 ts=2026-10-01T17:03:51.7640000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9160] _id=6ac3d00cde269131f9adac4f ts=2026-10-05T16:28:06.3860000Z; 71h 31m: 6aa4142c41b41dbac0c7f24d.jsonl[3079] _id=6ab6a9f0485cab4c955d3837 ts=2026-09-25T17:05:52.3770000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3143] _id=6aba97b6485cab4c956abbb3 ts=2026-09-28T16:37:10.9330000Z; 23h 39m: 6aa4142c41b41dbac0c7f24d.jsonl[1077] _id=6ab55439485cab4c95534e81 ts=2026-09-24T16:47:53.8170000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[1089] _id=6ab6a0d7485cab4c95596d23 ts=2026-09-25T16:27:03.3030000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 494 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[12971] _id=6ac67a55de269131f9bd6ca4 ts=2026-10-07T16:59:01.5530000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12972] _id=6ac67a55de269131f9bd6ca5 ts=2026-10-07T16:59:01.5530000Z; 1ms: 6aa4142c41b41dbac0c7f24d.jsonl[12630] _id=6ac67676de269131f9bcf494 ts=2026-10-07T16:42:30.3530000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12631] _id=6ac67676de269131f9bcf495 ts=2026-10-07T16:42:30.3540000Z; 1ms: 6aa4142c41b41dbac0c7f24d.jsonl[12636] _id=6ac6767ade269131f9bcf545 ts=2026-10-07T16:42:33.9330000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12637] _id=6ac6767ade269131f9bcf546 ts=2026-10-07T16:42:33.9340000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 288h 9m 
  - Evidence: 288h 9m: 6aa4142c41b41dbac0c7f24d.jsonl[1078] _id=6ab5543c485cab4c95534e8d ts=2026-09-24T16:47:56.2490000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11751] _id=6ac52889de269131f9b5bd59 ts=2026-10-06T16:57:45.0060000Z; 24h 8m: 6aa4142c41b41dbac0c7f24d.jsonl[11751] _id=6ac52889de269131f9b5bd59 ts=2026-10-06T16:57:45.0060000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[13121] _id=6ac67c0ede269131f9bd94b0 ts=2026-10-07T17:06:22.8260000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4142c41b41dbac0c7f24d.jsonl[9120] _id=6abe9287485cab4c95ac40b6 ts=2026-10-01T17:04:07.4620000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9140] _id=6ac3cff7de269131f9adaa63 ts=2026-10-05T16:27:44.6870000Z; 71h 29m: 6aa4142c41b41dbac0c7f24d.jsonl[3098] _id=6ab6aa29485cab4c955d3a25 ts=2026-09-25T17:06:49.7880000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3120] _id=6aba976f485cab4c956ab950 ts=2026-09-28T16:35:59.0840000Z; 23h 39m: 6aa4142c41b41dbac0c7f24d.jsonl[1057] _id=6ab55411485cab4c95534d01 ts=2026-09-24T16:47:13.6280000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[1087] _id=6ab6a0d7485cab4c95596cfb ts=2026-09-25T16:27:02.0230000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 113 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[10487] _id=6ac51acbde269131f9b4d2b7 ts=2026-10-06T15:59:07.5320000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[10474] _id=6ac51acbde269131f9b4d2b9 ts=2026-10-06T15:59:07.5320000Z; 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[11099] _id=6ac5213dde269131f9b4fd1b ts=2026-10-06T16:26:36.9440000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11100] _id=6ac5213dde269131f9b4fd1f ts=2026-10-06T16:26:36.9440000Z; 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[12424] _id=6ac67500de269131f9bca909 ts=2026-10-07T16:36:15.2960000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12425] _id=6ac67500de269131f9bca90a ts=2026-10-07T16:36:15.2960000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4142c41b41dbac0c7f24d.jsonl[9126] _id=6abe9282485cab4c95ac409e ts=2026-10-01T17:04:02.2050000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9153] _id=6ac3d00cde269131f9adac57 ts=2026-10-05T16:28:06.4040000Z; 72h 10m: 6aa4142c41b41dbac0c7f24d.jsonl[2556] _id=6ab6a47e485cab4c955bd4a3 ts=2026-09-25T16:42:38.3810000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3846] _id=6aba9b79485cab4c956adc77 ts=2026-09-28T16:53:13.0280000Z; 24h 4m: 6aa4142c41b41dbac0c7f24d.jsonl[6373] _id=6abbe83b485cab4c9580daff ts=2026-09-29T16:32:59.6870000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[7164] _id=6abd3ac0485cab4c958e03c4 ts=2026-09-30T16:37:20.8520000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24d.jsonl[10783] _id=6ac51d22de269131f9b4e257 ts=2026-10-06T16:09:05.8960000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[10784] _id=6ac51d22de269131f9b4e259 ts=2026-10-06T16:09:05.8970000Z; 1ms: 6aa4142c41b41dbac0c7f24d.jsonl[11251] _id=6ac52219de269131f9b508bd ts=2026-10-06T16:30:17.1900000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11252] _id=6ac52219de269131f9b508bf ts=2026-10-06T16:30:17.1910000Z; 2ms: 6aa4142c41b41dbac0c7f24d.jsonl[11009] _id=6ac51e22de269131f9b4eb21 ts=2026-10-06T16:13:22.0540000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11013] _id=6ac51e22de269131f9b4eb23 ts=2026-10-06T16:13:22.0560000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4142c41b41dbac0c7f24d.jsonl[9119] _id=6abe9287485cab4c95ac40ae ts=2026-10-01T17:04:07.0480000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9136] _id=6ac3cff7de269131f9adaa5d ts=2026-10-05T16:27:43.7800000Z; 71h 28m: 6aa4142c41b41dbac0c7f24d.jsonl[3099] _id=6ab6aa2b485cab4c955d3a33 ts=2026-09-25T17:06:51.7110000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3119] _id=6aba976f485cab4c956ab94c ts=2026-09-28T16:35:50.4340000Z; 23h 29m: 6aa4142c41b41dbac0c7f24d.jsonl[792] _id=6ab40768485cab4c954e947e ts=2026-09-23T17:07:52.3770000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[805] _id=6ab551b5485cab4c955322c9 ts=2026-09-24T16:37:02.5350000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6aa4142c41b41dbac0c7f24d.jsonl[8771] _id=6abe8b67485cab4c95ac0fcc ts=2026-10-01T16:33:41.9230000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[10011] _id=6ac3d6cdde269131f9ae46a5 ts=2026-10-05T16:56:44.4100000Z; 72h 13m: 6aa4142c41b41dbac0c7f24d.jsonl[2531] _id=6ab6a432485cab4c955ba25c ts=2026-09-25T16:41:21.2810000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3917] _id=6aba9bdf485cab4c956ae121 ts=2026-09-28T16:54:54.6300000Z; 47h 52m: 6aa4142c41b41dbac0c7f24d.jsonl[6579] _id=6abbe958485cab4c9580ed97 ts=2026-09-29T16:37:43.2740000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[8314] _id=6abe8aa3485cab4c95ac038c ts=2026-10-01T16:30:26.7460000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2822 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[10005] _id=6ac3d6d6de269131f9ae474f ts=2026-10-05T16:56:53.1960000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9900] _id=6ac3d6d6de269131f9ae4751 ts=2026-10-05T16:56:53.1960000Z; 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[10006] _id=6ac3d6d6de269131f9ae475f ts=2026-10-05T16:56:53.5490000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9947] _id=6ac3d6d6de269131f9ae4763 ts=2026-10-05T16:56:53.5490000Z; 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[10013] _id=6ac3d6cdde269131f9ae46ab ts=2026-10-05T16:56:44.5510000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[10014] _id=6ac3d6cdde269131f9ae46ad ts=2026-10-05T16:56:44.5510000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 72h 10m 
  - Evidence: 72h 10m: 6aa4142c41b41dbac0c7f24d.jsonl[2558] _id=6ab6a481485cab4c955bd6c2 ts=2026-09-25T16:42:41.3520000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3845] _id=6aba9b79485cab4c956adc75 ts=2026-09-28T16:53:13.0240000Z; 71h 35m: 6aa4142c41b41dbac0c7f24d.jsonl[3887] _id=6aba9baa485cab4c956ade8e ts=2026-09-28T16:54:02.3910000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[8284] _id=6abe8a88485cab4c95ac0040 ts=2026-10-01T16:30:00.6050000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f24d.jsonl[12963] _id=6ac679ebde269131f9bd5fe4 ts=2026-10-07T16:57:15.3950000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12964] _id=6ac679ebde269131f9bd5fe5 ts=2026-10-07T16:57:15.3960000Z; 8ms: 6aa4142c41b41dbac0c7f24d.jsonl[12962] _id=6ac679ebde269131f9bd5fe2 ts=2026-10-07T16:57:15.3870000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12963] _id=6ac679ebde269131f9bd5fe4 ts=2026-10-07T16:57:15.3950000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 71h 33m 
  - Evidence: 71h 33m: 6aa4142c41b41dbac0c7f24d.jsonl[3080] _id=6ab6a9f1485cab4c955d3849 ts=2026-09-25T17:05:53.6030000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3170] _id=6aba982b485cab4c956abf62 ts=2026-09-28T16:39:07.4290000Z; 24h 17m: 6aa4142c41b41dbac0c7f24d.jsonl[3172] _id=6aba9837485cab4c956abf9a ts=2026-09-28T16:39:19.2080000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[6855] _id=6abbedd2485cab4c958279d1 ts=2026-09-29T16:56:50.5830000Z; 23h 37m: 6aa4142c41b41dbac0c7f24d.jsonl[6864] _id=6abbedec485cab4c9582843b ts=2026-09-29T16:57:16.3780000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[7082] _id=6abd3a15485cab4c958dd4fa ts=2026-09-30T16:34:29.5680000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.034s shown 
  - Evidence: 26ms: 6aa4142c41b41dbac0c7f24d.jsonl[2952] _id=6ab6a81c485cab4c955d09cf ts=2026-09-25T16:58:04.7100000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[2947] _id=6ab6a81c485cab4c955d09d1 ts=2026-09-25T16:58:04.7360000Z; 34ms: 6aa4142c41b41dbac0c7f24d.jsonl[2947] _id=6ab6a81c485cab4c955d09d1 ts=2026-09-25T16:58:04.7360000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[2950] _id=6ab6a81d485cab4c955d09d9 ts=2026-09-25T16:58:04.7700000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 28m 
  - Evidence: 23h 28m: 6aa4142c41b41dbac0c7f24d.jsonl[12408] _id=6ac52ae1de269131f9b61483 ts=2026-10-06T17:07:45.3210000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12442] _id=6ac67514de269131f9bcad46 ts=2026-10-07T16:36:36.8440000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 287h 48m 
  - Evidence: 287h 48m: 6aa4142c41b41dbac0c7f24d.jsonl[962] _id=6ab55381485cab4c955347c9 ts=2026-09-24T16:44:49.3770000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11356] _id=6ac522e4de269131f9b51375 ts=2026-10-06T16:33:40.3800000Z; 24h 17m: 6aa4142c41b41dbac0c7f24d.jsonl[11356] _id=6ac522e4de269131f9b51375 ts=2026-10-06T16:33:40.3800000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12840] _id=6ac6787dde269131f9bd3f43 ts=2026-10-07T16:51:09.4300000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 287h 48m 
  - Evidence: 287h 48m: 6aa4142c41b41dbac0c7f24d.jsonl[949] _id=6ab55381485cab4c955347cb ts=2026-09-24T16:44:49.4000000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11297] _id=6ac522cfde269131f9b511f9 ts=2026-10-06T16:33:19.0490000Z; 24h 16m: 6aa4142c41b41dbac0c7f24d.jsonl[11354] _id=6ac522e4de269131f9b51383 ts=2026-10-06T16:33:40.4210000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12781] _id=6ac67852de269131f9bd39e7 ts=2026-10-07T16:50:26.1270000Z; 23h 37m: 6aa4142c41b41dbac0c7f24d.jsonl[765] _id=6ab406c2485cab4c954e9448 ts=2026-09-23T17:05:06.7760000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[879] _id=6ab552f2485cab4c95533dbd ts=2026-09-24T16:42:26.5980000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.026s..0.026s shown 
  - Evidence: 26ms: 6aa4142c41b41dbac0c7f24d.jsonl[11357] _id=6ac522e4de269131f9b51377 ts=2026-10-06T16:33:40.3950000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11354] _id=6ac522e4de269131f9b51383 ts=2026-10-06T16:33:40.4210000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 287h 48m 
  - Evidence: 287h 48m: 6aa4142c41b41dbac0c7f24d.jsonl[961] _id=6ab5537f485cab4c955347a7 ts=2026-09-24T16:44:47.7010000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11313] _id=6ac522cfde269131f9b51215 ts=2026-10-06T16:33:19.8650000Z; 24h 16m: 6aa4142c41b41dbac0c7f24d.jsonl[11352] _id=6ac522e2de269131f9b51361 ts=2026-10-06T16:33:38.6730000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12783] _id=6ac67857de269131f9bd3a73 ts=2026-10-07T16:50:31.8780000Z; 23h 36m: 6aa4142c41b41dbac0c7f24d.jsonl[784] _id=6ab406c8485cab4c954e9456 ts=2026-09-23T17:05:12.9330000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[864] _id=6ab552bd485cab4c955338d7 ts=2026-09-24T16:41:33.6080000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 45 interval(s) ≤ 0.005s..0.020s shown 
  - Evidence: 5ms: 6aa4142c41b41dbac0c7f24d.jsonl[12788] _id=6ac67859de269131f9bd3a98 ts=2026-10-07T16:50:33.4120000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12789] _id=6ac67859de269131f9bd3a9d ts=2026-10-07T16:50:33.4170000Z; 19ms: 6aa4142c41b41dbac0c7f24d.jsonl[898] _id=6ab55303485cab4c95533f59 ts=2026-09-24T16:42:43.8220000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[899] _id=6ab55303485cab4c95533f5b ts=2026-09-24T16:42:43.8410000Z; 20ms: 6aa4142c41b41dbac0c7f24d.jsonl[888] _id=6ab55302485cab4c95533f2f ts=2026-09-24T16:42:42.0160000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[889] _id=6ab55302485cab4c95533f33 ts=2026-09-24T16:42:42.0360000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 38m 
  - Evidence: 23h 38m: 6aa4142c41b41dbac0c7f24d.jsonl[9129] _id=6ac528a1de269131f9b5c2e7 ts=2026-10-06T16:58:09.5610000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12419] _id=6ac674fade269131f9bca7f6 ts=2026-10-07T16:36:10.3780000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 6aa4142c41b41dbac0c7f24d.jsonl[8201] _id=6abe8904485cab4c95abdca6 ts=2026-10-01T16:23:32.1590000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9139] _id=6ac3cfeede269131f9ada9c5 ts=2026-10-05T16:27:35.8840000Z; 72h 9m: 6aa4142c41b41dbac0c7f24d.jsonl[1079] _id=6ab6a09d485cab4c95594685 ts=2026-09-25T16:26:05.5260000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3116] _id=6aba9754485cab4c956ab8d0 ts=2026-09-28T16:35:32.5230000Z; 24h 9m: 6aa4142c41b41dbac0c7f24d.jsonl[8] _id=6ab3fde9485cab4c954e60da ts=2026-09-23T16:27:21.4920000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[801] _id=6ab551a4485cab4c95532227 ts=2026-09-24T16:36:52.0980000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 6aa4142c41b41dbac0c7f24d.jsonl[8200] _id=6abe8904485cab4c95abdca4 ts=2026-10-01T16:23:32.1580000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9138] _id=6ac3cfedde269131f9ada9c3 ts=2026-10-05T16:27:35.8820000Z; 71h 42m: 6aa4142c41b41dbac0c7f24d.jsonl[2787] _id=6ab6a6d6485cab4c955cead3 ts=2026-09-25T16:52:38.2010000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3115] _id=6aba9754485cab4c956ab8ce ts=2026-09-28T16:35:32.5220000Z; 24h 9m: 6aa4142c41b41dbac0c7f24d.jsonl[7] _id=6ab3fde9485cab4c954e60d8 ts=2026-09-23T16:27:21.4910000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[800] _id=6ab551a4485cab4c95532225 ts=2026-09-24T16:36:52.0980000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 142h 14m 
  - Evidence: 142h 14m: 6aa4142c41b41dbac0c7f24d.jsonl[8196] _id=6abd4ecc485cab4c9590d389 ts=2026-09-30T18:02:51.4750000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[11076] _id=6ac51f1ade269131f9b4f23f ts=2026-10-06T16:17:30.1350000Z; 71h 47m: 6aa4142c41b41dbac0c7f24d.jsonl[2785] _id=6ab6a6d5485cab4c955ceaac ts=2026-09-25T16:52:37.5080000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3253] _id=6aba9882485cab4c956ac1f0 ts=2026-09-28T16:40:34.4470000Z; 24h 30m: 6aa4142c41b41dbac0c7f24d.jsonl[11076] _id=6ac51f1ade269131f9b4f23f ts=2026-10-06T16:17:30.1350000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12733] _id=6ac677bade269131f9bd2cf8 ts=2026-10-07T16:47:54.1790000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 31m 
  - Evidence: 95h 31m: 6aa4142c41b41dbac0c7f24d.jsonl[9035] _id=6abe9094485cab4c95ac31de ts=2026-10-01T16:55:48.2900000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[9141] _id=6ac3cff7de269131f9adaa69 ts=2026-10-05T16:27:44.7170000Z; 71h 38m: 6aa4142c41b41dbac0c7f24d.jsonl[2939] _id=6ab6a804485cab4c955d08bd ts=2026-09-25T16:57:40.4410000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[3122] _id=6aba976f485cab4c956ab958 ts=2026-09-28T16:35:59.1150000Z; 23h 43m: 6aa4142c41b41dbac0c7f24d.jsonl[1058] _id=6ab55414485cab4c95534d11 ts=2026-09-24T16:47:16.9200000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[1127] _id=6ab6a1ae485cab4c9559f7ab ts=2026-09-25T16:30:38.9110000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[12546] _id=6ac675cfde269131f9bcd9aa ts=2026-10-07T16:39:43.4360000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12547] _id=6ac675cfde269131f9bcd9ab ts=2026-10-07T16:39:43.4360000Z; 0ms: 6aa4142c41b41dbac0c7f24d.jsonl[12892] _id=6ac678c8de269131f9bd4915 ts=2026-10-07T16:52:24.0070000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12893] _id=6ac678c8de269131f9bd4916 ts=2026-10-07T16:52:24.0070000Z; 1ms: 6aa4142c41b41dbac0c7f24d.jsonl[12339] _id=6ac52a57de269131f9b6106d ts=2026-10-06T17:05:27.5980000Z -> 6aa4142c41b41dbac0c7f24d.jsonl[12341] _id=6ac52a57de269131f9b6106f ts=2026-10-06T17:05:27.5990000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[633] _id=6ab40568485cab4c954e8d60 ts=2026-09-23T16:59:20.1520000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[967] _id=6ab55397485cab4c955348b7 ts=2026-09-24T16:45:11.7980000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[3079] _id=6ab6a9f0485cab4c955d3837 ts=2026-09-25T17:05:52.3770000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 102 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1534] _id=6ab6a33f485cab4c955afc07 ts=2026-09-25T16:37:17.6470000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1531] _id=6ab6a33f485cab4c955afc17 ts=2026-09-25T16:37:17.6470000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1535] _id=6ab6a33f485cab4c955afc20 ts=2026-09-25T16:37:17.7600000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 254 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1358] _id=6ab6a2f3485cab4c955acc3e ts=2026-09-25T16:33:05.4030000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1370] _id=6ab6a2f4485cab4c955accb6 ts=2026-09-25T16:33:05.4630000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1378] _id=6ab6a2f4485cab4c955accf9 ts=2026-09-25T16:33:05.5320000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[11354] _id=6ac522e4de269131f9b51383 ts=2026-10-06T16:33:40.4210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[866] _id=6ab552bd485cab4c955338dd ts=2026-09-24T16:41:33.7230000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[886] _id=6ab552fb485cab4c95533e67 ts=2026-09-24T16:42:35.4970000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[889] _id=6ab55302485cab4c95533f33 ts=2026-09-24T16:42:42.0360000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[9129] _id=6ac528a1de269131f9b5c2e7 ts=2026-10-06T16:58:09.5610000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[12419] _id=6ac674fade269131f9bca7f6 ts=2026-10-07T16:36:10.3780000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[12640] _id=6ac67686de269131f9bcf779 ts=2026-10-07T16:42:46.3390000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[12544] _id=6ac675cfde269131f9bcd9a4 ts=2026-10-07T16:39:43.4200000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[12545] _id=6ac675cfde269131f9bcd9a9 ts=2026-10-07T16:39:43.4280000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1082] _id=6ab6a0d6485cab4c95596cb3 ts=?`; `6aa4142c41b41dbac0c7f24d.jsonl[3123] _id=6aba976f485cab4c956ab94a ts=?`; `6aa4142c41b41dbac0c7f24d.jsonl[5648] _id=6abbe77c485cab4c9580c5c9 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 514 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1674] _id=6ab6a362485cab4c955b13b0 ts=2026-09-25T16:37:53.5650000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1668] _id=6ab6a362485cab4c955b13ba ts=2026-09-25T16:37:53.5950000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1692] _id=6ab6a368485cab4c955b17b5 ts=2026-09-25T16:37:59.8220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1055 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1360] _id=6ab6a2f2485cab4c955acc09 ts=2026-09-25T16:33:05.3610000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1334] _id=6ab6a2f2485cab4c955acc1d ts=2026-09-25T16:33:05.3610000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1340] _id=6ab6a2f3485cab4c955acc2e ts=2026-09-25T16:33:05.3610000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 23 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[2947] _id=6ab6a81c485cab4c955d09d1 ts=2026-09-25T16:58:04.7360000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[2950] _id=6ab6a81d485cab4c955d09d9 ts=2026-09-25T16:58:04.7700000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[3043] _id=6ab6a96d485cab4c955d316f ts=2026-09-25T17:03:41.4730000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[914] _id=6ab5535b485cab4c95534543 ts=2026-09-24T16:44:11.2380000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[883] _id=6ab552fa485cab4c95533e45 ts=2026-09-24T16:42:34.5820000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[897] _id=6ab55303485cab4c95533f55 ts=2026-09-24T16:42:43.5210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'DialogueStartEvent' (totals: 319 start, 313 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 99 unmatched 'BecameCameraCentered' (totals: 724 open, 727 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 223 unmatched 'BecameVisible' (totals: 1474 open, 1505 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 25 open, 23 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 6 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 46 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 304 of 13121 adjacent _id pairs reverse in client time; worst 176.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f24d.jsonl[1367] _id=6ab6a2f3485cab4c955acc22 ts=2026-09-25T16:36:02.2090000Z`; `6aa4142c41b41dbac0c7f24d.jsonl[1340] _id=6ab6a2f3485cab4c955acc2e ts=2026-09-25T16:33:05.3610000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -180.75s, max +9.91s over 13122 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f24d\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4430 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3356); Unit 4 Dev (654); Unit 5 Dev - Dungeon (420)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.26s, n=4429)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4430/4430 records)
    "BecameInvisible"  x1505
    "BecameVisible"  x1474
    "BecameCameraUncentered"  x727
    "BecameCameraCentered"  x724
data.pieceId  (string, 4430/4430 records)
    35 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4430/4430 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4011 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1295); Unit 3 Dev (768); Unit 4 Dev - Dungeon (628); Unit 4 Dev - Anderson Base (466); Unit 1 Dev (340); Unit 4 Dev (244); Unit 5 Dev - Dungeon (221); Unit 5 Dev (49)
- **Intervals:** median 0.93s (p5 0.09s / p95 14.26s, n=4010)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4011/4011 records)
    "pressed"  x4011
data.actionType  (string, 4011/4011 records)
    "Move"  x2539
    "Jump"  x557
    "Interact"  x544
    "Sprint"  x234
    "Ascend"  x78
    "Hoverboard"  x37
    "Map"  x10
    "Descend"  x9
    "SkipCinematic"  x2
    "ToggleDebug"  x1
data.key  (string, 4011/4011 records, 11 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4011/4011 records)
    "Player"  x3022
    "Drone"  x989
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2121 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (641); Unit 4 Dev (329); Unit 1 Dev (306); Unit 4 Dev - Dungeon (294); Unit 3 Dev (191); Unit 5 Dev (135); Unit 4 Dev - Anderson Base (124); Unit 5 Dev - Dungeon (101)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.02s, n=2111)
- **Fields under `data`:**

```text
data.position  (object, 2121/2121 records)
data.position.x  (number, 2121/2121 records)
    numeric range -336.71 .. 1556.96 (643 unique)
data.position.y  (number, 2121/2121 records)
    numeric range -114.326 .. 220.599 (467 unique)
data.position.z  (number, 2121/2121 records)
    numeric range -727.046 .. 1775.05 (643 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1744 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (496); Unit 4 Dev (311); Unit 1 Dev (244); Unit 5 Dev (213); Unit 3 Dev (154); Unit 4 Dev - Dungeon (128); Unit 4 Dev - Anderson Base (117); Unit 5 Dev - Dungeon (81)
- **eventKey:** present on 1112 of 1744 records
- **Intervals:** median 5.17s (p5 0.00s / p95 43.29s, n=1743)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1112; [conversationId, dialogueEventType] x632
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1744/1744 records)
    numeric range 8 .. 118 (44 unique)
data.dialogueEventType  (string, 1744/1744 records)
    "DialogueNodeEvent"  x1112
    "DialogueStartEvent"  x319
    "DialogueFinishEvent"  x313
data.nodeId  (number, 1112/1744 records)
    numeric range 0 .. 290 (178 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 249 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (102); Unit 1 Dev (48); Unit 2 Prod (Refactor) (42); Unit 4 Dev (21); Unit 4 Dev - Anderson Base (18); Unit 5 Dev (7); Unit 5 Dev - Dungeon (6); Unit 3 Dev (5)
- **Intervals:** median 10.78s (p5 0.20s / p95 558.16s, n=248)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 249/249 records)
    36 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 249/249 records)
    84 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 187 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (98); Unit 5 Dev (50); Unit 4 Dev - Anderson Base (39)
- **Intervals:** median 0.36s (p5 0.03s / p95 7.85s, n=186)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 187/187 records)
    "argumentationNodeHoverEnd"  x86
    "argumentationNodeHoverStart"  x82
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 187/187 records)
    "Unit 1 - Argumentation Tutorial"  x65
    "Unit 5"  x50
    "Unit 4 - Flooding"  x39
    "Unit 1 - Freshwater"  x33
data.nodeName  (string, 187/187 records)
    "I"  x40
    "1"  x39
    "A"  x32
    "II"  x22
    "3"  x13
    "4"  x10
    "C"  x10
    "B"  x8
    "2"  x7
    "D"  x6
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 76 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (41); Unit 2 Prod (Refactor) (35)
- **Intervals:** median 7.25s (p5 0.92s / p95 898.65s, n=75)
- **`data` key-set variants:** [actionType, featureUsed] x48; [actionType, featureUsed, location] x27; [actionType, featureUsed, legendName] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapOpenEvent"  x25
    "WaypointMoveEvent"  x24
    "MapCloseEvent"  x23
    "WaypointSetEvent"  x3
    "Selected"  x1
data.featureUsed  (string, 76/76 records)
    "Map"  x48
    "Waypoint"  x27
    "Legend"  x1
data.legendName  (string, 1/76 records)
    "90 ft"  x1
data.location  (object, 27/76 records)
data.location.x  (number, 27/76 records)
    numeric range -335.778 .. 298.482 (27 unique)
data.location.y  (number, 27/76 records)
    numeric range -269.5 .. 354.826 (26 unique)
data.location.z  (number, 27/76 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (15); Unit 2 Prod (Refactor) (14); Unit 4 Dev - Dungeon (12); Unit 4 Dev (11); Unit 5 Dev - Dungeon (10); Unit 5 Dev (7); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 234.50s (p5 0.00s / p95 85118.39s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x46; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x46
    "questFinishEvent"  x30
data.questID  (string, 76/76 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/76 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 42 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (36); Unit 4 Dev (6)
- **Intervals:** median 0.80s (p5 0.21s / p95 11.98s, n=41)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x36; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/42 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/42 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 36/42 records)
    "RightDrag"  x20
    "LeftDrag"  x16
data.currentSoilType  (string, 36/42 records)
    "CLAY"  x7
    "CLAYROCK"  x6
    "CLAYSAND"  x6
    "SAND"  x6
    "SANDGRAVEL"  x6
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 36/42 records)
    "false"  x29
    "true"  x7
data.waterLevelStatus  (string, 36/42 records)
    "TooHigh"  x24
    "Proper"  x9
    "TooLow"  x3
data.waterRetentionChange  (string, 36/42 records)
    "Increase"  x20
    "Decrease"  x9
    "NoChange"  x7
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 40 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (40)
- **Intervals:** median 5.70s (p5 1.06s / p95 76.72s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "On"  x26
    "Off"  x14
data.floor  (string, 40/40 records)
    "3"  x20
    "4"  x13
    "1"  x4
    "2"  x3
data.machineNumber  (string, 40/40 records)
    "One"  x39
    "Two"  x1
data.machineType  (string, 40/40 records)
    "Evaporator"  x14
    "Condenser"  x13
    "DualChamber_Evaporator"  x6
    "DualChamber_Condenser"  x5
    "VentSwitch"  x2
data.room  (string, 40/40 records)
    "2"  x20
    "3"  x12
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 27 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 2 Prod (Refactor) (6); Transition (2); Unit 3 Dev (2); Unit 5 Dev (1)
- **Intervals:** median 1373.33s (p5 62.19s / p95 215373.39s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    true  x27
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 20 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 1 Dev (2); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); MainMenu (1)
- **Intervals:** median 2113.71s (p5 80.59s / p95 268280.29s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "DebugMenuStateChanged"  x20
data.isOpened  (bool, 20/20 records)
    false  x20
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `SolarStillDesignEvent` — 17 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (17)
- **Intervals:** median 1.86s (p5 0.01s / p95 18.37s, n=16)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x16; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "optionSelected"  x16
    "DesignSubmitted"  x1
data.designSelections  (object, 1/17 records)
data.designSelections.glassRoofTemperature  (string, 1/17 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/17 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/17 records)
    "Tilted Out"  x1
data.featureUsed  (string, 17/17 records)
    "GlassRoofTemperature"  x8
    "RoofStyle"  x5
    "ExtraCovering"  x3
    "Submit"  x1
data.selectedOption  (string, 16/17 records, 3 empty-string)
    "Cold"  x4
    ""  x3
    "Hot"  x3
    "Tilted Out"  x2
    "Uncovered"  x2
    "Flat"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 84432.75s (p5 91.80s / p95 285590.02s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 12 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (12)
- **Intervals:** median 3.88s (p5 0.77s / p95 35.53s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records, 8 empty-string)
    ""  x8
    "cameraPlaced"  x4
data.boxId  (string, 12/12 records)
    "0"  x8
    "1"  x2
    "2"  x2
data.soilType  (string, 12/12 records)
    "Sand"  x7
    "Gravel"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 54.53s (p5 10.69s / p95 561757.68s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 12/12 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 4 - Flooding"  x3
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (6); Transition (2); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 3844.16s (p5 54.78s / p95 385277.80s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 42.84s (p5 1.86s / p95 181.17s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Clay"  x5
    "Gravel"  x3
    "Bedrock"  x2
    "Sand"  x1
data.floor  (string, 11/11 records)
    "5"  x7
    "4"  x3
    "3"  x1
data.machine  (string, 11/11 records)
    "1"  x10
    "2"  x1
data.row  (string, 11/11 records)
    "TopRow"  x9
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 6 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 98.86s (p5 5.63s / p95 846394.61s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "submitAnswerEvent"  x6
data.answerSubmitted  (string, 6/6 records)
    "A,1,I"  x2
    "A,1,II"  x2
    "C,A,D,2,II"  x1
    "C,D,3,II"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 4 - Flooding"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 6.09s (p5 3.78s / p95 1570.29s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "Permissions check failed"  x2
    "A user gesture is required to request Pointer Lock."  x1
    "Pointer is already locked."  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x2
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x3
    "unit5"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 562153.29s (p5 134441.37s / p95 989865.21s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3)
- **Intervals:** median 83.90s (p5 18.40s / p95 149.41s, n=2)
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

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 42738.39s (p5 4630.20s / p95 80846.57s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (36 records)
- `TerasGardenBox` data.actionType: "" (8x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (24x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (27x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*