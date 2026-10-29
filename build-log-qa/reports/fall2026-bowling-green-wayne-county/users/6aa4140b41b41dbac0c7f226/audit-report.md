# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f226

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f226
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f226.jsonl
- **Records:** 10909 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f226
- **Time span:** 2026-09-23T13:56:16.635000+00:00 .. 2026-10-05T14:11:01.711000+00:00 (288h 14m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f226\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 10909 records, 11 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 105 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3201 | 29.34 | 1 | 4 | 0 | 2026-09-24T13:43:28.448000+00:00 | 2026-10-01T14:01:01.752000+00:00 | 168h 17m |
| InputEvent | 2657 | 24.36 | 1 | 9 | 0 | 2026-09-23T14:00:15.715000+00:00 | 2026-10-05T14:11:01.711000+00:00 | 288h 10m |
| DialogueEvent | 1955 | 17.92 | 1 | 9 | 1235 | 2026-09-23T13:56:58.253000+00:00 | 2026-10-05T14:10:51.199000+00:00 | 288h 13m |
| PlayerPositionEvent | 1914 | 17.55 | 1 | 9 | 0 | 2026-09-23T13:56:36.109000+00:00 | 2026-10-05T14:10:55.669000+00:00 | 288h 14m |
| ObjectInterEvent | 367 | 3.36 | 1 | 9 | 0 | 2026-09-23T14:01:41.137000+00:00 | 2026-10-05T14:11:01.710000+00:00 | 288h 9m |
| argumentationNodeEvent | 356 | 3.26 | 1 | 5 | 0 | 2026-09-23T14:25:05.620000+00:00 | 2026-10-01T14:28:41.047000+00:00 | 192h 3m |
| questEvent | 85 | 0.78 | 1 | 9 | 85 | 2026-09-23T13:56:58.232000+00:00 | 2026-10-05T14:04:08.077000+00:00 | 288h 7m |
| TopographicMapEvent | 68 | 0.62 | 1 | 3 | 0 | 2026-09-24T13:44:32.521000+00:00 | 2026-10-01T13:50:00.326000+00:00 | 168h 5m |
| DaniEvent | 48 | 0.44 | 1 | 5 | 0 | 2026-09-25T14:30:14.987000+00:00 | 2026-10-01T14:18:29.867000+00:00 | 143h 48m |
| Soil Key Puzzle | 48 | 0.44 | 1 | 3 | 0 | 2026-09-24T13:52:10.349000+00:00 | 2026-09-29T14:17:26.833000+00:00 | 120h 25m |
| argumentationAnswerEvent | 36 | 0.33 | 1 | 5 | 0 | 2026-09-23T14:25:44.420000+00:00 | 2026-10-01T14:28:52.557000+00:00 | 192h 3m |
| WaterChamberEvent | 27 | 0.25 | 1 | 1 | 0 | 2026-10-01T13:59:51.882000+00:00 | 2026-10-01T14:19:32.460000+00:00 | 19m 40s |
| gameWindowFocusEvent | 24 | 0.22 | 1 | 7 | 0 | 2026-09-23T13:56:16.635000+00:00 | 2026-10-05T13:49:08.157000+00:00 | 287h 52m |
| chatEvent | 21 | 0.19 | 1 | 6 | 0 | 2026-09-25T14:30:19.522000+00:00 | 2026-10-05T13:48:00.299000+00:00 | 239h 17m |
| DEBUGMenu | 19 | 0.17 | 1 | 8 | 0 | 2026-09-23T13:56:36.101000+00:00 | 2026-10-01T13:56:15.245000+00:00 | 191h 59m |
| gameStartEvent | 15 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:56:16.635000+00:00 | 2026-10-05T13:47:26.113000+00:00 | 287h 51m |
| argumentationEvent | 14 | 0.13 | 1 | 5 | 0 | 2026-09-23T14:22:29.125000+00:00 | 2026-10-01T14:28:52.596000+00:00 | 192h 6m |
| SolarStillDesignEvent | 12 | 0.11 | 1 | 1 | 0 | 2026-10-05T13:53:27.268000+00:00 | 2026-10-05T13:54:01.405000+00:00 | 34.1s |
| argumentationToolEvent | 12 | 0.11 | 1 | 3 | 0 | 2026-09-23T14:24:57.394000+00:00 | 2026-09-28T14:03:31.286000+00:00 | 119h 38m |
| gameWindowUnfocusEvent | 11 | 0.1 | 1 | 6 | 0 | 2026-09-23T14:00:18.737000+00:00 | 2026-10-05T13:49:08.056000+00:00 | 287h 48m |
| TerasGardenBox | 7 | 0.06 | 1 | 1 | 0 | 2026-09-30T14:24:24.937000+00:00 | 2026-09-30T14:25:18.217000+00:00 | 53.3s |
| crash | 6 | 0.06 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 4 | 0.04 | 1 | 4 | 0 | 2026-09-23T14:28:39.575000+00:00 | 2026-10-05T14:11:01.699000+00:00 | 287h 42m |
| soilMachine | 2 | 0.02 | 1 | 1 | 0 | 2026-09-30T14:03:11.232000+00:00 | 2026-09-30T14:03:50.199000+00:00 | 39.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 343622.204s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.171s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.492s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 0.279s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.669s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 11.95s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43154.522s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 533.595s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 42892.368s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 48 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Switch Canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 12 records 
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
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.2x vs baseline. 
  - Observed: 36 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; C,3,II; C,4,II; C,D,3,II 
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
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 10.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-175, 18-176, 18-284, 18-287, 18-289]; [91-70, 91-72, 91-73, 91-79, 91-118]; [95-1, 95-4, 95-5, 95-76, 95-77, 95-78]; [95-60, 95-63, 95-64, 95-66, 95-87, 95-88]; [95-63, 95-64, 95-66, 95-87, 95-88]; [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 24 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 1 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 25 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[144] _id=6ab3dc44485cab4c954cf295 ts=2026-09-23T14:03:47.9440000Z`; `6aa4140b41b41dbac0c7f226.jsonl[215] _id=6ab3ddbd485cab4c954cfeb1 ts=2026-09-23T14:10:05.4880000Z`; `6aa4140b41b41dbac0c7f226.jsonl[261] _id=6ab3dea5485cab4c954d04ed ts=2026-09-23T14:13:57.6910000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[2868] _id=6ab67c90485cab4c95559c98 ts=2026-09-25T13:52:15.5640000Z`; `6aa4140b41b41dbac0c7f226.jsonl[2841] _id=6ab67cfd485cab4c9555a036 ts=2026-09-25T13:54:04.9160000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[36] _id=6ab3da80485cab4c954ce401 ts=2026-09-23T13:56:16.6350000Z`; `6aa4140b41b41dbac0c7f226.jsonl[523] _id=6ab3e26a485cab4c954d3002 ts=2026-09-23T14:30:02.4340000Z`; `6aa4140b41b41dbac0c7f226.jsonl[532] _id=6ab527b8485cab4c95513935 ts=2026-09-24T13:38:00.1480000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[35] _id=6ab3da80485cab4c954ce3ff ts=2026-09-23T13:56:16.6350000Z`; `6aa4140b41b41dbac0c7f226.jsonl[8] _id=6ab3db75485cab4c954ceb29 ts=2026-09-23T14:00:21.5610000Z`; `6aa4140b41b41dbac0c7f226.jsonl[524] _id=6ab3e26a485cab4c954d2ffe ts=2026-09-23T14:30:02.4320000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[7] _id=6ab3db72485cab4c954ceb03 ts=2026-09-23T14:00:18.7370000Z`; `6aa4140b41b41dbac0c7f226.jsonl[679] _id=6ab52874485cab4c95514a0f ts=2026-09-24T13:41:08.1700000Z`; `6aa4140b41b41dbac0c7f226.jsonl[2946] _id=6ab67cb5485cab4c95559dec ts=2026-09-25T13:52:53.8980000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3200 | 0.0 | 0.034 | 189.329 | 1.426 | 258661.07 | 0.32 | 1890 | 7 |
| InputEvent | 2656 | 0.001 | 1.171 | 390.605 | 25.359 | 343149.055 | 0.15 | 37 | 7 |
| DialogueEvent | 1954 | 0.001 | 4.114 | 531.03 | 33.817 | 343099.648 | 0.11 | 556 | 7 |
| PlayerPositionEvent | 1902 | 9.909 | 9.999 | 501.644 | 10.03 | 342969.242 | 0.12 | 0 | 6 |
| ObjectInterEvent | 366 | 0.001 | 6.246 | 2834.319 | 374.433 | 343620.086 | 0.02 | 3 | 13 |
| argumentationNodeEvent | 355 | 0.015 | 0.493 | 1947.649 | 5.647 | 256941.254 | 0.03 | 58 | 5 |
| questEvent | 84 | 0.001 | 181.663 | 12347.974 | 84066.158 | 343072.957 | 0.0 | 18 | 14 |
| TopographicMapEvent | 67 | 0.016 | 4.492 | 9031.758 | 59300.136 | 258108.135 | 0.01 | 2 | 7 |
| DaniEvent | 47 | 0.003 | 2.942 | 11014.785 | 60600.301 | 342514.537 | 0.01 | 4 | 5 |
| Soil Key Puzzle | 47 | 0.18 | 0.784 | 9223.755 | 977.821 | 345464.378 | 0.01 | 0 | 3 |
| argumentationAnswerEvent | 35 | 0.167 | 0.279 | 19753.947 | 173645.724 | 257036.256 | 0.0 | 0 | 4 |
| WaterChamberEvent | 26 | 1.966 | 20.431 | 45.407 | 159.19 | 230.724 | 1.32 | 0 | 0 |
| gameWindowFocusEvent | 23 | 8.982 | 533.595 | 45059.631 | 239056.599 | 343009.669 | 0.0 | 0 | 11 |
| chatEvent | 20 | 1.456 | 11.95 | 43073.039 | 343526.13 | 343653.476 | 0.0 | 0 | 5 |
| DEBUGMenu | 18 | 109.727 | 959.857 | 38398.841 | 112546.904 | 255945.275 | 0.0 | 0 | 11 |
| gameStartEvent | 14 | 106.389 | 43154.522 | 74019.248 | 287141.124 | 345075.447 | 0.0 | 0 | 10 |
| argumentationEvent | 13 | 0.024 | 79.315 | 53198.729 | 206943.667 | 256942.636 | 0.0 | 2 | 4 |
| SolarStillDesignEvent | 11 | 0.527 | 1.643 | 3.103 | 10.143 | 16.172 | 19.33 | 0 | 0 |
| argumentationToolEvent | 11 | 0.127 | 1.669 | 39155.808 | 215329.757 | 257076.288 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 10 | 9.698 | 42892.368 | 103612.932 | 344513.253 | 345723.834 | 0.0 | 0 | 5 |
| TerasGardenBox | 6 | 1.316 | 6.599 | 8.88 | 21.985 | 25.258 | 6.76 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 3 | 173722.522 | 343622.204 | 345247.375 | 500919.879 | 518397.398 | 0.0 | 0 | 3 |
| soilMachine | 1 | 38.967 | 38.967 | 38.967 | 38.967 | 38.967 | 1.54 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 100 group(s), 132 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[878] _id=6ab52916485cab4c95516051 ts=2026-09-24T13:43:48.5590000Z == 6aa4140b41b41dbac0c7f226.jsonl[876] _id=6ab52916485cab4c95516059 ts=2026-09-24T13:43:48.5590000Z`; `6aa4140b41b41dbac0c7f226.jsonl[926] _id=6ab5292d485cab4c95516537 ts=2026-09-24T13:44:12.4960000Z == 6aa4140b41b41dbac0c7f226.jsonl[920] _id=6ab5292d485cab4c95516539 ts=2026-09-24T13:44:12.4960000Z`; `6aa4140b41b41dbac0c7f226.jsonl[933] _id=6ab5292e485cab4c95516550 ts=2026-09-24T13:44:12.5180000Z == 6aa4140b41b41dbac0c7f226.jsonl[927] _id=6ab5292e485cab4c95516554 ts=2026-09-24T13:44:12.5180000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 114 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4140b41b41dbac0c7f226.jsonl[104] _id=6ab3dbc5485cab4c954ced99 ts=2026-09-23T14:01:41.1370000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[105] _id=6ab3dbc5485cab4c954ced9d ts=2026-09-23T14:01:41.1400000Z`; `850ms: 6aa4140b41b41dbac0c7f226.jsonl[603] _id=6ab52861485cab4c955147a7 ts=2026-09-24T13:40:49.3860000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[601] _id=6ab52862485cab4c955147af ts=2026-09-24T13:40:50.2360000Z`; `382ms: 6aa4140b41b41dbac0c7f226.jsonl[601] _id=6ab52862485cab4c955147af ts=2026-09-24T13:40:50.2360000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[593] _id=6ab52862485cab4c955147bd ts=2026-09-24T13:40:50.6180000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 325 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `268ms: 6aa4140b41b41dbac0c7f226.jsonl[908] _id=6ab52927485cab4c95516405 ts=2026-09-24T13:44:06.4150000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[913] _id=6ab52927485cab4c95516409 ts=2026-09-24T13:44:06.6830000Z`; `37ms: 6aa4140b41b41dbac0c7f226.jsonl[1054] _id=6ab529a5485cab4c95517a03 ts=2026-09-24T13:44:11.3710000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[1055] _id=6ab529a5485cab4c95517a05 ts=2026-09-24T13:44:11.4080000Z`; `36ms: 6aa4140b41b41dbac0c7f226.jsonl[932] _id=6ab5292d485cab4c95516533 ts=2026-09-24T13:44:12.4600000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[926] _id=6ab5292d485cab4c95516537 ts=2026-09-24T13:44:12.4960000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `578ms: 6aa4140b41b41dbac0c7f226.jsonl[2740] _id=6ab53075485cab4c9551edd5 ts=2026-09-24T14:15:17.5950000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[2741] _id=6ab53076485cab4c9551edd9 ts=2026-09-24T14:15:18.1730000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `25ms: 6aa4140b41b41dbac0c7f226.jsonl[2408] _id=6ab52cd8485cab4c9551bd23 ts=2026-09-24T13:59:52.5460000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[2416] _id=6ab52cd8485cab4c9551bd31 ts=2026-09-24T13:59:52.5710000Z`; `739ms: 6aa4140b41b41dbac0c7f226.jsonl[5175] _id=6ab68980485cab4c95564f0e ts=2026-09-25T14:47:29.1250000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[5185] _id=6ab68981485cab4c95564f10 ts=2026-09-25T14:47:29.8640000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `222ms: 6aa4140b41b41dbac0c7f226.jsonl[10487] _id=6abe6e1b485cab4c95a88b29 ts=2026-10-01T14:28:43.6400000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[10488] _id=6abe6e1b485cab4c95a88b39 ts=2026-10-01T14:28:43.8620000Z`; `230ms: 6aa4140b41b41dbac0c7f226.jsonl[10488] _id=6abe6e1b485cab4c95a88b39 ts=2026-10-01T14:28:43.8620000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[10496] _id=6abe6e1b485cab4c95a88b46 ts=2026-10-01T14:28:44.0920000Z`; `227ms: 6aa4140b41b41dbac0c7f226.jsonl[10496] _id=6abe6e1b485cab4c95a88b46 ts=2026-10-01T14:28:44.0920000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[10480] _id=6abe6e1c485cab4c95a88b53 ts=2026-10-01T14:28:44.3190000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `24ms: 6aa4140b41b41dbac0c7f226.jsonl[6081] _id=6aba73fa485cab4c956876d3 ts=2026-09-28T14:04:42.8990000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[6061] _id=6aba73fb485cab4c956876e3 ts=2026-09-28T14:04:42.9230000Z`; `48ms: 6aa4140b41b41dbac0c7f226.jsonl[9113] _id=6abd1a78485cab4c958aeb46 ts=2026-09-30T14:19:36.7150000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[9119] _id=6abd1a78485cab4c958aeb4e ts=2026-09-30T14:19:36.7630000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 69 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `597ms: 6aa4140b41b41dbac0c7f226.jsonl[399] _id=6ab3e141485cab4c954d236f ts=2026-09-23T14:25:05.6200000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[402] _id=6ab3e142485cab4c954d2379 ts=2026-09-23T14:25:06.2170000Z`; `741ms: 6aa4140b41b41dbac0c7f226.jsonl[397] _id=6ab3e141485cab4c954d2371 ts=2026-09-23T14:25:05.6490000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[404] _id=6ab3e142485cab4c954d237b ts=2026-09-23T14:25:06.3900000Z`; `835ms: 6aa4140b41b41dbac0c7f226.jsonl[402] _id=6ab3e142485cab4c954d2379 ts=2026-09-23T14:25:06.2170000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[394] _id=6ab3e143485cab4c954d2385 ts=2026-09-23T14:25:07.0520000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `702ms: 6aa4140b41b41dbac0c7f226.jsonl[5984] _id=6aba73b2485cab4c95687235 ts=2026-09-28T14:03:30.5840000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[5986] _id=6aba73b3485cab4c95687240 ts=2026-09-28T14:03:31.2860000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4140b41b41dbac0c7f226.jsonl[2868] _id=6ab67c90485cab4c95559c98 ts=2026-09-25T13:52:15.5640000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[2854] _id=6ab67c90485cab4c95559c9a ts=2026-09-25T13:52:15.5660000Z`; `2ms: 6aa4140b41b41dbac0c7f226.jsonl[2841] _id=6ab67cfd485cab4c9555a036 ts=2026-09-25T13:54:04.9160000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[2842] _id=6ab67cfe485cab4c9555a03a ts=2026-09-25T13:54:04.9180000Z`; `1ms: 6aa4140b41b41dbac0c7f226.jsonl[10561] _id=6abe6e77485cab4c95a8a04b ts=2026-10-01T14:30:15.6780000Z ~ 6aa4140b41b41dbac0c7f226.jsonl[10562] _id=6abe6e77485cab4c95a8a056 ts=2026-10-01T14:30:15.6790000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 5m 
  - Evidence: 71h 5m: 6aa4140b41b41dbac0c7f226.jsonl[5064] _id=6ab688cf485cab4c95564e62 ts=2026-09-25T14:44:32.1270000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5352] _id=6aba7099485cab4c95682479 ts=2026-09-28T13:50:17.4020000Z; 24h 14m: 6aa4140b41b41dbac0c7f226.jsonl[531] _id=6ab527c0485cab4c955139c5 ts=2026-09-24T13:38:08.5300000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2848] _id=6ab67c89485cab4c95559c84 ts=2026-09-25T13:52:09.8390000Z; 23h 41m: 6aa4140b41b41dbac0c7f226.jsonl[37] _id=6ab3da94485cab4c954ce447 ts=2026-09-23T13:56:36.1010000Z -> 6aa4140b41b41dbac0c7f226.jsonl[531] _id=6ab527c0485cab4c955139c5 ts=2026-09-24T13:38:08.5300000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 8m 
  - Evidence: 95h 8m: 6aa4140b41b41dbac0c7f226.jsonl[5172] _id=6ab68967485cab4c95564ef6 ts=2026-09-25T14:47:03.7940000Z -> 6aa4140b41b41dbac0c7f226.jsonl[7009] _id=6abbc35a485cab4c957e0dad ts=2026-09-29T13:55:38.3310000Z; 23h 54m: 6aa4140b41b41dbac0c7f226.jsonl[8273] _id=6abd1448485cab4c958959ef ts=2026-09-30T13:53:12.4890000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9457] _id=6abe6473485cab4c95a6cb51 ts=2026-10-01T13:47:31.2310000Z; 23h 50m: 6aa4140b41b41dbac0c7f226.jsonl[7169] _id=6abbc4c9485cab4c957e33c0 ts=2026-09-29T14:01:45.3330000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8248] _id=6abd1417485cab4c958958b5 ts=2026-09-30T13:52:23.1830000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.003s..0.008s shown 
  - Evidence: 3ms: 6aa4140b41b41dbac0c7f226.jsonl[7082] _id=6abbc3d4485cab4c957e1a13 ts=2026-09-29T13:57:40.8370000Z -> 6aa4140b41b41dbac0c7f226.jsonl[7083] _id=6abbc3d4485cab4c957e1a17 ts=2026-09-29T13:57:40.8400000Z; 4ms: 6aa4140b41b41dbac0c7f226.jsonl[8255] _id=6abd142e485cab4c9589590b ts=2026-09-30T13:52:46.6620000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8256] _id=6abd142e485cab4c9589590d ts=2026-09-30T13:52:46.6660000Z; 8ms: 6aa4140b41b41dbac0c7f226.jsonl[8243] _id=6abd1428485cab4c958958f5 ts=2026-09-30T13:52:40.8430000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8252] _id=6abd1428485cab4c958958f7 ts=2026-09-30T13:52:40.8510000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f226.jsonl[10571] _id=6abe6e7b485cab4c95a8a19e ts=2026-10-01T14:30:19.9600000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10591] _id=6ac3aab7de269131f9a9d214 ts=2026-10-05T13:48:39.6080000Z; 70h 54m: 6aa4140b41b41dbac0c7f226.jsonl[5348] _id=6ab68b93485cab4c955651c8 ts=2026-09-25T14:56:19.7830000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5363] _id=6aba70c9485cab4c95682873 ts=2026-09-28T13:51:05.5060000Z; 23h 35m: 6aa4140b41b41dbac0c7f226.jsonl[2821] _id=6ab530dc485cab4c9551ef33 ts=2026-09-24T14:17:00.6320000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2846] _id=6ab67c90485cab4c95559c94 ts=2026-09-25T13:52:15.5170000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 556 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f226.jsonl[10458] _id=6abe6e03485cab4c95a88715 ts=2026-10-01T14:28:20.1760000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10459] _id=6abe6e04485cab4c95a88719 ts=2026-10-01T14:28:20.1770000Z; 1ms: 6aa4140b41b41dbac0c7f226.jsonl[10469] _id=6abe6e11485cab4c95a88923 ts=2026-10-01T14:28:33.8670000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10474] _id=6abe6e11485cab4c95a88927 ts=2026-10-01T14:28:33.8680000Z; 1ms: 6aa4140b41b41dbac0c7f226.jsonl[10528] _id=6abe6e54485cab4c95a898d6 ts=2026-10-01T14:29:40.1640000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10529] _id=6abe6e54485cab4c95a898e0 ts=2026-10-01T14:29:40.1650000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6aa4140b41b41dbac0c7f226.jsonl[7278] _id=6abbc6f8485cab4c957e6589 ts=2026-09-29T14:11:04.3010000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10899] _id=6ac3aff5de269131f9aad73d ts=2026-10-05T14:11:01.6990000Z; 95h 27m: 6aa4140b41b41dbac0c7f226.jsonl[5133] _id=6ab688b1485cab4c95564e56 ts=2026-09-25T14:44:02.0970000Z -> 6aa4140b41b41dbac0c7f226.jsonl[7278] _id=6abbc6f8485cab4c957e6589 ts=2026-09-29T14:11:04.3010000Z; 48h 15m: 6aa4140b41b41dbac0c7f226.jsonl[521] _id=6ab3e217485cab4c954d2c39 ts=2026-09-23T14:28:39.5750000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5133] _id=6ab688b1485cab4c95564e56 ts=2026-09-25T14:44:02.0970000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa4140b41b41dbac0c7f226.jsonl[10553] _id=6abe6e8c485cab4c95a8a621 ts=2026-10-01T14:30:36.4890000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10612] _id=6ac3aaf9de269131f9a9dfd1 ts=2026-10-05T13:49:45.5440000Z; 70h 55m: 6aa4140b41b41dbac0c7f226.jsonl[5325] _id=6ab68b3d485cab4c95565168 ts=2026-09-25T14:54:53.4600000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5357] _id=6aba70ae485cab4c9568261b ts=2026-09-28T13:50:38.6080000Z; 23h 35m: 6aa4140b41b41dbac0c7f226.jsonl[2802] _id=6ab530c9485cab4c9551ef0b ts=2026-09-24T14:16:41.5480000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2911] _id=6ab67ca7485cab4c95559d20 ts=2026-09-25T13:52:39.4120000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 37 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f226.jsonl[6347] _id=6aba7678485cab4c9568abe5 ts=2026-09-28T14:15:20.7500000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6348] _id=6aba7679485cab4c9568abe7 ts=2026-09-28T14:15:20.7510000Z; 1ms: 6aa4140b41b41dbac0c7f226.jsonl[6348] _id=6aba7679485cab4c9568abe7 ts=2026-09-28T14:15:20.7510000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6349] _id=6aba7679485cab4c9568abe9 ts=2026-09-28T14:15:20.7520000Z; 1ms: 6aa4140b41b41dbac0c7f226.jsonl[6349] _id=6aba7679485cab4c9568abe9 ts=2026-09-28T14:15:20.7520000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6350] _id=6aba7679485cab4c9568abed ts=2026-09-28T14:15:20.7530000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 27m 
  - Evidence: 95h 27m: 6aa4140b41b41dbac0c7f226.jsonl[10365] _id=6abe6d89485cab4c95a86975 ts=2026-10-01T14:26:17.3320000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10669] _id=6ac3abcdde269131f9aa0e68 ts=2026-10-05T13:53:17.4180000Z; 71h 0m: 6aa4140b41b41dbac0c7f226.jsonl[5291] _id=6ab68acc485cab4c955650e0 ts=2026-09-25T14:53:00.6010000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5427] _id=6aba7171485cab4c95683da3 ts=2026-09-28T13:53:53.6910000Z; 23h 41m: 6aa4140b41b41dbac0c7f226.jsonl[2712] _id=6ab53063485cab4c9551ecf9 ts=2026-09-24T14:14:59.3150000Z -> 6aa4140b41b41dbac0c7f226.jsonl[3157] _id=6ab67d92485cab4c9555a748 ts=2026-09-25T13:56:34.4120000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f226.jsonl[8997] _id=6abd19a9485cab4c958ac8c8 ts=2026-09-30T14:16:08.8200000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8998] _id=6abd19a9485cab4c958ac8ce ts=2026-09-30T14:16:08.8210000Z; 2ms: 6aa4140b41b41dbac0c7f226.jsonl[8965] _id=6abd1971485cab4c958abbc1 ts=2026-09-30T14:15:13.3590000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8963] _id=6abd1971485cab4c958abbc9 ts=2026-09-30T14:15:13.3610000Z; 3ms: 6aa4140b41b41dbac0c7f226.jsonl[104] _id=6ab3dbc5485cab4c954ced99 ts=2026-09-23T14:01:41.1370000Z -> 6aa4140b41b41dbac0c7f226.jsonl[105] _id=6ab3dbc5485cab4c954ced9d ts=2026-09-23T14:01:41.1400000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa4140b41b41dbac0c7f226.jsonl[10578] _id=6abe6ed7485cab4c95a8b45a ts=2026-10-01T14:31:51.1390000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10583] _id=6ac3aa99de269131f9a9caef ts=2026-10-05T13:48:00.3810000Z; 70h 53m: 6aa4140b41b41dbac0c7f226.jsonl[5349] _id=6ab68b98485cab4c955651ce ts=2026-09-25T14:56:24.4330000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5355] _id=6aba709e485cab4c956824ed ts=2026-09-28T13:50:17.4100000Z; 23h 34m: 6aa4140b41b41dbac0c7f226.jsonl[2837] _id=6ab5311b485cab4c9551ef71 ts=2026-09-24T14:18:02.9600000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2845] _id=6ab67c8f485cab4c95559c92 ts=2026-09-25T13:52:09.8440000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 51m 
  - Evidence: 71h 51m: 6aa4140b41b41dbac0c7f226.jsonl[4707] _id=6ab68405485cab4c955636ba ts=2026-09-25T14:24:04.4960000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6341] _id=6aba766a485cab4c9568a98f ts=2026-09-28T14:15:05.5660000Z; 24h 0m: 6aa4140b41b41dbac0c7f226.jsonl[6529] _id=6aba76eb485cab4c9568baad ts=2026-09-28T14:17:11.3990000Z -> 6aa4140b41b41dbac0c7f226.jsonl[7408] _id=6abbc879485cab4c957e8413 ts=2026-09-29T14:17:29.1280000Z; 23h 45m: 6aa4140b41b41dbac0c7f226.jsonl[7731] _id=6abbc8f9485cab4c957e963b ts=2026-09-29T14:19:35.0040000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8698] _id=6abd1705485cab4c9589ef91 ts=2026-09-30T14:04:52.4060000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1890 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f226.jsonl[1008] _id=6ab529a8485cab4c95517af5 ts=2026-09-24T13:45:53.4540000Z -> 6aa4140b41b41dbac0c7f226.jsonl[1009] _id=6ab529a9485cab4c95517af7 ts=2026-09-24T13:45:53.4540000Z; 0ms: 6aa4140b41b41dbac0c7f226.jsonl[1014] _id=6ab529a2485cab4c95517979 ts=2026-09-24T13:44:08.3820000Z -> 6aa4140b41b41dbac0c7f226.jsonl[1027] _id=6ab529a2485cab4c9551797d ts=2026-09-24T13:44:08.3820000Z; 0ms: 6aa4140b41b41dbac0c7f226.jsonl[1033] _id=6ab529a3485cab4c955179ab ts=2026-09-24T13:44:08.9990000Z -> 6aa4140b41b41dbac0c7f226.jsonl[1036] _id=6ab529a3485cab4c955179af ts=2026-09-24T13:44:08.9990000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4140b41b41dbac0c7f226.jsonl[2745] _id=6ab5307b485cab4c9551ee01 ts=2026-09-24T14:15:23.2920000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6307] _id=6aba75f3485cab4c9568a13d ts=2026-09-28T14:13:07.6700000Z; 24h 2m: 6aa4140b41b41dbac0c7f226.jsonl[6329] _id=6aba7645485cab4c9568a6d3 ts=2026-09-28T14:14:29.8840000Z -> 6aa4140b41b41dbac0c7f226.jsonl[7387] _id=6abbc869485cab4c957e821d ts=2026-09-29T14:17:13.8370000Z; 22m 45s: 6aa4140b41b41dbac0c7f226.jsonl[2271] _id=6ab52b0d485cab4c95519d21 ts=2026-09-24T13:52:13.3270000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2711] _id=6ab53063485cab4c9551ecf5 ts=2026-09-24T14:14:59.3080000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 41m 
  - Evidence: 71h 41m: 6aa4140b41b41dbac0c7f226.jsonl[5207] _id=6ab68a0f485cab4c95564fc6 ts=2026-09-25T14:49:51.2780000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6951] _id=6aba7a4b485cab4c9568f24f ts=2026-09-28T14:31:39.4130000Z; 47h 47m: 6aa4140b41b41dbac0c7f226.jsonl[7172] _id=6abbc4ce485cab4c957e3477 ts=2026-09-29T14:01:50.1990000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9508] _id=6abe64ec485cab4c95a6ee99 ts=2026-10-01T13:49:32.3020000Z; 24h 5m: 6aa4140b41b41dbac0c7f226.jsonl[2511] _id=6ab52e26485cab4c9551ce9f ts=2026-09-24T14:05:26.5940000Z -> 6aa4140b41b41dbac0c7f226.jsonl[4309] _id=6ab680ec485cab4c9555d6ea ts=2026-09-25T14:10:53.0110000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.016s..0.025s shown 
  - Evidence: 16ms: 6aa4140b41b41dbac0c7f226.jsonl[2410] _id=6ab52cd8485cab4c9551bd1f ts=2026-09-24T13:59:52.5300000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2408] _id=6ab52cd8485cab4c9551bd23 ts=2026-09-24T13:59:52.5460000Z; 25ms: 6aa4140b41b41dbac0c7f226.jsonl[2408] _id=6ab52cd8485cab4c9551bd23 ts=2026-09-24T13:59:52.5460000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2416] _id=6ab52cd8485cab4c9551bd31 ts=2026-09-24T13:59:52.5710000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 23m 
  - Evidence: 71h 23m: 6aa4140b41b41dbac0c7f226.jsonl[4991] _id=6ab687a7485cab4c95564d9e ts=2026-09-25T14:39:35.7270000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5980] _id=6aba73b4485cab4c95687247 ts=2026-09-28T14:03:31.9830000Z; 48h 14m: 6aa4140b41b41dbac0c7f226.jsonl[6075] _id=6aba73fa485cab4c956876d1 ts=2026-09-28T14:04:42.8850000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9098] _id=6abd1a6a485cab4c958ae924 ts=2026-09-30T14:19:22.2500000Z; 48h 13m: 6aa4140b41b41dbac0c7f226.jsonl[428] _id=6ab3e168485cab4c954d257b ts=2026-09-23T14:25:44.4200000Z -> 6aa4140b41b41dbac0c7f226.jsonl[4991] _id=6ab687a7485cab4c95564d9e ts=2026-09-25T14:39:35.7270000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 22m 
  - Evidence: 71h 22m: 6aa4140b41b41dbac0c7f226.jsonl[5053] _id=6ab687a7485cab4c95564da0 ts=2026-09-25T14:39:35.7450000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5862] _id=6aba7356485cab4c95686c9d ts=2026-09-28T14:01:58.3810000Z; 48h 13m: 6aa4140b41b41dbac0c7f226.jsonl[6061] _id=6aba73fb485cab4c956876e3 ts=2026-09-28T14:04:42.9230000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9037] _id=6abd1a25485cab4c958adf4c ts=2026-09-30T14:18:13.9440000Z; 48h 12m: 6aa4140b41b41dbac0c7f226.jsonl[429] _id=6ab3e168485cab4c954d257d ts=2026-09-23T14:25:44.4400000Z -> 6aa4140b41b41dbac0c7f226.jsonl[4979] _id=6ab68770485cab4c95564d30 ts=2026-09-25T14:38:40.7120000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.024s..0.048s shown 
  - Evidence: 24ms: 6aa4140b41b41dbac0c7f226.jsonl[6081] _id=6aba73fa485cab4c956876d3 ts=2026-09-28T14:04:42.8990000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6061] _id=6aba73fb485cab4c956876e3 ts=2026-09-28T14:04:42.9230000Z; 48ms: 6aa4140b41b41dbac0c7f226.jsonl[9113] _id=6abd1a78485cab4c958aeb46 ts=2026-09-30T14:19:36.7150000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9119] _id=6abd1a78485cab4c958aeb4e ts=2026-09-30T14:19:36.7630000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 71h 22m 
  - Evidence: 71h 22m: 6aa4140b41b41dbac0c7f226.jsonl[5052] _id=6ab687a4485cab4c95564d9c ts=2026-09-25T14:39:32.9450000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5539] _id=6aba7352485cab4c95686c3d ts=2026-09-28T14:01:54.1990000Z; 48h 4m: 6aa4140b41b41dbac0c7f226.jsonl[423] _id=6ab3e160485cab4c954d2517 ts=2026-09-23T14:25:36.3410000Z -> 6aa4140b41b41dbac0c7f226.jsonl[4912] _id=6ab68589485cab4c95564ada ts=2026-09-25T14:30:34.1760000Z; 24h 21m: 6aa4140b41b41dbac0c7f226.jsonl[7076] _id=6abbc3b9485cab4c957e1779 ts=2026-09-29T13:57:13.0100000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9043] _id=6abd1a2f485cab4c958ae0c6 ts=2026-09-30T14:18:23.3810000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 58 interval(s) ≤ 0.015s..0.019s shown 
  - Evidence: 15ms: 6aa4140b41b41dbac0c7f226.jsonl[9048] _id=6abd1a34485cab4c958ae178 ts=2026-09-30T14:18:28.0280000Z -> 6aa4140b41b41dbac0c7f226.jsonl[9045] _id=6abd1a34485cab4c958ae17c ts=2026-09-30T14:18:28.0430000Z; 16ms: 6aa4140b41b41dbac0c7f226.jsonl[6019] _id=6aba73d1485cab4c9568744d ts=2026-09-28T14:04:01.7240000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6009] _id=6aba73d1485cab4c9568744f ts=2026-09-28T14:04:01.7400000Z; 19ms: 6aa4140b41b41dbac0c7f226.jsonl[4863] _id=6ab6858d485cab4c95564aec ts=2026-09-25T14:30:37.2990000Z -> 6aa4140b41b41dbac0c7f226.jsonl[4915] _id=6ab6858d485cab4c95564aee ts=2026-09-25T14:30:37.3180000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 71h 24m 
  - Evidence: 71h 24m: 6aa4140b41b41dbac0c7f226.jsonl[4981] _id=6ab68774485cab4c95564d38 ts=2026-09-25T14:38:44.3090000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5977] _id=6aba73a8485cab4c9568714f ts=2026-09-28T14:03:20.5970000Z; 48h 13m: 6aa4140b41b41dbac0c7f226.jsonl[413] _id=6ab3e165485cab4c954d2555 ts=2026-09-23T14:25:41.0830000Z -> 6aa4140b41b41dbac0c7f226.jsonl[4981] _id=6ab68774485cab4c95564d38 ts=2026-09-25T14:38:44.3090000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 27m 
  - Evidence: 95h 27m: 6aa4140b41b41dbac0c7f226.jsonl[10264] _id=6abe6c2a485cab4c95a80f26 ts=2026-10-01T14:20:26.8230000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10582] _id=6ac3aa90de269131f9a9c915 ts=2026-10-05T13:48:00.2990000Z; 95h 25m: 6aa4140b41b41dbac0c7f226.jsonl[4903] _id=6ab6857c485cab4c95564a9a ts=2026-09-25T14:30:20.9780000Z -> 6aa4140b41b41dbac0c7f226.jsonl[7012] _id=6abbc35c485cab4c957e0ddd ts=2026-09-29T13:55:40.4060000Z; 23h 55m: 6aa4140b41b41dbac0c7f226.jsonl[7021] _id=6abbc3be485cab4c957e17e7 ts=2026-09-29T13:57:18.1640000Z -> 6aa4140b41b41dbac0c7f226.jsonl[8250] _id=6abd141b485cab4c958958c1 ts=2026-09-30T13:52:27.1520000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 51m 
  - Evidence: 95h 51m: 6aa4140b41b41dbac0c7f226.jsonl[9642] _id=6abe667a485cab4c95a758bb ts=2026-10-01T13:56:10.6660000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10581] _id=6ac3aa6ede269131f9a9c5d8 ts=2026-10-05T13:47:26.1130000Z; 71h 5m: 6aa4140b41b41dbac0c7f226.jsonl[5134] _id=6ab688c5485cab4c95564e60 ts=2026-09-25T14:44:21.5990000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5351] _id=6aba708f485cab4c956822f9 ts=2026-09-28T13:50:07.3180000Z; 24h 14m: 6aa4140b41b41dbac0c7f226.jsonl[532] _id=6ab527b8485cab4c95513935 ts=2026-09-24T13:38:00.1480000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2844] _id=6ab67c83485cab4c95559c80 ts=2026-09-25T13:52:03.8800000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa4140b41b41dbac0c7f226.jsonl[10554] _id=6abe6e8c485cab4c95a8a61b ts=2026-10-01T14:30:36.4430000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10580] _id=6ac3aa6ede269131f9a9c5c9 ts=2026-10-05T13:47:26.1120000Z; 71h 5m: 6aa4140b41b41dbac0c7f226.jsonl[5120] _id=6ab688c5485cab4c95564e5e ts=2026-09-25T14:44:21.5980000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5350] _id=6aba708f485cab4c956822ef ts=2026-09-28T13:50:07.3170000Z; 24h 10m: 6aa4140b41b41dbac0c7f226.jsonl[686] _id=6ab52875485cab4c95514a2d ts=2026-09-24T13:41:09.3630000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2847] _id=6ab67c83485cab4c95559c7e ts=2026-09-25T13:52:03.8790000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 2m 
  - Evidence: 96h 2m: 6aa4140b41b41dbac0c7f226.jsonl[2946] _id=6ab67cb5485cab4c95559dec ts=2026-09-25T13:52:53.8980000Z -> 6aa4140b41b41dbac0c7f226.jsonl[6990] _id=6abbc331485cab4c957e0ad5 ts=2026-09-29T13:54:57.7320000Z; 95h 17m: 6aa4140b41b41dbac0c7f226.jsonl[10579] _id=6abe6eda485cab4c95a8b4d6 ts=2026-10-01T14:31:54.4010000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10598] _id=6ac3aad4de269131f9a9d7c6 ts=2026-10-05T13:49:08.0560000Z; 48h 19m: 6aa4140b41b41dbac0c7f226.jsonl[6990] _id=6abbc331485cab4c957e0ad5 ts=2026-09-29T13:54:57.7320000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10138] _id=6abe6ad3485cab4c95a7c081 ts=2026-10-01T14:14:43.0470000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4140b41b41dbac0c7f226.jsonl[10562] _id=6abe6e77485cab4c95a8a056 ts=2026-10-01T14:30:15.6790000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10585] _id=6ac3aa99de269131f9a9cafc ts=2026-10-05T13:48:08.6360000Z; 70h 55m: 6aa4140b41b41dbac0c7f226.jsonl[5329] _id=6ab68b59485cab4c95565186 ts=2026-09-25T14:55:21.5460000Z -> 6aa4140b41b41dbac0c7f226.jsonl[5353] _id=6aba709e485cab4c956824f1 ts=2026-09-28T13:50:22.3310000Z; 23h 37m: 6aa4140b41b41dbac0c7f226.jsonl[2707] _id=6ab5305b485cab4c9551ec57 ts=2026-09-24T14:14:51.4750000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2868] _id=6ab67c90485cab4c95559c98 ts=2026-09-25T13:52:15.5640000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f226.jsonl[10561] _id=6abe6e77485cab4c95a8a04b ts=2026-10-01T14:30:15.6780000Z -> 6aa4140b41b41dbac0c7f226.jsonl[10562] _id=6abe6e77485cab4c95a8a056 ts=2026-10-01T14:30:15.6790000Z; 2ms: 6aa4140b41b41dbac0c7f226.jsonl[2841] _id=6ab67cfd485cab4c9555a036 ts=2026-09-25T13:54:04.9160000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2842] _id=6ab67cfe485cab4c9555a03a ts=2026-09-25T13:54:04.9180000Z; 2ms: 6aa4140b41b41dbac0c7f226.jsonl[2868] _id=6ab67c90485cab4c95559c98 ts=2026-09-25T13:52:15.5640000Z -> 6aa4140b41b41dbac0c7f226.jsonl[2854] _id=6ab67c90485cab4c95559c9a ts=2026-09-25T13:52:15.5660000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[332] _id=6ab3e041485cab4c954d180f ts=2026-09-23T14:20:49.8610000Z`; `6aa4140b41b41dbac0c7f226.jsonl[439] _id=6ab3e17d485cab4c954d2629 ts=2026-09-23T14:26:05.0580000Z`; `6aa4140b41b41dbac0c7f226.jsonl[2510] _id=6ab52e23485cab4c9551ce85 ts=2026-09-24T14:05:23.5350000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 68 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[1210] _id=6ab529bd485cab4c95517dc5 ts=2026-09-24T13:46:36.5480000Z`; `6aa4140b41b41dbac0c7f226.jsonl[1445] _id=6ab529f7485cab4c95518681 ts=2026-09-24T13:47:34.6610000Z`; `6aa4140b41b41dbac0c7f226.jsonl[1524] _id=6ab52a15485cab4c95518a8b ts=2026-09-24T13:48:04.7300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 140 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[908] _id=6ab52927485cab4c95516405 ts=2026-09-24T13:44:06.4150000Z`; `6aa4140b41b41dbac0c7f226.jsonl[913] _id=6ab52927485cab4c95516409 ts=2026-09-24T13:44:06.6830000Z`; `6aa4140b41b41dbac0c7f226.jsonl[1055] _id=6ab529a5485cab4c95517a05 ts=2026-09-24T13:44:11.4080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[6061] _id=6aba73fb485cab4c956876e3 ts=2026-09-28T14:04:42.9230000Z`; `6aa4140b41b41dbac0c7f226.jsonl[9119] _id=6abd1a78485cab4c958aeb4e ts=2026-09-30T14:19:36.7630000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[10486] _id=6abe6e18485cab4c95a88a93 ts=2026-10-01T14:28:41.0470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[9645] _id=6abe667f485cab4c95a759b1 ts=2026-10-01T13:56:15.1470000Z`; `6aa4140b41b41dbac0c7f226.jsonl[10264] _id=6abe6c2a485cab4c95a80f26 ts=2026-10-01T14:20:26.8230000Z`; `6aa4140b41b41dbac0c7f226.jsonl[10582] _id=6ac3aa90de269131f9a9c915 ts=2026-10-05T13:48:00.2990000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[8087] _id=6abd12c0485cab4c95893607 ts=2026-09-30T13:46:39.9920000Z`; `6aa4140b41b41dbac0c7f226.jsonl[8227] _id=6abd1472485cab4c95895b71 ts=2026-09-30T13:53:54.1840000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[38] _id=6ab3da99485cab4c954ce45d ts=?`; `6aa4140b41b41dbac0c7f226.jsonl[533] _id=6ab527c6485cab4c95513a07 ts=?`; `6aa4140b41b41dbac0c7f226.jsonl[2955] _id=6ab67cfc485cab4c9555a01c ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 389 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[1143] _id=6ab529ac485cab4c95517b87 ts=2026-09-24T13:46:20.4340000Z`; `6aa4140b41b41dbac0c7f226.jsonl[1217] _id=6ab529bd485cab4c95517dc9 ts=2026-09-24T13:46:37.0160000Z`; `6aa4140b41b41dbac0c7f226.jsonl[1250] _id=6ab529c9485cab4c95517fa5 ts=2026-09-24T13:46:48.9920000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 652 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[862] _id=6ab52915485cab4c95516021 ts=2026-09-24T13:43:48.3650000Z`; `6aa4140b41b41dbac0c7f226.jsonl[871] _id=6ab52915485cab4c95516031 ts=2026-09-24T13:43:48.4320000Z`; `6aa4140b41b41dbac0c7f226.jsonl[872] _id=6ab52915485cab4c95516035 ts=2026-09-24T13:43:48.4820000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 17 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[2408] _id=6ab52cd8485cab4c9551bd23 ts=2026-09-24T13:59:52.5460000Z`; `6aa4140b41b41dbac0c7f226.jsonl[2416] _id=6ab52cd8485cab4c9551bd31 ts=2026-09-24T13:59:52.5710000Z`; `6aa4140b41b41dbac0c7f226.jsonl[2466] _id=6ab52d8e485cab4c9551c8f5 ts=2026-09-24T14:02:54.3600000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[411] _id=6ab3e161485cab4c954d2523 ts=2026-09-23T14:25:37.8380000Z`; `6aa4140b41b41dbac0c7f226.jsonl[412] _id=6ab3e163485cab4c954d253d ts=2026-09-23T14:25:39.6340000Z`; `6aa4140b41b41dbac0c7f226.jsonl[5982] _id=6aba73ac485cab4c956871bd ts=2026-09-28T14:03:24.1960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 363 start, 357 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 89 unmatched 'BecameCameraCentered' (totals: 618 open, 597 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 92 unmatched 'BecameVisible' (totals: 969 open, 1017 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 19 open, 17 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 10 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 49 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 208 of 10902 adjacent _id pairs reverse in client time; worst 159.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f226.jsonl[990] _id=6ab529a0485cab4c955178db ts=2026-09-24T13:46:08.2630000Z`; `6aa4140b41b41dbac0c7f226.jsonl[994] _id=6ab529a1485cab4c95517901 ts=2026-09-24T13:43:28.4480000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -160.84s, max +0.29s over 10903 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f226\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 6 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3201 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2387); Unit 4 Dev (460); Unit 5 Dev - Dungeon (210); Unit 3 Dungeon Dev (144)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.43s, n=3200)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3201/3201 records)
    "BecameInvisible"  x1017
    "BecameVisible"  x969
    "BecameCameraCentered"  x618
    "BecameCameraUncentered"  x597
data.pieceId  (string, 3201/3201 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3201/3201 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2657 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (851); Unit 3 Dev (657); Unit 4 Dev - Dungeon (392); Unit 4 Dev (215); Unit 3 Dungeon Dev (186); Unit 5 Dev - Dungeon (134); Unit 5 Dev (91); Unit 1 Dev (73); Unit 4 Dev - Anderson Base (58)
- **Intervals:** median 1.17s (p5 0.13s / p95 25.36s, n=2656)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2657/2657 records)
    "pressed"  x2657
data.actionType  (string, 2657/2657 records)
    "Move"  x1822
    "Interact"  x543
    "Jump"  x168
    "Ascend"  x66
    "Hoverboard"  x37
    "Pause"  x14
    "Sprint"  x6
    "Map"  x1
data.key  (string, 2657/2657 records, 7 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2657/2657 records)
    "Player"  x1968
    "Drone"  x689
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1955 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (538); Unit 3 Dev (319); Unit 4 Dev (257); Unit 5 Dev (219); Unit 1 Dev (196); Unit 4 Dev - Dungeon (151); Unit 3 Dungeon Dev (116); Unit 5 Dev - Dungeon (83); Unit 4 Dev - Anderson Base (76)
- **eventKey:** present on 1235 of 1955 records
- **Intervals:** median 4.11s (p5 0.00s / p95 33.82s, n=1954)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1235; [conversationId, dialogueEventType] x720
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1955/1955 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 1955/1955 records)
    "DialogueNodeEvent"  x1235
    "DialogueStartEvent"  x363
    "DialogueFinishEvent"  x357
data.nodeId  (number, 1235/1955 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1914 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (523); Unit 3 Dev (323); Unit 4 Dev (234); Unit 5 Dev (194); Unit 1 Dev (192); Unit 4 Dev - Dungeon (176); Unit 5 Dev - Dungeon (140); Unit 3 Dungeon Dev (89); Unit 4 Dev - Anderson Base (43)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1902)
- **Fields under `data`:**

```text
data.position  (object, 1914/1914 records)
data.position.x  (number, 1914/1914 records)
    numeric range -700.433 .. 1733.44 (678 unique)
data.position.y  (number, 1914/1914 records)
    numeric range -114.326 .. 222.007 (485 unique)
data.position.z  (number, 1914/1914 records)
    numeric range -1309.34 .. 2021 (678 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 367 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (155); Unit 4 Dev - Dungeon (108); Unit 3 Dungeon Dev (31); Unit 4 Dev (20); Unit 5 Dev (16); Unit 3 Dev (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (7)
- **Intervals:** median 6.25s (p5 0.17s / p95 374.43s, n=366)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 367/367 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 367/367 records)
    99 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 356 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (153); Unit 4 Dev - Anderson Base (61); Unit 5 Dev (60); Unit 2 Prod (Refactor) (59); Unit 1 Dev (23)
- **Intervals:** median 0.49s (p5 0.02s / p95 5.65s, n=355)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 356/356 records)
    "argumentationNodeHoverEnd"  x164
    "argumentationNodeHoverStart"  x163
    "argumentationNodeAdd"  x23
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 356/356 records)
    "Unit 3 - Pollution Upstream"  x153
    "Unit 4 - Flooding"  x61
    "Unit 5"  x60
    "Unit 2 – Watershed"  x59
    "Unit 1 - Freshwater"  x23
