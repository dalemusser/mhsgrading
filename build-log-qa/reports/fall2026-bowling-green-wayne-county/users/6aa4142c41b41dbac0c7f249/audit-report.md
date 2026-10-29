# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f249

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4142c41b41dbac0c7f249
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4142c41b41dbac0c7f249.jsonl
- **Records:** 13792 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4142c41b41dbac0c7f249
- **Time span:** 2026-09-23T16:29:31.168000+00:00 .. 2026-10-06T15:57:42.485000+00:00 (311h 28m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f249\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13792 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 109 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5211 | 37.78 | 1 | 4 | 0 | 2026-09-25T16:36:59.443000+00:00 | 2026-10-05T16:51:45.012000+00:00 | 240h 14m |
| InputEvent | 3263 | 23.66 | 1 | 9 | 0 | 2026-09-23T16:30:12.871000+00:00 | 2026-10-06T15:57:42.485000+00:00 | 311h 27m |
| DialogueEvent | 2200 | 15.95 | 1 | 9 | 1368 | 2026-09-23T16:30:14.967000+00:00 | 2026-10-06T15:57:31.301000+00:00 | 311h 27m |
| PlayerPositionEvent | 1911 | 13.86 | 1 | 9 | 0 | 2026-09-23T16:29:50.804000+00:00 | 2026-10-06T15:57:37.133000+00:00 | 311h 27m |
| argumentationNodeEvent | 449 | 3.26 | 1 | 4 | 0 | 2026-09-24T16:27:13.100000+00:00 | 2026-10-06T15:44:12.178000+00:00 | 287h 16m |
| ObjectInterEvent | 299 | 2.17 | 1 | 9 | 0 | 2026-09-23T16:49:24.501000+00:00 | 2026-10-06T15:57:42.482000+00:00 | 311h 8m |
| TopographicMapEvent | 87 | 0.63 | 1 | 2 | 0 | 2026-09-25T16:37:39.542000+00:00 | 2026-10-01T16:53:15.169000+00:00 | 144h 15m |
| questEvent | 83 | 0.6 | 1 | 9 | 83 | 2026-09-23T16:30:14.934000+00:00 | 2026-10-06T15:53:01.129000+00:00 | 311h 22m |
| Soil Key Puzzle | 64 | 0.46 | 1 | 3 | 0 | 2026-09-28T16:51:47.482000+00:00 | 2026-10-05T15:45:44.773000+00:00 | 166h 53m |
| argumentationAnswerEvent | 33 | 0.24 | 1 | 4 | 0 | 2026-09-24T16:29:37.374000+00:00 | 2026-10-06T15:44:13.521000+00:00 | 287h 14m |
| gameWindowFocusEvent | 31 | 0.22 | 1 | 5 | 0 | 2026-09-23T16:29:31.168000+00:00 | 2026-10-06T15:39:23.652000+00:00 | 311h 9m |
| WaterChamberEvent | 25 | 0.18 | 1 | 1 | 0 | 2026-10-05T16:50:30.090000+00:00 | 2026-10-05T17:01:16.120000+00:00 | 10m 46s |
| SolarStillDesignEvent | 23 | 0.17 | 1 | 1 | 0 | 2026-10-06T15:49:45.358000+00:00 | 2026-10-06T15:50:23.494000+00:00 | 38.1s |
| gameWindowUnfocusEvent | 22 | 0.16 | 1 | 7 | 0 | 2026-09-23T16:34:05.297000+00:00 | 2026-10-05T17:08:10.496000+00:00 | 288h 34m |
| DEBUGMenu | 20 | 0.15 | 1 | 8 | 0 | 2026-09-23T16:29:50.794000+00:00 | 2026-10-05T16:47:04.185000+00:00 | 288h 17m |
| gameStartEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-09-23T16:29:31.169000+00:00 | 2026-10-06T15:39:23.653000+00:00 | 311h 9m |
| argumentationEvent | 15 | 0.11 | 1 | 4 | 0 | 2026-09-24T16:28:05.519000+00:00 | 2026-10-06T15:44:13.592000+00:00 | 287h 16m |
| TerasGardenBox | 9 | 0.07 | 1 | 1 | 0 | 2026-10-05T16:37:40.314000+00:00 | 2026-10-05T16:38:28.966000+00:00 | 48.7s |
| DaniEvent | 8 | 0.06 | 1 | 2 | 0 | 2026-09-25T17:03:40.998000+00:00 | 2026-09-30T16:47:41.616000+00:00 | 119h 44m |
| argumentationToolEvent | 8 | 0.06 | 1 | 3 | 0 | 2026-09-24T16:29:23.829000+00:00 | 2026-10-06T15:43:29.052000+00:00 | 287h 14m |
| chatEvent | 5 | 0.04 | 1 | 3 | 0 | 2026-09-30T16:45:43.959000+00:00 | 2026-10-06T15:39:32.431000+00:00 | 142h 53m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-25T16:32:22.605000+00:00 | 2026-10-06T15:57:42.462000+00:00 | 263h 25m |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |
| soilMachine | 3 | 0.02 | 1 | 1 | 0 | 2026-10-05T16:04:27.499000+00:00 | 2026-10-05T16:04:35.654000+00:00 | 8.2s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 344411.958s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.736s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.492s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 11.741s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 41174.202s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 82349.641s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 491.823s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1358.426s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.077s median 
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
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 5.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 4 in 09-23-26 
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 330 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.6x vs baseline. 
  - Observed: 33 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,I; A,2,II; A,3,I; A,3,II; A,C,2,II; B,1,I; B,1,II; B,2,II; B,3,I; B,3,II; C,2,II; C,3,II; C,4,II; D,2,II; D,3,II; II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 449 records 
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
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-218, 11-224, 11-226, 11-23, 11-24] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 22 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
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
  - Observed: 38 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[439] _id=6ab403a6485cab4c954e802c ts=2026-09-23T16:51:50.2460000Z`; `6aa4142c41b41dbac0c7f249.jsonl[535] _id=6ab40501485cab4c954e8a23 ts=2026-09-23T16:57:37.2210000Z`; `6aa4142c41b41dbac0c7f249.jsonl[567] _id=6ab4056a485cab4c954e8d70 ts=2026-09-23T16:59:22.6040000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:29' vs expected 'questActiveEvent:32' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[655] _id=6ab54d06485cab4c9552e571 ts=2026-09-24T16:17:10.6120000Z`; `6aa4142c41b41dbac0c7f249.jsonl[956] _id=6ab6a06b485cab4c95592637 ts=2026-09-25T16:25:14.6880000Z`; `6aa4142c41b41dbac0c7f249.jsonl[5878] _id=6abbe6ed485cab4c9580bfd7 ts=2026-09-29T16:27:23.5580000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[14] _id=6ab3fe6b485cab4c954e6184 ts=2026-09-23T16:29:31.1690000Z`; `6aa4142c41b41dbac0c7f249.jsonl[275] _id=6ab401af485cab4c954e762e ts=2026-09-23T16:43:27.8930000Z`; `6aa4142c41b41dbac0c7f249.jsonl[652] _id=6ab54cf9485cab4c9552e52d ts=2026-09-24T16:16:57.5180000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 31 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 31} 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[15] _id=6ab3fe6b485cab4c954e6182 ts=2026-09-23T16:29:31.1680000Z`; `6aa4142c41b41dbac0c7f249.jsonl[221] _id=6ab3ff7d485cab4c954e6740 ts=2026-09-23T16:34:05.9160000Z`; `6aa4142c41b41dbac0c7f249.jsonl[231] _id=6ab3ff97485cab4c954e6844 ts=2026-09-23T16:34:31.5780000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[219] _id=6ab3ff7d485cab4c954e673a ts=2026-09-23T16:34:05.2970000Z`; `6aa4142c41b41dbac0c7f249.jsonl[229] _id=6ab3ff8a485cab4c954e67ee ts=2026-09-23T16:34:18.9140000Z`; `6aa4142c41b41dbac0c7f249.jsonl[639] _id=6ab406d3485cab4c954e9460 ts=2026-09-23T17:05:23.1850000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 11 of 87 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1242] _id=6ab6a353485cab4c955b09a6 ts=2026-09-25T16:37:39.5420000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1243] _id=6ab6a354485cab4c955b0a48 ts=2026-09-25T16:37:40.6500000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1244] _id=6ab6a355485cab4c955b0aa6 ts=2026-09-25T16:37:41.2040000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5210 | 0.0 | 0.019 | 166.005 | 0.983 | 343163.21 | 0.36 | 3468 | 7 |
