# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f9

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f9
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f9.jsonl
- **Records:** 16646 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f9
- **Time span:** 2026-09-23T13:07:21.799000+00:00 .. 2026-10-07T02:21:10.386000+00:00 (325h 13m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f9\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 16646 records, 10 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 110 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6522 | 39.18 | 1 | 9 | 0 | 2026-09-23T13:07:51.381000+00:00 | 2026-10-07T02:21:10.386000+00:00 | 325h 13m |
| PlayerPositionEvent | 2882 | 17.31 | 1 | 9 | 0 | 2026-09-23T13:07:44.509000+00:00 | 2026-10-07T02:21:02.518000+00:00 | 325h 13m |
| PuzzlePieceVisibleEvent | 2826 | 16.98 | 1 | 4 | 0 | 2026-09-28T13:06:47.082000+00:00 | 2026-10-07T01:48:47.585000+00:00 | 204h 42m |
| DialogueEvent | 2697 | 16.2 | 1 | 9 | 1657 | 2026-09-23T13:08:08.218000+00:00 | 2026-10-07T02:21:04.320000+00:00 | 325h 12m |
| argumentationNodeEvent | 896 | 5.38 | 1 | 5 | 0 | 2026-09-25T13:23:25.094000+00:00 | 2026-10-07T02:09:15.606000+00:00 | 276h 45m |
| ObjectInterEvent | 330 | 1.98 | 1 | 9 | 0 | 2026-09-23T13:19:46.654000+00:00 | 2026-10-07T02:21:10.386000+00:00 | 325h 1m |
| questEvent | 95 | 0.57 | 1 | 9 | 95 | 2026-09-23T13:08:08.200000+00:00 | 2026-10-07T02:17:33.927000+00:00 | 325h 9m |
| TopographicMapEvent | 76 | 0.46 | 1 | 3 | 0 | 2026-09-28T13:07:16.060000+00:00 | 2026-10-07T01:03:42.202000+00:00 | 203h 56m |
| Soil Key Puzzle | 56 | 0.34 | 1 | 3 | 0 | 2026-09-28T13:13:54.622000+00:00 | 2026-10-06T13:04:38.967000+00:00 | 191h 50m |
| TerasGardenBox | 44 | 0.26 | 1 | 1 | 0 | 2026-10-06T23:41:32.007000+00:00 | 2026-10-07T01:07:39.348000+00:00 | 1h 26m |
| argumentationAnswerEvent | 38 | 0.23 | 1 | 5 | 0 | 2026-09-25T13:27:01.561000+00:00 | 2026-10-07T02:09:21.321000+00:00 | 276h 42m |
| WaterChamberEvent | 35 | 0.21 | 1 | 1 | 0 | 2026-10-07T01:19:56.589000+00:00 | 2026-10-07T01:54:27.040000+00:00 | 34m 30s |
| DEBUGMenu | 34 | 0.2 | 1 | 9 | 0 | 2026-09-23T13:07:44.502000+00:00 | 2026-10-07T01:16:13.053000+00:00 | 324h 8m |
| gameWindowFocusEvent | 26 | 0.16 | 1 | 4 | 0 | 2026-09-23T13:07:21.799000+00:00 | 2026-10-07T01:16:09.195000+00:00 | 324h 8m |
| gameStartEvent | 23 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:07:21.800000+00:00 | 2026-10-07T01:16:09.195000+00:00 | 324h 8m |
| argumentationEvent | 15 | 0.09 | 1 | 5 | 0 | 2026-09-25T13:24:12.364000+00:00 | 2026-10-07T02:09:21.329000+00:00 | 276h 45m |
| DaniEvent | 14 | 0.08 | 1 | 1 | 0 | 2026-10-07T00:57:49.272000+00:00 | 2026-10-07T01:03:06.250000+00:00 | 5m 16s |
| argumentationToolEvent | 10 | 0.06 | 1 | 3 | 0 | 2026-09-25T13:26:36.123000+00:00 | 2026-10-07T02:07:39.182000+00:00 | 276h 41m |
| chatEvent | 8 | 0.05 | 1 | 3 | 0 | 2026-10-07T01:01:28.614000+00:00 | 2026-10-07T01:55:08.185000+00:00 | 53m 39s |
| SolarStillDesignEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-07T02:14:45.814000+00:00 | 2026-10-07T02:15:02.482000+00:00 | 16.7s |
| gameWindowUnfocusEvent | 4 | 0.02 | 1 | 3 | 0 | 2026-09-24T13:16:22.027000+00:00 | 2026-10-07T00:02:27.663000+00:00 | 298h 46m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-25T13:30:08.648000+00:00 | 2026-10-07T02:21:10.382000+00:00 | 276h 51m |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |
| soilMachine | 3 | 0.02 | 1 | 1 | 0 | 2026-10-06T13:24:58.573000+00:00 | 2026-10-06T13:25:19.135000+00:00 | 20.6s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 498330.867s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.647s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.697s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 7.705s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 16.512s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 235.046s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.965s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 3.595s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6332.729s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 3303.822s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 517415.183s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 10.281s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 14 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend; Sprint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; press; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Plant Seed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` — record volume changed 4.0x vs baseline. 
  - Observed: 44 records 
  - Expected: 11 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 150 ft; 180 ft; 210 ft; 270 ft; 300 ft; 330 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.6x vs baseline. 
  - Observed: 38 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,4,I; B,1,II; B,4,I; B,4,II; B,C,A,2,II; C,1,II; C,2,II; C,D,2,II; C,D,3,4,II; C,D,3,II; C,D,A,2,II; D,1,II; D,2,II; D,3,I; D,3,II; D,4,II; D,C,4,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 6.4x vs baseline. 
  - Observed: 896 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 8 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [105-7, 105-8, 105-10, 105-12, 105-14] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 26 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 4 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 54; 55 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Leader of Evidence; Part of a Balanced Ecosystem 
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
  - Observed: 34 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[679] _id=6ab3d579485cab4c954c82d3 ts=2026-09-23T13:34:49.6690000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[928] _id=6ab523d5485cab4c9550a2b1 ts=2026-09-24T13:21:25.4590000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1152] _id=6ab67249485cab4c955470c3 ts=2026-09-25T13:08:25.9250000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[5121] _id=6abd0797485cab4c958675bd ts=2026-09-30T12:59:01.3150000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[2] _id=6ab3cf09485cab4c954b866c ts=2026-09-23T13:07:21.8000000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[724] _id=6ab5224e485cab4c9550512f ts=2026-09-24T13:14:54.2710000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1028] _id=6ab67122485cab4c95545f0d ts=2026-09-25T13:03:30.3330000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 26 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 26} 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1] _id=6ab3cf09485cab4c954b866a ts=2026-09-23T13:07:21.7990000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[723] _id=6ab5224d485cab4c95505121 ts=2026-09-24T13:14:54.2700000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[816] _id=6ab522da485cab4c955068c1 ts=2026-09-24T13:17:14.9110000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 4 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 4} 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[806] _id=6ab522a5485cab4c95506261 ts=2026-09-24T13:16:22.0270000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[5203] _id=6abd07cd485cab4c95867921 ts=2026-09-30T12:59:57.2100000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[14044] _id=6ac58927de269131f9b878c3 ts=2026-10-06T23:47:50.1730000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 10 of 76 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1852] _id=6aba6684485cab4c9567a3d3 ts=2026-09-28T13:07:16.0600000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1844] _id=6aba6694485cab4c9567a42f ts=2026-09-28T13:07:32.5500000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[3130] _id=6aba6aaf485cab4c9567f241 ts=2026-09-28T13:25:03.4990000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 6521 | 0.0 | 0.533 | 179.543 | 9.859 | 337575.959 | 0.33 | 294 | 17 |
| PlayerPositionEvent | 2867 | 0.0 | 9.999 | 289.725 | 10.019 | 337518.322 | 0.21 | 1 | 10 |
| PuzzlePieceVisibleEvent | 2825 | 0.0 | 0.031 | 260.857 | 1.447 | 433459.759 | 0.23 | 1707 | 10 |
| DialogueEvent | 2696 | 0.0 | 4.578 | 434.264 | 33.889 | 337601.519 | 0.14 | 798 | 15 |
| argumentationNodeEvent | 895 | 0.012 | 0.379 | 1113.241 | 8.83 | 432662.899 | 0.05 | 223 | 6 |
| ObjectInterEvent | 329 | 0.0 | 10.986 | 3556.486 | 945.666 | 345167.628 | 0.02 | 7 | 20 |
| questEvent | 94 | 0.0 | 254.375 | 12452.827 | 85099.395 | 337624.677 | 0.0 | 22 | 25 |
| TopographicMapEvent | 75 | 0.028 | 3.697 | 9789.149 | 26456.858 | 344059.976 | 0.01 | 2 | 6 |
| Soil Key Puzzle | 55 | 0.216 | 1.647 | 12557.17 | 28069.365 | 518704.625 | 0.0 | 0 | 5 |
| TerasGardenBox | 43 | 0.145 | 2.116 | 120.171 | 280.554 | 3183.531 | 0.5 | 0 | 2 |
| argumentationAnswerEvent | 37 | 0.859 | 16.512 | 26922.696 | 142373.372 | 432675.569 | 0.0 | 0 | 6 |
| WaterChamberEvent | 34 | 0.799 | 7.705 | 60.896 | 51.303 | 1562.164 | 0.99 | 0 | 1 |
| DEBUGMenu | 33 | 3.896 | 1179.107 | 35360.865 | 155965.128 | 337624.261 | 0.0 | 0 | 22 |
| gameWindowFocusEvent | 25 | 35.405 | 3303.822 | 46677.096 | 223336.485 | 337613.052 | 0.0 | 0 | 19 |
| gameStartEvent | 22 | 35.405 | 6332.729 | 53042.154 | 248851.985 | 337613.052 | 0.0 | 0 | 19 |
| argumentationEvent | 14 | 0.014 | 235.046 | 71164.926 | 375422.35 | 432651.248 | 0.0 | 2 | 6 |
| DaniEvent | 13 | 1.414 | 4.316 | 24.383 | 103.174 | 199.448 | 2.46 | 0 | 0 |
| argumentationToolEvent | 9 | 0.068 | 0.965 | 110673.673 | 511095.148 | 563361.946 | 0.0 | 0 | 2 |
| chatEvent | 7 | 0.503 | 3.595 | 459.939 | 1895.547 | 2335.193 | 0.13 | 0 | 2 |
| SolarStillDesignEvent | 5 | 1.566 | 3.216 | 3.334 | 5.852 | 6.38 | 18.0 | 0 | 0 |
| gameWindowUnfocusEvent | 3 | 877.49 | 517415.183 | 358521.879 | 553287.185 | 557272.963 | 0.0 | 0 | 3 |
| EndOfUnit | 2 | 3915.646 | 498330.867 | 498330.867 | 943304.566 | 992746.088 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| soilMachine | 2 | 1.946 | 10.281 | 10.281 | 17.782 | 18.616 | 5.84 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[9680] _id=6ac3a8f1de269131f9a99aeb ts=2026-10-05T13:41:05.3340000Z == 6aa413b141b41dbac0c7f1f9.jsonl[9681] _id=6ac3a8f1de269131f9a99aed ts=2026-10-05T13:41:05.3340000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[12497] _id=6ac4f834de269131f9b0bb31 ts=2026-10-06T13:31:32.0350000Z == 6aa413b141b41dbac0c7f1f9.jsonl[12501] _id=6ac4f834de269131f9b0bb39 ts=2026-10-06T13:31:32.0350000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[13324] _id=6ac58450de269131f9b871d4 ts=2026-10-06T23:27:10.2040000Z == 6aa413b141b41dbac0c7f1f9.jsonl[13325] _id=6ac58450de269131f9b871d5 ts=2026-10-06T23:27:10.2040000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 103 group(s), 135 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[2011] _id=6aba6721485cab4c9567ad53 ts=2026-09-28T13:09:34.0390000Z == 6aa413b141b41dbac0c7f1f9.jsonl[2012] _id=6aba6721485cab4c9567ad57 ts=2026-09-28T13:09:34.0390000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[2032] _id=6aba6722485cab4c9567ad6d ts=2026-09-28T13:09:42.5310000Z == 6aa413b141b41dbac0c7f1f9.jsonl[2021] _id=6aba6722485cab4c9567ad71 ts=2026-09-28T13:09:42.5310000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[2023] _id=6aba6722485cab4c9567ad7b ts=2026-09-28T13:09:49.7320000Z == 6aa413b141b41dbac0c7f1f9.jsonl[2024] _id=6aba6722485cab4c9567ad7d ts=2026-09-28T13:09:49.7320000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[16425] _id=6ac5aac6de269131f9b89bf8 ts=2026-10-07T02:10:32.1270000Z == 6aa413b141b41dbac0c7f1f9.jsonl[16426] _id=6ac5aac6de269131f9b89bf9 ts=2026-10-07T02:10:32.1270000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 37 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `403ms: 6aa413b141b41dbac0c7f1f9.jsonl[229] _id=6ab3d1fd485cab4c954be0e6 ts=2026-09-23T13:19:57.5980000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[230] _id=6ab3d1fd485cab4c954be0ef ts=2026-09-23T13:19:58.0010000Z`; `237ms: 6aa413b141b41dbac0c7f1f9.jsonl[230] _id=6ab3d1fd485cab4c954be0ef ts=2026-09-23T13:19:58.0010000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[240] _id=6ab3d1fe485cab4c954be0fe ts=2026-09-23T13:19:58.2380000Z`; `210ms: 6aa413b141b41dbac0c7f1f9.jsonl[240] _id=6ab3d1fe485cab4c954be0fe ts=2026-09-23T13:19:58.2380000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[241] _id=6ab3d1fe485cab4c954be106 ts=2026-09-23T13:19:58.4480000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 348 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa413b141b41dbac0c7f1f9.jsonl[1929] _id=6aba6719485cab4c9567ac13 ts=2026-09-28T13:06:47.7220000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[1930] _id=6aba6719485cab4c9567ac17 ts=2026-09-28T13:06:47.7420000Z`; `75ms: 6aa413b141b41dbac0c7f1f9.jsonl[1975] _id=6aba671f485cab4c9567ad3d ts=2026-09-28T13:09:31.6150000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[2004] _id=6aba6720485cab4c9567ad41 ts=2026-09-28T13:09:31.6900000Z`; `30ms: 6aa413b141b41dbac0c7f1f9.jsonl[2012] _id=6aba6721485cab4c9567ad57 ts=2026-09-28T13:09:34.0390000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[2020] _id=6aba6721485cab4c9567ad5f ts=2026-09-28T13:09:34.0690000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `433ms: 6aa413b141b41dbac0c7f1f9.jsonl[13865] _id=6ac587f7de269131f9b875c2 ts=2026-10-06T23:42:45.5950000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[13856] _id=6ac587f7de269131f9b875c4 ts=2026-10-06T23:42:46.0280000Z`; `420ms: 6aa413b141b41dbac0c7f1f9.jsonl[13858] _id=6ac587fdde269131f9b875ce ts=2026-10-06T23:42:51.8480000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[13835] _id=6ac587fede269131f9b875d0 ts=2026-10-06T23:42:52.2680000Z`; `372ms: 6aa413b141b41dbac0c7f1f9.jsonl[13835] _id=6ac587fede269131f9b875d0 ts=2026-10-06T23:42:52.2680000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[13860] _id=6ac587fede269131f9b875d4 ts=2026-10-06T23:42:52.6400000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa413b141b41dbac0c7f1f9.jsonl[3127] _id=6aba6ab2485cab4c9567f25b ts=2026-09-28T13:25:06.4520000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[3129] _id=6aba6ab2485cab4c9567f269 ts=2026-09-28T13:25:06.4800000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `859ms: 6aa413b141b41dbac0c7f1f9.jsonl[6266] _id=6abd112b485cab4c9588e971 ts=2026-09-30T13:39:55.1680000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[6257] _id=6abd112c485cab4c9588e99d ts=2026-09-30T13:39:56.0270000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa413b141b41dbac0c7f1f9.jsonl[8759] _id=6ac3a478de269131f9a8bbd9 ts=2026-10-05T13:22:00.5100000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[8794] _id=6ac3a478de269131f9a8bbe3 ts=2026-10-05T13:22:00.5330000Z`; `14ms: 6aa413b141b41dbac0c7f1f9.jsonl[13685] _id=6ac5868fde269131f9b8746f ts=2026-10-06T23:36:45.2500000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[13688] _id=6ac5868fde269131f9b87472 ts=2026-10-06T23:36:45.2640000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 104 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6aa413b141b41dbac0c7f1f9.jsonl[1472] _id=6ab675cd485cab4c9554cab7 ts=2026-09-25T13:23:26.1410000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[1473] _id=6ab675cd485cab4c9554cabe ts=2026-09-25T13:23:26.1680000Z`; `12ms: 6aa413b141b41dbac0c7f1f9.jsonl[1473] _id=6ab675cd485cab4c9554cabe ts=2026-09-25T13:23:26.1680000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[1478] _id=6ab675ce485cab4c9554cac2 ts=2026-09-25T13:23:26.1800000Z`; `807ms: 6aa413b141b41dbac0c7f1f9.jsonl[1478] _id=6ab675ce485cab4c9554cac2 ts=2026-09-25T13:23:26.1800000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[1476] _id=6ab675ce485cab4c9554cae0 ts=2026-09-25T13:23:26.9870000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `313ms: 6aa413b141b41dbac0c7f1f9.jsonl[16282] _id=6ac5aa15de269131f9b89aba ts=2026-10-07T02:07:35.5370000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[16283] _id=6ac5aa15de269131f9b89abc ts=2026-10-07T02:07:35.8500000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa413b141b41dbac0c7f1f9.jsonl[5121] _id=6abd0797485cab4c958675bd ts=2026-09-30T12:59:01.3150000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[5122] _id=6abd0797485cab4c958675bf ts=2026-09-30T12:59:01.3220000Z`; `2ms: 6aa413b141b41dbac0c7f1f9.jsonl[16545] _id=6ac5ac19de269131f9b89e63 ts=2026-10-07T02:16:11.4770000Z ~ 6aa413b141b41dbac0c7f1f9.jsonl[16548] _id=6ac5ac19de269131f9b89e65 ts=2026-10-07T02:16:11.4790000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 93h 47m 
  - Evidence: 93h 47m: 6aa413b141b41dbac0c7f1f9.jsonl[8101] _id=6abe7895485cab4c95a9efc2 ts=2026-10-01T15:13:25.0250000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8172] _id=6ac39f6dde269131f9a840fa ts=2026-10-05T13:00:29.2860000Z; 71h 57m: 6aa413b141b41dbac0c7f1f9.jsonl[1029] _id=6ab6712d485cab4c95545f4b ts=2026-09-25T13:03:41.3430000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1710] _id=6aba6513485cab4c956799cd ts=2026-09-28T13:01:07.2830000Z; 24h 14m: 6aa413b141b41dbac0c7f1f9.jsonl[1710] _id=6aba6513485cab4c956799cd ts=2026-09-28T13:01:07.2830000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3717] _id=6abbb9df485cab4c957c5a7d ts=2026-09-29T13:15:11.8700000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 93h 46m 
  - Evidence: 93h 46m: 6aa413b141b41dbac0c7f1f9.jsonl[8165] _id=6abe78fd485cab4c95a9fc4c ts=2026-10-01T15:15:09.0370000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8195] _id=6ac39fbede269131f9a843ae ts=2026-10-05T13:01:50.5560000Z; 71h 31m: 6aa413b141b41dbac0c7f1f9.jsonl[1693] _id=6ab6775d485cab4c95550b06 ts=2026-09-25T13:30:06.2210000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1716] _id=6aba651a485cab4c956799fb ts=2026-09-28T13:01:14.4440000Z; 23h 37m: 6aa413b141b41dbac0c7f1f9.jsonl[712] _id=6ab3d663485cab4c954ca2e5 ts=2026-09-23T13:38:43.5620000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[802] _id=6ab522a1485cab4c95506217 ts=2026-09-24T13:16:17.9150000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 798 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13388] _id=6ac58715de269131f9b874d8 ts=2026-10-06T23:38:59.7080000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13739] _id=6ac58715de269131f9b874d9 ts=2026-10-06T23:38:59.7080000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13503] _id=6ac585c0de269131f9b87344 ts=2026-10-06T23:33:18.4550000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13504] _id=6ac585c0de269131f9b87345 ts=2026-10-06T23:33:18.4550000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13558] _id=6ac585fade269131f9b8738f ts=2026-10-06T23:34:15.3460000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13559] _id=6ac585fade269131f9b87390 ts=2026-10-06T23:34:15.3460000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 275h 45m 
  - Evidence: 275h 45m: 6aa413b141b41dbac0c7f1f9.jsonl[1694] _id=6ab67760485cab4c95550bbc ts=2026-09-25T13:30:08.6480000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[15087] _id=6ac59df8de269131f9b880ce ts=2026-10-07T01:15:54.7360000Z; 1h 5m: 6aa413b141b41dbac0c7f1f9.jsonl[15087] _id=6ac59df8de269131f9b880ce ts=2026-10-07T01:15:54.7360000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[16641] _id=6ac5ad44de269131f9b8a083 ts=2026-10-07T02:21:10.3820000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 93h 46m 
  - Evidence: 93h 46m: 6aa413b141b41dbac0c7f1f9.jsonl[8157] _id=6abe78df485cab4c95a9f876 ts=2026-10-01T15:14:39.3430000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8177] _id=6ac39f87de269131f9a841c2 ts=2026-10-05T13:00:55.3020000Z; 71h 31m: 6aa413b141b41dbac0c7f1f9.jsonl[1669] _id=6ab67734485cab4c955505c0 ts=2026-09-25T13:29:25.1420000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1709] _id=6aba6519485cab4c956799f1 ts=2026-09-28T13:01:13.1100000Z; 23h 42m: 6aa413b141b41dbac0c7f1f9.jsonl[925] _id=6ab523d4485cab4c9550a257 ts=2026-09-24T13:21:24.0830000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1038] _id=6ab67144485cab4c95546143 ts=2026-09-25T13:04:04.2660000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 294 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[12497] _id=6ac4f834de269131f9b0bb31 ts=2026-10-06T13:31:32.0350000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[12501] _id=6ac4f834de269131f9b0bb39 ts=2026-10-06T13:31:32.0350000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13324] _id=6ac58450de269131f9b871d4 ts=2026-10-06T23:27:10.2040000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13325] _id=6ac58450de269131f9b871d5 ts=2026-10-06T23:27:10.2040000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13918] _id=6ac58872de269131f9b876ca ts=2026-10-06T23:44:48.5910000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13919] _id=6ac58872de269131f9b876cb ts=2026-10-06T23:44:48.5910000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa413b141b41dbac0c7f1f9.jsonl[6621] _id=6abe5cba485cab4c95a48b5d ts=2026-10-01T13:14:34.6090000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8263] _id=6ac3a10ade269131f9a8580a ts=2026-10-05T13:07:22.2370000Z; 71h 36m: 6aa413b141b41dbac0c7f1f9.jsonl[1670] _id=6ab67736485cab4c95550632 ts=2026-09-25T13:29:27.1770000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1798] _id=6aba6627485cab4c9567a1bf ts=2026-09-28T13:05:43.0720000Z; 23h 44m: 6aa413b141b41dbac0c7f1f9.jsonl[927] _id=6ab523d5485cab4c9550a2ab ts=2026-09-24T13:21:25.4500000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1110] _id=6ab671bc485cab4c955469d5 ts=2026-09-25T13:06:04.5030000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13360] _id=6ac584bede269131f9b8723a ts=2026-10-06T23:29:00.2900000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13375] _id=6ac584bede269131f9b8723b ts=2026-10-06T23:29:00.2900000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13464] _id=6ac5852fde269131f9b872e8 ts=2026-10-06T23:30:53.4220000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13465] _id=6ac5852fde269131f9b872e9 ts=2026-10-06T23:30:53.4220000Z; 2ms: 6aa413b141b41dbac0c7f1f9.jsonl[12747] _id=6ac50a17de269131f9b3e6c6 ts=2026-10-06T14:47:51.0510000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[12744] _id=6ac50a17de269131f9b3e6d0 ts=2026-10-06T14:47:51.0530000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 93h 45m 
  - Evidence: 93h 45m: 6aa413b141b41dbac0c7f1f9.jsonl[8166] _id=6abe78fe485cab4c95a9fcaa ts=2026-10-01T15:15:10.9710000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8173] _id=6ac39f73de269131f9a84126 ts=2026-10-05T13:00:29.2930000Z; 23h 34m: 6aa413b141b41dbac0c7f1f9.jsonl[722] _id=6ab3d6c8485cab4c954caea3 ts=2026-09-23T13:40:24.6660000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[725] _id=6ab52271485cab4c9550583f ts=2026-09-24T13:15:22.6300000Z; 23h 32m: 6aa413b141b41dbac0c7f1f9.jsonl[1024] _id=6ab5260a485cab4c95511d14 ts=2026-09-24T13:30:50.1480000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1031] _id=6ab67134485cab4c95545fb7 ts=2026-09-25T13:03:41.3500000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[6270] _id=6abd1132485cab4c9588ea8a ts=2026-09-30T13:40:02.4470000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[6275] _id=6abe5830485cab4c95a3fed9 ts=2026-09-30T13:40:02.447Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6aa413b141b41dbac0c7f1f9.jsonl[5523] _id=6abd084c485cab4c958683ad ts=2026-09-30T13:02:02.5420000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8953] _id=6ac3a57fde269131f9a8fed3 ts=2026-10-05T13:26:22.3010000Z; 23h 39m: 6aa413b141b41dbac0c7f1f9.jsonl[3705] _id=6aba6eb7485cab4c95681abb ts=2026-09-28T13:42:14.8600000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3950] _id=6abbbb4c485cab4c957ca920 ts=2026-09-29T13:21:16.2740000Z; 23h 27m: 6aa413b141b41dbac0c7f1f9.jsonl[4936] _id=6abbbdcc485cab4c957d3d52 ts=2026-09-29T13:31:54.5340000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[5114] _id=6abd0797485cab4c958675c1 ts=2026-09-30T12:59:01.6350000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1707 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[10433] _id=6ac3be8fde269131f9ace0ed ts=2026-10-05T15:13:18.4500000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[10795] _id=6ac3be8fde269131f9ace0ef ts=2026-10-05T15:13:18.4500000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[10435] _id=6ac3be8fde269131f9ace0f9 ts=2026-10-05T15:13:18.7570000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[10797] _id=6ac3be8fde269131f9ace0fb ts=2026-10-05T15:13:18.7570000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[10436] _id=6ac3be90de269131f9ace0ff ts=2026-10-05T15:13:18.8000000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[10800] _id=6ac3be90de269131f9ace105 ts=2026-10-05T15:13:18.8000000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 5m 
  - Evidence: 144h 5m: 6aa413b141b41dbac0c7f1f9.jsonl[3931] _id=6abbbb13485cab4c957c9962 ts=2026-09-29T13:20:19.7510000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8923] _id=6ac3a544de269131f9a8f0a1 ts=2026-10-05T13:25:24.3760000Z; 23h 39m: 6aa413b141b41dbac0c7f1f9.jsonl[3611] _id=6aba6e4c485cab4c956817a5 ts=2026-09-28T13:40:28.0790000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3916] _id=6abbbb00485cab4c957c94a8 ts=2026-09-29T13:20:00.1210000Z; 21h 52m: 6aa413b141b41dbac0c7f1f9.jsonl[10466] _id=6ac3be39de269131f9acdba1 ts=2026-10-05T15:11:53.1580000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[11099] _id=6ac4f1d2de269131f9b00c44 ts=2026-10-06T13:04:18.1240000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 53m 3s 
  - Evidence: 53m 3s: 6aa413b141b41dbac0c7f1f9.jsonl[14184] _id=6ac58a59de269131f9b879c1 ts=2026-10-06T23:52:56.1450000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14341] _id=6ac596f5de269131f9b87b51 ts=2026-10-07T00:45:59.6760000Z; 19m 33s: 6aa413b141b41dbac0c7f1f9.jsonl[14068] _id=6ac59746de269131f9b87b97 ts=2026-10-07T00:47:20.3910000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14850] _id=6ac59bdcde269131f9b87f04 ts=2026-10-07T01:06:53.9890000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 95h 34m 
  - Evidence: 95h 34m: 6aa413b141b41dbac0c7f1f9.jsonl[7805] _id=6abe617a485cab4c95a60e21 ts=2026-10-01T13:34:50.1840000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8330] _id=6ac3a176de269131f9a85db8 ts=2026-10-05T13:09:10.1600000Z; 47h 41m: 6aa413b141b41dbac0c7f1f9.jsonl[3396] _id=6aba6d02485cab4c95680a03 ts=2026-09-28T13:34:58.8930000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[5764] _id=6abd0bb1485cab4c9586c219 ts=2026-09-30T13:16:33.3620000Z; 35h 51m: 6aa413b141b41dbac0c7f1f9.jsonl[8412] _id=6ac3a1bfde269131f9a86156 ts=2026-10-05T13:10:23.0680000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14715] _id=6ac59aa9de269131f9b87dd8 ts=2026-10-07T01:01:47.3030000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.028s..0.036s shown 
  - Evidence: 28ms: 6aa413b141b41dbac0c7f1f9.jsonl[3127] _id=6aba6ab2485cab4c9567f25b ts=2026-09-28T13:25:06.4520000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3129] _id=6aba6ab2485cab4c9567f269 ts=2026-09-28T13:25:06.4800000Z; 36ms: 6aa413b141b41dbac0c7f1f9.jsonl[3118] _id=6aba6ab2485cab4c9567f259 ts=2026-09-28T13:25:06.4160000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3127] _id=6aba6ab2485cab4c9567f25b ts=2026-09-28T13:25:06.4520000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 26m 2s 
  - Evidence: 26m 2s: 6aa413b141b41dbac0c7f1f9.jsonl[15407] _id=6ac59f46de269131f9b88312 ts=2026-10-07T01:21:28.2770000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[15614] _id=6ac5a560de269131f9b88bbe ts=2026-10-07T01:47:30.4410000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 11m 
  - Evidence: 120h 11m: 6aa413b141b41dbac0c7f1f9.jsonl[1516] _id=6ab676a5485cab4c9554ed60 ts=2026-09-25T13:27:01.5610000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[6189] _id=6abd10c9485cab4c9588ce91 ts=2026-09-30T13:38:17.1300000Z; 95h 40m: 6aa413b141b41dbac0c7f1f9.jsonl[8026] _id=6abe62f7485cab4c95a68005 ts=2026-10-01T13:41:11.7550000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8792] _id=6ac3a478de269131f9a8bbd1 ts=2026-10-05T13:22:00.4860000Z; 25h 30m: 6aa413b141b41dbac0c7f1f9.jsonl[8792] _id=6ac3a478de269131f9a8bbd1 ts=2026-10-05T13:22:00.4860000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[12919] _id=6ac50b47de269131f9b402a1 ts=2026-10-06T14:52:55.0180000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 10m 
  - Evidence: 120h 10m: 6aa413b141b41dbac0c7f1f9.jsonl[1557] _id=6ab676a5485cab4c9554ed64 ts=2026-09-25T13:27:01.5900000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[6164] _id=6abd10b0485cab4c9588c810 ts=2026-09-30T13:37:52.8380000Z; 95h 43m: 6aa413b141b41dbac0c7f1f9.jsonl[7864] _id=6abe624c485cab4c95a64de1 ts=2026-10-01T13:38:20.7460000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8770] _id=6ac3a46bde269131f9a8b98f ts=2026-10-05T13:21:47.5360000Z; 25h 29m: 6aa413b141b41dbac0c7f1f9.jsonl[8794] _id=6ac3a478de269131f9a8bbe3 ts=2026-10-05T13:22:00.5330000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[12861] _id=6ac50afcde269131f9b40025 ts=2026-10-06T14:51:40.4020000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.014s..0.023s shown 
  - Evidence: 14ms: 6aa413b141b41dbac0c7f1f9.jsonl[13685] _id=6ac5868fde269131f9b8746f ts=2026-10-06T23:36:45.2500000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13688] _id=6ac5868fde269131f9b87472 ts=2026-10-06T23:36:45.2640000Z; 23ms: 6aa413b141b41dbac0c7f1f9.jsonl[8759] _id=6ac3a478de269131f9a8bbd9 ts=2026-10-05T13:22:00.5100000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8794] _id=6ac3a478de269131f9a8bbe3 ts=2026-10-05T13:22:00.5330000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 120h 11m 
  - Evidence: 120h 11m: 6aa413b141b41dbac0c7f1f9.jsonl[1550] _id=6ab676a0485cab4c9554ec8e ts=2026-09-25T13:26:57.1510000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[6167] _id=6abd10b8485cab4c9588ca22 ts=2026-09-30T13:38:00.0500000Z; 95h 40m: 6aa413b141b41dbac0c7f1f9.jsonl[8094] _id=6abe6306485cab4c95a682a1 ts=2026-10-01T13:41:26.7280000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8762] _id=6ac3a464de269131f9a8b83b ts=2026-10-05T13:21:40.0270000Z; 25h 29m: 6aa413b141b41dbac0c7f1f9.jsonl[8786] _id=6ac3a474de269131f9a8bb29 ts=2026-10-05T13:21:56.8750000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[12859] _id=6ac50af7de269131f9b3fffd ts=2026-10-06T14:51:35.8700000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 223 interval(s) ≤ 0.012s..0.016s shown 
  - Evidence: 12ms: 6aa413b141b41dbac0c7f1f9.jsonl[1473] _id=6ab675cd485cab4c9554cabe ts=2026-09-25T13:23:26.1680000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1478] _id=6ab675ce485cab4c9554cac2 ts=2026-09-25T13:23:26.1800000Z; 15ms: 6aa413b141b41dbac0c7f1f9.jsonl[13511] _id=6ac585d0de269131f9b87361 ts=2026-10-06T23:33:35.0460000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13512] _id=6ac585d0de269131f9b87363 ts=2026-10-06T23:33:35.0610000Z; 16ms: 6aa413b141b41dbac0c7f1f9.jsonl[13515] _id=6ac585c0de269131f9b87347 ts=2026-10-06T23:33:19.1190000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13505] _id=6ac585c0de269131f9b87349 ts=2026-10-06T23:33:19.1350000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 156h 29m 
  - Evidence: 156h 29m: 6aa413b141b41dbac0c7f1f9.jsonl[6188] _id=6abd10c5485cab4c9588cd6a ts=2026-09-30T13:38:13.5910000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[16282] _id=6ac5aa15de269131f9b89aba ts=2026-10-07T02:07:35.5370000Z; 120h 11m: 6aa413b141b41dbac0c7f1f9.jsonl[1528] _id=6ab6768e485cab4c9554ea6a ts=2026-09-25T13:26:38.6410000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[6188] _id=6abd10c5485cab4c9588cd6a ts=2026-09-30T13:38:13.5910000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 38m 55s 
  - Evidence: 38m 55s: 6aa413b141b41dbac0c7f1f9.jsonl[15091] _id=6ac59e0bde269131f9b880df ts=2026-10-07T01:16:12.9920000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[15965] _id=6ac5a72ade269131f9b88fd2 ts=2026-10-07T01:55:08.1850000Z; 14m 29s: 6aa413b141b41dbac0c7f1f9.jsonl[14706] _id=6ac59aa5de269131f9b87dd2 ts=2026-10-07T01:01:43.2870000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[15091] _id=6ac59e0bde269131f9b880df ts=2026-10-07T01:16:12.9920000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 93h 46m 
  - Evidence: 93h 46m: 6aa413b141b41dbac0c7f1f9.jsonl[8100] _id=6abe788d485cab4c95a9eeb7 ts=2026-10-01T15:13:17.4440000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8171] _id=6ac39f5ade269131f9a84046 ts=2026-10-05T13:00:10.4960000Z; 71h 29m: 6aa413b141b41dbac0c7f1f9.jsonl[1696] _id=6ab677b5485cab4c95551170 ts=2026-09-25T13:31:33.3950000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1705] _id=6aba6502485cab4c95679991 ts=2026-09-28T13:00:50.5470000Z; 24h 14m: 6aa413b141b41dbac0c7f1f9.jsonl[1705] _id=6aba6502485cab4c95679991 ts=2026-09-28T13:00:50.5470000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3716] _id=6abbb9d8485cab4c957c5980 ts=2026-09-29T13:15:04.3650000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 93h 46m 
  - Evidence: 93h 46m: 6aa413b141b41dbac0c7f1f9.jsonl[8099] _id=6abe788d485cab4c95a9eeb2 ts=2026-10-01T15:13:17.4430000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8169] _id=6ac39f5ade269131f9a84042 ts=2026-10-05T13:00:10.4950000Z; 71h 29m: 6aa413b141b41dbac0c7f1f9.jsonl[1695] _id=6ab677b5485cab4c9555116b ts=2026-09-25T13:31:33.3940000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1704] _id=6aba6502485cab4c9567998f ts=2026-09-28T13:00:50.5450000Z; 24h 14m: 6aa413b141b41dbac0c7f1f9.jsonl[1704] _id=6aba6502485cab4c9567998f ts=2026-09-28T13:00:50.5450000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[3715] _id=6abbb9d8485cab4c957c5978 ts=2026-09-29T13:15:04.3640000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 154h 47m 
  - Evidence: 154h 47m: 6aa413b141b41dbac0c7f1f9.jsonl[5203] _id=6abd07cd485cab4c95867921 ts=2026-09-30T12:59:57.2100000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14044] _id=6ac58927de269131f9b878c3 ts=2026-10-06T23:47:50.1730000Z; 143h 43m: 6aa413b141b41dbac0c7f1f9.jsonl[806] _id=6ab522a5485cab4c95506261 ts=2026-09-24T13:16:22.0270000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[5203] _id=6abd07cd485cab4c95867921 ts=2026-09-30T12:59:57.2100000Z; 14m 37s: 6aa413b141b41dbac0c7f1f9.jsonl[14044] _id=6ac58927de269131f9b878c3 ts=2026-10-06T23:47:50.1730000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14348] _id=6ac58c95de269131f9b87b04 ts=2026-10-07T00:02:27.6630000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 93h 47m 
  - Evidence: 93h 47m: 6aa413b141b41dbac0c7f1f9.jsonl[8103] _id=6abe789a485cab4c95a9f05e ts=2026-10-01T15:13:30.1870000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[8174] _id=6ac39f73de269131f9a8412a ts=2026-10-05T13:00:34.8640000Z; 71h 34m: 6aa413b141b41dbac0c7f1f9.jsonl[1672] _id=6ab67739485cab4c955506a2 ts=2026-09-25T13:29:29.3110000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[1755] _id=6aba65c5485cab4c9567a043 ts=2026-09-28T13:04:05.3920000Z; 23h 45m: 6aa413b141b41dbac0c7f1f9.jsonl[5668] _id=6abd0a4a485cab4c9586a083 ts=2026-09-30T13:10:34.3150000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[6272] _id=6abe585d485cab4c95a40049 ts=2026-10-01T12:55:56.6720000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[13921] _id=6ac58872de269131f9b876cd ts=2026-10-06T23:44:48.6150000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[13922] _id=6ac58872de269131f9b876ce ts=2026-10-06T23:44:48.6150000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[14012] _id=6ac58980de269131f9b878dd ts=2026-10-06T23:49:18.8210000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14013] _id=6ac58980de269131f9b878de ts=2026-10-06T23:49:18.8210000Z; 0ms: 6aa413b141b41dbac0c7f1f9.jsonl[14362] _id=6ac596aade269131f9b87b16 ts=2026-10-07T00:44:44.7200000Z -> 6aa413b141b41dbac0c7f1f9.jsonl[14363] _id=6ac596aade269131f9b87b17 ts=2026-10-07T00:44:44.7200000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1404] _id=6ab67564485cab4c9554bab4 ts=2026-09-25T13:21:40.8050000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[3254] _id=6aba6c08485cab4c9568004d ts=2026-09-28T13:30:48.8380000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[4725] _id=6abbbd88485cab4c957d290e ts=2026-09-29T13:30:48.5900000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 61 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[2044] _id=6aba6724485cab4c9567adb5 ts=2026-09-28T13:09:55.7260000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[2077] _id=6aba672a485cab4c9567ae0f ts=2026-09-28T13:10:00.7920000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[2245] _id=6aba6761485cab4c9567b13f ts=2026-09-28T13:10:56.1640000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 199 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1897] _id=6aba6719485cab4c9567ac0a ts=2026-09-28T13:06:47.6750000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1931] _id=6aba6719485cab4c9567ac2b ts=2026-09-28T13:06:49.2510000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1900] _id=6aba671a485cab4c9567ac3b ts=2026-09-28T13:06:49.5060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1483] _id=6ab675d4485cab4c9554cb9e ts=2026-09-25T13:23:32.1960000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[6168] _id=6abd10b8485cab4c9588ca42 ts=2026-09-30T13:38:00.3450000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[7946] _id=6abe6276485cab4c95a65ae9 ts=2026-10-01T13:39:02.6310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[15091] _id=6ac59e0bde269131f9b880df ts=2026-10-07T01:16:12.9920000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[15965] _id=6ac5a72ade269131f9b88fd2 ts=2026-10-07T01:55:08.1850000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[11532] _id=6ac4f333de269131f9b02160 ts=2026-10-06T13:10:11.7610000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[13] _id=6ab3cf27485cab4c954b86d6 ts=?`; `6aa413b141b41dbac0c7f1f9.jsonl[735] _id=6ab52271485cab4c95505839 ts=?`; `6aa413b141b41dbac0c7f1f9.jsonl[1714] _id=6aba6519485cab4c956799eb ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 382 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[2060] _id=6aba6727485cab4c9567addb ts=2026-09-28T13:09:57.8980000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[2062] _id=6aba6727485cab4c9567adeb ts=2026-09-28T13:09:58.8250000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[2047] _id=6aba672a485cab4c9567ae1b ts=2026-09-28T13:10:01.7700000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 449 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1929] _id=6aba6719485cab4c9567ac13 ts=2026-09-28T13:06:47.7220000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1930] _id=6aba6719485cab4c9567ac17 ts=2026-09-28T13:06:47.7420000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1920] _id=6aba6719485cab4c9567ac1f ts=2026-09-28T13:06:47.8130000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 19 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[3127] _id=6aba6ab2485cab4c9567f25b ts=2026-09-28T13:25:06.4520000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[3129] _id=6aba6ab2485cab4c9567f269 ts=2026-09-28T13:25:06.4800000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[3214] _id=6aba6b77485cab4c9567fa53 ts=2026-09-28T13:28:23.3230000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[8770] _id=6ac3a46bde269131f9a8b98f ts=2026-10-05T13:21:47.5360000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[13514] _id=6ac585c0de269131f9b87342 ts=2026-10-06T23:33:18.4530000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 119 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1473] _id=6ab675cd485cab4c9554cabe ts=2026-09-25T13:23:26.1680000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1478] _id=6ab675ce485cab4c9554cac2 ts=2026-09-25T13:23:26.1800000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1476] _id=6ab675ce485cab4c9554cae0 ts=2026-09-25T13:23:26.9870000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1527] _id=6ab6768d485cab4c9554ea42 ts=2026-09-25T13:26:37.6800000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[16283] _id=6ac5aa15de269131f9b89abc ts=2026-10-07T02:07:35.8500000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[16284] _id=6ac5aa18de269131f9b89ac0 ts=2026-10-07T02:07:38.1490000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 523 start, 517 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 78 unmatched 'BecameCameraCentered' (totals: 585 open, 568 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 96 unmatched 'BecameVisible' (totals: 785 open, 888 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 21 open, 19 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 8 open, 7 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationNodeHoverStart' (totals: 383 open, 389 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 7 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 28 unmatched 'questActiveEvent' (totals: 61 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 283 of 16642 adjacent _id pairs reverse in client time; worst 176.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f9.jsonl[1886] _id=6aba6717485cab4c9567abbd ts=2026-09-28T13:09:43.4950000Z`; `6aa413b141b41dbac0c7f1f9.jsonl[1887] _id=6aba6718485cab4c9567abcb ts=2026-09-28T13:06:47.0820000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -83710.16s, max +13.36s over 16643 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f9\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 6522 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1531); Unit 2 Prod (Refactor) (1348); Unit 4 Dev (845); Unit 1 Dev (806); Unit 3 Dungeon Dev (738); Unit 4 Dev - Dungeon (644); Unit 5 Dev - Dungeon (312); Unit 4 Dev - Anderson Base (186); Unit 5 Dev (112)
- **Intervals:** median 0.53s (p5 0.06s / p95 9.86s, n=6521)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 6522/6522 records)
    "pressed"  x6522
data.actionType  (string, 6522/6522 records)
    "Move"  x5441
    "Interact"  x727
    "Jump"  x221
    "Ascend"  x93
    "Hoverboard"  x29
    "Map"  x9
    "Pause"  x2
data.key  (string, 6522/6522 records, 7 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 6522/6522 records)
    "Player"  x4930
    "Drone"  x1592
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2882 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (660); Unit 4 Dev (470); Unit 1 Dev (447); Unit 3 Dev (421); Unit 5 Dev - Dungeon (234); Unit 4 Dev - Anderson Base (199); Unit 3 Dungeon Dev (176); Unit 5 Dev (153); Unit 4 Dev - Dungeon (122)
- **Intervals:** median 10.00s (p5 9.99s / p95 10.02s, n=2867)
- **Fields under `data`:**

```text
data.position  (object, 2882/2882 records)
data.position.x  (number, 2882/2882 records)
    numeric range -624.911 .. 1576.2 (736 unique)
data.position.y  (number, 2882/2882 records)
    numeric range -112.489 .. 220.466 (579 unique)
data.position.z  (number, 2882/2882 records)
    numeric range -1036.31 .. 2188 (737 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 2826 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1772); Unit 4 Dev (634); Unit 3 Dungeon Dev (214); Unit 5 Dev - Dungeon (206)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.45s, n=2825)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2826/2826 records)
    "BecameInvisible"  x888
    "BecameVisible"  x785
    "BecameCameraCentered"  x585
    "BecameCameraUncentered"  x568
