# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b07

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b07
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b07.jsonl
- **Records:** 12085 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b07
- **Time span:** 2026-10-05T15:15:47.857000+00:00 .. 2026-10-16T16:05:07.196000+00:00 (264h 49m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b07\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 12085 records, 10 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 94 INFO, 0 NOT_TESTED, 99 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3304 | 27.34 | 1 | 9 | 0 | 2026-10-05T15:19:45.765000+00:00 | 2026-10-16T16:05:07.196000+00:00 | 264h 45m |
| PuzzlePieceVisibleEvent | 3166 | 26.2 | 1 | 4 | 0 | 2026-10-06T15:37:26.678000+00:00 | 2026-10-16T15:36:28.717000+00:00 | 239h 59m |
| DialogueEvent | 2315 | 19.16 | 1 | 9 | 1457 | 2026-10-05T15:16:31.804000+00:00 | 2026-10-16T16:04:56.946000+00:00 | 264h 48m |
| PlayerPositionEvent | 2024 | 16.75 | 1 | 9 | 0 | 2026-10-05T15:16:11.705000+00:00 | 2026-10-16T16:04:59.883000+00:00 | 264h 48m |
| ObjectInterEvent | 411 | 3.4 | 1 | 9 | 0 | 2026-10-05T15:21:33.547000+00:00 | 2026-10-16T16:05:07.196000+00:00 | 264h 43m |
| argumentationNodeEvent | 382 | 3.16 | 1 | 5 | 0 | 2026-10-05T15:44:32.171000+00:00 | 2026-10-16T15:55:09.569000+00:00 | 264h 10m |
| questEvent | 93 | 0.77 | 1 | 9 | 93 | 2026-10-05T15:16:31.778000+00:00 | 2026-10-16T16:01:06.010000+00:00 | 264h 44m |
| Soil Key Puzzle | 83 | 0.69 | 1 | 3 | 0 | 2026-10-06T15:46:40.590000+00:00 | 2026-10-15T15:34:55.702000+00:00 | 215h 48m |
| TopographicMapEvent | 81 | 0.67 | 1 | 2 | 0 | 2026-10-06T15:38:11.360000+00:00 | 2026-10-15T15:22:39.645000+00:00 | 215h 44m |
| DEBUGMenu | 33 | 0.27 | 1 | 9 | 0 | 2026-10-05T15:16:11.688000+00:00 | 2026-10-16T15:31:17.735000+00:00 | 264h 15m |
| soilMachine | 33 | 0.27 | 1 | 1 | 0 | 2026-10-15T15:45:42.778000+00:00 | 2026-10-15T16:59:21.513000+00:00 | 1h 13m |
| argumentationAnswerEvent | 31 | 0.26 | 1 | 5 | 0 | 2026-10-05T15:44:52.850000+00:00 | 2026-10-16T15:55:10.958000+00:00 | 264h 10m |
| WaterChamberEvent | 22 | 0.18 | 1 | 1 | 0 | 2026-10-16T15:35:06.948000+00:00 | 2026-10-16T15:45:32.941000+00:00 | 10m 25s |
| TerasGardenBox | 18 | 0.15 | 1 | 1 | 0 | 2026-10-16T15:20:26.527000+00:00 | 2026-10-16T15:21:53.578000+00:00 | 1m 27s |
| argumentationEvent | 18 | 0.15 | 1 | 5 | 0 | 2026-10-05T15:44:26.511000+00:00 | 2026-10-16T15:55:10.996000+00:00 | 264h 10m |
| gameWindowFocusEvent | 18 | 0.15 | 1 | 4 | 0 | 2026-10-05T15:15:47.857000+00:00 | 2026-10-16T15:31:10.833000+00:00 | 264h 15m |
| gameStartEvent | 15 | 0.12 | 1 | 1 | 0 | 2026-10-05T15:15:47.858000+00:00 | 2026-10-16T15:31:10.833000+00:00 | 264h 15m |
| argumentationToolEvent | 10 | 0.08 | 1 | 3 | 0 | 2026-10-06T15:28:05.895000+00:00 | 2026-10-14T15:28:02.548000+00:00 | 191h 59m |
| SolarStillDesignEvent | 9 | 0.07 | 1 | 1 | 0 | 2026-10-16T15:58:22.714000+00:00 | 2026-10-16T15:58:40.697000+00:00 | 18.0s |
| gameWindowUnfocusEvent | 8 | 0.07 | 1 | 5 | 0 | 2026-10-05T15:48:00.165000+00:00 | 2026-10-15T18:18:53.368000+00:00 | 242h 30m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T15:32:02.577000+00:00 | 2026-10-16T16:05:07.169000+00:00 | 240h 33m |
| DaniEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-14T15:18:25.342000+00:00 | 2026-10-15T15:18:28.922000+00:00 | 24h 0m |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-16T15:31:17.593000+00:00 | 2026-10-16T15:46:39.728000+00:00 | 15m 22s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 129358.06s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.628s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.064s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.503s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.681s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.867s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 14.743s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 4.138s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 39869.791s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2399.186s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86373.633s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 13.678s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: a; leftShift 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 31 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,I; A,2,II; A,3,I; A,4,I; A,C,2,II; B,2,II; C,2,II; C,A,2,II; C,D,3,II; D,1,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 6.6x vs baseline. 
  - Observed: 33 records 
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
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[450] _id=6ac3c295de269131f9ad35ef ts=2026-10-05T15:30:28.8960000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[504] _id=6ac3c379de269131f9ad41a7 ts=2026-10-05T15:34:16.9630000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[541] _id=6ac3c3fede269131f9ad4a3b ts=2026-10-05T15:36:29.3370000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:28' vs expected 'questActiveEvent:32' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[788] _id=6ac512a9de269131f9b459fb ts=2026-10-06T15:24:23.9620000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[5] _id=6ac3bf24de269131f9ace709 ts=2026-10-05T15:15:47.8580000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[776] _id=6ac5129dde269131f9b459d5 ts=2026-10-06T15:24:12.8030000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[980] _id=6ac514c5de269131f9b470b3 ts=2026-10-06T15:33:24.6860000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[4] _id=6ac3bf24de269131f9ace707 ts=2026-10-05T15:15:47.8570000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[775] _id=6ac5129dde269131f9b459d3 ts=2026-10-06T15:24:12.8020000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[981] _id=6ac514c5de269131f9b470b1 ts=2026-10-06T15:33:24.6850000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[767] _id=6ac3c6b1de269131f9ad7871 ts=2026-10-05T15:48:00.1650000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[2103] _id=6ac6626ede269131f9bb9928 ts=2026-10-06T15:47:33.798Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[3349] _id=6ac66994de269131f9bc304b ts=2026-10-07T15:47:30.4720000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3303 | 0.0 | 1.628 | 288.562 | 20.28 | 429603.743 | 0.21 | 101 | 11 |
| PuzzlePieceVisibleEvent | 3165 | 0.0 | 0.064 | 272.967 | 2.058 | 518617.814 | 0.22 | 1476 | 9 |
| DialogueEvent | 2314 | 0.0 | 3.673 | 411.973 | 28.753 | 429523.354 | 0.15 | 657 | 9 |
| PlayerPositionEvent | 2012 | 0.0 | 10.001 | 473.694 | 10.127 | 429486.435 | 0.13 | 1 | 9 |
| ObjectInterEvent | 410 | 0.0 | 8.794 | 2324.424 | 328.336 | 431526.103 | 0.03 | 3 | 12 |
| argumentationNodeEvent | 381 | 0.0 | 0.747 | 2496.161 | 8.506 | 605034.373 | 0.02 | 32 | 5 |
| questEvent | 92 | 0.0 | 189.448 | 10359.503 | 84232.186 | 430134.284 | 0.01 | 18 | 17 |
| Soil Key Puzzle | 82 | 0.199 | 2.503 | 9474.331 | 16.567 | 519064.546 | 0.01 | 0 | 4 |
| TopographicMapEvent | 80 | 0.022 | 4.867 | 9708.354 | 84094.609 | 432065.6 | 0.01 | 2 | 8 |
| DEBUGMenu | 32 | 7.078 | 658.925 | 29728.314 | 86678.172 | 431044.656 | 0.0 | 0 | 17 |
| soilMachine | 32 | 1.28 | 13.678 | 138.085 | 398.911 | 2656.942 | 0.43 | 0 | 2 |
| argumentationAnswerEvent | 30 | 0.806 | 14.743 | 31700.604 | 133206.008 | 605086.682 | 0.0 | 0 | 5 |
| WaterChamberEvent | 21 | 6.954 | 19.964 | 29.809 | 80.973 | 89.257 | 2.01 | 0 | 0 |
| TerasGardenBox | 17 | 0.256 | 1.681 | 5.121 | 17.491 | 22.803 | 11.72 | 0 | 0 |
| argumentationEvent | 17 | 0.035 | 41.864 | 55943.793 | 258436.768 | 605024.3 | 0.0 | 1 | 5 |
| gameWindowFocusEvent | 17 | 26.221 | 2399.186 | 55960.175 | 155735.255 | 431056.493 | 0.0 | 0 | 15 |
| gameStartEvent | 14 | 551.883 | 39869.791 | 67951.641 | 207357.987 | 431056.493 | 0.0 | 0 | 13 |
| argumentationToolEvent | 9 | 0.916 | 4.138 | 76799.628 | 397486.709 | 605105.346 | 0.0 | 0 | 2 |
| SolarStillDesignEvent | 8 | 1.364 | 2.015 | 2.248 | 3.542 | 3.908 | 26.69 | 0 | 0 |
| gameWindowUnfocusEvent | 7 | 2425.554 | 86373.633 | 124721.886 | 388290.759 | 515965.401 | 0.0 | 0 | 7 |
| EndOfUnit | 4 | 2052.2 | 129358.06 | 216496.148 | 540258.455 | 605216.272 | 0.0 | 0 | 4 |
| DaniEvent | 3 | 1.933 | 4.3 | 28801.193 | 77758.042 | 86397.347 | 0.0 | 0 | 1 |
| chatEvent | 1 | 922.135 | 922.135 | 922.135 | 922.135 | 922.135 | 0.07 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 11 group(s), 41 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[3360] _id=6ac7b47dde269131f9c3826a ts=2026-10-08T15:19:24.0140000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[3361] _id=6ac7b47dde269131f9c3826b ts=2026-10-08T15:19:24.0140000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[4715] _id=6ace4851de269131f9cf0124 ts=2026-10-13T15:03:42.4220000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[4716] _id=6ace4851de269131f9cf0125 ts=2026-10-13T15:03:42.4220000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[4719] _id=6ace4851de269131f9cf0128 ts=2026-10-13T15:03:42.4230000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[4720] _id=6ace4851de269131f9cf0129 ts=2026-10-13T15:03:42.4230000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 113 group(s), 177 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[1082] _id=6ac515cbde269131f9b487bb ts=2026-10-06T15:37:45.5860000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[1083] _id=6ac515cbde269131f9b487c6 ts=2026-10-06T15:37:45.5860000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1102] _id=6ac515dade269131f9b48949 ts=2026-10-06T15:38:00.6280000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[1103] _id=6ac515dade269131f9b4894d ts=2026-10-06T15:38:00.6280000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1146] _id=6ac51618de269131f9b48d00 ts=2026-10-06T15:39:01.1230000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[1133] _id=6ac51618de269131f9b48d04 ts=2026-10-06T15:39:01.1230000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[11848] _id=6ad24926de269131f9e56b43 ts=2026-10-16T15:56:22.0930000Z == 6ab9a8bc9a8420a1e6b56b07.jsonl[11849] _id=6ad24926de269131f9e56b44 ts=2026-10-16T15:56:22.0930000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 58 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `647ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[93] _id=6ac3c07ede269131f9ad0afb ts=2026-10-05T15:21:33.5470000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[98] _id=6ac3c07ede269131f9ad0b17 ts=2026-10-05T15:21:34.1940000Z`; `953ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[98] _id=6ac3c07ede269131f9ad0b17 ts=2026-10-05T15:21:34.1940000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[100] _id=6ac3c07fde269131f9ad0b2b ts=2026-10-05T15:21:35.1470000Z`; `113ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[100] _id=6ac3c07fde269131f9ad0b2b ts=2026-10-05T15:21:35.1470000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[102] _id=6ac3c080de269131f9ad0b35 ts=2026-10-05T15:21:35.2600000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 121 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `147ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[1133] _id=6ac51618de269131f9b48d04 ts=2026-10-06T15:39:01.1230000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[1134] _id=6ac51618de269131f9b48d08 ts=2026-10-06T15:39:01.2700000Z`; `201ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[1188] _id=6ac51635de269131f9b48f4f ts=2026-10-06T15:39:26.5990000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[1199] _id=6ac51635de269131f9b48f53 ts=2026-10-06T15:39:26.8000000Z`; `129ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[1199] _id=6ac51635de269131f9b48f53 ts=2026-10-06T15:39:26.8000000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[1189] _id=6ac51635de269131f9b48f55 ts=2026-10-06T15:39:26.9290000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `256ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10877] _id=6ad240ecde269131f9e5228d ts=2026-10-16T15:21:16.1620000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[10878] _id=6ad240edde269131f9e52293 ts=2026-10-16T15:21:16.4180000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `868ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10616] _id=6ad23f46de269131f9e50dac ts=2026-10-16T15:14:14.0230000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[10614] _id=6ad23f47de269131f9e50db8 ts=2026-10-16T15:14:14.8910000Z`; `806ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10630] _id=6ad23f57de269131f9e50e5a ts=2026-10-16T15:14:31.1090000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[10627] _id=6ad23f58de269131f9e50e72 ts=2026-10-16T15:14:31.9150000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[6714] _id=6acf9fb6de269131f9d4b35d ts=2026-10-14T15:28:53.6470000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[6717] _id=6acf9fb6de269131f9d4b360 ts=2026-10-14T15:28:53.6820000Z`; `53ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10738] _id=6ad23fd7de269131f9e515cf ts=2026-10-16T15:16:39.1890000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[10741] _id=6ad23fd7de269131f9e515d3 ts=2026-10-16T15:16:39.2420000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 13 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `71ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[684] _id=6ac3c5e9de269131f9ad691d ts=2026-10-05T15:44:40.3460000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[685] _id=6ac3c5e9de269131f9ad6921 ts=2026-10-05T15:44:40.4170000Z`; `949ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[806] _id=6ac512ecde269131f9b45af3 ts=2026-10-06T15:25:31.7650000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[807] _id=6ac512edde269131f9b45af7 ts=2026-10-06T15:25:32.7140000Z`; `447ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[825] _id=6ac5132dde269131f9b45c65 ts=2026-10-06T15:26:36.3910000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[829] _id=6ac5132dde269131f9b45c6d ts=2026-10-06T15:26:36.8380000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `916ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[6639] _id=6acf9f80de269131f9d4b073 ts=2026-10-14T15:27:59.9870000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[6641] _id=6acf9f81de269131f9d4b082 ts=2026-10-14T15:28:00.9030000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[788] _id=6ac512a9de269131f9b459fb ts=2026-10-06T15:24:23.9620000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[781] _id=6ac512a9de269131f9b459fd ts=2026-10-06T15:24:23.9650000Z`; `8ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[11993] _id=6ad249ffde269131f9e57ae1 ts=2026-10-16T15:59:58.4860000Z ~ 6ab9a8bc9a8420a1e6b56b07.jsonl[11989] _id=6ad249ffde269131f9e57ae5 ts=2026-10-16T15:59:58.4940000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3356] _id=6ac7b479de269131f9c38226 ts=2026-10-08T15:19:21.4960000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4705] _id=6ace483fde269131f9cf00f9 ts=2026-10-13T15:03:26.1520000Z; 24h 8m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2] _id=6ac3bf3cde269131f9ace78d ts=2026-10-05T15:16:11.6880000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[773] _id=6ac512a6de269131f9b459f3 ts=2026-10-06T15:24:22.1040000Z; 24h 1m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2118] _id=6ac66286de269131f9bb993e ts=2026-10-07T15:17:25.2980000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3353] _id=6ac7b46ede269131f9c380ab ts=2026-10-08T15:19:09.8160000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 59m 
  - Evidence: 23h 59m: 6ab9a8bc9a8420a1e6b56b07.jsonl[6214] _id=6acf9d46de269131f9d48eda ts=2026-10-14T15:18:29.6420000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[7950] _id=6ad0eec3de269131f9dc6f3f ts=2026-10-15T15:18:26.9890000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4699] _id=6ac7ba8fde269131f9c41eb4 ts=2026-10-08T15:45:19.5080000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4749] _id=6ace4863de269131f9cf0181 ts=2026-10-13T15:04:02.8620000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b07.jsonl[761] _id=6ac3c696de269131f9ad7741 ts=2026-10-05T15:47:33.3020000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[785] _id=6ac512cbde269131f9b45a3b ts=2026-10-06T15:24:58.3000000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3295] _id=6ac6692fde269131f9bc2760 ts=2026-10-07T15:45:50.1410000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3364] _id=6ac7b47dde269131f9c3826e ts=2026-10-08T15:19:24.0340000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 657 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10557] _id=6ad23f3bde269131f9e50d13 ts=2026-10-16T15:14:02.3700000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10558] _id=6ad23f3bde269131f9e50d14 ts=2026-10-16T15:14:02.3700000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10577] _id=6ad23f11de269131f9e50ade ts=2026-10-16T15:13:21.2600000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10578] _id=6ad23f11de269131f9e50adf ts=2026-10-16T15:13:21.2600000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10593] _id=6ad23f31de269131f9e50c56 ts=2026-10-16T15:13:52.5370000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10596] _id=6ad23f31de269131f9e50c57 ts=2026-10-16T15:13:52.5370000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 168h 6m 
  - Evidence: 168h 6m: 6ab9a8bc9a8420a1e6b56b07.jsonl[978] _id=6ac51473de269131f9b46b45 ts=2026-10-06T15:32:02.5770000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5446] _id=6ace5093de269131f9cf366d ts=2026-10-13T15:38:58.8490000Z; 47h 49m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5446] _id=6ace5093de269131f9cf366d ts=2026-10-13T15:38:58.8490000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[8200] _id=6ad0f117de269131f9dc94be ts=2026-10-15T15:28:23.0080000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b07.jsonl[8200] _id=6ad0f117de269131f9dc94be ts=2026-10-15T15:28:23.0080000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[11104] _id=6ad2432fde269131f9e54138 ts=2026-10-16T15:30:54.9690000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4677] _id=6ac7ba2bde269131f9c41b2d ts=2026-10-08T15:43:38.6780000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4714] _id=6ace4851de269131f9cf0123 ts=2026-10-13T15:03:42.4210000Z; 23h 36m: 6ab9a8bc9a8420a1e6b56b07.jsonl[764] _id=6ac3c6a3de269131f9ad77c9 ts=2026-10-05T15:47:46.4640000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[782] _id=6ac512b1de269131f9b45a13 ts=2026-10-06T15:24:32.7310000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3301] _id=6ac6693dde269131f9bc2879 ts=2026-10-07T15:46:04.9730000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3359] _id=6ac7b47dde269131f9c38269 ts=2026-10-08T15:19:24.0130000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 101 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10044] _id=6ad23badde269131f9e4bdcd ts=2026-10-16T14:58:52.3670000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10045] _id=6ad23badde269131f9e4bdce ts=2026-10-16T14:58:52.3670000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10046] _id=6ad23badde269131f9e4bdcf ts=2026-10-16T14:58:52.3680000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10047] _id=6ad23badde269131f9e4bdd0 ts=2026-10-16T14:58:52.3680000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10047] _id=6ad23badde269131f9e4bdd0 ts=2026-10-16T14:58:52.3680000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10048] _id=6ad23badde269131f9e4bdd1 ts=2026-10-16T14:58:52.3680000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4136] _id=6ac7b654de269131f9c3b823 ts=2026-10-08T15:27:16.2960000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4855] _id=6ace4bfbde269131f9cf0fb8 ts=2026-10-13T15:19:22.3990000Z; 23h 41m: 6ab9a8bc9a8420a1e6b56b07.jsonl[648] _id=6ac3c58bde269131f9ad625f ts=2026-10-05T15:43:06.8100000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[790] _id=6ac512cbde269131f9b45a39 ts=2026-10-06T15:24:58.2630000Z; 23h 35m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3305] _id=6ac66941de269131f9bc28d2 ts=2026-10-07T15:46:08.5800000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3413] _id=6ac7b4f7de269131f9c38ddf ts=2026-10-08T15:21:26.8640000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10381] _id=6ad23dcfde269131f9e4f175 ts=2026-10-16T15:07:58.4800000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10382] _id=6ad23dcfde269131f9e4f176 ts=2026-10-16T15:07:58.4800000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10435] _id=6ad23e1dde269131f9e4f946 ts=2026-10-16T15:09:16.3240000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10436] _id=6ad23e1dde269131f9e4f947 ts=2026-10-16T15:09:16.3240000Z; 5ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[395] _id=6ac3c219de269131f9ad2fa7 ts=2026-10-05T15:28:24.7010000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[401] _id=6ac3c219de269131f9ad2fab ts=2026-10-05T15:28:24.7060000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 18m 
  - Evidence: 119h 18m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4698] _id=6ac7ba9bde269131f9c41ef1 ts=2026-10-08T15:45:31.1380000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4713] _id=6ace4851de269131f9cf0122 ts=2026-10-13T15:03:37.5730000Z; 23h 36m: 6ab9a8bc9a8420a1e6b56b07.jsonl[766] _id=6ac3c6b0de269131f9ad7867 ts=2026-10-05T15:47:59.2230000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[774] _id=6ac512a9de269131f9b459f9 ts=2026-10-06T15:24:22.1160000Z; 23h 31m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3347] _id=6ac66990de269131f9bc300d ts=2026-10-07T15:47:27.0350000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3358] _id=6ac7b47dde269131f9c38268 ts=2026-10-08T15:19:21.5130000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10030] _id=6ad1190dde269131f9dee494 ts=2026-10-15T18:18:53.0670000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10034] _id=6ad23ba1de269131f9e4bd53 ts=2026-10-15T18:18:53.067Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 144h 3m 
  - Evidence: 144h 3m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4417] _id=6ac7b72cde269131f9c3dc03 ts=2026-10-08T15:30:51.5880000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6869] _id=6acfa106de269131f9d4c148 ts=2026-10-14T15:34:29.4020000Z; 23h 58m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2826] _id=6ac66418de269131f9bbb17b ts=2026-10-07T15:24:04.5810000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3453] _id=6ac7b549de269131f9c39638 ts=2026-10-08T15:22:48.3570000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2041] _id=6ac517a2de269131f9b4b329 ts=2026-10-06T15:45:35.6060000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[2226] _id=6ac66377de269131f9bb9f4d ts=2026-10-07T15:19:54.0280000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1476 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10036] _id=6ad23bd3de269131f9e4c00e ts=2026-10-16T14:59:29.6400000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10123] _id=6ad23bd4de269131f9e4c012 ts=2026-10-16T14:59:29.6400000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10064] _id=6ad23bb2de269131f9e4be13 ts=2026-10-16T14:58:57.5520000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10065] _id=6ad23bb2de269131f9e4be14 ts=2026-10-16T14:58:57.5520000Z; 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10066] _id=6ad23bb4de269131f9e4be29 ts=2026-10-16T14:58:58.6170000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10075] _id=6ad23bb4de269131f9e4be34 ts=2026-10-16T14:58:58.6170000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 11m 
  - Evidence: 144h 11m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3432] _id=6ac7b521de269131f9c3928f ts=2026-10-08T15:22:09.3190000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6843] _id=6acfa0bade269131f9d4be47 ts=2026-10-14T15:33:13.8650000Z; 24h 0m: 6ab9a8bc9a8420a1e6b56b07.jsonl[6861] _id=6acfa0eede269131f9d4c058 ts=2026-10-14T15:34:06.0540000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[8276] _id=6ad0f272de269131f9dcaa14 ts=2026-10-15T15:34:09.3330000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2057] _id=6ac517e4de269131f9b4babd ts=2026-10-06T15:46:43.4980000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3304] _id=6ac66941de269131f9bc28ce ts=2026-10-07T15:46:08.5750000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4669] _id=6ac7ba16de269131f9c41a47 ts=2026-10-08T15:43:18.3620000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5529] _id=6ace51d8de269131f9cf4240 ts=2026-10-13T15:44:23.9620000Z; 23h 57m: 6ab9a8bc9a8420a1e6b56b07.jsonl[6282] _id=6acf9d8ade269131f9d49559 ts=2026-10-14T15:19:38.2400000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[7920] _id=6ad0ee86de269131f9dc6b0a ts=2026-10-15T15:17:25.2890000Z; 23h 46m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3208] _id=6ac668b6de269131f9bc1e0f ts=2026-10-07T15:43:49.0910000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4337] _id=6ac7b706de269131f9c3d659 ts=2026-10-08T15:30:13.4850000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.028s shown 
  - Evidence: 22ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[2991] _id=6ac6661dde269131f9bbed78 ts=2026-10-07T15:32:44.9820000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[2993] _id=6ac6661ede269131f9bbed7a ts=2026-10-07T15:32:45.0040000Z; 28ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[2993] _id=6ac6661ede269131f9bbed7a ts=2026-10-07T15:32:45.0040000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[2997] _id=6ac6661ede269131f9bbed7e ts=2026-10-07T15:32:45.0320000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 168h 4m 
  - Evidence: 168h 4m: 6ab9a8bc9a8420a1e6b56b07.jsonl[866] _id=6ac5138bde269131f9b45df3 ts=2026-10-06T15:28:10.9290000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5319] _id=6ace4f2ade269131f9cf27b1 ts=2026-10-13T15:32:57.6110000Z; 47h 44m: 6ab9a8bc9a8420a1e6b56b07.jsonl[6699] _id=6acf9fb6de269131f9d4b359 ts=2026-10-14T15:28:53.6310000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10566] _id=6ad23f03de269131f9e50a35 ts=2026-10-16T15:13:06.3920000Z; 23h 52m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5360] _id=6ace4f77de269131f9cf2ba2 ts=2026-10-13T15:34:15.0940000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6617] _id=6acf9f4ade269131f9d4ae06 ts=2026-10-14T15:27:06.1810000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 168h 3m 
  - Evidence: 168h 3m: 6ab9a8bc9a8420a1e6b56b07.jsonl[867] _id=6ac5138bde269131f9b45df5 ts=2026-10-06T15:28:10.9580000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5278] _id=6ace4eecde269131f9cf2548 ts=2026-10-13T15:31:55.2580000Z; 47h 43m: 6ab9a8bc9a8420a1e6b56b07.jsonl[6717] _id=6acf9fb6de269131f9d4b360 ts=2026-10-14T15:28:53.6820000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10522] _id=6ad23ec4de269131f9e50787 ts=2026-10-16T15:12:03.5670000Z; 23h 52m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5353] _id=6ace4f78de269131f9cf2ba4 ts=2026-10-13T15:34:15.1170000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6581] _id=6acf9f29de269131f9d4ac59 ts=2026-10-14T15:26:33.0690000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.035s..0.035s shown 
  - Evidence: 35ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[6714] _id=6acf9fb6de269131f9d4b35d ts=2026-10-14T15:28:53.6470000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6717] _id=6acf9fb6de269131f9d4b360 ts=2026-10-14T15:28:53.6820000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 168h 3m 
  - Evidence: 168h 3m: 6ab9a8bc9a8420a1e6b56b07.jsonl[855] _id=6ac51384de269131f9b45dd9 ts=2026-10-06T15:28:03.7050000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5274] _id=6ace4eeede269131f9cf2567 ts=2026-10-13T15:31:58.0780000Z; 47h 43m: 6ab9a8bc9a8420a1e6b56b07.jsonl[6713] _id=6acf9fb3de269131f9d4b345 ts=2026-10-14T15:28:51.2290000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10511] _id=6ad23ebede269131f9e5072c ts=2026-10-16T15:11:57.6120000Z; 23h 52m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5352] _id=6ace4f76de269131f9cf2b8c ts=2026-10-13T15:34:13.4050000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6578] _id=6acf9f23de269131f9d4ac24 ts=2026-10-14T15:26:27.3540000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 32 interval(s) ≤ 0.000s..0.007s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10700] _id=6ad23fb3de269131f9e51394 ts=2026-10-16T15:16:02.9640000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10701] _id=6ad23fb3de269131f9e51395 ts=2026-10-16T15:16:02.9640000Z; 6ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[5304] _id=6ace4f21de269131f9cf272c ts=2026-10-13T15:32:48.4600000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5310] _id=6ace4f21de269131f9cf2730 ts=2026-10-13T15:32:48.4660000Z; 7ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[10516] _id=6ad23ec1de269131f9e50758 ts=2026-10-16T15:12:01.1130000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[10514] _id=6ad23ec1de269131f9e5075c ts=2026-10-16T15:12:01.1200000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 5m 
  - Evidence: 168h 5m: 6ab9a8bc9a8420a1e6b56b07.jsonl[874] _id=6ac51386de269131f9b45de5 ts=2026-10-06T15:28:05.8950000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[5323] _id=6ace4f38de269131f9cf2828 ts=2026-10-13T15:33:11.2410000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5331] _id=6ace4f51de269131f9cf29bd ts=2026-10-13T15:33:36.6610000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[6638] _id=6acf9f7bde269131f9d4b041 ts=2026-10-14T15:27:55.4150000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 15m 22s 
  - Evidence: 15m 22s: 6ab9a8bc9a8420a1e6b56b07.jsonl[11112] _id=6ad24346de269131f9e54238 ts=2026-10-16T15:31:17.5930000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[11627] _id=6ad246e0de269131f9e56101 ts=2026-10-16T15:46:39.7280000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3355] _id=6ac7b46ede269131f9c380b0 ts=2026-10-08T15:19:09.9880000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4707] _id=6ace483fde269131f9cf00fc ts=2026-10-13T15:03:26.4810000Z; 24h 8m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5] _id=6ac3bf24de269131f9ace709 ts=2026-10-05T15:15:47.8580000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[776] _id=6ac5129dde269131f9b459d5 ts=2026-10-06T15:24:12.8030000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2099] _id=6ac6626fde269131f9bb992c ts=2026-10-07T15:17:01.5870000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3355] _id=6ac7b46ede269131f9c380b0 ts=2026-10-08T15:19:09.9880000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3354] _id=6ac7b46ede269131f9c380af ts=2026-10-08T15:19:09.9880000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4706] _id=6ace483fde269131f9cf00fb ts=2026-10-13T15:03:26.4810000Z; 24h 8m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4] _id=6ac3bf24de269131f9ace707 ts=2026-10-05T15:15:47.8570000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[775] _id=6ac5129dde269131f9b459d3 ts=2026-10-06T15:24:12.8020000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2098] _id=6ac6626fde269131f9bb992b ts=2026-10-07T15:17:01.5870000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3354] _id=6ac7b46ede269131f9c380af ts=2026-10-08T15:19:09.9880000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 19m 
  - Evidence: 143h 19m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3349] _id=6ac66994de269131f9bc304b ts=2026-10-07T15:47:30.4720000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4785] _id=6ace4910de269131f9cf059b ts=2026-10-13T15:06:55.8730000Z; 25h 6m: 6ab9a8bc9a8420a1e6b56b07.jsonl[5622] _id=6acf997fde269131f9d442f4 ts=2026-10-14T15:02:23.1110000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[9384] _id=6ad0fa8ede269131f9dd445f ts=2026-10-15T16:08:46.3730000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b07.jsonl[2103] _id=6ac6626ede269131f9bb9928 ts=2026-10-06T15:47:33.798Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3349] _id=6ac66994de269131f9bc304b ts=2026-10-07T15:47:30.4720000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 28m 
  - Evidence: 119h 28m: 6ab9a8bc9a8420a1e6b56b07.jsonl[4493] _id=6ac7b818de269131f9c3f341 ts=2026-10-08T15:34:48.1940000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[4741] _id=6ace4851de269131f9cf013e ts=2026-10-13T15:03:42.4780000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b07.jsonl[740] _id=6ac3c66bde269131f9ad7271 ts=2026-10-05T15:46:50.7680000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[788] _id=6ac512a9de269131f9b459fb ts=2026-10-06T15:24:23.9620000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b07.jsonl[3292] _id=6ac6692bde269131f9bc273d ts=2026-10-07T15:45:46.8940000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[3366] _id=6ac7b47dde269131f9c38270 ts=2026-10-08T15:19:24.1010000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[11848] _id=6ad24926de269131f9e56b43 ts=2026-10-16T15:56:22.0930000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[11849] _id=6ad24926de269131f9e56b44 ts=2026-10-16T15:56:22.0930000Z; 3ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[649] _id=6ac3c58cde269131f9ad6279 ts=2026-10-05T15:43:06.8350000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[601] _id=6ac3c58cde269131f9ad627e ts=2026-10-05T15:43:06.8380000Z; 3ms: 6ab9a8bc9a8420a1e6b56b07.jsonl[788] _id=6ac512a9de269131f9b459fb ts=2026-10-06T15:24:23.9620000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[781] _id=6ac512a9de269131f9b459fd ts=2026-10-06T15:24:23.9650000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 44m 16s 
  - Evidence: 44m 16s: 6ab9a8bc9a8420a1e6b56b07.jsonl[9367] _id=6ad0fa54de269131f9dd3e1c ts=2026-10-15T16:07:48.7460000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[9478] _id=6ad104b6de269131f9ddfa71 ts=2026-10-15T16:52:05.6880000Z; 10m 22s: 6ab9a8bc9a8420a1e6b56b07.jsonl[8898] _id=6ad0f567de269131f9dcdbfa ts=2026-10-15T15:46:46.9010000Z -> 6ab9a8bc9a8420a1e6b56b07.jsonl[9049] _id=6ad0f7d5de269131f9dcf709 ts=2026-10-15T15:57:09.2400000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[639] _id=6ac3c573de269131f9ad60db ts=2026-10-05T15:42:42.5670000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[730] _id=6ac3c65bde269131f9ad70b9 ts=2026-10-05T15:46:34.4370000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[878] _id=6ac513a1de269131f9b45e45 ts=2026-10-06T15:28:32.3030000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 26 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[1280] _id=6ac51659de269131f9b492d7 ts=2026-10-06T15:40:06.8240000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1260] _id=6ac51659de269131f9b492d9 ts=2026-10-06T15:40:07.1280000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1309] _id=6ac51667de269131f9b4947e ts=2026-10-06T15:40:20.3670000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 63 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[1185] _id=6ac51634de269131f9b48f1f ts=2026-10-06T15:39:16.6420000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1226] _id=6ac51640de269131f9b4909c ts=2026-10-06T15:39:42.7200000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1276] _id=6ac51658de269131f9b492bb ts=2026-10-06T15:40:06.1510000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[6717] _id=6acf9fb6de269131f9d4b360 ts=2026-10-14T15:28:53.6820000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[10741] _id=6ad23fd7de269131f9e515d3 ts=2026-10-16T15:16:39.2420000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[685] _id=6ac3c5e9de269131f9ad6921 ts=2026-10-05T15:44:40.4170000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[11112] _id=6ad24346de269131f9e54238 ts=2026-10-16T15:31:17.5930000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[11627] _id=6ad246e0de269131f9e56101 ts=2026-10-16T15:46:39.7280000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[420] _id=6ac3c25ede269131f9ad3345 ts=2026-10-05T15:29:33.5920000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 185 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[1416] _id=6ac5167fde269131f9b498f7 ts=2026-10-06T15:40:45.2680000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1417] _id=6ac51680de269131f9b4990e ts=2026-10-06T15:40:45.3510000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1414] _id=6ac51682de269131f9b49958 ts=2026-10-06T15:40:48.7540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 464 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[1083] _id=6ac515cbde269131f9b487c6 ts=2026-10-06T15:37:45.5860000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1090] _id=6ac515cbde269131f9b487ca ts=2026-10-06T15:37:45.5860000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1084] _id=6ac515cbde269131f9b487d4 ts=2026-10-06T15:37:45.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[3412] _id=6ac7b4f7de269131f9c38dd6 ts=2026-10-08T15:21:26.8580000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[5326] _id=6ace4f4cde269131f9cf297b ts=2026-10-13T15:33:31.3980000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[5328] _id=6ace4f4fde269131f9cf29ab ts=2026-10-13T15:33:34.7330000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[5331] _id=6ace4f51de269131f9cf29bd ts=2026-10-13T15:33:36.6610000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 432 start, 426 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 51 unmatched 'BecameCameraCentered' (totals: 572 open, 547 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 64 unmatched 'BecameVisible' (totals: 1024 open, 1023 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 10 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 54 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 242 of 12084 adjacent _id pairs reverse in client time; worst 121.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b07.jsonl[1173] _id=6ac51630de269131f9b48ebd ts=2026-10-06T15:39:27.8860000Z`; `6ab9a8bc9a8420a1e6b56b07.jsonl[1179] _id=6ac51631de269131f9b48ecf ts=2026-10-06T15:37:26.6780000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.81s, min -84569.00s, max -0.10s over 12085 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b07\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

No coverage-related findings.

## 9. Event-Type Details

### `InputEvent` — 3304 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (884); Unit 2 Prod (Refactor) (812); Unit 4 Dev - Dungeon (467); Unit 1 Dev (354); Unit 3 Dungeon Dev (286); Unit 4 Dev (211); Unit 5 Dev - Dungeon (112); Unit 4 Dev - Anderson Base (109); Unit 5 Dev (69)
- **Intervals:** median 1.63s (p5 0.12s / p95 20.28s, n=3303)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3304/3304 records)
    "pressed"  x3304
data.actionType  (string, 3304/3304 records)
    "Move"  x2226
    "Interact"  x522
    "Jump"  x368
    "Ascend"  x124
    "Hoverboard"  x38
    "Sprint"  x16
    "Map"  x8
    "ToggleDebug"  x2
data.key  (string, 3304/3304 records, 7 empty-string)
    14 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3304/3304 records)
    "Player"  x2387
    "Drone"  x917
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 3166 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2178); Unit 4 Dev (496); Unit 3 Dungeon Dev (290); Unit 5 Dev - Dungeon (202)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.06s, n=3165)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3166/3166 records)
    "BecameVisible"  x1024
    "BecameInvisible"  x1023
    "BecameCameraCentered"  x572
    "BecameCameraUncentered"  x547
