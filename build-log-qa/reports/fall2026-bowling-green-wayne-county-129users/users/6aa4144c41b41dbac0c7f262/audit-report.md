# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f262

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4144c41b41dbac0c7f262
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f262.jsonl
- **Records:** 17920 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f262
- **Time span:** 2026-09-23T18:16:11.826000+00:00 .. 2026-10-06T20:26:29.913000+00:00 (314h 10m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f262\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 17920 records, 10 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 110 INFO, 0 NOT_TESTED, 94 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 6207 | 34.64 | 1 | 4 | 0 | 2026-09-24T17:59:37.552000+00:00 | 2026-10-06T18:45:27.090000+00:00 | 288h 45m |
| InputEvent | 5417 | 30.23 | 1 | 9 | 0 | 2026-09-23T18:16:28.282000+00:00 | 2026-10-06T20:26:29.913000+00:00 | 314h 10m |
| PlayerPositionEvent | 2374 | 13.25 | 1 | 9 | 0 | 2026-09-23T18:16:23.009000+00:00 | 2026-10-06T20:26:24.606000+00:00 | 314h 10m |
| DialogueEvent | 2140 | 11.94 | 1 | 9 | 1272 | 2026-09-23T18:16:45.020000+00:00 | 2026-10-06T20:26:18.293000+00:00 | 314h 9m |
| argumentationNodeEvent | 639 | 3.57 | 1 | 4 | 0 | 2026-09-24T17:45:06.165000+00:00 | 2026-10-06T20:08:55.399000+00:00 | 290h 23m |
| ObjectInterEvent | 488 | 2.72 | 1 | 9 | 0 | 2026-09-23T18:23:07.823000+00:00 | 2026-10-06T20:26:29.913000+00:00 | 314h 3m |
| soilMachine | 159 | 0.89 | 1 | 1 | 0 | 2026-10-05T18:14:25.811000+00:00 | 2026-10-05T18:39:57.631000+00:00 | 25m 31s |
| Soil Key Puzzle | 116 | 0.65 | 1 | 3 | 0 | 2026-09-24T18:11:30.776000+00:00 | 2026-10-05T14:45:29.042000+00:00 | 260h 33m |
| questEvent | 92 | 0.51 | 1 | 9 | 92 | 2026-09-23T18:16:44.995000+00:00 | 2026-10-06T20:21:57.057000+00:00 | 314h 5m |
| TopographicMapEvent | 47 | 0.26 | 1 | 3 | 0 | 2026-09-24T17:54:13.598000+00:00 | 2026-10-05T14:43:14.177000+00:00 | 260h 49m |
| gameWindowFocusEvent | 37 | 0.21 | 1 | 6 | 0 | 2026-09-23T18:16:11.826000+00:00 | 2026-10-06T20:15:11.249000+00:00 | 313h 58m |
| argumentationAnswerEvent | 36 | 0.2 | 1 | 4 | 0 | 2026-09-24T17:46:32.119000+00:00 | 2026-10-06T20:08:56.782000+00:00 | 290h 22m |
| WaterChamberEvent | 33 | 0.18 | 1 | 1 | 0 | 2026-10-06T18:36:58.676000+00:00 | 2026-10-06T18:45:34.205000+00:00 | 8m 35s |
| DEBUGMenu | 29 | 0.16 | 1 | 9 | 0 | 2026-09-23T18:16:23.001000+00:00 | 2026-10-06T19:45:40.050000+00:00 | 313h 29m |
| SolarStillDesignEvent | 29 | 0.16 | 1 | 1 | 0 | 2026-10-06T20:15:36.718000+00:00 | 2026-10-06T20:17:42.300000+00:00 | 2m 5s |
| gameWindowUnfocusEvent | 26 | 0.15 | 1 | 6 | 0 | 2026-09-23T18:46:09.306000+00:00 | 2026-10-06T20:14:57.330000+00:00 | 313h 28m |
| gameStartEvent | 23 | 0.13 | 1 | 1 | 0 | 2026-09-23T18:16:11.827000+00:00 | 2026-10-06T19:45:40.136000+00:00 | 313h 29m |
| argumentationEvent | 12 | 0.07 | 1 | 4 | 0 | 2026-09-24T17:46:02.815000+00:00 | 2026-10-06T20:08:56.799000+00:00 | 290h 22m |
| TerasGardenBox | 4 | 0.02 | 1 | 1 | 0 | 2026-10-06T18:27:05.963000+00:00 | 2026-10-06T18:28:04.596000+00:00 | 58.6s |
| argumentationToolEvent | 4 | 0.02 | 1 | 2 | 0 | 2026-09-24T17:45:51.075000+00:00 | 2026-09-29T18:43:00.357000+00:00 | 120h 57m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-24T17:52:08.090000+00:00 | 2026-10-06T20:26:29.907000+00:00 | 290h 34m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-06T18:32:47.654000+00:00 | 2026-10-06T19:45:47.597000+00:00 | 1h 12m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 523030.909s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 19.231s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 6.105s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.54s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 3.0s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 123.968s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2189.971s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6471.965s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 919.204s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1468.236s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 0.488s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.1x vs baseline. 
  - Observed: 116 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 7.2x vs baseline. 
  - Observed: 29 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 240 ft; 30 ft; 330 ft; 60 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.2x vs baseline. 
  - Observed: 36 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,II; A,3,I; A,C,2,II; B,2,II; B,A,C,2,II; C,2,II; C,A,2,II; D,2,II; D,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.6x vs baseline. 
  - Observed: 639 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54; 56 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 31.8x vs baseline. 
  - Observed: 159 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 28 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[166] _id=6ab4199b485cab4c954f48ea ts=2026-09-23T18:25:31.6310000Z`; `6aa4144c41b41dbac0c7f262.jsonl[227] _id=6ab41acc485cab4c954f5256 ts=2026-09-23T18:30:36.1290000Z`; `6aa4144c41b41dbac0c7f262.jsonl[287] _id=6ab41bde485cab4c954f5a59 ts=2026-09-23T18:35:10.1840000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:40' vs expected 'questActiveEvent:39' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[14590] _id=6ac40ce9de269131f9afa08d ts=2026-10-05T20:47:37.9610000Z`; `6aa4144c41b41dbac0c7f262.jsonl[16212] _id=6ac53ea2de269131f9b67899 ts=2026-10-06T18:32:01.9460000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[16] _id=6ab4176b485cab4c954f376e ts=2026-09-23T18:16:11.8270000Z`; `6aa4144c41b41dbac0c7f262.jsonl[419] _id=6ab560ee485cab4c95537b8f ts=2026-09-24T17:42:06.0840000Z`; `6aa4144c41b41dbac0c7f262.jsonl[795] _id=6ab563a4485cab4c9553b528 ts=2026-09-24T17:53:39.9340000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 37 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 37} 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[15] _id=6ab4176b485cab4c954f376c ts=2026-09-23T18:16:11.8260000Z`; `6aa4144c41b41dbac0c7f262.jsonl[414] _id=6ab41e71485cab4c954f70dd ts=2026-09-23T18:46:09.3170000Z`; `6aa4144c41b41dbac0c7f262.jsonl[420] _id=6ab560ee485cab4c95537b89 ts=2026-09-24T17:42:06.0830000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[415] _id=6ab41e71485cab4c954f70d9 ts=2026-09-23T18:46:09.3060000Z`; `6aa4144c41b41dbac0c7f262.jsonl[3458] _id=6ab56806485cab4c9554227a ts=2026-09-24T18:12:22.3310000Z`; `6aa4144c41b41dbac0c7f262.jsonl[3576] _id=6ab6ba74485cab4c955de157 ts=2026-09-25T18:16:20.7230000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 15 of 47 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[808] _id=6ab563c5485cab4c9553b7c8 ts=2026-09-24T17:54:13.5980000Z`; `6aa4144c41b41dbac0c7f262.jsonl[807] _id=6ab563c5485cab4c9553b7ce ts=2026-09-24T17:54:13.7240000Z`; `6aa4144c41b41dbac0c7f262.jsonl[934] _id=6ab56557485cab4c9553df49 ts=2026-09-24T18:00:54.8650000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 6206 | 0.0 | 0.03 | 167.507 | 1.016 | 352506.921 | 0.36 | 3834 | 10 |
| InputEvent | 5416 | 0.0 | 0.736 | 208.826 | 10.233 | 352289.637 | 0.29 | 167 | 15 |
| PlayerPositionEvent | 2362 | 1.574 | 10.0 | 478.721 | 10.029 | 352273.859 | 0.13 | 0 | 12 |
| DialogueEvent | 2139 | 0.0 | 4.166 | 528.739 | 46.656 | 352335.884 | 0.11 | 653 | 14 |
| argumentationNodeEvent | 638 | 0.001 | 0.373 | 1638.604 | 5.663 | 603146.256 | 0.04 | 139 | 3 |
| ObjectInterEvent | 487 | 0.001 | 4.811 | 2321.565 | 348.584 | 352514.545 | 0.03 | 3 | 16 |
| soilMachine | 158 | 0.125 | 0.488 | 9.695 | 35.491 | 250.19 | 6.19 | 0 | 0 |
| Soil Key Puzzle | 115 | 0.118 | 0.659 | 8156.854 | 12.325 | 352497.214 | 0.01 | 0 | 5 |
| questEvent | 91 | 0.0 | 219.21 | 12425.407 | 79539.277 | 352505.555 | 0.0 | 16 | 22 |
| TopographicMapEvent | 46 | 0.095 | 6.105 | 20411.752 | 86969.046 | 418893.835 | 0.0 | 0 | 6 |
| gameWindowFocusEvent | 36 | 2.091 | 919.204 | 31398.317 | 129804.405 | 352505.545 | 0.0 | 0 | 20 |
| argumentationAnswerEvent | 35 | 0.233 | 3.0 | 29866.99 | 135078.159 | 603289.695 | 0.0 | 0 | 3 |
| WaterChamberEvent | 32 | 0.478 | 5.54 | 16.11 | 50.726 | 80.707 | 3.72 | 0 | 0 |
| DEBUGMenu | 28 | 46.571 | 1219.641 | 40305.609 | 197966.016 | 352505.89 | 0.0 | 0 | 21 |
| SolarStillDesignEvent | 28 | 0.002 | 2.607 | 4.485 | 13.985 | 21.702 | 13.38 | 2 | 0 |
| gameWindowUnfocusEvent | 25 | 0.0 | 1468.236 | 45141.121 | 224039.174 | 367187.864 | 0.0 | 1 | 16 |
| gameStartEvent | 22 | 46.208 | 6471.965 | 51298.559 | 248995.771 | 352505.545 | 0.0 | 0 | 17 |
| argumentationEvent | 11 | 0.021 | 94.168 | 95033.999 | 519171.975 | 603146.482 | 0.0 | 2 | 3 |
| TerasGardenBox | 3 | 4.815 | 19.231 | 19.544 | 33.051 | 34.587 | 3.07 | 0 | 0 |
| argumentationToolEvent | 3 | 11.712 | 123.968 | 145143.094 | 391776.639 | 435293.602 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 520750.239 | 523030.909 | 523030.909 | 525083.511 | 525311.578 | 0.0 | 0 | 2 |
| chatEvent | 2 | 806.789 | 2189.971 | 2189.972 | 3434.836 | 3573.154 | 0.03 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[11317] _id=6ac3b732de269131f9ac5d10 ts=2026-10-05T14:41:53.9450000Z == 6aa4144c41b41dbac0c7f262.jsonl[11311] _id=6ac3b732de269131f9ac5d14 ts=2026-10-05T14:41:53.9450000Z`; `6aa4144c41b41dbac0c7f262.jsonl[13363] _id=6ac3ebdfde269131f9aefdf9 ts=2026-10-05T18:26:39.1960000Z == 6aa4144c41b41dbac0c7f262.jsonl[13355] _id=6ac3ebdfde269131f9aefdfd ts=2026-10-05T18:26:39.1960000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 238 group(s), 336 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[970] _id=6ab5652a485cab4c9553d665 ts=2026-09-24T17:59:59.3250000Z == 6aa4144c41b41dbac0c7f262.jsonl[932] _id=6ab5652a485cab4c9553d66f ts=2026-09-24T17:59:59.3250000Z`; `6aa4144c41b41dbac0c7f262.jsonl[924] _id=6ab5652a485cab4c9553d678 ts=2026-09-24T17:59:59.3410000Z == 6aa4144c41b41dbac0c7f262.jsonl[971] _id=6ab5652a485cab4c9553d67d ts=2026-09-24T17:59:59.3410000Z`; `6aa4144c41b41dbac0c7f262.jsonl[935] _id=6ab5652b485cab4c9553d69c ts=2026-09-24T17:59:59.4800000Z == 6aa4144c41b41dbac0c7f262.jsonl[954] _id=6ab5652b485cab4c9553d6a0 ts=2026-09-24T17:59:59.4800000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[17564] _id=6ac555a6de269131f9b84ff9 ts=2026-10-06T20:10:14.6070000Z == 6aa4144c41b41dbac0c7f262.jsonl[17565] _id=6ac555a6de269131f9b84ffa ts=2026-10-06T20:10:14.6070000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 115 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4144c41b41dbac0c7f262.jsonl[113] _id=6ab4190b485cab4c954f4332 ts=2026-09-23T18:23:07.8230000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[117] _id=6ab4190b485cab4c954f4334 ts=2026-09-23T18:23:07.8290000Z`; `769ms: 6aa4144c41b41dbac0c7f262.jsonl[9054] _id=6abd0092485cab4c95865347 ts=2026-09-30T12:29:07.0720000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[9056] _id=6abd0092485cab4c95865353 ts=2026-09-30T12:29:07.8410000Z`; `955ms: 6aa4144c41b41dbac0c7f262.jsonl[9056] _id=6abd0092485cab4c95865353 ts=2026-09-30T12:29:07.8410000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[9068] _id=6abd0093485cab4c95865357 ts=2026-09-30T12:29:08.7960000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 890 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6aa4144c41b41dbac0c7f262.jsonl[938] _id=6ab56526485cab4c9553d5b9 ts=2026-09-24T17:59:58.5810000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[940] _id=6ab56527485cab4c9553d5ca ts=2026-09-24T17:59:58.5910000Z`; `16ms: 6aa4144c41b41dbac0c7f262.jsonl[940] _id=6ab56527485cab4c9553d5ca ts=2026-09-24T17:59:58.5910000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[922] _id=6ab56527485cab4c9553d5df ts=2026-09-24T17:59:58.6070000Z`; `34ms: 6aa4144c41b41dbac0c7f262.jsonl[923] _id=6ab56528485cab4c9553d5f2 ts=2026-09-24T17:59:58.6150000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[951] _id=6ab56529485cab4c9553d606 ts=2026-09-24T17:59:58.6490000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `646ms: 6aa4144c41b41dbac0c7f262.jsonl[5219] _id=6abaaf02485cab4c956fb4e7 ts=2026-09-28T18:16:34.4400000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[5227] _id=6abaaf03485cab4c956fb508 ts=2026-09-28T18:16:35.0860000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `900ms: 6aa4144c41b41dbac0c7f262.jsonl[1026] _id=6ab5656d485cab4c9553e2d6 ts=2026-09-24T18:01:17.7790000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[1024] _id=6ab5656e485cab4c9553e2fc ts=2026-09-24T18:01:18.6790000Z`; `383ms: 6aa4144c41b41dbac0c7f262.jsonl[3558] _id=6ab6b9ff485cab4c955dd1e3 ts=2026-09-25T18:14:23.9680000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[3552] _id=6ab6ba00485cab4c955dd1e7 ts=2026-09-25T18:14:24.3510000Z`; `203ms: 6aa4144c41b41dbac0c7f262.jsonl[3552] _id=6ab6ba00485cab4c955dd1e7 ts=2026-09-25T18:14:24.3510000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[3555] _id=6ab6ba00485cab4c955dd1e9 ts=2026-09-25T18:14:24.5540000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `385ms: 6aa4144c41b41dbac0c7f262.jsonl[15871] _id=6ac53b9cde269131f9b6459d ts=2026-10-06T18:19:08.4190000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[15862] _id=6ac53b9cde269131f9b645a1 ts=2026-10-06T18:19:08.8040000Z`; `483ms: 6aa4144c41b41dbac0c7f262.jsonl[15862] _id=6ac53b9cde269131f9b645a1 ts=2026-10-06T18:19:08.8040000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[15872] _id=6ac53b9dde269131f9b645ab ts=2026-10-06T18:19:09.2870000Z`; `389ms: 6aa4144c41b41dbac0c7f262.jsonl[15872] _id=6ac53b9dde269131f9b645ab ts=2026-10-06T18:19:09.2870000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[15867] _id=6ac53b9dde269131f9b645af ts=2026-10-06T18:19:09.6760000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6aa4144c41b41dbac0c7f262.jsonl[8617] _id=6abc06d0485cab4c9584b67b ts=2026-09-29T18:43:28.0170000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[8621] _id=6abc06d0485cab4c9584b681 ts=2026-09-29T18:43:28.0510000Z`; `21ms: 6aa4144c41b41dbac0c7f262.jsonl[16007] _id=6ac53c31de269131f9b64f39 ts=2026-10-06T18:21:37.8520000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[16003] _id=6ac53c32de269131f9b64f45 ts=2026-10-06T18:21:37.8730000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 124 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `704ms: 6aa4144c41b41dbac0c7f262.jsonl[508] _id=6ab561b1485cab4c95538c61 ts=2026-09-24T17:45:21.1920000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[514] _id=6ab561b2485cab4c95538c71 ts=2026-09-24T17:45:21.8960000Z`; `703ms: 6aa4144c41b41dbac0c7f262.jsonl[509] _id=6ab561b1485cab4c95538c63 ts=2026-09-24T17:45:21.2600000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[502] _id=6ab561b2485cab4c95538c76 ts=2026-09-24T17:45:21.9630000Z`; `284ms: 6aa4144c41b41dbac0c7f262.jsonl[499] _id=6ab561b2485cab4c95538c7b ts=2026-09-24T17:45:22.1260000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[500] _id=6ab561b2485cab4c95538c85 ts=2026-09-24T17:45:22.4100000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4144c41b41dbac0c7f262.jsonl[3576] _id=6ab6ba74485cab4c955de157 ts=2026-09-25T18:16:20.7230000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[3578] _id=6ab6ba89485cab4c955de4b3 ts=2026-09-25T18:16:20.723Z`; `363ms: 6aa4144c41b41dbac0c7f262.jsonl[9339] _id=6abd0189485cab4c958657ef ts=2026-09-30T12:33:13.9300000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[9340] _id=6abd018b485cab4c958657fd ts=2026-09-30T12:33:14.2930000Z`; `547ms: 6aa4144c41b41dbac0c7f262.jsonl[17645] _id=6ac556c0de269131f9b85f1c ts=2026-10-06T20:14:56.7830000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[17647] _id=6ac556c1de269131f9b85f22 ts=2026-10-06T20:14:57.3300000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4144c41b41dbac0c7f262.jsonl[14590] _id=6ac40ce9de269131f9afa08d ts=2026-10-05T20:47:37.9610000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[14609] _id=6ac40ce9de269131f9afa08f ts=2026-10-05T20:47:37.9630000Z`; `4ms: 6aa4144c41b41dbac0c7f262.jsonl[16212] _id=6ac53ea2de269131f9b67899 ts=2026-10-06T18:32:01.9460000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[16197] _id=6ac53ea2de269131f9b6789b ts=2026-10-06T18:32:01.9500000Z`; `1ms: 6aa4144c41b41dbac0c7f262.jsonl[17812] _id=6ac55815de269131f9b86116 ts=2026-10-06T20:20:37.0710000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[17821] _id=6ac55815de269131f9b86118 ts=2026-10-06T20:20:37.0720000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 102 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `288ms: 6aa4144c41b41dbac0c7f262.jsonl[13203] _id=6ac3eb31de269131f9aef323 ts=2026-10-05T18:23:45.6110000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[13233] _id=6ac3eb31de269131f9aef32b ts=2026-10-05T18:23:45.8990000Z`; `865ms: 6aa4144c41b41dbac0c7f262.jsonl[13233] _id=6ac3eb31de269131f9aef32b ts=2026-10-05T18:23:45.8990000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[13235] _id=6ac3eb32de269131f9aef341 ts=2026-10-05T18:23:46.7640000Z`; `476ms: 6aa4144c41b41dbac0c7f262.jsonl[13235] _id=6ac3eb32de269131f9aef341 ts=2026-10-05T18:23:46.7640000Z ~ 6aa4144c41b41dbac0c7f262.jsonl[13240] _id=6ac3eb33de269131f9aef34d ts=2026-10-05T18:23:47.2400000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11144] _id=6abe5630485cab4c95a3e2a3 ts=2026-10-01T12:46:43.1430000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11314] _id=6ac3b72cde269131f9ac5b19 ts=2026-10-05T14:41:49.0330000Z; 71h 31m: 6aa4144c41b41dbac0c7f262.jsonl[4574] _id=6ab6be78485cab4c955e4b27 ts=2026-09-25T18:33:28.3250000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4740] _id=6abaac54485cab4c956f6c99 ts=2026-09-28T18:05:08.8620000Z; 24h 16m: 6aa4144c41b41dbac0c7f262.jsonl[794] _id=6ab563ac485cab4c9553b5e8 ts=2026-09-24T17:53:48.3170000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3467] _id=6ab6b916485cab4c955db72a ts=2026-09-25T18:10:30.2230000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 97h 52m 
  - Evidence: 97h 52m: 6aa4144c41b41dbac0c7f262.jsonl[11309] _id=6abe5718485cab4c95a3f922 ts=2026-10-01T12:50:35.3320000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11365] _id=6ac3b76bde269131f9ac6768 ts=2026-10-05T14:42:51.2160000Z; 71h 24m: 6aa4144c41b41dbac0c7f262.jsonl[4716] _id=6ab6c077485cab4c955e666d ts=2026-09-25T18:41:59.1980000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4848] _id=6abaacb9485cab4c956f7213 ts=2026-09-28T18:06:49.8240000Z; 23h 59m: 6aa4144c41b41dbac0c7f262.jsonl[3453] _id=6ab56808485cab4c95542286 ts=2026-09-24T18:12:24.1530000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3493] _id=6ab6b956485cab4c955dbd81 ts=2026-09-25T18:11:34.4090000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 653 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f262.jsonl[17507] _id=6ac5554cde269131f9b84622 ts=2026-10-06T20:08:44.0130000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17508] _id=6ac5554cde269131f9b84623 ts=2026-10-06T20:08:44.0130000Z; 0ms: 6aa4144c41b41dbac0c7f262.jsonl[17544] _id=6ac55593de269131f9b84ded ts=2026-10-06T20:09:55.4560000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17545] _id=6ac55593de269131f9b84dee ts=2026-10-06T20:09:55.4560000Z; 0ms: 6aa4144c41b41dbac0c7f262.jsonl[17785] _id=6ac557f6de269131f9b860ea ts=2026-10-06T20:20:06.1080000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17786] _id=6ac557f6de269131f9b860eb ts=2026-10-06T20:20:06.1080000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 145h 55m 
  - Evidence: 145h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11021] _id=6abd5576485cab4c95919f6f ts=2026-09-30T18:31:18.3290000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17919] _id=6ac55975de269131f9b861e7 ts=2026-10-06T20:26:29.9070000Z; 144h 39m: 6aa4144c41b41dbac0c7f262.jsonl[790] _id=6ab56348485cab4c9553ad50 ts=2026-09-24T17:52:08.0900000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11021] _id=6abd5576485cab4c95919f6f ts=2026-09-30T18:31:18.3290000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 97h 51m 
  - Evidence: 97h 51m: 6aa4144c41b41dbac0c7f262.jsonl[11289] _id=6abe570d485cab4c95a3f802 ts=2026-10-01T12:50:24.3060000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11316] _id=6ac3b732de269131f9ac5cff ts=2026-10-05T14:41:53.9430000Z; 71h 22m: 6aa4144c41b41dbac0c7f262.jsonl[4735] _id=6ab6c094485cab4c955e66e3 ts=2026-09-25T18:42:28.8010000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4743] _id=6abaac5b485cab4c956f6ce1 ts=2026-09-28T18:05:15.0280000Z; 23h 58m: 6aa4144c41b41dbac0c7f262.jsonl[3452] _id=6ab567ed485cab4c95542180 ts=2026-09-24T18:11:57.4480000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3472] _id=6ab6b919485cab4c955db78d ts=2026-09-25T18:10:32.6850000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 167 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f262.jsonl[11317] _id=6ac3b732de269131f9ac5d10 ts=2026-10-05T14:41:53.9450000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11311] _id=6ac3b732de269131f9ac5d14 ts=2026-10-05T14:41:53.9450000Z; 0ms: 6aa4144c41b41dbac0c7f262.jsonl[13363] _id=6ac3ebdfde269131f9aefdf9 ts=2026-10-05T18:26:39.1960000Z -> 6aa4144c41b41dbac0c7f262.jsonl[13355] _id=6ac3ebdfde269131f9aefdfd ts=2026-10-05T18:26:39.1960000Z; 1ms: 6aa4144c41b41dbac0c7f262.jsonl[13319] _id=6ac3eb6bde269131f9aef705 ts=2026-10-05T18:24:42.7910000Z -> 6aa4144c41b41dbac0c7f262.jsonl[13320] _id=6ac3eb6bde269131f9aef707 ts=2026-10-05T18:24:42.7920000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11258] _id=6abe56f5485cab4c95a3f475 ts=2026-10-01T12:49:59.9020000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11439] _id=6ac3b7fade269131f9ac7f44 ts=2026-10-05T14:45:14.4470000Z; 71h 53m: 6aa4144c41b41dbac0c7f262.jsonl[4330] _id=6ab6bbdf485cab4c955e19c7 ts=2026-09-25T18:22:23.1200000Z -> 6aa4144c41b41dbac0c7f262.jsonl[5188] _id=6abaaec5485cab4c956fad55 ts=2026-09-28T18:15:33.4380000Z; 24h 1m: 6aa4144c41b41dbac0c7f262.jsonl[3439] _id=6ab567d2485cab4c95542096 ts=2026-09-24T18:11:30.7800000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3514] _id=6ab6b9a8485cab4c955dc85f ts=2026-09-25T18:12:56.3360000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f262.jsonl[15463] _id=6ac539eade269131f9b62eb6 ts=2026-10-06T18:11:54.3040000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15471] _id=6ac539eade269131f9b62eb9 ts=2026-10-06T18:11:54.3050000Z; 2ms: 6aa4144c41b41dbac0c7f262.jsonl[15543] _id=6ac53a3ade269131f9b63363 ts=2026-10-06T18:13:13.9830000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15545] _id=6ac53a3ade269131f9b63365 ts=2026-10-06T18:13:13.9850000Z; 6ms: 6aa4144c41b41dbac0c7f262.jsonl[113] _id=6ab4190b485cab4c954f4332 ts=2026-09-23T18:23:07.8230000Z -> 6aa4144c41b41dbac0c7f262.jsonl[117] _id=6ab4190b485cab4c954f4334 ts=2026-09-23T18:23:07.8290000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 97h 51m 
  - Evidence: 97h 51m: 6aa4144c41b41dbac0c7f262.jsonl[11308] _id=6abe5718485cab4c95a3f91d ts=2026-10-01T12:50:35.1810000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11315] _id=6ac3b732de269131f9ac5cf0 ts=2026-10-05T14:41:49.0400000Z; 71h 22m: 6aa4144c41b41dbac0c7f262.jsonl[4734] _id=6ab6c094485cab4c955e66e1 ts=2026-09-25T18:42:28.7710000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4742] _id=6abaac5a485cab4c956f6cdd ts=2026-09-28T18:05:08.8670000Z; 23h 58m: 6aa4144c41b41dbac0c7f262.jsonl[3459] _id=6ab56803485cab4c95542264 ts=2026-09-24T18:12:19.4850000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3471] _id=6ab6b919485cab4c955db785 ts=2026-09-25T18:10:30.2290000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11303] _id=6abe570f485cab4c95a3f843 ts=2026-10-01T12:50:24.3480000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11467] _id=6ac3b80bde269131f9ac8154 ts=2026-10-05T14:45:31.2690000Z; 71h 54m: 6aa4144c41b41dbac0c7f262.jsonl[4352] _id=6ab6bc0e485cab4c955e1c4d ts=2026-09-25T18:23:09.6250000Z -> 6aa4144c41b41dbac0c7f262.jsonl[5282] _id=6abaaf49485cab4c956fc068 ts=2026-09-28T18:17:44.8900000Z; 24h 22m: 6aa4144c41b41dbac0c7f262.jsonl[6582] _id=6abab141485cab4c956ffa57 ts=2026-09-28T18:26:07.7280000Z -> 6aa4144c41b41dbac0c7f262.jsonl[8797] _id=6abc07ed485cab4c9584c849 ts=2026-09-29T18:48:12.4290000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3834 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f262.jsonl[10130] _id=6abd4f5a485cab4c9590d86f ts=2026-09-30T18:05:13.3330000Z -> 6aa4144c41b41dbac0c7f262.jsonl[10182] _id=6abd4f5a485cab4c9590d871 ts=2026-09-30T18:05:13.3330000Z; 0ms: 6aa4144c41b41dbac0c7f262.jsonl[10131] _id=6abd4f5b485cab4c9590d879 ts=2026-09-30T18:05:13.3610000Z -> 6aa4144c41b41dbac0c7f262.jsonl[10171] _id=6abd4f5b485cab4c9590d87b ts=2026-09-30T18:05:13.3610000Z; 0ms: 6aa4144c41b41dbac0c7f262.jsonl[10133] _id=6abd4f5b485cab4c9590d885 ts=2026-09-30T18:05:14.0640000Z -> 6aa4144c41b41dbac0c7f262.jsonl[10134] _id=6abd4f5b485cab4c9590d889 ts=2026-09-30T18:05:14.0640000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 97h 54m 
  - Evidence: 97h 54m: 6aa4144c41b41dbac0c7f262.jsonl[11277] _id=6abe5706485cab4c95a3f6f9 ts=2026-10-01T12:50:17.2250000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11443] _id=6ac3b7fade269131f9ac7f40 ts=2026-10-05T14:45:14.4390000Z; 71h 53m: 6aa4144c41b41dbac0c7f262.jsonl[4308] _id=6ab6bbe2485cab4c955e1a0d ts=2026-09-25T18:22:26.1010000Z -> 6aa4144c41b41dbac0c7f262.jsonl[5190] _id=6abaaec5485cab4c956fad53 ts=2026-09-28T18:15:33.4330000Z; 42h 2m: 6aa4144c41b41dbac0c7f262.jsonl[8773] _id=6abc07c5485cab4c9584c653 ts=2026-09-29T18:47:33.4920000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11257] _id=6abe56f5485cab4c95a3f470 ts=2026-10-01T12:49:59.8960000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 6aa4144c41b41dbac0c7f262.jsonl[17669] _id=6ac55725de269131f9b85fff ts=2026-10-06T20:16:37.2050000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17681] _id=6ac55725de269131f9b86001 ts=2026-10-06T20:16:37.2070000Z; 2ms: 6aa4144c41b41dbac0c7f262.jsonl[17686] _id=6ac55753de269131f9b8602a ts=2026-10-06T20:17:23.6030000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17696] _id=6ac55753de269131f9b8602c ts=2026-10-06T20:17:23.6050000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 116h 21m 
  - Evidence: 116h 21m: 6aa4144c41b41dbac0c7f262.jsonl[10817] _id=6abd532b485cab4c95913f3d ts=2026-09-30T18:21:31.5690000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11372] _id=6ac3b779de269131f9ac69ca ts=2026-10-05T14:43:05.4040000Z; 71h 26m: 6aa4144c41b41dbac0c7f262.jsonl[4727] _id=6ab6c07c485cab4c955e6681 ts=2026-09-25T18:42:04.3720000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4868] _id=6abaad13485cab4c956f775f ts=2026-09-28T18:08:19.8170000Z; 24h 12m: 6aa4144c41b41dbac0c7f262.jsonl[1022] _id=6ab56570485cab4c9553e346 ts=2026-09-24T18:01:20.7430000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3542] _id=6ab6b9fb485cab4c955dd16f ts=2026-09-25T18:14:19.8130000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 34m 
  - Evidence: 167h 34m: 6aa4144c41b41dbac0c7f262.jsonl[8613] _id=6abc06d0485cab4c9584b677 ts=2026-09-29T18:43:27.9920000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15792] _id=6ac53b69de269131f9b64295 ts=2026-10-06T18:18:17.6870000Z; 120h 54m: 6aa4144c41b41dbac0c7f262.jsonl[676] _id=6ab56274485cab4c95539b84 ts=2026-09-24T17:48:36.3670000Z -> 6aa4144c41b41dbac0c7f262.jsonl[8580] _id=6abc06b6485cab4c9584b461 ts=2026-09-29T18:43:02.4930000Z; 1h 47m: 6aa4144c41b41dbac0c7f262.jsonl[16006] _id=6ac53c31de269131f9b64f35 ts=2026-10-06T18:21:37.8260000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17506] _id=6ac5554bde269131f9b8461e ts=2026-10-06T20:08:43.9990000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 32m 
  - Evidence: 167h 32m: 6aa4144c41b41dbac0c7f262.jsonl[8621] _id=6abc06d0485cab4c9584b681 ts=2026-09-29T18:43:28.0510000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15623] _id=6ac53adade269131f9b63ba7 ts=2026-10-06T18:15:54.5330000Z; 120h 53m: 6aa4144c41b41dbac0c7f262.jsonl[677] _id=6ab56274485cab4c95539b88 ts=2026-09-24T17:48:36.3800000Z -> 6aa4144c41b41dbac0c7f262.jsonl[8511] _id=6abc0671485cab4c9584ae41 ts=2026-09-29T18:41:53.8490000Z; 1h 44m: 6aa4144c41b41dbac0c7f262.jsonl[16003] _id=6ac53c32de269131f9b64f45 ts=2026-10-06T18:21:37.8730000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17344] _id=6ac554b3de269131f9b831c1 ts=2026-10-06T20:06:11.7000000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.034s shown 
  - Evidence: 21ms: 6aa4144c41b41dbac0c7f262.jsonl[16007] _id=6ac53c31de269131f9b64f39 ts=2026-10-06T18:21:37.8520000Z -> 6aa4144c41b41dbac0c7f262.jsonl[16003] _id=6ac53c32de269131f9b64f45 ts=2026-10-06T18:21:37.8730000Z; 34ms: 6aa4144c41b41dbac0c7f262.jsonl[8617] _id=6abc06d0485cab4c9584b67b ts=2026-09-29T18:43:28.0170000Z -> 6aa4144c41b41dbac0c7f262.jsonl[8621] _id=6abc06d0485cab4c9584b681 ts=2026-09-29T18:43:28.0510000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 32m 
  - Evidence: 167h 32m: 6aa4144c41b41dbac0c7f262.jsonl[8616] _id=6abc06ce485cab4c9584b661 ts=2026-09-29T18:43:26.6990000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15631] _id=6ac53ad9de269131f9b63b93 ts=2026-10-06T18:15:52.9550000Z; 120h 53m: 6aa4144c41b41dbac0c7f262.jsonl[675] _id=6ab56273485cab4c95539b7a ts=2026-09-24T17:48:34.9010000Z -> 6aa4144c41b41dbac0c7f262.jsonl[8516] _id=6abc067d485cab4c9584af67 ts=2026-09-29T18:42:05.0310000Z; 1h 44m: 6aa4144c41b41dbac0c7f262.jsonl[16001] _id=6ac53c2dde269131f9b64ecd ts=2026-10-06T18:21:33.7140000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17348] _id=6ac554b7de269131f9b83277 ts=2026-10-06T20:06:15.0170000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 139 interval(s) ≤ 0.001s..0.016s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f262.jsonl[15829] _id=6ac53b7dde269131f9b643bd ts=2026-10-06T18:18:37.6130000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15830] _id=6ac53b7dde269131f9b643c3 ts=2026-10-06T18:18:37.6140000Z; 16ms: 6aa4144c41b41dbac0c7f262.jsonl[15956] _id=6ac53c01de269131f9b64b77 ts=2026-10-06T18:20:49.3090000Z -> 6aa4144c41b41dbac0c7f262.jsonl[15957] _id=6ac53c01de269131f9b64b7b ts=2026-10-06T18:20:49.3250000Z; 16ms: 6aa4144c41b41dbac0c7f262.jsonl[17350] _id=6ac554b9de269131f9b83301 ts=2026-10-06T20:06:17.7820000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17351] _id=6ac554b9de269131f9b83305 ts=2026-10-06T20:06:17.7980000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 120h 54m 
  - Evidence: 120h 54m: 6aa4144c41b41dbac0c7f262.jsonl[655] _id=6ab56256485cab4c95539946 ts=2026-09-24T17:48:06.7550000Z -> 6aa4144c41b41dbac0c7f262.jsonl[8510] _id=6abc06b4485cab4c9584b429 ts=2026-09-29T18:43:00.3570000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 59m 33s 
  - Evidence: 59m 33s: 6aa4144c41b41dbac0c7f262.jsonl[17059] _id=6ac541f6de269131f9b6da90 ts=2026-10-06T18:46:14.4430000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17157] _id=6ac54febde269131f9b7b4c2 ts=2026-10-06T19:45:47.5970000Z; 13m 26s: 6aa4144c41b41dbac0c7f262.jsonl[16214] _id=6ac53ecfde269131f9b67be1 ts=2026-10-06T18:32:47.6540000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17059] _id=6ac541f6de269131f9b6da90 ts=2026-10-06T18:46:14.4430000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11143] _id=6abe5628485cab4c95a3e1e7 ts=2026-10-01T12:46:35.3900000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11313] _id=6ac3b724de269131f9ac58a4 ts=2026-10-05T14:41:40.9350000Z; 71h 31m: 6aa4144c41b41dbac0c7f262.jsonl[4571] _id=6ab6be72485cab4c955e4af1 ts=2026-09-25T18:33:22.8890000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4741] _id=6abaac4e485cab4c956f6c5d ts=2026-09-28T18:05:03.4350000Z; 24h 16m: 6aa4144c41b41dbac0c7f262.jsonl[795] _id=6ab563a4485cab4c9553b528 ts=2026-09-24T17:53:39.9340000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3466] _id=6ab6b910485cab4c955db6cb ts=2026-09-25T18:10:24.9770000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11142] _id=6abe5628485cab4c95a3e1e3 ts=2026-10-01T12:46:35.3900000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11312] _id=6ac3b724de269131f9ac5896 ts=2026-10-05T14:41:40.9350000Z; 71h 23m: 6aa4144c41b41dbac0c7f262.jsonl[4721] _id=6ab6c064485cab4c955e65ff ts=2026-09-25T18:41:40.9430000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4739] _id=6abaac4e485cab4c956f6c56 ts=2026-09-28T18:05:03.4350000Z; 24h 16m: 6aa4144c41b41dbac0c7f262.jsonl[793] _id=6ab563a4485cab4c9553b522 ts=2026-09-24T17:53:39.9330000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3465] _id=6ab6b910485cab4c955db6c5 ts=2026-09-25T18:10:24.9760000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 101h 59m 
  - Evidence: 101h 59m: 6aa4144c41b41dbac0c7f262.jsonl[11307] _id=6abe5719485cab4c95a3f92f ts=2026-10-01T12:50:35.8970000Z -> 6aa4144c41b41dbac0c7f262.jsonl[14581] _id=6ac3f16fde269131f9af6687 ts=2026-10-05T18:50:23.7610000Z; 71h 46m: 6aa4144c41b41dbac0c7f262.jsonl[4736] _id=6ab6c096485cab4c955e66e9 ts=2026-09-25T18:42:30.6250000Z -> 6aa4144c41b41dbac0c7f262.jsonl[6646] _id=6abab1ec485cab4c95700654 ts=2026-09-28T18:28:59.9950000Z; 24h 3m: 6aa4144c41b41dbac0c7f262.jsonl[3458] _id=6ab56806485cab4c9554227a ts=2026-09-24T18:12:22.3310000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3576] _id=6ab6ba74485cab4c955de157 ts=2026-09-25T18:16:20.7230000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f262.jsonl[3576] _id=6ab6ba74485cab4c955de157 ts=2026-09-25T18:16:20.7230000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3578] _id=6ab6ba89485cab4c955de4b3 ts=2026-09-25T18:16:20.723Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f262.jsonl[11147] _id=6abe5636485cab4c95a3e339 ts=2026-10-01T12:46:48.4130000Z -> 6aa4144c41b41dbac0c7f262.jsonl[11318] _id=6ac3b732de269131f9ac5d18 ts=2026-10-05T14:41:53.9680000Z; 71h 27m: 6aa4144c41b41dbac0c7f262.jsonl[4645] _id=6ab6bf6e485cab4c955e5669 ts=2026-09-25T18:37:34.2990000Z -> 6aa4144c41b41dbac0c7f262.jsonl[4751] _id=6abaac5b485cab4c956f6cf7 ts=2026-09-28T18:05:15.0600000Z; 23h 58m: 6aa4144c41b41dbac0c7f262.jsonl[3449] _id=6ab567f7485cab4c955421fc ts=2026-09-24T18:12:07.6840000Z -> 6aa4144c41b41dbac0c7f262.jsonl[3478] _id=6ab6b91a485cab4c955db7cf ts=2026-09-25T18:10:32.7360000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f262.jsonl[17564] _id=6ac555a6de269131f9b84ff9 ts=2026-10-06T20:10:14.6070000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17565] _id=6ac555a6de269131f9b84ffa ts=2026-10-06T20:10:14.6070000Z; 1ms: 6aa4144c41b41dbac0c7f262.jsonl[16714] _id=6ac54020de269131f9b6a2d7 ts=2026-10-06T18:38:24.3440000Z -> 6aa4144c41b41dbac0c7f262.jsonl[16748] _id=6ac54020de269131f9b6a2db ts=2026-10-06T18:38:24.3450000Z; 1ms: 6aa4144c41b41dbac0c7f262.jsonl[17812] _id=6ac55815de269131f9b86116 ts=2026-10-06T20:20:37.0710000Z -> 6aa4144c41b41dbac0c7f262.jsonl[17821] _id=6ac55815de269131f9b86118 ts=2026-10-06T20:20:37.0720000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[411] _id=6ab41e62485cab4c954f7057 ts=2026-09-23T18:45:54.1300000Z`; `6aa4144c41b41dbac0c7f262.jsonl[691] _id=6ab5629d485cab4c95539e54 ts=2026-09-24T17:49:16.9230000Z`; `6aa4144c41b41dbac0c7f262.jsonl[6535] _id=6abab126485cab4c956ff82b ts=2026-09-28T18:25:42.7180000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 224 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[1597] _id=6ab56602485cab4c9553fa30 ts=2026-09-24T18:03:45.7440000Z`; `6aa4144c41b41dbac0c7f262.jsonl[1624] _id=6ab5660a485cab4c9553fb2c ts=2026-09-24T18:03:53.3700000Z`; `6aa4144c41b41dbac0c7f262.jsonl[1731] _id=6ab5661a485cab4c9553fe26 ts=2026-09-24T18:04:08.6610000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 403 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[913] _id=6ab56523485cab4c9553d582 ts=2026-09-24T17:59:58.5580000Z`; `6aa4144c41b41dbac0c7f262.jsonl[938] _id=6ab56526485cab4c9553d5b9 ts=2026-09-24T17:59:58.5810000Z`; `6aa4144c41b41dbac0c7f262.jsonl[940] _id=6ab56527485cab4c9553d5ca ts=2026-09-24T17:59:58.5910000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[8621] _id=6abc06d0485cab4c9584b681 ts=2026-09-29T18:43:28.0510000Z`; `6aa4144c41b41dbac0c7f262.jsonl[16003] _id=6ac53c32de269131f9b64f45 ts=2026-10-06T18:21:37.8730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[561] _id=6ab561ec485cab4c95539166 ts=2026-09-24T17:46:20.4170000Z`; `6aa4144c41b41dbac0c7f262.jsonl[574] _id=6ab561ef485cab4c955391b6 ts=2026-09-24T17:46:23.5780000Z`; `6aa4144c41b41dbac0c7f262.jsonl[616] _id=6ab56242485cab4c9553976c ts=2026-09-24T17:47:45.9800000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[16214] _id=6ac53ecfde269131f9b67be1 ts=2026-10-06T18:32:47.6540000Z`; `6aa4144c41b41dbac0c7f262.jsonl[17059] _id=6ac541f6de269131f9b6da90 ts=2026-10-06T18:46:14.4430000Z`; `6aa4144c41b41dbac0c7f262.jsonl[17157] _id=6ac54febde269131f9b7b4c2 ts=2026-10-06T19:45:47.5970000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[12443] _id=6ac3bad4de269131f9acbca9 ts=2026-10-05T14:57:24.1580000Z`; `6aa4144c41b41dbac0c7f262.jsonl[12759] _id=6ac3e810de269131f9aec2b0 ts=2026-10-05T18:10:24.3440000Z`; `6aa4144c41b41dbac0c7f262.jsonl[13335] _id=6ac3ebafde269131f9aefa0d ts=2026-10-05T18:25:51.3940000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[422] _id=6ab56108485cab4c95537d43 ts=?`; `6aa4144c41b41dbac0c7f262.jsonl[14607] _id=6ac40ce9de269131f9afa087 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 784 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[1711] _id=6ab5662c485cab4c9554004e ts=2026-09-24T18:04:27.4160000Z`; `6aa4144c41b41dbac0c7f262.jsonl[1808] _id=6ab5662d485cab4c9554005e ts=2026-09-24T18:04:27.7740000Z`; `6aa4144c41b41dbac0c7f262.jsonl[1713] _id=6ab5662d485cab4c95540062 ts=2026-09-24T18:04:28.2080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1230 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[906] _id=6ab5651f485cab4c9553d54c ts=2026-09-24T17:59:58.4510000Z`; `6aa4144c41b41dbac0c7f262.jsonl[911] _id=6ab5651f485cab4c9553d550 ts=2026-09-24T17:59:58.5030000Z`; `6aa4144c41b41dbac0c7f262.jsonl[901] _id=6ab5651f485cab4c9553d55a ts=2026-09-24T17:59:58.5310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 25 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[637] _id=6ab56250485cab4c95539896 ts=2026-09-24T17:48:00.3050000Z`; `6aa4144c41b41dbac0c7f262.jsonl[640] _id=6ab56250485cab4c95539898 ts=2026-09-24T17:48:00.4710000Z`; `6aa4144c41b41dbac0c7f262.jsonl[669] _id=6ab56267485cab4c95539a88 ts=2026-09-24T17:48:23.2520000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 438 start, 430 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 226 unmatched 'BecameCameraCentered' (totals: 1088 open, 1086 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 148 unmatched 'BecameVisible' (totals: 1889 open, 2144 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationNodeHoverStart' (totals: 288 open, 297 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 28 unmatched 'questActiveEvent' (totals: 58 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 484 of 17917 adjacent _id pairs reverse in client time; worst 205.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f262.jsonl[945] _id=6ab565d7485cab4c9553f2a3 ts=2026-09-24T18:03:03.2740000Z`; `6aa4144c41b41dbac0c7f262.jsonl[1197] _id=6ab565d8485cab4c9553f2c7 ts=2026-09-24T17:59:37.5870000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.07s, min -206.74s, max +2.71s over 17918 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4144c41b41dbac0c7f262\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 6207 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3860); Unit 4 Dev (1239); Unit 3 Dungeon Dev (674); Unit 5 Dev - Dungeon (434)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.02s, n=6206)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6207/6207 records)
    "BecameInvisible"  x2144
    "BecameVisible"  x1889
    "BecameCameraCentered"  x1088
    "BecameCameraUncentered"  x1086
data.pieceId  (string, 6207/6207 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 6207/6207 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 5417 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1173); Unit 2 Prod (Refactor) (1156); Unit 4 Dev - Dungeon (998); Unit 3 Dungeon Dev (750); Unit 4 Dev (616); Unit 5 Dev - Dungeon (204); Unit 5 Dev (180); Unit 1 Dev (178); Unit 4 Dev - Anderson Base (162)
- **Intervals:** median 0.74s (p5 0.08s / p95 10.23s, n=5416)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5417/5417 records)
    "pressed"  x5417
data.actionType  (string, 5417/5417 records)
    "Move"  x3487
    "Jump"  x1059
    "Interact"  x717
    "Sprint"  x79
    "Hoverboard"  x33
    "Ascend"  x22
    "Descend"  x16
    "Map"  x3
    "SkipCinematic"  x1
data.key  (string, 5417/5417 records)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5417/5417 records)
    "Player"  x4327
    "Drone"  x1090
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2374 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (577); Unit 4 Dev (361); Unit 4 Dev - Dungeon (335); Unit 3 Dev (269); Unit 1 Dev (237); Unit 5 Dev (231); Unit 3 Dungeon Dev (199); Unit 4 Dev - Anderson Base (84); Unit 5 Dev - Dungeon (81)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.03s, n=2362)
- **Fields under `data`:**

```text
data.position  (object, 2374/2374 records)
data.position.x  (number, 2374/2374 records)
    numeric range -652.43 .. 1795.58 (781 unique)
data.position.y  (number, 2374/2374 records)
    numeric range -112.909 .. 222.405 (564 unique)
data.position.z  (number, 2374/2374 records)
    numeric range -1040.33 .. 2392.29 (782 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2140 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (538); Unit 3 Dev (335); Unit 4 Dev (277); Unit 3 Dungeon Dev (231); Unit 5 Dev (223); Unit 1 Dev (191); Unit 4 Dev - Dungeon (162); Unit 4 Dev - Anderson Base (114); Unit 5 Dev - Dungeon (69)
- **eventKey:** present on 1272 of 2140 records
- **Intervals:** median 4.17s (p5 0.00s / p95 46.66s, n=2139)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1272; [conversationId, dialogueEventType] x868
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2140/2140 records)
    numeric range 8 .. 118 (53 unique)
data.dialogueEventType  (string, 2140/2140 records)
    "DialogueNodeEvent"  x1272
    "DialogueStartEvent"  x438
    "DialogueFinishEvent"  x430
data.nodeId  (number, 1272/2140 records)
    numeric range 0 .. 290 (215 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 639 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (271); Unit 5 Dev (146); Unit 1 Dev (135); Unit 3 Dev (87)
- **Intervals:** median 0.37s (p5 0.02s / p95 5.66s, n=638)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 639/639 records)
    "argumentationNodeHoverEnd"  x297
    "argumentationNodeHoverStart"  x288
    "argumentationNodeAdd"  x34
    "argumentationNodeRemove"  x20
data.argumentationTitle  (string, 639/639 records)
    "Unit 4 - Flooding"  x271
    "Unit 5"  x146
    "Unit 3 - Pollution Upstream"  x87
    "Unit 1 - Argumentation Tutorial"  x78
    "Unit 1 - Freshwater"  x57
data.nodeName  (string, 639/639 records)
    "A"  x120
    "1"  x90
    "B"  x74
    "3"  x65
    "II"  x60
    "C"  x58
    "D"  x52
    "I"  x44
    "2"  x39
    "4"  x34
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 488 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (256); Unit 3 Dungeon Dev (75); Unit 2 Prod (Refactor) (73); Unit 5 Dev (27); Unit 4 Dev (17); Unit 3 Dev (11); Unit 1 Dev (10); Unit 5 Dev - Dungeon (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 4.81s (p5 0.22s / p95 348.58s, n=487)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 488/488 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 488/488 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `soilMachine` — 159 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (159)
- **Intervals:** median 0.49s (p5 0.19s / p95 35.49s, n=158)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 159/159 records)
    "ChangeCanister"  x159
data.canisterType  (string, 159/159 records)
    "Clay"  x113
    "Bedrock"  x22
    "Gravel"  x18
    "Sand"  x6
data.floor  (string, 159/159 records)
    "5"  x82
    "3"  x72
    "4"  x5
data.machine  (string, 159/159 records)
    "1"  x143
    "2"  x16
data.row  (string, 159/159 records)
    "TopRow"  x152
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 116 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (64); Unit 3 Dev (26); Unit 4 Dev (26)
- **Intervals:** median 0.66s (p5 0.16s / p95 12.33s, n=115)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x104; [Soil Key Puzzle Status, Unit] x12
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/116 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/116 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 104/116 records)
    "RightDrag"  x55
    "LeftDrag"  x49
