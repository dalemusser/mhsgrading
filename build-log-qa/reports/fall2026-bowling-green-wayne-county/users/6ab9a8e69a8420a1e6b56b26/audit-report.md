# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b26

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b26
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b26.jsonl
- **Records:** 13748 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b26
- **Time span:** 2026-10-05T16:26:02.204000+00:00 .. 2026-10-16T16:27:21.014000+00:00 (264h 1m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b26\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 13748 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 92 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6129 | 44.58 | 1 | 9 | 0 | 2026-10-05T16:32:00.839000+00:00 | 2026-10-16T16:27:21.014000+00:00 | 263h 55m |
| PuzzlePieceVisibleEvent | 2736 | 19.9 | 1 | 4 | 0 | 2026-10-06T16:50:21.230000+00:00 | 2026-10-15T20:55:33.628000+00:00 | 220h 5m |
| DialogueEvent | 2187 | 15.91 | 1 | 9 | 1367 | 2026-10-05T16:32:17.291000+00:00 | 2026-10-16T16:27:14.782000+00:00 | 263h 54m |
| PlayerPositionEvent | 1666 | 12.12 | 1 | 9 | 0 | 2026-10-05T16:31:57.410000+00:00 | 2026-10-16T16:27:16.990000+00:00 | 263h 55m |
| ObjectInterEvent | 341 | 2.48 | 1 | 9 | 0 | 2026-10-05T16:37:47.672000+00:00 | 2026-10-16T16:27:21.014000+00:00 | 263h 49m |
| argumentationNodeEvent | 315 | 2.29 | 1 | 5 | 0 | 2026-10-05T16:54:28.499000+00:00 | 2026-10-15T21:11:14.231000+00:00 | 244h 16m |
| questEvent | 89 | 0.65 | 1 | 9 | 89 | 2026-10-05T16:32:17.266000+00:00 | 2026-10-16T16:23:49.195000+00:00 | 263h 51m |
| TopographicMapEvent | 61 | 0.44 | 1 | 2 | 0 | 2026-10-06T16:51:13.229000+00:00 | 2026-10-14T16:32:06.364000+00:00 | 191h 40m |
| Soil Key Puzzle | 38 | 0.28 | 1 | 3 | 0 | 2026-10-06T16:58:51.994000+00:00 | 2026-10-14T16:47:39.367000+00:00 | 191h 48m |
| DEBUGMenu | 34 | 0.25 | 1 | 9 | 0 | 2026-10-05T16:31:57.394000+00:00 | 2026-10-16T16:16:13.979000+00:00 | 263h 44m |
| soilMachine | 26 | 0.19 | 1 | 1 | 0 | 2026-10-14T17:00:15.453000+00:00 | 2026-10-15T16:28:03.728000+00:00 | 23h 27m |
| WaterChamberEvent | 19 | 0.14 | 1 | 1 | 0 | 2026-10-15T20:54:37.218000+00:00 | 2026-10-15T21:03:02.693000+00:00 | 8m 25s |
| TerasGardenBox | 18 | 0.13 | 1 | 1 | 0 | 2026-10-15T16:49:43.302000+00:00 | 2026-10-15T16:52:08.578000+00:00 | 2m 25s |
| gameWindowFocusEvent | 17 | 0.12 | 1 | 2 | 0 | 2026-10-05T16:26:02.204000+00:00 | 2026-10-16T16:16:14.139000+00:00 | 263h 50m |
| gameStartEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-10-05T16:26:02.205000+00:00 | 2026-10-16T16:16:14.139000+00:00 | 263h 50m |
| argumentationAnswerEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-10-05T16:55:34.915000+00:00 | 2026-10-15T21:11:15.500000+00:00 | 244h 15m |
| argumentationEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-10-05T16:55:18.933000+00:00 | 2026-10-15T21:11:15.538000+00:00 | 244h 15m |
| SolarStillDesignEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-16T16:20:52.292000+00:00 | 2026-10-16T16:21:07.245000+00:00 | 15.0s |
| argumentationToolEvent | 6 | 0.04 | 1 | 3 | 0 | 2026-10-05T16:55:14.756000+00:00 | 2026-10-13T16:48:33.022000+00:00 | 191h 53m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-05T17:02:09.997000+00:00 | 2026-10-16T16:27:20.997000+00:00 | 263h 25m |
| gameWindowUnfocusEvent | 5 | 0.04 | 1 | 2 | 0 | 2026-10-05T17:04:12.051000+00:00 | 2026-10-13T16:22:41.439000+00:00 | 191h 18m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-15T17:00:55.897000+00:00 | 2026-10-16T16:16:26.574000+00:00 | 23h 15m |
| DaniEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-10-13T16:35:44.014000+00:00 | 2026-10-13T16:35:46.230000+00:00 | 2.2s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 173378.258s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.046s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.813s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.404s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 58.888s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 111.95s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 13825.173s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 13827.613s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 8187.404s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86541.831s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 10.137s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: GRAVEL 
  - Expected: may simply not have been exercised — review
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
  - Observed: Covered; Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: B,1,II; C,3,II; C,4,II; C,D,3,II; D,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 5 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[174] _id=6ac3d2d0de269131f9ade91e ts=2026-10-05T16:39:43.0660000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[223] _id=6ac3d3b8de269131f9adf8fb ts=2026-10-05T16:43:36.0030000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[302] _id=6ac3d480de269131f9ae0eb9 ts=2026-10-05T16:46:55.7050000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[15] _id=6ac3cf9bde269131f9ada757 ts=2026-10-05T16:26:02.2050000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[807] _id=6ac3d866de269131f9ae6e93 ts=2026-10-05T17:03:32.9350000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[819] _id=6ac525adde269131f9b53d81 ts=2026-10-06T16:45:32.1280000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[16] _id=6ac3cf9bde269131f9ada755 ts=2026-10-05T16:26:02.2040000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[808] _id=6ac3d865de269131f9ae6e91 ts=2026-10-05T17:03:32.9340000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[818] _id=6ac525acde269131f9b53d75 ts=2026-10-06T16:45:32.1260000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 5 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 5} 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[817] _id=6ac3d88dde269131f9ae71ed ts=2026-10-05T17:04:12.0510000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[2616] _id=6ac673f2de269131f9bc898a ts=2026-10-06T17:04:16.988Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[4069] _id=6ac67a84de269131f9bd7211 ts=2026-10-07T16:59:48.3580000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6128 | 0.0 | 0.41 | 155.046 | 6.391 | 429269.461 | 0.39 | 471 | 8 |
