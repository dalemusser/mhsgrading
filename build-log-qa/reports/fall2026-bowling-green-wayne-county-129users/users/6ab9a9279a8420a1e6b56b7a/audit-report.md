# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7a
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b7a.jsonl
- **Records:** 14592 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b7a
- **Time span:** 2026-10-06T18:40:59.323000+00:00 .. 2026-10-16T18:58:53.667000+00:00 (240h 17m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 14592 records, 10 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 104 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4308 | 29.52 | 1 | 9 | 0 | 2026-10-06T18:46:26.664000+00:00 | 2026-10-16T18:58:41.804000+00:00 | 240h 12m |
| PlayerPositionEvent | 2826 | 19.37 | 1 | 9 | 0 | 2026-10-06T18:41:22.307000+00:00 | 2026-10-16T18:58:53.667000+00:00 | 240h 17m |
| PuzzlePieceVisibleEvent | 2630 | 18.02 | 1 | 4 | 0 | 2026-10-08T18:52:08.912000+00:00 | 2026-10-15T21:16:16.502000+00:00 | 170h 24m |
| DialogueEvent | 2608 | 17.87 | 1 | 9 | 1624 | 2026-10-06T18:41:42.287000+00:00 | 2026-10-16T18:58:50.648000+00:00 | 240h 17m |
| argumentationNodeEvent | 1087 | 7.45 | 1 | 4 | 0 | 2026-10-06T19:09:28.283000+00:00 | 2026-10-15T20:47:59.231000+00:00 | 217h 38m |
| ObjectInterEvent | 403 | 2.76 | 1 | 9 | 0 | 2026-10-06T18:48:12.140000+00:00 | 2026-10-16T18:58:50.649000+00:00 | 240h 10m |
| Soil Key Puzzle | 180 | 1.23 | 1 | 3 | 0 | 2026-10-08T19:04:38.698000+00:00 | 2026-10-15T18:35:24.031000+00:00 | 167h 30m |
| TopographicMapEvent | 118 | 0.81 | 1 | 3 | 0 | 2026-10-07T18:54:16.019000+00:00 | 2026-10-14T22:39:18.109000+00:00 | 171h 45m |
| questEvent | 90 | 0.62 | 1 | 9 | 90 | 2026-10-06T18:41:42.264000+00:00 | 2026-10-16T18:56:43.225000+00:00 | 240h 15m |
| WaterChamberEvent | 60 | 0.41 | 1 | 1 | 0 | 2026-10-15T21:15:26.031000+00:00 | 2026-10-16T18:50:18.846000+00:00 | 21h 34m |
| argumentationAnswerEvent | 55 | 0.38 | 1 | 4 | 0 | 2026-10-06T19:09:49.411000+00:00 | 2026-10-15T20:48:00.064000+00:00 | 217h 38m |
| DEBUGMenu | 53 | 0.36 | 1 | 9 | 0 | 2026-10-06T18:41:22.284000+00:00 | 2026-10-16T18:35:29.815000+00:00 | 239h 54m |
| gameWindowFocusEvent | 31 | 0.21 | 1 | 6 | 0 | 2026-10-06T18:40:59.323000+00:00 | 2026-10-16T18:35:11.122000+00:00 | 239h 54m |
| DaniEvent | 23 | 0.16 | 1 | 3 | 0 | 2026-10-07T18:54:22.976000+00:00 | 2026-10-14T18:57:33.563000+00:00 | 168h 3m |
| gameStartEvent | 23 | 0.16 | 1 | 1 | 0 | 2026-10-06T18:40:59.324000+00:00 | 2026-10-16T18:35:11.122000+00:00 | 239h 54m |
| TerasGardenBox | 21 | 0.14 | 1 | 1 | 0 | 2026-10-15T20:52:17.815000+00:00 | 2026-10-15T20:54:53.011000+00:00 | 2m 35s |
| argumentationEvent | 17 | 0.12 | 1 | 4 | 0 | 2026-10-06T19:09:24.667000+00:00 | 2026-10-15T20:48:00.140000+00:00 | 217h 38m |
| soilMachine | 16 | 0.11 | 1 | 1 | 0 | 2026-10-15T18:50:20.244000+00:00 | 2026-10-15T18:57:24.349000+00:00 | 7m 4s |
| argumentationToolEvent | 15 | 0.1 | 1 | 2 | 0 | 2026-10-06T19:09:20.645000+00:00 | 2026-10-14T16:09:56.007000+00:00 | 189h 0m |
| gameWindowUnfocusEvent | 12 | 0.08 | 1 | 6 | 0 | 2026-10-07T18:57:55.400000+00:00 | 2026-10-15T20:40:05.267000+00:00 | 193h 42m |
| chatEvent | 11 | 0.08 | 1 | 4 | 0 | 2026-10-07T18:54:26.937000+00:00 | 2026-10-16T18:53:10.349000+00:00 | 215h 58m |
| EndOfUnit | 5 | 0.03 | 1 | 4 | 0 | 2026-10-06T19:16:47.456000+00:00 | 2026-10-15T21:10:03.530000+00:00 | 217h 53m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 277.525s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 83524.017s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.07s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.919s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.196s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 18.873s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 156.423s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.245s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 8.573s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6331.971s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1674.93s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 12629.667s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.901s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.4x vs baseline. 
  - Observed: 53 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 23 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 4.7x vs baseline. 
  - Observed: 180 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Teleporter Room; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 60 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 11.0x vs baseline. 
  - Observed: 55 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,II; 2,II; A,2,I; A,2,II; A,3,I; A,3,II; A,4,I; A,4,II; A,B,1,II; A,B,C,2,II; A,C,B,2,II; B,2,II; B,4,II; B,A,C,2,II; B,C,2,II; B,C,A,2,II; C,1,I; C,1,II; C,2,II; C,3,II; C,4,II; C,A,2,II; C,B,A,2,II; C,D,2,II; C,D,A,2,II; D,1,I; D,2,II; D,4,II; D,C,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 7.8x vs baseline. 
  - Observed: 1087 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.5x vs baseline. 
  - Observed: 11 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [16-3, 18-1, 18-2, 18-4, 18-5]; [18-271, 18-273, 18-179, 68-1, 68-5]; [18-7, 18-9, 18-10, 17-17, 17-19, 17-20, 17-22]; [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[131] _id=6ac542f0de269131f9b6fbb6 ts=2026-10-06T18:50:24.5160000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[195] _id=6ac54431de269131f9b713dd ts=2026-10-06T18:55:45.3930000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[248] _id=6ac544f6de269131f9b71fa8 ts=2026-10-06T18:59:01.8210000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[1] _id=6ac540bbde269131f9b6b5d5 ts=2026-10-06T18:40:59.3240000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[731] _id=6ac6931ade269131f9bdf938 ts=2026-10-07T18:44:40.4040000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[835] _id=6ac693b3de269131f9be0dca ts=2026-10-07T18:47:15.0290000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 31 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 31} 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[0] _id=6ac540bbde269131f9b6b5d1 ts=2026-10-06T18:40:59.3230000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[730] _id=6ac6931ade269131f9bdf937 ts=2026-10-07T18:44:40.4040000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[834] _id=6ac693b3de269131f9be0dc9 ts=2026-10-07T18:47:15.0290000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[1495] _id=6ac69634de269131f9be9714 ts=2026-10-07T18:57:55.4000000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4190] _id=6ace815ade269131f9d15f88 ts=2026-10-13T19:07:05.7500000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4192] _id=6ace815dde269131f9d15ff5 ts=2026-10-13T19:07:08.5710000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 8 of 118 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[1259] _id=6ac69558de269131f9be622d ts=2026-10-07T18:54:16.0190000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[1269] _id=6ac6955fde269131f9be6403 ts=2026-10-07T18:54:22.9690000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[1226] _id=6ac69567de269131f9be65ad ts=2026-10-07T18:54:30.9310000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4307 | 0.0 | 1.103 | 200.774 | 20.611 | 429622.584 | 0.3 | 130 | 17 |