| InputEvent | 3262 | 0.0 | 0.986 | 343.731 | 20.904 | 340621.288 | 0.17 | 115 | 9 |
| DialogueEvent | 2199 | 0.001 | 4.289 | 509.885 | 27.727 | 340422.728 | 0.12 | 636 | 10 |
| PlayerPositionEvent | 1899 | 9.696 | 10.0 | 411.069 | 10.185 | 257217.143 | 0.15 | 0 | 7 |
| argumentationNodeEvent | 448 | 0.016 | 0.323 | 2308.525 | 7.055 | 432982.207 | 0.03 | 73 | 5 |
| ObjectInterEvent | 298 | 0.001 | 7.204 | 3758.718 | 458.65 | 340755.899 | 0.02 | 5 | 11 |
| TopographicMapEvent | 86 | 0.014 | 4.492 | 6038.786 | 765.488 | 257391.961 | 0.01 | 2 | 6 |
| questEvent | 82 | 0.001 | 189.356 | 13670.319 | 84512.646 | 340602.949 | 0.0 | 17 | 15 |
| Soil Key Puzzle | 63 | 0.186 | 1.007 | 9537.1 | 8.175 | 427297.257 | 0.01 | 0 | 2 |
| argumentationAnswerEvent | 32 | 0.926 | 11.741 | 32314.88 | 241054.054 | 433746.156 | 0.0 | 0 | 4 |
| gameWindowFocusEvent | 30 | 0.646 | 491.823 | 37339.749 | 181110.695 | 340379.753 | 0.0 | 0 | 14 |
| WaterChamberEvent | 24 | 1.001 | 10.165 | 26.918 | 82.885 | 93.67 | 2.23 | 0 | 0 |
| SolarStillDesignEvent | 22 | 0.679 | 1.287 | 1.733 | 3.743 | 6.938 | 34.61 | 0 | 0 |
| gameWindowUnfocusEvent | 21 | 0.49 | 1358.426 | 49468.819 | 258922.352 | 340599.565 | 0.0 | 0 | 11 |
| DEBUGMenu | 19 | 132.662 | 1035.763 | 54622.81 | 266532.597 | 341398.309 | 0.0 | 0 | 14 |
| gameStartEvent | 15 | 131.707 | 82349.641 | 74679.499 | 282864.113 | 340379.752 | 0.0 | 0 | 13 |
| argumentationEvent | 14 | 0.028 | 54.76 | 73869.148 | 431423.249 | 433712.196 | 0.0 | 2 | 4 |
| TerasGardenBox | 8 | 0.736 | 1.736 | 6.082 | 19.804 | 20.313 | 9.87 | 0 | 0 |
| DaniEvent | 7 | 1.363 | 2.097 | 61577.231 | 301674.053 | 430913.023 | 0.0 | 0 | 1 |
| argumentationToolEvent | 7 | 0.575 | 12.835 | 147720.746 | 518262.464 | 520176.74 | 0.0 | 0 | 2 |
| chatEvent | 4 | 4.301 | 41174.202 | 128607.118 | 379479.813 | 432075.766 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 83467.621 | 344411.958 | 316106.619 | 502837.446 | 520440.278 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| soilMachine | 2 | 4.01 | 4.077 | 4.077 | 4.138 | 4.145 | 14.71 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[5854] _id=6abbe6ec485cab4c9580bfb9 ts=2026-09-29T16:27:23.5010000Z == 6aa4142c41b41dbac0c7f249.jsonl[5872] _id=6abbe6ed485cab4c9580bfbb ts=2026-09-29T16:27:23.5010000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 362 group(s), 552 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1229] _id=6ab6a33f485cab4c955afc9d ts=2026-09-25T16:37:19.7940000Z == 6aa4142c41b41dbac0c7f249.jsonl[1230] _id=6ab6a340485cab4c955afcb0 ts=2026-09-25T16:37:19.7940000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1236] _id=6ab6a341485cab4c955afda1 ts=2026-09-25T16:37:20.3520000Z == 6aa4142c41b41dbac0c7f249.jsonl[1235] _id=6ab6a341485cab4c955afdb3 ts=2026-09-25T16:37:20.3520000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1284] _id=6ab6a398485cab4c955b37fa ts=2026-09-25T16:38:46.8440000Z == 6aa4142c41b41dbac0c7f249.jsonl[1285] _id=6ab6a398485cab4c955b380b ts=2026-09-25T16:38:46.8440000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6aa4142c41b41dbac0c7f249.jsonl[412] _id=6ab4032e485cab4c954e7cfc ts=2026-09-23T16:49:50.7740000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[413] _id=6ab4032e485cab4c954e7cfe ts=2026-09-23T16:49:50.7790000Z`; `1ms: 6aa4142c41b41dbac0c7f249.jsonl[11876] _id=6ac3ccfade269131f9ada081 ts=2026-10-05T16:14:50.0350000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[11879] _id=6ac3ccfade269131f9ada083 ts=2026-10-05T16:14:50.0360000Z`; `1ms: 6aa4142c41b41dbac0c7f249.jsonl[11901] _id=6ac3cd38de269131f9ada23b ts=2026-10-05T16:15:52.7040000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[11902] _id=6ac3cd38de269131f9ada23d ts=2026-10-05T16:15:52.7050000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1058 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `58ms: 6aa4142c41b41dbac0c7f249.jsonl[1350] _id=6ab6a3a8485cab4c955b4205 ts=2026-09-25T16:37:04.8910000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[1338] _id=6ab6a3a8485cab4c955b4211 ts=2026-09-25T16:37:04.9490000Z`; `21ms: 6aa4142c41b41dbac0c7f249.jsonl[1234] _id=6ab6a341485cab4c955afd98 ts=2026-09-25T16:37:20.3310000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[1236] _id=6ab6a341485cab4c955afda1 ts=2026-09-25T16:37:20.3520000Z`; `24ms: 6aa4142c41b41dbac0c7f249.jsonl[1266] _id=6ab6a396485cab4c955b3665 ts=2026-09-25T16:38:46.0640000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[1267] _id=6ab6a396485cab4c955b3676 ts=2026-09-25T16:38:46.0880000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6aa4142c41b41dbac0c7f249.jsonl[3985] _id=6ab6a95c485cab4c955d2eb9 ts=2026-09-25T17:03:24.3610000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[3988] _id=6ab6a95c485cab4c955d2ed1 ts=2026-09-25T17:03:24.3800000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `926ms: 6aa4142c41b41dbac0c7f249.jsonl[913] _id=6ab54ff1485cab4c95531061 ts=2026-09-24T16:29:37.3740000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[917] _id=6ab54ff2485cab4c95531077 ts=2026-09-24T16:29:38.3000000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa4142c41b41dbac0c7f249.jsonl[8766] _id=6abd402a485cab4c958edeb2 ts=2026-09-30T17:00:25.9800000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[8764] _id=6abd402a485cab4c958edeba ts=2026-09-30T17:00:26.0080000Z`; `47ms: 6aa4142c41b41dbac0c7f249.jsonl[12236] _id=6ac3d13cde269131f9adca95 ts=2026-10-05T16:33:00.5490000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[12241] _id=6ac3d13cde269131f9adca9e ts=2026-10-05T16:33:00.5960000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 78 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa4142c41b41dbac0c7f249.jsonl[812] _id=6ab54f69485cab4c95530827 ts=2026-09-24T16:27:21.3530000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[806] _id=6ab54f69485cab4c9553082b ts=2026-09-24T16:27:21.3760000Z`; `515ms: 6aa4142c41b41dbac0c7f249.jsonl[831] _id=6ab54f73485cab4c955308bf ts=2026-09-24T16:27:31.4170000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[833] _id=6ab54f74485cab4c955308c7 ts=2026-09-24T16:27:31.9320000Z`; `43ms: 6aa4142c41b41dbac0c7f249.jsonl[833] _id=6ab54f74485cab4c955308c7 ts=2026-09-24T16:27:31.9320000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[834] _id=6ab54f74485cab4c955308cb ts=2026-09-24T16:27:31.9750000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `646ms: 6aa4142c41b41dbac0c7f249.jsonl[1167] _id=6ab6a2b1485cab4c955aa4d8 ts=2026-09-25T16:34:57.9230000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[1170] _id=6ab6a2b2485cab4c955aa553 ts=2026-09-25T16:34:58.5690000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `499ms: 6aa4142c41b41dbac0c7f249.jsonl[1168] _id=6ab6a2b1485cab4c955aa48f ts=2026-09-25T16:34:57.5380000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[1169] _id=6ab6a2b2485cab4c955aa549 ts=2026-09-25T16:34:58.0370000Z`; `490ms: 6aa4142c41b41dbac0c7f249.jsonl[9949] _id=6abe91d0485cab4c95ac3ab8 ts=2026-10-01T17:01:04.4250000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[9946] _id=6abe91d2485cab4c95ac3ac8 ts=2026-10-01T17:01:04.9150000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `47ms: 6aa4142c41b41dbac0c7f249.jsonl[655] _id=6ab54d06485cab4c9552e571 ts=2026-09-24T16:17:10.6120000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[656] _id=6ab54d07485cab4c9552e573 ts=2026-09-24T16:17:10.6590000Z`; `1ms: 6aa4142c41b41dbac0c7f249.jsonl[956] _id=6ab6a06b485cab4c95592637 ts=2026-09-25T16:25:14.6880000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[957] _id=6ab6a06b485cab4c95592647 ts=2026-09-25T16:25:14.6890000Z`; `3ms: 6aa4142c41b41dbac0c7f249.jsonl[5878] _id=6abbe6ed485cab4c9580bfd7 ts=2026-09-29T16:27:23.5580000Z ~ 6aa4142c41b41dbac0c7f249.jsonl[5863] _id=6abbe6ee485cab4c9580bfd9 ts=2026-09-29T16:27:23.5610000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 49m 
  - Evidence: 94h 49m: 6aa4142c41b41dbac0c7f249.jsonl[9751] _id=6abe8f26485cab4c95ac1fe9 ts=2026-10-01T16:49:42.5770000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10027] _id=6ac3c4bcde269131f9ad5813 ts=2026-10-05T15:39:40.8860000Z; 71h 43m: 6aa4142c41b41dbac0c7f249.jsonl[2234] _id=6ab6a5ac485cab4c955c8ba2 ts=2026-09-25T16:47:39.5210000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4037] _id=6aba9651485cab4c956aa3c1 ts=2026-09-28T16:31:13.7050000Z; 24h 7m: 6aa4142c41b41dbac0c7f249.jsonl[653] _id=6ab54d05485cab4c9552e56b ts=2026-09-24T16:17:09.8730000Z -> 6aa4142c41b41dbac0c7f249.jsonl[953] _id=6ab6a063485cab4c95592148 ts=2026-09-25T16:25:07.2970000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 119h 41m 
  - Evidence: 119h 41m: 6aa4142c41b41dbac0c7f249.jsonl[4001] _id=6ab6a96e485cab4c955d31a8 ts=2026-09-25T17:03:42.9460000Z -> 6aa4142c41b41dbac0c7f249.jsonl[7676] _id=6abd3cb0485cab4c958e9218 ts=2026-09-30T16:45:35.9690000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 33m 
  - Evidence: 94h 33m: 6aa4142c41b41dbac0c7f249.jsonl[10008] _id=6abe930e485cab4c95ac4268 ts=2026-10-01T17:06:22.9120000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10033] _id=6ac3c4d5de269131f9ad59d9 ts=2026-10-05T15:40:05.6400000Z; 71h 28m: 6aa4142c41b41dbac0c7f249.jsonl[4004] _id=6ab6a97b485cab4c955d3387 ts=2026-09-25T17:03:55.8670000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4069] _id=6aba9688485cab4c956aa992 ts=2026-09-28T16:32:08.3120000Z; 23h 56m: 6aa4142c41b41dbac0c7f249.jsonl[899] _id=6ab54fe7485cab4c95530f8f ts=2026-09-24T16:29:27.8670000Z -> 6aa4142c41b41dbac0c7f249.jsonl[963] _id=6ab6a088485cab4c955938c9 ts=2026-09-25T16:25:44.6720000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 636 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f249.jsonl[1084] _id=6ab6a1ad485cab4c9559f6aa ts=2026-09-25T16:30:37.0970000Z -> 6aa4142c41b41dbac0c7f249.jsonl[1083] _id=6ab6a1ad485cab4c9559f6b3 ts=2026-09-25T16:30:37.0980000Z; 1ms: 6aa4142c41b41dbac0c7f249.jsonl[12217] _id=6ac3d12fde269131f9adc955 ts=2026-10-05T16:32:47.7360000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12212] _id=6ac3d12fde269131f9adc957 ts=2026-10-05T16:32:47.7370000Z; 1ms: 6aa4142c41b41dbac0c7f249.jsonl[12293] _id=6ac3d1bade269131f9add34b ts=2026-10-05T16:35:06.7440000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12302] _id=6ac3d1bade269131f9add34d ts=2026-10-05T16:35:06.7450000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 34m 
  - Evidence: 144h 34m: 6aa4142c41b41dbac0c7f249.jsonl[1142] _id=6ab6a216485cab4c955a3a6d ts=2026-09-25T16:32:22.6050000Z -> 6aa4142c41b41dbac0c7f249.jsonl[9992] _id=6abe930e485cab4c95ac4266 ts=2026-10-01T17:06:22.8830000Z; 95h 40m: 6aa4142c41b41dbac0c7f249.jsonl[9992] _id=6abe930e485cab4c95ac4266 ts=2026-10-01T17:06:22.8830000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12536] _id=6ac3d46ade269131f9ae0be5 ts=2026-10-05T16:46:34.8410000Z; 23h 11m: 6aa4142c41b41dbac0c7f249.jsonl[12536] _id=6ac3d46ade269131f9ae0be5 ts=2026-10-05T16:46:34.8410000Z -> 6aa4142c41b41dbac0c7f249.jsonl[13789] _id=6ac51a76de269131f9b4cff5 ts=2026-10-06T15:57:42.4620000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 94h 37m 
  - Evidence: 94h 37m: 6aa4142c41b41dbac0c7f249.jsonl[10000] _id=6abe92fc485cab4c95ac4222 ts=2026-10-01T17:06:04.6080000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10054] _id=6ac3c589de269131f9ad623b ts=2026-10-05T15:43:05.8960000Z; 71h 27m: 6aa4142c41b41dbac0c7f249.jsonl[4015] _id=6ab6a98f485cab4c955d349b ts=2026-09-25T17:04:16.0210000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4045] _id=6aba9658485cab4c956aa477 ts=2026-09-28T16:31:20.0500000Z; 23h 58m: 6aa4142c41b41dbac0c7f249.jsonl[785] _id=6ab54f3d485cab4c95530421 ts=2026-09-24T16:26:37.6290000Z -> 6aa4142c41b41dbac0c7f249.jsonl[958] _id=6ab6a071485cab4c95592a79 ts=2026-09-25T16:25:21.6580000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 115 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f249.jsonl[5854] _id=6abbe6ec485cab4c9580bfb9 ts=2026-09-29T16:27:23.5010000Z -> 6aa4142c41b41dbac0c7f249.jsonl[5872] _id=6abbe6ed485cab4c9580bfbb ts=2026-09-29T16:27:23.5010000Z; 1ms: 6aa4142c41b41dbac0c7f249.jsonl[2239] _id=6ab6a5b4485cab4c955c9072 ts=2026-09-25T16:47:46.8080000Z -> 6aa4142c41b41dbac0c7f249.jsonl[2238] _id=6ab6a5b4485cab4c955c907c ts=2026-09-25T16:47:46.8090000Z; 1ms: 6aa4142c41b41dbac0c7f249.jsonl[280] _id=6ab401c0485cab4c954e7666 ts=2026-09-23T16:43:43.7480000Z -> 6aa4142c41b41dbac0c7f249.jsonl[281] _id=6ab401c0485cab4c954e7668 ts=2026-09-23T16:43:43.7490000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 39m 
  - Evidence: 94h 39m: 6aa4142c41b41dbac0c7f249.jsonl[10001] _id=6abe9300485cab4c95ac4236 ts=2026-10-01T17:06:08.6920000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10150] _id=6ac3c614de269131f9ad6b1f ts=2026-10-05T15:45:24.5910000Z; 71h 55m: 6aa4142c41b41dbac0c7f249.jsonl[3861] _id=6ab6a79b485cab4c955d01a9 ts=2026-09-25T16:55:55.1230000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4411] _id=6aba9b23485cab4c956ad7a2 ts=2026-09-28T16:51:47.4890000Z; 23h 59m: 6aa4142c41b41dbac0c7f249.jsonl[791] _id=6ab54f44485cab4c955304f3 ts=2026-09-24T16:26:44.2570000Z -> 6aa4142c41b41dbac0c7f249.jsonl[964] _id=6ab6a088485cab4c955938b9 ts=2026-09-25T16:25:44.6480000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f249.jsonl[11876] _id=6ac3ccfade269131f9ada081 ts=2026-10-05T16:14:50.0350000Z -> 6aa4142c41b41dbac0c7f249.jsonl[11879] _id=6ac3ccfade269131f9ada083 ts=2026-10-05T16:14:50.0360000Z; 1ms: 6aa4142c41b41dbac0c7f249.jsonl[11901] _id=6ac3cd38de269131f9ada23b ts=2026-10-05T16:15:52.7040000Z -> 6aa4142c41b41dbac0c7f249.jsonl[11902] _id=6ac3cd38de269131f9ada23d ts=2026-10-05T16:15:52.7050000Z; 1ms: 6aa4142c41b41dbac0c7f249.jsonl[11981] _id=6ac3cfd6de269131f9ada8c5 ts=2026-10-05T16:27:02.4560000Z -> 6aa4142c41b41dbac0c7f249.jsonl[11985] _id=6ac3cfd6de269131f9ada8c7 ts=2026-10-05T16:27:02.4570000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 26m 
  - Evidence: 71h 26m: 6aa4142c41b41dbac0c7f249.jsonl[4016] _id=6ab6a990485cab4c955d34a7 ts=2026-09-25T17:04:16.5700000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4039] _id=6aba9658485cab4c956aa471 ts=2026-09-28T16:31:13.7130000Z; 23h 52m: 6aa4142c41b41dbac0c7f249.jsonl[950] _id=6ab550b9485cab4c95531bad ts=2026-09-24T16:32:57.8300000Z -> 6aa4142c41b41dbac0c7f249.jsonl[954] _id=6ab6a06b485cab4c9559262e ts=2026-09-25T16:25:07.3050000Z; 23h 22m: 6aa4142c41b41dbac0c7f249.jsonl[6989] _id=6abbef99485cab4c9582b168 ts=2026-09-29T17:04:25.0880000Z -> 6aa4142c41b41dbac0c7f249.jsonl[6998] _id=6abd383d485cab4c958da0fa ts=2026-09-30T16:26:29.8280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa4142c41b41dbac0c7f249.jsonl[9278] _id=6abe89b7485cab4c95abe8ba ts=2026-10-01T16:26:26.7920000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10159] _id=6ac3c62fde269131f9ad6cab ts=2026-10-05T15:45:50.0020000Z; 71h 58m: 6aa4142c41b41dbac0c7f249.jsonl[3847] _id=6ab6a77a485cab4c955cfee7 ts=2026-09-25T16:55:20.4190000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4451] _id=6aba9b87485cab4c956adce4 ts=2026-09-28T16:53:26.6580000Z; 24h 34m: 6aa4142c41b41dbac0c7f249.jsonl[6444] _id=6abbe797485cab4c9580c995 ts=2026-09-29T16:30:09.1010000Z -> 6aa4142c41b41dbac0c7f249.jsonl[8896] _id=6abd411a485cab4c958ef19c ts=2026-09-30T17:04:26.0140000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3468 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4142c41b41dbac0c7f249.jsonl[10012] _id=6ac3c654de269131f9ad6fd9 ts=2026-10-05T15:46:27.2270000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10447] _id=6ac3c654de269131f9ad6fdb ts=2026-10-05T15:46:27.2270000Z; 0ms: 6aa4142c41b41dbac0c7f249.jsonl[10014] _id=6ac3c654de269131f9ad6fe5 ts=2026-10-05T15:46:27.3040000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10449] _id=6ac3c654de269131f9ad6fe7 ts=2026-10-05T15:46:27.3040000Z; 0ms: 6aa4142c41b41dbac0c7f249.jsonl[10016] _id=6ac3c654de269131f9ad6ff4 ts=2026-10-05T15:46:27.3430000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10440] _id=6ac3c654de269131f9ad6ff7 ts=2026-10-05T15:46:27.3430000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 118h 41m 
  - Evidence: 118h 41m: 6aa4142c41b41dbac0c7f249.jsonl[8885] _id=6abd40f3485cab4c958eeebe ts=2026-09-30T17:03:47.3280000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10154] _id=6ac3c614de269131f9ad6b1d ts=2026-10-05T15:45:24.5850000Z; 48h 10m: 6aa4142c41b41dbac0c7f249.jsonl[4428] _id=6aba9b49485cab4c956ad9e8 ts=2026-09-28T16:52:25.2450000Z -> 6aa4142c41b41dbac0c7f249.jsonl[8775] _id=6abd40cc485cab4c958eed58 ts=2026-09-30T17:03:08.8410000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 71h 29m 
  - Evidence: 71h 29m: 6aa4142c41b41dbac0c7f249.jsonl[4012] _id=6ab6a97f485cab4c955d33db ts=2026-09-25T17:04:00.0220000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4115] _id=6aba96f0485cab4c956ab492 ts=2026-09-28T16:33:51.9830000Z; 24h 5m: 6aa4142c41b41dbac0c7f249.jsonl[4238] _id=6aba98ba485cab4c956ac359 ts=2026-09-28T16:41:30.2490000Z -> 6aa4142c41b41dbac0c7f249.jsonl[6696] _id=6abbeb6f485cab4c958170ab ts=2026-09-29T16:46:39.9220000Z; 23h 57m: 6aa4142c41b41dbac0c7f249.jsonl[8302] _id=6abd3e7b485cab4c958eba9f ts=2026-09-30T16:53:15.3010000Z -> 6aa4142c41b41dbac0c7f249.jsonl[9787] _id=6abe8f71485cab4c95ac22cf ts=2026-10-01T16:50:57.7330000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.014s..0.019s shown 
  - Evidence: 14ms: 6aa4142c41b41dbac0c7f249.jsonl[3989] _id=6ab6a95c485cab4c955d2eb5 ts=2026-09-25T17:03:24.3470000Z -> 6aa4142c41b41dbac0c7f249.jsonl[3985] _id=6ab6a95c485cab4c955d2eb9 ts=2026-09-25T17:03:24.3610000Z; 19ms: 6aa4142c41b41dbac0c7f249.jsonl[3985] _id=6ab6a95c485cab4c955d2eb9 ts=2026-09-25T17:03:24.3610000Z -> 6aa4142c41b41dbac0c7f249.jsonl[3988] _id=6ab6a95c485cab4c955d2ed1 ts=2026-09-25T17:03:24.3800000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 29m 
  - Evidence: 120h 29m: 6aa4142c41b41dbac0c7f249.jsonl[1045] _id=6ab6a160485cab4c9559c73e ts=2026-09-25T16:29:20.3430000Z -> 6aa4142c41b41dbac0c7f249.jsonl[8482] _id=6abd3fb2485cab4c958ed33c ts=2026-09-30T16:58:26.4990000Z; 119h 29m: 6aa4142c41b41dbac0c7f249.jsonl[8765] _id=6abd402a485cab4c958edeac ts=2026-09-30T17:00:25.9570000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12062] _id=6ac3d09bde269131f9adb8cf ts=2026-10-05T16:30:19.7840000Z; 23h 58m: 6aa4142c41b41dbac0c7f249.jsonl[931] _id=6ab54ffb485cab4c95531139 ts=2026-09-24T16:29:47.1580000Z -> 6aa4142c41b41dbac0c7f249.jsonl[1003] _id=6ab6a11a485cab4c9559986c ts=2026-09-25T16:28:10.4880000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 28m 
  - Evidence: 120h 28m: 6aa4142c41b41dbac0c7f249.jsonl[1048] _id=6ab6a160485cab4c9559c74e ts=2026-09-25T16:29:20.3590000Z -> 6aa4142c41b41dbac0c7f249.jsonl[8451] _id=6abd3f90485cab4c958ed10a ts=2026-09-30T16:57:52.5550000Z; 119h 29m: 6aa4142c41b41dbac0c7f249.jsonl[8764] _id=6abd402a485cab4c958edeba ts=2026-09-30T17:00:26.0080000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12057] _id=6ac3d098de269131f9adb89d ts=2026-10-05T16:30:16.7470000Z; 23h 58m: 6aa4142c41b41dbac0c7f249.jsonl[888] _id=6ab54fe1485cab4c95530f19 ts=2026-09-24T16:29:21.8030000Z -> 6aa4142c41b41dbac0c7f249.jsonl[996] _id=6ab6a0fd485cab4c955986c0 ts=2026-09-25T16:27:42.0020000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.028s..0.047s shown 
  - Evidence: 28ms: 6aa4142c41b41dbac0c7f249.jsonl[8766] _id=6abd402a485cab4c958edeb2 ts=2026-09-30T17:00:25.9800000Z -> 6aa4142c41b41dbac0c7f249.jsonl[8764] _id=6abd402a485cab4c958edeba ts=2026-09-30T17:00:26.0080000Z; 47ms: 6aa4142c41b41dbac0c7f249.jsonl[12236] _id=6ac3d13cde269131f9adca95 ts=2026-10-05T16:33:00.5490000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12241] _id=6ac3d13cde269131f9adca9e ts=2026-10-05T16:33:00.5960000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 16m 
  - Evidence: 120h 16m: 6aa4142c41b41dbac0c7f249.jsonl[1043] _id=6ab6a15d485cab4c9559c567 ts=2026-09-25T16:29:17.6620000Z -> 6aa4142c41b41dbac0c7f249.jsonl[7678] _id=6abd3cb3485cab4c958e9264 ts=2026-09-30T16:45:39.8690000Z; 119h 29m: 6aa4142c41b41dbac0c7f249.jsonl[8762] _id=6abd4028485cab4c958ede7d ts=2026-09-30T17:00:24.8660000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12054] _id=6ac3d09ade269131f9adb8bb ts=2026-10-05T16:30:18.1640000Z; 23h 56m: 6aa4142c41b41dbac0c7f249.jsonl[930] _id=6ab54ffa485cab4c95531131 ts=2026-09-24T16:29:46.1890000Z -> 6aa4142c41b41dbac0c7f249.jsonl[976] _id=6ab6a0a3485cab4c95594a11 ts=2026-09-25T16:26:11.3130000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 73 interval(s) ≤ 0.016s..0.018s shown 
  - Evidence: 16ms: 6aa4142c41b41dbac0c7f249.jsonl[1024] _id=6ab6a153485cab4c9559be8d ts=2026-09-25T16:29:07.6130000Z -> 6aa4142c41b41dbac0c7f249.jsonl[1025] _id=6ab6a153485cab4c9559be96 ts=2026-09-25T16:29:07.6290000Z; 18ms: 6aa4142c41b41dbac0c7f249.jsonl[865] _id=6ab54fa8485cab4c95530b3b ts=2026-09-24T16:28:24.0560000Z -> 6aa4142c41b41dbac0c7f249.jsonl[869] _id=6ab54fa8485cab4c95530b3d ts=2026-09-24T16:28:24.0740000Z; 18ms: 6aa4142c41b41dbac0c7f249.jsonl[922] _id=6ab54ff6485cab4c955310e9 ts=2026-09-24T16:29:42.6210000Z -> 6aa4142c41b41dbac0c7f249.jsonl[926] _id=6ab54ff6485cab4c955310ed ts=2026-09-24T16:29:42.6390000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 29m 
  - Evidence: 144h 29m: 6aa4142c41b41dbac0c7f249.jsonl[915] _id=6ab54ff1485cab4c9553105d ts=2026-09-24T16:29:37.2390000Z -> 6aa4142c41b41dbac0c7f249.jsonl[8559] _id=6abd3fe2485cab4c958ed680 ts=2026-09-30T16:59:13.9790000Z; 142h 43m: 6aa4142c41b41dbac0c7f249.jsonl[8747] _id=6abd401b485cab4c958edc50 ts=2026-09-30T17:00:11.4180000Z -> 6aa4142c41b41dbac0c7f249.jsonl[13436] _id=6ac5171ede269131f9b4a6d1 ts=2026-10-06T15:43:27.2370000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6aa4142c41b41dbac0c7f249.jsonl[7685] _id=6abd3cbc485cab4c958e934c ts=2026-09-30T16:45:48.2600000Z -> 6aa4142c41b41dbac0c7f249.jsonl[12576] _id=6ac3d488de269131f9ae0fc3 ts=2026-10-05T16:47:04.0260000Z; 22h 37m: 6aa4142c41b41dbac0c7f249.jsonl[13205] _id=6ac3d818de269131f9ae68af ts=2026-10-05T17:02:16.3510000Z -> 6aa4142c41b41dbac0c7f249.jsonl[13316] _id=6ac51632de269131f9b48ef7 ts=2026-10-06T15:39:32.4310000Z; 15m 12s: 6aa4142c41b41dbac0c7f249.jsonl[12576] _id=6ac3d488de269131f9ae0fc3 ts=2026-10-05T16:47:04.0260000Z -> 6aa4142c41b41dbac0c7f249.jsonl[13205] _id=6ac3d818de269131f9ae68af ts=2026-10-05T17:02:16.3510000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 94h 32m 
  - Evidence: 94h 32m: 6aa4142c41b41dbac0c7f249.jsonl[9993] _id=6abe931a485cab4c95ac4286 ts=2026-10-01T17:06:34.0910000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10026] _id=6ac3c4b6de269131f9ad57b9 ts=2026-10-05T15:39:33.8430000Z; 71h 43m: 6aa4142c41b41dbac0c7f249.jsonl[2233] _id=6ab6a5a4485cab4c955c8704 ts=2026-09-25T16:47:31.8090000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4034] _id=6aba964a485cab4c956aa2c5 ts=2026-09-28T16:31:06.3630000Z; 24h 7m: 6aa4142c41b41dbac0c7f249.jsonl[652] _id=6ab54cf9485cab4c9552e52d ts=2026-09-24T16:16:57.5180000Z -> 6aa4142c41b41dbac0c7f249.jsonl[952] _id=6ab6a052485cab4c95591798 ts=2026-09-25T16:24:50.1640000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 94h 32m 
  - Evidence: 94h 32m: 6aa4142c41b41dbac0c7f249.jsonl[10009] _id=6abe931a485cab4c95ac4284 ts=2026-10-01T17:06:34.0900000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10025] _id=6ac3c4b5de269131f9ad57b3 ts=2026-10-05T15:39:33.8430000Z; 71h 43m: 6aa4142c41b41dbac0c7f249.jsonl[2232] _id=6ab6a5a4485cab4c955c86de ts=2026-09-25T16:47:31.8080000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4036] _id=6aba964a485cab4c956aa2bd ts=2026-09-28T16:31:06.3620000Z; 24h 7m: 6aa4142c41b41dbac0c7f249.jsonl[651] _id=6ab54cf9485cab4c9552e529 ts=2026-09-24T16:16:57.5170000Z -> 6aa4142c41b41dbac0c7f249.jsonl[951] _id=6ab6a052485cab4c95591787 ts=2026-09-25T16:24:50.1630000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 94h 36m 
  - Evidence: 94h 36m: 6aa4142c41b41dbac0c7f249.jsonl[10010] _id=6abe931c485cab4c95ac4288 ts=2026-10-01T17:06:36.2190000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10081] _id=6ac3c593de269131f9ad6377 ts=2026-10-05T15:43:15.7840000Z; 71h 55m: 6aa4142c41b41dbac0c7f249.jsonl[4014] _id=6ab6a994485cab4c955d34db ts=2026-09-25T17:04:20.1290000Z -> 6aa4142c41b41dbac0c7f249.jsonl[5432] _id=6aba9cfe485cab4c956b4222 ts=2026-09-28T16:59:42.4810000Z; 47h 20m: 6aa4142c41b41dbac0c7f249.jsonl[639] _id=6ab406d3485cab4c954e9460 ts=2026-09-23T17:05:23.1850000Z -> 6aa4142c41b41dbac0c7f249.jsonl[978] _id=6ab6a0a5485cab4c95594b9c ts=2026-09-25T16:26:13.3760000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 94h 36m 
  - Evidence: 94h 36m: 6aa4142c41b41dbac0c7f249.jsonl[10002] _id=6abe9305485cab4c95ac424e ts=2026-10-01T17:06:13.8490000Z -> 6aa4142c41b41dbac0c7f249.jsonl[10050] _id=6ac3c580de269131f9ad619f ts=2026-10-05T15:42:56.7980000Z; 71h 28m: 6aa4142c41b41dbac0c7f249.jsonl[3975] _id=6ab6a944485cab4c955d2a6d ts=2026-09-25T17:03:00.3350000Z -> 6aa4142c41b41dbac0c7f249.jsonl[4033] _id=6aba965b485cab4c956aa4ec ts=2026-09-28T16:31:20.1590000Z; 23h 58m: 6aa4142c41b41dbac0c7f249.jsonl[795] _id=6ab54f44485cab4c955304ff ts=2026-09-24T16:26:44.2890000Z -> 6aa4142c41b41dbac0c7f249.jsonl[956] _id=6ab6a06b485cab4c95592637 ts=2026-09-25T16:25:14.6880000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4142c41b41dbac0c7f249.jsonl[956] _id=6ab6a06b485cab4c95592637 ts=2026-09-25T16:25:14.6880000Z -> 6aa4142c41b41dbac0c7f249.jsonl[957] _id=6ab6a06b485cab4c95592647 ts=2026-09-25T16:25:14.6890000Z; 2ms: 6aa4142c41b41dbac0c7f249.jsonl[13076] _id=6ac3d72cde269131f9ae4fd9 ts=2026-10-05T16:58:20.0510000Z -> 6aa4142c41b41dbac0c7f249.jsonl[13073] _id=6ac3d72cde269131f9ae4fdd ts=2026-10-05T16:58:20.0530000Z; 2ms: 6aa4142c41b41dbac0c7f249.jsonl[793] _id=6ab54f44485cab4c955304fb ts=2026-09-24T16:26:44.2870000Z -> 6aa4142c41b41dbac0c7f249.jsonl[795] _id=6ab54f44485cab4c955304ff ts=2026-09-24T16:26:44.2890000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1057] _id=6ab6a178485cab4c9559d74c ts=2026-09-25T16:29:44.4440000Z`; `6aa4142c41b41dbac0c7f249.jsonl[4237] _id=6aba98b5485cab4c956ac341 ts=2026-09-28T16:41:25.6680000Z`; `6aa4142c41b41dbac0c7f249.jsonl[6488] _id=6abbe860485cab4c9580dbf9 ts=2026-09-29T16:33:36.7040000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 189 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1520] _id=6ab6a3c7485cab4c955b5898 ts=2026-09-25T16:39:35.1100000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1526] _id=6ab6a3c7485cab4c955b58a2 ts=2026-09-25T16:39:35.1280000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1550] _id=6ab6a3cc485cab4c955b5cbe ts=2026-09-25T16:39:39.4710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 534 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1356] _id=6ab6a3a8485cab4c955b4281 ts=2026-09-25T16:37:17.5810000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1363] _id=6ab6a3a8485cab4c955b429d ts=2026-09-25T16:37:17.6240000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1279] _id=6ab6a398485cab4c955b37dd ts=2026-09-25T16:38:46.7740000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[8764] _id=6abd402a485cab4c958edeba ts=2026-09-30T17:00:26.0080000Z`; `6aa4142c41b41dbac0c7f249.jsonl[12241] _id=6ac3d13cde269131f9adca9e ts=2026-10-05T16:33:00.5960000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 22 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[812] _id=6ab54f69485cab4c95530827 ts=2026-09-24T16:27:21.3530000Z`; `6aa4142c41b41dbac0c7f249.jsonl[806] _id=6ab54f69485cab4c9553082b ts=2026-09-24T16:27:21.3760000Z`; `6aa4142c41b41dbac0c7f249.jsonl[833] _id=6ab54f74485cab4c955308c7 ts=2026-09-24T16:27:31.9320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[12576] _id=6ac3d488de269131f9ae0fc3 ts=2026-10-05T16:47:04.0260000Z`; `6aa4142c41b41dbac0c7f249.jsonl[13205] _id=6ac3d818de269131f9ae68af ts=2026-10-05T17:02:16.3510000Z`; `6aa4142c41b41dbac0c7f249.jsonl[13316] _id=6ac51632de269131f9b48ef7 ts=2026-10-06T15:39:32.4310000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[429] _id=6ab40371485cab4c954e7e56 ts=2026-09-23T16:50:57.3270000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[955] _id=6ab6a06a485cab4c95592618 ts=?`; `6aa4142c41b41dbac0c7f249.jsonl[2228] _id=6ab6a44b485cab4c955bb2fd ts=?`; `6aa4142c41b41dbac0c7f249.jsonl[5870] _id=6abbe6eb485cab4c9580bfb5 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 840 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1534] _id=6ab6a3c9485cab4c955b5a75 ts=2026-09-25T16:39:37.2910000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1632] _id=6ab6a3d6485cab4c955b63fc ts=2026-09-25T16:39:50.3990000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1647] _id=6ab6a3d9485cab4c955b65ec ts=2026-09-25T16:39:53.2530000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1013 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1334] _id=6ab6a3a7485cab4c955b418c ts=2026-09-25T16:36:59.5000000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1343] _id=6ab6a3a7485cab4c955b4197 ts=2026-09-25T16:37:00.2780000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1344] _id=6ab6a3a7485cab4c955b41ba ts=2026-09-25T16:37:00.3260000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 21 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[3985] _id=6ab6a95c485cab4c955d2eb9 ts=2026-09-25T17:03:24.3610000Z`; `6aa4142c41b41dbac0c7f249.jsonl[3988] _id=6ab6a95c485cab4c955d2ed1 ts=2026-09-25T17:03:24.3800000Z`; `6aa4142c41b41dbac0c7f249.jsonl[4002] _id=6ab6a96e485cab4c955d31af ts=2026-09-25T17:03:42.9510000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1017] _id=6ab6a14e485cab4c9559bb6a ts=2026-09-25T16:29:02.9990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[912] _id=6ab54ff0485cab4c9553104f ts=2026-09-24T16:29:36.6640000Z`; `6aa4142c41b41dbac0c7f249.jsonl[13437] _id=6ac5171fde269131f9b4a6ed ts=2026-10-06T15:43:28.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 420 start, 412 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 334 unmatched 'BecameCameraCentered' (totals: 1096 open, 951 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 204 unmatched 'BecameVisible' (totals: 1417 open, 1747 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 24 open, 22 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 7 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 7 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 51 start, 32 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 413 of 13788 adjacent _id pairs reverse in client time; worst 123.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4142c41b41dbac0c7f249.jsonl[1333] _id=6ab6a3a6485cab4c955b411b ts=2026-09-25T16:39:02.4890000Z`; `6aa4142c41b41dbac0c7f249.jsonl[1337] _id=6ab6a3a7485cab4c955b417b ts=2026-09-25T16:36:59.4430000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.11s, min -123.98s, max +1.60s over 13789 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4142c41b41dbac0c7f249\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 5211 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3783); Unit 4 Dev (830); Unit 3 Dungeon Dev (374); Unit 5 Dev - Dungeon (224)
- **Intervals:** median 0.02s (p5 0.00s / p95 0.98s, n=5210)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5211/5211 records)
    "BecameInvisible"  x1747
    "BecameVisible"  x1417
    "BecameCameraCentered"  x1096
    "BecameCameraUncentered"  x951
data.pieceId  (string, 5211/5211 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5211/5211 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3263 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1107); Unit 2 Prod (Refactor) (725); Unit 1 Dev (394); Unit 4 Dev - Dungeon (302); Unit 3 Dungeon Dev (268); Unit 5 Dev - Dungeon (178); Unit 4 Dev (167); Unit 5 Dev (74); Unit 4 Dev - Anderson Base (48)
- **Intervals:** median 0.99s (p5 0.09s / p95 20.90s, n=3262)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3263/3263 records)
    "pressed"  x3263
data.actionType  (string, 3263/3263 records)
    "Move"  x2296
    "Interact"  x605
    "Jump"  x138
    "Sprint"  x96
    "Ascend"  x54
    "Hoverboard"  x43
    "Descend"  x29
    "Map"  x1
    "Pause"  x1
data.key  (string, 3263/3263 records, 12 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3263/3263 records)
    "Player"  x2184
    "Drone"  x1079
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2200 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (592); Unit 3 Dev (350); Unit 4 Dev (258); Unit 1 Dev (257); Unit 5 Dev (253); Unit 4 Dev - Anderson Base (141); Unit 3 Dungeon Dev (137); Unit 4 Dev - Dungeon (119); Unit 5 Dev - Dungeon (93)
- **eventKey:** present on 1368 of 2200 records
- **Intervals:** median 4.29s (p5 0.00s / p95 27.73s, n=2199)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1368; [conversationId, dialogueEventType] x832
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2200/2200 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2200/2200 records)
    "DialogueNodeEvent"  x1368
    "DialogueStartEvent"  x420
    "DialogueFinishEvent"  x412
data.nodeId  (number, 1368/2200 records)
    numeric range 0 .. 290 (224 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1911 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (588); Unit 3 Dev (301); Unit 1 Dev (299); Unit 4 Dev (170); Unit 5 Dev (140); Unit 3 Dungeon Dev (137); Unit 4 Dev - Dungeon (103); Unit 5 Dev - Dungeon (91); Unit 4 Dev - Anderson Base (82)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.19s, n=1899)
- **Fields under `data`:**

```text
data.position  (object, 1911/1911 records)
data.position.x  (number, 1911/1911 records)
    numeric range -674.061 .. 1551.97 (611 unique)
