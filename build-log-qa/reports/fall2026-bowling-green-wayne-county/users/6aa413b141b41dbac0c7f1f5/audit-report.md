# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f5

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1f5
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f5.jsonl
- **Records:** 14391 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f5
- **Time span:** 2026-09-22T12:59:29.437000+00:00 .. 2026-10-05T20:38:14.706000+00:00 (319h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f5\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14391 records, 11 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 111 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5836 | 40.55 | 1 | 9 | 0 | 2026-09-22T13:00:13.631000+00:00 | 2026-10-05T20:38:14.706000+00:00 | 319h 38m |
| PuzzlePieceVisibleEvent | 2942 | 20.44 | 1 | 4 | 0 | 2026-09-24T12:58:15.928000+00:00 | 2026-10-05T20:08:16.137000+00:00 | 271h 10m |
| DialogueEvent | 2120 | 14.73 | 1 | 9 | 1329 | 2026-09-22T13:00:15.131000+00:00 | 2026-10-05T20:38:04.967000+00:00 | 319h 37m |
| PlayerPositionEvent | 2054 | 14.27 | 1 | 9 | 0 | 2026-09-22T12:59:52.716000+00:00 | 2026-10-05T20:38:07.894000+00:00 | 319h 38m |
| argumentationNodeEvent | 678 | 4.71 | 1 | 5 | 0 | 2026-09-23T13:33:05.403000+00:00 | 2026-10-05T20:25:48.692000+00:00 | 294h 52m |
| ObjectInterEvent | 219 | 1.52 | 1 | 9 | 0 | 2026-09-23T13:17:04.525000+00:00 | 2026-10-05T20:38:14.706000+00:00 | 295h 21m |
| TopographicMapEvent | 109 | 0.76 | 1 | 2 | 0 | 2026-09-24T12:58:46.760000+00:00 | 2026-10-01T13:37:09.936000+00:00 | 168h 38m |
| questEvent | 83 | 0.58 | 1 | 9 | 83 | 2026-09-22T13:00:15.107000+00:00 | 2026-10-05T20:33:57.733000+00:00 | 319h 33m |
| Soil Key Puzzle | 56 | 0.39 | 1 | 3 | 0 | 2026-09-24T13:06:20.737000+00:00 | 2026-10-05T13:17:26.633000+00:00 | 264h 11m |
| argumentationAnswerEvent | 49 | 0.34 | 1 | 4 | 0 | 2026-09-23T13:34:06.156000+00:00 | 2026-10-05T20:25:49.987000+00:00 | 294h 51m |
| DaniEvent | 40 | 0.28 | 1 | 1 | 0 | 2026-09-24T13:29:41.696000+00:00 | 2026-09-29T13:40:01.724000+00:00 | 120h 10m |
| gameWindowFocusEvent | 39 | 0.27 | 1 | 8 | 0 | 2026-09-22T12:59:29.437000+00:00 | 2026-10-05T20:20:59.258000+00:00 | 319h 21m |
| gameWindowUnfocusEvent | 28 | 0.19 | 1 | 8 | 0 | 2026-09-22T13:00:47.544000+00:00 | 2026-10-05T20:20:59.253000+00:00 | 319h 20m |
| DEBUGMenu | 26 | 0.18 | 1 | 8 | 0 | 2026-09-22T12:59:52.710000+00:00 | 2026-10-05T20:02:02.755000+00:00 | 319h 2m |
| WaterChamberEvent | 26 | 0.18 | 1 | 1 | 0 | 2026-10-05T20:07:06.041000+00:00 | 2026-10-05T20:16:31.902000+00:00 | 9m 25s |
| gameStartEvent | 21 | 0.15 | 1 | 1 | 0 | 2026-09-22T12:59:29.438000+00:00 | 2026-10-05T20:01:56.028000+00:00 | 319h 2m |
| chatEvent | 19 | 0.13 | 1 | 3 | 0 | 2026-09-24T13:29:44.009000+00:00 | 2026-10-05T20:17:22.304000+00:00 | 270h 47m |
| argumentationEvent | 13 | 0.09 | 1 | 4 | 0 | 2026-09-23T13:33:55.793000+00:00 | 2026-10-05T20:25:50.011000+00:00 | 294h 51m |
| soilMachine | 12 | 0.08 | 1 | 1 | 0 | 2026-10-05T13:31:47.926000+00:00 | 2026-10-05T13:39:03.549000+00:00 | 7m 15s |
| TerasGardenBox | 6 | 0.04 | 1 | 1 | 0 | 2026-10-05T19:47:17.971000+00:00 | 2026-10-05T19:48:07.560000+00:00 | 49.6s |
| crash | 5 | 0.03 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-23T13:37:52.117000+00:00 | 2026-10-05T20:38:14.699000+00:00 | 295h 0m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-05T20:31:19.429000+00:00 | 2026-10-05T20:31:29.430000+00:00 | 10.0s |
| argumentationToolEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-09-23T13:33:54.032000+00:00 | 2026-09-23T13:33:55.770000+00:00 | 1.7s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 24706.542s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.87s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 14.496s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.738s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 4.657s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6101.109s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 693.168s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 839.093s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 7.099s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 40 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
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
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay 
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
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 9.8x vs baseline. 
  - Observed: 49 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,B,C,2,II; A,C,2,II; A,C,3,II; A,C,4,II; A,C,B,2,II; A,D,C,2,II; B,2,II; B,C,2,II; C,2,II; C,3,II; C,4,II; C,A,2,II; C,B,D,2,II; C,D,2,II; C,D,3,II; D,2,II; D,A,2,II; D,C,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.8x vs baseline. 
  - Observed: 678 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 9.5x vs baseline. 
  - Observed: 19 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-287, 18-289]; [21-21, 21-22, 21-23, 21-24, 21-25]; [22-22, 22-46, 22-48, 22-27, 18-287, 18-289]; [22-46, 22-48, 22-27, 18-287, 18-289]; [23-35, 23-36, 23-38, 23-40, 23-41] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 41 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[336] _id=6ab3d211485cab4c954be374 ts=2026-09-23T13:20:17.1660000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[401] _id=6ab3d303485cab4c954c0316 ts=2026-09-23T13:24:19.4600000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[442] _id=6ab3d38f485cab4c954c18bc ts=2026-09-23T13:26:39.1860000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[11] _id=6ab27bb1485cab4c95479d0a ts=2026-09-22T12:59:29.4380000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[20] _id=6ab3ce39485cab4c954b8486 ts=2026-09-23T13:03:53.4850000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[745] _id=6ab3d686485cab4c954ca78f ts=2026-09-23T13:39:18.8170000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 39 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 39} 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[8] _id=6ab27bb1485cab4c95479d08 ts=2026-09-22T12:59:29.4370000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[7] _id=6ab27c01485cab4c95479d40 ts=2026-09-22T13:00:49.3580000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[19] _id=6ab3ce39485cab4c954b8482 ts=2026-09-23T13:03:53.4850000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[17] _id=6ab27bff485cab4c95479d3e ts=2026-09-22T13:00:47.5440000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[18] _id=6ab27c07485cab4c95479d42 ts=2026-09-22T13:00:55.6760000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[22] _id=6ab3cfff485cab4c954b8daa ts=2026-09-23T13:11:27.7060000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5835 | 0.0 | 0.533 | 197.203 | 8.963 | 343092.808 | 0.3 | 331 | 11 |
