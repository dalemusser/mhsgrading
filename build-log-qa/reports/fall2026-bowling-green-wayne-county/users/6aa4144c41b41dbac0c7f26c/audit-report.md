# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26c
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f26c.jsonl
- **Records:** 14692 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f26c
- **Time span:** 2026-09-23T18:15:44.792000+00:00 .. 2026-10-07T15:01:02.663000+00:00 (332h 45m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 14692 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 106 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5167 | 35.17 | 1 | 8 | 0 | 2026-09-23T18:16:01.294000+00:00 | 2026-10-07T15:01:02.663000+00:00 | 332h 45m |
| PuzzlePieceVisibleEvent | 3032 | 20.64 | 1 | 4 | 0 | 2026-09-24T17:57:52.633000+00:00 | 2026-10-06T18:42:20.550000+00:00 | 288h 44m |
| PlayerPositionEvent | 2920 | 19.87 | 1 | 8 | 0 | 2026-09-23T18:15:56.195000+00:00 | 2026-10-07T15:00:54.756000+00:00 | 332h 44m |
| DialogueEvent | 2297 | 15.63 | 1 | 8 | 1386 | 2026-09-23T18:16:17.849000+00:00 | 2026-10-07T15:00:41.239000+00:00 | 332h 44m |
| argumentationNodeEvent | 335 | 2.28 | 1 | 4 | 0 | 2026-09-24T17:46:45.682000+00:00 | 2026-10-06T19:16:08.728000+00:00 | 289h 29m |
| ObjectInterEvent | 327 | 2.23 | 1 | 8 | 0 | 2026-09-23T18:24:09.781000+00:00 | 2026-10-07T15:01:02.663000+00:00 | 332h 36m |
| TopographicMapEvent | 117 | 0.8 | 1 | 3 | 0 | 2026-09-24T17:58:48.526000+00:00 | 2026-10-06T18:54:39.362000+00:00 | 288h 55m |
| questEvent | 96 | 0.65 | 1 | 8 | 96 | 2026-09-23T18:16:17.828000+00:00 | 2026-10-07T14:56:08.510000+00:00 | 332h 39m |
| Soil Key Puzzle | 60 | 0.41 | 1 | 3 | 0 | 2026-09-24T18:04:16.284000+00:00 | 2026-10-06T11:28:39.743000+00:00 | 281h 24m |
| gameWindowFocusEvent | 60 | 0.41 | 1 | 9 | 0 | 2026-09-23T18:15:44.792000+00:00 | 2026-10-07T14:47:41+00:00 | 332h 31m |
| argumentationAnswerEvent | 52 | 0.35 | 1 | 4 | 0 | 2026-09-24T17:48:15.127000+00:00 | 2026-10-06T19:16:14.341000+00:00 | 289h 27m |
| WaterChamberEvent | 50 | 0.34 | 1 | 1 | 0 | 2026-10-06T18:40:58.590000+00:00 | 2026-10-06T19:04:12.216000+00:00 | 23m 13s |
| gameWindowUnfocusEvent | 43 | 0.29 | 1 | 8 | 0 | 2026-09-23T18:17:05.952000+00:00 | 2026-10-07T14:47:26.370000+00:00 | 332h 30m |
| DEBUGMenu | 24 | 0.16 | 1 | 8 | 0 | 2026-09-23T18:15:56.190000+00:00 | 2026-10-07T14:47:40.943000+00:00 | 332h 31m |
| gameStartEvent | 23 | 0.16 | 1 | 1 | 0 | 2026-09-23T18:15:44.793000+00:00 | 2026-10-07T14:47:41+00:00 | 332h 31m |
| SolarStillDesignEvent | 20 | 0.14 | 1 | 1 | 0 | 2026-10-07T14:44:52.840000+00:00 | 2026-10-07T14:53:28.009000+00:00 | 8m 35s |
| soilMachine | 19 | 0.13 | 1 | 1 | 0 | 2026-10-06T18:17:09.876000+00:00 | 2026-10-06T18:31:28.724000+00:00 | 14m 18s |
| chatEvent | 16 | 0.11 | 1 | 4 | 0 | 2026-09-24T17:53:49.625000+00:00 | 2026-10-07T14:47:57.738000+00:00 | 308h 54m |
| DaniEvent | 12 | 0.08 | 1 | 2 | 0 | 2026-09-24T17:53:47.730000+00:00 | 2026-10-05T20:04:17.118000+00:00 | 266h 10m |
| argumentationEvent | 11 | 0.07 | 1 | 4 | 0 | 2026-09-24T17:46:29.426000+00:00 | 2026-10-06T19:16:14.366000+00:00 | 289h 29m |
| argumentationToolEvent | 5 | 0.03 | 1 | 3 | 0 | 2026-09-24T17:46:23.341000+00:00 | 2026-10-05T18:23:43.855000+00:00 | 264h 37m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-24T17:51:51.325000+00:00 | 2026-10-07T15:01:02.631000+00:00 | 309h 9m |
| crash | 2 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 10481.65s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 437421.532s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.656s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 1.096s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 218674.559s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 5.3s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 15050.705s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 345.611s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 256.007s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 4 Dev - Anderson Base 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E To Place Cameras; Press E To Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.4x vs baseline. 
  - Observed: 52 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,II; A,2,I; A,3,I; A,4,I; A,B,1,II; A,D,1,II; C,D,3,II; D,C,3,4,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 - Flooding 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 8.0x vs baseline. 
  - Observed: 16 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [16-3]; [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 56 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Desert Delicacies; Power Play; Saving Cadet Anderson 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 43 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[267] _id=6ab419cc485cab4c954f4ab8 ts=2026-09-23T18:26:20.1360000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[357] _id=6ab41acf485cab4c954f5268 ts=2026-09-23T18:30:39.5460000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[431] _id=6ab41b85485cab4c954f5790 ts=2026-09-23T18:33:41.4970000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[4167] _id=6abbffdd485cab4c9584270b ts=2026-09-29T18:13:46.9850000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[13613] _id=6ac5452dde269131f9b72379 ts=2026-10-06T18:59:56.9980000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[22] _id=6ab41750485cab4c954f36ae ts=2026-09-23T18:15:44.7930000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[63] _id=6ab417b2485cab4c954f38f4 ts=2026-09-23T18:17:21.8760000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[45] _id=6ab417c6485cab4c954f3942 ts=2026-09-23T18:17:42.3480000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 60 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 60} 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[21] _id=6ab41750485cab4c954f36ac ts=2026-09-23T18:15:44.7920000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[53] _id=6ab417a2485cab4c954f38a2 ts=2026-09-23T18:17:06.3020000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[59] _id=6ab417a2485cab4c954f38a6 ts=2026-09-23T18:17:06.3710000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 43 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 43} 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[48] _id=6ab417a1485cab4c954f389e ts=2026-09-23T18:17:05.9520000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[54] _id=6ab417a2485cab4c954f38a4 ts=2026-09-23T18:17:06.3320000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[55] _id=6ab417a4485cab4c954f38aa ts=2026-09-23T18:17:06.4120000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5166 | 0.0 | 0.909 | 231.882 | 16.701 | 364785.772 | 0.26 | 173 | 13 |
