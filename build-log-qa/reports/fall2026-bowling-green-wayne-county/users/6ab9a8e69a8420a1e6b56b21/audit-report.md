# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b21

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b21
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b21.jsonl
- **Records:** 10723 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b21
- **Time span:** 2026-10-05T16:31:45.387000+00:00 .. 2026-10-16T17:01:44.377000+00:00 (264h 29m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b21\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 10723 records, 10 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 103 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2821 | 26.31 | 1 | 9 | 0 | 2026-10-05T16:36:13.539000+00:00 | 2026-10-16T17:01:44.377000+00:00 | 264h 25m |
| PuzzlePieceVisibleEvent | 2486 | 23.18 | 1 | 4 | 0 | 2026-10-06T16:51:18.192000+00:00 | 2026-10-16T16:20:25.909000+00:00 | 239h 29m |
| DialogueEvent | 2307 | 21.51 | 1 | 9 | 1441 | 2026-10-05T16:32:14.687000+00:00 | 2026-10-16T17:01:39.136000+00:00 | 264h 29m |
| PlayerPositionEvent | 1967 | 18.34 | 1 | 9 | 0 | 2026-10-05T16:31:56.691000+00:00 | 2026-10-16T17:01:35.913000+00:00 | 264h 29m |
| argumentationNodeEvent | 349 | 3.25 | 1 | 5 | 0 | 2026-10-05T16:55:43.226000+00:00 | 2026-10-16T16:38:41.151000+00:00 | 263h 42m |
| ObjectInterEvent | 332 | 3.1 | 1 | 9 | 0 | 2026-10-05T16:37:59.674000+00:00 | 2026-10-16T17:01:44.377000+00:00 | 264h 23m |
| TopographicMapEvent | 102 | 0.95 | 1 | 3 | 0 | 2026-10-06T16:51:40.693000+00:00 | 2026-10-14T16:58:51.119000+00:00 | 192h 7m |
| questEvent | 90 | 0.84 | 1 | 9 | 90 | 2026-10-05T16:32:14.663000+00:00 | 2026-10-16T16:57:59.683000+00:00 | 264h 25m |
| Soil Key Puzzle | 38 | 0.35 | 1 | 3 | 0 | 2026-10-07T16:55:18.567000+00:00 | 2026-10-14T16:58:22.675000+00:00 | 168h 3m |
| DEBUGMenu | 34 | 0.32 | 1 | 9 | 0 | 2026-10-05T16:31:56.683000+00:00 | 2026-10-16T16:51:20.296000+00:00 | 264h 19m |
| WaterChamberEvent | 34 | 0.32 | 1 | 1 | 0 | 2026-10-16T16:19:41.348000+00:00 | 2026-10-16T16:30:09.364000+00:00 | 10m 28s |
| argumentationAnswerEvent | 28 | 0.26 | 1 | 5 | 0 | 2026-10-05T16:55:56.275000+00:00 | 2026-10-16T16:38:42.961000+00:00 | 263h 42m |
| SolarStillDesignEvent | 23 | 0.21 | 1 | 1 | 0 | 2026-10-16T16:44:41.346000+00:00 | 2026-10-16T16:55:44.512000+00:00 | 11m 3s |
| TerasGardenBox | 18 | 0.17 | 1 | 1 | 0 | 2026-10-15T16:53:53.546000+00:00 | 2026-10-16T15:58:03.856000+00:00 | 23h 4m |
| gameStartEvent | 16 | 0.15 | 1 | 1 | 0 | 2026-10-05T16:31:45.388000+00:00 | 2026-10-16T16:51:20.379000+00:00 | 264h 19m |
| gameWindowFocusEvent | 16 | 0.15 | 1 | 1 | 0 | 2026-10-05T16:31:45.387000+00:00 | 2026-10-16T16:51:20.379000+00:00 | 264h 19m |
| soilMachine | 16 | 0.15 | 1 | 1 | 0 | 2026-10-14T20:09:37.716000+00:00 | 2026-10-15T16:28:33.676000+00:00 | 20h 18m |
| argumentationEvent | 14 | 0.13 | 1 | 5 | 0 | 2026-10-05T16:55:38.262000+00:00 | 2026-10-16T16:38:42.985000+00:00 | 263h 43m |
| DaniEvent | 12 | 0.11 | 1 | 2 | 0 | 2026-10-07T16:34:45.929000+00:00 | 2026-10-15T16:03:36.916000+00:00 | 191h 28m |
| argumentationToolEvent | 6 | 0.06 | 1 | 2 | 0 | 2026-10-05T16:55:34.077000+00:00 | 2026-10-08T16:57:58.996000+00:00 | 72h 2m |
| chatEvent | 6 | 0.06 | 1 | 3 | 0 | 2026-10-15T16:03:37.027000+00:00 | 2026-10-16T16:51:26.330000+00:00 | 24h 47m |
| EndOfUnit | 5 | 0.05 | 1 | 5 | 0 | 2026-10-05T17:00:30.376000+00:00 | 2026-10-16T17:01:44.365000+00:00 | 264h 1m |
| gameWindowUnfocusEvent | 3 | 0.03 | 1 | 2 | 0 | 2026-10-06T17:04:19.775000+00:00 | 2026-10-14T20:11:05.559000+00:00 | 195h 6m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 214994.423s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.478s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.948s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.052s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 8.782s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.281s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.266s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 12.499s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 11081.054s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 11081.054s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 351202.892s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 5.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.6x vs baseline. 
  - Observed: 28 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; B,1,II; B,2,II; B,3,I; C,2,II; C,D,3,II; C,D,A,2,II; D,2,II; D,C,3,2,II 
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
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [91-52, 91-54, 91-55, 91-61, 91-117] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 3 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
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
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[274] _id=6ac3d395de269131f9adf66d ts=2026-10-05T16:43:00.3850000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[320] _id=6ac3d460de269131f9ae0a55 ts=2026-10-05T16:46:23.3850000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[355] _id=6ac3d4e5de269131f9ae1813 ts=2026-10-05T16:48:36.7330000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[0] _id=6ac3d0f2de269131f9adbff1 ts=2026-10-05T16:31:45.3880000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[623] _id=6ac3d7fbde269131f9ae6593 ts=2026-10-05T17:01:46.7170000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[656] _id=6ac5266fde269131f9b55c5d ts=2026-10-06T16:48:46.6530000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[5] _id=6ac3d0f2de269131f9adbfec ts=2026-10-05T16:31:45.3870000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[622] _id=6ac3d7fbde269131f9ae6590 ts=2026-10-05T17:01:46.7160000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[655] _id=6ac5266fde269131f9b55c59 ts=2026-10-06T16:48:46.6520000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 3 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 3} 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[1736] _id=6ac67365de269131f9bc8055 ts=2026-10-06T17:04:19.775Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[6815] _id=6acfddf5de269131f9d92f62 ts=2026-10-14T17:04:22.058Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[7284] _id=6ad0f8abde269131f9dd0a33 ts=2026-10-14T20:11:05.559Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 19 of 102 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[735] _id=6ac5271dde269131f9b57215 ts=2026-10-06T16:51:40.6930000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[745] _id=6ac5272cde269131f9b573ec ts=2026-10-06T16:51:55.6780000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[1799] _id=6ac67421de269131f9bc8c77 ts=2026-10-07T16:32:32.5760000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 2820 | 0.0 | 1.478 | 337.564 | 25.516 | 429648.083 | 0.18 | 49 | 8 |
| PuzzlePieceVisibleEvent | 2485 | 0.0 | 0.052 | 346.941 | 2.197 | 433347.251 | 0.17 | 1214 | 7 |
| DialogueEvent | 2306 | 0.0 | 3.662 | 412.907 | 27.535 | 429451.509 | 0.15 | 669 | 8 |
| PlayerPositionEvent | 1955 | 9.75 | 10.0 | 267.086 | 10.051 | 85488.731 | 0.22 | 0 | 7 |
| argumentationNodeEvent | 348 | 0.005 | 0.402 | 2728.097 | 8.966 | 431264.967 | 0.02 | 58 | 4 |
| ObjectInterEvent | 331 | 0.0 | 12.948 | 2875.603 | 452.075 | 430474.018 | 0.02 | 4 | 11 |
| TopographicMapEvent | 101 | 0.016 | 5.281 | 6847.826 | 695.312 | 431191.84 | 0.01 | 2 | 6 |
| questEvent | 89 | 0.0 | 200.115 | 10696.011 | 83487.818 | 429617.467 | 0.01 | 18 | 15 |
| Soil Key Puzzle | 37 | 0.25 | 1.368 | 16350.922 | 17355.152 | 518183.287 | 0.0 | 0 | 2 |
| DEBUGMenu | 33 | 4.596 | 724.153 | 28835.261 | 85911.408 | 431454.364 | 0.0 | 0 | 18 |
| WaterChamberEvent | 33 | 0.748 | 6.266 | 19.031 | 75.829 | 116.887 | 3.15 | 0 | 0 |
| argumentationAnswerEvent | 27 | 0.185 | 12.499 | 35161.729 | 233281.579 | 431338.746 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 22 | 0.718 | 2.384 | 30.144 | 12.715 | 592.732 | 1.99 | 0 | 0 |
| TerasGardenBox | 17 | 0.516 | 8.782 | 4885.312 | 16717.76 | 82662.395 | 0.01 | 0 | 1 |
| gameStartEvent | 15 | 219.703 | 11081.054 | 63438.333 | 189887.587 | 431461.321 | 0.0 | 0 | 13 |
| gameWindowFocusEvent | 15 | 219.704 | 11081.054 | 63438.333 | 189887.587 | 431461.321 | 0.0 | 0 | 13 |
| soilMachine | 15 | 0.132 | 50.467 | 4875.731 | 21968.687 | 71857.984 | 0.01 | 0 | 1 |
| argumentationEvent | 13 | 0.027 | 58.906 | 73029.594 | 328027.237 | 431268.749 | 0.0 | 2 | 4 |
| DaniEvent | 11 | 0.229 | 4.313 | 62666.453 | 344647.702 | 617461.015 | 0.0 | 0 | 2 |
| argumentationToolEvent | 5 | 4.131 | 17.998 | 51868.984 | 207407.033 | 259239.141 | 0.0 | 0 | 1 |
| chatEvent | 5 | 2.572 | 933.006 | 17853.861 | 69604.936 | 86700.835 | 0.0 | 0 | 3 |
| EndOfUnit | 4 | 3211.085 | 214994.423 | 237618.497 | 478580.192 | 517274.058 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 2 | 11203.501 | 351202.892 | 351202.892 | 657202.344 | 691202.283 | 0.0 | 0 | 2 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 33 group(s), 44 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[831] _id=6ac52761de269131f9b57a99 ts=2026-10-06T16:52:41.6070000Z == 6ab9a8e69a8420a1e6b56b21.jsonl[791] _id=6ac52761de269131f9b57aa0 ts=2026-10-06T16:52:41.6070000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[848] _id=6ac52764de269131f9b57b03 ts=2026-10-06T16:52:51.2510000Z == 6ab9a8e69a8420a1e6b56b21.jsonl[844] _id=6ac52764de269131f9b57b07 ts=2026-10-06T16:52:51.2510000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[1148] _id=6ac527d4de269131f9b591eb ts=2026-10-06T16:54:42.8210000Z == 6ab9a8e69a8420a1e6b56b21.jsonl[1138] _id=6ac527d4de269131f9b591f1 ts=2026-10-06T16:54:42.8210000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[10265] _id=6ad25360de269131f9e60096 ts=2026-10-16T16:39:59.7510000Z == 6ab9a8e69a8420a1e6b56b21.jsonl[10266] _id=6ad25360de269131f9e60097 ts=2026-10-16T16:39:59.7510000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `899ms: 6ab9a8e69a8420a1e6b56b21.jsonl[7370] _id=6ad0f955de269131f9dd20e8 ts=2026-10-15T16:03:32.8890000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[7374] _id=6ad0f956de269131f9dd2112 ts=2026-10-15T16:03:33.7880000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `950ms: 6ab9a8e69a8420a1e6b56b21.jsonl[112] _id=6ac3d274de269131f9ade119 ts=2026-10-05T16:38:11.8220000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[102] _id=6ac3d275de269131f9ade129 ts=2026-10-05T16:38:12.7720000Z`; `849ms: 6ab9a8e69a8420a1e6b56b21.jsonl[120] _id=6ac3d277de269131f9ade163 ts=2026-10-05T16:38:14.9390000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[121] _id=6ac3d278de269131f9ade185 ts=2026-10-05T16:38:15.7880000Z`; `250ms: 6ab9a8e69a8420a1e6b56b21.jsonl[121] _id=6ac3d278de269131f9ade185 ts=2026-10-05T16:38:15.7880000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[115] _id=6ac3d278de269131f9ade18f ts=2026-10-05T16:38:16.0380000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 48 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: 6ab9a8e69a8420a1e6b56b21.jsonl[780] _id=6ac5275ede269131f9b579a9 ts=2026-10-06T16:51:18.4840000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[787] _id=6ac5275ede269131f9b579ab ts=2026-10-06T16:51:18.5160000Z`; `51ms: 6ab9a8e69a8420a1e6b56b21.jsonl[771] _id=6ac52761de269131f9b57a75 ts=2026-10-06T16:52:31.6000000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[772] _id=6ac52761de269131f9b57a78 ts=2026-10-06T16:52:31.6510000Z`; `33ms: 6ab9a8e69a8420a1e6b56b21.jsonl[827] _id=6ac52761de269131f9b57a93 ts=2026-10-06T16:52:41.5740000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[831] _id=6ac52761de269131f9b57a99 ts=2026-10-06T16:52:41.6070000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `516ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8779] _id=6ad1064cde269131f9de25c2 ts=2026-10-15T16:58:52.2110000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[8780] _id=6ad1064dde269131f9de25da ts=2026-10-15T16:58:52.7270000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `483ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8457] _id=6ad10377de269131f9ddd808 ts=2026-10-15T16:46:47.2440000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[8452] _id=6ad10378de269131f9ddd80c ts=2026-10-15T16:46:47.7270000Z`; `582ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8452] _id=6ad10378de269131f9ddd80c ts=2026-10-15T16:46:47.7270000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[8455] _id=6ad10378de269131f9ddd812 ts=2026-10-15T16:46:48.3090000Z`; `602ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8455] _id=6ad10378de269131f9ddd812 ts=2026-10-15T16:46:48.3090000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[8456] _id=6ad10379de269131f9ddd81a ts=2026-10-15T16:46:48.9110000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6ab9a8e69a8420a1e6b56b21.jsonl[4852] _id=6ace60adde269131f9cfbdbd ts=2026-10-13T16:47:40.3570000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[4855] _id=6ace60adde269131f9cfbdc0 ts=2026-10-13T16:47:40.3840000Z`; `29ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8594] _id=6ad1042ede269131f9dde924 ts=2026-10-15T16:49:49.9670000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[8597] _id=6ad1042ede269131f9dde927 ts=2026-10-15T16:49:49.9960000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 34 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6ab9a8e69a8420a1e6b56b21.jsonl[469] _id=6ac3d690de269131f9ae40d3 ts=2026-10-05T16:55:43.6190000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[465] _id=6ac3d690de269131f9ae40d9 ts=2026-10-05T16:55:43.6580000Z`; `38ms: 6ab9a8e69a8420a1e6b56b21.jsonl[478] _id=6ac3d695de269131f9ae4163 ts=2026-10-05T16:55:48.4520000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[477] _id=6ac3d695de269131f9ae4169 ts=2026-10-05T16:55:48.4900000Z`; `24ms: 6ab9a8e69a8420a1e6b56b21.jsonl[483] _id=6ac3d698de269131f9ae41cb ts=2026-10-05T16:55:52.2530000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[484] _id=6ac3d698de269131f9ae41cd ts=2026-10-05T16:55:52.2770000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10424] _id=6ad2550ede269131f9e616f0 ts=2026-10-16T16:47:10.2990000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[10420] _id=6ad2550ede269131f9e616f3 ts=2026-10-16T16:47:10.3030000Z`; `4ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10498] _id=6ad25610de269131f9e62cf6 ts=2026-10-16T16:51:27.4890000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[10499] _id=6ad25610de269131f9e62cf7 ts=2026-10-16T16:51:27.4930000Z`; `4ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10624] _id=6ad25757de269131f9e644ed ts=2026-10-16T16:56:55.2800000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[10625] _id=6ad25757de269131f9e644f2 ts=2026-10-16T16:56:55.2840000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `535ms: 6ab9a8e69a8420a1e6b56b21.jsonl[7840] _id=6ad0fe7bde269131f9dd76fb ts=2026-10-15T16:25:31.0400000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[7845] _id=6ad0fe7cde269131f9dd770f ts=2026-10-15T16:25:31.5750000Z`; `148ms: 6ab9a8e69a8420a1e6b56b21.jsonl[7879] _id=6ad0fedade269131f9dd800b ts=2026-10-15T16:27:06.3750000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[7882] _id=6ad0fedbde269131f9dd8024 ts=2026-10-15T16:27:06.5230000Z`; `169ms: 6ab9a8e69a8420a1e6b56b21.jsonl[7882] _id=6ad0fedbde269131f9dd8024 ts=2026-10-15T16:27:06.5230000Z ~ 6ab9a8e69a8420a1e6b56b21.jsonl[7885] _id=6ad0fedbde269131f9dd8027 ts=2026-10-15T16:27:06.6920000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a8e69a8420a1e6b56b21.jsonl[3032] _id=6ac7c4bfde269131f9c4271d ts=2026-10-08T16:28:47.0270000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3964] _id=6ace5a1ede269131f9cf5a31 ts=2026-10-13T16:19:41.3910000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b21.jsonl[1742] _id=6ac6736cde269131f9bc80ac ts=2026-10-07T16:29:31.5410000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3025] _id=6ac7c4b9de269131f9c426a2 ts=2026-10-08T16:28:40.0960000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b21.jsonl[624] _id=6ac3d802de269131f9ae6683 ts=2026-10-05T17:01:53.6210000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[659] _id=6ac52676de269131f9b55d83 ts=2026-10-06T16:48:53.5980000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 171h 31m 
  - Evidence: 171h 31m: 6ab9a8e69a8420a1e6b56b21.jsonl[1840] _id=6ac674a8de269131f9bc98b4 ts=2026-10-07T16:34:47.6420000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[7134] _id=6acfe09dde269131f9d955b7 ts=2026-10-14T20:05:48.6570000Z; 19h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[7144] _id=6acfe0acde269131f9d95682 ts=2026-10-14T20:06:02.4820000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[7362] _id=6ad0f945de269131f9dd1f0d ts=2026-10-15T16:03:16.8710000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 17m 
  - Evidence: 119h 17m: 6ab9a8e69a8420a1e6b56b21.jsonl[3959] _id=6ac7cca1de269131f9c4da1e ts=2026-10-08T17:02:25.3490000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3974] _id=6ace5a2dde269131f9cf5ac6 ts=2026-10-13T16:19:56.8580000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b21.jsonl[653] _id=6ac3d889de269131f9ae719d ts=2026-10-05T17:04:09.0710000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[667] _id=6ac5268dde269131f9b560c3 ts=2026-10-06T16:49:16.9460000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b21.jsonl[2984] _id=6ac67b5fde269131f9bd8ab5 ts=2026-10-07T17:03:26.9490000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3214] _id=6ac7c585de269131f9c436da ts=2026-10-08T16:32:05.2400000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 669 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10197] _id=6ad25300de269131f9e5fc1f ts=2026-10-16T16:38:24.5310000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10198] _id=6ad25300de269131f9e5fc20 ts=2026-10-16T16:38:24.5310000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10250] _id=6ad2534ade269131f9e5ff7b ts=2026-10-16T16:39:37.9710000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10251] _id=6ad2534ade269131f9e5ff7c ts=2026-10-16T16:39:37.9710000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10395] _id=6ad254efde269131f9e614ce ts=2026-10-16T16:46:39.3720000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10397] _id=6ad254efde269131f9e614cf ts=2026-10-16T16:46:39.3720000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 41m 
  - Evidence: 143h 41m: 6ab9a8e69a8420a1e6b56b21.jsonl[3958] _id=6ac7cca1de269131f9c4da1b ts=2026-10-08T17:02:25.3240000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[6093] _id=6acfb13cde269131f9d5bd16 ts=2026-10-14T16:43:39.3820000Z; 72h 1m: 6ab9a8e69a8420a1e6b56b21.jsonl[620] _id=6ac3d7afde269131f9ae5db9 ts=2026-10-05T17:00:30.3760000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3958] _id=6ac7cca1de269131f9c4da1b ts=2026-10-08T17:02:25.3240000Z; 47h 24m: 6ab9a8e69a8420a1e6b56b21.jsonl[6093] _id=6acfb13cde269131f9d5bd16 ts=2026-10-14T16:43:39.3820000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[9183] _id=6ad24bedde269131f9e59c06 ts=2026-10-16T16:08:13.2800000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b21.jsonl[3950] _id=6ac7cc89de269131f9c4d8f6 ts=2026-10-08T17:02:01.6150000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4008] _id=6ace5adade269131f9cf606d ts=2026-10-13T16:22:49.6980000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b21.jsonl[644] _id=6ac3d874de269131f9ae6fbd ts=2026-10-05T17:03:47.7770000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[661] _id=6ac5267fde269131f9b55f09 ts=2026-10-06T16:49:03.4530000Z; 23h 25m: 6ab9a8e69a8420a1e6b56b21.jsonl[1711] _id=6ac529ecde269131f9b60241 ts=2026-10-06T17:03:39.8860000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1743] _id=6ac67371de269131f9bc80e3 ts=2026-10-07T16:29:36.7740000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 49 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[7318] _id=6ad0f8f7de269131f9dd14f7 ts=2026-10-15T16:01:59.1150000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[7319] _id=6ad0f8f7de269131f9dd14f8 ts=2026-10-15T16:01:59.1150000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8279] _id=6ad1024fde269131f9ddbead ts=2026-10-15T16:41:51.2290000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8280] _id=6ad1024fde269131f9ddbeae ts=2026-10-15T16:41:51.2290000Z; 1ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10028] _id=6ad2514ade269131f9e5e3fa ts=2026-10-16T16:31:05.3910000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10029] _id=6ad2514ade269131f9e5e3fb ts=2026-10-16T16:31:05.3920000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 34m 
  - Evidence: 119h 34m: 6ab9a8e69a8420a1e6b56b21.jsonl[3778] _id=6ac7cab1de269131f9c4b778 ts=2026-10-08T16:54:09.2340000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4094] _id=6ace5c3bde269131f9cf708e ts=2026-10-13T16:28:43.2520000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[1600] _id=6ac5287dde269131f9b5b9c3 ts=2026-10-06T16:57:32.6040000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[2350] _id=6ac67977de269131f9bd569e ts=2026-10-07T16:55:18.5720000Z; 23h 50m: 6ab9a8e69a8420a1e6b56b21.jsonl[595] _id=6ac3d783de269131f9ae5963 ts=2026-10-05T16:59:46.9250000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[697] _id=6ac526d0de269131f9b567a3 ts=2026-10-06T16:50:24.5050000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8236] _id=6ad10224de269131f9ddbaa9 ts=2026-10-15T16:41:07.6760000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8237] _id=6ad10224de269131f9ddbaaa ts=2026-10-15T16:41:07.6760000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8314] _id=6ad10285de269131f9ddc3c8 ts=2026-10-15T16:42:44.3780000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8315] _id=6ad10285de269131f9ddc3c9 ts=2026-10-15T16:42:44.3780000Z; 4ms: 6ab9a8e69a8420a1e6b56b21.jsonl[237] _id=6ac3d313de269131f9adede1 ts=2026-10-05T16:40:51.3560000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[236] _id=6ac3d314de269131f9adede5 ts=2026-10-05T16:40:51.3600000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 23h 44m 
  - Evidence: 23h 44m: 6ab9a8e69a8420a1e6b56b21.jsonl[650] _id=6ac3d885de269131f9ae7125 ts=2026-10-05T17:04:04.8750000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[657] _id=6ac52679de269131f9b55e05 ts=2026-10-06T16:48:53.6060000Z; 23h 25m: 6ab9a8e69a8420a1e6b56b21.jsonl[1734] _id=6ac52a11de269131f9b609ad ts=2026-10-06T17:04:16.8040000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1740] _id=6ac6736ede269131f9bc80ba ts=2026-10-07T16:29:31.5490000Z; 23h 25m: 6ab9a8e69a8420a1e6b56b21.jsonl[3024] _id=6ac67b6bde269131f9bd8c78 ts=2026-10-07T17:03:38.8920000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3040] _id=6ac7c4c2de269131f9c42779 ts=2026-10-08T16:28:47.0440000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 22m 
  - Evidence: 120h 22m: 6ab9a8e69a8420a1e6b56b21.jsonl[3192] _id=6ac7c546de269131f9c43135 ts=2026-10-08T16:31:01.4770000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[5006] _id=6ace620ade269131f9cfd692 ts=2026-10-13T16:53:28.7280000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b21.jsonl[1594] _id=6ac5285dde269131f9b5b256 ts=2026-10-06T16:56:59.5050000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[2400] _id=6ac679cfde269131f9bd5d5b ts=2026-10-07T16:56:45.1800000Z; 23h 34m: 6ab9a8e69a8420a1e6b56b21.jsonl[8086] _id=6ad10085de269131f9dd9f30 ts=2026-10-15T16:34:11.6910000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[9189] _id=6ad24c0fde269131f9e59d9f ts=2026-10-16T16:08:45.8370000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1214 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[1017] _id=6ac527a3de269131f9b586bb ts=2026-10-06T16:53:54.3050000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1018] _id=6ac527a4de269131f9b586c2 ts=2026-10-06T16:53:54.3050000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[1075] _id=6ac527d8de269131f9b59305 ts=2026-10-06T16:54:46.5970000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1156] _id=6ac527d8de269131f9b59313 ts=2026-10-06T16:54:46.5970000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[1093] _id=6ac527c1de269131f9b58d5d ts=2026-10-06T16:54:24.4390000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1100] _id=6ac527c1de269131f9b58d63 ts=2026-10-06T16:54:24.4390000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 6ab9a8e69a8420a1e6b56b21.jsonl[2376] _id=6ac679a6de269131f9bd5a63 ts=2026-10-07T16:56:05.6980000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4983] _id=6ace61cdde269131f9cfd1ee ts=2026-10-13T16:52:28.9850000Z; 24h 4m: 6ab9a8e69a8420a1e6b56b21.jsonl[4995] _id=6ace61e4de269131f9cfd378 ts=2026-10-13T16:52:52.2480000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[6183] _id=6acfb48bde269131f9d616b1 ts=2026-10-14T16:57:46.4260000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22h 57m 
  - Evidence: 22h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[8773] _id=6ad10650de269131f9de2633 ts=2026-10-15T16:58:55.7950000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8920] _id=6ad24936de269131f9e56c0c ts=2026-10-16T15:56:38.1900000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8e69a8420a1e6b56b21.jsonl[3362] _id=6ac7c768de269131f9c477a4 ts=2026-10-08T16:40:08.6350000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4045] _id=6ace5bc1de269131f9cf6a24 ts=2026-10-13T16:26:40.4750000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b21.jsonl[2332] _id=6ac67951de269131f9bd533a ts=2026-10-07T16:54:40.9920000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3359] _id=6ac7c758de269131f9c475a2 ts=2026-10-08T16:39:52.0040000Z; 23h 43m: 6ab9a8e69a8420a1e6b56b21.jsonl[4921] _id=6ace6143de269131f9cfc8d6 ts=2026-10-13T16:50:10.7850000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[5879] _id=6acfaecede269131f9d5895d ts=2026-10-14T16:33:17.3330000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.016s..0.024s shown 
  - Evidence: 16ms: 6ab9a8e69a8420a1e6b56b21.jsonl[1805] _id=6ac6744bde269131f9bc8ffc ts=2026-10-07T16:33:14.1450000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1809] _id=6ac6744bde269131f9bc9000 ts=2026-10-07T16:33:14.1610000Z; 24ms: 6ab9a8e69a8420a1e6b56b21.jsonl[1811] _id=6ac6744bde269131f9bc8ff6 ts=2026-10-07T16:33:14.1210000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1805] _id=6ac6744bde269131f9bc8ffc ts=2026-10-07T16:33:14.1450000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6ab9a8e69a8420a1e6b56b21.jsonl[3870] _id=6ac7cb98de269131f9c4c669 ts=2026-10-08T16:58:00.0360000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4804] _id=6ace6083de269131f9cfbac1 ts=2026-10-13T16:46:58.7820000Z; 72h 0m: 6ab9a8e69a8420a1e6b56b21.jsonl[520] _id=6ac3d6f0de269131f9ae4a79 ts=2026-10-05T16:57:19.8580000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3870] _id=6ac7cb98de269131f9c4c669 ts=2026-10-08T16:58:00.0360000Z; 47h 58m: 6ab9a8e69a8420a1e6b56b21.jsonl[4858] _id=6ace60adde269131f9cfbdb5 ts=2026-10-13T16:47:40.3480000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8295] _id=6ad10354de269131f9ddd5b9 ts=2026-10-15T16:46:11.8630000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8e69a8420a1e6b56b21.jsonl[3872] _id=6ac7cb98de269131f9c4c66d ts=2026-10-08T16:58:00.0560000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4738] _id=6ace603dde269131f9cfb53f ts=2026-10-13T16:45:48.8050000Z; 71h 59m: 6ab9a8e69a8420a1e6b56b21.jsonl[521] _id=6ac3d6f0de269131f9ae4a7b ts=2026-10-05T16:57:19.8710000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3840] _id=6ac7cb6fde269131f9c4c3ca ts=2026-10-08T16:57:19.4330000Z; 47h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[4855] _id=6ace60adde269131f9cfbdc0 ts=2026-10-13T16:47:40.3840000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8376] _id=6ad10309de269131f9ddd0dc ts=2026-10-15T16:44:56.7310000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.029s shown 
  - Evidence: 27ms: 6ab9a8e69a8420a1e6b56b21.jsonl[4852] _id=6ace60adde269131f9cfbdbd ts=2026-10-13T16:47:40.3570000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4855] _id=6ace60adde269131f9cfbdc0 ts=2026-10-13T16:47:40.3840000Z; 29ms: 6ab9a8e69a8420a1e6b56b21.jsonl[8594] _id=6ad1042ede269131f9dde924 ts=2026-10-15T16:49:49.9670000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8597] _id=6ad1042ede269131f9dde927 ts=2026-10-15T16:49:49.9960000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8e69a8420a1e6b56b21.jsonl[3858] _id=6ac7cb91de269131f9c4c5f3 ts=2026-10-08T16:57:53.0500000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4720] _id=6ace6032de269131f9cfb463 ts=2026-10-13T16:45:38.0170000Z; 71h 59m: 6ab9a8e69a8420a1e6b56b21.jsonl[512] _id=6ac3d6e7de269131f9ae4970 ts=2026-10-05T16:57:10.3750000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3828] _id=6ac7cb65de269131f9c4c31a ts=2026-10-08T16:57:09.2350000Z; 47h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[4808] _id=6ace60aade269131f9cfbd87 ts=2026-10-13T16:47:37.6820000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[8367] _id=6ad10305de269131f9ddd09a ts=2026-10-15T16:44:52.7780000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 58 interval(s) ≤ 0.005s..0.021s shown 
  - Evidence: 5ms: 6ab9a8e69a8420a1e6b56b21.jsonl[4800] _id=6ace6079de269131f9cfb9f5 ts=2026-10-13T16:46:48.8820000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4798] _id=6ace6079de269131f9cfb9f8 ts=2026-10-13T16:46:48.8870000Z; 20ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10188] _id=6ad25311de269131f9e5fcef ts=2026-10-16T16:38:41.1310000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10215] _id=6ad25311de269131f9e5fcf1 ts=2026-10-16T16:38:41.1510000Z; 21ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10187] _id=6ad252f4de269131f9e5fb7b ts=2026-10-16T16:38:12.3100000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10185] _id=6ad252f4de269131f9e5fb7d ts=2026-10-16T16:38:12.3310000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 72h 0m 
  - Evidence: 72h 0m: 6ab9a8e69a8420a1e6b56b21.jsonl[518] _id=6ac3d6f0de269131f9ae4a73 ts=2026-10-05T16:57:19.8550000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3871] _id=6ac7cb97de269131f9c4c650 ts=2026-10-08T16:57:58.9960000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 24h 5m 
  - Evidence: 24h 5m: 6ab9a8e69a8420a1e6b56b21.jsonl[7377] _id=6ad0f95bde269131f9dd21a9 ts=2026-10-15T16:03:39.5990000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[9188] _id=6ad24c09de269131f9e59d2c ts=2026-10-16T16:08:40.4340000Z; 20m 21s: 6ab9a8e69a8420a1e6b56b21.jsonl[10031] _id=6ad25149de269131f9e5e3e9 ts=2026-10-16T16:31:04.9920000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10500] _id=6ad2560ede269131f9e62cbe ts=2026-10-16T16:51:26.3300000Z; 15m 33s: 6ab9a8e69a8420a1e6b56b21.jsonl[9258] _id=6ad24da4de269131f9e5a8e7 ts=2026-10-16T16:15:31.9860000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10031] _id=6ad25149de269131f9e5e3e9 ts=2026-10-16T16:31:04.9920000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6ab9a8e69a8420a1e6b56b21.jsonl[3034] _id=6ac7c4b9de269131f9c426a5 ts=2026-10-08T16:28:40.1580000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3966] _id=6ace5a1ede269131f9cf5a36 ts=2026-10-13T16:19:41.4790000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b21.jsonl[1739] _id=6ac67365de269131f9bc805b ts=2026-10-07T16:29:24.1710000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3034] _id=6ac7c4b9de269131f9c426a5 ts=2026-10-08T16:28:40.1580000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[3966] _id=6ace5a1ede269131f9cf5a36 ts=2026-10-13T16:19:41.4790000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[5366] _id=6acfab0ede269131f9d54a4a ts=2026-10-14T16:17:17.4970000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 51m 
  - Evidence: 119h 51m: 6ab9a8e69a8420a1e6b56b21.jsonl[3033] _id=6ac7c4b9de269131f9c426a4 ts=2026-10-08T16:28:40.1580000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3965] _id=6ace5a1ede269131f9cf5a35 ts=2026-10-13T16:19:41.4790000Z; 23h 59m: 6ab9a8e69a8420a1e6b56b21.jsonl[1738] _id=6ac67365de269131f9bc805a ts=2026-10-07T16:29:24.1710000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[3033] _id=6ac7c4b9de269131f9c426a4 ts=2026-10-08T16:28:40.1580000Z; 23h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[3965] _id=6ace5a1ede269131f9cf5a35 ts=2026-10-13T16:19:41.4790000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[5365] _id=6acfab0ede269131f9d54a49 ts=2026-10-14T16:17:17.4970000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 192h 0m 
  - Evidence: 192h 0m: 6ab9a8e69a8420a1e6b56b21.jsonl[1736] _id=6ac67365de269131f9bc8055 ts=2026-10-06T17:04:19.775Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[6815] _id=6acfddf5de269131f9d92f62 ts=2026-10-14T17:04:22.058Z; 3h 6m: 6ab9a8e69a8420a1e6b56b21.jsonl[6815] _id=6acfddf5de269131f9d92f62 ts=2026-10-14T17:04:22.058Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[7284] _id=6ad0f8abde269131f9dd0a33 ts=2026-10-14T20:11:05.559Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8e69a8420a1e6b56b21.jsonl[3960] _id=6ac7cc9ade269131f9c4d9d4 ts=2026-10-08T17:02:18.1700000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[4000] _id=6ace5accde269131f9cf5fe4 ts=2026-10-13T16:22:35.6370000Z; 23h 45m: 6ab9a8e69a8420a1e6b56b21.jsonl[637] _id=6ac3d856de269131f9ae6d83 ts=2026-10-05T17:03:18.2930000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[658] _id=6ac52679de269131f9b55e0c ts=2026-10-06T16:48:56.5560000Z; 23h 27m: 6ab9a8e69a8420a1e6b56b21.jsonl[1676] _id=6ac52974de269131f9b5eceb ts=2026-10-06T17:01:39.6230000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[1741] _id=6ac6736ede269131f9bc80bb ts=2026-10-07T16:29:32.8060000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[10265] _id=6ad25360de269131f9e60096 ts=2026-10-16T16:39:59.7510000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[10266] _id=6ad25360de269131f9e60097 ts=2026-10-16T16:39:59.7510000Z; 0ms: 6ab9a8e69a8420a1e6b56b21.jsonl[9784] _id=6ad24f18de269131f9e5c02e ts=2026-10-16T16:21:43.6340000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[9785] _id=6ad24f18de269131f9e5c02f ts=2026-10-16T16:21:43.6340000Z; 1ms: 6ab9a8e69a8420a1e6b56b21.jsonl[444] _id=6ac3d637de269131f9ae35ab ts=2026-10-05T16:54:14.5120000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[441] _id=6ac3d637de269131f9ae35af ts=2026-10-05T16:54:14.5130000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 19h 57m 
  - Evidence: 19h 57m: 6ab9a8e69a8420a1e6b56b21.jsonl[7239] _id=6acfe182de269131f9d96189 ts=2026-10-14T20:09:37.7160000Z -> 6ab9a8e69a8420a1e6b56b21.jsonl[7480] _id=6ad0fa33de269131f9dd3a70 ts=2026-10-15T16:07:15.7000000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[433] _id=6ac3d623de269131f9ae32eb ts=2026-10-05T16:53:54.7710000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[529] _id=6ac3d706de269131f9ae4c99 ts=2026-10-05T16:57:41.6540000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[2246] _id=6ac67829de269131f9bd3589 ts=2026-10-07T16:49:44.6580000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 24 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[853] _id=6ac52765de269131f9b57b29 ts=2026-10-06T16:52:51.6540000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[838] _id=6ac5276ade269131f9b57bd5 ts=2026-10-06T16:52:56.4420000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[889] _id=6ac52771de269131f9b57cb2 ts=2026-10-06T16:53:03.8340000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 40 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[775] _id=6ac5275dde269131f9b5798b ts=2026-10-06T16:51:18.3560000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[787] _id=6ac5275ede269131f9b579ab ts=2026-10-06T16:51:18.5160000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[781] _id=6ac5275ede269131f9b579b7 ts=2026-10-06T16:51:18.5240000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[4855] _id=6ace60adde269131f9cfbdc0 ts=2026-10-13T16:47:40.3840000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[8597] _id=6ad1042ede269131f9dde927 ts=2026-10-15T16:49:49.9960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[465] _id=6ac3d690de269131f9ae40d9 ts=2026-10-05T16:55:43.6580000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[477] _id=6ac3d695de269131f9ae4169 ts=2026-10-05T16:55:48.4900000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[484] _id=6ac3d698de269131f9ae41cd ts=2026-10-05T16:55:52.2770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[9188] _id=6ad24c09de269131f9e59d2c ts=2026-10-16T16:08:40.4340000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[9258] _id=6ad24da4de269131f9e5a8e7 ts=2026-10-16T16:15:31.9860000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[10031] _id=6ad25149de269131f9e5e3e9 ts=2026-10-16T16:31:04.9920000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[257] _id=6ac3d35ede269131f9adf325 ts=2026-10-05T16:42:06.1260000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[7294] _id=6ad0f8bfde269131f9dd0c5d ts=2026-10-15T16:01:02.8850000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[7411] _id=6ad0f99cde269131f9dd289b ts=2026-10-15T16:04:44.7510000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 149 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[832] _id=6ac5276bde269131f9b57be9 ts=2026-10-06T16:52:57.7140000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[887] _id=6ac52773de269131f9b57ce1 ts=2026-10-06T16:53:06.3050000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[911] _id=6ac5277ade269131f9b57e75 ts=2026-10-06T16:53:13.2220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 136 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[772] _id=6ac52761de269131f9b57a78 ts=2026-10-06T16:52:31.6510000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[855] _id=6ac52765de269131f9b57b2f ts=2026-10-06T16:52:52.9240000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[840] _id=6ac5276ade269131f9b57bdd ts=2026-10-06T16:52:57.0000000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[516] _id=6ac3d6ebde269131f9ae49fb ts=2026-10-05T16:57:14.8070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 438 start, 428 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 15 unmatched 'BecameCameraCentered' (totals: 586 open, 595 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 29 unmatched 'BecameVisible' (totals: 647 open, 658 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 4 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 52 start, 38 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 163 of 10722 adjacent _id pairs reverse in client time; worst 84.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b21.jsonl[774] _id=6ac5275bde269131f9b57937 ts=2026-10-06T16:52:42.9860000Z`; `6ab9a8e69a8420a1e6b56b21.jsonl[777] _id=6ac5275cde269131f9b5795d ts=2026-10-06T16:51:18.1920000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.68s, min -84305.52s, max -0.16s over 10723 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b21\coverage.yaml

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

### `InputEvent` — 2821 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (749); Unit 4 Dev - Dungeon (569); Unit 3 Dev (556); Unit 3 Dungeon Dev (237); Unit 4 Dev (207); Unit 1 Dev (160); Unit 5 Dev - Dungeon (148); Unit 5 Dev (109); Unit 4 Dev - Anderson Base (86)
- **Intervals:** median 1.48s (p5 0.13s / p95 25.52s, n=2820)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2821/2821 records)
    "pressed"  x2821
data.actionType  (string, 2821/2821 records)
    "Move"  x1936
    "Interact"  x441
    "Jump"  x198
    "Sprint"  x90
    "Hoverboard"  x66
    "Ascend"  x29
    "Descend"  x28
    "Map"  x23
    "Pause"  x7
    "ToggleDebug"  x3
data.key  (string, 2821/2821 records, 16 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2821/2821 records)
    "Player"  x2158
    "Drone"  x663
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2486 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1342); Unit 4 Dev (504); Unit 5 Dev - Dungeon (446); Unit 3 Dungeon Dev (194)
- **Intervals:** median 0.05s (p5 0.00s / p95 2.20s, n=2485)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2486/2486 records)
    "BecameInvisible"  x658
    "BecameVisible"  x647
    "BecameCameraUncentered"  x595
    "BecameCameraCentered"  x586
data.pieceId  (string, 2486/2486 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2486/2486 records)
    1808 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2307 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (579); Unit 4 Dev (354); Unit 5 Dev (321); Unit 3 Dev (299); Unit 4 Dev - Dungeon (190); Unit 3 Dungeon Dev (189); Unit 1 Dev (183); Unit 4 Dev - Anderson Base (105); Unit 5 Dev - Dungeon (87)
- **eventKey:** present on 1441 of 2307 records
- **Intervals:** median 3.66s (p5 0.00s / p95 27.54s, n=2306)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1441; [conversationId, dialogueEventType] x866
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2307/2307 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2307/2307 records)
    "DialogueNodeEvent"  x1441
    "DialogueStartEvent"  x438
    "DialogueFinishEvent"  x428
data.nodeId  (number, 1441/2307 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1967 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (497); Unit 4 Dev (290); Unit 3 Dev (267); Unit 4 Dev - Dungeon (252); Unit 5 Dev (173); Unit 1 Dev (171); Unit 3 Dungeon Dev (150); Unit 5 Dev - Dungeon (100); Unit 4 Dev - Anderson Base (67)
- **Intervals:** median 10.00s (p5 9.97s / p95 10.05s, n=1955)
- **Fields under `data`:**

```text
data.position  (object, 1967/1967 records)
data.position.x  (number, 1967/1967 records)
    numeric range -684.957 .. 1554.08 (770 unique)
