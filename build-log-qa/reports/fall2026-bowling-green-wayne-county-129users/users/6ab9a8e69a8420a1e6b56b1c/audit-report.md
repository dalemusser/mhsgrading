# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b1c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b1c
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b1c.jsonl
- **Records:** 15261 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b1c
- **Time span:** 2026-10-05T16:25:31.479000+00:00 .. 2026-10-16T14:37:25.735000+00:00 (262h 11m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b1c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 15261 records, 10 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 109 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5804 | 38.03 | 1 | 9 | 0 | 2026-10-05T16:32:06.273000+00:00 | 2026-10-16T14:37:25.735000+00:00 | 262h 5m |
| PuzzlePieceVisibleEvent | 3285 | 21.53 | 1 | 4 | 0 | 2026-10-06T16:42:31.561000+00:00 | 2026-10-15T16:55:52.101000+00:00 | 216h 13m |
| DialogueEvent | 2495 | 16.35 | 1 | 9 | 1540 | 2026-10-05T16:32:22.911000+00:00 | 2026-10-16T14:37:16.099000+00:00 | 262h 4m |
| PlayerPositionEvent | 1928 | 12.63 | 1 | 9 | 0 | 2026-10-05T16:32:02.763000+00:00 | 2026-10-16T14:37:25.203000+00:00 | 262h 5m |
| argumentationNodeEvent | 681 | 4.46 | 1 | 5 | 0 | 2026-10-05T16:53:47.496000+00:00 | 2026-10-16T13:57:56.619000+00:00 | 261h 4m |
| ObjectInterEvent | 336 | 2.2 | 1 | 9 | 0 | 2026-10-05T16:37:22.487000+00:00 | 2026-10-16T14:37:25.735000+00:00 | 262h 0m |
| TopographicMapEvent | 164 | 1.07 | 1 | 3 | 0 | 2026-10-06T16:42:53.068000+00:00 | 2026-10-14T18:15:41.971000+00:00 | 193h 32m |
| Soil Key Puzzle | 118 | 0.77 | 1 | 3 | 0 | 2026-10-06T16:49:18.817000+00:00 | 2026-10-14T16:48:54.240000+00:00 | 191h 59m |
| questEvent | 91 | 0.6 | 1 | 9 | 91 | 2026-10-05T16:32:22.879000+00:00 | 2026-10-16T14:33:22.164000+00:00 | 262h 0m |
| gameWindowFocusEvent | 57 | 0.37 | 1 | 10 | 0 | 2026-10-05T16:25:31.479000+00:00 | 2026-10-16T14:29:14.862000+00:00 | 262h 3m |
| argumentationAnswerEvent | 50 | 0.33 | 1 | 5 | 0 | 2026-10-05T16:53:55.628000+00:00 | 2026-10-16T13:57:58.417000+00:00 | 261h 4m |
| gameWindowUnfocusEvent | 46 | 0.3 | 1 | 10 | 0 | 2026-10-05T16:25:56.324000+00:00 | 2026-10-16T13:58:29.364000+00:00 | 261h 32m |
| DEBUGMenu | 40 | 0.26 | 1 | 9 | 0 | 2026-10-05T16:32:02.737000+00:00 | 2026-10-16T14:29:14.714000+00:00 | 261h 57m |
| WaterChamberEvent | 37 | 0.24 | 1 | 1 | 0 | 2026-10-15T16:56:07.257000+00:00 | 2026-10-16T13:49:53.128000+00:00 | 20h 53m |
| argumentationToolEvent | 27 | 0.18 | 1 | 4 | 0 | 2026-10-05T16:53:39.902000+00:00 | 2026-10-16T13:56:21.791000+00:00 | 261h 2m |
| gameStartEvent | 20 | 0.13 | 1 | 1 | 0 | 2026-10-05T16:25:31.481000+00:00 | 2026-10-16T14:29:14.862000+00:00 | 262h 3m |
| soilMachine | 19 | 0.12 | 1 | 1 | 0 | 2026-10-14T17:02:16.338000+00:00 | 2026-10-14T18:10:44.344000+00:00 | 1h 8m |
| DaniEvent | 16 | 0.1 | 1 | 1 | 0 | 2026-10-06T16:54:00.721000+00:00 | 2026-10-07T16:32:08.452000+00:00 | 23h 38m |
| TerasGardenBox | 15 | 0.1 | 1 | 1 | 0 | 2026-10-15T16:40:55.563000+00:00 | 2026-10-15T16:42:11.129000+00:00 | 1m 15s |
| argumentationEvent | 14 | 0.09 | 1 | 5 | 0 | 2026-10-05T16:53:44.383000+00:00 | 2026-10-16T13:57:58.456000+00:00 | 261h 4m |
| chatEvent | 8 | 0.05 | 1 | 3 | 0 | 2026-10-06T16:54:15.504000+00:00 | 2026-10-16T14:29:25.229000+00:00 | 237h 35m |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-05T16:59:39.089000+00:00 | 2026-10-16T14:37:25.720000+00:00 | 261h 37m |
| SolarStillDesignEvent | 5 | 0.03 | 1 | 1 | 0 | 2026-10-16T14:31:00.728000+00:00 | 2026-10-16T14:31:08.768000+00:00 | 8.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 87219.959s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.037s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 19.153s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.63s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 339.302s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 442.171s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 307.655s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.722s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.3x vs baseline. 
  - Observed: 40 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 16 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.1x vs baseline. 
  - Observed: 118 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 180 ft; 210 ft; 270 ft; 30 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.0x vs baseline. 
  - Observed: 50 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,B,2,II; A,B,D,2,II; A,C,2,II; A,C,B,2,II; B,2,II; B,3,I; B,3,II; B,C,A,2,II; B,D,2,II; C,2,II; C,3,I; C,3,II; C,4,II; C,A,2,II; C,B,2,II; C,D,2,II; C,D,3,II; D,2,II; D,3,II; D,A,2,II; II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.9x vs baseline. 
  - Observed: 681 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 27 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 8 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-89, 18-91, 18-92, 18-93, 18-95, 18-98]; [18-92, 18-93, 18-95, 18-98, 18-283] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[135] _id=6ac3d2acde269131f9ade687 ts=2026-10-05T16:39:07.7500000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[187] _id=6ac3d395de269131f9adf66f ts=2026-10-05T16:43:00.3110000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[218] _id=6ac3d3cfde269131f9adfb3f ts=2026-10-05T16:43:58.3840000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[6] _id=6ac3cf7cde269131f9ada67d ts=2026-10-05T16:25:31.4810000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[10] _id=6ac3d0f2de269131f9adbfe9 ts=2026-10-05T16:31:45.3300000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[606] _id=6ac3d7d1de269131f9ae60cd ts=2026-10-05T17:01:04.0430000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 57 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 57} 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[5] _id=6ac3cf7cde269131f9ada67b ts=2026-10-05T16:25:31.4790000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[0] _id=6ac3d0f2de269131f9adbfe5 ts=2026-10-05T16:31:45.3280000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[394] _id=6ac3d64ade269131f9ae38e3 ts=2026-10-05T16:54:33.2570000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 46 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 46} 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[7] _id=6ac3cf95de269131f9ada73b ts=2026-10-05T16:25:56.3240000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[392] _id=6ac3d647de269131f9ae3859 ts=2026-10-05T16:54:30.9510000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[683] _id=6ac5247dde269131f9b52499 ts=2026-10-05T17:04:32.379Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 28 of 164 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[753] _id=6ac5250dde269131f9b52be7 ts=2026-10-06T16:42:53.0680000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[766] _id=6ac5251cde269131f9b52d97 ts=2026-10-06T16:43:07.7350000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[1885] _id=6ac527acde269131f9b5888d ts=2026-10-06T16:54:03.3430000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5803 | 0.0 | 0.576 | 162.592 | 11.244 | 250963.697 | 0.37 | 276 | 13 |
