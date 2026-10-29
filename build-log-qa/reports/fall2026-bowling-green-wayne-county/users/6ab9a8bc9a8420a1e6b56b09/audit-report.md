# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b09

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b09
- **Game version string(s) in log:** 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b09.jsonl
- **Records:** 10004 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b09
- **Time span:** 2026-10-05T15:16:01.067000+00:00 .. 2026-10-16T15:51:13.219000+00:00 (264h 35m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b09\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 10004 records, 10 scenes.
- Findings: **0 FAIL**, **32 WARNING**, 87 INFO, 0 NOT_TESTED, 100 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4125 | 41.23 | 1 | 9 | 0 | 2026-10-05T15:21:14.728000+00:00 | 2026-10-16T15:51:13.219000+00:00 | 264h 29m |
| DialogueEvent | 2137 | 21.36 | 1 | 9 | 1354 | 2026-10-05T15:16:31.711000+00:00 | 2026-10-16T15:51:03.856000+00:00 | 264h 34m |
| PlayerPositionEvent | 1603 | 16.02 | 1 | 9 | 0 | 2026-10-05T15:16:11.951000+00:00 | 2026-10-16T15:51:09.220000+00:00 | 264h 34m |
| PuzzlePieceVisibleEvent | 1215 | 12.15 | 1 | 4 | 0 | 2026-10-06T15:33:43.604000+00:00 | 2026-10-16T15:20:55.836000+00:00 | 239h 47m |
| argumentationNodeEvent | 284 | 2.84 | 1 | 5 | 0 | 2026-10-05T15:38:41.201000+00:00 | 2026-10-16T15:37:50.205000+00:00 | 263h 59m |
| ObjectInterEvent | 249 | 2.49 | 1 | 9 | 0 | 2026-10-05T15:22:16.635000+00:00 | 2026-10-16T15:51:13.218000+00:00 | 264h 28m |
| questEvent | 91 | 0.91 | 1 | 9 | 91 | 2026-10-05T15:16:31.683000+00:00 | 2026-10-16T15:45:42.255000+00:00 | 264h 29m |
| Soil Key Puzzle | 73 | 0.73 | 1 | 3 | 0 | 2026-10-07T15:47:09.374000+00:00 | 2026-10-14T15:40:48.732000+00:00 | 167h 53m |
| TopographicMapEvent | 59 | 0.59 | 1 | 2 | 0 | 2026-10-06T15:34:17.181000+00:00 | 2026-10-14T15:23:39.381000+00:00 | 191h 49m |
| DEBUGMenu | 32 | 0.32 | 1 | 9 | 0 | 2026-10-05T15:16:11.939000+00:00 | 2026-10-16T15:17:22.035000+00:00 | 264h 1m |
| WaterChamberEvent | 21 | 0.21 | 1 | 1 | 0 | 2026-10-16T15:21:08.701000+00:00 | 2026-10-16T15:31:06.773000+00:00 | 9m 58s |
| argumentationAnswerEvent | 20 | 0.2 | 1 | 5 | 0 | 2026-10-05T15:39:40.351000+00:00 | 2026-10-16T15:37:51.849000+00:00 | 263h 58m |
| argumentationEvent | 17 | 0.17 | 1 | 5 | 0 | 2026-10-05T15:39:29.681000+00:00 | 2026-10-16T15:37:51.883000+00:00 | 263h 58m |
| gameWindowFocusEvent | 17 | 0.17 | 1 | 3 | 0 | 2026-10-05T15:16:01.067000+00:00 | 2026-10-16T15:17:15.113000+00:00 | 264h 1m |
| gameStartEvent | 14 | 0.14 | 1 | 1 | 0 | 2026-10-05T15:16:01.069000+00:00 | 2026-10-16T15:17:15.113000+00:00 | 264h 1m |
| soilMachine | 13 | 0.13 | 1 | 1 | 0 | 2026-10-15T15:09:00.670000+00:00 | 2026-10-15T15:27:32.074000+00:00 | 18m 31s |
| gameWindowUnfocusEvent | 8 | 0.08 | 1 | 3 | 0 | 2026-10-05T15:48:03.687000+00:00 | 2026-10-15T15:48:15.957000+00:00 | 240h 0m |
| EndOfUnit | 6 | 0.06 | 1 | 5 | 0 | 2026-10-05T15:44:01.307000+00:00 | 2026-10-16T15:51:13.216000+00:00 | 264h 7m |
| TerasGardenBox | 6 | 0.06 | 1 | 1 | 0 | 2026-10-16T15:08:36.991000+00:00 | 2026-10-16T15:09:23.408000+00:00 | 46.4s |
| SolarStillDesignEvent | 5 | 0.05 | 1 | 1 | 0 | 2026-10-16T15:43:21.906000+00:00 | 2026-10-16T15:43:35.019000+00:00 | 13.1s |
| DaniEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-10-13T15:07:59.300000+00:00 | 2026-10-13T15:09:24.968000+00:00 | 1m 25s |
| argumentationToolEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-05T15:39:27.591000+00:00 | 2026-10-05T15:39:29.579000+00:00 | 2.0s |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-16T15:17:21.776000+00:00 | 2026-10-16T15:32:08.257000+00:00 | 14m 46s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 86574.088s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.065s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.276s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 9.047s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.798s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.988s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 84685.665s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1648.264s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 85321.06s median 
  - Expected: 108.82s in 09-23-26 
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
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; p; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 1215 records 
  - Expected: 5172 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; B,2,II; B,4,II; C,2,II; D,1,II; D,2,II; D,C,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 17 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
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
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[152] _id=6ac3c127de269131f9ad2023 ts=2026-10-05T15:24:22.2760000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[206] _id=6ac3c1fede269131f9ad2dde ts=2026-10-05T15:27:57.0380000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[256] _id=6ac3c29bde269131f9ad367f ts=2026-10-05T15:30:34.6750000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[1] _id=6ac3bf32de269131f9ace74b ts=2026-10-05T15:16:01.0690000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[618] _id=6ac3c617de269131f9ad6b57 ts=2026-10-05T15:45:26.3440000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[652] _id=6ac51437de269131f9b4679b ts=2026-10-06T15:31:02.8970000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[2] _id=6ac3bf32de269131f9ace749 ts=2026-10-05T15:16:01.0670000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[619] _id=6ac3c617de269131f9ad6b53 ts=2026-10-05T15:45:26.3420000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[654] _id=6ac51437de269131f9b46799 ts=2026-10-06T15:31:02.8960000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[653] _id=6ac51437de269131f9b46793 ts=2026-10-05T15:48:03.687Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[1484] _id=6ac662f0de269131f9bb9a4a ts=2026-10-06T15:47:37.952Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[1496] _id=6ac66307de269131f9bb9ad0 ts=2026-10-07T15:19:35.0860000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 4124 | 0.0 | 0.565 | 230.892 | 10.682 | 429698.241 | 0.26 | 87 | 7 |
| DialogueEvent | 2136 | 0.0 | 4.013 | 445.914 | 25.719 | 429671.575 | 0.13 | 613 | 7 |
| PlayerPositionEvent | 1589 | 9.78 | 10.001 | 546.662 | 10.138 | 429655.964 | 0.11 | 0 | 6 |
| PuzzlePieceVisibleEvent | 1214 | 0.0 | 0.065 | 711.064 | 1.971 | 516926.532 | 0.08 | 558 | 5 |
| argumentationNodeEvent | 283 | 0.001 | 0.593 | 3358.124 | 10.28 | 689990.14 | 0.02 | 42 | 5 |
| ObjectInterEvent | 248 | 0.0 | 10.776 | 3839.26 | 375.467 | 431050.86 | 0.02 | 5 | 9 |
| questEvent | 90 | 0.0 | 179.988 | 10579.451 | 83813.342 | 430246.975 | 0.01 | 16 | 11 |
| Soil Key Puzzle | 72 | 0.162 | 2.276 | 8394.713 | 15.135 | 517323.316 | 0.01 | 0 | 3 |
| TopographicMapEvent | 58 | 0.021 | 9.047 | 11906.245 | 85048.069 | 430025.186 | 0.01 | 3 | 6 |
| DEBUGMenu | 31 | 7.084 | 545.406 | 30660.326 | 85727.95 | 431160.266 | 0.0 | 0 | 14 |
| WaterChamberEvent | 20 | 1.342 | 26.27 | 29.904 | 68.384 | 161.954 | 2.01 | 0 | 0 |
| argumentationAnswerEvent | 19 | 3.202 | 20.798 | 50015.342 | 224386.722 | 690037.822 | 0.0 | 0 | 5 |
| argumentationEvent | 16 | 0.031 | 56.722 | 59393.888 | 301933.23 | 689991.543 | 0.0 | 2 | 5 |
| gameWindowFocusEvent | 16 | 16.014 | 1648.264 | 59404.628 | 172139.506 | 431186.111 | 0.0 | 0 | 13 |
| gameStartEvent | 13 | 646.46 | 84685.665 | 73113.388 | 223948.827 | 431186.111 | 0.0 | 0 | 13 |
| soilMachine | 12 | 2.041 | 90.93 | 92.617 | 223.139 | 251.099 | 0.65 | 0 | 0 |
| gameWindowUnfocusEvent | 7 | 15.599 | 85321.06 | 123430.324 | 389107.962 | 518363.025 | 0.0 | 0 | 6 |
| EndOfUnit | 5 | 0.664 | 86574.088 | 190166.382 | 586511.22 | 690120.282 | 0.0 | 0 | 4 |
| TerasGardenBox | 5 | 2.18 | 2.975 | 9.283 | 22.349 | 24.233 | 6.46 | 0 | 0 |
| SolarStillDesignEvent | 4 | 2.184 | 3.183 | 3.278 | 4.414 | 4.563 | 18.3 | 0 | 0 |
| DaniEvent | 3 | 0.48 | 4.422 | 28.556 | 73.132 | 80.766 | 2.1 | 0 | 0 |
| argumentationToolEvent | 1 | 1.988 | 1.988 | 1.988 | 1.988 | 1.988 | 30.18 | 0 | 0 |
| chatEvent | 1 | 886.481 | 886.481 | 886.481 | 886.481 | 886.481 | 0.07 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[6694] _id=6ad0ecf7de269131f9dc4ce0 ts=2026-10-15T15:10:46.9220000Z == 6ab9a8bc9a8420a1e6b56b09.jsonl[6695] _id=6ad0ecf7de269131f9dc4ce1 ts=2026-10-15T15:10:46.9220000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 41 group(s), 69 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[781] _id=6ac51554de269131f9b47c5e ts=2026-10-06T15:35:47.6730000Z == 6ab9a8bc9a8420a1e6b56b09.jsonl[776] _id=6ac51555de269131f9b47c63 ts=2026-10-06T15:35:47.6730000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[789] _id=6ac51556de269131f9b47c8b ts=2026-10-06T15:35:48.0980000Z == 6ab9a8bc9a8420a1e6b56b09.jsonl[785] _id=6ac51556de269131f9b47c90 ts=2026-10-06T15:35:48.0980000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[796] _id=6ac51558de269131f9b47cd7 ts=2026-10-06T15:35:49.4120000Z == 6ab9a8bc9a8420a1e6b56b09.jsonl[780] _id=6ac51558de269131f9b47cdb ts=2026-10-06T15:35:49.4120000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[9735] _id=6ad2451bde269131f9e556a2 ts=2026-10-16T15:39:06.5160000Z == 6ab9a8bc9a8420a1e6b56b09.jsonl[9736] _id=6ad2451bde269131f9e556a3 ts=2026-10-16T15:39:06.5160000Z`
- **INFO / Info** `EndOfUnit` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `664ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[10001] _id=6ad247f1de269131f9e56417 ts=2026-10-16T15:51:12.5520000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[9995] _id=6ad247f1de269131f9e5641c ts=2026-10-16T15:51:13.2160000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[106] _id=6ac3c0a9de269131f9ad0fff ts=2026-10-05T15:22:16.6350000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[108] _id=6ac3c0aade269131f9ad100b ts=2026-10-05T15:22:16.6420000Z`; `342ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[703] _id=6ac5149bde269131f9b46dce ts=2026-10-06T15:32:42.9360000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[689] _id=6ac5149bde269131f9b46dd9 ts=2026-10-06T15:32:43.2780000Z`; `956ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[689] _id=6ac5149bde269131f9b46dd9 ts=2026-10-06T15:32:43.2780000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[691] _id=6ac5149cde269131f9b46de1 ts=2026-10-06T15:32:44.2340000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 51 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `425ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[777] _id=6ac51555de269131f9b47c79 ts=2026-10-06T15:35:47.6730000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[789] _id=6ac51556de269131f9b47c8b ts=2026-10-06T15:35:48.0980000Z`; `139ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[801] _id=6ac51559de269131f9b47cef ts=2026-10-06T15:35:50.0140000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[797] _id=6ac51559de269131f9b47cf3 ts=2026-10-06T15:35:50.1530000Z`; `32ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[798] _id=6ac51559de269131f9b47cf5 ts=2026-10-06T15:35:50.1530000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[802] _id=6ac51559de269131f9b47cfd ts=2026-10-06T15:35:50.1850000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1471] _id=6ac51813de269131f9b4be3b ts=2026-10-06T15:47:31.0040000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[1476] _id=6ac51813de269131f9b4be45 ts=2026-10-06T15:47:31.0330000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `31ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[4290] _id=6ace51e9de269131f9cf4345 ts=2026-10-13T15:44:41.1340000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[4296] _id=6ace51e9de269131f9cf4348 ts=2026-10-13T15:44:41.1650000Z`; `51ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8218] _id=6ad0f4e3de269131f9dcd4a2 ts=2026-10-15T15:44:35.0040000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[8221] _id=6ad0f4e3de269131f9dcd4a5 ts=2026-10-15T15:44:35.0550000Z`; `33ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8464] _id=6ad23d0ade269131f9e4d856 ts=2026-10-16T15:04:41.9770000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[8467] _id=6ad23d0ade269131f9e4d859 ts=2026-10-16T15:04:42.0100000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `607ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[430] _id=6ac3c484de269131f9ad53cc ts=2026-10-05T15:38:43.5650000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[420] _id=6ac3c485de269131f9ad53e1 ts=2026-10-05T15:38:44.1720000Z`; `35ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[453] _id=6ac3c4b8de269131f9ad57dd ts=2026-10-05T15:39:35.5070000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[454] _id=6ac3c4b8de269131f9ad57e1 ts=2026-10-05T15:39:35.5420000Z`; `641ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[3601] _id=6ace4c50de269131f9cf1159 ts=2026-10-13T15:20:47.7580000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[3588] _id=6ace4c51de269131f9cf115f ts=2026-10-13T15:20:48.3990000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[9887] _id=6ad2466ade269131f9e55e7e ts=2026-10-16T15:44:42.1960000Z ~ 6ab9a8bc9a8420a1e6b56b09.jsonl[9889] _id=6ad2466ade269131f9e55e80 ts=2026-10-16T15:44:42.1990000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2270] _id=6ac7b4aede269131f9c386d7 ts=2026-10-08T15:20:14.7240000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3163] _id=6ace48e7de269131f9cf04ed ts=2026-10-13T15:06:14.9900000Z; 23h 49m: 6ab9a8bc9a8420a1e6b56b09.jsonl[1829] _id=6ac66581de269131f9bbdb2d ts=2026-10-07T15:30:08.8910000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2265] _id=6ac7b495de269131f9c384d7 ts=2026-10-08T15:19:48.8940000Z; 23h 47m: 6ab9a8bc9a8420a1e6b56b09.jsonl[651] _id=6ac51444de269131f9b46885 ts=2026-10-06T15:31:15.9000000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1485] _id=6ac662f1de269131f9bb9a4c ts=2026-10-07T15:19:11.7970000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a8bc9a8420a1e6b56b09.jsonl[3156] _id=6ac7ba8cde269131f9c41e91 ts=2026-10-08T15:45:16.1610000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3167] _id=6ace48f5de269131f9cf0519 ts=2026-10-13T15:06:27.7360000Z; 23h 44m: 6ab9a8bc9a8420a1e6b56b09.jsonl[642] _id=6ac3c688de269131f9ad75e3 ts=2026-10-05T15:47:19.1040000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[676] _id=6ac51475de269131f9b46b5f ts=2026-10-06T15:32:04.9590000Z; 23h 36m: 6ab9a8bc9a8420a1e6b56b09.jsonl[1475] _id=6ac51813de269131f9b4be43 ts=2026-10-06T15:47:31.0280000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1758] _id=6ac663f4de269131f9bbad5b ts=2026-10-07T15:23:31.9040000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 613 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[3059] _id=6ac7b959de269131f9c410c3 ts=2026-10-08T15:40:09.0340000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3060] _id=6ac7b959de269131f9c410c4 ts=2026-10-08T15:40:09.0340000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[4252] _id=6ace51b3de269131f9cf40c9 ts=2026-10-13T15:43:46.5130000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4253] _id=6ace51b3de269131f9cf40ca ts=2026-10-13T15:43:46.5130000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8092] _id=6ad0f451de269131f9dccb9e ts=2026-10-15T15:42:08.8610000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8093] _id=6ad0f451de269131f9dccb9f ts=2026-10-15T15:42:08.8610000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 191h 42m 
  - Evidence: 191h 42m: 6ab9a8bc9a8420a1e6b56b09.jsonl[616] _id=6ac3c5c2de269131f9ad6749 ts=2026-10-05T15:44:01.3070000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3744] _id=6ace4d8ade269131f9cf1b33 ts=2026-10-13T15:26:01.5890000Z; 47h 47m: 6ab9a8bc9a8420a1e6b56b09.jsonl[5451] _id=6acf9fb7de269131f9d4b36d ts=2026-10-14T15:28:55.6770000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8850] _id=6ad23fe3de269131f9e5166d ts=2026-10-16T15:16:50.6510000Z; 24h 2m: 6ab9a8bc9a8420a1e6b56b09.jsonl[3744] _id=6ace4d8ade269131f9cf1b33 ts=2026-10-13T15:26:01.5890000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[5451] _id=6acf9fb7de269131f9d4b36d ts=2026-10-14T15:28:55.6770000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 21m 
  - Evidence: 119h 21m: 6ab9a8bc9a8420a1e6b56b09.jsonl[3145] _id=6ac7ba71de269131f9c41d6b ts=2026-10-08T15:44:49.4750000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3166] _id=6ace48f5de269131f9cf0518 ts=2026-10-13T15:06:27.7160000Z; 23h 45m: 6ab9a8bc9a8420a1e6b56b09.jsonl[626] _id=6ac3c634de269131f9ad6d27 ts=2026-10-05T15:45:55.4370000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[661] _id=6ac51465de269131f9b46a97 ts=2026-10-06T15:31:49.3350000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2232] _id=6ac6697dde269131f9bc2ecc ts=2026-10-07T15:47:08.5710000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2278] _id=6ac7b4c0de269131f9c38878 ts=2026-10-08T15:20:32.1530000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 87 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[6694] _id=6ad0ecf7de269131f9dc4ce0 ts=2026-10-15T15:10:46.9220000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[6695] _id=6ad0ecf7de269131f9dc4ce1 ts=2026-10-15T15:10:46.9220000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8894] _id=6ad2403ade269131f9e5199f ts=2026-10-16T15:18:17.4900000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8895] _id=6ad2403ade269131f9e519a0 ts=2026-10-16T15:18:17.4900000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[9045] _id=6ad240d9de269131f9e521b9 ts=2026-10-16T15:20:57.0390000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[9046] _id=6ad240d9de269131f9e521ba ts=2026-10-16T15:20:57.0390000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 44m 
  - Evidence: 119h 44m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2794] _id=6ac7b6b8de269131f9c3caaa ts=2026-10-08T15:28:56.0180000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3390] _id=6ace4a83de269131f9cf09eb ts=2026-10-13T15:13:06.8780000Z; 24h 8m: 6ab9a8bc9a8420a1e6b56b09.jsonl[1298] _id=6ac515fade269131f9b48b13 ts=2026-10-06T15:38:34.1070000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2235] _id=6ac6697ede269131f9bc2ed6 ts=2026-10-07T15:47:09.3780000Z; 23h 49m: 6ab9a8bc9a8420a1e6b56b09.jsonl[595] _id=6ac3c597de269131f9ad63dd ts=2026-10-05T15:43:18.7050000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[683] _id=6ac51498de269131f9b46daf ts=2026-10-06T15:32:40.1850000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[7967] _id=6ad0f34dde269131f9dcbc56 ts=2026-10-15T15:37:48.7320000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[7968] _id=6ad0f34dde269131f9dcbc57 ts=2026-10-15T15:37:48.7320000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8006] _id=6ad0f383de269131f9dcbf07 ts=2026-10-15T15:38:43.0510000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8007] _id=6ad0f383de269131f9dcbf08 ts=2026-10-15T15:38:43.0510000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8343] _id=6ad23c51de269131f9e4c798 ts=2026-10-16T15:01:36.7730000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8344] _id=6ad23c51de269131f9e4c799 ts=2026-10-16T15:01:36.7730000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a8bc9a8420a1e6b56b09.jsonl[3157] _id=6ac7ba99de269131f9c41edf ts=2026-10-08T15:45:28.9440000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3165] _id=6ace48f5de269131f9cf0517 ts=2026-10-13T15:06:24.9080000Z; 23h 43m: 6ab9a8bc9a8420a1e6b56b09.jsonl[647] _id=6ac3c6b2de269131f9ad787f ts=2026-10-05T15:48:01.1720000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[649] _id=6ac51447de269131f9b468b3 ts=2026-10-06T15:31:15.9140000Z; 23h 32m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2262] _id=6ac669b1de269131f9bc3145 ts=2026-10-07T15:48:00.4100000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2271] _id=6ac7b4b2de269131f9c38726 ts=2026-10-08T15:20:14.7360000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 35m 
  - Evidence: 143h 35m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2888] _id=6ac7b76bde269131f9c3e325 ts=2026-10-08T15:31:53.8400000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4563] _id=6acf9aa9de269131f9d45718 ts=2026-10-14T15:07:20.3720000Z; 47h 46m: 6ab9a8bc9a8420a1e6b56b09.jsonl[1246] _id=6ac515dcde269131f9b48981 ts=2026-10-06T15:38:02.3320000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2404] _id=6ac7b5c0de269131f9c3a2cd ts=2026-10-08T15:24:47.5770000Z; 23h 46m: 6ab9a8bc9a8420a1e6b56b09.jsonl[5950] _id=6acfa2e3de269131f9d4e4f4 ts=2026-10-14T15:42:24.7540000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[7666] _id=6ad0f11fde269131f9dc954a ts=2026-10-15T15:28:30.3790000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 558 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1010] _id=6ac515a4de269131f9b483c0 ts=2026-10-06T15:37:07.0500000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[992] _id=6ac515a4de269131f9b483c4 ts=2026-10-06T15:37:07.0500000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1012] _id=6ac515a8de269131f9b4841c ts=2026-10-06T15:37:10.7280000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1013] _id=6ac515a8de269131f9b48422 ts=2026-10-06T15:37:10.7280000Z; 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1013] _id=6ac515a8de269131f9b48422 ts=2026-10-06T15:37:10.7280000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1028] _id=6ac515a8de269131f9b48424 ts=2026-10-06T15:37:10.7280000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 143h 42m 
  - Evidence: 143h 42m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2377] _id=6ac7b58dde269131f9c39d17 ts=2026-10-08T15:23:57.5730000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4507] _id=6acf9a59de269131f9d4517c ts=2026-10-14T15:06:00.8890000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2242] _id=6ac669b2de269131f9bc3158 ts=2026-10-07T15:48:02.0350000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2345] _id=6ac7b52fde269131f9c393e9 ts=2026-10-08T15:22:23.1720000Z; 33m 32s: 6ab9a8bc9a8420a1e6b56b09.jsonl[4528] _id=6acf9a7ede269131f9d453cb ts=2026-10-14T15:06:38.6430000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[5590] _id=6acfa25bde269131f9d4dbb4 ts=2026-10-14T15:40:11.3870000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 27m 
  - Evidence: 119h 27m: 6ab9a8bc9a8420a1e6b56b09.jsonl[3074] _id=6ac7b986de269131f9c41293 ts=2026-10-08T15:40:54.5960000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3273] _id=6ace4950de269131f9cf06c1 ts=2026-10-13T15:07:59.7820000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2137] _id=6ac66932de269131f9bc2792 ts=2026-10-07T15:45:53.3220000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3072] _id=6ac7b97ade269131f9c41214 ts=2026-10-08T15:40:42.2640000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b09.jsonl[3840] _id=6ace4f0fde269131f9cf2665 ts=2026-10-13T15:32:30.4290000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[5226] _id=6acf9df4de269131f9d49b76 ts=2026-10-14T15:21:24.6490000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.021s..0.029s shown 
  - Evidence: 21ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1474] _id=6ac51813de269131f9b4be39 ts=2026-10-06T15:47:30.9830000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1471] _id=6ac51813de269131f9b4be3b ts=2026-10-06T15:47:31.0040000Z; 26ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1941] _id=6ac666e1de269131f9bc00ad ts=2026-10-07T15:36:00.2050000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1946] _id=6ac666e1de269131f9bc00b1 ts=2026-10-07T15:36:00.2310000Z; 29ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[1471] _id=6ac51813de269131f9b4be3b ts=2026-10-06T15:47:31.0040000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1476] _id=6ac51813de269131f9b4be45 ts=2026-10-06T15:47:31.0330000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 40m 
  - Evidence: 191h 40m: 6ab9a8bc9a8420a1e6b56b09.jsonl[484] _id=6ac3c50dde269131f9ad5c5f ts=2026-10-05T15:41:00.1730000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3641] _id=6ace4c82de269131f9cf12ba ts=2026-10-13T15:21:37.9950000Z; 47h 57m: 6ab9a8bc9a8420a1e6b56b09.jsonl[4295] _id=6ace51e9de269131f9cf4343 ts=2026-10-13T15:44:41.1190000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8099] _id=6ad0f451de269131f9dccb98 ts=2026-10-15T15:42:08.8300000Z; 23h 20m: 6ab9a8bc9a8420a1e6b56b09.jsonl[8216] _id=6ad0f4e3de269131f9dcd49d ts=2026-10-15T15:44:34.9890000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8463] _id=6ad23d0ade269131f9e4d84f ts=2026-10-16T15:04:41.9580000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 39m 
  - Evidence: 191h 39m: 6ab9a8bc9a8420a1e6b56b09.jsonl[485] _id=6ac3c50dde269131f9ad5c61 ts=2026-10-05T15:41:00.1960000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3605] _id=6ace4c54de269131f9cf117a ts=2026-10-13T15:20:51.7390000Z; 47h 56m: 6ab9a8bc9a8420a1e6b56b09.jsonl[4296] _id=6ace51e9de269131f9cf4348 ts=2026-10-13T15:44:41.1650000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8053] _id=6ad0f40ede269131f9dcc85e ts=2026-10-15T15:41:01.6240000Z; 23h 19m: 6ab9a8bc9a8420a1e6b56b09.jsonl[8221] _id=6ad0f4e3de269131f9dcd4a5 ts=2026-10-15T15:44:35.0550000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8440] _id=6ad23cf6de269131f9e4d5e7 ts=2026-10-16T15:04:21.7900000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.031s..0.033s shown 
  - Evidence: 31ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[4290] _id=6ace51e9de269131f9cf4345 ts=2026-10-13T15:44:41.1340000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4296] _id=6ace51e9de269131f9cf4348 ts=2026-10-13T15:44:41.1650000Z; 33ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[8464] _id=6ad23d0ade269131f9e4d856 ts=2026-10-16T15:04:41.9770000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8467] _id=6ad23d0ade269131f9e4d859 ts=2026-10-16T15:04:42.0100000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 191h 39m 
  - Evidence: 191h 39m: 6ab9a8bc9a8420a1e6b56b09.jsonl[495] _id=6ac3c50ade269131f9ad5c49 ts=2026-10-05T15:40:57.6180000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3601] _id=6ace4c50de269131f9cf1159 ts=2026-10-13T15:20:47.7580000Z; 47h 56m: 6ab9a8bc9a8420a1e6b56b09.jsonl[4293] _id=6ace51e5de269131f9cf4309 ts=2026-10-13T15:44:36.4870000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8052] _id=6ad0f40bde269131f9dcc831 ts=2026-10-15T15:40:58.9950000Z; 23h 19m: 6ab9a8bc9a8420a1e6b56b09.jsonl[8180] _id=6ad0f4e2de269131f9dcd47d ts=2026-10-15T15:44:33.0480000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8443] _id=6ad23cf9de269131f9e4d654 ts=2026-10-16T15:04:24.6850000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 42 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[4211] _id=6ace5187de269131f9cf3ef0 ts=2026-10-13T15:43:03.3430000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4212] _id=6ace5187de269131f9cf3ef1 ts=2026-10-13T15:43:03.3440000Z; 5ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[4232] _id=6ace5191de269131f9cf3f86 ts=2026-10-13T15:43:13.1850000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4233] _id=6ace5191de269131f9cf3f88 ts=2026-10-13T15:43:13.1900000Z; 6ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[9672] _id=6ad244c1de269131f9e553c5 ts=2026-10-16T15:37:36.8390000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[9675] _id=6ad244c1de269131f9e553c9 ts=2026-10-16T15:37:36.8450000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 14m 46s 
  - Evidence: 14m 46s: 6ab9a8bc9a8420a1e6b56b09.jsonl[8683] _id=6ad24002de269131f9e5177a ts=2026-10-16T15:17:21.7760000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[9485] _id=6ad24378de269131f9e544c2 ts=2026-10-16T15:32:08.2570000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2267] _id=6ac7b495de269131f9c384d9 ts=2026-10-08T15:19:49.0320000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3162] _id=6ace48e7de269131f9cf04f0 ts=2026-10-13T15:06:15.1430000Z; 23h 49m: 6ab9a8bc9a8420a1e6b56b09.jsonl[1822] _id=6ac66577de269131f9bbda2a ts=2026-10-07T15:29:58.3940000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2267] _id=6ac7b495de269131f9c384d9 ts=2026-10-08T15:19:49.0320000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b09.jsonl[652] _id=6ac51437de269131f9b4679b ts=2026-10-06T15:31:02.8970000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1487] _id=6ac662f1de269131f9bb9a4e ts=2026-10-07T15:19:11.9340000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2266] _id=6ac7b495de269131f9c384d8 ts=2026-10-08T15:19:49.0320000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3161] _id=6ace48e7de269131f9cf04ef ts=2026-10-13T15:06:15.1430000Z; 23h 49m: 6ab9a8bc9a8420a1e6b56b09.jsonl[1821] _id=6ac66577de269131f9bbda29 ts=2026-10-07T15:29:58.3940000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2266] _id=6ac7b495de269131f9c384d8 ts=2026-10-08T15:19:49.0320000Z; 23h 48m: 6ab9a8bc9a8420a1e6b56b09.jsonl[654] _id=6ac51437de269131f9b46799 ts=2026-10-06T15:31:02.8960000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1486] _id=6ac662f1de269131f9bb9a4d ts=2026-10-07T15:19:11.9330000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 143h 59m 
  - Evidence: 143h 59m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2264] _id=6ac7b495de269131f9c384d5 ts=2026-10-07T15:48:03.458Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[4426] _id=6acf99cfde269131f9d448d6 ts=2026-10-13T15:47:26.483Z; 24h 18m: 6ab9a8bc9a8420a1e6b56b09.jsonl[5465] _id=6acf9fe8de269131f9d4b584 ts=2026-10-14T15:29:43.1420000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[8302] _id=6ad23c02de269131f9e4c1ed ts=2026-10-15T15:48:15.957Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b09.jsonl[653] _id=6ac51437de269131f9b46793 ts=2026-10-05T15:48:03.687Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[1484] _id=6ac662f0de269131f9bb9a4a ts=2026-10-06T15:47:37.952Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2981] _id=6ac7b84dde269131f9c3f6e8 ts=2026-10-08T15:35:40.8400000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[3169] _id=6ace48f5de269131f9cf051b ts=2026-10-13T15:06:27.8150000Z; 23h 44m: 6ab9a8bc9a8420a1e6b56b09.jsonl[641] _id=6ac3c67ede269131f9ad74bb ts=2026-10-05T15:47:09.7350000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[655] _id=6ac51447de269131f9b468bd ts=2026-10-06T15:31:17.8070000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b09.jsonl[2209] _id=6ac66973de269131f9bc2d64 ts=2026-10-07T15:46:58.2530000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[2274] _id=6ac7b4b2de269131f9c38729 ts=2026-10-08T15:20:17.5910000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[9735] _id=6ad2451bde269131f9e556a2 ts=2026-10-16T15:39:06.5160000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[9736] _id=6ad2451bde269131f9e556a3 ts=2026-10-16T15:39:06.5160000Z; 2ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[414] _id=6ac3c467de269131f9ad51ad ts=2026-10-05T15:38:13.6640000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[415] _id=6ac3c467de269131f9ad51b4 ts=2026-10-05T15:38:13.6660000Z; 3ms: 6ab9a8bc9a8420a1e6b56b09.jsonl[9887] _id=6ad2466ade269131f9e55e7e ts=2026-10-16T15:44:42.1960000Z -> 6ab9a8bc9a8420a1e6b56b09.jsonl[9889] _id=6ad2466ade269131f9e55e80 ts=2026-10-16T15:44:42.1990000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[366] _id=6ac3c444de269131f9ad4f2d ts=2026-10-05T15:37:39.7080000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[501] _id=6ac3c522de269131f9ad5d17 ts=2026-10-05T15:41:21.4360000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[2084] _id=6ac66839de269131f9bc180d ts=2026-10-07T15:41:44.4650000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[968] _id=6ac5159ade269131f9b48270 ts=2026-10-06T15:36:56.0510000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[963] _id=6ac5159ede269131f9b4830a ts=2026-10-06T15:37:00.9040000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[1000] _id=6ac5159ede269131f9b48310 ts=2026-10-06T15:37:01.3050000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 45 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[800] _id=6ac51558de269131f9b47ce1 ts=2026-10-06T15:35:49.4120000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[801] _id=6ac51559de269131f9b47cef ts=2026-10-06T15:35:50.0140000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[797] _id=6ac51559de269131f9b47cf3 ts=2026-10-06T15:35:50.1530000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[4296] _id=6ace51e9de269131f9cf4348 ts=2026-10-13T15:44:41.1650000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[8221] _id=6ad0f4e3de269131f9dcd4a5 ts=2026-10-15T15:44:35.0550000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[8467] _id=6ad23d0ade269131f9e4d859 ts=2026-10-16T15:04:42.0100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[454] _id=6ac3c4b8de269131f9ad57e1 ts=2026-10-05T15:39:35.5420000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[8683] _id=6ad24002de269131f9e5177a ts=2026-10-16T15:17:21.7760000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[9485] _id=6ad24378de269131f9e544c2 ts=2026-10-16T15:32:08.2570000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[4550] _id=6acf9aa2de269131f9d45691 ts=2026-10-14T15:07:14.4830000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[5471] _id=6acfa15fde269131f9d4c7ea ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 62 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[903] _id=6ac5157ede269131f9b47fa2 ts=2026-10-06T15:36:27.9520000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[899] _id=6ac5157fde269131f9b47fa6 ts=2026-10-06T15:36:28.2020000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[901] _id=6ac5157fde269131f9b47fac ts=2026-10-06T15:36:28.2180000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 129 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[776] _id=6ac51555de269131f9b47c63 ts=2026-10-06T15:35:47.6730000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[789] _id=6ac51556de269131f9b47c8b ts=2026-10-06T15:35:48.0980000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[785] _id=6ac51556de269131f9b47c90 ts=2026-10-06T15:35:48.0980000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[2345] _id=6ac7b52fde269131f9c393e9 ts=2026-10-08T15:22:23.1720000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 22 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[1471] _id=6ac51813de269131f9b4be3b ts=2026-10-06T15:47:31.0040000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[1476] _id=6ac51813de269131f9b4be45 ts=2026-10-06T15:47:31.0330000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[1720] _id=6ac663d3de269131f9bba8eb ts=2026-10-07T15:22:58.0170000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 395 start, 388 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 14 unmatched 'BecameCameraCentered' (totals: 252 open, 248 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 34 unmatched 'BecameVisible' (totals: 352 open, 363 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'MapOpenEvent' (totals: 24 open, 21 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 52 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 188 of 10002 adjacent _id pairs reverse in client time; worst 151.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b09.jsonl[822] _id=6ac5156fde269131f9b47e4e ts=2026-10-06T15:36:14.6290000Z`; `6ab9a8bc9a8420a1e6b56b09.jsonl[823] _id=6ac51570de269131f9b47e5a ts=2026-10-06T15:33:43.6040000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.69s, min -85379.54s, max -0.22s over 10003 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b09\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 4125 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1199); Unit 2 Prod (Refactor) (1023); Unit 3 Dev (470); Unit 4 Dev (358); Unit 3 Dungeon Dev (333); Unit 5 Dev - Dungeon (314); Unit 1 Dev (186); Unit 5 Dev (151); Unit 4 Dev - Anderson Base (91)
- **Intervals:** median 0.56s (p5 0.11s / p95 10.68s, n=4124)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4125/4125 records)
    "pressed"  x4125
data.actionType  (string, 4125/4125 records)
    "Move"  x3437
    "Interact"  x373
    "Sprint"  x197
    "Ascend"  x33
    "Hoverboard"  x32
    "Jump"  x30
    "Descend"  x11
    "Map"  x7
    "Pause"  x3
    "ToggleDebug"  x2
data.key  (string, 4125/4125 records, 11 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4125/4125 records)
    "Player"  x3803
    "Drone"  x322
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2137 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (627); Unit 3 Dev (283); Unit 4 Dev (281); Unit 5 Dev (210); Unit 1 Dev (199); Unit 4 Dev - Dungeon (172); Unit 4 Dev - Anderson Base (168); Unit 3 Dungeon Dev (123); Unit 5 Dev - Dungeon (74)
- **eventKey:** present on 1354 of 2137 records
- **Intervals:** median 4.01s (p5 0.00s / p95 25.72s, n=2136)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1354; [conversationId, dialogueEventType] x783
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2137/2137 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2137/2137 records)
    "DialogueNodeEvent"  x1354
    "DialogueStartEvent"  x395
    "DialogueFinishEvent"  x388
data.nodeId  (number, 1354/2137 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1603 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (512); Unit 4 Dev - Dungeon (195); Unit 3 Dev (191); Unit 4 Dev (177); Unit 1 Dev (167); Unit 5 Dev (113); Unit 5 Dev - Dungeon (87); Unit 4 Dev - Anderson Base (84); Unit 3 Dungeon Dev (77)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.14s, n=1589)
- **Fields under `data`:**

```text
data.position  (object, 1603/1603 records)
data.position.x  (number, 1603/1603 records)
    numeric range -689.089 .. 1556.59 (526 unique)
