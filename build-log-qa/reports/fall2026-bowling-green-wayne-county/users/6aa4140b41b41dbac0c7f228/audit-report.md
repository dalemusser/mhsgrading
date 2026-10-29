# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f228

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f228
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f228.jsonl
- **Records:** 15185 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f228
- **Time span:** 2026-09-23T13:56:05.962000+00:00 .. 2026-10-07T15:08:26.267000+00:00 (337h 12m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f228\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 15185 records, 11 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 102 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4865 | 32.04 | 1 | 4 | 0 | 2026-09-24T13:57:12.782000+00:00 | 2026-10-07T14:16:58.480000+00:00 | 312h 19m |
| InputEvent | 3843 | 25.31 | 1 | 9 | 0 | 2026-09-23T13:56:20.862000+00:00 | 2026-10-07T15:08:26.267000+00:00 | 337h 12m |
| DialogueEvent | 2331 | 15.35 | 1 | 9 | 1473 | 2026-09-23T13:56:42.776000+00:00 | 2026-10-07T15:08:14.626000+00:00 | 337h 11m |
| PlayerPositionEvent | 2314 | 15.24 | 1 | 9 | 0 | 2026-09-23T13:56:20.889000+00:00 | 2026-10-07T15:08:18.155000+00:00 | 337h 11m |
| argumentationNodeEvent | 794 | 5.23 | 1 | 5 | 0 | 2026-09-23T14:22:54.980000+00:00 | 2026-10-07T14:51:15.947000+00:00 | 336h 28m |
| ObjectInterEvent | 425 | 2.8 | 1 | 9 | 0 | 2026-09-23T14:02:46.907000+00:00 | 2026-10-07T15:08:26.267000+00:00 | 337h 5m |
| TopographicMapEvent | 137 | 0.9 | 1 | 4 | 0 | 2026-09-24T13:44:03.178000+00:00 | 2026-10-07T14:42:17.724000+00:00 | 312h 58m |
| questEvent | 91 | 0.6 | 1 | 9 | 91 | 2026-09-23T13:56:42.753000+00:00 | 2026-10-07T15:03:38.406000+00:00 | 337h 6m |
| argumentationAnswerEvent | 79 | 0.52 | 1 | 5 | 0 | 2026-09-23T14:30:12.363000+00:00 | 2026-10-07T14:51:17.149000+00:00 | 336h 21m |
| Soil Key Puzzle | 58 | 0.38 | 1 | 3 | 0 | 2026-09-25T14:24:23.324000+00:00 | 2026-10-01T14:03:32.133000+00:00 | 143h 39m |
| gameWindowFocusEvent | 31 | 0.2 | 1 | 7 | 0 | 2026-09-23T13:56:05.962000+00:00 | 2026-10-07T14:40:50.800000+00:00 | 336h 44m |
| WaterChamberEvent | 27 | 0.18 | 1 | 1 | 0 | 2026-10-07T14:16:00.817000+00:00 | 2026-10-07T14:26:26.212000+00:00 | 10m 25s |
| DEBUGMenu | 26 | 0.17 | 1 | 9 | 0 | 2026-09-23T13:56:20.885000+00:00 | 2026-10-07T14:40:50.358000+00:00 | 336h 44m |
| soilMachine | 23 | 0.15 | 1 | 1 | 0 | 2026-10-01T14:23:11.452000+00:00 | 2026-10-05T14:04:38.353000+00:00 | 95h 41m |
| argumentationEvent | 22 | 0.14 | 1 | 5 | 0 | 2026-09-23T14:24:59.026000+00:00 | 2026-10-07T14:51:17.183000+00:00 | 336h 26m |
| SolarStillDesignEvent | 19 | 0.13 | 1 | 1 | 0 | 2026-10-07T15:00:01.688000+00:00 | 2026-10-07T15:00:24.774000+00:00 | 23.1s |
| gameStartEvent | 19 | 0.13 | 1 | 1 | 0 | 2026-09-23T13:56:05.963000+00:00 | 2026-10-07T14:40:50.800000+00:00 | 336h 44m |
| DaniEvent | 18 | 0.12 | 1 | 4 | 0 | 2026-09-24T13:44:11.745000+00:00 | 2026-10-07T14:42:19.194000+00:00 | 312h 58m |
| TerasGardenBox | 17 | 0.11 | 1 | 1 | 0 | 2026-10-06T14:06:34.162000+00:00 | 2026-10-06T14:07:34.248000+00:00 | 1m 0s |
| argumentationToolEvent | 16 | 0.11 | 1 | 3 | 0 | 2026-09-23T14:24:54.628000+00:00 | 2026-10-07T14:50:02.135000+00:00 | 336h 25m |
| gameWindowUnfocusEvent | 12 | 0.08 | 1 | 7 | 0 | 2026-09-24T13:39:23.827000+00:00 | 2026-10-07T14:33:14.441000+00:00 | 312h 53m |
| chatEvent | 8 | 0.05 | 1 | 3 | 0 | 2026-09-24T13:44:14.570000+00:00 | 2026-10-07T14:41:51.996000+00:00 | 312h 57m |
| crash | 6 | 0.04 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-24T13:46:13.389000+00:00 | 2026-10-07T15:08:26.252000+00:00 | 313h 22m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 433668.266s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.037s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.284s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 9.334s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 4.255s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 146.488s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 6.143s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43625.208s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 468.076s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85037.714s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.334s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 15.8x vs baseline. 
  - Observed: 79 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,4,I; A,B,1,II; A,B,D,1,4,II; A,C,1,II; A,C,2,II; A,C,3,II; A,C,4,II; B,A,2,I; C,2,II; C,3,II; C,4,I; C,4,II; C,A,2,II; C,D,3,II; C,D,4,3,II; D,1,II; D,2,II; D,3,4,II; D,3,II; D,4,II; D,B,A,4,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.7x vs baseline. 
  - Observed: 794 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 8 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [30-100, 30-101, 30-102, 30-103, 30-104]; [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.6x vs baseline. 
  - Observed: 23 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 40 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[221] _id=6ab3dc71485cab4c954cf3ef ts=2026-09-23T14:04:33.0280000Z`; `6aa4140b41b41dbac0c7f228.jsonl[301] _id=6ab3dd7e485cab4c954cfcff ts=2026-09-23T14:09:02.2380000Z`; `6aa4140b41b41dbac0c7f228.jsonl[370] _id=6ab3de7b485cab4c954d034b ts=2026-09-23T14:13:15.3760000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[4365] _id=6aba7022485cab4c95681c57 ts=2026-09-28T13:48:16.5580000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[18] _id=6ab3da76485cab4c954ce3e1 ts=2026-09-23T13:56:05.9630000Z`; `6aa4140b41b41dbac0c7f228.jsonl[757] _id=6ab5278c485cab4c9551358b ts=2026-09-24T13:37:15.8170000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1057] _id=6ab529f2485cab4c955185dd ts=2026-09-24T13:47:30.6780000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 31 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 31} 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[21] _id=6ab3da76485cab4c954ce3df ts=2026-09-23T13:56:05.9620000Z`; `6aa4140b41b41dbac0c7f228.jsonl[756] _id=6ab5278b485cab4c95513587 ts=2026-09-24T13:37:15.8170000Z`; `6aa4140b41b41dbac0c7f228.jsonl[790] _id=6ab52811485cab4c9551406d ts=2026-09-24T13:39:29.8950000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[789] _id=6ab5280b485cab4c95513fc5 ts=2026-09-24T13:39:23.8270000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1092] _id=6ab52aa3485cab4c95519929 ts=2026-09-24T13:50:26.9850000Z`; `6aa4140b41b41dbac0c7f228.jsonl[2209] _id=6ab52ddc485cab4c9551cbdd ts=2026-09-24T14:04:12.9640000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 49 of 137 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[971] _id=6ab52923485cab4c95516365 ts=2026-09-24T13:44:03.1780000Z`; `6aa4140b41b41dbac0c7f228.jsonl[974] _id=6ab52925485cab4c955163c5 ts=2026-09-24T13:44:05.8940000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1175] _id=6ab52c55485cab4c9551b72f ts=2026-09-24T13:57:41.7430000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4864 | 0.0 | 0.037 | 231.165 | 1.754 | 345423.253 | 0.26 | 2736 | 8 |
