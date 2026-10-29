# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f22c

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f22c
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f22c.jsonl
- **Records:** 14167 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f22c
- **Time span:** 2026-09-23T13:54:23.227000+00:00 .. 2026-10-07T15:32:56.254000+00:00 (337h 38m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f22c\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14167 records, 10 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 119 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4563 | 32.21 | 1 | 9 | 0 | 2026-09-23T13:54:37.771000+00:00 | 2026-10-07T15:32:56.254000+00:00 | 337h 38m |
| PuzzlePieceVisibleEvent | 2772 | 19.57 | 1 | 4 | 0 | 2026-09-24T13:52:08.235000+00:00 | 2026-10-07T14:23:45.521000+00:00 | 312h 31m |
| PlayerPositionEvent | 2542 | 17.94 | 1 | 9 | 0 | 2026-09-23T13:54:32.761000+00:00 | 2026-10-07T15:32:51.961000+00:00 | 337h 38m |
| DialogueEvent | 2371 | 16.74 | 1 | 9 | 1458 | 2026-09-23T13:54:54.700000+00:00 | 2026-10-07T15:32:44.531000+00:00 | 337h 37m |
| argumentationNodeEvent | 787 | 5.56 | 1 | 4 | 0 | 2026-09-23T14:27:46.422000+00:00 | 2026-10-07T15:02:42.332000+00:00 | 336h 34m |
| ObjectInterEvent | 349 | 2.46 | 1 | 9 | 0 | 2026-09-23T14:09:27.392000+00:00 | 2026-10-07T15:32:56.254000+00:00 | 337h 23m |
| TopographicMapEvent | 195 | 1.38 | 1 | 4 | 0 | 2026-09-24T13:47:02.562000+00:00 | 2026-10-05T14:11:10.537000+00:00 | 264h 24m |
| Soil Key Puzzle | 140 | 0.99 | 1 | 3 | 0 | 2026-09-24T13:57:37.830000+00:00 | 2026-10-01T14:25:48.481000+00:00 | 168h 28m |
| questEvent | 98 | 0.69 | 1 | 9 | 98 | 2026-09-23T13:54:54.680000+00:00 | 2026-10-07T15:28:09.965000+00:00 | 337h 33m |
| soilMachine | 79 | 0.56 | 1 | 1 | 0 | 2026-10-05T14:13:48.198000+00:00 | 2026-10-05T14:29:52.130000+00:00 | 16m 3s |
| WaterChamberEvent | 59 | 0.42 | 1 | 1 | 0 | 2026-10-07T14:19:50.406000+00:00 | 2026-10-07T14:53:30.991000+00:00 | 33m 40s |
| argumentationAnswerEvent | 40 | 0.28 | 1 | 4 | 0 | 2026-09-23T14:30:53.917000+00:00 | 2026-10-07T15:02:43.697000+00:00 | 336h 31m |
| DEBUGMenu | 28 | 0.2 | 1 | 9 | 0 | 2026-09-23T13:54:32.752000+00:00 | 2026-10-07T15:20:01.528000+00:00 | 337h 25m |
| gameWindowFocusEvent | 26 | 0.18 | 1 | 3 | 0 | 2026-09-23T13:54:23.227000+00:00 | 2026-10-07T15:20:01.975000+00:00 | 337h 25m |
| gameStartEvent | 20 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:54:23.227000+00:00 | 2026-10-07T15:20:01.975000+00:00 | 337h 25m |
| gameWindowUnfocusEvent | 19 | 0.13 | 1 | 7 | 0 | 2026-09-23T13:56:49.003000+00:00 | 2026-10-07T15:16:07.989000+00:00 | 337h 19m |
| SolarStillDesignEvent | 18 | 0.13 | 1 | 1 | 0 | 2026-10-07T15:09:15.791000+00:00 | 2026-10-07T15:25:50.639000+00:00 | 16m 34s |
| argumentationEvent | 15 | 0.11 | 1 | 4 | 0 | 2026-09-23T14:27:31.057000+00:00 | 2026-10-07T15:02:43.745000+00:00 | 336h 35m |
| argumentationToolEvent | 13 | 0.09 | 1 | 2 | 0 | 2026-09-23T14:27:23.443000+00:00 | 2026-09-30T14:07:05.265000+00:00 | 167h 39m |
| TerasGardenBox | 12 | 0.08 | 1 | 1 | 0 | 2026-10-06T14:18:44.209000+00:00 | 2026-10-06T14:20:07.515000+00:00 | 1m 23s |
| DaniEvent | 8 | 0.06 | 1 | 1 | 0 | 2026-09-25T13:56:39.772000+00:00 | 2026-09-25T14:30:18.127000+00:00 | 33m 38s |
| chatEvent | 5 | 0.04 | 1 | 2 | 0 | 2026-10-07T14:14:52.712000+00:00 | 2026-10-07T15:20:10.274000+00:00 | 1h 5m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-24T13:45:27.411000+00:00 | 2026-10-07T15:32:56.235000+00:00 | 313h 47m |
| crash | 4 | 0.03 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 432645.512s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.825s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.935s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.653s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 5.353s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1493.633s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 2519.218s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 1.516s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.7x vs baseline. 
  - Observed: 140 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.5x vs baseline. 
  - Observed: 18 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 240 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 8.0x vs baseline. 
  - Observed: 40 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,3,I; A,C,B,2,II; B,2,II; B,4,II; B,A,2,II; B,C,2,I; B,C,2,II; B,C,A,2,II; B,D,2,II; C,2,II; C,A,2,II; C,B,2,II; C,D,2,II; C,D,A,2,II; C,D,B,2,II; D,2,II; D,B,C,2,II; D,C,2,II; I 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.6x vs baseline. 
  - Observed: 787 records 
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
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 15.8x vs baseline. 
  - Observed: 79 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 44 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[256] _id=6ab3de20485cab4c954d00cb ts=2026-09-23T14:11:44.7560000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[302] _id=6ab3df1e485cab4c954d0921 ts=2026-09-23T14:15:58.0750000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[319] _id=6ab3df44485cab4c954d0b37 ts=2026-09-23T14:16:36.9640000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[30] _id=6ab3da0f485cab4c954ce2bb ts=2026-09-23T13:54:23.2270000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[89] _id=6ab3dc25485cab4c954cf19b ts=2026-09-23T14:03:17.3090000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[509] _id=6ab3e202485cab4c954d2b3d ts=2026-09-23T14:28:18.4860000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[18] _id=6ab3da0f485cab4c954ce2b9 ts=2026-09-23T13:54:23.2270000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[70] _id=6ab3daf6485cab4c954ce6a1 ts=2026-09-23T13:58:14.6930000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[88] _id=6ab3dc25485cab4c954cf199 ts=2026-09-23T14:03:17.3090000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[62] _id=6ab3daa0485cab4c954ce48b ts=2026-09-23T13:56:49.0030000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1] _id=6ab3db69485cab4c954ceab3 ts=2026-09-23T14:00:09.5740000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[104] _id=6ab3dc63485cab4c954cf3a7 ts=2026-09-23T14:04:19.3310000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 195 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[836] _id=6ab529d8485cab4c95518203 ts=2026-09-24T13:47:02.5620000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[837] _id=6ab529dd485cab4c955182c7 ts=2026-09-24T13:47:09.0620000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[838] _id=6ab529e1485cab4c95518365 ts=2026-09-24T13:47:13.8760000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4562 | 0.0 | 0.995 | 266.44 | 15.273 | 343063.437 | 0.23 | 213 | 12 |
