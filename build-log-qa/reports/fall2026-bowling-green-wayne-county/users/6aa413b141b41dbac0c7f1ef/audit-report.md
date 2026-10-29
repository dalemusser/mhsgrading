# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1ef

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1ef
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1ef.jsonl
- **Records:** 13186 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1ef
- **Time span:** 2026-09-23T13:03:57.591000+00:00 .. 2026-10-01T13:40:48.012000+00:00 (192h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1ef\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13186 records, 10 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 110 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially
  - WARNING/Medium `DialogueEvent`: eventKey does not match its documented format

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4356 | 33.04 | 1 | 9 | 0 | 2026-09-23T13:04:35.603000+00:00 | 2026-10-01T13:40:48.012000+00:00 | 192h 36m |
| PuzzlePieceVisibleEvent | 4202 | 31.87 | 1 | 4 | 0 | 2026-09-24T12:53:26.995000+00:00 | 2026-10-01T13:16:09.423000+00:00 | 168h 22m |
| DialogueEvent | 2033 | 15.42 | 1 | 9 | 1280 | 2026-09-23T13:04:52.325000+00:00 | 2026-10-01T13:40:42.770000+00:00 | 192h 35m |
| PlayerPositionEvent | 1694 | 12.85 | 1 | 9 | 0 | 2026-09-23T13:04:30.259000+00:00 | 2026-10-01T13:40:45.222000+00:00 | 192h 36m |
| argumentationNodeEvent | 330 | 2.5 | 1 | 4 | 0 | 2026-09-23T13:27:51.007000+00:00 | 2026-10-01T13:30:51.341000+00:00 | 192h 3m |
| ObjectInterEvent | 246 | 1.87 | 1 | 9 | 0 | 2026-09-23T13:12:21.975000+00:00 | 2026-10-01T13:40:48.011000+00:00 | 192h 28m |
| questEvent | 76 | 0.58 | 1 | 9 | 76 | 2026-09-23T13:04:52.294000+00:00 | 2026-10-01T13:37:04.683000+00:00 | 192h 32m |
| Soil Key Puzzle | 35 | 0.27 | 1 | 3 | 0 | 2026-09-24T13:00:11.731000+00:00 | 2026-09-29T13:36:29.991000+00:00 | 120h 36m |
| TopographicMapEvent | 35 | 0.27 | 1 | 2 | 0 | 2026-09-23T13:35:00.344000+00:00 | 2026-09-29T13:19:11.303000+00:00 | 143h 44m |
| gameWindowFocusEvent | 31 | 0.24 | 1 | 7 | 0 | 2026-09-23T13:03:57.591000+00:00 | 2026-10-01T13:09:37.996000+00:00 | 192h 5m |
| gameWindowUnfocusEvent | 23 | 0.17 | 1 | 7 | 0 | 2026-09-23T13:23:32.519000+00:00 | 2026-09-30T15:15:25.038000+00:00 | 169h 51m |
| DEBUGMenu | 19 | 0.14 | 1 | 8 | 0 | 2026-09-23T13:04:30.249000+00:00 | 2026-10-01T13:09:45.152000+00:00 | 192h 5m |
| DaniEvent | 19 | 0.14 | 1 | 3 | 0 | 2026-09-23T13:11:12.411000+00:00 | 2026-09-29T13:42:16.526000+00:00 | 144h 31m |
| WaterChamberEvent | 17 | 0.13 | 1 | 1 | 0 | 2026-10-01T13:14:51.504000+00:00 | 2026-10-01T13:22:41.449000+00:00 | 7m 49s |
| argumentationAnswerEvent | 13 | 0.1 | 1 | 4 | 0 | 2026-09-23T13:28:52.077000+00:00 | 2026-10-01T13:30:52.477000+00:00 | 192h 2m |
| argumentationEvent | 13 | 0.1 | 1 | 4 | 0 | 2026-09-23T13:28:40.036000+00:00 | 2026-10-01T13:30:52.504000+00:00 | 192h 2m |
| gameStartEvent | 13 | 0.1 | 1 | 1 | 0 | 2026-09-23T13:03:57.592000+00:00 | 2026-10-01T13:09:37.999000+00:00 | 192h 5m |
| TerasGardenBox | 9 | 0.07 | 1 | 1 | 0 | 2026-10-01T12:56:09.881000+00:00 | 2026-10-01T12:57:10.498000+00:00 | 1m 0s |
| SolarStillDesignEvent | 8 | 0.06 | 1 | 1 | 0 | 2026-10-01T13:34:14.022000+00:00 | 2026-10-01T13:34:20.635000+00:00 | 6.6s |
| chatEvent | 6 | 0.05 | 1 | 3 | 0 | 2026-09-23T13:35:08.832000+00:00 | 2026-10-01T13:23:30.651000+00:00 | 191h 48m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-23T13:32:52.474000+00:00 | 2026-10-01T13:40:48.003000+00:00 | 192h 7m |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-28T13:28:46.568000+00:00 | 2026-09-28T13:29:01.419000+00:00 | 14.9s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |
| soilMachine | 1 | 0.01 | 1 | 1 | 0 | 2026-09-30T13:17:56.729000+00:00 | 2026-09-30T13:17:56.729000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 171628.909s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 0.669s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 10.273s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 38.109s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43036.095s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 703.106s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 577.956s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 19 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Switch Canister 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,C,B,2,II; C,2,II; C,A,2,II; C,B,2,II; C,D,3,II; D,1,II; D,2,II; D,4,II; I 
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
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [16-3]; [21-73, 21-75, 21-76, 23-0, 23-28] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
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
  - Observed: 26 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[269] _id=6ab3d0ca485cab4c954ba685 ts=2026-09-23T13:14:50.5420000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[328] _id=6ab3d177485cab4c954bcaa2 ts=2026-09-23T13:17:43.0270000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[377] _id=6ab3d224485cab4c954be6a2 ts=2026-09-23T13:20:36.7770000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[5010] _id=6ab670d4485cab4c9554582f ts=2026-09-25T13:02:14.6570000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[5] _id=6ab3ce3d485cab4c954b848c ts=2026-09-23T13:03:57.5920000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[817] _id=6ab3d553485cab4c954c7e5b ts=2026-09-23T13:34:11.7540000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[971] _id=6ab3d682485cab4c954ca715 ts=2026-09-23T13:39:14.1160000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 31 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 31} 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[4] _id=6ab3ce3d485cab4c954b848a ts=2026-09-23T13:03:57.5910000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[439] _id=6ab3d2d4485cab4c954bfb9a ts=2026-09-23T13:23:32.9720000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[816] _id=6ab3d553485cab4c954c7e57 ts=2026-09-23T13:34:11.7520000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[438] _id=6ab3d2d4485cab4c954bfb94 ts=2026-09-23T13:23:32.5190000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[869] _id=6ab3d590485cab4c954c8669 ts=2026-09-23T13:35:12.3610000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[3263] _id=6ab520ae485cab4c95501b59 ts=2026-09-24T13:07:58.4500000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4355 | 0.001 | 0.49 | 159.213 | 11.644 | 257036.835 | 0.38 | 280 | 9 |