| PuzzlePieceVisibleEvent | 2735 | 0.0 | 0.046 | 289.694 | 1.465 | 433477.978 | 0.21 | 1399 | 8 |
| DialogueEvent | 2186 | 0.0 | 3.615 | 434.628 | 27.935 | 429287.651 | 0.14 | 623 | 8 |
| PlayerPositionEvent | 1654 | 9.735 | 10.003 | 574.272 | 10.142 | 429260.395 | 0.1 | 0 | 8 |
| ObjectInterEvent | 340 | 0.0 | 7.236 | 2793.451 | 331.242 | 429409.771 | 0.02 | 3 | 10 |
| argumentationNodeEvent | 314 | 0.005 | 0.649 | 2800.655 | 11.628 | 431605.377 | 0.02 | 32 | 4 |
| questEvent | 88 | 0.0 | 166.368 | 10794.226 | 84045.05 | 429429.315 | 0.01 | 16 | 13 |
| TopographicMapEvent | 60 | 0.02 | 5.404 | 11500.886 | 85403.903 | 429404.384 | 0.01 | 2 | 6 |
| Soil Key Puzzle | 37 | 0.007 | 1.813 | 18662.902 | 85743.754 | 518221.923 | 0.0 | 1 | 3 |
| DEBUGMenu | 33 | 6.602 | 595.533 | 28771.412 | 85415.724 | 429554.202 | 0.0 | 0 | 16 |
| soilMachine | 25 | 0.168 | 10.137 | 3378.731 | 147.862 | 83745.495 | 0.02 | 0 | 1 |
| WaterChamberEvent | 18 | 6.155 | 21.277 | 28.082 | 64.124 | 103.572 | 2.14 | 0 | 0 |
| TerasGardenBox | 17 | 0.77 | 2.155 | 8.546 | 32.102 | 45.512 | 7.02 | 0 | 0 |
| gameWindowFocusEvent | 16 | 407.622 | 8187.404 | 59363.246 | 171571.18 | 429563.605 | 0.0 | 0 | 14 |
| gameStartEvent | 15 | 420.61 | 13827.613 | 63320.796 | 188770.674 | 429563.605 | 0.0 | 0 | 14 |
| argumentationAnswerEvent | 13 | 0.263 | 58.888 | 67641.583 | 328077.41 | 431649.229 | 0.0 | 0 | 4 |
| argumentationEvent | 13 | 0.036 | 67.988 | 67642.816 | 327950.943 | 431598.663 | 0.0 | 1 | 4 |
| SolarStillDesignEvent | 5 | 1.135 | 2.602 | 2.991 | 4.982 | 5.134 | 20.06 | 0 | 0 |
| argumentationToolEvent | 5 | 4.088 | 111.95 | 138159.653 | 397216.416 | 431801.55 | 0.0 | 0 | 2 |
| EndOfUnit | 4 | 84407.133 | 173378.258 | 237077.75 | 478425.582 | 517147.351 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 4 | 86131.37 | 86541.831 | 172177.347 | 378072.011 | 429494.356 | 0.0 | 0 | 4 |
| chatEvent | 3 | 759.013 | 13825.173 | 27910.226 | 63614.359 | 69146.491 | 0.0 | 0 | 3 |
| DaniEvent | 1 | 2.216 | 2.216 | 2.216 | 2.216 | 2.216 | 27.08 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 22 group(s), 34 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[2626] _id=6ac67403de269131f9bc8a7a ts=2026-10-07T16:32:01.7870000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[2627] _id=6ac67403de269131f9bc8a7b ts=2026-10-07T16:32:01.7870000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[2628] _id=6ac67403de269131f9bc8a7c ts=2026-10-07T16:32:01.7880000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[2629] _id=6ac67403de269131f9bc8a7d ts=2026-10-07T16:32:01.7880000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[2630] _id=6ac67403de269131f9bc8a7e ts=2026-10-07T16:32:01.7890000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[2631] _id=6ac67403de269131f9bc8a7f ts=2026-10-07T16:32:01.7890000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 139 group(s), 231 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[942] _id=6ac526d0de269131f9b567a1 ts=2026-10-06T16:50:21.6480000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[943] _id=6ac526d1de269131f9b567a7 ts=2026-10-06T16:50:21.6480000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[949] _id=6ac526d1de269131f9b567b1 ts=2026-10-06T16:50:21.6480000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[944] _id=6ac526d1de269131f9b567b3 ts=2026-10-06T16:50:21.6480000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[951] _id=6ac526d2de269131f9b567bd ts=2026-10-06T16:50:21.8360000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[945] _id=6ac526d2de269131f9b567bf ts=2026-10-06T16:50:21.8360000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[13434] _id=6ad141b7de269131f9e16d48 ts=2026-10-15T21:12:23.4720000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[13435] _id=6ad141b7de269131f9e16d49 ts=2026-10-15T21:12:23.4720000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[13479] _id=6ad24ddede269131f9e5a9da ts=2026-10-16T16:16:29.7630000Z == 6ab9a8e69a8420a1e6b56b26.jsonl[13480] _id=6ad24ddede269131f9e5a9db ts=2026-10-16T16:16:29.7630000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 25 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8e69a8420a1e6b56b26.jsonl[124] _id=6ac3d25cde269131f9addf3d ts=2026-10-05T16:37:47.6720000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[127] _id=6ac3d25cde269131f9addf41 ts=2026-10-05T16:37:47.6770000Z`; `872ms: 6ab9a8e69a8420a1e6b56b26.jsonl[628] _id=6ac3d76ade269131f9ae5683 ts=2026-10-05T16:59:22.0270000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[629] _id=6ac3d76bde269131f9ae569b ts=2026-10-05T16:59:22.8990000Z`; `529ms: 6ab9a8e69a8420a1e6b56b26.jsonl[629] _id=6ac3d76bde269131f9ae569b ts=2026-10-05T16:59:22.8990000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[630] _id=6ac3d76cde269131f9ae56ad ts=2026-10-05T16:59:23.4280000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 340 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `406ms: 6ab9a8e69a8420a1e6b56b26.jsonl[938] _id=6ac526d0de269131f9b56799 ts=2026-10-06T16:50:21.2300000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[941] _id=6ac526d0de269131f9b5679b ts=2026-10-06T16:50:21.6360000Z`; `12ms: 6ab9a8e69a8420a1e6b56b26.jsonl[941] _id=6ac526d0de269131f9b5679b ts=2026-10-06T16:50:21.6360000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[942] _id=6ac526d0de269131f9b567a1 ts=2026-10-06T16:50:21.6480000Z`; `163ms: 6ab9a8e69a8420a1e6b56b26.jsonl[944] _id=6ac526d1de269131f9b567b3 ts=2026-10-06T16:50:21.6480000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[950] _id=6ac526d2de269131f9b567b7 ts=2026-10-06T16:50:21.8110000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `770ms: 6ab9a8e69a8420a1e6b56b26.jsonl[11643] _id=6ad10450de269131f9dded1d ts=2026-10-15T16:50:23.7740000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[11645] _id=6ad10450de269131f9dded33 ts=2026-10-15T16:50:24.5440000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `799ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6145] _id=6ace5eb5de269131f9cf98c1 ts=2026-10-13T16:39:15.5530000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[6148] _id=6ace5eb5de269131f9cf98e1 ts=2026-10-13T16:39:16.3520000Z`; `895ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6142] _id=6ace5eb5de269131f9cf98ca ts=2026-10-13T16:39:15.8210000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[6137] _id=6ace5eb5de269131f9cf98ea ts=2026-10-13T16:39:16.7160000Z`; `697ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6148] _id=6ace5eb5de269131f9cf98e1 ts=2026-10-13T16:39:16.3520000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[6146] _id=6ace5eb6de269131f9cf98f2 ts=2026-10-13T16:39:17.0490000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `263ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13353] _id=6ad14147de269131f9e1675c ts=2026-10-15T21:10:31.7840000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[13351] _id=6ad14148de269131f9e16760 ts=2026-10-15T21:10:32.0470000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `36ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6461] _id=6ace60e8de269131f9cfc0f6 ts=2026-10-13T16:48:38.9920000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[6471] _id=6ace60e8de269131f9cfc0f9 ts=2026-10-13T16:48:39.0280000Z`; `87ms: 6ab9a8e69a8420a1e6b56b26.jsonl[11458] _id=6ad10338de269131f9ddd3b1 ts=2026-10-15T16:45:44.1760000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[11461] _id=6ad10338de269131f9ddd3b7 ts=2026-10-15T16:45:44.2630000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `51ms: 6ab9a8e69a8420a1e6b56b26.jsonl[474] _id=6ac3d67bde269131f9ae3f03 ts=2026-10-05T16:55:22.7270000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[476] _id=6ac3d67cde269131f9ae3f0d ts=2026-10-05T16:55:22.7780000Z`; `22ms: 6ab9a8e69a8420a1e6b56b26.jsonl[483] _id=6ac3d67fde269131f9ae3f5d ts=2026-10-05T16:55:25.9780000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[480] _id=6ac3d67fde269131f9ae3f5f ts=2026-10-05T16:55:26.0000000Z`; `694ms: 6ab9a8e69a8420a1e6b56b26.jsonl[501] _id=6ac3d6dbde269131f9ae47e7 ts=2026-10-05T16:56:58.4220000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[499] _id=6ac3d6dcde269131f9ae47f5 ts=2026-10-05T16:56:59.1160000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13625] _id=6ad24f46de269131f9e5c36b ts=2026-10-16T16:22:30.5200000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[13626] _id=6ad24f46de269131f9e5c36d ts=2026-10-16T16:22:30.5230000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `808ms: 6ab9a8e69a8420a1e6b56b26.jsonl[10322] _id=6ad0fe33de269131f9dd70c3 ts=2026-10-15T16:24:19.1410000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[10326] _id=6ad0fe34de269131f9dd70dd ts=2026-10-15T16:24:19.9490000Z`; `454ms: 6ab9a8e69a8420a1e6b56b26.jsonl[10326] _id=6ad0fe34de269131f9dd70dd ts=2026-10-15T16:24:19.9490000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[10327] _id=6ad0fe34de269131f9dd70e4 ts=2026-10-15T16:24:20.4030000Z`; `204ms: 6ab9a8e69a8420a1e6b56b26.jsonl[10327] _id=6ad0fe34de269131f9dd70e4 ts=2026-10-15T16:24:20.4030000Z ~ 6ab9a8e69a8420a1e6b56b26.jsonl[10330] _id=6ad0fe34de269131f9dd70eb ts=2026-10-15T16:24:20.6070000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8e69a8420a1e6b56b26.jsonl[5194] _id=6ac7cbe5de269131f9c4cbab ts=2026-10-08T16:59:16.2230000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5338] _id=6ace59d7de269131f9cf58ee ts=2026-10-13T16:18:30.4250000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b26.jsonl[823] _id=6ac525c1de269131f9b5403b ts=2026-10-06T16:45:49.4230000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2617] _id=6ac673f2de269131f9bc8991 ts=2026-10-07T16:31:45.6900000Z; 23h 42m: 6ab9a8e69a8420a1e6b56b26.jsonl[810] _id=6ac3d874de269131f9ae6fb5 ts=2026-10-05T17:03:47.3940000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[823] _id=6ac525c1de269131f9b5403b ts=2026-10-06T16:45:49.4230000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 14m 
  - Evidence: 119h 14m: 6ab9a8e69a8420a1e6b56b26.jsonl[5325] _id=6ac7cd18de269131f9c4dfb9 ts=2026-10-08T17:04:23.9960000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5369] _id=6ace5a00de269131f9cf598d ts=2026-10-13T16:19:11.6470000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b26.jsonl[815] _id=6ac3d87fde269131f9ae709b ts=2026-10-05T17:03:58.4250000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[826] _id=6ac525c2de269131f9b5404d ts=2026-10-06T16:45:53.1050000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b26.jsonl[2587] _id=6ac529eade269131f9b601f9 ts=2026-10-06T17:03:37.6570000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2676] _id=6ac67439de269131f9bc8e75 ts=2026-10-07T16:32:57.4510000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 623 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[11351] _id=6ad102c4de269131f9ddc9f6 ts=2026-10-15T16:43:47.5970000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[11352] _id=6ad102c4de269131f9ddc9f7 ts=2026-10-15T16:43:47.5970000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13348] _id=6ad14140de269131f9e16707 ts=2026-10-15T21:10:24.6520000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13349] _id=6ad14140de269131f9e16708 ts=2026-10-15T21:10:24.6520000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13371] _id=6ad1415cde269131f9e168bd ts=2026-10-15T21:10:52.3790000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13372] _id=6ad1415cde269131f9e168be ts=2026-10-15T21:10:52.3790000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 39m 
  - Evidence: 143h 39m: 6ab9a8e69a8420a1e6b56b26.jsonl[5180] _id=6ac7cbcdde269131f9c4ca93 ts=2026-10-08T16:58:52.2210000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[8081] _id=6acfafe8de269131f9d59f05 ts=2026-10-14T16:37:59.5720000Z; 71h 56m: 6ab9a8e69a8420a1e6b56b26.jsonl[672] _id=6ac3d812de269131f9ae6843 ts=2026-10-05T17:02:09.9970000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5180] _id=6ac7cbcdde269131f9c4ca93 ts=2026-10-08T16:58:52.2210000Z; 24h 22m: 6ab9a8e69a8420a1e6b56b26.jsonl[8081] _id=6acfafe8de269131f9d59f05 ts=2026-10-14T16:37:59.5720000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[12181] _id=6ad106b2de269131f9de315e ts=2026-10-15T17:00:33.8640000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 14m 
  - Evidence: 119h 14m: 6ab9a8e69a8420a1e6b56b26.jsonl[5321] _id=6ac7cd0fde269131f9c4df50 ts=2026-10-08T17:04:14.9580000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5342] _id=6ace59e7de269131f9cf58fb ts=2026-10-13T16:18:44.4190000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b26.jsonl[812] _id=6ac3d878de269131f9ae7005 ts=2026-10-05T17:03:49.9160000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[821] _id=6ac525bede269131f9b53f9d ts=2026-10-06T16:45:49.3850000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b26.jsonl[2610] _id=6ac52a10de269131f9b60985 ts=2026-10-06T17:04:15.8960000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2622] _id=6ac67403de269131f9bc8a77 ts=2026-10-07T16:32:01.7820000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 471 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[10067] _id=6ad0fd5dde269131f9dd5f54 ts=2026-10-15T16:20:44.8180000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[10068] _id=6ad0fd5dde269131f9dd5f55 ts=2026-10-15T16:20:44.8180000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[10075] _id=6ad0fd5dde269131f9dd5f5f ts=2026-10-15T16:20:45.1460000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[10076] _id=6ad0fd5dde269131f9dd5f60 ts=2026-10-15T16:20:45.1460000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[10264] _id=6ad0fdedde269131f9dd6c29 ts=2026-10-15T16:23:08.8780000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[10265] _id=6ad0fdedde269131f9dd6c2a ts=2026-10-15T16:23:08.8780000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b26.jsonl[5291] _id=6ac7ccefde269131f9c4de00 ts=2026-10-08T17:03:42.9900000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5409] _id=6ace5a51de269131f9cf5b9a ts=2026-10-13T16:20:32.7610000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b26.jsonl[3700] _id=6ac67897de269131f9bd4323 ts=2026-10-07T16:51:34.9130000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[4715] _id=6ac7c835de269131f9c48a1b ts=2026-10-08T16:43:32.3240000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b26.jsonl[784] _id=6ac3d7e7de269131f9ae6361 ts=2026-10-05T17:01:26.5320000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[894] _id=6ac526aade269131f9b56319 ts=2026-10-06T16:49:45.6320000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[11170] _id=6ad10164de269131f9ddae2f ts=2026-10-15T16:37:56.5370000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[11171] _id=6ad10164de269131f9ddae30 ts=2026-10-15T16:37:56.5370000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[11204] _id=6ad101a0de269131f9ddb23e ts=2026-10-15T16:38:55.9200000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[11205] _id=6ad101a0de269131f9ddb23f ts=2026-10-15T16:38:55.9200000Z; 5ms: 6ab9a8e69a8420a1e6b56b26.jsonl[124] _id=6ac3d25cde269131f9addf3d ts=2026-10-05T16:37:47.6720000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[127] _id=6ac3d25cde269131f9addf41 ts=2026-10-05T16:37:47.6770000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 14m 
  - Evidence: 119h 14m: 6ab9a8e69a8420a1e6b56b26.jsonl[5324] _id=6ac7cd15de269131f9c4dfa7 ts=2026-10-08T17:04:20.6700000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5341] _id=6ace59e7de269131f9cf58fa ts=2026-10-13T16:18:41.0650000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b26.jsonl[816] _id=6ac3d88bde269131f9ae71b3 ts=2026-10-05T17:04:10.3330000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[824] _id=6ac525c1de269131f9b54048 ts=2026-10-06T16:45:49.4310000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b26.jsonl[2611] _id=6ac52a0dde269131f9b608f7 ts=2026-10-06T17:04:13.1140000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2621] _id=6ac67403de269131f9bc8a76 ts=2026-10-07T16:31:59.8040000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6ab9a8e69a8420a1e6b56b26.jsonl[4219] _id=6ac7c4c8de269131f9c42830 ts=2026-10-08T16:28:51.5370000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6635] _id=6ace620bde269131f9cfd6c4 ts=2026-10-13T16:53:29.5150000Z; 23h 49m: 6ab9a8e69a8420a1e6b56b26.jsonl[2447] _id=6ac5289ede269131f9b5c24c ts=2026-10-06T16:58:02.5380000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[3180] _id=6ac677b5de269131f9bd2c3f ts=2026-10-07T16:47:48.5530000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b26.jsonl[8803] _id=6acfb2b7de269131f9d5ebfb ts=2026-10-14T16:49:55.0170000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[10727] _id=6ad0ff5dde269131f9dd8c3e ts=2026-10-15T16:29:16.5280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1399 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[1002] _id=6ac526ecde269131f9b56af2 ts=2026-10-06T16:50:50.2050000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[977] _id=6ac526ecde269131f9b56afd ts=2026-10-06T16:50:50.2050000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[1004] _id=6ac526ecde269131f9b56b05 ts=2026-10-06T16:50:50.2050000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[979] _id=6ac526ecde269131f9b56b0d ts=2026-10-06T16:50:50.2050000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[1006] _id=6ac526f6de269131f9b56c69 ts=2026-10-06T16:51:00.8580000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[1012] _id=6ac526f6de269131f9b56c6f ts=2026-10-06T16:51:00.8580000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 6ab9a8e69a8420a1e6b56b26.jsonl[3154] _id=6ac67789de269131f9bd254c ts=2026-10-07T16:47:05.2840000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6329] _id=6ace5fd8de269131f9cfafb0 ts=2026-10-13T16:44:07.2070000Z; 23h 54m: 6ab9a8e69a8420a1e6b56b26.jsonl[6619] _id=6ace61dade269131f9cfd2cb ts=2026-10-13T16:52:41.9010000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[8230] _id=6acfb219de269131f9d5d42b ts=2026-10-14T16:47:20.8330000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b26.jsonl[2494] _id=6ac528cfde269131f9b5cd5f ts=2026-10-06T16:58:54.9460000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[3143] _id=6ac6776bde269131f9bd1f22 ts=2026-10-07T16:46:34.9060000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.007s..0.007s shown 
  - Evidence: 7ms: 6ab9a8e69a8420a1e6b56b26.jsonl[8240] _id=6acfb21fde269131f9d5d4cf ts=2026-10-14T16:47:27.1450000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[8244] _id=6acfb21fde269131f9d5d4d1 ts=2026-10-14T16:47:27.1520000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a8e69a8420a1e6b56b26.jsonl[5293] _id=6ac7cce5de269131f9c4dd7a ts=2026-10-08T17:03:32.6770000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5397] _id=6ace5a42de269131f9cf5b51 ts=2026-10-13T16:20:17.0610000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b26.jsonl[2857] _id=6ac67621de269131f9bce7ad ts=2026-10-07T16:41:05.2540000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[4516] _id=6ac7c6a7de269131f9c45e11 ts=2026-10-08T16:36:54.2020000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b26.jsonl[6155] _id=6ace5ebdde269131f9cf99b1 ts=2026-10-13T16:39:24.8520000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[7819] _id=6acfae0bde269131f9d57cea ts=2026-10-14T16:30:02.7390000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.025s shown 
  - Evidence: 20ms: 6ab9a8e69a8420a1e6b56b26.jsonl[2714] _id=6ac674a3de269131f9bc980b ts=2026-10-07T16:34:43.6770000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2716] _id=6ac674a4de269131f9bc980f ts=2026-10-07T16:34:43.6970000Z; 25ms: 6ab9a8e69a8420a1e6b56b26.jsonl[2716] _id=6ac674a4de269131f9bc980f ts=2026-10-07T16:34:43.6970000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2720] _id=6ac674a4de269131f9bc9813 ts=2026-10-07T16:34:43.7220000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 54m 
  - Evidence: 119h 54m: 6ab9a8e69a8420a1e6b56b26.jsonl[5084] _id=6ac7cac6de269131f9c4b8c5 ts=2026-10-08T16:54:29.7470000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6460] _id=6ace60e8de269131f9cfc0f2 ts=2026-10-13T16:48:38.9760000Z; 71h 57m: 6ab9a8e69a8420a1e6b56b26.jsonl[541] _id=6ac3d6f1de269131f9ae4a83 ts=2026-10-05T16:57:20.2170000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5084] _id=6ac7cac6de269131f9c4b8c5 ts=2026-10-08T16:54:29.7470000Z; 47h 54m: 6ab9a8e69a8420a1e6b56b26.jsonl[6460] _id=6ace60e8de269131f9cfc0f2 ts=2026-10-13T16:48:38.9760000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[11332] _id=6ad10288de269131f9ddc42c ts=2026-10-15T16:42:48.6880000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a8e69a8420a1e6b56b26.jsonl[5080] _id=6ac7cac6de269131f9c4b8c9 ts=2026-10-08T16:54:29.7740000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6428] _id=6ace60b5de269131f9cfbe3c ts=2026-10-13T16:47:48.4370000Z; 71h 54m: 6ab9a8e69a8420a1e6b56b26.jsonl[538] _id=6ac3d6f1de269131f9ae4a85 ts=2026-10-05T16:57:20.2450000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5046] _id=6ac7ca15de269131f9c4afeb ts=2026-10-08T16:51:32.7080000Z; 47h 52m: 6ab9a8e69a8420a1e6b56b26.jsonl[6471] _id=6ace60e8de269131f9cfc0f9 ts=2026-10-13T16:48:39.0280000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[11247] _id=6ad10222de269131f9ddba74 ts=2026-10-15T16:41:05.9310000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.036s..0.036s shown 
  - Evidence: 36ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6461] _id=6ace60e8de269131f9cfc0f6 ts=2026-10-13T16:48:38.9920000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6471] _id=6ace60e8de269131f9cfc0f9 ts=2026-10-13T16:48:39.0280000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a8e69a8420a1e6b56b26.jsonl[5077] _id=6ac7cabede269131f9c4b86b ts=2026-10-08T16:54:21.3140000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6425] _id=6ace60b3de269131f9cfbe1b ts=2026-10-13T16:47:46.6910000Z; 71h 53m: 6ab9a8e69a8420a1e6b56b26.jsonl[540] _id=6ac3d6f0de269131f9ae4a65 ts=2026-10-05T16:57:19.1390000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5030] _id=6ac7ca06de269131f9c4af12 ts=2026-10-08T16:51:17.0450000Z; 47h 52m: 6ab9a8e69a8420a1e6b56b26.jsonl[6467] _id=6ace60e0de269131f9cfc066 ts=2026-10-13T16:48:31.0710000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[11249] _id=6ad10225de269131f9ddbad4 ts=2026-10-15T16:41:09.4560000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 32 interval(s) ≤ 0.005s..0.019s shown 
  - Evidence: 5ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13325] _id=6ad1412ede269131f9e1659d ts=2026-10-15T21:10:06.7070000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13317] _id=6ad1412ede269131f9e1659f ts=2026-10-15T21:10:06.7120000Z; 7ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6432] _id=6ace60d1de269131f9cfbfaf ts=2026-10-13T16:48:16.1050000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6446] _id=6ace60d1de269131f9cfbfb1 ts=2026-10-13T16:48:16.1120000Z; 19ms: 6ab9a8e69a8420a1e6b56b26.jsonl[6446] _id=6ace60d1de269131f9cfbfb1 ts=2026-10-13T16:48:16.1120000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6447] _id=6ace60d1de269131f9cfbfb2 ts=2026-10-13T16:48:16.1310000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8e69a8420a1e6b56b26.jsonl[5056] _id=6ac7ca28de269131f9c4b091 ts=2026-10-08T16:51:51.4720000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[6465] _id=6ace60e2de269131f9cfc083 ts=2026-10-13T16:48:33.0220000Z; 71h 54m: 6ab9a8e69a8420a1e6b56b26.jsonl[533] _id=6ac3d6e7de269131f9ae497f ts=2026-10-05T16:57:10.7940000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5053] _id=6ac7ca23de269131f9c4b071 ts=2026-10-08T16:51:46.6730000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 19h 12m 
  - Evidence: 19h 12m: 6ab9a8e69a8420a1e6b56b26.jsonl[13012] _id=6ad13fc0de269131f9e1523d ts=2026-10-15T21:04:00.0830000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13469] _id=6ad24ddade269131f9e5a9bc ts=2026-10-16T16:16:26.5740000Z; 3h 50m: 6ab9a8e69a8420a1e6b56b26.jsonl[12184] _id=6ad106c8de269131f9de32f8 ts=2026-10-15T17:00:55.8970000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[12250] _id=6ad13cc9de269131f9e13b11 ts=2026-10-15T20:51:21.0700000Z; 12m 39s: 6ab9a8e69a8420a1e6b56b26.jsonl[12250] _id=6ad13cc9de269131f9e13b11 ts=2026-10-15T20:51:21.0700000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13012] _id=6ad13fc0de269131f9e1523d ts=2026-10-15T21:04:00.0830000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8e69a8420a1e6b56b26.jsonl[5185] _id=6ac7cbdcde269131f9c4cb1f ts=2026-10-08T16:59:06.9640000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5340] _id=6ace59d7de269131f9cf58f0 ts=2026-10-13T16:18:30.5690000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b26.jsonl[819] _id=6ac525adde269131f9b53d81 ts=2026-10-06T16:45:32.1280000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2619] _id=6ac673f2de269131f9bc8993 ts=2026-10-07T16:31:45.8310000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b26.jsonl[807] _id=6ac3d866de269131f9ae6e93 ts=2026-10-05T17:03:32.9350000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[819] _id=6ac525adde269131f9b53d81 ts=2026-10-06T16:45:32.1280000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a8e69a8420a1e6b56b26.jsonl[5184] _id=6ac7cbdcde269131f9c4cb1e ts=2026-10-08T16:59:06.9640000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5339] _id=6ace59d7de269131f9cf58ef ts=2026-10-13T16:18:30.5690000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b26.jsonl[818] _id=6ac525acde269131f9b53d75 ts=2026-10-06T16:45:32.1260000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2618] _id=6ac673f2de269131f9bc8992 ts=2026-10-07T16:31:45.8310000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b26.jsonl[808] _id=6ac3d865de269131f9ae6e91 ts=2026-10-05T17:03:32.9340000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[818] _id=6ac525acde269131f9b53d75 ts=2026-10-06T16:45:32.1260000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8e69a8420a1e6b56b26.jsonl[5333] _id=6ace59d7de269131f9cf58ec ts=2026-10-08T17:04:27.083Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5464] _id=6ace5ad2de269131f9cf601d ts=2026-10-13T16:22:41.4390000Z; 24h 4m: 6ab9a8e69a8420a1e6b56b26.jsonl[4069] _id=6ac67a84de269131f9bd7211 ts=2026-10-07T16:59:48.3580000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5333] _id=6ace59d7de269131f9cf58ec ts=2026-10-08T17:04:27.083Z; 24h 0m: 6ab9a8e69a8420a1e6b56b26.jsonl[817] _id=6ac3d88dde269131f9ae71ed ts=2026-10-05T17:04:12.0510000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2616] _id=6ac673f2de269131f9bc898a ts=2026-10-06T17:04:16.988Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b26.jsonl[5223] _id=6ac7cc70de269131f9c4d74a ts=2026-10-08T17:01:35.1430000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[5345] _id=6ace59e7de269131f9cf58fe ts=2026-10-13T16:18:44.4580000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b26.jsonl[785] _id=6ac3d7e9de269131f9ae638b ts=2026-10-05T17:01:29.0120000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[860] _id=6ac5266cde269131f9b55bf3 ts=2026-10-06T16:48:43.5850000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b26.jsonl[2584] _id=6ac529e4de269131f9b60137 ts=2026-10-06T17:03:32.0710000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[2633] _id=6ac67403de269131f9bc8a81 ts=2026-10-07T16:32:01.8300000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13434] _id=6ad141b7de269131f9e16d48 ts=2026-10-15T21:12:23.4720000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13435] _id=6ad141b7de269131f9e16d49 ts=2026-10-15T21:12:23.4720000Z; 0ms: 6ab9a8e69a8420a1e6b56b26.jsonl[13479] _id=6ad24ddede269131f9e5a9da ts=2026-10-16T16:16:29.7630000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[13480] _id=6ad24ddede269131f9e5a9db ts=2026-10-16T16:16:29.7630000Z; 1ms: 6ab9a8e69a8420a1e6b56b26.jsonl[12591] _id=6ad13dffde269131f9e14376 ts=2026-10-15T20:56:31.4070000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[12592] _id=6ad13dffde269131f9e14377 ts=2026-10-15T20:56:31.4080000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 15m 
  - Evidence: 23h 15m: 6ab9a8e69a8420a1e6b56b26.jsonl[9899] _id=6acfb620de269131f9d64416 ts=2026-10-14T17:04:31.4410000Z -> 6ab9a8e69a8420a1e6b56b26.jsonl[10018] _id=6ad0fd41de269131f9dd5cc9 ts=2026-10-15T16:20:16.9360000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[415] _id=6ac3d60ade269131f9ae304d ts=2026-10-05T16:53:29.5970000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[554] _id=6ac3d70ade269131f9ae4d15 ts=2026-10-05T16:57:45.7770000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[2886] _id=6ac67616de269131f9bce65d ts=2026-10-07T16:40:54.6700000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 52 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[1171] _id=6ac52786de269131f9b58053 ts=2026-10-06T16:53:23.7120000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1172] _id=6ac52786de269131f9b58055 ts=2026-10-06T16:53:23.7150000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1166] _id=6ac52786de269131f9b58059 ts=2026-10-06T16:53:23.7490000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 136 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[935] _id=6ac526cfde269131f9b5678d ts=2026-10-06T16:50:21.2300000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[936] _id=6ac526d0de269131f9b56793 ts=2026-10-06T16:50:21.2300000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[937] _id=6ac526d0de269131f9b56795 ts=2026-10-06T16:50:21.2300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[6471] _id=6ace60e8de269131f9cfc0f9 ts=2026-10-13T16:48:39.0280000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[11461] _id=6ad10338de269131f9ddd3b7 ts=2026-10-15T16:45:44.2630000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[476] _id=6ac3d67cde269131f9ae3f0d ts=2026-10-05T16:55:22.7780000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[480] _id=6ac3d67fde269131f9ae3f5f ts=2026-10-05T16:55:26.0000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[12184] _id=6ad106c8de269131f9de32f8 ts=2026-10-15T17:00:55.8970000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[12250] _id=6ad13cc9de269131f9e13b11 ts=2026-10-15T20:51:21.0700000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[13012] _id=6ad13fc0de269131f9e1523d ts=2026-10-15T21:04:00.0830000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[9103] _id=6acfb3ccde269131f9d60751 ts=2026-10-14T16:54:35.5980000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[9923] _id=6ad0fce8de269131f9dd57c5 ts=2026-10-15T16:18:48.1260000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 222 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[1035] _id=6ac5277fde269131f9b57f24 ts=2026-10-06T16:53:17.5170000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1134] _id=6ac5277fde269131f9b57f3d ts=2026-10-06T16:53:17.7590000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1156] _id=6ac52781de269131f9b57f8d ts=2026-10-06T16:53:19.3890000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 383 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[947] _id=6ac526d3de269131f9b567d1 ts=2026-10-06T16:50:21.9700000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1056] _id=6ac52735de269131f9b57507 ts=2026-10-06T16:50:32.4690000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1083] _id=6ac52736de269131f9b57543 ts=2026-10-06T16:50:33.5540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 414 start, 406 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 82 unmatched 'BecameCameraCentered' (totals: 564 open, 534 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 74 unmatched 'BecameVisible' (totals: 788 open, 850 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 5 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 52 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 414 of 13747 adjacent _id pairs reverse in client time; worst 90.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b26.jsonl[1064] _id=6ac52734de269131f9b574cb ts=2026-10-06T16:52:02.9400000Z`; `6ab9a8e69a8420a1e6b56b26.jsonl[1070] _id=6ac52734de269131f9b574e1 ts=2026-10-06T16:50:32.1710000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.81s, min -429244.54s, max -0.17s over 13748 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b26\coverage.yaml

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

### `InputEvent` — 6129 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1449); Unit 2 Prod (Refactor) (1288); Unit 3 Dev (945); Unit 4 Dev (750); Unit 3 Dungeon Dev (592); Unit 5 Dev - Dungeon (401); Unit 1 Dev (329); Unit 5 Dev (295); Unit 4 Dev - Anderson Base (80)
- **Intervals:** median 0.41s (p5 0.02s / p95 6.39s, n=6128)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6129/6129 records)
    "pressed"  x6129
data.actionType  (string, 6129/6129 records)
    "Move"  x4647
    "Sprint"  x540
    "Interact"  x529
    "Jump"  x251
    "Ascend"  x72
    "Hoverboard"  x44
    "Descend"  x37
    "Map"  x5
    "ToggleDebug"  x3
    "SkipCinematic"  x1
data.key  (string, 6129/6129 records, 14 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6129/6129 records)
    "Player"  x5232
    "Drone"  x897
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2736 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1810); Unit 4 Dev (512); Unit 5 Dev - Dungeon (208); Unit 3 Dungeon Dev (206)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.46s, n=2735)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2736/2736 records)
    "BecameInvisible"  x850
    "BecameVisible"  x788
    "BecameCameraCentered"  x564
    "BecameCameraUncentered"  x534
data.pieceId  (string, 2736/2736 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2736/2736 records)
    1509 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2187 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (614); Unit 3 Dev (340); Unit 4 Dev (271); Unit 5 Dev (231); Unit 3 Dungeon Dev (213); Unit 1 Dev (211); Unit 4 Dev - Dungeon (141); Unit 4 Dev - Anderson Base (85); Unit 5 Dev - Dungeon (81)
- **eventKey:** present on 1367 of 2187 records
- **Intervals:** median 3.62s (p5 0.00s / p95 27.93s, n=2186)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1367; [conversationId, dialogueEventType] x820
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2187/2187 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2187/2187 records)
    "DialogueNodeEvent"  x1367
    "DialogueStartEvent"  x414
    "DialogueFinishEvent"  x406
data.nodeId  (number, 1367/2187 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1666 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (487); Unit 3 Dev (276); Unit 1 Dev (181); Unit 4 Dev (174); Unit 4 Dev - Dungeon (149); Unit 3 Dungeon Dev (122); Unit 5 Dev (117); Unit 5 Dev - Dungeon (96); Unit 4 Dev - Anderson Base (64)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.14s, n=1654)
- **Fields under `data`:**

```text
data.position  (object, 1666/1666 records)
data.position.x  (number, 1666/1666 records)
    numeric range -688.607 .. 1557.51 (579 unique)