data.position.y  (number, 1967/1967 records)
    numeric range -115.43 .. 222.252 (552 unique)
data.position.z  (number, 1967/1967 records)
    numeric range -1156.6 .. 1973.32 (768 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 349 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (151); Unit 3 Dev (101); Unit 5 Dev (38); Unit 2 Prod (Refactor) (33); Unit 1 Dev (26)
- **Intervals:** median 0.40s (p5 0.03s / p95 8.97s, n=348)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 349/349 records)
    "argumentationNodeHoverEnd"  x155
    "argumentationNodeHoverStart"  x152
    "argumentationNodeAdd"  x30
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 349/349 records)
    "Unit 4 - Flooding"  x151
    "Unit 3 - Pollution Upstream"  x101
    "Unit 5"  x38
    "Unit 2 – Watershed"  x33
    "Unit 1 - Argumentation Tutorial"  x13
    "Unit 1 - Freshwater"  x13
data.nodeName  (string, 349/349 records)
    "II"  x61
    "I"  x39
    "2"  x37
    "3"  x37
    "A"  x35
    "C"  x34
    "B"  x32
    "1"  x31
    "D"  x18
    "4"  x16
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 332 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (119); Unit 3 Dungeon Dev (48); Unit 1 Dev (45); Unit 2 Prod (Refactor) (40); Unit 4 Dev (36); Unit 3 Dev (12); Unit 5 Dev - Dungeon (12); Unit 5 Dev (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 12.95s (p5 0.18s / p95 452.07s, n=331)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 332/332 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 332/332 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 102 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (57); Unit 3 Dev (38); Unit 4 Dev (7)
- **Intervals:** median 5.28s (p5 0.90s / p95 695.31s, n=101)
- **`data` key-set variants:** [actionType, featureUsed] x62; [actionType, featureUsed, location] x21; [actionType, featureUsed, legendName] x19
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 102/102 records)
    "MapCloseEvent"  x31
    "MapOpenEvent"  x31
    "Selected"  x16
    "WaypointMoveEvent"  x13
    "WaypointSetEvent"  x6
    "Unselected"  x3
    "WaypointResetEvent"  x2
