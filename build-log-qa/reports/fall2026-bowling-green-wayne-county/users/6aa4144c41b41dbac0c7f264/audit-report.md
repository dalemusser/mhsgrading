# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f264

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f264
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f264.jsonl
- **Records:** 14756 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f264
- **Time span:** 2026-09-23T18:15:33.570000+00:00 .. 2026-10-07T18:48:56.516000+00:00 (336h 33m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f264\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 14756 records, 11 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 107 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4194 | 28.42 | 1 | 4 | 0 | 2026-09-25T18:14:02.793000+00:00 | 2026-10-07T15:57:44.683000+00:00 | 285h 43m |
| InputEvent | 4182 | 28.34 | 1 | 9 | 0 | 2026-09-23T18:21:01.705000+00:00 | 2026-10-07T18:48:56.516000+00:00 | 336h 27m |
| PlayerPositionEvent | 2816 | 19.08 | 1 | 9 | 0 | 2026-09-23T18:16:15.325000+00:00 | 2026-10-07T18:48:49.808000+00:00 | 336h 32m |
| DialogueEvent | 2270 | 15.38 | 1 | 9 | 1389 | 2026-09-23T18:16:36.964000+00:00 | 2026-10-07T18:48:46.197000+00:00 | 336h 32m |
| ObjectInterEvent | 379 | 2.57 | 1 | 9 | 0 | 2026-09-23T18:22:07.266000+00:00 | 2026-10-07T18:48:56.515000+00:00 | 336h 26m |
| argumentationNodeEvent | 265 | 1.8 | 1 | 4 | 0 | 2026-09-24T18:03:34.820000+00:00 | 2026-10-07T16:17:52.454000+00:00 | 310h 14m |
| Soil Key Puzzle | 120 | 0.81 | 1 | 3 | 0 | 2026-09-28T18:31:39.661000+00:00 | 2026-10-05T18:17:26.571000+00:00 | 167h 45m |
| questEvent | 106 | 0.72 | 1 | 9 | 106 | 2026-09-23T18:16:36.947000+00:00 | 2026-10-07T18:44:04.963000+00:00 | 336h 27m |
| WaterChamberEvent | 68 | 0.46 | 1 | 1 | 0 | 2026-10-07T15:47:32.149000+00:00 | 2026-10-07T16:05:23.400000+00:00 | 17m 51s |
| soilMachine | 60 | 0.41 | 1 | 1 | 0 | 2026-10-05T18:36:43.553000+00:00 | 2026-10-06T18:25:08.838000+00:00 | 23h 48m |
| gameWindowFocusEvent | 59 | 0.4 | 1 | 10 | 0 | 2026-09-23T18:15:33.570000+00:00 | 2026-10-07T18:35:44.704000+00:00 | 336h 20m |
| TopographicMapEvent | 49 | 0.33 | 1 | 3 | 0 | 2026-09-25T18:14:35.926000+00:00 | 2026-10-06T18:33:55.720000+00:00 | 264h 19m |
| gameWindowUnfocusEvent | 45 | 0.3 | 1 | 9 | 0 | 2026-09-23T18:17:49.474000+00:00 | 2026-10-07T16:02:47.906000+00:00 | 333h 44m |
| DEBUGMenu | 31 | 0.21 | 1 | 9 | 0 | 2026-09-23T18:16:15.317000+00:00 | 2026-10-07T18:35:44.199000+00:00 | 336h 19m |
| gameStartEvent | 24 | 0.16 | 1 | 1 | 0 | 2026-09-23T18:15:33.571000+00:00 | 2026-10-07T18:35:44.704000+00:00 | 336h 20m |
| argumentationAnswerEvent | 20 | 0.14 | 1 | 4 | 0 | 2026-09-24T18:03:31.637000+00:00 | 2026-10-07T16:17:55.823000+00:00 | 310h 14m |
| TerasGardenBox | 17 | 0.12 | 1 | 1 | 0 | 2026-10-06T18:52:37.488000+00:00 | 2026-10-07T15:29:47.610000+00:00 | 20h 37m |
| DaniEvent | 12 | 0.08 | 1 | 3 | 0 | 2026-09-30T16:00:02.004000+00:00 | 2026-10-06T18:33:17.647000+00:00 | 146h 33m |
| argumentationEvent | 12 | 0.08 | 1 | 4 | 0 | 2026-09-24T18:00:58.378000+00:00 | 2026-10-07T16:17:55.845000+00:00 | 310h 16m |
| SolarStillDesignEvent | 8 | 0.05 | 1 | 1 | 0 | 2026-10-07T18:41:21.435000+00:00 | 2026-10-07T18:41:35.524000+00:00 | 14.1s |
| crash | 7 | 0.05 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 6 | 0.04 | 1 | 3 | 0 | 2026-09-30T16:00:06.745000+00:00 | 2026-10-07T18:35:52.808000+00:00 | 170h 35m |
| EndOfUnit | 4 | 0.03 | 1 | 4 | 0 | 2026-09-24T18:07:20.145000+00:00 | 2026-10-07T18:48:56.459000+00:00 | 312h 41m |
| argumentationToolEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-09-30T18:27:11.679000+00:00 | 2026-10-07T16:16:18.166000+00:00 | 165h 49m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1836.663s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 525398.966s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 9.414s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 4.3s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 6.392s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 596946.487s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 8303.519s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 406.217s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 524.308s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.418s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.2x vs baseline. 
  - Observed: 120 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` — record volume changed 3.4x vs baseline. 
  - Observed: 68 records 
  - Expected: 20 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; 2,3,; A,B,D,2,I; A,D,B,2,3,I; C,A,D,3,I; C,D,3,I; C,D,3,II; D,C,A,2,II 
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
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [11-26, 11-29, 11-26, 11-27, 11-25] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 24 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 54 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 12.0x vs baseline. 
  - Observed: 60 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 22 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[152] _id=6ab419bf485cab4c954f4a56 ts=2026-09-23T18:26:07.0510000Z`; `6aa4144c41b41dbac0c7f264.jsonl[299] _id=6ab41c3d485cab4c954f5d47 ts=2026-09-23T18:36:45.2490000Z`; `6aa4144c41b41dbac0c7f264.jsonl[321] _id=6ab41c89485cab4c954f5fef ts=2026-09-23T18:38:01.5060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[4688] _id=6abc0035485cab4c9584318f ts=2026-09-29T18:15:16.5440000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 24 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 24} 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[24] _id=6ab41745485cab4c954f3682 ts=2026-09-23T18:15:33.5710000Z`; `6aa4144c41b41dbac0c7f264.jsonl[413] _id=6ab56131485cab4c95537fbb ts=2026-09-24T17:43:12.3500000Z`; `6aa4144c41b41dbac0c7f264.jsonl[868] _id=6ab5672a485cab4c95541812 ts=2026-09-24T18:08:42.6690000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 59 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 59} 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[23] _id=6ab41745485cab4c954f3680 ts=2026-09-23T18:15:33.5700000Z`; `6aa4144c41b41dbac0c7f264.jsonl[43] _id=6ab417cd485cab4c954f3956 ts=2026-09-23T18:17:49.7800000Z`; `6aa4144c41b41dbac0c7f264.jsonl[188] _id=6ab41a51485cab4c954f4f00 ts=2026-09-23T18:28:33.9750000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 45 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 45} 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[47] _id=6ab417cd485cab4c954f3954 ts=2026-09-23T18:17:49.4740000Z`; `6aa4144c41b41dbac0c7f264.jsonl[187] _id=6ab41a4f485cab4c954f4eee ts=2026-09-23T18:28:31.7430000Z`; `6aa4144c41b41dbac0c7f264.jsonl[409] _id=6ab41e6d485cab4c954f70b7 ts=2026-09-23T18:46:05.3380000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4193 | 0.0 | 0.031 | 245.319 | 1.355 | 428556.683 | 0.24 | 2502 | 6 |
| InputEvent | 4181 | 0.0 | 0.801 | 289.709 | 22.107 | 425098.166 | 0.21 | 223 | 14 |
| PlayerPositionEvent | 2802 | 9.774 | 9.999 | 406.398 | 10.032 | 352287.339 | 0.15 | 0 | 13 |
| DialogueEvent | 2269 | 0.0 | 4.892 | 533.949 | 42.856 | 352419.035 | 0.11 | 668 | 15 |
| ObjectInterEvent | 378 | 0.001 | 11.409 | 3204.257 | 473.499 | 425605.97 | 0.02 | 6 | 18 |
| argumentationNodeEvent | 264 | 0.015 | 0.268 | 4230.521 | 4.525 | 519423.031 | 0.01 | 64 | 4 |
| Soil Key Puzzle | 119 | 0.116 | 0.652 | 5075.184 | 10.766 | 428732.486 | 0.01 | 0 | 3 |
| questEvent | 105 | 0.0 | 225.528 | 11535.695 | 76263.586 | 425300.127 | 0.01 | 22 | 21 |
| WaterChamberEvent | 67 | 0.125 | 4.3 | 15.989 | 79.132 | 111.497 | 3.75 | 0 | 0 |
| soilMachine | 59 | 0.138 | 5.418 | 1452.632 | 386.159 | 76288.407 | 0.04 | 0 | 2 |
| gameWindowFocusEvent | 58 | 0.048 | 406.217 | 20876.054 | 86054.928 | 352406.998 | 0.0 | 1 | 27 |
| TopographicMapEvent | 48 | 0.018 | 9.414 | 19824.162 | 78353.813 | 513821.751 | 0.0 | 3 | 10 |
| gameWindowUnfocusEvent | 44 | 0.158 | 524.308 | 27306.783 | 85991.283 | 427937.052 | 0.0 | 0 | 21 |
| DEBUGMenu | 30 | 4.794 | 1836.663 | 40358.963 | 181515.57 | 352411.643 | 0.0 | 0 | 21 |
| gameStartEvent | 23 | 53.881 | 8303.519 | 52643.962 | 241779.881 | 352406.996 | 0.0 | 0 | 18 |
| argumentationAnswerEvent | 19 | 0.176 | 6.392 | 58782.326 | 519508.872 | 519999.215 | 0.0 | 0 | 3 |
| TerasGardenBox | 16 | 0.366 | 2.393 | 4639.383 | 18552.237 | 74097.101 | 0.01 | 0 | 1 |
| DaniEvent | 11 | 1.501 | 6.954 | 47963.24 | 263774.194 | 442463.496 | 0.0 | 0 | 2 |
| argumentationEvent | 11 | 0.029 | 85.343 | 101547.042 | 519608.481 | 519794.101 | 0.0 | 1 | 3 |
| SolarStillDesignEvent | 7 | 0.512 | 0.991 | 2.013 | 4.938 | 5.671 | 29.81 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 5 | 5.243 | 1406.675 | 122829.213 | 484747.888 | 603768.851 | 0.0 | 0 | 3 |
| EndOfUnit | 3 | 11176.747 | 525398.966 | 375232.105 | 582748.438 | 589120.601 | 0.0 | 0 | 3 |
| argumentationToolEvent | 1 | 596946.487 | 596946.487 | 596946.487 | 596946.487 | 596946.487 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 5 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[3033] _id=6abaad19485cab4c956f77dd ts=2026-09-28T18:08:24.8860000Z == 6aa4144c41b41dbac0c7f264.jsonl[3043] _id=6abaad19485cab4c956f77e1 ts=2026-09-28T18:08:24.8860000Z`; `6aa4144c41b41dbac0c7f264.jsonl[12903] _id=6ac664f1de269131f9bbcd39 ts=2026-10-07T15:27:45.3920000Z == 6aa4144c41b41dbac0c7f264.jsonl[12904] _id=6ac664f1de269131f9bbcd3a ts=2026-10-07T15:27:45.3920000Z`; `6aa4144c41b41dbac0c7f264.jsonl[14517] _id=6ac69113de269131f9bdcf22 ts=2026-10-07T18:35:59.6990000Z == 6aa4144c41b41dbac0c7f264.jsonl[14518] _id=6ac69113de269131f9bdcf23 ts=2026-10-07T18:35:59.6990000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 137 group(s), 181 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[1034] _id=6ab6b9ec485cab4c955dcfa9 ts=2026-09-25T18:14:04.0190000Z == 6aa4144c41b41dbac0c7f264.jsonl[1081] _id=6ab6b9ec485cab4c955dcfab ts=2026-09-25T18:14:04.0190000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1301] _id=6ab6baba485cab4c955deb15 ts=2026-09-25T18:14:04.9020000Z == 6aa4144c41b41dbac0c7f264.jsonl[1293] _id=6ab6baba485cab4c955deb1b ts=2026-09-25T18:14:04.9020000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1319] _id=6ab6babb485cab4c955deb69 ts=2026-09-25T18:14:05.0290000Z == 6aa4144c41b41dbac0c7f264.jsonl[1329] _id=6ab6babc485cab4c955deb6d ts=2026-09-25T18:14:05.0290000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[27] _id=6ab41774485cab4c954f37a6 ts=? == 6aa4144c41b41dbac0c7f264.jsonl[420] _id=6ab56161485cab4c95538519 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[14457] _id=6ac670ffde269131f9bc5a44 ts=2026-10-07T16:19:11.2740000Z == 6aa4144c41b41dbac0c7f264.jsonl[14458] _id=6ac670ffde269131f9bc5a45 ts=2026-10-07T16:19:11.2740000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 36 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4144c41b41dbac0c7f264.jsonl[100] _id=6ab418cf485cab4c954f40de ts=2026-09-23T18:22:07.2660000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[101] _id=6ab418cf485cab4c954f40e0 ts=2026-09-23T18:22:07.2720000Z`; `2ms: 6aa4144c41b41dbac0c7f264.jsonl[462] _id=6ab561a2485cab4c95538afd ts=2026-09-24T17:45:05.2710000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[459] _id=6ab561a2485cab4c95538aff ts=2026-09-24T17:45:05.2730000Z`; `328ms: 6aa4144c41b41dbac0c7f264.jsonl[927] _id=6ab5680b485cab4c955422a4 ts=2026-09-24T18:12:27.3100000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[933] _id=6ab5680b485cab4c955422aa ts=2026-09-24T18:12:27.6380000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 497 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4144c41b41dbac0c7f264.jsonl[1033] _id=6ab6b9ec485cab4c955dcfa1 ts=2026-09-25T18:14:04.0130000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[1080] _id=6ab6b9ec485cab4c955dcfa3 ts=2026-09-25T18:14:04.0190000Z`; `23ms: 6aa4144c41b41dbac0c7f264.jsonl[1075] _id=6ab6b9ed485cab4c955dcfc3 ts=2026-09-25T18:14:04.0790000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[1076] _id=6ab6b9ed485cab4c955dcfc7 ts=2026-09-25T18:14:04.1020000Z`; `183ms: 6aa4144c41b41dbac0c7f264.jsonl[1082] _id=6ab6b9ed485cab4c955dcfce ts=2026-09-25T18:14:04.1020000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[1084] _id=6ab6b9ed485cab4c955dcfd3 ts=2026-09-25T18:14:04.2850000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `366ms: 6aa4144c41b41dbac0c7f264.jsonl[12964] _id=6ac66556de269131f9bbd6d9 ts=2026-10-07T15:29:26.6140000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[12972] _id=6ac66556de269131f9bbd6e8 ts=2026-10-07T15:29:26.9800000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6aa4144c41b41dbac0c7f264.jsonl[3283] _id=6abab093485cab4c956fee15 ts=2026-09-28T18:23:15.1280000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[3281] _id=6abab093485cab4c956fee1b ts=2026-09-28T18:23:15.1580000Z`; `18ms: 6aa4144c41b41dbac0c7f264.jsonl[3281] _id=6abab093485cab4c956fee1b ts=2026-09-28T18:23:15.1580000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[3289] _id=6abab093485cab4c956fee35 ts=2026-09-28T18:23:15.1760000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `986ms: 6aa4144c41b41dbac0c7f264.jsonl[13558] _id=6ac669bede269131f9bc31b2 ts=2026-10-07T15:48:14.4190000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[13545] _id=6ac669bfde269131f9bc31c8 ts=2026-10-07T15:48:15.4050000Z`; `307ms: 6aa4144c41b41dbac0c7f264.jsonl[13561] _id=6ac669bfde269131f9bc31c4 ts=2026-10-07T15:48:15.2520000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[13563] _id=6ac669bfde269131f9bc31cc ts=2026-10-07T15:48:15.5590000Z`; `306ms: 6aa4144c41b41dbac0c7f264.jsonl[13545] _id=6ac669bfde269131f9bc31c8 ts=2026-10-07T15:48:15.4050000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[13565] _id=6ac669bfde269131f9bc31cf ts=2026-10-07T15:48:15.7110000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `970ms: 6aa4144c41b41dbac0c7f264.jsonl[14236] _id=6ac67035de269131f9bc52de ts=2026-10-07T16:15:49.9090000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[14228] _id=6ac67036de269131f9bc52e4 ts=2026-10-07T16:15:50.8790000Z`; `190ms: 6aa4144c41b41dbac0c7f264.jsonl[14228] _id=6ac67036de269131f9bc52e4 ts=2026-10-07T16:15:50.8790000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[14237] _id=6ac67037de269131f9bc52e6 ts=2026-10-07T16:15:51.0690000Z`; `200ms: 6aa4144c41b41dbac0c7f264.jsonl[14237] _id=6ac67037de269131f9bc52e6 ts=2026-10-07T16:15:51.0690000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[14238] _id=6ac67037de269131f9bc52e8 ts=2026-10-07T16:15:51.2690000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `57ms: 6aa4144c41b41dbac0c7f264.jsonl[7906] _id=6abd5540485cab4c959197e9 ts=2026-09-30T18:30:24.8630000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[7904] _id=6abd5541485cab4c959197f3 ts=2026-09-30T18:30:24.9200000Z`; `29ms: 6aa4144c41b41dbac0c7f264.jsonl[12632] _id=6ac5425fde269131f9b6e943 ts=2026-10-06T18:47:59.2410000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[12637] _id=6ac5425fde269131f9b6e94b ts=2026-10-06T18:47:59.2700000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 32 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `236ms: 6aa4144c41b41dbac0c7f264.jsonl[739] _id=6ab565f9485cab4c9553f8fc ts=2026-09-24T18:03:37.0200000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[741] _id=6ab565f9485cab4c9553f906 ts=2026-09-24T18:03:37.2560000Z`; `359ms: 6aa4144c41b41dbac0c7f264.jsonl[740] _id=6ab565f9485cab4c9553f900 ts=2026-09-24T18:03:37.0540000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[743] _id=6ab565f9485cab4c9553f90c ts=2026-09-24T18:03:37.4130000Z`; `825ms: 6aa4144c41b41dbac0c7f264.jsonl[749] _id=6ab565fd485cab4c9553f994 ts=2026-09-24T18:03:41.4950000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[744] _id=6ab565fe485cab4c9553f9ae ts=2026-09-24T18:03:42.3200000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `208ms: 6aa4144c41b41dbac0c7f264.jsonl[969] _id=6ab56857485cab4c955424c6 ts=2026-09-24T18:13:43.3650000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[972] _id=6ab56857485cab4c955424ca ts=2026-09-24T18:13:43.5730000Z`; `48ms: 6aa4144c41b41dbac0c7f264.jsonl[13939] _id=6ac66d29de269131f9bc439b ts=2026-10-07T16:02:47.0520000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[13941] _id=6ac66d29de269131f9bc43a2 ts=2026-10-07T16:02:47.1000000Z`; `952ms: 6aa4144c41b41dbac0c7f264.jsonl[13941] _id=6ac66d29de269131f9bc43a2 ts=2026-10-07T16:02:47.1000000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[13943] _id=6ac66d29de269131f9bc43a4 ts=2026-10-07T16:02:48.0520000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `387ms: 6aa4144c41b41dbac0c7f264.jsonl[971] _id=6ab56857485cab4c955424c4 ts=2026-09-24T18:13:43.1040000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[970] _id=6ab56857485cab4c955424c8 ts=2026-09-24T18:13:43.4910000Z`; `158ms: 6aa4144c41b41dbac0c7f264.jsonl[12433] _id=6ac5406ade269131f9b6ad30 ts=2026-10-06T18:39:38.6020000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[12435] _id=6ac5406ade269131f9b6ad3b ts=2026-10-06T18:39:38.7600000Z`; `877ms: 6aa4144c41b41dbac0c7f264.jsonl[13064] _id=6ac6660bde269131f9bbec0d ts=2026-10-07T15:32:27.5520000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[13067] _id=6ac6660cde269131f9bbec28 ts=2026-10-07T15:32:28.4290000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f264.jsonl[4688] _id=6abc0035485cab4c9584318f ts=2026-09-29T18:15:16.5440000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[4694] _id=6abc0035485cab4c95843197 ts=2026-09-29T18:15:16.5480000Z`; `4ms: 6aa4144c41b41dbac0c7f264.jsonl[14523] _id=6ac69113de269131f9bdcf28 ts=2026-10-07T18:36:02.4540000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[14524] _id=6ac69113de269131f9bdcf29 ts=2026-10-07T18:36:02.4580000Z`; `9ms: 6aa4144c41b41dbac0c7f264.jsonl[14653] _id=6ac692a6de269131f9bdece3 ts=2026-10-07T18:42:46.8650000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[14654] _id=6ac692a6de269131f9bdece7 ts=2026-10-07T18:42:46.8740000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `939ms: 6aa4144c41b41dbac0c7f264.jsonl[10787] _id=6ac3eefdde269131f9af3ffe ts=2026-10-05T18:39:57.5640000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[10827] _id=6ac3eefede269131f9af4027 ts=2026-10-05T18:39:58.5030000Z`; `967ms: 6aa4144c41b41dbac0c7f264.jsonl[10965] _id=6ac3f072de269131f9af5dff ts=2026-10-05T18:46:10.8440000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[10971] _id=6ac3f073de269131f9af5e0f ts=2026-10-05T18:46:11.8110000Z`; `666ms: 6aa4144c41b41dbac0c7f264.jsonl[11807] _id=6ac53bdcde269131f9b64947 ts=2026-10-06T18:20:12.1020000Z ~ 6aa4144c41b41dbac0c7f264.jsonl[11809] _id=6ac53bdcde269131f9b64957 ts=2026-10-06T18:20:12.7680000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 97h 53m 
  - Evidence: 97h 53m: 6aa4144c41b41dbac0c7f264.jsonl[9427] _id=6abe8703485cab4c95abcd18 ts=2026-10-01T16:14:59.7310000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9446] _id=6ac3e79ede269131f9aebc19 ts=2026-10-05T18:08:31.3740000Z; 71h 56m: 6aa4144c41b41dbac0c7f264.jsonl[987] _id=6ab6b95e485cab4c955dbe80 ts=2026-09-25T18:11:42.2690000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3032] _id=6abaad12485cab4c956f7759 ts=2026-09-28T18:08:18.7520000Z; 24h 6m: 6aa4144c41b41dbac0c7f264.jsonl[3032] _id=6abaad12485cab4c956f7759 ts=2026-09-28T18:08:18.7520000Z -> 6aa4144c41b41dbac0c7f264.jsonl[4689] _id=6abc0033485cab4c95843134 ts=2026-09-29T18:15:15.4290000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 122h 54m 
  - Evidence: 122h 54m: 6aa4144c41b41dbac0c7f264.jsonl[6718] _id=6abd322d485cab4c958d2e34 ts=2026-09-30T16:00:45.7830000Z -> 6aa4144c41b41dbac0c7f264.jsonl[11148] _id=6ac3f28dde269131f9af6869 ts=2026-10-05T18:55:09.2790000Z; 23h 38m: 6aa4144c41b41dbac0c7f264.jsonl[11167] _id=6ac3f28fde269131f9af686b ts=2026-10-05T18:55:11.2530000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12221] _id=6ac53eecde269131f9b67ee3 ts=2026-10-06T18:33:16.1460000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 97h 53m 
  - Evidence: 97h 53m: 6aa4144c41b41dbac0c7f264.jsonl[9432] _id=6abe8716485cab4c95abcdde ts=2026-10-01T16:15:18.5970000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9450] _id=6ac3e7b8de269131f9aebdbd ts=2026-10-05T18:08:57.6320000Z; 71h 34m: 6aa4144c41b41dbac0c7f264.jsonl[2997] _id=6ab6bef5485cab4c955e4fd7 ts=2026-09-25T18:35:33.2150000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3086] _id=6abaad93485cab4c956f8989 ts=2026-09-28T18:10:27.3080000Z; 24h 0m: 6aa4144c41b41dbac0c7f264.jsonl[921] _id=6ab567ff485cab4c9554223e ts=2026-09-24T18:12:15.8110000Z -> 6aa4144c41b41dbac0c7f264.jsonl[997] _id=6ab6b983485cab4c955dc289 ts=2026-09-25T18:12:20.0540000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 668 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f264.jsonl[14242] _id=6ac6703ede269131f9bc5314 ts=2026-10-07T16:15:58.2800000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14243] _id=6ac6703ede269131f9bc5315 ts=2026-10-07T16:15:58.2800000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[14348] _id=6ac67092de269131f9bc556f ts=2026-10-07T16:17:21.9230000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14349] _id=6ac67092de269131f9bc5570 ts=2026-10-07T16:17:21.9230000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[14441] _id=6ac670ecde269131f9bc590c ts=2026-10-07T16:18:52.0940000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14442] _id=6ac670ecde269131f9bc590d ts=2026-10-07T16:18:52.0940000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 163h 38m 
  - Evidence: 163h 38m: 6aa4144c41b41dbac0c7f264.jsonl[9413] _id=6abd6b2f485cab4c95a3368f ts=2026-09-30T20:03:59.1110000Z -> 6aa4144c41b41dbac0c7f264.jsonl[13214] _id=6ac6686fde269131f9bc1af0 ts=2026-10-07T15:42:39.7120000Z; 145h 56m: 6aa4144c41b41dbac0c7f264.jsonl[860] _id=6ab566d8485cab4c9554105a ts=2026-09-24T18:07:20.1450000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9413] _id=6abd6b2f485cab4c95a3368f ts=2026-09-30T20:03:59.1110000Z; 3h 6m: 6aa4144c41b41dbac0c7f264.jsonl[13214] _id=6ac6686fde269131f9bc1af0 ts=2026-10-07T15:42:39.7120000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14753] _id=6ac69418de269131f9be1f97 ts=2026-10-07T18:48:56.4590000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 118h 4m 
  - Evidence: 118h 4m: 6aa4144c41b41dbac0c7f264.jsonl[9404] _id=6abd6b1a485cab4c95a3331f ts=2026-09-30T20:03:38.8180000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9447] _id=6ac3e7a6de269131f9aebc9b ts=2026-10-05T18:08:36.9840000Z; 71h 33m: 6aa4144c41b41dbac0c7f264.jsonl[2987] _id=6ab6bec2485cab4c955e4def ts=2026-09-25T18:34:42.8800000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3033] _id=6abaad19485cab4c956f77dd ts=2026-09-28T18:08:24.8860000Z; 23h 59m: 6aa4144c41b41dbac0c7f264.jsonl[962] _id=6ab56822485cab4c9554236a ts=2026-09-24T18:12:50.4770000Z -> 6aa4144c41b41dbac0c7f264.jsonl[991] _id=6ab6b969485cab4c955dbfbf ts=2026-09-25T18:11:53.9880000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 223 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f264.jsonl[12903] _id=6ac664f1de269131f9bbcd39 ts=2026-10-07T15:27:45.3920000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12904] _id=6ac664f1de269131f9bbcd3a ts=2026-10-07T15:27:45.3920000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[12904] _id=6ac664f1de269131f9bbcd3a ts=2026-10-07T15:27:45.3920000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12906] _id=6ac664f1de269131f9bbcd3b ts=2026-10-07T15:27:45.3920000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[14517] _id=6ac69113de269131f9bdcf22 ts=2026-10-07T18:35:59.6990000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14518] _id=6ac69113de269131f9bdcf23 ts=2026-10-07T18:35:59.6990000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 118h 13m 
  - Evidence: 118h 13m: 6aa4144c41b41dbac0c7f264.jsonl[9406] _id=6abd6b1d485cab4c95a333a0 ts=2026-09-30T20:03:41.7380000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9545] _id=6ac3e9a3de269131f9aed855 ts=2026-10-05T18:17:07.7080000Z; 72h 6m: 6aa4144c41b41dbac0c7f264.jsonl[2830] _id=6ab6bc7f485cab4c955e2675 ts=2026-09-25T18:25:03.4280000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3458] _id=6abab28b485cab4c957011b5 ts=2026-09-28T18:31:39.6640000Z; 24h 0m: 6aa4144c41b41dbac0c7f264.jsonl[964] _id=6ab56822485cab4c95542368 ts=2026-09-24T18:12:50.4740000Z -> 6aa4144c41b41dbac0c7f264.jsonl[1021] _id=6ab6b9ab485cab4c955dc925 ts=2026-09-25T18:12:59.7890000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f264.jsonl[12369] _id=6ac5400ede269131f9b6a0a3 ts=2026-10-06T18:38:06.6040000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12372] _id=6ac5400ede269131f9b6a0a7 ts=2026-10-06T18:38:06.6050000Z; 1ms: 6aa4144c41b41dbac0c7f264.jsonl[12415] _id=6ac5404fde269131f9b6a95b ts=2026-10-06T18:39:11.0370000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12416] _id=6ac5404fde269131f9b6a95f ts=2026-10-06T18:39:11.0380000Z; 1ms: 6aa4144c41b41dbac0c7f264.jsonl[12496] _id=6ac54162de269131f9b6c8a9 ts=2026-10-06T18:43:45.9970000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12497] _id=6ac54162de269131f9b6c8ab ts=2026-10-06T18:43:45.9980000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 97h 51m 
  - Evidence: 97h 51m: 6aa4144c41b41dbac0c7f264.jsonl[9443] _id=6abe8780485cab4c95abd42a ts=2026-10-01T16:17:04.0410000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9448] _id=6ac3e7a4de269131f9aebc7b ts=2026-10-05T18:08:31.3800000Z; 71h 27m: 6aa4144c41b41dbac0c7f264.jsonl[3026] _id=6ab6c03d485cab4c955e64c5 ts=2026-09-25T18:41:02.0740000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3038] _id=6abaad19485cab4c956f77d7 ts=2026-09-28T18:08:18.7580000Z; 23h 57m: 6aa4144c41b41dbac0c7f264.jsonl[977] _id=6ab56865485cab4c955424fc ts=2026-09-24T18:13:57.5440000Z -> 6aa4144c41b41dbac0c7f264.jsonl[984] _id=6ab6b964485cab4c955dbf43 ts=2026-09-25T18:11:42.2750000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 2m 
  - Evidence: 119h 2m: 6aa4144c41b41dbac0c7f264.jsonl[8540] _id=6abd5fb1485cab4c9592916e ts=2026-09-30T19:14:56.5080000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9564] _id=6ac3e9bdde269131f9aed979 ts=2026-10-05T18:17:33.1910000Z; 72h 12m: 6aa4144c41b41dbac0c7f264.jsonl[2812] _id=6ab6bc24485cab4c955e1f63 ts=2026-09-25T18:23:31.5840000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3578] _id=6abab396485cab4c95702483 ts=2026-09-28T18:36:05.4170000Z; 24h 45m: 6aa4144c41b41dbac0c7f264.jsonl[5380] _id=6abc02d8485cab4c95846d2f ts=2026-09-29T18:26:31.1080000Z -> 6aa4144c41b41dbac0c7f264.jsonl[8276] _id=6abd5f0f485cab4c95926f30 ts=2026-09-30T19:12:15.1120000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2502 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f264.jsonl[10006] _id=6ac3ea4bde269131f9aee2c5 ts=2026-10-05T18:19:54.6170000Z -> 6aa4144c41b41dbac0c7f264.jsonl[10000] _id=6ac3ea4bde269131f9aee2c7 ts=2026-10-05T18:19:54.6170000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[10012] _id=6ac3ea4fde269131f9aee321 ts=2026-10-05T18:19:58.6120000Z -> 6aa4144c41b41dbac0c7f264.jsonl[10019] _id=6ac3ea4fde269131f9aee325 ts=2026-10-05T18:19:58.6120000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[10013] _id=6ac3ea4fde269131f9aee327 ts=2026-10-05T18:19:58.6340000Z -> 6aa4144c41b41dbac0c7f264.jsonl[10023] _id=6ac3ea4fde269131f9aee329 ts=2026-10-05T18:19:58.6340000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 5m 
  - Evidence: 119h 5m: 6aa4144c41b41dbac0c7f264.jsonl[8267] _id=6abd5ee6485cab4c95926e9a ts=2026-09-30T19:11:35.2190000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9544] _id=6ac3e9a3de269131f9aed853 ts=2026-10-05T18:17:07.7050000Z; 48h 2m: 6aa4144c41b41dbac0c7f264.jsonl[3535] _id=6abab301485cab4c95701a29 ts=2026-09-28T18:33:37.9060000Z -> 6aa4144c41b41dbac0c7f264.jsonl[8127] _id=6abd567c485cab4c9591c1ad ts=2026-09-30T18:35:40.0300000Z; 34m 47s: 6aa4144c41b41dbac0c7f264.jsonl[8149] _id=6abd569c485cab4c9591c6f1 ts=2026-09-30T18:36:12.3900000Z -> 6aa4144c41b41dbac0c7f264.jsonl[8234] _id=6abd5ec3485cab4c95926e38 ts=2026-09-30T19:10:59.5570000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 20h 34m 
  - Evidence: 20h 34m: 6aa4144c41b41dbac0c7f264.jsonl[12782] _id=6ac543c9de269131f9b70ba1 ts=2026-10-06T18:54:00.9850000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12946] _id=6ac6653ade269131f9bbd452 ts=2026-10-07T15:28:58.0860000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 142h 43m 
  - Evidence: 142h 43m: 6aa4144c41b41dbac0c7f264.jsonl[9212] _id=6abd67ef485cab4c95a0656c ts=2026-09-30T19:50:07.2060000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12255] _id=6ac53f0dde269131f9b683a7 ts=2026-10-06T18:33:48.9570000Z; 71h 57m: 6aa4144c41b41dbac0c7f264.jsonl[1131] _id=6ab6ba19485cab4c955dd44b ts=2026-09-25T18:14:49.8620000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3128] _id=6abaae0f485cab4c956f9c53 ts=2026-09-28T18:12:30.9350000Z; 23h 51m: 6aa4144c41b41dbac0c7f264.jsonl[3295] _id=6abab0a3485cab4c956ff043 ts=2026-09-28T18:23:31.3790000Z -> 6aa4144c41b41dbac0c7f264.jsonl[4692] _id=6abc0035485cab4c95843175 ts=2026-09-29T18:15:16.4710000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.018s..0.048s shown 
  - Evidence: 18ms: 6aa4144c41b41dbac0c7f264.jsonl[3281] _id=6abab093485cab4c956fee1b ts=2026-09-28T18:23:15.1580000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3289] _id=6abab093485cab4c956fee35 ts=2026-09-28T18:23:15.1760000Z; 30ms: 6aa4144c41b41dbac0c7f264.jsonl[3283] _id=6abab093485cab4c956fee15 ts=2026-09-28T18:23:15.1280000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3281] _id=6abab093485cab4c956fee1b ts=2026-09-28T18:23:15.1580000Z; 48ms: 6aa4144c41b41dbac0c7f264.jsonl[3280] _id=6abab093485cab4c956fee01 ts=2026-09-28T18:23:15.0800000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3283] _id=6abab093485cab4c956fee15 ts=2026-09-28T18:23:15.1280000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 26m 
  - Evidence: 144h 26m: 6aa4144c41b41dbac0c7f264.jsonl[752] _id=6ab56601485cab4c9553fa14 ts=2026-09-24T18:03:45.6160000Z -> 6aa4144c41b41dbac0c7f264.jsonl[7851] _id=6abd5540485cab4c959197e7 ts=2026-09-30T18:30:24.8310000Z; 144h 17m: 6aa4144c41b41dbac0c7f264.jsonl[7851] _id=6abd5540485cab4c959197e7 ts=2026-09-30T18:30:24.8310000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12631] _id=6ac5425fde269131f9b6e940 ts=2026-10-06T18:47:59.2210000Z; 21h 27m: 6aa4144c41b41dbac0c7f264.jsonl[12631] _id=6ac5425fde269131f9b6e940 ts=2026-10-06T18:47:59.2210000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14201] _id=6ac67027de269131f9bc5277 ts=2026-10-07T16:15:35.7730000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 23m 
  - Evidence: 144h 23m: 6aa4144c41b41dbac0c7f264.jsonl[730] _id=6ab56601485cab4c9553fa1a ts=2026-09-24T18:03:45.6340000Z -> 6aa4144c41b41dbac0c7f264.jsonl[7700] _id=6abd5473485cab4c959175c3 ts=2026-09-30T18:26:59.7350000Z; 144h 17m: 6aa4144c41b41dbac0c7f264.jsonl[7904] _id=6abd5541485cab4c959197f3 ts=2026-09-30T18:30:24.9200000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12605] _id=6ac5423fde269131f9b6e4bf ts=2026-10-06T18:47:27.7800000Z; 21h 27m: 6aa4144c41b41dbac0c7f264.jsonl[12637] _id=6ac5425fde269131f9b6e94b ts=2026-10-06T18:47:59.2700000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14172] _id=6ac67008de269131f9bc51b9 ts=2026-10-07T16:15:04.8690000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.029s..0.029s shown 
  - Evidence: 29ms: 6aa4144c41b41dbac0c7f264.jsonl[12632] _id=6ac5425fde269131f9b6e943 ts=2026-10-06T18:47:59.2410000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12637] _id=6ac5425fde269131f9b6e94b ts=2026-10-06T18:47:59.2700000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 144h 17m 
  - Evidence: 144h 17m: 6aa4144c41b41dbac0c7f264.jsonl[7900] _id=6abd553c485cab4c95919717 ts=2026-09-30T18:30:19.9710000Z -> 6aa4144c41b41dbac0c7f264.jsonl[12591] _id=6ac5423bde269131f9b6e3c9 ts=2026-10-06T18:47:23.0020000Z; 141h 56m: 6aa4144c41b41dbac0c7f264.jsonl[747] _id=6ab56600485cab4c9553f9de ts=2026-09-24T18:03:43.7890000Z -> 6aa4144c41b41dbac0c7f264.jsonl[6714] _id=6abd321f485cab4c958d2d26 ts=2026-09-30T16:00:31.2320000Z; 21h 27m: 6aa4144c41b41dbac0c7f264.jsonl[12636] _id=6ac5425ede269131f9b6e91a ts=2026-10-06T18:47:58.0650000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14176] _id=6ac6700cde269131f9bc51d0 ts=2026-10-07T16:15:08.2310000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 64 interval(s) ≤ 0.015s..0.017s shown 
  - Evidence: 15ms: 6aa4144c41b41dbac0c7f264.jsonl[14183] _id=6ac67011de269131f9bc51f5 ts=2026-10-07T16:15:13.1690000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14185] _id=6ac67011de269131f9bc51f7 ts=2026-10-07T16:15:13.1840000Z; 17ms: 6aa4144c41b41dbac0c7f264.jsonl[14181] _id=6ac6700ede269131f9bc51e5 ts=2026-10-07T16:15:10.6830000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14179] _id=6ac6700ede269131f9bc51e7 ts=2026-10-07T16:15:10.7000000Z; 17ms: 6aa4144c41b41dbac0c7f264.jsonl[14366] _id=6ac67098de269131f9bc55a1 ts=2026-10-07T16:17:28.4920000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14358] _id=6ac67098de269131f9bc55a3 ts=2026-10-07T16:17:28.5090000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 165h 49m 
  - Evidence: 165h 49m: 6aa4144c41b41dbac0c7f264.jsonl[7703] _id=6abd547f485cab4c95917835 ts=2026-09-30T18:27:11.6790000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14261] _id=6ac67052de269131f9bc5387 ts=2026-10-07T16:16:18.1660000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 42m 
  - Evidence: 167h 42m: 6aa4144c41b41dbac0c7f264.jsonl[6708] _id=6abd320c485cab4c958d2bf5 ts=2026-09-30T16:00:11.9880000Z -> 6aa4144c41b41dbac0c7f264.jsonl[13219] _id=6ac66884de269131f9bc1bd6 ts=2026-10-07T15:43:00.8390000Z; 2h 24m: 6aa4144c41b41dbac0c7f264.jsonl[14038] _id=6ac66e03de269131f9bc4815 ts=2026-10-07T16:06:27.5140000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14506] _id=6ac68fdbde269131f9bdbe5e ts=2026-10-07T18:30:51.5480000Z; 23m 26s: 6aa4144c41b41dbac0c7f264.jsonl[13219] _id=6ac66884de269131f9bc1bd6 ts=2026-10-07T15:43:00.8390000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14038] _id=6ac66e03de269131f9bc4815 ts=2026-10-07T16:06:27.5140000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 97h 53m 
  - Evidence: 97h 53m: 6aa4144c41b41dbac0c7f264.jsonl[9425] _id=6abe86fc485cab4c95abccd4 ts=2026-10-01T16:14:52.6320000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9445] _id=6ac3e793de269131f9aebb47 ts=2026-10-05T18:08:19.6280000Z; 71h 56m: 6aa4144c41b41dbac0c7f264.jsonl[986] _id=6ab6b954485cab4c955dbd6d ts=2026-09-25T18:11:32.3460000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3031] _id=6abaad0c485cab4c956f7689 ts=2026-09-28T18:08:12.4840000Z; 24h 6m: 6aa4144c41b41dbac0c7f264.jsonl[3031] _id=6abaad0c485cab4c956f7689 ts=2026-09-28T18:08:12.4840000Z -> 6aa4144c41b41dbac0c7f264.jsonl[4680] _id=6abc001a485cab4c95842e01 ts=2026-09-29T18:14:50.0560000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 27 gap(s), longest 97h 53m 
  - Evidence: 97h 53m: 6aa4144c41b41dbac0c7f264.jsonl[9426] _id=6abe86fc485cab4c95abccd2 ts=2026-10-01T16:14:52.6300000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9444] _id=6ac3e792de269131f9aebb43 ts=2026-10-05T18:08:19.6280000Z; 71h 56m: 6aa4144c41b41dbac0c7f264.jsonl[985] _id=6ab6b954485cab4c955dbd6b ts=2026-09-25T18:11:32.3450000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3030] _id=6abaad0c485cab4c956f7681 ts=2026-09-28T18:08:12.4830000Z; 23h 56m: 6aa4144c41b41dbac0c7f264.jsonl[973] _id=6ab5685b485cab4c955424d8 ts=2026-09-24T18:13:47.0540000Z -> 6aa4144c41b41dbac0c7f264.jsonl[980] _id=6ab6b91e485cab4c955db88b ts=2026-09-25T18:10:38.4640000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.048s..0.048s shown 
  - Evidence: 48ms: 6aa4144c41b41dbac0c7f264.jsonl[13939] _id=6ac66d29de269131f9bc439b ts=2026-10-07T16:02:47.0520000Z -> 6aa4144c41b41dbac0c7f264.jsonl[13941] _id=6ac66d29de269131f9bc43a2 ts=2026-10-07T16:02:47.1000000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 118h 52m 
  - Evidence: 118h 52m: 6aa4144c41b41dbac0c7f264.jsonl[9419] _id=6abd6b50485cab4c95a33951 ts=2026-09-30T20:04:32.5010000Z -> 6aa4144c41b41dbac0c7f264.jsonl[11220] _id=6ac3f2f1de269131f9af68fb ts=2026-10-05T18:56:49.5530000Z; 72h 10m: 6aa4144c41b41dbac0c7f264.jsonl[981] _id=6ab6b925485cab4c955db98d ts=2026-09-25T18:10:45.9470000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3243] _id=6abab00e485cab4c956fdc43 ts=2026-09-28T18:21:02.7270000Z; 23h 56m: 6aa4144c41b41dbac0c7f264.jsonl[976] _id=6ab56865485cab4c955424fa ts=2026-09-24T18:13:56.8870000Z -> 6aa4144c41b41dbac0c7f264.jsonl[983] _id=6ab6b924485cab4c955db96d ts=2026-09-25T18:10:44.1390000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 118h 8m 
  - Evidence: 118h 8m: 6aa4144c41b41dbac0c7f264.jsonl[9410] _id=6abd6b24485cab4c95a334c6 ts=2026-09-30T20:03:48.8510000Z -> 6aa4144c41b41dbac0c7f264.jsonl[9477] _id=6ac3e878de269131f9aecad3 ts=2026-10-05T18:12:08.9780000Z; 71h 32m: 6aa4144c41b41dbac0c7f264.jsonl[2996] _id=6ab6bef5485cab4c955e4fd5 ts=2026-09-25T18:35:33.2040000Z -> 6aa4144c41b41dbac0c7f264.jsonl[3039] _id=6abaad1a485cab4c956f7821 ts=2026-09-28T18:08:24.9650000Z; 24h 0m: 6aa4144c41b41dbac0c7f264.jsonl[864] _id=6ab567b5485cab4c95541fad ts=2026-09-24T18:11:01.1580000Z -> 6aa4144c41b41dbac0c7f264.jsonl[989] _id=6ab6b964485cab4c955dbf4b ts=2026-09-25T18:11:48.4840000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f264.jsonl[13605] _id=6ac66a26de269131f9bc34f4 ts=2026-10-07T15:49:58.4480000Z -> 6aa4144c41b41dbac0c7f264.jsonl[13606] _id=6ac66a26de269131f9bc34f5 ts=2026-10-07T15:49:58.4480000Z; 0ms: 6aa4144c41b41dbac0c7f264.jsonl[14457] _id=6ac670ffde269131f9bc5a44 ts=2026-10-07T16:19:11.2740000Z -> 6aa4144c41b41dbac0c7f264.jsonl[14458] _id=6ac670ffde269131f9bc5a45 ts=2026-10-07T16:19:11.2740000Z; 1ms: 6aa4144c41b41dbac0c7f264.jsonl[679] _id=6ab564f9485cab4c9553d040 ts=2026-09-24T17:59:20.3080000Z -> 6aa4144c41b41dbac0c7f264.jsonl[650] _id=6ab564f9485cab4c9553d046 ts=2026-09-24T17:59:20.3090000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 21h 11m 
  - Evidence: 21h 11m: 6aa4144c41b41dbac0c7f264.jsonl[11184] _id=6ac3f2b8de269131f9af689f ts=2026-10-05T18:55:52.0850000Z -> 6aa4144c41b41dbac0c7f264.jsonl[11308] _id=6ac51cb8de269131f9b4dead ts=2026-10-06T16:07:20.4920000Z; 1h 50m: 6aa4144c41b41dbac0c7f264.jsonl[11526] _id=6ac51f08de269131f9b4f17f ts=2026-10-06T16:17:12.4090000Z -> 6aa4144c41b41dbac0c7f264.jsonl[11592] _id=6ac538f3de269131f9b62204 ts=2026-10-06T18:07:46.8090000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[6698] _id=6abd3206485cab4c958d2b2d ts=2026-09-30T16:00:02.0040000Z`; `6aa4144c41b41dbac0c7f264.jsonl[6702] _id=6abd3208485cab4c958d2b53 ts=2026-09-30T16:00:06.6350000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[670] _id=6ab564e1485cab4c9553ce5a ts=2026-09-24T17:58:56.6860000Z`; `6aa4144c41b41dbac0c7f264.jsonl[765] _id=6ab5662a485cab4c9553ffda ts=2026-09-24T18:04:26.4730000Z`; `6aa4144c41b41dbac0c7f264.jsonl[3222] _id=6abaafca485cab4c956fd3f5 ts=2026-09-28T18:19:54.5700000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 112 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[1438] _id=6ab6bade485cab4c955df115 ts=2026-09-25T18:18:05.6340000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1459] _id=6ab6baf9485cab4c955df557 ts=2026-09-25T18:18:32.5520000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1703] _id=6ab6bb1d485cab4c955dfc81 ts=2026-09-25T18:19:08.3250000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 152 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[1081] _id=6ab6b9ec485cab4c955dcfab ts=2026-09-25T18:14:04.0190000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1066] _id=6ab6b9ed485cab4c955dcfbc ts=2026-09-25T18:14:04.0790000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1288] _id=6ab6baba485cab4c955deb11 ts=2026-09-25T18:14:04.9020000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[7904] _id=6abd5541485cab4c959197f3 ts=2026-09-30T18:30:24.9200000Z`; `6aa4144c41b41dbac0c7f264.jsonl[12637] _id=6ac5425fde269131f9b6e94b ts=2026-10-06T18:47:59.2700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[13219] _id=6ac66884de269131f9bc1bd6 ts=2026-10-07T15:43:00.8390000Z`; `6aa4144c41b41dbac0c7f264.jsonl[14038] _id=6ac66e03de269131f9bc4815 ts=2026-10-07T16:06:27.5140000Z`; `6aa4144c41b41dbac0c7f264.jsonl[14506] _id=6ac68fdbde269131f9bdbe5e ts=2026-10-07T18:30:51.5480000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[8272] _id=6abd5f07485cab4c95926f08 ts=2026-09-30T19:12:08.0690000Z`; `6aa4144c41b41dbac0c7f264.jsonl[11244] _id=6ac51c23de269131f9b4d8cb ts=2026-10-06T16:04:51.4050000Z`; `6aa4144c41b41dbac0c7f264.jsonl[11557] _id=6ac53883de269131f9b61df0 ts=2026-10-06T18:05:54.8130000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 7 records 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[27] _id=6ab41774485cab4c954f37a6 ts=?`; `6aa4144c41b41dbac0c7f264.jsonl[420] _id=6ab56161485cab4c95538519 ts=?`; `6aa4144c41b41dbac0c7f264.jsonl[988] _id=6ab6b964485cab4c955dbf3b ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 573 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[1470] _id=6ab6bae2485cab4c955df248 ts=2026-09-25T18:18:09.9370000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1480] _id=6ab6bae4485cab4c955df2b3 ts=2026-09-25T18:18:11.3730000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1557] _id=6ab6baf7485cab4c955df513 ts=2026-09-25T18:18:30.9070000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 799 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[1078] _id=6ab6b9ec485cab4c955dcf91 ts=2026-09-25T18:14:03.4130000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1080] _id=6ab6b9ec485cab4c955dcfa3 ts=2026-09-25T18:14:04.0190000Z`; `6aa4144c41b41dbac0c7f264.jsonl[1075] _id=6ab6b9ed485cab4c955dcfc3 ts=2026-09-25T18:14:04.0790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 14 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[3281] _id=6abab093485cab4c956fee1b ts=2026-09-28T18:23:15.1580000Z`; `6aa4144c41b41dbac0c7f264.jsonl[3289] _id=6abab093485cab4c956fee35 ts=2026-09-28T18:23:15.1760000Z`; `6aa4144c41b41dbac0c7f264.jsonl[4692] _id=6abc0035485cab4c95843175 ts=2026-09-29T18:15:16.4710000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 17 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[7796] _id=6abd552e485cab4c9591943b ts=2026-09-30T18:30:05.7800000Z`; `6aa4144c41b41dbac0c7f264.jsonl[7886] _id=6abd5535485cab4c959195b9 ts=2026-09-30T18:30:13.0950000Z`; `6aa4144c41b41dbac0c7f264.jsonl[7894] _id=6abd5538485cab4c95919654 ts=2026-09-30T18:30:16.2090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 chatEvent record in 'Unit 5 Dev' inside a 'MainMenu' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[14506] _id=6ac68fdbde269131f9bdbe5e ts=2026-10-07T18:30:51.5480000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 25 unmatched 'DialogueStartEvent' (totals: 446 start, 435 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 152 unmatched 'BecameCameraCentered' (totals: 849 open, 809 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 120 unmatched 'BecameVisible' (totals: 1252 open, 1284 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 20 open, 17 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationNodeHoverStart' (totals: 114 open, 112 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 2 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 62 start, 44 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 304 of 14748 adjacent _id pairs reverse in client time; worst 5708.7s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f264.jsonl[14463] _id=6ac67106de269131f9bc5ab1 ts=2026-10-07T16:19:18.2030000Z`; `6aa4144c41b41dbac0c7f264.jsonl[14468] _id=6ac68fa6de269131f9bdbcdc ts=2026-10-07T14:44:09.454Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -13548.90s, max +1.18s over 14749 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f264\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 7 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4194 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2936); Unit 4 Dev (822); Unit 5 Dev - Dungeon (244); Unit 3 Dungeon Dev (192)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.35s, n=4193)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4194/4194 records)
    "BecameInvisible"  x1284
    "BecameVisible"  x1252
    "BecameCameraCentered"  x849
    "BecameCameraUncentered"  x809
data.pieceId  (string, 4194/4194 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4194/4194 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4182 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1672); Unit 4 Dev - Dungeon (692); Unit 2 Prod (Refactor) (543); Unit 3 Dungeon Dev (315); Unit 4 Dev (283); Unit 5 Dev - Dungeon (275); Unit 1 Dev (220); Unit 4 Dev - Anderson Base (122); Unit 5 Dev (60)
- **Intervals:** median 0.80s (p5 0.05s / p95 22.11s, n=4181)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4182/4182 records)
    "pressed"  x4182
data.actionType  (string, 4182/4182 records)
    "Move"  x2872
    "Interact"  x663
    "Jump"  x341
    "Sprint"  x160
    "Hoverboard"  x58
    "Ascend"  x54
    "SkipCinematic"  x24
    "Map"  x5
    "Descend"  x3
    "Pause"  x2
data.key  (string, 4182/4182 records, 14 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4182/4182 records)
    "Player"  x2965
    "Drone"  x1217
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2816 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (679); Unit 3 Dev (500); Unit 4 Dev - Dungeon (408); Unit 1 Dev (319); Unit 4 Dev (307); Unit 3 Dungeon Dev (215); Unit 5 Dev (154); Unit 5 Dev - Dungeon (137); Unit 4 Dev - Anderson Base (97)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2802)
- **Fields under `data`:**

```text
data.position  (object, 2816/2816 records)
data.position.x  (number, 2816/2816 records)
    numeric range -701.161 .. 1551.59 (823 unique)
data.position.y  (number, 2816/2816 records)
    numeric range -22125.2 .. 222.252 (585 unique)
data.position.z  (number, 2816/2816 records)
    numeric range -1136.14 .. 1992.69 (825 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2270 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (486); Unit 3 Dev (451); Unit 4 Dev (360); Unit 1 Dev (250); Unit 5 Dev (249); Unit 4 Dev - Dungeon (179); Unit 3 Dungeon Dev (121); Unit 4 Dev - Anderson Base (102); Unit 5 Dev - Dungeon (72)
- **eventKey:** present on 1389 of 2270 records
- **Intervals:** median 4.89s (p5 0.00s / p95 42.86s, n=2269)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1389; [conversationId, dialogueEventType] x881
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2270/2270 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2270/2270 records)
    "DialogueNodeEvent"  x1389
    "DialogueStartEvent"  x446
    "DialogueFinishEvent"  x435
data.nodeId  (number, 1389/2270 records)
    numeric range 0 .. 290 (217 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 379 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (186); Unit 2 Prod (Refactor) (56); Unit 3 Dungeon Dev (40); Unit 4 Dev (35); Unit 4 Dev - Anderson Base (18); Unit 1 Dev (16); Unit 3 Dev (14); Unit 5 Dev - Dungeon (8); Unit 5 Dev (6)
- **Intervals:** median 11.41s (p5 0.30s / p95 473.50s, n=378)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 379/379 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 379/379 records)
    93 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 265 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 5 Dev (172); Unit 3 Dev (41); Unit 4 Dev - Anderson Base (37); Unit 1 Dev (15)
- **Intervals:** median 0.27s (p5 0.02s / p95 4.52s, n=264)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 265/265 records)
    "argumentationNodeHoverStart"  x114
    "argumentationNodeHoverEnd"  x112
    "argumentationNodeAdd"  x27
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 265/265 records)
    "Unit 5"  x172
    "Unit 3 - Pollution Upstream"  x41
    "Unit 4 - Flooding"  x37
    "Unit 1 - Freshwater"  x15