| PuzzlePieceVisibleEvent | 3031 | 0.0 | 0.033 | 342.946 | 1.811 | 518841.479 | 0.17 | 1763 | 7 |
| PlayerPositionEvent | 2909 | 0.06 | 9.999 | 371.668 | 10.016 | 354237.681 | 0.16 | 0 | 11 |
| DialogueEvent | 2296 | 0.001 | 4.649 | 521.718 | 47.949 | 364815.924 | 0.12 | 687 | 13 |
| argumentationNodeEvent | 334 | 0.014 | 0.373 | 3120.249 | 8.04 | 515097.236 | 0.02 | 89 | 3 |
| ObjectInterEvent | 326 | 0.004 | 9.453 | 3673.046 | 483.075 | 365213.645 | 0.02 | 1 | 16 |
| TopographicMapEvent | 116 | 0.015 | 5.656 | 8966.818 | 30283.932 | 437187.247 | 0.01 | 6 | 11 |
| questEvent | 95 | 0.001 | 247.315 | 12606.218 | 73599.023 | 354510.32 | 0.0 | 20 | 21 |
| Soil Key Puzzle | 59 | 0.17 | 1.002 | 17170.567 | 6107.816 | 604746.882 | 0.0 | 0 | 3 |
| gameWindowFocusEvent | 59 | 0.0 | 345.611 | 20290.105 | 84417.459 | 354267.768 | 0.0 | 1 | 25 |
| argumentationAnswerEvent | 51 | 0.18 | 1.096 | 20432.926 | 44739.109 | 515171.919 | 0.0 | 0 | 3 |
| WaterChamberEvent | 49 | 2.244 | 16.067 | 28.441 | 77.453 | 203.894 | 2.11 | 0 | 0 |
| gameWindowUnfocusEvent | 42 | 0.0 | 256.007 | 28500.486 | 86942.785 | 354294.677 | 0.0 | 1 | 15 |
| DEBUGMenu | 23 | 118.41 | 10481.65 | 52048.033 | 241071.762 | 354645.904 | 0.0 | 0 | 21 |
| gameStartEvent | 22 | 20.472 | 15050.705 | 54414.373 | 249599.571 | 354648.495 | 0.0 | 0 | 19 |
| SolarStillDesignEvent | 19 | 0.0 | 2.65 | 27.114 | 84.039 | 414.618 | 2.21 | 2 | 0 |
| soilMachine | 18 | 1.399 | 35.287 | 47.714 | 175.383 | 211.035 | 1.26 | 0 | 0 |
| chatEvent | 15 | 0.084 | 5.3 | 74136.541 | 344200.712 | 958212.573 | 0.0 | 0 | 4 |
| DaniEvent | 11 | 0.864 | 3.893 | 87111.763 | 435144.118 | 438933.356 | 0.0 | 0 | 3 |
| argumentationEvent | 10 | 0.028 | 81.118 | 104218.494 | 480036.283 | 515082.7 | 0.0 | 1 | 3 |
| argumentationToolEvent | 4 | 6.06 | 218674.559 | 238160.128 | 503577.339 | 515285.335 | 0.0 | 0 | 2 |
| EndOfUnit | 3 | 153778.85 | 437421.532 | 370983.769 | 513317.985 | 521750.924 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 6 group(s), 13 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[32] _id=6ab41762485cab4c954f371a ts=2026-09-23T18:16:01.2980000Z == 6aa4144c41b41dbac0c7f26c.jsonl[33] _id=6ab41762485cab4c954f371c ts=2026-09-23T18:16:01.2980000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[10120] _id=6ac3ffbbde269131f9af8699 ts=2026-10-05T19:51:23.0880000Z == 6aa4144c41b41dbac0c7f26c.jsonl[10121] _id=6ac3ffbbde269131f9af869b ts=2026-10-05T19:51:23.0880000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[10122] _id=6ac3ffbbde269131f9af869d ts=2026-10-05T19:51:23.0890000Z == 6aa4144c41b41dbac0c7f26c.jsonl[10104] _id=6ac3ffbbde269131f9af869f ts=2026-10-05T19:51:23.0890000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 90 group(s), 133 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[1132] _id=6ab564af485cab4c9553c9e0 ts=2026-09-24T17:58:07.1960000Z == 6aa4144c41b41dbac0c7f26c.jsonl[1134] _id=6ab564af485cab4c9553c9e8 ts=2026-09-24T17:58:07.1960000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1168] _id=6ab564b3485cab4c9553ca78 ts=2026-09-24T17:58:10.0060000Z == 6aa4144c41b41dbac0c7f26c.jsonl[1169] _id=6ab564b3485cab4c9553ca80 ts=2026-09-24T17:58:10.0060000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1197] _id=6ab564bd485cab4c9553cb24 ts=2026-09-24T17:58:20.7570000Z == 6aa4144c41b41dbac0c7f26c.jsonl[1183] _id=6ab564bd485cab4c9553cb30 ts=2026-09-24T17:58:20.7570000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 79 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f26c.jsonl[206] _id=6ab41949485cab4c954f45ca ts=2026-09-23T18:24:09.7810000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[205] _id=6ab41949485cab4c954f45ce ts=2026-09-23T18:24:09.7850000Z`; `179ms: 6aa4144c41b41dbac0c7f26c.jsonl[1080] _id=6ab56461485cab4c9553c2b7 ts=2026-09-24T17:56:49.7400000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[1068] _id=6ab56461485cab4c9553c2c7 ts=2026-09-24T17:56:49.9190000Z`; `283ms: 6aa4144c41b41dbac0c7f26c.jsonl[1068] _id=6ab56461485cab4c9553c2c7 ts=2026-09-24T17:56:49.9190000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[1075] _id=6ab56462485cab4c9553c2d0 ts=2026-09-24T17:56:50.2020000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 286 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `15ms: 6aa4144c41b41dbac0c7f26c.jsonl[1180] _id=6ab564be485cab4c9553cb46 ts=2026-09-24T17:58:20.8320000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[1186] _id=6ab564be485cab4c9553cb4a ts=2026-09-24T17:58:20.8470000Z`; `8ms: 6aa4144c41b41dbac0c7f26c.jsonl[1211] _id=6ab564bf485cab4c9553cb9e ts=2026-09-24T17:58:21.4840000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[1203] _id=6ab564c0485cab4c9553cba0 ts=2026-09-24T17:58:21.4920000Z`; `8ms: 6aa4144c41b41dbac0c7f26c.jsonl[1203] _id=6ab564c0485cab4c9553cba0 ts=2026-09-24T17:58:21.4920000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[1212] _id=6ab564c0485cab4c9553cba3 ts=2026-09-24T17:58:21.5000000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa4144c41b41dbac0c7f26c.jsonl[2144] _id=6ab5687a485cab4c95542536 ts=2026-09-24T18:14:18.4620000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[2152] _id=6ab5687a485cab4c9554253e ts=2026-09-24T18:14:18.4790000Z`; `19ms: 6aa4144c41b41dbac0c7f26c.jsonl[2299] _id=6ab6b9e8485cab4c955dcefb ts=2026-09-25T18:14:01.1620000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[2296] _id=6ab6b9e8485cab4c955dcf0f ts=2026-09-25T18:14:01.1810000Z`; `21ms: 6aa4144c41b41dbac0c7f26c.jsonl[2630] _id=6ab6bd86485cab4c955e42bf ts=2026-09-25T18:29:26.8000000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[2632] _id=6ab6bd87485cab4c955e42cd ts=2026-09-25T18:29:26.8210000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 23 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `524ms: 6aa4144c41b41dbac0c7f26c.jsonl[821] _id=6ab56262485cab4c95539a14 ts=2026-09-24T17:48:18.9800000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[837] _id=6ab56263485cab4c95539a32 ts=2026-09-24T17:48:19.5040000Z`; `305ms: 6aa4144c41b41dbac0c7f26c.jsonl[834] _id=6ab56266485cab4c95539a6b ts=2026-09-24T17:48:22.3040000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[838] _id=6ab56266485cab4c95539a78 ts=2026-09-24T17:48:22.6090000Z`; `248ms: 6aa4144c41b41dbac0c7f26c.jsonl[838] _id=6ab56266485cab4c95539a78 ts=2026-09-24T17:48:22.6090000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[840] _id=6ab56266485cab4c95539a7e ts=2026-09-24T17:48:22.8570000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa4144c41b41dbac0c7f26c.jsonl[8372] _id=6ac3eb9dde269131f9aef947 ts=2026-10-05T18:25:33.0890000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[8295] _id=6ac3eb9dde269131f9aef951 ts=2026-10-05T18:25:33.1170000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 45 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `15ms: 6aa4144c41b41dbac0c7f26c.jsonl[794] _id=6ab56205485cab4c95539348 ts=2026-09-24T17:46:46.0490000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[798] _id=6ab56206485cab4c9553934a ts=2026-09-24T17:46:46.0640000Z`; `14ms: 6aa4144c41b41dbac0c7f26c.jsonl[802] _id=6ab5620a485cab4c95539398 ts=2026-09-24T17:46:50.7820000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[789] _id=6ab5620a485cab4c9553939a ts=2026-09-24T17:46:50.7960000Z`; `629ms: 6aa4144c41b41dbac0c7f26c.jsonl[824] _id=6ab56258485cab4c9553995a ts=2026-09-24T17:48:08.2300000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[825] _id=6ab56258485cab4c9553996a ts=2026-09-24T17:48:08.8590000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `69ms: 6aa4144c41b41dbac0c7f26c.jsonl[53] _id=6ab417a2485cab4c954f38a2 ts=2026-09-23T18:17:06.3020000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[59] _id=6ab417a2485cab4c954f38a6 ts=2026-09-23T18:17:06.3710000Z`; `361ms: 6aa4144c41b41dbac0c7f26c.jsonl[59] _id=6ab417a2485cab4c954f38a6 ts=2026-09-23T18:17:06.3710000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[60] _id=6ab417a5485cab4c954f38b0 ts=2026-09-23T18:17:06.7320000Z`; `206ms: 6aa4144c41b41dbac0c7f26c.jsonl[60] _id=6ab417a5485cab4c954f38b0 ts=2026-09-23T18:17:06.7320000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[61] _id=6ab417a7485cab4c954f38b6 ts=2026-09-23T18:17:06.9380000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `380ms: 6aa4144c41b41dbac0c7f26c.jsonl[48] _id=6ab417a1485cab4c954f389e ts=2026-09-23T18:17:05.9520000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[54] _id=6ab417a2485cab4c954f38a4 ts=2026-09-23T18:17:06.3320000Z`; `80ms: 6aa4144c41b41dbac0c7f26c.jsonl[54] _id=6ab417a2485cab4c954f38a4 ts=2026-09-23T18:17:06.3320000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[55] _id=6ab417a4485cab4c954f38aa ts=2026-09-23T18:17:06.4120000Z`; `487ms: 6aa4144c41b41dbac0c7f26c.jsonl[55] _id=6ab417a4485cab4c954f38aa ts=2026-09-23T18:17:06.4120000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[56] _id=6ab417a6485cab4c954f38b4 ts=2026-09-23T18:17:06.8990000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4144c41b41dbac0c7f26c.jsonl[4167] _id=6abbffdd485cab4c9584270b ts=2026-09-29T18:13:46.9850000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[4168] _id=6abbffdd485cab4c9584270f ts=2026-09-29T18:13:46.9910000Z`; `7ms: 6aa4144c41b41dbac0c7f26c.jsonl[13613] _id=6ac5452dde269131f9b72379 ts=2026-10-06T18:59:56.9980000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[13610] _id=6ac5452dde269131f9b7237f ts=2026-10-06T18:59:57.0050000Z`; `2ms: 6aa4144c41b41dbac0c7f26c.jsonl[14041] _id=6ac5495bde269131f9b79ca3 ts=2026-10-06T19:17:47.0020000Z ~ 6aa4144c41b41dbac0c7f26c.jsonl[14042] _id=6ac5495bde269131f9b79ca5 ts=2026-10-06T19:17:47.0040000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 98h 30m 
  - Evidence: 98h 30m: 6aa4144c41b41dbac0c7f26c.jsonl[7430] _id=6abe5561485cab4c95a3dbd1 ts=2026-10-01T12:43:15.9520000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7731] _id=6ac3beb9de269131f9ace2be ts=2026-10-05T15:14:01.8560000Z; 71h 42m: 6aa4144c41b41dbac0c7f26c.jsonl[2565] _id=6ab6bcb5485cab4c955e2e11 ts=2026-09-25T18:25:57.5770000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2842] _id=6abaad22485cab4c956f793b ts=2026-09-28T18:08:34.3680000Z; 24h 15m: 6aa4144c41b41dbac0c7f26c.jsonl[973] _id=6ab56392485cab4c9553b34a ts=2026-09-24T17:53:23.0190000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2175] _id=6ab6b89c485cab4c955daaf7 ts=2026-09-25T18:08:29.5230000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 121h 55m 
  - Evidence: 121h 55m: 6aa4144c41b41dbac0c7f26c.jsonl[5973] _id=6abd501d485cab4c9590e3db ts=2026-09-30T18:08:29.3910000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10285] _id=6ac402b2de269131f9af8dab ts=2026-10-05T20:04:02.7470000Z; 119h 49m: 6aa4144c41b41dbac0c7f26c.jsonl[2370] _id=6ab6bb20485cab4c955dfd31 ts=2026-09-25T18:19:13.0760000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5972] _id=6abd501b485cab4c9590e3c1 ts=2026-09-30T18:08:27.9550000Z; 24h 15m: 6aa4144c41b41dbac0c7f26c.jsonl[1961] _id=6ab565e3485cab4c9553f58e ts=2026-09-24T18:03:15.9900000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2369] _id=6ab6bb1d485cab4c955dfc77 ts=2026-09-25T18:19:09.1830000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 101h 20m 
  - Evidence: 101h 20m: 6aa4144c41b41dbac0c7f26c.jsonl[7719] _id=6abe56d0485cab4c95a3f0f3 ts=2026-10-01T12:49:20.9470000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7754] _id=6ac3e7e0de269131f9aec043 ts=2026-10-05T18:09:36.8710000Z; 71h 28m: 6aa4144c41b41dbac0c7f26c.jsonl[2834] _id=6ab6c054485cab4c955e658b ts=2026-09-25T18:41:24.9840000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2869] _id=6abaad76485cab4c956f8578 ts=2026-09-28T18:09:58.6700000Z; 23h 57m: 6aa4144c41b41dbac0c7f26c.jsonl[2159] _id=6ab56890485cab4c95542566 ts=2026-09-24T18:14:40.9870000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2212] _id=6ab6b976485cab4c955dc0f0 ts=2026-09-25T18:12:06.9400000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 687 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26c.jsonl[10076] _id=6ac3ff52de269131f9af8615 ts=2026-10-05T19:49:38.1960000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10080] _id=6ac3ff52de269131f9af8617 ts=2026-10-05T19:49:38.1970000Z; 1ms: 6aa4144c41b41dbac0c7f26c.jsonl[13968] _id=6ac548ecde269131f9b78e17 ts=2026-10-06T19:15:56.7820000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[13967] _id=6ac548ecde269131f9b78e1a ts=2026-10-06T19:15:56.7830000Z; 1ms: 6aa4144c41b41dbac0c7f26c.jsonl[14022] _id=6ac5494cde269131f9b79c15 ts=2026-10-06T19:17:32.6450000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[14021] _id=6ac5494cde269131f9b79c17 ts=2026-10-06T19:17:32.6460000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 55m 
  - Evidence: 144h 55m: 6aa4144c41b41dbac0c7f26c.jsonl[5661] _id=6abc0fe4485cab4c958561f1 ts=2026-09-29T19:22:12.8570000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10527] _id=6ac405fbde269131f9af99cd ts=2026-10-05T20:18:03.7810000Z; 121h 30m: 6aa4144c41b41dbac0c7f26c.jsonl[969] _id=6ab56337485cab4c9553ac3f ts=2026-09-24T17:51:51.3250000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5661] _id=6abc0fe4485cab4c958561f1 ts=2026-09-29T19:22:12.8570000Z; 42h 42m: 6aa4144c41b41dbac0c7f26c.jsonl[10527] _id=6ac405fbde269131f9af99cd ts=2026-10-05T20:18:03.7810000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[14691] _id=6ac65eaede269131f9bb5f85 ts=2026-10-07T15:01:02.6310000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 101h 19m 
  - Evidence: 101h 19m: 6aa4144c41b41dbac0c7f26c.jsonl[7715] _id=6abe56cf485cab4c95a3f0e1 ts=2026-10-01T12:49:20.3530000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7743] _id=6ac3e7c2de269131f9aebe5d ts=2026-10-05T18:09:06.1250000Z; 71h 27m: 6aa4144c41b41dbac0c7f26c.jsonl[2838] _id=6ab6c054485cab4c955e658d ts=2026-09-25T18:41:25.0020000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2845] _id=6abaad28485cab4c956f7a31 ts=2026-09-28T18:08:40.3320000Z; 23h 53m: 6aa4144c41b41dbac0c7f26c.jsonl[2164] _id=6ab568a9485cab4c95542580 ts=2026-09-24T18:15:06.0180000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2177] _id=6ab6b89d485cab4c955dab1d ts=2026-09-25T18:08:30.1830000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 173 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[10120] _id=6ac3ffbbde269131f9af8699 ts=2026-10-05T19:51:23.0880000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10121] _id=6ac3ffbbde269131f9af869b ts=2026-10-05T19:51:23.0880000Z; 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[10122] _id=6ac3ffbbde269131f9af869d ts=2026-10-05T19:51:23.0890000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10104] _id=6ac3ffbbde269131f9af869f ts=2026-10-05T19:51:23.0890000Z; 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[14125] _id=6ac65987de269131f9baf9c7 ts=2026-10-07T14:39:03.7550000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[14126] _id=6ac65987de269131f9baf9c8 ts=2026-10-07T14:39:03.7550000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 101h 26m 
  - Evidence: 101h 26m: 6aa4144c41b41dbac0c7f26c.jsonl[7484] _id=6abe55fc485cab4c95a3e041 ts=2026-10-01T12:45:51.0930000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7826] _id=6ac3e89cde269131f9aeccc5 ts=2026-10-05T18:12:44.7380000Z; 96h 27m: 6aa4144c41b41dbac0c7f26c.jsonl[1990] _id=6ab56620485cab4c9553feb0 ts=2026-09-24T18:04:16.2870000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[3384] _id=6abab29f485cab4c957013fd ts=2026-09-28T18:31:59.7200000Z; 23h 36m: 6aa4144c41b41dbac0c7f26c.jsonl[3553] _id=6abab444485cab4c957034b5 ts=2026-09-28T18:39:00.7270000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[4382] _id=6abc0060485cab4c9584353a ts=2026-09-29T18:16:00.3220000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.004s..0.004s shown 
  - Evidence: 4ms: 6aa4144c41b41dbac0c7f26c.jsonl[206] _id=6ab41949485cab4c954f45ca ts=2026-09-23T18:24:09.7810000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[205] _id=6ab41949485cab4c954f45ce ts=2026-09-23T18:24:09.7850000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 98h 23m 
  - Evidence: 98h 23m: 6aa4144c41b41dbac0c7f26c.jsonl[7724] _id=6abe56fb485cab4c95a3f547 ts=2026-10-01T12:50:04.1820000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7726] _id=6ac3bebede269131f9ace2fb ts=2026-10-05T15:14:01.8630000Z; 71h 27m: 6aa4144c41b41dbac0c7f26c.jsonl[2839] _id=6ab6c05a485cab4c955e65c0 ts=2026-09-25T18:41:30.8750000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2843] _id=6abaad28485cab4c956f7a25 ts=2026-09-28T18:08:34.3750000Z; 23h 53m: 6aa4144c41b41dbac0c7f26c.jsonl[2166] _id=6ab568b7485cab4c95542590 ts=2026-09-24T18:15:19.3660000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2176] _id=6ab6b89d485cab4c955dab15 ts=2026-09-25T18:08:29.5280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 144h 7m 
  - Evidence: 144h 7m: 6aa4144c41b41dbac0c7f26c.jsonl[4734] _id=6abc02be485cab4c95846bf9 ts=2026-09-29T18:26:05.4130000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8656] _id=6ac3ed77de269131f9af1e17 ts=2026-10-05T18:33:26.8920000Z; 96h 16m: 6aa4144c41b41dbac0c7f26c.jsonl[1957] _id=6ab565d0485cab4c9553f1cd ts=2026-09-24T18:02:55.6710000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[3021] _id=6abaafa2485cab4c956fd11f ts=2026-09-28T18:19:13.6620000Z; 23h 28m: 6aa4144c41b41dbac0c7f26c.jsonl[4076] _id=6abab5cd485cab4c95705959 ts=2026-09-28T18:45:31.6890000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[4169] _id=6abbffdd485cab4c95842711 ts=2026-09-29T18:13:47.3740000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1763 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[10540] _id=6ac4dbbdde269131f9aff312 ts=2026-10-06T11:30:04.1640000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10541] _id=6ac4dbbdde269131f9aff314 ts=2026-10-06T11:30:04.1640000Z; 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[10545] _id=6ac4dbbede269131f9aff326 ts=2026-10-06T11:30:05.6920000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10551] _id=6ac4dbbede269131f9aff328 ts=2026-10-06T11:30:05.6920000Z; 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[10562] _id=6ac4dbc0de269131f9aff346 ts=2026-10-06T11:30:07.5720000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10584] _id=6ac4dbc0de269131f9aff348 ts=2026-10-06T11:30:07.5720000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 59m 
  - Evidence: 167h 59m: 6aa4144c41b41dbac0c7f26c.jsonl[3420] _id=6abab2d7485cab4c957017e5 ts=2026-09-28T18:32:55.2310000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8620] _id=6ac3ed22de269131f9af19af ts=2026-10-05T18:32:02.1130000Z; 96h 27m: 6aa4144c41b41dbac0c7f26c.jsonl[1992] _id=6ab56623485cab4c9553feee ts=2026-09-24T18:04:19.2800000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[3383] _id=6abab29f485cab4c957013f9 ts=2026-09-28T18:31:59.7150000Z; 16h 55m: 6aa4144c41b41dbac0c7f26c.jsonl[8649] _id=6ac3ed48de269131f9af1bbf ts=2026-10-05T18:32:40.5350000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10609] _id=6ac4db4bde269131f9aff148 ts=2026-10-06T11:28:11.9030000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[14261] _id=6ac65b21de269131f9bb10b8 ts=2026-10-07T14:45:53.9690000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[14262] _id=6ac65b21de269131f9bb10b9 ts=2026-10-07T14:45:53.9690000Z; 4ms: 6aa4144c41b41dbac0c7f26c.jsonl[14256] _id=6ac65b21de269131f9bb10b4 ts=2026-10-07T14:45:53.9650000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[14261] _id=6ac65b21de269131f9bb10b8 ts=2026-10-07T14:45:53.9690000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 121h 26m 
  - Evidence: 121h 26m: 6aa4144c41b41dbac0c7f26c.jsonl[7164] _id=6abd55ef485cab4c9591acc3 ts=2026-09-30T18:33:19.3650000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10189] _id=6ac401b2de269131f9af8923 ts=2026-10-05T19:59:46.6120000Z; 71h 29m: 6aa4144c41b41dbac0c7f26c.jsonl[2797] _id=6ab6bfe1485cab4c955e5f83 ts=2026-09-25T18:39:29.1640000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2844] _id=6abaad28485cab4c956f7a2b ts=2026-09-28T18:08:40.3300000Z; 24h 21m: 6aa4144c41b41dbac0c7f26c.jsonl[3150] _id=6abab0f8485cab4c956ff58f ts=2026-09-28T18:24:56.7330000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5033] _id=6abc077e485cab4c9584c28f ts=2026-09-29T18:46:22.9420000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.015s..0.016s shown 
  - Evidence: 15ms: 6aa4144c41b41dbac0c7f26c.jsonl[2150] _id=6ab5687a485cab4c95542534 ts=2026-09-24T18:14:18.4470000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2144] _id=6ab5687a485cab4c95542536 ts=2026-09-24T18:14:18.4620000Z; 16ms: 6aa4144c41b41dbac0c7f26c.jsonl[2294] _id=6ab6b9e8485cab4c955dcef9 ts=2026-09-25T18:14:01.1460000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2299] _id=6ab6b9e8485cab4c955dcefb ts=2026-09-25T18:14:01.1620000Z; 16ms: 6aa4144c41b41dbac0c7f26c.jsonl[2629] _id=6ab6bd86485cab4c955e42bc ts=2026-09-25T18:29:26.7840000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2630] _id=6ab6bd86485cab4c955e42bf ts=2026-09-25T18:29:26.8000000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 6m 
  - Evidence: 143h 6m: 6aa4144c41b41dbac0c7f26c.jsonl[5579] _id=6abc0eb7485cab4c95851bc3 ts=2026-09-29T19:17:10.9780000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8233] _id=6ac3eb1ade269131f9aef1d5 ts=2026-10-05T18:23:22.8970000Z; 121h 26m: 6aa4144c41b41dbac0c7f26c.jsonl[859] _id=6ab5627b485cab4c95539bec ts=2026-09-24T17:48:43.5950000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5480] _id=6abc0e5e485cab4c9585086f ts=2026-09-29T19:15:42.1910000Z; 24h 50m: 6aa4144c41b41dbac0c7f26c.jsonl[8293] _id=6ac3eb9dde269131f9aef945 ts=2026-10-05T18:25:33.0720000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[13966] _id=6ac548ecde269131f9b78e13 ts=2026-10-06T19:15:56.7650000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 4m 
  - Evidence: 143h 4m: 6aa4144c41b41dbac0c7f26c.jsonl[5576] _id=6abc0eb7485cab4c95851bcf ts=2026-09-29T19:17:10.9920000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8139] _id=6ac3eac1de269131f9aeec1d ts=2026-10-05T18:21:53.6920000Z; 121h 26m: 6aa4144c41b41dbac0c7f26c.jsonl[726] _id=6ab5627b485cab4c95539bee ts=2026-09-24T17:48:43.6080000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5469] _id=6abc0e4d485cab4c9585053c ts=2026-09-29T19:15:25.3810000Z; 24h 49m: 6aa4144c41b41dbac0c7f26c.jsonl[8295] _id=6ac3eb9dde269131f9aef951 ts=2026-10-05T18:25:33.1170000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[13912] _id=6ac548c5de269131f9b78813 ts=2026-10-06T19:15:17.7420000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.028s..0.028s shown 
  - Evidence: 28ms: 6aa4144c41b41dbac0c7f26c.jsonl[8372] _id=6ac3eb9dde269131f9aef947 ts=2026-10-05T18:25:33.0890000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8295] _id=6ac3eb9dde269131f9aef951 ts=2026-10-05T18:25:33.1170000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 4m 
  - Evidence: 143h 4m: 6aa4144c41b41dbac0c7f26c.jsonl[5569] _id=6abc0eaf485cab4c95851979 ts=2026-09-29T19:17:03.6950000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8163] _id=6ac3eac8de269131f9aeed01 ts=2026-10-05T18:22:00.9310000Z; 121h 26m: 6aa4144c41b41dbac0c7f26c.jsonl[863] _id=6ab56277485cab4c95539bc0 ts=2026-09-24T17:48:39.6690000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5472] _id=6abc0e50485cab4c958505dd ts=2026-09-29T19:15:28.6160000Z; 24h 49m: 6aa4144c41b41dbac0c7f26c.jsonl[8160] _id=6ac3eb96de269131f9aef8ff ts=2026-10-05T18:25:26.7990000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[13883] _id=6ac548bede269131f9b786fa ts=2026-10-06T19:15:10.0760000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 89 interval(s) ≤ 0.014s..0.017s shown 
  - Evidence: 14ms: 6aa4144c41b41dbac0c7f26c.jsonl[802] _id=6ab5620a485cab4c95539398 ts=2026-09-24T17:46:50.7820000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[789] _id=6ab5620a485cab4c9553939a ts=2026-09-24T17:46:50.7960000Z; 15ms: 6aa4144c41b41dbac0c7f26c.jsonl[794] _id=6ab56205485cab4c95539348 ts=2026-09-24T17:46:46.0490000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[798] _id=6ab56206485cab4c9553934a ts=2026-09-24T17:46:46.0640000Z; 17ms: 6aa4144c41b41dbac0c7f26c.jsonl[8378] _id=6ac3eb86de269131f9aef801 ts=2026-10-05T18:25:10.1350000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8382] _id=6ac3eb86de269131f9aef805 ts=2026-10-05T18:25:10.1520000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 8m 
  - Evidence: 143h 8m: 6aa4144c41b41dbac0c7f26c.jsonl[5477] _id=6abc0e5a485cab4c958507bd ts=2026-09-29T19:15:38.5200000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[8245] _id=6ac3eb2fde269131f9aef311 ts=2026-10-05T18:23:43.8550000Z; 121h 27m: 6aa4144c41b41dbac0c7f26c.jsonl[852] _id=6ab5626a485cab4c95539af2 ts=2026-09-24T17:48:26.4910000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5477] _id=6abc0e5a485cab4c958507bd ts=2026-09-29T19:15:38.5200000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 266h 10m 
  - Evidence: 266h 10m: 6aa4144c41b41dbac0c7f26c.jsonl[893] _id=6ab563b0485cab4c9553b62e ts=2026-09-24T17:53:52.6430000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[10291] _id=6ac402b5de269131f9af8db3 ts=2026-10-05T20:04:05.2160000Z; 22h 30m: 6aa4144c41b41dbac0c7f26c.jsonl[10295] _id=6ac402c3de269131f9af8deb ts=2026-10-05T20:04:19.6720000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[12617] _id=6ac53f60de269131f9b68cfb ts=2026-10-06T18:35:12.4440000Z; 19h 33m: 6aa4144c41b41dbac0c7f26c.jsonl[13734] _id=6ac54677de269131f9b745cd ts=2026-10-06T19:05:27.7240000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[14121] _id=6ac6597fde269131f9baf985 ts=2026-10-07T14:38:58.1250000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 98h 30m 
  - Evidence: 98h 30m: 6aa4144c41b41dbac0c7f26c.jsonl[7428] _id=6abe5557485cab4c95a3dba9 ts=2026-10-01T12:43:05.3770000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7730] _id=6ac3beb1de269131f9ace287 ts=2026-10-05T15:13:53.8720000Z; 71h 42m: 6aa4144c41b41dbac0c7f26c.jsonl[2567] _id=6ab6bcac485cab4c955e2cdf ts=2026-09-25T18:25:48.7630000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2841] _id=6abaad0a485cab4c956f765f ts=2026-09-28T18:08:10.9190000Z; 24h 14m: 6aa4144c41b41dbac0c7f26c.jsonl[971] _id=6ab56382485cab4c9553b1d8 ts=2026-09-24T17:53:06.2730000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2174] _id=6ab6b87c485cab4c955da934 ts=2026-09-25T18:07:56.7250000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 98h 24m 
  - Evidence: 98h 24m: 6aa4144c41b41dbac0c7f26c.jsonl[7721] _id=6abe56d5485cab4c95a3f195 ts=2026-10-01T12:49:26.1030000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7729] _id=6ac3beb1de269131f9ace281 ts=2026-10-05T15:13:53.8710000Z; 71h 42m: 6aa4144c41b41dbac0c7f26c.jsonl[2566] _id=6ab6bcac485cab4c955e2cdb ts=2026-09-25T18:25:48.7610000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2840] _id=6abaad0a485cab4c956f7657 ts=2026-09-28T18:08:10.9180000Z; 23h 52m: 6aa4144c41b41dbac0c7f26c.jsonl[2171] _id=6ab568b6485cab4c9554258e ts=2026-09-24T18:15:18.0660000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2173] _id=6ab6b87b485cab4c955da92d ts=2026-09-25T18:07:56.7230000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[61] _id=6ab417a7485cab4c954f38b6 ts=2026-09-23T18:17:06.9380000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[50] _id=6ab417b1485cab4c954f38e8 ts=2026-09-23T18:17:06.938Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 98h 24m 
  - Evidence: 98h 24m: 6aa4144c41b41dbac0c7f26c.jsonl[7722] _id=6abe56d7485cab4c95a3f1a3 ts=2026-10-01T12:49:28.2120000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7732] _id=6ac3becede269131f9ace32d ts=2026-10-05T15:14:22.8890000Z; 71h 43m: 6aa4144c41b41dbac0c7f26c.jsonl[2562] _id=6ab6bc9a485cab4c955e2ad9 ts=2026-09-25T18:25:30.3570000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2849] _id=6abaad40485cab4c956f7dea ts=2026-09-28T18:09:03.7610000Z; 24h 9m: 6aa4144c41b41dbac0c7f26c.jsonl[4146] _id=6abab6bb485cab4c957083b2 ts=2026-09-28T18:49:31.6210000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[5210] _id=6abc0a7f485cab4c9584cd33 ts=2026-09-29T18:59:11.3310000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26c.jsonl[57] _id=6ab417a8485cab4c954f38c4 ts=2026-09-23T18:17:07.0160000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[51] _id=6ab417b1485cab4c954f38ec ts=2026-09-23T18:17:07.016Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 98h 28m 
  - Evidence: 98h 28m: 6aa4144c41b41dbac0c7f26c.jsonl[7467] _id=6abe55ee485cab4c95a3df77 ts=2026-10-01T12:45:36.6880000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[7727] _id=6ac3bebfde269131f9ace2fd ts=2026-10-05T15:14:07.0080000Z; 71h 39m: 6aa4144c41b41dbac0c7f26c.jsonl[2624] _id=6ab6bd74485cab4c955e4237 ts=2026-09-25T18:29:08.7340000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2846] _id=6abaad28485cab4c956f7a33 ts=2026-09-28T18:08:40.3640000Z; 23h 54m: 6aa4144c41b41dbac0c7f26c.jsonl[2140] _id=6ab56864485cab4c955424f4 ts=2026-09-24T18:13:56.3980000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[2178] _id=6ab6b89e485cab4c955dab23 ts=2026-09-25T18:08:30.2360000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 20 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26c.jsonl[13610] _id=6ac5452dde269131f9b7237f ts=2026-10-06T18:59:57.0050000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[13611] _id=6ac5452dde269131f9b72383 ts=2026-10-06T18:59:57.0060000Z; 1ms: 6aa4144c41b41dbac0c7f26c.jsonl[762] _id=6ab56186485cab4c95538913 ts=2026-09-24T17:44:38.9510000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[757] _id=6ab56187485cab4c95538917 ts=2026-09-24T17:44:38.9520000Z; 2ms: 6aa4144c41b41dbac0c7f26c.jsonl[13101] _id=6ac5411ede269131f9b6c0f3 ts=2026-10-06T18:42:37.8480000Z -> 6aa4144c41b41dbac0c7f26c.jsonl[13030] _id=6ac5411ede269131f9b6c101 ts=2026-10-06T18:42:37.8500000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[2725] _id=6ab6bef7485cab4c955e4fe9 ts=2026-09-25T18:35:35.1330000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[2891] _id=6abaadc6485cab4c956f9178 ts=2026-09-28T18:11:18.5220000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[4055] _id=6abab5bf485cab4c95705797 ts=2026-09-28T18:45:19.2720000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 62 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[1880] _id=6ab565ba485cab4c9553ee29 ts=2026-09-24T18:02:34.4900000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1875] _id=6ab565ba485cab4c9553ee2e ts=2026-09-24T18:02:34.5440000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1855] _id=6ab565bb485cab4c9553ee4c ts=2026-09-24T18:02:34.6510000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 146 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[1220] _id=6ab564bf485cab4c9553cb70 ts=2026-09-24T17:58:21.3240000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1235] _id=6ab564c1485cab4c9553cbdc ts=2026-09-24T17:58:21.6770000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1236] _id=6ab564c1485cab4c9553cbde ts=2026-09-24T17:58:21.6770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[8295] _id=6ac3eb9dde269131f9aef951 ts=2026-10-05T18:25:33.1170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[798] _id=6ab56206485cab4c9553934a ts=2026-09-24T17:46:46.0640000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[789] _id=6ab5620a485cab4c9553939a ts=2026-09-24T17:46:50.7960000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[8228] _id=6ac3eb17de269131f9aef1a1 ts=2026-10-05T18:23:19.7530000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[12617] _id=6ac53f60de269131f9b68cfb ts=2026-10-06T18:35:12.4440000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[13416] _id=6ac543c8de269131f9b70b8c ts=2026-10-06T18:54:00.1650000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[13445] _id=6ac5443dde269131f9b7147d ts=2026-10-06T18:55:56.9820000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[13608] _id=6ac5452dde269131f9b72377 ts=2026-10-06T18:59:56.9910000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[13610] _id=6ac5452dde269131f9b7237f ts=2026-10-06T18:59:57.0050000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[29] _id=6ab41761485cab4c954f370a ts=?`; `6aa4144c41b41dbac0c7f26c.jsonl[2847] _id=6abaad28485cab4c956f7a1f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 364 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[901] _id=6ab56551485cab4c9553de04 ts=2026-09-24T18:00:47.7910000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1356] _id=6ab56552485cab4c9553de2e ts=2026-09-24T18:00:48.7910000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1612] _id=6ab5656a485cab4c9553e272 ts=2026-09-24T18:01:13.0210000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 383 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[1134] _id=6ab564af485cab4c9553c9e8 ts=2026-09-24T17:58:07.1960000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1136] _id=6ab564af485cab4c9553c9ee ts=2026-09-24T17:58:07.1960000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1130] _id=6ab564b0485cab4c9553c9f2 ts=2026-09-24T17:58:07.1960000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 33 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[2144] _id=6ab5687a485cab4c95542536 ts=2026-09-24T18:14:18.4620000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[2152] _id=6ab5687a485cab4c9554253e ts=2026-09-24T18:14:18.4790000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[2290] _id=6ab6b9e3485cab4c955dce73 ts=2026-09-25T18:13:56.0570000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 20 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[8382] _id=6ac3eb86de269131f9aef805 ts=2026-10-05T18:25:10.1520000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[8087] _id=6ac3eb91de269131f9aef8c1 ts=2026-10-05T18:25:21.7610000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[8157] _id=6ac3eb94de269131f9aef8e1 ts=2026-10-05T18:25:24.1550000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 460 start, 451 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 87 unmatched 'BecameCameraCentered' (totals: 655 open, 630 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 71 unmatched 'BecameVisible' (totals: 836 open, 911 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'MapOpenEvent' (totals: 35 open, 29 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationNodeHoverStart' (totals: 145 open, 147 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 4 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 58 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 192 of 14689 adjacent _id pairs reverse in client time; worst 115.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f26c.jsonl[1342] _id=6ab56515485cab4c9553d3d6 ts=2026-09-24T17:59:49.2050000Z`; `6aa4144c41b41dbac0c7f26c.jsonl[1346] _id=6ab56516485cab4c9553d402 ts=2026-09-24T17:57:53.5990000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -2300.86s, max +2.98s over 14690 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26c\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5167 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2017); Unit 2 Prod (Refactor) (1022); Unit 4 Dev - Dungeon (686); Unit 3 Dungeon Dev (507); Unit 5 Dev - Dungeon (393); Unit 5 Dev (229); Unit 1 Dev (210); Unit 4 Dev (103)
- **Intervals:** median 0.91s (p5 0.09s / p95 16.70s, n=5166)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5167/5167 records)
    "pressed"  x5167
data.actionType  (string, 5167/5167 records)
    "Move"  x3937
    "Interact"  x645
    "Jump"  x360
    "Hoverboard"  x83
    "Ascend"  x53
    "Sprint"  x53
    "Descend"  x21
    "Map"  x7
    "Pause"  x6
    "SkipCinematic"  x2
data.key  (string, 5167/5167 records, 22 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5167/5167 records)
    "Player"  x3525
    "Drone"  x1642
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3032 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1644); Unit 4 Dev (656); Unit 3 Dungeon Dev (384); Unit 5 Dev - Dungeon (348)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.81s, n=3031)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3032/3032 records)
    "BecameInvisible"  x911
    "BecameVisible"  x836
    "BecameCameraCentered"  x655
    "BecameCameraUncentered"  x630
data.pieceId  (string, 3032/3032 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3032/3032 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2920 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (959); Unit 3 Dev (576); Unit 1 Dev (401); Unit 3 Dungeon Dev (275); Unit 4 Dev - Dungeon (252); Unit 5 Dev (227); Unit 5 Dev - Dungeon (168); Unit 4 Dev (62)
- **Intervals:** median 10.00s (p5 1.65s / p95 10.02s, n=2909)
- **Fields under `data`:**

```text
data.position  (object, 2920/2920 records)
data.position.x  (number, 2920/2920 records)
    numeric range -832.782 .. 2486.72 (921 unique)