data.currentSoilType  (string, 104/116 records)
    "SAND"  x23
    "CLAYSAND"  x21
    "SANDGRAVEL"  x18
    "CLAY"  x16
    "CLAYROCK"  x13
    "GRAVEL"  x8
    "BEDROCK"  x5
data.isCorrectSelection  (string, 104/116 records)
    "false"  x81
    "true"  x23
data.waterLevelStatus  (string, 104/116 records)
    "Proper"  x40
    "TooLow"  x34
    "TooHigh"  x30
data.waterRetentionChange  (string, 104/116 records)
    "Decrease"  x41
    "Increase"  x40
    "NoChange"  x23
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 92 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 4 Dev - Dungeon (16); Unit 1 Dev (13); Unit 4 Dev (13); Unit 3 Dev (9); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 92 of 92 records
- **Intervals:** median 219.21s (p5 0.00s / p95 79539.28s, n=91)
- **`data` key-set variants:** [questEventType, questID, questName] x58; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 92/92 records)
    "questActiveEvent"  x58
    "questFinishEvent"  x34
data.questID  (string, 92/92 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 92/92 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/92 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 47 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (40); Unit 3 Dev (4); Unit 4 Dev (3)
- **Intervals:** median 6.11s (p5 0.18s / p95 86969.05s, n=46)
- **`data` key-set variants:** [actionType, featureUsed] x24; [actionType, featureUsed, legendName] x15; [actionType, featureUsed, location] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 47/47 records)
    "MapCloseEvent"  x12
    "MapOpenEvent"  x12
    "Selected"  x12
    "WaypointMoveEvent"  x6
    "Unselected"  x3
    "WaypointSetEvent"  x2