| InputEvent | 3842 | 0.0 | 1.063 | 315.962 | 17.466 | 343257.538 | 0.19 | 170 | 10 |
| DialogueEvent | 2330 | 0.0 | 4.346 | 520.984 | 38.31 | 343332.168 | 0.12 | 652 | 10 |
| PlayerPositionEvent | 2302 | 9.446 | 9.999 | 527.208 | 10.029 | 343248.545 | 0.11 | 0 | 10 |
| argumentationNodeEvent | 793 | 0.001 | 0.425 | 1527.492 | 10.281 | 432741.396 | 0.04 | 169 | 7 |
| ObjectInterEvent | 424 | 0.001 | 7.424 | 2862.121 | 407.822 | 343384.971 | 0.02 | 5 | 15 |
| TopographicMapEvent | 136 | 0.027 | 2.337 | 8284.519 | 803.988 | 605322.763 | 0.01 | 2 | 8 |
| questEvent | 90 | 0.0 | 241.726 | 13484.618 | 84725.645 | 343599.145 | 0.0 | 16 | 19 |
| argumentationAnswerEvent | 78 | 0.152 | 4.255 | 15523.908 | 85290.701 | 432768.493 | 0.0 | 0 | 7 |
| Soil Key Puzzle | 57 | 0.154 | 0.822 | 9072.786 | 10.595 | 431384.045 | 0.01 | 0 | 2 |
| gameWindowFocusEvent | 30 | 3.592 | 468.076 | 40409.495 | 181493.382 | 345214.959 | 0.0 | 0 | 13 |
| WaterChamberEvent | 26 | 1.387 | 9.334 | 24.054 | 70.635 | 78.133 | 2.49 | 0 | 0 |
| DEBUGMenu | 25 | 10.389 | 905.59 | 48490.779 | 224488.109 | 344478.694 | 0.0 | 0 | 19 |
| soilMachine | 22 | 0.625 | 6.334 | 15658.496 | 152.386 | 343790.745 | 0.0 | 0 | 1 |
| argumentationEvent | 21 | 0.028 | 146.488 | 57675.15 | 348478.547 | 432742.626 | 0.0 | 2 | 7 |
| SolarStillDesignEvent | 18 | 0.525 | 1.077 | 1.283 | 2.37 | 2.581 | 46.78 | 0 | 0 |
| gameStartEvent | 18 | 108.493 | 43625.208 | 67349.158 | 271850.171 | 345219.591 | 0.0 | 0 | 14 |
| DaniEvent | 17 | 0.707 | 9.049 | 66275.732 | 344989.662 | 692485.242 | 0.0 | 0 | 5 |
| TerasGardenBox | 16 | 0.319 | 1.284 | 3.755 | 18.546 | 19.498 | 15.98 | 0 | 0 |
| argumentationToolEvent | 15 | 0.919 | 6.143 | 80740.5 | 512072.438 | 692335.252 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 11 | 0.976 | 85037.714 | 102402.783 | 384546.191 | 519357.805 | 0.0 | 0 | 9 |
| chatEvent | 7 | 2.235 | 821.6 | 160951.061 | 753135.409 | 1039225.693 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 3 | 89054.075 | 433668.266 | 376044.288 | 588236.296 | 605410.522 | 0.0 | 0 | 3 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 27 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[2911] _id=6ab67cd8485cab4c95559f18 ts=2026-09-25T13:53:27.2420000Z == 6aa4140b41b41dbac0c7f228.jsonl[2904] _id=6ab67cd8485cab4c95559f1a ts=2026-09-25T13:53:27.2420000Z`; `6aa4140b41b41dbac0c7f228.jsonl[13449] _id=6ac6530cde269131f9ba6bfd ts=2026-10-07T14:11:23.8300000Z == 6aa4140b41b41dbac0c7f228.jsonl[13450] _id=6ac6530cde269131f9ba6bfe ts=2026-10-07T14:11:23.8300000Z`; `6aa4140b41b41dbac0c7f228.jsonl[13454] _id=6ac6530cde269131f9ba6c02 ts=2026-10-07T14:11:23.8310000Z == 6aa4140b41b41dbac0c7f228.jsonl[13455] _id=6ac6530cde269131f9ba6c03 ts=2026-10-07T14:11:23.8310000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 176 group(s), 245 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[1308] _id=6ab52ccc485cab4c9551bc5d ts=2026-09-24T13:59:19.9460000Z == 6aa4140b41b41dbac0c7f228.jsonl[1324] _id=6ab52ccc485cab4c9551bc5f ts=2026-09-24T13:59:19.9460000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1316] _id=6ab52ccc485cab4c9551bc61 ts=2026-09-24T13:59:19.9670000Z == 6aa4140b41b41dbac0c7f228.jsonl[1317] _id=6ab52ccd485cab4c9551bc65 ts=2026-09-24T13:59:19.9670000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1333] _id=6ab52cce485cab4c9551bc8d ts=2026-09-24T13:59:32.6600000Z == 6aa4140b41b41dbac0c7f228.jsonl[1345] _id=6ab52cce485cab4c9551bc8f ts=2026-09-24T13:59:32.6600000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[2908] _id=6ab67cd8485cab4c95559f0e ts=? == 6aa4140b41b41dbac0c7f228.jsonl[6612] _id=6abbc387485cab4c957e11f5 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[14863] _id=6ac65cc5de269131f9bb326a ts=2026-10-07T14:52:53.4940000Z == 6aa4140b41b41dbac0c7f228.jsonl[14864] _id=6ac65cc5de269131f9bb326b ts=2026-10-07T14:52:53.4940000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 84 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4140b41b41dbac0c7f228.jsonl[161] _id=6ab3dc06485cab4c954cf06f ts=2026-09-23T14:02:46.9070000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[162] _id=6ab3dc06485cab4c954cf073 ts=2026-09-23T14:02:46.9090000Z`; `180ms: 6aa4140b41b41dbac0c7f228.jsonl[268] _id=6ab3dd60485cab4c954cfbaf ts=2026-09-23T14:08:32.8450000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[262] _id=6ab3dd60485cab4c954cfbb5 ts=2026-09-23T14:08:33.0250000Z`; `166ms: 6aa4140b41b41dbac0c7f228.jsonl[262] _id=6ab3dd60485cab4c954cfbb5 ts=2026-09-23T14:08:33.0250000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[266] _id=6ab3dd61485cab4c954cfbbb ts=2026-09-23T14:08:33.1910000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 635 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4140b41b41dbac0c7f228.jsonl[1315] _id=6ab52ccc485cab4c9551bc59 ts=2026-09-24T13:59:19.9290000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[1307] _id=6ab52ccc485cab4c9551bc5b ts=2026-09-24T13:59:19.9370000Z`; `9ms: 6aa4140b41b41dbac0c7f228.jsonl[1307] _id=6ab52ccc485cab4c9551bc5b ts=2026-09-24T13:59:19.9370000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[1308] _id=6ab52ccc485cab4c9551bc5d ts=2026-09-24T13:59:19.9460000Z`; `21ms: 6aa4140b41b41dbac0c7f228.jsonl[1324] _id=6ab52ccc485cab4c9551bc5f ts=2026-09-24T13:59:19.9460000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[1316] _id=6ab52ccc485cab4c9551bc61 ts=2026-09-24T13:59:19.9670000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `848ms: 6aa4140b41b41dbac0c7f228.jsonl[12973] _id=6ac5006dde269131f9b25468 ts=2026-10-06T14:06:37.3820000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[12971] _id=6ac5006ede269131f9b25472 ts=2026-10-06T14:06:38.2300000Z`; `898ms: 6aa4140b41b41dbac0c7f228.jsonl[12680] _id=6ac50075de269131f9b254e0 ts=2026-10-06T14:06:45.7640000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[12967] _id=6ac50076de269131f9b254ec ts=2026-10-06T14:06:46.6620000Z`; `436ms: 6aa4140b41b41dbac0c7f228.jsonl[12967] _id=6ac50076de269131f9b254ec ts=2026-10-06T14:06:46.6620000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[12968] _id=6ac50077de269131f9b254f0 ts=2026-10-06T14:06:47.0980000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `262ms: 6aa4140b41b41dbac0c7f228.jsonl[1218] _id=6ab52c85485cab4c9551b9c7 ts=2026-09-24T13:58:29.3500000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[1219] _id=6ab52c85485cab4c9551b9cb ts=2026-09-24T13:58:29.6120000Z`; `34ms: 6aa4140b41b41dbac0c7f228.jsonl[3670] _id=6ab6802a485cab4c9555ce24 ts=2026-09-25T14:07:38.7910000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[3673] _id=6ab6802b485cab4c9555ce32 ts=2026-09-25T14:07:38.8250000Z`; `532ms: 6aa4140b41b41dbac0c7f228.jsonl[7020] _id=6abbc8c9485cab4c957e8f83 ts=2026-09-29T14:18:49.4460000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[7022] _id=6abbc8c9485cab4c957e8fa3 ts=2026-09-29T14:18:49.9780000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 23 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `599ms: 6aa4140b41b41dbac0c7f228.jsonl[7625] _id=6abbcb99485cab4c957edeb7 ts=2026-09-29T14:30:49.4450000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[7627] _id=6abbcb9a485cab4c957edecd ts=2026-09-29T14:30:50.0440000Z`; `665ms: 6aa4140b41b41dbac0c7f228.jsonl[7658] _id=6abbcbb3485cab4c957ee22b ts=2026-09-29T14:31:15.1770000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[7663] _id=6abbcbb3485cab4c957ee23d ts=2026-09-29T14:31:15.8420000Z`; `359ms: 6aa4140b41b41dbac0c7f228.jsonl[7663] _id=6abbcbb3485cab4c957ee23d ts=2026-09-29T14:31:15.8420000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[7666] _id=6abbcbb4485cab4c957ee24b ts=2026-09-29T14:31:16.2010000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa4140b41b41dbac0c7f228.jsonl[7717] _id=6abbcbd8485cab4c957ee67b ts=2026-09-29T14:31:52.7430000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[7719] _id=6abbcbd9485cab4c957ee685 ts=2026-09-29T14:31:52.7710000Z`; `38ms: 6aa4140b41b41dbac0c7f228.jsonl[8135] _id=6abd1856485cab4c958a7ec2 ts=2026-09-30T14:10:30.1430000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[8137] _id=6abd1856485cab4c958a7ed6 ts=2026-09-30T14:10:30.1810000Z`; `56ms: 6aa4140b41b41dbac0c7f228.jsonl[12806] _id=6ac4ff24de269131f9b23e7f ts=2026-10-06T14:01:08.0060000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[12808] _id=6ac4ff24de269131f9b23e87 ts=2026-10-06T14:01:08.0620000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 109 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `660ms: 6aa4140b41b41dbac0c7f228.jsonl[549] _id=6ab3e0c2485cab4c954d1f0d ts=2026-09-23T14:22:58.4210000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[551] _id=6ab3e0c3485cab4c954d1f1b ts=2026-09-23T14:22:59.0810000Z`; `277ms: 6aa4140b41b41dbac0c7f228.jsonl[556] _id=6ab3e0c9485cab4c954d1f71 ts=2026-09-23T14:23:05.9500000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[557] _id=6ab3e0ca485cab4c954d1f77 ts=2026-09-23T14:23:06.2270000Z`; `378ms: 6aa4140b41b41dbac0c7f228.jsonl[580] _id=6ab3e148485cab4c954d23d1 ts=2026-09-23T14:25:12.1710000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[581] _id=6ab3e148485cab4c954d23d7 ts=2026-09-23T14:25:12.5490000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `976ms: 6aa4140b41b41dbac0c7f228.jsonl[13513] _id=6ac65373de269131f9ba74d5 ts=2026-10-07T14:13:07.0270000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[13514] _id=6ac65374de269131f9ba74e7 ts=2026-10-07T14:13:08.0030000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4140b41b41dbac0c7f228.jsonl[4365] _id=6aba7022485cab4c95681c57 ts=2026-09-28T13:48:16.5580000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[4392] _id=6aba7022485cab4c95681c59 ts=2026-09-28T13:48:16.5610000Z`; `2ms: 6aa4140b41b41dbac0c7f228.jsonl[14978] _id=6ac65ee1de269131f9bb64a5 ts=2026-10-07T15:01:53.1940000Z ~ 6aa4140b41b41dbac0c7f228.jsonl[14979] _id=6ac65ee1de269131f9bb64aa ts=2026-10-07T15:01:53.1960000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 41m 
  - Evidence: 95h 41m: 6aa4140b41b41dbac0c7f228.jsonl[10453] _id=6abe69b0485cab4c95a7a405 ts=2026-10-01T14:09:52.3590000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10949] _id=6ac3ab4dde269131f9a9f01c ts=2026-10-05T13:51:11.0530000Z; 71h 54m: 6aa4140b41b41dbac0c7f228.jsonl[2907] _id=6ab67cd1485cab4c95559eea ts=2026-09-25T13:53:21.0540000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4383] _id=6aba7018485cab4c95681bd3 ts=2026-09-28T13:48:09.1540000Z; 24h 8m: 6aa4140b41b41dbac0c7f228.jsonl[4383] _id=6aba7018485cab4c95681bd3 ts=2026-09-28T13:48:09.1540000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6607] _id=6abbc381485cab4c957e118d ts=2026-09-29T13:56:17.3000000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 192h 21m 
  - Evidence: 192h 21m: 6aa4140b41b41dbac0c7f228.jsonl[7155] _id=6abbc944485cab4c957e9ddd ts=2026-09-29T14:20:52.4860000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14471] _id=6ac65a46de269131f9bb04de ts=2026-10-07T14:42:17.7280000Z; 71h 41m: 6aa4140b41b41dbac0c7f228.jsonl[3699] _id=6ab6805f485cab4c9555d072 ts=2026-09-25T14:08:31.8770000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4503] _id=6aba70a3485cab4c95682543 ts=2026-09-28T13:50:27.6440000Z; 24h 15m: 6aa4140b41b41dbac0c7f228.jsonl[4378] _id=6aba70a4485cab4c95682557 ts=2026-09-28T13:50:28.7920000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6647] _id=6abbc5cb485cab4c957e5293 ts=2026-09-29T14:06:03.5570000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa4140b41b41dbac0c7f228.jsonl[10924] _id=6abe6e30485cab4c95a88f39 ts=2026-10-01T14:29:04.2360000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10951] _id=6ac3ab53de269131f9a9f1a0 ts=2026-10-05T13:51:16.4040000Z; 71h 19m: 6aa4140b41b41dbac0c7f228.jsonl[4200] _id=6ab6850f485cab4c9556461e ts=2026-09-25T14:28:31.3550000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4363] _id=6aba7022485cab4c95681c53 ts=2026-09-28T13:48:15.5950000Z; 23h 41m: 6aa4140b41b41dbac0c7f228.jsonl[13405] _id=6ac50607de269131f9b3371a ts=2026-10-06T14:30:31.9080000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13484] _id=6ac6531ade269131f9ba6d3f ts=2026-10-07T14:11:38.3460000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 652 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f228.jsonl[12799] _id=6ac4ff15de269131f9b23d69 ts=2026-10-06T14:00:52.9360000Z -> 6aa4140b41b41dbac0c7f228.jsonl[12800] _id=6ac4ff15de269131f9b23d6b ts=2026-10-06T14:00:52.9360000Z; 0ms: 6aa4140b41b41dbac0c7f228.jsonl[14713] _id=6ac65c00de269131f9bb21cc ts=2026-10-07T14:49:36.9160000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14714] _id=6ac65c00de269131f9bb21cd ts=2026-10-07T14:49:36.9160000Z; 0ms: 6aa4140b41b41dbac0c7f228.jsonl[14795] _id=6ac65c59de269131f9bb2880 ts=2026-10-07T14:51:05.1190000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14796] _id=6ac65c59de269131f9bb2881 ts=2026-10-07T14:51:05.1190000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 10m 
  - Evidence: 168h 10m: 6aa4140b41b41dbac0c7f228.jsonl[1055] _id=6ab529a5485cab4c95517a1d ts=2026-09-24T13:46:13.3890000Z -> 6aa4140b41b41dbac0c7f228.jsonl[9439] _id=6abe6687485cab4c95a75b13 ts=2026-10-01T13:56:23.9110000Z; 120h 27m: 6aa4140b41b41dbac0c7f228.jsonl[9439] _id=6abe6687485cab4c95a75b13 ts=2026-10-01T13:56:23.9110000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13176] _id=6ac5048cde269131f9b2ea4f ts=2026-10-06T14:24:12.1770000Z; 24h 44m: 6aa4140b41b41dbac0c7f228.jsonl[13176] _id=6ac5048cde269131f9b2ea4f ts=2026-10-06T14:24:12.1770000Z -> 6aa4140b41b41dbac0c7f228.jsonl[15181] _id=6ac6606ade269131f9bb8521 ts=2026-10-07T15:08:26.2520000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f228.jsonl[10944] _id=6abe6e7a485cab4c95a8a14b ts=2026-10-01T14:30:18.7180000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10956] _id=6ac3ab53de269131f9a9f16e ts=2026-10-05T13:51:16.2560000Z; 71h 19m: 6aa4140b41b41dbac0c7f228.jsonl[4231] _id=6ab68511485cab4c95564650 ts=2026-09-25T14:28:33.9410000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4368] _id=6aba7021485cab4c95681c35 ts=2026-09-28T13:48:15.5400000Z; 23h 40m: 6aa4140b41b41dbac0c7f228.jsonl[13428] _id=6ac5060dde269131f9b33872 ts=2026-10-06T14:30:36.7980000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13447] _id=6ac6530cde269131f9ba6bfb ts=2026-10-07T14:11:23.8280000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 170 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f228.jsonl[13449] _id=6ac6530cde269131f9ba6bfd ts=2026-10-07T14:11:23.8300000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13450] _id=6ac6530cde269131f9ba6bfe ts=2026-10-07T14:11:23.8300000Z; 0ms: 6aa4140b41b41dbac0c7f228.jsonl[13450] _id=6ac6530cde269131f9ba6bfe ts=2026-10-07T14:11:23.8300000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13451] _id=6ac6530cde269131f9ba6bff ts=2026-10-07T14:11:23.8300000Z; 0ms: 6aa4140b41b41dbac0c7f228.jsonl[13451] _id=6ac6530cde269131f9ba6bff ts=2026-10-07T14:11:23.8300000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13452] _id=6ac6530cde269131f9ba6c00 ts=2026-10-07T14:11:23.8300000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa4140b41b41dbac0c7f228.jsonl[10921] _id=6abe6e19485cab4c95a88ab3 ts=2026-10-01T14:28:41.3900000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10970] _id=6ac3ab71de269131f9a9f93a ts=2026-10-05T13:51:46.3610000Z; 71h 27m: 6aa4140b41b41dbac0c7f228.jsonl[4015] _id=6ab68417485cab4c955637b6 ts=2026-09-25T14:24:23.3290000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4636] _id=6aba70e9485cab4c95682bf5 ts=2026-09-28T13:51:37.5540000Z; 23h 55m: 6aa4140b41b41dbac0c7f228.jsonl[7113] _id=6abbc90e485cab4c957e98ab ts=2026-09-29T14:19:58.3260000Z -> 6aa4140b41b41dbac0c7f228.jsonl[8422] _id=6abd196c485cab4c958aba86 ts=2026-09-30T14:15:08.3920000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f228.jsonl[11972] _id=6ac3b1f6de269131f9ab54c2 ts=2026-10-05T14:19:34.4300000Z -> 6aa4140b41b41dbac0c7f228.jsonl[11976] _id=6ac3b1f6de269131f9ab54ca ts=2026-10-05T14:19:34.4310000Z; 1ms: 6aa4140b41b41dbac0c7f228.jsonl[12596] _id=6ac4fdf2de269131f9b1fa51 ts=2026-10-06T13:56:01.5710000Z -> 6aa4140b41b41dbac0c7f228.jsonl[12597] _id=6ac4fdf3de269131f9b1fa71 ts=2026-10-06T13:56:01.5720000Z; 2ms: 6aa4140b41b41dbac0c7f228.jsonl[11929] _id=6ac3b193de269131f9ab393b ts=2026-10-05T14:17:55.6020000Z -> 6aa4140b41b41dbac0c7f228.jsonl[11927] _id=6ac3b193de269131f9ab3943 ts=2026-10-05T14:17:55.6040000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f228.jsonl[10946] _id=6abe6e7e485cab4c95a8a268 ts=2026-10-01T14:30:22.5150000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10953] _id=6ac3ab53de269131f9a9f164 ts=2026-10-05T13:51:11.0600000Z; 69h 22m: 6aa4140b41b41dbac0c7f228.jsonl[10958] _id=6ac3ab34de269131f9a9eb22 ts=2026-09-25T16:25:43.113Z -> 6aa4140b41b41dbac0c7f228.jsonl[4358] _id=6aba7021485cab4c95681c33 ts=2026-09-28T13:48:09.1600000Z; 23h 40m: 6aa4140b41b41dbac0c7f228.jsonl[13424] _id=6ac5060cde269131f9b33860 ts=2026-10-06T14:30:36.4320000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13446] _id=6ac6530cde269131f9ba6bfa ts=2026-10-07T14:11:16.8080000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4140b41b41dbac0c7f228.jsonl[10440] _id=6abe6976485cab4c95a7a297 ts=2026-10-01T14:08:52.8500000Z -> 6aa4140b41b41dbac0c7f228.jsonl[11477] _id=6ac3aec4de269131f9aa9666 ts=2026-10-05T14:05:56.1030000Z; 71h 14m: 6aa4140b41b41dbac0c7f228.jsonl[4348] _id=6ab68633485cab4c95564cb2 ts=2026-09-25T14:33:20.6160000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4393] _id=6aba7022485cab4c95681c5b ts=2026-09-28T13:48:15.6510000Z; 48h 16m: 6aa4140b41b41dbac0c7f228.jsonl[5889] _id=6aba72b9485cab4c9568614b ts=2026-09-28T13:59:20.9850000Z -> 6aa4140b41b41dbac0c7f228.jsonl[8506] _id=6abd19a1485cab4c958ac71e ts=2026-09-30T14:16:00.7850000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2736 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f228.jsonl[10000] _id=6abe689e485cab4c95a797e7 ts=2026-10-01T14:05:16.9080000Z -> 6aa4140b41b41dbac0c7f228.jsonl[9992] _id=6abe689e485cab4c95a797e9 ts=2026-10-01T14:05:16.9080000Z; 0ms: 6aa4140b41b41dbac0c7f228.jsonl[10002] _id=6abe689e485cab4c95a797f9 ts=2026-10-01T14:05:17.0050000Z -> 6aa4140b41b41dbac0c7f228.jsonl[9982] _id=6abe689f485cab4c95a797fb ts=2026-10-01T14:05:17.0050000Z; 0ms: 6aa4140b41b41dbac0c7f228.jsonl[10012] _id=6abe68a2485cab4c95a79823 ts=2026-10-01T14:05:20.8910000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10013] _id=6abe68a2485cab4c95a79825 ts=2026-10-01T14:05:20.8910000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6aa4140b41b41dbac0c7f228.jsonl[4048] _id=6ab68454485cab4c95563ad0 ts=2026-09-25T14:25:24.3440000Z -> 6aa4140b41b41dbac0c7f228.jsonl[8476] _id=6abd196c485cab4c958aba7d ts=2026-09-30T14:15:08.3890000Z; 23h 47m: 6aa4140b41b41dbac0c7f228.jsonl[8487] _id=6abd197a485cab4c958abd9c ts=2026-09-30T14:15:22.5980000Z -> 6aa4140b41b41dbac0c7f228.jsonl[9714] _id=6abe681a485cab4c95a792c3 ts=2026-10-01T14:03:06.7650000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 168h 8m 
  - Evidence: 168h 8m: 6aa4140b41b41dbac0c7f228.jsonl[9254] _id=6abd1d9e485cab4c958b4abd ts=2026-09-30T14:33:02.8760000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14450] _id=6ac65a26de269131f9bb0295 ts=2026-10-07T14:41:45.6390000Z; 71h 32m: 6aa4140b41b41dbac0c7f228.jsonl[3870] _id=6ab682a4485cab4c95561e8a ts=2026-09-25T14:18:13.0020000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4481] _id=6aba7097485cab4c95682455 ts=2026-09-28T13:50:15.4650000Z; 24h 12m: 6aa4140b41b41dbac0c7f228.jsonl[7157] _id=6abbc943485cab4c957e9dc5 ts=2026-09-29T14:20:51.5220000Z -> 6aa4140b41b41dbac0c7f228.jsonl[9249] _id=6abd1d95485cab4c958b4a85 ts=2026-09-30T14:32:53.0590000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.034s shown 
  - Evidence: 27ms: 6aa4140b41b41dbac0c7f228.jsonl[3681] _id=6ab6802a485cab4c9555ce1d ts=2026-09-25T14:07:38.7640000Z -> 6aa4140b41b41dbac0c7f228.jsonl[3670] _id=6ab6802a485cab4c9555ce24 ts=2026-09-25T14:07:38.7910000Z; 34ms: 6aa4140b41b41dbac0c7f228.jsonl[3670] _id=6ab6802a485cab4c9555ce24 ts=2026-09-25T14:07:38.7910000Z -> 6aa4140b41b41dbac0c7f228.jsonl[3673] _id=6ab6802b485cab4c9555ce32 ts=2026-09-25T14:07:38.8250000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 12m 
  - Evidence: 120h 12m: 6aa4140b41b41dbac0c7f228.jsonl[8132] _id=6abd1856485cab4c958a7eb7 ts=2026-09-30T14:10:30.1220000Z -> 6aa4140b41b41dbac0c7f228.jsonl[12061] _id=6ac3b2d6de269131f9ab8f5e ts=2026-10-05T14:23:18.6150000Z; 96h 50m: 6aa4140b41b41dbac0c7f228.jsonl[908] _id=6ab528ae485cab4c955155c0 ts=2026-09-24T13:42:06.8180000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6583] _id=6aba7a7f485cab4c9568f40f ts=2026-09-28T14:32:31.8410000Z; 24h 47m: 6aa4140b41b41dbac0c7f228.jsonl[12805] _id=6ac4ff24de269131f9b23e7d ts=2026-10-06T14:01:07.9910000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14659] _id=6ac65bdbde269131f9bb1f1d ts=2026-10-07T14:48:59.6780000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 12m 
  - Evidence: 120h 12m: 6aa4140b41b41dbac0c7f228.jsonl[8137] _id=6abd1856485cab4c958a7ed6 ts=2026-09-30T14:10:30.1810000Z -> 6aa4140b41b41dbac0c7f228.jsonl[12044] _id=6ac3b2bcde269131f9ab8990 ts=2026-10-05T14:22:52.8070000Z; 96h 47m: 6aa4140b41b41dbac0c7f228.jsonl[899] _id=6ab528ae485cab4c955155c3 ts=2026-09-24T13:42:06.8410000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6538] _id=6aba79ed485cab4c9568ed85 ts=2026-09-28T14:30:05.3880000Z; 24h 46m: 6aa4140b41b41dbac0c7f228.jsonl[12808] _id=6ac4ff24de269131f9b23e87 ts=2026-10-06T14:01:08.0620000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14610] _id=6ac65ba2de269131f9bb1a01 ts=2026-10-07T14:48:02.6130000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.028s..0.038s shown 
  - Evidence: 28ms: 6aa4140b41b41dbac0c7f228.jsonl[7717] _id=6abbcbd8485cab4c957ee67b ts=2026-09-29T14:31:52.7430000Z -> 6aa4140b41b41dbac0c7f228.jsonl[7719] _id=6abbcbd9485cab4c957ee685 ts=2026-09-29T14:31:52.7710000Z; 38ms: 6aa4140b41b41dbac0c7f228.jsonl[8135] _id=6abd1856485cab4c958a7ec2 ts=2026-09-30T14:10:30.1430000Z -> 6aa4140b41b41dbac0c7f228.jsonl[8137] _id=6abd1856485cab4c958a7ed6 ts=2026-09-30T14:10:30.1810000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 12m 
  - Evidence: 120h 12m: 6aa4140b41b41dbac0c7f228.jsonl[8134] _id=6abd1856485cab4c958a7eb1 ts=2026-09-30T14:10:28.5610000Z -> 6aa4140b41b41dbac0c7f228.jsonl[12038] _id=6ac3b2bade269131f9ab88e3 ts=2026-10-05T14:22:49.9570000Z; 96h 48m: 6aa4140b41b41dbac0c7f228.jsonl[895] _id=6ab528a8485cab4c955154a7 ts=2026-09-24T13:42:00.7270000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6528] _id=6aba79e9485cab4c9568ed5d ts=2026-09-28T14:30:01.6550000Z; 24h 47m: 6aa4140b41b41dbac0c7f228.jsonl[12732] _id=6ac4ff20de269131f9b23e37 ts=2026-10-06T14:01:03.9960000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14615] _id=6ac65baade269131f9bb1a8c ts=2026-10-07T14:48:10.8910000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 169 interval(s) ≤ 0.001s..0.018s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f228.jsonl[810] _id=6ab52836485cab4c95514463 ts=2026-09-24T13:40:06.8010000Z -> 6aa4140b41b41dbac0c7f228.jsonl[812] _id=6ab52836485cab4c95514465 ts=2026-09-24T13:40:06.8020000Z; 14ms: 6aa4140b41b41dbac0c7f228.jsonl[812] _id=6ab52836485cab4c95514465 ts=2026-09-24T13:40:06.8020000Z -> 6aa4140b41b41dbac0c7f228.jsonl[811] _id=6ab52837485cab4c95514467 ts=2026-09-24T13:40:06.8160000Z; 18ms: 6aa4140b41b41dbac0c7f228.jsonl[589] _id=6ab3e149485cab4c954d23e7 ts=2026-09-23T14:25:13.5180000Z -> 6aa4140b41b41dbac0c7f228.jsonl[582] _id=6ab3e149485cab4c954d23e9 ts=2026-09-23T14:25:13.5360000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 192h 18m 
  - Evidence: 192h 18m: 6aa4140b41b41dbac0c7f228.jsonl[7598] _id=6abbcb75485cab4c957eda76 ts=2026-09-29T14:30:13.1510000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14685] _id=6ac65be4de269131f9bb1fca ts=2026-10-07T14:49:08.4030000Z; 120h 46m: 6aa4140b41b41dbac0c7f228.jsonl[874] _id=6ab528ab485cab4c95515507 ts=2026-09-24T13:42:03.5700000Z -> 6aa4140b41b41dbac0c7f228.jsonl[7547] _id=6abbcb2c485cab4c957ed349 ts=2026-09-29T14:29:00.5160000Z; 23h 10m: 6aa4140b41b41dbac0c7f228.jsonl[683] _id=6ab3e274485cab4c954d3089 ts=2026-09-23T14:30:12.2170000Z -> 6aa4140b41b41dbac0c7f228.jsonl[837] _id=6ab5284f485cab4c95514699 ts=2026-09-24T13:40:31.4190000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 288h 40m 
  - Evidence: 288h 40m: 6aa4140b41b41dbac0c7f228.jsonl[980] _id=6ab52933485cab4c955165dd ts=2026-09-24T13:44:19.5750000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13172] _id=6ac504adde269131f9b2ef7f ts=2026-10-06T14:24:45.2680000Z; 23h 46m: 6aa4140b41b41dbac0c7f228.jsonl[13172] _id=6ac504adde269131f9b2ef7f ts=2026-10-06T14:24:45.2680000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13435] _id=6ac65304de269131f9ba6b27 ts=2026-10-07T14:11:16.6800000Z; 16m 6s: 6aa4140b41b41dbac0c7f228.jsonl[13435] _id=6ac65304de269131f9ba6b27 ts=2026-10-07T14:11:16.6800000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14366] _id=6ac656cbde269131f9bad954 ts=2026-10-07T14:27:23.4950000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa4140b41b41dbac0c7f228.jsonl[9441] _id=6abe66b1485cab4c95a762bd ts=2026-10-01T13:57:05.6030000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10960] _id=6ac3ab34de269131f9a9eb2a ts=2026-10-05T13:50:45.1940000Z; 71h 55m: 6aa4140b41b41dbac0c7f228.jsonl[2900] _id=6ab67cb6485cab4c95559df4 ts=2026-09-25T13:52:53.8430000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4380] _id=6aba700c485cab4c95681ba5 ts=2026-09-28T13:47:56.4690000Z; 24h 8m: 6aa4140b41b41dbac0c7f228.jsonl[4380] _id=6aba700c485cab4c95681ba5 ts=2026-09-28T13:47:56.4690000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6606] _id=6abbc373485cab4c957e1039 ts=2026-09-29T13:56:02.1450000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa4140b41b41dbac0c7f228.jsonl[9446] _id=6abe66b6485cab4c95a7636f ts=2026-10-01T13:57:10.2320000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10959] _id=6ac3ab34de269131f9a9eb28 ts=2026-10-05T13:50:45.1910000Z; 71h 55m: 6aa4140b41b41dbac0c7f228.jsonl[2899] _id=6ab67cb6485cab4c95559df2 ts=2026-09-25T13:52:53.8430000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4379] _id=6aba700c485cab4c95681ba1 ts=2026-09-28T13:47:56.4680000Z; 24h 8m: 6aa4140b41b41dbac0c7f228.jsonl[4382] _id=6aba700f485cab4c95681bb7 ts=2026-09-28T13:48:00.0600000Z -> 6aa4140b41b41dbac0c7f228.jsonl[6605] _id=6abbc372485cab4c957e1020 ts=2026-09-29T13:56:02.1440000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 144h 15m 
  - Evidence: 144h 15m: 6aa4140b41b41dbac0c7f228.jsonl[9445] _id=6abe66b5485cab4c95a76355 ts=2026-10-01T13:57:09.2220000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13513] _id=6ac65373de269131f9ba74d5 ts=2026-10-07T14:13:07.0270000Z; 69h 22m: 6aa4140b41b41dbac0c7f228.jsonl[10964] _id=6ac3ab34de269131f9a9eb24 ts=2026-09-25T16:25:45.294Z -> 6aa4140b41b41dbac0c7f228.jsonl[4381] _id=6aba700f485cab4c95681bb3 ts=2026-09-28T13:47:59.8700000Z; 26h 21m: 6aa4140b41b41dbac0c7f228.jsonl[2209] _id=6ab52ddc485cab4c9551cbdd ts=2026-09-24T14:04:12.9640000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10964] _id=6ac3ab34de269131f9a9eb24 ts=2026-09-25T16:25:45.294Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4140b41b41dbac0c7f228.jsonl[10823] _id=6abe6d25485cab4c95a85681 ts=2026-10-01T14:24:37.1530000Z -> 6aa4140b41b41dbac0c7f228.jsonl[10963] _id=6ac3ab53de269131f9a9f196 ts=2026-10-05T13:51:16.2980000Z; 71h 24m: 6aa4140b41b41dbac0c7f228.jsonl[4005] _id=6ab68405485cab4c955636bc ts=2026-09-25T14:24:05.2970000Z -> 6aa4140b41b41dbac0c7f228.jsonl[4365] _id=6aba7022485cab4c95681c57 ts=2026-09-28T13:48:16.5580000Z; 23h 46m: 6aa4140b41b41dbac0c7f228.jsonl[13182] _id=6ac504aede269131f9b2efb9 ts=2026-10-06T14:24:45.3620000Z -> 6aa4140b41b41dbac0c7f228.jsonl[13469] _id=6ac6530cde269131f9ba6c11 ts=2026-10-07T14:11:23.8630000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f228.jsonl[14863] _id=6ac65cc5de269131f9bb326a ts=2026-10-07T14:52:53.4940000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14864] _id=6ac65cc5de269131f9bb326b ts=2026-10-07T14:52:53.4940000Z; 1ms: 6aa4140b41b41dbac0c7f228.jsonl[14041] _id=6ac65481de269131f9ba9647 ts=2026-10-07T14:17:37.5930000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14042] _id=6ac65481de269131f9ba9648 ts=2026-10-07T14:17:37.5940000Z; 2ms: 6aa4140b41b41dbac0c7f228.jsonl[14978] _id=6ac65ee1de269131f9bb64a5 ts=2026-10-07T15:01:53.1940000Z -> 6aa4140b41b41dbac0c7f228.jsonl[14979] _id=6ac65ee1de269131f9bb64aa ts=2026-10-07T15:01:53.1960000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 29m 
  - Evidence: 95h 29m: 6aa4140b41b41dbac0c7f228.jsonl[10844] _id=6abe6dab485cab4c95a871de ts=2026-10-01T14:26:51.3770000Z -> 6aa4140b41b41dbac0c7f228.jsonl[11141] _id=6ac3ac99de269131f9aa3d32 ts=2026-10-05T13:56:42.1220000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[495] _id=6ab3e076485cab4c954d1b14 ts=2026-09-23T14:21:42.1840000Z`; `6aa4140b41b41dbac0c7f228.jsonl[669] _id=6ab3e294485cab4c954d32a0 ts=2026-09-23T14:30:44.9150000Z`; `6aa4140b41b41dbac0c7f228.jsonl[905] _id=6ab528c0485cab4c955157d5 ts=2026-09-24T13:42:24.6440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 92 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[1408] _id=6ab52ce9485cab4c9551be28 ts=2026-09-24T14:00:07.1550000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1475] _id=6ab52cea485cab4c9551be43 ts=2026-09-24T14:00:07.4170000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1466] _id=6ab52ceb485cab4c9551be85 ts=2026-09-24T14:00:07.8030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 255 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[1258] _id=6ab52cc7485cab4c9551bbc0 ts=2026-09-24T13:57:13.2900000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1260] _id=6ab52cc7485cab4c9551bbc7 ts=2026-09-24T13:57:13.3440000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1242] _id=6ab52cc8485cab4c9551bbd4 ts=2026-09-24T13:57:13.5170000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[7719] _id=6abbcbd9485cab4c957ee685 ts=2026-09-29T14:31:52.7710000Z`; `6aa4140b41b41dbac0c7f228.jsonl[8137] _id=6abd1856485cab4c958a7ed6 ts=2026-09-30T14:10:30.1810000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 17 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[582] _id=6ab3e149485cab4c954d23e9 ts=2026-09-23T14:25:13.5360000Z`; `6aa4140b41b41dbac0c7f228.jsonl[600] _id=6ab3e14b485cab4c954d240b ts=2026-09-23T14:25:15.6600000Z`; `6aa4140b41b41dbac0c7f228.jsonl[663] _id=6ab3e25c485cab4c954d2e76 ts=2026-09-23T14:29:48.7400000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[13172] _id=6ac504adde269131f9b2ef7f ts=2026-10-06T14:24:45.2680000Z`; `6aa4140b41b41dbac0c7f228.jsonl[13435] _id=6ac65304de269131f9ba6b27 ts=2026-10-07T14:11:16.6800000Z`; `6aa4140b41b41dbac0c7f228.jsonl[14366] _id=6ac656cbde269131f9bad954 ts=2026-10-07T14:27:23.4950000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[10968] _id=6ac3ab63de269131f9a9f57f ts=2026-10-05T13:51:32.4600000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[19] _id=6ab3da8a485cab4c954ce41f ts=?`; `6aa4140b41b41dbac0c7f228.jsonl[2908] _id=6ab67cd8485cab4c95559f0e ts=?`; `6aa4140b41b41dbac0c7f228.jsonl[6612] _id=6abbc387485cab4c957e11f5 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 603 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[1341] _id=6ab52cd1485cab4c9551bcc5 ts=2026-09-24T13:59:45.1210000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1464] _id=6ab52ce8485cab4c9551be0d ts=2026-09-24T14:00:07.0190000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1453] _id=6ab52cf1485cab4c9551bf27 ts=2026-09-24T14:00:16.6770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 939 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[1265] _id=6ab52cc7485cab4c9551bbb9 ts=2026-09-24T13:57:13.2900000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1241] _id=6ab52cc8485cab4c9551bbcf ts=2026-09-24T13:57:13.5170000Z`; `6aa4140b41b41dbac0c7f228.jsonl[1253] _id=6ab52cc8485cab4c9551bbeb ts=2026-09-24T13:57:13.6800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[3670] _id=6ab6802a485cab4c9555ce24 ts=2026-09-25T14:07:38.7910000Z`; `6aa4140b41b41dbac0c7f228.jsonl[3673] _id=6ab6802b485cab4c9555ce32 ts=2026-09-25T14:07:38.8250000Z`; `6aa4140b41b41dbac0c7f228.jsonl[3700] _id=6ab6805f485cab4c9555d074 ts=2026-09-25T14:08:31.8880000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[12657] _id=6ac4fe94de269131f9b22924 ts=2026-10-06T13:58:44.2000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 74 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[799] _id=6ab52821485cab4c95514225 ts=2026-09-24T13:39:45.2670000Z`; `6aa4140b41b41dbac0c7f228.jsonl[803] _id=6ab52822485cab4c9551424b ts=2026-09-24T13:39:46.2170000Z`; `6aa4140b41b41dbac0c7f228.jsonl[801] _id=6ab52823485cab4c95514279 ts=2026-09-24T13:39:47.7000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[686] _id=6ab3e273485cab4c954d3072 ts=2026-09-23T14:30:11.2980000Z`; `6aa4140b41b41dbac0c7f228.jsonl[874] _id=6ab528ab485cab4c95515507 ts=2026-09-24T13:42:03.5700000Z`; `6aa4140b41b41dbac0c7f228.jsonl[7598] _id=6abbcb75485cab4c957eda76 ts=2026-09-29T14:30:13.1510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 434 start, 424 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 136 unmatched 'BecameCameraCentered' (totals: 992 open, 948 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 134 unmatched 'BecameVisible' (totals: 1402 open, 1523 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 21 open, 19 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'argumentationNodeHoverStart' (totals: 344 open, 350 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 12 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 55 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 344 of 15178 adjacent _id pairs reverse in client time; worst 607189.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f228.jsonl[10946] _id=6abe6e7e485cab4c95a8a268 ts=2026-10-01T14:30:22.5150000Z`; `6aa4140b41b41dbac0c7f228.jsonl[10957] _id=6ac3ab33de269131f9a9eb05 ts=2026-09-24T13:50:33.228Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -950410.30s, max +2.83s over 15179 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f228\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 6 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4865 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3143); Unit 4 Dev (874); Unit 5 Dev - Dungeon (586); Unit 3 Dungeon Dev (262)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.75s, n=4864)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4865/4865 records)
    "BecameInvisible"  x1523
    "BecameVisible"  x1402
    "BecameCameraCentered"  x992
    "BecameCameraUncentered"  x948
data.pieceId  (string, 4865/4865 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4865/4865 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3843 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (971); Unit 2 Prod (Refactor) (858); Unit 4 Dev - Dungeon (501); Unit 4 Dev (336); Unit 5 Dev - Dungeon (300); Unit 1 Dev (275); Unit 3 Dungeon Dev (258); Unit 4 Dev - Anderson Base (178); Unit 5 Dev (166)
- **Intervals:** median 1.06s (p5 0.07s / p95 17.47s, n=3842)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3843/3843 records)
    "pressed"  x3843
data.actionType  (string, 3843/3843 records)
    "Move"  x2547
    "Interact"  x617
    "Jump"  x462
    "Hoverboard"  x113
    "Ascend"  x51
    "Sprint"  x21
    "Descend"  x13
    "Map"  x11
    "Pause"  x5
    "SkipCinematic"  x3
data.key  (string, 3843/3843 records, 3 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3843/3843 records)
    "Player"  x2933
    "Drone"  x910
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2331 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (615); Unit 3 Dev (413); Unit 1 Dev (283); Unit 4 Dev (263); Unit 5 Dev (241); Unit 4 Dev - Anderson Base (184); Unit 4 Dev - Dungeon (128); Unit 3 Dungeon Dev (120); Unit 5 Dev - Dungeon (84)
- **eventKey:** present on 1473 of 2331 records
- **Intervals:** median 4.35s (p5 0.00s / p95 38.31s, n=2330)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1473; [conversationId, dialogueEventType] x858
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2331/2331 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2331/2331 records)
    "DialogueNodeEvent"  x1473
    "DialogueStartEvent"  x434
    "DialogueFinishEvent"  x424
data.nodeId  (number, 1473/2331 records)
    numeric range 0 .. 290 (233 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2314 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (642); Unit 3 Dev (352); Unit 1 Dev (265); Unit 4 Dev (265); Unit 4 Dev - Dungeon (211); Unit 5 Dev (194); Unit 4 Dev - Anderson Base (166); Unit 5 Dev - Dungeon (132); Unit 3 Dungeon Dev (87)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2302)
- **Fields under `data`:**

```text
data.position  (object, 2314/2314 records)
data.position.x  (number, 2314/2314 records)
    numeric range -684.016 .. 1555.89 (743 unique)
