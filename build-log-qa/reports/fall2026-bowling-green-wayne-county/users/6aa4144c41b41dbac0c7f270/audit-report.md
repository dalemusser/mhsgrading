# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f270

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f270
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f270.jsonl
- **Records:** 13151 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f270
- **Time span:** 2026-09-22T18:24:33.311000+00:00 .. 2026-10-06T18:34:12.775000+00:00 (336h 9m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f270\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13151 records, 11 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 104 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially
  - WARNING/Medium `soilMachine`: median interval between records changed substantially
  - WARNING/Medium `DialogueEvent`: eventKey does not match its documented format
  - WARNING/Medium `DialogueEvent`: dialogue lifecycle: finish without preceding start

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5110 | 38.86 | 1 | 9 | 0 | 2026-09-22T18:24:54.672000+00:00 | 2026-10-06T18:34:12.775000+00:00 | 336h 9m |
| PuzzlePieceVisibleEvent | 3036 | 23.09 | 1 | 4 | 0 | 2026-09-24T17:48:56.400000+00:00 | 2026-10-06T18:10:11.296000+00:00 | 288h 21m |
| DialogueEvent | 2049 | 15.58 | 1 | 9 | 1265 | 2026-09-22T18:25:11.366000+00:00 | 2026-10-06T18:34:08.725000+00:00 | 336h 8m |
| PlayerPositionEvent | 1854 | 14.1 | 1 | 9 | 0 | 2026-09-22T18:24:49.464000+00:00 | 2026-10-06T18:34:12.559000+00:00 | 336h 9m |
| argumentationNodeEvent | 312 | 2.37 | 1 | 4 | 0 | 2026-09-23T18:35:22.021000+00:00 | 2026-10-06T18:25:55.884000+00:00 | 311h 50m |
| ObjectInterEvent | 205 | 1.56 | 1 | 9 | 0 | 2026-09-23T18:21:51.792000+00:00 | 2026-10-06T18:34:12.774000+00:00 | 312h 12m |
| TopographicMapEvent | 166 | 1.26 | 1 | 3 | 0 | 2026-09-24T17:49:28.940000+00:00 | 2026-10-01T16:16:14.290000+00:00 | 166h 26m |
| questEvent | 85 | 0.65 | 1 | 9 | 85 | 2026-09-22T18:25:11.353000+00:00 | 2026-10-06T18:30:47.993000+00:00 | 336h 5m |
| gameWindowFocusEvent | 56 | 0.43 | 1 | 6 | 0 | 2026-09-22T18:24:33.311000+00:00 | 2026-10-06T18:05:32.868000+00:00 | 335h 40m |
| Soil Key Puzzle | 50 | 0.38 | 1 | 3 | 0 | 2026-09-24T17:57:47.445000+00:00 | 2026-10-05T18:25:59.717000+00:00 | 264h 28m |
| gameWindowUnfocusEvent | 41 | 0.31 | 1 | 8 | 0 | 2026-09-22T18:26:10.483000+00:00 | 2026-10-06T16:17:20.959000+00:00 | 333h 51m |
| DEBUGMenu | 29 | 0.22 | 1 | 8 | 0 | 2026-09-22T18:24:49.459000+00:00 | 2026-10-06T18:05:38.127000+00:00 | 335h 40m |
| WaterChamberEvent | 23 | 0.17 | 1 | 1 | 0 | 2026-10-06T18:08:54.802000+00:00 | 2026-10-06T18:17:55.345000+00:00 | 9m 0s |
| gameStartEvent | 23 | 0.17 | 1 | 1 | 0 | 2026-09-22T18:24:33.311000+00:00 | 2026-10-06T18:05:32.869000+00:00 | 335h 40m |
| argumentationToolEvent | 20 | 0.15 | 1 | 3 | 0 | 2026-09-23T18:36:01.473000+00:00 | 2026-10-06T18:25:04.478000+00:00 | 311h 49m |
| argumentationAnswerEvent | 18 | 0.14 | 1 | 4 | 0 | 2026-09-23T18:36:20.684000+00:00 | 2026-10-06T18:25:56.968000+00:00 | 311h 49m |
| DaniEvent | 16 | 0.12 | 1 | 4 | 0 | 2026-09-22T18:26:01.448000+00:00 | 2026-10-05T18:38:00.850000+00:00 | 312h 11m |
| soilMachine | 16 | 0.12 | 1 | 1 | 0 | 2026-10-05T18:36:25.226000+00:00 | 2026-10-05T18:46:49.498000+00:00 | 10m 24s |
| TerasGardenBox | 15 | 0.11 | 1 | 1 | 0 | 2026-10-06T16:04:01.824000+00:00 | 2026-10-06T16:05:33.654000+00:00 | 1m 31s |
| argumentationEvent | 12 | 0.09 | 1 | 4 | 0 | 2026-09-23T18:36:06.161000+00:00 | 2026-10-06T18:25:57.026000+00:00 | 311h 49m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-23T18:43:50.676000+00:00 | 2026-10-06T18:34:12.745000+00:00 | 311h 50m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-06T18:28:43.733000+00:00 | 2026-10-06T18:28:46.012000+00:00 | 2.3s |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-06T16:14:04.396000+00:00 | 2026-10-06T18:18:44.026000+00:00 | 2h 4m |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 78885.048s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 0.591s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.3s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.345s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 23.017s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.969s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 16 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; ctrl; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,3,I; A,4,I; A,C,2,II; B,3,I; B,C,A,2,II; C,2,II; C,D,2,II; C,D,3,II; C,D,B,2,II; D,C,4,II 
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
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
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
  - Observed: 27 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[229] _id=6ab41941485cab4c954f455b ts=2026-09-23T18:24:01.1710000Z`; `6aa4144c41b41dbac0c7f270.jsonl[271] _id=6ab419f5485cab4c954f4c56 ts=2026-09-23T18:27:01.2640000Z`; `6aa4144c41b41dbac0c7f270.jsonl[328] _id=6ab41a7b485cab4c954f4fe4 ts=2026-09-23T18:29:15.1160000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[20] _id=6ab2c7e1485cab4c954b6972 ts=2026-09-22T18:24:33.3110000Z`; `6aa4144c41b41dbac0c7f270.jsonl[85] _id=6ab4174b485cab4c954f36a0 ts=2026-09-23T18:15:38.9810000Z`; `6aa4144c41b41dbac0c7f270.jsonl[832] _id=6ab41e38485cab4c954f6eb3 ts=2026-09-23T18:45:12.6190000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 56 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 56} 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[29] _id=6ab2c7e1485cab4c954b6970 ts=2026-09-22T18:24:33.3110000Z`; `6aa4144c41b41dbac0c7f270.jsonl[84] _id=6ab4174a485cab4c954f369e ts=2026-09-23T18:15:38.9800000Z`; `6aa4144c41b41dbac0c7f270.jsonl[94] _id=6ab41773485cab4c954f379a ts=2026-09-23T18:16:19.0990000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 41 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 41} 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[63] _id=6ab2c842485cab4c954b69c4 ts=2026-09-22T18:26:10.4830000Z`; `6aa4144c41b41dbac0c7f270.jsonl[88] _id=6ab41754485cab4c954f36be ts=2026-09-23T18:15:48.4160000Z`; `6aa4144c41b41dbac0c7f270.jsonl[883] _id=6ab41eb0485cab4c954f7143 ts=2026-09-23T18:47:12.0430000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5109 | 0.001 | 0.65 | 236.868 | 9.748 | 352458.56 | 0.25 | 220 | 12 |