data.position.y  (number, 1911/1911 records)
    numeric range -115.127 .. 222.65 (454 unique)
data.position.z  (number, 1911/1911 records)
    numeric range -1040.66 .. 2165.61 (610 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 449 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (153); Unit 4 Dev - Anderson Base (117); Unit 1 Dev (111); Unit 5 Dev (68)
- **Intervals:** median 0.32s (p5 0.03s / p95 7.06s, n=448)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 449/449 records)
    "argumentationNodeHoverEnd"  x210
    "argumentationNodeHoverStart"  x188
    "argumentationNodeAdd"  x34
    "argumentationNodeRemove"  x17
data.argumentationTitle  (string, 449/449 records)
    "Unit 3 - Pollution Upstream"  x153
    "Unit 4 - Flooding"  x117
    "Unit 5"  x68
    "Unit 1 - Freshwater"  x56
    "Unit 1 - Argumentation Tutorial"  x55
data.nodeName  (string, 449/449 records)
    "A"  x68
    "1"  x63
    "I"  x58
    "II"  x54
    "2"  x45
    "3"  x42
    "B"  x42
    "C"  x36
    "4"  x20
    "D"  x18
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 299 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (84); Unit 2 Prod (Refactor) (79); Unit 3 Dungeon Dev (41); Unit 4 Dev (20); Unit 1 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 5 Dev (18); Unit 3 Dev (11); Unit 5 Dev - Dungeon (10)
- **Intervals:** median 7.20s (p5 1.11s / p95 458.65s, n=298)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 299/299 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 299/299 records)
    100 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 87 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (49); Unit 2 Prod (Refactor) (38)
