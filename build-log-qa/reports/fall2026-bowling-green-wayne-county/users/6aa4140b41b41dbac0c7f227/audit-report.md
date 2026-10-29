# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f227

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f227
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f227.jsonl
- **Records:** 12061 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f227
- **Time span:** 2026-09-23T14:15:59.985000+00:00 .. 2026-10-07T15:01:06.778000+00:00 (336h 45m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f227\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 12061 records, 10 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 107 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3347 | 27.75 | 1 | 9 | 0 | 2026-09-23T14:16:19.992000+00:00 | 2026-10-07T15:01:06.778000+00:00 | 336h 44m |
| PuzzlePieceVisibleEvent | 3254 | 26.98 | 1 | 4 | 0 | 2026-09-29T14:01:42.964000+00:00 | 2026-10-07T14:21:10.387000+00:00 | 192h 19m |
| PlayerPositionEvent | 2201 | 18.25 | 1 | 9 | 0 | 2026-09-23T14:16:14.126000+00:00 | 2026-10-07T15:01:02.334000+00:00 | 336h 44m |
| DialogueEvent | 2013 | 16.69 | 1 | 9 | 1252 | 2026-09-23T14:16:36.943000+00:00 | 2026-10-07T15:01:00.624000+00:00 | 336h 44m |
| argumentationNodeEvent | 455 | 3.77 | 1 | 4 | 0 | 2026-09-28T14:18:56.809000+00:00 | 2026-10-07T14:49:29.334000+00:00 | 216h 30m |
| ObjectInterEvent | 305 | 2.53 | 1 | 9 | 0 | 2026-09-23T14:23:34.382000+00:00 | 2026-10-07T15:01:06.778000+00:00 | 336h 37m |
| Soil Key Puzzle | 86 | 0.71 | 1 | 3 | 0 | 2026-09-29T14:09:36.821000+00:00 | 2026-10-05T14:37:08.610000+00:00 | 144h 27m |
| questEvent | 85 | 0.7 | 1 | 9 | 85 | 2026-09-23T14:16:36.914000+00:00 | 2026-10-07T14:56:44.757000+00:00 | 336h 40m |
| TopographicMapEvent | 67 | 0.56 | 1 | 4 | 0 | 2026-09-29T14:02:13.815000+00:00 | 2026-10-06T14:05:26.316000+00:00 | 168h 3m |
| WaterChamberEvent | 57 | 0.47 | 1 | 1 | 0 | 2026-10-07T14:18:48.060000+00:00 | 2026-10-07T14:32:55.933000+00:00 | 14m 7s |
| soilMachine | 42 | 0.35 | 1 | 1 | 0 | 2026-10-05T14:59:13.768000+00:00 | 2026-10-06T13:59:46.612000+00:00 | 23h 0m |
| gameWindowFocusEvent | 25 | 0.21 | 1 | 6 | 0 | 2026-09-23T14:15:59.985000+00:00 | 2026-10-07T14:13:02.639000+00:00 | 335h 57m |
| DEBUGMenu | 22 | 0.18 | 1 | 9 | 0 | 2026-09-23T14:16:14.118000+00:00 | 2026-10-07T14:13:16.277000+00:00 | 335h 57m |
| argumentationAnswerEvent | 18 | 0.15 | 1 | 4 | 0 | 2026-09-28T14:21:59.644000+00:00 | 2026-10-07T14:49:41.756000+00:00 | 216h 27m |
| gameStartEvent | 15 | 0.12 | 1 | 1 | 0 | 2026-09-23T14:15:59.987000+00:00 | 2026-10-07T14:13:02.639000+00:00 | 335h 57m |
| TerasGardenBox | 13 | 0.11 | 1 | 1 | 0 | 2026-10-06T14:28:54.242000+00:00 | 2026-10-06T15:06:51.852000+00:00 | 37m 57s |
| argumentationEvent | 12 | 0.1 | 1 | 4 | 0 | 2026-09-28T14:19:28.158000+00:00 | 2026-10-07T14:49:41.829000+00:00 | 216h 30m |
| gameWindowUnfocusEvent | 11 | 0.09 | 1 | 5 | 0 | 2026-09-24T13:58:07.596000+00:00 | 2026-10-06T14:29:21.870000+00:00 | 288h 31m |
| argumentationToolEvent | 9 | 0.07 | 1 | 2 | 0 | 2026-09-28T14:19:27.173000+00:00 | 2026-10-07T14:49:38.770000+00:00 | 216h 30m |
| SolarStillDesignEvent | 8 | 0.07 | 1 | 1 | 0 | 2026-10-07T14:53:39.263000+00:00 | 2026-10-07T14:53:51.626000+00:00 | 12.4s |
| crash | 6 | 0.05 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-05T14:58:53.940000+00:00 | 2026-10-06T15:04:25.647000+00:00 | 24h 5m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-28T14:26:25.280000+00:00 | 2026-10-07T15:01:06.724000+00:00 | 216h 34m |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-06T15:10:53.045000+00:00 | 2026-10-07T14:33:52.362000+00:00 | 23h 22m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 389840.722s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.32s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.404s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 19.571s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.456s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.351s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 24.299s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 185.535s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.86s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 42089.659s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 83449.454s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1837.475s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 43525.889s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.668s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
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
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,3,I; B,A,4,I; C,D,1,II; C,D,3,II; D,2,II; D,3,II; D,4,II; D,C,3,1,II; D,C,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 455 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54; 56 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 8.4x vs baseline. 
  - Observed: 42 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 24 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[427] _id=6ab52d92485cab4c9551c92d ts=2026-09-24T14:02:58.1810000Z`; `6aa4140b41b41dbac0c7f227.jsonl[510] _id=6ab52edd485cab4c9551d59d ts=2026-09-24T14:08:29.0680000Z`; `6aa4140b41b41dbac0c7f227.jsonl[566] _id=6ab52fd1485cab4c9551e305 ts=2026-09-24T14:12:33.7870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[3] _id=6ab3df20485cab4c954d093f ts=2026-09-23T14:15:59.9870000Z`; `6aa4140b41b41dbac0c7f227.jsonl[302] _id=6ab52c2f485cab4c9551b441 ts=2026-09-24T13:57:02.9410000Z`; `6aa4140b41b41dbac0c7f227.jsonl[639] _id=6aba7131485cab4c956833df ts=2026-09-28T13:52:48.9400000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[2] _id=6ab3df1f485cab4c954d093d ts=2026-09-23T14:15:59.9850000Z`; `6aa4140b41b41dbac0c7f227.jsonl[303] _id=6ab52c2f485cab4c9551b436 ts=2026-09-24T13:57:02.9410000Z`; `6aa4140b41b41dbac0c7f227.jsonl[325] _id=6ab52c7b485cab4c9551b95f ts=2026-09-24T13:58:19.2030000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[326] _id=6ab52c6f485cab4c9551b90d ts=2026-09-24T13:58:07.5960000Z`; `6aa4140b41b41dbac0c7f227.jsonl[911] _id=6aba7463485cab4c95687c2f ts=2026-09-28T14:06:27.3730000Z`; `6aa4140b41b41dbac0c7f227.jsonl[928] _id=6aba74ff485cab4c95688363 ts=2026-09-28T14:09:03.5930000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3346 | 0.0 | 1.32 | 362.309 | 21.994 | 344273.034 | 0.17 | 109 | 12 |
| PuzzlePieceVisibleEvent | 3253 | 0.0 | 0.033 | 212.84 | 1.325 | 430707.318 | 0.28 | 1926 | 6 |
| PlayerPositionEvent | 2189 | 0.867 | 9.999 | 553.682 | 10.028 | 344268.628 | 0.11 | 0 | 9 |
| DialogueEvent | 2012 | 0.001 | 5.079 | 602.517 | 41.748 | 344337.524 | 0.1 | 581 | 9 |
| argumentationNodeEvent | 454 | 0.001 | 0.429 | 1716.812 | 5.967 | 431676.292 | 0.03 | 73 | 3 |
| ObjectInterEvent | 304 | 0.001 | 12.404 | 3986.357 | 420.608 | 344399.464 | 0.02 | 5 | 13 |
| Soil Key Puzzle | 85 | 0.174 | 1.148 | 6118.256 | 17.842 | 431193.356 | 0.01 | 0 | 3 |
| questEvent | 84 | 0.0 | 241.25 | 14428.665 | 84462.99 | 344771.515 | 0.0 | 17 | 17 |
| TopographicMapEvent | 66 | 0.022 | 4.456 | 9166.553 | 63069.934 | 345459.956 | 0.01 | 2 | 8 |
| WaterChamberEvent | 56 | 0.188 | 5.351 | 15.141 | 45.773 | 188.209 | 3.96 | 0 | 0 |
| soilMachine | 41 | 1.469 | 7.668 | 2020.313 | 183.843 | 81588.844 | 0.03 | 0 | 1 |
| gameWindowFocusEvent | 24 | 0.108 | 1837.475 | 50392.611 | 304857.019 | 345269.736 | 0.0 | 0 | 16 |
| DEBUGMenu | 21 | 14.138 | 980.139 | 57591.531 | 345329.17 | 345469.703 | 0.0 | 0 | 15 |
| argumentationAnswerEvent | 17 | 2.884 | 24.299 | 45838.948 | 293764.904 | 431729.116 | 0.0 | 0 | 3 |
| gameStartEvent | 14 | 220.462 | 83449.454 | 86387.332 | 345394.945 | 345485.844 | 0.0 | 0 | 12 |
| TerasGardenBox | 12 | 0.668 | 19.571 | 189.801 | 956.395 | 2041.044 | 0.32 | 0 | 1 |
| argumentationEvent | 11 | 0.029 | 185.535 | 70855.788 | 345410.666 | 431657.11 | 0.0 | 2 | 3 |
| gameWindowUnfocusEvent | 10 | 0.109 | 43525.889 | 103867.427 | 345688.893 | 346099.777 | 0.0 | 0 | 6 |
| argumentationToolEvent | 8 | 0.156 | 0.86 | 97426.45 | 506575.415 | 779275.834 | 0.0 | 0 | 1 |
| SolarStillDesignEvent | 7 | 0.784 | 1.22 | 1.766 | 3.411 | 3.83 | 33.97 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 3 | 2.292 | 2.957 | 28910.569 | 78054.108 | 86726.458 | 0.0 | 0 | 1 |
| EndOfUnit | 2 | 174707.861 | 389840.722 | 389840.722 | 583460.297 | 604973.583 | 0.0 | 0 | 2 |
| chatEvent | 2 | 1236.146 | 42089.659 | 42089.658 | 78857.82 | 82943.171 | 0.0 | 0 | 2 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 11 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[10706] _id=6ac65382de269131f9ba7603 ts=2026-10-07T14:13:21.9550000Z == 6aa4140b41b41dbac0c7f227.jsonl[10707] _id=6ac65382de269131f9ba7604 ts=2026-10-07T14:13:21.9550000Z`; `6aa4140b41b41dbac0c7f227.jsonl[11388] _id=6ac65852de269131f9baed54 ts=2026-10-07T14:33:54.1810000Z == 6aa4140b41b41dbac0c7f227.jsonl[11390] _id=6ac65852de269131f9baed55 ts=2026-10-07T14:33:54.1810000Z`; `6aa4140b41b41dbac0c7f227.jsonl[11391] _id=6ac65852de269131f9baed56 ts=2026-10-07T14:33:54.1820000Z == 6aa4140b41b41dbac0c7f227.jsonl[11392] _id=6ac65852de269131f9baed57 ts=2026-10-07T14:33:54.1820000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 133 group(s), 182 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1629] _id=6abbc4d7485cab4c957e357d ts=2026-09-29T14:01:59.4990000Z == 6aa4140b41b41dbac0c7f227.jsonl[1633] _id=6abbc4d7485cab4c957e357f ts=2026-09-29T14:01:59.4990000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1626] _id=6abbc4d8485cab4c957e3591 ts=2026-09-29T14:01:59.6590000Z == 6aa4140b41b41dbac0c7f227.jsonl[1631] _id=6abbc4d8485cab4c957e3597 ts=2026-09-29T14:01:59.6590000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1713] _id=6abbc537485cab4c957e3ee3 ts=2026-09-29T14:03:28.6780000Z == 6aa4140b41b41dbac0c7f227.jsonl[1728] _id=6abbc537485cab4c957e3eea ts=2026-09-29T14:03:28.6780000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[309] _id=6ab52c5e485cab4c9551b7f7 ts=? == 6aa4140b41b41dbac0c7f227.jsonl[645] _id=6aba714d485cab4c9568380f ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `572ms: 6aa4140b41b41dbac0c7f227.jsonl[129] _id=6ab3e0eb485cab4c954d2091 ts=2026-09-23T14:23:39.5800000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[136] _id=6ab3e0ec485cab4c954d2097 ts=2026-09-23T14:23:40.1520000Z`; `218ms: 6aa4140b41b41dbac0c7f227.jsonl[136] _id=6ab3e0ec485cab4c954d2097 ts=2026-09-23T14:23:40.1520000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[139] _id=6ab3e0ec485cab4c954d209d ts=2026-09-23T14:23:40.3700000Z`; `1ms: 6aa4140b41b41dbac0c7f227.jsonl[195] _id=6ab3e17a485cab4c954d25f5 ts=2026-09-23T14:26:02.1620000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[200] _id=6ab3e17a485cab4c954d25f8 ts=2026-09-23T14:26:02.1630000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 532 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6aa4140b41b41dbac0c7f227.jsonl[1665] _id=6abbc534485cab4c957e3e2d ts=2026-09-29T14:01:43.6420000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[1666] _id=6abbc534485cab4c957e3e2f ts=2026-09-29T14:01:43.6610000Z`; `213ms: 6aa4140b41b41dbac0c7f227.jsonl[1718] _id=6abbc536485cab4c957e3e9f ts=2026-09-29T14:01:45.7590000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[1647] _id=6abbc536485cab4c957e3ea3 ts=2026-09-29T14:01:45.9720000Z`; `136ms: 6aa4140b41b41dbac0c7f227.jsonl[1647] _id=6abbc536485cab4c957e3ea3 ts=2026-09-29T14:01:45.9720000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[1722] _id=6abbc536485cab4c957e3eab ts=2026-09-29T14:01:46.1080000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `362ms: 6aa4140b41b41dbac0c7f227.jsonl[3593] _id=6abd174c485cab4c958a178c ts=2026-09-30T14:06:02.0890000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[3601] _id=6abd174d485cab4c958a17bc ts=2026-09-30T14:06:02.4510000Z`; `837ms: 6aa4140b41b41dbac0c7f227.jsonl[3601] _id=6abd174d485cab4c958a17bc ts=2026-09-30T14:06:02.4510000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[3599] _id=6abd174d485cab4c958a17e9 ts=2026-09-30T14:06:03.2880000Z`; `205ms: 6aa4140b41b41dbac0c7f227.jsonl[7385] _id=6ac3b60cde269131f9ac1472 ts=2026-10-05T14:37:00.1760000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[7399] _id=6ac3b60cde269131f9ac1478 ts=2026-10-05T14:37:00.3810000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `33ms: 6aa4140b41b41dbac0c7f227.jsonl[3140] _id=6abbc989485cab4c957ea4c3 ts=2026-09-29T14:22:01.8460000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[3144] _id=6abbc98a485cab4c957ea4d5 ts=2026-09-29T14:22:01.8790000Z`; `931ms: 6aa4140b41b41dbac0c7f227.jsonl[3155] _id=6abbc99a485cab4c957ea66f ts=2026-09-29T14:22:18.8380000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[3153] _id=6abbc99b485cab4c957ea67b ts=2026-09-29T14:22:19.7690000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `704ms: 6aa4140b41b41dbac0c7f227.jsonl[10944] _id=6ac654fdde269131f9baaaf9 ts=2026-10-07T14:19:41.1440000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[10946] _id=6ac654fdde269131f9baab31 ts=2026-10-07T14:19:41.8480000Z`; `487ms: 6aa4140b41b41dbac0c7f227.jsonl[10927] _id=6ac654fdde269131f9baab1a ts=2026-10-07T14:19:41.5490000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[10949] _id=6ac654fede269131f9baab39 ts=2026-10-07T14:19:42.0360000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6aa4140b41b41dbac0c7f227.jsonl[5880] _id=6abe6d49485cab4c95a85c49 ts=2026-10-01T14:25:12.9350000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[5882] _id=6abe6d49485cab4c95a85c57 ts=2026-10-01T14:25:12.9690000Z`; `29ms: 6aa4140b41b41dbac0c7f227.jsonl[10257] _id=6ac50431de269131f9b2d989 ts=2026-10-06T14:22:41.6610000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[10258] _id=6ac50432de269131f9b2d993 ts=2026-10-06T14:22:41.6900000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 80 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6aa4140b41b41dbac0c7f227.jsonl[1171] _id=6aba7750485cab4c9568c2d1 ts=2026-09-28T14:18:56.8370000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[1172] _id=6aba7750485cab4c9568c2d3 ts=2026-09-28T14:18:56.8720000Z`; `540ms: 6aa4140b41b41dbac0c7f227.jsonl[1173] _id=6aba7752485cab4c9568c2df ts=2026-09-28T14:18:58.4170000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[1176] _id=6aba7752485cab4c9568c2e9 ts=2026-09-28T14:18:58.9570000Z`; `850ms: 6aa4140b41b41dbac0c7f227.jsonl[1174] _id=6aba7752485cab4c9568c2e2 ts=2026-09-28T14:18:58.4320000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[1175] _id=6aba7753485cab4c9568c2f6 ts=2026-09-28T14:18:59.2820000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `604ms: 6aa4140b41b41dbac0c7f227.jsonl[11787] _id=6ac65c00de269131f9bb21c8 ts=2026-10-07T14:49:36.6630000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[11795] _id=6ac65c01de269131f9bb21d0 ts=2026-10-07T14:49:37.2670000Z`; `955ms: 6aa4140b41b41dbac0c7f227.jsonl[11795] _id=6ac65c01de269131f9bb21d0 ts=2026-10-07T14:49:37.2670000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[11790] _id=6ac65c02de269131f9bb21e4 ts=2026-10-07T14:49:38.2220000Z`; `704ms: 6aa4140b41b41dbac0c7f227.jsonl[11789] _id=6ac65c02de269131f9bb21e2 ts=2026-10-07T14:49:38.0660000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[11793] _id=6ac65c02de269131f9bb21f4 ts=2026-10-07T14:49:38.7700000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `108ms: 6aa4140b41b41dbac0c7f227.jsonl[7052] _id=6ac3b1b5de269131f9ab4364 ts=2026-10-05T14:18:29.8970000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[7056] _id=6ac3b1b7de269131f9ab43d1 ts=2026-10-05T14:18:30.0050000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `277ms: 6aa4140b41b41dbac0c7f227.jsonl[7055] _id=6ac3b1b5de269131f9ab4357 ts=2026-10-05T14:18:29.7070000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[7054] _id=6ac3b1b6de269131f9ab436d ts=2026-10-05T14:18:29.9840000Z`; `109ms: 6aa4140b41b41dbac0c7f227.jsonl[7054] _id=6ac3b1b6de269131f9ab436d ts=2026-10-05T14:18:29.9840000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[7057] _id=6ac3b1b8de269131f9ab4413 ts=2026-10-05T14:18:30.0930000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6aa4140b41b41dbac0c7f227.jsonl[11803] _id=6ac65c54de269131f9bb27f7 ts=2026-10-07T14:51:00.1910000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[11804] _id=6ac65c54de269131f9bb27f8 ts=2026-10-07T14:51:00.1920000Z`; `8ms: 6aa4140b41b41dbac0c7f227.jsonl[11961] _id=6ac65d43de269131f9bb3a9c ts=2026-10-07T14:54:59.5400000Z ~ 6aa4140b41b41dbac0c7f227.jsonl[11957] _id=6ac65d43de269131f9bb3a9e ts=2026-10-07T14:54:59.5480000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4140b41b41dbac0c7f227.jsonl[4927] _id=6abe659e485cab4c95a727a7 ts=2026-10-01T13:52:30.8540000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6031] _id=6ac3ab1cde269131f9a9e6fe ts=2026-10-05T13:50:20.5570000Z; 95h 55m: 6aa4140b41b41dbac0c7f227.jsonl[308] _id=6ab52c57485cab4c9551b767 ts=2026-09-24T13:57:43.2140000Z -> 6aa4140b41b41dbac0c7f227.jsonl[640] _id=6aba7148485cab4c95683737 ts=2026-09-28T13:53:12.3840000Z; 23h 55m: 6aa4140b41b41dbac0c7f227.jsonl[1408] _id=6abbc3d0485cab4c957e197f ts=2026-09-29T13:57:36.3470000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3325] _id=6abd145a485cab4c95895a95 ts=2026-09-30T13:53:31.7730000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 24h 5m 
  - Evidence: 24h 5m: 6aa4140b41b41dbac0c7f227.jsonl[8752] _id=6ac3bb30de269131f9acbff9 ts=2026-10-05T14:58:56.2320000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10527] _id=6ac50df6de269131f9b4278f ts=2026-10-06T15:04:22.6900000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa4140b41b41dbac0c7f227.jsonl[621] _id=6ab5305c485cab4c9551ec6d ts=2026-09-24T14:14:52.4930000Z -> 6aa4140b41b41dbac0c7f227.jsonl[661] _id=6aba716d485cab4c95683cfd ts=2026-09-28T13:53:50.0170000Z; 95h 25m: 6aa4140b41b41dbac0c7f227.jsonl[5934] _id=6abe6df4485cab4c95a8844b ts=2026-10-01T14:28:04.8970000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6098] _id=6ac3abd3de269131f9aa0fca ts=2026-10-05T13:53:23.8720000Z; 23h 27m: 6aa4140b41b41dbac0c7f227.jsonl[285] _id=6ab3e267485cab4c954d2fdc ts=2026-09-23T14:30:00.0330000Z -> 6aa4140b41b41dbac0c7f227.jsonl[322] _id=6ab52c67485cab4c9551b89b ts=2026-09-24T13:57:58.9560000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 581 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f227.jsonl[11371] _id=6ac65842de269131f9baebfd ts=2026-10-07T14:33:37.9480000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11372] _id=6ac65842de269131f9baebfe ts=2026-10-07T14:33:37.9490000Z; 1ms: 6aa4140b41b41dbac0c7f227.jsonl[11379] _id=6ac65840de269131f9baebf6 ts=2026-10-07T14:33:36.0370000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11380] _id=6ac65840de269131f9baebf7 ts=2026-10-07T14:33:36.0380000Z; 1ms: 6aa4140b41b41dbac0c7f227.jsonl[11679] _id=6ac65ba0de269131f9bb19d6 ts=2026-10-07T14:48:00.4110000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11680] _id=6ac65ba0de269131f9bb19d7 ts=2026-10-07T14:48:00.4120000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 2m 
  - Evidence: 168h 2m: 6aa4140b41b41dbac0c7f227.jsonl[1355] _id=6aba7911485cab4c9568dbd1 ts=2026-09-28T14:26:25.2800000Z -> 6aa4140b41b41dbac0c7f227.jsonl[7272] _id=6ac3b43ede269131f9abdbf6 ts=2026-10-05T14:29:18.8630000Z; 48h 31m: 6aa4140b41b41dbac0c7f227.jsonl[7272] _id=6ac3b43ede269131f9abdbf6 ts=2026-10-05T14:29:18.8630000Z -> 6aa4140b41b41dbac0c7f227.jsonl[12058] _id=6ac65eb2de269131f9bb602e ts=2026-10-07T15:01:06.7240000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa4140b41b41dbac0c7f227.jsonl[634] _id=6ab5307c485cab4c9551ee07 ts=2026-09-24T14:15:24.4330000Z -> 6aa4140b41b41dbac0c7f227.jsonl[641] _id=6aba714d485cab4c9568381b ts=2026-09-28T13:53:17.4670000Z; 95h 20m: 6aa4140b41b41dbac0c7f227.jsonl[6014] _id=6abe6e78485cab4c95a8a08f ts=2026-10-01T14:30:16.6060000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6033] _id=6ac3ab21de269131f9a9e7d2 ts=2026-10-05T13:50:25.0280000Z; 23h 29m: 6aa4140b41b41dbac0c7f227.jsonl[1373] _id=6aba798f485cab4c9568e451 ts=2026-09-28T14:28:31.8800000Z -> 6aa4140b41b41dbac0c7f227.jsonl[1413] _id=6abbc3e8485cab4c957e1c00 ts=2026-09-29T13:58:00.4630000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 109 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f227.jsonl[10706] _id=6ac65382de269131f9ba7603 ts=2026-10-07T14:13:21.9550000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10707] _id=6ac65382de269131f9ba7604 ts=2026-10-07T14:13:21.9550000Z; 0ms: 6aa4140b41b41dbac0c7f227.jsonl[10707] _id=6ac65382de269131f9ba7604 ts=2026-10-07T14:13:21.9550000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10708] _id=6ac65382de269131f9ba7605 ts=2026-10-07T14:13:21.9550000Z; 0ms: 6aa4140b41b41dbac0c7f227.jsonl[10708] _id=6ac65382de269131f9ba7605 ts=2026-10-07T14:13:21.9550000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10709] _id=6ac65382de269131f9ba7606 ts=2026-10-07T14:13:21.9550000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 39m 
  - Evidence: 95h 39m: 6aa4140b41b41dbac0c7f227.jsonl[611] _id=6ab53043485cab4c9551ea59 ts=2026-09-24T14:14:27.7180000Z -> 6aa4140b41b41dbac0c7f227.jsonl[692] _id=6aba7193485cab4c956842b7 ts=2026-09-28T13:54:27.1820000Z; 95h 39m: 6aa4140b41b41dbac0c7f227.jsonl[5459] _id=6abe6ab1485cab4c95a7bbef ts=2026-10-01T14:14:09.4570000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6139] _id=6ac3abfdde269131f9aa18e5 ts=2026-10-05T13:54:05.2970000Z; 23h 55m: 6aa4140b41b41dbac0c7f227.jsonl[2896] _id=6abbc6a0485cab4c957e6183 ts=2026-09-29T14:09:36.8260000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3570] _id=6abd170f485cab4c9589f5a0 ts=2026-09-30T14:05:03.2800000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f227.jsonl[10003] _id=6ac501c6de269131f9b26d16 ts=2026-10-06T14:12:22.8110000Z -> 6aa4140b41b41dbac0c7f227.jsonl[9999] _id=6ac501c7de269131f9b26d1c ts=2026-10-06T14:12:22.8120000Z; 1ms: 6aa4140b41b41dbac0c7f227.jsonl[10035] _id=6ac50218de269131f9b2794e ts=2026-10-06T14:13:44.4000000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10036] _id=6ac50218de269131f9b27950 ts=2026-10-06T14:13:44.4010000Z; 1ms: 6aa4140b41b41dbac0c7f227.jsonl[195] _id=6ab3e17a485cab4c954d25f5 ts=2026-09-23T14:26:02.1620000Z -> 6aa4140b41b41dbac0c7f227.jsonl[200] _id=6ab3e17a485cab4c954d25f8 ts=2026-09-23T14:26:02.1630000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa4140b41b41dbac0c7f227.jsonl[633] _id=6ab5307b485cab4c9551ee05 ts=2026-09-24T14:15:23.7620000Z -> 6aa4140b41b41dbac0c7f227.jsonl[646] _id=6aba714d485cab4c95683815 ts=2026-09-28T13:53:12.3900000Z; 95h 20m: 6aa4140b41b41dbac0c7f227.jsonl[6013] _id=6abe6e79485cab4c95a8a101 ts=2026-10-01T14:30:17.8610000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6032] _id=6ac3ab21de269131f9a9e7d0 ts=2026-10-05T13:50:20.5620000Z; 23h 27m: 6aa4140b41b41dbac0c7f227.jsonl[297] _id=6ab3e274485cab4c954d3085 ts=2026-09-23T14:30:12.0990000Z -> 6aa4140b41b41dbac0c7f227.jsonl[314] _id=6ab52c5e485cab4c9551b7fd ts=2026-09-24T13:57:43.2210000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6aa4140b41b41dbac0c7f227.jsonl[4586] _id=6abd19c8485cab4c958acfde ts=2026-09-30T14:16:37.9710000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6168] _id=6ac3ac3ade269131f9aa27c8 ts=2026-10-05T13:55:05.2890000Z; 24h 0m: 6aa4140b41b41dbac0c7f227.jsonl[2338] _id=6abbc658485cab4c957e5ea7 ts=2026-09-29T14:08:22.2170000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3664] _id=6abd1807485cab4c958a6dfd ts=2026-09-30T14:09:11.1750000Z; 23h 20m: 6aa4140b41b41dbac0c7f227.jsonl[8281] _id=6ac3b6d1de269131f9ac4496 ts=2026-10-05T14:40:15.1250000Z -> 6aa4140b41b41dbac0c7f227.jsonl[9684] _id=6ac4ff13de269131f9b23d55 ts=2026-10-06T14:00:50.4960000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1926 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f227.jsonl[10549] _id=6ac50f86de269131f9b44a3d ts=2026-10-06T15:11:01.5540000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10645] _id=6ac50f86de269131f9b44a43 ts=2026-10-06T15:11:01.5540000Z; 0ms: 6aa4140b41b41dbac0c7f227.jsonl[10625] _id=6ac50f83de269131f9b449ed ts=2026-10-06T15:10:58.5870000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10626] _id=6ac50f83de269131f9b449ef ts=2026-10-06T15:10:58.5870000Z; 0ms: 6aa4140b41b41dbac0c7f227.jsonl[10626] _id=6ac50f83de269131f9b449ef ts=2026-10-06T15:10:58.5870000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10641] _id=6ac50f83de269131f9b449f5 ts=2026-10-06T15:10:58.5870000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6aa4140b41b41dbac0c7f227.jsonl[3635] _id=6abd17a3485cab4c958a4df5 ts=2026-09-30T14:07:31.9350000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6131] _id=6ac3abfdde269131f9aa18d8 ts=2026-10-05T13:54:05.2910000Z; 23h 55m: 6aa4140b41b41dbac0c7f227.jsonl[2890] _id=6abbc6a3485cab4c957e6199 ts=2026-09-29T14:09:39.7990000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3571] _id=6abd170f485cab4c9589f576 ts=2026-09-30T14:05:03.2740000Z; 41m 38s: 6aa4140b41b41dbac0c7f227.jsonl[6146] _id=6ac3ac0fde269131f9aa1dd3 ts=2026-10-05T13:54:23.4870000Z -> 6aa4140b41b41dbac0c7f227.jsonl[7360] _id=6ac3b5d2de269131f9ac0b46 ts=2026-10-05T14:36:02.1410000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 34m 1s 
  - Evidence: 34m 1s: 6aa4140b41b41dbac0c7f227.jsonl[10452] _id=6ac5062ade269131f9b33d98 ts=2026-10-06T14:31:06.1740000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10543] _id=6ac50e23de269131f9b429eb ts=2026-10-06T15:05:07.2180000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4140b41b41dbac0c7f227.jsonl[5555] _id=6abe6b12485cab4c95a7caab ts=2026-10-01T14:15:46.2210000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6925] _id=6ac3b086de269131f9aaee09 ts=2026-10-05T14:13:26.1770000Z; 23h 29m: 6aa4140b41b41dbac0c7f227.jsonl[4826] _id=6abd1cb0485cab4c958b3f99 ts=2026-09-30T14:29:04.2530000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5057] _id=6abe6716485cab4c95a7730b ts=2026-10-01T13:58:46.9430000Z; 23h 23m: 6aa4140b41b41dbac0c7f227.jsonl[3303] _id=6abbcbfd485cab4c957ee927 ts=2026-09-29T14:32:29.5050000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3361] _id=6abd14e4485cab4c95896127 ts=2026-09-30T13:55:50.4630000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.033s shown 
  - Evidence: 22ms: 6aa4140b41b41dbac0c7f227.jsonl[3139] _id=6abbc989485cab4c957ea4bb ts=2026-09-29T14:22:01.8240000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3140] _id=6abbc989485cab4c957ea4c3 ts=2026-09-29T14:22:01.8460000Z; 33ms: 6aa4140b41b41dbac0c7f227.jsonl[3140] _id=6abbc989485cab4c957ea4c3 ts=2026-09-29T14:22:01.8460000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3144] _id=6abbc98a485cab4c957ea4d5 ts=2026-09-29T14:22:01.8790000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 55m 
  - Evidence: 119h 55m: 6aa4140b41b41dbac0c7f227.jsonl[5879] _id=6abe6d48485cab4c95a85c41 ts=2026-10-01T14:25:12.9140000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10152] _id=6ac503bade269131f9b2ca15 ts=2026-10-06T14:20:42.0300000Z; 72h 1m: 6aa4140b41b41dbac0c7f227.jsonl[1244] _id=6aba7821485cab4c9568cd95 ts=2026-09-28T14:22:25.2460000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5799] _id=6abe6ceb485cab4c95a84c25 ts=2026-10-01T14:23:39.0970000Z; 24h 25m: 6aa4140b41b41dbac0c7f227.jsonl[10256] _id=6ac50431de269131f9b2d985 ts=2026-10-06T14:22:41.6400000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11675] _id=6ac65b9bde269131f9bb198d ts=2026-10-07T14:47:55.9610000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 54m 
  - Evidence: 119h 54m: 6aa4140b41b41dbac0c7f227.jsonl[5882] _id=6abe6d49485cab4c95a85c57 ts=2026-10-01T14:25:12.9690000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10110] _id=6ac50372de269131f9b2b884 ts=2026-10-06T14:19:30.0790000Z; 71h 59m: 6aa4140b41b41dbac0c7f227.jsonl[1245] _id=6aba7821485cab4c9568cd97 ts=2026-09-28T14:22:25.2680000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5683] _id=6abe6c7d485cab4c95a83306 ts=2026-10-01T14:21:49.4900000Z; 24h 23m: 6aa4140b41b41dbac0c7f227.jsonl[10258] _id=6ac50432de269131f9b2d993 ts=2026-10-06T14:22:41.6900000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11606] _id=6ac65b4cde269131f9bb137c ts=2026-10-07T14:46:36.2940000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.029s..0.034s shown 
  - Evidence: 29ms: 6aa4140b41b41dbac0c7f227.jsonl[10257] _id=6ac50431de269131f9b2d989 ts=2026-10-06T14:22:41.6610000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10258] _id=6ac50432de269131f9b2d993 ts=2026-10-06T14:22:41.6900000Z; 34ms: 6aa4140b41b41dbac0c7f227.jsonl[5880] _id=6abe6d49485cab4c95a85c49 ts=2026-10-01T14:25:12.9350000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5882] _id=6abe6d49485cab4c95a85c57 ts=2026-10-01T14:25:12.9690000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 54m 
  - Evidence: 119h 54m: 6aa4140b41b41dbac0c7f227.jsonl[5876] _id=6abe6d44485cab4c95a85b8f ts=2026-10-01T14:25:08.4120000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10119] _id=6ac50380de269131f9b2bbde ts=2026-10-06T14:19:44.7040000Z; 71h 59m: 6aa4140b41b41dbac0c7f227.jsonl[1249] _id=6aba781f485cab4c9568cd8b ts=2026-09-28T14:22:23.7480000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5684] _id=6abe6c80485cab4c95a8338f ts=2026-10-01T14:21:52.1780000Z; 24h 23m: 6aa4140b41b41dbac0c7f227.jsonl[10252] _id=6ac5042fde269131f9b2d94d ts=2026-10-06T14:22:39.7060000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11602] _id=6ac65b4dde269131f9bb1397 ts=2026-10-07T14:46:37.1890000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 73 interval(s) ≤ 0.001s..0.008s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f227.jsonl[5691] _id=6abe6c8b485cab4c95a836bc ts=2026-10-01T14:22:03.3760000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5693] _id=6abe6c8b485cab4c95a836c2 ts=2026-10-01T14:22:03.3770000Z; 3ms: 6aa4140b41b41dbac0c7f227.jsonl[5855] _id=6abe6d2d485cab4c95a8579f ts=2026-10-01T14:24:45.1840000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5830] _id=6abe6d2d485cab4c95a857ac ts=2026-10-01T14:24:45.1870000Z; 8ms: 6aa4140b41b41dbac0c7f227.jsonl[5755] _id=6abe6cca485cab4c95a845d7 ts=2026-10-01T14:23:06.7680000Z -> 6aa4140b41b41dbac0c7f227.jsonl[5761] _id=6abe6cca485cab4c95a845d9 ts=2026-10-01T14:23:06.7760000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 216h 27m 
  - Evidence: 216h 27m: 6aa4140b41b41dbac0c7f227.jsonl[1219] _id=6aba77f3485cab4c9568cb6b ts=2026-09-28T14:21:39.9080000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11792] _id=6ac65bffde269131f9bb21b7 ts=2026-10-07T14:49:35.7420000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 2m 
  - Evidence: 23h 2m: 6aa4140b41b41dbac0c7f227.jsonl[10631] _id=6ac50f7dde269131f9b44969 ts=2026-10-06T15:10:53.0450000Z -> 6aa4140b41b41dbac0c7f227.jsonl[10701] _id=6ac6537cde269131f9ba7576 ts=2026-10-07T14:13:16.2160000Z; 20m 36s: 6aa4140b41b41dbac0c7f227.jsonl[10701] _id=6ac6537cde269131f9ba7576 ts=2026-10-07T14:13:16.2160000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11389] _id=6ac65850de269131f9baec73 ts=2026-10-07T14:33:52.3620000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 58m 
  - Evidence: 95h 58m: 6aa4140b41b41dbac0c7f227.jsonl[4926] _id=6abe6587485cab4c95a72019 ts=2026-10-01T13:52:06.8920000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6029] _id=6ac3ab14de269131f9a9e5ae ts=2026-10-05T13:50:12.7360000Z; 95h 55m: 6aa4140b41b41dbac0c7f227.jsonl[302] _id=6ab52c2f485cab4c9551b441 ts=2026-09-24T13:57:02.9410000Z -> 6aa4140b41b41dbac0c7f227.jsonl[639] _id=6aba7131485cab4c956833df ts=2026-09-28T13:52:48.9400000Z; 23h 56m: 6aa4140b41b41dbac0c7f227.jsonl[1407] _id=6abbc3b5485cab4c957e1701 ts=2026-09-29T13:57:08.8760000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3322] _id=6abd1449485cab4c95895a11 ts=2026-09-30T13:53:15.3950000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 54m 
  - Evidence: 95h 54m: 6aa4140b41b41dbac0c7f227.jsonl[325] _id=6ab52c7b485cab4c9551b95f ts=2026-09-24T13:58:19.2030000Z -> 6aa4140b41b41dbac0c7f227.jsonl[638] _id=6aba7130485cab4c956833d9 ts=2026-09-28T13:52:48.9390000Z; 95h 24m: 6aa4140b41b41dbac0c7f227.jsonl[5906] _id=6abe6d7b485cab4c95a866fe ts=2026-10-01T14:26:03.2750000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6028] _id=6ac3ab14de269131f9a9e5a5 ts=2026-10-05T13:50:12.7350000Z; 23h 56m: 6aa4140b41b41dbac0c7f227.jsonl[1406] _id=6abbc3b4485cab4c957e16fb ts=2026-09-29T13:57:08.8740000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3321] _id=6abd1449485cab4c95895a0b ts=2026-09-30T13:53:15.3950000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 8m 
  - Evidence: 96h 8m: 6aa4140b41b41dbac0c7f227.jsonl[326] _id=6ab52c6f485cab4c9551b90d ts=2026-09-24T13:58:07.5960000Z -> 6aa4140b41b41dbac0c7f227.jsonl[911] _id=6aba7463485cab4c95687c2f ts=2026-09-28T14:06:27.3730000Z; 95h 53m: 6aa4140b41b41dbac0c7f227.jsonl[5888] _id=6abe6d53485cab4c95a85df9 ts=2026-10-01T14:25:23.0050000Z -> 6aa4140b41b41dbac0c7f227.jsonl[7055] _id=6ac3b1b5de269131f9ab4357 ts=2026-10-05T14:18:29.7070000Z; 47h 48m: 6aa4140b41b41dbac0c7f227.jsonl[1042] _id=6aba762d485cab4c9568a4f1 ts=2026-09-28T14:14:05.8860000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3476] _id=6abd1680485cab4c9589a37e ts=2026-09-30T14:02:40.0360000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 46m 
  - Evidence: 95h 46m: 6aa4140b41b41dbac0c7f227.jsonl[471] _id=6ab52e8a485cab4c9551d277 ts=2026-09-24T14:07:05.9780000Z -> 6aa4140b41b41dbac0c7f227.jsonl[650] _id=6aba714e485cab4c9568383d ts=2026-09-28T13:53:17.4930000Z; 95h 22m: 6aa4140b41b41dbac0c7f227.jsonl[5932] _id=6abe6de9485cab4c95a881ad ts=2026-10-01T14:27:53.6480000Z -> 6aa4140b41b41dbac0c7f227.jsonl[6035] _id=6ac3ab21de269131f9a9e7d8 ts=2026-10-05T13:50:25.0470000Z; 23h 31m: 6aa4140b41b41dbac0c7f227.jsonl[3131] _id=6abbc972485cab4c957ea23b ts=2026-09-29T14:21:38.6190000Z -> 6aa4140b41b41dbac0c7f227.jsonl[3328] _id=6abd1460485cab4c95895ad1 ts=2026-09-30T13:53:37.4010000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f227.jsonl[11285] _id=6ac6574dde269131f9bade3c ts=2026-10-07T14:29:33.4960000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11286] _id=6ac6574dde269131f9bade3d ts=2026-10-07T14:29:33.4960000Z; 1ms: 6aa4140b41b41dbac0c7f227.jsonl[11084] _id=6ac65562de269131f9bab869 ts=2026-10-07T14:21:22.2820000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11085] _id=6ac65562de269131f9bab86a ts=2026-10-07T14:21:22.2830000Z; 1ms: 6aa4140b41b41dbac0c7f227.jsonl[11803] _id=6ac65c54de269131f9bb27f7 ts=2026-10-07T14:51:00.1910000Z -> 6aa4140b41b41dbac0c7f227.jsonl[11804] _id=6ac65c54de269131f9bb27f8 ts=2026-10-07T14:51:00.1920000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 22h 39m 
  - Evidence: 22h 39m: 6aa4140b41b41dbac0c7f227.jsonl[9195] _id=6ac3be2fde269131f9acdb55 ts=2026-10-05T15:11:43.0700000Z -> 6aa4140b41b41dbac0c7f227.jsonl[9318] _id=6ac4fce3de269131f9b1b0a3 ts=2026-10-06T13:51:31.9140000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1104] _id=6aba76be485cab4c9568b43f ts=2026-09-28T14:16:30.1390000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1258] _id=6aba783a485cab4c9568cea9 ts=2026-09-28T14:22:50.1960000Z`; `6aa4140b41b41dbac0c7f227.jsonl[3364] _id=6abd14f4485cab4c9589622d ts=2026-09-30T13:56:05.6800000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 122 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1542] _id=6abbc555485cab4c957e4365 ts=2026-09-29T14:04:04.5920000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1545] _id=6abbc556485cab4c957e438d ts=2026-09-29T14:04:05.1260000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1578] _id=6abbc55e485cab4c957e445f ts=2026-09-29T14:04:13.2440000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 278 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1676] _id=6abbc532485cab4c957e3ddf ts=2026-09-29T14:01:43.2910000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1662] _id=6abbc533485cab4c957e3e07 ts=2026-09-29T14:01:43.4470000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1666] _id=6abbc534485cab4c957e3e2f ts=2026-09-29T14:01:43.6610000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[5882] _id=6abe6d49485cab4c95a85c57 ts=2026-10-01T14:25:12.9690000Z`; `6aa4140b41b41dbac0c7f227.jsonl[10258] _id=6ac50432de269131f9b2d993 ts=2026-10-06T14:22:41.6900000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[5696] _id=6abe6c8b485cab4c95a836cb ts=2026-10-01T14:22:03.4180000Z`; `6aa4140b41b41dbac0c7f227.jsonl[5756] _id=6abe6cca485cab4c95a845dd ts=2026-10-01T14:23:06.7980000Z`; `6aa4140b41b41dbac0c7f227.jsonl[5824] _id=6abe6d03485cab4c95a85053 ts=2026-10-01T14:24:02.2570000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[10631] _id=6ac50f7dde269131f9b44969 ts=2026-10-06T15:10:53.0450000Z`; `6aa4140b41b41dbac0c7f227.jsonl[10701] _id=6ac6537cde269131f9ba7576 ts=2026-10-07T14:13:16.2160000Z`; `6aa4140b41b41dbac0c7f227.jsonl[11389] _id=6ac65850de269131f9baec73 ts=2026-10-07T14:33:52.3620000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[6171] _id=6ac3ac35de269131f9aa26d8 ts=2026-10-05T13:55:01.7330000Z`; `6aa4140b41b41dbac0c7f227.jsonl[9254] _id=6ac4fc4cde269131f9b1849d ts=2026-10-06T13:49:00.8400000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[309] _id=6ab52c5e485cab4c9551b7f7 ts=?`; `6aa4140b41b41dbac0c7f227.jsonl[645] _id=6aba714d485cab4c9568380f ts=?`; `6aa4140b41b41dbac0c7f227.jsonl[1409] _id=6abbc3d6485cab4c957e1a4d ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 478 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1757] _id=6abbc54c485cab4c957e41d7 ts=2026-09-29T14:03:55.9380000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1498] _id=6abbc54c485cab4c957e41dd ts=2026-09-29T14:03:55.9470000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1525] _id=6abbc554485cab4c957e434d ts=2026-09-29T14:04:04.3750000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 548 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1702] _id=6abbc534485cab4c957e3e31 ts=2026-09-29T14:01:43.6610000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1691] _id=6abbc534485cab4c957e3e4d ts=2026-09-29T14:01:43.7870000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1707] _id=6abbc535485cab4c957e3e5d ts=2026-09-29T14:01:43.8480000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 16 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[3140] _id=6abbc989485cab4c957ea4c3 ts=2026-09-29T14:22:01.8460000Z`; `6aa4140b41b41dbac0c7f227.jsonl[3144] _id=6abbc98a485cab4c957ea4d5 ts=2026-09-29T14:22:01.8790000Z`; `6aa4140b41b41dbac0c7f227.jsonl[3191] _id=6abbc9f1485cab4c957eb099 ts=2026-09-29T14:23:45.5380000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 54 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1172] _id=6aba7750485cab4c9568c2d3 ts=2026-09-28T14:18:56.8720000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1173] _id=6aba7752485cab4c9568c2df ts=2026-09-28T14:18:58.4170000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1176] _id=6aba7752485cab4c9568c2e9 ts=2026-09-28T14:18:58.9570000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[11795] _id=6ac65c01de269131f9bb21d0 ts=2026-10-07T14:49:37.2670000Z`; `6aa4140b41b41dbac0c7f227.jsonl[11790] _id=6ac65c02de269131f9bb21e4 ts=2026-10-07T14:49:38.2220000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'DialogueStartEvent' (totals: 382 start, 379 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 145 unmatched 'BecameCameraCentered' (totals: 716 open, 693 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 103 unmatched 'BecameVisible' (totals: 835 open, 1010 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 18 open, 16 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationNodeHoverStart' (totals: 200 open, 203 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationToolOpen' (totals: 6 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 50 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 277 of 12054 adjacent _id pairs reverse in client time; worst 107.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f227.jsonl[1721] _id=6abbc536485cab4c957e3e99 ts=2026-09-29T14:03:33.0730000Z`; `6aa4140b41b41dbac0c7f227.jsonl[1718] _id=6abbc536485cab4c957e3e9f ts=2026-09-29T14:01:45.7590000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -109.43s, max +1.72s over 12055 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f227\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 6 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3347 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (722); Unit 2 Prod (Refactor) (614); Unit 3 Dev (612); Unit 1 Dev (557); Unit 4 Dev (264); Unit 3 Dungeon Dev (259); Unit 5 Dev - Dungeon (211); Unit 5 Dev (85); Unit 4 Dev - Anderson Base (23)
- **Intervals:** median 1.32s (p5 0.12s / p95 21.99s, n=3346)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3347/3347 records)
    "pressed"  x3347
data.actionType  (string, 3347/3347 records)
    "Move"  x2456
    "Interact"  x547
    "Jump"  x267
    "Hoverboard"  x43
    "Map"  x12
    "Sprint"  x12
    "Ascend"  x3
    "ToggleDebug"  x3
    "Pause"  x2
    "SkipCinematic"  x2
data.key  (string, 3347/3347 records, 10 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3347/3347 records)
    "Player"  x3054
    "Drone"  x293
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3254 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1864); Unit 4 Dev (892); Unit 5 Dev - Dungeon (254); Unit 3 Dungeon Dev (244)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.33s, n=3253)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3254/3254 records)
    "BecameInvisible"  x1010
    "BecameVisible"  x835
    "BecameCameraCentered"  x716
    "BecameCameraUncentered"  x693
data.pieceId  (string, 3254/3254 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3254/3254 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2201 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (492); Unit 1 Dev (389); Unit 3 Dev (361); Unit 4 Dev - Dungeon (262); Unit 4 Dev (211); Unit 5 Dev (161); Unit 5 Dev - Dungeon (146); Unit 3 Dungeon Dev (98); Unit 4 Dev - Anderson Base (81)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2189)
- **Fields under `data`:**

```text
data.position  (object, 2201/2201 records)
data.position.x  (number, 2201/2201 records)
    numeric range -816.112 .. 1555.76 (762 unique)