| PuzzlePieceVisibleEvent | 3284 | 0.0 | 0.037 | 237.028 | 1.772 | 433191.856 | 0.25 | 1720 | 6 |
| DialogueEvent | 2494 | 0.0 | 3.412 | 378.305 | 26.475 | 250881.481 | 0.16 | 727 | 12 |
| PlayerPositionEvent | 1916 | 0.0 | 10.003 | 492.303 | 10.541 | 250874.098 | 0.12 | 1 | 12 |
| argumentationNodeEvent | 680 | 0.0 | 0.594 | 1382.131 | 12.278 | 601721.394 | 0.04 | 73 | 4 |
| ObjectInterEvent | 335 | 0.0 | 8.938 | 2815.532 | 356.569 | 338878.556 | 0.02 | 4 | 14 |
| TopographicMapEvent | 163 | 0.026 | 3.435 | 4274.656 | 503.686 | 430739.534 | 0.01 | 2 | 7 |
| Soil Key Puzzle | 117 | 0.006 | 0.976 | 5907.482 | 43.421 | 433462.213 | 0.01 | 6 | 4 |
| questEvent | 90 | 0.0 | 176.746 | 10480.659 | 84532.881 | 251619.189 | 0.01 | 18 | 17 |
| gameWindowFocusEvent | 56 | 2.0 | 442.171 | 16846.846 | 86025.843 | 251189.074 | 0.0 | 0 | 23 |
| argumentationAnswerEvent | 49 | 0.123 | 19.153 | 19180.465 | 84103.707 | 601818.706 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 45 | 1.066 | 307.655 | 20923.401 | 86279.348 | 340926.523 | 0.0 | 0 | 19 |
| DEBUGMenu | 39 | 7.33 | 523.827 | 24180.307 | 87656.087 | 251607.855 | 0.0 | 0 | 19 |
| WaterChamberEvent | 36 | 0.199 | 11.5 | 2089.608 | 68.13 | 74488.612 | 0.03 | 0 | 1 |
| argumentationToolEvent | 26 | 0.065 | 2.63 | 36144.688 | 208784.329 | 601862.565 | 0.0 | 0 | 3 |
| gameStartEvent | 19 | 179.179 | 4884.406 | 49653.862 | 107178.856 | 251618.936 | 0.0 | 0 | 16 |
| soilMachine | 18 | 0.38 | 4.722 | 228.223 | 695.107 | 3759.197 | 0.26 | 0 | 1 |
| DaniEvent | 15 | 0.005 | 2.023 | 5672.515 | 25598.742 | 84868.222 | 0.01 | 4 | 1 |
| TerasGardenBox | 14 | 0.234 | 2.947 | 5.398 | 18.118 | 21.027 | 11.12 | 0 | 0 |
| argumentationEvent | 13 | 0.028 | 133.208 | 72296.467 | 343319.289 | 601710.415 | 0.0 | 1 | 5 |
| chatEvent | 7 | 0.346 | 339.302 | 122187.104 | 566724.988 | 777332.744 | 0.0 | 0 | 3 |
| EndOfUnit | 4 | 78474.437 | 87219.959 | 235466.658 | 598738.848 | 688952.275 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 4 | 1.387 | 1.692 | 2.01 | 3.038 | 3.27 | 29.85 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 15 group(s), 39 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[2117] _id=6ac672fcde269131f9bc79af ts=2026-10-07T16:27:38.4970000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[2118] _id=6ac672fcde269131f9bc79b0 ts=2026-10-07T16:27:38.4970000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[3132] _id=6ac67af6de269131f9bd7fde ts=2026-10-07T17:01:41.4990000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[3133] _id=6ac67af6de269131f9bd7fdf ts=2026-10-07T17:01:41.4990000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[3220] _id=6ac7c47fde269131f9c424ce ts=2026-10-08T16:27:41.0690000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[3221] _id=6ac7c47fde269131f9c424cf ts=2026-10-08T16:27:41.0690000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 48 group(s), 66 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[856] _id=6ac52547de269131f9b5316f ts=2026-10-06T16:43:34.8890000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[861] _id=6ac52547de269131f9b53173 ts=2026-10-06T16:43:34.8890000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[858] _id=6ac52547de269131f9b5317d ts=2026-10-06T16:43:42.2650000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[863] _id=6ac52548de269131f9b53181 ts=2026-10-06T16:43:42.2650000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[835] _id=6ac52548de269131f9b53189 ts=2026-10-06T16:43:42.3250000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[836] _id=6ac52548de269131f9b5318d ts=2026-10-06T16:43:42.3250000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[14972] _id=6ad22dabde269131f9e447af ts=2026-10-16T13:59:07.4780000Z == 6ab9a8e69a8420a1e6b56b1c.jsonl[14973] _id=6ad22dabde269131f9e447b0 ts=2026-10-16T13:59:07.4780000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 39 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[100] _id=6ac3d243de269131f9addcdf ts=2026-10-05T16:37:22.4870000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[101] _id=6ac3d243de269131f9addce2 ts=2026-10-05T16:37:22.4930000Z`; `798ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[653] _id=6ac3d87dde269131f9ae7075 ts=2026-10-05T17:03:56.6180000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[651] _id=6ac3d87ede269131f9ae708d ts=2026-10-05T17:03:57.4160000Z`; `411ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[885] _id=6ac5254dde269131f9b5321f ts=2026-10-06T16:43:57.0440000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[879] _id=6ac5254ede269131f9b5322f ts=2026-10-06T16:43:57.4550000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 97 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[832] _id=6ac52547de269131f9b53163 ts=2026-10-06T16:43:34.7290000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[855] _id=6ac52547de269131f9b53167 ts=2026-10-06T16:43:34.7400000Z`; `64ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[855] _id=6ac52547de269131f9b53167 ts=2026-10-06T16:43:34.7400000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[833] _id=6ac52547de269131f9b53169 ts=2026-10-06T16:43:34.8040000Z`; `1ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[833] _id=6ac52547de269131f9b53169 ts=2026-10-06T16:43:34.8040000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[834] _id=6ac52547de269131f9b5316d ts=2026-10-06T16:43:34.8050000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `548ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12872] _id=6ad1021ede269131f9ddba16 ts=2026-10-15T16:41:02.0110000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[12875] _id=6ad1021ede269131f9ddba20 ts=2026-10-15T16:41:02.5590000Z`; `319ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12954] _id=6ad1025fde269131f9ddc04d ts=2026-10-15T16:42:07.2350000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[12958] _id=6ad1025fde269131f9ddc055 ts=2026-10-15T16:42:07.5540000Z`; `234ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12962] _id=6ad10263de269131f9ddc099 ts=2026-10-15T16:42:10.8950000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[12963] _id=6ad10263de269131f9ddc09d ts=2026-10-15T16:42:11.1290000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[1974] _id=6ac52899de269131f9b5c11d ts=2026-10-06T16:58:00.9030000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[1979] _id=6ac5289ade269131f9b5c14b ts=2026-10-06T16:58:00.9290000Z`; `205ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[1987] _id=6ac528abde269131f9b5c4f9 ts=2026-10-06T16:58:18.5300000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[1993] _id=6ac528abde269131f9b5c503 ts=2026-10-06T16:58:18.7350000Z`; `205ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[2161] _id=6ac6737ede269131f9bc817f ts=2026-10-07T16:29:49.3680000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[2159] _id=6ac6737ede269131f9bc8185 ts=2026-10-07T16:29:49.5730000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `565ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14093] _id=6ad10707de269131f9de38ba ts=2026-10-15T17:01:59.3960000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[14095] _id=6ad10708de269131f9de38cc ts=2026-10-15T17:01:59.9610000Z`; `568ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14102] _id=6ad10708de269131f9de38c2 ts=2026-10-15T17:01:59.6770000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[14105] _id=6ad10708de269131f9de38d6 ts=2026-10-15T17:02:00.2450000Z`; `483ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14095] _id=6ad10708de269131f9de38cc ts=2026-10-15T17:01:59.9610000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[14100] _id=6ad10708de269131f9de38ec ts=2026-10-15T17:02:00.4440000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `857ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[431] _id=6ac3d681de269131f9ae3f6f ts=2026-10-05T16:55:28.6630000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[429] _id=6ac3d682de269131f9ae3f84 ts=2026-10-05T16:55:29.5200000Z`; `186ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[432] _id=6ac3d689de269131f9ae4037 ts=2026-10-05T16:55:36.8980000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[433] _id=6ac3d689de269131f9ae4041 ts=2026-10-05T16:55:37.0840000Z`; `123ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[433] _id=6ac3d689de269131f9ae4041 ts=2026-10-05T16:55:37.0840000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[434] _id=6ac3d689de269131f9ae4047 ts=2026-10-05T16:55:37.2070000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `58ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[6318] _id=6ace6156de269131f9cfca66 ts=2026-10-13T16:50:29.3010000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[6321] _id=6ace6156de269131f9cfca69 ts=2026-10-13T16:50:29.3590000Z`; `28ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12747] _id=6ad10124de269131f9dda95c ts=2026-10-15T16:36:52.5500000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[12750] _id=6ad10124de269131f9dda95f ts=2026-10-15T16:36:52.5780000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 36 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[376] _id=6ac3d61fde269131f9ae3243 ts=2026-10-05T16:53:50.6390000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[374] _id=6ac3d61fde269131f9ae3245 ts=2026-10-05T16:53:50.6780000Z`; `495ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[420] _id=6ac3d67bde269131f9ae3ef9 ts=2026-10-05T16:55:22.7980000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[426] _id=6ac3d67cde269131f9ae3f09 ts=2026-10-05T16:55:23.2930000Z`; `62ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[383] _id=6ac3d6a3de269131f9ae42b6 ts=2026-10-05T16:56:01.3630000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[464] _id=6ac3d6a3de269131f9ae42c1 ts=2026-10-05T16:56:01.4250000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `866ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[404] _id=6ac3d664de269131f9ae3c69 ts=2026-10-05T16:54:59.9640000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[406] _id=6ac3d665de269131f9ae3c75 ts=2026-10-05T16:55:00.8300000Z`; `431ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[4909] _id=6acd0573de269131f9cd10a6 ts=2026-10-12T16:06:10.4820000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[4842] _id=6acd0573de269131f9cd10a8 ts=2026-10-12T16:06:10.9130000Z`; `985ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[6236] _id=6ace6078de269131f9cfb9e0 ts=2026-10-13T16:46:47.7040000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[6238] _id=6ace6079de269131f9cfb9f2 ts=2026-10-13T16:46:48.6890000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[15009] _id=6ad234c9de269131f9e47b1e ts=2026-10-16T14:29:28.6420000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[15010] _id=6ad234c9de269131f9e47b1f ts=2026-10-16T14:29:28.6470000Z`; `5ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[15138] _id=6ad23577de269131f9e47dd7 ts=2026-10-16T14:32:23.0900000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[15136] _id=6ad23577de269131f9e47dd9 ts=2026-10-16T14:32:23.0950000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `866ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[10662] _id=6acfb59ade269131f9d6393e ts=2026-10-14T17:02:17.4220000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[10667] _id=6acfb59ade269131f9d63959 ts=2026-10-14T17:02:18.2880000Z`; `380ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[10667] _id=6acfb59ade269131f9d63959 ts=2026-10-14T17:02:18.2880000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[10668] _id=6acfb59bde269131f9d63975 ts=2026-10-14T17:02:18.6680000Z`; `692ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[11237] _id=6acfc55bde269131f9d6e815 ts=2026-10-14T18:09:30.3590000Z ~ 6ab9a8e69a8420a1e6b56b1c.jsonl[11238] _id=6acfc55bde269131f9d6e822 ts=2026-10-14T18:09:31.0510000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 69h 53m 
  - Evidence: 69h 53m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4509] _id=6ac92e4bde269131f9cad35a ts=2026-10-09T18:11:22.6780000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4832] _id=6acd0523de269131f9cd102a ts=2026-10-12T16:04:50.5330000Z; 25h 18m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4210] _id=6ac7ca52de269131f9c4b225 ts=2026-10-08T16:52:33.3790000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4508] _id=6ac92e40de269131f9cad343 ts=2026-10-09T18:11:11.6170000Z; 24h 14m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4850] _id=6acd052ede269131f9cd102f ts=2026-10-12T16:05:01.3880000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5012] _id=6ace5a15de269131f9cf59f4 ts=2026-10-13T16:19:32.7920000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 34m 
  - Evidence: 23h 34m: 6ab9a8e69a8420a1e6b56b1c.jsonl[1893] _id=6ac527b8de269131f9b58b5d ts=2026-10-06T16:54:15.2840000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[2140] _id=6ac6733cde269131f9bc7d52 ts=2026-10-07T16:28:43.5060000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.005s..0.010s shown 
  - Evidence: 5ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[2143] _id=6ac67340de269131f9bc7da5 ts=2026-10-07T16:28:47.0220000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[2144] _id=6ac67340de269131f9bc7da9 ts=2026-10-07T16:28:47.0270000Z; 6ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[1891] _id=6ac527b5de269131f9b58adb ts=2026-10-06T16:54:12.4040000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[1892] _id=6ac527b5de269131f9b58ae1 ts=2026-10-06T16:54:12.4100000Z; 10ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[2142] _id=6ac6733dde269131f9bc7d6b ts=2026-10-07T16:28:44.4720000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[2139] _id=6ac6733dde269131f9bc7d73 ts=2026-10-07T16:28:44.4820000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 69h 41m 
  - Evidence: 69h 41m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4824] _id=6ac93132de269131f9cae6c0 ts=2026-10-09T18:23:46.3310000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4833] _id=6acd0534de269131f9cd1036 ts=2026-10-12T16:05:07.8120000Z; 25h 7m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4462] _id=6ac7cce8de269131f9c4dd9c ts=2026-10-08T17:03:35.3100000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4522] _id=6ac92e50de269131f9cad374 ts=2026-10-09T18:11:26.2570000Z; 24h 8m: 6ab9a8e69a8420a1e6b56b1c.jsonl[5011] _id=6acd0696de269131f9cd1186 ts=2026-10-12T16:11:01.9810000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5028] _id=6ace5a31de269131f9cf5ad9 ts=2026-10-13T16:20:00.2120000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 727 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12163] _id=6ad0fdafde269131f9dd66b9 ts=2026-10-15T16:22:07.5430000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12164] _id=6ad0fdafde269131f9dd66ba ts=2026-10-15T16:22:07.5430000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12210] _id=6ad0fde7de269131f9dd6bb1 ts=2026-10-15T16:23:03.1310000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12211] _id=6ad0fde7de269131f9dd6bb2 ts=2026-10-15T16:23:03.1310000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12258] _id=6ad0fe15de269131f9dd6edb ts=2026-10-15T16:23:48.8980000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12259] _id=6ad0fe15de269131f9dd6edc ts=2026-10-15T16:23:48.8980000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 22m 
  - Evidence: 191h 22m: 6ab9a8e69a8420a1e6b56b1c.jsonl[586] _id=6ac3d77bde269131f9ae584f ts=2026-10-05T16:59:39.0890000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5111] _id=6ace5ab4de269131f9cf5f16 ts=2026-10-13T16:22:11.3640000Z; 24h 18m: 6ab9a8e69a8420a1e6b56b1c.jsonl[5111] _id=6ace5ab4de269131f9cf5f16 ts=2026-10-13T16:22:11.3640000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[9202] _id=6acfb09dde269131f9d5b029 ts=2026-10-14T16:41:00.7950000Z; 24h 8m: 6ab9a8e69a8420a1e6b56b1c.jsonl[9202] _id=6acfb09dde269131f9d5b029 ts=2026-10-14T16:41:00.7950000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[13201] _id=6ad1041bde269131f9dde6f4 ts=2026-10-15T16:49:31.2830000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 69h 42m 
  - Evidence: 69h 42m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4811] _id=6ac930dede269131f9cae574 ts=2026-10-09T18:22:21.7520000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4852] _id=6acd0533de269131f9cd1032 ts=2026-10-12T16:05:05.4490000Z; 25h 6m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4500] _id=6ac7cd20de269131f9c4e00d ts=2026-10-08T17:04:31.7510000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4511] _id=6ac92e50de269131f9cad369 ts=2026-10-09T18:11:26.2330000Z; 24h 9m: 6ab9a8e69a8420a1e6b56b1c.jsonl[5003] _id=6acd068ade269131f9cd117b ts=2026-10-12T16:10:49.4240000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5017] _id=6ace5a29de269131f9cf5a8b ts=2026-10-13T16:19:51.4640000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 276 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[10140] _id=6acfb37dde269131f9d6015e ts=2026-10-14T16:53:17.2410000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[10141] _id=6acfb37dde269131f9d6015f ts=2026-10-14T16:53:17.2410000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[11119] _id=6acfc4d8de269131f9d6e56a ts=2026-10-14T18:07:19.5920000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[11120] _id=6acfc4d8de269131f9d6e56b ts=2026-10-14T18:07:19.5920000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14253] _id=6ad22a5ede269131f9e3ec32 ts=2026-10-16T13:45:01.7480000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14254] _id=6ad22a5ede269131f9e3ec33 ts=2026-10-16T13:45:01.7480000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 7m 
  - Evidence: 94h 7m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4791] _id=6ac930bfde269131f9cae41f ts=2026-10-09T18:21:51.2860000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5247] _id=6ace5c7ede269131f9cf733f ts=2026-10-13T16:29:49.8420000Z; 25h 12m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4443] _id=6ac7ccf9de269131f9c4de76 ts=2026-10-08T17:03:52.4500000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4618] _id=6ac92f62de269131f9caddc5 ts=2026-10-09T18:16:01.6890000Z; 24h 11m: 6ab9a8e69a8420a1e6b56b1c.jsonl[1797] _id=6ac5268fde269131f9b5610f ts=2026-10-06T16:49:18.8230000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[3096] _id=6ac67aa7de269131f9bd7613 ts=2026-10-07T17:00:22.7280000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12048] _id=6ad0fcd8de269131f9dd5729 ts=2026-10-15T16:18:31.7340000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12049] _id=6ad0fcd8de269131f9dd572a ts=2026-10-15T16:18:31.7340000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12084] _id=6ad0fd14de269131f9dd59fb ts=2026-10-15T16:19:32.3030000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12085] _id=6ad0fd14de269131f9dd59fc ts=2026-10-15T16:19:32.3030000Z; 1ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[11955] _id=6acfc868de269131f9d705a7 ts=2026-10-14T18:22:31.6640000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[11957] _id=6acfc868de269131f9d705a8 ts=2026-10-14T18:22:31.6650000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 69h 41m 
  - Evidence: 69h 41m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4825] _id=6ac93133de269131f9cae6c2 ts=2026-10-09T18:23:47.3050000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4851] _id=6acd0533de269131f9cd1031 ts=2026-10-12T16:05:01.4030000Z; 25h 6m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4497] _id=6ac7cd1ede269131f9c4dfed ts=2026-10-08T17:04:29.9800000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4510] _id=6ac92e50de269131f9cad368 ts=2026-10-09T18:11:22.6890000Z; 24h 8m: 6ab9a8e69a8420a1e6b56b1c.jsonl[5010] _id=6acd0690de269131f9cd1182 ts=2026-10-12T16:10:55.7310000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5016] _id=6ace5a29de269131f9cf5a8a ts=2026-10-13T16:19:47.5650000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[4204] _id=6ac7ca2dde269131f9c4b0b9 ts=2026-10-08T16:51:56.1930000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4205] _id=6ac7ca46de269131f9c4b1aa ts=2026-10-08T16:51:56.193Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 19m 
  - Evidence: 120h 19m: 6ab9a8e69a8420a1e6b56b1c.jsonl[3887] _id=6ac7c6abde269131f9c45ec6 ts=2026-10-08T16:36:55.6910000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6631] _id=6ace62d1de269131f9cfe44b ts=2026-10-13T16:56:47.5470000Z; 47h 42m: 6ab9a8e69a8420a1e6b56b1c.jsonl[1775] _id=6ac52659de269131f9b558c9 ts=2026-10-06T16:48:22.9630000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[3344] _id=6ac7c554de269131f9c4328a ts=2026-10-08T16:31:15.5090000Z; 23h 3m: 6ab9a8e69a8420a1e6b56b1c.jsonl[7496] _id=6ace6491de269131f9d010d5 ts=2026-10-13T17:04:16.3320000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[7629] _id=6acfa8d2de269131f9d53619 ts=2026-10-14T16:07:44.3300000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1720 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[10000] _id=6acfb2f8de269131f9d5f49e ts=2026-10-14T16:51:00.6980000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[10033] _id=6acfb2f8de269131f9d5f4a0 ts=2026-10-14T16:51:00.6980000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[10002] _id=6acfb2f4de269131f9d5f427 ts=2026-10-14T16:50:58.1730000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[10003] _id=6acfb2f4de269131f9d5f428 ts=2026-10-14T16:50:58.1730000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[10003] _id=6acfb2f4de269131f9d5f428 ts=2026-10-14T16:50:58.1730000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[9999] _id=6acfb2f4de269131f9d5f42a ts=2026-10-14T16:50:58.1730000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6ab9a8e69a8420a1e6b56b1c.jsonl[3327] _id=6ac7c537de269131f9c42fc8 ts=2026-10-08T16:30:46.7440000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6554] _id=6ace626dde269131f9cfdfe9 ts=2026-10-13T16:55:08.9570000Z; 24h 11m: 6ab9a8e69a8420a1e6b56b1c.jsonl[1799] _id=6ac52692de269131f9b56131 ts=2026-10-06T16:49:21.7800000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[3097] _id=6ac67aa7de269131f9bd7608 ts=2026-10-07T17:00:22.7230000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b1c.jsonl[6581] _id=6ace628dde269131f9cfe16e ts=2026-10-13T16:55:40.7170000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[9309] _id=6acfb264de269131f9d5de12 ts=2026-10-14T16:48:35.9840000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.006s..0.008s shown 
  - Evidence: 6ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[6572] _id=6ace6282de269131f9cfe117 ts=2026-10-13T16:55:29.9890000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6576] _id=6ace6283de269131f9cfe119 ts=2026-10-13T16:55:29.9950000Z; 8ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[3260] _id=6ac7c4e5de269131f9c429a3 ts=2026-10-08T16:29:24.2230000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[3265] _id=6ac7c4e5de269131f9c429aa ts=2026-10-08T16:29:24.2310000Z; 8ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[3285] _id=6ac7c4efde269131f9c42a33 ts=2026-10-08T16:29:34.3790000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[3283] _id=6ac7c4efde269131f9c42a37 ts=2026-10-08T16:29:34.3870000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4121] _id=6ac7c8e0de269131f9c49cd2 ts=2026-10-08T16:46:23.9590000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5160] _id=6ace5b74de269131f9cf65a8 ts=2026-10-13T16:25:23.4930000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b1c.jsonl[6426] _id=6ace61e1de269131f9cfd33f ts=2026-10-13T16:52:48.6020000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[8958] _id=6acfaf02de269131f9d58d38 ts=2026-10-14T16:34:10.4080000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b1c.jsonl[2965] _id=6ac67a44de269131f9bd6aa4 ts=2026-10-07T16:58:42.9940000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[3233] _id=6ac7c489de269131f9c42525 ts=2026-10-08T16:27:52.6290000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.036s shown 
  - Evidence: 26ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[1974] _id=6ac52899de269131f9b5c11d ts=2026-10-06T16:58:00.9030000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[1979] _id=6ac5289ade269131f9b5c14b ts=2026-10-06T16:58:00.9290000Z; 36ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[1965] _id=6ac52899de269131f9b5c111 ts=2026-10-06T16:58:00.8670000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[1974] _id=6ac52899de269131f9b5c11d ts=2026-10-06T16:58:00.9030000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 20h 41m 
  - Evidence: 20h 41m: 6ab9a8e69a8420a1e6b56b1c.jsonl[14234] _id=6ad1077ade269131f9de4397 ts=2026-10-15T17:03:53.6100000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14287] _id=6ad22a72de269131f9e3ee4b ts=2026-10-16T13:45:22.2220000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 10m 
  - Evidence: 167h 10m: 6ab9a8e69a8420a1e6b56b1c.jsonl[488] _id=6ac3d6ccde269131f9ae467b ts=2026-10-05T16:56:43.9330000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4939] _id=6acd05a7de269131f9cd10f6 ts=2026-10-12T16:07:02.6390000Z; 47h 31m: 6ab9a8e69a8420a1e6b56b1c.jsonl[6323] _id=6ace6156de269131f9cfca62 ts=2026-10-13T16:50:29.2620000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12162] _id=6ad0fdafde269131f9dd66b5 ts=2026-10-15T16:22:07.5260000Z; 24h 43m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4939] _id=6acd05a7de269131f9cd10f6 ts=2026-10-12T16:07:02.6390000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6323] _id=6ace6156de269131f9cfca62 ts=2026-10-13T16:50:29.2620000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 8m 
  - Evidence: 167h 8m: 6ab9a8e69a8420a1e6b56b1c.jsonl[500] _id=6ac3d6ccde269131f9ae4681 ts=2026-10-05T16:56:43.9500000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4856] _id=6acd053bde269131f9cd103c ts=2026-10-12T16:05:14.3650000Z; 47h 30m: 6ab9a8e69a8420a1e6b56b1c.jsonl[6321] _id=6ace6156de269131f9cfca69 ts=2026-10-13T16:50:29.3590000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12127] _id=6ad0fd88de269131f9dd62c3 ts=2026-10-15T16:21:27.8980000Z; 24h 39m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4940] _id=6acd05a7de269131f9cd10f8 ts=2026-10-12T16:07:02.6560000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6221] _id=6ace6066de269131f9cfb83e ts=2026-10-13T16:46:29.5240000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.028s..0.028s shown 
  - Evidence: 28ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[12747] _id=6ad10124de269131f9dda95c ts=2026-10-15T16:36:52.5500000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12750] _id=6ad10124de269131f9dda95f ts=2026-10-15T16:36:52.5780000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 8m 
  - Evidence: 167h 8m: 6ab9a8e69a8420a1e6b56b1c.jsonl[487] _id=6ac3d6cade269131f9ae4649 ts=2026-10-05T16:56:41.5990000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4837] _id=6acd0543de269131f9cd1043 ts=2026-10-12T16:05:22.9930000Z; 47h 31m: 6ab9a8e69a8420a1e6b56b1c.jsonl[6304] _id=6ace6154de269131f9cfca46 ts=2026-10-13T16:50:27.3600000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[12133] _id=6ad0fd89de269131f9dd62d2 ts=2026-10-15T16:21:28.6730000Z; 24h 39m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4950] _id=6acd05a5de269131f9cd10f4 ts=2026-10-12T16:07:00.4640000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6224] _id=6ace6069de269131f9cfb87f ts=2026-10-13T16:46:32.8430000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 73 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[4894] _id=6acd056ade269131f9cd1089 ts=2026-10-12T16:06:01.0940000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4895] _id=6acd056ade269131f9cd108a ts=2026-10-12T16:06:01.0940000Z; 4ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14867] _id=6ad22d2bde269131f9e43b3e ts=2026-10-16T13:56:59.1920000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14868] _id=6ad22d2bde269131f9e43b40 ts=2026-10-16T13:56:59.1960000Z; 5ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14866] _id=6ad22d2dde269131f9e43b7d ts=2026-10-16T13:57:01.3290000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14857] _id=6ad22d2dde269131f9e43b84 ts=2026-10-16T13:57:01.3340000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 11m 
  - Evidence: 167h 11m: 6ab9a8e69a8420a1e6b56b1c.jsonl[409] _id=6ac3d66bde269131f9ae3d0d ts=2026-10-05T16:55:06.7410000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4841] _id=6acd0572de269131f9cd10a4 ts=2026-10-12T16:06:09.3060000Z; 69h 6m: 6ab9a8e69a8420a1e6b56b1c.jsonl[6307] _id=6ace6145de269131f9cfc914 ts=2026-10-13T16:50:12.9810000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14829] _id=6ad22d06de269131f9e437e2 ts=2026-10-16T13:56:21.7910000Z; 24h 40m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4845] _id=6acd0579de269131f9cd10b0 ts=2026-10-12T16:06:16.8200000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[6236] _id=6ace6078de269131f9cfb9e0 ts=2026-10-13T16:46:47.7040000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 55m 
  - Evidence: 215h 55m: 6ab9a8e69a8420a1e6b56b1c.jsonl[1896] _id=6ac527bcde269131f9b58c3b ts=2026-10-06T16:54:19.6220000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[13203] _id=6ad10430de269131f9dde96d ts=2026-10-15T16:49:52.3660000Z; 20h 55m: 6ab9a8e69a8420a1e6b56b1c.jsonl[13203] _id=6ad10430de269131f9dde96d ts=2026-10-15T16:49:52.3660000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14266] _id=6ad22a5bde269131f9e3ebf5 ts=2026-10-16T13:44:59.2580000Z; 38m 46s: 6ab9a8e69a8420a1e6b56b1c.jsonl[14595] _id=6ad22bafde269131f9e412f3 ts=2026-10-16T13:50:38.5600000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[15007] _id=6ad234c5de269131f9e47b17 ts=2026-10-16T14:29:25.2290000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 69h 53m 
  - Evidence: 69h 53m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4505] _id=6ac92e40de269131f9cad346 ts=2026-10-09T18:11:11.7710000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4831] _id=6acd0523de269131f9cd102d ts=2026-10-12T16:04:50.7070000Z; 25h 18m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4208] _id=6ac7ca46de269131f9c4b1b8 ts=2026-10-08T16:52:21.8130000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4505] _id=6ac92e40de269131f9cad346 ts=2026-10-09T18:11:11.7710000Z; 24h 14m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4831] _id=6acd0523de269131f9cd102d ts=2026-10-12T16:04:50.7070000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5014] _id=6ace5a15de269131f9cf59f9 ts=2026-10-13T16:19:32.9600000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 69h 46m 
  - Evidence: 69h 46m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4682] _id=6ac92feede269131f9cae0b9 ts=2026-10-09T18:18:21.6330000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4830] _id=6acd0523de269131f9cd102c ts=2026-10-12T16:04:50.7070000Z; 25h 18m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4207] _id=6ac7ca46de269131f9c4b1b7 ts=2026-10-08T16:52:21.8130000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4504] _id=6ac92e40de269131f9cad345 ts=2026-10-09T18:11:11.7700000Z; 24h 14m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4830] _id=6acd0523de269131f9cd102c ts=2026-10-12T16:04:50.7070000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5013] _id=6ace5a15de269131f9cf59f8 ts=2026-10-13T16:19:32.9600000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4681] _id=6ac92fe9de269131f9cae0af ts=2026-10-09T18:18:16.6580000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[7017] _id=6ace63a8de269131f9cff447 ts=2026-10-13T17:00:23.1810000Z; 25h 13m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4496] _id=6ac7cd25de269131f9c4e025 ts=2026-10-08T17:04:36.5990000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4681] _id=6ac92fe9de269131f9cae0af ts=2026-10-09T18:18:16.6580000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b1c.jsonl[683] _id=6ac5247dde269131f9b52499 ts=2026-10-05T17:04:32.379Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[2111] _id=6ac672e4de269131f9bc77d7 ts=2026-10-06T17:04:36.358Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 69h 53m 
  - Evidence: 69h 53m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4524] _id=6ac92e50de269131f9cad376 ts=2026-10-09T18:11:26.3050000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4854] _id=6acd0533de269131f9cd1034 ts=2026-10-12T16:05:05.4940000Z; 25h 18m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4214] _id=6ac7ca58de269131f9c4b270 ts=2026-10-08T16:52:38.5620000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[4524] _id=6ac92e50de269131f9cad376 ts=2026-10-09T18:11:26.3050000Z; 24h 11m: 6ab9a8e69a8420a1e6b56b1c.jsonl[4962] _id=6acd060fde269131f9cd1129 ts=2026-10-12T16:08:46.9160000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[5044] _id=6ace5a29de269131f9cf5aa0 ts=2026-10-13T16:19:51.5100000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[13994] _id=6ad10685de269131f9de2d0d ts=2026-10-15T16:59:48.7040000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[13995] _id=6ad10685de269131f9de2d0e ts=2026-10-15T16:59:48.7040000Z; 0ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14972] _id=6ad22dabde269131f9e447af ts=2026-10-16T13:59:07.4780000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14973] _id=6ad22dabde269131f9e447b0 ts=2026-10-16T13:59:07.4780000Z; 1ms: 6ab9a8e69a8420a1e6b56b1c.jsonl[14434] _id=6ad22af3de269131f9e3fb45 ts=2026-10-16T13:47:30.8560000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[14435] _id=6ad22af3de269131f9e3fb46 ts=2026-10-16T13:47:30.8570000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 2m 
  - Evidence: 1h 2m: 6ab9a8e69a8420a1e6b56b1c.jsonl[10673] _id=6acfb59cde269131f9d6398a ts=2026-10-14T17:02:19.4570000Z -> 6ab9a8e69a8420a1e6b56b1c.jsonl[10924] _id=6acfc44bde269131f9d6e2c5 ts=2026-10-14T18:04:58.6540000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[334] _id=6ac3d5c3de269131f9ae2aab ts=2026-10-05T16:52:19.1500000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[505] _id=6ac3d6e0de269131f9ae4886 ts=2026-10-05T16:57:03.1960000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[2089] _id=6ac529e4de269131f9b60113 ts=2026-10-06T17:03:31.1110000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 26 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[943] _id=6ac5255cde269131f9b53391 ts=2026-10-06T16:44:10.7390000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[1020] _id=6ac52579de269131f9b5369d ts=2026-10-06T16:44:40.1370000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[1042] _id=6ac5257ede269131f9b5372f ts=2026-10-06T16:44:44.1220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 40 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[821] _id=6ac52544de269131f9b530ab ts=2026-10-06T16:42:35.6920000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[794] _id=6ac52545de269131f9b530f1 ts=2026-10-06T16:42:46.3280000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[777] _id=6ac52545de269131f9b5310b ts=2026-10-06T16:42:46.3280000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[6321] _id=6ace6156de269131f9cfca69 ts=2026-10-13T16:50:29.3590000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[12750] _id=6ad10124de269131f9dda95f ts=2026-10-15T16:36:52.5780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[374] _id=6ac3d61fde269131f9ae3245 ts=2026-10-05T16:53:50.6780000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[464] _id=6ac3d6a3de269131f9ae42c1 ts=2026-10-05T16:56:01.4250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[13203] _id=6ad10430de269131f9dde96d ts=2026-10-15T16:49:52.3660000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[14266] _id=6ad22a5bde269131f9e3ebf5 ts=2026-10-16T13:44:59.2580000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[14595] _id=6ad22bafde269131f9e412f3 ts=2026-10-16T13:50:38.5600000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[10821] _id=6acfc3d7de269131f9d6e1e1 ts=2026-10-14T18:03:03.0040000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[14438] _id=6ad22af3de269131f9e3fb40 ts=2026-10-16T13:47:30.8150000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[14433] _id=6ad22af3de269131f9e3fb44 ts=2026-10-16T13:47:30.8360000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 137 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[953] _id=6ac5255dde269131f9b533a3 ts=2026-10-06T16:44:11.4400000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[963] _id=6ac52566de269131f9b5344d ts=2026-10-06T16:44:20.4180000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[973] _id=6ac52569de269131f9b53485 ts=2026-10-06T16:44:24.2180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 280 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[772] _id=6ac52544de269131f9b530bb ts=2026-10-06T16:42:35.6920000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[774] _id=6ac52545de269131f9b530e3 ts=2026-10-06T16:42:35.6920000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[829] _id=6ac52547de269131f9b53151 ts=2026-10-06T16:43:34.6530000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 36 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[1974] _id=6ac52899de269131f9b5c11d ts=2026-10-06T16:58:00.9030000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[1979] _id=6ac5289ade269131f9b5c14b ts=2026-10-06T16:58:00.9290000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[2048] _id=6ac5294cde269131f9b5e42a ts=2026-10-06T17:00:59.1860000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[404] _id=6ac3d664de269131f9ae3c69 ts=2026-10-05T16:54:59.9640000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[406] _id=6ac3d665de269131f9ae3c75 ts=2026-10-05T16:55:00.8300000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[407] _id=6ac3d668de269131f9ae3ca9 ts=2026-10-05T16:55:03.3000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 482 start, 473 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 17 unmatched 'BecameCameraCentered' (totals: 765 open, 774 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 66 unmatched 'BecameVisible' (totals: 886 open, 860 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 39 open, 37 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 19 unmatched 'argumentationToolOpen' (totals: 23 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 55 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 442 of 15260 adjacent _id pairs reverse in client time; worst 71.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b1c.jsonl[795] _id=6ac52540de269131f9b5304b ts=2026-10-06T16:43:43.9630000Z`; `6ab9a8e69a8420a1e6b56b1c.jsonl[796] _id=6ac52541de269131f9b53057 ts=2026-10-06T16:42:32.1340000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.87s, min -84957.24s, max -0.23s over 15261 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b1c\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

No coverage-related findings.

## 9. Event-Type Details

### `InputEvent` — 5804 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1318); Unit 3 Dev (1052); Unit 3 Dungeon Dev (1006); Unit 4 Dev - Dungeon (891); Unit 5 Dev - Dungeon (661); Unit 4 Dev (511); Unit 5 Dev (181); Unit 4 Dev - Anderson Base (113); Unit 1 Dev (71)
- **Intervals:** median 0.58s (p5 0.06s / p95 11.24s, n=5803)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5804/5804 records)
    "pressed"  x5804
data.actionType  (string, 5804/5804 records)
    "Move"  x4466
    "Interact"  x921
    "Jump"  x188
    "Ascend"  x118
    "Hoverboard"  x78
    "Pause"  x11
    "Map"  x7
    "SkipCinematic"  x7
    "Sprint"  x7
    "ToggleDebug"  x1
data.key  (string, 5804/5804 records, 22 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5804/5804 records)
    "Player"  x4879
    "Drone"  x925
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3285 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1270); Unit 3 Dungeon Dev (854); Unit 4 Dev (736); Unit 5 Dev - Dungeon (425)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.77s, n=3284)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3285/3285 records)
    "BecameVisible"  x886
    "BecameInvisible"  x860
    "BecameCameraUncentered"  x774
    "BecameCameraCentered"  x765
