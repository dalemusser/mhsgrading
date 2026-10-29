# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b1f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b1f
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b1f.jsonl
- **Records:** 15417 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b1f
- **Time span:** 2026-10-05T16:26:53.368000+00:00 .. 2026-10-16T17:03:42.832000+00:00 (264h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b1f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 15417 records, 11 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 101 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5214 | 33.82 | 1 | 4 | 0 | 2026-10-07T16:37:24.810000+00:00 | 2026-10-16T16:27:06.393000+00:00 | 215h 49m |
| InputEvent | 4261 | 27.64 | 1 | 9 | 0 | 2026-10-05T16:36:28.945000+00:00 | 2026-10-16T17:03:42.832000+00:00 | 264h 27m |
| PlayerPositionEvent | 2423 | 15.72 | 1 | 9 | 0 | 2026-10-05T16:27:07.143000+00:00 | 2026-10-16T17:03:39.777000+00:00 | 264h 36m |
| DialogueEvent | 2082 | 13.5 | 1 | 9 | 1318 | 2026-10-05T16:27:27.045000+00:00 | 2026-10-16T17:03:37.039000+00:00 | 264h 36m |
| ObjectInterEvent | 462 | 3.0 | 1 | 9 | 0 | 2026-10-05T16:42:31.519000+00:00 | 2026-10-16T17:03:42.832000+00:00 | 264h 21m |
| argumentationNodeEvent | 388 | 2.52 | 1 | 5 | 0 | 2026-10-05T17:03:04.590000+00:00 | 2026-10-16T16:51:13.040000+00:00 | 263h 48m |
| Soil Key Puzzle | 200 | 1.3 | 1 | 3 | 0 | 2026-10-08T16:47:09.227000+00:00 | 2026-10-15T16:22:48.625000+00:00 | 167h 35m |
| TopographicMapEvent | 87 | 0.56 | 1 | 4 | 0 | 2026-10-06T16:57:18.944000+00:00 | 2026-10-16T01:37:50.640000+00:00 | 224h 40m |
| questEvent | 84 | 0.54 | 1 | 9 | 84 | 2026-10-05T16:27:27.022000+00:00 | 2026-10-16T16:59:55.735000+00:00 | 264h 32m |
| DEBUGMenu | 38 | 0.25 | 1 | 9 | 0 | 2026-10-05T16:27:07.133000+00:00 | 2026-10-16T16:17:36.536000+00:00 | 263h 50m |
| WaterChamberEvent | 34 | 0.22 | 1 | 1 | 0 | 2026-10-16T16:24:35.818000+00:00 | 2026-10-16T16:41:37.164000+00:00 | 17m 1s |
| DaniEvent | 26 | 0.17 | 1 | 2 | 0 | 2026-10-07T16:35:00.228000+00:00 | 2026-10-13T16:30:18.893000+00:00 | 143h 55m |
| gameWindowFocusEvent | 20 | 0.13 | 1 | 3 | 0 | 2026-10-05T16:26:53.368000+00:00 | 2026-10-16T16:17:29.734000+00:00 | 263h 50m |
| gameStartEvent | 18 | 0.12 | 1 | 1 | 0 | 2026-10-05T16:26:53.369000+00:00 | 2026-10-16T16:17:29.734000+00:00 | 263h 50m |
| soilMachine | 17 | 0.11 | 1 | 1 | 0 | 2026-10-15T16:38:24.357000+00:00 | 2026-10-15T16:58:51.744000+00:00 | 20m 27s |
| argumentationEvent | 16 | 0.1 | 1 | 5 | 0 | 2026-10-05T17:03:01.683000+00:00 | 2026-10-16T16:51:14.647000+00:00 | 263h 48m |
| argumentationAnswerEvent | 14 | 0.09 | 1 | 5 | 0 | 2026-10-05T17:03:10.174000+00:00 | 2026-10-16T16:51:14.615000+00:00 | 263h 48m |
| TerasGardenBox | 8 | 0.05 | 1 | 1 | 0 | 2026-10-16T01:25:14.847000+00:00 | 2026-10-16T01:27:26.558000+00:00 | 2m 11s |
| gameWindowUnfocusEvent | 8 | 0.05 | 1 | 5 | 0 | 2026-10-06T16:59:52.399000+00:00 | 2026-10-16T01:39:51.607000+00:00 | 224h 39m |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-06T16:58:45.920000+00:00 | 2026-10-16T17:03:42.808000+00:00 | 240h 4m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-16T16:56:56.226000+00:00 | 2026-10-16T16:57:15.206000+00:00 | 19.0s |
| argumentationToolEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-05T17:02:59.878000+00:00 | 2026-10-06T16:49:36.087000+00:00 | 23h 46m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-16T01:39:38.745000+00:00 | 2026-10-16T16:43:05.710000+00:00 | 15h 3m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 130194.33s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.504s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.073s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 7.573s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 13.711s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.024s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 115.419s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.627s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 27103.483s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 31020.211s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 4349.837s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85347.229s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 17.099s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName>; PodsEscapingCopernicus Cutscene 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 38 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 26 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E To Pick Up 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 5.3x vs baseline. 
  - Observed: 200 records 
  - Expected: 38 in 09-23-26 
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
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 180 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: B,5,I; B,C,A,2,II; B,C,D,2,II; B,C,D,4,II; C,D,3,4,II; C,D,3,II; C,D,A,2,II; D,1,II; D,C,B,1,II 
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
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.4x vs baseline. 
  - Observed: 17 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[247] _id=6ac3d406de269131f9adfff3 ts=2026-10-05T16:44:53.5000000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[343] _id=6ac3d59bde269131f9ae27e9 ts=2026-10-05T16:51:38.7210000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[401] _id=6ac3d63cde269131f9ae36a1 ts=2026-10-05T16:54:19.7920000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[5] _id=6ac3cfcede269131f9ada885 ts=2026-10-05T16:26:53.3690000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[44] _id=6ac3d1f3de269131f9add69b ts=2026-10-05T16:36:02.5700000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[573] _id=6ac52595de269131f9b53a25 ts=2026-10-06T16:45:08.4250000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[6] _id=6ac3cfcede269131f9ada883 ts=2026-10-05T16:26:53.3680000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[43] _id=6ac3d1f3de269131f9add696 ts=2026-10-05T16:36:02.5690000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[570] _id=6ac52595de269131f9b53a21 ts=2026-10-06T16:45:08.4240000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[967] _id=6ac52909de269131f9b5d8b1 ts=2026-10-06T16:59:52.3990000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1060] _id=6ac6742ade269131f9bc8d60 ts=2026-10-06T17:04:16.901Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1666] _id=6ac67775de269131f9bd2100 ts=2026-10-07T16:46:44.1300000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 87 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[866] _id=6ac5286fde269131f9b5b5c7 ts=2026-10-06T16:57:18.9440000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[875] _id=6ac52871de269131f9b5b626 ts=2026-10-06T16:57:21.0570000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1222] _id=6ac67566de269131f9bcc0c0 ts=2026-10-07T16:37:57.7240000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5213 | 0.0 | 0.073 | 149.047 | 2.203 | 372901.777 | 0.4 | 2205 | 9 |