data.position.y  (number, 2201/2201 records)
    numeric range -115.127 .. 222.252 (588 unique)
data.position.z  (number, 2201/2201 records)
    numeric range -1197.96 .. 1915.43 (760 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2013 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (428); Unit 3 Dev (386); Unit 1 Dev (304); Unit 5 Dev (236); Unit 4 Dev (225); Unit 4 Dev - Dungeon (151); Unit 3 Dungeon Dev (116); Unit 4 Dev - Anderson Base (87); Unit 5 Dev - Dungeon (80)
- **eventKey:** present on 1252 of 2013 records
- **Intervals:** median 5.08s (p5 0.00s / p95 41.75s, n=2012)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1252; [conversationId, dialogueEventType] x761
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2013/2013 records)
    numeric range 8 .. 118 (54 unique)
data.dialogueEventType  (string, 2013/2013 records)
    "DialogueNodeEvent"  x1252
    "DialogueStartEvent"  x382
    "DialogueFinishEvent"  x379
data.nodeId  (number, 1252/2013 records)
    numeric range 0 .. 290 (217 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 455 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (157); Unit 5 Dev (152); Unit 4 Dev - Anderson Base (113); Unit 1 Dev (33)
- **Intervals:** median 0.43s (p5 0.03s / p95 5.97s, n=454)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 455/455 records)
    "argumentationNodeHoverEnd"  x203
    "argumentationNodeHoverStart"  x200
    "argumentationNodeAdd"  x33
    "argumentationNodeRemove"  x19