data.position.y  (number, 1603/1603 records)
    numeric range -112.489 .. 221.782 (390 unique)
data.position.z  (number, 1603/1603 records)
    numeric range -1041.82 .. 1743.17 (527 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `PuzzlePieceVisibleEvent` — 1215 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (721); Unit 4 Dev (294); Unit 5 Dev - Dungeon (126); Unit 3 Dungeon Dev (74)
- **Intervals:** median 0.07s (p5 0.00s / p95 1.97s, n=1214)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1215/1215 records)
    "BecameInvisible"  x363
    "BecameVisible"  x352
    "BecameCameraCentered"  x252
    "BecameCameraUncentered"  x248
data.pieceId  (string, 1215/1215 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1215/1215 records)
    756 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `argumentationNodeEvent` — 284 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (122); Unit 3 Dev (61); Unit 2 Prod (Refactor) (51); Unit 1 Dev (30); Unit 5 Dev (20)
- **Intervals:** median 0.59s (p5 0.03s / p95 10.28s, n=283)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 284/284 records)
    "argumentationNodeHoverEnd"  x119
    "argumentationNodeHoverStart"  x118
    "argumentationNodeAdd"  x36
    "argumentationNodeRemove"  x11
data.argumentationTitle  (string, 284/284 records)
    "Unit 4 - Flooding"  x122
    "Unit 3 - Pollution Upstream"  x61
    "Unit 2 – Watershed"  x51
    "Unit 5"  x20
    "Unit 1 - Argumentation Tutorial"  x17
    "Unit 1 - Freshwater"  x13