data.featureUsed  (string, 47/47 records)
    "Map"  x24
    "Legend"  x15
    "Waypoint"  x8
data.legendName  (string, 15/47 records)
    "60 ft"  x5
    "330 ft"  x3
    "0 ft"  x2
    "30 ft"  x2
    "120 ft"  x1
    "240 ft"  x1
    "90 ft"  x1
data.location  (object, 8/47 records)
data.location.x  (number, 8/47 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 8/47 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 8/47 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 37 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (23); Unit 5 Dev (6); Unit 2 Prod (Refactor) (5); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 919.20s (p5 11.75s / p95 129804.41s, n=36)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 37/37 records)
    true  x37
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 36 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (30); Unit 1 Dev (2); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 3.00s (p5 0.26s / p95 135078.16s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "submitAnswerEvent"  x36
data.answerSubmitted  (string, 36/36 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 36/36 records)
    "Unit 4 - Flooding"  x30
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 33 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (33)
- **Intervals:** median 5.54s (p5 0.73s / p95 50.73s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "On"  x22
    "Off"  x11
data.floor  (string, 33/33 records)
    "4"  x20
    "3"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 33/33 records)
    "One"  x32
    "Two"  x1
data.machineType  (string, 33/33 records)
    "Condenser"  x19
    "Evaporator"  x11
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 33/33 records)
    "3"  x18
    "2"  x9
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 4 Dev (7); Unit 3 Dungeon Dev (4); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2); MainMenu (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1219.64s (p5 138.89s / p95 197966.02s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `SolarStillDesignEvent` — 29 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (29)
- **Intervals:** median 2.61s (p5 0.29s / p95 13.99s, n=28)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x28; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "optionSelected"  x28
    "DesignSubmitted"  x1
data.designSelections  (object, 1/29 records)
data.designSelections.glassRoofTemperature  (string, 1/29 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/29 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/29 records)
    "Tilted Out"  x1
data.featureUsed  (string, 29/29 records)
    "RoofStyle"  x17
    "GlassRoofTemperature"  x8
    "ExtraCovering"  x3
    "Submit"  x1
data.selectedOption  (string, 28/29 records, 7 empty-string)
    ""  x7
    "Flat"  x5
    "Tilted In"  x4
    "Tilted Out"  x4
    "Cold"  x3
    "Hot"  x3
    "Covered"  x2
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameWindowUnfocusEvent` — 26 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 5 Dev (6); Unit 3 Dungeon Dev (4); Unit 4 Dev (4); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1468.24s (p5 0.40s / p95 224039.17s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 6471.96s (p5 134.74s / p95 248995.77s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 94.17s (p5 0.03s / p95 519171.98s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 4 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (4)
- **Intervals:** median 19.23s (p5 6.26s / p95 33.05s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records, 1 empty-string)
    "cameraPlaced"  x3
    ""  x1
data.boxId  (string, 4/4 records)
    "2"  x2
    "0"  x1
    "1"  x1
data.soilType  (string, 4/4 records)
    "Gravel"  x2
    "None"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (1)
- **Intervals:** median 123.97s (p5 22.94s / p95 391776.64s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 523030.91s (p5 520978.31s / p95 525083.51s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 2189.97s (p5 945.11s / p95 3434.84s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "Permissions check failed"  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records)
    "TypeError: Permissions check failed"  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit1"  x1
    "unit4"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (64 records)
- `TerasGardenBox` data.actionType: "" (1x)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "Selected" (12x); "Unselected" (3x); "WaypointMoveEvent" (6x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Legend" (15x); "Waypoint" (8x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (20x)
- `soilMachine` data.canisterType: "Bedrock" (22x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*