data.pieceId  (string, 2826/2826 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2826/2826 records)
    1848 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2697 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (614); Unit 4 Dev (559); Unit 3 Dev (455); Unit 1 Dev (299); Unit 5 Dev (217); Unit 4 Dev - Anderson Base (197); Unit 3 Dungeon Dev (184); Unit 4 Dev - Dungeon (95); Unit 5 Dev - Dungeon (77)
- **eventKey:** present on 1657 of 2697 records
- **Intervals:** median 4.58s (p5 0.00s / p95 33.89s, n=2696)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1657; [conversationId, dialogueEventType] x1040
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2697/2697 records)
    numeric range 8 .. 118 (54 unique)
data.dialogueEventType  (string, 2697/2697 records)
    "DialogueNodeEvent"  x1657
    "DialogueStartEvent"  x523
    "DialogueFinishEvent"  x517
data.nodeId  (number, 1657/2697 records)
    numeric range 0 .. 290 (213 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 896 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (434); Unit 3 Dev (184); Unit 5 Dev (166); Unit 2 Prod (Refactor) (73); Unit 1 Dev (39)
- **Intervals:** median 0.38s (p5 0.02s / p95 8.83s, n=895)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 896/896 records)
    "argumentationNodeHoverEnd"  x389
    "argumentationNodeHoverStart"  x383
    "argumentationNodeAdd"  x73
    "argumentationNodeRemove"  x51