data.pieceId  (string, 3166/3166 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3166/3166 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2315 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (649); Unit 3 Dev (364); Unit 4 Dev (314); Unit 1 Dev (231); Unit 5 Dev (210); Unit 3 Dungeon Dev (189); Unit 4 Dev - Dungeon (179); Unit 4 Dev - Anderson Base (113); Unit 5 Dev - Dungeon (66)
- **eventKey:** present on 1457 of 2315 records
- **Intervals:** median 3.67s (p5 0.00s / p95 28.75s, n=2314)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1457; [conversationId, dialogueEventType] x858
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2315/2315 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2315/2315 records)
    "DialogueNodeEvent"  x1457
    "DialogueStartEvent"  x432
    "DialogueFinishEvent"  x426
data.nodeId  (number, 1457/2315 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2024 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (569); Unit 3 Dev (312); Unit 4 Dev (254); Unit 1 Dev (237); Unit 4 Dev - Dungeon (225); Unit 3 Dungeon Dev (158); Unit 5 Dev (108); Unit 5 Dev - Dungeon (92); Unit 4 Dev - Anderson Base (69)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.13s, n=2012)
- **Fields under `data`:**

```text
data.position  (object, 2024/2024 records)
data.position.x  (number, 2024/2024 records)
    numeric range -661.466 .. 1549.85 (809 unique)
data.position.y  (number, 2024/2024 records)
    numeric range -115.127 .. 222.252 (547 unique)
data.position.z  (number, 2024/2024 records)
    numeric range -1268.45 .. 1821.21 (808 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 411 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (148); Unit 2 Prod (Refactor) (68); Unit 3 Dungeon Dev (63); Unit 1 Dev (53); Unit 5 Dev (26); Unit 4 Dev (22); Unit 3 Dev (15); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (7)
- **Intervals:** median 8.79s (p5 0.17s / p95 328.34s, n=410)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 411/411 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 411/411 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 382 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (139); Unit 3 Dev (87); Unit 1 Dev (67); Unit 2 Prod (Refactor) (55); Unit 5 Dev (34)
- **Intervals:** median 0.75s (p5 0.03s / p95 8.51s, n=381)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 382/382 records)
    "argumentationNodeHoverEnd"  x160
    "argumentationNodeHoverStart"  x159
    "argumentationNodeAdd"  x44
    "argumentationNodeRemove"  x19
data.argumentationTitle  (string, 382/382 records)
    "Unit 4 - Flooding"  x139
    "Unit 3 - Pollution Upstream"  x87
    "Unit 2 – Watershed"  x55
    "Unit 1 - Argumentation Tutorial"  x37
    "Unit 5"  x34
    "Unit 1 - Freshwater"  x30
data.nodeName  (string, 382/382 records)
    "A"  x57
    "C"  x54
    "I"  x52
    "1"  x41
    "B"  x40
    "II"  x37
    "D"  x26
    "2"  x25
    "3"  x25
    "4"  x18
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 93 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (18); Unit 2 Prod (Refactor) (17); Unit 1 Dev (16); Unit 4 Dev (13); Unit 3 Dev (10); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 93 of 93 records
- **Intervals:** median 189.45s (p5 0.01s / p95 84232.19s, n=92)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 93/93 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x39
data.questID  (string, 93/93 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 93/93 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/93 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 83 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (52); Unit 4 Dev (16); Unit 3 Dev (15)
- **Intervals:** median 2.50s (p5 0.37s / p95 16.57s, n=82)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x74; [Soil Key Puzzle Status, Unit] x9
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/83 records)
    "Started"  x5
    "Finished"  x4
data.Unit  (string, 9/83 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 74/83 records)
    "RightDrag"  x43
    "LeftDrag"  x31
data.currentSoilType  (string, 74/83 records)
    "SAND"  x18
    "CLAYSAND"  x17
    "CLAY"  x13
    "CLAYROCK"  x11
    "SANDGRAVEL"  x10
    "BEDROCK"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 74/83 records)
    "false"  x53
    "true"  x21
data.waterLevelStatus  (string, 74/83 records)
    "TooHigh"  x33
    "Proper"  x30
    "TooLow"  x11
data.waterRetentionChange  (string, 74/83 records)
    "Increase"  x33
    "NoChange"  x21
    "Decrease"  x20
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 81 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (41); Unit 2 Prod (Refactor) (40)
- **Intervals:** median 4.87s (p5 1.05s / p95 84094.61s, n=80)
- **`data` key-set variants:** [actionType, featureUsed] x42; [actionType, featureUsed, location] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 81/81 records)
    "WaypointMoveEvent"  x34
    "MapCloseEvent"  x21
    "MapOpenEvent"  x21
    "WaypointSetEvent"  x5
data.featureUsed  (string, 81/81 records)
    "Map"  x42
    "Waypoint"  x39
data.location  (object, 39/81 records)
data.location.x  (number, 39/81 records)
    numeric range -225.655 .. 538.192 (35 unique)
data.location.y  (number, 39/81 records)
    numeric range -149.456 .. 224.515 (37 unique)
data.location.z  (number, 39/81 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 33 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (12); Unit 4 Dev (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 658.92s (p5 8.60s / p95 86678.17s, n=32)
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "DebugMenuStateChanged"  x33
data.isOpened  (bool, 33/33 records)
    false  x33
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `soilMachine` — 33 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (33)
- **Intervals:** median 13.68s (p5 2.34s / p95 398.91s, n=32)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "ChangeCanister"  x33
data.canisterType  (string, 33/33 records)
    "Clay"  x10
    "Gravel"  x10
    "Sand"  x7
    "Bedrock"  x6
data.floor  (string, 33/33 records)
    "5"  x11
    "2"  x8
    "4"  x8
    "3"  x6
data.machine  (string, 33/33 records)
    "1"  x31
    "2"  x2
data.row  (string, 33/33 records)
    "TopRow"  x28
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 31 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (17); Unit 3 Dev (8); Unit 1 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (1)
- **Intervals:** median 14.74s (p5 1.07s / p95 133206.01s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "submitAnswerEvent"  x31
data.answerSubmitted  (string, 31/31 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 31/31 records)
    "Unit 4 - Flooding"  x17
    "Unit 3 - Pollution Upstream"  x8
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 22 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (22)
- **Intervals:** median 19.96s (p5 7.32s / p95 80.97s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "On"  x16
    "Off"  x6
data.floor  (string, 22/22 records)
    "3"  x9
    "4"  x8
    "2"  x3
    "1"  x2
data.machineNumber  (string, 22/22 records)
    "One"  x20
    "Two"  x2
data.machineType  (string, 22/22 records)
    "Condenser"  x11
    "Evaporator"  x6
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 22/22 records)
    "2"  x9
    "3"  x6
    "1"  x4
    "4"  x3
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `TerasGardenBox` — 18 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (18)
- **Intervals:** median 1.68s (p5 0.58s / p95 17.49s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records, 11 empty-string)
    ""  x11
    "cameraPlaced"  x7
data.boxId  (string, 18/18 records)
    "1"  x9
    "0"  x6
    "2"  x3
data.soilType  (string, 18/18 records)
    "Sand"  x9
    "Clay"  x7
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 41.86s (p5 0.05s / p95 258436.77s, n=17)
- **Open findings:** 1 — see sections 5-8
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

### `gameWindowFocusEvent` — 18 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 2399.19s (p5 446.75s / p95 155735.25s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 15 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (15)
- **Intervals:** median 39869.79s (p5 1116.20s / p95 207357.99s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (4); Unit 1 Dev (1)
- **Intervals:** median 4.14s (p5 1.21s / p95 397486.71s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolOpen"  x10
data.argumentationTitle  (string, 10/10 records)
    "Unit 2 – Watershed"  x5
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Waterfall Data"  x4
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `SolarStillDesignEvent` — 9 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (9)
- **Intervals:** median 2.02s (p5 1.45s / p95 3.54s, n=8)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x8; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "optionSelected"  x8
    "DesignSubmitted"  x1
data.designSelections  (object, 1/9 records)
data.designSelections.glassRoofTemperature  (string, 1/9 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/9 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/9 records)
    "Tilted In"  x1
data.featureUsed  (string, 9/9 records)
    "RoofStyle"  x4
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "Submit"  x1
data.selectedOption  (string, 8/9 records)
    "Tilted In"  x2
    "Tilted Out"  x2
    "Cold"  x1
    "Covered"  x1
    "Hot"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 1 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 86373.63s (p5 4039.99s / p95 388290.76s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 129358.06s (p5 14727.16s / p95 540258.46s, n=4)
- **Open findings:** 1 — see sections 5-8
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

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 4.30s (p5 2.17s / p95 77758.04s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 922.13s (p5 922.13s / p95 922.13s, n=1)
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

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (52 records)
- `TerasGardenBox` data.actionType: "" (11x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (34x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (39x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (19x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*