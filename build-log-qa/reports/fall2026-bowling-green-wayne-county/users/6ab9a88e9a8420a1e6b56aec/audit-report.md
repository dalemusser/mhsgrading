# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56aec

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56aec
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56aec.jsonl
- **Records:** 13764 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56aec
- **Time span:** 2026-10-06T13:14:36.218000+00:00 .. 2026-10-16T14:50:08.999000+00:00 (241h 35m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56aec\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13764 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 103 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3786 | 27.51 | 1 | 9 | 0 | 2026-10-06T13:15:08.529000+00:00 | 2026-10-16T14:48:03.385000+00:00 | 241h 32m |
| PuzzlePieceVisibleEvent | 3760 | 27.32 | 1 | 4 | 0 | 2026-10-07T13:29:27.385000+00:00 | 2026-10-16T13:36:52.961000+00:00 | 216h 7m |
| PlayerPositionEvent | 2796 | 20.31 | 1 | 9 | 0 | 2026-10-06T13:14:48.681000+00:00 | 2026-10-16T14:50:08.999000+00:00 | 241h 35m |
| DialogueEvent | 2360 | 17.15 | 1 | 9 | 1494 | 2026-10-06T13:15:08.730000+00:00 | 2026-10-16T14:49:30.191000+00:00 | 241h 34m |
| ObjectInterEvent | 326 | 2.37 | 1 | 9 | 0 | 2026-10-06T13:22:31.102000+00:00 | 2026-10-16T14:47:10.201000+00:00 | 241h 24m |
| argumentationNodeEvent | 266 | 1.93 | 1 | 5 | 0 | 2026-10-06T13:49:26.433000+00:00 | 2026-10-16T14:39:11.794000+00:00 | 240h 49m |
| questEvent | 86 | 0.62 | 1 | 9 | 86 | 2026-10-06T13:15:08.711000+00:00 | 2026-10-16T14:48:47.700000+00:00 | 241h 33m |
| TopographicMapEvent | 68 | 0.49 | 1 | 2 | 0 | 2026-10-07T13:29:59.432000+00:00 | 2026-10-14T18:48:22.202000+00:00 | 173h 18m |
| Soil Key Puzzle | 66 | 0.48 | 1 | 3 | 0 | 2026-10-08T13:41:49.881000+00:00 | 2026-10-16T13:15:22.338000+00:00 | 191h 33m |
| argumentationAnswerEvent | 43 | 0.31 | 1 | 5 | 0 | 2026-10-06T13:48:24.709000+00:00 | 2026-10-16T14:39:13.402000+00:00 | 240h 50m |
| DEBUGMenu | 38 | 0.28 | 1 | 9 | 0 | 2026-10-06T13:14:48.663000+00:00 | 2026-10-16T13:25:33.810000+00:00 | 240h 10m |
| soilMachine | 30 | 0.22 | 1 | 1 | 0 | 2026-10-15T13:42:00.167000+00:00 | 2026-10-15T14:09:39.826000+00:00 | 27m 39s |
| gameWindowFocusEvent | 27 | 0.2 | 1 | 7 | 0 | 2026-10-06T13:14:36.218000+00:00 | 2026-10-16T13:25:24.066000+00:00 | 240h 10m |
| WaterChamberEvent | 26 | 0.19 | 1 | 1 | 0 | 2026-10-16T13:30:53.216000+00:00 | 2026-10-16T13:53:58.218000+00:00 | 23m 5s |
| gameStartEvent | 17 | 0.12 | 1 | 1 | 0 | 2026-10-06T13:14:36.219000+00:00 | 2026-10-16T13:25:24.066000+00:00 | 240h 10m |
| gameWindowUnfocusEvent | 17 | 0.12 | 1 | 8 | 0 | 2026-10-06T13:21:41.413000+00:00 | 2026-10-16T14:49:47.147000+00:00 | 241h 28m |
| argumentationEvent | 14 | 0.1 | 1 | 5 | 0 | 2026-10-06T13:47:45.437000+00:00 | 2026-10-16T14:39:13.447000+00:00 | 240h 51m |
| TerasGardenBox | 10 | 0.07 | 1 | 1 | 0 | 2026-10-15T16:08:12.129000+00:00 | 2026-10-16T13:14:04.993000+00:00 | 21h 5m |
| DaniEvent | 9 | 0.07 | 1 | 4 | 0 | 2026-10-09T00:30:49.987000+00:00 | 2026-10-15T14:01:20.179000+00:00 | 157h 30m |
| SolarStillDesignEvent | 7 | 0.05 | 1 | 1 | 0 | 2026-10-16T14:46:35.188000+00:00 | 2026-10-16T14:46:49.376000+00:00 | 14.2s |
| argumentationToolEvent | 5 | 0.04 | 1 | 2 | 0 | 2026-10-06T13:49:49.777000+00:00 | 2026-10-14T13:44:31.083000+00:00 | 191h 54m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-10-06T13:53:33.936000+00:00 | 2026-10-16T13:25:07.035000+00:00 | 239h 31m |
| chatEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-10-16T13:25:33.701000+00:00 | 2026-10-16T13:55:06.148000+00:00 | 29m 32s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 153052.996s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.178s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 19.217s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.66s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 21.113s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 153.506s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.989s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8732.364s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2011.327s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 4580.453s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.831s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 38 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 9 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
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
  - Observed: ; Covered; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 8.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,3,I; A,3,II; A,D,2,II; A,D,C,2,II; B,1,II; B,2,II; B,3,I; B,3,II; B,4,II; C,1,II; C,2,I; C,2,II; C,3,II; C,4,II; C,D,3,II; D,2,II; I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 27 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 6.0x vs baseline. 
  - Observed: 30 records 
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
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[159] _id=6ac4f6bdde269131f9b079f2 ts=2026-10-06T13:25:16.7030000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[276] _id=6ac4f7d5de269131f9b0a86f ts=2026-10-06T13:29:56.1040000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[297] _id=6ac4f81fde269131f9b0b772 ts=2026-10-06T13:31:10.5440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[5] _id=6ac4f43dde269131f9b0300c ts=2026-10-06T13:14:36.2190000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[707] _id=6ac4fe0dde269131f9b20137 ts=2026-10-06T13:56:28.7250000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[749] _id=6ac648adde269131f9b9082c ts=2026-10-07T13:27:08.1990000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 27 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 27} 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[4] _id=6ac4f43cde269131f9b03008 ts=2026-10-06T13:14:36.2180000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[115] _id=6ac4f5ebde269131f9b0496f ts=2026-10-06T13:21:46.7640000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[702] _id=6ac4fe0dde269131f9b20125 ts=2026-10-06T13:56:28.7240000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[113] _id=6ac4f5e6de269131f9b048b5 ts=2026-10-06T13:21:41.4130000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[750] _id=6ac648adde269131f9b90822 ts=2026-10-06T13:59:29.458Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[2694] _id=6ac64d09de269131f9b9eafe ts=2026-10-07T13:45:44.7940000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 68 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[933] _id=6ac64958de269131f9b93361 ts=2026-10-07T13:29:59.4320000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[931] _id=6ac64959de269131f9b93398 ts=2026-10-07T13:30:00.9160000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[941] _id=6ac6496cde269131f9b9380a ts=2026-10-07T13:30:20.2570000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3785 | 0.0 | 1.178 | 229.742 | 18.025 | 391519.474 | 0.26 | 119 | 14 |
| PuzzlePieceVisibleEvent | 3759 | 0.0 | 0.023 | 206.982 | 1.37 | 481835.148 | 0.29 | 2034 | 7 |
| PlayerPositionEvent | 2784 | 0.0 | 10.0 | 288.477 | 10.103 | 391524.07 | 0.21 | 1 | 10 |
| DialogueEvent | 2359 | 0.0 | 4.241 | 368.657 | 37.032 | 391704.007 | 0.16 | 691 | 13 |
| ObjectInterEvent | 325 | 0.0 | 10.719 | 2674.09 | 507.28 | 430963.236 | 0.02 | 3 | 12 |
| argumentationNodeEvent | 265 | 0.02 | 0.441 | 3271.643 | 24.068 | 604765.318 | 0.02 | 50 | 4 |
| questEvent | 85 | 0.0 | 222.159 | 10230.812 | 73993.786 | 392552.654 | 0.01 | 15 | 22 |
| TopographicMapEvent | 67 | 0.019 | 10.66 | 9311.982 | 8887.073 | 478580.224 | 0.01 | 2 | 9 |
| Soil Key Puzzle | 65 | 0.116 | 0.83 | 10609.422 | 262.612 | 519041.561 | 0.01 | 0 | 3 |
| argumentationAnswerEvent | 42 | 0.147 | 21.113 | 20644.017 | 85699.319 | 604784.324 | 0.0 | 0 | 4 |
| DEBUGMenu | 37 | 8.225 | 677.012 | 23368.788 | 84802.247 | 392843.575 | 0.0 | 0 | 20 |
| soilMachine | 29 | 0.23 | 5.831 | 57.23 | 220.488 | 396.304 | 1.05 | 0 | 0 |
| gameWindowFocusEvent | 26 | 8.676 | 2011.327 | 33255.686 | 85239.563 | 392855.802 | 0.0 | 0 | 20 |
| WaterChamberEvent | 25 | 3.292 | 26.436 | 55.4 | 240.229 | 285.846 | 1.08 | 0 | 0 |
| gameStartEvent | 16 | 859.952 | 8732.364 | 54040.49 | 162368.232 | 392855.802 | 0.0 | 0 | 16 |
| gameWindowUnfocusEvent | 16 | 6.104 | 4580.453 | 54330.358 | 172201.737 | 429517.464 | 0.0 | 0 | 12 |
| argumentationEvent | 13 | 0.048 | 153.506 | 66699.078 | 298647.329 | 604757.919 | 0.0 | 1 | 4 |
| TerasGardenBox | 9 | 0.663 | 19.217 | 8439.207 | 45523.828 | 75853.002 | 0.01 | 0 | 1 |
| DaniEvent | 8 | 0.559 | 207.953 | 70878.774 | 339223.789 | 480720.515 | 0.0 | 0 | 3 |
| SolarStillDesignEvent | 6 | 0.738 | 2.035 | 2.365 | 4.314 | 4.408 | 25.37 | 0 | 0 |
| argumentationToolEvent | 4 | 1.571 | 1.989 | 172720.326 | 587244.72 | 690875.758 | 0.0 | 0 | 1 |
| EndOfUnit | 3 | 104346.678 | 153052.996 | 287431.033 | 559709.382 | 604893.425 | 0.0 | 0 | 3 |
| chatEvent | 1 | 1772.447 | 1772.447 | 1772.447 | 1772.447 | 1772.447 | 0.03 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 9 group(s), 24 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[5029] _id=6acf7fccde269131f9d2d176 ts=2026-10-14T13:12:43.2820000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[5030] _id=6acf7fccde269131f9d2d177 ts=2026-10-14T13:12:43.2820000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[5037] _id=6acf7fccde269131f9d2d17e ts=2026-10-14T13:12:43.2830000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[5038] _id=6acf7fccde269131f9d2d17f ts=2026-10-14T13:12:43.2830000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[6365] _id=6acf8af0de269131f9d3cfb6 ts=2026-10-14T14:00:15.1310000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[6366] _id=6acf8af0de269131f9d3cfb7 ts=2026-10-14T14:00:15.1310000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 44 group(s), 78 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[862] _id=6ac64938de269131f9b92a74 ts=2026-10-07T13:29:27.3850000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[863] _id=6ac64939de269131f9b92a7e ts=2026-10-07T13:29:27.3850000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[868] _id=6ac64939de269131f9b92a9e ts=2026-10-07T13:29:27.7760000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[857] _id=6ac64939de269131f9b92aae ts=2026-10-07T13:29:27.7760000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[864] _id=6ac6493ade269131f9b92acb ts=2026-10-07T13:29:28.3100000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[873] _id=6ac6493ade269131f9b92ade ts=2026-10-07T13:29:28.3100000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[13557] _id=6ad2376dde269131f9e48b8d ts=2026-10-16T14:40:44.2550000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[13558] _id=6ad2376dde269131f9e48b8e ts=2026-10-16T14:40:44.2550000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[13749] _id=6ad23950de269131f9e4a39b ts=2026-10-16T14:48:47.7000000Z == 6ab9a88e9a8420a1e6b56aec.jsonl[13750] _id=6ad23950de269131f9e4a39c ts=2026-10-16T14:48:47.7000000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 19 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a88e9a8420a1e6b56aec.jsonl[133] _id=6ac4f617de269131f9b05394 ts=2026-10-06T13:22:31.1020000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[140] _id=6ac4f617de269131f9b0539c ts=2026-10-06T13:22:31.1080000Z`; `201ms: 6ab9a88e9a8420a1e6b56aec.jsonl[805] _id=6ac64900de269131f9b91d66 ts=2026-10-07T13:28:32.0790000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[806] _id=6ac64900de269131f9b91d71 ts=2026-10-07T13:28:32.2800000Z`; `283ms: 6ab9a88e9a8420a1e6b56aec.jsonl[806] _id=6ac64900de269131f9b91d71 ts=2026-10-07T13:28:32.2800000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[807] _id=6ac64901de269131f9b91d80 ts=2026-10-07T13:28:32.5630000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `663ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11486] _id=6ad2231ade269131f9e35dae ts=2026-10-16T13:14:01.7480000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[11505] _id=6ad2231bde269131f9e35db4 ts=2026-10-16T13:14:02.4110000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `741ms: 6ab9a88e9a8420a1e6b56aec.jsonl[567] _id=6ac4fc82de269131f9b194b7 ts=2026-10-06T13:49:53.2400000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[559] _id=6ac4fc82de269131f9b194f9 ts=2026-10-06T13:49:53.9810000Z`; `147ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11198] _id=6ad0f95ede269131f9dd21cd ts=2026-10-15T16:03:41.0690000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[11200] _id=6ad0f95ede269131f9dd21d3 ts=2026-10-15T16:03:41.2160000Z`; `195ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11200] _id=6ad0f95ede269131f9dd21d3 ts=2026-10-15T16:03:41.2160000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[11201] _id=6ad0f95ede269131f9dd21db ts=2026-10-15T16:03:41.4110000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `54ms: 6ab9a88e9a8420a1e6b56aec.jsonl[6039] _id=6acf875ade269131f9d35401 ts=2026-10-14T13:44:57.9340000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[6047] _id=6acf875ade269131f9d35405 ts=2026-10-14T13:44:57.9880000Z`; `48ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11210] _id=6ad0f96ede269131f9dd238c ts=2026-10-15T16:03:57.4430000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[11214] _id=6ad0f96ede269131f9dd239a ts=2026-10-15T16:03:57.4910000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `51ms: 6ab9a88e9a8420a1e6b56aec.jsonl[547] _id=6ac4fc8bde269131f9b19766 ts=2026-10-06T13:50:01.0380000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[580] _id=6ac4fc8cde269131f9b19795 ts=2026-10-06T13:50:01.0890000Z`; `966ms: 6ab9a88e9a8420a1e6b56aec.jsonl[5984] _id=6acf86f4de269131f9d34bd9 ts=2026-10-14T13:43:16.0730000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[5981] _id=6acf86f5de269131f9d34beb ts=2026-10-14T13:43:17.0390000Z`; `796ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11091] _id=6ad0f8cbde269131f9dd0e07 ts=2026-10-15T16:01:14.6860000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[11094] _id=6ad0f8ccde269131f9dd0e26 ts=2026-10-15T16:01:15.4820000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `732ms: 6ab9a88e9a8420a1e6b56aec.jsonl[9729] _id=6ad0d9abde269131f9db1553 ts=2026-10-15T13:48:26.9390000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[9728] _id=6ad0d9acde269131f9db1574 ts=2026-10-15T13:48:27.6710000Z`; `910ms: 6ab9a88e9a8420a1e6b56aec.jsonl[10108] _id=6ad0dba1de269131f9db5396 ts=2026-10-15T13:56:48.9430000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[10111] _id=6ad0dba2de269131f9db53b3 ts=2026-10-15T13:56:49.8530000Z`; `230ms: 6ab9a88e9a8420a1e6b56aec.jsonl[10207] _id=6ad0dc2cde269131f9db64ce ts=2026-10-15T13:59:08.1990000Z ~ 6ab9a88e9a8420a1e6b56aec.jsonl[10212] _id=6ad0dc2cde269131f9db64d9 ts=2026-10-15T13:59:08.4290000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 109h 7m 
  - Evidence: 109h 7m: 6ab9a88e9a8420a1e6b56aec.jsonl[3927] _id=6ac8307ede269131f9c76956 ts=2026-10-09T00:08:29.8090000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4298] _id=6ace2f0ade269131f9ce8df8 ts=2026-10-13T13:15:53.3840000Z; 23h 45m: 6ab9a88e9a8420a1e6b56aec.jsonl[2653] _id=6ac64cb1de269131f9b9e3df ts=2026-10-07T13:44:16.7110000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2929] _id=6ac79ac9de269131f9c03d06 ts=2026-10-08T13:29:44.5340000Z; 23h 30m: 6ab9a88e9a8420a1e6b56aec.jsonl[712] _id=6ac4fe1fde269131f9b206a5 ts=2026-10-06T13:56:47.2110000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[747] _id=6ac648adde269131f9b9082a ts=2026-10-07T13:27:08.0640000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 133h 32m 
  - Evidence: 133h 32m: 6ab9a88e9a8420a1e6b56aec.jsonl[4294] _id=6ac835bade269131f9c77e66 ts=2026-10-09T00:30:49.9870000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[6404] _id=6acf8b8bde269131f9d3df21 ts=2026-10-14T14:02:50.5020000Z; 21h 14m: 6ab9a88e9a8420a1e6b56aec.jsonl[7782] _id=6acfb167de269131f9d5c0c4 ts=2026-10-14T16:44:23.2130000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[10170] _id=6ad0dc04de269131f9db5ef6 ts=2026-10-15T13:58:27.3670000Z; 2h 37m: 6ab9a88e9a8420a1e6b56aec.jsonl[6422] _id=6acf8c8bde269131f9d3e8f0 ts=2026-10-14T14:07:06.3030000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[7779] _id=6acfb161de269131f9d5c02a ts=2026-10-14T16:44:17.1260000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 108h 48m 
  - Evidence: 108h 48m: 6ab9a88e9a8420a1e6b56aec.jsonl[4276] _id=6ac83501de269131f9c77b5a ts=2026-10-09T00:27:45.4830000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4305] _id=6ace2f1bde269131f9ce8e9c ts=2026-10-13T13:16:09.4900000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aec.jsonl[2922] _id=6ac6501dde269131f9ba395d ts=2026-10-07T13:58:52.6710000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2950] _id=6ac79b09de269131f9c044e8 ts=2026-10-08T13:30:49.2520000Z; 23h 28m: 6ab9a88e9a8420a1e6b56aec.jsonl[745] _id=6ac4febfde269131f9b23322 ts=2026-10-06T13:59:27.1120000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[774] _id=6ac648d1de269131f9b911e4 ts=2026-10-07T13:27:44.3520000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 691 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11112] _id=6ad0f8d5de269131f9dd0f95 ts=2026-10-15T16:01:24.0390000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11113] _id=6ad0f8d5de269131f9dd0f96 ts=2026-10-15T16:01:24.0390000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11121] _id=6ad0f8e6de269131f9dd1266 ts=2026-10-15T16:01:41.2620000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11122] _id=6ad0f8e6de269131f9dd1267 ts=2026-10-15T16:01:41.2620000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11137] _id=6ad0f8fbde269131f9dd1597 ts=2026-10-15T16:02:02.3940000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11138] _id=6ad0f8fbde269131f9dd1598 ts=2026-10-15T16:02:02.3940000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 1m 
  - Evidence: 168h 1m: 6ab9a88e9a8420a1e6b56aec.jsonl[631] _id=6ac4fd5ede269131f9b1cef2 ts=2026-10-06T13:53:33.9360000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4956] _id=6ace383cde269131f9cef2fb ts=2026-10-13T13:55:07.3610000Z; 42h 30m: 6ab9a88e9a8420a1e6b56aec.jsonl[8076] _id=6acfcfd6de269131f9d7b27a ts=2026-10-14T18:54:14.0390000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11687] _id=6ad225b4de269131f9e39294 ts=2026-10-16T13:25:07.0350000Z; 28h 59m: 6ab9a88e9a8420a1e6b56aec.jsonl[4956] _id=6ace383cde269131f9cef2fb ts=2026-10-13T13:55:07.3610000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[8076] _id=6acfcfd6de269131f9d7b27a ts=2026-10-14T18:54:14.0390000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 108h 45m 
  - Evidence: 108h 45m: 6ab9a88e9a8420a1e6b56aec.jsonl[4295] _id=6ac835bade269131f9c77e6b ts=2026-10-09T00:30:49.9960000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4303] _id=6ace2f1bde269131f9ce8e9a ts=2026-10-13T13:16:09.4700000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aec.jsonl[2908] _id=6ac64ff8de269131f9ba36a6 ts=2026-10-07T13:58:15.9220000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2937] _id=6ac79adbde269131f9c03efe ts=2026-10-08T13:30:02.0750000Z; 23h 28m: 6ab9a88e9a8420a1e6b56aec.jsonl[734] _id=6ac4feacde269131f9b22f38 ts=2026-10-06T13:59:07.7650000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[754] _id=6ac648c3de269131f9b90e2c ts=2026-10-07T13:27:30.5990000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 119 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[10983] _id=6ad0f7fade269131f9dcfa14 ts=2026-10-15T15:57:45.8950000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[10984] _id=6ad0f7fade269131f9dcfa15 ts=2026-10-15T15:57:45.8950000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11235] _id=6ad0f99bde269131f9dd2883 ts=2026-10-15T16:04:42.6790000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11236] _id=6ad0f99bde269131f9dd2884 ts=2026-10-15T16:04:42.6790000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11415] _id=6ad22276de269131f9e351a8 ts=2026-10-16T13:11:16.3350000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11416] _id=6ad22276de269131f9e351a9 ts=2026-10-16T13:11:16.3350000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 42m 
  - Evidence: 119h 42m: 6ab9a88e9a8420a1e6b56aec.jsonl[3588] _id=6ac79ec5de269131f9c0e9ce ts=2026-10-08T13:46:45.2550000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4462] _id=6ace3239de269131f9ceaa26 ts=2026-10-13T13:29:28.4910000Z; 24h 4m: 6ab9a88e9a8420a1e6b56aec.jsonl[2524] _id=6ac64b0dde269131f9b9a08b ts=2026-10-07T13:37:16.8360000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[3222] _id=6ac79d9ede269131f9c0b961 ts=2026-10-08T13:41:49.8850000Z; 23h 35m: 6ab9a88e9a8420a1e6b56aec.jsonl[633] _id=6ac4fd34de269131f9b1c384 ts=2026-10-06T13:52:51.5410000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[808] _id=6ac648fede269131f9b91cbe ts=2026-10-07T13:28:29.6550000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.006s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[10905] _id=6ad0f7aede269131f9dcf3f2 ts=2026-10-15T15:56:29.1140000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[10906] _id=6ad0f7aede269131f9dcf3f3 ts=2026-10-15T15:56:29.1140000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[10961] _id=6ad0f7eede269131f9dcf8c7 ts=2026-10-15T15:57:33.0070000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[10962] _id=6ad0f7eede269131f9dcf8c8 ts=2026-10-15T15:57:33.0070000Z; 6ms: 6ab9a88e9a8420a1e6b56aec.jsonl[133] _id=6ac4f617de269131f9b05394 ts=2026-10-06T13:22:31.1020000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[140] _id=6ac4f617de269131f9b0539c ts=2026-10-06T13:22:31.1080000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 108h 45m 
  - Evidence: 108h 45m: 6ab9a88e9a8420a1e6b56aec.jsonl[4293] _id=6ac835b0de269131f9c77e2b ts=2026-10-09T00:30:40.4240000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4299] _id=6ace2f1bde269131f9ce8e99 ts=2026-10-13T13:16:04.4940000Z; 23h 30m: 6ab9a88e9a8420a1e6b56aec.jsonl[2927] _id=6ac65049de269131f9ba3bd4 ts=2026-10-07T13:59:36.8250000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2933] _id=6ac79adbde269131f9c03efd ts=2026-10-08T13:29:56.2000000Z; 23h 27m: 6ab9a88e9a8420a1e6b56aec.jsonl[739] _id=6ac4feb9de269131f9b23208 ts=2026-10-06T13:59:20.4550000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[752] _id=6ac648bcde269131f9b90c74 ts=2026-10-07T13:27:20.3730000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[8078] _id=6acfcfd7de269131f9d7b283 ts=2026-10-14T18:54:14.3710000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[8079] _id=6ad0d292de269131f9da5c82 ts=2026-10-14T18:54:14.371Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 133h 50m 
  - Evidence: 133h 50m: 6ab9a88e9a8420a1e6b56aec.jsonl[4002] _id=6ac830c5de269131f9c76aca ts=2026-10-09T00:09:39.9920000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[6369] _id=6acf8af0de269131f9d3cfcc ts=2026-10-14T14:00:15.1400000Z; 24h 7m: 6ab9a88e9a8420a1e6b56aec.jsonl[2514] _id=6ac64ae9de269131f9b999cf ts=2026-10-07T13:36:38.9800000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[3284] _id=6ac79e1dde269131f9c0cbcc ts=2026-10-08T13:43:56.7790000Z; 23h 10m: 6ab9a88e9a8420a1e6b56aec.jsonl[10685] _id=6ad0dfdcde269131f9db9c2e ts=2026-10-15T14:14:49.3110000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11697] _id=6ad225d6de269131f9e394ad ts=2026-10-16T13:25:40.1180000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2034 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[1000] _id=6ac6499cde269131f9b94540 ts=2026-10-07T13:29:36.0020000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[1021] _id=6ac6499cde269131f9b9454d ts=2026-10-07T13:29:36.0020000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[1003] _id=6ac6499ade269131f9b944c2 ts=2026-10-07T13:29:35.3480000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[1005] _id=6ac6499ade269131f9b944c8 ts=2026-10-07T13:29:35.3480000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[1004] _id=6ac6499ade269131f9b944bc ts=2026-10-07T13:29:35.3480000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[1003] _id=6ac6499ade269131f9b944c2 ts=2026-10-07T13:29:35.3480000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 10m 
  - Evidence: 144h 10m: 6ab9a88e9a8420a1e6b56aec.jsonl[3239] _id=6ac79db8de269131f9c0be33 ts=2026-10-08T13:42:16.1390000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[6212] _id=6acf893ade269131f9d38ac6 ts=2026-10-14T13:52:57.7000000Z; 23h 48m: 6ab9a88e9a8420a1e6b56aec.jsonl[8584] _id=6ad0d4a0de269131f9da89e8 ts=2026-10-15T13:26:55.8880000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11541] _id=6ad2236ade269131f9e363a5 ts=2026-10-16T13:15:21.2610000Z; 23h 24m: 6ab9a88e9a8420a1e6b56aec.jsonl[6349] _id=6acf8ac9de269131f9d3c907 ts=2026-10-14T13:59:36.3440000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[8196] _id=6ad0d40bde269131f9da7a01 ts=2026-10-15T13:24:27.4160000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 21h 4m 
  - Evidence: 21h 4m: 6ab9a88e9a8420a1e6b56aec.jsonl[11386] _id=6ad0fa9ede269131f9dd45ff ts=2026-10-15T16:09:01.6420000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11467] _id=6ad222ebde269131f9e35992 ts=2026-10-16T13:13:14.6440000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 132h 56m 
  - Evidence: 132h 56m: 6ab9a88e9a8420a1e6b56aec.jsonl[4198] _id=6ac83351de269131f9c770f7 ts=2026-10-09T00:20:32.7490000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[5090] _id=6acf80c5de269131f9d2dd1e ts=2026-10-14T13:16:52.9730000Z; 23h 37m: 6ab9a88e9a8420a1e6b56aec.jsonl[2841] _id=6ac64f1dde269131f9ba2716 ts=2026-10-07T13:54:37.1650000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2967] _id=6ac79b68de269131f9c050a6 ts=2026-10-08T13:32:24.1100000Z; 10h 9m: 6ab9a88e9a8420a1e6b56aec.jsonl[3920] _id=6ac7a1ecde269131f9c15bc1 ts=2026-10-08T14:00:11.9730000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4030] _id=6ac830c9de269131f9c76aee ts=2026-10-09T00:09:45.3290000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.021s shown 
  - Evidence: 19ms: 6ab9a88e9a8420a1e6b56aec.jsonl[2734] _id=6ac64d7ede269131f9b9f3c2 ts=2026-10-07T13:47:41.7670000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2738] _id=6ac64d7ede269131f9b9f3c6 ts=2026-10-07T13:47:41.7860000Z; 21ms: 6ab9a88e9a8420a1e6b56aec.jsonl[2733] _id=6ac64d7ede269131f9b9f3c1 ts=2026-10-07T13:47:41.7460000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2734] _id=6ac64d7ede269131f9b9f3c2 ts=2026-10-07T13:47:41.7670000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 59m 
  - Evidence: 167h 59m: 6ab9a88e9a8420a1e6b56aec.jsonl[581] _id=6ac4fc8dde269131f9b1982a ts=2026-10-06T13:50:05.0650000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4834] _id=6ace36fede269131f9cee1d6 ts=2026-10-13T13:49:49.3890000Z; 26h 16m: 6ab9a88e9a8420a1e6b56aec.jsonl[6038] _id=6acf875ade269131f9d353ff ts=2026-10-14T13:44:57.9020000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11104] _id=6ad0f8d5de269131f9dd0f92 ts=2026-10-15T16:01:24.0200000Z; 23h 52m: 6ab9a88e9a8420a1e6b56aec.jsonl[4834] _id=6ace36fede269131f9cee1d6 ts=2026-10-13T13:49:49.3890000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[5943] _id=6acf86c3de269131f9d348eb ts=2026-10-14T13:42:26.8070000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 59m 
  - Evidence: 167h 59m: 6ab9a88e9a8420a1e6b56aec.jsonl[588] _id=6ac4fc8ede269131f9b19840 ts=2026-10-06T13:50:05.0870000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4813] _id=6ace36e3de269131f9cee00c ts=2026-10-13T13:49:23.0060000Z; 26h 16m: 6ab9a88e9a8420a1e6b56aec.jsonl[6047] _id=6acf875ade269131f9d35405 ts=2026-10-14T13:44:57.9880000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11086] _id=6ad0f8c8de269131f9dd0d85 ts=2026-10-15T16:01:11.5900000Z; 23h 52m: 6ab9a88e9a8420a1e6b56aec.jsonl[4835] _id=6ace36fede269131f9cee1dc ts=2026-10-13T13:49:49.4200000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[5942] _id=6acf86c1de269131f9d348cc ts=2026-10-14T13:42:24.4280000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.048s..0.048s shown 
  - Evidence: 48ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11210] _id=6ad0f96ede269131f9dd238c ts=2026-10-15T16:03:57.4430000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11214] _id=6ad0f96ede269131f9dd239a ts=2026-10-15T16:03:57.4910000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 59m 
  - Evidence: 167h 59m: 6ab9a88e9a8420a1e6b56aec.jsonl[580] _id=6ac4fc8cde269131f9b19795 ts=2026-10-06T13:50:01.0890000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4811] _id=6ace36e7de269131f9cee03c ts=2026-10-13T13:49:26.4070000Z; 26h 16m: 6ab9a88e9a8420a1e6b56aec.jsonl[6043] _id=6acf8758de269131f9d353ce ts=2026-10-14T13:44:55.2320000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11090] _id=6ad0f8cade269131f9dd0dd8 ts=2026-10-15T16:01:13.3900000Z; 23h 53m: 6ab9a88e9a8420a1e6b56aec.jsonl[4832] _id=6ace36fbde269131f9cee1bc ts=2026-10-13T13:49:46.6370000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[5955] _id=6acf86e4de269131f9d34aa0 ts=2026-10-14T13:42:59.5190000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 50 interval(s) ≤ 0.020s..0.021s shown 
  - Evidence: 20ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11067] _id=6ad0f90ede269131f9dd1804 ts=2026-10-15T16:02:21.1280000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11059] _id=6ad0f90ede269131f9dd180a ts=2026-10-15T16:02:21.1480000Z; 21ms: 6ab9a88e9a8420a1e6b56aec.jsonl[11109] _id=6ad0f8dede269131f9dd1119 ts=2026-10-15T16:01:33.6840000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[11110] _id=6ad0f8dede269131f9dd1122 ts=2026-10-15T16:01:33.7050000Z; 21ms: 6ab9a88e9a8420a1e6b56aec.jsonl[13514] _id=6ad236f6de269131f9e4872c ts=2026-10-16T14:38:44.9390000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[13515] _id=6ad236f6de269131f9e4872d ts=2026-10-16T14:38:44.9600000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 54m 
  - Evidence: 191h 54m: 6ab9a88e9a8420a1e6b56aec.jsonl[566] _id=6ac4fc81de269131f9b194a7 ts=2026-10-06T13:49:53.1520000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[6021] _id=6acf873dde269131f9d351cd ts=2026-10-14T13:44:28.9100000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 29m 32s 
  - Evidence: 29m 32s: 6ab9a88e9a8420a1e6b56aec.jsonl[11692] _id=6ad225cede269131f9e39436 ts=2026-10-16T13:25:33.7010000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[12970] _id=6ad22cbbde269131f9e43084 ts=2026-10-16T13:55:06.1480000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 109h 7m 
  - Evidence: 109h 7m: 6ab9a88e9a8420a1e6b56aec.jsonl[3933] _id=6ac83072de269131f9c76916 ts=2026-10-09T00:08:17.7480000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4297] _id=6ace2f0ade269131f9ce8dfd ts=2026-10-13T13:15:53.5500000Z; 23h 45m: 6ab9a88e9a8420a1e6b56aec.jsonl[2651] _id=6ac64ca6de269131f9b9e32c ts=2026-10-07T13:44:05.6280000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2931] _id=6ac79ac9de269131f9c03d08 ts=2026-10-08T13:29:44.6700000Z; 23h 30m: 6ab9a88e9a8420a1e6b56aec.jsonl[707] _id=6ac4fe0dde269131f9b20137 ts=2026-10-06T13:56:28.7250000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[749] _id=6ac648adde269131f9b9082c ts=2026-10-07T13:27:08.1990000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 109h 7m 
  - Evidence: 109h 7m: 6ab9a88e9a8420a1e6b56aec.jsonl[3932] _id=6ac83072de269131f9c76915 ts=2026-10-09T00:08:17.7480000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4296] _id=6ace2f0ade269131f9ce8dfc ts=2026-10-13T13:15:53.5500000Z; 23h 43m: 6ab9a88e9a8420a1e6b56aec.jsonl[2695] _id=6ac64d09de269131f9b9eb02 ts=2026-10-07T13:45:45.0780000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2930] _id=6ac79ac9de269131f9c03d07 ts=2026-10-08T13:29:44.6700000Z; 23h 30m: 6ab9a88e9a8420a1e6b56aec.jsonl[702] _id=6ac4fe0dde269131f9b20125 ts=2026-10-06T13:56:28.7240000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[748] _id=6ac648adde269131f9b9082b ts=2026-10-07T13:27:08.1990000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a88e9a8420a1e6b56aec.jsonl[3934] _id=6ac83071de269131f9c76912 ts=2026-10-08T14:00:14.774Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4339] _id=6ace2fbdde269131f9ce9344 ts=2026-10-13T13:18:52.2380000Z; 24h 0m: 6ab9a88e9a8420a1e6b56aec.jsonl[2928] _id=6ac79ac9de269131f9c03cf4 ts=2026-10-07T13:59:44.946Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[3934] _id=6ac83071de269131f9c76912 ts=2026-10-08T14:00:14.774Z; 23h 54m: 6ab9a88e9a8420a1e6b56aec.jsonl[5022] _id=6acf7fbade269131f9d2d067 ts=2026-10-13T14:00:39.181Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[6252] _id=6acf89a3de269131f9d39a1e ts=2026-10-14T13:54:42.1060000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 109h 2m 
  - Evidence: 109h 2m: 6ab9a88e9a8420a1e6b56aec.jsonl[4100] _id=6ac831b1de269131f9c76d74 ts=2026-10-09T00:13:36.8830000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[4307] _id=6ace2f1bde269131f9ce8e9e ts=2026-10-13T13:16:09.5370000Z; 23h 42m: 6ab9a88e9a8420a1e6b56aec.jsonl[2724] _id=6ac64d66de269131f9b9f1c8 ts=2026-10-07T13:47:17.7390000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[2938] _id=6ac79adbde269131f9c03eff ts=2026-10-08T13:30:02.1150000Z; 23h 28m: 6ab9a88e9a8420a1e6b56aec.jsonl[732] _id=6ac4fe9ede269131f9b22b8a ts=2026-10-06T13:58:53.2840000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[753] _id=6ac648bcde269131f9b90c75 ts=2026-10-07T13:27:23.5670000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[13557] _id=6ad2376dde269131f9e48b8d ts=2026-10-16T14:40:44.2550000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[13558] _id=6ad2376dde269131f9e48b8e ts=2026-10-16T14:40:44.2550000Z; 0ms: 6ab9a88e9a8420a1e6b56aec.jsonl[13749] _id=6ad23950de269131f9e4a39b ts=2026-10-16T14:48:47.7000000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[13750] _id=6ad23950de269131f9e4a39c ts=2026-10-16T14:48:47.7000000Z; 2ms: 6ab9a88e9a8420a1e6b56aec.jsonl[499] _id=6ac4fb92de269131f9b1559b ts=2026-10-06T13:45:53.1330000Z -> 6ab9a88e9a8420a1e6b56aec.jsonl[495] _id=6ac4fb92de269131f9b155a0 ts=2026-10-06T13:45:53.1350000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[486] _id=6ac4fb85de269131f9b1522e ts=2026-10-06T13:45:40.3510000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[604] _id=6ac4fcb1de269131f9b1a3c6 ts=2026-10-06T13:50:40.6650000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[2840] _id=6ac64f1cde269131f9ba26ce ts=2026-10-07T13:54:35.3280000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[6047] _id=6acf875ade269131f9d35405 ts=2026-10-14T13:44:57.9880000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[11214] _id=6ad0f96ede269131f9dd239a ts=2026-10-15T16:03:57.4910000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[580] _id=6ac4fc8cde269131f9b19795 ts=2026-10-06T13:50:01.0890000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[11692] _id=6ad225cede269131f9e39436 ts=2026-10-16T13:25:33.7010000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[12970] _id=6ad22cbbde269131f9e43084 ts=2026-10-16T13:55:06.1480000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[6357] _id=6acf8ae4de269131f9d3cd99 ts=2026-10-14T14:00:03.8350000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[9826] _id=6ad0da3cde269131f9db28e6 ts=2026-10-15T13:50:51.6990000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[2936] _id=6ac79adbde269131f9c03eeb ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[6404] _id=6acf8b8bde269131f9d3df21 ts=2026-10-14T14:02:50.5020000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[7779] _id=6acfb161de269131f9d5c02a ts=2026-10-14T16:44:17.1260000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[10170] _id=6ad0dc04de269131f9db5ef6 ts=2026-10-15T13:58:27.3670000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 24 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[3492] _id=6ac79e9fde269131f9c0e342 ts=2026-10-08T13:46:05.8210000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[3493] _id=6ac79ea0de269131f9c0e34a ts=2026-10-08T13:46:05.8210000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[3521] _id=6ac79ea8de269131f9c0e4d2 ts=2026-10-08T13:46:14.0830000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 59 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[863] _id=6ac64939de269131f9b92a7e ts=2026-10-07T13:29:27.3850000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[868] _id=6ac64939de269131f9b92a9e ts=2026-10-07T13:29:27.7760000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[857] _id=6ac64939de269131f9b92aae ts=2026-10-07T13:29:27.7760000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[4030] _id=6ac830c9de269131f9c76aee ts=2026-10-09T00:09:45.3290000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[4188] _id=6ac8331ade269131f9c76ff5 ts=2026-10-09T00:19:38.5230000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[4202] _id=6ac8334fde269131f9c770dd ts=2026-10-09T00:20:30.9570000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[565] _id=6ac4fc80de269131f9b1943e ts=2026-10-06T13:49:51.5810000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[6022] _id=6acf873fde269131f9d351f3 ts=2026-10-14T13:44:31.0830000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'DialogueStartEvent' (totals: 438 start, 428 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'BecameCameraCentered' (totals: 801 open, 799 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 1086 open, 1074 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 24 open, 23 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 4 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 50 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 354 of 13762 adjacent _id pairs reverse in client time; worst 90.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56aec.jsonl[1001] _id=6ac64999de269131f9b94470 ts=2026-10-07T13:31:04.7740000Z`; `6ab9a88e9a8420a1e6b56aec.jsonl[1009] _id=6ac6499ade269131f9b944b0 ts=2026-10-07T13:29:34.7940000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.85s, min -84600.21s, max -0.26s over 13763 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56aec\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3786 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (835); Unit 2 Prod (Refactor) (833); Unit 3 Dev (731); Unit 5 Dev - Dungeon (393); Unit 3 Dungeon Dev (293); Unit 4 Dev (265); Unit 1 Dev (203); Unit 4 Dev - Anderson Base (138); Unit 5 Dev (95)
- **Intervals:** median 1.18s (p5 0.10s / p95 18.02s, n=3785)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3786/3786 records)
    "pressed"  x3786
data.actionType  (string, 3786/3786 records)
    "Move"  x2628
    "Interact"  x584
    "Jump"  x393
    "Ascend"  x67
    "Sprint"  x48
    "Hoverboard"  x33
    "Map"  x22
    "Pause"  x6
    "SkipCinematic"  x4
    "ToggleDebug"  x1
data.key  (string, 3786/3786 records, 12 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3786/3786 records)
    "Player"  x3150
    "Drone"  x636
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3760 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1758); Unit 4 Dev (862); Unit 5 Dev - Dungeon (582); Unit 3 Dungeon Dev (558)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.37s, n=3759)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3760/3760 records)
    "BecameVisible"  x1086
    "BecameInvisible"  x1074
    "BecameCameraCentered"  x801
    "BecameCameraUncentered"  x799
data.pieceId  (string, 3760/3760 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3760/3760 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2796 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (746); Unit 3 Dev (650); Unit 5 Dev (328); Unit 4 Dev - Dungeon (241); Unit 4 Dev (234); Unit 1 Dev (232); Unit 5 Dev - Dungeon (176); Unit 3 Dungeon Dev (118); Unit 4 Dev - Anderson Base (71)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.10s, n=2784)
- **Fields under `data`:**

```text
data.position  (object, 2796/2796 records)
data.position.x  (number, 2796/2796 records)
    numeric range -706.559 .. 1557.09 (761 unique)
