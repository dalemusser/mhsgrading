# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22b
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f22b.jsonl
- **Records:** 15301 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f22b
- **Time span:** 2026-09-23T13:56:25.899000+00:00 .. 2026-10-07T13:28:11.687000+00:00 (335h 31m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 15301 records, 11 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 111 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5599 | 36.59 | 1 | 9 | 0 | 2026-09-23T13:56:42.856000+00:00 | 2026-10-07T13:28:11.558000+00:00 | 335h 31m |
| PuzzlePieceVisibleEvent | 3946 | 25.79 | 1 | 4 | 0 | 2026-09-25T14:11:21.678000+00:00 | 2026-10-06T14:54:05.376000+00:00 | 264h 42m |
| PlayerPositionEvent | 2378 | 15.54 | 1 | 9 | 0 | 2026-09-23T13:56:37.533000+00:00 | 2026-10-07T13:28:11.687000+00:00 | 335h 31m |
| DialogueEvent | 2015 | 13.17 | 1 | 9 | 1200 | 2026-09-23T13:56:59.711000+00:00 | 2026-10-07T13:28:02.788000+00:00 | 335h 31m |
| ObjectInterEvent | 446 | 2.91 | 1 | 9 | 0 | 2026-09-24T13:43:28.268000+00:00 | 2026-10-07T13:28:11.558000+00:00 | 311h 44m |
| argumentationNodeEvent | 424 | 2.77 | 1 | 4 | 0 | 2026-09-24T14:14:06.005000+00:00 | 2026-10-07T13:14:49.047000+00:00 | 311h 0m |
| questEvent | 87 | 0.57 | 1 | 9 | 87 | 2026-09-23T13:56:59.679000+00:00 | 2026-10-07T13:22:10.058000+00:00 | 335h 25m |
| TopographicMapEvent | 69 | 0.45 | 1 | 4 | 0 | 2026-09-23T14:07:34.055000+00:00 | 2026-10-01T14:04:20.660000+00:00 | 191h 56m |
| Soil Key Puzzle | 52 | 0.34 | 1 | 3 | 0 | 2026-09-25T14:19:10.197000+00:00 | 2026-10-01T14:20:03.862000+00:00 | 144h 0m |
| WaterChamberEvent | 43 | 0.28 | 1 | 1 | 0 | 2026-10-06T14:53:15.546000+00:00 | 2026-10-06T15:02:45.945000+00:00 | 9m 30s |
| argumentationAnswerEvent | 38 | 0.25 | 1 | 4 | 0 | 2026-09-25T13:59:15.543000+00:00 | 2026-10-07T13:14:50.229000+00:00 | 287h 15m |
| gameWindowFocusEvent | 36 | 0.24 | 1 | 7 | 0 | 2026-09-23T13:56:25.899000+00:00 | 2026-10-07T13:05:41.052000+00:00 | 335h 9m |
| DaniEvent | 30 | 0.2 | 1 | 3 | 0 | 2026-09-23T14:06:01.005000+00:00 | 2026-10-01T13:53:14.349000+00:00 | 191h 47m |
| DEBUGMenu | 29 | 0.19 | 1 | 9 | 0 | 2026-09-23T13:56:37.524000+00:00 | 2026-10-07T13:05:40.565000+00:00 | 335h 9m |
| gameStartEvent | 22 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:56:25.899000+00:00 | 2026-10-07T13:05:41.052000+00:00 | 335h 9m |
| soilMachine | 22 | 0.14 | 1 | 1 | 0 | 2026-10-05T14:01:54.254000+00:00 | 2026-10-05T14:12:21.553000+00:00 | 10m 27s |
| gameWindowUnfocusEvent | 19 | 0.12 | 1 | 6 | 0 | 2026-09-23T14:07:34.550000+00:00 | 2026-10-06T14:55:47.980000+00:00 | 312h 48m |
| argumentationEvent | 14 | 0.09 | 1 | 4 | 0 | 2026-09-25T13:58:59.428000+00:00 | 2026-10-07T13:14:50.261000+00:00 | 287h 15m |
| SolarStillDesignEvent | 11 | 0.07 | 1 | 1 | 0 | 2026-10-07T13:18:10.456000+00:00 | 2026-10-07T13:18:34.897000+00:00 | 24.4s |
| TerasGardenBox | 8 | 0.05 | 1 | 1 | 0 | 2026-10-06T14:23:48.141000+00:00 | 2026-10-06T14:30:53.053000+00:00 | 7m 4s |
| crash | 6 | 0.04 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-06T14:42:34.596000+00:00 | 2026-10-07T13:05:49.134000+00:00 | 22h 23m |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-25T14:04:32.509000+00:00 | 2026-10-07T13:28:11.530000+00:00 | 287h 23m |
| argumentationToolEvent | 1 | 0.01 | 1 | 1 | 0 | 2026-10-06T15:14:07.948000+00:00 | 2026-10-06T15:14:07.948000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 1034619.021s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 13.605s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 15.759s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 6.601s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 10.957s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 671.559s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1001.368s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.95s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 30 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; p; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E To Return To Base; Press E to Plant Seed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Sand 
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
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.6x vs baseline. 
  - Observed: 38 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,4,I; A,C,2,II; A,C,B,2,II; B,1,I; B,2,II; B,3,II; B,4,I; B,4,II; C,2,II; C,3,II; C,D,2,II; C,D,3,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 424 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 1 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 22 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 54; 55; 56 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Leader of Evidence; Part of a Balanced Ecosystem 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.4x vs baseline. 
  - Observed: 22 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 33 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[968] _id=6ab52aef485cab4c95519b95 ts=2026-09-24T13:51:43.1000000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1015] _id=6ab52c15485cab4c9551b1e5 ts=2026-09-24T13:56:37.1430000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1075] _id=6ab52cd2485cab4c9551bcc9 ts=2026-09-24T13:59:45.9270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[27] _id=6ab3da89485cab4c954ce41d ts=2026-09-23T13:56:25.8990000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[780] _id=6ab5288f485cab4c95514f7a ts=2026-09-24T13:41:35.1380000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1427] _id=6ab67d8d485cab4c9555a706 ts=2026-09-25T13:56:29.1060000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 36 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 36} 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[26] _id=6ab3da89485cab4c954ce41b ts=2026-09-23T13:56:25.8990000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[360] _id=6ab3dd29485cab4c954cf9f7 ts=2026-09-23T14:07:37.4580000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[758] _id=6ab3e2b2485cab4c954d34a8 ts=2026-09-23T14:31:14.8970000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[359] _id=6ab3dd27485cab4c954cf9e3 ts=2026-09-23T14:07:34.5500000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[767] _id=6ab3e2af485cab4c954d34a2 ts=2026-09-23T14:31:11.4830000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[760] _id=6ab3e2b6485cab4c954d34b8 ts=2026-09-23T14:31:18.8730000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5598 | 0.0 | 0.502 | 215.771 | 12.034 | 340937.387 | 0.28 | 413 | 15 |