| PuzzlePieceVisibleEvent | 3035 | 0.0 | 0.023 | 342.035 | 1.188 | 353952.827 | 0.18 | 1945 | 8 |
| DialogueEvent | 2048 | 0.0 | 3.574 | 590.887 | 30.834 | 352465.647 | 0.1 | 611 | 11 |
| PlayerPositionEvent | 1842 | 1.659 | 10.0 | 656.85 | 11.051 | 352422.755 | 0.09 | 0 | 10 |
| argumentationNodeEvent | 311 | 0.001 | 0.383 | 3609.755 | 7.651 | 518974.419 | 0.02 | 62 | 4 |
| ObjectInterEvent | 204 | 0.001 | 10.514 | 5509.515 | 429.638 | 352493.778 | 0.01 | 3 | 9 |
| TopographicMapEvent | 165 | 0.023 | 3.462 | 3631.548 | 508.96 | 257608.785 | 0.02 | 2 | 8 |
| questEvent | 84 | 0.002 | 160.454 | 14404.008 | 84817.718 | 352496.393 | 0.0 | 13 | 13 |
| gameWindowFocusEvent | 55 | 0.724 | 72.869 | 21971.992 | 87225.013 | 352406.878 | 0.0 | 0 | 15 |
| Soil Key Puzzle | 49 | 0.189 | 0.852 | 19430.455 | 103945.601 | 431422.404 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 40 | 0.727 | 23.017 | 30046.762 | 96938.502 | 430319.386 | 0.0 | 0 | 13 |
| DEBUGMenu | 28 | 31.628 | 675.449 | 43158.881 | 199009.664 | 352553.796 | 0.0 | 0 | 14 |
| WaterChamberEvent | 22 | 0.744 | 13.644 | 24.57 | 76.992 | 79.415 | 2.44 | 0 | 0 |
| gameStartEvent | 22 | 31.608 | 1741.42 | 54929.98 | 250151.383 | 353094.553 | 0.0 | 0 | 12 |
| argumentationToolEvent | 19 | 0.069 | 1.345 | 59081.211 | 526859.816 | 604097.176 | 0.0 | 0 | 2 |
| argumentationAnswerEvent | 17 | 0.747 | 15.3 | 66033.899 | 528355.921 | 604165.071 | 0.0 | 0 | 3 |
| DaniEvent | 15 | 0.108 | 4.87 | 74927.96 | 335922.727 | 517835.783 | 0.0 | 0 | 6 |
| soilMachine | 15 | 1.715 | 4.969 | 41.618 | 160.105 | 245.564 | 1.44 | 0 | 0 |
| TerasGardenBox | 14 | 0.64 | 2.705 | 6.559 | 19.306 | 21.064 | 9.15 | 0 | 0 |
| argumentationEvent | 11 | 0.035 | 56.62 | 102053.715 | 556731.236 | 604094.904 | 0.0 | 2 | 3 |
| EndOfUnit | 3 | 8429.5 | 78885.048 | 374207.356 | 939665.274 | 1035307.521 | 0.0 | 0 | 3 |
| SolarStillDesignEvent | 3 | 0.539 | 0.591 | 0.76 | 1.093 | 1.149 | 78.98 | 0 | 0 |
| chatEvent | 3 | 148.241 | 785.988 | 2493.21 | 5969.46 | 6545.401 | 0.02 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 159 group(s), 228 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[978] _id=6ab5628c485cab4c95539cf4 ts=2026-09-24T17:48:58.7970000Z == 6aa4144c41b41dbac0c7f270.jsonl[898] _id=6ab5628c485cab4c95539cf6 ts=2026-09-24T17:48:58.7970000Z`; `6aa4144c41b41dbac0c7f270.jsonl[974] _id=6ab5628d485cab4c95539d09 ts=2026-09-24T17:48:59.2830000Z == 6aa4144c41b41dbac0c7f270.jsonl[980] _id=6ab5628d485cab4c95539d0c ts=2026-09-24T17:48:59.2830000Z`; `6aa4144c41b41dbac0c7f270.jsonl[985] _id=6ab5628e485cab4c95539d20 ts=2026-09-24T17:48:59.9650000Z == 6aa4144c41b41dbac0c7f270.jsonl[991] _id=6ab5628e485cab4c95539d22 ts=2026-09-24T17:48:59.9650000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4144c41b41dbac0c7f270.jsonl[191] _id=6ab418bf485cab4c954f4042 ts=2026-09-23T18:21:51.7920000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[18] _id=6ab418bf485cab4c954f4046 ts=2026-09-23T18:21:51.7970000Z`; `1ms: 6aa4144c41b41dbac0c7f270.jsonl[11110] _id=6ac519c9de269131f9b4c99f ts=2026-10-06T15:54:49.3470000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[11104] _id=6ac519c9de269131f9b4c9a1 ts=2026-10-06T15:54:49.3480000Z`; `2ms: 6aa4144c41b41dbac0c7f270.jsonl[11156] _id=6ac51a00de269131f9b4cbb5 ts=2026-10-06T15:55:44.0050000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[11159] _id=6ac51a00de269131f9b4cbb9 ts=2026-10-06T15:55:44.0070000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 471 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `18ms: 6aa4144c41b41dbac0c7f270.jsonl[969] _id=6ab5628c485cab4c95539cf0 ts=2026-09-24T17:48:58.7590000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[897] _id=6ab5628c485cab4c95539cf2 ts=2026-09-24T17:48:58.7770000Z`; `20ms: 6aa4144c41b41dbac0c7f270.jsonl[897] _id=6ab5628c485cab4c95539cf2 ts=2026-09-24T17:48:58.7770000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[978] _id=6ab5628c485cab4c95539cf4 ts=2026-09-24T17:48:58.7970000Z`; `15ms: 6aa4144c41b41dbac0c7f270.jsonl[898] _id=6ab5628c485cab4c95539cf6 ts=2026-09-24T17:48:58.7970000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[979] _id=6ab5628d485cab4c95539cf8 ts=2026-09-24T17:48:58.8120000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `777ms: 6aa4144c41b41dbac0c7f270.jsonl[4182] _id=6abab185485cab4c956fffa8 ts=2026-09-28T18:27:16.9830000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[4190] _id=6abab185485cab4c956fffcd ts=2026-09-28T18:27:17.7600000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `879ms: 6aa4144c41b41dbac0c7f270.jsonl[11439] _id=6ac51c00de269131f9b4d827 ts=2026-10-06T16:04:16.6340000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[11440] _id=6ac51c01de269131f9b4d829 ts=2026-10-06T16:04:17.5130000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa4144c41b41dbac0c7f270.jsonl[2615] _id=6ab56669485cab4c95540600 ts=2026-09-24T18:05:29.6470000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[2616] _id=6ab5666a485cab4c9554060c ts=2026-09-24T18:05:29.6750000Z`; `499ms: 6aa4144c41b41dbac0c7f270.jsonl[3802] _id=6abaaf95485cab4c956fcf07 ts=2026-09-28T18:19:01.7600000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[3806] _id=6abaaf96485cab4c956fcf1b ts=2026-09-28T18:19:02.2590000Z`; `426ms: 6aa4144c41b41dbac0c7f270.jsonl[6335] _id=6abc081a485cab4c9584cb21 ts=2026-09-29T18:48:56.4730000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[6322] _id=6abc081a485cab4c9584cb27 ts=2026-09-29T18:48:56.8990000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `747ms: 6aa4144c41b41dbac0c7f270.jsonl[7669] _id=6abd5496485cab4c95917b23 ts=2026-09-30T18:27:34.7430000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[7670] _id=6abd5497485cab4c95917b4c ts=2026-09-30T18:27:35.4900000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `40ms: 6aa4144c41b41dbac0c7f270.jsonl[7726] _id=6abd54c1485cab4c9591825f ts=2026-09-30T18:28:17.6650000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[7724] _id=6abd54c2485cab4c9591826f ts=2026-09-30T18:28:17.7050000Z`; `35ms: 6aa4144c41b41dbac0c7f270.jsonl[11326] _id=6ac51af6de269131f9b4d3c9 ts=2026-10-06T15:59:50.0980000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[11327] _id=6ac51af6de269131f9b4d3d1 ts=2026-10-06T15:59:50.1330000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 43 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `216ms: 6aa4144c41b41dbac0c7f270.jsonl[432] _id=6ab41bea485cab4c954f5ab3 ts=2026-09-23T18:35:22.9580000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[443] _id=6ab41beb485cab4c954f5ab7 ts=2026-09-23T18:35:23.1740000Z`; `437ms: 6aa4144c41b41dbac0c7f270.jsonl[442] _id=6ab41beb485cab4c954f5ab5 ts=2026-09-23T18:35:23.0370000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[444] _id=6ab41beb485cab4c954f5abb ts=2026-09-23T18:35:23.4740000Z`; `929ms: 6aa4144c41b41dbac0c7f270.jsonl[443] _id=6ab41beb485cab4c954f5ab7 ts=2026-09-23T18:35:23.1740000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[439] _id=6ab41bec485cab4c954f5ac7 ts=2026-09-23T18:35:24.1030000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `982ms: 6aa4144c41b41dbac0c7f270.jsonl[7594] _id=6abd543c485cab4c95916e51 ts=2026-09-30T18:26:04.8060000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[7592] _id=6abd543d485cab4c95916e71 ts=2026-09-30T18:26:05.7880000Z`; `884ms: 6aa4144c41b41dbac0c7f270.jsonl[12817] _id=6ac53cfede269131f9b65dab ts=2026-10-06T18:25:02.7640000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[12822] _id=6ac53cffde269131f9b65db9 ts=2026-10-06T18:25:03.6480000Z`; `515ms: 6aa4144c41b41dbac0c7f270.jsonl[12818] _id=6ac53cffde269131f9b65db5 ts=2026-10-06T18:25:03.5390000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[12819] _id=6ac53d00de269131f9b65dc3 ts=2026-10-06T18:25:04.0540000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `875ms: 6aa4144c41b41dbac0c7f270.jsonl[5226] _id=6abc0199485cab4c95845ab5 ts=2026-09-29T18:21:13.5280000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[5218] _id=6abc019a485cab4c95845ac7 ts=2026-09-29T18:21:14.4030000Z`; `724ms: 6aa4144c41b41dbac0c7f270.jsonl[5218] _id=6abc019a485cab4c95845ac7 ts=2026-09-29T18:21:14.4030000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[5219] _id=6abc019b485cab4c95845ae3 ts=2026-09-29T18:21:15.1270000Z`; `892ms: 6aa4144c41b41dbac0c7f270.jsonl[5231] _id=6abc019c485cab4c95845aff ts=2026-09-29T18:21:16.1410000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[5230] _id=6abc019d485cab4c95845b1f ts=2026-09-29T18:21:17.0330000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `892ms: 6aa4144c41b41dbac0c7f270.jsonl[5220] _id=6abc0199485cab4c95845ab1 ts=2026-09-29T18:21:13.4990000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[5217] _id=6abc019a485cab4c95845ac3 ts=2026-09-29T18:21:14.3910000Z`; `727ms: 6aa4144c41b41dbac0c7f270.jsonl[5217] _id=6abc019a485cab4c95845ac3 ts=2026-09-29T18:21:14.3910000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[5227] _id=6abc019b485cab4c95845adf ts=2026-09-29T18:21:15.1180000Z`; `880ms: 6aa4144c41b41dbac0c7f270.jsonl[5216] _id=6abc019c485cab4c95845af9 ts=2026-09-29T18:21:16.1250000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[5229] _id=6abc019d485cab4c95845b1d ts=2026-09-29T18:21:17.0050000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4144c41b41dbac0c7f270.jsonl[12942] _id=6ac53d7bde269131f9b666f9 ts=2026-10-06T18:27:06.9490000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[12943] _id=6ac53d7bde269131f9b666fb ts=2026-10-06T18:27:06.9510000Z`; `3ms: 6aa4144c41b41dbac0c7f270.jsonl[13052] _id=6ac53e1cde269131f9b66fc7 ts=2026-10-06T18:29:48.0310000Z ~ 6aa4144c41b41dbac0c7f270.jsonl[13050] _id=6ac53e1cde269131f9b66fca ts=2026-10-06T18:29:48.0340000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 97h 55m 
  - Evidence: 97h 55m: 6aa4144c41b41dbac0c7f270.jsonl[8898] _id=6abe8701485cab4c95abccfa ts=2026-10-01T16:14:57.4300000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8975] _id=6ac3e82bde269131f9aec72f ts=2026-10-05T18:10:51.2260000Z; 71h 51m: 6aa4144c41b41dbac0c7f270.jsonl[2861] _id=6ab6ba17485cab4c955dd3f1 ts=2026-09-25T18:14:48.0360000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3454] _id=6abaaca0485cab4c956f6fe5 ts=2026-09-28T18:06:24.7450000Z; 24h 29m: 6aa4144c41b41dbac0c7f270.jsonl[901] _id=6ab561b5485cab4c95538ce3 ts=2026-09-24T17:45:25.7410000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2861] _id=6ab6ba17485cab4c955dd3f1 ts=2026-09-25T18:14:48.0360000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 50m 
  - Evidence: 143h 50m: 6aa4144c41b41dbac0c7f270.jsonl[6180] _id=6abc07bb485cab4c9584c5ad ts=2026-09-29T18:47:23.3500000Z -> 6aa4144c41b41dbac0c7f270.jsonl[10167] _id=6ac3ee87de269131f9af2e1f ts=2026-10-05T18:37:59.1330000Z; 71h 39m: 6aa4144c41b41dbac0c7f270.jsonl[3193] _id=6ab6bf30485cab4c955e538d ts=2026-09-25T18:36:32.1400000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3657] _id=6abaaed8485cab4c956fafc3 ts=2026-09-28T18:15:52.1280000Z; 47h 43m: 6aa4144c41b41dbac0c7f270.jsonl[48] _id=6ab2c83e485cab4c954b69c0 ts=2026-09-22T18:26:06.3180000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2703] _id=6ab56749485cab4c95541ab6 ts=2026-09-24T18:09:13.1930000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 97h 54m 
  - Evidence: 97h 54m: 6aa4144c41b41dbac0c7f270.jsonl[8960] _id=6abe8783485cab4c95abd468 ts=2026-10-01T16:17:07.8720000Z -> 6aa4144c41b41dbac0c7f270.jsonl[9002] _id=6ac3e855de269131f9aec979 ts=2026-10-05T18:11:33.5190000Z; 71h 21m: 6aa4144c41b41dbac0c7f270.jsonl[3448] _id=6ab6c193485cab4c955e6ad3 ts=2026-09-25T18:46:43.3530000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3498] _id=6abaad04485cab4c956f75f5 ts=2026-09-28T18:08:04.7320000Z; 24h 4m: 6aa4144c41b41dbac0c7f270.jsonl[2757] _id=6ab567d5485cab4c955420a8 ts=2026-09-24T18:11:33.3870000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2886] _id=6ab6ba4d485cab4c955dda59 ts=2026-09-25T18:15:41.2360000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 611 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f270.jsonl[12873] _id=6ac53d22de269131f9b66055 ts=2026-10-06T18:25:38.3700000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12876] _id=6ac53d22de269131f9b66059 ts=2026-10-06T18:25:38.3700000Z; 1ms: 6aa4144c41b41dbac0c7f270.jsonl[12671] _id=6ac53b73de269131f9b6431f ts=2026-10-06T18:18:27.3100000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12672] _id=6ac53b73de269131f9b64325 ts=2026-10-06T18:18:27.3110000Z; 1ms: 6aa4144c41b41dbac0c7f270.jsonl[2580] _id=6ab56612485cab4c9553fc7a ts=2026-09-24T18:04:02.2610000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2581] _id=6ab56612485cab4c9553fc80 ts=2026-09-24T18:04:02.2620000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 287h 35m 
  - Evidence: 287h 35m: 6aa4144c41b41dbac0c7f270.jsonl[830] _id=6ab41de6485cab4c954f6b95 ts=2026-09-23T18:43:50.6760000Z -> 6aa4144c41b41dbac0c7f270.jsonl[9144] _id=6ac3ea12de269131f9aede94 ts=2026-10-05T18:18:58.1970000Z; 21h 54m: 6aa4144c41b41dbac0c7f270.jsonl[9144] _id=6ac3ea12de269131f9aede94 ts=2026-10-05T18:18:58.1970000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11648] _id=6ac51e37de269131f9b4eb9b ts=2026-10-06T16:13:43.2450000Z; 2h 20m: 6aa4144c41b41dbac0c7f270.jsonl[11648] _id=6ac51e37de269131f9b4eb9b ts=2026-10-06T16:13:43.2450000Z -> 6aa4144c41b41dbac0c7f270.jsonl[13148] _id=6ac53f24de269131f9b6864d ts=2026-10-06T18:34:12.7450000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 97h 54m 
  - Evidence: 97h 54m: 6aa4144c41b41dbac0c7f270.jsonl[8951] _id=6abe8765485cab4c95abd2c0 ts=2026-10-01T16:16:37.2030000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8977] _id=6ac3e832de269131f9aec7a5 ts=2026-10-05T18:10:55.7630000Z; 71h 19m: 6aa4144c41b41dbac0c7f270.jsonl[3380] _id=6ab6c18b485cab4c955e6ab9 ts=2026-09-25T18:46:35.7660000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3461] _id=6abaaca7485cab4c956f7091 ts=2026-09-28T18:06:30.9450000Z; 24h 1m: 6aa4144c41b41dbac0c7f270.jsonl[2857] _id=6ab56857485cab4c955424c2 ts=2026-09-24T18:13:43.2520000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2866] _id=6ab6ba1e485cab4c955dd4a1 ts=2026-09-25T18:14:53.9360000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 220 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f270.jsonl[10554] _id=6ac3f0c7de269131f9af60c9 ts=2026-10-05T18:47:35.2920000Z -> 6aa4144c41b41dbac0c7f270.jsonl[10555] _id=6ac3f0c7de269131f9af60cb ts=2026-10-05T18:47:35.2930000Z; 1ms: 6aa4144c41b41dbac0c7f270.jsonl[10555] _id=6ac3f0c7de269131f9af60cb ts=2026-10-05T18:47:35.2930000Z -> 6aa4144c41b41dbac0c7f270.jsonl[10571] _id=6ac3f0c7de269131f9af60cd ts=2026-10-05T18:47:35.2940000Z; 1ms: 6aa4144c41b41dbac0c7f270.jsonl[10656] _id=6ac517a6de269131f9b4b3a9 ts=2026-10-06T15:45:43.5790000Z -> 6aa4144c41b41dbac0c7f270.jsonl[10657] _id=6ac517a6de269131f9b4b3ad ts=2026-10-06T15:45:43.5800000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 97h 54m 
  - Evidence: 97h 54m: 6aa4144c41b41dbac0c7f270.jsonl[8955] _id=6abe8767485cab4c95abd2e4 ts=2026-10-01T16:16:39.7220000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8995] _id=6ac3e855de269131f9aec973 ts=2026-10-05T18:11:33.5000000Z; 96h 29m: 6aa4144c41b41dbac0c7f270.jsonl[2415] _id=6ab5649b485cab4c9553c7aa ts=2026-09-24T17:57:47.4520000Z -> 6aa4144c41b41dbac0c7f270.jsonl[4184] _id=6abab181485cab4c956fff2f ts=2026-09-28T18:27:13.8720000Z; 24h 1m: 6aa4144c41b41dbac0c7f270.jsonl[4653] _id=6abab2a0485cab4c95701407 ts=2026-09-28T18:31:59.9120000Z -> 6aa4144c41b41dbac0c7f270.jsonl[5400] _id=6abc0496485cab4c95848c65 ts=2026-09-29T18:33:58.1590000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.005s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f270.jsonl[11110] _id=6ac519c9de269131f9b4c99f ts=2026-10-06T15:54:49.3470000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11104] _id=6ac519c9de269131f9b4c9a1 ts=2026-10-06T15:54:49.3480000Z; 2ms: 6aa4144c41b41dbac0c7f270.jsonl[11156] _id=6ac51a00de269131f9b4cbb5 ts=2026-10-06T15:55:44.0050000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11159] _id=6ac51a00de269131f9b4cbb9 ts=2026-10-06T15:55:44.0070000Z; 5ms: 6aa4144c41b41dbac0c7f270.jsonl[191] _id=6ab418bf485cab4c954f4042 ts=2026-09-23T18:21:51.7920000Z -> 6aa4144c41b41dbac0c7f270.jsonl[18] _id=6ab418bf485cab4c954f4046 ts=2026-09-23T18:21:51.7970000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 97h 53m 
  - Evidence: 97h 53m: 6aa4144c41b41dbac0c7f270.jsonl[8964] _id=6abe8784485cab4c95abd46a ts=2026-10-01T16:17:08.4790000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8976] _id=6ac3e831de269131f9aec7a1 ts=2026-10-05T18:10:51.2340000Z; 71h 19m: 6aa4144c41b41dbac0c7f270.jsonl[3449] _id=6ab6c19c485cab4c955e6ae7 ts=2026-09-25T18:46:53.0020000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3460] _id=6abaaca7485cab4c956f708b ts=2026-09-28T18:06:24.7500000Z; 24h 1m: 6aa4144c41b41dbac0c7f270.jsonl[2856] _id=6ab56856485cab4c955424be ts=2026-09-24T18:13:42.2650000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2862] _id=6ab6ba1e485cab4c955dd49f ts=2026-09-25T18:14:48.0410000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 98h 19m 
  - Evidence: 98h 19m: 6aa4144c41b41dbac0c7f270.jsonl[8606] _id=6abe851c485cab4c95abbb78 ts=2026-10-01T16:06:49.8060000Z -> 6aa4144c41b41dbac0c7f270.jsonl[9245] _id=6ac3ebbbde269131f9aefab1 ts=2026-10-05T18:26:02.6330000Z; 96h 26m: 6aa4144c41b41dbac0c7f270.jsonl[2402] _id=6ab56469485cab4c9553c3b0 ts=2026-09-24T17:56:55.4920000Z -> 6aa4144c41b41dbac0c7f270.jsonl[4005] _id=6abab082485cab4c956feb91 ts=2026-09-28T18:22:56.9430000Z; 48h 1m: 6aa4144c41b41dbac0c7f270.jsonl[4840] _id=6abab33e485cab4c95701ee9 ts=2026-09-28T18:34:36.8300000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8176] _id=6abd568f485cab4c9591c4db ts=2026-09-30T18:35:58.2360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1945 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f270.jsonl[1022] _id=6ab56293485cab4c95539d76 ts=2026-09-24T17:49:06.0520000Z -> 6aa4144c41b41dbac0c7f270.jsonl[1299] _id=6ab5630f485cab4c9553a766 ts=2026-09-24T17:49:06.0520000Z; 0ms: 6aa4144c41b41dbac0c7f270.jsonl[1028] _id=6ab56292485cab4c95539d66 ts=2026-09-24T17:49:05.9830000Z -> 6aa4144c41b41dbac0c7f270.jsonl[1026] _id=6ab56292485cab4c95539d69 ts=2026-09-24T17:49:05.9830000Z; 0ms: 6aa4144c41b41dbac0c7f270.jsonl[1030] _id=6ab56293485cab4c95539d82 ts=2026-09-24T17:49:06.0820000Z -> 6aa4144c41b41dbac0c7f270.jsonl[1309] _id=6ab5630f485cab4c9553a776 ts=2026-09-24T17:49:06.0820000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6aa4144c41b41dbac0c7f270.jsonl[8154] _id=6abd5668485cab4c9591bf25 ts=2026-09-30T18:35:20.1230000Z -> 6aa4144c41b41dbac0c7f270.jsonl[9231] _id=6ac3eba6de269131f9aef9bb ts=2026-10-05T18:25:42.5270000Z; 96h 29m: 6aa4144c41b41dbac0c7f270.jsonl[2413] _id=6ab5649e485cab4c9553c81a ts=2026-09-24T17:57:50.4470000Z -> 6aa4144c41b41dbac0c7f270.jsonl[4183] _id=6abab181485cab4c956fff29 ts=2026-09-28T18:27:13.8670000Z; 48h 7m: 6aa4144c41b41dbac0c7f270.jsonl[4210] _id=6abab1aa485cab4c95700263 ts=2026-09-28T18:27:54.4780000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8140] _id=6abd565b485cab4c9591bd4f ts=2026-09-30T18:35:07.2560000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 71h 33m 
  - Evidence: 71h 33m: 6aa4144c41b41dbac0c7f270.jsonl[3195] _id=6ab6bf3f485cab4c955e5419 ts=2026-09-25T18:36:47.5640000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3522] _id=6abaad88485cab4c956f87fd ts=2026-09-28T18:10:16.3490000Z; 24h 5m: 6aa4144c41b41dbac0c7f270.jsonl[2760] _id=6ab567d8485cab4c955420c0 ts=2026-09-24T18:11:36.4310000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2904] _id=6ab6baa9485cab4c955de8bd ts=2026-09-25T18:17:14.0620000Z; 23h 46m: 6aa4144c41b41dbac0c7f270.jsonl[5064] _id=6abab5cc485cab4c95705918 ts=2026-09-28T18:45:32.1130000Z -> 6aa4144c41b41dbac0c7f270.jsonl[5361] _id=6abc0421485cab4c9584866a ts=2026-09-29T18:32:01.7440000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.028s shown 
  - Evidence: 23ms: 6aa4144c41b41dbac0c7f270.jsonl[2614] _id=6ab56669485cab4c955405fe ts=2026-09-24T18:05:29.6240000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2615] _id=6ab56669485cab4c95540600 ts=2026-09-24T18:05:29.6470000Z; 28ms: 6aa4144c41b41dbac0c7f270.jsonl[2615] _id=6ab56669485cab4c95540600 ts=2026-09-24T18:05:29.6470000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2616] _id=6ab5666a485cab4c9554060c ts=2026-09-24T18:05:29.6750000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 49m 
  - Evidence: 167h 49m: 6aa4144c41b41dbac0c7f270.jsonl[559] _id=6ab41c7b485cab4c954f5f89 ts=2026-09-23T18:37:47.7360000Z -> 6aa4144c41b41dbac0c7f270.jsonl[7636] _id=6abd5480485cab4c9591785d ts=2026-09-30T18:27:12.8070000Z; 141h 30m: 6aa4144c41b41dbac0c7f270.jsonl[7722] _id=6abd54c1485cab4c9591825c ts=2026-09-30T18:28:17.6360000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11234] _id=6ac51a9dde269131f9b4d12f ts=2026-10-06T15:58:21.2690000Z; 2h 25m: 6aa4144c41b41dbac0c7f270.jsonl[11331] _id=6ac51af6de269131f9b4d3c7 ts=2026-10-06T15:59:50.0850000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12875] _id=6ac53d22de269131f9b66053 ts=2026-10-06T18:25:38.3180000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 48m 
  - Evidence: 167h 48m: 6aa4144c41b41dbac0c7f270.jsonl[560] _id=6ab41c7b485cab4c954f5f8b ts=2026-09-23T18:37:47.7690000Z -> 6aa4144c41b41dbac0c7f270.jsonl[7595] _id=6abd543a485cab4c95916e02 ts=2026-09-30T18:26:02.6730000Z; 141h 29m: 6aa4144c41b41dbac0c7f270.jsonl[7724] _id=6abd54c2485cab4c9591826f ts=2026-09-30T18:28:17.7050000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11181] _id=6ac51a79de269131f9b4d013 ts=2026-10-06T15:57:45.2740000Z; 2h 25m: 6aa4144c41b41dbac0c7f270.jsonl[11327] _id=6ac51af6de269131f9b4d3d1 ts=2026-10-06T15:59:50.1330000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12814] _id=6ac53cfcde269131f9b65d8a ts=2026-10-06T18:25:00.4060000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.035s..0.040s shown 
  - Evidence: 35ms: 6aa4144c41b41dbac0c7f270.jsonl[11326] _id=6ac51af6de269131f9b4d3c9 ts=2026-10-06T15:59:50.0980000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11327] _id=6ac51af6de269131f9b4d3d1 ts=2026-10-06T15:59:50.1330000Z; 40ms: 6aa4144c41b41dbac0c7f270.jsonl[7726] _id=6abd54c1485cab4c9591825f ts=2026-09-30T18:28:17.6650000Z -> 6aa4144c41b41dbac0c7f270.jsonl[7724] _id=6abd54c2485cab4c9591826f ts=2026-09-30T18:28:17.7050000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 9m 
  - Evidence: 144h 9m: 6aa4144c41b41dbac0c7f270.jsonl[555] _id=6ab41c77485cab4c954f5f6d ts=2026-09-23T18:37:43.6720000Z -> 6aa4144c41b41dbac0c7f270.jsonl[6174] _id=6abc07b6485cab4c9584c55d ts=2026-09-29T18:47:18.0910000Z; 141h 29m: 6aa4144c41b41dbac0c7f270.jsonl[7736] _id=6abd54c0485cab4c95918229 ts=2026-09-30T18:28:16.2600000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11213] _id=6ac51a7bde269131f9b4d019 ts=2026-10-06T15:57:46.9720000Z; 23h 38m: 6aa4144c41b41dbac0c7f270.jsonl[6142] _id=6abc07b7485cab4c9584c573 ts=2026-09-29T18:47:19.4850000Z -> 6aa4144c41b41dbac0c7f270.jsonl[7587] _id=6abd5434485cab4c95916d54 ts=2026-09-30T18:25:56.3740000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 62 interval(s) ≤ 0.001s..0.017s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f270.jsonl[12831] _id=6ac53d08de269131f9b65e55 ts=2026-10-06T18:25:12.1330000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12832] _id=6ac53d08de269131f9b65e59 ts=2026-10-06T18:25:12.1340000Z; 16ms: 6aa4144c41b41dbac0c7f270.jsonl[469] _id=6ab41c1d485cab4c954f5c17 ts=2026-09-23T18:36:13.7370000Z -> 6aa4144c41b41dbac0c7f270.jsonl[472] _id=6ab41c1d485cab4c954f5c19 ts=2026-09-23T18:36:13.7530000Z; 17ms: 6aa4144c41b41dbac0c7f270.jsonl[518] _id=6ab41c51485cab4c954f5df9 ts=2026-09-23T18:37:05.6050000Z -> 6aa4144c41b41dbac0c7f270.jsonl[519] _id=6ab41c51485cab4c954f5dfb ts=2026-09-23T18:37:05.6220000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 48m 
  - Evidence: 167h 48m: 6aa4144c41b41dbac0c7f270.jsonl[565] _id=6ab41c7b485cab4c954f5f87 ts=2026-09-23T18:37:47.6300000Z -> 6aa4144c41b41dbac0c7f270.jsonl[7594] _id=6abd543c485cab4c95916e51 ts=2026-09-30T18:26:04.8060000Z; 143h 57m: 6aa4144c41b41dbac0c7f270.jsonl[7619] _id=6abd5477485cab4c95917685 ts=2026-09-30T18:27:03.2060000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12812] _id=6ac53cfdde269131f9b65d93 ts=2026-10-06T18:25:01.0930000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 1h 49m 
  - Evidence: 1h 49m: 6aa4144c41b41dbac0c7f270.jsonl[11653] _id=6ac51e4cde269131f9b4ec1e ts=2026-10-06T16:14:04.3960000Z -> 6aa4144c41b41dbac0c7f270.jsonl[11841] _id=6ac537ddde269131f9b619a5 ts=2026-10-06T18:03:09.7970000Z; 13m 5s: 6aa4144c41b41dbac0c7f270.jsonl[11929] _id=6ac53872de269131f9b61d04 ts=2026-10-06T18:05:38.0380000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12561] _id=6ac53b84de269131f9b64419 ts=2026-10-06T18:18:44.0260000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 98h 4m 
  - Evidence: 98h 4m: 6aa4144c41b41dbac0c7f270.jsonl[8497] _id=6abe84d6485cab4c95abb628 ts=2026-10-01T16:05:42.4700000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8972] _id=6ac3e81dde269131f9aec505 ts=2026-10-05T18:10:37.0230000Z; 71h 51m: 6aa4144c41b41dbac0c7f270.jsonl[2860] _id=6ab6ba11485cab4c955dd361 ts=2026-09-25T18:14:41.1280000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3452] _id=6abaac86485cab4c956f6e93 ts=2026-09-28T18:05:58.2710000Z; 24h 29m: 6aa4144c41b41dbac0c7f270.jsonl[900] _id=6ab561af485cab4c95538c2e ts=2026-09-24T17:45:19.1830000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2860] _id=6ab6ba11485cab4c955dd361 ts=2026-09-25T18:14:41.1280000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 97h 53m 
  - Evidence: 97h 53m: 6aa4144c41b41dbac0c7f270.jsonl[8961] _id=6abe8786485cab4c95abd46e ts=2026-10-01T16:17:10.1440000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8971] _id=6ac3e81dde269131f9aec4ff ts=2026-10-05T18:10:37.0220000Z; 71h 23m: 6aa4144c41b41dbac0c7f270.jsonl[3348] _id=6ab6c08a485cab4c955e66bd ts=2026-09-25T18:42:18.4700000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3453] _id=6abaac86485cab4c956f6e91 ts=2026-09-28T18:05:58.2700000Z; 24h 28m: 6aa4144c41b41dbac0c7f270.jsonl[929] _id=6ab561e1485cab4c9553909e ts=2026-09-24T17:46:09.3320000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2859] _id=6ab6ba11485cab4c955dd35e ts=2026-09-25T18:14:41.1270000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6aa4144c41b41dbac0c7f270.jsonl[8965] _id=6abe8786485cab4c95abd46c ts=2026-10-01T16:17:10.1300000Z -> 6aa4144c41b41dbac0c7f270.jsonl[10898] _id=6ac51874de269131f9b4c0ab ts=2026-10-06T15:49:09.5160000Z; 72h 1m: 6aa4144c41b41dbac0c7f270.jsonl[3450] _id=6ab6c19d485cab4c955e6aeb ts=2026-09-25T18:46:53.2410000Z -> 6aa4144c41b41dbac0c7f270.jsonl[5097] _id=6abab65b485cab4c95706bdc ts=2026-09-28T18:47:55.1870000Z; 24h 33m: 6aa4144c41b41dbac0c7f270.jsonl[928] _id=6ab561da485cab4c95539003 ts=2026-09-24T17:46:02.3850000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2988] _id=6ab6bb25485cab4c955dfe05 ts=2026-09-25T18:19:17.5480000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 97h 54m 
  - Evidence: 97h 54m: 6aa4144c41b41dbac0c7f270.jsonl[8931] _id=6abe8740485cab4c95abd044 ts=2026-10-01T16:16:00.9050000Z -> 6aa4144c41b41dbac0c7f270.jsonl[8978] _id=6ac3e832de269131f9aec7a9 ts=2026-10-05T18:10:57.2980000Z; 71h 51m: 6aa4144c41b41dbac0c7f270.jsonl[2867] _id=6ab6ba1f485cab4c955dd4ab ts=2026-09-25T18:14:53.9910000Z -> 6aa4144c41b41dbac0c7f270.jsonl[3464] _id=6abaaca8485cab4c956f70ab ts=2026-09-28T18:06:30.9770000Z; 24h 9m: 6aa4144c41b41dbac0c7f270.jsonl[2603] _id=6ab5664e485cab4c955403f6 ts=2026-09-24T18:05:02.8420000Z -> 6aa4144c41b41dbac0c7f270.jsonl[2867] _id=6ab6ba1f485cab4c955dd4ab ts=2026-09-25T18:14:53.9910000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4144c41b41dbac0c7f270.jsonl[12942] _id=6ac53d7bde269131f9b666f9 ts=2026-10-06T18:27:06.9490000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12943] _id=6ac53d7bde269131f9b666fb ts=2026-10-06T18:27:06.9510000Z; 2ms: 6aa4144c41b41dbac0c7f270.jsonl[426] _id=6ab41bc6485cab4c954f598e ts=2026-09-23T18:34:46.4580000Z -> 6aa4144c41b41dbac0c7f270.jsonl[423] _id=6ab41bc6485cab4c954f5990 ts=2026-09-23T18:34:46.4600000Z; 3ms: 6aa4144c41b41dbac0c7f270.jsonl[12400] _id=6ac539acde269131f9b62b5d ts=2026-10-06T18:10:52.2960000Z -> 6aa4144c41b41dbac0c7f270.jsonl[12401] _id=6ac539acde269131f9b62b65 ts=2026-10-06T18:10:52.2990000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[569] _id=6ab41c8d485cab4c954f601d ts=2026-09-23T18:38:05.4610000Z`; `6aa4144c41b41dbac0c7f270.jsonl[2757] _id=6ab567d5485cab4c955420a8 ts=2026-09-24T18:11:33.3870000Z`; `6aa4144c41b41dbac0c7f270.jsonl[2909] _id=6ab6babc485cab4c955deb93 ts=2026-09-25T18:17:32.6060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 102 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[1408] _id=6ab5631c485cab4c9553a922 ts=2026-09-24T17:50:56.4390000Z`; `6aa4144c41b41dbac0c7f270.jsonl[1675] _id=6ab56352485cab4c9553add2 ts=2026-09-24T17:52:16.7520000Z`; `6aa4144c41b41dbac0c7f270.jsonl[1733] _id=6ab56352485cab4c9553add6 ts=2026-09-24T17:52:16.7820000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 308 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[1303] _id=6ab5630e485cab4c9553a756 ts=2026-09-24T17:48:57.1570000Z`; `6aa4144c41b41dbac0c7f270.jsonl[898] _id=6ab5628c485cab4c95539cf6 ts=2026-09-24T17:48:58.7970000Z`; `6aa4144c41b41dbac0c7f270.jsonl[979] _id=6ab5628d485cab4c95539cf8 ts=2026-09-24T17:48:58.8120000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[7724] _id=6abd54c2485cab4c9591826f ts=2026-09-30T18:28:17.7050000Z`; `6aa4144c41b41dbac0c7f270.jsonl[11327] _id=6ac51af6de269131f9b4d3d1 ts=2026-10-06T15:59:50.1330000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[472] _id=6ab41c1d485cab4c954f5c19 ts=2026-09-23T18:36:13.7530000Z`; `6aa4144c41b41dbac0c7f270.jsonl[477] _id=6ab41c22485cab4c954f5c43 ts=2026-09-23T18:36:18.2060000Z`; `6aa4144c41b41dbac0c7f270.jsonl[479] _id=6ab41c23485cab4c954f5c4d ts=2026-09-23T18:36:19.1510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[11653] _id=6ac51e4cde269131f9b4ec1e ts=2026-10-06T16:14:04.3960000Z`; `6aa4144c41b41dbac0c7f270.jsonl[11841] _id=6ac537ddde269131f9b619a5 ts=2026-10-06T18:03:09.7970000Z`; `6aa4144c41b41dbac0c7f270.jsonl[11929] _id=6ac53872de269131f9b61d04 ts=2026-10-06T18:05:38.0380000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[888] _id=6ab41eb3485cab4c954f7147 ts=?`; `6aa4144c41b41dbac0c7f270.jsonl[5272] _id=6abc0278485cab4c95846859 ts=?`; `6aa4144c41b41dbac0c7f270.jsonl[6469] _id=6abd4f1d485cab4c9590d553 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 391 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[1690] _id=6ab56347485cab4c9553ad46 ts=2026-09-24T17:52:06.2510000Z`; `6aa4144c41b41dbac0c7f270.jsonl[1705] _id=6ab56350485cab4c9553adc0 ts=2026-09-24T17:52:16.0320000Z`; `6aa4144c41b41dbac0c7f270.jsonl[1747] _id=6ab56356485cab4c9553ae4a ts=2026-09-24T17:52:20.5300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 561 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[1296] _id=6ab5630e485cab4c9553a747 ts=2026-09-24T17:48:56.7780000Z`; `6aa4144c41b41dbac0c7f270.jsonl[973] _id=6ab5628b485cab4c95539cd8 ts=2026-09-24T17:48:58.7240000Z`; `6aa4144c41b41dbac0c7f270.jsonl[896] _id=6ab5628b485cab4c95539cde ts=2026-09-24T17:48:58.7270000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 45 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[2615] _id=6ab56669485cab4c95540600 ts=2026-09-24T18:05:29.6470000Z`; `6aa4144c41b41dbac0c7f270.jsonl[2616] _id=6ab5666a485cab4c9554060c ts=2026-09-24T18:05:29.6750000Z`; `6aa4144c41b41dbac0c7f270.jsonl[2692] _id=6ab56734485cab4c955418ee ts=2026-09-24T18:08:52.2110000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[12874] _id=6ac53d20de269131f9b6602d ts=2026-10-06T18:25:36.0750000Z`; `6aa4144c41b41dbac0c7f270.jsonl[12883] _id=6ac53d2cde269131f9b660fa ts=2026-10-06T18:25:48.1350000Z`; `6aa4144c41b41dbac0c7f270.jsonl[12887] _id=6ac53d30de269131f9b6614c ts=2026-10-06T18:25:52.2610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 10 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[558] _id=6ab41c7b485cab4c954f5f85 ts=2026-09-23T18:37:47.1340000Z`; `6aa4144c41b41dbac0c7f270.jsonl[7592] _id=6abd543d485cab4c95916e71 ts=2026-09-30T18:26:05.7880000Z`; `6aa4144c41b41dbac0c7f270.jsonl[7600] _id=6abd543f485cab4c95916ebb ts=2026-09-30T18:26:07.6220000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 396 start, 388 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 149 unmatched 'BecameCameraCentered' (totals: 570 open, 523 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 105 unmatched 'BecameVisible' (totals: 870 open, 1073 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 136 open, 141 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 15 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'questActiveEvent' (totals: 54 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 263 of 13147 adjacent _id pairs reverse in client time; worst 131.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f270.jsonl[1265] _id=6ab5630b485cab4c9553a702 ts=2026-09-24T17:51:07.7910000Z`; `6aa4144c41b41dbac0c7f270.jsonl[1279] _id=6ab5630c485cab4c9553a70a ts=2026-09-24T17:48:56.4000000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -133.60s, max +1.86s over 13148 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f270\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5110 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2108); Unit 2 Prod (Refactor) (1443); Unit 4 Dev - Dungeon (389); Unit 1 Dev (326); Unit 5 Dev - Dungeon (256); Unit 4 Dev (214); Unit 3 Dungeon Dev (201); Unit 4 Dev - Anderson Base (98); Unit 5 Dev (75)
- **Intervals:** median 0.65s (p5 0.07s / p95 9.75s, n=5109)
- **Fields under `data`:**

```text
data.Value  (string, 5110/5110 records)
    "pressed"  x5110