data.argumentationTitle  (string, 896/896 records)
    "Unit 4 - Flooding"  x434
    "Unit 3 - Pollution Upstream"  x184
    "Unit 5"  x166
    "Unit 2 – Watershed"  x73
    "Unit 1 - Freshwater"  x23
    "Unit 1 - Argumentation Tutorial"  x16
data.nodeName  (string, 896/896 records)
    "C"  x102
    "B"  x100
    "1"  x97
    "D"  x97
    "4"  x89
    "2"  x83
    "A"  x83
    "I"  x83
    "II"  x78
    "3"  x61
    "5"  x23
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 330 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (70); Unit 4 Dev (68); Unit 1 Dev (64); Unit 3 Dungeon Dev (51); Unit 2 Prod (Refactor) (38); Unit 4 Dev - Anderson Base (19); Unit 5 Dev (8); Unit 3 Dev (7); Unit 5 Dev - Dungeon (5)
- **Intervals:** median 10.99s (p5 0.24s / p95 945.67s, n=329)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 330/330 records)
    39 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 330/330 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 95 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev (21); Unit 1 Dev (18); Unit 2 Prod (Refactor) (17); Unit 3 Dev (9); Unit 4 Dev - Dungeon (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 95 of 95 records
- **Intervals:** median 254.38s (p5 0.00s / p95 85099.39s, n=94)
- **`data` key-set variants:** [questEventType, questID, questName] x61; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 95/95 records)
    "questActiveEvent"  x61
    "questFinishEvent"  x34