data.nodeName  (string, 265/265 records)
    "I"  x46
    "A"  x45
    "3"  x30
    "C"  x30
    "D"  x22
    "II"  x22
    "2"  x21
    "B"  x16
    "1"  x14
    "4"  x14
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 120 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (70); Unit 3 Dev (42); Unit 4 Dev (8)
- **Intervals:** median 0.65s (p5 0.15s / p95 10.77s, n=119)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x112; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/120 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/120 records)
    "Unit 3 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 112/120 records)
    "RightDrag"  x60
    "LeftDrag"  x52
data.currentSoilType  (string, 112/120 records)
    "CLAYSAND"  x22
    "CLAY"  x21
    "SAND"  x20
    "CLAYROCK"  x18
    "SANDGRAVEL"  x16
    "BEDROCK"  x8
    "GRAVEL"  x7
data.isCorrectSelection  (string, 112/120 records)
    "false"  x88
    "true"  x24
data.waterLevelStatus  (string, 112/120 records)
    "Proper"  x57
    "TooHigh"  x42
    "TooLow"  x13
data.waterRetentionChange  (string, 112/120 records)
    "Increase"  x53
    "Decrease"  x35
    "NoChange"  x24
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 106 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (21); Unit 3 Dev (19); Unit 1 Dev (17); Unit 2 Prod (Refactor) (17); Unit 4 Dev (11); Unit 5 Dev (9); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 106 of 106 records
- **Intervals:** median 225.53s (p5 0.00s / p95 76263.59s, n=105)
- **`data` key-set variants:** [questEventType, questID, questName] x62; [questEventType, questID, questName, questSuccessOrFailure] x44
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 106/106 records)
    "questActiveEvent"  x62
    "questFinishEvent"  x44