- **Intervals:** median 4.49s (p5 0.76s / p95 765.49s, n=86)
- **`data` key-set variants:** [actionType, featureUsed] x46; [actionType, featureUsed, location] x30; [actionType, featureUsed, legendName] x11
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 87/87 records)
    "WaypointMoveEvent"  x25
    "MapOpenEvent"  x24
    "MapCloseEvent"  x22
    "Selected"  x10
    "WaypointSetEvent"  x5
    "Unselected"  x1
data.featureUsed  (string, 87/87 records)
    "Map"  x46
    "Waypoint"  x30
    "Legend"  x11
data.legendName  (string, 11/87 records)
    "360 ft"  x3
    "0 ft"  x2
    "90 ft"  x2
    "Water"  x2
    "120 ft"  x1
    "330 ft"  x1
data.location  (object, 30/87 records)
data.location.x  (number, 30/87 records)
    numeric range -406.09 .. 331.91 (29 unique)
data.location.y  (number, 30/87 records)
    numeric range -306.5 .. 379.5 (26 unique)
data.location.z  (number, 30/87 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 83 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (19); Unit 2 Prod (Refactor) (17); Unit 3 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 83 of 83 records
- **Intervals:** median 189.36s (p5 0.00s / p95 84512.65s, n=82)
- **`data` key-set variants:** [questEventType, questID, questName] x51; [questEventType, questID, questName, questSuccessOrFailure] x32
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 83/83 records)
    "questActiveEvent"  x51
    "questFinishEvent"  x32