data.nodeName  (string, 284/284 records)
    "A"  x42
    "II"  x38
    "B"  x36
    "2"  x32
    "C"  x29
    "D"  x27
    "1"  x25
    "3"  x19
    "4"  x16
    "I"  x15
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 249 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (103); Unit 2 Prod (Refactor) (45); Unit 3 Dungeon Dev (28); Unit 4 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (11); Unit 1 Dev (10); Unit 5 Dev (9); Unit 5 Dev - Dungeon (7)
- **Intervals:** median 10.78s (p5 0.75s / p95 375.47s, n=248)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 249/249 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 249/249 records)
    104 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 91 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 4 Dev - Dungeon (18); Unit 1 Dev (12); Unit 3 Dev (11); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 91 of 91 records
- **Intervals:** median 179.99s (p5 0.01s / p95 83813.34s, n=90)
- **`data` key-set variants:** [questEventType, questID, questName] x52; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 91/91 records)
    "questActiveEvent"  x52
    "questFinishEvent"  x39
data.questID  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 91/91 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/91 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 73 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (47); Unit 4 Dev (14); Unit 3 Dev (12)
- **Intervals:** median 2.28s (p5 0.30s / p95 15.14s, n=72)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x66; [Soil Key Puzzle Status, Unit] x7
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 7/73 records)
    "Started"  x4
    "Finished"  x3