| PuzzlePieceVisibleEvent | 4201 | 0.0 | 0.026 | 144.29 | 0.861 | 261123.898 | 0.42 | 2688 | 7 |
| DialogueEvent | 2032 | 0.001 | 3.611 | 341.216 | 29.968 | 257526.479 | 0.18 | 592 | 7 |
| PlayerPositionEvent | 1682 | 9.439 | 10.0 | 411.956 | 10.029 | 256904.886 | 0.15 | 0 | 7 |
| argumentationNodeEvent | 329 | 0.019 | 0.438 | 2101.46 | 8.874 | 431926.209 | 0.03 | 68 | 4 |
| ObjectInterEvent | 245 | 0.001 | 9.703 | 2828.188 | 369.565 | 344876.212 | 0.02 | 5 | 9 |
| questEvent | 75 | 0.001 | 199.741 | 9241.765 | 83660.992 | 258407.697 | 0.01 | 14 | 11 |
| Soil Key Puzzle | 34 | 0.167 | 1.136 | 12769.949 | 85811.117 | 261121.119 | 0.0 | 0 | 4 |
| TopographicMapEvent | 34 | 0.004 | 10.273 | 15219.146 | 86626.448 | 258784.415 | 0.0 | 3 | 5 |
| gameWindowFocusEvent | 30 | 1.753 | 703.106 | 23051.347 | 84419.516 | 256899.529 | 0.0 | 0 | 16 |
| gameWindowUnfocusEvent | 22 | 1.823 | 577.956 | 27796.024 | 86036.126 | 256981.162 | 0.0 | 0 | 11 |
| DEBUGMenu | 18 | 300.342 | 1472.537 | 38417.495 | 112774.285 | 258859.901 | 0.0 | 0 | 16 |
| DaniEvent | 18 | 0.002 | 1.812 | 28903.562 | 198023.211 | 346556.419 | 0.0 | 5 | 3 |
| WaterChamberEvent | 16 | 4.721 | 24.398 | 29.372 | 70.44 | 101.916 | 2.04 | 0 | 0 |
| argumentationAnswerEvent | 12 | 8.259 | 38.109 | 57610.033 | 289687.356 | 431967.223 | 0.0 | 0 | 4 |
| argumentationEvent | 12 | 0.019 | 57.339 | 57611.039 | 289640.745 | 431932.321 | 0.0 | 2 | 4 |
| gameStartEvent | 12 | 302.362 | 43036.095 | 57628.367 | 164334.582 | 258862.199 | 0.0 | 0 | 10 |
| TerasGardenBox | 8 | 1.341 | 3.994 | 7.577 | 21.008 | 22.452 | 7.92 | 0 | 0 |
| SolarStillDesignEvent | 7 | 0.411 | 0.669 | 0.945 | 1.726 | 1.748 | 63.51 | 0 | 0 |
| chatEvent | 5 | 0.786 | 825.634 | 138100.364 | 448370.709 | 517396.117 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 1883.896 | 171628.909 | 230558.51 | 483509.342 | 518162.724 | 0.0 | 0 | 3 |
| argumentationToolEvent | 1 | 14.851 | 14.851 | 14.851 | 14.851 | 14.851 | 4.04 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| soilMachine | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 230 group(s), 302 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[1113] _id=6ab51d86485cab4c954fc123 ts=2026-09-24T12:54:28.9890000Z == 6aa413b141b41dbac0c7f1ef.jsonl[1114] _id=6ab51d86485cab4c954fc127 ts=2026-09-24T12:54:28.9890000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1127] _id=6ab51d88485cab4c954fc177 ts=2026-09-24T12:54:30.0720000Z == 6aa413b141b41dbac0c7f1ef.jsonl[1128] _id=6ab51d88485cab4c954fc17b ts=2026-09-24T12:54:30.0720000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1131] _id=6ab51d88485cab4c954fc199 ts=2026-09-24T12:54:30.5220000Z == 6aa413b141b41dbac0c7f1ef.jsonl[1132] _id=6ab51d88485cab4c954fc19d ts=2026-09-24T12:54:30.5220000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 23 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `400ms: 6aa413b141b41dbac0c7f1ef.jsonl[157] _id=6ab3d037485cab4c954b9243 ts=2026-09-23T13:12:23.2060000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[153] _id=6ab3d037485cab4c954b924e ts=2026-09-23T13:12:23.6060000Z`; `257ms: 6aa413b141b41dbac0c7f1ef.jsonl[153] _id=6ab3d037485cab4c954b924e ts=2026-09-23T13:12:23.6060000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[161] _id=6ab3d037485cab4c954b9256 ts=2026-09-23T13:12:23.8630000Z`; `203ms: 6aa413b141b41dbac0c7f1ef.jsonl[161] _id=6ab3d037485cab4c954b9256 ts=2026-09-23T13:12:23.8630000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[165] _id=6ab3d037485cab4c954b925e ts=2026-09-23T13:12:24.0660000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 888 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `10ms: 6aa413b141b41dbac0c7f1ef.jsonl[1107] _id=6ab51d86485cab4c954fc11d ts=2026-09-24T12:54:28.9790000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[1113] _id=6ab51d86485cab4c954fc123 ts=2026-09-24T12:54:28.9890000Z`; `83ms: 6aa413b141b41dbac0c7f1ef.jsonl[1114] _id=6ab51d86485cab4c954fc127 ts=2026-09-24T12:54:28.9890000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[1108] _id=6ab51d86485cab4c954fc12b ts=2026-09-24T12:54:29.0720000Z`; `22ms: 6aa413b141b41dbac0c7f1ef.jsonl[1126] _id=6ab51d87485cab4c954fc16f ts=2026-09-24T12:54:29.3780000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[1111] _id=6ab51d87485cab4c954fc173 ts=2026-09-24T12:54:29.4000000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `902ms: 6aa413b141b41dbac0c7f1ef.jsonl[860] _id=6ab3d585485cab4c954c84db ts=2026-09-23T13:35:01.1570000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[862] _id=6ab3d586485cab4c954c84ff ts=2026-09-23T13:35:02.0590000Z`; `36ms: 6aa413b141b41dbac0c7f1ef.jsonl[3320] _id=6ab5214e485cab4c955022f3 ts=2026-09-24T13:10:38.3780000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[3319] _id=6ab5214e485cab4c955022fb ts=2026-09-24T13:10:38.4140000Z`; `4ms: 6aa413b141b41dbac0c7f1ef.jsonl[3319] _id=6ab5214e485cab4c955022fb ts=2026-09-24T13:10:38.4140000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[3325] _id=6ab5214e485cab4c95502303 ts=2026-09-24T13:10:38.4180000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `39ms: 6aa413b141b41dbac0c7f1ef.jsonl[7587] _id=6aba6bda485cab4c9567fe99 ts=2026-09-28T13:30:02.3910000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[7468] _id=6aba6bdb485cab4c9567fea5 ts=2026-09-28T13:30:02.4300000Z`; `19ms: 6aa413b141b41dbac0c7f1ef.jsonl[11330] _id=6abd2687485cab4c958bcef3 ts=2026-09-30T15:11:03.3690000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[11393] _id=6abd2687485cab4c958bcefd ts=2026-09-30T15:11:03.3880000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 51 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `768ms: 6aa413b141b41dbac0c7f1ef.jsonl[622] _id=6ab3d3fe485cab4c954c36e5 ts=2026-09-23T13:28:30.6200000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[623] _id=6ab3d3ff485cab4c954c371c ts=2026-09-23T13:28:31.3880000Z`; `24ms: 6aa413b141b41dbac0c7f1ef.jsonl[632] _id=6ab3d40e485cab4c954c3a93 ts=2026-09-23T13:28:46.8380000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[633] _id=6ab3d40e485cab4c954c3a95 ts=2026-09-23T13:28:46.8620000Z`; `24ms: 6aa413b141b41dbac0c7f1ef.jsonl[638] _id=6ab3d410485cab4c954c3b17 ts=2026-09-23T13:28:48.8720000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[641] _id=6ab3d410485cab4c954c3b1b ts=2026-09-23T13:28:48.8960000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa413b141b41dbac0c7f1ef.jsonl[5010] _id=6ab670d4485cab4c9554582f ts=2026-09-25T13:02:14.6570000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[5011] _id=6ab670d4485cab4c95545833 ts=2026-09-25T13:02:14.6620000Z`; `2ms: 6aa413b141b41dbac0c7f1ef.jsonl[12956] _id=6abe60d4485cab4c95a5e04a ts=2026-10-01T13:32:04.2950000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[12954] _id=6abe60d4485cab4c95a5e056 ts=2026-10-01T13:32:04.2970000Z`; `3ms: 6aa413b141b41dbac0c7f1ef.jsonl[13091] _id=6abe61af485cab4c95a61dff ts=2026-10-01T13:35:43.4670000Z ~ 6aa413b141b41dbac0c7f1ef.jsonl[13092] _id=6abe61af485cab4c95a61e05 ts=2026-10-01T13:35:43.4700000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 71h 54m 
  - Evidence: 71h 54m: 6aa413b141b41dbac0c7f1ef.jsonl[5012] _id=6ab670cd485cab4c95545799 ts=2026-09-25T13:02:08.6810000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6830] _id=6aba63fd485cab4c95679599 ts=2026-09-28T12:56:28.5820000Z; 24h 9m: 6aa413b141b41dbac0c7f1ef.jsonl[1034] _id=6ab51cfe485cab4c954fbc63 ts=2026-09-24T12:52:14.2100000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5012] _id=6ab670cd485cab4c95545799 ts=2026-09-25T13:02:08.6810000Z; 23h 26m: 6aa413b141b41dbac0c7f1ef.jsonl[7912] _id=6aba6d4f485cab4c95680c07 ts=2026-09-28T13:36:15.5030000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8244] _id=6abbb6ed485cab4c957c19ca ts=2026-09-29T13:02:37.5250000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 15m 
  - Evidence: 96h 15m: 6aa413b141b41dbac0c7f1ef.jsonl[6051] _id=6ab6767a485cab4c9554e786 ts=2026-09-25T13:26:18.4720000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[9652] _id=6abbc036485cab4c957daa3b ts=2026-09-29T13:42:14.8910000Z; 47h 43m: 6aa413b141b41dbac0c7f1ef.jsonl[863] _id=6ab3d58c485cab4c954c85eb ts=2026-09-23T13:35:08.7420000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5714] _id=6ab674b0485cab4c9554ab29 ts=2026-09-25T13:18:40.2110000Z; 23m 44s: 6aa413b141b41dbac0c7f1ef.jsonl[90] _id=6ab3cff9485cab4c954b8d5a ts=2026-09-23T13:11:21.6100000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[868] _id=6ab3d58a485cab4c954c85a7 ts=2026-09-23T13:35:06.4530000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6aa413b141b41dbac0c7f1ef.jsonl[65] _id=6ab3cff5485cab4c954b8d19 ts=2026-09-23T13:11:17.3440000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[89] _id=6ab3cff5485cab4c954b8d1e ts=2026-09-23T13:11:17.3460000Z; 3ms: 6aa413b141b41dbac0c7f1ef.jsonl[5721] _id=6ab674b4485cab4c9554abc5 ts=2026-09-25T13:18:44.2840000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5722] _id=6ab674b4485cab4c9554abca ts=2026-09-25T13:18:44.2870000Z; 6ms: 6aa413b141b41dbac0c7f1ef.jsonl[5720] _id=6ab674b1485cab4c9554ab67 ts=2026-09-25T13:18:41.4690000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5719] _id=6ab674b1485cab4c9554ab6d ts=2026-09-25T13:18:41.4750000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 32m 
  - Evidence: 71h 32m: 6aa413b141b41dbac0c7f1ef.jsonl[5894] _id=6ab6760b485cab4c9554d394 ts=2026-09-25T13:24:27.3670000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6827] _id=6aba6403485cab4c9567959f ts=2026-09-28T12:56:33.8460000Z; 23h 31m: 6aa413b141b41dbac0c7f1ef.jsonl[4989] _id=6ab525f2485cab4c95511985 ts=2026-09-24T13:30:26.3360000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5097] _id=6ab670de485cab4c955459db ts=2026-09-25T13:02:25.6680000Z; 23h 22m: 6aa413b141b41dbac0c7f1ef.jsonl[8213] _id=6aba6e5a485cab4c9568184b ts=2026-09-28T13:40:42.4780000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8326] _id=6abbb710485cab4c957c1b06 ts=2026-09-29T13:03:12.7150000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 592 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[12348] _id=6abe5d26485cab4c95a499ca ts=2026-10-01T13:16:22.3860000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12349] _id=6abe5d26485cab4c95a499cf ts=2026-10-01T13:16:22.3870000Z; 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[12695] _id=6abe5ec3485cab4c95a537db ts=2026-10-01T13:23:14.9230000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12696] _id=6abe5ec3485cab4c95a537e9 ts=2026-10-01T13:23:14.9240000Z; 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[12923] _id=6abe60b0485cab4c95a5d5fe ts=2026-10-01T13:31:28.7760000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12921] _id=6abe60b0485cab4c95a5d607 ts=2026-10-01T13:31:28.7770000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 56m 
  - Evidence: 143h 56m: 6aa413b141b41dbac0c7f1ef.jsonl[815] _id=6ab3d504485cab4c954c6dab ts=2026-09-23T13:32:52.4740000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[9044] _id=6abbbd17485cab4c957d1096 ts=2026-09-29T13:28:55.1980000Z; 47h 40m: 6aa413b141b41dbac0c7f1ef.jsonl[9044] _id=6abbbd17485cab4c957d1096 ts=2026-09-29T13:28:55.1980000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11868] _id=6abe5b84485cab4c95a4515c ts=2026-10-01T13:09:24.1070000Z; 31m 23s: 6aa413b141b41dbac0c7f1ef.jsonl[11868] _id=6abe5b84485cab4c95a4515c ts=2026-10-01T13:09:24.1070000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[13184] _id=6abe62e0485cab4c95a67a97 ts=2026-10-01T13:40:48.0030000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 71h 23m 
  - Evidence: 71h 23m: 6aa413b141b41dbac0c7f1ef.jsonl[6816] _id=6ab67862485cab4c95552706 ts=2026-09-25T13:34:26.4190000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6850] _id=6aba646f485cab4c956795ed ts=2026-09-28T12:58:23.2540000Z; 23h 34m: 6aa413b141b41dbac0c7f1ef.jsonl[4931] _id=6ab5253b485cab4c9550f8b5 ts=2026-09-24T13:27:23.8030000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5014] _id=6ab670d4485cab4c95545815 ts=2026-09-25T13:02:14.6030000Z; 23h 21m: 6aa413b141b41dbac0c7f1ef.jsonl[8212] _id=6aba6e58485cab4c9568183f ts=2026-09-28T13:40:40.9440000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8225] _id=6abbb6f1485cab4c957c19ce ts=2026-09-29T13:02:40.0020000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 280 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[1048] _id=6ab51d05485cab4c954fbc75 ts=2026-09-24T12:52:20.5000000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[1036] _id=6ab51d05485cab4c954fbc77 ts=2026-09-24T12:52:20.5010000Z; 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[10885] _id=6abd0ff0485cab4c958883aa ts=2026-09-30T13:34:39.3650000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10906] _id=6abd0ff0485cab4c958883bd ts=2026-09-30T13:34:39.3660000Z; 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[11514] _id=6abe5802485cab4c95a3fe47 ts=2026-10-01T12:54:23.2640000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11515] _id=6abe5802485cab4c95a3fe4b ts=2026-10-01T12:54:23.2650000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 47m 
  - Evidence: 95h 47m: 6aa413b141b41dbac0c7f1ef.jsonl[4695] _id=6ab52471485cab4c9550cc47 ts=2026-09-24T13:24:01.3360000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7030] _id=6aba679d485cab4c9567b5b6 ts=2026-09-28T13:11:57.5480000Z; 23h 25m: 6aa413b141b41dbac0c7f1ef.jsonl[8107] _id=6aba6d87485cab4c95680f21 ts=2026-09-28T13:37:11.0820000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8266] _id=6abbb703485cab4c957c1a48 ts=2026-09-29T13:02:59.1530000Z; 23h 19m: 6aa413b141b41dbac0c7f1ef.jsonl[9617] _id=6abbbfe6485cab4c957d9f08 ts=2026-09-29T13:40:54.2640000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[9661] _id=6abd07d9485cab4c958679a9 ts=2026-09-30T13:00:09.8300000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[10810] _id=6abd0f83485cab4c9588544b ts=2026-09-30T13:32:51.7530000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10804] _id=6abd0f84485cab4c95885453 ts=2026-09-30T13:32:51.7540000Z; 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[11210] _id=6abd2558485cab4c958bb3ed ts=2026-09-30T15:06:00.1200000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11216] _id=6abd2558485cab4c958bb3f1 ts=2026-09-30T15:06:00.1210000Z; 2ms: 6aa413b141b41dbac0c7f1ef.jsonl[11252] _id=6abd2586485cab4c958bb615 ts=2026-09-30T15:06:46.6690000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11244] _id=6abd2586485cab4c958bb617 ts=2026-09-30T15:06:46.6710000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa413b141b41dbac0c7f1ef.jsonl[6819] _id=6ab67873485cab4c95552900 ts=2026-09-25T13:34:43.7020000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6826] _id=6aba6403485cab4c9567959b ts=2026-09-28T12:56:28.5880000Z; 23h 31m: 6aa413b141b41dbac0c7f1ef.jsonl[4990] _id=6ab525f9485cab4c95511b01 ts=2026-09-24T13:30:33.8620000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5013] _id=6ab670d4485cab4c95545811 ts=2026-09-25T13:02:08.6900000Z; 23h 21m: 6aa413b141b41dbac0c7f1ef.jsonl[8219] _id=6aba6e62485cab4c95681889 ts=2026-09-28T13:40:50.1500000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8224] _id=6abbb6f1485cab4c957c19cc ts=2026-09-29T13:02:37.5400000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 72h 32m 
  - Evidence: 72h 32m: 6aa413b141b41dbac0c7f1ef.jsonl[5458] _id=6ab67156485cab4c955463ef ts=2026-09-25T13:04:12.5250000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7915] _id=6aba6d51485cab4c95680c13 ts=2026-09-28T13:36:16.4230000Z; 23h 43m: 6aa413b141b41dbac0c7f1ef.jsonl[10588] _id=6abd0df5485cab4c9587a3fa ts=2026-09-30T13:26:08.0480000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11883] _id=6abe5b9f485cab4c95a4592e ts=2026-10-01T13:09:50.4290000Z; 23h 38m: 6aa413b141b41dbac0c7f1ef.jsonl[9607] _id=6abbbfd5485cab4c957d9cd0 ts=2026-09-29T13:40:36.8720000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10438] _id=6abd0c51485cab4c9586e50f ts=2026-09-30T13:19:11.9340000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2688 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1ef.jsonl[10438] _id=6abd0c51485cab4c9586e50f ts=2026-09-30T13:19:11.9340000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10439] _id=6abd0c51485cab4c9586e515 ts=2026-09-30T13:19:11.9340000Z; 0ms: 6aa413b141b41dbac0c7f1ef.jsonl[10439] _id=6abd0c51485cab4c9586e515 ts=2026-09-30T13:19:11.9340000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10440] _id=6abd0c51485cab4c9586e519 ts=2026-09-30T13:19:11.9340000Z; 0ms: 6aa413b141b41dbac0c7f1ef.jsonl[10440] _id=6abd0c51485cab4c9586e519 ts=2026-09-30T13:19:11.9340000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10434] _id=6abd0c51485cab4c9586e523 ts=2026-09-30T13:19:11.9340000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 72h 32m 
  - Evidence: 72h 32m: 6aa413b141b41dbac0c7f1ef.jsonl[5109] _id=6ab6710d485cab4c95545e7f ts=2026-09-25T13:03:11.9420000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7833] _id=6aba6d11485cab4c95680a6d ts=2026-09-28T13:35:13.0610000Z; 24h 0m: 6aa413b141b41dbac0c7f1ef.jsonl[7889] _id=6aba6d2f485cab4c95680b59 ts=2026-09-28T13:35:43.2310000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[9159] _id=6abbbecd485cab4c957d6f98 ts=2026-09-29T13:36:13.0900000Z; 23h 44m: 6aa413b141b41dbac0c7f1ef.jsonl[3483] _id=6ab52327485cab4c95507b39 ts=2026-09-24T13:18:31.4780000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5110] _id=6ab6710a485cab4c95545e5d ts=2026-09-25T13:03:09.4270000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 71h 53m 
  - Evidence: 71h 53m: 6aa413b141b41dbac0c7f1ef.jsonl[5718] _id=6ab674b0485cab4c9554ab25 ts=2026-09-25T13:18:40.2050000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7022] _id=6aba6790485cab4c9567b503 ts=2026-09-28T13:11:44.6200000Z; 24h 4m: 6aa413b141b41dbac0c7f1ef.jsonl[3359] _id=6ab521d9485cab4c9550322b ts=2026-09-24T13:12:57.8980000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5689] _id=6ab67466485cab4c95549fcd ts=2026-09-25T13:17:26.2160000Z; 24h 3m: 6aa413b141b41dbac0c7f1ef.jsonl[7127] _id=6aba6835485cab4c9567bd25 ts=2026-09-28T13:14:29.7260000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8833] _id=6abbba81485cab4c957c79f6 ts=2026-09-29T13:17:53.6290000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.004s..0.036s shown 
  - Evidence: 4ms: 6aa413b141b41dbac0c7f1ef.jsonl[3319] _id=6ab5214e485cab4c955022fb ts=2026-09-24T13:10:38.4140000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[3325] _id=6ab5214e485cab4c95502303 ts=2026-09-24T13:10:38.4180000Z; 20ms: 6aa413b141b41dbac0c7f1ef.jsonl[3323] _id=6ab5214e485cab4c955022ef ts=2026-09-24T13:10:38.3580000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[3320] _id=6ab5214e485cab4c955022f3 ts=2026-09-24T13:10:38.3780000Z; 36ms: 6aa413b141b41dbac0c7f1ef.jsonl[3320] _id=6ab5214e485cab4c955022f3 ts=2026-09-24T13:10:38.3780000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[3319] _id=6ab5214e485cab4c955022fb ts=2026-09-24T13:10:38.4140000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6aa413b141b41dbac0c7f1ef.jsonl[682] _id=6ab3d450485cab4c954c4961 ts=2026-09-23T13:29:52.2760000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7561] _id=6aba6baf485cab4c9567fca1 ts=2026-09-28T13:29:19.4990000Z; 48h 7m: 6aa413b141b41dbac0c7f1ef.jsonl[7586] _id=6aba6bda485cab4c9567fe97 ts=2026-09-28T13:30:02.3690000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10991] _id=6abd10b6485cab4c9588c9e1 ts=2026-09-30T13:37:58.9240000Z; 22h 19m: 6aa413b141b41dbac0c7f1ef.jsonl[11392] _id=6abd2687485cab4c958bceef ts=2026-09-30T15:11:03.3550000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12876] _id=6abe608c485cab4c95a5c9d1 ts=2026-10-01T13:30:52.4770000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6aa413b141b41dbac0c7f1ef.jsonl[677] _id=6ab3d450485cab4c954c4965 ts=2026-09-23T13:29:52.2970000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7516] _id=6aba6b8c485cab4c9567fb1f ts=2026-09-28T13:28:44.6180000Z; 48h 7m: 6aa413b141b41dbac0c7f1ef.jsonl[7468] _id=6aba6bdb485cab4c9567fea5 ts=2026-09-28T13:30:02.4300000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10927] _id=6abd107e485cab4c9588b836 ts=2026-09-30T13:37:02.7950000Z; 22h 19m: 6aa413b141b41dbac0c7f1ef.jsonl[11393] _id=6abd2687485cab4c958bcefd ts=2026-09-30T15:11:03.3880000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12882] _id=6abe606a485cab4c95a5becb ts=2026-10-01T13:30:18.7520000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.039s shown 
  - Evidence: 19ms: 6aa413b141b41dbac0c7f1ef.jsonl[11330] _id=6abd2687485cab4c958bcef3 ts=2026-09-30T15:11:03.3690000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11393] _id=6abd2687485cab4c958bcefd ts=2026-09-30T15:11:03.3880000Z; 39ms: 6aa413b141b41dbac0c7f1ef.jsonl[7587] _id=6aba6bda485cab4c9567fe99 ts=2026-09-28T13:30:02.3910000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7468] _id=6aba6bdb485cab4c9567fea5 ts=2026-09-28T13:30:02.4300000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6aa413b141b41dbac0c7f1ef.jsonl[676] _id=6ab3d44d485cab4c954c48bb ts=2026-09-23T13:29:49.3040000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7506] _id=6aba6b83485cab4c9567fae3 ts=2026-09-28T13:28:35.5130000Z; 48h 6m: 6aa413b141b41dbac0c7f1ef.jsonl[7585] _id=6aba6bd8485cab4c9567fe91 ts=2026-09-28T13:30:00.7400000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[10967] _id=6abd107b485cab4c9588b753 ts=2026-09-30T13:36:59.8100000Z; 22h 19m: 6aa413b141b41dbac0c7f1ef.jsonl[11329] _id=6abd2686485cab4c958bcec9 ts=2026-09-30T15:11:02.1270000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12878] _id=6abe6068485cab4c95a5be39 ts=2026-10-01T13:30:16.0990000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 68 interval(s) ≤ 0.019s..0.021s shown 
  - Evidence: 19ms: 6aa413b141b41dbac0c7f1ef.jsonl[11318] _id=6abd2643485cab4c958bc731 ts=2026-09-30T15:09:55.3650000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11321] _id=6abd2643485cab4c958bc737 ts=2026-09-30T15:09:55.3840000Z; 20ms: 6aa413b141b41dbac0c7f1ef.jsonl[7509] _id=6aba6b88485cab4c9567fb0b ts=2026-09-28T13:28:40.3610000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[7505] _id=6aba6b88485cab4c9567fb0d ts=2026-09-28T13:28:40.3810000Z; 21ms: 6aa413b141b41dbac0c7f1ef.jsonl[612] _id=6ab3d3df485cab4c954c3038 ts=2026-09-23T13:28:00.0490000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[611] _id=6ab3d3e0485cab4c954c303e ts=2026-09-23T13:28:00.0700000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 43m 
  - Evidence: 143h 43m: 6aa413b141b41dbac0c7f1ef.jsonl[6054] _id=6ab67684485cab4c9554e8e2 ts=2026-09-25T13:26:28.9000000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[11872] _id=6abe5b99485cab4c95a456d6 ts=2026-10-01T13:09:45.0170000Z; 47h 51m: 6aa413b141b41dbac0c7f1ef.jsonl[872] _id=6ab3d58d485cab4c954c8613 ts=2026-09-23T13:35:09.6180000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6052] _id=6ab6767a485cab4c9554e792 ts=2026-09-25T13:26:18.6950000Z; 13m 45s: 6aa413b141b41dbac0c7f1ef.jsonl[11872] _id=6abe5b99485cab4c95a456d6 ts=2026-10-01T13:09:45.0170000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12702] _id=6abe5ed2485cab4c95a54009 ts=2026-10-01T13:23:30.6510000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 71h 54m 
  - Evidence: 71h 54m: 6aa413b141b41dbac0c7f1ef.jsonl[5006] _id=6ab670c6485cab4c955456d5 ts=2026-09-25T13:02:01.1670000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6825] _id=6aba63f8485cab4c95679597 ts=2026-09-28T12:56:23.3660000Z; 24h 9m: 6aa413b141b41dbac0c7f1ef.jsonl[1029] _id=6ab51cf7485cab4c954fbc53 ts=2026-09-24T12:52:07.3630000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5006] _id=6ab670c6485cab4c955456d5 ts=2026-09-25T13:02:01.1670000Z; 23h 56m: 6aa413b141b41dbac0c7f1ef.jsonl[6895] _id=6aba664c485cab4c9567a27f ts=2026-09-28T13:06:20.6570000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8223] _id=6abbb6e2485cab4c957c19c8 ts=2026-09-29T13:02:26.1260000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa413b141b41dbac0c7f1ef.jsonl[6818] _id=6ab67873485cab4c95552910 ts=2026-09-25T13:34:43.8370000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6824] _id=6aba63f8485cab4c95679595 ts=2026-09-28T12:56:23.3660000Z; 23h 31m: 6aa413b141b41dbac0c7f1ef.jsonl[4992] _id=6ab525fe485cab4c95511bbd ts=2026-09-24T13:30:38.4330000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5005] _id=6ab670c6485cab4c955456d1 ts=2026-09-25T13:02:01.1660000Z; 23h 21m: 6aa413b141b41dbac0c7f1ef.jsonl[8218] _id=6aba6e60485cab4c95681875 ts=2026-09-28T13:40:48.3190000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8243] _id=6abbb6e2485cab4c957c19c6 ts=2026-09-29T13:02:26.1250000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 23m 
  - Evidence: 71h 23m: 6aa413b141b41dbac0c7f1ef.jsonl[6821] _id=6ab67875485cab4c95552942 ts=2026-09-25T13:34:45.9650000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6847] _id=6aba644b485cab4c956795d7 ts=2026-09-28T12:57:47.1270000Z; 23h 54m: 6aa413b141b41dbac0c7f1ef.jsonl[8220] _id=6aba6e62485cab4c9568188f ts=2026-09-28T13:40:50.2680000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[9124] _id=6abbbe80485cab4c957d62d4 ts=2026-09-29T13:34:55.9880000Z; 23h 50m: 6aa413b141b41dbac0c7f1ef.jsonl[4991] _id=6ab525fe485cab4c95511bae ts=2026-09-24T13:30:38.4170000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5841] _id=6ab6755c485cab4c9554b99c ts=2026-09-25T13:21:32.2530000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 46m 
  - Evidence: 71h 46m: 6aa413b141b41dbac0c7f1ef.jsonl[5555] _id=6ab67299485cab4c95547781 ts=2026-09-25T13:09:46.1420000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[6840] _id=6aba6403485cab4c9567959d ts=2026-09-28T12:56:33.8390000Z; 23h 34m: 6aa413b141b41dbac0c7f1ef.jsonl[4935] _id=6ab5254b485cab4c9550fca9 ts=2026-09-24T13:27:39.9340000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[5010] _id=6ab670d4485cab4c9554582f ts=2026-09-25T13:02:14.6570000Z; 23h 26m: 6aa413b141b41dbac0c7f1ef.jsonl[7920] _id=6aba6d52485cab4c95680c25 ts=2026-09-28T13:36:18.3690000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[8238] _id=6abbb6f2485cab4c957c19e6 ts=2026-09-29T13:02:41.5510000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[12346] _id=6abe5d26485cab4c95a499bb ts=2026-10-01T13:16:22.0020000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12347] _id=6abe5d26485cab4c95a499c3 ts=2026-10-01T13:16:22.0030000Z; 1ms: 6aa413b141b41dbac0c7f1ef.jsonl[12620] _id=6abe5e40485cab4c95a4ef56 ts=2026-10-01T13:21:03.9890000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12618] _id=6abe5e40485cab4c95a4ef68 ts=2026-10-01T13:21:03.9900000Z; 2ms: 6aa413b141b41dbac0c7f1ef.jsonl[12956] _id=6abe60d4485cab4c95a5e04a ts=2026-10-01T13:32:04.2950000Z -> 6aa413b141b41dbac0c7f1ef.jsonl[12954] _id=6abe60d4485cab4c95a5e056 ts=2026-10-01T13:32:04.2970000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[540] _id=6ab3d38d485cab4c954c187e ts=2026-09-23T13:26:37.6430000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[693] _id=6ab3d461485cab4c954c4d91 ts=2026-09-23T13:30:09.2820000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[4832] _id=6ab52517485cab4c9550ee87 ts=2026-09-24T13:26:47.2190000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 156 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[1171] _id=6ab51dad485cab4c954fc50b ts=2026-09-24T12:54:51.3000000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1172] _id=6ab51dad485cab4c954fc50f ts=2026-09-24T12:54:51.5840000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1462] _id=6ab51dbe485cab4c954fc7b2 ts=2026-09-24T12:55:25.6870000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 476 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[1196] _id=6ab51d9f485cab4c954fc305 ts=2026-09-24T12:53:27.0520000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1185] _id=6ab51da2485cab4c954fc351 ts=2026-09-24T12:53:28.2230000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1207] _id=6ab51da2485cab4c954fc355 ts=2026-09-24T12:53:28.2230000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[7468] _id=6aba6bdb485cab4c9567fea5 ts=2026-09-28T13:30:02.4300000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[633] _id=6ab3d40e485cab4c954c3a95 ts=2026-09-23T13:28:46.8620000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[641] _id=6ab3d410485cab4c954c3b1b ts=2026-09-23T13:28:48.8960000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[644] _id=6ab3d412485cab4c954c3b4f ts=2026-09-23T13:28:50.0580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[11872] _id=6abe5b99485cab4c95a456d6 ts=2026-10-01T13:09:45.0170000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[12702] _id=6abe5ed2485cab4c95a54009 ts=2026-10-01T13:23:30.6510000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[5503] _id=6ab671dd485cab4c95546b2b ts=2026-09-25T13:06:38.4200000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[9670] _id=6abd07c5485cab4c9586789f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 584 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[1332] _id=6ab51dab485cab4c954fc4c9 ts=2026-09-24T12:54:46.4410000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1433] _id=6ab51db8485cab4c954fc6dd ts=2026-09-24T12:55:19.1160000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1429] _id=6ab51db8485cab4c954fc6e5 ts=2026-09-24T12:55:19.2280000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 795 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[1215] _id=6ab51da0485cab4c954fc315 ts=2026-09-24T12:53:27.0780000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1176] _id=6ab51da1485cab4c954fc329 ts=2026-09-24T12:53:27.1220000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1222] _id=6ab51da1485cab4c954fc32d ts=2026-09-24T12:53:27.1310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[3319] _id=6ab5214e485cab4c955022fb ts=2026-09-24T13:10:38.4140000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[3325] _id=6ab5214e485cab4c95502303 ts=2026-09-24T13:10:38.4180000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[3355] _id=6ab521d0485cab4c95503053 ts=2026-09-24T13:12:48.3880000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[11313] _id=6abd263d485cab4c958bc673 ts=2026-09-30T15:09:49.2010000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[7541] _id=6aba6b9d485cab4c9567fbf9 ts=2026-09-28T13:29:01.4190000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Open' (totals: 10 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 380 start, 373 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 196 unmatched 'BecameCameraCentered' (totals: 783 open, 743 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 140 unmatched 'BecameVisible' (totals: 1170 open, 1506 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 16 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 45 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 422 of 13184 adjacent _id pairs reverse in client time; worst 87.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1ef.jsonl[1174] _id=6ab51d9e485cab4c954fc2ef ts=2026-09-24T12:54:54.2380000Z`; `6aa413b141b41dbac0c7f1ef.jsonl[1193] _id=6ab51d9f485cab4c954fc2f5 ts=2026-09-24T12:53:26.9950000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -90.83s, max +3.04s over 13185 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1ef\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4356 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1691); Unit 3 Dev (587); Unit 4 Dev - Dungeon (489); Unit 1 Dev (353); Unit 5 Dev - Dungeon (325); Unit 4 Dev (317); Unit 3 Dungeon Dev (257); Unit 4 Dev - Anderson Base (235); Unit 5 Dev (102)
- **Intervals:** median 0.49s (p5 0.04s / p95 11.64s, n=4355)
- **Fields under `data`:**

```text
data.Value  (string, 4356/4356 records)
    "pressed"  x4356