| PuzzlePieceVisibleEvent | 2771 | 0.0 | 0.032 | 406.026 | 1.25 | 345780.942 | 0.15 | 1665 | 9 |
| PlayerPositionEvent | 2528 | 9.814 | 10.0 | 446.706 | 10.039 | 343033.616 | 0.13 | 0 | 8 |
| DialogueEvent | 2370 | 0.0 | 4.096 | 512.856 | 37.147 | 343054.73 | 0.12 | 708 | 10 |
| argumentationNodeEvent | 786 | 0.002 | 0.349 | 1541.598 | 6.67 | 519817.329 | 0.04 | 188 | 4 |
| ObjectInterEvent | 348 | 0.001 | 8.156 | 3490.255 | 458.105 | 345410.524 | 0.02 | 3 | 14 |
| TopographicMapEvent | 194 | 0.016 | 2.599 | 4906.433 | 498.57 | 345237.946 | 0.01 | 4 | 9 |
| Soil Key Puzzle | 139 | 0.125 | 0.465 | 4363.242 | 10.12 | 345407.543 | 0.01 | 0 | 3 |
| questEvent | 97 | 0.0 | 233.712 | 12527.786 | 84247.797 | 343082.801 | 0.0 | 20 | 20 |
| soilMachine | 78 | 0.098 | 1.516 | 12.358 | 44.21 | 232.785 | 4.86 | 0 | 0 |
| WaterChamberEvent | 58 | 0.169 | 8.935 | 34.838 | 79.059 | 662.078 | 1.72 | 0 | 1 |
| argumentationAnswerEvent | 39 | 1.901 | 20.653 | 31064.353 | 132178.81 | 519838.212 | 0.0 | 0 | 4 |
| DEBUGMenu | 27 | 6.311 | 1486.393 | 44989.955 | 207289.471 | 343133.746 | 0.0 | 0 | 19 |
| gameWindowFocusEvent | 25 | 1.131 | 1493.633 | 48589.55 | 222935.951 | 343683.193 | 0.0 | 0 | 15 |
| gameStartEvent | 19 | 104.637 | 2422.246 | 63933.618 | 267450.749 | 343683.192 | 0.0 | 0 | 14 |
| gameWindowUnfocusEvent | 18 | 0.0 | 2519.218 | 67464.388 | 270224.925 | 345640.443 | 0.0 | 1 | 12 |
| SolarStillDesignEvent | 17 | 0.734 | 1.449 | 58.52 | 199.589 | 965.463 | 1.03 | 0 | 1 |
| argumentationEvent | 14 | 0.025 | 84.942 | 86550.906 | 518644.129 | 519797.523 | 0.0 | 2 | 5 |
| argumentationToolEvent | 12 | 0.618 | 5.353 | 50298.485 | 279818.425 | 519857.458 | 0.0 | 0 | 2 |
| TerasGardenBox | 11 | 0.667 | 1.825 | 7.573 | 21.797 | 25.697 | 7.92 | 0 | 0 |
| DaniEvent | 7 | 0.007 | 1.725 | 288.336 | 1406.75 | 2007.628 | 0.21 | 2 | 1 |
| chatEvent | 4 | 580.741 | 895.126 | 979.39 | 1451.383 | 1546.569 | 0.06 | 0 | 3 |
| EndOfUnit | 3 | 90185.374 | 432645.512 | 376549.608 | 589400.695 | 606817.938 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 8 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[830] _id=6ab529d7485cab4c955181db ts=2026-09-24T13:47:02.5370000Z == 6aa4140b41b41dbac0c7f22c.jsonl[831] _id=6ab529d7485cab4c955181e1 ts=2026-09-24T13:47:02.5370000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[13071] _id=6ac659b7de269131f9bafb69 ts=2026-10-07T14:39:50.3780000Z == 6aa4140b41b41dbac0c7f22c.jsonl[13072] _id=6ac659b7de269131f9bafb6a ts=2026-10-07T14:39:50.3780000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[13889] _id=6ac66334de269131f9bb9c91 ts=2026-10-07T15:20:16.2270000Z == 6aa4140b41b41dbac0c7f22c.jsonl[13890] _id=6ac66334de269131f9bb9c92 ts=2026-10-07T15:20:16.2270000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 113 group(s), 138 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[989] _id=6ab52b0c485cab4c95519d03 ts=2026-09-24T13:52:12.2090000Z == 6aa4140b41b41dbac0c7f22c.jsonl[990] _id=6ab52b0c485cab4c95519d05 ts=2026-09-24T13:52:12.2090000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[994] _id=6ab52b0e485cab4c95519d3b ts=2026-09-24T13:52:13.0380000Z == 6aa4140b41b41dbac0c7f22c.jsonl[1005] _id=6ab52b0e485cab4c95519d3d ts=2026-09-24T13:52:13.0380000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1126] _id=6ab52b62485cab4c9551a0e9 ts=2026-09-24T13:52:26.4200000Z == 6aa4140b41b41dbac0c7f22c.jsonl[1127] _id=6ab52b62485cab4c9551a0eb ts=2026-09-24T13:52:26.4200000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[19] _id=6ab3da1d485cab4c954ce2cf ts=? == 6aa4140b41b41dbac0c7f22c.jsonl[93] _id=6ab3dc33485cab4c954cf212 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[13626] _id=6ac65f5ede269131f9bb700a ts=2026-10-07T15:03:58.5890000Z == 6aa4140b41b41dbac0c7f22c.jsonl[13627] _id=6ac65f5ede269131f9bb700b ts=2026-10-07T15:03:58.5890000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 38 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4140b41b41dbac0c7f22c.jsonl[222] _id=6ab3dd97485cab4c954cfdcd ts=2026-09-23T14:09:27.3920000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[226] _id=6ab3dd97485cab4c954cfdcf ts=2026-09-23T14:09:27.3950000Z`; `524ms: 6aa4140b41b41dbac0c7f22c.jsonl[4357] _id=6aba7326485cab4c95686863 ts=2026-09-28T14:01:10.7370000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[4350] _id=6aba7327485cab4c9568686b ts=2026-09-28T14:01:11.2610000Z`; `753ms: 6aa4140b41b41dbac0c7f22c.jsonl[7783] _id=6abe65df485cab4c95a735dd ts=2026-10-01T13:53:35.5560000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[7787] _id=6abe65e0485cab4c95a73611 ts=2026-10-01T13:53:36.3090000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 327 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `18ms: 6aa4140b41b41dbac0c7f22c.jsonl[992] _id=6ab52b0c485cab4c95519d0d ts=2026-09-24T13:52:12.3480000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[993] _id=6ab52b0c485cab4c95519d11 ts=2026-09-24T13:52:12.3660000Z`; `19ms: 6aa4140b41b41dbac0c7f22c.jsonl[1002] _id=6ab52b0e485cab4c95519d33 ts=2026-09-24T13:52:13.0050000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[1003] _id=6ab52b0e485cab4c95519d35 ts=2026-09-24T13:52:13.0240000Z`; `20ms: 6aa4140b41b41dbac0c7f22c.jsonl[1005] _id=6ab52b0e485cab4c95519d3d ts=2026-09-24T13:52:13.0380000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[995] _id=6ab52b0e485cab4c95519d41 ts=2026-09-24T13:52:13.0580000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `561ms: 6aa4140b41b41dbac0c7f22c.jsonl[3760] _id=6aba71b6485cab4c95684878 ts=2026-09-28T13:55:02.6450000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[3761] _id=6aba71b7485cab4c95684890 ts=2026-09-28T13:55:03.2060000Z`; `524ms: 6aa4140b41b41dbac0c7f22c.jsonl[3758] _id=6aba71b6485cab4c95684880 ts=2026-09-28T13:55:02.8770000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[3725] _id=6aba71b7485cab4c95684895 ts=2026-09-28T13:55:03.4010000Z`; `879ms: 6aa4140b41b41dbac0c7f22c.jsonl[3761] _id=6aba71b7485cab4c95684890 ts=2026-09-28T13:55:03.2060000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[3727] _id=6aba71b8485cab4c956848bb ts=2026-09-28T13:55:04.0850000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `774ms: 6aa4140b41b41dbac0c7f22c.jsonl[12070] _id=6ac50346de269131f9b2ad52 ts=2026-10-06T14:18:46.1660000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[12071] _id=6ac50346de269131f9b2ad7e ts=2026-10-06T14:18:46.9400000Z`; `667ms: 6aa4140b41b41dbac0c7f22c.jsonl[12071] _id=6ac50346de269131f9b2ad7e ts=2026-10-06T14:18:46.9400000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[12072] _id=6ac50347de269131f9b2adac ts=2026-10-06T14:18:47.6070000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6aa4140b41b41dbac0c7f22c.jsonl[2298] _id=6ab53005485cab4c9551e54b ts=2026-09-24T14:13:25.4690000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[2302] _id=6ab53005485cab4c9551e55b ts=2026-09-24T14:13:25.4880000Z`; `20ms: 6aa4140b41b41dbac0c7f22c.jsonl[2356] _id=6ab67d5b485cab4c9555a416 ts=2026-09-25T13:55:39.7520000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[2433] _id=6ab67d5b485cab4c9555a41e ts=2026-09-25T13:55:39.7720000Z`; `912ms: 6aa4140b41b41dbac0c7f22c.jsonl[2856] _id=6ab6818f485cab4c9555e8d0 ts=2026-09-25T14:13:35.2610000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[2858] _id=6ab6818f485cab4c9555e91d ts=2026-09-25T14:13:36.1730000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `389ms: 6aa4140b41b41dbac0c7f22c.jsonl[13133] _id=6ac65a1fde269131f9bb021e ts=2026-10-07T14:41:36.8420000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[13136] _id=6ac65a20de269131f9bb0225 ts=2026-10-07T14:41:37.2310000Z`; `869ms: 6aa4140b41b41dbac0c7f22c.jsonl[13134] _id=6ac65a20de269131f9bb0222 ts=2026-10-07T14:41:37.0110000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[13137] _id=6ac65a20de269131f9bb022f ts=2026-10-07T14:41:37.8800000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `25ms: 6aa4140b41b41dbac0c7f22c.jsonl[6576] _id=6abd17c1485cab4c958a5a0b ts=2026-09-30T14:08:01.5830000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[6609] _id=6abd17c3485cab4c958a5a66 ts=2026-09-30T14:08:01.6080000Z`; `26ms: 6aa4140b41b41dbac0c7f22c.jsonl[11900] _id=6ac5023ede269131f9b27d3e ts=2026-10-06T14:14:22.6170000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[11908] _id=6ac5023ede269131f9b27d48 ts=2026-10-06T14:14:22.6430000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 140 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `24ms: 6aa4140b41b41dbac0c7f22c.jsonl[490] _id=6ab3e1e3485cab4c954d2a37 ts=2026-09-23T14:27:47.4550000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[485] _id=6ab3e1e3485cab4c954d2a39 ts=2026-09-23T14:27:47.4790000Z`; `984ms: 6aa4140b41b41dbac0c7f22c.jsonl[487] _id=6ab3e1e6485cab4c954d2a55 ts=2026-09-23T14:27:50.2220000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[493] _id=6ab3e1e7485cab4c954d2a69 ts=2026-09-23T14:27:51.2060000Z`; `22ms: 6aa4140b41b41dbac0c7f22c.jsonl[494] _id=6ab3e1e7485cab4c954d2a6d ts=2026-09-23T14:27:51.6490000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[500] _id=6ab3e1e7485cab4c954d2a6f ts=2026-09-23T14:27:51.6710000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `752ms: 6aa4140b41b41dbac0c7f22c.jsonl[6487] _id=6abd1788485cab4c958a3d4e ts=2026-09-30T14:07:04.5130000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[6494] _id=6abd1789485cab4c958a3da2 ts=2026-09-30T14:07:05.2650000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4140b41b41dbac0c7f22c.jsonl[5012] _id=6abbc3d9485cab4c957e1a7f ts=2026-09-29T13:57:45.1170000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[5015] _id=6abbc3e8485cab4c957e1beb ts=2026-09-29T13:57:45.117Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4140b41b41dbac0c7f22c.jsonl[13790] _id=6ac66109de269131f9bb8e9d ts=2026-10-07T15:11:05.4610000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[13796] _id=6ac66109de269131f9bb8e9f ts=2026-10-07T15:11:05.4650000Z`; `3ms: 6aa4140b41b41dbac0c7f22c.jsonl[13896] _id=6ac66334de269131f9bb9c98 ts=2026-10-07T15:20:18.8110000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[13897] _id=6ac66334de269131f9bb9c99 ts=2026-10-07T15:20:18.8140000Z`; `3ms: 6aa4140b41b41dbac0c7f22c.jsonl[14041] _id=6ac664c2de269131f9bbc792 ts=2026-10-07T15:26:58.5960000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[14042] _id=6ac664c2de269131f9bbc794 ts=2026-10-07T15:26:58.5990000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 26 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `366ms: 6aa4140b41b41dbac0c7f22c.jsonl[9962] _id=6ac3b168de269131f9ab2ebe ts=2026-10-05T14:17:12.8350000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[9964] _id=6ac3b169de269131f9ab2ed4 ts=2026-10-05T14:17:13.2010000Z`; `265ms: 6aa4140b41b41dbac0c7f22c.jsonl[9964] _id=6ac3b169de269131f9ab2ed4 ts=2026-10-05T14:17:13.2010000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[9977] _id=6ac3b169de269131f9ab2ee7 ts=2026-10-05T14:17:13.4660000Z`; `269ms: 6aa4140b41b41dbac0c7f22c.jsonl[9977] _id=6ac3b169de269131f9ab2ee7 ts=2026-10-05T14:17:13.4660000Z ~ 6aa4140b41b41dbac0c7f22c.jsonl[9955] _id=6ac3b169de269131f9ab2efa ts=2026-10-05T14:17:13.7350000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f22c.jsonl[9032] _id=6abe6e11485cab4c95a88925 ts=2026-10-01T14:28:33.5150000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9081] _id=6ac3aa6fde269131f9a9c608 ts=2026-10-05T13:47:27.2610000Z; 71h 56m: 6aa4140b41b41dbac0c7f22c.jsonl[2361] _id=6ab67c77485cab4c95559c62 ts=2026-09-25T13:51:51.4860000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3543] _id=6aba7014485cab4c95681bc7 ts=2026-09-28T13:48:04.3850000Z; 24h 4m: 6aa4140b41b41dbac0c7f22c.jsonl[822] _id=6ab529d0485cab4c955180b7 ts=2026-09-24T13:46:56.6800000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2361] _id=6ab67c77485cab4c95559c62 ts=2026-09-25T13:51:51.4860000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 33m 27s 
  - Evidence: 33m 27s: 6aa4140b41b41dbac0c7f22c.jsonl[2451] _id=6ab67da1485cab4c9555a85a ts=2026-09-25T13:56:49.6070000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3531] _id=6ab68579485cab4c95564a82 ts=2026-09-25T14:30:17.2350000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.007s..0.011s shown 
  - Evidence: 7ms: 6aa4140b41b41dbac0c7f22c.jsonl[2442] _id=6ab67d9f485cab4c9555a81a ts=2026-09-25T13:56:47.8750000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2450] _id=6ab67d9f485cab4c9555a81e ts=2026-09-25T13:56:47.8820000Z; 11ms: 6aa4140b41b41dbac0c7f22c.jsonl[2448] _id=6ab67d9c485cab4c9555a7c8 ts=2026-09-25T13:56:44.4720000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2449] _id=6ab67d9c485cab4c9555a7ce ts=2026-09-25T13:56:44.4830000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[9067] _id=6abe6e75485cab4c95a89fc3 ts=2026-10-01T14:30:13.1270000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9080] _id=6ac3aa83de269131f9a9c7ee ts=2026-10-05T13:47:47.8570000Z; 71h 24m: 6aa4140b41b41dbac0c7f22c.jsonl[3170] _id=6ab683d0485cab4c95563412 ts=2026-09-25T14:23:12.3190000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3575] _id=6aba701d485cab4c95681c21 ts=2026-09-28T13:48:10.9760000Z; 23h 45m: 6aa4140b41b41dbac0c7f22c.jsonl[12284] _id=6ac505dede269131f9b32fac ts=2026-10-06T14:29:50.8810000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12313] _id=6ac653ecde269131f9ba8498 ts=2026-10-07T14:15:08.6030000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 708 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[13781] _id=6ac660f4de269131f9bb8dc2 ts=2026-10-07T15:10:44.3240000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13782] _id=6ac660f4de269131f9bb8dc3 ts=2026-10-07T15:10:44.3240000Z; 1ms: 6aa4140b41b41dbac0c7f22c.jsonl[11206] _id=6ac500b4de269131f9b258ed ts=2026-10-06T14:07:48.6200000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11207] _id=6ac500b4de269131f9b258f2 ts=2026-10-06T14:07:48.6210000Z; 1ms: 6aa4140b41b41dbac0c7f22c.jsonl[11230] _id=6ac500bfde269131f9b25988 ts=2026-10-06T14:07:59.0070000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11231] _id=6ac500bfde269131f9b2598a ts=2026-10-06T14:07:59.0080000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 168h 33m 
  - Evidence: 168h 33m: 6aa4140b41b41dbac0c7f22c.jsonl[810] _id=6ab52977485cab4c95517077 ts=2026-09-24T13:45:27.4110000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[8364] _id=6abe6bd9485cab4c95a7fcb7 ts=2026-10-01T14:19:05.3490000Z; 120h 10m: 6aa4140b41b41dbac0c7f22c.jsonl[8364] _id=6abe6bd9485cab4c95a7fcb7 ts=2026-10-01T14:19:05.3490000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12283] _id=6ac505dede269131f9b32fa8 ts=2026-10-06T14:29:50.8610000Z; 25h 3m: 6aa4140b41b41dbac0c7f22c.jsonl[12283] _id=6ac505dede269131f9b32fa8 ts=2026-10-06T14:29:50.8610000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[14164] _id=6ac66628de269131f9bbee47 ts=2026-10-07T15:32:56.2350000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[9060] _id=6abe6e5c485cab4c95a89adf ts=2026-10-01T14:29:48.7240000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9084] _id=6ac3aa74de269131f9a9c6a8 ts=2026-10-05T13:47:32.1610000Z; 71h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[3499] _id=6ab68586485cab4c95564ad4 ts=2026-09-25T14:30:31.0800000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3546] _id=6aba701b485cab4c95681be3 ts=2026-09-28T13:48:10.9090000Z; 23h 45m: 6aa4140b41b41dbac0c7f22c.jsonl[12277] _id=6ac505c8de269131f9b32bf4 ts=2026-10-06T14:29:28.0800000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12312] _id=6ac653ecde269131f9ba8492 ts=2026-10-07T14:15:08.5660000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 213 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[13071] _id=6ac659b7de269131f9bafb69 ts=2026-10-07T14:39:50.3780000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13072] _id=6ac659b7de269131f9bafb6a ts=2026-10-07T14:39:50.3780000Z; 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[13889] _id=6ac66334de269131f9bb9c91 ts=2026-10-07T15:20:16.2270000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13890] _id=6ac66334de269131f9bb9c92 ts=2026-10-07T15:20:16.2270000Z; 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[13890] _id=6ac66334de269131f9bb9c92 ts=2026-10-07T15:20:16.2270000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13891] _id=6ac66334de269131f9bb9c93 ts=2026-10-07T15:20:16.2270000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 6aa4140b41b41dbac0c7f22c.jsonl[2012] _id=6ab52c51485cab4c9551b6df ts=2026-09-24T13:57:37.8340000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3748] _id=6aba7194485cab4c956842e1 ts=2026-09-28T13:54:28.3580000Z; 95h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[9063] _id=6abe6e5e485cab4c95a89b7b ts=2026-10-01T14:29:50.7870000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9088] _id=6ac3aa83de269131f9a9c7f4 ts=2026-10-05T13:47:47.8710000Z; 24h 11m: 6aa4140b41b41dbac0c7f22c.jsonl[4516] _id=6aba7339485cab4c95686a4d ts=2026-09-28T14:01:29.5120000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[5252] _id=6abbc780485cab4c957e6d4d ts=2026-09-29T14:13:20.6310000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f22c.jsonl[11051] _id=6ac4fe63de269131f9b21baf ts=2026-10-06T13:57:55.6420000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11052] _id=6ac4fe64de269131f9b21bbf ts=2026-10-06T13:57:55.6430000Z; 1ms: 6aa4140b41b41dbac0c7f22c.jsonl[11110] _id=6ac4fea6de269131f9b22db9 ts=2026-10-06T13:59:02.0860000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11111] _id=6ac4fea6de269131f9b22dc0 ts=2026-10-06T13:59:02.0870000Z; 3ms: 6aa4140b41b41dbac0c7f22c.jsonl[222] _id=6ab3dd97485cab4c954cfdcd ts=2026-09-23T14:09:27.3920000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[226] _id=6ab3dd97485cab4c954cfdcf ts=2026-09-23T14:09:27.3950000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[9068] _id=6abe6e75485cab4c95a89fe9 ts=2026-10-01T14:30:13.6530000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9083] _id=6ac3aa74de269131f9a9c6a6 ts=2026-10-05T13:47:27.2690000Z; 71h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[3500] _id=6ab6858c485cab4c95564ae8 ts=2026-09-25T14:30:36.4330000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3563] _id=6aba701b485cab4c95681be1 ts=2026-09-28T13:48:04.3910000Z; 23h 36m: 6aa4140b41b41dbac0c7f22c.jsonl[2349] _id=6ab5307b485cab4c9551ee03 ts=2026-09-24T14:15:23.4820000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2370] _id=6ab67c78485cab4c95559c64 ts=2026-09-25T13:51:51.4940000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa4140b41b41dbac0c7f22c.jsonl[9009] _id=6abe6def485cab4c95a8834b ts=2026-10-01T14:27:56.7170000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[10569] _id=6ac3b4a1de269131f9abe9e0 ts=2026-10-05T14:30:57.6590000Z; 71h 43m: 6aa4140b41b41dbac0c7f22c.jsonl[2874] _id=6ab681b6485cab4c9555f018 ts=2026-09-25T14:14:14.4640000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3855] _id=6aba7244485cab4c95685ae5 ts=2026-09-28T13:57:23.8260000Z; 47h 57m: 6aa4140b41b41dbac0c7f22c.jsonl[4773] _id=6aba771a485cab4c9568bf02 ts=2026-09-28T14:17:58.9250000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6861] _id=6abd1972485cab4c958abbe6 ts=2026-09-30T14:15:13.2630000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1665 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[1003] _id=6ab52b0e485cab4c95519d35 ts=2026-09-24T13:52:13.0240000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[1004] _id=6ab52b0e485cab4c95519d39 ts=2026-09-24T13:52:13.0240000Z; 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[1017] _id=6ab52b5a485cab4c9551a00b ts=2026-09-24T13:52:09.1920000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[1018] _id=6ab52b5a485cab4c9551a00d ts=2026-09-24T13:52:09.1920000Z; 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[1019] _id=6ab52b5a485cab4c9551a00f ts=2026-09-24T13:52:09.2150000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[1044] _id=6ab52b5a485cab4c9551a011 ts=2026-09-24T13:52:09.2150000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 6aa4140b41b41dbac0c7f22c.jsonl[2013] _id=6ab52c54485cab4c9551b721 ts=2026-09-24T13:57:40.8110000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3747] _id=6aba7194485cab4c956842dd ts=2026-09-28T13:54:28.3540000Z; 48h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[3832] _id=6aba7221485cab4c9568589b ts=2026-09-28T13:56:49.0920000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6837] _id=6abd1935485cab4c958aaf18 ts=2026-09-30T14:14:13.0540000Z; 24h 10m: 6aa4140b41b41dbac0c7f22c.jsonl[6735] _id=6abd194a485cab4c958ab311 ts=2026-09-30T14:14:34.5930000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[8474] _id=6abe6d4f485cab4c95a85d81 ts=2026-10-01T14:25:19.3470000Z