data.featureUsed  (string, 102/102 records)
    "Map"  x62
    "Waypoint"  x21
    "Legend"  x19
data.legendName  (string, 19/102 records)
    "330 ft"  x7
    "300 ft"  x3
    "270 ft"  x2
    "90 ft"  x2
    "120 ft"  x1
    "210 ft"  x1
    "240 ft"  x1
    "30 ft"  x1
    "360 ft"  x1
data.location  (object, 21/102 records)
data.location.x  (number, 21/102 records)
    numeric range -343.312 .. 110.796 (17 unique)
data.location.y  (number, 21/102 records)
    numeric range -368.777 .. 151.408 (19 unique)
data.location.z  (number, 21/102 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 90 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (20); Unit 2 Prod (Refactor) (15); Unit 5 Dev (12); Unit 4 Dev (11); Unit 1 Dev (10); Unit 3 Dev (9); Unit 5 Dev - Dungeon (8); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 90 of 90 records
- **Intervals:** median 200.12s (p5 0.00s / p95 83487.82s, n=89)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x38
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 90/90 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x38
data.questID  (string, 90/90 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 90/90 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 38/90 records)
    "Succeeded"  x38
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 38 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 4 Dev (10); Unit 3 Dev (8)
- **Intervals:** median 1.37s (p5 0.26s / p95 17355.15s, n=37)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x32; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/38 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/38 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 32/38 records)
    "RightDrag"  x19
    "LeftDrag"  x13
