# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26a

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26a
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f26a.jsonl
- **Records:** 12294 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f26a
- **Time span:** 2026-09-28T18:17:18.765000+00:00 .. 2026-10-06T18:29:50.118000+00:00 (192h 12m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26a\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 12294 records, 10 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 100 INFO, 0 NOT_TESTED, 95 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4423 | 35.98 | 1 | 4 | 0 | 2026-09-29T18:36:57.571000+00:00 | 2026-10-06T15:09:55.808000+00:00 | 164h 32m |
| InputEvent | 2883 | 23.45 | 1 | 9 | 0 | 2026-09-28T18:17:33.960000+00:00 | 2026-10-06T18:29:50.118000+00:00 | 192h 12m |
| DialogueEvent | 1982 | 16.12 | 1 | 9 | 1221 | 2026-09-28T18:17:50.667000+00:00 | 2026-10-06T18:29:44.888000+00:00 | 192h 11m |
| PlayerPositionEvent | 1600 | 13.01 | 1 | 9 | 0 | 2026-09-28T18:17:28.453000+00:00 | 2026-10-06T18:29:47.818000+00:00 | 192h 12m |
| argumentationNodeEvent | 543 | 4.42 | 1 | 4 | 0 | 2026-09-28T18:41:01.787000+00:00 | 2026-10-06T18:18:15.233000+00:00 | 191h 37m |
| ObjectInterEvent | 307 | 2.5 | 1 | 9 | 0 | 2026-09-28T18:24:44.647000+00:00 | 2026-10-06T18:29:50.118000+00:00 | 192h 5m |
| Soil Key Puzzle | 166 | 1.35 | 1 | 3 | 0 | 2026-09-29T18:45:09.838000+00:00 | 2026-10-05T18:07:52.521000+00:00 | 143h 22m |
| questEvent | 86 | 0.7 | 1 | 9 | 86 | 2026-09-28T18:17:50.651000+00:00 | 2026-10-06T18:25:49.521000+00:00 | 192h 7m |
| argumentationAnswerEvent | 50 | 0.41 | 1 | 4 | 0 | 2026-09-28T18:42:32.032000+00:00 | 2026-10-06T18:18:16.620000+00:00 | 191h 35m |
| TopographicMapEvent | 46 | 0.37 | 1 | 3 | 0 | 2026-09-29T18:24:40.773000+00:00 | 2026-09-30T19:53:59.971000+00:00 | 25h 29m |
| WaterChamberEvent | 38 | 0.31 | 1 | 1 | 0 | 2026-10-06T15:06:43.355000+00:00 | 2026-10-06T18:09:02.548000+00:00 | 3h 2m |
| gameWindowFocusEvent | 33 | 0.27 | 1 | 6 | 0 | 2026-09-28T18:17:18.765000+00:00 | 2026-10-06T18:21:58.990000+00:00 | 192h 4m |
| DEBUGMenu | 28 | 0.23 | 1 | 8 | 0 | 2026-09-28T18:17:28.447000+00:00 | 2026-10-06T18:03:48.118000+00:00 | 191h 46m |
| gameStartEvent | 22 | 0.18 | 1 | 1 | 0 | 2026-09-28T18:17:18.766000+00:00 | 2026-10-06T18:03:25.819000+00:00 | 191h 46m |
| soilMachine | 22 | 0.18 | 1 | 1 | 0 | 2026-10-05T18:29:19.178000+00:00 | 2026-10-05T18:37:55.770000+00:00 | 8m 36s |
| gameWindowUnfocusEvent | 16 | 0.13 | 1 | 7 | 0 | 2026-09-29T18:17:52.600000+00:00 | 2026-10-06T18:21:49.630000+00:00 | 168h 3m |
| argumentationToolEvent | 13 | 0.11 | 1 | 2 | 0 | 2026-09-28T18:41:42.264000+00:00 | 2026-09-30T18:16:45.061000+00:00 | 47h 35m |
| argumentationEvent | 12 | 0.1 | 1 | 4 | 0 | 2026-09-28T18:41:45.095000+00:00 | 2026-10-06T18:18:16.663000+00:00 | 191h 36m |
| TerasGardenBox | 7 | 0.06 | 1 | 1 | 0 | 2026-10-06T14:53:55.856000+00:00 | 2026-10-06T14:54:47.547000+00:00 | 51.7s |
| crash | 6 | 0.05 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-28T18:47:20.988000+00:00 | 2026-10-06T18:29:50.075000+00:00 | 191h 42m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-06T18:22:07.278000+00:00 | 2026-10-06T18:22:21.306000+00:00 | 14.0s |
| chatEvent | 3 | 0.02 | 1 | 2 | 0 | 2026-10-06T15:02:57.021000+00:00 | 2026-10-06T18:10:01.786000+00:00 | 3h 7m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 177221.454s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.3s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 0.362s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 5.534s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.358s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 12.276s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 10.712s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.295s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 5612.382s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 1186.397s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 411.645s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 774.147s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.534s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
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
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 4.4x vs baseline. 
  - Observed: 166 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Gravel 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 10.0x vs baseline. 
  - Observed: 50 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,I; A,2,II; A,3,; A,3,I; A,3,II; A,4,I; A,4,II; A,B,2,II; A,B,3,I; A,C,2,II; A,C,B,2,II; A,D,2,II; B,3,I; B,3,II; B,4,II; C,4,II; C,D,3,II; C,D,A,2,II; C,D,B,2,II; D,C,2,II 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.9x vs baseline. 
  - Observed: 543 records 
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
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.7x vs baseline. 
  - Observed: 22 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.4x vs baseline. 
  - Observed: 22 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 45 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[171] _id=6abab15b485cab4c956ffbdd ts=2026-09-28T18:26:35.2800000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[222] _id=6abab234485cab4c95700b79 ts=2026-09-28T18:30:12.7510000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[258] _id=6abab26e485cab4c95700ee7 ts=2026-09-28T18:31:09.9780000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[3778] _id=6abd00e9485cab4c9586564f ts=2026-09-30T12:30:32.3780000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[4823] _id=6abd1ff0485cab4c958b549e ts=2026-09-30T14:42:57.4990000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[4805] _id=6abd1ff0485cab4c958b54a3 ts=2026-09-30T14:42:57.5060000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 22 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 22} 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[3] _id=6abaaf2e485cab4c956fbba9 ts=2026-09-28T18:17:18.7660000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[624] _id=6abbff46485cab4c95841ee5 ts=2026-09-29T18:11:18.7140000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[625] _id=6abbffba485cab4c958424fd ts=2026-09-29T18:13:14.6400000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 33 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 33} 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[2] _id=6abaaf2e485cab4c956fbba3 ts=2026-09-28T18:17:18.7650000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[623] _id=6abbff46485cab4c95841ee1 ts=2026-09-29T18:11:18.7130000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[637] _id=6abbffba485cab4c958424fb ts=2026-09-29T18:13:14.6390000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[729] _id=6abc00d1485cab4c9584443f ts=2026-09-29T18:17:52.6000000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[735] _id=6abc010d485cab4c95844ccd ts=2026-09-29T18:17:52.6Z`; `6aa4144c41b41dbac0c7f26a.jsonl[3751] _id=6abd00aa485cab4c95865427 ts=2026-09-30T12:29:30.0340000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4422 | 0.0 | 0.025 | 133.962 | 1.28 | 364609.258 | 0.45 | 2801 | 8 |