data.position.y  (number, 2314/2314 records)
    numeric range -115.127 .. 222.252 (514 unique)
data.position.z  (number, 2314/2314 records)
    numeric range -1158.89 .. 1964.47 (742 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 794 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (338); Unit 3 Dev (160); Unit 1 Dev (141); Unit 5 Dev (122); Unit 2 Prod (Refactor) (33)
- **Intervals:** median 0.42s (p5 0.02s / p95 10.28s, n=793)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 794/794 records)
    "argumentationNodeHoverEnd"  x350
    "argumentationNodeHoverStart"  x344
    "argumentationNodeAdd"  x62
    "argumentationNodeRemove"  x38
data.argumentationTitle  (string, 794/794 records)
    "Unit 4 - Flooding"  x338
    "Unit 3 - Pollution Upstream"  x160
    "Unit 5"  x122
    "Unit 1 - Argumentation Tutorial"  x91
    "Unit 1 - Freshwater"  x50
    "Unit 2 – Watershed"  x33
data.nodeName  (string, 794/794 records)
    "I"  x115
    "1"  x109
    "A"  x103
    "4"  x87
    "II"  x72
    "D"  x68
    "B"  x63
    "3"  x62
    "2"  x58
    "C"  x41
    "5"  x16
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 425 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (134); Unit 4 Dev - Dungeon (110); Unit 1 Dev (36); Unit 5 Dev - Dungeon (34); Unit 3 Dungeon Dev (31); Unit 4 Dev (26); Unit 5 Dev (25); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (11)
- **Intervals:** median 7.42s (p5 0.17s / p95 407.82s, n=424)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 425/425 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 425/425 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 137 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (100); Unit 3 Dev (29); Unit 5 Dev (6); Unit 1 Dev (2)
- **Intervals:** median 2.34s (p5 0.43s / p95 803.99s, n=136)
- **`data` key-set variants:** [actionType, featureUsed, legendName] x49; [actionType, featureUsed, location] x48; [actionType, featureUsed] x40
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 137/137 records)
    "Selected"  x43
    "WaypointMoveEvent"  x36
    "MapOpenEvent"  x21
    "MapCloseEvent"  x19
    "WaypointSetEvent"  x11
    "Unselected"  x6
    "WaypointResetEvent"  x1