- **INFO / Info** `SolarStillDesignEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 16m 5s 
  - Evidence: 16m 5s: 6aa4140b41b41dbac0c7f22c.jsonl[13723] _id=6ac660afde269131f9bb8a16 ts=2026-10-07T15:09:35.5110000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13991] _id=6ac66475de269131f9bbb969 ts=2026-10-07T15:25:40.9740000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 53m 
  - Evidence: 95h 53m: 6aa4140b41b41dbac0c7f22c.jsonl[8217] _id=6abe6961485cab4c95a7a1a1 ts=2026-10-01T14:08:33.1980000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9531] _id=6ac3adf7de269131f9aa7568 ts=2026-10-05T14:02:31.1440000Z; 71h 24m: 6aa4140b41b41dbac0c7f22c.jsonl[3210] _id=6ab68407485cab4c955636dc ts=2026-09-25T14:24:07.8440000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3587] _id=6aba7032485cab4c95681ce3 ts=2026-09-28T13:48:34.6930000Z; 24h 2m: 6aa4140b41b41dbac0c7f22c.jsonl[5927] _id=6abd144d485cab4c95895a4d ts=2026-09-30T13:53:17.4920000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[7873] _id=6abe666e485cab4c95a755e7 ts=2026-10-01T13:55:58.2530000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.016s..0.019s shown 
  - Evidence: 16ms: 6aa4140b41b41dbac0c7f22c.jsonl[2431] _id=6ab67d5b485cab4c9555a414 ts=2026-09-25T13:55:39.7360000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2356] _id=6ab67d5b485cab4c9555a416 ts=2026-09-25T13:55:39.7520000Z; 19ms: 6aa4140b41b41dbac0c7f22c.jsonl[2297] _id=6ab53005485cab4c9551e547 ts=2026-09-24T14:13:25.4500000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2298] _id=6ab53005485cab4c9551e54b ts=2026-09-24T14:13:25.4690000Z; 19ms: 6aa4140b41b41dbac0c7f22c.jsonl[2298] _id=6ab53005485cab4c9551e54b ts=2026-09-24T14:13:25.4690000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[2302] _id=6ab53005485cab4c9551e55b ts=2026-09-24T14:13:25.4880000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 11m 2s 
  - Evidence: 11m 2s: 6aa4140b41b41dbac0c7f22c.jsonl[13004] _id=6ac65735de269131f9badcfd ts=2026-10-07T14:29:09.7730000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13083] _id=6ac659cade269131f9bafc29 ts=2026-10-07T14:40:11.8510000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4140b41b41dbac0c7f22c.jsonl[599] _id=6ab528cc485cab4c95515933 ts=2026-09-24T13:42:36.5210000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6532] _id=6abd176a485cab4c958a2a91 ts=2026-09-30T14:06:34.7330000Z; 143h 54m: 6aa4140b41b41dbac0c7f22c.jsonl[6607] _id=6abd17c1485cab4c958a5a02 ts=2026-09-30T14:08:01.5620000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11308] _id=6ac4ff7fde269131f9b243bc ts=2026-10-06T14:02:39.6850000Z; 24h 48m: 6aa4140b41b41dbac0c7f22c.jsonl[11906] _id=6ac5023ede269131f9b27d3c ts=2026-10-06T14:14:22.5890000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13576] _id=6ac65f13de269131f9bb6839 ts=2026-10-07T15:02:43.6970000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4140b41b41dbac0c7f22c.jsonl[724] _id=6ab528cc485cab4c95515935 ts=2026-09-24T13:42:36.5430000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6512] _id=6abd1742485cab4c958a1358 ts=2026-09-30T14:05:54.0660000Z; 143h 53m: 6aa4140b41b41dbac0c7f22c.jsonl[6609] _id=6abd17c3485cab4c958a5a66 ts=2026-09-30T14:08:01.6080000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11268] _id=6ac4ff48de269131f9b240b4 ts=2026-10-06T14:01:44.6790000Z; 24h 47m: 6aa4140b41b41dbac0c7f22c.jsonl[11908] _id=6ac5023ede269131f9b27d48 ts=2026-10-06T14:14:22.6430000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13512] _id=6ac65eedde269131f9bb659e ts=2026-10-07T15:02:05.9180000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.025s..0.026s shown 
  - Evidence: 25ms: 6aa4140b41b41dbac0c7f22c.jsonl[6576] _id=6abd17c1485cab4c958a5a0b ts=2026-09-30T14:08:01.5830000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6609] _id=6abd17c3485cab4c958a5a66 ts=2026-09-30T14:08:01.6080000Z; 26ms: 6aa4140b41b41dbac0c7f22c.jsonl[11900] _id=6ac5023ede269131f9b27d3e ts=2026-10-06T14:14:22.6170000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11908] _id=6ac5023ede269131f9b27d48 ts=2026-10-06T14:14:22.6430000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4140b41b41dbac0c7f22c.jsonl[708] _id=6ab528c3485cab4c9551582b ts=2026-09-24T13:42:27.8080000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6516] _id=6abd174d485cab4c958a17b2 ts=2026-09-30T14:06:05.1370000Z; 143h 53m: 6aa4140b41b41dbac0c7f22c.jsonl[6608] _id=6abd17c0485cab4c958a596e ts=2026-09-30T14:08:00.1060000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11259] _id=6ac4ff44de269131f9b24082 ts=2026-10-06T14:01:40.8140000Z; 24h 47m: 6aa4140b41b41dbac0c7f22c.jsonl[11954] _id=6ac50238de269131f9b27cea ts=2026-10-06T14:14:16.6210000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13504] _id=6ac65eefde269131f9bb65ab ts=2026-10-07T15:02:07.1550000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 188 interval(s) ≤ 0.002s..0.002s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f22c.jsonl[11617] _id=6ac5007ade269131f9b25522 ts=2026-10-06T14:06:49.9980000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11611] _id=6ac5007ade269131f9b25524 ts=2026-10-06T14:06:50.0000000Z; 2ms: 6aa4140b41b41dbac0c7f22c.jsonl[11720] _id=6ac5013ede269131f9b26112 ts=2026-10-06T14:10:06.4930000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[11721] _id=6ac5013ede269131f9b26114 ts=2026-10-06T14:10:06.4950000Z; 2ms: 6aa4140b41b41dbac0c7f22c.jsonl[565] _id=6ab3e28e485cab4c954d3240 ts=2026-09-23T14:30:38.9880000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[561] _id=6ab3e28f485cab4c954d3242 ts=2026-09-23T14:30:38.9900000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 24m 
  - Evidence: 144h 24m: 6aa4140b41b41dbac0c7f22c.jsonl[684] _id=6ab528b3485cab4c9551567b ts=2026-09-24T13:42:11.4500000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[6519] _id=6abd1764485cab4c958a26a8 ts=2026-09-30T14:06:28.9080000Z; 23h 10m: 6aa4140b41b41dbac0c7f22c.jsonl[563] _id=6ab3e28b485cab4c954d321e ts=2026-09-23T14:30:36.0350000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[658] _id=6ab5286a485cab4c95514885 ts=2026-09-24T13:40:58.8870000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 25m 46s 
  - Evidence: 25m 46s: 6aa4140b41b41dbac0c7f22c.jsonl[13379] _id=6ac65d1fde269131f9bb3845 ts=2026-10-07T14:54:23.7050000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13878] _id=6ac6632ade269131f9bb9c13 ts=2026-10-07T15:20:10.2740000Z; 15m 11s: 6aa4140b41b41dbac0c7f22c.jsonl[12289] _id=6ac653dcde269131f9ba82a9 ts=2026-10-07T14:14:52.7120000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13034] _id=6ac6576cde269131f9badf98 ts=2026-10-07T14:30:04.7070000Z; 14m 38s: 6aa4140b41b41dbac0c7f22c.jsonl[13065] _id=6ac659b0de269131f9bafb32 ts=2026-10-07T14:39:45.4480000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13379] _id=6ac65d1fde269131f9bb3845 ts=2026-10-07T14:54:23.7050000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4140b41b41dbac0c7f22c.jsonl[8366] _id=6abe6be6485cab4c95a7ff5f ts=2026-10-01T14:19:18.4840000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9078] _id=6ac3aa69de269131f9a9c52a ts=2026-10-05T13:47:21.6760000Z; 71h 56m: 6aa4140b41b41dbac0c7f22c.jsonl[2369] _id=6ab67c68485cab4c95559c50 ts=2026-09-25T13:51:36.9670000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3552] _id=6aba700d485cab4c95681bb1 ts=2026-09-28T13:47:57.4440000Z; 24h 28m: 6aa4140b41b41dbac0c7f22c.jsonl[10587] _id=6ac4fb8ade269131f9b1539a ts=2026-10-06T13:45:46.4380000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12287] _id=6ac653d6de269131f9ba81ca ts=2026-10-07T14:14:46.0960000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 28m 
  - Evidence: 95h 28m: 6aa4140b41b41dbac0c7f22c.jsonl[8367] _id=6abe6be6485cab4c95a7ff59 ts=2026-10-01T14:19:18.4830000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9077] _id=6ac3aa69de269131f9a9c522 ts=2026-10-05T13:47:21.6760000Z; 71h 17m: 6aa4140b41b41dbac0c7f22c.jsonl[3538] _id=6ab68592485cab4c95564b16 ts=2026-09-25T14:30:42.4190000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3545] _id=6aba700d485cab4c95681bad ts=2026-09-28T13:47:57.4430000Z; 24h 28m: 6aa4140b41b41dbac0c7f22c.jsonl[10588] _id=6ac4fb8ade269131f9b15390 ts=2026-10-06T13:45:46.4370000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12286] _id=6ac653d6de269131f9ba81c9 ts=2026-10-07T14:14:46.0960000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 96h 0m 
  - Evidence: 96h 0m: 6aa4140b41b41dbac0c7f22c.jsonl[9069] _id=6abe6e7f485cab4c95a8a29b ts=2026-10-01T14:30:22.9670000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[10585] _id=6ac3b4a7de269131f9abea88 ts=2026-10-05T14:31:03.4100000Z; 71h 21m: 6aa4140b41b41dbac0c7f22c.jsonl[3540] _id=6ab68591485cab4c95564b0c ts=2026-09-25T14:30:41.2980000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3696] _id=6aba7125485cab4c956832b1 ts=2026-09-28T13:52:37.6020000Z; 48h 1m: 6aa4140b41b41dbac0c7f22c.jsonl[10585] _id=6ac3b4a7de269131f9abea88 ts=2026-10-05T14:31:03.4100000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13059] _id=6ac657e4de269131f9baea0c ts=2026-10-07T14:32:04.5790000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[5012] _id=6abbc3d9485cab4c957e1a7f ts=2026-09-29T13:57:45.1170000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[5015] _id=6abbc3e8485cab4c957e1beb ts=2026-09-29T13:57:45.117Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f22c.jsonl[9051] _id=6abe6e49485cab4c95a89546 ts=2026-10-01T14:29:29.3770000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[9082] _id=6ac3aa74de269131f9a9c6aa ts=2026-10-05T13:47:32.1780000Z; 71h 53m: 6aa4140b41b41dbac0c7f22c.jsonl[2424] _id=6ab67d28485cab4c9555a20e ts=2026-09-25T13:54:48.5640000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[3542] _id=6aba701d485cab4c95681c29 ts=2026-09-28T13:48:11.0100000Z; 23h 45m: 6aa4140b41b41dbac0c7f22c.jsonl[12280] _id=6ac505d4de269131f9b32e0d ts=2026-10-06T14:29:40.7540000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12290] _id=6ac653e2de269131f9ba8363 ts=2026-10-07T14:14:52.8220000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 20 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22c.jsonl[13626] _id=6ac65f5ede269131f9bb700a ts=2026-10-07T15:03:58.5890000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13627] _id=6ac65f5ede269131f9bb700b ts=2026-10-07T15:03:58.5890000Z; 1ms: 6aa4140b41b41dbac0c7f22c.jsonl[12768] _id=6ac65561de269131f9bab84f ts=2026-10-07T14:21:21.4450000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[12769] _id=6ac65561de269131f9bab850 ts=2026-10-07T14:21:21.4460000Z; 1ms: 6aa4140b41b41dbac0c7f22c.jsonl[13185] _id=6ac65ab2de269131f9bb0b5d ts=2026-10-07T14:44:02.8640000Z -> 6aa4140b41b41dbac0c7f22c.jsonl[13220] _id=6ac65ab2de269131f9bb0b5e ts=2026-10-07T14:44:02.8650000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[4726] _id=6aba76d2485cab4c9568b6c3 ts=2026-09-28T14:16:50.5780000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[4870] _id=6aba787a485cab4c9568d2ad ts=2026-09-28T14:23:54.7070000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[4972] _id=6aba7a57485cab4c9568f2a9 ts=2026-09-28T14:31:51.0680000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 121 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[1205] _id=6ab52b68485cab4c9551a181 ts=2026-09-24T13:53:43.3820000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1206] _id=6ab52b68485cab4c9551a183 ts=2026-09-24T13:53:43.4110000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1216] _id=6ab52b68485cab4c9551a185 ts=2026-09-24T13:53:43.4480000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 159 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[1091] _id=6ab52b5e485cab4c9551a08b ts=2026-09-24T13:52:10.8450000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1112] _id=6ab52b5f485cab4c9551a0a3 ts=2026-09-24T13:52:11.7480000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1098] _id=6ab52b5f485cab4c9551a0a5 ts=2026-09-24T13:52:11.8570000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[6609] _id=6abd17c3485cab4c958a5a66 ts=2026-09-30T14:08:01.6080000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[11908] _id=6ac5023ede269131f9b27d48 ts=2026-10-06T14:14:22.6430000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 27 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[485] _id=6ab3e1e3485cab4c954d2a39 ts=2026-09-23T14:27:47.4790000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[500] _id=6ab3e1e7485cab4c954d2a6f ts=2026-09-23T14:27:51.6710000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[576] _id=6ab3e296485cab4c954d32ca ts=2026-09-23T14:30:46.4880000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[12289] _id=6ac653dcde269131f9ba82a9 ts=2026-10-07T14:14:52.7120000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[13034] _id=6ac6576cde269131f9badf98 ts=2026-10-07T14:30:04.7070000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[13065] _id=6ac659b0de269131f9bafb32 ts=2026-10-07T14:39:45.4480000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[9466] _id=6ac3ae4ede269131f9aa8088 ts=2026-10-05T14:03:57.9960000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[13219] _id=6ac65ab2de269131f9bb0b57 ts=2026-10-07T14:44:02.8420000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[13184] _id=6ac65ab2de269131f9bb0b5c ts=2026-10-07T14:44:02.8550000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[19] _id=6ab3da1d485cab4c954ce2cf ts=?`; `6aa4140b41b41dbac0c7f22c.jsonl[93] _id=6ab3dc33485cab4c954cf212 ts=?`; `6aa4140b41b41dbac0c7f22c.jsonl[612] _id=6ab527fe485cab4c95513d68 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 296 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[1201] _id=6ab52b67485cab4c9551a173 ts=2026-09-24T13:53:43.1120000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1263] _id=6ab52b74485cab4c9551a231 ts=2026-09-24T13:53:54.9420000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1264] _id=6ab52b74485cab4c9551a233 ts=2026-09-24T13:53:55.0160000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 403 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[1016] _id=6ab52b5a485cab4c9551a007 ts=2026-09-24T13:52:09.1310000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1044] _id=6ab52b5a485cab4c9551a011 ts=2026-09-24T13:52:09.2150000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1020] _id=6ab52b5a485cab4c9551a015 ts=2026-09-24T13:52:09.5630000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 66 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[2298] _id=6ab53005485cab4c9551e54b ts=2026-09-24T14:13:25.4690000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[2302] _id=6ab53005485cab4c9551e55b ts=2026-09-24T14:13:25.4880000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[2429] _id=6ab67d4c485cab4c9555a366 ts=2026-09-25T13:55:24.1390000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[564] _id=6ab3e28c485cab4c954d3222 ts=2026-09-23T14:30:36.0830000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[660] _id=6ab5286c485cab4c955148d3 ts=2026-09-24T13:41:00.8160000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 100 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[561] _id=6ab3e28f485cab4c954d3242 ts=2026-09-23T14:30:38.9900000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[567] _id=6ab3e293485cab4c954d326e ts=2026-09-23T14:30:43.3000000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[554] _id=6ab3e298485cab4c954d32ee ts=2026-09-23T14:30:48.0730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[6523] _id=6abd1767485cab4c958a28b9 ts=2026-09-30T14:06:31.9160000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[6521] _id=6abd1769485cab4c958a2a05 ts=2026-09-30T14:06:33.7950000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[6487] _id=6abd1788485cab4c958a3d4e ts=2026-09-30T14:07:04.5130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 462 start, 451 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 100 unmatched 'BecameCameraCentered' (totals: 589 open, 610 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 84 unmatched 'BecameVisible' (totals: 749 open, 824 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'MapOpenEvent' (totals: 69 open, 65 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationNodeHoverStart' (totals: 344 open, 363 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationToolOpen' (totals: 10 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 58 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 214 of 14162 adjacent _id pairs reverse in client time; worst 82.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f22c.jsonl[1110] _id=6ab52b5e485cab4c9551a091 ts=2026-09-24T13:53:33.4920000Z`; `6aa4140b41b41dbac0c7f22c.jsonl[1092] _id=6ab52b5e485cab4c9551a093 ts=2026-09-24T13:52:10.8450000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.03s, min -84.59s, max +1.09s over 14163 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f22c\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4563 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1279); Unit 3 Dev (1014); Unit 4 Dev - Dungeon (837); Unit 3 Dungeon Dev (457); Unit 5 Dev - Dungeon (327); Unit 4 Dev (201); Unit 1 Dev (187); Unit 5 Dev (157); Unit 4 Dev - Anderson Base (104)
- **Intervals:** median 0.99s (p5 0.06s / p95 15.27s, n=4562)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4563/4563 records)
    "pressed"  x4563
data.actionType  (string, 4563/4563 records)
    "Move"  x2940
    "Jump"  x704
    "Interact"  x677
    "Map"  x84
    "Sprint"  x64
    "Hoverboard"  x50
    "Ascend"  x22
    "ToggleDebug"  x19
    "Pause"  x3
data.key  (string, 4563/4563 records, 45 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4563/4563 records)
    "Player"  x3878
    "Drone"  x685
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2772 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1564); Unit 4 Dev (632); Unit 5 Dev - Dungeon (358); Unit 3 Dungeon Dev (218)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.25s, n=2771)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2772/2772 records)
    "BecameInvisible"  x824
    "BecameVisible"  x749
    "BecameCameraUncentered"  x610
    "BecameCameraCentered"  x589
data.pieceId  (string, 2772/2772 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2772/2772 records)
    1813 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2542 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (670); Unit 3 Dev (454); Unit 4 Dev - Dungeon (269); Unit 1 Dev (239); Unit 5 Dev (214); Unit 4 Dev (204); Unit 3 Dungeon Dev (200); Unit 5 Dev - Dungeon (177); Unit 4 Dev - Anderson Base (115)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.04s, n=2528)
- **Fields under `data`:**

```text
data.position  (object, 2542/2542 records)
data.position.x  (number, 2542/2542 records)
    numeric range -684.245 .. 1969.61 (1005 unique)