| InputEvent | 2882 | 0.001 | 1.3 | 240.089 | 19.537 | 364449.555 | 0.25 | 103 | 10 |
| DialogueEvent | 1981 | 0.001 | 3.299 | 349.275 | 27.112 | 364474.969 | 0.17 | 590 | 9 |
| PlayerPositionEvent | 1588 | 9.345 | 10.0 | 397.716 | 10.52 | 364421.975 | 0.15 | 0 | 8 |
| argumentationNodeEvent | 542 | 0.002 | 0.248 | 1272.755 | 7.571 | 505650.32 | 0.05 | 144 | 3 |
| ObjectInterEvent | 306 | 0.001 | 8.244 | 2259.822 | 407.714 | 364578.541 | 0.03 | 3 | 12 |
| Soil Key Puzzle | 165 | 0.122 | 0.362 | 3128.259 | 9.025 | 364571.824 | 0.02 | 0 | 4 |
| questEvent | 85 | 0.001 | 158.25 | 8137.398 | 50413.545 | 364689.347 | 0.01 | 19 | 15 |
| argumentationAnswerEvent | 49 | 0.46 | 10.712 | 14076.42 | 7545.233 | 505663.365 | 0.0 | 0 | 3 |
| TopographicMapEvent | 45 | 1.615 | 12.276 | 2039.093 | 7844.143 | 63286.232 | 0.03 | 0 | 7 |
| WaterChamberEvent | 37 | 0.821 | 10.81 | 295.654 | 69.551 | 10187.753 | 0.2 | 0 | 1 |
| gameWindowFocusEvent | 32 | 19.857 | 411.645 | 21608.757 | 78756.406 | 364414.235 | 0.0 | 0 | 14 |
| DEBUGMenu | 27 | 66.803 | 716.599 | 25569.617 | 81737.699 | 364880.757 | 0.0 | 0 | 17 |
| gameStartEvent | 21 | 64.035 | 1186.397 | 32874.622 | 86039.948 | 364889.243 | 0.0 | 0 | 13 |
| soilMachine | 21 | 0.382 | 5.534 | 24.6 | 109.544 | 168.425 | 2.44 | 0 | 0 |
| gameWindowUnfocusEvent | 15 | 0.0 | 774.147 | 40335.802 | 161186.984 | 366892.66 | 0.0 | 1 | 8 |
| argumentationToolEvent | 12 | 0.104 | 3.295 | 14275.233 | 77043.076 | 170929.855 | 0.0 | 0 | 1 |
| argumentationEvent | 11 | 0.026 | 57.297 | 62708.324 | 338281.943 | 505656.728 | 0.0 | 2 | 3 |
| TerasGardenBox | 6 | 0.945 | 1.358 | 8.615 | 25.289 | 27.13 | 6.96 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 3 | 12429.645 | 177221.454 | 230049.696 | 468170.335 | 500497.988 | 0.0 | 0 | 3 |
| SolarStillDesignEvent | 3 | 1.378 | 5.534 | 4.676 | 6.958 | 7.116 | 12.83 | 0 | 0 |
| chatEvent | 2 | 373.777 | 5612.382 | 5612.382 | 10327.127 | 10850.988 | 0.01 | 0 | 1 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 185 group(s), 264 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[1097] _id=6abc0561485cab4c958497a9 ts=2026-09-29T18:37:21.4470000Z == 6aa4144c41b41dbac0c7f26a.jsonl[1108] _id=6abc0561485cab4c958497ab ts=2026-09-29T18:37:21.4470000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1137] _id=6abc0563485cab4c958497db ts=2026-09-29T18:37:21.6020000Z == 6aa4144c41b41dbac0c7f26a.jsonl[1138] _id=6abc0563485cab4c958497df ts=2026-09-29T18:37:21.6020000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1116] _id=6abc0565485cab4c95849823 ts=2026-09-29T18:37:23.3110000Z == 6aa4144c41b41dbac0c7f26a.jsonl[1131] _id=6abc0565485cab4c95849825 ts=2026-09-29T18:37:23.3110000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[629] _id=6abbff67485cab4c958420e9 ts=? == 6aa4144c41b41dbac0c7f26a.jsonl[703] _id=6abc0073485cab4c95843679 ts=?`; `6aa4144c41b41dbac0c7f26a.jsonl[2771] _id=6abcfc4a485cab4c95864901 ts=? == 6aa4144c41b41dbac0c7f26a.jsonl[4815] _id=6abd1fee485cab4c958b5479 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 33 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f26a.jsonl[144] _id=6abab0ec485cab4c956ff4d9 ts=2026-09-28T18:24:44.6470000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[122] _id=6abab0ec485cab4c956ff4dd ts=2026-09-28T18:24:44.6510000Z`; `261ms: 6aa4144c41b41dbac0c7f26a.jsonl[619] _id=6abbff9b485cab4c958424af ts=2026-09-29T18:12:43.0580000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[614] _id=6abbff9b485cab4c958424b3 ts=2026-09-29T18:12:43.3190000Z`; `153ms: 6aa4144c41b41dbac0c7f26a.jsonl[614] _id=6abbff9b485cab4c958424b3 ts=2026-09-29T18:12:43.3190000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[620] _id=6abbff9b485cab4c958424b7 ts=2026-09-29T18:12:43.4720000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 584 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `18ms: 6aa4144c41b41dbac0c7f26a.jsonl[1100] _id=6abc0562485cab4c958497ca ts=2026-09-29T18:37:21.5610000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[1136] _id=6abc0562485cab4c958497cd ts=2026-09-29T18:37:21.5790000Z`; `61ms: 6aa4144c41b41dbac0c7f26a.jsonl[1131] _id=6abc0565485cab4c95849825 ts=2026-09-29T18:37:23.3110000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[1132] _id=6abc0565485cab4c95849827 ts=2026-09-29T18:37:23.3720000Z`; `62ms: 6aa4144c41b41dbac0c7f26a.jsonl[1132] _id=6abc0565485cab4c95849827 ts=2026-09-29T18:37:23.3720000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[1133] _id=6abc0565485cab4c9584982b ts=2026-09-29T18:37:23.4340000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `674ms: 6aa4144c41b41dbac0c7f26a.jsonl[6139] _id=6abd513c485cab4c9590fbaf ts=2026-09-30T18:13:16.3260000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[6079] _id=6abd513d485cab4c9590fbc9 ts=2026-09-30T18:13:17.0000000Z`; `889ms: 6aa4144c41b41dbac0c7f26a.jsonl[6312] _id=6abd5226485cab4c95911701 ts=2026-09-30T18:17:10.1180000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[6319] _id=6abd5227485cab4c9591170f ts=2026-09-30T18:17:11.0070000Z`; `460ms: 6aa4144c41b41dbac0c7f26a.jsonl[6319] _id=6abd5227485cab4c9591170f ts=2026-09-30T18:17:11.0070000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[6320] _id=6abd5227485cab4c95911719 ts=2026-09-30T18:17:11.4670000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6aa4144c41b41dbac0c7f26a.jsonl[6392] _id=6abd5260485cab4c95911f5b ts=2026-09-30T18:18:08.3030000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[6394] _id=6abd5260485cab4c95911f6f ts=2026-09-30T18:18:08.3320000Z`; `26ms: 6aa4144c41b41dbac0c7f26a.jsonl[10543] _id=6ac50a97de269131f9b3fd3e ts=2026-10-06T14:49:59.8730000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[10545] _id=6ac50a98de269131f9b3fd46 ts=2026-10-06T14:49:59.8990000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 84 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `443ms: 6aa4144c41b41dbac0c7f26a.jsonl[460] _id=6abab558485cab4c95705077 ts=2026-09-28T18:43:36.7090000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[455] _id=6abab559485cab4c95705083 ts=2026-09-28T18:43:37.1520000Z`; `779ms: 6aa4144c41b41dbac0c7f26a.jsonl[461] _id=6abab558485cab4c9570507b ts=2026-09-28T18:43:36.7300000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[457] _id=6abab559485cab4c9570508e ts=2026-09-28T18:43:37.5090000Z`; `154ms: 6aa4144c41b41dbac0c7f26a.jsonl[475] _id=6abab575485cab4c957051f5 ts=2026-09-28T18:44:05.7410000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[473] _id=6abab575485cab4c957051ff ts=2026-09-28T18:44:05.8950000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `904ms: 6aa4144c41b41dbac0c7f26a.jsonl[452] _id=6abab554485cab4c9570503d ts=2026-09-28T18:43:32.3860000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[459] _id=6abab555485cab4c95705049 ts=2026-09-28T18:43:33.2900000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4144c41b41dbac0c7f26a.jsonl[729] _id=6abc00d1485cab4c9584443f ts=2026-09-29T18:17:52.6000000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[735] _id=6abc010d485cab4c95844ccd ts=2026-09-29T18:17:52.6Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4144c41b41dbac0c7f26a.jsonl[3778] _id=6abd00e9485cab4c9586564f ts=2026-09-30T12:30:32.3780000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[3788] _id=6abd00e9485cab4c95865651 ts=2026-09-30T12:30:32.3840000Z`; `7ms: 6aa4144c41b41dbac0c7f26a.jsonl[4823] _id=6abd1ff0485cab4c958b549e ts=2026-09-30T14:42:57.4990000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[4805] _id=6abd1ff0485cab4c958b54a3 ts=2026-09-30T14:42:57.5060000Z`; `5ms: 6aa4144c41b41dbac0c7f26a.jsonl[4805] _id=6abd1ff0485cab4c958b54a3 ts=2026-09-30T14:42:57.5060000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[4806] _id=6abd1ff0485cab4c958b54a6 ts=2026-09-30T14:42:57.5110000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `585ms: 6aa4144c41b41dbac0c7f26a.jsonl[9672] _id=6ac3ee0bde269131f9af2671 ts=2026-10-05T18:35:55.9760000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[9670] _id=6ac3ee0cde269131f9af267f ts=2026-10-05T18:35:56.5610000Z`; `382ms: 6aa4144c41b41dbac0c7f26a.jsonl[9670] _id=6ac3ee0cde269131f9af267f ts=2026-10-05T18:35:56.5610000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[9657] _id=6ac3ee0cde269131f9af268b ts=2026-10-05T18:35:56.9430000Z`; `507ms: 6aa4144c41b41dbac0c7f26a.jsonl[9657] _id=6ac3ee0cde269131f9af268b ts=2026-10-05T18:35:56.9430000Z ~ 6aa4144c41b41dbac0c7f26a.jsonl[9676] _id=6ac3ee0dde269131f9af269b ts=2026-10-05T18:35:57.4500000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 101h 21m 
  - Evidence: 101h 21m: 6aa4144c41b41dbac0c7f26a.jsonl[7502] _id=6abe5577485cab4c95a3dc59 ts=2026-10-01T12:43:38.8520000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7893] _id=6ac3e6cbde269131f9aeb12d ts=2026-10-05T18:04:59.6090000Z; 23h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[4] _id=6abaaf38485cab4c956fbd2d ts=2026-09-28T18:17:28.4470000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[626] _id=6abbff62485cab4c95842087 ts=2026-09-29T18:11:46.4720000Z; 19h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[9989] _id=6ac3f063de269131f9af5ce3 ts=2026-10-05T18:45:55.0040000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10015] _id=6ac50849de269131f9b3932e ts=2026-10-06T14:40:11.9440000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 101h 14m 
  - Evidence: 101h 14m: 6aa4144c41b41dbac0c7f26a.jsonl[7874] _id=6abe573c485cab4c95a3fcf1 ts=2026-10-01T12:51:08.6000000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7912] _id=6ac3e6f7de269131f9aeb2c5 ts=2026-10-05T18:05:43.5690000Z; 23h 46m: 6aa4144c41b41dbac0c7f26a.jsonl[590] _id=6abab636485cab4c957060f4 ts=2026-09-28T18:47:18.5370000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[1009] _id=6abc0479485cab4c95848b2d ts=2026-09-29T18:33:28.9730000Z; 19h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[9998] _id=6ac3f06fde269131f9af5dbf ts=2026-10-05T18:46:07.5180000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10014] _id=6ac5084fde269131f9b3948d ts=2026-10-06T14:40:16.6090000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 590 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10238] _id=6ac5099fde269131f9b3d043 ts=2026-10-06T14:45:51.6720000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10229] _id=6ac5099fde269131f9b3d04f ts=2026-10-06T14:45:51.6730000Z; 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10244] _id=6ac509a9de269131f9b3d307 ts=2026-10-06T14:46:02.1420000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10245] _id=6ac509a9de269131f9b3d30c ts=2026-10-06T14:46:02.1430000Z; 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10280] _id=6ac509ccde269131f9b3d959 ts=2026-10-06T14:46:36.5680000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10281] _id=6ac509ccde269131f9b3d95b ts=2026-10-06T14:46:36.5690000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 139h 1m 
  - Evidence: 139h 1m: 6aa4144c41b41dbac0c7f26a.jsonl[7493] _id=6abd6a7b485cab4c95a32313 ts=2026-09-30T20:01:02.4420000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10896] _id=6ac50d90de269131f9b420f4 ts=2026-10-06T15:02:40.4300000Z; 49h 13m: 6aa4144c41b41dbac0c7f26a.jsonl[596] _id=6abab639485cab4c95706222 ts=2026-09-28T18:47:20.9880000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7493] _id=6abd6a7b485cab4c95a32313 ts=2026-09-30T20:01:02.4420000Z; 3h 27m: 6aa4144c41b41dbac0c7f26a.jsonl[10896] _id=6ac50d90de269131f9b420f4 ts=2026-10-06T15:02:40.4300000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[12291] _id=6ac53e1ede269131f9b66fe3 ts=2026-10-06T18:29:50.0750000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 101h 14m 
  - Evidence: 101h 14m: 6aa4144c41b41dbac0c7f26a.jsonl[7880] _id=6abe573e485cab4c95a3fd1f ts=2026-10-01T12:51:10.4110000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7901] _id=6ac3e6dfde269131f9aeb1a9 ts=2026-10-05T18:05:19.9660000Z; 23h 24m: 6aa4144c41b41dbac0c7f26a.jsonl[598] _id=6abab638485cab4c957061d2 ts=2026-09-28T18:47:20.9180000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[628] _id=6abbff68485cab4c958420f5 ts=2026-09-29T18:11:51.5720000Z; 19h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[9993] _id=6ac3f063de269131f9af5cef ts=2026-10-05T18:45:55.3690000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10022] _id=6ac5084dde269131f9b3940f ts=2026-10-06T14:40:11.9520000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 103 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10006] _id=6ac5084dde269131f9b39413 ts=2026-10-06T14:40:15.4680000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10007] _id=6ac5084dde269131f9b39415 ts=2026-10-06T14:40:15.4690000Z; 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10016] _id=6ac5084dde269131f9b39417 ts=2026-10-06T14:40:15.4710000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10023] _id=6ac5084dde269131f9b3941a ts=2026-10-06T14:40:15.4720000Z; 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10017] _id=6ac5084ede269131f9b39421 ts=2026-10-06T14:40:15.4740000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10024] _id=6ac5084ede269131f9b39428 ts=2026-10-06T14:40:15.4750000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 101h 16m 
  - Evidence: 101h 16m: 6aa4144c41b41dbac0c7f26a.jsonl[7857] _id=6abe5737485cab4c95a3fc91 ts=2026-10-01T12:51:04.0490000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7961] _id=6ac3e75ade269131f9aeb6bd ts=2026-10-05T18:07:22.5900000Z; 23h 26m: 6aa4144c41b41dbac0c7f26a.jsonl[574] _id=6abab60f485cab4c95705e33 ts=2026-09-28T18:46:39.5120000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[612] _id=6abbff98485cab4c958424ab ts=2026-09-29T18:12:40.1060000Z; 19h 56m: 6aa4144c41b41dbac0c7f26a.jsonl[9905] _id=6ac3eff0de269131f9af51a7 ts=2026-10-05T18:44:00.7490000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10057] _id=6ac50878de269131f9b39c52 ts=2026-10-06T14:40:58.7900000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[10091] _id=6ac508b2de269131f9b3a95e ts=2026-10-06T14:41:56.7940000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10093] _id=6ac508b2de269131f9b3a960 ts=2026-10-06T14:41:56.7950000Z; 2ms: 6aa4144c41b41dbac0c7f26a.jsonl[10143] _id=6ac508f5de269131f9b3b243 ts=2026-10-06T14:43:02.9070000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10144] _id=6ac508f5de269131f9b3b245 ts=2026-10-06T14:43:02.9090000Z; 4ms: 6aa4144c41b41dbac0c7f26a.jsonl[144] _id=6abab0ec485cab4c956ff4d9 ts=2026-09-28T18:24:44.6470000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[122] _id=6abab0ec485cab4c956ff4dd ts=2026-09-28T18:24:44.6510000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 101h 13m 
  - Evidence: 101h 13m: 6aa4144c41b41dbac0c7f26a.jsonl[7882] _id=6abe5745485cab4c95a3fd9d ts=2026-10-01T12:51:17.6410000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7897] _id=6ac3e6d1de269131f9aeb139 ts=2026-10-05T18:04:59.6160000Z; 23h 24m: 6aa4144c41b41dbac0c7f26a.jsonl[584] _id=6abab634485cab4c957060a7 ts=2026-09-28T18:47:16.6550000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[627] _id=6abbff68485cab4c958420ed ts=2026-09-29T18:11:46.4790000Z; 19h 53m: 6aa4144c41b41dbac0c7f26a.jsonl[10000] _id=6ac3f080de269131f9af5e9e ts=2026-10-05T18:46:24.4430000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10021] _id=6ac5084dde269131f9b39406 ts=2026-10-06T14:40:11.9490000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 101h 16m 
  - Evidence: 101h 16m: 6aa4144c41b41dbac0c7f26a.jsonl[7866] _id=6abe573a485cab4c95a3fccb ts=2026-10-01T12:51:05.5180000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[8012] _id=6ac3e77bde269131f9aeb953 ts=2026-10-05T18:07:54.7760000Z; 20h 21m: 6aa4144c41b41dbac0c7f26a.jsonl[9909] _id=6ac3ef76de269131f9af472b ts=2026-10-05T18:41:56.1400000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10819] _id=6ac50da7de269131f9b4226a ts=2026-10-06T15:03:02.4150000Z; 18h 22m: 6aa4144c41b41dbac0c7f26a.jsonl[6868] _id=6abd549c485cab4c95917c05 ts=2026-09-30T18:27:38.0890000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7652] _id=6abe56fb485cab4c95a3f54d ts=2026-10-01T12:50:04.4480000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2801 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26a.jsonl[10808] _id=6ac50dd5de269131f9b42575 ts=2026-10-06T15:03:49.1080000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10809] _id=6ac50dd5de269131f9b42578 ts=2026-10-06T15:03:49.1080000Z; 0ms: 6aa4144c41b41dbac0c7f26a.jsonl[10809] _id=6ac50dd5de269131f9b42578 ts=2026-10-06T15:03:49.1080000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10810] _id=6ac50dd5de269131f9b4257b ts=2026-10-06T15:03:49.1080000Z; 0ms: 6aa4144c41b41dbac0c7f26a.jsonl[10811] _id=6ac50dd5de269131f9b4257d ts=2026-10-06T15:03:49.1210000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10941] _id=6ac50dd5de269131f9b4257f ts=2026-10-06T15:03:49.1210000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 101h 16m 
  - Evidence: 101h 16m: 6aa4144c41b41dbac0c7f26a.jsonl[7881] _id=6abe573e485cab4c95a3fd23 ts=2026-10-01T12:51:10.7580000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7960] _id=6ac3e75ade269131f9aeb6bb ts=2026-10-05T18:07:22.5820000Z; 18h 23m: 6aa4144c41b41dbac0c7f26a.jsonl[6623] _id=6abd5408485cab4c959167f1 ts=2026-09-30T18:25:12.8880000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7579] _id=6abe56b8485cab4c95a3ee95 ts=2026-10-01T12:48:58.2570000Z; 17h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[2636] _id=6abc0738485cab4c9584bd8b ts=2026-09-29T18:45:12.8220000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[3915] _id=6abd0328485cab4c9586605d ts=2026-09-30T12:40:08.7740000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 17h 34m 
  - Evidence: 17h 34m: 6aa4144c41b41dbac0c7f26a.jsonl[1178] _id=6abc0592485cab4c95849bdb ts=2026-09-29T18:38:10.4020000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[2985] _id=6abcfcc6485cab4c95864a5f ts=2026-09-30T12:12:56.6340000Z; 3h 8m: 6aa4144c41b41dbac0c7f26a.jsonl[5412] _id=6abd23d3485cab4c958b9c21 ts=2026-09-30T14:59:31.6050000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[5872] _id=6abd4ff6485cab4c9590e1bb ts=2026-09-30T18:07:50.0300000Z; 2h 24m: 6aa4144c41b41dbac0c7f26a.jsonl[3812] _id=6abd0162485cab4c9586575f ts=2026-09-30T12:32:34.6190000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[5352] _id=6abd235a485cab4c958b9628 ts=2026-09-30T14:57:30.3780000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 49m 
  - Evidence: 2h 49m: 6aa4144c41b41dbac0c7f26a.jsonl[11506] _id=6ac5105fde269131f9b454f9 ts=2026-10-06T15:14:39.5710000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11556] _id=6ac5382ade269131f9b61abb ts=2026-10-06T18:04:27.3240000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 140h 27m 
  - Evidence: 140h 27m: 6aa4144c41b41dbac0c7f26a.jsonl[6390] _id=6abd5260485cab4c95911f57 ts=2026-09-30T18:18:08.2890000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10240] _id=6ac5099fde269131f9b3d03a ts=2026-10-06T14:45:51.6540000Z; 47h 28m: 6aa4144c41b41dbac0c7f26a.jsonl[479] _id=6abab57b485cab4c9570529e ts=2026-09-28T18:44:10.9700000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[6076] _id=6abd511a485cab4c9590f799 ts=2026-09-30T18:12:42.1560000Z; 3h 28m: 6aa4144c41b41dbac0c7f26a.jsonl[10542] _id=6ac50a97de269131f9b3fd37 ts=2026-10-06T14:49:59.8550000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11979] _id=6ac53b68de269131f9b6427d ts=2026-10-06T18:18:16.6200000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 140h 27m 
  - Evidence: 140h 27m: 6aa4144c41b41dbac0c7f26a.jsonl[6394] _id=6abd5260485cab4c95911f6f ts=2026-09-30T18:18:08.3320000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10219] _id=6ac50998de269131f9b3ce41 ts=2026-10-06T14:45:45.0600000Z; 47h 28m: 6aa4144c41b41dbac0c7f26a.jsonl[480] _id=6abab57b485cab4c957052a8 ts=2026-09-28T18:44:10.9940000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[6069] _id=6abd5116485cab4c9590f72d ts=2026-09-30T18:12:38.1510000Z; 3h 27m: 6aa4144c41b41dbac0c7f26a.jsonl[10545] _id=6ac50a98de269131f9b3fd46 ts=2026-10-06T14:49:59.8990000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11919] _id=6ac53b3ade269131f9b63ff5 ts=2026-10-06T18:17:30.8320000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.026s..0.029s shown 
  - Evidence: 26ms: 6aa4144c41b41dbac0c7f26a.jsonl[10543] _id=6ac50a97de269131f9b3fd3e ts=2026-10-06T14:49:59.8730000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10545] _id=6ac50a98de269131f9b3fd46 ts=2026-10-06T14:49:59.8990000Z; 29ms: 6aa4144c41b41dbac0c7f26a.jsonl[6392] _id=6abd5260485cab4c95911f5b ts=2026-09-30T18:18:08.3030000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[6394] _id=6abd5260485cab4c95911f6f ts=2026-09-30T18:18:08.3320000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 140h 27m 
  - Evidence: 140h 27m: 6aa4144c41b41dbac0c7f26a.jsonl[6380] _id=6abd525f485cab4c95911f29 ts=2026-09-30T18:18:06.9200000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10202] _id=6ac50990de269131f9b3cc21 ts=2026-10-06T14:45:37.2400000Z; 47h 28m: 6aa4144c41b41dbac0c7f26a.jsonl[478] _id=6abab576485cab4c95705227 ts=2026-09-28T18:44:06.8450000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[6026] _id=6abd5108485cab4c9590f5a3 ts=2026-09-30T18:12:24.2940000Z; 3h 27m: 6aa4144c41b41dbac0c7f26a.jsonl[10540] _id=6ac50a95de269131f9b3fd08 ts=2026-10-06T14:49:57.6650000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11900] _id=6ac53b2ade269131f9b63f17 ts=2026-10-06T18:17:14.9320000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 144 interval(s) ≤ 0.002s..0.015s shown 
  - Evidence: 2ms: 6aa4144c41b41dbac0c7f26a.jsonl[6125] _id=6abd5136485cab4c9590fad1 ts=2026-09-30T18:13:09.9760000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[6134] _id=6abd5136485cab4c9590fad7 ts=2026-09-30T18:13:09.9780000Z; 14ms: 6aa4144c41b41dbac0c7f26a.jsonl[10234] _id=6ac50999de269131f9b3ce9f ts=2026-10-06T14:45:46.1550000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10235] _id=6ac50999de269131f9b3cea5 ts=2026-10-06T14:45:46.1690000Z; 15ms: 6aa4144c41b41dbac0c7f26a.jsonl[10523] _id=6ac50a8bde269131f9b3fb92 ts=2026-10-06T14:49:47.0030000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10522] _id=6ac50a8bde269131f9b3fb96 ts=2026-10-06T14:49:47.0180000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 28m 
  - Evidence: 47h 28m: 6aa4144c41b41dbac0c7f26a.jsonl[466] _id=6abab565485cab4c9570510f ts=2026-09-28T18:43:49.8120000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[6072] _id=6abd5117485cab4c9590f761 ts=2026-09-30T18:12:39.6670000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 3h 0m 
  - Evidence: 3h 0m: 6aa4144c41b41dbac0c7f26a.jsonl[10904] _id=6ac50da1de269131f9b421fc ts=2026-10-06T15:02:57.0210000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11539] _id=6ac53803de269131f9b61a3f ts=2026-10-06T18:03:48.0090000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 101h 21m 
  - Evidence: 101h 21m: 6aa4144c41b41dbac0c7f26a.jsonl[7496] _id=6abe5565485cab4c95a3dbf5 ts=2026-10-01T12:43:20.7370000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7892] _id=6ac3e6c1de269131f9aeb127 ts=2026-10-05T18:04:49.9800000Z; 23h 53m: 6aa4144c41b41dbac0c7f26a.jsonl[3] _id=6abaaf2e485cab4c956fbba9 ts=2026-09-28T18:17:18.7660000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[624] _id=6abbff46485cab4c95841ee5 ts=2026-09-29T18:11:18.7140000Z; 20h 13m: 6aa4144c41b41dbac0c7f26a.jsonl[9325] _id=6ac3ebe6de269131f9aefe9f ts=2026-10-05T18:26:46.3420000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10012] _id=6ac50841de269131f9b39210 ts=2026-10-06T14:40:03.4870000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 101h 13m 
  - Evidence: 101h 13m: 6aa4144c41b41dbac0c7f26a.jsonl[7884] _id=6abe5743485cab4c95a3fd81 ts=2026-10-01T12:51:15.7440000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7894] _id=6ac3e6c1de269131f9aeb125 ts=2026-10-05T18:04:49.9790000Z; 23h 53m: 6aa4144c41b41dbac0c7f26a.jsonl[2] _id=6abaaf2e485cab4c956fbba3 ts=2026-09-28T18:17:18.7650000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[623] _id=6abbff46485cab4c95841ee1 ts=2026-09-29T18:11:18.7130000Z; 20h 13m: 6aa4144c41b41dbac0c7f26a.jsonl[9324] _id=6ac3ebe6de269131f9aefe9b ts=2026-10-05T18:26:46.3410000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10013] _id=6ac50841de269131f9b39208 ts=2026-10-06T14:40:03.4860000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 101h 54m 
  - Evidence: 101h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[7883] _id=6abe5747485cab4c95a3fdaf ts=2026-10-01T12:51:19.0630000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[9999] _id=6ac3f073de269131f9af5e0d ts=2026-10-05T18:46:11.7230000Z; 20h 17m: 6aa4144c41b41dbac0c7f26a.jsonl[9999] _id=6ac3f073de269131f9af5e0d ts=2026-10-05T18:46:11.7230000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10916] _id=6ac50db7de269131f9b42356 ts=2026-10-06T15:03:19.1320000Z; 18h 11m: 6aa4144c41b41dbac0c7f26a.jsonl[735] _id=6abc010d485cab4c95844ccd ts=2026-09-29T18:17:52.6Z -> 6aa4144c41b41dbac0c7f26a.jsonl[3751] _id=6abd00aa485cab4c95865427 ts=2026-09-30T12:29:30.0340000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26a.jsonl[729] _id=6abc00d1485cab4c9584443f ts=2026-09-29T18:17:52.6000000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[735] _id=6abc010d485cab4c95844ccd ts=2026-09-29T18:17:52.6Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 101h 18m 
  - Evidence: 101h 18m: 6aa4144c41b41dbac0c7f26a.jsonl[7532] _id=6abe563c485cab4c95a3e417 ts=2026-10-01T12:46:55.6400000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[7895] _id=6ac3e6d1de269131f9aeb13b ts=2026-10-05T18:05:04.9870000Z; 23h 48m: 6aa4144c41b41dbac0c7f26a.jsonl[570] _id=6abab611485cab4c95705e43 ts=2026-09-28T18:46:41.6350000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[1004] _id=6abc04ee485cab4c95849067 ts=2026-09-29T18:35:26.4510000Z; 19h 54m: 6aa4144c41b41dbac0c7f26a.jsonl[9994] _id=6ac3f064de269131f9af5cf7 ts=2026-10-05T18:45:56.2630000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[10019] _id=6ac5084ede269131f9b3946e ts=2026-10-06T14:40:15.5160000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 19 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[11267] _id=6ac50ed6de269131f9b439a7 ts=2026-10-06T15:08:06.5630000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11262] _id=6ac50ed6de269131f9b439aa ts=2026-10-06T15:08:06.5640000Z; 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[11668] _id=6ac538c9de269131f9b61fc0 ts=2026-10-06T18:07:05.5200000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[11669] _id=6ac538c9de269131f9b61fc2 ts=2026-10-06T18:07:05.5210000Z; 1ms: 6aa4144c41b41dbac0c7f26a.jsonl[390] _id=6abab489485cab4c95703e09 ts=2026-09-28T18:40:09.6830000Z -> 6aa4144c41b41dbac0c7f26a.jsonl[394] _id=6abab48a485cab4c95703e0d ts=2026-09-28T18:40:09.6840000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[377] _id=6abab473485cab4c95703a2d ts=2026-09-28T18:39:47.0300000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[492] _id=6abab58c485cab4c957053d1 ts=2026-09-28T18:44:27.9840000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[3771] _id=6abd00b4485cab4c9586549b ts=2026-09-30T12:29:39.9340000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 135 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[1442] _id=6abc05da485cab4c9584a245 ts=2026-09-29T18:39:21.1060000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1475] _id=6abc05e5485cab4c9584a2e1 ts=2026-09-29T18:39:32.7820000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1743] _id=6abc0625485cab4c9584a7d3 ts=2026-09-29T18:40:36.1800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 260 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[1217] _id=6abc05b9485cab4c95849ec5 ts=2026-09-29T18:37:12.5580000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1233] _id=6abc05ba485cab4c95849efb ts=2026-09-29T18:37:14.0590000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1125] _id=6abc0562485cab4c958497c5 ts=2026-09-29T18:37:21.5390000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[6394] _id=6abd5260485cab4c95911f6f ts=2026-09-30T18:18:08.3320000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[10545] _id=6ac50a98de269131f9b3fd46 ts=2026-10-06T14:49:59.8990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 22 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[6128] _id=6abd5135485cab4c9590fabd ts=2026-09-30T18:13:09.4310000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[6129] _id=6abd5135485cab4c9590fac3 ts=2026-09-30T18:13:09.4600000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[6125] _id=6abd5136485cab4c9590fad1 ts=2026-09-30T18:13:09.9760000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[10904] _id=6ac50da1de269131f9b421fc ts=2026-10-06T15:02:57.0210000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[11539] _id=6ac53803de269131f9b61a3f ts=2026-10-06T18:03:48.0090000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[11760] _id=6ac53979de269131f9b6290e ts=2026-10-06T18:10:01.7860000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[9039] _id=6ac3e9a6de269131f9aed86f ts=2026-10-05T18:17:10.7060000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[9260] _id=6ac3eb55de269131f9aef5d9 ts=2026-10-05T18:24:21.5940000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[9339] _id=6ac3ebf6de269131f9af003b ts=2026-10-05T18:27:02.1710000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 6 records 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[629] _id=6abbff67485cab4c958420e9 ts=?`; `6aa4144c41b41dbac0c7f26a.jsonl[703] _id=6abc0073485cab4c95843679 ts=?`; `6aa4144c41b41dbac0c7f26a.jsonl[2771] _id=6abcfc4a485cab4c95864901 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 458 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[1285] _id=6abc05c2485cab4c9584a01e ts=2026-09-29T18:38:57.2520000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1269] _id=6abc05c2485cab4c9584a023 ts=2026-09-29T18:38:57.4520000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1259] _id=6abc05c3485cab4c9584a025 ts=2026-09-29T18:38:57.4710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 927 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[1108] _id=6abc0561485cab4c958497ab ts=2026-09-29T18:37:21.4470000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1109] _id=6abc0561485cab4c958497ad ts=2026-09-29T18:37:21.4470000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1098] _id=6abc0561485cab4c958497af ts=2026-09-29T18:37:21.4470000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 61 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[6214] _id=6abd5182485cab4c9591042b ts=2026-09-30T18:14:26.2740000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[6168] _id=6abd5189485cab4c9591050d ts=2026-09-30T18:14:33.0880000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[6180] _id=6abd518b485cab4c95910533 ts=2026-09-30T18:14:35.1950000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[452] _id=6abab554485cab4c9570503d ts=2026-09-28T18:43:32.3860000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[459] _id=6abab555485cab4c95705049 ts=2026-09-28T18:43:33.2900000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[465] _id=6abab562485cab4c957050f5 ts=2026-09-28T18:43:46.6360000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 385 start, 376 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 120 unmatched 'BecameCameraCentered' (totals: 756 open, 771 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 126 unmatched 'BecameVisible' (totals: 1381 open, 1515 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationNodeHoverStart' (totals: 230 open, 246 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 9 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'questActiveEvent' (totals: 50 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 329 of 12287 adjacent _id pairs reverse in client time; worst 110.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f26a.jsonl[1211] _id=6abc05b8485cab4c95849e89 ts=2026-09-29T18:38:47.9900000Z`; `6aa4144c41b41dbac0c7f26a.jsonl[1184] _id=6abc05b9485cab4c95849ea5 ts=2026-09-29T18:36:57.5710000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -111.62s, max +3.34s over 12288 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26a\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 6 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4423 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2869); Unit 4 Dev (1042); Unit 5 Dev - Dungeon (282); Unit 3 Dungeon Dev (230)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.28s, n=4422)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4423/4423 records)
    "BecameInvisible"  x1515
    "BecameVisible"  x1381
    "BecameCameraUncentered"  x771
    "BecameCameraCentered"  x756
data.pieceId  (string, 4423/4423 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4423/4423 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2883 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (543); Unit 4 Dev - Dungeon (495); Unit 2 Prod (Refactor) (465); Unit 1 Dev (398); Unit 5 Dev - Dungeon (342); Unit 3 Dungeon Dev (235); Unit 4 Dev (234); Unit 4 Dev - Anderson Base (97); Unit 5 Dev (74)
- **Intervals:** median 1.30s (p5 0.09s / p95 19.54s, n=2882)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2883/2883 records)
    "pressed"  x2883
data.actionType  (string, 2883/2883 records)
    "Move"  x1990
    "Interact"  x451
    "Jump"  x188
    "Sprint"  x180
    "Hoverboard"  x34
    "Ascend"  x21
    "Map"  x16
    "SkipCinematic"  x2
    "Pause"  x1
data.key  (string, 2883/2883 records, 3 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2883/2883 records)
    "Player"  x2507
    "Drone"  x376
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 1982 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (419); Unit 3 Dev (374); Unit 4 Dev (282); Unit 5 Dev (253); Unit 1 Dev (197); Unit 4 Dev - Anderson Base (142); Unit 3 Dungeon Dev (116); Unit 4 Dev - Dungeon (107); Unit 5 Dev - Dungeon (92)
- **eventKey:** present on 1221 of 1982 records
- **Intervals:** median 3.30s (p5 0.00s / p95 27.11s, n=1981)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1221; [conversationId, dialogueEventType] x761
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1982/1982 records)
    numeric range 10 .. 118 (51 unique)
data.dialogueEventType  (string, 1982/1982 records)
    "DialogueNodeEvent"  x1221
    "DialogueStartEvent"  x385
    "DialogueFinishEvent"  x376
data.nodeId  (number, 1221/1982 records)
    numeric range 0 .. 289 (207 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1600 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (348); Unit 3 Dev (266); Unit 1 Dev (262); Unit 4 Dev (198); Unit 4 Dev - Dungeon (158); Unit 5 Dev (115); Unit 5 Dev - Dungeon (110); Unit 3 Dungeon Dev (76); Unit 4 Dev - Anderson Base (67)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.52s, n=1588)
- **Fields under `data`:**

```text
data.position  (object, 1600/1600 records)
data.position.x  (number, 1600/1600 records)
    numeric range -700.439 .. 1553.08 (686 unique)