data.position.y  (number, 2920/2920 records)
    numeric range -115.527 .. 280.357 (703 unique)
data.position.z  (number, 2920/2920 records)
    numeric range -1046.4 .. 2265.96 (920 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2297 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (773); Unit 3 Dev (528); Unit 5 Dev (299); Unit 1 Dev (228); Unit 3 Dungeon Dev (206); Unit 4 Dev - Dungeon (115); Unit 5 Dev - Dungeon (107); Unit 4 Dev (41)
- **eventKey:** present on 1386 of 2297 records
- **Intervals:** median 4.65s (p5 0.00s / p95 47.95s, n=2296)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1386; [conversationId, dialogueEventType] x911
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2297/2297 records)
    numeric range 8 .. 118 (51 unique)
data.dialogueEventType  (string, 2297/2297 records)
    "DialogueNodeEvent"  x1386
    "DialogueStartEvent"  x460
    "DialogueFinishEvent"  x451
data.nodeId  (number, 1386/2297 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 335 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (155); Unit 5 Dev (78); Unit 2 Prod (Refactor) (73); Unit 1 Dev (29)
- **Intervals:** median 0.37s (p5 0.02s / p95 8.04s, n=334)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 335/335 records)
    "argumentationNodeHoverEnd"  x147
    "argumentationNodeHoverStart"  x145
    "argumentationNodeAdd"  x28
    "argumentationNodeRemove"  x15