data.questID  (string, 83/83 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 83/83 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 32/83 records)
    "Succeeded"  x32
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 64 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (28); Unit 2 Prod (Refactor) (18); Unit 3 Dev (18)
- **Intervals:** median 1.01s (p5 0.21s / p95 8.17s, n=63)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x58; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/64 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/64 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 58/64 records)
    "RightDrag"  x32
    "LeftDrag"  x26
data.currentSoilType  (string, 58/64 records)
    "CLAY"  x12
    "CLAYSAND"  x12
    "SAND"  x12
    "CLAYROCK"  x11
    "SANDGRAVEL"  x6
    "BEDROCK"  x4
    "GRAVEL"  x1
data.isCorrectSelection  (string, 58/64 records)
    "false"  x42
    "true"  x16
data.waterLevelStatus  (string, 58/64 records)
    "Proper"  x26
    "TooLow"  x20
    "TooHigh"  x12
data.waterRetentionChange  (string, 58/64 records)
    "Increase"  x26
    "Decrease"  x16
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 33 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (12); Unit 3 Dev (8); Unit 1 Dev (7); Unit 5 Dev (6)
- **Intervals:** median 11.74s (p5 1.58s / p95 241054.05s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "submitAnswerEvent"  x33
data.answerSubmitted  (string, 33/33 records, 1 empty-string)
    21 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 33/33 records)
    "Unit 4 - Flooding"  x12
    "Unit 3 - Pollution Upstream"  x8
    "Unit 1 - Freshwater"  x6
    "Unit 5"  x6
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 31 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 2 Prod (Refactor) (6); Unit 3 Dev (5); Unit 1 Dev (3); Unit 4 Dev (1)
- **Intervals:** median 491.82s (p5 1.80s / p95 181110.70s, n=30)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 31/31 records)
    true  x31
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `WaterChamberEvent` — 25 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (25)
- **Intervals:** median 10.17s (p5 1.19s / p95 82.89s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "On"  x18
    "Off"  x7
data.floor  (string, 25/25 records)
    "4"  x11
    "3"  x8
    "2"  x4
    "1"  x2
data.machineNumber  (string, 25/25 records)
    "One"  x24
    "Two"  x1
data.machineType  (string, 25/25 records)
    "Condenser"  x12
    "Evaporator"  x8
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 25/25 records)
    "3"  x10
    "2"  x8
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `SolarStillDesignEvent` — 23 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (23)
- **Intervals:** median 1.29s (p5 0.70s / p95 3.74s, n=22)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x22; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "optionSelected"  x22
    "DesignSubmitted"  x1