data.featureUsed  (string, 137/137 records)
    "Legend"  x49
    "Waypoint"  x48
    "Map"  x40
data.legendName  (string, 49/137 records)
    14 unique values (see csv/event_unique_values.csv)
data.location  (object, 48/137 records)
data.location.x  (number, 48/137 records)
    numeric range -244.09 .. 241.91 (33 unique)
data.location.y  (number, 48/137 records)
    numeric range -282.5 .. 337.5 (41 unique)
data.location.z  (number, 48/137 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 91 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (17); Unit 3 Dev (14); Unit 4 Dev - Dungeon (13); Unit 4 Dev (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (8); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 91 of 91 records
- **Intervals:** median 241.73s (p5 0.00s / p95 84725.65s, n=90)
- **`data` key-set variants:** [questEventType, questID, questName] x55; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 91/91 records)
    "questActiveEvent"  x55
    "questFinishEvent"  x36
data.questID  (string, 91/91 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 91/91 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/91 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 79 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (25); Unit 3 Dev (24); Unit 5 Dev (24); Unit 1 Dev (5); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 4.25s (p5 0.17s / p95 85290.70s, n=78)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 79/79 records)
    "submitAnswerEvent"  x79
data.answerSubmitted  (string, 79/79 records)
    28 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 79/79 records)
    "Unit 4 - Flooding"  x25
    "Unit 3 - Pollution Upstream"  x24
    "Unit 5"  x24
    "Unit 1 - Freshwater"  x5
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `Soil Key Puzzle` — 58 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev (20); Unit 3 Dev (12)
- **Intervals:** median 0.82s (p5 0.21s / p95 10.59s, n=57)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/58 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/58 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/58 records)
    "RightDrag"  x29
    "LeftDrag"  x23
