# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56aea

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a88e9a8420a1e6b56aea
- **Game version string(s) in log:** 2.8.1, 2.8.9, 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56aea.jsonl
- **Records:** 11648 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56aea
- **Time span:** 2026-10-06T13:31:07.470000+00:00 .. 2026-10-16T13:28:03.343000+00:00 (239h 56m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56aea\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 11648 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 93 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3399 | 29.18 | 1 | 9 | 0 | 2026-10-06T13:36:40.298000+00:00 | 2026-10-16T13:28:03.343000+00:00 | 239h 51m |
| DialogueEvent | 2518 | 21.62 | 1 | 9 | 1581 | 2026-10-06T13:31:37.791000+00:00 | 2026-10-16T13:27:56.283000+00:00 | 239h 56m |
| PlayerPositionEvent | 2090 | 17.94 | 1 | 9 | 0 | 2026-10-06T13:31:17.939000+00:00 | 2026-10-16T13:27:56.749000+00:00 | 239h 56m |
| PuzzlePieceVisibleEvent | 1910 | 16.4 | 1 | 4 | 0 | 2026-10-07T13:35:04.555000+00:00 | 2026-10-15T21:24:45.201000+00:00 | 199h 49m |
| argumentationNodeEvent | 1015 | 8.71 | 1 | 5 | 0 | 2026-10-06T13:56:53.387000+00:00 | 2026-10-16T13:16:50.968000+00:00 | 239h 19m |
| ObjectInterEvent | 232 | 1.99 | 1 | 9 | 0 | 2026-10-06T13:37:56.135000+00:00 | 2026-10-16T13:28:03.298000+00:00 | 239h 50m |
| questEvent | 87 | 0.75 | 1 | 9 | 87 | 2026-10-06T13:31:37.762000+00:00 | 2026-10-16T13:24:37.354000+00:00 | 239h 52m |
| TopographicMapEvent | 74 | 0.64 | 1 | 2 | 0 | 2026-10-07T13:35:24.128000+00:00 | 2026-10-14T19:54:32.246000+00:00 | 174h 19m |
| argumentationAnswerEvent | 72 | 0.62 | 1 | 5 | 0 | 2026-10-06T13:57:01.919000+00:00 | 2026-10-16T13:16:52.429000+00:00 | 239h 19m |
| Soil Key Puzzle | 57 | 0.49 | 1 | 3 | 0 | 2026-10-07T13:43:49.566000+00:00 | 2026-10-15T13:20:58.124000+00:00 | 191h 37m |
| DEBUGMenu | 35 | 0.3 | 1 | 9 | 0 | 2026-10-06T13:31:17.920000+00:00 | 2026-10-16T13:10:58.073000+00:00 | 239h 39m |
| gameWindowFocusEvent | 28 | 0.24 | 1 | 6 | 0 | 2026-10-06T13:31:07.470000+00:00 | 2026-10-16T13:10:58.229000+00:00 | 239h 39m |
| argumentationEvent | 23 | 0.2 | 1 | 5 | 0 | 2026-10-06T13:56:50.365000+00:00 | 2026-10-16T13:16:52.463000+00:00 | 239h 20m |
| WaterChamberEvent | 22 | 0.19 | 1 | 1 | 0 | 2026-10-15T21:23:19.077000+00:00 | 2026-10-15T21:32:38.402000+00:00 | 9m 19s |
| argumentationToolEvent | 20 | 0.17 | 1 | 4 | 0 | 2026-10-06T13:56:47.541000+00:00 | 2026-10-16T13:16:08.878000+00:00 | 239h 19m |
| gameStartEvent | 16 | 0.14 | 1 | 1 | 0 | 2026-10-06T13:31:07.471000+00:00 | 2026-10-16T13:10:58.229000+00:00 | 239h 39m |
| gameWindowUnfocusEvent | 15 | 0.13 | 1 | 8 | 0 | 2026-10-06T14:00:02.662000+00:00 | 2026-10-15T21:41:33.082000+00:00 | 223h 41m |
| TerasGardenBox | 9 | 0.08 | 1 | 1 | 0 | 2026-10-15T21:09:44.443000+00:00 | 2026-10-15T21:11:19.290000+00:00 | 1m 34s |
| soilMachine | 9 | 0.08 | 1 | 1 | 0 | 2026-10-15T13:34:47.253000+00:00 | 2026-10-15T13:43:08.804000+00:00 | 8m 21s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-07T13:29:52.552000+00:00 | 2026-10-16T13:28:03.279000+00:00 | 215h 58m |
| SolarStillDesignEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-16T13:22:14.664000+00:00 | 2026-10-16T13:22:23.197000+00:00 | 8.5s |
| chatEvent | 3 | 0.03 | 1 | 2 | 0 | 2026-10-15T21:19:19.489000+00:00 | 2026-10-16T13:11:10.852000+00:00 | 15h 51m |
| crash | 3 | 0.03 | 1 | 1 | 0 |  |  | ? |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-13T13:34:54.050000+00:00 | 2026-10-13T13:35:01.649000+00:00 | 7.6s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 74446.27s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 18.487s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.072s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1.742s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.971s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 19.377s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.713s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 28555.681s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 13258.273s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1169.279s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 4029.208s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
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
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Flat; Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 14.4x vs baseline. 
  - Observed: 72 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,I; A,2,II; A,3,II; A,4,I; A,4,II; A,C,D,3,II; B,2,I; B,2,II; B,3,II; B,4,II; C,1,II; C,2,II; C,3,II; C,4,I; C,4,II; C,A,2,II; C,D,3,II; D,2,II; D,3,I; D,4,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 7.2x vs baseline. 
  - Observed: 1015 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[147] _id=6ac4fa35de269131f9b1100d ts=2026-10-06T13:40:04.7700000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[195] _id=6ac4fb12de269131f9b13a7f ts=2026-10-06T13:43:45.9690000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[255] _id=6ac4fc0cde269131f9b16fe2 ts=2026-10-06T13:47:56.1550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[1] _id=6ac4f81bde269131f9b0b70e ts=2026-10-06T13:31:07.4710000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[496] _id=6ac647c0de269131f9b8da2d ts=2026-10-07T13:23:11.8890000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[708] _id=6ac649a5de269131f9b94779 ts=2026-10-07T13:31:16.7450000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 28 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 28} 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[0] _id=6ac4f81bde269131f9b0b70a ts=2026-10-06T13:31:07.4700000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[495] _id=6ac647c0de269131f9b8da2c ts=2026-10-07T13:23:11.8880000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[706] _id=6ac649a5de269131f9b94778 ts=2026-10-07T13:31:16.7450000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[493] _id=6ac647c0de269131f9b8da29 ts=2026-10-06T14:00:02.662Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2200] _id=6ac79c55de269131f9c07de4 ts=2026-10-08T13:36:19.5230000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[3536] _id=6ace338ade269131f9ceb4bb ts=2026-10-13T13:35:05.6230000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 2 of 74 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[784] _id=6ac64a9cde269131f9b989c6 ts=2026-10-07T13:35:24.1280000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[789] _id=6ac64aadde269131f9b98d6e ts=2026-10-07T13:35:41.0090000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[797] _id=6ac64abade269131f9b9909a ts=2026-10-07T13:35:54.1440000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3398 | 0.0 | 0.86 | 254.115 | 17.487 | 429759.779 | 0.24 | 122 | 11 |