data.actionType  (string, 4356/4356 records)
    "Move"  x2783
    "Jump"  x768
    "Interact"  x438
    "Sprint"  x243
    "Hoverboard"  x53
    "Ascend"  x40
    "Map"  x15
    "Pause"  x9
    "SkipCinematic"  x7
data.key  (string, 4356/4356 records, 4 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4356/4356 records)
    "Player"  x3966
    "Drone"  x390
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4202 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3186); Unit 4 Dev (400); Unit 3 Dungeon Dev (316); Unit 5 Dev - Dungeon (300)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.86s, n=4201)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4202/4202 records)
    "BecameInvisible"  x1506
    "BecameVisible"  x1170
    "BecameCameraCentered"  x783
    "BecameCameraUncentered"  x743
data.pieceId  (string, 4202/4202 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4202/4202 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2033 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (551); Unit 3 Dev (327); Unit 4 Dev (269); Unit 5 Dev (213); Unit 1 Dev (193); Unit 3 Dungeon Dev (154); Unit 4 Dev - Anderson Base (152); Unit 4 Dev - Dungeon (102); Unit 5 Dev - Dungeon (72)
- **eventKey:** present on 1280 of 2033 records
- **Intervals:** median 3.61s (p5 0.00s / p95 29.97s, n=2032)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1280; [conversationId, dialogueEventType] x753
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2033/2033 records)
    numeric range 8 .. 118 (53 unique)