data.questID  (string, 106/106 records)
    33 unique values (see csv/event_unique_values.csv)
data.questName  (string, 106/106 records)
    33 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 44/106 records)
    "Succeeded"  x44
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 68 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (68)
- **Intervals:** median 4.30s (p5 0.13s / p95 79.13s, n=67)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 68/68 records)
    "On"  x39
    "Off"  x29
data.floor  (string, 68/68 records)
    "3"  x24
    "1"  x23
    "4"  x18
    "2"  x3
data.machineNumber  (string, 68/68 records)
    "One"  x66
    "Two"  x2
data.machineType  (string, 68/68 records)
    "Evaporator"  x27
    "Condenser"  x25
    "DualChamber_Evaporator"  x12
    "DualChamber_Condenser"  x2
    "VentSwitch"  x2
data.room  (string, 68/68 records)
    "2"  x45
    "3"  x13
    "1"  x5
    "4"  x5
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `soilMachine` — 60 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (60)
- **Intervals:** median 5.42s (p5 0.62s / p95 386.16s, n=59)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "ChangeCanister"  x60
data.canisterType  (string, 60/60 records)
    "Clay"  x25
    "Bedrock"  x23
    "Gravel"  x7
    "Sand"  x5
data.floor  (string, 60/60 records)
    "5"  x50
    "4"  x7
    "3"  x3