data.position.y  (number, 2542/2542 records)
    numeric range -115.127 .. 535.691 (731 unique)
data.position.z  (number, 2542/2542 records)
    numeric range -1127.98 .. 2263.69 (1002 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2371 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (444); Unit 3 Dev (435); Unit 5 Dev (340); Unit 4 Dev (259); Unit 1 Dev (239); Unit 3 Dungeon Dev (230); Unit 4 Dev - Anderson Base (166); Unit 4 Dev - Dungeon (148); Unit 5 Dev - Dungeon (110)
- **eventKey:** present on 1458 of 2371 records
- **Intervals:** median 4.10s (p5 0.00s / p95 37.15s, n=2370)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1458; [conversationId, dialogueEventType] x913
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2371/2371 records)
    numeric range 8 .. 118 (54 unique)
data.dialogueEventType  (string, 2371/2371 records)
    "DialogueNodeEvent"  x1458
    "DialogueStartEvent"  x462
    "DialogueFinishEvent"  x451
data.nodeId  (number, 1458/2371 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 787 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (573); Unit 3 Dev (95); Unit 1 Dev (75); Unit 5 Dev (44)
- **Intervals:** median 0.35s (p5 0.02s / p95 6.67s, n=786)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 787/787 records)
    "argumentationNodeHoverEnd"  x363
    "argumentationNodeHoverStart"  x344
    "argumentationNodeAdd"  x47
    "argumentationNodeRemove"  x33