data.actionType  (string, 5110/5110 records)
    "Move"  x3096
    "Jump"  x902
    "Interact"  x532
    "Sprint"  x188
    "Hoverboard"  x173
    "Ascend"  x133
    "Map"  x44
    "ToggleDebug"  x26
    "Descend"  x10
    "Pause"  x3
    "SkipCinematic"  x3
data.key  (string, 5110/5110 records, 65 empty-string)
    21 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5110/5110 records)
    "Player"  x3585
    "Drone"  x1525
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3036 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1534); Unit 4 Dev (700); Unit 5 Dev - Dungeon (526); Unit 3 Dungeon Dev (276)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.19s, n=3035)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3036/3036 records)
    "BecameInvisible"  x1073
    "BecameVisible"  x870
    "BecameCameraCentered"  x570
    "BecameCameraUncentered"  x523
data.pieceId  (string, 3036/3036 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3036/3036 records)
    1760 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2049 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (545); Unit 3 Dev (406); Unit 4 Dev (282); Unit 5 Dev (218); Unit 1 Dev (198); Unit 3 Dungeon Dev (132); Unit 4 Dev - Dungeon (99); Unit 4 Dev - Anderson Base (90); Unit 5 Dev - Dungeon (79)
- **eventKey:** present on 1265 of 2049 records
- **Intervals:** median 3.57s (p5 0.00s / p95 30.83s, n=2048)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1265; [conversationId, dialogueEventType] x784
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2049/2049 records)
    numeric range 8 .. 118 (54 unique)