data.machine  (string, 60/60 records)
    "1"  x57
    "2"  x3
data.row  (string, 60/60 records)
    "BottomRow"  x31
    "TopRow"  x29
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 59 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (24); Unit 2 Prod (Refactor) (9); Unit 4 Dev (8); Unit 3 Dev (6); Unit 1 Dev (4); Unit 5 Dev - Dungeon (4); Transition (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 406.22s (p5 1.05s / p95 86054.93s, n=58)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 59/59 records)
    true  x59
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TopographicMapEvent` — 49 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (27); Unit 2 Prod (Refactor) (20); Unit 4 Dev (2)
- **Intervals:** median 9.41s (p5 0.15s / p95 78353.81s, n=48)
- **`data` key-set variants:** [actionType, featureUsed] x37; [actionType, featureUsed, location] x12
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "MapOpenEvent"  x20
    "MapCloseEvent"  x17
    "WaypointMoveEvent"  x6
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x2
data.featureUsed  (string, 49/49 records)
    "Map"  x37
    "Waypoint"  x12
data.location  (object, 12/49 records)
data.location.x  (number, 12/49 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 12/49 records)
    9 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 12/49 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowUnfocusEvent` — 45 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (12); Unit 4 Dev (9); Unit 3 Dev (8); Unit 1 Dev (5); Unit 5 Dev - Dungeon (4); Unit 4 Dev - Anderson Base (3); Transition (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 524.31s (p5 0.84s / p95 85991.28s, n=44)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 45/45 records)
    false  x45
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DEBUGMenu` — 31 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (6); Unit 4 Dev (6); MainMenu (4); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 3 Dungeon Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1836.66s (p5 65.22s / p95 181515.57s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "DebugMenuStateChanged"  x31
data.isOpened  (bool, 31/31 records)
    false  x31
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 24 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (24)
- **Intervals:** median 8303.52s (p5 137.21s / p95 241779.88s, n=23)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 24/24 records)
    true  x24
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 20 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 5 Dev (16); Unit 1 Dev (2); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 6.39s (p5 0.19s / p95 519508.87s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "submitAnswerEvent"  x20
data.answerSubmitted  (string, 20/20 records, 1 empty-string)
    "A,D,B,2,3,I"  x7
    "C,A,D,3,I"  x4
    "C,D,3,I"  x2
    ""  x1
    "2,3,"  x1
    "A,1,I"  x1
    "A,5,I"  x1
    "A,B,D,2,I"  x1
    "C,D,3,II"  x1
    "D,C,A,2,II"  x1
data.argumentationTitle  (string, 20/20 records)
    "Unit 5"  x16
    "Unit 1 - Freshwater"  x2
    "Unit 3 - Pollution Upstream"  x1
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TerasGardenBox` — 17 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (17)
- **Intervals:** median 2.39s (p5 0.87s / p95 18552.24s, n=16)
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records, 10 empty-string)
    ""  x10
    "cameraPlaced"  x7