| PlayerPositionEvent | 2812 | 0.0 | 10.001 | 270.648 | 10.143 | 429598.571 | 0.22 | 3 | 12 |
| PuzzlePieceVisibleEvent | 2629 | 0.0 | 0.07 | 233.339 | 2.712 | 431405.336 | 0.26 | 1166 | 9 |
| DialogueEvent | 2607 | 0.0 | 3.986 | 331.81 | 35.828 | 429673.029 | 0.18 | 751 | 15 |
| argumentationNodeEvent | 1086 | 0.001 | 0.326 | 721.465 | 10.932 | 593497.879 | 0.08 | 103 | 5 |
| ObjectInterEvent | 402 | 0.0 | 8.61 | 2150.842 | 467.292 | 431517.319 | 0.03 | 6 | 19 |
| Soil Key Puzzle | 179 | 0.118 | 0.98 | 3368.968 | 14.566 | 431514.238 | 0.02 | 0 | 6 |
| TopographicMapEvent | 117 | 0.019 | 4.919 | 5284.633 | 1277.202 | 429872.564 | 0.01 | 4 | 8 |
| questEvent | 89 | 0.001 | 229.577 | 9717.988 | 54011.08 | 429763.097 | 0.01 | 17 | 25 |
| WaterChamberEvent | 59 | 0.516 | 8.196 | 1316.827 | 92.728 | 76439.835 | 0.05 | 0 | 1 |
| argumentationAnswerEvent | 54 | 0.601 | 18.873 | 14509.086 | 36973.115 | 593599.413 | 0.0 | 0 | 5 |
| DEBUGMenu | 52 | 0.0 | 277.525 | 16608.606 | 81042.302 | 431331.732 | 0.0 | 1 | 23 |
| gameWindowFocusEvent | 30 | 1.906 | 1674.93 | 28788.393 | 86268.634 | 431343.365 | 0.0 | 0 | 21 |
| DaniEvent | 22 | 0.246 | 3.556 | 27499.572 | 86172.677 | 431593.422 | 0.0 | 0 | 5 |
| gameStartEvent | 22 | 64.821 | 6331.971 | 39256.9 | 86584.878 | 431343.364 | 0.0 | 0 | 18 |
| TerasGardenBox | 20 | 0.636 | 2.846 | 7.76 | 27.39 | 27.762 | 7.73 | 0 | 0 |
| argumentationEvent | 16 | 0.033 | 156.423 | 48969.717 | 213545.34 | 593498.906 | 0.0 | 2 | 6 |
| soilMachine | 15 | 0.288 | 7.901 | 28.274 | 122.583 | 176.282 | 2.12 | 0 | 0 |
| argumentationToolEvent | 14 | 0.067 | 2.245 | 48602.526 | 263991.806 | 593682.645 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 11 | 0.515 | 12629.667 | 63393.624 | 293755.014 | 518950.35 | 0.0 | 0 | 8 |
| chatEvent | 10 | 0.662 | 8.573 | 77752.341 | 375981.553 | 612784.58 | 0.0 | 0 | 4 |
| EndOfUnit | 4 | 23471.38 | 83524.017 | 196099.019 | 517768.472 | 593876.66 | 0.0 | 0 | 4 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 12 group(s), 34 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[737] _id=6ac69323de269131f9bdfa60 ts=2026-10-07T18:44:50.6920000Z == 6ab9a9279a8420a1e6b56b7a.jsonl[738] _id=6ac69323de269131f9bdfa61 ts=2026-10-07T18:44:50.6920000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[1085] _id=6ac69516de269131f9be4fe9 ts=2026-10-07T18:53:09.8200000Z == 6ab9a9279a8420a1e6b56b7a.jsonl[1086] _id=6ac69516de269131f9be4fea ts=2026-10-07T18:53:09.8200000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[1418] _id=6ac69604de269131f9be8a89 ts=2026-10-07T18:57:06.9950000Z == 6ab9a9279a8420a1e6b56b7a.jsonl[1419] _id=6ac69604de269131f9be8a8a ts=2026-10-07T18:57:06.9950000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 28 group(s), 43 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[4169] _id=6ace814cde269131f9d15c90 ts=2026-10-13T19:06:50.8050000Z == 6ab9a9279a8420a1e6b56b7a.jsonl[4171] _id=6ace814cde269131f9d15c96 ts=2026-10-13T19:06:50.8050000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4146] _id=6ace814ede269131f9d15d53 ts=2026-10-13T19:06:52.1310000Z == 6ab9a9279a8420a1e6b56b7a.jsonl[4181] _id=6ace814ede269131f9d15d78 ts=2026-10-13T19:06:52.1310000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4403] _id=6ace97d1de269131f9d258ad ts=2026-10-13T20:42:56.4540000Z == 6ab9a9279a8420a1e6b56b7a.jsonl[4404] _id=6ace97d1de269131f9d258ae ts=2026-10-13T20:42:56.4540000Z`
- **INFO / Info** `DEBUGMenu` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[6550] _id=6acfc9afde269131f9d70e2f ts=2026-10-14T18:27:58.7890000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[6551] _id=6acfc9e6de269131f9d7106c ts=2026-10-14T18:27:58.789Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 90 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b7a.jsonl[100] _id=6ac5426cde269131f9b6eab3 ts=2026-10-06T18:48:12.1400000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[98] _id=6ac5426cde269131f9b6eabf ts=2026-10-06T18:48:12.1450000Z`; `696ms: 6ab9a9279a8420a1e6b56b7a.jsonl[760] _id=6ac6934cde269131f9be0009 ts=2026-10-07T18:45:32.0530000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[757] _id=6ac6934dde269131f9be001d ts=2026-10-07T18:45:32.7490000Z`; `329ms: 6ab9a9279a8420a1e6b56b7a.jsonl[763] _id=6ac6934fde269131f9be006e ts=2026-10-07T18:45:35.0310000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[766] _id=6ac69350de269131f9be008c ts=2026-10-07T18:45:35.3600000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `636ms: 6ab9a9279a8420a1e6b56b7a.jsonl[13381] _id=6ad13d80de269131f9e14018 ts=2026-10-15T20:54:24.4290000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[13387] _id=6ad13d81de269131f9e14020 ts=2026-10-15T20:54:25.0650000Z`; `800ms: 6ab9a9279a8420a1e6b56b7a.jsonl[13372] _id=6ad13d8ade269131f9e14051 ts=2026-10-15T20:54:34.5030000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[13382] _id=6ad13d8bde269131f9e1405d ts=2026-10-15T20:54:35.3030000Z`; `653ms: 6ab9a9279a8420a1e6b56b7a.jsonl[13382] _id=6ad13d8bde269131f9e1405d ts=2026-10-15T20:54:35.3030000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[13394] _id=6ad13d8cde269131f9e1406a ts=2026-10-15T20:54:35.9560000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `601ms: 6ab9a9279a8420a1e6b56b7a.jsonl[7927] _id=6acfd227de269131f9d7f97c ts=2026-10-14T19:04:06.7050000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[7919] _id=6acfd228de269131f9d7f986 ts=2026-10-14T19:04:07.3060000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6ab9a9279a8420a1e6b56b7a.jsonl[7921] _id=6acfd22bde269131f9d7f9bc ts=2026-10-14T19:04:10.6840000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[7924] _id=6acfd22bde269131f9d7f9bf ts=2026-10-14T19:04:10.7230000Z`; `33ms: 6ab9a9279a8420a1e6b56b7a.jsonl[13206] _id=6ad13c00de269131f9e137f9 ts=2026-10-15T20:48:00.1070000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[13209] _id=6ad13c00de269131f9e137fc ts=2026-10-15T20:48:00.1400000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 34 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `58ms: 6ab9a9279a8420a1e6b56b7a.jsonl[430] _id=6ac54774de269131f9b7665d ts=2026-10-06T19:09:40.5030000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[433] _id=6ac54775de269131f9b76661 ts=2026-10-06T19:09:40.5610000Z`; `71ms: 6ab9a9279a8420a1e6b56b7a.jsonl[371] _id=6ac547ddde269131f9b76d73 ts=2026-10-06T19:11:25.4590000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[372] _id=6ac547ddde269131f9b76d77 ts=2026-10-06T19:11:25.5300000Z`; `651ms: 6ab9a9279a8420a1e6b56b7a.jsonl[520] _id=6ac547fede269131f9b76fc5 ts=2026-10-06T19:11:57.7050000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[518] _id=6ac547fede269131f9b76fd0 ts=2026-10-06T19:11:58.3560000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `515ms: 6ab9a9279a8420a1e6b56b7a.jsonl[7344] _id=6acfceb0de269131f9d7968b ts=2026-10-14T18:49:19.2420000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[7341] _id=6acfceb0de269131f9d7969b ts=2026-10-14T18:49:19.7570000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `415ms: 6ab9a9279a8420a1e6b56b7a.jsonl[11481] _id=6ad120d2de269131f9df69b1 ts=2026-10-15T18:52:01.4620000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[11480] _id=6ad120d2de269131f9df69ba ts=2026-10-15T18:52:01.8770000Z`; `288ms: 6ab9a9279a8420a1e6b56b7a.jsonl[11480] _id=6ad120d2de269131f9df69ba ts=2026-10-15T18:52:01.8770000Z ~ 6ab9a9279a8420a1e6b56b7a.jsonl[11484] _id=6ad120d3de269131f9df69c3 ts=2026-10-15T18:52:02.1650000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a9279a8420a1e6b56b7a.jsonl[1989] _id=6ac7e58fde269131f9c58a18 ts=2026-10-08T18:48:46.9130000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3613] _id=6ace7a73de269131f9d0fd7e ts=2026-10-13T18:37:38.6450000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7a.jsonl[3] _id=6ac540d2de269131f9b6b83b ts=2026-10-06T18:41:22.2840000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[729] _id=6ac69319de269131f9bdf92d ts=2026-10-07T18:44:40.2020000Z; 23h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[1415] _id=6ac69601de269131f9be89f5 ts=2026-10-07T18:57:05.4650000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1986] _id=6ac7e584de269131f9c5896d ts=2026-10-08T18:48:35.4940000Z
- **INFO / Info** `DEBUGMenu` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[6550] _id=6acfc9afde269131f9d70e2f ts=2026-10-14T18:27:58.7890000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6551] _id=6acfc9e6de269131f9d7106c ts=2026-10-14T18:27:58.789Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a9279a8420a1e6b56b7a.jsonl[2702] _id=6ac7e781de269131f9c5cac5 ts=2026-10-08T18:57:05.0700000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3852] _id=6ace7d6ade269131f9d12ad2 ts=2026-10-13T18:50:18.4920000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7a.jsonl[1273] _id=6ac69567de269131f9be65a9 ts=2026-10-07T18:54:30.9230000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[2700] _id=6ac7e77fde269131f9c5ca26 ts=2026-10-08T18:57:02.2790000Z; 21h 56m: 6ab9a9279a8420a1e6b56b7a.jsonl[4873] _id=6ace9950de269131f9d25d9a ts=2026-10-13T20:49:20.0660000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[7157] _id=6acfcdd2de269131f9d77c61 ts=2026-10-14T18:45:37.8380000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a9279a8420a1e6b56b7a.jsonl[3611] _id=6ac7ec55de269131f9c68712 ts=2026-10-08T19:17:41.0570000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3639] _id=6ace7abede269131f9d10429 ts=2026-10-13T18:38:54.0860000Z; 23h 41m: 6ab9a9279a8420a1e6b56b7a.jsonl[720] _id=6ac5491dde269131f9b79580 ts=2026-10-06T19:16:45.0000000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1561] _id=6ac69657de269131f9be9f0e ts=2026-10-07T18:58:30.3480000Z; 23h 30m: 6ab9a9279a8420a1e6b56b7a.jsonl[1971] _id=6ac69af6de269131f9bf20f5 ts=2026-10-07T19:18:13.7100000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[2004] _id=6ac7e594de269131f9c58a63 ts=2026-10-08T18:48:51.2180000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 751 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12573] _id=6ad13743de269131f9e12628 ts=2026-10-15T20:27:46.9620000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12574] _id=6ad13743de269131f9e12629 ts=2026-10-15T20:27:46.9620000Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12584] _id=6ad13754de269131f9e12650 ts=2026-10-15T20:28:04.2320000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12585] _id=6ad13754de269131f9e12651 ts=2026-10-15T20:28:04.2320000Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12639] _id=6ad137adde269131f9e126f7 ts=2026-10-15T20:29:33.2430000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12640] _id=6ad137adde269131f9e126f8 ts=2026-10-15T20:29:33.2430000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 164h 57m 
  - Evidence: 164h 57m: 6ab9a9279a8420a1e6b56b7a.jsonl[1966] _id=6ac69af8de269131f9bf20f7 ts=2026-10-07T19:18:16.1980000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6397] _id=6acfaacdde269131f9d54934 ts=2026-10-14T16:16:12.8580000Z; 24h 1m: 6ab9a9279a8420a1e6b56b7a.jsonl[722] _id=6ac5491fde269131f9b795c3 ts=2026-10-06T19:16:47.4560000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1966] _id=6ac69af8de269131f9bf20f7 ts=2026-10-07T19:18:16.1980000Z; 22h 22m: 6ab9a9279a8420a1e6b56b7a.jsonl[9805] _id=6ad0067cde269131f9d99bad ts=2026-10-14T22:47:24.2380000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[13688] _id=6ad1412bde269131f9e1656b ts=2026-10-15T21:10:03.5300000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9279a8420a1e6b56b7a.jsonl[3597] _id=6ac7ec54de269131f9c686ed ts=2026-10-08T19:17:39.8750000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3619] _id=6ace7a8ade269131f9d10013 ts=2026-10-13T18:38:02.4590000Z; 23h 31m: 6ab9a9279a8420a1e6b56b7a.jsonl[1953] _id=6ac69ac5de269131f9bf20b0 ts=2026-10-07T19:17:25.0140000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1991] _id=6ac7e593de269131f9c58a46 ts=2026-10-08T18:48:49.7010000Z; 23h 28m: 6ab9a9279a8420a1e6b56b7a.jsonl[694] _id=6ac548f0de269131f9b78ea6 ts=2026-10-06T19:16:00.3920000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[736] _id=6ac69323de269131f9bdfa5f ts=2026-10-07T18:44:50.6900000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 130 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[10668] _id=6ad11c6ade269131f9deec41 ts=2026-10-15T18:33:13.3420000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[10669] _id=6ad11c6ade269131f9deec42 ts=2026-10-15T18:33:13.3420000Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[10669] _id=6ad11c6ade269131f9deec42 ts=2026-10-15T18:33:13.3420000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[10670] _id=6ad11c6ade269131f9deec43 ts=2026-10-15T18:33:13.3420000Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[1085] _id=6ac69516de269131f9be4fe9 ts=2026-10-07T18:53:09.8200000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1086] _id=6ac69516de269131f9be4fea ts=2026-10-07T18:53:09.8200000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[3292] _id=6ac7e947de269131f9c61446 ts=2026-10-08T19:04:38.7060000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3970] _id=6ace7ee4de269131f9d13375 ts=2026-10-13T18:56:36.0250000Z; 23h 34m: 6ab9a9279a8420a1e6b56b7a.jsonl[1967] _id=6ac69acdde269131f9bf20c2 ts=2026-10-07T19:17:33.0540000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[2068] _id=6ac7e636de269131f9c59d56 ts=2026-10-08T18:51:33.8430000Z; 23h 28m: 6ab9a9279a8420a1e6b56b7a.jsonl[670] _id=6ac548f4de269131f9b78f5e ts=2026-10-06T19:16:04.3900000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[740] _id=6ac6932ede269131f9bdfbb6 ts=2026-10-07T18:45:01.6040000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12019] _id=6ad124afde269131f9dff995 ts=2026-10-15T19:08:30.0430000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12020] _id=6ad124afde269131f9dff996 ts=2026-10-15T19:08:30.0430000Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12053] _id=6ad124f7de269131f9e00490 ts=2026-10-15T19:09:42.7500000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12054] _id=6ad124f7de269131f9e00491 ts=2026-10-15T19:09:42.7500000Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12424] _id=6ad13634de269131f9e1241f ts=2026-10-15T20:23:16.4520000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12425] _id=6ad13634de269131f9e12420 ts=2026-10-15T20:23:16.4520000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b7a.jsonl[3612] _id=6ac7ec5fde269131f9c687f5 ts=2026-10-08T19:17:50.8990000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3617] _id=6ace7a83de269131f9d0ff37 ts=2026-10-13T18:37:49.4700000Z; 23h 28m: 6ab9a9279a8420a1e6b56b7a.jsonl[721] _id=6ac54919de269131f9b79509 ts=2026-10-06T19:16:41.6810000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[735] _id=6ac69323de269131f9bdfa5e ts=2026-10-07T18:44:48.9720000Z; 21h 12m: 6ab9a9279a8420a1e6b56b7a.jsonl[14115] _id=6ad14427de269131f9e17c7a ts=2026-10-15T21:22:46.8810000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[14142] _id=6ad26e77de269131f9e71338 ts=2026-10-16T18:35:29.8220000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[5374] _id=6ace9f48de269131f9d26ef8 ts=2026-10-13T21:14:48.1650000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[5381] _id=6acf779fde269131f9d2cea0 ts=2026-10-13T21:14:48.165Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[6544] _id=6acfc9b2de269131f9d70e39 ts=2026-10-14T18:27:58.8020000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6555] _id=6acfc9e6de269131f9d7106d ts=2026-10-14T18:27:58.802Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[775] _id=6ac693a5de269131f9be0b85 ts=2026-10-07T18:47:00.9920000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[832] _id=6ac693b3de269131f9be0db7 ts=2026-10-07T18:47:00.992Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a9279a8420a1e6b56b7a.jsonl[3269] _id=6ac7e905de269131f9c606e5 ts=2026-10-08T19:03:30.3090000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3918] _id=6ace7e30de269131f9d1303c ts=2026-10-13T18:53:35.6450000Z; 22h 20m: 6ab9a9279a8420a1e6b56b7a.jsonl[4902] _id=6ace995fde269131f9d25dd9 ts=2026-10-13T20:49:34.6150000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[8172] _id=6acfd39ede269131f9d83239 ts=2026-10-14T19:10:20.3200000Z; 15h 2m: 6ab9a9279a8420a1e6b56b7a.jsonl[8732] _id=6acff6fede269131f9d98110 ts=2026-10-14T21:41:15.6440000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[9945] _id=6ad117bade269131f9dedfe9 ts=2026-10-15T12:44:10.967Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1166 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[10001] _id=6ad117bbde269131f9dee020 ts=2026-10-15T12:44:58.947Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[10002] _id=6ad117bbde269131f9dee021 ts=2026-10-15T12:44:58.947Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[10012] _id=6ad117bbde269131f9dee02b ts=2026-10-15T12:45:02.164Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[10013] _id=6ad117bbde269131f9dee02c ts=2026-10-15T12:45:02.164Z; 0ms: 6ab9a9279a8420a1e6b56b7a.jsonl[10018] _id=6ad117bbde269131f9dee031 ts=2026-10-15T12:45:03.897Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[10019] _id=6ad117bbde269131f9dee032 ts=2026-10-15T12:45:03.897Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[3294] _id=6ac7e94ade269131f9c614b6 ts=2026-10-08T19:04:41.7820000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3975] _id=6ace7ee4de269131f9d13373 ts=2026-10-13T18:56:36.0200000Z; 22h 27m: 6ab9a9279a8420a1e6b56b7a.jsonl[4377] _id=6ace977dde269131f9d25807 ts=2026-10-13T20:41:33.0180000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[8105] _id=6acfd342de269131f9d8231d ts=2026-10-14T19:08:49.9650000Z; 17h 33m: 6ab9a9279a8420a1e6b56b7a.jsonl[8133] _id=6acfd371de269131f9d82afd ts=2026-10-14T19:09:36.3530000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[9915] _id=6ad117bade269131f9dedfca ts=2026-10-15T12:43:28.428Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 24m 
  - Evidence: 119h 24m: 6ab9a9279a8420a1e6b56b7a.jsonl[3542] _id=6ac7ebe4de269131f9c67926 ts=2026-10-08T19:15:47.4580000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3680] _id=6ace7b14de269131f9d109f1 ts=2026-10-13T18:40:20.0220000Z; 23h 54m: 6ab9a9279a8420a1e6b56b7a.jsonl[1490] _id=6ac69631de269131f9be963b ts=2026-10-07T18:57:52.8190000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[2093] _id=6ac7e675de269131f9c5a4fb ts=2026-10-08T18:52:36.2480000Z; 21h 20m: 6ab9a9279a8420a1e6b56b7a.jsonl[5124] _id=6ace9c63de269131f9d268ae ts=2026-10-13T21:02:27.5440000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6499] _id=6acfc87cde269131f9d70682 ts=2026-10-14T18:22:52.0070000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.019s..0.033s shown 
  - Evidence: 19ms: 6ab9a9279a8420a1e6b56b7a.jsonl[3529] _id=6ac7ebd3de269131f9c67791 ts=2026-10-08T19:15:30.9680000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3533] _id=6ac7ebd3de269131f9c67795 ts=2026-10-08T19:15:30.9870000Z; 23ms: 6ab9a9279a8420a1e6b56b7a.jsonl[3682] _id=6ace7b21de269131f9d10aa7 ts=2026-10-13T18:40:32.7350000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3686] _id=6ace7b21de269131f9d10aab ts=2026-10-13T18:40:32.7580000Z; 33ms: 6ab9a9279a8420a1e6b56b7a.jsonl[3528] _id=6ac7ebd3de269131f9c67790 ts=2026-10-08T19:15:30.9350000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3529] _id=6ac7ebd3de269131f9c67791 ts=2026-10-08T19:15:30.9680000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21h 13m 
  - Evidence: 21h 13m: 6ab9a9279a8420a1e6b56b7a.jsonl[14117] _id=6ad143fede269131f9e17afb ts=2026-10-15T21:22:06.4080000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[14166] _id=6ad26e96de269131f9e7153f ts=2026-10-16T18:36:06.2430000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 164h 53m 
  - Evidence: 164h 53m: 6ab9a9279a8420a1e6b56b7a.jsonl[1892] _id=6ac69a4fde269131f9bf16d7 ts=2026-10-07T19:15:27.1230000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6191] _id=6acfa90fde269131f9d53be3 ts=2026-10-14T16:08:46.5360000Z; 24h 9m: 6ab9a9279a8420a1e6b56b7a.jsonl[7920] _id=6acfd22bde269131f9d7f9b6 ts=2026-10-14T19:04:10.6560000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12180] _id=6ad125f7de269131f9e02aba ts=2026-10-15T19:13:58.0900000Z; 24h 0m: 6ab9a9279a8420a1e6b56b7a.jsonl[626] _id=6ac54855de269131f9b7790d ts=2026-10-06T19:13:25.6730000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1856] _id=6ac699e7de269131f9bf0d94 ts=2026-10-07T19:13:42.8490000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 164h 51m 
  - Evidence: 164h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[1893] _id=6ac69a4fde269131f9bf16db ts=2026-10-07T19:15:27.1510000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6087] _id=6acfa8aade269131f9d53255 ts=2026-10-14T16:07:06.0570000Z; 24h 8m: 6ab9a9279a8420a1e6b56b7a.jsonl[7924] _id=6acfd22bde269131f9d7f9bf ts=2026-10-14T19:04:10.7230000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12101] _id=6ad12599de269131f9e01d20 ts=2026-10-15T19:12:24.8750000Z; 24h 0m: 6ab9a9279a8420a1e6b56b7a.jsonl[628] _id=6ac54856de269131f9b77913 ts=2026-10-06T19:13:25.7000000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1838] _id=6ac699dcde269131f9bf0c79 ts=2026-10-07T19:13:32.2510000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.033s..0.039s shown 
  - Evidence: 33ms: 6ab9a9279a8420a1e6b56b7a.jsonl[13206] _id=6ad13c00de269131f9e137f9 ts=2026-10-15T20:48:00.1070000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[13209] _id=6ad13c00de269131f9e137fc ts=2026-10-15T20:48:00.1400000Z; 39ms: 6ab9a9279a8420a1e6b56b7a.jsonl[7921] _id=6acfd22bde269131f9d7f9bc ts=2026-10-14T19:04:10.6840000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[7924] _id=6acfd22bde269131f9d7f9bf ts=2026-10-14T19:04:10.7230000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 164h 51m 
  - Evidence: 164h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[1901] _id=6ac69a4ede269131f9bf16bb ts=2026-10-07T19:15:25.6020000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6076] _id=6acfa8a8de269131f9d53229 ts=2026-10-14T16:07:03.4810000Z; 24h 8m: 6ab9a9279a8420a1e6b56b7a.jsonl[7912] _id=6acfd225de269131f9d7f95e ts=2026-10-14T19:04:05.0050000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12104] _id=6ad12597de269131f9e01cdf ts=2026-10-15T19:12:22.5480000Z; 23h 59m: 6ab9a9279a8420a1e6b56b7a.jsonl[622] _id=6ac54853de269131f9b778bd ts=2026-10-06T19:13:23.4430000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1817] _id=6ac6999cde269131f9bf0845 ts=2026-10-07T19:12:27.9750000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 103 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b7a.jsonl[12465] _id=6ad136afde269131f9e12493 ts=2026-10-15T20:25:18.7170000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[12466] _id=6ad136afde269131f9e12494 ts=2026-10-15T20:25:18.7180000Z; 5ms: 6ab9a9279a8420a1e6b56b7a.jsonl[1845] _id=6ac699e3de269131f9bf0d26 ts=2026-10-07T19:13:39.4610000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1843] _id=6ac699e4de269131f9bf0d30 ts=2026-10-07T19:13:39.4660000Z; 6ms: 6ab9a9279a8420a1e6b56b7a.jsonl[13150] _id=6ad13bb8de269131f9e135cb ts=2026-10-15T20:46:47.7660000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[13146] _id=6ad13bb8de269131f9e135cd ts=2026-10-15T20:46:47.7720000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 164h 54m 
  - Evidence: 164h 54m: 6ab9a9279a8420a1e6b56b7a.jsonl[1890] _id=6ac69a41de269131f9bf15ae ts=2026-10-07T19:15:13.3620000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[6271] _id=6acfa954de269131f9d5425d ts=2026-10-14T16:09:56.0070000Z; 24h 1m: 6ab9a9279a8420a1e6b56b7a.jsonl[541] _id=6ac54818de269131f9b7717b ts=2026-10-06T19:12:24.0050000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1836] _id=6ac699dade269131f9bf0c4c ts=2026-10-07T19:13:29.9750000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 170h 13m 
  - Evidence: 170h 13m: 6ab9a9279a8420a1e6b56b7a.jsonl[2705] _id=6ac7e79ade269131f9c5cf00 ts=2026-10-08T18:57:29.9610000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[13693] _id=6ad1414ade269131f9e1677c ts=2026-10-15T21:10:34.5410000Z; 24h 2m: 6ab9a9279a8420a1e6b56b7a.jsonl[1217] _id=6ac69566de269131f9be652d ts=2026-10-07T18:54:29.6290000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[2703] _id=6ac7e782de269131f9c5cadf ts=2026-10-08T18:57:05.2600000Z; 21h 24m: 6ab9a9279a8420a1e6b56b7a.jsonl[13693] _id=6ad1414ade269131f9e1677c ts=2026-10-15T21:10:34.5410000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[14140] _id=6ad26e71de269131f9e712e7 ts=2026-10-16T18:35:29.6310000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a9279a8420a1e6b56b7a.jsonl[1988] _id=6ac7e584de269131f9c58972 ts=2026-10-08T18:48:35.6430000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3615] _id=6ace7a73de269131f9d0fd81 ts=2026-10-13T18:37:39.0070000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7a.jsonl[1] _id=6ac540bbde269131f9b6b5d5 ts=2026-10-06T18:40:59.3240000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[731] _id=6ac6931ade269131f9bdf938 ts=2026-10-07T18:44:40.4040000Z; 23h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[1414] _id=6ac695fbde269131f9be8840 ts=2026-10-07T18:56:58.5970000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1988] _id=6ac7e584de269131f9c58972 ts=2026-10-08T18:48:35.6430000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a9279a8420a1e6b56b7a.jsonl[1987] _id=6ac7e584de269131f9c58971 ts=2026-10-08T18:48:35.6420000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3614] _id=6ace7a73de269131f9d0fd80 ts=2026-10-13T18:37:39.0070000Z; 24h 3m: 6ab9a9279a8420a1e6b56b7a.jsonl[0] _id=6ac540bbde269131f9b6b5d1 ts=2026-10-06T18:40:59.3230000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[730] _id=6ac6931ade269131f9bdf937 ts=2026-10-07T18:44:40.4040000Z; 23h 50m: 6ab9a9279a8420a1e6b56b7a.jsonl[1497] _id=6ac69636de269131f9be977d ts=2026-10-07T18:57:57.7760000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1987] _id=6ac7e584de269131f9c58971 ts=2026-10-08T18:48:35.6420000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 144h 9m 
  - Evidence: 144h 9m: 6ab9a9279a8420a1e6b56b7a.jsonl[1495] _id=6ac69634de269131f9be9714 ts=2026-10-07T18:57:55.4000000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[4190] _id=6ace815ade269131f9d15f88 ts=2026-10-13T19:07:05.7500000Z; 19h 2m: 6ab9a9279a8420a1e6b56b7a.jsonl[4192] _id=6ace815dde269131f9d15ff5 ts=2026-10-13T19:07:08.5710000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[5494] _id=6acf8d2dde269131f9d3f512 ts=2026-10-14T14:09:48.2500000Z; 13h 51m: 6ab9a9279a8420a1e6b56b7a.jsonl[9814] _id=6ad006c6de269131f9d99bdf ts=2026-10-14T22:48:37.9980000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[9841] _id=6ad0c9b9de269131f9da4cf2 ts=2026-10-15T12:40:24.6380000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9279a8420a1e6b56b7a.jsonl[3521] _id=6ac7ebc0de269131f9c675a1 ts=2026-10-08T19:15:11.6080000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[3618] _id=6ace7a83de269131f9d0ff38 ts=2026-10-13T18:37:54.7050000Z; 23h 43m: 6ab9a9279a8420a1e6b56b7a.jsonl[703] _id=6ac548f7de269131f9b78feb ts=2026-10-06T19:16:06.7820000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1578] _id=6ac69693de269131f9beace7 ts=2026-10-07T18:59:31.3750000Z; 23h 32m: 6ab9a9279a8420a1e6b56b7a.jsonl[1968] _id=6ac69acfde269131f9bf20c4 ts=2026-10-07T19:17:35.1770000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[2022] _id=6ac7e5e3de269131f9c59141 ts=2026-10-08T18:50:11.0440000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b7a.jsonl[14362] _id=6ad270ebde269131f9e74b1c ts=2026-10-16T18:46:02.5570000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[14363] _id=6ad270ebde269131f9e74b1d ts=2026-10-16T18:46:02.5580000Z; 1ms: 6ab9a9279a8420a1e6b56b7a.jsonl[1799] _id=6ac6996fde269131f9bf0482 ts=2026-10-07T19:11:42.5460000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[1800] _id=6ac6996fde269131f9bf0483 ts=2026-10-07T19:11:42.5470000Z; 3ms: 6ab9a9279a8420a1e6b56b7a.jsonl[389] _id=6ac5470ede269131f9b75e81 ts=2026-10-06T19:07:57.5760000Z -> 6ab9a9279a8420a1e6b56b7a.jsonl[393] _id=6ac5470ede269131f9b75e8b ts=2026-10-06T19:07:57.5790000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[375] _id=6ac546e8de269131f9b758a7 ts=2026-10-06T19:07:20.0450000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[571] _id=6ac5487bde269131f9b77cf7 ts=2026-10-06T19:14:02.9930000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[1788] _id=6ac6995dde269131f9bf0337 ts=2026-10-07T19:11:25.2500000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[10664] _id=6ad11c5fde269131f9deebe6 ts=2026-10-15T18:18:46.212Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[7924] _id=6acfd22bde269131f9d7f9bf ts=2026-10-14T19:04:10.7230000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[433] _id=6ac54775de269131f9b76661 ts=2026-10-06T19:09:40.5610000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[372] _id=6ac547ddde269131f9b76d77 ts=2026-10-06T19:11:25.5300000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[565] _id=6ac54840de269131f9b775de ts=2026-10-06T19:13:03.9060000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[13693] _id=6ad1414ade269131f9e1677c ts=2026-10-15T21:10:34.5410000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[14140] _id=6ad26e71de269131f9e712e7 ts=2026-10-16T18:35:29.6310000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[14500] _id=6ad27296de269131f9e76c30 ts=2026-10-16T18:53:10.3490000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[1578] _id=6ac69693de269131f9beace7 ts=2026-10-07T18:59:31.3750000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[14365] _id=6ad270eade269131f9e74b19 ts=2026-10-16T18:46:02.5160000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[14361] _id=6ad270ebde269131f9e74b1b ts=2026-10-16T18:46:02.5390000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[4871] _id=6ace993dde269131f9d25d7e ts=2026-10-13T20:49:00.9050000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[7157] _id=6acfcdd2de269131f9d77c61 ts=2026-10-14T18:45:37.8380000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[7235] _id=6acfce40de269131f9d78c12 ts=2026-10-14T18:47:27.3520000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 29 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[4494] _id=6ace983dde269131f9d259e9 ts=2026-10-13T20:44:42.8040000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4524] _id=6ace983dde269131f9d259ee ts=2026-10-13T20:44:42.9460000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4517] _id=6ace983ede269131f9d259f2 ts=2026-10-13T20:44:43.0230000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 155 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[4171] _id=6ace814cde269131f9d15c96 ts=2026-10-13T19:06:50.8050000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4172] _id=6ace814cde269131f9d15cb9 ts=2026-10-13T19:06:50.8050000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[4174] _id=6ace814cde269131f9d15cd1 ts=2026-10-13T19:06:50.8050000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[12346] _id=6ad136b2de269131f9e1249d ts=2026-10-15T20:25:22.0350000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[462] _id=6ac547d3de269131f9b76caf ts=2026-10-06T19:11:15.0690000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[463] _id=6ac547d5de269131f9b76cd3 ts=2026-10-06T19:11:17.3270000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[539] _id=6ac54814de269131f9b77145 ts=2026-10-06T19:12:20.0980000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 12 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 497 start, 487 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 19 unmatched 'BecameVisible' (totals: 745 open, 726 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 9 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 53 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 243 of 14591 adjacent _id pairs reverse in client time; worst 94.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b7a.jsonl[2109] _id=6ac7e6b8de269131f9c5ac8a ts=2026-10-08T18:53:43.5200000Z`; `6ab9a9279a8420a1e6b56b7a.jsonl[2127] _id=6ac7e6b9de269131f9c5ac9c ts=2026-10-08T18:52:08.9120000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.82s, min -55383.43s, max -0.11s over 14592 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)