data.dialogueEventType  (string, 2049/2049 records)
    "DialogueNodeEvent"  x1265
    "DialogueStartEvent"  x396
    "DialogueFinishEvent"  x388
data.nodeId  (number, 1265/2049 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1854 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (660); Unit 3 Dev (369); Unit 4 Dev (202); Unit 1 Dev (178); Unit 4 Dev - Dungeon (115); Unit 5 Dev - Dungeon (111); Unit 5 Dev (93); Unit 3 Dungeon Dev (79); Unit 4 Dev - Anderson Base (47)
- **Intervals:** median 10.00s (p5 9.98s / p95 11.05s, n=1842)
- **Fields under `data`:**

```text
data.position  (object, 1854/1854 records)
data.position.x  (number, 1854/1854 records)
    numeric range -702.364 .. 1554.05 (711 unique)
data.position.y  (number, 1854/1854 records)
    numeric range -112.49 .. 218.656 (587 unique)
data.position.z  (number, 1854/1854 records)
    numeric range -1100.12 .. 2051.13 (710 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 312 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (93); Unit 1 Dev (84); Unit 4 Dev - Anderson Base (77); Unit 5 Dev (58)
- **Intervals:** median 0.38s (p5 0.03s / p95 7.65s, n=311)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 312/312 records)
    "argumentationNodeHoverEnd"  x141
    "argumentationNodeHoverStart"  x136
    "argumentationNodeAdd"  x25
    "argumentationNodeRemove"  x10
data.argumentationTitle  (string, 312/312 records)
    "Unit 3 - Pollution Upstream"  x93
    "Unit 4 - Flooding"  x77
    "Unit 5"  x58
    "Unit 1 - Argumentation Tutorial"  x43
    "Unit 1 - Freshwater"  x41
data.nodeName  (string, 312/312 records)
    "1"  x54
    "A"  x38
    "B"  x38
    "I"  x38
    "3"  x32
    "4"  x26
    "2"  x23
    "D"  x22
    "C"  x20
    "II"  x18
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 205 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (72); Unit 3 Dungeon Dev (32); Unit 4 Dev (28); Unit 2 Prod (Refactor) (23); Unit 3 Dev (13); Unit 5 Dev - Dungeon (12); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (6)
- **Intervals:** median 10.51s (p5 1.50s / p95 429.64s, n=204)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 205/205 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 205/205 records)
    96 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 166 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (97); Unit 3 Dev (67); Unit 3 Dungeon Dev (2)
- **Intervals:** median 3.46s (p5 0.44s / p95 508.96s, n=165)
- **`data` key-set variants:** [actionType, featureUsed] x110; [actionType, featureUsed, location] x56
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 166/166 records)
    "MapCloseEvent"  x55
    "MapOpenEvent"  x55
    "WaypointMoveEvent"  x50
    "WaypointSetEvent"  x6
data.featureUsed  (string, 166/166 records)
    "Map"  x110
    "Waypoint"  x56
data.location  (object, 56/166 records)
data.location.x  (number, 56/166 records)
    numeric range -404.09 .. 438.91 (53 unique)
data.location.y  (number, 56/166 records)
    numeric range -281.5 .. 293.5 (51 unique)
data.location.z  (number, 56/166 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 85 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (13); Unit 3 Dev (13); Unit 4 Dev (10); Unit 4 Dev - Dungeon (9); Unit 5 Dev - Dungeon (9); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 85 of 85 records
- **Intervals:** median 160.45s (p5 0.00s / p95 84817.72s, n=84)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Fields under `data`:**

```text
data.questEventType  (string, 85/85 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x31
data.questID  (string, 85/85 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 85/85 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/85 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 56 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (26); MainMenu (24); Unit 3 Dev (3); Transition (1); Unit 1 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 72.87s (p5 0.98s / p95 87225.01s, n=55)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 56/56 records)
    true  x56
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 50 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 3 Dev (12); Unit 4 Dev (12)
- **Intervals:** median 0.85s (p5 0.21s / p95 103945.60s, n=49)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x42; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/50 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/50 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 42/50 records)
    "RightDrag"  x24
    "LeftDrag"  x18
data.currentSoilType  (string, 42/50 records)
    "CLAY"  x10
    "CLAYSAND"  x10
    "CLAYROCK"  x7
    "SAND"  x7
    "SANDGRAVEL"  x4
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 42/50 records)
    "false"  x33
    "true"  x9
