# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1ee

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1ee
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1ee.jsonl
- **Records:** 11153 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1ee
- **Time span:** 2026-09-23T13:04:20.607000+00:00 .. 2026-10-08T15:57:10.850000+00:00 (362h 52m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1ee\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 11153 records, 9 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 114 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3596 | 32.24 | 1 | 3 | 0 | 2026-09-24T13:21:42.655000+00:00 | 2026-10-07T13:28:01.631000+00:00 | 312h 6m |
| InputEvent | 2554 | 22.9 | 1 | 8 | 0 | 2026-09-23T13:06:03.456000+00:00 | 2026-10-08T15:54:31.149000+00:00 | 362h 48m |
| PlayerPositionEvent | 2304 | 20.66 | 1 | 8 | 0 | 2026-09-23T13:05:57.663000+00:00 | 2026-10-08T15:57:10.850000+00:00 | 362h 51m |
| DialogueEvent | 1731 | 15.52 | 1 | 8 | 1080 | 2026-09-23T13:06:20.407000+00:00 | 2026-10-08T15:57:08.878000+00:00 | 362h 50m |
| argumentationNodeEvent | 250 | 2.24 | 1 | 3 | 0 | 2026-09-23T13:41:07.229000+00:00 | 2026-10-08T15:46:05.885000+00:00 | 362h 4m |
| ObjectInterEvent | 244 | 2.19 | 1 | 8 | 0 | 2026-09-23T13:16:38.945000+00:00 | 2026-10-08T15:54:05.322000+00:00 | 362h 37m |
| questEvent | 87 | 0.78 | 1 | 8 | 87 | 2026-09-23T13:06:20.387000+00:00 | 2026-10-08T15:57:03.084000+00:00 | 362h 50m |
| WaterChamberEvent | 72 | 0.65 | 1 | 1 | 0 | 2026-10-07T13:26:21.994000+00:00 | 2026-10-07T15:47:18.877000+00:00 | 2h 20m |
| TopographicMapEvent | 63 | 0.56 | 1 | 2 | 0 | 2026-09-24T13:11:38.702000+00:00 | 2026-10-01T13:09:51.474000+00:00 | 167h 58m |
| Soil Key Puzzle | 50 | 0.45 | 1 | 2 | 0 | 2026-09-25T13:19:48.361000+00:00 | 2026-10-01T13:21:43.650000+00:00 | 144h 1m |
| gameWindowFocusEvent | 36 | 0.32 | 1 | 5 | 0 | 2026-09-23T13:04:20.607000+00:00 | 2026-10-08T15:40:09.768000+00:00 | 362h 35m |
| DEBUGMenu | 29 | 0.26 | 1 | 8 | 0 | 2026-09-23T13:05:57.656000+00:00 | 2026-10-08T15:40:09.291000+00:00 | 362h 34m |
| SolarStillDesignEvent | 24 | 0.22 | 1 | 1 | 0 | 2026-10-08T15:53:05.768000+00:00 | 2026-10-08T15:53:44.772000+00:00 | 39.0s |
| gameStartEvent | 23 | 0.21 | 1 | 1 | 0 | 2026-09-23T13:04:20.608000+00:00 | 2026-10-08T15:40:09.768000+00:00 | 362h 35m |
| argumentationAnswerEvent | 17 | 0.15 | 1 | 3 | 0 | 2026-09-24T13:03:54.001000+00:00 | 2026-10-08T15:46:19.158000+00:00 | 338h 42m |
| gameWindowUnfocusEvent | 16 | 0.14 | 1 | 5 | 0 | 2026-09-23T13:04:27.180000+00:00 | 2026-10-07T16:02:43.665000+00:00 | 338h 58m |
| soilMachine | 14 | 0.13 | 1 | 1 | 0 | 2026-10-01T13:38:11.270000+00:00 | 2026-10-05T13:26:04.768000+00:00 | 95h 47m |
| argumentationToolEvent | 12 | 0.11 | 1 | 2 | 0 | 2026-09-24T13:03:25.763000+00:00 | 2026-10-08T15:46:17.392000+00:00 | 338h 42m |
| argumentationEvent | 9 | 0.08 | 1 | 3 | 0 | 2026-09-24T13:03:26.474000+00:00 | 2026-10-08T15:46:19.215000+00:00 | 338h 42m |
| TerasGardenBox | 6 | 0.05 | 1 | 1 | 0 | 2026-10-06T13:18:12.277000+00:00 | 2026-10-06T13:20:41.959000+00:00 | 2m 29s |
| chatEvent | 6 | 0.05 | 1 | 2 | 0 | 2026-10-06T13:38:40.656000+00:00 | 2026-10-08T15:40:17.403000+00:00 | 50h 1m |
| DaniEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-01T13:00:51.943000+00:00 | 2026-10-01T13:02:31.715000+00:00 | 1m 39s |
| crash | 4 | 0.04 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-24T13:09:48.037000+00:00 | 2026-10-06T13:38:00.020000+00:00 | 288h 28m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 1038491.983s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.645s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.145s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.037s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 13.45s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 7.504s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.607s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.724s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 7063.493s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 5344.017s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 485.195s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 490.701s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.436s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: E to Talk; Place Cube; Press E To Change Direction; Press E To Pick Up; Press E To Place Glyph; Press E to Plant Seed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 6.0x vs baseline. 
  - Observed: 24 records 
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
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 72 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.4x vs baseline. 
  - Observed: 17 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,1,; C,2,II; C,D,2,II; C,D,3,II; C,D,4,3,II; C,D,A,2,II; C,D,B,2,II; D,C,4,II 
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
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 31; 54; 55 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Forsaken Facility; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; TK, Reporting In! 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 80 mismatch(es); e.g. 'DialogueNodeEvent:30:50' vs expected 'DialogueNodeEvent:31:68' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2224] _id=6aba64cb485cab4c95679659 ts=2026-09-23T13:21:35.912Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2227] _id=6aba64cd485cab4c95679669 ts=2026-09-23T13:22:03.664Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2200] _id=6aba64ce485cab4c95679671 ts=2026-09-23T13:22:31.006Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'questFinishEvent:29' vs expected 'questFinishEvent:32' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2197] _id=6aba64cc485cab4c95679661 ts=2026-09-23T13:22:03.651Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2198] _id=6aba64cd485cab4c95679667 ts=2026-09-23T13:22:03.658Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2289] _id=6aba64dc485cab4c956796f7 ts=2026-09-23T13:27:22.472Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[3] _id=6ab3ce54485cab4c954b849e ts=2026-09-23T13:04:20.6080000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[199] _id=6ab51ea0485cab4c954fe661 ts=2026-09-24T12:59:12.0360000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[487] _id=6ab5216f485cab4c95502577 ts=2026-09-24T13:11:11.0230000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 36 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 36} 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2] _id=6ab3ce54485cab4c954b849c ts=2026-09-23T13:04:20.6070000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[6] _id=6ab3ce62485cab4c954b84ac ts=2026-09-23T13:04:34.9170000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[93] _id=6ab3d048485cab4c954b9400 ts=2026-09-23T13:12:40.1120000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[1] _id=6ab3ce5a485cab4c954b84a0 ts=2026-09-23T13:04:27.1800000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[90] _id=6ab3d045485cab4c954b93c8 ts=2026-09-23T13:12:37.8810000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[196] _id=6ab3d18b485cab4c954bce2a ts=2026-09-23T13:18:03.4900000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 7 of 63 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[497] _id=6ab5218a485cab4c9550277b ts=2026-09-24T13:11:38.7020000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[498] _id=6ab5218c485cab4c9550278f ts=2026-09-24T13:11:40.2550000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[630] _id=6ab52334485cab4c95507ec3 ts=2026-09-24T13:18:44.4150000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3595 | 0.0 | 0.037 | 312.539 | 1.868 | 345725.836 | 0.19 | 2079 | 9 |
| InputEvent | 2553 | 0.0 | 1.645 | 511.597 | 26.44 | 342957.71 | 0.12 | 111 | 13 |
| PlayerPositionEvent | 2292 | 4.469 | 10.0 | 566.722 | 10.03 | 342943.501 | 0.11 | 0 | 10 |
| DialogueEvent | 1730 | 0.0 | 4.669 | 755.057 | 53.185 | 343032.482 | 0.08 | 520 | 12 |
| argumentationNodeEvent | 249 | 0.018 | 0.45 | 5234.934 | 10.373 | 1036959.239 | 0.01 | 40 | 3 |
| ObjectInterEvent | 243 | 0.001 | 12.145 | 5372.207 | 1498.893 | 343032.508 | 0.01 | 3 | 18 |
| questEvent | 86 | 0.0 | 287.59 | 15188.869 | 84898.933 | 343382.084 | 0.0 | 19 | 22 |
| WaterChamberEvent | 71 | 0.218 | 7.504 | 119.111 | 74.397 | 7142.102 | 0.5 | 0 | 1 |
| TopographicMapEvent | 62 | 0.542 | 13.45 | 9753.109 | 84949.443 | 258812.601 | 0.01 | 0 | 7 |
| Soil Key Puzzle | 49 | 0.148 | 1.458 | 10581.945 | 51363.248 | 258816.677 | 0.01 | 0 | 4 |
| gameWindowFocusEvent | 35 | 0.5 | 485.195 | 37295.69 | 138302.566 | 344426.413 | 0.0 | 0 | 17 |
| DEBUGMenu | 28 | 6.876 | 1194.064 | 46616.13 | 198542.996 | 343843.668 | 0.0 | 0 | 19 |
| SolarStillDesignEvent | 23 | 0.467 | 1.365 | 1.696 | 4.329 | 4.683 | 35.38 | 0 | 0 |
| gameStartEvent | 22 | 91.893 | 5344.017 | 59334.053 | 250173.161 | 344426.413 | 0.0 | 0 | 15 |
| argumentationAnswerEvent | 16 | 5.903 | 20.607 | 76209.072 | 395718.475 | 1037033.091 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 15 | 0.0 | 490.701 | 81353.099 | 519249.002 | 520385.269 | 0.0 | 1 | 6 |
| soilMachine | 13 | 0.636 | 6.436 | 26528.731 | 137810.28 | 344111.1 | 0.0 | 0 | 1 |
| argumentationToolEvent | 11 | 0.684 | 1.724 | 110851.966 | 609656.106 | 1219215.84 | 0.0 | 0 | 1 |
| argumentationEvent | 8 | 0.029 | 93.15 | 152421.593 | 737693.15 | 1036957.388 | 0.0 | 1 | 2 |
| TerasGardenBox | 5 | 1.416 | 2.845 | 29.936 | 94.405 | 109.706 | 2.0 | 0 | 0 |
| chatEvent | 5 | 541.3 | 7063.493 | 36019.349 | 85783.616 | 85909.889 | 0.0 | 0 | 4 |
| DaniEvent | 3 | 1.93 | 3.218 | 33.257 | 85.483 | 94.624 | 1.8 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 1038491.983 | 1038491.983 | 1038491.983 | 1038491.983 | 1038491.983 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 6 group(s), 24 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[7556] _id=6ac39e92de269131f9a83cde ts=2026-10-05T12:56:49.7760000Z == 6aa413b141b41dbac0c7f1ee.jsonl[7557] _id=6ac39e92de269131f9a83ce0 ts=2026-10-05T12:56:49.7760000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[9517] _id=6ac64704de269131f9b8c3da ts=2026-10-07T13:20:04.3230000Z == 6aa413b141b41dbac0c7f1ee.jsonl[9518] _id=6ac64704de269131f9b8c3db ts=2026-10-07T13:20:04.3230000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[9525] _id=6ac64704de269131f9b8c3e2 ts=2026-10-07T13:20:04.3240000Z == 6aa413b141b41dbac0c7f1ee.jsonl[9526] _id=6ac64704de269131f9b8c3e3 ts=2026-10-07T13:20:04.3240000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 130 group(s), 190 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[708] _id=6ab523e9485cab4c9550a7a9 ts=2026-09-24T13:21:44.6380000Z == 6aa413b141b41dbac0c7f1ee.jsonl[696] _id=6ab523e9485cab4c9550a7ab ts=2026-09-24T13:21:44.6380000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[697] _id=6ab523e9485cab4c9550a7ba ts=2026-09-24T13:21:45.2480000Z == 6aa413b141b41dbac0c7f1ee.jsonl[716] _id=6ab523ea485cab4c9550a7c3 ts=2026-09-24T13:21:45.2480000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[727] _id=6ab523ee485cab4c9550a883 ts=2026-09-24T13:21:49.4160000Z == 6aa413b141b41dbac0c7f1ee.jsonl[728] _id=6ab523ee485cab4c9550a887 ts=2026-09-24T13:21:49.4160000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[5798] _id=6abd0e96485cab4c9587ecba ts=? == 6aa413b141b41dbac0c7f1ee.jsonl[6185] _id=6abe5a7e485cab4c95a42b06 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[10904] _id=6ac7bb18de269131f9c41f95 ts=2026-10-08T15:47:35.9880000Z == 6aa413b141b41dbac0c7f1ee.jsonl[10905] _id=6ac7bb18de269131f9c41f96 ts=2026-10-08T15:47:35.9880000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 42 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa413b141b41dbac0c7f1ee.jsonl[176] _id=6ab3d136485cab4c954bbbc0 ts=2026-09-23T13:16:38.9450000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[177] _id=6ab3d136485cab4c954bbbca ts=2026-09-23T13:16:38.9530000Z`; `189ms: 6aa413b141b41dbac0c7f1ee.jsonl[593] _id=6ab5232c485cab4c95507ce5 ts=2026-09-24T13:18:36.8920000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[583] _id=6ab5232d485cab4c95507cee ts=2026-09-24T13:18:37.0810000Z`; `163ms: 6aa413b141b41dbac0c7f1ee.jsonl[583] _id=6ab5232d485cab4c95507cee ts=2026-09-24T13:18:37.0810000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[596] _id=6ab5232d485cab4c95507cf7 ts=2026-09-24T13:18:37.2440000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 394 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `18ms: 6aa413b141b41dbac0c7f1ee.jsonl[733] _id=6ab523ef485cab4c9550a8a1 ts=2026-09-24T13:21:49.5150000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[734] _id=6ab523ef485cab4c9550a8a3 ts=2026-09-24T13:21:49.5330000Z`; `285ms: 6aa413b141b41dbac0c7f1ee.jsonl[780] _id=6ab5249d485cab4c9550d487 ts=2026-09-24T13:24:44.6710000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[781] _id=6ab5249d485cab4c9550d48b ts=2026-09-24T13:24:44.9560000Z`; `65ms: 6aa413b141b41dbac0c7f1ee.jsonl[781] _id=6ab5249d485cab4c9550d48b ts=2026-09-24T13:24:44.9560000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[782] _id=6ab5249d485cab4c9550d491 ts=2026-09-24T13:24:45.0210000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `891ms: 6aa413b141b41dbac0c7f1ee.jsonl[3479] _id=6aba6a93485cab4c9567eefd ts=2026-09-28T13:24:35.9550000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[3480] _id=6aba6a94485cab4c9567ef31 ts=2026-09-28T13:24:36.8460000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `794ms: 6aa413b141b41dbac0c7f1ee.jsonl[10163] _id=6ac64b18de269131f9b9a231 ts=2026-10-07T13:37:28.2020000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[10166] _id=6ac64b19de269131f9b9a25b ts=2026-10-07T13:37:28.9960000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6aa413b141b41dbac0c7f1ee.jsonl[9064] _id=6ac4f3c7de269131f9b027dd ts=2026-10-06T13:12:39.2080000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[9069] _id=6ac4f3c7de269131f9b027ed ts=2026-10-06T13:12:39.2370000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 45 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `449ms: 6aa413b141b41dbac0c7f1ee.jsonl[2480] _id=6aba64ec485cab4c95679901 ts=2026-09-23T13:41:07.229Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[2481] _id=6aba64ec485cab4c95679905 ts=2026-09-23T13:41:07.678Z`; `584ms: 6aa413b141b41dbac0c7f1ee.jsonl[2481] _id=6aba64ec485cab4c95679905 ts=2026-09-23T13:41:07.678Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[2207] _id=6aba64ec485cab4c95679907 ts=2026-09-23T13:41:08.262Z`; `90ms: 6aa413b141b41dbac0c7f1ee.jsonl[2207] _id=6aba64ec485cab4c95679907 ts=2026-09-23T13:41:08.262Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[2482] _id=6aba64ec485cab4c9567990b ts=2026-09-23T13:41:08.352Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `500ms: 6aa413b141b41dbac0c7f1ee.jsonl[6249] _id=6abe5b6a485cab4c95a44cbf ts=2026-10-01T13:08:58.4970000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[6255] _id=6abe5b6b485cab4c95a44cce ts=2026-10-01T13:08:58.9970000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `447ms: 6aa413b141b41dbac0c7f1ee.jsonl[5710] _id=6abd0c9b485cab4c9586fe63 ts=2026-09-30T13:20:27.4350000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[5712] _id=6abd0c9d485cab4c9586fefd ts=2026-09-30T13:20:27.8820000Z`; `0ms: 6aa413b141b41dbac0c7f1ee.jsonl[5712] _id=6abd0c9d485cab4c9586fefd ts=2026-09-30T13:20:27.8820000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[5713] _id=6abd0caa485cab4c958703fb ts=2026-09-30T13:20:27.882Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa413b141b41dbac0c7f1ee.jsonl[4997] _id=6abd0799485cab4c958675dd ts=2026-09-30T12:59:02.6080000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[4989] _id=6abd0799485cab4c958675df ts=2026-09-30T12:59:02.6120000Z`; `2ms: 6aa413b141b41dbac0c7f1ee.jsonl[11087] _id=6ac7bce4de269131f9c420f2 ts=2026-10-08T15:55:16.8000000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[11088] _id=6ac7bce4de269131f9c420f4 ts=2026-10-08T15:55:16.8020000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `636ms: 6aa413b141b41dbac0c7f1ee.jsonl[7430] _id=6abe6243485cab4c95a64af5 ts=2026-10-01T13:38:11.2700000Z ~ 6aa413b141b41dbac0c7f1ee.jsonl[7427] _id=6abe6243485cab4c95a64b17 ts=2026-10-01T13:38:11.9060000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 30m 
  - Evidence: 95h 30m: 6aa413b141b41dbac0c7f1ee.jsonl[6268] _id=6abe5f69485cab4c95a575a4 ts=2026-10-01T13:26:00.9400000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7547] _id=6ac39e8cde269131f9a83cd6 ts=2026-10-05T12:56:44.6080000Z; 71h 52m: 6aa413b141b41dbac0c7f1ee.jsonl[1312] _id=6ab671f6485cab4c95546c61 ts=2026-09-25T13:07:02.8150000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2468] _id=6aba64ee485cab4c95679941 ts=2026-09-28T13:00:00.8270000Z; 24h 4m: 6aa413b141b41dbac0c7f1ee.jsonl[2468] _id=6aba64ee485cab4c95679941 ts=2026-09-28T13:00:00.8270000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[3795] _id=6abbb766485cab4c957c1ce0 ts=2026-09-29T13:04:38.7920000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa413b141b41dbac0c7f1ee.jsonl[7534] _id=6abe62e5485cab4c95a67bc6 ts=2026-10-01T13:40:53.0830000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7586] _id=6ac39eddde269131f9a83dee ts=2026-10-05T12:58:05.5650000Z; 71h 43m: 6aa413b141b41dbac0c7f1ee.jsonl[2119] _id=6ab67542485cab4c9554b870 ts=2026-09-25T13:21:06.3140000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2534] _id=6aba65ee485cab4c9567a0dd ts=2026-09-28T13:04:46.0530000Z; 23h 44m: 6aa413b141b41dbac0c7f1ee.jsonl[929] _id=6ab524d3485cab4c9550df3d ts=2026-09-24T13:25:39.6570000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[1339] _id=6ab672a4485cab4c95547861 ts=2026-09-25T13:09:57.0260000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 520 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10804] _id=6ac7ba81de269131f9c41e17 ts=2026-10-08T15:45:06.1590000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10805] _id=6ac7ba81de269131f9c41e18 ts=2026-10-08T15:45:06.1590000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10821] _id=6ac7ba99de269131f9c41ee7 ts=2026-10-08T15:45:30.0400000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10822] _id=6ac7ba99de269131f9c41ee8 ts=2026-10-08T15:45:30.0400000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10889] _id=6ac7baf4de269131f9c41f5d ts=2026-10-08T15:47:00.4730000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10890] _id=6ac7baf4de269131f9c41f5e ts=2026-10-08T15:47:00.4730000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 288h 28m 
  - Evidence: 288h 28m: 6aa413b141b41dbac0c7f1ee.jsonl[486] _id=6ab5211c485cab4c95501fa7 ts=2026-09-24T13:09:48.0370000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[9472] _id=6ac4f9b8de269131f9b0fa04 ts=2026-10-06T13:38:00.0200000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 6aa413b141b41dbac0c7f1ee.jsonl[7526] _id=6abe62e4485cab4c95a67b92 ts=2026-10-01T13:40:52.0640000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7548] _id=6ac39e92de269131f9a83cda ts=2026-10-05T12:56:49.7740000Z; 71h 39m: 6aa413b141b41dbac0c7f1ee.jsonl[2066] _id=6ab67525485cab4c9554b5d4 ts=2026-09-25T13:20:37.4380000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2470] _id=6aba64ee485cab4c95679945 ts=2026-09-28T13:00:06.9660000Z; 23h 52m: 6aa413b141b41dbac0c7f1ee.jsonl[10557] _id=6ac6699bde269131f9bc307c ts=2026-10-07T15:47:39.4560000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10671] _id=6ac7b967de269131f9c41142 ts=2026-10-08T15:40:24.1120000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 111 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10307] _id=6ac64c18de269131f9b9d3be ts=2026-10-07T13:41:44.5630000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10308] _id=6ac64c18de269131f9b9d3bf ts=2026-10-07T13:41:44.5630000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10309] _id=6ac64c18de269131f9b9d3c0 ts=2026-10-07T13:41:44.5640000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10310] _id=6ac64c18de269131f9b9d3c1 ts=2026-10-07T13:41:44.5640000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10310] _id=6ac64c18de269131f9b9d3c1 ts=2026-10-07T13:41:44.5640000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10311] _id=6ac64c18de269131f9b9d3c2 ts=2026-10-07T13:41:44.5640000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa413b141b41dbac0c7f1ee.jsonl[7532] _id=6abe62e5485cab4c95a67bd3 ts=2026-10-01T13:40:53.0860000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7587] _id=6ac39eddde269131f9a83df2 ts=2026-10-05T12:58:05.5940000Z; 71h 46m: 6aa413b141b41dbac0c7f1ee.jsonl[2092] _id=6ab674f4485cab4c9554b0cd ts=2026-09-25T13:19:48.3650000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2562] _id=6aba6636485cab4c9567a215 ts=2026-09-28T13:05:58.3390000Z; 23h 56m: 6aa413b141b41dbac0c7f1ee.jsonl[10482] _id=6ac668dcde269131f9bc213e ts=2026-10-07T15:44:28.1090000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10702] _id=6ac7b99ade269131f9c414ae ts=2026-10-08T15:41:15.5110000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1ee.jsonl[8706] _id=6ac4f191de269131f9b00a3d ts=2026-10-06T13:03:12.7580000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8707] _id=6ac4f191de269131f9b00a41 ts=2026-10-06T13:03:12.7590000Z; 2ms: 6aa413b141b41dbac0c7f1ee.jsonl[8840] _id=6ac4f216de269131f9b01064 ts=2026-10-06T13:05:25.9440000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8837] _id=6ac4f216de269131f9b01068 ts=2026-10-06T13:05:25.9460000Z; 8ms: 6aa413b141b41dbac0c7f1ee.jsonl[176] _id=6ab3d136485cab4c954bbbc0 ts=2026-09-23T13:16:38.9450000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[177] _id=6ab3d136485cab4c954bbbca ts=2026-09-23T13:16:38.9530000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 15m 
  - Evidence: 95h 15m: 6aa413b141b41dbac0c7f1ee.jsonl[7481] _id=6abe62ed485cab4c95a67dae ts=2026-10-01T13:41:01.1130000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7555] _id=6ac39e92de269131f9a83cd8 ts=2026-10-05T12:56:44.6140000Z; 71h 28m: 6aa413b141b41dbac0c7f1ee.jsonl[2185] _id=6ab677c5485cab4c955512d2 ts=2026-09-25T13:31:49.6050000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2469] _id=6aba64ee485cab4c95679943 ts=2026-09-28T13:00:00.8420000Z; 23h 39m: 6aa413b141b41dbac0c7f1ee.jsonl[9505] _id=6ac4fa31de269131f9b10f6e ts=2026-10-06T13:40:01.7760000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[9515] _id=6ac64704de269131f9b8c3d8 ts=2026-10-07T13:19:59.3940000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa413b141b41dbac0c7f1ee.jsonl[7115] _id=6abe5f4c485cab4c95a56bbc ts=2026-10-01T13:25:30.2270000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8275] _id=6ac3a5c9de269131f9a90885 ts=2026-10-05T13:27:36.0630000Z; 71h 48m: 6aa413b141b41dbac0c7f1ee.jsonl[2052] _id=6ab674a0485cab4c9554a883 ts=2026-09-25T13:18:24.0840000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2579] _id=6aba6662485cab4c9567a2fb ts=2026-09-28T13:06:42.0740000Z; 24h 14m: 6aa413b141b41dbac0c7f1ee.jsonl[5463] _id=6abd0990485cab4c958693b3 ts=2026-09-30T13:07:27.3060000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[6516] _id=6abe5e6e485cab4c95a50aa4 ts=2026-10-01T13:21:50.0510000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2079 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[1004] _id=6ab52530485cab4c9550f4e5 ts=2026-09-24T13:27:09.6200000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[1005] _id=6ab52530485cab4c9550f4ea ts=2026-09-24T13:27:09.6200000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[1027] _id=6ab524f0485cab4c9550e503 ts=2026-09-24T13:26:07.4100000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[1019] _id=6ab524f0485cab4c9550e509 ts=2026-09-24T13:26:07.4100000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[1083] _id=6ab52501485cab4c9550e92f ts=2026-09-24T13:26:23.9020000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[1099] _id=6ab52501485cab4c9550e937 ts=2026-09-24T13:26:23.9020000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 53m 
  - Evidence: 71h 53m: 6aa413b141b41dbac0c7f1ee.jsonl[2091] _id=6ab674f7485cab4c9554b11c ts=2026-09-25T13:19:51.3670000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2507] _id=6aba67f8485cab4c9567bacb ts=2026-09-28T13:13:28.0440000Z; 48h 11m: 6aa413b141b41dbac0c7f1ee.jsonl[3916] _id=6abbb8a5485cab4c957c33f4 ts=2026-09-29T13:09:57.9520000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[6479] _id=6abe5e50485cab4c95a4f835 ts=2026-10-01T13:21:19.9830000Z; 23h 29m: 6aa413b141b41dbac0c7f1ee.jsonl[3728] _id=6aba6e3a485cab4c956816e9 ts=2026-09-28T13:40:10.0430000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[3897] _id=6abbb88e485cab4c957c2f5a ts=2026-09-29T13:09:34.6980000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 53m 
  - Evidence: 71h 53m: 6aa413b141b41dbac0c7f1ee.jsonl[1403] _id=6ab67383485cab4c95548a79 ts=2026-09-25T13:13:39.2160000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2621] _id=6aba6680485cab4c9567a3c3 ts=2026-09-28T13:07:11.8170000Z; 24h 6m: 6aa413b141b41dbac0c7f1ee.jsonl[3633] _id=6aba6cfc485cab4c956809c9 ts=2026-09-28T13:34:52.8670000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[4978] _id=6abbc014485cab4c957da638 ts=2026-09-29T13:41:40.5840000Z; 23h 48m: 6aa413b141b41dbac0c7f1ee.jsonl[807] _id=6ab524a9485cab4c9550d699 ts=2026-09-24T13:24:57.2180000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[1396] _id=6ab6736a485cab4c9554882b ts=2026-09-25T13:13:14.1150000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 59m 
  - Evidence: 1h 59m: 6aa413b141b41dbac0c7f1ee.jsonl[10285] _id=6ac64be4de269131f9b9cbc3 ts=2026-10-07T13:40:52.6950000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10336] _id=6ac667cade269131f9bc0c9a ts=2026-10-07T15:39:54.7970000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 288h 3m 
  - Evidence: 288h 3m: 6aa413b141b41dbac0c7f1ee.jsonl[371] _id=6ab52045485cab4c95501727 ts=2026-09-24T13:06:13.2630000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8962] _id=6ac4f32ede269131f9b02133 ts=2026-10-06T13:10:06.3540000Z; 50h 32m: 6aa413b141b41dbac0c7f1ee.jsonl[9063] _id=6ac4f3c7de269131f9b027d9 ts=2026-10-06T13:12:39.1880000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10803] _id=6ac7ba81de269131f9c41e13 ts=2026-10-08T15:45:06.1240000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 288h 2m 
  - Evidence: 288h 2m: 6aa413b141b41dbac0c7f1ee.jsonl[375] _id=6ab52045485cab4c95501729 ts=2026-09-24T13:06:13.3000000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8916] _id=6ac4f2e2de269131f9b01e24 ts=2026-10-06T13:08:50.6880000Z; 50h 31m: 6aa413b141b41dbac0c7f1ee.jsonl[9069] _id=6ac4f3c7de269131f9b027ed ts=2026-10-06T13:12:39.2370000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10774] _id=6ac7ba63de269131f9c41ce4 ts=2026-10-08T15:44:35.9460000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.029s..0.029s shown 
  - Evidence: 29ms: 6aa413b141b41dbac0c7f1ee.jsonl[9064] _id=6ac4f3c7de269131f9b027dd ts=2026-10-06T13:12:39.2080000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[9069] _id=6ac4f3c7de269131f9b027ed ts=2026-10-06T13:12:39.2370000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 288h 2m 
  - Evidence: 288h 2m: 6aa413b141b41dbac0c7f1ee.jsonl[313] _id=6ab5203c485cab4c95501703 ts=2026-09-24T13:06:04.5330000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8903] _id=6ac4f2dbde269131f9b01db6 ts=2026-10-06T13:08:43.7720000Z; 50h 32m: 6aa413b141b41dbac0c7f1ee.jsonl[9059] _id=6ac4f3b3de269131f9b026c7 ts=2026-10-06T13:12:19.1380000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10786] _id=6ac7ba6cde269131f9c41d21 ts=2026-10-08T15:44:44.7590000Z; 23h 21m: 6aa413b141b41dbac0c7f1ee.jsonl[2464] _id=6aba64ed485cab4c95679931 ts=2026-09-23T13:41:21.465Z -> 6aa413b141b41dbac0c7f1ee.jsonl[264] _id=6ab51f6b485cab4c9550030b ts=2026-09-24T13:02:35.6480000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 40 interval(s) ≤ 0.018s..0.021s shown 
  - Evidence: 18ms: 6aa413b141b41dbac0c7f1ee.jsonl[208] _id=6ab51fb2485cab4c955009c9 ts=2026-09-24T13:03:46.6800000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[214] _id=6ab51fb2485cab4c955009cf ts=2026-09-24T13:03:46.6980000Z; 20ms: 6aa413b141b41dbac0c7f1ee.jsonl[340] _id=6ab5201a485cab4c95501531 ts=2026-09-24T13:05:30.5000000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[342] _id=6ab5201a485cab4c95501533 ts=2026-09-24T13:05:30.5200000Z; 21ms: 6aa413b141b41dbac0c7f1ee.jsonl[8981] _id=6ac4f33fde269131f9b021be ts=2026-10-06T13:10:23.1480000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8982] _id=6ac4f33fde269131f9b021c0 ts=2026-10-06T13:10:23.1690000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 338h 40m 
  - Evidence: 338h 40m: 6aa413b141b41dbac0c7f1ee.jsonl[359] _id=6ab52034485cab4c955016af ts=2026-09-24T13:05:56.6800000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10860] _id=6ac7bac4de269131f9c41f31 ts=2026-10-08T15:46:12.5200000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 23h 51m 
  - Evidence: 23h 51m: 6aa413b141b41dbac0c7f1ee.jsonl[10572] _id=6ac669cbde269131f9bc325d ts=2026-10-07T15:48:27.5140000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10669] _id=6ac7b960de269131f9c41108 ts=2026-10-08T15:40:17.4030000Z; 23h 41m: 6aa413b141b41dbac0c7f1ee.jsonl[9480] _id=6ac4f9e0de269131f9b0fdf7 ts=2026-10-06T13:38:40.6560000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[9510] _id=6ac646ffde269131f9b8c3a1 ts=2026-10-07T13:19:59.1780000Z; 1h 57m: 6aa413b141b41dbac0c7f1ee.jsonl[10305] _id=6ac64c16de269131f9b9d38e ts=2026-10-07T13:41:42.7210000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10320] _id=6ac667aede269131f9bc0b08 ts=2026-10-07T15:39:26.2140000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 6aa413b141b41dbac0c7f1ee.jsonl[6410] _id=6abe5ce9485cab4c95a49157 ts=2026-10-01T13:15:20.8450000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7546] _id=6ac39e53de269131f9a83cd4 ts=2026-10-05T12:55:47.2580000Z; 71h 52m: 6aa413b141b41dbac0c7f1ee.jsonl[1310] _id=6ab671ef485cab4c95546c2f ts=2026-09-25T13:06:55.8340000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2497] _id=6aba64ee485cab4c9567993f ts=2026-09-28T12:59:54.4250000Z; 24h 4m: 6aa413b141b41dbac0c7f1ee.jsonl[7546] _id=6ac39e53de269131f9a83cd4 ts=2026-10-05T12:55:47.2580000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8577] _id=6ac4f0e1de269131f9b00059 ts=2026-10-06T13:00:17.2510000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 40m 
  - Evidence: 95h 40m: 6aa413b141b41dbac0c7f1ee.jsonl[6411] _id=6abe5ce8485cab4c95a4914f ts=2026-10-01T13:15:20.8440000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7545] _id=6ac39e53de269131f9a83cd2 ts=2026-10-05T12:55:47.2570000Z; 71h 52m: 6aa413b141b41dbac0c7f1ee.jsonl[1311] _id=6ab671ef485cab4c95546c2d ts=2026-09-25T13:06:55.8330000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2496] _id=6aba64ee485cab4c9567993d ts=2026-09-28T12:59:54.4040000Z; 24h 4m: 6aa413b141b41dbac0c7f1ee.jsonl[7545] _id=6ac39e53de269131f9a83cd2 ts=2026-10-05T12:55:47.2570000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[8572] _id=6ac4f0e1de269131f9b00055 ts=2026-10-06T13:00:17.2500000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 144h 33m 
  - Evidence: 144h 33m: 6aa413b141b41dbac0c7f1ee.jsonl[6244] _id=6abe5b6c485cab4c95a44d11 ts=2026-10-01T13:09:00.5110000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10318] _id=6ac64c2dde269131f9b9d62a ts=2026-10-07T13:42:05.7800000Z; 144h 6m: 6aa413b141b41dbac0c7f1ee.jsonl[537] _id=6ab52231485cab4c955049d5 ts=2026-09-24T13:14:25.4040000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[5710] _id=6abd0c9b485cab4c9586fe63 ts=2026-09-30T13:20:27.4350000Z; 23h 44m: 6aa413b141b41dbac0c7f1ee.jsonl[2311] _id=6aba64e0485cab4c95679749 ts=2026-09-23T13:30:13.13Z -> 6aa413b141b41dbac0c7f1ee.jsonl[537] _id=6ab52231485cab4c955049d5 ts=2026-09-24T13:14:25.4040000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[5712] _id=6abd0c9d485cab4c9586fefd ts=2026-09-30T13:20:27.8820000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[5713] _id=6abd0caa485cab4c958703fb ts=2026-09-30T13:20:27.882Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa413b141b41dbac0c7f1ee.jsonl[7324] _id=6abe613b485cab4c95a5fef0 ts=2026-10-01T13:33:47.7670000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7575] _id=6ac39e93de269131f9a83cfe ts=2026-10-05T12:56:49.8510000Z; 71h 39m: 6aa413b141b41dbac0c7f1ee.jsonl[2111] _id=6ab6752b485cab4c9554b65a ts=2026-09-25T13:20:43.3230000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[2487] _id=6aba64ee485cab4c95679949 ts=2026-09-28T13:00:07.0090000Z; 23h 41m: 6aa413b141b41dbac0c7f1ee.jsonl[9476] _id=6ac4f9e2de269131f9b0fe3f ts=2026-10-06T13:38:41.9210000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[9531] _id=6ac64704de269131f9b8c3e8 ts=2026-10-07T13:20:04.3450000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10058] _id=6ac64a12de269131f9b96505 ts=2026-10-07T13:33:06.8570000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10059] _id=6ac64a12de269131f9b96506 ts=2026-10-07T13:33:06.8570000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10485] _id=6ac668e1de269131f9bc219c ts=2026-10-07T15:44:33.7800000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10486] _id=6ac668e1de269131f9bc219d ts=2026-10-07T15:44:33.7800000Z; 0ms: 6aa413b141b41dbac0c7f1ee.jsonl[10904] _id=6ac7bb18de269131f9c41f95 ts=2026-10-08T15:47:35.9880000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[10905] _id=6ac7bb18de269131f9c41f96 ts=2026-10-08T15:47:35.9880000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa413b141b41dbac0c7f1ee.jsonl[7442] _id=6abe6262485cab4c95a65453 ts=2026-10-01T13:38:42.8410000Z -> 6aa413b141b41dbac0c7f1ee.jsonl[7893] _id=6ac3a291de269131f9a87548 ts=2026-10-05T13:13:53.9410000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2190] _id=6aba64cf485cab4c9567968d ts=2026-09-23T13:23:01.626Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2291] _id=6aba64dc485cab4c956796fd ts=2026-09-23T13:27:28.521Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2297] _id=6aba64e1485cab4c9567977b ts=2026-09-23T13:31:57.259Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 47 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[817] _id=6ab524ea485cab4c9550e370 ts=2026-09-24T13:26:01.8120000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[1022] _id=6ab524f0485cab4c9550e4c4 ts=2026-09-24T13:26:07.0400000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[1051] _id=6ab524f7485cab4c9550e6c9 ts=2026-09-24T13:26:14.4200000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 191 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[734] _id=6ab523ef485cab4c9550a8a3 ts=2026-09-24T13:21:49.5330000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[737] _id=6ab523ef485cab4c9550a8a5 ts=2026-09-24T13:21:49.5330000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[839] _id=6ab524c1485cab4c9550db8b ts=2026-09-24T13:21:52.9890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[9069] _id=6ac4f3c7de269131f9b027ed ts=2026-10-06T13:12:39.2370000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 20 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2480] _id=6aba64ec485cab4c95679901 ts=2026-09-23T13:41:07.229Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2481] _id=6aba64ec485cab4c95679905 ts=2026-09-23T13:41:07.678Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2207] _id=6aba64ec485cab4c95679907 ts=2026-09-23T13:41:08.262Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[9480] _id=6ac4f9e0de269131f9b0fdf7 ts=2026-10-06T13:38:40.6560000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[9510] _id=6ac646ffde269131f9b8c3a1 ts=2026-10-07T13:19:59.1780000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[10305] _id=6ac64c16de269131f9b9d38e ts=2026-10-07T13:41:42.7210000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2197] _id=6aba64cc485cab4c95679661 ts=2026-09-23T13:22:03.651Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2289] _id=6aba64dc485cab4c956796f7 ts=2026-09-23T13:27:22.472Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2437] _id=6aba64eb485cab4c956798e7 ts=2026-09-23T13:40:30.47Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[5748] _id=6abd0dca485cab4c958790b5 ts=?`; `6aa413b141b41dbac0c7f1ee.jsonl[5798] _id=6abd0e96485cab4c9587ecba ts=?`; `6aa413b141b41dbac0c7f1ee.jsonl[6185] _id=6abe5a7e485cab4c95a42b06 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 338 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[996] _id=6ab524eb485cab4c9550e3c4 ts=2026-09-24T13:26:03.1190000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[1016] _id=6ab524ee485cab4c9550e471 ts=2026-09-24T13:26:06.0570000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[1059] _id=6ab524fb485cab4c9550e7b5 ts=2026-09-24T13:26:19.3250000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 771 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[696] _id=6ab523e9485cab4c9550a7ab ts=2026-09-24T13:21:44.6380000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[712] _id=6ab523e9485cab4c9550a7b3 ts=2026-09-24T13:21:44.6380000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[713] _id=6ab523e9485cab4c9550a7b5 ts=2026-09-24T13:21:44.6380000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[5678] _id=6abd0c12485cab4c9586d7f5 ts=2026-09-30T13:18:10.4710000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[5897] _id=6abd1073485cab4c9588b4e1 ts=2026-09-30T13:36:51.4710000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[5902] _id=6abd10a4485cab4c9588c317 ts=2026-09-30T13:37:40.2530000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[332] _id=6ab52012485cab4c95501467 ts=2026-09-24T13:05:22.3750000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[361] _id=6ab52032485cab4c9550169f ts=2026-09-24T13:05:54.9560000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[10861] _id=6ac7bac5de269131f9c41f33 ts=2026-10-08T15:46:13.8890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 330 start, 321 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 89 unmatched 'BecameCameraCentered' (totals: 600 open, 558 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 91 unmatched 'BecameVisible' (totals: 1169 open, 1269 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 20 open, 19 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 8 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 27 unmatched 'questActiveEvent' (totals: 55 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 220 of 11148 adjacent _id pairs reverse in client time; worst 173624.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1ee.jsonl[2185] _id=6ab677c5485cab4c955512d2 ts=2026-09-25T13:31:49.6050000Z`; `6aa413b141b41dbac0c7f1ee.jsonl[2194] _id=6aba64ca485cab4c95679639 ts=2026-09-23T13:18:05.455Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.06s, min -430909.30s, max +0.80s over 11149 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1ee\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3596 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2656); Unit 4 Dev (628); Unit 5 Dev - Dungeon (312)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.87s, n=3595)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3596/3596 records)
    "BecameInvisible"  x1269
    "BecameVisible"  x1169
    "BecameCameraCentered"  x600
    "BecameCameraUncentered"  x558
data.pieceId  (string, 3596/3596 records)
    35 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3596/3596 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2554 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (587); Unit 4 Dev - Dungeon (577); Unit 3 Dev (394); Unit 5 Dev - Dungeon (349); Unit 4 Dev - Anderson Base (223); Unit 4 Dev (172); Unit 1 Dev (160); Unit 5 Dev (92)
- **Intervals:** median 1.65s (p5 0.08s / p95 26.44s, n=2553)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2554/2554 records)
    "pressed"  x2554
data.actionType  (string, 2554/2554 records)
    "Move"  x1747
    "Interact"  x543
    "Jump"  x129
    "Sprint"  x53
    "Hoverboard"  x41
    "Ascend"  x23
    "Map"  x14
    "Pause"  x3
    "SkipCinematic"  x1
data.key  (string, 2554/2554 records)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2554/2554 records)
    "Player"  x2331
    "Drone"  x223
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2304 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (888); Unit 4 Dev (288); Unit 4 Dev - Dungeon (272); Unit 1 Dev (268); Unit 5 Dev - Dungeon (191); Unit 5 Dev (176); Unit 3 Dev (141); Unit 4 Dev - Anderson Base (80)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2292)
- **Fields under `data`:**

```text
data.position  (object, 2304/2304 records)
data.position.x  (number, 2304/2304 records)
    numeric range -336.71 .. 1556.88 (671 unique)