data.argumentationTitle  (string, 335/335 records)
    "Unit 3 - Pollution Upstream"  x155
    "Unit 5"  x78
    "Unit 2 – Watershed"  x73
    "Unit 1 - Freshwater"  x15
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 335/335 records)
    "3"  x53
    "2"  x44
    "4"  x40
    "1"  x37
    "II"  x37
    "A"  x32
    "I"  x28
    "C"  x21
    "B"  x20
    "D"  x15
    "5"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 327 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (93); Unit 5 Dev (86); Unit 2 Prod (Refactor) (50); Unit 3 Dungeon Dev (46); Unit 3 Dev (17); Unit 5 Dev - Dungeon (16); Unit 1 Dev (11); Unit 4 Dev (8)
- **Intervals:** median 9.45s (p5 0.14s / p95 483.08s, n=326)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 327/327 records)
    34 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 327/327 records)
    89 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 117 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (68); Unit 3 Dev (39); Unit 5 Dev (10)
- **Intervals:** median 5.66s (p5 0.19s / p95 30283.93s, n=116)
- **`data` key-set variants:** [actionType, featureUsed] x64; [actionType, featureUsed, location] x53
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 117/117 records)
    "WaypointMoveEvent"  x41
    "MapOpenEvent"  x35
    "MapCloseEvent"  x29
    "WaypointSetEvent"  x12