| DialogueEvent | 2517 | 0.0 | 3.834 | 343.178 | 27.191 | 429379.147 | 0.17 | 750 | 11 |
| PlayerPositionEvent | 2078 | 0.0 | 10.002 | 415.554 | 10.135 | 429375.777 | 0.14 | 1 | 10 |
| PuzzlePieceVisibleEvent | 1909 | 0.0 | 0.072 | 376.836 | 2.281 | 429790.427 | 0.16 | 807 | 6 |
| argumentationNodeEvent | 1014 | 0.0 | 0.509 | 849.702 | 12.4 | 519989.038 | 0.07 | 135 | 9 |
| ObjectInterEvent | 231 | 0.0 | 18.487 | 3737.693 | 742.513 | 431803.733 | 0.02 | 9 | 14 |
| questEvent | 86 | 0.0 | 201.824 | 10041.623 | 60123.359 | 429548.611 | 0.01 | 15 | 18 |
| TopographicMapEvent | 73 | 0.023 | 5.971 | 8596.55 | 9466.951 | 431053.672 | 0.01 | 2 | 6 |
| argumentationAnswerEvent | 71 | 0.185 | 19.377 | 12135.078 | 70077.083 | 520066.87 | 0.0 | 0 | 9 |
| Soil Key Puzzle | 56 | 0.299 | 1.742 | 12318.367 | 22445.794 | 516576.071 | 0.0 | 0 | 4 |
| DEBUGMenu | 34 | 7.798 | 466.155 | 25375.887 | 86226.056 | 431151.469 | 0.0 | 0 | 16 |
| gameWindowFocusEvent | 27 | 26.399 | 1169.279 | 31955.213 | 86154.705 | 430724.376 | 0.0 | 0 | 16 |
| argumentationEvent | 22 | 0.028 | 127.882 | 39163.732 | 87680.513 | 519989.385 | 0.0 | 2 | 10 |
| WaterChamberEvent | 21 | 3.19 | 22.521 | 26.635 | 85.966 | 87.083 | 2.25 | 0 | 0 |
| argumentationToolEvent | 19 | 0.006 | 2.713 | 45345.334 | 156326.61 | 520123.516 | 0.0 | 1 | 5 |
| gameStartEvent | 15 | 79.444 | 13258.273 | 57519.384 | 189730.422 | 431176.806 | 0.0 | 0 | 12 |
| gameWindowUnfocusEvent | 14 | 46.322 | 4029.208 | 57520.744 | 262569.095 | 431926.1 | 0.0 | 0 | 9 |
| TerasGardenBox | 8 | 1.337 | 5.582 | 11.856 | 36.32 | 45.87 | 5.06 | 0 | 0 |
| soilMachine | 8 | 1.053 | 36.312 | 62.694 | 185.828 | 203.818 | 0.96 | 0 | 0 |
| EndOfUnit | 4 | 24667.155 | 74446.27 | 194372.682 | 526953.317 | 603931.031 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 1.875 | 3.243 | 2.844 | 3.398 | 3.415 | 21.09 | 0 | 0 |
| chatEvent | 2 | 852.648 | 28555.681 | 28555.681 | 53488.412 | 56258.715 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| DaniEvent | 1 | 7.599 | 7.599 | 7.599 | 7.599 | 7.599 | 7.9 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 8 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[2037] _id=6ac79ab2de269131f9c03a7a ts=2026-10-08T13:29:20.4580000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[2038] _id=6ac79ab2de269131f9c03a7b ts=2026-10-08T13:29:20.4580000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2041] _id=6ac79ab2de269131f9c03a7e ts=2026-10-08T13:29:20.4610000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[2042] _id=6ac79ab2de269131f9c03a7f ts=2026-10-08T13:29:20.4610000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[3114] _id=6ace2eeade269131f9ce8d3d ts=2026-10-13T13:15:19.9720000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[3115] _id=6ace2eeade269131f9ce8d3e ts=2026-10-13T13:15:19.9720000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 26 group(s), 42 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[2438] _id=6ac79e85de269131f9c0ddb9 ts=2026-10-08T13:45:38.5950000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[2449] _id=6ac79e85de269131f9c0ddc5 ts=2026-10-08T13:45:38.5950000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2451] _id=6ac79e87de269131f9c0de1a ts=2026-10-08T13:45:41.0210000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[2455] _id=6ac79e87de269131f9c0de2c ts=2026-10-08T13:45:41.0210000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2457] _id=6ac79e87de269131f9c0de2e ts=2026-10-08T13:45:41.1100000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[2458] _id=6ac79e87de269131f9c0de2f ts=2026-10-08T13:45:41.1100000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[11115] _id=6ad14a04de269131f9e1a25c ts=2026-10-15T21:47:47.2500000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[11116] _id=6ad14a04de269131f9e1a25d ts=2026-10-15T21:47:47.2500000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[11421] _id=6ad2240ade269131f9e37010 ts=2026-10-16T13:18:02.0960000Z == 6ab9a88e9a8420a1e6b56aea.jsonl[11422] _id=6ad2240ade269131f9e37011 ts=2026-10-16T13:18:02.0960000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `9ms: 6ab9a88e9a8420a1e6b56aea.jsonl[104] _id=6ac4f9b4de269131f9b0f989 ts=2026-10-06T13:37:56.1350000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[105] _id=6ac4f9b4de269131f9b0f995 ts=2026-10-06T13:37:56.1440000Z`; `223ms: 6ab9a88e9a8420a1e6b56aea.jsonl[990] _id=6ac64b19de269131f9b9a270 ts=2026-10-07T13:37:28.9580000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[991] _id=6ac64b19de269131f9b9a280 ts=2026-10-07T13:37:29.1810000Z`; `185ms: 6ab9a88e9a8420a1e6b56aea.jsonl[991] _id=6ac64b19de269131f9b9a280 ts=2026-10-07T13:37:29.1810000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[995] _id=6ac64b19de269131f9b9a290 ts=2026-10-07T13:37:29.3660000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `909ms: 6ab9a88e9a8420a1e6b56aea.jsonl[5133] _id=6acf84e0de269131f9d32ee4 ts=2026-10-14T13:34:24.1910000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[5136] _id=6acf84e1de269131f9d32eef ts=2026-10-14T13:34:25.1000000Z`; `335ms: 6ab9a88e9a8420a1e6b56aea.jsonl[5136] _id=6acf84e1de269131f9d32eef ts=2026-10-14T13:34:25.1000000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[5138] _id=6acf84e1de269131f9d32ef7 ts=2026-10-14T13:34:25.4350000Z`; `185ms: 6ab9a88e9a8420a1e6b56aea.jsonl[5138] _id=6acf84e1de269131f9d32ef7 ts=2026-10-14T13:34:25.4350000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[5139] _id=6acf84e1de269131f9d32f03 ts=2026-10-14T13:34:25.6200000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `30ms: 6ab9a88e9a8420a1e6b56aea.jsonl[5176] _id=6acf850ade269131f9d331d9 ts=2026-10-14T13:35:05.9680000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[5179] _id=6acf850ade269131f9d331dc ts=2026-10-14T13:35:05.9980000Z`; `28ms: 6ab9a88e9a8420a1e6b56aea.jsonl[9691] _id=6ad13e53de269131f9e1474b ts=2026-10-15T20:57:54.8520000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[9694] _id=6ad13e53de269131f9e1474e ts=2026-10-15T20:57:54.8800000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 50 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `453ms: 6ab9a88e9a8420a1e6b56aea.jsonl[406] _id=6ac4fe25de269131f9b20830 ts=2026-10-06T13:56:53.3870000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[400] _id=6ac4fe26de269131f9b2084e ts=2026-10-06T13:56:53.8400000Z`; `832ms: 6ab9a88e9a8420a1e6b56aea.jsonl[399] _id=6ac4fe25de269131f9b20832 ts=2026-10-06T13:56:53.4640000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[410] _id=6ac4fe26de269131f9b2087a ts=2026-10-06T13:56:54.2960000Z`; `23ms: 6ab9a88e9a8420a1e6b56aea.jsonl[336] _id=6ac4fe2bde269131f9b209b5 ts=2026-10-06T13:56:59.0220000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[389] _id=6ac4fe2bde269131f9b209c5 ts=2026-10-06T13:56:59.0450000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `982ms: 6ab9a88e9a8420a1e6b56aea.jsonl[431] _id=6ac4fe68de269131f9b21d58 ts=2026-10-06T13:58:00.2210000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[432] _id=6ac4fe69de269131f9b21d99 ts=2026-10-06T13:58:01.2030000Z`; `897ms: 6ab9a88e9a8420a1e6b56aea.jsonl[433] _id=6ac4fe6bde269131f9b21e01 ts=2026-10-06T13:58:02.7650000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[436] _id=6ac4fe6bde269131f9b21e17 ts=2026-10-06T13:58:03.6620000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6ab9a88e9a8420a1e6b56aea.jsonl[11554] _id=6ad2255ede269131f9e38be8 ts=2026-10-16T13:23:42.5160000Z ~ 6ab9a88e9a8420a1e6b56aea.jsonl[11555] _id=6ad2255ede269131f9e38bec ts=2026-10-16T13:23:42.5200000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 45m 
  - Evidence: 119h 45m: 6ab9a88e9a8420a1e6b56aea.jsonl[2033] _id=6ac79aacde269131f9c039bd ts=2026-10-08T13:29:15.3170000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3105] _id=6ace2edbde269131f9ce8d23 ts=2026-10-13T13:15:06.7860000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aea.jsonl[711] _id=6ac649b8de269131f9b94b8a ts=2026-10-07T13:31:36.2240000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2030] _id=6ac79a92de269131f9c036fd ts=2026-10-08T13:28:49.7910000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aea.jsonl[3111] _id=6ace2ee6de269131f9ce8d30 ts=2026-10-13T13:15:17.3960000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4389] _id=6acf7fb3de269131f9d2d023 ts=2026-10-14T13:12:19.4070000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a88e9a8420a1e6b56aea.jsonl[3098] _id=6ac7a1a5de269131f9c15927 ts=2026-10-08T13:59:00.8460000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3116] _id=6ace2eeade269131f9ce8d3f ts=2026-10-13T13:15:19.9930000Z; 23h 31m: 6ab9a88e9a8420a1e6b56aea.jsonl[2021] _id=6ac65012de269131f9ba3889 ts=2026-10-07T13:58:42.0410000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2054] _id=6ac79affde269131f9c043d8 ts=2026-10-08T13:30:39.0550000Z; 23h 24m: 6ab9a88e9a8420a1e6b56aea.jsonl[488] _id=6ac4fedade269131f9b238b2 ts=2026-10-06T13:59:54.5450000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[515] _id=6ac647eede269131f9b8dff5 ts=2026-10-07T13:23:58.0740000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 750 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[11063] _id=6ad149b1de269131f9e19f5b ts=2026-10-15T21:46:24.5690000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11064] _id=6ad149b1de269131f9e19f5c ts=2026-10-15T21:46:24.5690000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[8149] _id=6ad0dc45de269131f9db677b ts=2026-10-15T13:59:32.1180000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8150] _id=6ad0dc45de269131f9db677c ts=2026-10-15T13:59:32.1180000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[8391] _id=6ad0fa8ade269131f9dd43f0 ts=2026-10-15T16:08:41.8250000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8392] _id=6ad0fa8ade269131f9dd43f1 ts=2026-10-15T16:08:41.8250000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 167h 45m 
  - Evidence: 167h 45m: 6ab9a88e9a8420a1e6b56aea.jsonl[705] _id=6ac64950de269131f9b93156 ts=2026-10-07T13:29:52.5520000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4457] _id=6acf806bde269131f9d2d902 ts=2026-10-14T13:15:23.5830000Z; 25h 12m: 6ab9a88e9a8420a1e6b56aea.jsonl[6173] _id=6acfe0c7de269131f9d957cc ts=2026-10-14T20:06:30.7380000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[10059] _id=6ad14342de269131f9e175c8 ts=2026-10-15T21:18:57.0070000Z; 16h 9m: 6ab9a88e9a8420a1e6b56aea.jsonl[10059] _id=6ad14342de269131f9e175c8 ts=2026-10-15T21:18:57.0070000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11644] _id=6ad22663de269131f9e39e51 ts=2026-10-16T13:28:03.2790000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a88e9a8420a1e6b56aea.jsonl[2991] _id=6ac7a028de269131f9c12aaa ts=2026-10-08T13:52:40.1900000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3113] _id=6ace2eeade269131f9ce8d3c ts=2026-10-13T13:15:19.9690000Z; 23h 29m: 6ab9a88e9a8420a1e6b56aea.jsonl[2026] _id=6ac65051de269131f9ba3c46 ts=2026-10-07T13:59:45.3660000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2035] _id=6ac79ab2de269131f9c03a78 ts=2026-10-08T13:29:20.4560000Z; 23h 23m: 6ab9a88e9a8420a1e6b56aea.jsonl[492] _id=6ac647c0de269131f9b8da28 ts=2026-10-06T14:00:01.338Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[500] _id=6ac647cdde269131f9b8db1c ts=2026-10-07T13:23:25.3300000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 122 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[10535] _id=6ad1454fde269131f9e18123 ts=2026-10-15T21:27:42.3110000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[10536] _id=6ad1454fde269131f9e18124 ts=2026-10-15T21:27:42.3110000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[2037] _id=6ac79ab2de269131f9c03a7a ts=2026-10-08T13:29:20.4580000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2038] _id=6ac79ab2de269131f9c03a7b ts=2026-10-08T13:29:20.4580000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[2041] _id=6ac79ab2de269131f9c03a7e ts=2026-10-08T13:29:20.4610000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2042] _id=6ac79ab2de269131f9c03a7f ts=2026-10-08T13:29:20.4610000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a88e9a8420a1e6b56aea.jsonl[2811] _id=6ac79f24de269131f9c0fb7c ts=2026-10-08T13:48:20.1380000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4005] _id=6ace35e0de269131f9ced4ec ts=2026-10-13T13:45:03.8710000Z; 23h 59m: 6ab9a88e9a8420a1e6b56aea.jsonl[1742] _id=6ac64c96de269131f9b9e1df ts=2026-10-07T13:43:49.5710000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2355] _id=6ac79de2de269131f9c0c499 ts=2026-10-08T13:42:57.6320000Z; 23h 29m: 6ab9a88e9a8420a1e6b56aea.jsonl[4197] _id=6ace372cde269131f9cee488 ts=2026-10-13T13:50:35.9320000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4545] _id=6acf8179de269131f9d2e835 ts=2026-10-14T13:19:53.7860000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[8009] _id=6ad0dafade269131f9db403f ts=2026-10-15T13:54:01.8430000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8010] _id=6ad0dafade269131f9db4040 ts=2026-10-15T13:54:01.8430000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[8054] _id=6ad0db4ade269131f9db4a49 ts=2026-10-15T13:55:22.0080000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8055] _id=6ad0db4ade269131f9db4a4a ts=2026-10-15T13:55:22.0080000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[8246] _id=6ad0f961de269131f9dd221a ts=2026-10-15T16:03:44.6510000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8247] _id=6ad0f961de269131f9dd221b ts=2026-10-15T16:03:44.6510000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 16m 
  - Evidence: 119h 16m: 6ab9a88e9a8420a1e6b56aea.jsonl[3101] _id=6ac7a1a6de269131f9c1593a ts=2026-10-08T13:59:01.6300000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3112] _id=6ace2eeade269131f9ce8d3b ts=2026-10-13T13:15:17.4070000Z; 23h 29m: 6ab9a88e9a8420a1e6b56aea.jsonl[2029] _id=6ac65064de269131f9ba3d06 ts=2026-10-07T14:00:04.2140000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2034] _id=6ac79ab2de269131f9c03a77 ts=2026-10-08T13:29:15.3350000Z; 23h 23m: 6ab9a88e9a8420a1e6b56aea.jsonl[485] _id=6ac4fedade269131f9b238b4 ts=2026-10-06T13:59:54.7150000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[498] _id=6ac647cbde269131f9b8daf7 ts=2026-10-07T13:23:20.4040000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[11104] _id=6ad14a08de269131f9e1a273 ts=2026-10-15T21:47:51.0360000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11120] _id=6ad22212de269131f9e34ed9 ts=2026-10-15T21:47:51.036Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a88e9a8420a1e6b56aea.jsonl[2976] _id=6ac7a00dde269131f9c12549 ts=2026-10-08T13:52:10.6530000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3119] _id=6ace2eeade269131f9ce8d43 ts=2026-10-13T13:15:21.0800000Z; 24h 24m: 6ab9a88e9a8420a1e6b56aea.jsonl[3167] _id=6ace2effde269131f9ce8dc5 ts=2026-10-13T13:15:42.0000000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5323] _id=6acf8636de269131f9d341c4 ts=2026-10-14T13:40:04.8860000Z; 24h 2m: 6ab9a88e9a8420a1e6b56aea.jsonl[1712] _id=6ac64c43de269131f9b9d8fd ts=2026-10-07T13:42:24.8760000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2423] _id=6ac79e53de269131f9c0d4c0 ts=2026-10-08T13:44:50.3490000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 807 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[1001] _id=6ac64b1dde269131f9b9a33e ts=2026-10-07T13:37:30.9430000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[1007] _id=6ac64b1dde269131f9b9a340 ts=2026-10-07T13:37:30.9430000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[1005] _id=6ac64b1cde269131f9b9a32e ts=2026-10-07T13:37:30.9060000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[1006] _id=6ac64b1cde269131f9b9a336 ts=2026-10-07T13:37:30.9060000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[10066] _id=6ad14360de269131f9e17675 ts=2026-10-15T21:19:25.9880000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[10067] _id=6ad14360de269131f9e17677 ts=2026-10-15T21:19:25.9880000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 143h 29m 
  - Evidence: 143h 29m: 6ab9a88e9a8420a1e6b56aea.jsonl[2392] _id=6ac79e0ede269131f9c0ca84 ts=2026-10-08T13:43:42.0290000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4409] _id=6acf7feede269131f9d2d423 ts=2026-10-14T13:13:18.1000000Z; 23h 59m: 6ab9a88e9a8420a1e6b56aea.jsonl[1744] _id=6ac64c98de269131f9b9e219 ts=2026-10-07T13:43:52.5990000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2349] _id=6ac79de2de269131f9c0c493 ts=2026-10-08T13:42:57.6270000Z; 23h 40m: 6ab9a88e9a8420a1e6b56aea.jsonl[5318] _id=6acf862ade269131f9d34146 ts=2026-10-14T13:39:54.6550000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[6280] _id=6ad0d315de269131f9da6443 ts=2026-10-15T13:20:20.4370000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a88e9a8420a1e6b56aea.jsonl[2299] _id=6ac79d66de269131f9c0afdf ts=2026-10-08T13:40:53.5920000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3335] _id=6ace3133de269131f9ce9f79 ts=2026-10-13T13:25:07.2640000Z; 23h 34m: 6ab9a88e9a8420a1e6b56aea.jsonl[3937] _id=6ace3592de269131f9ced1b7 ts=2026-10-13T13:43:45.4410000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4500] _id=6acf8115de269131f9d2e17f ts=2026-10-14T13:18:13.0930000Z; 23h 32m: 6ab9a88e9a8420a1e6b56aea.jsonl[2024] _id=6ac65047de269131f9ba3ba9 ts=2026-10-07T13:59:35.2130000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2080] _id=6ac79b53de269131f9c04d30 ts=2026-10-08T13:32:02.9860000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.028s shown 
  - Evidence: 23ms: 6ab9a88e9a8420a1e6b56aea.jsonl[1904] _id=6ac64e9fde269131f9ba1124 ts=2026-10-07T13:52:30.9630000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[1908] _id=6ac64e9fde269131f9ba1128 ts=2026-10-07T13:52:30.9860000Z; 28ms: 6ab9a88e9a8420a1e6b56aea.jsonl[1903] _id=6ac64e9fde269131f9ba111f ts=2026-10-07T13:52:30.9350000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[1904] _id=6ac64e9fde269131f9ba1124 ts=2026-10-07T13:52:30.9630000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 144h 27m 
  - Evidence: 144h 27m: 6ab9a88e9a8420a1e6b56aea.jsonl[610] _id=6ac64899de269131f9b90378 ts=2026-10-07T13:26:48.8590000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4309] _id=6ace381cde269131f9cef11c ts=2026-10-13T13:54:35.7290000Z; 24h 24m: 6ab9a88e9a8420a1e6b56aea.jsonl[5175] _id=6acf850ade269131f9d331d6 ts=2026-10-14T13:35:05.9520000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8136] _id=6ad0dc31de269131f9db6584 ts=2026-10-15T13:59:12.3810000Z; 23h 39m: 6ab9a88e9a8420a1e6b56aea.jsonl[4309] _id=6ace381cde269131f9cef11c ts=2026-10-13T13:54:35.7290000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5108] _id=6acf84c9de269131f9d32d27 ts=2026-10-14T13:34:01.5590000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 144h 26m 
  - Evidence: 144h 26m: 6ab9a88e9a8420a1e6b56aea.jsonl[606] _id=6ac64899de269131f9b90380 ts=2026-10-07T13:26:48.8850000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4250] _id=6ace37cede269131f9ceed8d ts=2026-10-13T13:53:18.2700000Z; 24h 23m: 6ab9a88e9a8420a1e6b56aea.jsonl[5179] _id=6acf850ade269131f9d331dc ts=2026-10-14T13:35:05.9980000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8105] _id=6ad0dc12de269131f9db60c4 ts=2026-10-15T13:58:41.9650000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aea.jsonl[4311] _id=6ace381cde269131f9cef11e ts=2026-10-13T13:54:35.7510000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5070] _id=6acf848ede269131f9d328e8 ts=2026-10-14T13:33:02.6450000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.028s..0.030s shown 
  - Evidence: 28ms: 6ab9a88e9a8420a1e6b56aea.jsonl[9691] _id=6ad13e53de269131f9e1474b ts=2026-10-15T20:57:54.8520000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[9694] _id=6ad13e53de269131f9e1474e ts=2026-10-15T20:57:54.8800000Z; 30ms: 6ab9a88e9a8420a1e6b56aea.jsonl[5176] _id=6acf850ade269131f9d331d9 ts=2026-10-14T13:35:05.9680000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5179] _id=6acf850ade269131f9d331dc ts=2026-10-14T13:35:05.9980000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 144h 26m 
  - Evidence: 144h 26m: 6ab9a88e9a8420a1e6b56aea.jsonl[603] _id=6ac64897de269131f9b90335 ts=2026-10-07T13:26:47.0210000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4252] _id=6ace37ccde269131f9ceed77 ts=2026-10-13T13:53:16.0590000Z; 24h 23m: 6ab9a88e9a8420a1e6b56aea.jsonl[5174] _id=6acf8508de269131f9d331b0 ts=2026-10-14T13:35:04.4390000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8100] _id=6ad0dc15de269131f9db6121 ts=2026-10-15T13:58:44.5240000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aea.jsonl[4302] _id=6ace3816de269131f9cef0dc ts=2026-10-13T13:54:29.7710000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5073] _id=6acf848cde269131f9d328bc ts=2026-10-14T13:33:00.1730000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 135 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[9668] _id=6ad13e2dde269131f9e1464a ts=2026-10-15T20:57:16.8370000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[9669] _id=6ad13e2dde269131f9e1464b ts=2026-10-15T20:57:16.8370000Z; 4ms: 6ab9a88e9a8420a1e6b56aea.jsonl[11264] _id=6ad2234dde269131f9e3613a ts=2026-10-16T13:14:53.4220000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11265] _id=6ad2234dde269131f9e3613e ts=2026-10-16T13:14:53.4260000Z; 4ms: 6ab9a88e9a8420a1e6b56aea.jsonl[8165] _id=6ad0dc5cde269131f9db69b6 ts=2026-10-15T13:59:55.1710000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[8170] _id=6ad0dc5cde269131f9db69ba ts=2026-10-15T13:59:55.1750000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 144h 28m 
  - Evidence: 144h 28m: 6ab9a88e9a8420a1e6b56aea.jsonl[553] _id=6ac64850de269131f9b8f334 ts=2026-10-07T13:25:36.2940000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4300] _id=6ace380cde269131f9cef038 ts=2026-10-13T13:54:19.8100000Z; 32h 11m: 6ab9a88e9a8420a1e6b56aea.jsonl[5106] _id=6acf84bcde269131f9d32c1a ts=2026-10-14T13:33:47.9610000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11012] _id=6ad1497dde269131f9e19c8d ts=2026-10-15T21:45:32.6920000Z; 23h 38m: 6ab9a88e9a8420a1e6b56aea.jsonl[4300] _id=6ace380cde269131f9cef038 ts=2026-10-13T13:54:19.8100000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5086] _id=6acf849ade269131f9d329e6 ts=2026-10-14T13:33:14.6450000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.006s..0.006s shown 
  - Evidence: 6ms: 6ab9a88e9a8420a1e6b56aea.jsonl[433] _id=6ac4fe6bde269131f9b21e01 ts=2026-10-06T13:58:02.7650000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[435] _id=6ac4fe6bde269131f9b21e06 ts=2026-10-06T13:58:02.7710000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 15h 37m 
  - Evidence: 15h 37m: 6ab9a88e9a8420a1e6b56aea.jsonl[10799] _id=6ad146adde269131f9e189a1 ts=2026-10-15T21:33:32.1370000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11133] _id=6ad2226fde269131f9e3514c ts=2026-10-16T13:11:10.8520000Z; 14m 12s: 6ab9a88e9a8420a1e6b56aea.jsonl[10065] _id=6ad14358de269131f9e1764b ts=2026-10-15T21:19:19.4890000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[10799] _id=6ad146adde269131f9e189a1 ts=2026-10-15T21:33:32.1370000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a88e9a8420a1e6b56aea.jsonl[2032] _id=6ac79a92de269131f9c03704 ts=2026-10-08T13:28:50.1450000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3104] _id=6ace2edbde269131f9ce8d26 ts=2026-10-13T13:15:06.9510000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aea.jsonl[708] _id=6ac649a5de269131f9b94779 ts=2026-10-07T13:31:16.7450000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2032] _id=6ac79a92de269131f9c03704 ts=2026-10-08T13:28:50.1450000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aea.jsonl[3104] _id=6ace2edbde269131f9ce8d26 ts=2026-10-13T13:15:06.9510000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[4390] _id=6acf7fb4de269131f9d2d026 ts=2026-10-14T13:12:19.7370000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 38m 
  - Evidence: 119h 38m: 6ab9a88e9a8420a1e6b56aea.jsonl[2198] _id=6ac79c57de269131f9c07e55 ts=2026-10-08T13:36:22.5740000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3103] _id=6ace2edbde269131f9ce8d25 ts=2026-10-13T13:15:06.9500000Z; 23h 57m: 6ab9a88e9a8420a1e6b56aea.jsonl[706] _id=6ac649a5de269131f9b94778 ts=2026-10-07T13:31:16.7450000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2031] _id=6ac79a92de269131f9c03703 ts=2026-10-08T13:28:50.1450000Z; 23h 52m: 6ab9a88e9a8420a1e6b56aea.jsonl[0] _id=6ac4f81bde269131f9b0b70a ts=2026-10-06T13:31:07.4700000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[495] _id=6ac647c0de269131f9b8da2c ts=2026-10-07T13:23:11.8880000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a88e9a8420a1e6b56aea.jsonl[2200] _id=6ac79c55de269131f9c07de4 ts=2026-10-08T13:36:19.5230000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3536] _id=6ace338ade269131f9ceb4bb ts=2026-10-13T13:35:05.6230000Z; 47h 36m: 6ab9a88e9a8420a1e6b56aea.jsonl[493] _id=6ac647c0de269131f9b8da29 ts=2026-10-06T14:00:02.662Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2200] _id=6ac79c55de269131f9c07de4 ts=2026-10-08T13:36:19.5230000Z; 24h 24m: 6ab9a88e9a8420a1e6b56aea.jsonl[3536] _id=6ace338ade269131f9ceb4bb ts=2026-10-13T13:35:05.6230000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[5964] _id=6acfdd63de269131f9d9251b ts=2026-10-14T14:00:04.261Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a88e9a8420a1e6b56aea.jsonl[3055] _id=6ac7a0fcde269131f9c149d0 ts=2026-10-08T13:56:11.4530000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[3118] _id=6ace2eeade269131f9ce8d41 ts=2026-10-13T13:15:20.0640000Z; 23h 37m: 6ab9a88e9a8420a1e6b56aea.jsonl[1896] _id=6ac64e8cde269131f9ba0e15 ts=2026-10-07T13:52:12.0490000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[2043] _id=6ac79ab2de269131f9c03a80 ts=2026-10-08T13:29:20.5020000Z; 23h 24m: 6ab9a88e9a8420a1e6b56aea.jsonl[474] _id=6ac4feafde269131f9b22fd6 ts=2026-10-06T13:59:11.6450000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[499] _id=6ac647cbde269131f9b8daf8 ts=2026-10-07T13:23:22.3360000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[11115] _id=6ad14a04de269131f9e1a25c ts=2026-10-15T21:47:47.2500000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11116] _id=6ad14a04de269131f9e1a25d ts=2026-10-15T21:47:47.2500000Z; 0ms: 6ab9a88e9a8420a1e6b56aea.jsonl[11421] _id=6ad2240ade269131f9e37010 ts=2026-10-16T13:18:02.0960000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[11422] _id=6ad2240ade269131f9e37011 ts=2026-10-16T13:18:02.0960000Z; 2ms: 6ab9a88e9a8420a1e6b56aea.jsonl[334] _id=6ac4fdbcde269131f9b1e8fd ts=2026-10-06T13:55:07.6990000Z -> 6ab9a88e9a8420a1e6b56aea.jsonl[340] _id=6ac4fdbdde269131f9b1e933 ts=2026-10-06T13:55:07.7010000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 15 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[363] _id=6ac4fdabde269131f9b1e365 ts=2026-10-06T13:54:51.2480000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[463] _id=6ac4fea0de269131f9b22c08 ts=2026-10-06T13:58:55.2810000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[561] _id=6ac648acde269131f9b90807 ts=2026-10-07T13:27:08.2060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[5179] _id=6acf850ade269131f9d331dc ts=2026-10-14T13:35:05.9980000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[389] _id=6ac4fe2bde269131f9b209c5 ts=2026-10-06T13:56:59.0450000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[10065] _id=6ad14358de269131f9e1764b ts=2026-10-15T21:19:19.4890000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[10799] _id=6ad146adde269131f9e189a1 ts=2026-10-15T21:33:32.1370000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[11133] _id=6ad2226fde269131f9e3514c ts=2026-10-16T13:11:10.8520000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[6857] _id=6ad0d4fbde269131f9da9480 ts=2026-10-15T13:28:26.8920000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[5] _id=6ac4f838de269131f9b0bbb1 ts=?`; `6ab9a88e9a8420a1e6b56aea.jsonl[4398] _id=6acf7fc6de269131f9d2d100 ts=?`; `6ab9a88e9a8420a1e6b56aea.jsonl[4473] _id=6acf8096de269131f9d2daa0 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 27 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[2569] _id=6ac79ef7de269131f9c0f240 ts=2026-10-08T13:47:33.4590000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2585] _id=6ac79efbde269131f9c0f307 ts=2026-10-08T13:47:37.2400000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2586] _id=6ac79efbde269131f9c0f30c ts=2026-10-08T13:47:37.2400000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 50 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[2438] _id=6ac79e85de269131f9c0ddb9 ts=2026-10-08T13:45:38.5950000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2449] _id=6ac79e85de269131f9c0ddc5 ts=2026-10-08T13:45:38.5950000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[2450] _id=6ac79e85de269131f9c0ddc6 ts=2026-10-08T13:45:38.5950000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[8344] _id=6ad0fa58de269131f9dd3e78 ts=2026-10-15T16:07:51.6280000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[8675] _id=6ad10666de269131f9de290b ts=2026-10-15T16:59:18.3080000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[9119] _id=6ad13a9dde269131f9e1304b ts=2026-10-15T20:42:04.3470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[432] _id=6ac4fe69de269131f9b21d99 ts=2026-10-06T13:58:01.2030000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[435] _id=6ac4fe6bde269131f9b21e06 ts=2026-10-06T13:58:02.7710000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[437] _id=6ac4fe6cde269131f9b21e23 ts=2026-10-06T13:58:03.8080000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 473 start, 464 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 568 open, 556 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationSessionOpen' (totals: 12 open, 11 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 15 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 51 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 197 of 11644 adjacent _id pairs reverse in client time; worst 102.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56aea.jsonl[824] _id=6ac64af1de269131f9b99b30 ts=2026-10-07T13:36:49.3590000Z`; `6ab9a88e9a8420a1e6b56aea.jsonl[856] _id=6ac64af1de269131f9b99b38 ts=2026-10-07T13:35:06.5190000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.81s, min -84192.60s, max -0.12s over 11645 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a88e9a8420a1e6b56aea\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 3399 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1094); Unit 4 Dev - Dungeon (684); Unit 3 Dev (453); Unit 5 Dev - Dungeon (266); Unit 4 Dev (247); Unit 4 Dev - Anderson Base (226); Unit 5 Dev (183); Unit 3 Dungeon Dev (139); Unit 1 Dev (107)
- **Intervals:** median 0.86s (p5 0.08s / p95 17.49s, n=3398)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3399/3399 records)
    "pressed"  x3399
data.actionType  (string, 3399/3399 records)
    "Move"  x2352
    "Interact"  x420
    "Sprint"  x376
    "Ascend"  x100
    "Descend"  x50
    "Hoverboard"  x43
    "Jump"  x43
    "Map"  x12
    "ToggleDebug"  x3
data.key  (string, 3399/3399 records, 12 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3399/3399 records)
    "Player"  x2336
    "Drone"  x1063
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2518 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (645); Unit 4 Dev - Anderson Base (421); Unit 3 Dev (365); Unit 5 Dev (306); Unit 1 Dev (257); Unit 4 Dev (251); Unit 3 Dungeon Dev (116); Unit 4 Dev - Dungeon (85); Unit 5 Dev - Dungeon (72)
- **eventKey:** present on 1581 of 2518 records
- **Intervals:** median 3.83s (p5 0.00s / p95 27.19s, n=2517)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1581; [conversationId, dialogueEventType] x937
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2518/2518 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2518/2518 records)
    "DialogueNodeEvent"  x1581
    "DialogueStartEvent"  x473
    "DialogueFinishEvent"  x464
data.nodeId  (number, 1581/2518 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2090 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (619); Unit 4 Dev - Anderson Base (331); Unit 3 Dev (262); Unit 4 Dev (215); Unit 1 Dev (211); Unit 5 Dev (168); Unit 4 Dev - Dungeon (120); Unit 5 Dev - Dungeon (85); Unit 3 Dungeon Dev (79)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.14s, n=2078)
- **Fields under `data`:**

```text
data.position  (object, 2090/2090 records)
data.position.x  (number, 2090/2090 records)
    numeric range -740.735 .. 1556.8 (548 unique)