| InputEvent | 4260 | 0.0 | 1.504 | 223.482 | 16.239 | 370934.889 | 0.27 | 89 | 11 |
| PlayerPositionEvent | 2411 | 9.728 | 10.001 | 372.476 | 10.115 | 370750.107 | 0.16 | 0 | 8 |
| DialogueEvent | 2081 | 0.0 | 4.586 | 457.746 | 51.796 | 370756.864 | 0.13 | 574 | 9 |
| ObjectInterEvent | 461 | 0.0 | 7.816 | 2064.363 | 342.374 | 372392.057 | 0.03 | 4 | 15 |
| argumentationNodeEvent | 387 | 0.004 | 0.737 | 2453.975 | 10.734 | 548356.161 | 0.02 | 46 | 5 |
| Soil Key Puzzle | 199 | 0.001 | 0.431 | 3031.856 | 8.547 | 372388.956 | 0.02 | 8 | 3 |
| TopographicMapEvent | 86 | 0.023 | 7.024 | 9405.02 | 77962.539 | 371160.907 | 0.01 | 2 | 10 |
| questEvent | 83 | 0.0 | 273.536 | 11474.081 | 83911.229 | 371435.847 | 0.01 | 15 | 21 |
| DEBUGMenu | 37 | 6.956 | 578.156 | 25671.065 | 85809.492 | 373086.862 | 0.0 | 0 | 18 |
| WaterChamberEvent | 33 | 0.271 | 20.592 | 30.95 | 109.749 | 166.031 | 1.94 | 0 | 0 |
| DaniEvent | 25 | 1.375 | 6.825 | 20724.747 | 81140.211 | 371147.411 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 19 | 213.835 | 4349.837 | 49991.388 | 115561.165 | 373098.957 | 0.0 | 0 | 15 |
| gameStartEvent | 17 | 213.835 | 31020.211 | 55872.727 | 144176.475 | 373098.957 | 0.0 | 0 | 15 |
| soilMachine | 16 | 0.823 | 17.099 | 76.712 | 277.529 | 279.559 | 0.78 | 0 | 0 |
| argumentationEvent | 15 | 0.037 | 111.137 | 63312.864 | 306460.807 | 548336.204 | 0.0 | 2 | 5 |
| argumentationAnswerEvent | 13 | 15.87 | 115.419 | 73052.649 | 341108.247 | 548403.823 | 0.0 | 0 | 5 |
| TerasGardenBox | 7 | 0.991 | 13.711 | 18.816 | 46.493 | 47.233 | 3.19 | 0 | 0 |
| gameWindowUnfocusEvent | 7 | 264.502 | 85347.229 | 115542.744 | 388887.97 | 518402.409 | 0.0 | 0 | 6 |
| EndOfUnit | 4 | 55488.719 | 130194.33 | 216074.222 | 487531.203 | 548419.509 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 2.055 | 7.573 | 6.327 | 9.174 | 9.352 | 9.48 | 0 | 0 |
| argumentationToolEvent | 3 | 1.76 | 2.627 | 28532.07 | 77032.902 | 85591.822 | 0.0 | 0 | 1 |
| chatEvent | 2 | 1529.395 | 27103.483 | 27103.482 | 50120.161 | 52677.57 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 11 group(s), 21 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[5351] _id=6acd7630de269131f9ce7521 ts=2026-10-13T00:07:11.3860000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[5352] _id=6acd7630de269131f9ce7522 ts=2026-10-13T00:07:11.3860000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[6977] _id=6acd7b2bde269131f9ce7ffc ts=2026-10-13T00:28:27.4750000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[6978] _id=6acd7b2bde269131f9ce7ffd ts=2026-10-13T00:28:27.4750000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[9273] _id=6ace63edde269131f9cffba3 ts=2026-10-13T17:01:32.3230000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[9274] _id=6ace63edde269131f9cffba4 ts=2026-10-13T17:01:32.3230000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 80 group(s), 137 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[1678] _id=6ac67796de269131f9bd279b ts=2026-10-07T16:47:17.0540000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[1679] _id=6ac67796de269131f9bd27a5 ts=2026-10-07T16:47:17.0540000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1687] _id=6ac677a0de269131f9bd2960 ts=2026-10-07T16:47:26.0180000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[1693] _id=6ac677a1de269131f9bd2987 ts=2026-10-07T16:47:26.0180000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1694] _id=6ac677a1de269131f9bd2988 ts=2026-10-07T16:47:26.3030000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[1697] _id=6ac677a1de269131f9bd2989 ts=2026-10-07T16:47:26.3030000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[15174] _id=6ad25647de269131f9e630be ts=2026-10-16T16:52:22.8870000Z == 6ab9a8e69a8420a1e6b56b1f.jsonl[15175] _id=6ad25647de269131f9e630bf ts=2026-10-16T16:52:22.8870000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 139 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[198] _id=6ac3d378de269131f9adf499 ts=2026-10-05T16:42:31.5190000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[196] _id=6ac3d378de269131f9adf49b ts=2026-10-05T16:42:31.5250000Z`; `249ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[324] _id=6ac3d584de269131f9ae263b ts=2026-10-05T16:51:15.5730000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[318] _id=6ac3d584de269131f9ae2645 ts=2026-10-05T16:51:15.8220000Z`; `206ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[318] _id=6ac3d584de269131f9ae2645 ts=2026-10-05T16:51:15.8220000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[327] _id=6ac3d584de269131f9ae264d ts=2026-10-05T16:51:16.0280000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `625ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10784] _id=6ad0fdcfde269131f9dd69b2 ts=2026-10-15T16:22:39.2170000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[10785] _id=6ad0fdd0de269131f9dd69c3 ts=2026-10-15T16:22:39.8420000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `641ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[14608] _id=6ad2518ede269131f9e5e7bf ts=2026-10-16T16:32:13.9080000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[14607] _id=6ad2518fde269131f9e5e7ce ts=2026-10-16T16:32:14.5490000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[9045] _id=6ace61b9de269131f9cfd0e3 ts=2026-10-13T16:52:08.9620000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[9048] _id=6ace61b9de269131f9cfd0e6 ts=2026-10-13T16:52:08.9990000Z`; `46ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[13547] _id=6ad17b53de269131f9e27102 ts=2026-10-16T01:18:10.4170000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[13563] _id=6ad17b53de269131f9e27105 ts=2026-10-16T01:18:10.4630000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[501] _id=6ac3d84ade269131f9ae6c77 ts=2026-10-05T17:03:05.4740000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[507] _id=6ac3d84ade269131f9ae6c79 ts=2026-10-05T17:03:05.5040000Z`; `45ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[549] _id=6ac3d84cde269131f9ae6ca3 ts=2026-10-05T17:03:07.4460000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[550] _id=6ac3d84cde269131f9ae6ca9 ts=2026-10-05T17:03:07.4910000Z`; `30ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[527] _id=6ac3d84dde269131f9ae6cb9 ts=2026-10-05T17:03:08.3210000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[556] _id=6ac3d84dde269131f9ae6cbb ts=2026-10-05T17:03:08.3510000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[15320] _id=6ad257c7de269131f9e64cb7 ts=2026-10-16T16:58:46.6840000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[15321] _id=6ad257c7de269131f9e64cb9 ts=2026-10-16T16:58:46.6900000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `823ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[12068] _id=6ad101b8de269131f9ddb38c ts=2026-10-15T16:39:20.4450000Z ~ 6ab9a8e69a8420a1e6b56b1f.jsonl[12071] _id=6ad101b9de269131f9ddb393 ts=2026-10-15T16:39:21.2680000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 103h 38m 
  - Evidence: 103h 38m: 6ab9a8e69a8420a1e6b56b1f.jsonl[3353] _id=6ac7c4bcde269131f9c426ed ts=2026-10-08T16:28:44.5370000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5333] _id=6acd761cde269131f9ce7515 ts=2026-10-13T00:06:51.3990000Z; 24h 9m: 6ab9a8e69a8420a1e6b56b1f.jsonl[81] _id=6ac3d1fcde269131f9add757 ts=2026-10-05T16:36:11.9060000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[576] _id=6ac525c9de269131f9b54154 ts=2026-10-06T16:46:00.6010000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1593] _id=6ac676a6de269131f9bcfc70 ts=2026-10-07T16:43:17.9530000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[3349] _id=6ac7c4b1de269131f9c42639 ts=2026-10-08T16:28:32.6440000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 103h 5m 
  - Evidence: 103h 5m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5198] _id=6ac7cce9de269131f9c4ddb4 ts=2026-10-08T17:03:37.5050000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5386] _id=6acd76b5de269131f9ce757b ts=2026-10-13T00:09:24.9160000Z; 24h 21m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1440] _id=6ac6764bde269131f9bceddf ts=2026-10-07T16:41:46.5400000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5202] _id=6ac7cce3de269131f9c4dd60 ts=2026-10-08T17:03:30.6800000Z; 15h 14m: 6ab9a8e69a8420a1e6b56b1f.jsonl[7724] _id=6acd8488de269131f9ce86c8 ts=2026-10-13T01:08:24.2050000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[7977] _id=6ace5aedde269131f9cf6150 ts=2026-10-13T16:23:08.6990000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 102h 59m 
  - Evidence: 102h 59m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5266] _id=6ac7cdeade269131f9c4e0be ts=2026-10-08T17:07:54.5440000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5355] _id=6acd7630de269131f9ce7525 ts=2026-10-13T00:07:11.4080000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b1f.jsonl[569] _id=6ac3d888de269131f9ae7175 ts=2026-10-05T17:04:07.1920000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[637] _id=6ac52649de269131f9b55575 ts=2026-10-06T16:48:08.4890000Z; 23h 30m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1024] _id=6ac529e5de269131f9b60157 ts=2026-10-06T17:03:33.2050000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[1100] _id=6ac6748bde269131f9bc95b6 ts=2026-10-07T16:34:18.9260000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 574 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[13480] _id=6ad17ad0de269131f9e26ea6 ts=2026-10-16T01:15:59.1330000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13481] _id=6ad17ad0de269131f9e26ea7 ts=2026-10-16T01:15:59.1330000Z; 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[15105] _id=6ad255ebde269131f9e62929 ts=2026-10-16T16:50:50.8990000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[15106] _id=6ad255ebde269131f9e6292a ts=2026-10-16T16:50:50.8990000Z; 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[9030] _id=6ace6196de269131f9cfced0 ts=2026-10-13T16:51:33.5140000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[9031] _id=6ace6196de269131f9cfced1 ts=2026-10-13T16:51:33.5140000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 152h 20m 
  - Evidence: 152h 20m: 6ab9a8e69a8420a1e6b56b1f.jsonl[966] _id=6ac528c6de269131f9b5cbe7 ts=2026-10-06T16:58:45.9200000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[7257] _id=6acd8709de269131f9ce890e ts=2026-10-13T01:19:05.4290000Z; 39h 34m: 6ab9a8e69a8420a1e6b56b1f.jsonl[7257] _id=6acd8709de269131f9ce890e ts=2026-10-13T01:19:05.4290000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10675] _id=6acfb3abde269131f9d60509 ts=2026-10-14T16:54:02.8990000Z; 32h 44m: 6ab9a8e69a8420a1e6b56b1f.jsonl[10675] _id=6acfb3abde269131f9d60509 ts=2026-10-14T16:54:02.8990000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13952] _id=6ad1802fde269131f9e28abc ts=2026-10-16T01:38:54.0890000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 103h 2m 
  - Evidence: 103h 2m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5241] _id=6ac7cd38de269131f9c4e062 ts=2026-10-08T17:04:56.4950000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5349] _id=6acd7630de269131f9ce751f ts=2026-10-13T00:07:11.3840000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b1f.jsonl[534] _id=6ac3d7eede269131f9ae63f9 ts=2026-10-05T17:01:33.9180000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[579] _id=6ac525cfde269131f9b54205 ts=2026-10-06T16:46:06.8080000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1047] _id=6ac52a06de269131f9b607af ts=2026-10-06T17:04:05.8140000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[1070] _id=6ac67459de269131f9bc9130 ts=2026-10-07T16:33:28.6410000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 89 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10143] _id=6acfafd6de269131f9d59db3 ts=2026-10-14T16:37:41.0660000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10144] _id=6acfafd6de269131f9d59db4 ts=2026-10-14T16:37:41.0660000Z; 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10612] _id=6acfb2f8de269131f9d5f4c0 ts=2026-10-14T16:51:03.2310000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10613] _id=6acfb2f8de269131f9d5f4c1 ts=2026-10-14T16:51:03.2310000Z; 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10613] _id=6acfb2f8de269131f9d5f4c1 ts=2026-10-14T16:51:03.2310000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10614] _id=6acfb2f8de269131f9d5f4c2 ts=2026-10-14T16:51:03.2310000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 103h 26m 
  - Evidence: 103h 26m: 6ab9a8e69a8420a1e6b56b1f.jsonl[4916] _id=6ac7c90dde269131f9c4a0b8 ts=2026-10-08T16:47:09.2320000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5471] _id=6acd77b6de269131f9ce7619 ts=2026-10-13T00:13:41.2890000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b1f.jsonl[536] _id=6ac3d7f3de269131f9ae6489 ts=2026-10-05T17:01:38.3990000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[580] _id=6ac525cfde269131f9b54201 ts=2026-10-06T16:46:06.7970000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1046] _id=6ac52a06de269131f9b607a9 ts=2026-10-06T17:04:05.8120000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[1140] _id=6ac674d3de269131f9bca028 ts=2026-10-07T16:35:30.7870000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[13317] _id=6ad1792ede269131f9e26689 ts=2026-10-16T01:09:01.0980000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13318] _id=6ad1792ede269131f9e2668a ts=2026-10-16T01:09:01.0980000Z; 1ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[13270] _id=6ad178cfde269131f9e264b4 ts=2026-10-16T01:07:26.0840000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13271] _id=6ad178cfde269131f9e264b5 ts=2026-10-16T01:07:26.0850000Z; 1ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[6428] _id=6acd7aa3de269131f9ce7c4c ts=2026-10-13T00:26:11.2520000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[6444] _id=6acd7aa3de269131f9ce7c4e ts=2026-10-13T00:26:11.2530000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 102h 59m 
  - Evidence: 102h 59m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5265] _id=6ac7cdecde269131f9c4e0c0 ts=2026-10-08T17:07:55.9830000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5348] _id=6acd7630de269131f9ce751e ts=2026-10-13T00:07:06.0900000Z; 23h 41m: 6ab9a8e69a8420a1e6b56b1f.jsonl[568] _id=6ac3d887de269131f9ae7169 ts=2026-10-05T17:04:06.6740000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[578] _id=6ac525cbde269131f9b5419f ts=2026-10-06T16:46:00.6210000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1056] _id=6ac52a0dde269131f9b608e0 ts=2026-10-06T17:04:12.8210000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[1065] _id=6ac67451de269131f9bc9090 ts=2026-10-07T16:33:18.0400000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 103h 35m 
  - Evidence: 103h 35m: 6ab9a8e69a8420a1e6b56b1f.jsonl[4908] _id=6ac7c8dade269131f9c49c62 ts=2026-10-08T16:46:16.2630000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5595] _id=6acd797fde269131f9ce773a ts=2026-10-13T00:21:18.0400000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b1f.jsonl[9671] _id=6acfac39de269131f9d55bcb ts=2026-10-14T16:22:14.7020000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10885] _id=6ad0fddcde269131f9dd6ad4 ts=2026-10-15T16:22:52.1960000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b1f.jsonl[3254] _id=6ac67a50de269131f9bd6bf3 ts=2026-10-07T16:58:54.0880000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[3397] _id=6ac7c52cde269131f9c42eb3 ts=2026-10-08T16:30:36.5470000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2205 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10876] _id=6ad0fddfde269131f9dd6b07 ts=2026-10-15T16:22:53.5610000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10877] _id=6ad0fddfde269131f9dd6b08 ts=2026-10-15T16:22:53.5610000Z; 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10881] _id=6ad0fde1de269131f9dd6b3f ts=2026-10-15T16:22:54.7350000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10904] _id=6ad0fde1de269131f9dd6b41 ts=2026-10-15T16:22:54.7350000Z; 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10885] _id=6ad0fddcde269131f9dd6ad4 ts=2026-10-15T16:22:52.1960000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10889] _id=6ad0fddcde269131f9dd6ad6 ts=2026-10-15T16:22:52.1960000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 103h 26m 
  - Evidence: 103h 26m: 6ab9a8e69a8420a1e6b56b1f.jsonl[4918] _id=6ac7c910de269131f9c4a100 ts=2026-10-08T16:47:12.3270000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5461] _id=6acd77b5de269131f9ce7617 ts=2026-10-13T00:13:41.2830000Z; 47h 20m: 6ab9a8e69a8420a1e6b56b1f.jsonl[9249] _id=6ace63c6de269131f9cff771 ts=2026-10-13T17:00:53.3210000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10798] _id=6ad0fd83de269131f9dd626b ts=2026-10-15T16:21:23.1320000Z; 16h 39m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5587] _id=6acd7957de269131f9ce7714 ts=2026-10-13T00:20:39.3060000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[9237] _id=6ace63abde269131f9cff495 ts=2026-10-13T17:00:26.2540000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10867] _id=6ad0fdd0de269131f9dd69d7 ts=2026-10-15T16:22:40.1560000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10868] _id=6ad0fdd0de269131f9dd69d8 ts=2026-10-15T16:22:40.1570000Z; 2ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[9211] _id=6ace63bdde269131f9cff669 ts=2026-10-13T17:00:44.7570000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[9212] _id=6ace63bdde269131f9cff66a ts=2026-10-13T17:00:44.7590000Z; 6ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[10785] _id=6ad0fdd0de269131f9dd69c3 ts=2026-10-15T16:22:39.8420000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10866] _id=6ad0fdd0de269131f9dd69cb ts=2026-10-15T16:22:39.8480000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 103h 6m 
  - Evidence: 103h 6m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5197] _id=6ac7ccddde269131f9c4dd42 ts=2026-10-08T17:03:25.6820000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5393] _id=6acd76b7de269131f9ce7581 ts=2026-10-13T00:09:26.5890000Z; 32h 5m: 6ab9a8e69a8420a1e6b56b1f.jsonl[10601] _id=6acfb2bcde269131f9d5ec87 ts=2026-10-14T16:50:03.5170000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[12910] _id=6ad1760bde269131f9e25317 ts=2026-10-16T00:55:37.9080000Z; 23h 42m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1777] _id=6ac677d9de269131f9bd301e ts=2026-10-07T16:48:24.9920000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[3404] _id=6ac7c541de269131f9c430bf ts=2026-10-08T16:30:57.3550000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.035s shown 
  - Evidence: 23ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[5089] _id=6ac7cb57de269131f9c4c283 ts=2026-10-08T16:56:54.7980000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5093] _id=6ac7cb57de269131f9c4c287 ts=2026-10-08T16:56:54.8210000Z; 35ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[5088] _id=6ac7cb57de269131f9c4c27f ts=2026-10-08T16:56:54.7630000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5089] _id=6ac7cb57de269131f9c4c283 ts=2026-10-08T16:56:54.7980000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 152h 20m 
  - Evidence: 152h 20m: 6ab9a8e69a8420a1e6b56b1f.jsonl[747] _id=6ac52796de269131f9b5832f ts=2026-10-06T16:53:41.6330000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[7784] _id=6acd85c9de269131f9ce8839 ts=2026-10-13T01:13:45.4560000Z; 56h 21m: 6ab9a8e69a8420a1e6b56b1f.jsonl[9050] _id=6ace61b9de269131f9cfd0dd ts=2026-10-13T16:52:08.9450000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13432] _id=6ad17a59de269131f9e26d1f ts=2026-10-16T01:14:00.1410000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b1f.jsonl[558] _id=6ac3d84fde269131f9ae6cd7 ts=2026-10-05T17:03:10.1740000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[689] _id=6ac526b5de269131f9b5649b ts=2026-10-06T16:49:56.8230000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 152h 18m 
  - Evidence: 152h 18m: 6ab9a8e69a8420a1e6b56b1f.jsonl[748] _id=6ac52796de269131f9b58334 ts=2026-10-06T16:53:41.6550000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[7812] _id=6acd8586de269131f9ce87ed ts=2026-10-13T01:12:37.8590000Z; 56h 19m: 6ab9a8e69a8420a1e6b56b1f.jsonl[9048] _id=6ace61b9de269131f9cfd0e6 ts=2026-10-13T16:52:08.9990000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13368] _id=6ad179e9de269131f9e26af2 ts=2026-10-16T01:12:08.9210000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b1f.jsonl[561] _id=6ac3d856de269131f9ae6d81 ts=2026-10-05T17:03:17.7820000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[671] _id=6ac526a1de269131f9b56233 ts=2026-10-06T16:49:36.1210000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.037s..0.046s shown 
  - Evidence: 37ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[9045] _id=6ace61b9de269131f9cfd0e3 ts=2026-10-13T16:52:08.9620000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[9048] _id=6ace61b9de269131f9cfd0e6 ts=2026-10-13T16:52:08.9990000Z; 46ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[13547] _id=6ad17b53de269131f9e27102 ts=2026-10-16T01:18:10.4170000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13563] _id=6ad17b53de269131f9e27105 ts=2026-10-16T01:18:10.4630000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 152h 19m 
  - Evidence: 152h 19m: 6ab9a8e69a8420a1e6b56b1f.jsonl[742] _id=6ac52794de269131f9b582df ts=2026-10-06T16:53:39.5740000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[7813] _id=6acd8598de269131f9ce87f4 ts=2026-10-13T01:12:55.7350000Z; 56h 20m: 6ab9a8e69a8420a1e6b56b1f.jsonl[9042] _id=6ace61a4de269131f9cfcfa6 ts=2026-10-13T16:51:47.8480000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13372] _id=6ad179e6de269131f9e26add ts=2026-10-16T01:12:06.0490000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b1f.jsonl[557] _id=6ac3d84ede269131f9ae6cc9 ts=2026-10-05T17:03:09.1790000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[672] _id=6ac526a3de269131f9b56261 ts=2026-10-06T16:49:38.7970000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 46 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[13418] _id=6ad17a3ede269131f9e26cac ts=2026-10-16T01:13:33.6350000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13420] _id=6ad17a3ede269131f9e26cb0 ts=2026-10-16T01:13:33.6390000Z; 4ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[8958] _id=6ace6147de269131f9cfc928 ts=2026-10-13T16:50:14.7410000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[8959] _id=6ace6147de269131f9cfc92a ts=2026-10-13T16:50:14.7450000Z; 5ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[685] _id=6ac526b2de269131f9b56439 ts=2026-10-06T16:49:53.8930000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[686] _id=6ac526b2de269131f9b5643b ts=2026-10-06T16:49:53.8980000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 46m 
  - Evidence: 23h 46m: 6ab9a8e69a8420a1e6b56b1f.jsonl[504] _id=6ac3d846de269131f9ae6c3d ts=2026-10-05T17:03:01.6380000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[665] _id=6ac5269ede269131f9b56207 ts=2026-10-06T16:49:33.4600000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 14h 37m 
  - Evidence: 14h 37m: 6ab9a8e69a8420a1e6b56b1f.jsonl[13961] _id=6ad1805bde269131f9e28b61 ts=2026-10-16T01:39:38.7450000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[13984] _id=6ad24e20de269131f9e5ac3b ts=2026-10-16T16:17:36.3150000Z; 25m 29s: 6ab9a8e69a8420a1e6b56b1f.jsonl[13984] _id=6ad24e20de269131f9e5ac3b ts=2026-10-16T16:17:36.3150000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[14928] _id=6ad2541ade269131f9e60a73 ts=2026-10-16T16:43:05.7100000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 103h 38m 
  - Evidence: 103h 38m: 6ab9a8e69a8420a1e6b56b1f.jsonl[3351] _id=6ac7c4b1de269131f9c4263b ts=2026-10-08T16:28:32.7780000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5346] _id=6acd761cde269131f9ce7518 ts=2026-10-13T00:06:51.7350000Z; 24h 9m: 6ab9a8e69a8420a1e6b56b1f.jsonl[44] _id=6ac3d1f3de269131f9add69b ts=2026-10-05T16:36:02.5700000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[573] _id=6ac52595de269131f9b53a25 ts=2026-10-06T16:45:08.4250000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b1f.jsonl[1592] _id=6ac67691de269131f9bcf8f9 ts=2026-10-07T16:42:56.3150000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[3351] _id=6ac7c4b1de269131f9c4263b ts=2026-10-08T16:28:32.7780000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 103h 38m 
  - Evidence: 103h 38m: 6ab9a8e69a8420a1e6b56b1f.jsonl[3350] _id=6ac7c4b1de269131f9c4263a ts=2026-10-08T16:28:32.7780000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5332] _id=6acd761cde269131f9ce7517 ts=2026-10-13T00:06:51.7350000Z; 24h 9m: 6ab9a8e69a8420a1e6b56b1f.jsonl[43] _id=6ac3d1f3de269131f9add696 ts=2026-10-05T16:36:02.5690000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[570] _id=6ac52595de269131f9b53a21 ts=2026-10-06T16:45:08.4240000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b1f.jsonl[8340] _id=6ace5dfdde269131f9cf89f9 ts=2026-10-13T16:36:13.0010000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[9542] _id=6acfabc0de269131f9d55226 ts=2026-10-14T16:20:15.6570000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6ab9a8e69a8420a1e6b56b1f.jsonl[3352] _id=6ac7c4b0de269131f9c42637 ts=2026-10-07T17:04:17.124Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[9540] _id=6acfabc0de269131f9d55220 ts=2026-10-13T17:04:19.533Z; 24h 4m: 6ab9a8e69a8420a1e6b56b1f.jsonl[10706] _id=6acfb4eade269131f9d621cb ts=2026-10-14T16:59:21.8130000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[12905] _id=6ad175fdde269131f9e252a9 ts=2026-10-15T17:04:09.424Z; 23h 55m: 6ab9a8e69a8420a1e6b56b1f.jsonl[9540] _id=6acfabc0de269131f9d55220 ts=2026-10-13T17:04:19.533Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[10706] _id=6acfb4eade269131f9d621cb ts=2026-10-14T16:59:21.8130000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 103h 10m 
  - Evidence: 103h 10m: 6ab9a8e69a8420a1e6b56b1f.jsonl[5079] _id=6ac7cb43de269131f9c4c129 ts=2026-10-08T16:56:35.6080000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[5357] _id=6acd7630de269131f9ce7527 ts=2026-10-13T00:07:11.4550000Z; 23h 44m: 6ab9a8e69a8420a1e6b56b1f.jsonl[539] _id=6ac3d7f3de269131f9ae64a5 ts=2026-10-05T17:01:38.4310000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[577] _id=6ac525cbde269131f9b541a3 ts=2026-10-06T16:46:02.4540000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b1f.jsonl[997] _id=6ac52992de269131f9b5f24f ts=2026-10-06T17:02:09.9250000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[1066] _id=6ac67451de269131f9bc9091 ts=2026-10-07T16:33:20.3530000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[15174] _id=6ad25647de269131f9e630be ts=2026-10-16T16:52:22.8870000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[15175] _id=6ad25647de269131f9e630bf ts=2026-10-16T16:52:22.8870000Z; 1ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[12911] _id=6ad1760bde269131f9e25318 ts=2026-10-16T00:55:38.0230000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[12912] _id=6ad1760bde269131f9e25319 ts=2026-10-16T00:55:38.0240000Z; 2ms: 6ab9a8e69a8420a1e6b56b1f.jsonl[537] _id=6ac3d7f3de269131f9ae649a ts=2026-10-05T17:01:38.4290000Z -> 6ab9a8e69a8420a1e6b56b1f.jsonl[539] _id=6ac3d7f3de269131f9ae64a5 ts=2026-10-05T17:01:38.4310000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[7077] _id=6acd7c07de269131f9ce80a3 ts=2026-10-13T00:32:07.4520000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[7251] _id=6acd7e05de269131f9ce81f5 ts=2026-10-13T00:40:37.4430000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[7308] _id=6acd7fbbde269131f9ce82a4 ts=2026-10-13T00:47:54.9760000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[9048] _id=6ace61b9de269131f9cfd0e6 ts=2026-10-13T16:52:08.9990000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[13563] _id=6ad17b53de269131f9e27105 ts=2026-10-16T01:18:10.4630000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[507] _id=6ac3d84ade269131f9ae6c79 ts=2026-10-05T17:03:05.5040000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[550] _id=6ac3d84cde269131f9ae6ca9 ts=2026-10-05T17:03:07.4910000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[556] _id=6ac3d84dde269131f9ae6cbb ts=2026-10-05T17:03:08.3510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[13961] _id=6ad1805bde269131f9e28b61 ts=2026-10-16T01:39:38.7450000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[13984] _id=6ad24e20de269131f9e5ac3b ts=2026-10-16T16:17:36.3150000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[14928] _id=6ad2541ade269131f9e60a73 ts=2026-10-16T16:43:05.7100000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[11883] _id=6ad0fff7de269131f9dd97ca ts=2026-10-15T16:31:50.7020000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[5305] _id=6acd7630de269131f9ce751c ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 174 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[1588] _id=6ac67691de269131f9bcf8ee ts=2026-10-07T16:42:34.701Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[2001] _id=6ac6786ade269131f9bd3cd6 ts=2026-10-07T16:50:49.5450000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[2075] _id=6ac67883de269131f9bd4013 ts=2026-10-07T16:51:13.2320000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 775 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[1589] _id=6ac67691de269131f9bcf8ef ts=2026-10-07T16:42:34.703Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1678] _id=6ac67796de269131f9bd279b ts=2026-10-07T16:47:17.0540000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1679] _id=6ac67796de269131f9bd27a5 ts=2026-10-07T16:47:17.0540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 DEBUGMenu record in 'Unit 3 Dev' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[7236] _id=6acd8724de269131f9ce8917 ts=2026-10-13T01:19:31.5750000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 387 start, 377 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'BecameCameraCentered' (totals: 944 open, 939 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 43 unmatched 'BecameVisible' (totals: 1687 open, 1644 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 50 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 461 of 15415 adjacent _id pairs reverse in client time; worst 182.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b1f.jsonl[1295] _id=6ac675fcde269131f9bce210 ts=2026-10-07T16:40:27.0670000Z`; `6ab9a8e69a8420a1e6b56b1f.jsonl[1298] _id=6ac675fcde269131f9bce237 ts=2026-10-07T16:37:24.8100000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.87s, min -84506.09s, max -0.29s over 15416 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b1f\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 5214 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3786); Unit 4 Dev (812); Unit 5 Dev - Dungeon (350); Unit 3 Dungeon Dev (266)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.20s, n=5213)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5214/5214 records)
    "BecameVisible"  x1687
    "BecameInvisible"  x1644
    "BecameCameraCentered"  x944
    "BecameCameraUncentered"  x939
data.pieceId  (string, 5214/5214 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5214/5214 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4261 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1275); Unit 3 Dev (933); Unit 4 Dev - Dungeon (677); Unit 3 Dungeon Dev (334); Unit 5 Dev - Dungeon (320); Unit 1 Dev (283); Unit 4 Dev (257); Unit 4 Dev - Anderson Base (100); Unit 5 Dev (82)
- **Intervals:** median 1.50s (p5 0.13s / p95 16.24s, n=4260)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4261/4261 records)
    "pressed"  x4261
data.actionType  (string, 4261/4261 records)
    "Move"  x3004
    "Interact"  x739
    "Sprint"  x226
    "Jump"  x169
    "Ascend"  x51
    "Hoverboard"  x30
    "Descend"  x20
    "Map"  x9
    "Pause"  x9
    "SkipCinematic"  x2
    "ToggleDebug"  x2
data.key  (string, 4261/4261 records, 10 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4261/4261 records)
    "Player"  x3557
    "Drone"  x704
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2423 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (862); Unit 3 Dev (325); Unit 1 Dev (295); Unit 4 Dev (263); Unit 4 Dev - Dungeon (197); Unit 5 Dev - Dungeon (151); Unit 5 Dev (121); Unit 3 Dungeon Dev (118); Unit 4 Dev - Anderson Base (91)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=2411)
- **Fields under `data`:**

```text
data.position  (object, 2423/2423 records)
data.position.x  (number, 2423/2423 records)
    numeric range -686.415 .. 1554.02 (974 unique)