data.nodeName  (string, 356/356 records)
    "B"  x44
    "II"  x43
    "4"  x40
    "3"  x39
    "A"  x38
    "1"  x34
    "I"  x28
    "2"  x27
    "D"  x24
    "C"  x20
    "5"  x19
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 85 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (17); Unit 2 Prod (Refactor) (16); Unit 1 Dev (12); Unit 3 Dev (12); Unit 5 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 85 of 85 records
- **Intervals:** median 181.66s (p5 0.00s / p95 84066.16s, n=84)
- **`data` key-set variants:** [questEventType, questID, questName] x49; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 85/85 records)
    "questActiveEvent"  x49
    "questFinishEvent"  x36
data.questID  (string, 85/85 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 85/85 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/85 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 68 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (39); Unit 2 Prod (Refactor) (22); Unit 4 Dev (7)
- **Intervals:** median 4.49s (p5 0.57s / p95 59300.14s, n=67)
- **`data` key-set variants:** [actionType, featureUsed] x36; [actionType, featureUsed, location] x32
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "WaypointMoveEvent"  x24
    "MapOpenEvent"  x19
    "MapCloseEvent"  x17
    "WaypointSetEvent"  x6
    "WaypointResetEvent"  x2
data.featureUsed  (string, 68/68 records)
    "Map"  x36
    "Waypoint"  x32
data.location  (object, 32/68 records)
data.location.x  (number, 32/68 records)
    numeric range -280.09 .. 204.701 (24 unique)
data.location.y  (number, 32/68 records)
    numeric range -355.733 .. 314.5 (28 unique)
data.location.z  (number, 32/68 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DaniEvent` — 48 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (22); Unit 4 Dev - Dungeon (10); Unit 2 Prod (Refactor) (8); Unit 4 Dev (6); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 2.94s (p5 0.01s / p95 60600.30s, n=47)
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "Close"  x24
    "Open"  x24
data.toolName  (string, 48/48 records, 44 empty-string)
    ""  x44
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `Soil Key Puzzle` — 48 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (14); Unit 4 Dev (12)
- **Intervals:** median 0.78s (p5 0.20s / p95 977.82s, n=47)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x40; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/48 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/48 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 40/48 records)
    "RightDrag"  x23
    "LeftDrag"  x17
data.currentSoilType  (string, 40/48 records)
    "CLAYSAND"  x8
    "SAND"  x8
    "CLAY"  x7
    "SANDGRAVEL"  x7
    "CLAYROCK"  x5
    "GRAVEL"  x4
    "BEDROCK"  x1
data.isCorrectSelection  (string, 40/48 records)
    "false"  x33
    "true"  x7
data.waterLevelStatus  (string, 40/48 records)
    "TooHigh"  x15
    "TooLow"  x14
    "Proper"  x11
data.waterRetentionChange  (string, 40/48 records)
    "Decrease"  x19
    "Increase"  x14
    "NoChange"  x7
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 36 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (27); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 0.28s (p5 0.17s / p95 173645.72s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "submitAnswerEvent"  x36
data.answerSubmitted  (string, 36/36 records)
    "C,D,3,II"  x25
    "A,1,I"  x2
    "A,3,I"  x2
    "A,C,D,2,II"  x2
    "A,1,II"  x1
    "A,2,II"  x1
    "A,5,I"  x1
    "C,3,II"  x1
    "C,4,II"  x1
data.argumentationTitle  (string, 36/36 records)
    "Unit 5"  x27
    "Unit 3 - Pollution Upstream"  x4
    "Unit 4 - Flooding"  x3
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 27 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (27)
- **Intervals:** median 20.43s (p5 3.72s / p95 159.19s, n=26)
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "On"  x19
    "Off"  x8
data.floor  (string, 27/27 records)
    "4"  x14
    "3"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 27/27 records)
    "One"  x26
    "Two"  x1
data.machineType  (string, 27/27 records)
    "Condenser"  x14
    "Evaporator"  x8
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 27/27 records)
    "3"  x13
    "2"  x8
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 24 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 5 Dev (4); Transition (1); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 533.60s (p5 61.77s / p95 239056.60s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `chatEvent` — 21 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (9); Unit 3 Dev (4); Unit 2 Prod (Refactor) (2); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev (2)
- **Intervals:** median 11.95s (p5 1.69s / p95 343526.13s, n=20)
- **`data` key-set variants:** [actionType, chatID] x19; [actionKey, chatID] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/21 records)
    "ScrollStop"  x2
data.actionType  (string, 19/21 records)
    "Close"  x10
    "Open"  x7
    "ScrollStart"  x2
data.chatID  (string, 21/21 records)
    "NA"  x12
    "[]"  x3
    "[95-63, 95-64, 95-66, 95-87, 95-88]"  x2
    "[18-175, 18-176, 18-284, 18-287, 18-289]"  x1
    "[91-70, 91-72, 91-73, 91-79, 91-118]"  x1
    "[95-1, 95-4, 95-5, 95-76, 95-77, 95-78]"  x1
    "[95-60, 95-63, 95-64, 95-66, 95-87, 95-88]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `DEBUGMenu` — 19 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (5); Unit 3 Dev (4); Unit 2 Prod (Refactor) (3); Unit 4 Dev - Dungeon (3); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 959.86s (p5 250.75s / p95 112546.90s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "DebugMenuStateChanged"  x19
data.isOpened  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 43154.52s (p5 217.47s / p95 287141.12s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 79.31s (p5 0.04s / p95 206943.67s, n=13)
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

### `SolarStillDesignEvent` — 12 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (12)
- **Intervals:** median 1.64s (p5 0.65s / p95 10.14s, n=11)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x11; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "optionSelected"  x11
    "DesignSubmitted"  x1
data.designSelections  (object, 1/12 records)
data.designSelections.glassRoofTemperature  (string, 1/12 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/12 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/12 records)
    "Tilted Out"  x1
data.featureUsed  (string, 12/12 records)
    "GlassRoofTemperature"  x5
    "RoofStyle"  x4
    "ExtraCovering"  x2
    "Submit"  x1
data.selectedOption  (string, 11/12 records, 1 empty-string)
    "Hot"  x3
    "Tilted Out"  x2
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (5); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 1.67s (p5 0.28s / p95 215329.76s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x10
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Freshwater"  x5
    "Unit 2 – Watershed"  x1
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Watershed Image"  x4
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 5 Dev (5); Unit 2 Prod (Refactor) (2); Transition (1); Unit 1 Dev (1); Unit 3 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 42892.37s (p5 35.54s / p95 344513.25s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 6.60s (p5 1.32s / p95 21.98s, n=6)
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 3 empty-string)
    "cameraPlaced"  x4
    ""  x3
data.boxId  (string, 7/7 records)
    "0"  x3
    "1"  x2
    "2"  x2
data.soilType  (string, 7/7 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x2
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 4 empty-string)
    ""  x4
    "TypeError: Permissions check failed"  x2
data.type  (string, 6/6 records)
    "unhandled_rejection"  x6
data.unitId  (string, 6/6 records)
    "unit2"  x2
    "unit3"  x2
    "unit1"  x1
    "unit5"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 343622.20s (p5 190712.49s / p95 500919.88s, n=3)
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

### `soilMachine` — 2 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (2)
- **Intervals:** median 38.97s (p5 38.97s / p95 38.97s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "ChangeCanister"  x2
data.canisterType  (string, 2/2 records)
    "Gravel"  x1
    "Sand"  x1
data.floor  (string, 2/2 records)
    "5"  x2
data.machine  (string, 2/2 records)
    "2"  x2
data.row  (string, 2/2 records)
    "TopRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (24x); "WaypointResetEvent" (2x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (32x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*