data.questID  (string, 95/95 records)
    31 unique values (see csv/event_unique_values.csv)
data.questName  (string, 95/95 records)
    31 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/95 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 76 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 4 Dev (27); Unit 3 Dev (22)
- **Intervals:** median 3.70s (p5 0.32s / p95 26456.86s, n=75)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, location] x26; [actionType, featureUsed, legendName] x10
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 76/76 records)
    "MapOpenEvent"  x21
    "MapCloseEvent"  x19
    "WaypointMoveEvent"  x18
    "Selected"  x9
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x3
    "Unselected"  x1
data.featureUsed  (string, 76/76 records)
    "Map"  x40
    "Waypoint"  x26
    "Legend"  x10
data.legendName  (string, 10/76 records)
    "270 ft"  x2
    "0 ft"  x1
    "150 ft"  x1
    "180 ft"  x1
    "210 ft"  x1
    "300 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
    "90 ft"  x1
data.location  (object, 26/76 records)
data.location.x  (number, 26/76 records)
    numeric range -337.09 .. 450.146 (20 unique)
data.location.y  (number, 26/76 records)
    numeric range -316.718 .. 290.5 (20 unique)
data.location.z  (number, 26/76 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 56 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev (22); Unit 3 Dev (8)
- **Intervals:** median 1.65s (p5 0.39s / p95 28069.37s, n=55)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x44; [Soil Key Puzzle Status, Unit] x12
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/56 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/56 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 44/56 records)
    "RightDrag"  x27
    "LeftDrag"  x17