data.position.y  (number, 1600/1600 records)
    numeric range -115.207 .. 222.652 (489 unique)
data.position.z  (number, 1600/1600 records)
    numeric range -1105.71 .. 1783.36 (689 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 543 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (229); Unit 3 Dev (219); Unit 5 Dev (68); Unit 1 Dev (27)
- **Intervals:** median 0.25s (p5 0.02s / p95 7.57s, n=542)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 543/543 records)
    "argumentationNodeHoverEnd"  x246
    "argumentationNodeHoverStart"  x230
    "argumentationNodeAdd"  x41
    "argumentationNodeRemove"  x26
data.argumentationTitle  (string, 543/543 records)
    "Unit 4 - Flooding"  x229
    "Unit 3 - Pollution Upstream"  x219
    "Unit 5"  x68
    "Unit 1 - Freshwater"  x17
    "Unit 1 - Argumentation Tutorial"  x10
data.nodeName  (string, 543/543 records)
    "B"  x92
    "A"  x71
    "3"  x65
    "C"  x53
    "4"  x50
    "II"  x49
    "1"  x42
    "I"  x39
    "2"  x37
    "D"  x30
    "5"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 307 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (93); Unit 2 Prod (Refactor) (70); Unit 1 Dev (49); Unit 3 Dungeon Dev (30); Unit 4 Dev (25); Unit 5 Dev - Dungeon (13); Unit 3 Dev (12); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (6)