data.position.y  (number, 2423/2423 records)
    numeric range -115.052 .. 222.113 (574 unique)
data.position.z  (number, 2423/2423 records)
    numeric range -1259.06 .. 1804.77 (975 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2082 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (652); Unit 3 Dev (316); Unit 4 Dev (281); Unit 1 Dev (236); Unit 5 Dev (217); Unit 3 Dungeon Dev (112); Unit 4 Dev - Dungeon (97); Unit 4 Dev - Anderson Base (86); Unit 5 Dev - Dungeon (85)
- **eventKey:** present on 1318 of 2082 records
- **Intervals:** median 4.59s (p5 0.01s / p95 51.80s, n=2081)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1318; [conversationId, dialogueEventType] x764
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2082/2082 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2082/2082 records)
    "DialogueNodeEvent"  x1318
    "DialogueStartEvent"  x387
    "DialogueFinishEvent"  x377
data.nodeId  (number, 1318/2082 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 462 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (161); Unit 4 Dev - Dungeon (91); Unit 3 Dev (68); Unit 1 Dev (55); Unit 3 Dungeon Dev (37); Unit 4 Dev (18); Unit 5 Dev - Dungeon (14); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (9)
- **Intervals:** median 7.82s (p5 0.14s / p95 342.37s, n=461)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 462/462 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 462/462 records)
    108 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 388 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (131); Unit 3 Dev (123); Unit 1 Dev (55); Unit 5 Dev (44); Unit 2 Prod (Refactor) (35)