data.position.y  (number, 2304/2304 records)
    numeric range -90.1168 .. 222.252 (432 unique)
data.position.z  (number, 2304/2304 records)
    numeric range -721.177 .. 2142.59 (675 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1731 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (639); Unit 4 Dev (276); Unit 5 Dev (217); Unit 1 Dev (206); Unit 4 Dev - Dungeon (149); Unit 5 Dev - Dungeon (112); Unit 4 Dev - Anderson Base (90); Unit 3 Dev (42)
- **eventKey:** present on 1080 of 1731 records
- **Intervals:** median 4.67s (p5 0.00s / p95 53.18s, n=1730)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1080; [conversationId, dialogueEventType] x651
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1731/1731 records)
    numeric range 8 .. 118 (40 unique)
data.dialogueEventType  (string, 1731/1731 records)
    "DialogueNodeEvent"  x1080
    "DialogueStartEvent"  x330
    "DialogueFinishEvent"  x321
data.nodeId  (number, 1080/1731 records)
    numeric range 0 .. 290 (169 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 250 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (109); Unit 1 Dev (89); Unit 5 Dev (52)
- **Intervals:** median 0.45s (p5 0.03s / p95 10.37s, n=249)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 250/250 records)
    "argumentationNodeHoverEnd"  x124
    "argumentationNodeHoverStart"  x104
    "argumentationNodeAdd"  x17
    "argumentationNodeRemove"  x5