- **Intervals:** median 8.24s (p5 0.37s / p95 407.71s, n=306)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 307/307 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 307/307 records)
    96 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 166 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (84); Unit 2 Prod (Refactor) (56); Unit 3 Dev (26)
- **Intervals:** median 0.36s (p5 0.13s / p95 9.02s, n=165)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x156; [Soil Key Puzzle Status, Unit] x10
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 10/166 records)
    "Finished"  x5
    "Started"  x5
data.Unit  (string, 10/166 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 156/166 records)
    "RightDrag"  x81
    "LeftDrag"  x75
data.currentSoilType  (string, 156/166 records)
    "SAND"  x33
    "CLAYSAND"  x31
    "SANDGRAVEL"  x28
    "CLAY"  x25
    "CLAYROCK"  x19
    "GRAVEL"  x12
    "BEDROCK"  x8
data.isCorrectSelection  (string, 156/166 records)
    "false"  x122
    "true"  x34
data.waterLevelStatus  (string, 156/166 records)
    "Proper"  x78
    "TooLow"  x42
    "TooHigh"  x36
data.waterRetentionChange  (string, 156/166 records)
    "Decrease"  x63
    "Increase"  x59
    "NoChange"  x34
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 86 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (16); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev - Dungeon (12); Unit 5 Dev - Dungeon (12); Unit 4 Dev (9); Unit 5 Dev (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 86 of 86 records
- **Intervals:** median 158.25s (p5 0.00s / p95 50413.54s, n=85)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 86/86 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x36
data.questID  (string, 86/86 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 86/86 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/86 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 50 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 3 Dev (25); Unit 4 Dev - Anderson Base (21); Unit 1 Dev (3); Unit 5 Dev (1)
- **Intervals:** median 10.71s (p5 0.63s / p95 7545.23s, n=49)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 50/50 records)
    "submitAnswerEvent"  x50
data.answerSubmitted  (string, 50/50 records, 3 empty-string)
    23 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 50/50 records)
    "Unit 3 - Pollution Upstream"  x25
    "Unit 4 - Flooding"  x21
    "Unit 1 - Freshwater"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 46 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (16); Unit 1 Dev (8)