data.argumentationTitle  (string, 455/455 records)
    "Unit 3 - Pollution Upstream"  x157
    "Unit 5"  x152
    "Unit 4 - Flooding"  x113
    "Unit 1 - Freshwater"  x19
    "Unit 1 - Argumentation Tutorial"  x14
data.nodeName  (string, 455/455 records)
    "4"  x60
    "2"  x57
    "3"  x52
    "1"  x40
    "A"  x40
    "C"  x40
    "II"  x40
    "D"  x38
    "I"  x37
    "B"  x36
    "5"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 305 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (131); Unit 2 Prod (Refactor) (45); Unit 4 Dev (34); Unit 3 Dungeon Dev (29); Unit 1 Dev (23); Unit 3 Dev (20); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (8); Unit 5 Dev (6)
- **Intervals:** median 12.40s (p5 1.46s / p95 420.61s, n=304)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 305/305 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 305/305 records)
    96 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 86 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (52); Unit 4 Dev (26); Unit 3 Dev (8)
- **Intervals:** median 1.15s (p5 0.20s / p95 17.84s, n=85)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x78; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/86 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/86 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 78/86 records)
    "RightDrag"  x42
    "LeftDrag"  x36
data.currentSoilType  (string, 78/86 records)
    "SAND"  x19
    "CLAYSAND"  x14
    "SANDGRAVEL"  x14
    "CLAY"  x12
    "CLAYROCK"  x11
    "GRAVEL"  x5
    "BEDROCK"  x3