data.Unit  (string, 7/73 records)
    "Unit 2 Prod (Refactor)"  x3
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 66/73 records)
    "RightDrag"  x38
    "LeftDrag"  x28
data.currentSoilType  (string, 66/73 records)
    "CLAYSAND"  x15
    "SAND"  x14
    "CLAY"  x12
    "SANDGRAVEL"  x11
    "CLAYROCK"  x7
    "GRAVEL"  x5
    "BEDROCK"  x2
data.isCorrectSelection  (string, 66/73 records)
    "false"  x47
    "true"  x19
data.waterLevelStatus  (string, 66/73 records)
    "TooHigh"  x35
    "Proper"  x20
    "TooLow"  x11
data.waterRetentionChange  (string, 66/73 records)
    "Increase"  x24
    "Decrease"  x23
    "NoChange"  x19
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 59 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (38); Unit 3 Dev (21)
- **Intervals:** median 9.05s (p5 0.06s / p95 85048.07s, n=58)
- **`data` key-set variants:** [actionType, featureUsed] x45; [actionType, featureUsed, location] x14
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 59/59 records)
    "MapOpenEvent"  x24
    "MapCloseEvent"  x21
    "WaypointMoveEvent"  x9
    "WaypointSetEvent"  x5
data.featureUsed  (string, 59/59 records)
    "Map"  x45
    "Waypoint"  x14