data.dialogueEventType  (string, 2033/2033 records)
    "DialogueNodeEvent"  x1280
    "DialogueStartEvent"  x380
    "DialogueFinishEvent"  x373
data.nodeId  (number, 1280/2033 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1694 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (499); Unit 3 Dev (252); Unit 4 Dev (246); Unit 1 Dev (169); Unit 4 Dev - Dungeon (122); Unit 3 Dungeon Dev (111); Unit 4 Dev - Anderson Base (111); Unit 5 Dev (102); Unit 5 Dev - Dungeon (82)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1682)
- **Fields under `data`:**

```text
data.position  (object, 1694/1694 records)
data.position.x  (number, 1694/1694 records)
    numeric range -681.694 .. 2453.27 (607 unique)
data.position.y  (number, 1694/1694 records)
    numeric range -3497.89 .. 941.614 (459 unique)
data.position.z  (number, 1694/1694 records)
    numeric range -2163.72 .. 1922.06 (604 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 330 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (175); Unit 3 Dev (69); Unit 1 Dev (46); Unit 5 Dev (40)
- **Intervals:** median 0.44s (p5 0.03s / p95 8.87s, n=329)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 330/330 records)
    "argumentationNodeHoverEnd"  x152
    "argumentationNodeHoverStart"  x147
    "argumentationNodeAdd"  x25
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 330/330 records)
    "Unit 4 - Flooding"  x175
    "Unit 3 - Pollution Upstream"  x69
    "Unit 5"  x40
    "Unit 1 - Argumentation Tutorial"  x23
    "Unit 1 - Freshwater"  x23
data.nodeName  (string, 330/330 records)
    "I"  x49
    "1"  x42
    "B"  x39
    "A"  x38
    "C"  x31
    "II"  x29
    "D"  x28
    "3"  x27
    "2"  x26
    "4"  x16
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 246 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (70); Unit 2 Prod (Refactor) (41); Unit 3 Dungeon Dev (32); Unit 1 Dev (21); Unit 4 Dev (20); Unit 4 Dev - Anderson Base (18); Unit 5 Dev (17); Unit 5 Dev - Dungeon (16); Unit 3 Dev (11)
- **Intervals:** median 9.70s (p5 0.28s / p95 369.57s, n=245)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 246/246 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 246/246 records)
    89 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 1 Dev (12); Unit 4 Dev - Dungeon (10); Unit 3 Dev (9); Unit 4 Dev (9); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 199.74s (p5 0.00s / p95 83660.99s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x45; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x45
    "questFinishEvent"  x31
data.questID  (string, 76/76 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/76 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 35 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (10); Unit 4 Dev (10)
- **Intervals:** median 1.14s (p5 0.19s / p95 85811.12s, n=34)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x27; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/35 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/35 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 27/35 records)
    "RightDrag"  x17
    "LeftDrag"  x10
data.currentSoilType  (string, 27/35 records)
    "CLAY"  x5
    "CLAYROCK"  x5
    "CLAYSAND"  x5
    "SAND"  x5
    "SANDGRAVEL"  x3
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 27/35 records)
    "false"  x21
    "true"  x6
data.waterLevelStatus  (string, 27/35 records)
    "Proper"  x12
    "TooHigh"  x10
    "TooLow"  x5
data.waterRetentionChange  (string, 27/35 records)
    "Increase"  x11
    "Decrease"  x10
    "NoChange"  x6
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 35 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 3 Dev (10)
- **Intervals:** median 10.27s (p5 0.03s / p95 86626.45s, n=34)
- **`data` key-set variants:** [actionType, featureUsed] x30; [actionType, featureUsed, location] x5
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "MapOpenEvent"  x16
    "MapCloseEvent"  x14
    "WaypointSetEvent"  x3
    "WaypointMoveEvent"  x2
data.featureUsed  (string, 35/35 records)
    "Map"  x30
    "Waypoint"  x5
data.location  (object, 5/35 records)
data.location.x  (number, 5/35 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/35 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/35 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 31 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (11); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dev (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 703.11s (p5 5.20s / p95 84419.52s, n=30)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 31/31 records)
    true  x31
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 23 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 4 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 577.96s (p5 1.97s / p95 86036.13s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 19 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 4 Dev (4); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1472.54s (p5 528.58s / p95 112774.29s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "DebugMenuStateChanged"  x19
data.isOpened  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `DaniEvent` — 19 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 1 Dev (6); Unit 4 Dev - Dungeon (3)
- **Intervals:** median 1.81s (p5 0.00s / p95 198023.21s, n=18)
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "Open"  x10
    "Close"  x9
data.toolName  (string, 19/19 records, 14 empty-string)
    ""  x14
    "Settings"  x5
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `WaterChamberEvent` — 17 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (17)
- **Intervals:** median 24.40s (p5 4.82s / p95 70.44s, n=16)
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "On"  x14
    "Off"  x3
data.floor  (string, 17/17 records)
    "3"  x6
    "4"  x5
    "1"  x3
    "2"  x3
data.machineNumber  (string, 17/17 records)
    "One"  x16
    "Two"  x1
data.machineType  (string, 17/17 records)
    "Condenser"  x8
    "Evaporator"  x6
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 17/17 records)
    "2"  x8
    "1"  x4
    "3"  x3
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 13 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (8); Unit 1 Dev (2); Unit 3 Dev (2); Unit 5 Dev (1)
- **Intervals:** median 38.11s (p5 15.05s / p95 289687.36s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "submitAnswerEvent"  x13
data.answerSubmitted  (string, 13/13 records)
    "A,1,I"  x2
    "A,5,I"  x1
    "A,C,B,2,II"  x1
    "A,C,D,2,II"  x1
    "C,2,II"  x1
    "C,A,2,II"  x1
    "C,B,2,II"  x1
    "C,D,3,II"  x1
    "D,1,II"  x1
    "D,2,II"  x1
    "D,4,II"  x1
    "I"  x1
data.argumentationTitle  (string, 13/13 records)
    "Unit 4 - Flooding"  x8
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 57.34s (p5 0.03s / p95 289640.75s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 13/13 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 13/13 records)
    "Unit 4 - Flooding"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 43036.10s (p5 464.57s / p95 164334.58s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 3.99s (p5 1.39s / p95 21.01s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x4
data.boxId  (string, 9/9 records)
    "0"  x5
    "1"  x2
    "2"  x2
data.soilType  (string, 9/9 records)
    "Sand"  x4
    "Gravel"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 0.67s (p5 0.45s / p95 1.73s, n=7)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x7; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "optionSelected"  x7
    "DesignSubmitted"  x1
data.designSelections  (object, 1/8 records)
data.designSelections.glassRoofTemperature  (string, 1/8 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/8 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/8 records)
    "Tilted Out"  x1
data.featureUsed  (string, 8/8 records)
    "RoofStyle"  x4
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 7/8 records, 1 empty-string)
    "Tilted Out"  x2
    ""  x1
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 825.63s (p5 2.67s / p95 448370.71s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x4
    "Open"  x2
data.chatID  (string, 6/6 records)
    "NA"  x4
    "[16-3]"  x1
    "[21-73, 21-75, 21-76, 23-0, 23-28]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 171628.91s (p5 18858.40s / p95 483509.34s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 14.85s (p5 14.85s / p95 14.85s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

### `soilMachine` — 1 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "ChangeCanister"  x1
data.canisterType  (string, 1/1 records)
    "Gravel"  x1
data.floor  (string, 1/1 records)
    "5"  x1
data.machine  (string, 1/1 records)
    "2"  x1
data.row  (string, 1/1 records)
    "TopRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (15 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (2x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (5x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*