data.currentSoilType  (string, 52/58 records)
    "CLAYSAND"  x11
    "SAND"  x11
    "CLAY"  x9
    "SANDGRAVEL"  x9
    "CLAYROCK"  x6
    "GRAVEL"  x4
    "BEDROCK"  x2
data.isCorrectSelection  (string, 52/58 records)
    "false"  x41
    "true"  x11
data.waterLevelStatus  (string, 52/58 records)
    "Proper"  x18
    "TooHigh"  x18
    "TooLow"  x16
data.waterRetentionChange  (string, 52/58 records)
    "Decrease"  x21
    "Increase"  x20
    "NoChange"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 31 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (2); Transition (1); Unit 1 Dev (1)
- **Intervals:** median 468.08s (p5 4.53s / p95 181493.38s, n=30)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 31/31 records)
    true  x31
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 27 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (27)
- **Intervals:** median 9.33s (p5 1.57s / p95 70.63s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "On"  x19
    "Off"  x8
data.floor  (string, 27/27 records)
    "3"  x14
    "4"  x7
    "2"  x4
    "1"  x2
data.machineNumber  (string, 27/27 records)
    "One"  x26
    "Two"  x1
data.machineType  (string, 27/27 records)
    "Condenser"  x11
    "Evaporator"  x7
    "DualChamber_Evaporator"  x4
    "DualChamber_Condenser"  x3
    "VentSwitch"  x2
data.room  (string, 27/27 records)
    "2"  x12
    "3"  x7
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 26 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (4); Unit 4 Dev (3); MainMenu (2); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 905.59s (p5 106.12s / p95 224488.11s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "DebugMenuStateChanged"  x26
data.isOpened  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 23 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (23)
- **Intervals:** median 6.33s (p5 0.84s / p95 152.39s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "ChangeCanister"  x23
data.canisterType  (string, 23/23 records)
    "Gravel"  x8
    "Sand"  x7
    "Clay"  x6
    "Bedrock"  x2
data.floor  (string, 23/23 records)
    "3"  x11
    "4"  x6
    "5"  x6
data.machine  (string, 23/23 records)
    "1"  x21
    "2"  x2
data.row  (string, 23/23 records)
    "TopRow"  x20
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 22 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (6); Unit 4 Dev - Anderson Base (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 146.49s (p5 0.04s / p95 348478.55s, n=21)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "argumentationSessionClose"  x12
    "argumentationSessionOpen"  x10
data.argumentationDescription  (string, 22/22 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 22/22 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 4 - Flooding"  x4
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 19 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (19)
- **Intervals:** median 1.08s (p5 0.54s / p95 2.37s, n=18)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x18; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "optionSelected"  x18
    "DesignSubmitted"  x1
data.designSelections  (object, 1/19 records)
data.designSelections.glassRoofTemperature  (string, 1/19 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/19 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/19 records)
    "Tilted Out"  x1
data.featureUsed  (string, 19/19 records)
    "RoofStyle"  x14
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "Submit"  x1
data.selectedOption  (string, 18/19 records, 3 empty-string)
    "Tilted Out"  x5
    "Flat"  x4
    ""  x3
    "Tilted In"  x2
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 43625.21s (p5 118.93s / p95 271850.17s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (8); Unit 2 Prod (Refactor) (6); Unit 1 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 9.05s (p5 0.91s / p95 344989.66s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 18 empty-string)
    ""  x18
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 17 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (17)
- **Intervals:** median 1.28s (p5 0.41s / p95 18.55s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records, 14 empty-string)
    ""  x14
    "cameraPlaced"  x3
data.boxId  (string, 17/17 records)
    "0"  x13
    "1"  x2
    "2"  x2
data.soilType  (string, 17/17 records)
    "Gravel"  x7
    "Sand"  x7
    "Clay"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (8); Unit 5 Dev (5); Unit 3 Dev (3)
- **Intervals:** median 6.14s (p5 1.06s / p95 512072.44s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolOpen"  x12
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 16/16 records)
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (2); MainMenu (1); Transition (1); Unit 1 Dev (1)
- **Intervals:** median 85037.71s (p5 53.48s / p95 384546.19s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 8 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (4); Unit 1 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 821.60s (p5 3.07s / p95 753135.41s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x6
    "Open"  x2
data.chatID  (string, 8/8 records)
    "NA"  x6
    "[30-100, 30-101, 30-102, 30-103, 30-104]"  x1
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x3
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x3
data.type  (string, 6/6 records)
    "unhandled_rejection"  x6
data.unitId  (string, 6/6 records)
    "unit2"  x2
    "unit1"  x1
    "unit3"  x1
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 433668.27s (p5 123515.49s / p95 588236.30s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (26 records)
- `TerasGardenBox` data.actionType: "" (14x)
- `TopographicMapEvent` data.actionType: "Selected" (43x); "Unselected" (6x); "WaypointMoveEvent" (36x); "WaypointResetEvent" (1x); "WaypointSetEvent" (11x)
- `TopographicMapEvent` data.featureUsed: "Legend" (49x); "Waypoint" (48x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (38x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*