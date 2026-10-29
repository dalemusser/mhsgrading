# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b70

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b70
- **Game version string(s) in log:** 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b70.jsonl
- **Records:** 21743 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b70
- **Time span:** 2026-10-05T19:14:29.992000+00:00 .. 2026-10-19T04:20:02.845000+00:00 (321h 5m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b70\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 21743 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 109 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 12640 | 58.13 | 1 | 9 | 0 | 2026-10-06T18:31:03.291000+00:00 | 2026-10-19T04:20:02.845000+00:00 | 297h 48m |
| PuzzlePieceVisibleEvent | 2878 | 13.24 | 1 | 4 | 0 | 2026-10-06T19:01:25.122000+00:00 | 2026-10-19T03:51:09.656000+00:00 | 296h 49m |
| DialogueEvent | 2418 | 11.12 | 1 | 9 | 1522 | 2026-10-05T19:14:59.810000+00:00 | 2026-10-19T04:19:54.219000+00:00 | 321h 4m |
| PlayerPositionEvent | 2077 | 9.55 | 1 | 9 | 0 | 2026-10-05T19:14:39.825000+00:00 | 2026-10-19T04:20:01.579000+00:00 | 321h 5m |
| argumentationNodeEvent | 695 | 3.2 | 1 | 5 | 0 | 2026-10-06T18:50:02.364000+00:00 | 2026-10-19T04:10:21.641000+00:00 | 297h 20m |
| ObjectInterEvent | 372 | 1.71 | 1 | 9 | 0 | 2026-10-06T18:35:17.261000+00:00 | 2026-10-19T04:20:02.845000+00:00 | 297h 44m |
| Soil Key Puzzle | 238 | 1.09 | 1 | 3 | 0 | 2026-10-06T19:07:42.409000+00:00 | 2026-10-15T18:43:24.997000+00:00 | 215h 35m |
| questEvent | 99 | 0.46 | 1 | 9 | 99 | 2026-10-05T19:14:59.784000+00:00 | 2026-10-19T04:16:06.267000+00:00 | 321h 1m |
| TopographicMapEvent | 71 | 0.33 | 1 | 3 | 0 | 2026-10-06T19:01:48.656000+00:00 | 2026-10-15T17:02:51.420000+00:00 | 214h 1m |
| DEBUGMenu | 43 | 0.2 | 1 | 9 | 0 | 2026-10-05T19:14:39.811000+00:00 | 2026-10-19T03:44:01.209000+00:00 | 320h 29m |
| argumentationAnswerEvent | 43 | 0.2 | 1 | 5 | 0 | 2026-10-06T18:50:10.860000+00:00 | 2026-10-19T04:10:22.669000+00:00 | 297h 20m |
| soilMachine | 30 | 0.14 | 1 | 1 | 0 | 2026-10-15T18:56:58.833000+00:00 | 2026-10-16T18:37:00.168000+00:00 | 23h 40m |
| WaterChamberEvent | 28 | 0.13 | 1 | 1 | 0 | 2026-10-19T03:50:24.506000+00:00 | 2026-10-19T04:01:59.249000+00:00 | 11m 34s |
| gameWindowFocusEvent | 28 | 0.13 | 1 | 8 | 0 | 2026-10-05T19:14:29.992000+00:00 | 2026-10-19T04:05:58.187000+00:00 | 320h 51m |
| gameStartEvent | 20 | 0.09 | 1 | 1 | 0 | 2026-10-05T19:14:29.993000+00:00 | 2026-10-19T03:43:53.306000+00:00 | 320h 29m |
| argumentationEvent | 15 | 0.07 | 1 | 5 | 0 | 2026-10-06T18:49:58.240000+00:00 | 2026-10-19T04:10:22.709000+00:00 | 297h 20m |
| gameWindowUnfocusEvent | 14 | 0.06 | 1 | 9 | 0 | 2026-10-05T19:18:04.917000+00:00 | 2026-10-19T04:05:55.369000+00:00 | 320h 47m |
| DaniEvent | 10 | 0.05 | 1 | 2 | 0 | 2026-10-15T16:07:13.727000+00:00 | 2026-10-15T19:05:58.222000+00:00 | 2h 58m |
| SolarStillDesignEvent | 6 | 0.03 | 1 | 1 | 0 | 2026-10-19T04:13:15.424000+00:00 | 2026-10-19T04:13:28.062000+00:00 | 12.6s |
| EndOfUnit | 5 | 0.02 | 1 | 5 | 0 | 2026-10-06T18:55:51.278000+00:00 | 2026-10-19T04:20:02.821000+00:00 | 297h 24m |
| TerasGardenBox | 5 | 0.02 | 1 | 1 | 0 | 2026-10-19T03:28:36.181000+00:00 | 2026-10-19T03:29:21.343000+00:00 | 45.2s |
| argumentationToolEvent | 4 | 0.02 | 1 | 2 | 0 | 2026-10-06T18:49:53.756000+00:00 | 2026-10-14T18:45:48.086000+00:00 | 191h 55m |
| chatEvent | 4 | 0.02 | 1 | 3 | 0 | 2026-10-15T19:05:45.340000+00:00 | 2026-10-19T04:03:10.861000+00:00 | 80h 57m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 188737.538s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 0.261s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.053s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 9.349s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 21.557s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 70.297s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 9111.397s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1767.023s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 74929.366s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 8.884s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 10 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` — record volume changed 5.2x vs baseline. 
  - Observed: 12640 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 6.3x vs baseline. 
  - Observed: 238 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
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
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 8.6x vs baseline. 
  - Observed: 43 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,3,I; A,B,2,II; A,C,2,II; A,D,2,II; A,D,C,2,II; B,1,II; B,2,II; B,3,I; B,3,II; B,4,II; B,D,2,II; B,D,A,2,II; C,1,II; C,2,II; C,A,2,II; C,B,4,II; C,D,2,II; C,D,3,II; D,1,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 695 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [91-89, 91-91, 91-92, 91-98, 91-99] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 14 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[219] _id=6ac53fd5de269131f9b699e3 ts=2026-10-06T18:37:09.6390000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[328] _id=6ac540b4de269131f9b6b4db ts=2026-10-06T18:40:52.4520000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[393] _id=6ac54122de269131f9b6c197 ts=2026-10-06T18:42:42.1650000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[3] _id=6ac3f716de269131f9af6c11 ts=2026-10-05T19:14:29.9930000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[51] _id=6ac53e59de269131f9b67371 ts=2026-10-06T18:30:48.6810000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[941] _id=6ac5448dde269131f9b718b9 ts=2026-10-06T18:57:17.1240000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[2] _id=6ac3f716de269131f9af6c0f ts=2026-10-05T19:14:29.9920000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[53] _id=6ac53e59de269131f9b6736f ts=2026-10-06T18:30:48.6790000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[679] _id=6ac5430ede269131f9b6fe73 ts=2026-10-06T18:50:53.8250000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[52] _id=6ac53e58de269131f9b67365 ts=2026-10-05T19:18:04.917Z`; `6ab9a9279a8420a1e6b56b70.jsonl[677] _id=6ac5430bde269131f9b6fe2f ts=2026-10-06T18:50:51.1020000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[5010] _id=6ac7e5a0de269131f9c58b41 ts=2026-10-07T19:17:15.885Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 12639 | 0.0 | 0.261 | 84.828 | 1.865 | 431632.826 | 0.71 | 1184 | 13 |
| PuzzlePieceVisibleEvent | 2877 | 0.0 | 0.053 | 371.423 | 1.395 | 517559.893 | 0.16 | 1420 | 10 |
| DialogueEvent | 2417 | 0.0 | 4.71 | 478.235 | 28.149 | 431629.787 | 0.13 | 684 | 12 |
| PlayerPositionEvent | 2065 | 9.705 | 10.003 | 559.595 | 10.152 | 431606.368 | 0.11 | 0 | 13 |
| argumentationNodeEvent | 694 | 0.005 | 0.461 | 1542.391 | 10.019 | 690818.931 | 0.04 | 88 | 5 |
| ObjectInterEvent | 371 | 0.0 | 8.441 | 2889.179 | 392.914 | 431991.639 | 0.02 | 5 | 18 |
| Soil Key Puzzle | 237 | 0.0 | 0.537 | 3274.863 | 9.206 | 604958.211 | 0.02 | 24 | 3 |
| questEvent | 98 | 0.0 | 171.541 | 11792.515 | 76297.16 | 432615.938 | 0.01 | 19 | 16 |
| TopographicMapEvent | 70 | 0.023 | 3.285 | 11006.611 | 43099.736 | 517801.811 | 0.01 | 4 | 6 |
| DEBUGMenu | 42 | 6.485 | 439.018 | 27470.509 | 86533.048 | 433290.181 | 0.0 | 0 | 20 |
| argumentationAnswerEvent | 42 | 3.477 | 21.557 | 25485.995 | 163196.978 | 690869.04 | 0.0 | 0 | 5 |
| soilMachine | 29 | 0.164 | 8.884 | 2937.977 | 5641.915 | 74563.813 | 0.02 | 0 | 2 |
| WaterChamberEvent | 27 | 1.854 | 17.811 | 25.731 | 59.718 | 78.398 | 2.33 | 0 | 0 |
| gameWindowFocusEvent | 27 | 210.318 | 1767.023 | 42781.044 | 167991.445 | 433305.957 | 0.0 | 0 | 20 |
| gameStartEvent | 19 | 242.42 | 9111.397 | 60724.385 | 225920.692 | 433305.956 | 0.0 | 0 | 18 |
| argumentationEvent | 14 | 0.031 | 127.666 | 76458.891 | 373785.959 | 690815.035 | 0.0 | 2 | 5 |
| gameWindowUnfocusEvent | 13 | 107.491 | 74929.366 | 88836.189 | 329631.645 | 518422.495 | 0.0 | 0 | 11 |
| DaniEvent | 9 | 0.008 | 2.331 | 1191.611 | 6425.297 | 10705.572 | 0.05 | 2 | 1 |
| SolarStillDesignEvent | 5 | 1.113 | 2.375 | 2.528 | 4.359 | 4.826 | 23.74 | 0 | 0 |
| EndOfUnit | 4 | 2188.159 | 188737.538 | 267662.886 | 631133.43 | 690988.309 | 0.0 | 0 | 4 |
| TerasGardenBox | 4 | 1.174 | 9.349 | 11.29 | 23.932 | 25.289 | 5.31 | 0 | 0 |
| argumentationToolEvent | 3 | 4.393 | 70.297 | 230318.11 | 621798.706 | 690879.64 | 0.0 | 0 | 1 |
| chatEvent | 3 | 4.287 | 1149.952 | 97148.507 | 261377.149 | 290291.282 | 0.0 | 0 | 2 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 23 group(s), 29 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[3049] _id=6ac69371de269131f9be04dc ts=2026-10-07T18:46:08.2890000Z == 6ab9a9279a8420a1e6b56b70.jsonl[3050] _id=6ac69371de269131f9be04dd ts=2026-10-07T18:46:08.2890000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[3065] _id=6ac6937dde269131f9be0621 ts=2026-10-07T18:46:20.1040000Z == 6ab9a9279a8420a1e6b56b70.jsonl[3066] _id=6ac6937dde269131f9be0622 ts=2026-10-07T18:46:20.1040000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[5103] _id=6ac7e625de269131f9c59a60 ts=2026-10-08T18:51:16.2550000Z == 6ab9a9279a8420a1e6b56b70.jsonl[5104] _id=6ac7e625de269131f9c59a61 ts=2026-10-08T18:51:16.2550000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 131 group(s), 202 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[1190] _id=6ac545dade269131f9b731ab ts=2026-10-06T19:02:48.9600000Z == 6ab9a9279a8420a1e6b56b70.jsonl[1194] _id=6ac545dade269131f9b731af ts=2026-10-06T19:02:48.9600000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1161] _id=6ac545e0de269131f9b7323b ts=2026-10-06T19:02:55.0490000Z == 6ab9a9279a8420a1e6b56b70.jsonl[1213] _id=6ac545e0de269131f9b73241 ts=2026-10-06T19:02:55.0490000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1211] _id=6ac545e1de269131f9b7325b ts=2026-10-06T19:02:55.6820000Z == 6ab9a9279a8420a1e6b56b70.jsonl[1218] _id=6ac545e1de269131f9b7325d ts=2026-10-06T19:02:55.6820000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[21470] _id=6ad59878de269131f9e94e64 ts=2026-10-19T04:11:36.3670000Z == 6ab9a9279a8420a1e6b56b70.jsonl[21471] _id=6ad59878de269131f9e94e65 ts=2026-10-19T04:11:36.3670000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 15 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 6ab9a9279a8420a1e6b56b70.jsonl[160] _id=6ac53f65de269131f9b68d85 ts=2026-10-06T18:35:17.2610000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[161] _id=6ac53f65de269131f9b68d87 ts=2026-10-06T18:35:17.2720000Z`; `205ms: 6ab9a9279a8420a1e6b56b70.jsonl[1068] _id=6ac5454bde269131f9b72639 ts=2026-10-06T19:00:27.5080000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[1069] _id=6ac5454bde269131f9b7263f ts=2026-10-06T19:00:27.7130000Z`; `179ms: 6ab9a9279a8420a1e6b56b70.jsonl[1069] _id=6ac5454bde269131f9b7263f ts=2026-10-06T19:00:27.7130000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[1071] _id=6ac5454cde269131f9b72645 ts=2026-10-06T19:00:27.8920000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 318 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `576ms: 6ab9a9279a8420a1e6b56b70.jsonl[1194] _id=6ac545dade269131f9b731af ts=2026-10-06T19:02:48.9600000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[1195] _id=6ac545dade269131f9b731b3 ts=2026-10-06T19:02:49.5360000Z`; `29ms: 6ab9a9279a8420a1e6b56b70.jsonl[1218] _id=6ac545e1de269131f9b7325d ts=2026-10-06T19:02:55.6820000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[1219] _id=6ac545e1de269131f9b73261 ts=2026-10-06T19:02:55.7110000Z`; `767ms: 6ab9a9279a8420a1e6b56b70.jsonl[1294] _id=6ac545f1de269131f9b733ed ts=2026-10-06T19:02:55.8290000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[1271] _id=6ac545f1de269131f9b733f1 ts=2026-10-06T19:02:56.5960000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `665ms: 6ab9a9279a8420a1e6b56b70.jsonl[4100] _id=6ac697c0de269131f9bed59e ts=2026-10-07T19:04:31.9420000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[4101] _id=6ac697c1de269131f9bed5b9 ts=2026-10-07T19:04:32.6070000Z`; `342ms: 6ab9a9279a8420a1e6b56b70.jsonl[4163] _id=6ac6984bde269131f9beec58 ts=2026-10-07T19:06:50.5590000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[4165] _id=6ac6984bde269131f9beec68 ts=2026-10-07T19:06:50.9010000Z`; `335ms: 6ab9a9279a8420a1e6b56b70.jsonl[4164] _id=6ac6984bde269131f9beec62 ts=2026-10-07T19:06:50.5670000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[4166] _id=6ac6984bde269131f9beec69 ts=2026-10-07T19:06:50.9020000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6ab9a9279a8420a1e6b56b70.jsonl[2985] _id=6ac54910de269131f9b7936e ts=2026-10-06T19:16:31.9910000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[2980] _id=6ac54910de269131f9b79385 ts=2026-10-06T19:16:32.0200000Z`; `962ms: 6ab9a9279a8420a1e6b56b70.jsonl[8132] _id=6acfd240de269131f9d7fc1a ts=2026-10-14T19:04:31.6750000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[8121] _id=6acfd241de269131f9d7fc36 ts=2026-10-14T19:04:32.6370000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `31ms: 6ab9a9279a8420a1e6b56b70.jsonl[8451] _id=6acfd3ebde269131f9d8407b ts=2026-10-14T19:11:38.4940000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[8454] _id=6acfd3ebde269131f9d8407e ts=2026-10-14T19:11:38.5250000Z`; `45ms: 6ab9a9279a8420a1e6b56b70.jsonl[19108] _id=6ad58c6ade269131f9e93a03 ts=2026-10-19T03:20:09.1880000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[19111] _id=6ad58c6ade269131f9e93a06 ts=2026-10-19T03:20:09.2330000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 50 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6ab9a9279a8420a1e6b56b70.jsonl[654] _id=6ac542dede269131f9b6f9e3 ts=2026-10-06T18:50:06.5660000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[655] _id=6ac542dede269131f9b6f9e5 ts=2026-10-06T18:50:06.5860000Z`; `328ms: 6ab9a9279a8420a1e6b56b70.jsonl[711] _id=6ac5432bde269131f9b700d3 ts=2026-10-06T18:51:23.0080000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[712] _id=6ac5432bde269131f9b700de ts=2026-10-06T18:51:23.3360000Z`; `324ms: 6ab9a9279a8420a1e6b56b70.jsonl[715] _id=6ac5432bde269131f9b700d9 ts=2026-10-06T18:51:23.0910000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[701] _id=6ac5432bde269131f9b700e3 ts=2026-10-06T18:51:23.4150000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a9279a8420a1e6b56b70.jsonl[21615] _id=6ad59942de269131f9e94faf ts=2026-10-19T04:14:58.0510000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[21626] _id=6ad59942de269131f9e94fb1 ts=2026-10-19T04:14:58.0540000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `983ms: 6ab9a9279a8420a1e6b56b70.jsonl[14241] _id=6ad12270de269131f9dfa090 ts=2026-10-15T18:58:55.7260000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[14243] _id=6ad12271de269131f9dfa0b3 ts=2026-10-15T18:58:56.7090000Z`; `301ms: 6ab9a9279a8420a1e6b56b70.jsonl[14243] _id=6ad12271de269131f9dfa0b3 ts=2026-10-15T18:58:56.7090000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[14244] _id=6ad12272de269131f9dfa0db ts=2026-10-15T18:58:57.0100000Z`; `164ms: 6ab9a9279a8420a1e6b56b70.jsonl[14244] _id=6ad12272de269131f9dfa0db ts=2026-10-15T18:58:57.0100000Z ~ 6ab9a9279a8420a1e6b56b70.jsonl[14251] _id=6ad12272de269131f9dfa0de ts=2026-10-15T18:58:57.1740000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[5008] _id=6ac7e5afde269131f9c58c13 ts=2026-10-08T18:49:18.5710000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6308] _id=6ace8239de269131f9d1800b ts=2026-10-13T19:10:48.7520000Z; 56h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[17949] _id=6ad270f5de269131f9e74be2 ts=2026-10-16T18:46:12.3210000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18643] _id=6ad5896cde269131f9e93698 ts=2026-10-19T03:07:23.4520000Z; 24h 2m: 6ab9a9279a8420a1e6b56b70.jsonl[3046] _id=6ac6936fde269131f9be048e ts=2026-10-07T18:46:06.3060000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5011] _id=6ac7e5a0de269131f9c58b45 ts=2026-10-08T18:49:02.9770000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 58m 
  - Evidence: 2h 58m: 6ab9a9279a8420a1e6b56b70.jsonl[10608] _id=6ad0fa36de269131f9dd3ab9 ts=2026-10-15T16:07:17.7050000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[15100] _id=6ad12407de269131f9dfe17d ts=2026-10-15T19:05:43.2770000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.008s..0.008s shown 
  - Evidence: 8ms: 6ab9a9279a8420a1e6b56b70.jsonl[15076] _id=6ad12410de269131f9dfe30f ts=2026-10-15T19:05:52.2730000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[15077] _id=6ad12411de269131f9dfe317 ts=2026-10-15T19:05:52.2810000Z; 8ms: 6ab9a9279a8420a1e6b56b70.jsonl[15092] _id=6ad12415de269131f9dfe3dd ts=2026-10-15T19:05:56.7880000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[15090] _id=6ad12415de269131f9dfe3ef ts=2026-10-15T19:05:56.7960000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a9279a8420a1e6b56b70.jsonl[6306] _id=6ac7ec4cde269131f9c68633 ts=2026-10-08T19:17:31.5830000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6339] _id=6ace8259de269131f9d1849a ts=2026-10-13T19:11:21.3700000Z; 56h 8m: 6ab9a9279a8420a1e6b56b70.jsonl[18612] _id=6ad273e9de269131f9e7854a ts=2026-10-16T18:58:48.5100000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18669] _id=6ad58981de269131f9e936a9 ts=2026-10-19T03:07:45.3880000Z; 23h 33m: 6ab9a9279a8420a1e6b56b70.jsonl[4641] _id=6ac69a5fde269131f9bf18c0 ts=2026-10-07T19:15:43.1710000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5020] _id=6ac7e5b8de269131f9c58cd2 ts=2026-10-08T18:49:27.4470000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 684 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[18235] _id=6ad27257de269131f9e7672e ts=2026-10-16T18:52:06.1850000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18236] _id=6ad27257de269131f9e7672f ts=2026-10-16T18:52:06.1850000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[18338] _id=6ad272bdde269131f9e76f54 ts=2026-10-16T18:53:48.5740000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18339] _id=6ad272bdde269131f9e76f55 ts=2026-10-16T18:53:48.5740000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[18362] _id=6ad272d4de269131f9e770f9 ts=2026-10-16T18:54:11.2240000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18363] _id=6ad272d4de269131f9e770fa ts=2026-10-16T18:54:11.2240000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 56m 
  - Evidence: 191h 56m: 6ab9a9279a8420a1e6b56b70.jsonl[932] _id=6ac54437de269131f9b71435 ts=2026-10-06T18:55:51.2780000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7508] _id=6acfcf64de269131f9d7a70e ts=2026-10-14T18:52:19.5870000Z; 81h 5m: 6ab9a9279a8420a1e6b56b70.jsonl[12284] _id=6ad11d73de269131f9deff35 ts=2026-10-15T18:37:38.8820000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[19788] _id=6ad591e7de269131f9e93eda ts=2026-10-19T03:43:34.6620000Z; 23h 45m: 6ab9a9279a8420a1e6b56b70.jsonl[7508] _id=6acfcf64de269131f9d7a70e ts=2026-10-14T18:52:19.5870000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[12284] _id=6ad11d73de269131f9deff35 ts=2026-10-15T18:37:38.8820000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a9279a8420a1e6b56b70.jsonl[6301] _id=6ac7ec38de269131f9c68422 ts=2026-10-08T19:17:11.8120000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6316] _id=6ace824ade269131f9d18287 ts=2026-10-13T19:11:04.6380000Z; 56h 18m: 6ab9a9279a8420a1e6b56b70.jsonl[18126] _id=6ad271a0de269131f9e75a6d ts=2026-10-16T18:49:03.7480000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18646] _id=6ad58980de269131f9e936a0 ts=2026-10-19T03:07:41.4760000Z; 23h 32m: 6ab9a9279a8420a1e6b56b70.jsonl[4986] _id=6ac69aa5de269131f9bf1f42 ts=2026-10-07T19:16:52.3100000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5023] _id=6ac7e5b5de269131f9c58c90 ts=2026-10-08T18:49:24.3170000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1184 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[10001] _id=6ad0f971de269131f9dd2401 ts=2026-10-15T16:04:00.3650000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[10002] _id=6ad0f971de269131f9dd2402 ts=2026-10-15T16:04:00.3650000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[10003] _id=6ad0f972de269131f9dd2424 ts=2026-10-15T16:04:01.3110000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[10004] _id=6ad0f972de269131f9dd2425 ts=2026-10-15T16:04:01.3110000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[10012] _id=6ad0f971de269131f9dd240e ts=2026-10-15T16:04:00.7490000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[10013] _id=6ad0f971de269131f9dd240f ts=2026-10-15T16:04:00.7490000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6ab9a9279a8420a1e6b56b70.jsonl[6296] _id=6ac7ec39de269131f9c6843b ts=2026-10-08T19:17:12.2640000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6513] _id=6ace83b0de269131f9d1bb46 ts=2026-10-13T19:17:03.9030000Z; 56h 20m: 6ab9a9279a8420a1e6b56b70.jsonl[18124] _id=6ad271a0de269131f9e75a71 ts=2026-10-16T18:49:03.9160000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18691] _id=6ad589d1de269131f9e936ee ts=2026-10-19T03:09:04.9620000Z; 23h 56m: 6ab9a9279a8420a1e6b56b70.jsonl[2641] _id=6ac546fede269131f9b75c03 ts=2026-10-06T19:07:42.4100000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[4095] _id=6ac697bbde269131f9bed4ac ts=2026-10-07T19:04:26.9020000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[17992] _id=6ad2715dde269131f9e7547d ts=2026-10-16T18:47:56.7270000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[17993] _id=6ad2715dde269131f9e7547e ts=2026-10-16T18:47:56.7270000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[18097] _id=6ad27192de269131f9e75975 ts=2026-10-16T18:48:49.6410000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18098] _id=6ad27192de269131f9e75976 ts=2026-10-16T18:48:49.6410000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[18745] _id=6ad58a22de269131f9e93775 ts=2026-10-19T03:10:25.9470000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18746] _id=6ad58a22de269131f9e93776 ts=2026-10-19T03:10:25.9470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a9279a8420a1e6b56b70.jsonl[6307] _id=6ace8239de269131f9d17ffc ts=2026-10-08T19:17:33.102Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6315] _id=6ace824ade269131f9d18286 ts=2026-10-13T19:10:59.4700000Z; 56h 7m: 6ab9a9279a8420a1e6b56b70.jsonl[18619] _id=6ad27421de269131f9e78659 ts=2026-10-16T18:59:44.2420000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18645] _id=6ad58980de269131f9e9369f ts=2026-10-19T03:07:41.4690000Z; 23h 32m: 6ab9a9279a8420a1e6b56b70.jsonl[5007] _id=6ac69ab5de269131f9bf204e ts=2026-10-07T19:17:09.0790000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5014] _id=6ac7e5b3de269131f9c58c6c ts=2026-10-08T18:49:18.5820000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 143h 45m 
  - Evidence: 143h 45m: 6ab9a9279a8420a1e6b56b70.jsonl[5694] _id=6ac7e761de269131f9c5c433 ts=2026-10-08T18:56:29.5360000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7198] _id=6acfcd17de269131f9d76283 ts=2026-10-14T18:42:29.4290000Z; 57h 3m: 6ab9a9279a8420a1e6b56b70.jsonl[17686] _id=6ad26faade269131f9e73387 ts=2026-10-16T18:40:39.3790000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[19800] _id=6ad59209de269131f9e93ee9 ts=2026-10-19T03:44:08.0510000Z; 24h 6m: 6ab9a9279a8420a1e6b56b70.jsonl[2582] _id=6ac546d4de269131f9b75607 ts=2026-10-06T19:06:54.6480000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[4475] _id=6ac699ecde269131f9bf0e5f ts=2026-10-07T19:13:47.4020000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1420 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[10704] _id=6ad103f8de269131f9dde247 ts=2026-10-15T16:48:54.2000000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[10705] _id=6ad103f8de269131f9dde24f ts=2026-10-15T16:48:54.2000000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[10716] _id=6ad103fade269131f9dde29d ts=2026-10-15T16:48:57.7380000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[10708] _id=6ad103fade269131f9dde2bb ts=2026-10-15T16:48:57.7380000Z; 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[10736] _id=6ad10400de269131f9dde398 ts=2026-10-15T16:49:03.6410000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[10738] _id=6ad10400de269131f9dde39f ts=2026-10-15T16:49:03.6410000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 2m 
  - Evidence: 168h 2m: 6ab9a9279a8420a1e6b56b70.jsonl[4362] _id=6ac69977de269131f9bf0530 ts=2026-10-07T19:11:50.7980000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[8685] _id=6acfd496de269131f9d85d90 ts=2026-10-14T19:14:29.0090000Z; 23h 56m: 6ab9a9279a8420a1e6b56b70.jsonl[2576] _id=6ac54701de269131f9b75c6b ts=2026-10-06T19:07:45.3710000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[4098] _id=6ac697bbde269131f9bed4a7 ts=2026-10-07T19:04:26.8960000Z; 23h 28m: 6ab9a9279a8420a1e6b56b70.jsonl[8693] _id=6acfd4adde269131f9d861b7 ts=2026-10-14T19:14:52.5450000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[12416] _id=6ad11eb7de269131f9df244b ts=2026-10-15T18:43:03.0820000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 24 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[4168] _id=6ac6984cde269131f9beec73 ts=2026-10-07T19:06:51.2360000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[4169] _id=6ac6984cde269131f9beec74 ts=2026-10-07T19:06:51.2360000Z; 1ms: 6ab9a9279a8420a1e6b56b70.jsonl[4165] _id=6ac6984bde269131f9beec68 ts=2026-10-07T19:06:50.9010000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[4166] _id=6ac6984bde269131f9beec69 ts=2026-10-07T19:06:50.9020000Z; 1ms: 6ab9a9279a8420a1e6b56b70.jsonl[4166] _id=6ac6984bde269131f9beec69 ts=2026-10-07T19:06:50.9020000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[4167] _id=6ac6984bde269131f9beec6a ts=2026-10-07T19:06:50.9030000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 50m 
  - Evidence: 143h 50m: 6ab9a9279a8420a1e6b56b70.jsonl[5932] _id=6ac7e9ebde269131f9c635ba ts=2026-10-08T19:07:22.6190000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7609] _id=6acfd095de269131f9d7c744 ts=2026-10-14T18:57:24.4300000Z; 24h 8m: 6ab9a9279a8420a1e6b56b70.jsonl[3600] _id=6ac69647de269131f9be9ab2 ts=2026-10-07T18:58:14.4040000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5926] _id=6ac7e9d7de269131f9c63190 ts=2026-10-08T19:07:02.6660000Z; 23h 32m: 6ab9a9279a8420a1e6b56b70.jsonl[2994] _id=6ac54927de269131f9b796b3 ts=2026-10-06T19:16:55.0260000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[3228] _id=6ac69421de269131f9be2150 ts=2026-10-07T18:49:04.2910000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.023s..0.041s shown 
  - Evidence: 23ms: 6ab9a9279a8420a1e6b56b70.jsonl[3234] _id=6ac69425de269131f9be2211 ts=2026-10-07T18:49:08.7430000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[3238] _id=6ac69425de269131f9be2215 ts=2026-10-07T18:49:08.7660000Z; 29ms: 6ab9a9279a8420a1e6b56b70.jsonl[2985] _id=6ac54910de269131f9b7936e ts=2026-10-06T19:16:31.9910000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[2980] _id=6ac54910de269131f9b79385 ts=2026-10-06T19:16:32.0200000Z; 41ms: 6ab9a9279a8420a1e6b56b70.jsonl[3233] _id=6ac69425de269131f9be220f ts=2026-10-07T18:49:08.7020000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[3234] _id=6ac69425de269131f9be2211 ts=2026-10-07T18:49:08.7430000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 54m 
  - Evidence: 191h 54m: 6ab9a9279a8420a1e6b56b70.jsonl[687] _id=6ac54354de269131f9b703d7 ts=2026-10-06T18:52:04.0290000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7340] _id=6acfce0ade269131f9d784a5 ts=2026-10-14T18:46:33.0690000Z; 56h 17m: 6ab9a9279a8420a1e6b56b70.jsonl[18609] _id=6ad273e9de269131f9e78546 ts=2026-10-16T18:58:48.4590000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18919] _id=6ad58b6dde269131f9e938ca ts=2026-10-19T03:15:56.7390000Z; 47h 40m: 6ab9a9279a8420a1e6b56b70.jsonl[8450] _id=6acfd3ebde269131f9d84075 ts=2026-10-14T19:11:38.4780000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18241] _id=6ad27256de269131f9e7672c ts=2026-10-16T18:52:06.1660000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 53m 
  - Evidence: 191h 53m: 6ab9a9279a8420a1e6b56b70.jsonl[752] _id=6ac54354de269131f9b703d9 ts=2026-10-06T18:52:04.0470000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7299] _id=6acfcdd4de269131f9d77c98 ts=2026-10-14T18:45:39.0820000Z; 56h 24m: 6ab9a9279a8420a1e6b56b70.jsonl[18164] _id=6ad27209de269131f9e760df ts=2026-10-16T18:50:48.3780000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18891] _id=6ad58b4ede269131f9e9388f ts=2026-10-19T03:15:26.3730000Z; 47h 39m: 6ab9a9279a8420a1e6b56b70.jsonl[8454] _id=6acfd3ebde269131f9d8407e ts=2026-10-14T19:11:38.5250000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18164] _id=6ad27209de269131f9e760df ts=2026-10-16T18:50:48.3780000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.045s shown 
  - Evidence: 31ms: 6ab9a9279a8420a1e6b56b70.jsonl[8451] _id=6acfd3ebde269131f9d8407b ts=2026-10-14T19:11:38.4940000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[8454] _id=6acfd3ebde269131f9d8407e ts=2026-10-14T19:11:38.5250000Z; 45ms: 6ab9a9279a8420a1e6b56b70.jsonl[19108] _id=6ad58c6ade269131f9e93a03 ts=2026-10-19T03:20:09.1880000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[19111] _id=6ad58c6ade269131f9e93a06 ts=2026-10-19T03:20:09.2330000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 53m 
  - Evidence: 191h 53m: 6ab9a9279a8420a1e6b56b70.jsonl[748] _id=6ac54352de269131f9b7039d ts=2026-10-06T18:52:01.8510000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7303] _id=6acfcdd5de269131f9d77cdd ts=2026-10-14T18:45:40.7820000Z; 56h 16m: 6ab9a9279a8420a1e6b56b70.jsonl[18608] _id=6ad273e8de269131f9e7853e ts=2026-10-16T18:58:47.3290000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18889] _id=6ad58b4ade269131f9e93889 ts=2026-10-19T03:15:22.1490000Z; 47h 39m: 6ab9a9279a8420a1e6b56b70.jsonl[8449] _id=6acfd3eade269131f9d84040 ts=2026-10-14T19:11:37.2770000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18162] _id=6ad27208de269131f9e760d5 ts=2026-10-16T18:50:47.4780000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 88 interval(s) ≤ 0.005s..0.006s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b70.jsonl[18250] _id=6ad2726bde269131f9e768c8 ts=2026-10-16T18:52:26.3170000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18256] _id=6ad2726bde269131f9e768cc ts=2026-10-16T18:52:26.3220000Z; 6ms: 6ab9a9279a8420a1e6b56b70.jsonl[7391] _id=6acfce38de269131f9d78b07 ts=2026-10-14T18:47:19.2740000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7347] _id=6acfce38de269131f9d78b09 ts=2026-10-14T18:47:19.2800000Z; 6ms: 6ab9a9279a8420a1e6b56b70.jsonl[8346] _id=6acfd387de269131f9d82e6b ts=2026-10-14T19:09:58.4270000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[8347] _id=6acfd387de269131f9d82e6f ts=2026-10-14T19:09:58.4330000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 54m 
  - Evidence: 191h 54m: 6ab9a9279a8420a1e6b56b70.jsonl[682] _id=6ac5431cde269131f9b6ffa7 ts=2026-10-06T18:51:08.4460000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[7305] _id=6acfcdddde269131f9d77e03 ts=2026-10-14T18:45:48.0860000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 80h 38m 
  - Evidence: 80h 38m: 6ab9a9279a8420a1e6b56b70.jsonl[15074] _id=6ad1240ede269131f9dfe29f ts=2026-10-15T19:05:49.6270000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[19766] _id=6ad59201de269131f9e93ee3 ts=2026-10-19T03:44:00.9090000Z; 19m 9s: 6ab9a9279a8420a1e6b56b70.jsonl[19766] _id=6ad59201de269131f9e93ee3 ts=2026-10-19T03:44:00.9090000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[21083] _id=6ad5967fde269131f9e94adc ts=2026-10-19T04:03:10.8610000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[5013] _id=6ac7e5a0de269131f9c58b47 ts=2026-10-08T18:49:03.1150000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6310] _id=6ace8239de269131f9d1800d ts=2026-10-13T19:10:49.0710000Z; 56h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[17948] _id=6ad270eede269131f9e74b46 ts=2026-10-16T18:46:05.7710000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18653] _id=6ad5896cde269131f9e9369b ts=2026-10-19T03:07:23.6560000Z; 24h 3m: 6ab9a9279a8420a1e6b56b70.jsonl[3042] _id=6ac69362de269131f9be032a ts=2026-10-07T18:45:53.3610000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5013] _id=6ac7e5a0de269131f9c58b47 ts=2026-10-08T18:49:03.1150000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[5012] _id=6ac7e5a0de269131f9c58b46 ts=2026-10-08T18:49:03.1140000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6309] _id=6ace8239de269131f9d1800c ts=2026-10-13T19:10:49.0710000Z; 56h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[17947] _id=6ad270eede269131f9e74b45 ts=2026-10-16T18:46:05.7710000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18652] _id=6ad5896cde269131f9e9369a ts=2026-10-19T03:07:23.6560000Z; 24h 3m: 6ab9a9279a8420a1e6b56b70.jsonl[3041] _id=6ac69362de269131f9be0329 ts=2026-10-07T18:45:53.3610000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5012] _id=6ac7e5a0de269131f9c58b46 ts=2026-10-08T18:49:03.1140000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6ab9a9279a8420a1e6b56b70.jsonl[5010] _id=6ac7e5a0de269131f9c58b41 ts=2026-10-07T19:17:15.885Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6527] _id=6acfa712de269131f9d511e8 ts=2026-10-13T19:17:38.38Z; 56h 36m: 6ab9a9279a8420a1e6b56b70.jsonl[17307] _id=6ad26e7cde269131f9e71395 ts=2026-10-16T18:35:39.7270000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18831] _id=6ad58a77de269131f9e9381e ts=2026-10-19T03:11:50.8050000Z; 24h 26m: 6ab9a9279a8420a1e6b56b70.jsonl[677] _id=6ac5430bde269131f9b6fe2f ts=2026-10-06T18:50:51.1020000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5010] _id=6ac7e5a0de269131f9c58b41 ts=2026-10-07T19:17:15.885Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 120h 10m 
  - Evidence: 120h 10m: 6ab9a9279a8420a1e6b56b70.jsonl[5826] _id=6ac7e861de269131f9c5ebc0 ts=2026-10-08T19:00:48.7480000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[6321] _id=6ace824ade269131f9d1828c ts=2026-10-13T19:11:04.6860000Z; 56h 21m: 6ab9a9279a8420a1e6b56b70.jsonl[17951] _id=6ad270f6de269131f9e74bef ts=2026-10-16T18:46:13.5180000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[18668] _id=6ad58980de269131f9e936a7 ts=2026-10-19T03:07:44.1920000Z; 23h 45m: 6ab9a9279a8420a1e6b56b70.jsonl[4081] _id=6ac697b1de269131f9bed27f ts=2026-10-07T19:04:16.7300000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[5015] _id=6ac7e5b3de269131f9c58c6d ts=2026-10-08T18:49:21.1780000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b70.jsonl[21470] _id=6ad59878de269131f9e94e64 ts=2026-10-19T04:11:36.3670000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[21471] _id=6ad59878de269131f9e94e65 ts=2026-10-19T04:11:36.3670000Z; 1ms: 6ab9a9279a8420a1e6b56b70.jsonl[20644] _id=6ad5950bde269131f9e946e8 ts=2026-10-19T03:56:59.2920000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[20645] _id=6ad5950bde269131f9e946e9 ts=2026-10-19T03:56:59.2930000Z; 2ms: 6ab9a9279a8420a1e6b56b70.jsonl[17308] _id=6ad26e7ede269131f9e713b0 ts=2026-10-16T18:35:41.5500000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[17309] _id=6ad26e7ede269131f9e713b1 ts=2026-10-16T18:35:41.5520000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 20h 42m 
  - Evidence: 20h 42m: 6ab9a9279a8420a1e6b56b70.jsonl[16117] _id=6ad12691de269131f9e03f5a ts=2026-10-15T19:16:32.6050000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[16396] _id=6ad249d5de269131f9e57806 ts=2026-10-16T15:59:16.4180000Z; 2h 32m: 6ab9a9279a8420a1e6b56b70.jsonl[16602] _id=6ad24a47de269131f9e58026 ts=2026-10-16T16:01:10.1440000Z -> 6ab9a9279a8420a1e6b56b70.jsonl[17064] _id=6ad26df5de269131f9e706ee ts=2026-10-16T18:33:24.7170000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[768] _id=6ac543b0de269131f9b70967 ts=2026-10-06T18:53:35.7420000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[3487] _id=6ac695fdde269131f9be88f0 ts=2026-10-07T18:57:01.2310000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[5637] _id=6ac7e757de269131f9c5c28e ts=2026-10-08T18:56:22.5460000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 131 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[1278] _id=6ac545f5de269131f9b73465 ts=2026-10-06T19:03:14.2470000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1279] _id=6ac545f5de269131f9b73469 ts=2026-10-06T19:03:14.2770000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1318] _id=6ac545f5de269131f9b7346d ts=2026-10-06T19:03:14.3770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 96 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[1258] _id=6ac545eede269131f9b7338d ts=2026-10-06T19:02:39.7950000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1260] _id=6ac545eede269131f9b73399 ts=2026-10-06T19:02:39.7950000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1237] _id=6ac545eede269131f9b733a5 ts=2026-10-06T19:02:40.7990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[8454] _id=6acfd3ebde269131f9d8407e ts=2026-10-14T19:11:38.5250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[655] _id=6ac542dede269131f9b6f9e5 ts=2026-10-06T18:50:06.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[19766] _id=6ad59201de269131f9e93ee3 ts=2026-10-19T03:44:00.9090000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[21083] _id=6ad5967fde269131f9e94adc ts=2026-10-19T04:03:10.8610000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[15396] _id=6ad1247ade269131f9dff150 ts=2026-10-15T19:07:37.9270000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[16223] _id=6ad2496bde269131f9e56f56 ts=2026-10-16T15:57:30.7990000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[16935] _id=6ad26dbdde269131f9e703c8 ts=2026-10-16T18:32:28.2820000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 350 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[1325] _id=6ac545f8de269131f9b734cd ts=2026-10-06T19:03:16.5840000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1353] _id=6ac545f8de269131f9b734d9 ts=2026-10-06T19:03:16.9800000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1351] _id=6ac545f9de269131f9b734db ts=2026-10-06T19:03:17.0190000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 395 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[1254] _id=6ac545edde269131f9b73373 ts=2026-10-06T19:02:37.9850000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1256] _id=6ac545edde269131f9b73377 ts=2026-10-06T19:02:38.0820000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1238] _id=6ac545eede269131f9b733ab ts=2026-10-06T19:02:40.7990000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 31 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[2985] _id=6ac54910de269131f9b7936e ts=2026-10-06T19:16:31.9910000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[2980] _id=6ac54910de269131f9b79385 ts=2026-10-06T19:16:32.0200000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[3228] _id=6ac69421de269131f9be2150 ts=2026-10-07T18:49:04.2910000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[18891] _id=6ad58b4ede269131f9e9388f ts=2026-10-19T03:15:26.3730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 453 start, 443 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 87 unmatched 'BecameCameraCentered' (totals: 701 open, 745 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 66 unmatched 'BecameVisible' (totals: 701 open, 731 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 33 open, 31 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 3 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 59 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 627 of 21742 adjacent _id pairs reverse in client time; worst 101.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b70.jsonl[1224] _id=6ac545ebde269131f9b7332b ts=2026-10-06T19:03:06.9210000Z`; `6ab9a9279a8420a1e6b56b70.jsonl[1240] _id=6ac545ecde269131f9b7333d ts=2026-10-06T19:01:25.1220000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.80s, min -431596.16s, max -0.18s over 21743 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b70\coverage.yaml

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

### `InputEvent` — 12640 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (3902); Unit 2 Prod (Refactor) (2831); Unit 3 Dungeon Dev (2207); Unit 3 Dev (1000); Unit 5 Dev - Dungeon (841); Unit 4 Dev (835); Unit 1 Dev (424); Unit 5 Dev (309); Unit 4 Dev - Anderson Base (291)
- **Intervals:** median 0.26s (p5 0.01s / p95 1.87s, n=12639)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 12640/12640 records)
    "pressed"  x12640
data.actionType  (string, 12640/12640 records)
    "Move"  x10162
    "Jump"  x862
    "Interact"  x591
    "Hoverboard"  x589
    "Sprint"  x302
    "Ascend"  x64
    "Map"  x31
    "Descend"  x28
    "ToggleDebug"  x8
    "Pause"  x3
data.key  (string, 12640/12640 records, 19 empty-string)
    14 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 12640/12640 records)
    "Player"  x11538
    "Drone"  x1102
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2878 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1864); Unit 3 Dungeon Dev (492); Unit 4 Dev (318); Unit 5 Dev - Dungeon (204)
- **Intervals:** median 0.05s (p5 0.00s / p95 1.39s, n=2877)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2878/2878 records)
    "BecameCameraUncentered"  x745
    "BecameInvisible"  x731
    "BecameCameraCentered"  x701
    "BecameVisible"  x701
data.pieceId  (string, 2878/2878 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2878/2878 records)
    1613 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2418 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (757); Unit 3 Dev (301); Unit 4 Dev (254); Unit 4 Dev - Anderson Base (244); Unit 1 Dev (211); Unit 5 Dev (210); Unit 4 Dev - Dungeon (195); Unit 3 Dungeon Dev (171); Unit 5 Dev - Dungeon (75)
- **eventKey:** present on 1522 of 2418 records
- **Intervals:** median 4.71s (p5 0.00s / p95 28.15s, n=2417)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1522; [conversationId, dialogueEventType] x896
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2418/2418 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2418/2418 records)
    "DialogueNodeEvent"  x1522
    "DialogueStartEvent"  x453
    "DialogueFinishEvent"  x443
data.nodeId  (number, 1522/2418 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2077 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (693); Unit 4 Dev - Dungeon (256); Unit 4 Dev (218); Unit 3 Dev (186); Unit 4 Dev - Anderson Base (172); Unit 1 Dev (170); Unit 3 Dungeon Dev (170); Unit 5 Dev - Dungeon (112); Unit 5 Dev (100)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.15s, n=2065)
- **Fields under `data`:**

```text
data.position  (object, 2077/2077 records)
data.position.x  (number, 2077/2077 records)
    numeric range -629.602 .. 1561.28 (704 unique)
data.position.y  (number, 2077/2077 records)
    numeric range -114.326 .. 223.314 (472 unique)
data.position.z  (number, 2077/2077 records)
    numeric range -1114.54 .. 1902.02 (704 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 695 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (435); Unit 2 Prod (Refactor) (91); Unit 3 Dev (77); Unit 1 Dev (58); Unit 5 Dev (34)
- **Intervals:** median 0.46s (p5 0.04s / p95 10.02s, n=694)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 695/695 records)
    "argumentationNodeHoverEnd"  x293
    "argumentationNodeHoverStart"  x292
    "argumentationNodeAdd"  x67
    "argumentationNodeRemove"  x43
data.argumentationTitle  (string, 695/695 records)
    "Unit 4 - Flooding"  x435
    "Unit 2 – Watershed"  x91
    "Unit 3 - Pollution Upstream"  x77
    "Unit 1 - Freshwater"  x45
    "Unit 5"  x34
    "Unit 1 - Argumentation Tutorial"  x13
data.nodeName  (string, 695/695 records)
    "B"  x122
    "A"  x106
    "C"  x103
    "D"  x86
    "II"  x66
    "1"  x63
    "2"  x42
    "3"  x37
    "I"  x35
    "4"  x28
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 372 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (173); Unit 2 Prod (Refactor) (73); Unit 3 Dungeon Dev (50); Unit 4 Dev - Anderson Base (19); Unit 4 Dev (18); Unit 5 Dev - Dungeon (12); Unit 3 Dev (11); Unit 1 Dev (10); Unit 5 Dev (6)
- **Intervals:** median 8.44s (p5 0.54s / p95 392.91s, n=371)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 372/372 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 372/372 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 238 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (216); Unit 3 Dev (12); Unit 4 Dev (10)
- **Intervals:** median 0.54s (p5 0.01s / p95 9.21s, n=237)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x230; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/238 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/238 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 230/238 records)
    "RightDrag"  x118
    "LeftDrag"  x112