data.position.y  (number, 2090/2090 records)
    numeric range -113.43 .. 222.252 (421 unique)
data.position.z  (number, 2090/2090 records)
    numeric range -1117.15 .. 1988.29 (548 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 1910 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1200); Unit 4 Dev (322); Unit 5 Dev - Dungeon (272); Unit 3 Dungeon Dev (116)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.28s, n=1909)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1910/1910 records)
    "BecameVisible"  x568
    "BecameInvisible"  x556
    "BecameCameraCentered"  x393
    "BecameCameraUncentered"  x393
data.pieceId  (string, 1910/1910 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1910/1910 records)
    1345 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `argumentationNodeEvent` — 1015 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (699); Unit 5 Dev (138); Unit 1 Dev (70); Unit 3 Dev (59); Unit 2 Prod (Refactor) (49)
- **Intervals:** median 0.51s (p5 0.04s / p95 12.40s, n=1014)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1015/1015 records)
    "argumentationNodeHoverEnd"  x418
    "argumentationNodeHoverStart"  x417
    "argumentationNodeAdd"  x108
    "argumentationNodeRemove"  x72
data.argumentationTitle  (string, 1015/1015 records)
    "Unit 4 - Flooding"  x699
    "Unit 5"  x138
    "Unit 3 - Pollution Upstream"  x59
    "Unit 2 – Watershed"  x49
    "Unit 1 - Argumentation Tutorial"  x40
    "Unit 1 - Freshwater"  x30