data.waterLevelStatus  (string, 42/50 records)
    "TooHigh"  x18
    "TooLow"  x13
    "Proper"  x11
data.waterRetentionChange  (string, 42/50 records)
    "Increase"  x22
    "Decrease"  x11
    "NoChange"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowUnfocusEvent` — 41 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (31); Unit 3 Dev (3); Transition (2); MainMenu (1); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 23.02s (p5 0.89s / p95 96938.50s, n=40)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 41/41 records)
    false  x41
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 3 Dev (4); Unit 4 Dev (4); Unit 5 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 675.45s (p5 76.13s / p95 199009.66s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 23 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (23)
- **Intervals:** median 13.64s (p5 1.31s / p95 76.99s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "On"  x17
    "Off"  x6
data.floor  (string, 23/23 records)
    "3"  x10
    "4"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 23/23 records)
    "One"  x20
    "Two"  x3
data.machineType  (string, 23/23 records)
    "Condenser"  x13
    "Evaporator"  x5
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 23/23 records)
    "2"  x11
    "1"  x4
    "3"  x4
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 1741.42s (p5 73.35s / p95 250151.38s, n=22)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (8); Unit 5 Dev (7); Unit 1 Dev (5)
- **Intervals:** median 1.34s (p5 0.11s / p95 526859.82s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolOpen"  x15
    "argumentationToolClose"  x5
data.argumentationTitle  (string, 20/20 records)
    "Unit 3 - Pollution Upstream"  x8
    "Unit 5"  x7
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x7
    "BackingInfoPanel - Pollution Site Data"  x5
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Watershed Image"  x3
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (8); Unit 4 Dev - Anderson Base (6); Unit 1 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 15.30s (p5 2.45s / p95 528355.92s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 18/18 records)
    "Unit 3 - Pollution Upstream"  x8
    "Unit 4 - Flooding"  x6
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DaniEvent` — 16 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (6); Unit 1 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 4.87s (p5 1.11s / p95 335922.73s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "Close"  x8
    "Open"  x8
data.toolName  (string, 16/16 records, 16 empty-string)
    ""  x16
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `soilMachine` — 16 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (16)
- **Intervals:** median 4.97s (p5 2.39s / p95 160.10s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "ChangeCanister"  x16
data.canisterType  (string, 16/16 records)
    "Clay"  x7
    "Sand"  x4
    "Gravel"  x3
    "Bedrock"  x2
data.floor  (string, 16/16 records)
    "5"  x6
    "4"  x5
    "3"  x3
    "2"  x2
data.machine  (string, 16/16 records)
    "1"  x15
    "2"  x1
data.row  (string, 16/16 records)
    "TopRow"  x13
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 15 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (15)
- **Intervals:** median 2.71s (p5 0.80s / p95 19.31s, n=14)
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records, 6 empty-string)
    "cameraPlaced"  x9
    ""  x6
data.boxId  (string, 15/15 records)
    "0"  x9
    "1"  x3
    "2"  x3
data.soilType  (string, 15/15 records)
    "Sand"  x6
    "Clay"  x5
    "None"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 56.62s (p5 0.04s / p95 556731.24s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x7
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 12/12 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 78885.05s (p5 15475.05s / p95 939665.27s, n=3)
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

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 0.59s (p5 0.54s / p95 1.09s, n=3)
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
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted Out"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Cold"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 5 Dev (1)
- **Intervals:** median 785.99s (p5 212.02s / p95 5969.46s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Permissions check failed"  x2
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 1 empty-string)
    "TypeError: Permissions check failed"  x2
    ""  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x2
    "unit3"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open
- `PuzzlePieceVisibleEvent` actionType: piece visibility: close without preceding open
- `argumentationEvent` actionType: argumentation session: close without preceding open
- `argumentationNodeEvent` actionType: node hover: close without preceding open
- `chatEvent` actionType: chat open/close: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (26 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (50x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (56x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (10x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*