data.currentSoilType  (string, 230/238 records)
    "SANDGRAVEL"  x52
    "SAND"  x43
    "CLAYSAND"  x38
    "GRAVEL"  x31
    "CLAY"  x30
    "CLAYROCK"  x25
    "BEDROCK"  x11
data.isCorrectSelection  (string, 230/238 records)
    "false"  x184
    "true"  x46
data.waterLevelStatus  (string, 230/238 records)
    "TooHigh"  x101
    "TooLow"  x72
    "Proper"  x57
data.waterRetentionChange  (string, 230/238 records)
    "Increase"  x95
    "Decrease"  x89
    "NoChange"  x46
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 99 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (25); Unit 2 Prod (Refactor) (20); Unit 1 Dev (13); Unit 3 Dev (10); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (4)
- **eventKey:** present on 99 of 99 records
- **Intervals:** median 171.54s (p5 0.00s / p95 76297.16s, n=98)
- **`data` key-set variants:** [questEventType, questID, questName] x59; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 99/99 records)
    "questActiveEvent"  x59
    "questFinishEvent"  x40
data.questID  (string, 99/99 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 99/99 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/99 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 71 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (46); Unit 2 Prod (Refactor) (23); Unit 3 Dungeon Dev (2)
- **Intervals:** median 3.29s (p5 0.23s / p95 43099.74s, n=70)
- **`data` key-set variants:** [actionType, featureUsed] x64; [actionType, featureUsed, location] x7
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 71/71 records)
    "MapOpenEvent"  x33
    "MapCloseEvent"  x31
    "WaypointMoveEvent"  x3
    "WaypointSetEvent"  x3
    "WaypointResetEvent"  x1