data.argumentationTitle  (string, 787/787 records)
    "Unit 4 - Flooding"  x573
    "Unit 3 - Pollution Upstream"  x95
    "Unit 1 - Argumentation Tutorial"  x52
    "Unit 5"  x44
    "Unit 1 - Freshwater"  x23
data.nodeName  (string, 787/787 records)
    "B"  x152
    "C"  x110
    "A"  x109
    "2"  x85
    "D"  x78
    "I"  x75
    "II"  x70
    "4"  x36
    "3"  x33
    "1"  x30
    "5"  x9
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 349 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (169); Unit 3 Dungeon Dev (70); Unit 2 Prod (Refactor) (28); Unit 4 Dev (18); Unit 5 Dev - Dungeon (16); Unit 5 Dev (15); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 8.16s (p5 0.31s / p95 458.11s, n=348)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 349/349 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 349/349 records)
    97 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 195 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (118); Unit 3 Dev (71); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (2)
- **Intervals:** median 2.60s (p5 0.49s / p95 498.57s, n=194)
- **`data` key-set variants:** [actionType, featureUsed] x134; [actionType, featureUsed, location] x60; [actionType, featureUsed, legendName] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 195/195 records)
    "MapOpenEvent"  x69
    "MapCloseEvent"  x65
    "WaypointMoveEvent"  x55
    "WaypointSetEvent"  x5
    "Selected"  x1