- **Intervals:** median 0.74s (p5 0.03s / p95 10.73s, n=387)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 388/388 records)
    "argumentationNodeHoverEnd"  x168
    "argumentationNodeHoverStart"  x164
    "argumentationNodeAdd"  x38
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 388/388 records)
    "Unit 4 - Flooding"  x131
    "Unit 3 - Pollution Upstream"  x123
    "Unit 5"  x44
    "Unit 2 – Watershed"  x35
    "Unit 1 - Argumentation Tutorial"  x34
    "Unit 1 - Freshwater"  x21
data.nodeName  (string, 388/388 records)
    "A"  x66
    "1"  x56
    "II"  x51
    "B"  x42
    "3"  x37
    "I"  x34
    "D"  x28
    "4"  x26
    "2"  x23
    "C"  x18
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 200 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (88); Unit 4 Dev (88); Unit 3 Dev (24)
- **Intervals:** median 0.43s (p5 0.13s / p95 8.55s, n=199)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x192; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/200 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/200 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 192/200 records)
    "RightDrag"  x99
    "LeftDrag"  x93
data.currentSoilType  (string, 192/200 records)
    "CLAYSAND"  x43
    "SAND"  x43
    "CLAY"  x35
    "SANDGRAVEL"  x30
    "CLAYROCK"  x23
    "GRAVEL"  x12
    "BEDROCK"  x6