data.featureUsed  (string, 117/117 records)
    "Map"  x64
    "Waypoint"  x53
data.location  (object, 53/117 records)
data.location.x  (number, 53/117 records)
    numeric range -381.295 .. 621.91 (46 unique)
data.location.y  (number, 53/117 records)
    numeric range -150.5 .. 235.105 (47 unique)
data.location.z  (number, 53/117 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 96 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 3 Dev (18); Unit 1 Dev (16); Unit 4 Dev - Dungeon (12); Unit 5 Dev - Dungeon (12); Unit 5 Dev (11); Unit 3 Dungeon Dev (3); Unit 4 Dev (1)
- **eventKey:** present on 96 of 96 records
- **Intervals:** median 247.31s (p5 0.00s / p95 73599.02s, n=95)
- **`data` key-set variants:** [questEventType, questID, questName] x58; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 96/96 records)
    "questActiveEvent"  x58
    "questFinishEvent"  x38
data.questID  (string, 96/96 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 96/96 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/96 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 60 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (32); Unit 3 Dev (16); Unit 4 Dev (12)
- **Intervals:** median 1.00s (p5 0.21s / p95 6107.82s, n=59)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/60 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/60 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 52/60 records)
    "RightDrag"  x29
    "LeftDrag"  x23
data.currentSoilType  (string, 52/60 records)
    "CLAYSAND"  x12
    "CLAY"  x11
    "SAND"  x11
    "CLAYROCK"  x9
    "SANDGRAVEL"  x5
    "BEDROCK"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 52/60 records)
    "false"  x39
    "true"  x13