data.featureUsed  (string, 195/195 records)
    "Map"  x134
    "Waypoint"  x60
    "Legend"  x1
data.legendName  (string, 1/195 records)
    "240 ft"  x1
data.location  (object, 60/195 records)
data.location.x  (number, 60/195 records)
    numeric range -529.09 .. 605.741 (50 unique)
data.location.y  (number, 60/195 records)
    numeric range -289.098 .. 356.5 (48 unique)
data.location.z  (number, 60/195 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 140 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (72); Unit 4 Dev (44); Unit 3 Dev (24)
- **Intervals:** median 0.47s (p5 0.17s / p95 10.12s, n=139)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x132; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/140 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/140 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 132/140 records)
    "RightDrag"  x69
    "LeftDrag"  x63
data.currentSoilType  (string, 132/140 records)
    "CLAYSAND"  x25
    "SAND"  x24
    "CLAY"  x23
    "SANDGRAVEL"  x21
    "CLAYROCK"  x20
    "GRAVEL"  x10
    "BEDROCK"  x9
data.isCorrectSelection  (string, 132/140 records)
    "false"  x105
    "true"  x27
data.waterLevelStatus  (string, 132/140 records)
    "Proper"  x60
    "TooLow"  x40
    "TooHigh"  x32
data.waterRetentionChange  (string, 132/140 records)
    "Increase"  x58
    "Decrease"  x47
    "NoChange"  x27
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 98 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (19); Unit 2 Prod (Refactor) (16); Unit 3 Dev (12); Unit 4 Dev - Dungeon (12); Unit 5 Dev (12); Unit 5 Dev - Dungeon (12); Unit 4 Dev (9); Unit 3 Dungeon Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 98 of 98 records
- **Intervals:** median 233.71s (p5 0.00s / p95 84247.80s, n=97)
- **`data` key-set variants:** [questEventType, questID, questName] x58; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 98/98 records)
    "questActiveEvent"  x58
    "questFinishEvent"  x40