data.boxId  (string, 17/17 records)
    "0"  x6
    "2"  x6
    "1"  x5
data.soilType  (string, 17/17 records)
    "Gravel"  x8
    "Sand"  x6
    "Clay"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (8); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 6.95s (p5 1.74s / p95 263774.19s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x7
    "Open"  x5
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 85.34s (p5 0.04s / p95 519608.48s, n=11)
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

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 0.99s (p5 0.52s / p95 4.94s, n=7)
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
    "RoofStyle"  x5
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 7/8 records)
    "Tilted In"  x2
    "Tilted Out"  x2
    "Cold"  x1
    "Flat"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `crash` — 7 records

- **Scenes:** <missing sceneName> (7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 7/7 records)
    true  x7
data.message  (string, 7/7 records)
    "A user gesture is required to request Pointer Lock."  x6
    "Permissions check failed"  x1
data.phase  (string, 7/7 records)
    "running"  x7
data.stack  (string, 7/7 records, 6 empty-string)
    ""  x6
    "TypeError: Permissions check failed"  x1
data.type  (string, 7/7 records)
    "unhandled_rejection"  x7
data.unitId  (string, 7/7 records)
    "unit1"  x2
    "unit3"  x2
    "unit2"  x1
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 7/7 records)
    "mhs"  x7
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (3); Unit 3 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1406.67s (p5 64.45s / p95 484747.89s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x5
    "Open"  x1
data.chatID  (string, 6/6 records)
    "NA"  x5
    "[11-26, 11-29, 11-26, 11-27, 11-25]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 525398.97s (p5 62598.97s / p95 582748.44s, n=3)
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

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 596946.49s (p5 596946.49s / p95 596946.49s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 2/2 records)
    "Unit 3 - Pollution Upstream"  x1
    "Unit 5"  x1
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Pollution Site Data"  x1
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
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (70 records)
- `TerasGardenBox` data.actionType: "" (10x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (6x); "WaypointResetEvent" (2x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (23x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*