data.waterLevelStatus  (string, 52/60 records)
    "TooHigh"  x27
    "Proper"  x18
    "TooLow"  x7
data.waterRetentionChange  (string, 52/60 records)
    "Increase"  x25
    "Decrease"  x14
    "NoChange"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 60 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (23); Unit 2 Prod (Refactor) (14); Unit 3 Dev (7); Unit 1 Dev (6); Unit 5 Dev - Dungeon (4); Unit 5 Dev (3); Transition (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 345.61s (p5 0.35s / p95 84417.46s, n=59)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 60/60 records)
    true  x60
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 52 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (20); Unit 1 Dev (19); Unit 2 Prod (Refactor) (9); Unit 5 Dev (4)
- **Intervals:** median 1.10s (p5 0.20s / p95 44739.11s, n=51)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 52/52 records)
    "submitAnswerEvent"  x52
data.answerSubmitted  (string, 52/52 records)
    "I"  x18
    "A,3,I"  x8
    "A,1,I"  x5
    "A,1,II"  x5
    "A,4,I"  x4
    "A,2,I"  x3
    "C,D,3,II"  x3
    "1,II"  x2
    "A,5,I"  x1
    "A,B,1,II"  x1
    "A,D,1,II"  x1
    "D,C,3,4,II"  x1