data.position.y  (number, 1666/1666 records)
    numeric range -112.489 .. 222.005 (425 unique)
data.position.z  (number, 1666/1666 records)
    numeric range -1031.42 .. 1762.77 (578 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 341 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (120); Unit 2 Prod (Refactor) (78); Unit 3 Dungeon Dev (54); Unit 4 Dev (25); Unit 1 Dev (15); Unit 5 Dev - Dungeon (15); Unit 3 Dev (14); Unit 5 Dev (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 7.24s (p5 0.45s / p95 331.24s, n=340)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 341/341 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 341/341 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 315 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (157); Unit 5 Dev (50); Unit 1 Dev (44); Unit 3 Dev (39); Unit 2 Prod (Refactor) (25)
- **Intervals:** median 0.65s (p5 0.03s / p95 11.63s, n=314)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 315/315 records)
    "argumentationNodeHoverEnd"  x137
    "argumentationNodeHoverStart"  x135
    "argumentationNodeAdd"  x31
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 315/315 records)
    "Unit 4 - Flooding"  x157
    "Unit 5"  x50
    "Unit 3 - Pollution Upstream"  x39
    "Unit 1 - Freshwater"  x29
    "Unit 2 – Watershed"  x25
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 315/315 records)
    "I"  x45
    "B"  x40
    "1"  x39
    "II"  x33
    "C"  x32
    "A"  x31
    "4"  x30
    "D"  x26
    "2"  x21
    "3"  x13
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 89 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 4 Dev - Dungeon (14); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev (9); Unit 5 Dev (9); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 89 of 89 records
- **Intervals:** median 166.37s (p5 0.00s / p95 84045.05s, n=88)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 89/89 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x37
data.questID  (string, 89/89 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 89/89 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/89 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 61 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (43); Unit 2 Prod (Refactor) (18)
- **Intervals:** median 5.40s (p5 0.26s / p95 85403.90s, n=60)
- **`data` key-set variants:** [actionType, featureUsed] x42; [actionType, featureUsed, location] x19
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 61/61 records)
    "MapCloseEvent"  x21
    "MapOpenEvent"  x21
    "WaypointMoveEvent"  x16
    "WaypointSetEvent"  x3