data.isCorrectSelection  (string, 78/86 records)
    "false"  x59
    "true"  x19
data.waterLevelStatus  (string, 78/86 records)
    "Proper"  x29
    "TooHigh"  x28
    "TooLow"  x21
data.waterRetentionChange  (string, 78/86 records)
    "Increase"  x33
    "Decrease"  x26
    "NoChange"  x19
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 85 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (20); Unit 4 Dev - Dungeon (15); Unit 3 Dev (13); Unit 2 Prod (Refactor) (12); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 4 Dev (6); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 85 of 85 records
- **Intervals:** median 241.25s (p5 0.00s / p95 84462.99s, n=84)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 85/85 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x35
data.questID  (string, 85/85 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 85/85 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/85 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 67 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (45); Unit 3 Dev (18); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 4.46s (p5 0.87s / p95 63069.93s, n=66)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, location] x33
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 67/67 records)
    "WaypointMoveEvent"  x28
    "MapOpenEvent"  x18
    "MapCloseEvent"  x16
    "WaypointSetEvent"  x5
data.featureUsed  (string, 67/67 records)
    "Map"  x34
    "Waypoint"  x33
data.location  (object, 33/67 records)
data.location.x  (number, 33/67 records)
    numeric range -226.09 .. 641.526 (28 unique)