data.position.y  (number, 2796/2796 records)
    numeric range -41232 .. 227.602 (564 unique)
data.position.z  (number, 2796/2796 records)
    numeric range -1103.11 .. 2106.89 (763 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2360 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (735); Unit 3 Dev (388); Unit 4 Dev (314); Unit 5 Dev (217); Unit 1 Dev (201); Unit 4 Dev - Dungeon (158); Unit 3 Dungeon Dev (149); Unit 4 Dev - Anderson Base (120); Unit 5 Dev - Dungeon (78)
- **eventKey:** present on 1494 of 2360 records
- **Intervals:** median 4.24s (p5 0.00s / p95 37.03s, n=2359)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1494; [conversationId, dialogueEventType] x866
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2360/2360 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2360/2360 records)
    "DialogueNodeEvent"  x1494
    "DialogueStartEvent"  x438
    "DialogueFinishEvent"  x428
data.nodeId  (number, 1494/2360 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 326 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (125); Unit 2 Prod (Refactor) (77); Unit 3 Dungeon Dev (32); Unit 4 Dev (31); Unit 5 Dev (15); Unit 5 Dev - Dungeon (14); Unit 3 Dev (13); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 10.72s (p5 0.54s / p95 507.28s, n=325)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 326/326 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 326/326 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 266 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 5 Dev (106); Unit 4 Dev - Anderson Base (71); Unit 3 Dev (55); Unit 1 Dev (19); Unit 2 Prod (Refactor) (15)
- **Intervals:** median 0.44s (p5 0.03s / p95 24.07s, n=265)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 266/266 records)
    "argumentationNodeHoverEnd"  x105
    "argumentationNodeHoverStart"  x104
    "argumentationNodeAdd"  x37
    "argumentationNodeRemove"  x20