data.featureUsed  (string, 61/61 records)
    "Map"  x42
    "Waypoint"  x19
data.location  (object, 19/61 records)
data.location.x  (number, 19/61 records)
    numeric range -351.747 .. 165.626 (18 unique)
data.location.y  (number, 19/61 records)
    numeric range -291.453 .. 106.419 (18 unique)
data.location.z  (number, 19/61 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 38 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (14); Unit 2 Prod (Refactor) (12); Unit 3 Dev (12)
- **Intervals:** median 1.81s (p5 0.16s / p95 85743.75s, n=37)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x30; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/38 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/38 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 30/38 records)
    "RightDrag"  x18
    "LeftDrag"  x12
data.currentSoilType  (string, 30/38 records)
    "CLAY"  x9
    "CLAYROCK"  x8
    "CLAYSAND"  x6
    "BEDROCK"  x3
    "SAND"  x3
    "SANDGRAVEL"  x1
data.isCorrectSelection  (string, 30/38 records)
    "false"  x21
    "true"  x9
data.waterLevelStatus  (string, 30/38 records)
    "TooHigh"  x16
    "TooLow"  x10
    "Proper"  x4
data.waterRetentionChange  (string, 30/38 records)
    "Increase"  x17
    "NoChange"  x9
    "Decrease"  x4
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 34 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 4 Dev (4); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 595.53s (p5 8.74s / p95 85415.72s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "DebugMenuStateChanged"  x34
data.isOpened  (bool, 34/34 records)
    false  x34
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 26 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (26)
- **Intervals:** median 10.14s (p5 0.25s / p95 147.86s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "ChangeCanister"  x26
data.canisterType  (string, 26/26 records)
    "Bedrock"  x12
    "Clay"  x7
    "Gravel"  x4
    "Sand"  x3
data.floor  (string, 26/26 records)
    "5"  x19
    "4"  x5
    "3"  x2
data.machine  (string, 26/26 records)
    "1"  x25
    "2"  x1
data.row  (string, 26/26 records)
    "BottomRow"  x16
    "TopRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 19 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (19)
- **Intervals:** median 21.28s (p5 6.59s / p95 64.12s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "On"  x15
    "Off"  x4
data.floor  (string, 19/19 records)
    "3"  x8
    "4"  x5
    "2"  x4
    "1"  x2
data.machineNumber  (string, 19/19 records)
    "One"  x18
    "Two"  x1
data.machineType  (string, 19/19 records)
    "Condenser"  x9
    "Evaporator"  x5
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 19/19 records)
    "2"  x9
    "1"  x4
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TerasGardenBox` — 18 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (18)
- **Intervals:** median 2.15s (p5 0.98s / p95 32.10s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records, 12 empty-string)
    ""  x12
    "cameraPlaced"  x6
data.boxId  (string, 18/18 records)
    "1"  x9
    "0"  x6
    "2"  x3
data.soilType  (string, 18/18 records)
    "Sand"  x8
    "Clay"  x7
    "Gravel"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowFocusEvent` — 17 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 3 Dev (1)
- **Intervals:** median 8187.40s (p5 417.36s / p95 171571.18s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 13827.61s (p5 958.14s / p95 188770.67s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 14 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (6); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 58.89s (p5 0.88s / p95 328077.41s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "submitAnswerEvent"  x14
data.answerSubmitted  (string, 14/14 records)
    "C,4,II"  x4
    "A,1,I"  x2
    "B,1,II"  x2
    "A,1,II"  x1
    "A,5,I"  x1
    "A,C,D,2,II"  x1
    "C,3,II"  x1
    "C,D,3,II"  x1
    "D,1,II"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 5"  x6
    "Unit 4 - Flooding"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 67.99s (p5 0.07s / p95 327950.94s, n=13)
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

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 2.60s (p5 1.25s / p95 4.98s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted Out"  x1
data.featureUsed  (string, 6/6 records)
    "RoofStyle"  x3
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records)
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dev (1)
- **Intervals:** median 111.95s (p5 4.23s / p95 397216.42s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 173378.26s (p5 84909.21s / p95 478425.58s, n=4)
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

### `gameWindowUnfocusEvent` — 5 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2)
- **Intervals:** median 86541.83s (p5 86172.41s / p95 378072.01s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 5/5 records)
    false  x5
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 13825.17s (p5 2065.63s / p95 63614.36s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 2.22s (p5 2.22s / p95 2.22s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (12x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (16x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (12x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*