data.location.y  (number, 33/67 records)
    numeric range -237.5 .. 282.23 (31 unique)
data.location.z  (number, 33/67 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 57 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (57)
- **Intervals:** median 5.35s (p5 0.38s / p95 45.77s, n=56)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 57/57 records)
    "On"  x33
    "Off"  x24
data.floor  (string, 57/57 records)
    "4"  x21
    "3"  x20
    "1"  x11
    "2"  x5
data.machineNumber  (string, 57/57 records)
    "One"  x56
    "Two"  x1
data.machineType  (string, 57/57 records)
    "Evaporator"  x26
    "Condenser"  x19
    "DualChamber_Evaporator"  x6
    "DualChamber_Condenser"  x4
    "VentSwitch"  x2
data.room  (string, 57/57 records)
    "2"  x30
    "3"  x20
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 42 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (42)
- **Intervals:** median 7.67s (p5 1.90s / p95 183.84s, n=41)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "ChangeCanister"  x42
data.canisterType  (string, 42/42 records)
    "Bedrock"  x17
    "Clay"  x15
    "Gravel"  x6
    "Sand"  x4
data.floor  (string, 42/42 records)
    "5"  x29
    "4"  x11
    "3"  x2
data.machine  (string, 42/42 records)
    "1"  x41
    "2"  x1