data.location  (object, 14/59 records)
data.location.x  (number, 14/59 records)
    numeric range -270.205 .. 140.32 (14 unique)
data.location.y  (number, 14/59 records)
    numeric range -285.829 .. 134.537 (13 unique)
data.location.z  (number, 14/59 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 32 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (6); Unit 4 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Dungeon (3); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 545.41s (p5 7.59s / p95 85727.95s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "DebugMenuStateChanged"  x32
data.isOpened  (bool, 32/32 records)
    false  x32
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 21 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (21)
- **Intervals:** median 26.27s (p5 2.01s / p95 68.38s, n=20)
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "On"  x16
    "Off"  x5
data.floor  (string, 21/21 records)
    "3"  x10
    "4"  x6
    "2"  x3
    "1"  x2
data.machineNumber  (string, 21/21 records)
    "One"  x20
    "Two"  x1
data.machineType  (string, 21/21 records)
    "Condenser"  x10
    "DualChamber_Evaporator"  x4
    "Evaporator"  x4
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 21/21 records)
    "2"  x11
    "1"  x4
    "3"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 20 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (10); Unit 3 Dev (4); Unit 2 Prod (Refactor) (3); Unit 1 Dev (2); Unit 5 Dev (1)
- **Intervals:** median 20.80s (p5 5.24s / p95 224386.72s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "submitAnswerEvent"  x20
data.answerSubmitted  (string, 20/20 records)
    13 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 20/20 records)
    "Unit 4 - Flooding"  x10
    "Unit 3 - Pollution Upstream"  x4
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 5"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 56.72s (p5 0.03s / p95 301933.23s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 17/17 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 4 - Flooding"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowFocusEvent` — 17 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 4 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 1648.26s (p5 23.83s / p95 172139.51s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 84685.66s (p5 868.93s / p95 223948.83s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 13 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (13)
- **Intervals:** median 90.93s (p5 6.88s / p95 223.14s, n=12)
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "ChangeCanister"  x13
data.canisterType  (string, 13/13 records)
    "Clay"  x5
    "Gravel"  x4
    "Bedrock"  x2
    "Sand"  x2
data.floor  (string, 13/13 records)
    "5"  x8
    "4"  x3
    "3"  x2
data.machine  (string, 13/13 records)
    "1"  x12
    "2"  x1
data.row  (string, 13/13 records)
    "TopRow"  x8
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 4 Dev (3); Unit 3 Dev (1)
- **Intervals:** median 85321.06s (p5 523.43s / p95 389107.96s, n=7)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 8/8 records)
    false  x8
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 5 Dev (2); Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 86574.09s (p5 412.91s / p95 586511.22s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "5"  x2
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 2.98s (p5 2.19s / p95 22.35s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records, 3 empty-string)
    ""  x3
    "cameraPlaced"  x3
data.boxId  (string, 6/6 records)
    "0"  x2
    "1"  x2
    "2"  x2
data.soilType  (string, 6/6 records)
    "Clay"  x2
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `SolarStillDesignEvent` — 5 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (5)
- **Intervals:** median 3.18s (p5 2.28s / p95 4.41s, n=4)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x4; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "optionSelected"  x4
    "DesignSubmitted"  x1
data.designSelections  (object, 1/5 records)
data.designSelections.glassRoofTemperature  (string, 1/5 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/5 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/5 records)
    "Tilted Out"  x1
data.featureUsed  (string, 5/5 records)
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 4/5 records)
    "Cold"  x1
    "Covered"  x1
    "Tilted Out"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4)
- **Intervals:** median 4.42s (p5 0.87s / p95 73.13s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (2)
- **Intervals:** median 1.99s (p5 1.99s / p95 1.99s, n=1)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 886.48s (p5 886.48s / p95 886.48s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 1/1 records)
    "running"  x1
data.stack  (string, 1/1 records, 1 empty-string)
    ""  x1
data.type  (string, 1/1 records)
    "unhandled_rejection"  x1
data.unitId  (string, 1/1 records)
    "unit4"  x1
data.workspace  (string, 1/1 records)
    "mhs"  x1
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (47 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (9x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (11x)
- `soilMachine` data.canisterType: "Bedrock" (2x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*