## 9. Event-Type Details

### `InputEvent` — 4308 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1136); Unit 2 Prod (Refactor) (1003); Unit 1 Dev (796); Unit 4 Dev (431); Unit 3 Dungeon Dev (357); Unit 5 Dev - Dungeon (279); Unit 4 Dev - Dungeon (243); Unit 4 Dev - Anderson Base (40); Unit 5 Dev (23)
- **Intervals:** median 1.10s (p5 0.11s / p95 20.61s, n=4307)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4308/4308 records)
    "pressed"  x4308
data.actionType  (string, 4308/4308 records)
    "Move"  x2564
    "Interact"  x746
    "Jump"  x537
    "Sprint"  x165
    "Hoverboard"  x150
    "Ascend"  x128
    "Map"  x13
    "Pause"  x5
data.key  (string, 4308/4308 records, 17 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4308/4308 records)
    "Player"  x3216
    "Drone"  x1092
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2826 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (837); Unit 3 Dev (550); Unit 1 Dev (390); Unit 4 Dev (342); Unit 4 Dev - Anderson Base (217); Unit 5 Dev - Dungeon (168); Unit 3 Dungeon Dev (157); Unit 4 Dev - Dungeon (130); Unit 5 Dev (35)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.14s, n=2812)
- **Fields under `data`:**