- **Intervals:** median 12.28s (p5 1.70s / p95 7844.14s, n=45)
- **`data` key-set variants:** [actionType, featureUsed] x40; [actionType, featureUsed, location] x6
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "MapCloseEvent"  x20
    "MapOpenEvent"  x20
    "WaypointSetEvent"  x4
    "WaypointMoveEvent"  x2
data.featureUsed  (string, 46/46 records)
    "Map"  x40
    "Waypoint"  x6
data.location  (object, 6/46 records)
data.location.x  (number, 6/46 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 6/46 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 6/46 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 38 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (38)
- **Intervals:** median 10.81s (p5 1.14s / p95 69.55s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "On"  x29
    "Off"  x9
data.floor  (string, 38/38 records)
    "4"  x17
    "3"  x16
    "2"  x3
    "1"  x2
data.machineNumber  (string, 38/38 records)
    "One"  x34
    "Two"  x4
data.machineType  (string, 38/38 records)
    "Condenser"  x20
    "Evaporator"  x10
    "VentSwitch"  x4
    "DualChamber_Condenser"  x2
    "DualChamber_Evaporator"  x2
data.room  (string, 38/38 records)
    "3"  x13
    "2"  x12
    "1"  x7
    "4"  x6
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 33 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 5 Dev - Dungeon (2); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 411.65s (p5 24.45s / p95 78756.41s, n=32)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 33/33 records)
    true  x33
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 4 Dev (4); Unit 4 Dev - Dungeon (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 716.60s (p5 87.93s / p95 81737.70s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 22 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (22)
- **Intervals:** median 1186.40s (p5 65.46s / p95 86039.95s, n=21)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 22/22 records)
    true  x22
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 22 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (22)
- **Intervals:** median 5.53s (p5 0.47s / p95 109.54s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "ChangeCanister"  x22
data.canisterType  (string, 22/22 records)
    "Bedrock"  x12
    "Clay"  x6
    "Gravel"  x3
    "Sand"  x1
data.floor  (string, 22/22 records)
    "5"  x17
    "4"  x4
    "3"  x1
data.machine  (string, 22/22 records)
    "1"  x21
    "2"  x1
data.row  (string, 22/22 records)
    "TopRow"  x14
    "BottomRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 16 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 1 Dev (2); Unit 4 Dev (2); Unit 5 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev (1)
- **Intervals:** median 774.15s (p5 3.50s / p95 161186.98s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    false  x16
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (4)
- **Intervals:** median 3.29s (p5 0.49s / p95 77043.08s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 13/13 records)
    "Unit 1 - Freshwater"  x7
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 57.30s (p5 0.03s / p95 338281.94s, n=11)
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

### `TerasGardenBox` — 7 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (7)
- **Intervals:** median 1.36s (p5 0.99s / p95 25.29s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records, 4 empty-string)
    ""  x4
    "cameraPlaced"  x3
data.boxId  (string, 7/7 records)
    "0"  x3
    "1"  x2
    "2"  x2
data.soilType  (string, 7/7 records)
    "Clay"  x5
    "Sand"  x2
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
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x3
data.phase  (string, 6/6 records)
    "running"  x6
data.stack  (string, 6/6 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x3
data.type  (string, 6/6 records)
    "unhandled_rejection"  x6
data.unitId  (string, 6/6 records)
    "unit1"  x2
    "unit2"  x2
    "unit3"  x1
    "unit4"  x1
data.workspace  (string, 6/6 records)
    "mhs"  x6
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 177221.45s (p5 28908.83s / p95 468170.33s, n=3)
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
- **Intervals:** median 5.53s (p5 1.79s / p95 6.96s, n=3)
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

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 5612.38s (p5 897.64s / p95 10327.13s, n=2)
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
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (56 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (2x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (6x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (26x)
- `soilMachine` data.canisterType: "Bedrock" (12x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*