| PuzzlePieceVisibleEvent | 3945 | 0.0 | 0.026 | 241.562 | 1.138 | 345040.171 | 0.25 | 2479 | 8 |
| PlayerPositionEvent | 2367 | 1.518 | 10.0 | 509.731 | 10.106 | 340789.835 | 0.12 | 0 | 12 |
| DialogueEvent | 2014 | 0.0 | 4.228 | 599.733 | 43.15 | 340972.349 | 0.1 | 634 | 15 |
| ObjectInterEvent | 445 | 0.001 | 4.131 | 2521.985 | 291.006 | 344312.217 | 0.02 | 5 | 15 |
| argumentationNodeEvent | 423 | 0.008 | 0.48 | 2646.91 | 11.349 | 514989.268 | 0.02 | 89 | 5 |
| questEvent | 86 | 0.0 | 232.32 | 14040.818 | 85022.205 | 341331.446 | 0.0 | 15 | 19 |
| TopographicMapEvent | 68 | 0.021 | 15.759 | 10161.862 | 85660.613 | 257999.873 | 0.01 | 3 | 8 |
| Soil Key Puzzle | 51 | 0.183 | 1.026 | 10165.758 | 41717.052 | 344309.234 | 0.01 | 0 | 3 |
| WaterChamberEvent | 42 | 0.288 | 6.601 | 13.581 | 41.899 | 77.973 | 4.42 | 0 | 0 |
| argumentationAnswerEvent | 37 | 0.138 | 10.957 | 27949.586 | 150516.019 | 514994.199 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 35 | 0.148 | 671.559 | 34473.004 | 138172.616 | 341846.382 | 0.0 | 0 | 19 |
| DaniEvent | 29 | 0.004 | 2.06 | 23808.046 | 137669.25 | 344675.423 | 0.0 | 2 | 6 |
| DEBUGMenu | 28 | 2.182 | 1077.344 | 43090.823 | 198421.197 | 341848.626 | 0.0 | 0 | 21 |
| gameStartEvent | 21 | 150.246 | 2779.133 | 57455.007 | 258253.905 | 341846.383 | 0.0 | 0 | 15 |
| soilMachine | 21 | 0.196 | 1.95 | 29.871 | 167.315 | 235.275 | 2.01 | 0 | 0 |
| gameWindowUnfocusEvent | 18 | 0.105 | 1001.368 | 62560.746 | 283413.715 | 432337.93 | 0.0 | 0 | 10 |
| argumentationEvent | 13 | 0.023 | 93.233 | 79550.064 | 467410.457 | 514951.067 | 0.0 | 2 | 4 |
| SolarStillDesignEvent | 10 | 0.73 | 1.211 | 2.444 | 7.423 | 7.571 | 24.55 | 0 | 0 |
| TerasGardenBox | 7 | 2.193 | 13.605 | 60.702 | 213.585 | 266.881 | 0.99 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 3 | 450.331 | 811.044 | 26864.846 | 71480.951 | 79333.163 | 0.0 | 0 | 2 |
| EndOfUnit | 1 | 1034619.021 | 1034619.021 | 1034619.021 | 1034619.021 | 1034619.021 | 0.0 | 0 | 1 |
| argumentationToolEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 9 group(s), 19 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[4519] _id=6abbc365485cab4c957e0ec3 ts=2026-09-29T13:55:48.4810000Z == 6aa4140b41b41dbac0c7f22b.jsonl[4520] _id=6abbc365485cab4c957e0ec7 ts=2026-09-29T13:55:48.4810000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[12280] _id=6ac3b088de269131f9aaee83 ts=2026-10-05T14:13:28.2100000Z == 6aa4140b41b41dbac0c7f22b.jsonl[12281] _id=6ac3b088de269131f9aaee87 ts=2026-10-05T14:13:28.2100000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[12258] _id=6ac3b088de269131f9aaee92 ts=2026-10-05T14:13:28.2120000Z == 6aa4140b41b41dbac0c7f22b.jsonl[12279] _id=6ac3b089de269131f9aaee95 ts=2026-10-05T14:13:28.2120000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 231 group(s), 363 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[1922] _id=6ab6810d485cab4c9555d876 ts=2026-09-25T14:11:24.7270000Z == 6aa4140b41b41dbac0c7f22b.jsonl[1923] _id=6ab6810d485cab4c9555d87a ts=2026-09-25T14:11:24.7270000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1924] _id=6ab6810e485cab4c9555d87e ts=2026-09-25T14:11:24.7270000Z == 6aa4140b41b41dbac0c7f22b.jsonl[1931] _id=6ab6810e485cab4c9555d880 ts=2026-09-25T14:11:24.7270000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1935] _id=6ab68110485cab4c9555d898 ts=2026-09-25T14:11:25.6390000Z == 6aa4140b41b41dbac0c7f22b.jsonl[1927] _id=6ab68110485cab4c9555d89c ts=2026-09-25T14:11:25.6390000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[10875] _id=6abe74ba485cab4c95a97f8c ts=? == 6aa4140b41b41dbac0c7f22b.jsonl[11619] _id=6ac3ac12de269131f9aa1e7c ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[14998] _id=6ac64618de269131f9b8becf ts=2026-10-07T13:16:08.5350000Z == 6aa4140b41b41dbac0c7f22b.jsonl[14999] _id=6ac64618de269131f9b8bed0 ts=2026-10-07T13:16:08.5350000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `338ms: 6aa4140b41b41dbac0c7f22b.jsonl[278] _id=6ab3dccc485cab4c954cf645 ts=2026-09-23T14:06:01.0050000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[224] _id=6ab3dccc485cab4c954cf64b ts=2026-09-23T14:06:01.3430000Z`; `9ms: 6aa4140b41b41dbac0c7f22b.jsonl[269] _id=6ab3dccd485cab4c954cf653 ts=2026-09-23T14:06:03.9890000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[280] _id=6ab3dccd485cab4c954cf655 ts=2026-09-23T14:06:03.9980000Z`; `144ms: 6aa4140b41b41dbac0c7f22b.jsonl[764] _id=6ab3e2ac485cab4c954d3480 ts=2026-09-23T14:31:08.5500000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[753] _id=6ab3e2ac485cab4c954d3484 ts=2026-09-23T14:31:08.6940000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 124 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `635ms: 6aa4140b41b41dbac0c7f22b.jsonl[821] _id=6ab52900485cab4c95515cf3 ts=2026-09-24T13:43:28.2680000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[806] _id=6ab52900485cab4c95515d04 ts=2026-09-24T13:43:28.9030000Z`; `358ms: 6aa4140b41b41dbac0c7f22b.jsonl[806] _id=6ab52900485cab4c95515d04 ts=2026-09-24T13:43:28.9030000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[807] _id=6ab52901485cab4c95515d11 ts=2026-09-24T13:43:29.2610000Z`; `279ms: 6aa4140b41b41dbac0c7f22b.jsonl[807] _id=6ab52901485cab4c95515d11 ts=2026-09-24T13:43:29.2610000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[823] _id=6ab52901485cab4c95515d17 ts=2026-09-24T13:43:29.5400000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 742 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `138ms: 6aa4140b41b41dbac0c7f22b.jsonl[1925] _id=6ab6810e485cab4c9555d886 ts=2026-09-25T14:11:24.7270000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1932] _id=6ab6810f485cab4c9555d888 ts=2026-09-25T14:11:24.8650000Z`; `773ms: 6aa4140b41b41dbac0c7f22b.jsonl[1926] _id=6ab68110485cab4c9555d896 ts=2026-09-25T14:11:24.8660000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1935] _id=6ab68110485cab4c9555d898 ts=2026-09-25T14:11:25.6390000Z`; `55ms: 6aa4140b41b41dbac0c7f22b.jsonl[1927] _id=6ab68110485cab4c9555d89c ts=2026-09-25T14:11:25.6390000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1912] _id=6ab68110485cab4c9555d8a2 ts=2026-09-25T14:11:25.6940000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `569ms: 6aa4140b41b41dbac0c7f22b.jsonl[437] _id=6ab3dee5485cab4c954d0707 ts=2026-09-23T14:14:58.0130000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[66] _id=6ab3dee5485cab4c954d0711 ts=2026-09-23T14:14:58.5820000Z`; `66ms: 6aa4140b41b41dbac0c7f22b.jsonl[1327] _id=6ab53003485cab4c9551e517 ts=2026-09-24T14:13:22.5570000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1328] _id=6ab53004485cab4c9551e51b ts=2026-09-24T14:13:22.6230000Z`; `439ms: 6aa4140b41b41dbac0c7f22b.jsonl[3609] _id=6ab68358485cab4c95562d28 ts=2026-09-25T14:21:12.2940000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[3601] _id=6ab68358485cab4c95562d2e ts=2026-09-25T14:21:12.7330000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `288ms: 6aa4140b41b41dbac0c7f22b.jsonl[1523] _id=6ab67e88485cab4c9555b90c ts=2026-09-25T14:00:41.0390000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1542] _id=6ab67e89485cab4c9555b912 ts=2026-09-25T14:00:41.3270000Z`; `292ms: 6aa4140b41b41dbac0c7f22b.jsonl[1542] _id=6ab67e89485cab4c9555b912 ts=2026-09-25T14:00:41.3270000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1524] _id=6ab67e89485cab4c9555b914 ts=2026-09-25T14:00:41.6190000Z`; `623ms: 6aa4140b41b41dbac0c7f22b.jsonl[14675] _id=6ac5105bde269131f9b454ad ts=2026-10-06T15:14:35.3010000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[14676] _id=6ac5105bde269131f9b454b9 ts=2026-10-06T15:14:35.9240000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `26ms: 6aa4140b41b41dbac0c7f22b.jsonl[8275] _id=6abd2515485cab4c958bafc3 ts=2026-09-30T15:04:53.0270000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[8278] _id=6abd2516485cab4c958baff0 ts=2026-09-30T15:04:53.0530000Z`; `23ms: 6aa4140b41b41dbac0c7f22b.jsonl[13187] _id=6ac5028ade269131f9b287a7 ts=2026-10-06T14:15:37.9550000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[13148] _id=6ac5028ade269131f9b287be ts=2026-10-06T14:15:37.9780000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 53 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `310ms: 6aa4140b41b41dbac0c7f22b.jsonl[1369] _id=6ab5303f485cab4c9551e9f9 ts=2026-09-24T14:14:23.0540000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1373] _id=6ab5303f485cab4c9551ea03 ts=2026-09-24T14:14:23.3640000Z`; `565ms: 6aa4140b41b41dbac0c7f22b.jsonl[1362] _id=6ab5303f485cab4c9551ea00 ts=2026-09-24T14:14:23.1400000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1360] _id=6ab5303f485cab4c9551ea0d ts=2026-09-24T14:14:23.7050000Z`; `828ms: 6aa4140b41b41dbac0c7f22b.jsonl[1372] _id=6ab5303e485cab4c9551e9f1 ts=2026-09-24T14:14:22.8850000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[1374] _id=6ab5303f485cab4c9551ea11 ts=2026-09-24T14:14:23.7130000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `148ms: 6aa4140b41b41dbac0c7f22b.jsonl[13905] _id=6ac50bf3de269131f9b40a09 ts=2026-10-06T14:55:47.7790000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[13909] _id=6ac50bf4de269131f9b40a0d ts=2026-10-06T14:55:47.9270000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `481ms: 6aa4140b41b41dbac0c7f22b.jsonl[4086] _id=6aba7588485cab4c956893bb ts=2026-09-28T14:11:20.0390000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[4087] _id=6aba7589485cab4c95689415 ts=2026-09-28T14:11:20.5200000Z`; `491ms: 6aa4140b41b41dbac0c7f22b.jsonl[12770] _id=6ac4fed3de269131f9b23778 ts=2026-10-06T13:59:48.4230000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[12788] _id=6ac4fed4de269131f9b23794 ts=2026-10-06T13:59:48.9140000Z`; `295ms: 6aa4140b41b41dbac0c7f22b.jsonl[13908] _id=6ac50bf3de269131f9b40a07 ts=2026-10-06T14:55:47.5800000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[13906] _id=6ac50bf3de269131f9b40a0b ts=2026-10-06T14:55:47.8750000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4140b41b41dbac0c7f22b.jsonl[15149] _id=6ac646efde269131f9b8c347 ts=2026-10-07T13:19:43.1450000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[15146] _id=6ac646efde269131f9b8c349 ts=2026-10-07T13:19:43.1490000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `400ms: 6aa4140b41b41dbac0c7f22b.jsonl[11912] _id=6ac3ade1de269131f9aa7284 ts=2026-10-05T14:02:09.8070000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[11936] _id=6ac3ade2de269131f9aa729f ts=2026-10-05T14:02:10.2070000Z`; `321ms: 6aa4140b41b41dbac0c7f22b.jsonl[11936] _id=6ac3ade2de269131f9aa729f ts=2026-10-05T14:02:10.2070000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[11920] _id=6ac3ade2de269131f9aa72b5 ts=2026-10-05T14:02:10.5280000Z`; `615ms: 6aa4140b41b41dbac0c7f22b.jsonl[11920] _id=6ac3ade2de269131f9aa72b5 ts=2026-10-05T14:02:10.5280000Z ~ 6aa4140b41b41dbac0c7f22b.jsonl[11931] _id=6ac3ade3de269131f9aa72cc ts=2026-10-05T14:02:11.1430000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 94h 57m 
  - Evidence: 94h 57m: 6aa4140b41b41dbac0c7f22b.jsonl[10869] _id=6abe74b4485cab4c95a97f64 ts=2026-10-01T14:56:52.2330000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11618] _id=6ac3ac0cde269131f9aa1d1c ts=2026-10-05T13:54:20.8590000Z; 71h 44m: 6aa4140b41b41dbac0c7f22b.jsonl[1669] _id=6ab67fc4485cab4c9555c6f6 ts=2026-09-25T14:05:57.0790000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3798] _id=6aba709d485cab4c956824bd ts=2026-09-28T13:50:21.3590000Z; 24h 14m: 6aa4140b41b41dbac0c7f22b.jsonl[787] _id=6ab528a4485cab4c955153c3 ts=2026-09-24T13:41:56.3340000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1429] _id=6ab67d98485cab4c9555a786 ts=2026-09-25T13:56:40.3780000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 44m 
  - Evidence: 95h 44m: 6aa4140b41b41dbac0c7f22b.jsonl[3613] _id=6ab6836c485cab4c95562e6a ts=2026-09-25T14:21:32.2340000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[5603] _id=6abbc5d0485cab4c957e534f ts=2026-09-29T14:06:07.6570000Z; 47h 46m: 6aa4140b41b41dbac0c7f22b.jsonl[5307] _id=6abbc5d0485cab4c957e5353 ts=2026-09-29T14:06:08.7000000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[9133] _id=6abe65c0485cab4c95a72f12 ts=2026-10-01T13:53:04.0500000Z; 23h 55m: 6aa4140b41b41dbac0c7f22b.jsonl[1376] _id=6ab53044485cab4c9551ea75 ts=2026-09-24T14:14:28.5120000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1883] _id=6ab680ca485cab4c9555d584 ts=2026-09-25T14:10:18.6130000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.009s shown 
  - Evidence: 4ms: 6aa4140b41b41dbac0c7f22b.jsonl[281] _id=6ab3dcd3485cab4c954cf68f ts=2026-09-23T14:06:11.0760000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[226] _id=6ab3dcd3485cab4c954cf692 ts=2026-09-23T14:06:11.0800000Z; 9ms: 6aa4140b41b41dbac0c7f22b.jsonl[269] _id=6ab3dccd485cab4c954cf653 ts=2026-09-23T14:06:03.9890000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[280] _id=6ab3dccd485cab4c954cf655 ts=2026-09-23T14:06:03.9980000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 6aa4140b41b41dbac0c7f22b.jsonl[11530] _id=6abe7825485cab4c95a9e2b5 ts=2026-10-01T15:11:33.8240000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11630] _id=6ac3ac13de269131f9aa1ef2 ts=2026-10-05T13:54:26.1730000Z; 71h 23m: 6aa4140b41b41dbac0c7f22b.jsonl[3784] _id=6ab6852d485cab4c955647e4 ts=2026-09-25T14:29:01.1390000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3840] _id=6aba710a485cab4c95682f5d ts=2026-09-28T13:52:10.5140000Z; 23h 48m: 6aa4140b41b41dbac0c7f22b.jsonl[1205] _id=6ab52ee5485cab4c9551d5f9 ts=2026-09-24T14:08:37.1760000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1448] _id=6ab67dc1485cab4c9555ac1a ts=2026-09-25T13:57:22.0470000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 634 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[15157] _id=6ac646ffde269131f9b8c3a7 ts=2026-10-07T13:19:59.8920000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[15158] _id=6ac646ffde269131f9b8c3a8 ts=2026-10-07T13:19:59.8920000Z; 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[15176] _id=6ac64710de269131f9b8c4bb ts=2026-10-07T13:20:16.7040000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[15177] _id=6ac64710de269131f9b8c4bc ts=2026-10-07T13:20:16.7040000Z; 1ms: 6aa4140b41b41dbac0c7f22b.jsonl[13071] _id=6ac50125de269131f9b2601a ts=2026-10-06T14:09:41.6380000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[13070] _id=6ac50125de269131f9b2601c ts=2026-10-06T14:09:41.6390000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 287h 23m 
  - Evidence: 287h 23m: 6aa4140b41b41dbac0c7f22b.jsonl[1547] _id=6ab67f70485cab4c9555c46a ts=2026-09-25T14:04:32.5090000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[15300] _id=6ac648ebde269131f9b91956 ts=2026-10-07T13:28:11.5300000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 6aa4140b41b41dbac0c7f22b.jsonl[11579] _id=6abe7848485cab4c95a9e740 ts=2026-10-01T15:12:08.6310000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11625] _id=6ac3ac12de269131f9aa1e91 ts=2026-10-05T13:54:26.0180000Z; 71h 21m: 6aa4140b41b41dbac0c7f22b.jsonl[3794] _id=6ab68545485cab4c95564958 ts=2026-09-25T14:29:25.8130000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3802] _id=6aba70b4485cab4c956826bd ts=2026-09-28T13:50:44.4340000Z; 23h 41m: 6aa4140b41b41dbac0c7f22b.jsonl[1413] _id=6ab53074485cab4c9551edcd ts=2026-09-24T14:15:16.3530000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1432] _id=6ab67d9f485cab4c9555a80a ts=2026-09-25T13:56:46.6420000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 413 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[12258] _id=6ac3b088de269131f9aaee92 ts=2026-10-05T14:13:28.2120000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12279] _id=6ac3b089de269131f9aaee95 ts=2026-10-05T14:13:28.2120000Z; 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[12280] _id=6ac3b088de269131f9aaee83 ts=2026-10-05T14:13:28.2100000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12281] _id=6ac3b088de269131f9aaee87 ts=2026-10-05T14:13:28.2100000Z; 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[14396] _id=6ac50dcfde269131f9b42509 ts=2026-10-06T15:03:41.8360000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14405] _id=6ac50dcfde269131f9b4250d ts=2026-10-06T15:03:41.8360000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa4140b41b41dbac0c7f22b.jsonl[3556] _id=6ab682de485cab4c95562400 ts=2026-09-25T14:19:10.2030000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4620] _id=6abbc3d6485cab4c957e1a41 ts=2026-09-29T13:57:42.4200000Z; 94h 43m: 6aa4140b41b41dbac0c7f22b.jsonl[11560] _id=6abe783d485cab4c95a9e5d4 ts=2026-10-01T15:11:57.6340000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11648] _id=6ac3ac56de269131f9aa2e88 ts=2026-10-05T13:55:33.9920000Z; 24h 5m: 6aa4140b41b41dbac0c7f22b.jsonl[5560] _id=6abbc5e2485cab4c957e5535 ts=2026-09-29T14:06:26.7350000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[6426] _id=6abd1893485cab4c958a89b0 ts=2026-09-30T14:11:31.3830000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f22b.jsonl[12693] _id=6ac4fdcede269131f9b1ee76 ts=2026-10-06T13:55:28.2380000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12696] _id=6ac4fdcede269131f9b1ee81 ts=2026-10-06T13:55:28.2390000Z; 1ms: 6aa4140b41b41dbac0c7f22b.jsonl[12750] _id=6ac4fe21de269131f9b20738 ts=2026-10-06T13:56:51.2080000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12727] _id=6ac4fe21de269131f9b2073e ts=2026-10-06T13:56:51.2090000Z; 1ms: 6aa4140b41b41dbac0c7f22b.jsonl[12913] _id=6ac4ff83de269131f9b2440a ts=2026-10-06T14:02:43.8440000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12909] _id=6ac4ff84de269131f9b2440c ts=2026-10-06T14:02:43.8450000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 94h 39m 
  - Evidence: 94h 39m: 6aa4140b41b41dbac0c7f22b.jsonl[11594] _id=6abe78d7485cab4c95a9f76a ts=2026-10-01T15:14:31.0330000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11620] _id=6ac3ac12de269131f9aa1e86 ts=2026-10-05T13:54:20.8680000Z; 71h 21m: 6aa4140b41b41dbac0c7f22b.jsonl[3788] _id=6ab6853e485cab4c955648fc ts=2026-09-25T14:29:18.9560000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3795] _id=6aba70a3485cab4c95682535 ts=2026-09-28T13:50:21.3640000Z; 23h 41m: 6aa4140b41b41dbac0c7f22b.jsonl[1421] _id=6ab53081485cab4c9551ee1d ts=2026-09-24T14:15:29.1250000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1422] _id=6ab67d9e485cab4c9555a806 ts=2026-09-25T13:56:40.3850000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 6aa4140b41b41dbac0c7f22b.jsonl[10664] _id=6abe6cbe485cab4c95a84395 ts=2026-10-01T14:22:50.0440000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12288] _id=6ac3b08bde269131f9aaef0b ts=2026-10-05T14:13:30.2150000Z; 72h 3m: 6aa4140b41b41dbac0c7f22b.jsonl[3222] _id=6ab6829d485cab4c95561dac ts=2026-09-25T14:18:02.9430000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4288] _id=6aba77e8485cab4c9568ca7f ts=2026-09-28T14:21:27.1690000Z; 24h 56m: 6aa4140b41b41dbac0c7f22b.jsonl[5946] _id=6abbc780485cab4c957e6d41 ts=2026-09-29T14:13:17.0810000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8490] _id=6abd263c485cab4c958bc65f ts=2026-09-30T15:09:47.4240000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2479 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[10002] _id=6abe6c28485cab4c95a80e3b ts=2026-10-01T14:20:21.5380000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[10003] _id=6abe6c28485cab4c95a80e3f ts=2026-10-01T14:20:21.5380000Z; 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[10010] _id=6abe6c28485cab4c95a80e49 ts=2026-10-01T14:20:21.6030000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[9887] _id=6abe6c28485cab4c95a80e54 ts=2026-10-01T14:20:21.6030000Z; 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[10011] _id=6abe6c29485cab4c95a80e63 ts=2026-10-01T14:20:21.6230000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[10012] _id=6abe6c29485cab4c95a80e69 ts=2026-10-01T14:20:21.6230000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa4140b41b41dbac0c7f22b.jsonl[3560] _id=6ab682e1485cab4c95562422 ts=2026-09-25T14:19:13.1820000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4621] _id=6abbc3d6485cab4c957e1a3f ts=2026-09-29T13:57:42.4160000Z; 25h 10m: 6aa4140b41b41dbac0c7f22b.jsonl[4634] _id=6abbc3ff485cab4c957e1ee9 ts=2026-09-29T13:58:23.2480000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8451] _id=6abd25f1485cab4c958bbf79 ts=2026-09-30T15:08:33.8570000Z; 23h 10m: 6aa4140b41b41dbac0c7f22b.jsonl[8466] _id=6abd2613485cab4c958bc195 ts=2026-09-30T15:09:07.3900000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[9849] _id=6abe6bec485cab4c95a800b7 ts=2026-10-01T14:19:23.9980000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 71h 39m 
  - Evidence: 71h 39m: 6aa4140b41b41dbac0c7f22b.jsonl[3783] _id=6ab6852d485cab4c955647e2 ts=2026-09-25T14:29:01.1360000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4021] _id=6aba74fd485cab4c9568833b ts=2026-09-28T14:09:01.0090000Z; 24h 3m: 6aa4140b41b41dbac0c7f22b.jsonl[4427] _id=6aba791b485cab4c9568dc39 ts=2026-09-28T14:26:35.4450000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[6206] _id=6abbcb5c485cab4c957ed812 ts=2026-09-29T14:29:48.2590000Z; 23h 57m: 6aa4140b41b41dbac0c7f22b.jsonl[1407] _id=6ab53061485cab4c9551ecd5 ts=2026-09-24T14:14:57.1370000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1953] _id=6ab68135485cab4c9555db19 ts=2026-09-25T14:12:05.3980000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.021s..0.036s shown 
  - Evidence: 21ms: 6aa4140b41b41dbac0c7f22b.jsonl[4336] _id=6aba788f485cab4c9568d379 ts=2026-09-28T14:24:15.4820000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4338] _id=6aba7890485cab4c9568d387 ts=2026-09-28T14:24:15.5030000Z; 34ms: 6aa4140b41b41dbac0c7f22b.jsonl[4330] _id=6aba788f485cab4c9568d375 ts=2026-09-28T14:24:15.4480000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4336] _id=6aba788f485cab4c9568d379 ts=2026-09-28T14:24:15.4820000Z; 36ms: 6aa4140b41b41dbac0c7f22b.jsonl[4333] _id=6aba788f485cab4c9568d36f ts=2026-09-28T14:24:15.4120000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[4330] _id=6aba788f485cab4c9568d375 ts=2026-09-28T14:24:15.4480000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 3m 
  - Evidence: 143h 3m: 6aa4140b41b41dbac0c7f22b.jsonl[8274] _id=6abd2515485cab4c958bafb5 ts=2026-09-30T15:04:53.0110000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12856] _id=6ac500c7de269131f9b25a2e ts=2026-10-06T14:08:07.2100000Z; 121h 2m: 6aa4140b41b41dbac0c7f22b.jsonl[1577] _id=6ab67eb2485cab4c9555bcb8 ts=2026-09-25T14:01:23.0420000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8208] _id=6abd24ee485cab4c958ba9b5 ts=2026-09-30T15:04:14.1600000Z; 22h 0m: 6aa4140b41b41dbac0c7f22b.jsonl[14685] _id=6ac51068de269131f9b45509 ts=2026-10-06T15:14:47.9850000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14977] _id=6ac645cade269131f9b8bd41 ts=2026-10-07T13:14:50.2290000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 2m 
  - Evidence: 143h 2m: 6aa4140b41b41dbac0c7f22b.jsonl[8278] _id=6abd2516485cab4c958baff0 ts=2026-09-30T15:04:53.0530000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12810] _id=6ac5009cde269131f9b2576a ts=2026-10-06T14:07:24.1200000Z; 121h 1m: 6aa4140b41b41dbac0c7f22b.jsonl[1578] _id=6ab67eb3485cab4c9555bcba ts=2026-09-25T14:01:23.0770000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8196] _id=6abd24b7485cab4c958ba717 ts=2026-09-30T15:03:19.7940000Z; 21h 59m: 6aa4140b41b41dbac0c7f22b.jsonl[14660] _id=6ac51068de269131f9b45511 ts=2026-10-06T15:14:48.0150000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14930] _id=6ac64596de269131f9b8bac4 ts=2026-10-07T13:13:58.0340000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.026s shown 
  - Evidence: 23ms: 6aa4140b41b41dbac0c7f22b.jsonl[13187] _id=6ac5028ade269131f9b287a7 ts=2026-10-06T14:15:37.9550000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[13148] _id=6ac5028ade269131f9b287be ts=2026-10-06T14:15:37.9780000Z; 26ms: 6aa4140b41b41dbac0c7f22b.jsonl[8275] _id=6abd2515485cab4c958bafc3 ts=2026-09-30T15:04:53.0270000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8278] _id=6abd2516485cab4c958baff0 ts=2026-09-30T15:04:53.0530000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 3m 
  - Evidence: 143h 3m: 6aa4140b41b41dbac0c7f22b.jsonl[8271] _id=6abd2511485cab4c958baef8 ts=2026-09-30T15:04:48.9380000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12843] _id=6ac500bede269131f9b25976 ts=2026-10-06T14:07:58.2060000Z; 121h 2m: 6aa4140b41b41dbac0c7f22b.jsonl[1576] _id=6ab67eaf485cab4c9555bc5c ts=2026-09-25T14:01:19.9000000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8193] _id=6abd24bc485cab4c958ba76f ts=2026-09-30T15:03:24.3580000Z; 23h 43m: 6aa4140b41b41dbac0c7f22b.jsonl[1361] _id=6ab5303f485cab4c9551ea15 ts=2026-09-24T14:14:23.7480000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1462] _id=6ab67ded485cab4c9555b0f9 ts=2026-09-25T13:58:05.3300000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 89 interval(s) ≤ 0.008s..0.019s shown 
  - Evidence: 8ms: 6aa4140b41b41dbac0c7f22b.jsonl[1360] _id=6ab5303f485cab4c9551ea0d ts=2026-09-24T14:14:23.7050000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1374] _id=6ab5303f485cab4c9551ea11 ts=2026-09-24T14:14:23.7130000Z; 19ms: 6aa4140b41b41dbac0c7f22b.jsonl[8240] _id=6abd2501485cab4c958babd1 ts=2026-09-30T15:04:33.1150000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8245] _id=6abd2501485cab4c958babdd ts=2026-09-30T15:04:33.1340000Z; 19ms: 6aa4140b41b41dbac0c7f22b.jsonl[8265] _id=6abd250f485cab4c958bae8f ts=2026-09-30T15:04:47.5840000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[8268] _id=6abd250f485cab4c958bae9d ts=2026-09-30T15:04:47.6030000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 22h 2m 
  - Evidence: 22h 2m: 6aa4140b41b41dbac0c7f22b.jsonl[14395] _id=6ac50dc8de269131f9b42458 ts=2026-10-06T15:03:35.9710000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14738] _id=6ac643adde269131f9b8b6a0 ts=2026-10-07T13:05:49.1340000Z; 13m 31s: 6aa4140b41b41dbac0c7f22b.jsonl[13539] _id=6ac508dade269131f9b3af3d ts=2026-10-06T14:42:34.5960000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14079] _id=6ac50c05de269131f9b40af5 ts=2026-10-06T14:56:05.6400000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 94h 57m 
  - Evidence: 94h 57m: 6aa4140b41b41dbac0c7f22b.jsonl[10868] _id=6abe749e485cab4c95a97ed0 ts=2026-10-01T14:56:29.9770000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11600] _id=6ac3abf4de269131f9aa171e ts=2026-10-05T13:53:56.3600000Z; 71h 44m: 6aa4140b41b41dbac0c7f22b.jsonl[1668] _id=6ab67fbe485cab4c9555c6da ts=2026-09-25T14:05:50.8910000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3797] _id=6aba708d485cab4c956822a1 ts=2026-09-28T13:50:04.7960000Z; 24h 14m: 6aa4140b41b41dbac0c7f22b.jsonl[780] _id=6ab5288f485cab4c95514f7a ts=2026-09-24T13:41:35.1380000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1427] _id=6ab67d8d485cab4c9555a706 ts=2026-09-25T13:56:29.1060000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 94h 57m 
  - Evidence: 94h 57m: 6aa4140b41b41dbac0c7f22b.jsonl[10867] _id=6abe749d485cab4c95a97ece ts=2026-10-01T14:56:29.9770000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11599] _id=6ac3abf4de269131f9aa1714 ts=2026-10-05T13:53:56.3590000Z; 71h 21m: 6aa4140b41b41dbac0c7f22b.jsonl[3779] _id=6ab68513485cab4c9556465e ts=2026-09-25T14:28:35.3320000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3796] _id=6aba708c485cab4c9568229b ts=2026-09-28T13:50:04.7950000Z; 24h 14m: 6aa4140b41b41dbac0c7f22b.jsonl[779] _id=6ab5288f485cab4c95514f76 ts=2026-09-24T13:41:35.1370000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1426] _id=6ab67d8c485cab4c9555a704 ts=2026-09-25T13:56:29.1050000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 120h 5m 
  - Evidence: 120h 5m: 6aa4140b41b41dbac0c7f22b.jsonl[9168] _id=6abe6602485cab4c95a73cbb ts=2026-10-01T13:54:10.4930000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[12770] _id=6ac4fed3de269131f9b23778 ts=2026-10-06T13:59:48.4230000Z; 71h 25m: 6aa4140b41b41dbac0c7f22b.jsonl[3776] _id=6ab6850f485cab4c95564620 ts=2026-09-25T14:28:31.4780000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3870] _id=6aba717c485cab4c95683f19 ts=2026-09-28T13:54:04.4490000Z; 47h 42m: 6aa4140b41b41dbac0c7f22b.jsonl[4087] _id=6aba7589485cab4c95689415 ts=2026-09-28T14:11:20.5200000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[6265] _id=6abd1464485cab4c95895b0b ts=2026-09-30T13:53:39.7120000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 6aa4140b41b41dbac0c7f22b.jsonl[11262] _id=6abe76be485cab4c95a9a2a3 ts=2026-10-01T15:05:34.6110000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[11622] _id=6ac3ac13de269131f9aa1eee ts=2026-10-05T13:54:26.0570000Z; 71h 22m: 6aa4140b41b41dbac0c7f22b.jsonl[3716] _id=6ab684f2485cab4c9556443c ts=2026-09-25T14:28:02.6440000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[3799] _id=6aba70a3485cab4c9568253f ts=2026-09-28T13:50:27.0810000Z; 23h 48m: 6aa4140b41b41dbac0c7f22b.jsonl[1194] _id=6ab52ee0485cab4c9551d5bf ts=2026-09-24T14:08:32.4560000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[1435] _id=6ab67da0485cab4c9555a840 ts=2026-09-25T13:56:46.7470000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22b.jsonl[14998] _id=6ac64618de269131f9b8becf ts=2026-10-07T13:16:08.5350000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14999] _id=6ac64618de269131f9b8bed0 ts=2026-10-07T13:16:08.5350000Z; 1ms: 6aa4140b41b41dbac0c7f22b.jsonl[14053] _id=6ac50be2de269131f9b4095d ts=2026-10-06T14:55:29.8330000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14066] _id=6ac50be2de269131f9b4095f ts=2026-10-06T14:55:29.8340000Z; 1ms: 6aa4140b41b41dbac0c7f22b.jsonl[14124] _id=6ac50c56de269131f9b40f3d ts=2026-10-06T14:57:26.6560000Z -> 6aa4140b41b41dbac0c7f22b.jsonl[14130] _id=6ac50c56de269131f9b40f3f ts=2026-10-06T14:57:26.6570000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[764] _id=6ab3e2ac485cab4c954d3480 ts=2026-09-23T14:31:08.5500000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[753] _id=6ab3e2ac485cab4c954d3484 ts=2026-09-23T14:31:08.6940000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1314] _id=6ab53001485cab4c9551e4d9 ts=2026-09-24T14:13:20.9320000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[1175] _id=6ab52eac485cab4c9551d469 ts=2026-09-24T14:07:40.5530000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1592] _id=6ab67eca485cab4c9555bda2 ts=2026-09-25T14:01:46.5720000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[4329] _id=6aba788d485cab4c9568d35f ts=2026-09-28T14:24:13.2580000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 161 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[2084] _id=6ab68199485cab4c9555ea80 ts=2026-09-25T14:13:44.6120000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[2090] _id=6ab68199485cab4c9555ea86 ts=2026-09-25T14:13:44.6170000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[2094] _id=6ab68199485cab4c9555ea8a ts=2026-09-25T14:13:44.7520000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 307 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[2032] _id=6ab68190485cab4c9555e954 ts=2026-09-25T14:11:22.0160000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1933] _id=6ab6810f485cab4c9555d88c ts=2026-09-25T14:11:24.8660000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1934] _id=6ab6810f485cab4c9555d894 ts=2026-09-25T14:11:24.8660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[437] _id=6ab3dee5485cab4c954d0707 ts=2026-09-23T14:14:58.0130000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[66] _id=6ab3dee5485cab4c954d0711 ts=2026-09-23T14:14:58.5820000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1327] _id=6ab53003485cab4c9551e517 ts=2026-09-24T14:13:22.5570000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[8278] _id=6abd2516485cab4c958baff0 ts=2026-09-30T15:04:53.0530000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[13148] _id=6ac5028ade269131f9b287be ts=2026-10-06T14:15:37.9780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[1374] _id=6ab5303f485cab4c9551ea11 ts=2026-09-24T14:14:23.7130000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1361] _id=6ab5303f485cab4c9551ea15 ts=2026-09-24T14:14:23.7480000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1484] _id=6ab67e27485cab4c9555b5b4 ts=2026-09-25T13:59:02.9960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[13539] _id=6ac508dade269131f9b3af3d ts=2026-10-06T14:42:34.5960000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[14079] _id=6ac50c05de269131f9b40af5 ts=2026-10-06T14:56:05.6400000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[14395] _id=6ac50dc8de269131f9b42458 ts=2026-10-06T15:03:35.9710000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[14129] _id=6ac50c56de269131f9b40f37 ts=2026-10-06T14:57:26.6350000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[3891] _id=6aba73f4485cab4c9568761f ts=?`; `6aa4140b41b41dbac0c7f22b.jsonl[4515] _id=6abbc364485cab4c957e0ea9 ts=?`; `6aa4140b41b41dbac0c7f22b.jsonl[7845] _id=6abd2258485cab4c958b8ad5 ts=?`
- **WARNING / Low** `DaniEvent` `actionType` — tool open/close: repeated open with no intervening close. 
  - Observed: 12 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[224] _id=6ab3dccc485cab4c954cf64b ts=2026-09-23T14:06:01.3430000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[268] _id=6ab3dccd485cab4c954cf651 ts=2026-09-23T14:06:02.5150000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[269] _id=6ab3dccd485cab4c954cf653 ts=2026-09-23T14:06:03.9890000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 572 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[2186] _id=6ab681bc485cab4c9555f0f8 ts=2026-09-25T14:14:19.1770000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[2193] _id=6ab681bd485cab4c9555f145 ts=2026-09-25T14:14:20.4470000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[2180] _id=6ab681c1485cab4c9555f220 ts=2026-09-25T14:14:25.6650000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 783 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[2056] _id=6ab68190485cab4c9555e944 ts=2026-09-25T14:11:22.0150000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1923] _id=6ab6810d485cab4c9555d87a ts=2026-09-25T14:11:24.7270000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[1931] _id=6ab6810e485cab4c9555d880 ts=2026-09-25T14:11:24.7270000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 12 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[4336] _id=6aba788f485cab4c9568d379 ts=2026-09-28T14:24:15.4820000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[4338] _id=6aba7890485cab4c9568d387 ts=2026-09-28T14:24:15.5030000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[4428] _id=6aba7911485cab4c9568dbdb ts=2026-09-28T14:26:25.7270000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DaniEvent` `actionType` — tool open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'Open' (totals: 16 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 411 start, 404 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 204 unmatched 'BecameCameraCentered' (totals: 815 open, 772 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 166 unmatched 'BecameVisible' (totals: 1109 open, 1250 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 26 open, 32 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 1 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 54 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 358 of 15294 adjacent _id pairs reverse in client time; worst 132.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f22b.jsonl[2026] _id=6ab6818e485cab4c9555e8c4 ts=2026-09-25T14:13:34.6270000Z`; `6aa4140b41b41dbac0c7f22b.jsonl[2027] _id=6ab6818f485cab4c9555e8ee ts=2026-09-25T14:11:21.6780000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -398.13s, max +4.12s over 15295 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 6 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5599 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1557); Unit 2 Prod (Refactor) (1000); Unit 4 Dev - Dungeon (995); Unit 1 Dev (834); Unit 3 Dungeon Dev (441); Unit 4 Dev (291); Unit 5 Dev - Dungeon (216); Unit 5 Dev (168); Unit 4 Dev - Anderson Base (97)
- **Intervals:** median 0.50s (p5 0.03s / p95 12.03s, n=5598)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5599/5599 records)
    "pressed"  x5599
data.actionType  (string, 5599/5599 records)
    "Move"  x4009
    "Interact"  x750
    "Jump"  x535
    "Sprint"  x73
    "Hoverboard"  x69
    "Pause"  x58
    "Map"  x48
    "Ascend"  x40
    "SkipCinematic"  x12
    "ToggleDebug"  x3
    "Descend"  x2
data.key  (string, 5599/5599 records, 14 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5599/5599 records)
    "Player"  x4209
    "Drone"  x1390
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3946 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2358); Unit 4 Dev (797); Unit 3 Dungeon Dev (435); Unit 5 Dev - Dungeon (356)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.14s, n=3945)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3946/3946 records)
    "BecameInvisible"  x1250
    "BecameVisible"  x1109
    "BecameCameraCentered"  x815
    "BecameCameraUncentered"  x772