data.featureUsed  (string, 71/71 records)
    "Map"  x64
    "Waypoint"  x7
data.location  (object, 7/71 records)
data.location.x  (number, 7/71 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 7/71 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 7/71 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 43 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (6); Unit 3 Dungeon Dev (4); Unit 4 Dev - Dungeon (4); Unit 3 Dev (3); Unit 4 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 439.02s (p5 8.07s / p95 86533.05s, n=42)
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "DebugMenuStateChanged"  x43
data.isOpened  (bool, 43/43 records)
    false  x43
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 43 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (29); Unit 1 Dev (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 5 Dev (1)
- **Intervals:** median 21.56s (p5 8.75s / p95 163196.98s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "submitAnswerEvent"  x43
data.answerSubmitted  (string, 43/43 records, 1 empty-string)
    25 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 43/43 records)
    "Unit 4 - Flooding"  x29
    "Unit 1 - Freshwater"  x4
    "Unit 2 – Watershed"  x4
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 30 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (30)
- **Intervals:** median 8.88s (p5 0.27s / p95 5641.91s, n=29)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "ChangeCanister"  x30
data.canisterType  (string, 30/30 records)
    "Gravel"  x13
    "Clay"  x10
    "Sand"  x4
    "Bedrock"  x3
data.floor  (string, 30/30 records)
    "4"  x19
    "5"  x7
    "3"  x4
data.machine  (string, 30/30 records)
    "1"  x29
    "2"  x1
data.row  (string, 30/30 records)
    "TopRow"  x27
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 28 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (28)
- **Intervals:** median 17.81s (p5 2.80s / p95 59.72s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "On"  x17
    "Off"  x11
data.floor  (string, 28/28 records)
    "4"  x14
    "3"  x6
    "1"  x4
    "2"  x4
data.machineNumber  (string, 28/28 records)
    "One"  x27
    "Two"  x1
data.machineType  (string, 28/28 records)
    "Condenser"  x15
    "Evaporator"  x10
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 28/28 records)
    "2"  x11
    "1"  x8
    "3"  x7
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1767.02s (p5 245.95s / p95 167991.45s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 9111.40s (p5 775.39s / p95 225920.69s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 127.67s (p5 0.04s / p95 373785.96s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 14 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 2 Prod (Refactor) (2); Unit 3 Dungeon Dev (2); Unit 3 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 74929.37s (p5 195.00s / p95 329631.64s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    false  x14
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 10 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev - Dungeon (8); Unit 3 Dungeon Dev (2)
- **Intervals:** median 2.33s (p5 0.01s / p95 6425.30s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "Close"  x5
    "Open"  x5
data.toolName  (string, 10/10 records, 8 empty-string)
    ""  x8
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 2.38s (p5 1.26s / p95 4.36s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted In"  x1
data.featureUsed  (string, 6/6 records)
    "GlassRoofTemperature"  x3
    "ExtraCovering"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records, 1 empty-string)
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 188737.54s (p5 14687.83s / p95 631133.43s, n=4)
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

### `TerasGardenBox` — 5 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (5)
- **Intervals:** median 9.35s (p5 1.37s / p95 23.93s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records, 2 empty-string)
    "cameraPlaced"  x3
    ""  x2
data.boxId  (string, 5/5 records)
    "1"  x2
    "2"  x2
    "0"  x1
data.soilType  (string, 5/5 records)
    "Gravel"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 70.30s (p5 10.98s / p95 621798.71s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 4 Dev - Dungeon (2); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1149.95s (p5 118.85s / p95 261377.15s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x3
    "Open"  x1
data.chatID  (string, 4/4 records)
    "NA"  x3
    "[91-89, 91-91, 91-92, 91-98, 91-99]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

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
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (216 records)
- `TerasGardenBox` data.actionType: "" (2x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (3x); "WaypointResetEvent" (1x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (7x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (43x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*