data.designSelections  (object, 1/23 records)
data.designSelections.glassRoofTemperature  (string, 1/23 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/23 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/23 records)
    "Tilted Out"  x1
data.featureUsed  (string, 23/23 records)
    "ExtraCovering"  x10
    "RoofStyle"  x8
    "GlassRoofTemperature"  x4
    "Submit"  x1
data.selectedOption  (string, 22/23 records, 3 empty-string)
    "Covered"  x4
    ""  x3
    "Tilted In"  x3
    "Tilted Out"  x3
    "Uncovered"  x3
    "Cold"  x2
    "Flat"  x2
    "Hot"  x2
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameWindowUnfocusEvent` — 22 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (5); Unit 1 Dev (4); MainMenu (1); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 1358.43s (p5 0.50s / p95 258922.35s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    false  x22
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 20 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 1 Dev (4); Unit 4 Dev (3); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1035.76s (p5 420.00s / p95 266532.60s, n=19)
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "DebugMenuStateChanged"  x20
data.isOpened  (bool, 20/20 records)
    false  x20
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 82349.64s (p5 410.97s / p95 282864.11s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 54.76s (p5 0.04s / p95 431423.25s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 15/15 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 15/15 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 1.74s (p5 0.78s / p95 19.80s, n=8)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 6 empty-string)
    ""  x6
    "cameraPlaced"  x3
data.boxId  (string, 9/9 records)
    "0"  x5
    "1"  x2
    "2"  x2
data.soilType  (string, 9/9 records)
    "Sand"  x4
    "Clay"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (6); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 2.10s (p5 1.54s / p95 301674.05s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 8 empty-string)
    ""  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 8 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3); Unit 5 Dev (3); Unit 3 Dev (2)
- **Intervals:** median 12.84s (p5 0.62s / p95 518262.46s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "argumentationToolOpen"  x7
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x3
    "Unit 5"  x3
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 8/8 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 41174.20s (p5 140.50s / p95 379479.81s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x4
    "Open"  x1
data.chatID  (string, 5/5 records)
    "NA"  x4
    "[10-218, 11-224, 11-226, 11-23, 11-24]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 344411.96s (p5 109562.05s / p95 502837.45s, n=3)
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

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x2
    "unit1"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `soilMachine` — 3 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (3)
- **Intervals:** median 4.08s (p5 4.02s / p95 4.14s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "ChangeCanister"  x3
data.canisterType  (string, 3/3 records)
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 3/3 records)
    "5"  x3
data.machine  (string, 3/3 records)
    "2"  x3
data.row  (string, 3/3 records)
    "TopRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TopographicMapEvent` data.actionType: "Selected" (10x); "Unselected" (1x); "WaypointMoveEvent" (25x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (11x); "Waypoint" (30x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (17x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*