data.argumentationTitle  (string, 52/52 records)
    "Unit 3 - Pollution Upstream"  x20
    "Unit 1 - Freshwater"  x19
    "Unit 2 – Watershed"  x9
    "Unit 5"  x4
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 50 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (50)
- **Intervals:** median 16.07s (p5 2.58s / p95 77.45s, n=49)
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "On"  x33
    "Off"  x17
data.floor  (string, 50/50 records)
    "4"  x27
    "3"  x18
    "2"  x3
    "1"  x2
data.machineNumber  (string, 50/50 records)
    "One"  x46
    "Two"  x4
data.machineType  (string, 50/50 records)
    "Condenser"  x25
    "Evaporator"  x15
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x4
    "DualChamber_Condenser"  x2
data.room  (string, 50/50 records)
    "2"  x18
    "3"  x16
    "1"  x10
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 43 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (9); Unit 1 Dev (7); Unit 5 Dev (4); Unit 5 Dev - Dungeon (4); Transition (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 256.01s (p5 0.12s / p95 86942.79s, n=42)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 43/43 records)
    false  x43
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 24 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 3 Dev (7); Unit 2 Prod (Refactor) (5); Unit 1 Dev (3); MainMenu (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev (1)
- **Intervals:** median 10481.65s (p5 540.65s / p95 241071.76s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "DebugMenuStateChanged"  x24
data.isOpened  (bool, 24/24 records)
    false  x24
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 15050.70s (p5 118.77s / p95 249599.57s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 20 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (20)
- **Intervals:** median 2.65s (p5 0.00s / p95 84.04s, n=19)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x18; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "optionSelected"  x18
    "DesignSubmitted"  x2
data.designSelections  (object, 2/20 records)
data.designSelections.glassRoofTemperature  (string, 2/20 records)
    "Cold"  x1
    "Hot"  x1
data.designSelections.roofCovering  (string, 2/20 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/20 records)
    "Flat"  x1
    "Tilted Out"  x1
data.featureUsed  (string, 20/20 records)
    "RoofStyle"  x8
    "ExtraCovering"  x6
    "GlassRoofTemperature"  x4
    "Submit"  x2
data.selectedOption  (string, 18/20 records, 3 empty-string)
    ""  x3
    "Covered"  x3
    "Tilted Out"  x3
    "Cold"  x2
    "Flat"  x2
    "Tilted In"  x2
    "Uncovered"  x2
    "Hot"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 35.29s (p5 1.65s / p95 175.38s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Clay"  x9
    "Bedrock"  x5
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 19/19 records)
    "5"  x15
    "4"  x3
    "3"  x1
data.machine  (string, 19/19 records)
    "1"  x18
    "2"  x1
data.row  (string, 19/19 records)
    "TopRow"  x14
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `chatEvent` — 16 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (8); Unit 5 Dev (4); Unit 2 Prod (Refactor) (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 5.30s (p5 0.09s / p95 344200.71s, n=15)
- **`data` key-set variants:** [actionType, chatID] x14; [actionKey, chatID] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/16 records)
    "ScrollStop"  x2
data.actionType  (string, 14/16 records)
    "Close"  x9
    "Open"  x3
    "ScrollStart"  x2
data.chatID  (string, 16/16 records)
    "NA"  x11
    "[]"  x4
    "[16-3]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (6)
- **Intervals:** median 3.89s (p5 1.15s / p95 435144.12s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 11 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 81.12s (p5 19.14s / p95 480036.28s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "argumentationSessionClose"  x6
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 11/11 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 11/11 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 218674.56s (p5 22.71s / p95 503577.34s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 437421.53s (p5 182143.12s / p95 513317.98s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Permissions check failed"  x1
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 1 empty-string)
    ""  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit1"  x1
    "unit2"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (32 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (41x); "WaypointSetEvent" (12x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (53x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (15x)
- `soilMachine` data.canisterType: "Bedrock" (5x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*