| PuzzlePieceVisibleEvent | 2941 | 0.0 | 0.033 | 331.928 | 1.216 | 432120.936 | 0.18 | 1722 | 5 |
| DialogueEvent | 2119 | 0.0 | 4.038 | 543.025 | 33.489 | 343112.173 | 0.11 | 624 | 11 |
| PlayerPositionEvent | 2042 | 6.105 | 10.0 | 522.37 | 10.17 | 342993.688 | 0.11 | 0 | 10 |
| argumentationNodeEvent | 677 | 0.014 | 0.344 | 1568.04 | 6.809 | 518426.456 | 0.04 | 160 | 5 |
| ObjectInterEvent | 218 | 0.0 | 12.87 | 4877.386 | 479.382 | 432000.207 | 0.01 | 5 | 9 |
| TopographicMapEvent | 108 | 0.011 | 2.522 | 5621.326 | 823.303 | 346014.979 | 0.01 | 2 | 7 |
| questEvent | 82 | 0.001 | 202.183 | 14029.544 | 85217.729 | 343092.576 | 0.0 | 13 | 15 |
| Soil Key Puzzle | 55 | 0.143 | 1.162 | 17292.107 | 51992.278 | 431997.224 | 0.0 | 0 | 3 |
| argumentationAnswerEvent | 48 | 0.141 | 14.496 | 22114.663 | 7620.385 | 689513.625 | 0.0 | 0 | 5 |
| DaniEvent | 39 | 0.003 | 2.268 | 11092.821 | 9473.036 | 345976.232 | 0.01 | 6 | 3 |
| gameWindowFocusEvent | 38 | 0.249 | 693.168 | 30254.995 | 112530.398 | 342981.75 | 0.0 | 0 | 20 |
| gameWindowUnfocusEvent | 27 | 0.0 | 839.093 | 42578.211 | 208339.51 | 354725.847 | 0.0 | 1 | 16 |
| DEBUGMenu | 25 | 126.015 | 1204.569 | 45941.202 | 225136.691 | 343389.587 | 0.0 | 0 | 16 |
| WaterChamberEvent | 25 | 0.45 | 15.182 | 22.634 | 58.994 | 87.374 | 2.65 | 0 | 0 |
| gameStartEvent | 20 | 125.896 | 6101.109 | 57427.329 | 263866.818 | 345710.35 | 0.0 | 0 | 13 |
| chatEvent | 18 | 0.382 | 4.657 | 54158.794 | 375669.215 | 541315.871 | 0.0 | 0 | 4 |
| argumentationEvent | 12 | 0.021 | 54.048 | 88459.518 | 506514.758 | 689471.755 | 0.0 | 2 | 4 |
| soilMachine | 11 | 0.374 | 7.099 | 39.602 | 138.677 | 165.687 | 1.52 | 0 | 0 |
| TerasGardenBox | 5 | 1.599 | 2.324 | 9.918 | 23.416 | 24.414 | 6.05 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 3 | 2189.791 | 24706.542 | 354007.527 | 934084.278 | 1035126.249 | 0.0 | 0 | 3 |
| SolarStillDesignEvent | 3 | 1.702 | 2.851 | 3.334 | 5.188 | 5.448 | 18.0 | 0 | 0 |
| argumentationToolEvent | 1 | 1.738 | 1.738 | 1.738 | 1.738 | 1.738 | 34.52 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[12102] _id=6ac3f9a0de269131f9af73c7 ts=2026-10-05T19:25:20.0850000Z == 6aa413b141b41dbac0c7f1f5.jsonl[12103] _id=6ac3f9a0de269131f9af73c9 ts=2026-10-05T19:25:20.0850000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[12120] _id=6ac3f9a0de269131f9af73cb ts=2026-10-05T19:25:20.0860000Z == 6aa413b141b41dbac0c7f1f5.jsonl[12127] _id=6ac3f9a1de269131f9af73cd ts=2026-10-05T19:25:20.0860000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[13925] _id=6ac406acde269131f9af9a31 ts=2026-10-05T20:20:59.2630000Z == 6aa413b141b41dbac0c7f1f5.jsonl[13931] _id=6ac406acde269131f9af9a33 ts=2026-10-05T20:20:59.2630000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[11820] _id=6ac3cb1cde269131f9ad9099 ts=2026-10-05T16:06:53.2400000Z == 6aa413b141b41dbac0c7f1f5.jsonl[11821] _id=6ac3cb1cde269131f9ad909b ts=2026-10-05T16:06:53.2400000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[12166] _id=6ac3f9dcde269131f9af7455 ts=2026-10-05T19:26:19.8130000Z == 6aa413b141b41dbac0c7f1f5.jsonl[12162] _id=6ac3f9dcde269131f9af7457 ts=2026-10-05T19:26:19.8130000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 121 group(s), 166 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[936] _id=6ab51eb0485cab4c954fe81b ts=2026-09-24T12:59:27.1590000Z == 6aa413b141b41dbac0c7f1f5.jsonl[941] _id=6ab51eb0485cab4c954fe81d ts=2026-09-24T12:59:27.1590000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[948] _id=6ab51eb0485cab4c954fe821 ts=2026-09-24T12:59:27.2970000Z == 6aa413b141b41dbac0c7f1f5.jsonl[949] _id=6ab51eb0485cab4c954fe825 ts=2026-09-24T12:59:27.2970000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[963] _id=6ab51eb1485cab4c954fe871 ts=2026-09-24T12:59:27.5950000Z == 6aa413b141b41dbac0c7f1f5.jsonl[772] _id=6ab51eb1485cab4c954fe877 ts=2026-09-24T12:59:27.5950000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[6878] _id=6abd079e485cab4c95867611 ts=? == 6aa413b141b41dbac0c7f1f5.jsonl[6902] _id=6abd081c485cab4c95867d7d ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6aa413b141b41dbac0c7f1f5.jsonl[197] _id=6ab3d150485cab4c954bc2d4 ts=2026-09-23T13:17:04.5250000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[196] _id=6ab3d150485cab4c954bc2da ts=2026-09-23T13:17:04.5340000Z`; `565ms: 6aa413b141b41dbac0c7f1f5.jsonl[9470] _id=6abe5e28485cab4c95a4e267 ts=2026-10-01T13:20:40.2340000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[9432] _id=6abe5e28485cab4c95a4e2d2 ts=2026-10-01T13:20:40.7990000Z`; `185ms: 6aa413b141b41dbac0c7f1f5.jsonl[9432] _id=6abe5e28485cab4c95a4e2d2 ts=2026-10-01T13:20:40.7990000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[9465] _id=6abe5e29485cab4c95a4e30a ts=2026-10-01T13:20:40.9840000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 512 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa413b141b41dbac0c7f1f5.jsonl[998] _id=6ab51ebc485cab4c954fea49 ts=2026-09-24T12:58:17.2700000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[982] _id=6ab51ebc485cab4c954fea4f ts=2026-09-24T12:58:17.2870000Z`; `48ms: 6aa413b141b41dbac0c7f1f5.jsonl[1021] _id=6ab51ebd485cab4c954feaa7 ts=2026-09-24T12:58:17.9250000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[1017] _id=6ab51ebd485cab4c954feaa9 ts=2026-09-24T12:58:17.9730000Z`; `26ms: 6aa413b141b41dbac0c7f1f5.jsonl[1018] _id=6ab51ebd485cab4c954feabd ts=2026-09-24T12:58:18.0500000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[1019] _id=6ab51ebd485cab4c954feabf ts=2026-09-24T12:58:18.0760000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `310ms: 6aa413b141b41dbac0c7f1f5.jsonl[9211] _id=6abe5cd8485cab4c95a48f29 ts=2026-10-01T13:15:03.2450000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[9220] _id=6abe5cd8485cab4c95a48f38 ts=2026-10-01T13:15:03.5550000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 6aa413b141b41dbac0c7f1f5.jsonl[2870] _id=6ab52214485cab4c955040ae ts=2026-09-24T13:13:56.8500000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[2850] _id=6ab52215485cab4c955040c7 ts=2026-09-24T13:13:56.8610000Z`; `336ms: 6aa413b141b41dbac0c7f1f5.jsonl[2847] _id=6ab52218485cab4c955041d8 ts=2026-09-24T13:14:00.4950000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[2862] _id=6ab52218485cab4c955041f5 ts=2026-09-24T13:14:00.8310000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `932ms: 6aa413b141b41dbac0c7f1f5.jsonl[13563] _id=6ac40390de269131f9af91eb ts=2026-10-05T20:07:44.5630000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[13570] _id=6ac40391de269131f9af91f5 ts=2026-10-05T20:07:45.4950000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `937ms: 6aa413b141b41dbac0c7f1f5.jsonl[12570] _id=6ac3fbf3de269131f9af7c25 ts=2026-10-05T19:35:15.0640000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[12624] _id=6ac3fbf4de269131f9af7c2b ts=2026-10-05T19:35:16.0010000Z`; `591ms: 6aa413b141b41dbac0c7f1f5.jsonl[12624] _id=6ac3fbf4de269131f9af7c2b ts=2026-10-05T19:35:16.0010000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[12629] _id=6ac3fbf5de269131f9af7c31 ts=2026-10-05T19:35:16.5920000Z`; `692ms: 6aa413b141b41dbac0c7f1f5.jsonl[12629] _id=6ac3fbf5de269131f9af7c31 ts=2026-10-05T19:35:16.5920000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[12625] _id=6ac3fbf5de269131f9af7c35 ts=2026-10-05T19:35:17.2840000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `38ms: 6aa413b141b41dbac0c7f1f5.jsonl[8796] _id=6abe5af3485cab4c95a43ad1 ts=2026-10-01T13:06:58.9890000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[8791] _id=6abe5af3485cab4c95a43ae5 ts=2026-10-01T13:06:59.0270000Z`; `21ms: 6aa413b141b41dbac0c7f1f5.jsonl[12887] _id=6ac3fceede269131f9af81a5 ts=2026-10-05T19:39:25.4610000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[12889] _id=6ac3fceede269131f9af81ab ts=2026-10-05T19:39:25.4820000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 134 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `408ms: 6aa413b141b41dbac0c7f1f5.jsonl[551] _id=6ab3d517485cab4c954c721b ts=2026-09-23T13:33:11.6720000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[548] _id=6ab3d518485cab4c954c723a ts=2026-09-23T13:33:12.0800000Z`; `395ms: 6aa413b141b41dbac0c7f1f5.jsonl[547] _id=6ab3d517485cab4c954c7225 ts=2026-09-23T13:33:11.7430000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[553] _id=6ab3d518485cab4c954c7243 ts=2026-09-23T13:33:12.1380000Z`; `672ms: 6aa413b141b41dbac0c7f1f5.jsonl[548] _id=6ab3d518485cab4c954c723a ts=2026-09-23T13:33:12.0800000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[556] _id=6ab3d518485cab4c954c727d ts=2026-09-23T13:33:12.7520000Z`
- **INFO / Info** `chatEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `775ms: 6aa413b141b41dbac0c7f1f5.jsonl[3163] _id=6ab525cc485cab4c95511271 ts=2026-09-24T13:29:48.5260000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[3242] _id=6ab525cd485cab4c9551127e ts=2026-09-24T13:29:49.3010000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `249ms: 6aa413b141b41dbac0c7f1f5.jsonl[420] _id=6ab3d34b485cab4c954c0b5e ts=2026-09-23T13:25:31.5460000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[422] _id=6ab3d34b485cab4c954c0b6a ts=2026-09-23T13:25:31.7950000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `437ms: 6aa413b141b41dbac0c7f1f5.jsonl[417] _id=6ab3d34b485cab4c954c0b58 ts=2026-09-23T13:25:31.2150000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[421] _id=6ab3d34b485cab4c954c0b62 ts=2026-09-23T13:25:31.6520000Z`; `178ms: 6aa413b141b41dbac0c7f1f5.jsonl[421] _id=6ab3d34b485cab4c954c0b62 ts=2026-09-23T13:25:31.6520000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[418] _id=6ab3d34b485cab4c954c0b71 ts=2026-09-23T13:25:31.8300000Z`; `0ms: 6aa413b141b41dbac0c7f1f5.jsonl[6895] _id=6abd07ee485cab4c95867a69 ts=2026-09-30T13:00:30.3710000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[6898] _id=6abd080c485cab4c95867c29 ts=2026-09-30T13:00:30.371Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6aa413b141b41dbac0c7f1f5.jsonl[14166] _id=6ac40814de269131f9af9d91 ts=2026-10-05T20:27:00.4650000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[14150] _id=6ac40815de269131f9af9d93 ts=2026-10-05T20:27:00.4660000Z`; `4ms: 6aa413b141b41dbac0c7f1f5.jsonl[14301] _id=6ac4096bde269131f9af9f09 ts=2026-10-05T20:32:43.1630000Z ~ 6aa413b141b41dbac0c7f1f5.jsonl[14292] _id=6ac4096bde269131f9af9f0b ts=2026-10-05T20:32:43.1670000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa413b141b41dbac0c7f1f5.jsonl[9846] _id=6abe6163485cab4c95a60897 ts=2026-10-01T13:34:27.3890000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10037] _id=6ac39ec1de269131f9a83d54 ts=2026-10-05T12:57:36.9760000Z; 72h 7m: 6aa413b141b41dbac0c7f1f5.jsonl[4472] _id=6ab676dc485cab4c9554f5a6 ts=2026-09-25T13:27:56.6560000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4531] _id=6aba6d0f485cab4c95680a62 ts=2026-09-28T13:35:21.7040000Z; 24h 11m: 6aa413b141b41dbac0c7f1f5.jsonl[9] _id=6ab27bc8485cab4c95479d16 ts=2026-09-22T12:59:52.7100000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[24] _id=6ab3d007485cab4c954b8e22 ts=2026-09-23T13:11:35.9720000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa413b141b41dbac0c7f1f5.jsonl[4429] _id=6ab6760a485cab4c9554d38a ts=2026-09-25T13:24:27.2860000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[6011] _id=6abbbd83485cab4c957d2770 ts=2026-09-29T13:30:43.5180000Z; 23h 35m: 6aa413b141b41dbac0c7f1f5.jsonl[3239] _id=6ab525c7485cab4c955111b9 ts=2026-09-24T13:29:43.7470000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[3403] _id=6ab671a2485cab4c95546921 ts=2026-09-25T13:05:41.8290000Z; 18m 5s: 6aa413b141b41dbac0c7f1f5.jsonl[3417] _id=6ab671b9485cab4c955469bb ts=2026-09-25T13:06:04.3810000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4417] _id=6ab675f9485cab4c9554d142 ts=2026-09-25T13:24:10.1900000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 6aa413b141b41dbac0c7f1f5.jsonl[4344] _id=6ab67607485cab4c9554d33e ts=2026-09-25T13:24:24.1610000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4428] _id=6ab67607485cab4c9554d344 ts=2026-09-25T13:24:24.1640000Z; 6ms: 6aa413b141b41dbac0c7f1f5.jsonl[3408] _id=6ab671b8485cab4c955469b0 ts=2026-09-25T13:06:02.9460000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[3416] _id=6ab671b8485cab4c955469b5 ts=2026-09-25T13:06:02.9520000Z; 6ms: 6aa413b141b41dbac0c7f1f5.jsonl[4425] _id=6ab67602485cab4c9554d260 ts=2026-09-25T13:24:18.8670000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4426] _id=6ab67602485cab4c9554d266 ts=2026-09-25T13:24:18.8730000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1f5.jsonl[10018] _id=6abe62a7485cab4c95a66ee1 ts=2026-10-01T13:39:51.4240000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10058] _id=6ac39eefde269131f9a83e3e ts=2026-10-05T12:58:23.5970000Z; 72h 7m: 6aa413b141b41dbac0c7f1f5.jsonl[4469] _id=6ab676e3485cab4c9554f6e8 ts=2026-09-25T13:28:04.0660000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4535] _id=6aba6d16485cab4c95680a83 ts=2026-09-28T13:35:27.8250000Z; 24h 11m: 6aa413b141b41dbac0c7f1f5.jsonl[15] _id=6ab27be9485cab4c95479d36 ts=2026-09-22T13:00:25.7280000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[28] _id=6ab3d01e485cab4c954b8fca ts=2026-09-23T13:11:58.2980000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 624 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[12723] _id=6ac3fc7bde269131f9af7fab ts=2026-10-05T19:37:31.0560000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12724] _id=6ac3fc7bde269131f9af7fad ts=2026-10-05T19:37:31.0560000Z; 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[14115] _id=6ac407bbde269131f9af9cbf ts=2026-10-05T20:25:30.8310000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[14116] _id=6ac407bbde269131f9af9cc1 ts=2026-10-05T20:25:30.8310000Z; 1ms: 6aa413b141b41dbac0c7f1f5.jsonl[11970] _id=6ac3ccebde269131f9ada025 ts=2026-10-05T16:14:35.4130000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11971] _id=6ac3ccebde269131f9ada027 ts=2026-10-05T16:14:35.4140000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 287h 32m 
  - Evidence: 287h 32m: 6aa413b141b41dbac0c7f1f5.jsonl[744] _id=6ab3d630485cab4c954c993b ts=2026-09-23T13:37:52.1170000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10232] _id=6ac3a1a6de269131f9a86030 ts=2026-10-05T13:09:58.3660000Z; 6h 51m: 6aa413b141b41dbac0c7f1f5.jsonl[10232] _id=6ac3a1a6de269131f9a86030 ts=2026-10-05T13:09:58.3660000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[13306] _id=6ac40229de269131f9af8aef ts=2026-10-05T20:01:44.9080000Z; 36m 29s: 6aa413b141b41dbac0c7f1f5.jsonl[13306] _id=6ac40229de269131f9af8aef ts=2026-10-05T20:01:44.9080000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[14377] _id=6ac40ab7de269131f9afa075 ts=2026-10-05T20:38:14.6990000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1f5.jsonl[10011] _id=6abe6291485cab4c95a665c9 ts=2026-10-01T13:39:29.0570000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10039] _id=6ac39ec7de269131f9a83d94 ts=2026-10-05T12:57:41.8650000Z; 72h 6m: 6aa413b141b41dbac0c7f1f5.jsonl[4521] _id=6ab67729485cab4c9555038c ts=2026-09-25T13:29:13.6260000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4538] _id=6aba6d1e485cab4c95680acb ts=2026-09-28T13:35:35.9710000Z; 24h 14m: 6aa413b141b41dbac0c7f1f5.jsonl[14] _id=6ab27bde485cab4c95479d28 ts=2026-09-22T13:00:14.5770000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[57] _id=6ab3d0be485cab4c954ba3c8 ts=2026-09-23T13:14:38.8100000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 331 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[12102] _id=6ac3f9a0de269131f9af73c7 ts=2026-10-05T19:25:20.0850000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12103] _id=6ac3f9a0de269131f9af73c9 ts=2026-10-05T19:25:20.0850000Z; 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[12120] _id=6ac3f9a0de269131f9af73cb ts=2026-10-05T19:25:20.0860000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12127] _id=6ac3f9a1de269131f9af73cd ts=2026-10-05T19:25:20.0860000Z; 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[13925] _id=6ac406acde269131f9af9a31 ts=2026-10-05T20:20:59.2630000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[13931] _id=6ac406acde269131f9af9a33 ts=2026-10-05T20:20:59.2630000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6aa413b141b41dbac0c7f1f5.jsonl[2650] _id=6ab5204c485cab4c9550176d ts=2026-09-24T13:06:20.7390000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4678] _id=6abbb7cd485cab4c957c21ee ts=2026-09-29T13:06:20.9460000Z; 95h 19m: 6aa413b141b41dbac0c7f1f5.jsonl[9991] _id=6abe6270485cab4c95a658c3 ts=2026-10-01T13:38:56.3780000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10070] _id=6ac39eefde269131f9a83e3b ts=2026-10-05T12:58:23.5570000Z; 24h 4m: 6aa413b141b41dbac0c7f1f5.jsonl[5508] _id=6abbb904485cab4c957c3f54 ts=2026-09-29T13:11:32.6160000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[7069] _id=6abd0b77485cab4c9586bccb ts=2026-09-30T13:15:35.7020000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[11820] _id=6ac3cb1cde269131f9ad9099 ts=2026-10-05T16:06:53.2400000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11821] _id=6ac3cb1cde269131f9ad909b ts=2026-10-05T16:06:53.2400000Z; 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[12166] _id=6ac3f9dcde269131f9af7455 ts=2026-10-05T19:26:19.8130000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12162] _id=6ac3f9dcde269131f9af7457 ts=2026-10-05T19:26:19.8130000Z; 1ms: 6aa413b141b41dbac0c7f1f5.jsonl[11843] _id=6ac3cb66de269131f9ad9271 ts=2026-10-05T16:08:06.4590000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11866] _id=6ac3cb66de269131f9ad9273 ts=2026-10-05T16:08:06.4600000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa413b141b41dbac0c7f1f5.jsonl[10020] _id=6abe62ef485cab4c95a67e48 ts=2026-10-01T13:41:03.2940000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10038] _id=6ac39ec7de269131f9a83d92 ts=2026-10-05T12:57:36.9820000Z; 72h 5m: 6aa413b141b41dbac0c7f1f5.jsonl[4527] _id=6ab6775f485cab4c95550b8f ts=2026-09-25T13:30:07.7400000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4534] _id=6aba6d16485cab4c95680a81 ts=2026-09-28T13:35:21.7110000Z; 24h 10m: 6aa413b141b41dbac0c7f1f5.jsonl[6] _id=6ab27bfe485cab4c95479d3c ts=2026-09-22T13:00:46.3590000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[27] _id=6ab3d00d485cab4c954b8e7c ts=2026-09-23T13:11:35.9810000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 2m 
  - Evidence: 120h 2m: 6aa413b141b41dbac0c7f1f5.jsonl[2601] _id=6ab52011485cab4c95501455 ts=2026-09-24T13:05:19.4760000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4706] _id=6abbb808485cab4c957c23ea ts=2026-09-29T13:07:20.4120000Z; 96h 0m: 6aa413b141b41dbac0c7f1f5.jsonl[9374] _id=6abe5d6b485cab4c95a4a471 ts=2026-10-01T13:17:27.6360000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10345] _id=6ac3a369de269131f9a88d92 ts=2026-10-05T13:17:28.9760000Z; 48h 1m: 6aa413b141b41dbac0c7f1f5.jsonl[5618] _id=6abbb9c6485cab4c957c5714 ts=2026-09-29T13:14:45.2400000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[9260] _id=6abe5d22485cab4c95a49933 ts=2026-10-01T13:16:17.2650000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1722 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[1004] _id=6ab51ebd485cab4c954feaa1 ts=2026-09-24T12:58:17.8050000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[1016] _id=6ab51ebd485cab4c954feaa3 ts=2026-09-24T12:58:17.8050000Z; 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[1010] _id=6ab51ebd485cab4c954fea87 ts=2026-09-24T12:58:17.7330000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[1011] _id=6ab51ebd485cab4c954fea8b ts=2026-09-24T12:58:17.7330000Z; 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[1013] _id=6ab51ebd485cab4c954fea97 ts=2026-09-24T12:58:17.8050000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[1014] _id=6ab51ebd485cab4c954fea9b ts=2026-09-24T12:58:17.8050000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6aa413b141b41dbac0c7f1f5.jsonl[2646] _id=6ab5204f485cab4c95501785 ts=2026-09-24T13:06:23.7150000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4677] _id=6abbb7cc485cab4c957c21ec ts=2026-09-29T13:06:20.9390000Z; 96h 1m: 6aa413b141b41dbac0c7f1f5.jsonl[9213] _id=6abe5cf5485cab4c95a492ed ts=2026-10-01T13:15:33.2370000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10293] _id=6ac3a356de269131f9a88c1a ts=2026-10-05T13:17:10.1320000Z; 48h 8m: 6aa413b141b41dbac0c7f1f5.jsonl[4691] _id=6abbb7eb485cab4c957c22fe ts=2026-09-29T13:06:51.4570000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[9196] _id=6abe5ccf485cab4c95a48e13 ts=2026-10-01T13:14:55.1840000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa413b141b41dbac0c7f1f5.jsonl[4222] _id=6ab67452485cab4c95549c8d ts=2026-09-25T13:17:06.5930000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[5833] _id=6abbbbf1485cab4c957cd369 ts=2026-09-29T13:24:01.5720000Z; 24h 4m: 6aa413b141b41dbac0c7f1f5.jsonl[8086] _id=6abd0f49485cab4c95883b5f ts=2026-09-30T13:31:52.9400000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[9894] _id=6abe61d0485cab4c95a6288f ts=2026-10-01T13:36:16.3200000Z; 23h 46m: 6aa413b141b41dbac0c7f1f5.jsonl[3230] _id=6ab525b1485cab4c95510e71 ts=2026-09-24T13:29:21.0940000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4187] _id=6ab67417485cab4c955494dd ts=2026-09-25T13:16:07.2120000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.011s..0.027s shown 
  - Evidence: 11ms: 6aa413b141b41dbac0c7f1f5.jsonl[2870] _id=6ab52214485cab4c955040ae ts=2026-09-24T13:13:56.8500000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[2850] _id=6ab52215485cab4c955040c7 ts=2026-09-24T13:13:56.8610000Z; 27ms: 6aa413b141b41dbac0c7f1f5.jsonl[2869] _id=6ab52214485cab4c955040a9 ts=2026-09-24T13:13:56.8230000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[2870] _id=6ab52214485cab4c955040ae ts=2026-09-24T13:13:56.8500000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 31m 
  - Evidence: 191h 31m: 6aa413b141b41dbac0c7f1f5.jsonl[637] _id=6ab3d589485cab4c954c8577 ts=2026-09-23T13:35:05.3400000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[8795] _id=6abe5af2485cab4c95a43acf ts=2026-10-01T13:06:58.9650000Z; 99h 7m: 6aa413b141b41dbac0c7f1f5.jsonl[8795] _id=6abe5af2485cab4c95a43acf ts=2026-10-01T13:06:58.9650000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11969] _id=6ac3ccebde269131f9ada021 ts=2026-10-05T16:14:35.3960000Z; 2h 50m: 6aa413b141b41dbac0c7f1f5.jsonl[12045] _id=6ac3d2e1de269131f9adea5f ts=2026-10-05T16:40:01.8260000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12339] _id=6ac3fae4de269131f9af772d ts=2026-10-05T19:30:44.4040000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 31m 
  - Evidence: 191h 31m: 6aa413b141b41dbac0c7f1f5.jsonl[638] _id=6ab3d589485cab4c954c857b ts=2026-09-23T13:35:05.3760000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[8741] _id=6abe5ac9485cab4c95a43525 ts=2026-10-01T13:06:17.1310000Z; 99h 7m: 6aa413b141b41dbac0c7f1f5.jsonl[8791] _id=6abe5af3485cab4c95a43ae5 ts=2026-10-01T13:06:59.0270000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11934] _id=6ac3ccc9de269131f9ad9f29 ts=2026-10-05T16:14:01.6970000Z; 3h 15m: 6aa413b141b41dbac0c7f1f5.jsonl[11934] _id=6ac3ccc9de269131f9ad9f29 ts=2026-10-05T16:14:01.6970000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12284] _id=6ac3faa8de269131f9af75dd ts=2026-10-05T19:29:43.9980000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.038s shown 
  - Evidence: 21ms: 6aa413b141b41dbac0c7f1f5.jsonl[12887] _id=6ac3fceede269131f9af81a5 ts=2026-10-05T19:39:25.4610000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12889] _id=6ac3fceede269131f9af81ab ts=2026-10-05T19:39:25.4820000Z; 38ms: 6aa413b141b41dbac0c7f1f5.jsonl[8796] _id=6abe5af3485cab4c95a43ad1 ts=2026-10-01T13:06:58.9890000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[8791] _id=6abe5af3485cab4c95a43ae5 ts=2026-10-01T13:06:59.0270000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 0m 
  - Evidence: 144h 0m: 6aa413b141b41dbac0c7f1f5.jsonl[3375] _id=6ab671af485cab4c95546989 ts=2026-09-25T13:05:54.3790000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[8736] _id=6abe5acc485cab4c95a435c1 ts=2026-10-01T13:06:20.8350000Z; 99h 7m: 6aa413b141b41dbac0c7f1f5.jsonl[8787] _id=6abe5aef485cab4c95a43a55 ts=2026-10-01T13:06:54.9950000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11923] _id=6ac3cccdde269131f9ad9f45 ts=2026-10-05T16:14:05.2500000Z; 47h 30m: 6aa413b141b41dbac0c7f1f5.jsonl[627] _id=6ab3d583485cab4c954c849f ts=2026-09-23T13:34:59.2610000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[3409] _id=6ab671ac485cab4c95546963 ts=2026-09-25T13:05:51.6640000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 160 interval(s) ≤ 0.014s..0.015s shown 
  - Evidence: 14ms: 6aa413b141b41dbac0c7f1f5.jsonl[12432] _id=6ac3fb3cde269131f9af7893 ts=2026-10-05T19:32:12.3920000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12422] _id=6ac3fb3dde269131f9af7895 ts=2026-10-05T19:32:12.4060000Z; 15ms: 6aa413b141b41dbac0c7f1f5.jsonl[12436] _id=6ac3fb46de269131f9af78af ts=2026-10-05T19:32:22.3900000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12434] _id=6ac3fb46de269131f9af78b1 ts=2026-10-05T19:32:22.4050000Z; 15ms: 6aa413b141b41dbac0c7f1f5.jsonl[12459] _id=6ac3fb58de269131f9af78fb ts=2026-10-05T19:32:39.9600000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[12468] _id=6ac3fb58de269131f9af78fd ts=2026-10-05T19:32:39.9750000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 150h 21m 
  - Evidence: 150h 21m: 6aa413b141b41dbac0c7f1f5.jsonl[6759] _id=6abbbfb6485cab4c957d968c ts=2026-09-29T13:40:06.7750000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[13310] _id=6ac4023bde269131f9af8b69 ts=2026-10-05T20:02:02.6460000Z; 96h 13m: 6aa413b141b41dbac0c7f1f5.jsonl[4424] _id=6ab67601485cab4c9554d228 ts=2026-09-25T13:24:17.3580000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[6628] _id=6abbbf46485cab4c957d8232 ts=2026-09-29T13:38:14.8100000Z; 23h 54m: 6aa413b141b41dbac0c7f1f5.jsonl[3164] _id=6ab525cf485cab4c955112c3 ts=2026-09-24T13:29:51.0220000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4420] _id=6ab675fd485cab4c9554d1b4 ts=2026-09-25T13:24:13.6210000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa413b141b41dbac0c7f1f5.jsonl[8486] _id=6abe5848485cab4c95a3ff8f ts=2026-10-01T12:55:35.2700000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10030] _id=6ac39eb5de269131f9a83d32 ts=2026-10-05T12:57:25.6200000Z; 72h 5m: 6aa413b141b41dbac0c7f1f5.jsonl[4471] _id=6ab676cf485cab4c9554f3f4 ts=2026-09-25T13:27:43.3270000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4529] _id=6aba6cae485cab4c956806b9 ts=2026-09-28T13:33:42.5910000Z; 24h 8m: 6aa413b141b41dbac0c7f1f5.jsonl[749] _id=6ab51d9f485cab4c954fc301 ts=2026-09-24T12:54:56.0730000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[3258] _id=6ab67127485cab4c95545f2b ts=2026-09-25T13:03:37.2050000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 16m 
  - Evidence: 95h 16m: 6aa413b141b41dbac0c7f1f5.jsonl[10022] _id=6abe62f0485cab4c95a67e6a ts=2026-10-01T13:41:03.8690000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10036] _id=6ac39eb5de269131f9a83d2e ts=2026-10-05T12:57:25.6190000Z; 72h 5m: 6aa413b141b41dbac0c7f1f5.jsonl[4470] _id=6ab676cf485cab4c9554f3ee ts=2026-09-25T13:27:43.3260000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4528] _id=6aba6cac485cab4c956806b1 ts=2026-09-28T13:33:42.5910000Z; 24h 3m: 6aa413b141b41dbac0c7f1f5.jsonl[7] _id=6ab27c01485cab4c95479d40 ts=2026-09-22T13:00:49.3580000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[19] _id=6ab3ce39485cab4c954b8482 ts=2026-09-23T13:03:53.4850000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 98h 32m 
  - Evidence: 98h 32m: 6aa413b141b41dbac0c7f1f5.jsonl[10021] _id=6abe62ef485cab4c95a67e5b ts=2026-10-01T13:41:03.8600000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[11920] _id=6ac3cc95de269131f9ad9da2 ts=2026-10-05T16:13:09.7070000Z; 72h 18m: 6aa413b141b41dbac0c7f1f5.jsonl[4247] _id=6ab67520485cab4c9554b562 ts=2026-09-25T13:20:32.5050000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4567] _id=6aba6e02485cab4c956814a1 ts=2026-09-28T13:39:20.9350000Z; 24h 10m: 6aa413b141b41dbac0c7f1f5.jsonl[18] _id=6ab27c07485cab4c95479d42 ts=2026-09-22T13:00:55.6760000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[22] _id=6ab3cfff485cab4c954b8daa ts=2026-09-23T13:11:27.7060000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f5.jsonl[6895] _id=6abd07ee485cab4c95867a69 ts=2026-09-30T13:00:30.3710000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[6898] _id=6abd080c485cab4c95867c29 ts=2026-09-30T13:00:30.371Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1f5.jsonl[9994] _id=6abe6292485cab4c95a66661 ts=2026-10-01T13:39:30.6260000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[10049] _id=6ac39ec8de269131f9a83da4 ts=2026-10-05T12:57:43.2020000Z; 72h 7m: 6aa413b141b41dbac0c7f1f5.jsonl[4476] _id=6ab676dd485cab4c9554f5ec ts=2026-09-25T13:27:57.5600000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[4530] _id=6aba6d16485cab4c95680a89 ts=2026-09-28T13:35:27.8640000Z; 24h 11m: 6aa413b141b41dbac0c7f1f5.jsonl[2] _id=6ab27bdf485cab4c95479d2a ts=2026-09-22T13:00:15.1070000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[30] _id=6ab3d01e485cab4c954b8fc6 ts=2026-09-23T13:11:58.2780000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f5.jsonl[13612] _id=6ac403ddde269131f9af93cf ts=2026-10-05T20:09:00.8350000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[13613] _id=6ac403ddde269131f9af93d1 ts=2026-10-05T20:09:00.8360000Z; 1ms: 6aa413b141b41dbac0c7f1f5.jsonl[14166] _id=6ac40814de269131f9af9d91 ts=2026-10-05T20:27:00.4650000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[14150] _id=6ac40815de269131f9af9d93 ts=2026-10-05T20:27:00.4660000Z; 1ms: 6aa413b141b41dbac0c7f1f5.jsonl[529] _id=6ab3d4ee485cab4c954c6a05 ts=2026-09-23T13:32:29.9760000Z -> 6aa413b141b41dbac0c7f1f5.jsonl[516] _id=6ab3d4ee485cab4c954c6a09 ts=2026-09-23T13:32:29.9770000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[644] _id=6ab3d59d485cab4c954c876d ts=2026-09-23T13:35:25.5250000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[2961] _id=6ab5233b485cab4c95508087 ts=2026-09-24T13:18:51.8950000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[5635] _id=6abbb9c3485cab4c957c565a ts=2026-09-29T13:14:43.5600000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 91 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[1244] _id=6ab51eec485cab4c954ff0a7 ts=2026-09-24T13:00:27.0840000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1268] _id=6ab51ef0485cab4c954ff145 ts=2026-09-24T13:00:31.1480000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1304] _id=6ab51f04485cab4c954ff4a7 ts=2026-09-24T13:00:52.0250000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 198 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[982] _id=6ab51ebc485cab4c954fea4f ts=2026-09-24T12:58:17.2870000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1017] _id=6ab51ebd485cab4c954feaa9 ts=2026-09-24T12:58:17.9730000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[976] _id=6ab51eb3485cab4c954fe8b5 ts=2026-09-24T12:59:28.2220000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[8791] _id=6abe5af3485cab4c95a43ae5 ts=2026-10-01T13:06:59.0270000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 41 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[576] _id=6ab3d549485cab4c954c7cad ts=2026-09-23T13:34:01.3240000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[580] _id=6ab3d54b485cab4c954c7cf3 ts=2026-09-23T13:34:03.2180000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[564] _id=6ab3d54c485cab4c954c7d27 ts=2026-09-23T13:34:04.0430000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[13859] _id=6ac405d2de269131f9af9991 ts=2026-10-05T20:17:22.3040000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[26] _id=6ab3d00d485cab4c954b8e7a ts=?`; `6aa413b141b41dbac0c7f1f5.jsonl[4278] _id=6ab674d8485cab4c9554ae95 ts=?`; `6aa413b141b41dbac0c7f1f5.jsonl[6878] _id=6abd079e485cab4c95867611 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 436 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[1087] _id=6ab51ed7485cab4c954fed98 ts=2026-09-24T13:00:02.9970000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1115] _id=6ab51ed7485cab4c954fed9b ts=2026-09-24T13:00:03.0160000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1133] _id=6ab51ed7485cab4c954feda1 ts=2026-09-24T13:00:03.0300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 568 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[984] _id=6ab51ebc485cab4c954fea6b ts=2026-09-24T12:58:17.5200000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1014] _id=6ab51ebd485cab4c954fea9b ts=2026-09-24T12:58:17.8050000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[1023] _id=6ab51ebd485cab4c954feab6 ts=2026-09-24T12:58:18.0270000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 46 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[2870] _id=6ab52214485cab4c955040ae ts=2026-09-24T13:13:56.8500000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[2850] _id=6ab52215485cab4c955040c7 ts=2026-09-24T13:13:56.8610000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[2934] _id=6ab522c5485cab4c9550664d ts=2026-09-24T13:16:53.9110000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[12284] _id=6ac3faa8de269131f9af75dd ts=2026-10-05T19:29:43.9980000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 47 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[12437] _id=6ac3fb47de269131f9af78b3 ts=2026-10-05T19:32:23.4520000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[12440] _id=6ac3fb4dde269131f9af78bf ts=2026-10-05T19:32:29.0320000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[12443] _id=6ac3fb4dde269131f9af78c9 ts=2026-10-05T19:32:29.3210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `chatEvent` `actionType` — chat open/close: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[4420] _id=6ab675fd485cab4c9554d1b4 ts=2026-09-25T13:24:13.6210000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[6628] _id=6abbbf46485cab4c957d8232 ts=2026-09-29T13:38:14.8100000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[6673] _id=6abbbf7f485cab4c957d8aa0 ts=2026-09-29T13:39:11.1560000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 399 start, 392 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 169 unmatched 'BecameCameraCentered' (totals: 609 open, 531 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 90 unmatched 'BecameVisible' (totals: 847 open, 955 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 48 open, 46 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationNodeHoverStart' (totals: 279 open, 316 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 52 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 247 of 14385 adjacent _id pairs reverse in client time; worst 82.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f5.jsonl[980] _id=6ab51eba485cab4c954fe9bd ts=2026-09-24T12:59:38.0360000Z`; `6aa413b141b41dbac0c7f1f5.jsonl[987] _id=6ab51eba485cab4c954fe9e1 ts=2026-09-24T12:58:15.9280000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -83.92s, max +20.89s over 14386 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1f5\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 5836 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2647); Unit 3 Dev (1671); Unit 4 Dev - Dungeon (358); Unit 1 Dev (273); Unit 4 Dev (232); Unit 3 Dungeon Dev (229); Unit 5 Dev - Dungeon (180); Unit 4 Dev - Anderson Base (147); Unit 5 Dev (99)
- **Intervals:** median 0.53s (p5 0.05s / p95 8.96s, n=5835)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5836/5836 records)
    "pressed"  x5836
data.actionType  (string, 5836/5836 records)
    "Move"  x4141
    "Interact"  x859
    "Jump"  x462
    "Sprint"  x180
    "Hoverboard"  x73
    "Ascend"  x38
    "Map"  x38
    "ToggleDebug"  x18
    "Descend"  x13
    "SkipCinematic"  x10
    "Pause"  x4
data.key  (string, 5836/5836 records, 63 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5836/5836 records)
    "Player"  x4549
    "Drone"  x1287
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2942 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2176); Unit 4 Dev (478); Unit 5 Dev - Dungeon (172); Unit 3 Dungeon Dev (116)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.22s, n=2941)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2942/2942 records)
    "BecameInvisible"  x955
    "BecameVisible"  x847
    "BecameCameraCentered"  x609
    "BecameCameraUncentered"  x531