data.row  (string, 42/42 records)
    "TopRow"  x25
    "BottomRow"  x17
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1837.47s (p5 22.85s / p95 304857.02s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 22 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 4 Dev (4); Unit 1 Dev (3); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (2); MainMenu (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 980.14s (p5 236.27s / p95 345329.17s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "DebugMenuStateChanged"  x22
data.isOpened  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 18 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (9); Unit 1 Dev (3); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 24.30s (p5 4.08s / p95 293764.90s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "submitAnswerEvent"  x18
data.answerSubmitted  (string, 18/18 records, 2 empty-string)
    13 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 18/18 records)
    "Unit 5"  x9
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 83449.45s (p5 359.58s / p95 345394.94s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `TerasGardenBox` — 13 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (13)
- **Intervals:** median 19.57s (p5 1.31s / p95 956.40s, n=12)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records, 4 empty-string)
    "cameraPlaced"  x9
    ""  x4
data.boxId  (string, 13/13 records)
    "0"  x8
    "1"  x3
    "2"  x2
data.soilType  (string, 13/13 records)
    "None"  x7
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 185.53s (p5 0.03s / p95 345410.67s, n=11)
- **Open findings:** 2 — see sections 5-8
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

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (4); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 43525.89s (p5 0.18s / p95 345688.89s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (6); Unit 1 Dev (3)
- **Intervals:** median 0.86s (p5 0.29s / p95 506575.42s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x6
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 9/9 records)
    "Unit 5"  x6
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 1.22s (p5 0.83s / p95 3.41s, n=7)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x7; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "optionSelected"  x7
    "DesignSubmitted"  x1
data.designSelections  (object, 1/8 records)
data.designSelections.glassRoofTemperature  (string, 1/8 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/8 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/8 records)
    "Tilted Out"  x1
data.featureUsed  (string, 8/8 records)
    "RoofStyle"  x3
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "Submit"  x1
data.selectedOption  (string, 7/8 records)
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `crash` — 6 records

- **Scenes:** <missing sceneName> (6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 6/6 records)
    true  x6
data.message  (string, 6/6 records)
    "A user gesture is required to request Pointer Lock."  x4
    "Permissions check failed"  x1
    "Uncaught RuntimeError: memory access out of bounds"  x1
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 4 empty-string)
    ""  x4
    "RuntimeError: memory access out of bounds
    at wasm://wasm/0a8f805e:wasm-function[108509]:0x24df167
    at wasm://wasm/0a8f805e:wasm-function[3309]:0x143b2d
    at wasm://wasm/0a8f805e:wasm-function[59913]:0x11cf1cd
    at wasm://wasm/0a8f805e:wasm-function[3347]:0x145f40
    at wasm://wasm/0a8f805e:wasm-function[82466]:0x170453c
    at wasm://wasm/0a8f805e:wasm-function[83416]:0x17182aa
    at wasm://wasm/0a8f805e:wasm-function[110273]:0x2598735
    at invoke_iiii (blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:474038)
    at wasm://wasm/0a8f805e:wasm-function[83401]:0x171794a
    at wasm://wasm/0a8f805e:wasm-function[1942]:0xf5838
    at wasm://wasm/0a8f805e:wasm-function[109930]:0x255f709
    at wasm://wasm/0a8f805e:wasm-function[106236]:0x24b04bf
    at wasm://wasm/0a8f805e:wasm-function[84040]:0x173e5ce
    at wasm://wasm/0a8f805e:wasm-function[84039]:0x173e504
    at wasm://wasm/0a8f805e:wasm-function[104562]:0x23e3a49
    at wasm://wasm/0a8f805e:wasm-function[104548]:0x23dfb1e
    at wasm://wasm/0a8f805e:wasm-function[103926]:0x2354335
    at wasm://wasm/0a8f805e:wasm-function[105656]:0x245857d
    at wasm://wasm/0a8f805e:wasm-function[105656]:0x24585f2
    at wasm://wasm/0a8f805e:wasm-function[110008]:0x2567b3c
    at wasm://wasm/0a8f805e:wasm-function[110279]:0x2598788
    at blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:23580
    at _JS_CallAsLongAsNoExceptionsSeen (blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:23594)
    at wasm://wasm/0a8f805e:wasm-function[110009]:0x2567c4b
    at wasm://wasm/0a8f805e:wasm-function[110279]:0x2598788
    at browserIterationFunc (blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:115768)
    at callUserCallback (blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:98130)
    at Object.runIter (blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:99497)
    at Browser_mainLoop_runner (blob:https://mhs.adroit.games/9a038634-e848-4261-96b0-332bca7b1dd8:9:115294)"  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 6/6 records)
    "unhandled_rejection"  x5
    "runtime_error"  x1
data.unitId  (string, 6/6 records)
    "unit1"  x2
    "unit2"  x2
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 2.96s (p5 2.36s / p95 78054.11s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 389840.72s (p5 196221.15s / p95 583460.30s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "3"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 42089.66s (p5 5321.50s / p95 78857.82s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (52 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (7x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (28x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (33x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (19x)
- `soilMachine` data.canisterType: "Bedrock" (17x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*