data.pieceId  (string, 3946/3946 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3946/3946 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2378 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (562); Unit 1 Dev (434); Unit 4 Dev - Dungeon (262); Unit 4 Dev (257); Unit 3 Dev (234); Unit 5 Dev (205); Unit 3 Dungeon Dev (159); Unit 4 Dev - Anderson Base (145); Unit 5 Dev - Dungeon (120)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.11s, n=2367)
- **Fields under `data`:**

```text
data.position  (object, 2378/2378 records)
data.position.x  (number, 2378/2378 records)
    numeric range -689.045 .. 1554.35 (749 unique)
data.position.y  (number, 2378/2378 records)
    numeric range -114.26 .. 222.673 (546 unique)
data.position.z  (number, 2378/2378 records)
    numeric range -1043.98 .. 1996.91 (748 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2015 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (501); Unit 5 Dev (327); Unit 3 Dev (267); Unit 4 Dev (196); Unit 1 Dev (195); Unit 4 Dev - Anderson Base (166); Unit 4 Dev - Dungeon (163); Unit 3 Dungeon Dev (108); Unit 5 Dev - Dungeon (92)
- **eventKey:** present on 1200 of 2015 records
- **Intervals:** median 4.23s (p5 0.00s / p95 43.15s, n=2014)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1200; [conversationId, dialogueEventType] x815
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2015/2015 records)
    numeric range 8 .. 118 (50 unique)
data.dialogueEventType  (string, 2015/2015 records)
    "DialogueNodeEvent"  x1200
    "DialogueStartEvent"  x411
    "DialogueFinishEvent"  x404
data.nodeId  (number, 1200/2015 records)
    numeric range 0 .. 290 (183 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 446 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (148); Unit 2 Prod (Refactor) (116); Unit 3 Dungeon Dev (76); Unit 1 Dev (30); Unit 4 Dev (23); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (16); Unit 5 Dev (12); Unit 3 Dev (7)
- **Intervals:** median 4.13s (p5 0.18s / p95 291.01s, n=445)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 446/446 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 446/446 records)
    90 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 424 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 5 Dev (154); Unit 4 Dev - Anderson Base (137); Unit 1 Dev (82); Unit 3 Dev (51)
- **Intervals:** median 0.48s (p5 0.03s / p95 11.35s, n=423)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 424/424 records)
    "argumentationNodeHoverEnd"  x194
    "argumentationNodeHoverStart"  x185
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x13
data.argumentationTitle  (string, 424/424 records)
    "Unit 5"  x154
    "Unit 4 - Flooding"  x137
    "Unit 1 - Freshwater"  x59
    "Unit 3 - Pollution Upstream"  x51
    "Unit 1 - Argumentation Tutorial"  x23
data.nodeName  (string, 424/424 records)
    "B"  x78
    "A"  x60
    "I"  x55
    "C"  x43
    "1"  x36
    "II"  x35
    "3"  x32
    "D"  x29
    "2"  x25
    "4"  x23
    "5"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 87 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 1 Dev (16); Unit 4 Dev - Dungeon (14); Unit 5 Dev (9); Unit 5 Dev - Dungeon (9); Unit 3 Dev (8); Unit 4 Dev (5); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 87 of 87 records
- **Intervals:** median 232.32s (p5 0.00s / p95 85022.21s, n=86)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 87/87 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x33
data.questID  (string, 87/87 records)
    30 unique values (see csv/event_unique_values.csv)
data.questName  (string, 87/87 records)
    30 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/87 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 69 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 3 Dev (23); Unit 1 Dev (14); Unit 3 Dungeon Dev (2)
- **Intervals:** median 15.76s (p5 0.20s / p95 85660.61s, n=68)
- **`data` key-set variants:** [actionType, featureUsed] x58; [actionType, featureUsed, location] x11
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 69/69 records)
    "MapCloseEvent"  x32
    "MapOpenEvent"  x26
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x3
    "WaypointResetEvent"  x1
data.featureUsed  (string, 69/69 records)
    "Map"  x58
    "Waypoint"  x11
data.location  (object, 11/69 records)
data.location.x  (number, 11/69 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 11/69 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 11/69 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 52 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (20); Unit 3 Dev (18); Unit 2 Prod (Refactor) (14)
- **Intervals:** median 1.03s (p5 0.22s / p95 41717.05s, n=51)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/52 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/52 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 44/52 records)
    "RightDrag"  x25
    "LeftDrag"  x19
data.currentSoilType  (string, 44/52 records)
    "CLAYSAND"  x11
    "CLAY"  x10
    "CLAYROCK"  x8
    "SAND"  x8
    "BEDROCK"  x3
    "SANDGRAVEL"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 44/52 records)
    "false"  x32
    "true"  x12
data.waterLevelStatus  (string, 44/52 records)
    "TooHigh"  x24
    "Proper"  x18
    "TooLow"  x2
data.waterRetentionChange  (string, 44/52 records)
    "Increase"  x18
    "Decrease"  x14
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 43 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (43)
- **Intervals:** median 6.60s (p5 1.07s / p95 41.90s, n=42)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 43/43 records)
    "On"  x26
    "Off"  x17
data.floor  (string, 43/43 records)
    "3"  x18
    "4"  x15
    "2"  x6
    "1"  x4
data.machineNumber  (string, 43/43 records)
    "One"  x42
    "Two"  x1
data.machineType  (string, 43/43 records)
    "Condenser"  x27
    "Evaporator"  x13
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 43/43 records)
    "3"  x19
    "1"  x11
    "2"  x7
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 38 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (13); Unit 5 Dev (12); Unit 1 Dev (7); Unit 3 Dev (6)
- **Intervals:** median 10.96s (p5 0.19s / p95 150516.02s, n=37)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "submitAnswerEvent"  x38
data.answerSubmitted  (string, 38/38 records, 6 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 38/38 records)
    "Unit 4 - Flooding"  x13
    "Unit 5"  x12
    "Unit 1 - Freshwater"  x6
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 36 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 2 Prod (Refactor) (4); Unit 4 Dev - Anderson Base (3); Transition (2); Unit 1 Dev (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 671.56s (p5 2.57s / p95 138172.62s, n=35)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 36/36 records)
    true  x36
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 30 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 1 Dev (22); Unit 2 Prod (Refactor) (6); Unit 3 Dungeon Dev (2)
- **Intervals:** median 2.06s (p5 0.06s / p95 137669.25s, n=29)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "Open"  x16
    "Close"  x14
data.toolName  (string, 30/30 records, 24 empty-string)
    ""  x24
    "Settings"  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `DEBUGMenu` — 29 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 4 Dev - Anderson Base (5); Unit 1 Dev (3); Unit 3 Dev (3); Unit 3 Dungeon Dev (3); Unit 4 Dev (3); Unit 4 Dev - Dungeon (3); Unit 5 Dev - Dungeon (2); MainMenu (1)
- **Intervals:** median 1077.34s (p5 21.56s / p95 198421.20s, n=28)
- **Fields under `data`:**

```text
data.actionType  (string, 29/29 records)
    "DebugMenuStateChanged"  x29