data.isCorrectSelection  (string, 192/200 records)
    "false"  x145
    "true"  x47
data.waterLevelStatus  (string, 192/200 records)
    "TooHigh"  x87
    "Proper"  x77
    "TooLow"  x28
data.waterRetentionChange  (string, 192/200 records)
    "Increase"  x77
    "Decrease"  x68
    "NoChange"  x47
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 87 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (42); Unit 3 Dev (39); Unit 4 Dev (4); Unit 1 Dev (2)
- **Intervals:** median 7.02s (p5 1.24s / p95 77962.54s, n=86)
- **`data` key-set variants:** [actionType, featureUsed] x52; [actionType, featureUsed, location] x33; [actionType, featureUsed, legendName] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 87/87 records)
    "MapCloseEvent"  x26
    "MapOpenEvent"  x26
    "WaypointMoveEvent"  x26
    "WaypointSetEvent"  x7
    "Selected"  x2
data.featureUsed  (string, 87/87 records)
    "Map"  x52
    "Waypoint"  x33
    "Legend"  x2
data.legendName  (string, 2/87 records)
    "120 ft"  x1
    "180 ft"  x1
data.location  (object, 33/87 records)
data.location.x  (number, 33/87 records)
    numeric range -471.249 .. 654.711 (30 unique)