data.currentSoilType  (string, 32/38 records)
    "CLAYSAND"  x8
    "CLAY"  x7
    "SAND"  x7
    "CLAYROCK"  x4
    "SANDGRAVEL"  x4
    "GRAVEL"  x2
data.isCorrectSelection  (string, 32/38 records)
    "false"  x23
    "true"  x9
data.waterLevelStatus  (string, 32/38 records)
    "TooHigh"  x17
    "Proper"  x13
    "TooLow"  x2
data.waterRetentionChange  (string, 32/38 records)
    "Increase"  x12
    "Decrease"  x11
    "NoChange"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 34 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (13); Unit 4 Dev - Dungeon (5); Unit 2 Prod (Refactor) (4); Unit 4 Dev (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 724.15s (p5 5.27s / p95 85911.41s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "DebugMenuStateChanged"  x34
data.isOpened  (bool, 34/34 records)
    false  x34
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 34 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (34)
- **Intervals:** median 6.27s (p5 1.08s / p95 75.83s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "On"  x23
    "Off"  x11
data.floor  (string, 34/34 records)
    "4"  x23
    "3"  x6
    "2"  x3
    "1"  x2
data.machineNumber  (string, 34/34 records)
    "One"  x33
    "Two"  x1
data.machineType  (string, 34/34 records)
    "Evaporator"  x18
    "Condenser"  x13
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 34/34 records)
    "3"  x22
    "2"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 28 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (18); Unit 3 Dev (5); Unit 1 Dev (2); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 12.50s (p5 0.50s / p95 233281.58s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "submitAnswerEvent"  x28
data.answerSubmitted  (string, 28/28 records)
    13 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 28/28 records)
    "Unit 4 - Flooding"  x18
    "Unit 3 - Pollution Upstream"  x5
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `SolarStillDesignEvent` — 23 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (23)
- **Intervals:** median 2.38s (p5 0.98s / p95 12.71s, n=22)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x21; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "optionSelected"  x21
    "DesignSubmitted"  x2
data.designSelections  (object, 2/23 records)
data.designSelections.glassRoofTemperature  (string, 2/23 records)
    "Cold"  x1
    "Hot"  x1
data.designSelections.roofCovering  (string, 2/23 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/23 records)
    "Flat"  x1
    "Tilted In"  x1
data.featureUsed  (string, 23/23 records)
    "GlassRoofTemperature"  x9
    "ExtraCovering"  x7
    "RoofStyle"  x5
    "Submit"  x2
data.selectedOption  (string, 21/23 records)
    "Hot"  x5
    "Cold"  x4
    "Uncovered"  x4
    "Covered"  x3
    "Flat"  x2
    "Tilted In"  x2
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 18 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (18)
- **Intervals:** median 8.78s (p5 1.06s / p95 16717.76s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records, 10 empty-string)
    ""  x10
    "cameraPlaced"  x8
data.boxId  (string, 18/18 records)
    "0"  x7
    "1"  x7
    "2"  x4
data.soilType  (string, 18/18 records)
    "Clay"  x8
    "Gravel"  x6
    "Sand"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 11081.05s (p5 357.01s / p95 189887.59s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowFocusEvent` — 16 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16)
- **Intervals:** median 11081.05s (p5 357.01s / p95 189887.59s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 50.47s (p5 0.14s / p95 21968.69s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x8
    "Gravel"  x4
    "Sand"  x3
    "Bedrock"  x1
data.floor  (string, 16/16 records)
    "5"  x11
    "3"  x3
    "4"  x2
data.machine  (string, 16/16 records)
    "1"  x14
    "2"  x2
data.row  (string, 16/16 records)
    "TopRow"  x15
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 58.91s (p5 0.03s / p95 328027.24s, n=13)
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

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev - Dungeon (10); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 4.31s (p5 0.45s / p95 344647.70s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 6 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 18.00s (p5 4.31s / p95 207407.03s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x1
data.toolName  (string, 6/6 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 4 Dev - Dungeon (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 933.01s (p5 84.37s / p95 69604.94s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x5
    "Open"  x1
data.chatID  (string, 6/6 records)
    "NA"  x5
    "[91-52, 91-54, 91-55, 91-61, 91-117]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 214994.42s (p5 28330.51s / p95 478580.19s, n=4)
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

### `gameWindowUnfocusEvent` — 3 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev - Dungeon (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 351202.89s (p5 45203.44s / p95 657202.34s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 3/3 records)
    false  x3
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (20 records)
- `TerasGardenBox` data.actionType: "" (10x)
- `TopographicMapEvent` data.actionType: "Selected" (16x); "Unselected" (3x); "WaypointMoveEvent" (13x); "WaypointResetEvent" (2x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (19x); "Waypoint" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*