data.argumentationTitle  (string, 266/266 records)
    "Unit 5"  x106
    "Unit 4 - Flooding"  x71
    "Unit 3 - Pollution Upstream"  x55
    "Unit 1 - Freshwater"  x19
    "Unit 2 – Watershed"  x15
data.nodeName  (string, 266/266 records)
    "I"  x40
    "1"  x32
    "B"  x32
    "3"  x27
    "A"  x26
    "C"  x26
    "4"  x24
    "II"  x21
    "D"  x18
    "2"  x15
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 86 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 4 Dev - Dungeon (15); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev (9); Unit 5 Dev - Dungeon (7); Unit 5 Dev (6); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 86 of 86 records
- **Intervals:** median 222.16s (p5 0.01s / p95 73993.79s, n=85)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 86/86 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x36
data.questID  (string, 86/86 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 86/86 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/86 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 68 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dev (34)
- **Intervals:** median 10.66s (p5 0.89s / p95 8887.07s, n=67)
- **`data` key-set variants:** [actionType, featureUsed] x47; [actionType, featureUsed, location] x19; [actionType, featureUsed, legendName] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "MapOpenEvent"  x24
    "MapCloseEvent"  x23
    "WaypointMoveEvent"  x14
    "WaypointSetEvent"  x5
    "Selected"  x2
data.featureUsed  (string, 68/68 records)
    "Map"  x47
    "Waypoint"  x19
    "Legend"  x2
data.legendName  (string, 2/68 records)
    "0 ft"  x1
    "90 ft"  x1
data.location  (object, 19/68 records)
data.location.x  (number, 19/68 records)
    numeric range -348.935 .. 171.25 (19 unique)
data.location.y  (number, 19/68 records)
    numeric range -274.582 .. 261.069 (18 unique)
data.location.z  (number, 19/68 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 66 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (40); Unit 4 Dev (16); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 0.83s (p5 0.15s / p95 262.61s, n=65)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/66 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/66 records)
    "Unit 3 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 58/66 records)
    "RightDrag"  x32
    "LeftDrag"  x26
data.currentSoilType  (string, 58/66 records)
    "CLAY"  x12
    "CLAYSAND"  x12
    "SAND"  x11
    "CLAYROCK"  x10
    "SANDGRAVEL"  x6
    "BEDROCK"  x4
    "GRAVEL"  x3
data.isCorrectSelection  (string, 58/66 records)
    "false"  x45
    "true"  x13
data.waterLevelStatus  (string, 58/66 records)
    "Proper"  x22
    "TooHigh"  x19
    "TooLow"  x17
data.waterRetentionChange  (string, 58/66 records)
    "Decrease"  x24
    "Increase"  x21
    "NoChange"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 43 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (16); Unit 4 Dev - Anderson Base (15); Unit 1 Dev (6); Unit 3 Dev (5); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 21.11s (p5 0.21s / p95 85699.32s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "submitAnswerEvent"  x43
data.answerSubmitted  (string, 43/43 records, 2 empty-string)
    22 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 43/43 records)
    "Unit 5"  x16
    "Unit 4 - Flooding"  x15
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 38 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (6); Unit 3 Dev (5); Unit 4 Dev (4); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 677.01s (p5 8.73s / p95 84802.25s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "DebugMenuStateChanged"  x38
data.isOpened  (bool, 38/38 records)
    false  x38
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 30 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (30)
- **Intervals:** median 5.83s (p5 0.77s / p95 220.49s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "ChangeCanister"  x30
data.canisterType  (string, 30/30 records)
    "Clay"  x12
    "Bedrock"  x9
    "Gravel"  x5
    "Sand"  x4
data.floor  (string, 30/30 records)
    "5"  x21
    "4"  x7
    "3"  x2
data.machine  (string, 30/30 records)
    "1"  x28
    "2"  x2
data.row  (string, 30/30 records)
    "TopRow"  x24
    "BottomRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 27 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (17); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 3 Dungeon Dev (2); Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2011.33s (p5 123.46s / p95 85239.56s, n=26)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 27/27 records)
    true  x27
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 26 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (26)
- **Intervals:** median 26.44s (p5 3.74s / p95 240.23s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "On"  x19
    "Off"  x7
data.floor  (string, 26/26 records)
    "3"  x11
    "4"  x7
    "1"  x4
    "2"  x4
data.machineNumber  (string, 26/26 records)
    "One"  x25
    "Two"  x1
data.machineType  (string, 26/26 records)
    "Condenser"  x11
    "Evaporator"  x9
    "DualChamber_Condenser"  x2
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
data.room  (string, 26/26 records)
    "2"  x14
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 8732.36s (p5 978.06s / p95 162368.23s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 17 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2); Unit 1 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 4580.45s (p5 7.06s / p95 172201.74s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    false  x17
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 153.51s (p5 0.05s / p95 298647.33s, n=13)
- **Open findings:** 2 — see sections 5-8
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

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 19.22s (p5 1.19s / p95 45523.83s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records, 4 empty-string)
    "cameraPlaced"  x6
    ""  x4
data.boxId  (string, 10/10 records)
    "2"  x4
    "0"  x3
    "1"  x3
data.soilType  (string, 10/10 records)
    "Clay"  x3
    "None"  x3
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 9 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev - Dungeon (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 207.95s (p5 2.49s / p95 339223.79s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "Open"  x5
    "Close"  x4
data.toolName  (string, 9/9 records, 9 empty-string)
    ""  x9
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 7 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (7)
- **Intervals:** median 2.04s (p5 0.79s / p95 4.31s, n=6)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x6; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "optionSelected"  x6
    "DesignSubmitted"  x1
data.designSelections  (object, 1/7 records)
data.designSelections.glassRoofTemperature  (string, 1/7 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/7 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/7 records)
    "Tilted Out"  x1
data.featureUsed  (string, 7/7 records)
    "RoofStyle"  x3
    "GlassRoofTemperature"  x2
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 6/7 records, 1 empty-string)
    "Tilted Out"  x2
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 3 Dev (2)
- **Intervals:** median 1.99s (p5 1.61s / p95 587244.72s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 153053.00s (p5 109217.31s / p95 559709.38s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1772.45s (p5 1772.45s / p95 1772.45s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "Permissions check failed"  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records)
    "TypeError: Permissions check failed"  x1
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
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (10 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (14x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (20x)
- `soilMachine` data.canisterType: "Bedrock" (9x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*