data.pieceId  (string, 3285/3285 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3285/3285 records)
    1975 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2495 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (812); Unit 3 Dev (328); Unit 4 Dev (269); Unit 5 Dev (244); Unit 1 Dev (219); Unit 4 Dev - Anderson Base (213); Unit 3 Dungeon Dev (180); Unit 4 Dev - Dungeon (146); Unit 5 Dev - Dungeon (84)
- **eventKey:** present on 1540 of 2495 records
- **Intervals:** median 3.41s (p5 0.00s / p95 26.47s, n=2494)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1540; [conversationId, dialogueEventType] x955
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2495/2495 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2495/2495 records)
    "DialogueNodeEvent"  x1540
    "DialogueStartEvent"  x482
    "DialogueFinishEvent"  x473
data.nodeId  (number, 1540/2495 records)
    numeric range 0 .. 290 (229 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1928 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (689); Unit 3 Dev (244); Unit 4 Dev (167); Unit 1 Dev (165); Unit 3 Dungeon Dev (163); Unit 4 Dev - Anderson Base (154); Unit 4 Dev - Dungeon (126); Unit 5 Dev - Dungeon (119); Unit 5 Dev (101)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.54s, n=1916)
- **Fields under `data`:**

```text
data.position  (object, 1928/1928 records)
data.position.x  (number, 1928/1928 records)
    numeric range -684.302 .. 1556.24 (728 unique)
data.position.y  (number, 1928/1928 records)
    numeric range -114.115 .. 222.652 (547 unique)
data.position.z  (number, 1928/1928 records)
    numeric range -1139.01 .. 2181.47 (727 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 681 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (373); Unit 5 Dev (98); Unit 2 Prod (Refactor) (75); Unit 1 Dev (74); Unit 3 Dev (61)
- **Intervals:** median 0.59s (p5 0.04s / p95 12.28s, n=680)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 681/681 records)
    "argumentationNodeHoverEnd"  x284
    "argumentationNodeHoverStart"  x282
    "argumentationNodeAdd"  x67
    "argumentationNodeRemove"  x48
data.argumentationTitle  (string, 681/681 records)
    "Unit 4 - Flooding"  x373
    "Unit 5"  x98
    "Unit 2 – Watershed"  x75
    "Unit 1 - Freshwater"  x65
    "Unit 3 - Pollution Upstream"  x61
    "Unit 1 - Argumentation Tutorial"  x9
data.nodeName  (string, 681/681 records)
    "B"  x108
    "C"  x98
    "D"  x96
    "A"  x95
    "II"  x79
    "I"  x53
    "1"  x49
    "3"  x43
    "4"  x28
    "2"  x23
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 336 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (92); Unit 3 Dungeon Dev (66); Unit 2 Prod (Refactor) (65); Unit 5 Dev - Dungeon (33); Unit 4 Dev (29); Unit 4 Dev - Anderson Base (14); Unit 5 Dev (14); Unit 3 Dev (12); Unit 1 Dev (11)
- **Intervals:** median 8.94s (p5 0.36s / p95 356.57s, n=335)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 336/336 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 336/336 records)
    111 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 164 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (113); Unit 3 Dev (47); Unit 4 Dev (4)
- **Intervals:** median 3.44s (p5 0.57s / p95 503.69s, n=163)
- **`data` key-set variants:** [actionType, featureUsed] x76; [actionType, featureUsed, location] x60; [actionType, featureUsed, legendName] x28
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 164/164 records)
    "WaypointMoveEvent"  x54
    "MapOpenEvent"  x39
    "MapCloseEvent"  x37
    "Selected"  x23
    "WaypointSetEvent"  x6
    "Unselected"  x5
data.featureUsed  (string, 164/164 records)
    "Map"  x76
    "Waypoint"  x60
    "Legend"  x28
data.legendName  (string, 28/164 records)
    "0 ft"  x10
    "Water"  x8
    "90 ft"  x3
    "30 ft"  x2
    "120 ft"  x1
    "180 ft"  x1
    "210 ft"  x1
    "270 ft"  x1
    "360 ft"  x1
data.location  (object, 60/164 records)
data.location.x  (number, 60/164 records)
    numeric range -326.441 .. 583.181 (47 unique)
data.location.y  (number, 60/164 records)
    numeric range -280.205 .. 363.7 (51 unique)
data.location.z  (number, 60/164 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 118 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (86); Unit 3 Dev (22); Unit 4 Dev (10)
- **Intervals:** median 0.98s (p5 0.10s / p95 43.42s, n=117)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x108; [Soil Key Puzzle Status, Unit] x10
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/118 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/118 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 108/118 records)
    "RightDrag"  x56
    "LeftDrag"  x52
data.currentSoilType  (string, 108/118 records)
    "CLAYROCK"  x22
    "CLAY"  x21
    "CLAYSAND"  x18
    "SAND"  x17
    "SANDGRAVEL"  x14
    "BEDROCK"  x9
    "GRAVEL"  x7
data.isCorrectSelection  (string, 108/118 records)
    "false"  x91
    "true"  x17
data.waterLevelStatus  (string, 108/118 records)
    "TooHigh"  x74
    "Proper"  x18
    "TooLow"  x16
data.waterRetentionChange  (string, 108/118 records)
    "Increase"  x63
    "Decrease"  x28
    "NoChange"  x17
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 91 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev - Dungeon (13); Unit 1 Dev (12); Unit 5 Dev - Dungeon (12); Unit 3 Dev (9); Unit 5 Dev (9); Unit 4 Dev (8); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (4)
- **eventKey:** present on 91 of 91 records
- **Intervals:** median 176.75s (p5 0.01s / p95 84532.88s, n=90)
- **`data` key-set variants:** [questEventType, questID, questName] x55; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 91/91 records)
    "questActiveEvent"  x55
    "questFinishEvent"  x36
data.questID  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/91 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 57 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 4 Dev (8); Unit 2 Prod (Refactor) (7); Unit 4 Dev - Anderson Base (6); Unit 3 Dungeon Dev (4); Unit 4 Dev - Dungeon (4); Unit 3 Dev (3); Unit 5 Dev - Dungeon (3); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 442.17s (p5 9.39s / p95 86025.84s, n=56)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 57/57 records)
    true  x57
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 50 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (30); Unit 1 Dev (11); Unit 5 Dev (7); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 19.15s (p5 0.28s / p95 84103.71s, n=49)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "submitAnswerEvent"  x50
data.answerSubmitted  (string, 50/50 records)
    27 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 50/50 records)
    "Unit 4 - Flooding"  x30
    "Unit 1 - Freshwater"  x10
    "Unit 5"  x7
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 46 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 4 Dev (8); Unit 4 Dev - Anderson Base (8); Unit 3 Dungeon Dev (5); Unit 4 Dev - Dungeon (4); Unit 5 Dev - Dungeon (4); Unit 3 Dev (3); MainMenu (1); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 307.65s (p5 2.98s / p95 86279.35s, n=45)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 46/46 records)
    false  x46
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 40 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (16); Unit 2 Prod (Refactor) (8); Unit 3 Dungeon Dev (3); Unit 4 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 3 Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1)
- **Intervals:** median 523.83s (p5 7.74s / p95 87656.09s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "DebugMenuStateChanged"  x40
data.isOpened  (bool, 40/40 records)
    false  x40
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 37 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (37)
- **Intervals:** median 11.50s (p5 0.28s / p95 68.13s, n=36)
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "On"  x25
    "Off"  x12
data.floor  (string, 37/37 records)
    "3"  x21
    "4"  x10
    "1"  x3
    "2"  x3
data.machineNumber  (string, 37/37 records)
    "One"  x35
    "Two"  x2
data.machineType  (string, 37/37 records)
    "Condenser"  x19
    "DualChamber_Evaporator"  x7
    "Evaporator"  x6
    "VentSwitch"  x3
    "DualChamber_Condenser"  x2
data.room  (string, 37/37 records)
    "2"  x15
    "1"  x9
    "3"  x9
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 27 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (11); Unit 1 Dev (9); Unit 2 Prod (Refactor) (6); Unit 5 Dev (1)
- **Intervals:** median 2.63s (p5 0.20s / p95 208784.33s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "argumentationToolOpen"  x23
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 27/27 records)
    "Unit 3 - Pollution Upstream"  x11
    "Unit 1 - Freshwater"  x7
    "Unit 2 – Watershed"  x6
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x1
data.toolName  (string, 27/27 records)
    "BackingInfoPanel - Pollution Site Data"  x8
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Watershed Graph"  x4
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 4884.41s (p5 354.38s / p95 107178.86s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 4.72s (p5 0.65s / p95 695.11s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Gravel"  x7
    "Sand"  x5
    "Clay"  x4
    "Bedrock"  x3
data.floor  (string, 19/19 records)
    "4"  x7
    "3"  x6
    "5"  x6
data.machine  (string, 19/19 records)
    "1"  x18
    "2"  x1
data.row  (string, 19/19 records)
    "TopRow"  x16
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 16 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (16)
- **Intervals:** median 2.02s (p5 0.01s / p95 25598.74s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "Close"  x8
    "Open"  x8
data.toolName  (string, 16/16 records, 12 empty-string)
    ""  x12
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 2.95s (p5 0.29s / p95 18.12s, n=14)
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records, 5 empty-string)
    "cameraPlaced"  x10
    ""  x5
data.boxId  (string, 15/15 records)
    "0"  x6
    "2"  x5
    "1"  x4
data.soilType  (string, 15/15 records)
    "Sand"  x6
    "Clay"  x4
    "Gravel"  x4
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 133.21s (p5 0.05s / p95 343319.29s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 8 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 339.30s (p5 0.54s / p95 566724.99s, n=7)
- **`data` key-set variants:** [actionType, chatID] x7; [actionKey, chatID] x1
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 1/8 records)
    "ScrollStop"  x1
data.actionType  (string, 7/8 records)
    "Close"  x5
    "Open"  x1
    "ScrollStart"  x1
data.chatID  (string, 8/8 records)
    "NA"  x6
    "[18-89, 18-91, 18-92, 18-93, 18-95, 18-98]"  x1
    "[18-92, 18-93, 18-95, 18-98, 18-283]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 87219.96s (p5 79739.84s / p95 598738.85s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 5/5 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `SolarStillDesignEvent` — 5 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (5)
- **Intervals:** median 1.69s (p5 1.43s / p95 3.04s, n=4)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x4; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "optionSelected"  x4
    "DesignSubmitted"  x1
data.designSelections  (object, 1/5 records)
data.designSelections.glassRoofTemperature  (string, 1/5 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/5 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/5 records)
    "Tilted In"  x1
data.featureUsed  (string, 5/5 records)
    "RoofStyle"  x2
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 4/5 records)
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (86 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (23x); "Unselected" (5x); "WaypointMoveEvent" (54x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (28x); "Waypoint" (60x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (48x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*