data.argumentationTitle  (string, 250/250 records)
    "Unit 4 - Flooding"  x109
    "Unit 5"  x52
    "Unit 1 - Freshwater"  x47
    "Unit 1 - Argumentation Tutorial"  x42
data.nodeName  (string, 250/250 records)
    "1"  x40
    "A"  x35
    "D"  x30
    "I"  x29
    "II"  x26
    "B"  x24
    "C"  x24
    "4"  x18
    "2"  x15
    "3"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 244 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (95); Unit 2 Prod (Refactor) (78); Unit 5 Dev - Dungeon (17); Unit 4 Dev (16); Unit 5 Dev (15); Unit 1 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 3 Dev (2)
- **Intervals:** median 12.14s (p5 0.16s / p95 1498.89s, n=243)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 244/244 records)
    35 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 244/244 records)
    85 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 87 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 1 Dev (15); Unit 5 Dev - Dungeon (13); Unit 4 Dev - Dungeon (12); Unit 4 Dev (8); Unit 5 Dev (8); Unit 3 Dev (6); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 87 of 87 records
- **Intervals:** median 287.59s (p5 0.00s / p95 84898.93s, n=86)
- **`data` key-set variants:** [questEventType, questID, questName] x55; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 87/87 records)
    "questActiveEvent"  x55
    "questFinishEvent"  x32