data.pieceId  (string, 2942/2942 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2942/2942 records)
    1863 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2120 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (489); Unit 3 Dev (412); Unit 4 Dev (258); Unit 4 Dev - Anderson Base (233); Unit 5 Dev (222); Unit 1 Dev (196); Unit 3 Dungeon Dev (133); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (78)
- **eventKey:** present on 1329 of 2120 records
- **Intervals:** median 4.04s (p5 0.00s / p95 33.49s, n=2119)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1329; [conversationId, dialogueEventType] x791
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2120/2120 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2120/2120 records)
    "DialogueNodeEvent"  x1329
    "DialogueStartEvent"  x399
    "DialogueFinishEvent"  x392
data.nodeId  (number, 1329/2120 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2054 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (606); Unit 3 Dev (424); Unit 4 Dev (245); Unit 4 Dev - Anderson Base (173); Unit 1 Dev (162); Unit 5 Dev (124); Unit 4 Dev - Dungeon (120); Unit 3 Dungeon Dev (108); Unit 5 Dev - Dungeon (92)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.17s, n=2042)
- **Fields under `data`:**

```text
data.position  (object, 2054/2054 records)
data.position.x  (number, 2054/2054 records)
    numeric range -719.247 .. 1867.44 (702 unique)
data.position.y  (number, 2054/2054 records)
    numeric range -114.326 .. 222.405 (535 unique)
data.position.z  (number, 2054/2054 records)
    numeric range -1124.64 .. 2122.54 (701 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 678 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (503); Unit 1 Dev (60); Unit 5 Dev (56); Unit 3 Dev (49); Unit 2 Prod (Refactor) (10)
- **Intervals:** median 0.34s (p5 0.02s / p95 6.81s, n=677)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 678/678 records)
    "argumentationNodeHoverEnd"  x316
    "argumentationNodeHoverStart"  x279
    "argumentationNodeAdd"  x51
    "argumentationNodeRemove"  x32
data.argumentationTitle  (string, 678/678 records)
    "Unit 4 - Flooding"  x503
    "Unit 5"  x56
    "Unit 3 - Pollution Upstream"  x49
    "Unit 1 - Freshwater"  x31
    "Unit 1 - Argumentation Tutorial"  x29
    "Unit 2 – Watershed"  x10
data.nodeName  (string, 678/678 records)
    "C"  x121
    "B"  x105
    "A"  x102
    "2"  x70
    "D"  x60
    "4"  x53
    "II"  x50
    "I"  x47
    "3"  x35
    "1"  x30
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 219 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (61); Unit 2 Prod (Refactor) (44); Unit 3 Dungeon Dev (32); Unit 4 Dev (19); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (16); Unit 5 Dev (11); Unit 1 Dev (10); Unit 5 Dev - Dungeon (8)
- **Intervals:** median 12.87s (p5 0.56s / p95 479.38s, n=218)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 219/219 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 219/219 records)
    95 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 109 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (75); Unit 3 Dev (34)
- **Intervals:** median 2.52s (p5 0.65s / p95 823.30s, n=108)
- **`data` key-set variants:** [actionType, featureUsed] x94; [actionType, featureUsed, location] x15
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 109/109 records)
    "MapOpenEvent"  x48
    "MapCloseEvent"  x46
    "WaypointMoveEvent"  x13
    "WaypointSetEvent"  x2
data.featureUsed  (string, 109/109 records)
    "Map"  x94
    "Waypoint"  x15
data.location  (object, 15/109 records)
data.location.x  (number, 15/109 records)
    numeric range -562.718 .. 142.91 (13 unique)
data.location.y  (number, 15/109 records)
    12 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 15/109 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 83 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (19); Unit 3 Dev (14); Unit 1 Dev (13); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 83 of 83 records
- **Intervals:** median 202.18s (p5 0.00s / p95 85217.73s, n=82)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Fields under `data`:**

```text
data.questEventType  (string, 83/83 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x31
data.questID  (string, 83/83 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 83/83 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/83 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 56 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (30); Unit 2 Prod (Refactor) (16); Unit 4 Dev (10)
- **Intervals:** median 1.16s (p5 0.18s / p95 51992.28s, n=55)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x48; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/56 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/56 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 48/56 records)
    "RightDrag"  x27
    "LeftDrag"  x21
data.currentSoilType  (string, 48/56 records)
    "CLAY"  x11
    "CLAYSAND"  x10
    "CLAYROCK"  x8
    "SAND"  x7
    "SANDGRAVEL"  x7
    "BEDROCK"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 48/56 records)
    "false"  x36
    "true"  x12
