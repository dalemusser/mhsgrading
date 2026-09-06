# MHS Gameplay Log Audit Report — build 09-03-26-3

## 1. Build Information

- **Build ID:** 09-03-26-3
- **Game version string(s) in log:** 2.5.8, 2.6.3, 20260721-11840, 20260902-12353
- **Audit date:** 2026-09-06
- **Log file(s):** wenyi090326-3.stratalog.logdata.json
- **Records:** 11537 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6a9a0779e2ada9cb13ea75c0
- **Time span:** 2026-09-05T21:10:39.937000+00:00 .. 2026-09-06T00:00:16.993000+00:00 (2h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-03-26-3.yaml
- **Baseline:** snapshot build-log-qa\reports\08-31-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 11537 records, 12 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 97 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DialogueEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DaniEvent`: event type present in baseline 08-31-26 but absent now
  - WARNING/Medium `TerasGardenBox`: baseline field(s) absent this build
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3410 | 29.56 | 1 | 4 | 0 | 2026-09-05T21:37:16.727000+00:00 | 2026-09-05T23:44:03.614000+00:00 | 2h 6m |
| InputEvent | 3182 | 27.58 | 1 | 9 | 0 | 2026-09-05T21:12:09.234000+00:00 | 2026-09-06T00:00:16.993000+00:00 | 2h 48m |
| DialogueEvent | 2508 | 21.74 | 1 | 9 | 1539 | 2026-09-05T21:11:02.332000+00:00 | 2026-09-06T00:00:03.520000+00:00 | 2h 49m |
| PlayerPositionEvent | 974 | 8.44 | 1 | 9 | 0 | 2026-09-05T21:10:45.693000+00:00 | 2026-09-06T00:00:15.757000+00:00 | 2h 49m |
| argumentationNodeEvent | 743 | 6.44 | 1 | 5 | 0 | 2026-09-05T21:18:37.536000+00:00 | 2026-09-05T23:56:44.208000+00:00 | 2h 38m |
| ObjectInterEvent | 240 | 2.08 | 1 | 9 | 0 | 2026-09-05T21:10:45.695000+00:00 | 2026-09-06T00:00:16.993000+00:00 | 2h 49m |
| questEvent | 82 | 0.71 | 1 | 9 | 82 | 2026-09-05T21:11:02.328000+00:00 | 2026-09-05T23:59:31.704000+00:00 | 2h 48m |
| Soil Key Puzzle | 74 | 0.64 | 1 | 3 | 0 | 2026-09-05T21:40:28.157000+00:00 | 2026-09-05T22:59:13.192000+00:00 | 1h 18m |
| TopographicMapEvent | 65 | 0.56 | 1 | 2 | 0 | 2026-09-05T21:37:34.703000+00:00 | 2026-09-05T22:49:21.936000+00:00 | 1h 11m |
| argumentationAnswerEvent | 50 | 0.43 | 1 | 5 | 0 | 2026-09-05T21:18:41.988000+00:00 | 2026-09-05T23:56:45.641000+00:00 | 2h 38m |
| WaterChamberEvent | 43 | 0.37 | 1 | 1 | 0 | 2026-09-05T23:43:57.817000+00:00 | 2026-09-05T23:52:20.400000+00:00 | 8m 22s |
| soilMachine | 36 | 0.31 | 1 | 1 | 0 | 2026-09-05T23:10:32.540000+00:00 | 2026-09-05T23:20:07.925000+00:00 | 9m 35s |
| gameWindowUnfocusEvent | 35 | 0.3 | 1 | 11 | 0 | 2026-09-05T21:10:43.298000+00:00 | 2026-09-05T23:57:17.929000+00:00 | 2h 46m |
| gameWindowFocusEvent | 33 | 0.29 | 1 | 11 | 0 | 2026-09-05T21:10:45.141000+00:00 | 2026-09-05T23:57:40.562000+00:00 | 2h 46m |
| argumentationEvent | 18 | 0.16 | 1 | 5 | 0 | 2026-09-05T21:18:36.759000+00:00 | 2026-09-05T23:56:45.646000+00:00 | 2h 38m |
| argumentationToolEvent | 12 | 0.1 | 1 | 3 | 0 | 2026-09-05T21:18:36.074000+00:00 | 2026-09-05T22:28:29.800000+00:00 | 1h 9m |
| gameStartEvent | 8 | 0.07 | 1 | 1 | 0 | 2026-09-05T21:10:39.937000+00:00 | 2026-09-05T23:36:25.419000+00:00 | 2h 25m |
| TerasGardenBox | 6 | 0.05 | 1 | 1 | 0 | 2026-09-05T23:32:25.220000+00:00 | 2026-09-05T23:32:58.035000+00:00 | 32.8s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-09-05T21:34:41.060000+00:00 | 2026-09-06T00:00:16.991000+00:00 | 2h 25m |
| DEBUGMenu | 4 | 0.03 | 1 | 2 | 0 | 2026-09-05T22:36:53.195000+00:00 | 2026-09-05T23:46:55.914000+00:00 | 1h 10m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-09-05T23:58:08.180000+00:00 | 2026-09-05T23:58:13.720000+00:00 | 5.5s |
| crash | 3 | 0.03 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-09-05T23:36:27.269000+00:00 | 2026-09-05T23:53:07.703000+00:00 | 16m 40s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DaniEvent` — event type present in baseline 08-31-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 42 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — baseline field(s) absent this build. 
  - Observed: data.boxID 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.134s median 
  - Expected: 4.718s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.386s median 
  - Expected: 16.302s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 9.171s median 
  - Expected: 1006.195s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 114.425s median 
  - Expected: 36.299s in 08-31-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.335s median 
  - Expected: 37.414s in 08-31-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName>; PodsEscapingCopernicus Cutscene; Transition 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — event type not present in baseline 08-31-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: backquote 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Lower Map; Press E to Insert; Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to place; Press E to place glyph; Raise Map; TurnOff; TurnOn 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 3410 records 
  - Expected: 1018 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — categorical value(s) not seen in baseline. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
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
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Tilted Out; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: soilSelected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` — field(s) not present in baseline schema. 
  - Observed: data.legendName
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Selected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: Legend 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — categorical value(s) not seen in baseline. 
  - Observed: DualChamber_Evaporator 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.1x vs baseline. 
  - Observed: 50 records 
  - Expected: 7 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 4,I; A,2,I; A,3,I; A,4,I; A,B,C,2,II; A,D,3,I; A,D,C,3,I; B,1,I; B,1,II; B,4,I; B,4,II; B,C,1,I; B,C,D,1,II; B,C,D,2,II; B,C,D,3,II; C,1,I; C,1,II; C,2,I; C,3,I; C,4,I; D,1,I; D,1,II; D,4,I; D,C,B,4,I; D,C,B,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 743 records 
  - Expected: 155 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 08-31-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `soilMachine` — record volume changed 7.2x vs baseline. 
  - Observed: 36 records 
  - Expected: 5 in 08-31-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 38 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11432] _id=6a9c860b485cab4c953ffb7c ts=2026-09-05T21:13:47.3510000Z`; `wenyi090326-3.stratalog.logdata.json[11393] _id=6a9c8669485cab4c953ffbca ts=2026-09-05T21:15:22.1050000Z`; `wenyi090326-3.stratalog.logdata.json[11364] _id=6a9c867f485cab4c953ffc02 ts=2026-09-05T21:15:44.1080000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11533] _id=6a9c854f485cab4c953ffab0 ts=2026-09-05T21:10:39.9370000Z`; `wenyi090326-3.stratalog.logdata.json[11140] _id=6a9c87a0485cab4c953ffdc6 ts=2026-09-05T21:20:32.4420000Z`; `wenyi090326-3.stratalog.logdata.json[11134] _id=6a9c87d8485cab4c953ffdd6 ts=2026-09-05T21:21:29.0330000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 33 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 33} 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11531] _id=6a9c8554485cab4c953ffab4 ts=2026-09-05T21:10:45.1410000Z`; `wenyi090326-3.stratalog.logdata.json[11523] _id=6a9c8567485cab4c953ffac4 ts=2026-09-05T21:11:03.6140000Z`; `wenyi090326-3.stratalog.logdata.json[11519] _id=6a9c857b485cab4c953ffacc ts=2026-09-05T21:11:24.0400000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 35 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 35} 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11532] _id=6a9c8552485cab4c953ffab2 ts=2026-09-05T21:10:43.2980000Z`; `wenyi090326-3.stratalog.logdata.json[11527] _id=6a9c8560485cab4c953ffabc ts=2026-09-05T21:10:56.8530000Z`; `wenyi090326-3.stratalog.logdata.json[11520] _id=6a9c8575485cab4c953ffaca ts=2026-09-05T21:11:17.5890000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 65 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `wenyi090326-3.stratalog.logdata.json[10509] _id=6a9c8b9e485cab4c95400262 ts=2026-09-05T21:37:34.7030000Z`; `wenyi090326-3.stratalog.logdata.json[10503] _id=6a9c8ba1485cab4c9540026e ts=2026-09-05T21:37:38.0670000Z`; `wenyi090326-3.stratalog.logdata.json[9712] _id=6a9c8ce5485cab4c954008f6 ts=2026-09-05T21:43:01.3020000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3409 | 0.0 | 0.033 | 2.231 | 0.854 | 2264.45 | 26.89 | 2171 | 5 |
| InputEvent | 3181 | 0.0 | 0.467 | 3.171 | 7.637 | 447.102 | 18.92 | 147 | 0 |
| DialogueEvent | 2507 | 0.0 | 0.667 | 4.045 | 16.224 | 278.012 | 14.83 | 759 | 0 |
| PlayerPositionEvent | 962 | 9.968 | 10.005 | 10.295 | 10.007 | 67.567 | 5.83 | 0 | 0 |
| argumentationNodeEvent | 742 | 0.001 | 0.234 | 12.785 | 3.902 | 3252.734 | 4.69 | 186 | 5 |
| ObjectInterEvent | 239 | 0.0 | 6.103 | 42.558 | 188.478 | 941.325 | 1.41 | 4 | 2 |
| questEvent | 81 | 0.0 | 68.877 | 124.807 | 498.848 | 814.882 | 0.48 | 15 | 2 |
| Soil Key Puzzle | 73 | 0.2 | 1.001 | 64.727 | 12.552 | 2601.182 | 0.93 | 0 | 3 |
| TopographicMapEvent | 64 | 0.004 | 2.5 | 67.301 | 300.568 | 1742.369 | 0.89 | 4 | 3 |
| argumentationAnswerEvent | 49 | 3.3 | 9.171 | 193.544 | 1259.694 | 3374.957 | 0.31 | 0 | 5 |
| WaterChamberEvent | 42 | 0.433 | 6.386 | 11.966 | 47.406 | 63.096 | 5.01 | 0 | 0 |
| soilMachine | 35 | 0.534 | 3.335 | 16.44 | 109.75 | 180.984 | 3.65 | 0 | 0 |
| gameWindowUnfocusEvent | 34 | 0.0 | 208.783 | 293.96 | 987.469 | 1647.516 | 0.2 | 1 | 3 |
| gameWindowFocusEvent | 32 | 18.473 | 198.207 | 312.982 | 1060.297 | 1739.508 | 0.19 | 0 | 3 |
| argumentationEvent | 17 | 0.032 | 114.425 | 558.17 | 2423.79 | 3245.497 | 0.11 | 2 | 5 |
| argumentationToolEvent | 11 | 0.501 | 0.983 | 381.248 | 1688.332 | 2275.824 | 0.16 | 0 | 3 |
| gameStartEvent | 7 | 56.591 | 891.96 | 1249.355 | 2583.078 | 2685.784 | 0.05 | 0 | 5 |
| TerasGardenBox | 5 | 0.867 | 1.134 | 6.563 | 16.054 | 16.808 | 9.14 | 0 | 0 |
| EndOfUnit | 4 | 1473.244 | 2296.064 | 2183.983 | 2626.613 | 2670.56 | 0.03 | 0 | 4 |
| DEBUGMenu | 3 | 4.09 | 5.085 | 1400.906 | 3774.698 | 4193.544 | 0.04 | 0 | 1 |
| SolarStillDesignEvent | 3 | 1.238 | 1.901 | 1.847 | 2.351 | 2.401 | 32.49 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 1 | 1000.434 | 1000.434 | 1000.434 | 1000.434 | 1000.434 | 0.06 | 0 | 1 |

- **WARNING / Medium** `DialogueEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-3.stratalog.logdata.json[9523] _id=6a9c8da0485cab4c95400a70 ts=2026-09-05T21:46:08.7650000Z == wenyi090326-3.stratalog.logdata.json[9524] _id=6a9c8da0485cab4c95400a72 ts=2026-09-05T21:46:08.7650000Z`; `wenyi090326-3.stratalog.logdata.json[5228] _id=6a9c9bbe485cab4c95402c06 ts=2026-09-05T22:46:23.0890000Z == wenyi090326-3.stratalog.logdata.json[5229] _id=6a9c9bbf485cab4c95402c08 ts=2026-09-05T22:46:23.0890000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-3.stratalog.logdata.json[2638] _id=6a9ca4b9485cab4c95404048 ts=2026-09-05T23:24:41.3560000Z == wenyi090326-3.stratalog.logdata.json[2637] _id=6a9ca4b9485cab4c9540404a ts=2026-09-05T23:24:41.3560000Z`; `wenyi090326-3.stratalog.logdata.json[2607] _id=6a9ca4d3485cab4c95404086 ts=2026-09-05T23:25:08.0350000Z == wenyi090326-3.stratalog.logdata.json[2606] _id=6a9ca4d3485cab4c95404088 ts=2026-09-05T23:25:08.0350000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 71 group(s), 108 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-3.stratalog.logdata.json[9191] _id=6a9c8fc0485cab4c95400d0e ts=2026-09-05T21:55:11.4880000Z == wenyi090326-3.stratalog.logdata.json[9192] _id=6a9c8fc0485cab4c95400d10 ts=2026-09-05T21:55:11.4880000Z`; `wenyi090326-3.stratalog.logdata.json[9186] _id=6a9c8fc0485cab4c95400d18 ts=2026-09-05T21:55:11.9900000Z == wenyi090326-3.stratalog.logdata.json[9185] _id=6a9c8fc0485cab4c95400d1a ts=2026-09-05T21:55:11.9900000Z`; `wenyi090326-3.stratalog.logdata.json[9158] _id=6a9c8fc3485cab4c95400d4a ts=2026-09-05T21:55:13.5560000Z == wenyi090326-3.stratalog.logdata.json[9159] _id=6a9c8fc3485cab4c95400d4c ts=2026-09-05T21:55:13.5560000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `wenyi090326-3.stratalog.logdata.json[199] _id=6a9cac73485cab4c9540535a ts=2026-09-05T23:57:39.4690000Z == wenyi090326-3.stratalog.logdata.json[198] _id=6a9cac73485cab4c9540535c ts=2026-09-05T23:57:39.4690000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi090326-3.stratalog.logdata.json[11468] _id=6a9c85b6485cab4c953ffb32 ts=2026-09-05T21:12:22.4900000Z ~ wenyi090326-3.stratalog.logdata.json[11467] _id=6a9c85b6485cab4c953ffb34 ts=2026-09-05T21:12:22.4910000Z`; `768ms: wenyi090326-3.stratalog.logdata.json[11279] _id=6a9c871a485cab4c953ffcae ts=2026-09-05T21:18:18.9820000Z ~ wenyi090326-3.stratalog.logdata.json[11277] _id=6a9c871b485cab4c953ffcb2 ts=2026-09-05T21:18:19.7500000Z`; `1ms: wenyi090326-3.stratalog.logdata.json[11050] _id=6a9c8888485cab4c953ffe7e ts=2026-09-05T21:24:24.6910000Z ~ wenyi090326-3.stratalog.logdata.json[11049] _id=6a9c8888485cab4c953ffe80 ts=2026-09-05T21:24:24.6920000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 56 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `434ms: wenyi090326-3.stratalog.logdata.json[10423] _id=6a9c8bb5485cab4c95400380 ts=2026-09-05T21:37:51.8710000Z ~ wenyi090326-3.stratalog.logdata.json[10422] _id=6a9c8bb5485cab4c95400382 ts=2026-09-05T21:37:52.3050000Z`; `135ms: wenyi090326-3.stratalog.logdata.json[10356] _id=6a9c8bba485cab4c954003f6 ts=2026-09-05T21:38:00.0420000Z ~ wenyi090326-3.stratalog.logdata.json[10355] _id=6a9c8bba485cab4c954003f8 ts=2026-09-05T21:38:00.1770000Z`; `65ms: wenyi090326-3.stratalog.logdata.json[10355] _id=6a9c8bba485cab4c954003f8 ts=2026-09-05T21:38:00.1770000Z ~ wenyi090326-3.stratalog.logdata.json[10354] _id=6a9c8bba485cab4c954003fa ts=2026-09-05T21:38:00.2420000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: wenyi090326-3.stratalog.logdata.json[9707] _id=6a9c8cf1485cab4c95400900 ts=2026-09-05T21:43:13.3730000Z ~ wenyi090326-3.stratalog.logdata.json[9703] _id=6a9c8cf1485cab4c95400908 ts=2026-09-05T21:43:13.3770000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: wenyi090326-3.stratalog.logdata.json[5948] _id=6a9c9844485cab4c95402664 ts=2026-09-05T22:31:32.7180000Z ~ wenyi090326-3.stratalog.logdata.json[5945] _id=6a9c9844485cab4c9540266a ts=2026-09-05T22:31:32.7500000Z`; `32ms: wenyi090326-3.stratalog.logdata.json[2198] _id=6a9ca61e485cab4c954043b8 ts=2026-09-05T23:30:38.9890000Z ~ wenyi090326-3.stratalog.logdata.json[2195] _id=6a9ca61e485cab4c954043be ts=2026-09-05T23:30:39.0210000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 75 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `14ms: wenyi090326-3.stratalog.logdata.json[11245] _id=6a9c872d485cab4c953ffcf2 ts=2026-09-05T21:18:38.0890000Z ~ wenyi090326-3.stratalog.logdata.json[11244] _id=6a9c872d485cab4c953ffcf4 ts=2026-09-05T21:18:38.1030000Z`; `15ms: wenyi090326-3.stratalog.logdata.json[11239] _id=6a9c872f485cab4c953ffcfe ts=2026-09-05T21:18:39.7390000Z ~ wenyi090326-3.stratalog.logdata.json[11238] _id=6a9c872f485cab4c953ffd00 ts=2026-09-05T21:18:39.7540000Z`; `14ms: wenyi090326-3.stratalog.logdata.json[11235] _id=6a9c8730485cab4c953ffd06 ts=2026-09-05T21:18:40.9400000Z ~ wenyi090326-3.stratalog.logdata.json[11234] _id=6a9c8730485cab4c953ffd08 ts=2026-09-05T21:18:40.9540000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `617ms: wenyi090326-3.stratalog.logdata.json[11222] _id=6a9c873a485cab4c953ffd20 ts=2026-09-05T21:18:51.1260000Z ~ wenyi090326-3.stratalog.logdata.json[11221] _id=6a9c873b485cab4c953ffd22 ts=2026-09-05T21:18:51.7430000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: wenyi090326-3.stratalog.logdata.json[5832] _id=6a9c9975485cab4c9540274e ts=2026-09-05T22:36:37.4310000Z ~ wenyi090326-3.stratalog.logdata.json[5831] _id=6a9c997f485cab4c95402750 ts=2026-09-05T22:36:37.431Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: wenyi090326-3.stratalog.logdata.json[90] _id=6a9cacdd485cab4c95405434 ts=2026-09-05T23:59:25.3670000Z ~ wenyi090326-3.stratalog.logdata.json[89] _id=6a9cacdd485cab4c95405436 ts=2026-09-05T23:59:25.3680000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `767ms: wenyi090326-3.stratalog.logdata.json[2957] _id=6a9ca39f485cab4c95403dca ts=2026-09-05T23:19:59.3870000Z ~ wenyi090326-3.stratalog.logdata.json[2954] _id=6a9ca3a0485cab4c95403dd0 ts=2026-09-05T23:20:00.1540000Z`; `534ms: wenyi090326-3.stratalog.logdata.json[2954] _id=6a9ca3a0485cab4c95403dd0 ts=2026-09-05T23:20:00.1540000Z ~ wenyi090326-3.stratalog.logdata.json[2950] _id=6a9ca3a0485cab4c95403dd6 ts=2026-09-05T23:20:00.6880000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 1h 9m 
  - Evidence: 1h 9m: wenyi090326-3.stratalog.logdata.json[5820] _id=6a9c9989485cab4c95402768 ts=2026-09-05T22:36:57.2850000Z -> wenyi090326-3.stratalog.logdata.json[980] _id=6a9ca9ea485cab4c95404d40 ts=2026-09-05T23:46:50.8290000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 759 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-3.stratalog.logdata.json[10591] _id=6a9c8b74485cab4c95400214 ts=2026-09-05T21:36:53.1500000Z -> wenyi090326-3.stratalog.logdata.json[10592] _id=6a9c8b74485cab4c95400216 ts=2026-09-05T21:36:53.1500000Z; 0ms: wenyi090326-3.stratalog.logdata.json[10641] _id=6a9c8ae4485cab4c954001ae ts=2026-09-05T21:34:28.3270000Z -> wenyi090326-3.stratalog.logdata.json[10642] _id=6a9c8ae4485cab4c954001b0 ts=2026-09-05T21:34:28.3270000Z; 0ms: wenyi090326-3.stratalog.logdata.json[10651] _id=6a9c8ad3485cab4c9540019c ts=2026-09-05T21:34:12.1520000Z -> wenyi090326-3.stratalog.logdata.json[10650] _id=6a9c8ad3485cab4c9540019e ts=2026-09-05T21:34:12.1520000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 44m 30s 
  - Evidence: 44m 30s: wenyi090326-3.stratalog.logdata.json[5019] _id=6a9c9ce1485cab4c95402daa ts=2026-09-05T22:51:13.1870000Z -> wenyi090326-3.stratalog.logdata.json[1885] _id=6a9ca74f485cab4c9540462a ts=2026-09-05T23:35:43.7470000Z; 39m 37s: wenyi090326-3.stratalog.logdata.json[10637] _id=6a9c8af0485cab4c954001b8 ts=2026-09-05T21:34:41.0600000Z -> wenyi090326-3.stratalog.logdata.json[7082] _id=6a9c943a485cab4c95401d86 ts=2026-09-05T22:14:18.6370000Z; 36m 54s: wenyi090326-3.stratalog.logdata.json[7082] _id=6a9c943a485cab4c95401d86 ts=2026-09-05T22:14:18.6370000Z -> wenyi090326-3.stratalog.logdata.json[5019] _id=6a9c9ce1485cab4c95402daa ts=2026-09-05T22:51:13.1870000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 147 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi090326-3.stratalog.logdata.json[32] _id=6a9cacf5485cab4c954054a6 ts=2026-09-05T23:59:49.2450000Z -> wenyi090326-3.stratalog.logdata.json[33] _id=6a9cacf5485cab4c954054a8 ts=2026-09-05T23:59:49.2450000Z; 1ms: wenyi090326-3.stratalog.logdata.json[10841] _id=6a9c8a18485cab4c95400020 ts=2026-09-05T21:31:04.9100000Z -> wenyi090326-3.stratalog.logdata.json[10840] _id=6a9c8a18485cab4c95400022 ts=2026-09-05T21:31:04.9110000Z; 1ms: wenyi090326-3.stratalog.logdata.json[11075] _id=6a9c887b485cab4c953ffe4c ts=2026-09-05T21:24:11.9010000Z -> wenyi090326-3.stratalog.logdata.json[11074] _id=6a9c887b485cab4c953ffe4e ts=2026-09-05T21:24:11.9020000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 15m 41s 
  - Evidence: 15m 41s: wenyi090326-3.stratalog.logdata.json[6915] _id=6a9c95b5485cab4c95401ed6 ts=2026-09-05T22:20:37.6220000Z -> wenyi090326-3.stratalog.logdata.json[5849] _id=6a9c9962485cab4c9540272a ts=2026-09-05T22:36:18.9470000Z; 12m 17s: wenyi090326-3.stratalog.logdata.json[9809] _id=6a9c8c4b485cab4c95400832 ts=2026-09-05T21:40:28.1580000Z -> wenyi090326-3.stratalog.logdata.json[9378] _id=6a9c8f2d485cab4c95400b94 ts=2026-09-05T21:52:46.1260000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: wenyi090326-3.stratalog.logdata.json[2607] _id=6a9ca4d3485cab4c95404086 ts=2026-09-05T23:25:08.0350000Z -> wenyi090326-3.stratalog.logdata.json[2606] _id=6a9ca4d3485cab4c95404088 ts=2026-09-05T23:25:08.0350000Z; 0ms: wenyi090326-3.stratalog.logdata.json[2638] _id=6a9ca4b9485cab4c95404048 ts=2026-09-05T23:24:41.3560000Z -> wenyi090326-3.stratalog.logdata.json[2637] _id=6a9ca4b9485cab4c9540404a ts=2026-09-05T23:24:41.3560000Z; 1ms: wenyi090326-3.stratalog.logdata.json[11050] _id=6a9c8888485cab4c953ffe7e ts=2026-09-05T21:24:24.6910000Z -> wenyi090326-3.stratalog.logdata.json[11049] _id=6a9c8888485cab4c953ffe80 ts=2026-09-05T21:24:24.6920000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 37m 44s 
  - Evidence: 37m 44s: wenyi090326-3.stratalog.logdata.json[7765] _id=6a9c90b3485cab4c9540182e ts=2026-09-05T21:59:14.7920000Z -> wenyi090326-3.stratalog.logdata.json[5818] _id=6a9c998c485cab4c9540276e ts=2026-09-05T22:36:59.2420000Z; 21m 18s: wenyi090326-3.stratalog.logdata.json[5602] _id=6a9c99c7485cab4c9540291e ts=2026-09-05T22:37:57.6890000Z -> wenyi090326-3.stratalog.logdata.json[4874] _id=6a9c9ec5485cab4c95402ecc ts=2026-09-05T22:59:16.5600000Z; 18m 22s: wenyi090326-3.stratalog.logdata.json[3677] _id=6a9c9f84485cab4c9540382a ts=2026-09-05T23:02:26.2470000Z -> wenyi090326-3.stratalog.logdata.json[2892] _id=6a9ca3d1485cab4c95403e4a ts=2026-09-05T23:20:48.5280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2171 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-3.stratalog.logdata.json[10001] _id=6a9c8bdb485cab4c954006b2 ts=2026-09-05T21:38:33.2250000Z -> wenyi090326-3.stratalog.logdata.json[10003] _id=6a9c8bdc485cab4c954006b4 ts=2026-09-05T21:38:33.2250000Z; 0ms: wenyi090326-3.stratalog.logdata.json[10002] _id=6a9c8bdb485cab4c954006b0 ts=2026-09-05T21:38:33.2250000Z -> wenyi090326-3.stratalog.logdata.json[10001] _id=6a9c8bdb485cab4c954006b2 ts=2026-09-05T21:38:33.2250000Z; 0ms: wenyi090326-3.stratalog.logdata.json[10004] _id=6a9c8bdb485cab4c954006ae ts=2026-09-05T21:38:33.2250000Z -> wenyi090326-3.stratalog.logdata.json[10002] _id=6a9c8bdb485cab4c954006b0 ts=2026-09-05T21:38:33.2250000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 43m 21s 
  - Evidence: 43m 21s: wenyi090326-3.stratalog.logdata.json[9368] _id=6a9c8f39485cab4c95400ba8 ts=2026-09-05T21:52:57.7640000Z -> wenyi090326-3.stratalog.logdata.json[5850] _id=6a9c9962485cab4c95402728 ts=2026-09-05T22:36:18.9460000Z; 20m 25s: wenyi090326-3.stratalog.logdata.json[5837] _id=6a9c996f485cab4c95402742 ts=2026-09-05T22:36:31.4190000Z -> wenyi090326-3.stratalog.logdata.json[4947] _id=6a9c9e38485cab4c95402e3c ts=2026-09-05T22:56:57.0620000Z; 12m 15s: wenyi090326-3.stratalog.logdata.json[9808] _id=6a9c8c4e485cab4c95400834 ts=2026-09-05T21:40:31.1240000Z -> wenyi090326-3.stratalog.logdata.json[9379] _id=6a9c8f2d485cab4c95400b92 ts=2026-09-05T21:52:46.1250000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 29m 2s 
  - Evidence: 29m 2s: wenyi090326-3.stratalog.logdata.json[7012] _id=6a9c94f0485cab4c95401e14 ts=2026-09-05T22:17:20.7180000Z -> wenyi090326-3.stratalog.logdata.json[5230] _id=6a9c9bbe485cab4c95402c04 ts=2026-09-05T22:46:23.0870000Z; 16m 54s: wenyi090326-3.stratalog.logdata.json[9440] _id=6a9c8e3f485cab4c95400b18 ts=2026-09-05T21:48:47.4590000Z -> wenyi090326-3.stratalog.logdata.json[7573] _id=6a9c9236485cab4c954019ae ts=2026-09-05T22:05:42.3600000Z; 11m 21s: wenyi090326-3.stratalog.logdata.json[7570] _id=6a9c9239485cab4c954019b4 ts=2026-09-05T22:05:45.5610000Z -> wenyi090326-3.stratalog.logdata.json[7026] _id=6a9c94e2485cab4c95401df8 ts=2026-09-05T22:17:06.5780000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.033s shown 
  - Evidence: 4ms: wenyi090326-3.stratalog.logdata.json[9707] _id=6a9c8cf1485cab4c95400900 ts=2026-09-05T21:43:13.3730000Z -> wenyi090326-3.stratalog.logdata.json[9703] _id=6a9c8cf1485cab4c95400908 ts=2026-09-05T21:43:13.3770000Z; 30ms: wenyi090326-3.stratalog.logdata.json[9708] _id=6a9c8cf1485cab4c954008fe ts=2026-09-05T21:43:13.3430000Z -> wenyi090326-3.stratalog.logdata.json[9707] _id=6a9c8cf1485cab4c95400900 ts=2026-09-05T21:43:13.3730000Z; 33ms: wenyi090326-3.stratalog.logdata.json[9475] _id=6a9c8df1485cab4c95400ad2 ts=2026-09-05T21:47:30.1640000Z -> wenyi090326-3.stratalog.logdata.json[9473] _id=6a9c8df1485cab4c95400ad6 ts=2026-09-05T21:47:30.1970000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 56m 14s 
  - Evidence: 56m 14s: wenyi090326-3.stratalog.logdata.json[5949] _id=6a9c9844485cab4c95402662 ts=2026-09-05T22:31:32.7160000Z -> wenyi090326-3.stratalog.logdata.json[2530] _id=6a9ca573485cab4c95404120 ts=2026-09-05T23:27:47.6730000Z; 37m 37s: wenyi090326-3.stratalog.logdata.json[10727] _id=6a9c8a70485cab4c95400104 ts=2026-09-05T21:32:32.5120000Z -> wenyi090326-3.stratalog.logdata.json[7295] _id=6a9c9341485cab4c95401bda ts=2026-09-05T22:10:09.5930000Z; 24m 21s: wenyi090326-3.stratalog.logdata.json[2199] _id=6a9ca61e485cab4c954043b6 ts=2026-09-05T23:30:38.9870000Z -> wenyi090326-3.stratalog.logdata.json[456] _id=6a9cabd4485cab4c95405158 ts=2026-09-05T23:55:00.8920000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 54m 5s 
  - Evidence: 54m 5s: wenyi090326-3.stratalog.logdata.json[5945] _id=6a9c9844485cab4c9540266a ts=2026-09-05T22:31:32.7500000Z -> wenyi090326-3.stratalog.logdata.json[2571] _id=6a9ca4f2485cab4c954040ce ts=2026-09-05T23:25:38.2470000Z; 36m 58s: wenyi090326-3.stratalog.logdata.json[10726] _id=6a9c8a70485cab4c95400106 ts=2026-09-05T21:32:32.5150000Z -> wenyi090326-3.stratalog.logdata.json[7332] _id=6a9c931a485cab4c95401b90 ts=2026-09-05T22:09:30.8780000Z; 24m 12s: wenyi090326-3.stratalog.logdata.json[2195] _id=6a9ca61e485cab4c954043be ts=2026-09-05T23:30:39.0210000Z -> wenyi090326-3.stratalog.logdata.json[473] _id=6a9cabcb485cab4c95405136 ts=2026-09-05T23:54:51.2210000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.032s..0.032s shown 
  - Evidence: 32ms: wenyi090326-3.stratalog.logdata.json[2198] _id=6a9ca61e485cab4c954043b8 ts=2026-09-05T23:30:38.9890000Z -> wenyi090326-3.stratalog.logdata.json[2195] _id=6a9ca61e485cab4c954043be ts=2026-09-05T23:30:39.0210000Z; 32ms: wenyi090326-3.stratalog.logdata.json[5948] _id=6a9c9844485cab4c95402664 ts=2026-09-05T22:31:32.7180000Z -> wenyi090326-3.stratalog.logdata.json[5945] _id=6a9c9844485cab4c9540266a ts=2026-09-05T22:31:32.7500000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 54m 12s 
  - Evidence: 54m 12s: wenyi090326-3.stratalog.logdata.json[5950] _id=6a9c9842485cab4c95402660 ts=2026-09-05T22:31:31.0820000Z -> wenyi090326-3.stratalog.logdata.json[2568] _id=6a9ca4f7485cab4c954040d4 ts=2026-09-05T23:25:43.8160000Z; 37m 0s: wenyi090326-3.stratalog.logdata.json[10728] _id=6a9c8a6f485cab4c95400102 ts=2026-09-05T21:32:31.7120000Z -> wenyi090326-3.stratalog.logdata.json[7329] _id=6a9c931b485cab4c95401b96 ts=2026-09-05T22:09:32.1770000Z; 24m 14s: wenyi090326-3.stratalog.logdata.json[2200] _id=6a9ca61e485cab4c954043b4 ts=2026-09-05T23:30:38.2530000Z -> wenyi090326-3.stratalog.logdata.json[470] _id=6a9cabcc485cab4c9540513c ts=2026-09-05T23:54:53.0880000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 186 interval(s) ≤ 0.001s..0.014s shown 
  - Evidence: 1ms: wenyi090326-3.stratalog.logdata.json[6040] _id=6a9c9802485cab4c954025ac ts=2026-09-05T22:30:27.1200000Z -> wenyi090326-3.stratalog.logdata.json[6039] _id=6a9c9802485cab4c954025ae ts=2026-09-05T22:30:27.1210000Z; 14ms: wenyi090326-3.stratalog.logdata.json[11235] _id=6a9c8730485cab4c953ffd06 ts=2026-09-05T21:18:40.9400000Z -> wenyi090326-3.stratalog.logdata.json[11234] _id=6a9c8730485cab4c953ffd08 ts=2026-09-05T21:18:40.9540000Z; 14ms: wenyi090326-3.stratalog.logdata.json[11245] _id=6a9c872d485cab4c953ffcf2 ts=2026-09-05T21:18:38.0890000Z -> wenyi090326-3.stratalog.logdata.json[11244] _id=6a9c872d485cab4c953ffcf4 ts=2026-09-05T21:18:38.1030000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 37m 55s 
  - Evidence: 37m 55s: wenyi090326-3.stratalog.logdata.json[10771] _id=6a9c8a5b485cab4c954000ac ts=2026-09-05T21:32:11.8030000Z -> wenyi090326-3.stratalog.logdata.json[7298] _id=6a9c933f485cab4c95401bd4 ts=2026-09-05T22:10:07.6270000Z; 18m 20s: wenyi090326-3.stratalog.logdata.json[7297] _id=6a9c9340485cab4c95401bd6 ts=2026-09-05T22:10:08.4590000Z -> wenyi090326-3.stratalog.logdata.json[6143] _id=6a9c978d485cab4c954024de ts=2026-09-05T22:28:29.2990000Z; 12m 36s: wenyi090326-3.stratalog.logdata.json[11217] _id=6a9c873c485cab4c953ffd2a ts=2026-09-05T21:18:52.7260000Z -> wenyi090326-3.stratalog.logdata.json[10804] _id=6a9c8a31485cab4c9540006a ts=2026-09-05T21:31:29.5220000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16m 40s 
  - Evidence: 16m 40s: wenyi090326-3.stratalog.logdata.json[1882] _id=6a9ca77b485cab4c95404632 ts=2026-09-05T23:36:27.2690000Z -> wenyi090326-3.stratalog.logdata.json[597] _id=6a9cab63485cab4c9540503e ts=2026-09-05T23:53:07.7030000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 44m 45s 
  - Evidence: 44m 45s: wenyi090326-3.stratalog.logdata.json[5017] _id=6a9c9cfb485cab4c95402db0 ts=2026-09-05T22:51:39.6350000Z -> wenyi090326-3.stratalog.logdata.json[1883] _id=6a9ca779485cab4c95404630 ts=2026-09-05T23:36:25.4190000Z; 39m 3s: wenyi090326-3.stratalog.logdata.json[10634] _id=6a9c8b36485cab4c954001c0 ts=2026-09-05T21:35:50.5120000Z -> wenyi090326-3.stratalog.logdata.json[7080] _id=6a9c945d485cab4c95401d8c ts=2026-09-05T22:14:53.9410000Z; 21m 53s: wenyi090326-3.stratalog.logdata.json[7080] _id=6a9c945d485cab4c95401d8c ts=2026-09-05T22:14:53.9410000Z -> wenyi090326-3.stratalog.logdata.json[5829] _id=6a9c997f485cab4c95402756 ts=2026-09-05T22:36:47.6750000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 28m 59s 
  - Evidence: 28m 59s: wenyi090326-3.stratalog.logdata.json[9633] _id=6a9c8d1a485cab4c95400996 ts=2026-09-05T21:43:54.7500000Z -> wenyi090326-3.stratalog.logdata.json[7208] _id=6a9c93e6485cab4c95401c8a ts=2026-09-05T22:12:54.2580000Z; 24m 16s: wenyi090326-3.stratalog.logdata.json[2333] _id=6a9ca5c5485cab4c954042aa ts=2026-09-05T23:29:09.3810000Z -> wenyi090326-3.stratalog.logdata.json[590] _id=6a9cab75485cab4c9540504c ts=2026-09-05T23:53:25.5270000Z; 12m 16s: wenyi090326-3.stratalog.logdata.json[5261] _id=6a9c9b98485cab4c95402bc6 ts=2026-09-05T22:45:44.2220000Z -> wenyi090326-3.stratalog.logdata.json[4917] _id=6a9c9e78485cab4c95402e78 ts=2026-09-05T22:58:00.6420000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 27m 27s 
  - Evidence: 27m 27s: wenyi090326-3.stratalog.logdata.json[9634] _id=6a9c8d1a485cab4c95400994 ts=2026-09-05T21:43:54.7480000Z -> wenyi090326-3.stratalog.logdata.json[7218] _id=6a9c938a485cab4c95401c74 ts=2026-09-05T22:11:22.2640000Z; 24m 16s: wenyi090326-3.stratalog.logdata.json[2334] _id=6a9ca5c3485cab4c954042a8 ts=2026-09-05T23:29:07.2900000Z -> wenyi090326-3.stratalog.logdata.json[594] _id=6a9cab73485cab4c95405044 ts=2026-09-05T23:53:23.8170000Z; 12m 14s: wenyi090326-3.stratalog.logdata.json[5262] _id=6a9c9b97485cab4c95402bc4 ts=2026-09-05T22:45:43.5720000Z -> wenyi090326-3.stratalog.logdata.json[4918] _id=6a9c9e76485cab4c95402e76 ts=2026-09-05T22:57:58.4710000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-3.stratalog.logdata.json[5832] _id=6a9c9975485cab4c9540274e ts=2026-09-05T22:36:37.4310000Z -> wenyi090326-3.stratalog.logdata.json[5831] _id=6a9c997f485cab4c95402750 ts=2026-09-05T22:36:37.431Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 13m 34s 
  - Evidence: 13m 34s: wenyi090326-3.stratalog.logdata.json[6940] _id=6a9c95a5485cab4c95401ea4 ts=2026-09-05T22:20:21.4330000Z -> wenyi090326-3.stratalog.logdata.json[5929] _id=6a9c98d4485cab4c9540268a ts=2026-09-05T22:33:56.3150000Z; 11m 8s: wenyi090326-3.stratalog.logdata.json[7693] _id=6a9c9177485cab4c954018be ts=2026-09-05T22:02:31.5470000Z -> wenyi090326-3.stratalog.logdata.json[7142] _id=6a9c9413485cab4c95401d0e ts=2026-09-05T22:13:39.9190000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: wenyi090326-3.stratalog.logdata.json[10821] _id=6a9c8a28485cab4c95400048 ts=2026-09-05T21:31:20.8880000Z -> wenyi090326-3.stratalog.logdata.json[10820] _id=6a9c8a28485cab4c9540004a ts=2026-09-05T21:31:20.8880000Z; 0ms: wenyi090326-3.stratalog.logdata.json[11263] _id=6a9c8724485cab4c953ffcca ts=2026-09-05T21:18:28.9420000Z -> wenyi090326-3.stratalog.logdata.json[11265] _id=6a9c8724485cab4c953ffccc ts=2026-09-05T21:18:28.9420000Z; 0ms: wenyi090326-3.stratalog.logdata.json[199] _id=6a9cac73485cab4c9540535a ts=2026-09-05T23:57:39.4690000Z -> wenyi090326-3.stratalog.logdata.json[198] _id=6a9cac73485cab4c9540535c ts=2026-09-05T23:57:39.4690000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11294] _id=6a9c870e485cab4c953ffc90 ts=2026-09-05T21:18:06.6780000Z`; `wenyi090326-3.stratalog.logdata.json[11178] _id=6a9c8752485cab4c953ffd78 ts=2026-09-05T21:19:14.5920000Z`; `wenyi090326-3.stratalog.logdata.json[10843] _id=6a9c8a16485cab4c9540001c ts=2026-09-05T21:31:03.1440000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 24 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `wenyi090326-3.stratalog.logdata.json[10057] _id=6a9c8bd6485cab4c9540064a ts=2026-09-05T21:38:29.8230000Z`; `wenyi090326-3.stratalog.logdata.json[10055] _id=6a9c8bd7485cab4c95400650 ts=2026-09-05T21:38:29.8570000Z`; `wenyi090326-3.stratalog.logdata.json[9900] _id=6a9c8c06485cab4c95400786 ts=2026-09-05T21:39:16.4420000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 49 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `wenyi090326-3.stratalog.logdata.json[10422] _id=6a9c8bb5485cab4c95400382 ts=2026-09-05T21:37:52.3050000Z`; `wenyi090326-3.stratalog.logdata.json[10356] _id=6a9c8bba485cab4c954003f6 ts=2026-09-05T21:38:00.0420000Z`; `wenyi090326-3.stratalog.logdata.json[10355] _id=6a9c8bba485cab4c954003f8 ts=2026-09-05T21:38:00.1770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `wenyi090326-3.stratalog.logdata.json[5945] _id=6a9c9844485cab4c9540266a ts=2026-09-05T22:31:32.7500000Z`; `wenyi090326-3.stratalog.logdata.json[2195] _id=6a9ca61e485cab4c954043be ts=2026-09-05T23:30:39.0210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11244] _id=6a9c872d485cab4c953ffcf4 ts=2026-09-05T21:18:38.1030000Z`; `wenyi090326-3.stratalog.logdata.json[11238] _id=6a9c872f485cab4c953ffd00 ts=2026-09-05T21:18:39.7540000Z`; `wenyi090326-3.stratalog.logdata.json[11234] _id=6a9c8730485cab4c953ffd08 ts=2026-09-05T21:18:40.9540000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `wenyi090326-3.stratalog.logdata.json[1882] _id=6a9ca77b485cab4c95404632 ts=2026-09-05T23:36:27.2690000Z`; `wenyi090326-3.stratalog.logdata.json[597] _id=6a9cab63485cab4c9540503e ts=2026-09-05T23:53:07.7030000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `wenyi090326-3.stratalog.logdata.json[5824] _id=6a9c9989485cab4c95402760 ts=2026-09-05T22:36:57.2730000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11534] _id=6a9c87ab485cab4c953ffdcc ts=?`; `wenyi090326-3.stratalog.logdata.json[11535] _id=6a9c8d18485cab4c95400992 ts=?`; `wenyi090326-3.stratalog.logdata.json[11536] _id=6a9c9973485cab4c9540274c ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 346 occurrence(s) 
  - Examples: `wenyi090326-3.stratalog.logdata.json[10323] _id=6a9c8bbc485cab4c9540043a ts=2026-09-05T21:38:02.7120000Z`; `wenyi090326-3.stratalog.logdata.json[10308] _id=6a9c8bbe485cab4c95400452 ts=2026-09-05T21:38:04.1460000Z`; `wenyi090326-3.stratalog.logdata.json[10293] _id=6a9c8bbf485cab4c9540046a ts=2026-09-05T21:38:05.9800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 246 occurrence(s) 
  - Examples: `wenyi090326-3.stratalog.logdata.json[10394] _id=6a9c8bb6485cab4c954003ae ts=2026-09-05T21:37:55.9410000Z`; `wenyi090326-3.stratalog.logdata.json[10330] _id=6a9c8bbc485cab4c9540042e ts=2026-09-05T21:38:02.5460000Z`; `wenyi090326-3.stratalog.logdata.json[10321] _id=6a9c8bbc485cab4c9540043e ts=2026-09-05T21:38:02.7450000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 21 occurrence(s) 
  - Examples: `wenyi090326-3.stratalog.logdata.json[9707] _id=6a9c8cf1485cab4c95400900 ts=2026-09-05T21:43:13.3730000Z`; `wenyi090326-3.stratalog.logdata.json[9703] _id=6a9c8cf1485cab4c95400908 ts=2026-09-05T21:43:13.3770000Z`; `wenyi090326-3.stratalog.logdata.json[9525] _id=6a9c8da0485cab4c95400a6e ts=2026-09-05T21:46:08.7630000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `wenyi090326-3.stratalog.logdata.json[2301] _id=6a9ca5fb485cab4c954042ea ts=2026-09-05T23:30:03.0030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `wenyi090326-3.stratalog.logdata.json[11221] _id=6a9c873b485cab4c953ffd22 ts=2026-09-05T21:18:51.7430000Z`; `wenyi090326-3.stratalog.logdata.json[10771] _id=6a9c8a5b485cab4c954000ac ts=2026-09-05T21:32:11.8030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 486 start, 483 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 19 unmatched 'BecameCameraCentered' (totals: 906 open, 911 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 20 unmatched 'BecameVisible' (totals: 782 open, 811 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 23 open, 21 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 9 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 9 unmatched 'questActiveEvent' (totals: 45 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 529 of 11533 adjacent _id pairs reverse in client time; worst 34.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `wenyi090326-3.stratalog.logdata.json[10431] _id=6a9c8baf485cab4c954002cc ts=2026-09-05T21:37:51.5740000Z`; `wenyi090326-3.stratalog.logdata.json[10529] _id=6a9c8baf485cab4c954002ce ts=2026-09-05T21:37:16.9940000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median +0.15s, min -43.38s, max +0.39s over 11534 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\config\coverage\09-03-26-3.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Full playthrough by one tester on 2026-09-05/06 (log shows EndOfUnit for units 1-5).; First ~10 minutes (393 records, Unit 1 only, 21:10-21:19Z) were logged on the older build 20260721-11840 before the tester switched to 20260902-12353 and restarted Unit 1 from the intro cutscene; all EndOfUnit events are on the new build.; Debug menu opened briefly (DebugMenuStateChanged toggles in Unit 3 and Unit 5 dungeon; no debug actions logged). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3410 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1778); Unit 4 Dev (1042); Unit 5 Dev - Dungeon (452); Unit 3 Dungeon Dev (138)
- **Intervals:** median 0.03s (p5 0.00s / p95 0.85s, n=3409)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3410/3410 records)
    "BecameCameraUncentered"  x911
    "BecameCameraCentered"  x906
    "BecameInvisible"  x811
    "BecameVisible"  x782
data.pieceId  (string, 3410/3410 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3410/3410 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3182 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (657); Unit 2 Prod (Refactor) (649); Unit 5 Dev - Dungeon (527); Unit 4 Dev - Dungeon (424); Unit 4 Dev (341); Unit 1 Dev (237); Unit 3 Dungeon Dev (212); Unit 5 Dev (105); Unit 4 Dev - Anderson Base (30)
- **Intervals:** median 0.47s (p5 0.07s / p95 7.64s, n=3181)
- **Fields under `data`:**

```text
data.Value  (string, 3182/3182 records)
    "pressed"  x3182
data.actionType  (string, 3182/3182 records)
    "Move"  x2410
    "Interact"  x516
    "Sprint"  x150
    "Jump"  x41
    "Ascend"  x29
    "Map"  x16
    "Descend"  x9
    "Hoverboard"  x9
    "ToggleDebug"  x2
data.key  (string, 3182/3182 records, 1 empty-string)
    "w"  x792
    "a"  x589
    "s"  x533
    "d"  x496
    "leftButton"  x437
    "leftShift"  x159
    "e"  x91
    "space"  x58
    "m"  x16
    "h"  x8
    "backquote"  x2
    ""  x1
data.playerOrDrone  (string, 3182/3182 records)
    "Player"  x2539
    "Drone"  x643
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2508 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (666); Unit 3 Dev (459); Unit 1 Dev (347); Unit 4 Dev (285); Unit 5 Dev (264); Unit 5 Dev - Dungeon (137); Unit 4 Dev - Anderson Base (135); Unit 3 Dungeon Dev (116); Unit 4 Dev - Dungeon (99)
- **eventKey:** present on 1539 of 2508 records
- **Intervals:** median 0.67s (p5 0.00s / p95 16.22s, n=2507)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1539; [conversationId, dialogueEventType] x969
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2508/2508 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2508/2508 records)
    "DialogueNodeEvent"  x1539
    "DialogueStartEvent"  x486
    "DialogueFinishEvent"  x483
data.nodeId  (number, 1539/2508 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 974 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (226); Unit 3 Dev (161); Unit 1 Dev (135); Unit 4 Dev (113); Unit 4 Dev - Dungeon (101); Unit 5 Dev - Dungeon (99); Unit 3 Dungeon Dev (52); Unit 4 Dev - Anderson Base (44); Unit 5 Dev (43)
- **Intervals:** median 10.01s (p5 9.97s / p95 10.01s, n=962)
- **Fields under `data`:**

```text
data.position  (object, 974/974 records)
data.position.x  (number, 974/974 records)
    numeric range -706.223 .. 1559.25 (402 unique)
data.position.y  (number, 974/974 records)
    numeric range -112.489 .. 222.019 (320 unique)
data.position.z  (number, 974/974 records)
    numeric range -1032.64 .. 1993.52 (402 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 743 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (257); Unit 5 Dev (146); Unit 3 Dev (145); Unit 2 Prod (Refactor) (113); Unit 1 Dev (82)
- **Intervals:** median 0.23s (p5 0.03s / p95 3.90s, n=742)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 743/743 records)
    "argumentationNodeHoverEnd"  x305
    "argumentationNodeHoverStart"  x296
    "argumentationNodeAdd"  x82
    "argumentationNodeRemove"  x60
data.argumentationTitle  (string, 743/743 records)
    "Unit 4 - Flooding"  x257
    "Unit 5"  x146
    "Unit 3 - Pollution Upstream"  x145
    "Unit 2 – Watershed"  x113
    "Unit 1 - Freshwater"  x52
    "Unit 1 - Argumentation Tutorial"  x30
data.nodeName  (string, 743/743 records)
    "A"  x105
    "C"  x104
    "B"  x102
    "1"  x83
    "D"  x68
    "I"  x63
    "4"  x58
    "3"  x53
    "II"  x47
    "2"  x45
    "5"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 240 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (87); Unit 2 Prod (Refactor) (36); Unit 1 Dev (25); Unit 3 Dungeon Dev (25); Unit 4 Dev (20); Unit 5 Dev - Dungeon (17); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (9)
- **Intervals:** median 6.10s (p5 1.12s / p95 188.48s, n=239)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 240/240 records)
    46 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 240/240 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 82 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 2 Prod (Refactor) (12); Unit 3 Dev (11); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 82 of 82 records
- **Intervals:** median 68.88s (p5 0.00s / p95 498.85s, n=81)
- **`data` key-set variants:** [questEventType, questID, questName] x45; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 82/82 records)
    "questActiveEvent"  x45
    "questFinishEvent"  x37
data.questID  (string, 82/82 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 82/82 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/82 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 74 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (50); Unit 2 Prod (Refactor) (12); Unit 3 Dev (12)
- **Intervals:** median 1.00s (p5 0.27s / p95 12.55s, n=73)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x66; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/74 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/74 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 66/74 records)
    "RightDrag"  x36
    "LeftDrag"  x30
data.currentSoilType  (string, 66/74 records)
    "SAND"  x12
    "SANDGRAVEL"  x12
    "CLAY"  x11
    "CLAYSAND"  x11
    "CLAYROCK"  x10
    "GRAVEL"  x6
    "BEDROCK"  x4
data.isCorrectSelection  (string, 66/74 records)
    "false"  x54
    "true"  x12
data.waterLevelStatus  (string, 66/74 records)
    "TooLow"  x29
    "TooHigh"  x26
    "Proper"  x11
data.waterRetentionChange  (string, 66/74 records)
    "Decrease"  x30
    "Increase"  x24
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 65 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (39); Unit 3 Dev (26)
- **Intervals:** median 2.50s (p5 0.09s / p95 300.57s, n=64)
- **`data` key-set variants:** [actionType, featureUsed] x44; [actionType, featureUsed, location] x19; [actionType, featureUsed, legendName] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 65/65 records)
    "MapOpenEvent"  x23
    "MapCloseEvent"  x21
    "WaypointMoveEvent"  x18
    "Selected"  x2
    "WaypointSetEvent"  x1
data.featureUsed  (string, 65/65 records)
    "Map"  x44
    "Waypoint"  x19
    "Legend"  x2
data.legendName  (string, 2/65 records)
    "0 ft"  x1
    "90 ft"  x1
data.location  (object, 19/65 records)
data.location.x  (number, 19/65 records)
    numeric range -215.716 .. 314.451 (16 unique)
data.location.y  (number, 19/65 records)
    numeric range 68.1038 .. 229.98 (16 unique)
data.location.z  (number, 19/65 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 50 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (15); Unit 5 Dev (12); Unit 2 Prod (Refactor) (9); Unit 1 Dev (8); Unit 3 Dev (6)
- **Intervals:** median 9.17s (p5 3.65s / p95 1259.69s, n=49)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "submitAnswerEvent"  x50
data.answerSubmitted  (string, 50/50 records)
    30 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 50/50 records)
    "Unit 4 - Flooding"  x15
    "Unit 5"  x12
    "Unit 2 – Watershed"  x9
    "Unit 1 - Freshwater"  x6
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 43 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (43)
- **Intervals:** median 6.39s (p5 0.97s / p95 47.41s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "On"  x26
    "Off"  x17
data.floor  (string, 43/43 records)
    "3"  x25
    "4"  x11
    "2"  x5
    "1"  x2
data.machineNumber  (string, 43/43 records)
    "One"  x42
    "Two"  x1
data.machineType  (string, 43/43 records)
    "Condenser"  x15
    "Evaporator"  x10
    "DualChamber_Condenser"  x9
    "DualChamber_Evaporator"  x7
    "VentSwitch"  x2
data.room  (string, 43/43 records)
    "2"  x23
    "3"  x10
    "4"  x6
    "1"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 36 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (36)
- **Intervals:** median 3.33s (p5 0.81s / p95 109.75s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "ChangeCanister"  x36
data.canisterType  (string, 36/36 records)
    "Clay"  x12
    "Bedrock"  x10
    "Sand"  x8
    "Gravel"  x6
data.floor  (string, 36/36 records)
    "5"  x16
    "2"  x7
    "3"  x7
    "4"  x6
data.machine  (string, 36/36 records)
    "1"  x30
    "2"  x6
data.row  (string, 36/36 records)
    "TopRow"  x31
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 35 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (6); Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (3); Unit 4 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (2); MainMenu (1); PodsEscapingCopernicus Cutscene (1); Transition (1)
- **Intervals:** median 208.78s (p5 9.27s / p95 987.47s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 35/35 records)
    false  x35
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameWindowFocusEvent` — 33 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (5); Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (3); Unit 4 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (2); MainMenu (1); PodsEscapingCopernicus Cutscene (1); Transition (1)
- **Intervals:** median 198.21s (p5 23.02s / p95 1060.30s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 33/33 records)
    true  x33
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 114.42s (p5 0.03s / p95 2423.79s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 18/18 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 18/18 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2)
- **Intervals:** median 0.98s (p5 0.56s / p95 1688.33s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 2 – Watershed"  x2
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 8 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (8)
- **Intervals:** median 891.96s (p5 217.37s / p95 2583.08s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    true  x8
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.13s (p5 0.89s / p95 16.05s, n=5)
- **Open findings:** 2 — see sections 5-8
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
    "Clay"  x4
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 2296.06s (p5 1584.44s / p95 2626.61s, n=4)
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

### `DEBUGMenu` — 4 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 3 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 5.08s (p5 4.19s / p95 3774.70s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "DebugMenuStateChanged"  x4
data.isOpened  (bool, 4/4 records)
    false  x2
    true  x2
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 1.90s (p5 1.30s / p95 2.35s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Flat"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time."  x1
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 1 empty-string)
    ""  x1
    "NotAllowedError: Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time.
    at requestPointerLock (blob:https://dev.adroit.games/4e66f0bd-e8aa-4de7-bf0b-254aa18bfa48:9:213829)
    at Object.runDeferredCalls (blob:https://dev.adroit.games/4e66f0bd-e8aa-4de7-bf0b-254aa18bfa48:9:204819)
    at HTMLCanvasElement.jsEventHandler (blob:https://dev.adroit.games/4e66f0bd-e8aa-4de7-bf0b-254aa18bfa48:9:205513)"  x1
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a8f363e:wasm-function[73291]:0x1563591
    at wasm://wasm/0a8f363e:wasm-function[73290]:0x15634d3
    at wasm://wasm/0a8f363e:wasm-function[59956]:0x11d11ac
    at wasm://wasm/0a8f363e:wasm-function[59957]:0x11d11f3
    at wasm://wasm/0a8f363e:wasm-function[80769]:0x16e045b
    at wasm://wasm/0a8f363e:wasm-function[83409]:0x1717ed2
    at wasm://wasm/0a8f363e:wasm-function[110254]:0x259781d
    at invoke_iiii (blob:https://dev.adroit.games/95c86a99-4326-4def-8b2a-9537c93d3577:9:474038)
    at wasm://wasm/0a8f363e:wasm-function[83394]:0x1717572
    at wasm://wasm/0a8f363e:wasm-function[1942]:0xf57d9
    at wasm://wasm/0a8f363e:wasm-function[109911]:0x255e832
    at wasm://wasm/0a8f363e:wasm-function[106216]:0x24af5b6
    at wasm://wasm/0a8f363e:wasm-function[87318]:0x190fbf2
    at wasm://wasm/0a8f363e:wasm-function[102624]:0x2291c25
    at wasm://wasm/0a8f363e:wasm-function[105694]:0x245a569
    at wasm://wasm/0a8f363e:wasm-function[105709]:0x245ab0e
    at wasm://wasm/0a8f363e:wasm-function[104647]:0x23edaa7
    at wasm://wasm/0a8f363e:wasm-function[103118]:0x22d15fa
    at wasm://wasm/0a8f363e:wasm-function[86343]:0x18ae5bb
    at wasm://wasm/0a8f363e:wasm-function[103047]:0x22c2f96
    at wasm://wasm/0a8f363e:wasm-function[108883]:0x24f4871
    at wasm://wasm/0a8f363e:wasm-function[3934]:0x15e018
    at wasm://wasm/0a8f363e:wasm-function[110265]:0x25978c4
    at invoke_viiii (blob:https://dev.adroit.games/95c86a99-4326-4def-8b2a-9537c93d3577:9:474821)
    at wasm://wasm/0a8f363e:wasm-function[30556]:0x8ef73a
    at wasm://wasm/0a8f363e:wasm-function[110258]:0x2597858
    at invoke_viii (blob:https://dev.adroit.games/95c86a99-4326-4def-8b2a-9537c93d3577:9:474188)
    at wasm://wasm/0a8f363e:wasm-function[30543]:0x8e931b
    at wasm://wasm/0a8f363e:wasm-function[110258]:0x2597858
    at invoke_viii (blob:https://dev.adroit.games/95c86a99-4326-4def-8b2a-9537c93d3577:9:474188)
    at wasm://wasm/0a8f363e:wasm-function[30537]:0x8e66c3
    at wasm://wasm/0a8f363e:wasm-function[3753]:0x15846a
    at wasm://wasm/0a8f363e:wasm-function[110265]:0x25978c4
    at invoke_viiii (blob:https://dev.adroit.games/95c86a99-4326-4def-8b2a-9537c93d3577:9:474821)
    at wasm://wasm/0a8f363e:wasm-function[3789]:0x159d6b
    at wasm://wasm/0a8f363e:wasm-function[82090]:0x16fd557
    at wasm://wasm/0a8f363e:wasm-function[83409]:0x1717ed2
    at wasm://wasm/0a8f363e:wasm-function[110254]:0x259781d
    at invoke_iiii (blob:https://dev.adroit.games/95c86a99-4326-4def-8b2a-9537c93d3577:9:474038)
    at wasm://wasm/0a8f363e:wasm-function[83394]:0x1717572
    at wasm://wasm/0a8f363e:wasm-function[1942]:0xf57d9
    at wasm://wasm/0a8f363e:wasm-function[109911]:0x255e832
    at wasm://wasm/0a8f363e:wasm-function[106216]:0x24af5b6
    at wasm://wasm/0a8f363e:wasm-function[106219]:0x24af67c
    at wasm://wasm/0a8f363e:wasm-function[84651]:0x1792b0b
    at wasm://wasm/0a8f363e:wasm-function[85941]:0x185d320
    at wasm://wasm/0a8f363e:wasm-function[103890]:0x234f7d5
    at wasm://wasm/0a8f363e:wasm-function[105636]:0x2457674
    at wasm://wasm/0a8f363e:wasm-function[105636]:0x24576e9
    at wasm://wasm/0a8f363e:wasm-function[109989]:0x2566c65"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x2
    "runtime_error"  x1
data.unitId  (string, 3/3 records)
    "unit1"  x1
    "unit2"  x1
    "unit3"  x1
data.workspace  (string, 3/3 records)
    "dev"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1000.43s (p5 1000.43s / p95 1000.43s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\08-31-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `DialogueEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `DaniEvent` : event type present in baseline 08-31-26 but absent now
- `TerasGardenBox` : baseline field(s) absent this build
- `TerasGardenBox` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (18x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (19x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (60x)
- `soilMachine` data.canisterType: "Bedrock" (10x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*