data.currentSoilType  (string, 44/56 records)
    "CLAYSAND"  x10
    "CLAY"  x9
    "SAND"  x8
    "CLAYROCK"  x7
    "SANDGRAVEL"  x5
    "GRAVEL"  x3
    "BEDROCK"  x2
data.isCorrectSelection  (string, 44/56 records)
    "false"  x32
    "true"  x12
data.waterLevelStatus  (string, 44/56 records)
    "TooHigh"  x18
    "Proper"  x13
    "TooLow"  x13
data.waterRetentionChange  (string, 44/56 records)
    "Increase"  x19
    "Decrease"  x13
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 44 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (44)
- **Intervals:** median 2.12s (p5 0.17s / p95 280.55s, n=43)
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records, 13 empty-string)
    "cameraPlaced"  x31
    ""  x13
data.boxId  (string, 44/44 records)
    "2"  x20
    "1"  x15
    "0"  x9
data.soilType  (string, 44/44 records)
    "None"  x20
    "Sand"  x11
    "Clay"  x7
    "Gravel"  x6
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationAnswerEvent` — 38 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (17); Unit 3 Dev (10); Unit 2 Prod (Refactor) (6); Unit 5 Dev (4); Unit 1 Dev (1)
- **Intervals:** median 16.51s (p5 2.60s / p95 142373.37s, n=37)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "submitAnswerEvent"  x38
data.answerSubmitted  (string, 38/38 records)
    22 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 38/38 records)
    "Unit 4 - Flooding"  x17
    "Unit 3 - Pollution Upstream"  x10
    "Unit 2 – Watershed"  x6
    "Unit 5"  x4
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 35 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (35)
- **Intervals:** median 7.71s (p5 1.38s / p95 51.30s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "On"  x23
    "Off"  x12
data.floor  (string, 35/35 records)
    "4"  x18
    "3"  x10
    "1"  x4
    "2"  x3
data.machineNumber  (string, 35/35 records)
    "One"  x34
    "Two"  x1
data.machineType  (string, 35/35 records)
    "Condenser"  x16
    "Evaporator"  x14
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 35/35 records)
    "3"  x16
    "2"  x13
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 34 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 4 Dev (8); MainMenu (6); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1179.11s (p5 4.81s / p95 155965.13s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "DebugMenuStateChanged"  x34
data.isOpened  (bool, 34/34 records)
    false  x34
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 26 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (23); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1)
- **Intervals:** median 3303.82s (p5 80.15s / p95 223336.48s, n=25)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 26/26 records)
    true  x26
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 6332.73s (p5 189.46s / p95 248851.99s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 15 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 235.05s (p5 0.02s / p95 375422.35s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 15/15 records)
    "argumentationSessionOpen"  x8
    "argumentationSessionClose"  x7
data.argumentationDescription  (string, 15/15 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x4
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x4
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x1
data.argumentationTitle  (string, 15/15 records)
    "Unit 3 - Pollution Upstream"  x4
    "Unit 4 - Flooding"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 14 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 4 Dev (14)
- **Intervals:** median 4.32s (p5 2.22s / p95 103.17s, n=13)
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "Close"  x7
    "Open"  x7
data.toolName  (string, 14/14 records, 14 empty-string)
    ""  x14
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 5 Dev (6); Unit 1 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 0.96s (p5 0.09s / p95 511095.15s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolOpen"  x7
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 10/10 records)
    "Unit 5"  x6
    "Unit 1 - Freshwater"  x3
    "Unit 2 – Watershed"  x1
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x5
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `chatEvent` — 8 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 4 Dev (6); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 3.60s (p5 0.95s / p95 1895.55s, n=7)
- **`data` key-set variants:** [actionType, chatID] x6; [actionKey, chatID] x2
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 2/8 records)
    "ScrollStop"  x2
data.actionType  (string, 6/8 records)
    "Close"  x3
    "ScrollStart"  x2
    "Open"  x1
data.chatID  (string, 8/8 records)
    "NA"  x5
    "[105-7, 105-8, 105-10, 105-12, 105-14]"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `SolarStillDesignEvent` — 6 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (6)
- **Intervals:** median 3.22s (p5 1.61s / p95 5.85s, n=5)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x5; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "optionSelected"  x5
    "DesignSubmitted"  x1
data.designSelections  (object, 1/6 records)
data.designSelections.glassRoofTemperature  (string, 1/6 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/6 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/6 records)
    "Tilted Out"  x1
data.featureUsed  (string, 6/6 records)
    "ExtraCovering"  x2
    "RoofStyle"  x2
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 5/6 records)
    "Cold"  x1
    "Covered"  x1
    "Tilted In"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameWindowUnfocusEvent` — 4 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 517415.18s (p5 52531.26s / p95 553287.18s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 4/4 records)
    false  x4
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 498330.87s (p5 53357.17s / p95 943304.57s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
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
    "unit1"  x2
    "unit2"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `soilMachine` — 3 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (3)
- **Intervals:** median 10.28s (p5 2.78s / p95 17.78s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "ChangeCanister"  x3
data.canisterType  (string, 3/3 records)
    "Sand"  x2
    "Gravel"  x1
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
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (26 records)
- `TerasGardenBox` data.actionType: "" (13x)
- `TerasGardenBox` data.soilType: "None" (20x)
- `TopographicMapEvent` data.actionType: "Selected" (9x); "Unselected" (1x); "WaypointMoveEvent" (18x); "WaypointResetEvent" (3x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (10x); "Waypoint" (26x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (51x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*