data.nodeName  (string, 1015/1015 records)
    "A"  x143
    "2"  x116
    "1"  x113
    "II"  x107
    "I"  x105
    "B"  x102
    "C"  x101
    "3"  x76
    "D"  x75
    "4"  x72
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 232 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (62); Unit 2 Prod (Refactor) (41); Unit 4 Dev - Anderson Base (36); Unit 3 Dungeon Dev (27); Unit 4 Dev (19); Unit 3 Dev (16); Unit 1 Dev (11); Unit 5 Dev (10); Unit 5 Dev - Dungeon (10)
- **Intervals:** median 18.49s (p5 1.20s / p95 742.51s, n=231)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 232/232 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 232/232 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 87 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (17); Unit 3 Dev (11); Unit 5 Dev (11); Unit 4 Dev (9); Unit 4 Dev - Dungeon (8); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (5); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 87 of 87 records
- **Intervals:** median 201.82s (p5 0.00s / p95 60123.36s, n=86)
- **`data` key-set variants:** [questEventType, questID, questName] x51; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 87/87 records)
    "questActiveEvent"  x51
    "questFinishEvent"  x36
data.questID  (string, 87/87 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 87/87 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/87 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 74 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (38); Unit 3 Dev (36)
- **Intervals:** median 5.97s (p5 1.56s / p95 9466.95s, n=73)
- **`data` key-set variants:** [actionType, featureUsed] x52; [actionType, featureUsed, location] x20; [actionType, featureUsed, legendName] x2
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 74/74 records)
    "MapCloseEvent"  x26
    "MapOpenEvent"  x26
    "WaypointMoveEvent"  x14
    "WaypointSetEvent"  x6
    "Selected"  x2