data.waterLevelStatus  (string, 48/56 records)
    "TooHigh"  x26
    "Proper"  x16
    "TooLow"  x6
data.waterRetentionChange  (string, 48/56 records)
    "Decrease"  x19
    "Increase"  x17
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 49 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (42); Unit 1 Dev (3); Unit 5 Dev (3); Unit 3 Dev (1)
- **Intervals:** median 14.50s (p5 0.16s / p95 7620.38s, n=48)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "submitAnswerEvent"  x49
data.answerSubmitted  (string, 49/49 records)
    21 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 49/49 records)
    "Unit 4 - Flooding"  x42
    "Unit 5"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DaniEvent` — 40 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (40)
- **Intervals:** median 2.27s (p5 0.01s / p95 9473.04s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "Close"  x20
    "Open"  x20
data.toolName  (string, 40/40 records, 34 empty-string)
    ""  x34
    "Settings"  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowFocusEvent` — 39 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (21); Unit 2 Prod (Refactor) (6); Unit 1 Dev (4); Transition (2); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 693.17s (p5 4.92s / p95 112530.40s, n=38)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 39/39 records)
    true  x39
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 28 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 1 Dev (5); Unit 3 Dev (3); Transition (2); Unit 4 Dev - Anderson Base (2); MainMenu (1); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 839.09s (p5 0.26s / p95 208339.51s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 26 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 3 Dev (4); Unit 4 Dev (4); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1204.57s (p5 199.21s / p95 225136.69s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "DebugMenuStateChanged"  x26
data.isOpened  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 26 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (26)
- **Intervals:** median 15.18s (p5 0.64s / p95 58.99s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "On"  x19
    "Off"  x7
data.floor  (string, 26/26 records)
    "1"  x8
    "3"  x8
    "4"  x7
    "2"  x3
data.machineNumber  (string, 26/26 records)
    "One"  x25
    "Two"  x1
data.machineType  (string, 26/26 records)
    "Evaporator"  x12
    "Condenser"  x9
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 26/26 records)
    "2"  x14
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 6101.11s (p5 186.86s / p95 263866.82s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `chatEvent` — 19 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (17); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 4.66s (p5 0.39s / p95 375669.21s, n=18)
- **`data` key-set variants:** [actionType, chatID] x15; [actionKey, chatID] x4
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 4/19 records)
    "ScrollStop"  x4
data.actionType  (string, 15/19 records)
    "Close"  x6
    "Open"  x5
    "ScrollStart"  x4
data.chatID  (string, 19/19 records)
    "NA"  x10
    "[23-35, 23-36, 23-38, 23-40, 23-41]"  x4
    "[22-22, 22-46, 22-48, 22-27, 18-287, 18-289]"  x2
    "[18-287, 18-289]"  x1
    "[21-21, 21-22, 21-23, 21-24, 21-25]"  x1
    "[22-46, 22-48, 22-27, 18-287, 18-289]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationEvent` — 13 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 5 Dev (2)
- **Intervals:** median 54.05s (p5 0.03s / p95 506514.76s, n=12)
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

### `soilMachine` — 12 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (12)
- **Intervals:** median 7.10s (p5 0.85s / p95 138.68s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "ChangeCanister"  x12
data.canisterType  (string, 12/12 records)
    "Clay"  x4
    "Gravel"  x4
    "Sand"  x3
    "Bedrock"  x1
data.floor  (string, 12/12 records)
    "4"  x8
    "5"  x3
    "3"  x1
data.machine  (string, 12/12 records)
    "1"  x11
    "2"  x1
data.row  (string, 12/12 records)
    "TopRow"  x11
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.32s (p5 1.65s / p95 23.42s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "1"  x3
    "2"  x2
    "0"  x1
data.soilType  (string, 6/6 records)
    "Sand"  x3
    "Gravel"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "Permissions check failed"  x4
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 1 empty-string)
    "TypeError: Permissions check failed"  x4
    ""  x1
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit2"  x3
    "unit1"  x1
    "unit4"  x1
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 24706.54s (p5 4441.47s / p95 934084.28s, n=3)
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
- **Intervals:** median 2.85s (p5 1.82s / p95 5.19s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
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

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 1.74s (p5 1.74s / p95 1.74s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (16 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (13x); "WaypointSetEvent" (2x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (15x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (32x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*