data.questID  (string, 98/98 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 98/98 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/98 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 79 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (79)
- **Intervals:** median 1.52s (p5 0.19s / p95 44.21s, n=78)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 79/79 records)
    "ChangeCanister"  x79
data.canisterType  (string, 79/79 records)
    "Bedrock"  x36
    "Clay"  x26
    "Gravel"  x15
    "Sand"  x2
data.floor  (string, 79/79 records)
    "5"  x57
    "4"  x21
    "3"  x1
data.machine  (string, 79/79 records)
    "1"  x78
    "2"  x1
data.row  (string, 79/79 records)
    "TopRow"  x48
    "BottomRow"  x31
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `WaterChamberEvent` — 59 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (59)
- **Intervals:** median 8.94s (p5 1.09s / p95 79.06s, n=58)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 59/59 records)
    "On"  x38
    "Off"  x21
data.floor  (string, 59/59 records)
    "3"  x29
    "4"  x24
    "2"  x4
    "1"  x2
data.machineNumber  (string, 59/59 records)
    "One"  x57
    "Two"  x2
data.machineType  (string, 59/59 records)
    "Condenser"  x24
    "Evaporator"  x15
    "DualChamber_Evaporator"  x9
    "DualChamber_Condenser"  x7
    "VentSwitch"  x4