data.isOpened  (bool, 29/29 records)
    false  x29
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 22 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (22)
- **Intervals:** median 2779.13s (p5 392.79s / p95 258253.90s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 22 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (22)
- **Intervals:** median 1.95s (p5 0.23s / p95 167.31s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "ChangeCanister"  x22
data.canisterType  (string, 22/22 records)
    "Gravel"  x10
    "Clay"  x8
    "Bedrock"  x2
    "Sand"  x2
data.floor  (string, 22/22 records)
    "4"  x11
    "5"  x11
data.machine  (string, 22/22 records)
    "1"  x20
    "2"  x2
data.row  (string, 22/22 records)
    "TopRow"  x19
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 5 Dev - Dungeon (3); Transition (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1001.37s (p5 0.27s / p95 283413.71s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 5 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 93.23s (p5 0.02s / p95 467410.46s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 5"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 1.21s (p5 0.79s / p95 7.42s, n=10)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x10; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "optionSelected"  x10
    "DesignSubmitted"  x1
data.designSelections  (object, 1/11 records)
data.designSelections.glassRoofTemperature  (string, 1/11 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/11 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/11 records)
    "Tilted Out"  x1
data.featureUsed  (string, 11/11 records)
    "RoofStyle"  x4
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x3
    "Submit"  x1
data.selectedOption  (string, 10/11 records, 1 empty-string)
    "Cold"  x2
    "Covered"  x2
    "Tilted In"  x2
    ""  x1
    "Hot"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 13.61s (p5 3.01s / p95 213.59s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 1 empty-string)
    "cameraPlaced"  x7
    ""  x1
data.boxId  (string, 8/8 records)
    "0"  x6
    "1"  x1
    "2"  x1
data.soilType  (string, 8/8 records)
    "Gravel"  x4
    "None"  x4
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
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
    "unit4"  x2
    "unit3"  x1
    "unit5"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 811.04s (p5 486.40s / p95 71480.95s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1034619.02s (p5 1034619.02s / p95 1034619.02s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 1 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 1/1 records)
    "Unit 5"  x1
data.toolName  (string, 1/1 records)
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DaniEvent` actionType: tool open/close: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (14 records)
- `TerasGardenBox` data.actionType: "" (1x)
- `TerasGardenBox` data.soilType: "None" (4x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointResetEvent" (1x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (11x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (13x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*