data.featureUsed  (string, 74/74 records)
    "Map"  x52
    "Waypoint"  x20
    "Legend"  x2
data.legendName  (string, 2/74 records)
    "0 ft"  x1
    "90 ft"  x1
data.location  (object, 20/74 records)
data.location.x  (number, 20/74 records)
    numeric range -323.629 .. 550.845 (20 unique)
data.location.y  (number, 20/74 records)
    numeric range -360.342 .. 346.829 (20 unique)
data.location.z  (number, 20/74 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 72 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (49); Unit 3 Dev (11); Unit 5 Dev (7); Unit 1 Dev (4); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 19.38s (p5 2.27s / p95 70077.08s, n=71)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 72/72 records)
    "submitAnswerEvent"  x72
data.answerSubmitted  (string, 72/72 records)
    25 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 72/72 records)
    "Unit 4 - Flooding"  x49
    "Unit 3 - Pollution Upstream"  x11
    "Unit 5"  x7
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `Soil Key Puzzle` — 57 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 4 Dev (20); Unit 3 Dev (16)
- **Intervals:** median 1.74s (p5 0.42s / p95 22445.79s, n=56)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x49; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/57 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/57 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 49/57 records)
    "RightDrag"  x31
    "LeftDrag"  x18
data.currentSoilType  (string, 49/57 records)
    "CLAYSAND"  x12
    "SAND"  x11
    "CLAY"  x10
    "CLAYROCK"  x7
    "SANDGRAVEL"  x5
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 49/57 records)
    "false"  x36
    "true"  x13