data.location.y  (number, 33/87 records)
    numeric range -360.342 .. 310.139 (33 unique)
data.location.z  (number, 33/87 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 1 Dev (16); Unit 4 Dev (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (8); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 273.54s (p5 0.01s / p95 83911.23s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x34
data.questID  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/84 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DEBUGMenu` — 38 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (14); Unit 2 Prod (Refactor) (5); Unit 3 Dev (5); Unit 4 Dev (5); Unit 1 Dev (3); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 578.16s (p5 9.47s / p95 85809.49s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "DebugMenuStateChanged"  x38
data.isOpened  (bool, 38/38 records)
    false  x38
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 34 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (34)
- **Intervals:** median 20.59s (p5 0.59s / p95 109.75s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "On"  x22
    "Off"  x12
data.floor  (string, 34/34 records)
    "3"  x14
    "4"  x10
    "1"  x5
    "2"  x5
data.machineNumber  (string, 34/34 records)
    "One"  x33
    "Two"  x1
data.machineType  (string, 34/34 records)
    "Condenser"  x20
    "Evaporator"  x9
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 34/34 records)
    "2"  x21
    "3"  x6
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DaniEvent` — 26 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 3 Dev (8)
- **Intervals:** median 6.83s (p5 1.69s / p95 81140.21s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "Close"  x13
    "Open"  x13
data.toolName  (string, 26/26 records, 26 empty-string)
    ""  x26
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1)
- **Intervals:** median 4349.84s (p5 237.89s / p95 115561.17s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 31020.21s (p5 482.13s / p95 144176.48s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 17 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (17)
- **Intervals:** median 17.10s (p5 1.00s / p95 277.53s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "ChangeCanister"  x17
data.canisterType  (string, 17/17 records)
    "Gravel"  x8
    "Clay"  x4
    "Bedrock"  x3
    "Sand"  x2
data.floor  (string, 17/17 records)
    "4"  x8
    "2"  x5
    "5"  x3
    "3"  x1
data.machine  (string, 17/17 records)
    "1"  x16
    "2"  x1
data.row  (string, 17/17 records)
    "TopRow"  x17
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 111.14s (p5 0.04s / p95 306460.81s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 16/16 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationAnswerEvent` — 14 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (5); Unit 1 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 115.42s (p5 20.60s / p95 341108.25s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "submitAnswerEvent"  x14
data.answerSubmitted  (string, 14/14 records)
    "A,1,I"  x3
    "A,1,II"  x1
    "A,5,I"  x1
    "B,5,I"  x1
    "B,C,A,2,II"  x1
    "B,C,D,2,II"  x1
    "B,C,D,4,II"  x1
    "C,D,3,4,II"  x1
    "C,D,3,II"  x1
    "C,D,A,2,II"  x1
    "D,1,II"  x1
    "D,C,B,1,II"  x1
data.argumentationTitle  (string, 14/14 records)
    "Unit 4 - Flooding"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 13.71s (p5 1.04s / p95 46.49s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x4
data.boxId  (string, 8/8 records)
    "1"  x3
    "2"  x3
    "0"  x2
data.soilType  (string, 8/8 records)
    "Sand"  x3
    "Clay"  x2
    "Gravel"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 4 Dev (2); PodsEscapingCopernicus Cutscene (1); Unit 3 Dungeon Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 85347.23s (p5 501.05s / p95 388887.97s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 130194.33s (p5 64849.09s / p95 487531.20s, n=4)
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

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 7.57s (p5 2.61s / p95 9.17s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted Out"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Cold"  x1
    "Covered"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 2.63s (p5 1.85s / p95 77032.90s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 27103.48s (p5 4086.80s / p95 50120.16s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
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
    "unit2"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (88 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (26x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (33x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*