data.questID  (string, 87/87 records)
    28 unique values (see csv/event_unique_values.csv)
data.questName  (string, 87/87 records)
    28 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/87 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 72 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (72)
- **Intervals:** median 7.50s (p5 0.73s / p95 74.40s, n=71)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 72/72 records)
    "On"  x43
    "Off"  x29
data.floor  (string, 72/72 records)
    "3"  x49
    "4"  x11
    "1"  x7
    "2"  x5
data.machineNumber  (string, 72/72 records)
    "One"  x70
    "Two"  x2
data.machineType  (string, 72/72 records)
    "Condenser"  x29
    "DualChamber_Condenser"  x19
    "Evaporator"  x11
    "DualChamber_Evaporator"  x9
    "VentSwitch"  x4
data.room  (string, 72/72 records)
    "2"  x45
    "1"  x13
    "3"  x8
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TopographicMapEvent` — 63 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (50); Unit 3 Dev (13)
- **Intervals:** median 13.45s (p5 0.84s / p95 84949.44s, n=62)
- **`data` key-set variants:** [actionType, featureUsed] x39; [actionType, featureUsed, location] x17; [actionType, featureUsed, legendName] x7
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 63/63 records)
    "MapOpenEvent"  x20
    "MapCloseEvent"  x19
    "WaypointMoveEvent"  x13
    "Selected"  x6
    "WaypointSetEvent"  x4
    "Unselected"  x1
data.featureUsed  (string, 63/63 records)
    "Map"  x39
    "Waypoint"  x17
    "Legend"  x7
data.legendName  (string, 7/63 records)
    "90 ft"  x3
    "0 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
    "Water"  x1
data.location  (object, 17/63 records)
data.location.x  (number, 17/63 records)
    numeric range -376.09 .. 207.91 (14 unique)
data.location.y  (number, 17/63 records)
    numeric range -279.5 .. 113.5 (14 unique)
data.location.z  (number, 17/63 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 50 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (38); Unit 4 Dev (12)
- **Intervals:** median 1.46s (p5 0.19s / p95 51363.25s, n=49)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x40; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/50 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/50 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 4 Dev"  x2
data.actionType  (string, 40/50 records)
    "RightDrag"  x24
    "LeftDrag"  x16
data.currentSoilType  (string, 40/50 records)
    "SAND"  x11
    "CLAYSAND"  x8
    "SANDGRAVEL"  x7
    "CLAY"  x6
    "CLAYROCK"  x5
    "GRAVEL"  x2
    "BEDROCK"  x1
data.isCorrectSelection  (string, 40/50 records)
    "false"  x28
    "true"  x12
data.waterLevelStatus  (string, 40/50 records)
    "Proper"  x18
    "TooHigh"  x17
    "TooLow"  x5
data.waterRetentionChange  (string, 40/50 records)
    "Increase"  x17
    "NoChange"  x12
    "Decrease"  x11
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 36 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (24); Unit 3 Dev (5); Unit 1 Dev (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev (1)
- **Intervals:** median 485.19s (p5 2.07s / p95 138302.57s, n=35)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 36/36 records)
    true  x36
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (6); MainMenu (3); Unit 4 Dev (3); Unit 5 Dev - Dungeon (3); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 1194.06s (p5 50.04s / p95 198543.00s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `SolarStillDesignEvent` — 24 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (24)
- **Intervals:** median 1.36s (p5 0.59s / p95 4.33s, n=23)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x23; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "optionSelected"  x23
    "DesignSubmitted"  x1
data.designSelections  (object, 1/24 records)
data.designSelections.glassRoofTemperature  (string, 1/24 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/24 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/24 records)
    "Tilted Out"  x1
data.featureUsed  (string, 24/24 records)
    "RoofStyle"  x11
    "GlassRoofTemperature"  x8
    "ExtraCovering"  x4
    "Submit"  x1
data.selectedOption  (string, 23/24 records, 3 empty-string)
    "Tilted Out"  x5
    "Hot"  x4
    ""  x3
    "Cold"  x3
    "Covered"  x2
    "Flat"  x2
    "Tilted In"  x2
    "Uncovered"  x2
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 5344.02s (p5 98.04s / p95 250173.16s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 17 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (7); Unit 1 Dev (6); Unit 5 Dev (4)
- **Intervals:** median 20.61s (p5 6.67s / p95 395718.47s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "submitAnswerEvent"  x17
data.answerSubmitted  (string, 17/17 records, 3 empty-string)
    ""  x3
    "A,1,I"  x2
    "C,D,2,II"  x2
    "C,D,3,II"  x2
    "C,D,A,2,II"  x2
    "C,D,B,2,II"  x2
    "A,1,"  x1
    "C,2,II"  x1
    "C,D,4,3,II"  x1
    "D,C,4,II"  x1
data.argumentationTitle  (string, 17/17 records)
    "Unit 4 - Flooding"  x7
    "Unit 1 - Freshwater"  x5
    "Unit 5"  x4
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 16 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (5); Unit 1 Dev (4); Unit 2 Prod (Refactor) (4); Unit 5 Dev (2); MainMenu (1)
- **Intervals:** median 490.70s (p5 0.31s / p95 519249.00s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    false  x16
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 14 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (14)
- **Intervals:** median 6.44s (p5 1.12s / p95 137810.28s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "ChangeCanister"  x14
data.canisterType  (string, 14/14 records)
    "Sand"  x5
    "Clay"  x4
    "Bedrock"  x3
    "Gravel"  x2
data.floor  (string, 14/14 records)
    "5"  x6
    "2"  x5
    "4"  x2
    "3"  x1
data.machine  (string, 14/14 records)
    "1"  x12
    "2"  x2
data.row  (string, 14/14 records)
    "TopRow"  x11
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 5 Dev (5)
- **Intervals:** median 1.72s (p5 0.70s / p95 609656.11s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x8
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Freshwater"  x5
    "Unit 5"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Heat Added/Released Chart"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 93.15s (p5 11.90s / p95 737693.15s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 9/9 records)
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.85s (p5 1.64s / p95 94.41s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (3)
- **Intervals:** median 7063.49s (p5 693.75s / p95 85783.62s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x6
data.chatID  (string, 6/6 records)
    "NA"  x6
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 3.22s (p5 2.06s / p95 85.48s, n=3)
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
    "unit3"  x2
    "unit2"  x1
    "unit5"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 1038491.98s (p5 1038491.98s / p95 1038491.98s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "4"  x1
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
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (38 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (6x); "Unselected" (1x); "WaypointMoveEvent" (13x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (7x); "Waypoint" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (5x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*