```text
data.position  (object, 2826/2826 records)
data.position.x  (number, 2826/2826 records)
    numeric range -702.515 .. 1660.65 (869 unique)
data.position.y  (number, 2826/2826 records)
    numeric range -113.43 .. 222.123 (617 unique)
data.position.z  (number, 2826/2826 records)
    numeric range -1256.52 .. 2221.6 (868 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 2630 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1326); Unit 4 Dev (838); Unit 3 Dungeon Dev (292); Unit 5 Dev - Dungeon (174)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.71s, n=2629)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2630/2630 records)
    "BecameVisible"  x745
    "BecameInvisible"  x726
    "BecameCameraUncentered"  x580
    "BecameCameraCentered"  x579
data.pieceId  (string, 2630/2630 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2630/2630 records)
    1786 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2608 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (807); Unit 3 Dev (408); Unit 1 Dev (387); Unit 4 Dev (320); Unit 4 Dev - Anderson Base (269); Unit 3 Dungeon Dev (191); Unit 4 Dev - Dungeon (101); Unit 5 Dev - Dungeon (96); Unit 5 Dev (29)
- **eventKey:** present on 1624 of 2608 records
- **Intervals:** median 3.99s (p5 0.00s / p95 35.83s, n=2607)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1624; [conversationId, dialogueEventType] x984
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2608/2608 records)
    numeric range 8 .. 116 (51 unique)
data.dialogueEventType  (string, 2608/2608 records)
    "DialogueNodeEvent"  x1624
    "DialogueStartEvent"  x497
    "DialogueFinishEvent"  x487
data.nodeId  (number, 1624/2608 records)
    numeric range 0 .. 290 (231 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 1087 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (653); Unit 1 Dev (204); Unit 2 Prod (Refactor) (147); Unit 3 Dev (83)
- **Intervals:** median 0.33s (p5 0.03s / p95 10.93s, n=1086)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1087/1087 records)
    "argumentationNodeHoverEnd"  x416
    "argumentationNodeHoverStart"  x413
    "argumentationNodeAdd"  x141
    "argumentationNodeRemove"  x117
data.argumentationTitle  (string, 1087/1087 records)
    "Unit 4 - Flooding"  x653
    "Unit 1 - Freshwater"  x168
    "Unit 2 – Watershed"  x147
    "Unit 3 - Pollution Upstream"  x83
    "Unit 1 - Argumentation Tutorial"  x36
data.nodeName  (string, 1087/1087 records)
    "A"  x239
    "C"  x157
    "B"  x156
    "1"  x129
    "I"  x101
    "D"  x85
    "2"  x62
    "3"  x56
    "II"  x53
    "4"  x46
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 403 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (120); Unit 4 Dev - Dungeon (77); Unit 2 Prod (Refactor) (65); Unit 3 Dungeon Dev (57); Unit 4 Dev (38); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (14); Unit 5 Dev - Dungeon (11); Unit 5 Dev (3)
- **Intervals:** median 8.61s (p5 0.16s / p95 467.29s, n=402)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 403/403 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 403/403 records)
    101 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 180 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (118); Unit 4 Dev (40); Unit 3 Dev (22)
- **Intervals:** median 0.98s (p5 0.16s / p95 14.57s, n=179)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x166; [Soil Key Puzzle Status, Unit] x14
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 14/180 records)
    "Finished"  x7
    "Started"  x7
data.Unit  (string, 14/180 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 4 Dev"  x6
    "Unit 3 Dev"  x2
data.actionType  (string, 166/180 records)
    "RightDrag"  x88
    "LeftDrag"  x78
data.currentSoilType  (string, 166/180 records)
    "CLAYSAND"  x37
    "SAND"  x34
    "CLAY"  x33
    "CLAYROCK"  x24
    "SANDGRAVEL"  x22
    "BEDROCK"  x8
    "GRAVEL"  x8
data.isCorrectSelection  (string, 166/180 records)
    "false"  x124
    "true"  x42
data.waterLevelStatus  (string, 166/180 records)
    "Proper"  x84
    "TooHigh"  x52
    "TooLow"  x30
data.waterRetentionChange  (string, 166/180 records)
    "Increase"  x80
    "Decrease"  x44
    "NoChange"  x42
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 118 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (72); Unit 2 Prod (Refactor) (37); Unit 1 Dev (9)
- **Intervals:** median 4.92s (p5 0.82s / p95 1277.20s, n=117)
- **`data` key-set variants:** [actionType, featureUsed] x64; [actionType, featureUsed, location] x46; [actionType, featureUsed, legendName] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 118/118 records)
    "WaypointMoveEvent"  x37
    "MapCloseEvent"  x32
    "MapOpenEvent"  x32
    "WaypointSetEvent"  x7
    "Selected"  x5
    "Unselected"  x3
    "WaypointResetEvent"  x2
data.featureUsed  (string, 118/118 records)
    "Map"  x64
    "Waypoint"  x46
    "Legend"  x8
data.legendName  (string, 8/118 records)
    "Water"  x5
    "Teleporter Room"  x2
    "90 ft"  x1
data.location  (object, 46/118 records)
data.location.x  (number, 46/118 records)
    numeric range -347.529 .. 632.388 (41 unique)
data.location.y  (number, 46/118 records)
    numeric range -368.777 .. 263.881 (44 unique)
data.location.z  (number, 46/118 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 90 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (21); Unit 2 Prod (Refactor) (20); Unit 5 Dev - Dungeon (12); Unit 3 Dev (11); Unit 4 Dev (10); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (1)
- **eventKey:** present on 90 of 90 records
- **Intervals:** median 229.58s (p5 0.01s / p95 54011.08s, n=89)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 90/90 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x37
data.questID  (string, 90/90 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 90/90 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/90 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 60 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (60)
- **Intervals:** median 8.20s (p5 1.47s / p95 92.73s, n=59)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "On"  x35
    "Off"  x25
data.floor  (string, 60/60 records)
    "3"  x29
    "4"  x24
    "2"  x4
    "1"  x3
data.machineNumber  (string, 60/60 records)
    "One"  x58
    "Two"  x2
data.machineType  (string, 60/60 records)
    "Condenser"  x29
    "Evaporator"  x13
    "DualChamber_Evaporator"  x9
    "DualChamber_Condenser"  x6
    "VentSwitch"  x3
data.room  (string, 60/60 records)
    "2"  x24
    "3"  x22
    "1"  x8
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 55 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (35); Unit 3 Dev (10); Unit 2 Prod (Refactor) (6); Unit 1 Dev (4)
- **Intervals:** median 18.87s (p5 1.94s / p95 36973.12s, n=54)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "submitAnswerEvent"  x55
data.answerSubmitted  (string, 55/55 records)
    32 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 55/55 records)
    "Unit 4 - Flooding"  x35
    "Unit 3 - Pollution Upstream"  x10
    "Unit 2 – Watershed"  x6
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 53 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (22); Unit 2 Prod (Refactor) (6); Unit 3 Dev (6); Unit 4 Dev (6); Unit 1 Dev (5); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 277.52s (p5 8.37s / p95 81042.30s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "DebugMenuStateChanged"  x53
data.isOpened  (bool, 53/53 records)
    false  x53
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 31 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (23); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1674.93s (p5 56.79s / p95 86268.63s, n=30)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 31/31 records)
    true  x31
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 23 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (12); Unit 2 Prod (Refactor) (7); Unit 1 Dev (4)
- **Intervals:** median 3.56s (p5 1.00s / p95 86172.68s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "Open"  x12
    "Close"  x11
data.toolName  (string, 23/23 records, 23 empty-string)
    ""  x23
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 6331.97s (p5 157.62s / p95 86584.88s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 21 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (21)
- **Intervals:** median 2.85s (p5 0.65s / p95 27.39s, n=20)
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records, 8 empty-string)
    "cameraPlaced"  x13
    ""  x8
data.boxId  (string, 21/21 records)
    "0"  x9
    "1"  x7
    "2"  x5
data.soilType  (string, 21/21 records)
    "Sand"  x10
    "Clay"  x7
    "Gravel"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 156.42s (p5 0.04s / p95 213545.34s, n=16)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 17/17 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 7.90s (p5 0.38s / p95 122.58s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x9
    "Gravel"  x4
    "Sand"  x3
data.floor  (string, 16/16 records)
    "4"  x11
    "5"  x4
    "3"  x1
data.machine  (string, 16/16 records)
    "1"  x14
    "2"  x2
data.row  (string, 16/16 records)
    "TopRow"  x15
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 15 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (14); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 2.25s (p5 0.07s / p95 263991.81s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x6
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Freshwater"  x10
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 2 – Watershed"  x1
data.toolName  (string, 15/15 records)
    "BackingInfoPanel - "  x10
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (3); Unit 4 Dev (3); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 12629.67s (p5 1.67s / p95 293755.01s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 11 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 1 Dev (2); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 8.57s (p5 1.17s / p95 375981.55s, n=10)
- **`data` key-set variants:** [actionType, chatID] x9; [actionKey, chatID] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/11 records)
    "ScrollStop"  x2
data.actionType  (string, 9/11 records)
    "Close"  x5
    "Open"  x2
    "ScrollStart"  x2
data.chatID  (string, 11/11 records)
    "NA"  x7
    "[16-3, 18-1, 18-2, 18-4, 18-5]"  x1
    "[18-271, 18-273, 18-179, 68-1, 68-5]"  x1
    "[18-7, 18-9, 18-10, 17-17, 17-19, 17-20, 17-22]"  x1
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 83524.02s (p5 32034.57s / p95 517768.47s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x2
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (118 records)
- `TerasGardenBox` data.actionType: "" (8x)
- `TopographicMapEvent` data.actionType: "Selected" (5x); "Unselected" (3x); "WaypointMoveEvent" (37x); "WaypointResetEvent" (2x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (8x); "Waypoint" (46x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (117x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*