data.room  (string, 59/59 records)
    "2"  x28
    "3"  x20
    "1"  x7
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 40 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (32); Unit 1 Dev (4); Unit 3 Dev (3); Unit 5 Dev (1)
- **Intervals:** median 20.65s (p5 2.33s / p95 132178.81s, n=39)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "submitAnswerEvent"  x40
data.answerSubmitted  (string, 40/40 records)
    22 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 40/40 records)
    "Unit 4 - Flooding"  x32
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 1 Dev (4); Unit 4 Dev (4); MainMenu (3); Unit 3 Dev (3); Unit 4 Dev - Dungeon (3); Unit 3 Dungeon Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 1486.39s (p5 36.70s / p95 207289.47s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 26 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (20); Unit 1 Dev (3); Unit 2 Prod (Refactor) (3)
- **Intervals:** median 1493.63s (p5 16.32s / p95 222935.95s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 2422.25s (p5 235.18s / p95 267450.75s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (5); Unit 5 Dev (2); Unit 3 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2519.22s (p5 2.86s / p95 270224.92s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `SolarStillDesignEvent` — 18 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (18)
- **Intervals:** median 1.45s (p5 0.80s / p95 199.59s, n=17)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x16; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "optionSelected"  x16
    "DesignSubmitted"  x2
data.designSelections  (object, 2/18 records)
data.designSelections.glassRoofTemperature  (string, 2/18 records)
    "Cold"  x1
    "Hot"  x1
data.designSelections.roofCovering  (string, 2/18 records)
    "Covered"  x1
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 2/18 records)
    "Tilted Out"  x2
data.featureUsed  (string, 18/18 records)
    "RoofStyle"  x10
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x3
    "Submit"  x2
data.selectedOption  (string, 16/18 records, 3 empty-string)
    "Tilted Out"  x4
    ""  x3
    "Tilted In"  x3
    "Cold"  x2
    "Covered"  x2
    "Hot"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 84.94s (p5 0.03s / p95 518644.13s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x5
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Argumentation Tutorial"  x5
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (6)
- **Intervals:** median 5.35s (p5 0.69s / p95 279818.42s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x10
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Argumentation Tutorial"  x6
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - Argumentation"  x6
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 12 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (12)
- **Intervals:** median 1.82s (p5 0.72s / p95 21.80s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records, 8 empty-string)
    ""  x8
    "cameraPlaced"  x4
data.boxId  (string, 12/12 records)
    "0"  x7
    "1"  x3
    "2"  x2
data.soilType  (string, 12/12 records)
    "Clay"  x8
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (8)
- **Intervals:** median 1.73s (p5 0.01s / p95 1406.75s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 6 empty-string)
    ""  x6
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 895.13s (p5 625.37s / p95 1451.38s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x5
data.chatID  (string, 5/5 records)
    "NA"  x5
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 432645.51s (p5 124431.39s / p95 589400.70s, n=3)
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

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x2
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x2
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit1"  x3
    "unit2"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

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
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (72 records)
- `TerasGardenBox` data.actionType: "" (8x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (55x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (60x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (33x)
- `soilMachine` data.canisterType: "Bedrock" (36x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*