data.waterLevelStatus  (string, 49/57 records)
    "TooHigh"  x21
    "Proper"  x20
    "TooLow"  x8
data.waterRetentionChange  (string, 49/57 records)
    "Increase"  x19
    "Decrease"  x17
    "NoChange"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 35 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (4); Unit 3 Dev (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 466.15s (p5 8.97s / p95 86226.06s, n=34)
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "DebugMenuStateChanged"  x35
data.isOpened  (bool, 35/35 records)
    false  x35
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 28 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (17); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1169.28s (p5 73.29s / p95 86154.71s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 28/28 records)
    true  x28
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationEvent` — 23 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 4 Dev - Anderson Base (6); Unit 5 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 127.88s (p5 0.63s / p95 87680.51s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "argumentationSessionOpen"  x12
    "argumentationSessionClose"  x11
data.argumentationDescription  (string, 23/23 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x6
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 23/23 records)
    "Unit 4 - Flooding"  x6
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 5"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `WaterChamberEvent` — 22 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (22)
- **Intervals:** median 22.52s (p5 3.96s / p95 85.97s, n=21)
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "On"  x16
    "Off"  x6
data.floor  (string, 22/22 records)
    "3"  x8
    "4"  x7
    "2"  x4
    "1"  x3
data.machineNumber  (string, 22/22 records)
    "One"  x21
    "Two"  x1
data.machineType  (string, 22/22 records)
    "Condenser"  x9
    "Evaporator"  x8
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 22/22 records)
    "2"  x10
    "3"  x6
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 20 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (11); Unit 3 Dev (4); Unit 5 Dev (4); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 2.71s (p5 0.13s / p95 156326.61s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationToolOpen"  x15
    "argumentationToolClose"  x5
data.argumentationTitle  (string, 20/20 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x4
    "Unit 5"  x4
    "Unit 2 – Watershed"  x1
data.toolName  (string, 20/20 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Pollution Site Data"  x3
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Heat Added/Released Chart"  x2
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 13258.27s (p5 163.74s / p95 189730.42s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 15 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (3); Unit 2 Prod (Refactor) (2); MainMenu (1); Unit 1 Dev (1); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 4029.21s (p5 87.46s / p95 262569.09s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    false  x15
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 5.58s (p5 1.37s / p95 36.32s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 4 empty-string)
    "cameraPlaced"  x5
    ""  x4
data.boxId  (string, 9/9 records)
    "1"  x4
    "0"  x3
    "2"  x2
data.soilType  (string, 9/9 records)
    "Clay"  x4
    "Gravel"  x2
    "Sand"  x2
    "None"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 9 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (9)
- **Intervals:** median 36.31s (p5 1.44s / p95 185.83s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "ChangeCanister"  x9
data.canisterType  (string, 9/9 records)
    "Clay"  x3
    "Bedrock"  x2
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 9/9 records)
    "5"  x5
    "4"  x3
    "3"  x1
data.machine  (string, 9/9 records)
    "1"  x7
    "2"  x2
data.row  (string, 9/9 records)
    "TopRow"  x7
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 74446.27s (p5 29689.02s / p95 526953.32s, n=4)
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

### `SolarStillDesignEvent` — 4 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (4)
- **Intervals:** median 3.24s (p5 2.01s / p95 3.40s, n=3)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x3; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "optionSelected"  x3
    "DesignSubmitted"  x1
data.designSelections  (object, 1/4 records)
data.designSelections.glassRoofTemperature  (string, 1/4 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/4 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Flat"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Flat"  x1
    "Hot"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `chatEvent` — 3 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 28555.68s (p5 3622.95s / p95 53488.41s, n=2)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "Close"  x3
data.chatID  (string, 3/3 records)
    "NA"  x3
```

Raw examples: `event_examples.json` -> `chatEvent`.

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
    "unit1"  x1
    "unit2"  x1
    "unit3"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 7.60s (p5 7.60s / p95 7.60s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (21 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TerasGardenBox` data.soilType: "None" (1x)
- `TopographicMapEvent` data.actionType: "Selected" (2x); "WaypointMoveEvent" (14x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (2x); "Waypoint" (20x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (72x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*