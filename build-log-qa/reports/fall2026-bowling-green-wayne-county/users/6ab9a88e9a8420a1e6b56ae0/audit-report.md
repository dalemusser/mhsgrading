# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae0

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a88e9a8420a1e6b56ae0
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a88e9a8420a1e6b56ae0.jsonl
- **Records:** 17095 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a88e9a8420a1e6b56ae0
- **Time span:** 2026-10-06T13:33:20.958000+00:00 .. 2026-10-18T23:55:32.810000+00:00 (298h 22m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae0\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 17095 records, 11 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 98 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowUnfocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5214 | 30.5 | 1 | 9 | 0 | 2026-10-06T13:33:35.513000+00:00 | 2026-10-18T23:55:32.810000+00:00 | 298h 21m |
| PuzzlePieceVisibleEvent | 4500 | 26.32 | 1 | 4 | 0 | 2026-10-07T13:41:03.377000+00:00 | 2026-10-18T05:08:54.597000+00:00 | 255h 27m |
| PlayerPositionEvent | 2731 | 15.98 | 1 | 9 | 0 | 2026-10-06T13:33:31.807000+00:00 | 2026-10-18T23:55:28.700000+00:00 | 298h 21m |
| DialogueEvent | 2642 | 15.45 | 1 | 9 | 1640 | 2026-10-06T13:33:51.951000+00:00 | 2026-10-18T23:55:27.377000+00:00 | 298h 21m |
| argumentationNodeEvent | 739 | 4.32 | 1 | 5 | 0 | 2026-10-06T13:57:02.826000+00:00 | 2026-10-18T05:34:00.544000+00:00 | 279h 36m |
| ObjectInterEvent | 362 | 2.12 | 1 | 9 | 0 | 2026-10-06T13:39:21.791000+00:00 | 2026-10-18T23:55:32.810000+00:00 | 298h 16m |
| TopographicMapEvent | 183 | 1.07 | 1 | 3 | 0 | 2026-10-07T13:37:18.825000+00:00 | 2026-10-16T13:47:21.643000+00:00 | 216h 10m |
| DaniEvent | 160 | 0.94 | 1 | 4 | 0 | 2026-10-07T13:41:34.687000+00:00 | 2026-10-18T05:16:49.397000+00:00 | 255h 35m |
| Soil Key Puzzle | 104 | 0.61 | 1 | 3 | 0 | 2026-10-07T13:55:30.804000+00:00 | 2026-10-16T13:17:46.915000+00:00 | 215h 22m |
| questEvent | 94 | 0.55 | 1 | 9 | 94 | 2026-10-06T13:33:51.926000+00:00 | 2026-10-18T23:43:32.273000+00:00 | 298h 9m |
| argumentationAnswerEvent | 73 | 0.43 | 1 | 5 | 0 | 2026-10-06T13:58:31.574000+00:00 | 2026-10-18T05:34:02.495000+00:00 | 279h 35m |
| gameWindowFocusEvent | 58 | 0.34 | 1 | 6 | 0 | 2026-10-06T13:33:20.958000+00:00 | 2026-10-18T23:30:07.164000+00:00 | 297h 56m |
| DEBUGMenu | 54 | 0.32 | 1 | 9 | 0 | 2026-10-06T13:33:31.788000+00:00 | 2026-10-18T23:30:07.026000+00:00 | 297h 56m |
| WaterChamberEvent | 46 | 0.27 | 1 | 1 | 0 | 2026-10-18T05:07:23.270000+00:00 | 2026-10-18T05:25:19.873000+00:00 | 17m 56s |
| gameWindowUnfocusEvent | 45 | 0.26 | 1 | 8 | 0 | 2026-10-06T13:59:37.502000+00:00 | 2026-10-18T05:53:27.781000+00:00 | 279h 53m |
| gameStartEvent | 25 | 0.15 | 1 | 1 | 0 | 2026-10-06T13:33:20.959000+00:00 | 2026-10-18T23:30:07.165000+00:00 | 297h 56m |
| argumentationEvent | 18 | 0.11 | 1 | 5 | 0 | 2026-10-06T13:57:47.403000+00:00 | 2026-10-18T05:34:02.528000+00:00 | 279h 36m |
| soilMachine | 10 | 0.06 | 1 | 1 | 0 | 2026-10-16T13:33:53.808000+00:00 | 2026-10-16T13:42:32.003000+00:00 | 8m 38s |
| SolarStillDesignEvent | 9 | 0.05 | 1 | 1 | 0 | 2026-10-18T23:38:43.155000+00:00 | 2026-10-18T23:39:00.821000+00:00 | 17.7s |
| TerasGardenBox | 9 | 0.05 | 1 | 1 | 0 | 2026-10-16T23:40:25.909000+00:00 | 2026-10-16T23:41:52.351000+00:00 | 1m 26s |
| chatEvent | 7 | 0.04 | 1 | 3 | 0 | 2026-10-07T13:42:21.534000+00:00 | 2026-10-18T23:30:19.307000+00:00 | 273h 47m |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-07T13:35:36.209000+00:00 | 2026-10-18T23:55:32.793000+00:00 | 274h 19m |
| argumentationToolEvent | 4 | 0.02 | 1 | 1 | 0 | 2026-10-14T13:56:59.888000+00:00 | 2026-10-14T13:57:04.903000+00:00 | 5.0s |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 389.179s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 134702.035s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.063s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.046s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 8.62s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.092s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 9759.844s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 31.761s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 29.548s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.5x vs baseline. 
  - Observed: 54 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 160 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; p; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
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
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 14.6x vs baseline. 
  - Observed: 73 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,I; A,2,II; A,4,II; A,B,2,II; A,B,C,2,II; A,D,2,II; A,D,B,2,II; A,D,C,2,II; B,1,II; B,2,II; B,3,II; B,4,II; C,2,II; C,3,I; C,3,II; C,4,II; C,D,3,II; D,2,II; D,3,II; D,4,II; D,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.3x vs baseline. 
  - Observed: 739 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 7 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [17-26, 18-21, 18-22, 18-24, 18-25]; [95-83, 95-79, 95-42, 95-41, 95-84] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 25 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 6 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[165] _id=6ac4fa9ade269131f9b1257a ts=2026-10-06T13:41:46.2690000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[223] _id=6ac4fb8cde269131f9b1542c ts=2026-10-06T13:45:48.3520000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[248] _id=6ac4fbc5de269131f9b15fa7 ts=2026-10-06T13:46:44.5770000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[1] _id=6ac4f8a1de269131f9b0c892 ts=2026-10-06T13:33:20.9590000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[437] _id=6ac648f1de269131f9b91a8a ts=2026-10-07T13:28:16.6050000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[665] _id=6ac64afede269131f9b99e2e ts=2026-10-07T13:37:02.3130000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 58 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 58} 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[2] _id=6ac4f8a1de269131f9b0c88e ts=2026-10-06T13:33:20.9580000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[436] _id=6ac648f1de269131f9b91a89 ts=2026-10-07T13:28:16.6050000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[664] _id=6ac64afede269131f9b99e2d ts=2026-10-07T13:37:02.3130000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 45 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 45} 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[434] _id=6ac648f1de269131f9b91a76 ts=2026-10-06T13:59:37.502Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[2090] _id=6ac64e26de269131f9ba01c0 ts=2026-10-07T13:50:29.8430000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[3087] _id=6ac79acade269131f9c03d2b ts=2026-10-07T13:59:49.651Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 1 of 183 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[672] _id=6ac64b10de269131f9b9a106 ts=2026-10-07T13:37:18.8250000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[673] _id=6ac64b1cde269131f9b9a30d ts=2026-10-07T13:37:31.5860000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[674] _id=6ac64b1dde269131f9b9a354 ts=2026-10-07T13:37:33.0750000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5213 | 0.0 | 0.996 | 206.046 | 14.066 | 429604.294 | 0.29 | 283 | 18 |
| PuzzlePieceVisibleEvent | 4499 | 0.0 | 0.063 | 204.417 | 1.949 | 517143.062 | 0.29 | 2049 | 9 |
| PlayerPositionEvent | 2719 | 9.752 | 10.003 | 335.098 | 10.772 | 429605.898 | 0.18 | 0 | 14 |
| DialogueEvent | 2641 | 0.0 | 3.737 | 406.7 | 44.051 | 429657.139 | 0.15 | 767 | 17 |
| argumentationNodeEvent | 738 | 0.018 | 0.706 | 1363.981 | 8.533 | 606302.196 | 0.04 | 75 | 7 |
| ObjectInterEvent | 361 | 0.0 | 11.673 | 2974.435 | 921.908 | 433074.759 | 0.02 | 8 | 19 |
| TopographicMapEvent | 182 | 0.023 | 4.046 | 4275.84 | 783.585 | 430132.755 | 0.01 | 2 | 10 |
| DaniEvent | 159 | 0.005 | 0.226 | 5786.885 | 15.579 | 604439.8 | 0.01 | 8 | 5 |
| Soil Key Puzzle | 103 | 0.117 | 1.473 | 7527.535 | 742.237 | 433071.795 | 0.01 | 0 | 7 |
| questEvent | 93 | 0.001 | 249.129 | 11541.724 | 72193.101 | 430214.658 | 0.01 | 15 | 26 |
| argumentationAnswerEvent | 72 | 0.0 | 8.62 | 13979.596 | 84996.024 | 606350.13 | 0.0 | 1 | 7 |
| gameWindowFocusEvent | 57 | 4.444 | 141.997 | 18817.653 | 85344.19 | 431190.928 | 0.0 | 0 | 21 |
| DEBUGMenu | 53 | 7.973 | 389.179 | 20237.646 | 86003.622 | 431195.357 | 0.0 | 0 | 23 |
| WaterChamberEvent | 45 | 0.392 | 11.434 | 23.925 | 90.995 | 97.456 | 2.51 | 0 | 0 |
| gameWindowUnfocusEvent | 44 | 0.0 | 31.761 | 22900.688 | 91898.481 | 433690.287 | 0.0 | 1 | 11 |
| gameStartEvent | 24 | 130.097 | 9759.844 | 44691.925 | 103957.866 | 431206.145 | 0.0 | 0 | 18 |
| argumentationEvent | 17 | 0.027 | 106.678 | 59210.301 | 207527.918 | 606283.995 | 0.0 | 2 | 7 |
| soilMachine | 9 | 0.574 | 29.548 | 57.577 | 158.688 | 189.225 | 1.04 | 0 | 0 |
| SolarStillDesignEvent | 8 | 0.684 | 1.474 | 2.208 | 5.134 | 5.302 | 27.17 | 0 | 0 |
| TerasGardenBox | 8 | 1.668 | 4.06 | 10.805 | 28.51 | 29.287 | 5.55 | 0 | 0 |
| chatEvent | 6 | 5.269 | 752.288 | 164279.629 | 705588.947 | 919106.05 | 0.0 | 0 | 3 |
| EndOfUnit | 4 | 93203.925 | 134702.035 | 246899.146 | 557184.727 | 624988.59 | 0.0 | 0 | 4 |
| argumentationToolEvent | 3 | 0.689 | 2.092 | 1.672 | 2.22 | 2.234 | 35.89 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 23 group(s), 89 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[441] _id=6ac648fede269131f9b91ca7 ts=2026-10-07T13:28:28.4980000Z == 6ab9a88e9a8420a1e6b56ae0.jsonl[442] _id=6ac648fede269131f9b91ca8 ts=2026-10-07T13:28:28.4980000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[4827] _id=6ace38fede269131f9cefce3 ts=2026-10-13T13:58:20.9870000Z == 6ab9a88e9a8420a1e6b56ae0.jsonl[4828] _id=6ace38fede269131f9cefce4 ts=2026-10-13T13:58:20.9870000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[4835] _id=6ace38fede269131f9cefceb ts=2026-10-13T13:58:20.9880000Z == 6ab9a88e9a8420a1e6b56ae0.jsonl[4836] _id=6ace38fede269131f9cefcec ts=2026-10-13T13:58:20.9880000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 66 group(s), 133 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[830] _id=6ac64c4ade269131f9b9d99a ts=2026-10-07T13:42:32.9340000Z == 6ab9a88e9a8420a1e6b56ae0.jsonl[831] _id=6ac64c4bde269131f9b9d9af ts=2026-10-07T13:42:32.9340000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[827] _id=6ac64c4bde269131f9b9d9c1 ts=2026-10-07T13:42:33.5810000Z == 6ab9a88e9a8420a1e6b56ae0.jsonl[828] _id=6ac64c4bde269131f9b9d9c5 ts=2026-10-07T13:42:33.5810000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[895] _id=6ac64c6ede269131f9b9de0f ts=2026-10-07T13:43:09.4110000Z == 6ab9a88e9a8420a1e6b56ae0.jsonl[896] _id=6ac64c6ede269131f9b9de10 ts=2026-10-07T13:43:09.4110000Z`
- **INFO / Info** `DaniEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 110 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `371ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[2069] _id=6ac64e1dde269131f9ba00d4 ts=2026-10-07T13:50:20.3040000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[2058] _id=6ac64e1dde269131f9ba00da ts=2026-10-07T13:50:20.6750000Z`; `308ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[2082] _id=6ac64e1dde269131f9ba00d7 ts=2026-10-07T13:50:20.5340000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[2084] _id=6ac64e1dde269131f9ba00e6 ts=2026-10-07T13:50:20.8420000Z`; `348ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[2058] _id=6ac64e1dde269131f9ba00da ts=2026-10-07T13:50:20.6750000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[2085] _id=6ac64e1dde269131f9ba00ef ts=2026-10-07T13:50:21.0230000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[113] _id=6ac4fa0ade269131f9b10671 ts=2026-10-06T13:39:21.7910000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[114] _id=6ac4fa0ade269131f9b10677 ts=2026-10-06T13:39:21.7960000Z`; `959ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[16822] _id=6ad558a8de269131f9e8e3a4 ts=2026-10-18T23:39:19.4870000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[16819] _id=6ad558a9de269131f9e8e3af ts=2026-10-18T23:39:20.4460000Z`; `884ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[16831] _id=6ad558adde269131f9e8e3d3 ts=2026-10-18T23:39:24.9910000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[16833] _id=6ad558aede269131f9e8e3d9 ts=2026-10-18T23:39:25.8750000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `964ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[4989] _id=6ace3b03de269131f9cf0065 ts=2026-10-13T14:06:59.1960000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[4991] _id=6ace3b04de269131f9cf0069 ts=2026-10-13T14:07:00.1600000Z`; `537ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[5009] _id=6ace3b7fde269131f9cf00ab ts=2026-10-13T14:09:02.8350000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[5004] _id=6ace3b7fde269131f9cf00af ts=2026-10-13T14:09:03.3720000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `736ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[795] _id=6ac64c13de269131f9b9d30c ts=2026-10-07T13:41:38.8190000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[797] _id=6ac64c14de269131f9b9d330 ts=2026-10-07T13:41:39.5550000Z`; `653ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[2688] _id=6ac64eb4de269131f9ba1574 ts=2026-10-07T13:52:51.9400000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[2682] _id=6ac64eb5de269131f9ba1591 ts=2026-10-07T13:52:52.5930000Z`; `389ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[4643] _id=6ace31e8de269131f9cea61a ts=2026-10-13T13:28:07.6130000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[4647] _id=6ace31e8de269131f9cea61c ts=2026-10-13T13:28:08.0020000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `899ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7195] _id=6acf8a78de269131f9d3b666 ts=2026-10-14T13:58:15.5820000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[7196] _id=6acf8a79de269131f9d3b6a5 ts=2026-10-14T13:58:16.4810000Z`; `179ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7196] _id=6acf8a79de269131f9d3b6a5 ts=2026-10-14T13:58:16.4810000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[7193] _id=6acf8a79de269131f9d3b6ba ts=2026-10-14T13:58:16.6600000Z`; `165ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7193] _id=6acf8a79de269131f9d3b6ba ts=2026-10-14T13:58:16.6600000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[7197] _id=6acf8a79de269131f9d3b6c4 ts=2026-10-14T13:58:16.8250000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `35ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[8653] _id=6ad0d7dade269131f9dad7d7 ts=2026-10-15T13:40:42.3770000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[8656] _id=6ad0d7dade269131f9dad7da ts=2026-10-15T13:40:42.4120000Z`; `27ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[15230] _id=6ad2b4dfde269131f9e842b8 ts=2026-10-16T23:35:59.3070000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[15248] _id=6ad2b4dfde269131f9e842bb ts=2026-10-16T23:35:59.3340000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 54 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `429ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[516] _id=6ac649c0de269131f9b94d40 ts=2026-10-07T13:31:43.5710000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[517] _id=6ac649c0de269131f9b94d5e ts=2026-10-07T13:31:44.0000000Z`; `620ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[519] _id=6ac649c0de269131f9b94d45 ts=2026-10-07T13:31:43.6580000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[520] _id=6ac649c0de269131f9b94d7e ts=2026-10-07T13:31:44.2780000Z`; `793ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[534] _id=6ac649c8de269131f9b94f8a ts=2026-10-07T13:31:51.7790000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[536] _id=6ac649c9de269131f9b94fc0 ts=2026-10-07T13:31:52.5720000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `689ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7124] _id=6acf8a2fde269131f9d3a96a ts=2026-10-14T13:57:02.1220000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[7125] _id=6acf8a2fde269131f9d3a980 ts=2026-10-14T13:57:02.8110000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7554] _id=6acfd56fde269131f9d886a0 ts=2026-10-14T19:18:05.6980000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[7559] _id=6ad0d271de269131f9da5a8e ts=2026-10-14T19:18:05.698Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[16621] _id=6ad45a92de269131f9e89cfa ts=2026-10-18T05:35:13.8340000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[16622] _id=6ad45a92de269131f9e89cfb ts=2026-10-18T05:35:13.8350000Z`; `6ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[16698] _id=6ad5568fde269131f9e8de3f ts=2026-10-18T23:30:22.6580000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[16699] _id=6ad5568fde269131f9e8de40 ts=2026-10-18T23:30:22.6640000Z`; `4ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[16928] _id=6ad5591dde269131f9e8e595 ts=2026-10-18T23:41:17.0960000Z ~ 6ab9a88e9a8420a1e6b56ae0.jsonl[16934] _id=6ad5591dde269131f9e8e597 ts=2026-10-18T23:41:17.1000000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3127] _id=6ac79b5cde269131f9c04ebc ts=2026-10-08T13:32:11.4300000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4513] _id=6ace2fb7de269131f9ce92cc ts=2026-10-13T13:18:46.7870000Z; 29h 23m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15260] _id=6ad2b52ade269131f9e842e9 ts=2026-10-16T23:37:13.0320000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15602] _id=6ad4527cde269131f9e88f47 ts=2026-10-18T05:00:44.1800000Z; 23h 54m: 6ab9a88e9a8420a1e6b56ae0.jsonl[7] _id=6ac4f8acde269131f9b0ca09 ts=2026-10-06T13:33:31.7880000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[435] _id=6ac648f1de269131f9b91a88 ts=2026-10-07T13:28:16.4510000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 167h 53m 
  - Evidence: 167h 53m: 6ab9a88e9a8420a1e6b56ae0.jsonl[2696] _id=6ac64ebede269131f9ba173d ts=2026-10-07T13:53:02.2000000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[6694] _id=6acf87d6de269131f9d35e4f ts=2026-10-14T13:47:02.0000000Z; 61h 14m: 6ab9a88e9a8420a1e6b56ae0.jsonl[9741] _id=6ad0f91ade269131f9dd19b9 ts=2026-10-15T16:02:33.9450000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16109] _id=6ad4563fde269131f9e89751 ts=2026-10-18T05:16:46.7330000Z; 18h 7m: 6ab9a88e9a8420a1e6b56ae0.jsonl[7466] _id=6acfd3e3de269131f9d83ed4 ts=2026-10-14T19:11:29.9510000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7602] _id=6ad0d2dcde269131f9da6120 ts=2026-10-15T13:19:24.0320000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[2043] _id=6ac64e16de269131f9ba002b ts=2026-10-07T13:50:14.2700000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[2044] _id=6ac64e16de269131f9ba0030 ts=2026-10-07T13:50:14.2750000Z; 6ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[9738] _id=6ad0f917de269131f9dd196e ts=2026-10-15T16:02:31.2800000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[9739] _id=6ad0f917de269131f9dd1972 ts=2026-10-15T16:02:31.2860000Z; 7ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7603] _id=6ad0d2dfde269131f9da614c ts=2026-10-15T13:19:27.5160000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7604] _id=6ad0d2dfde269131f9da614e ts=2026-10-15T13:19:27.5230000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4500] _id=6ac7a198de269131f9c15845 ts=2026-10-08T13:58:47.7310000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4537] _id=6ace2ff1de269131f9ce956e ts=2026-10-13T13:19:44.8700000Z; 29h 8m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15594] _id=6ad2b8d2de269131f9e8456a ts=2026-10-16T23:52:49.9830000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15618] _id=6ad45293de269131f9e88f90 ts=2026-10-18T05:01:07.1690000Z; 23h 31m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3084] _id=6ac6504bde269131f9ba3be5 ts=2026-10-07T13:59:38.5660000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[3117] _id=6ac79b25de269131f9c0482a ts=2026-10-08T13:31:16.3270000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 767 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[13831] _id=6ad22de3de269131f9e44a8d ts=2026-10-16T14:00:01.1680000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13890] _id=6ad251dcde269131f9e5eb23 ts=2026-10-16T14:00:01.168Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[13836] _id=6ad22daade269131f9e4478b ts=2026-10-16T13:59:05.9370000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13837] _id=6ad22daade269131f9e4478c ts=2026-10-16T13:59:05.9370000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[13857] _id=6ad22dbcde269131f9e448b7 ts=2026-10-16T13:59:24.2000000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13858] _id=6ad22dbcde269131f9e448b8 ts=2026-10-16T13:59:24.2000000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 173h 36m 
  - Evidence: 173h 36m: 6ab9a88e9a8420a1e6b56ae0.jsonl[663] _id=6ac64aa8de269131f9b98c24 ts=2026-10-07T13:35:36.2090000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7482] _id=6acfd405de269131f9d844d6 ts=2026-10-14T19:12:04.7990000Z; 48h 2m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15589] _id=6ad2b8d2de269131f9e84568 ts=2026-10-16T23:52:49.9560000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[17094] _id=6ad55c75de269131f9e8ecd7 ts=2026-10-18T23:55:32.7930000Z; 26h 47m: 6ab9a88e9a8420a1e6b56ae0.jsonl[11520] _id=6ad14019de269131f9e154db ts=2026-10-15T21:05:28.7240000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15589] _id=6ad2b8d2de269131f9e84568 ts=2026-10-16T23:52:49.9560000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4509] _id=6ac7a1a6de269131f9c15936 ts=2026-10-08T13:59:01.3430000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4517] _id=6ace2fcbde269131f9ce942f ts=2026-10-13T13:19:05.6370000Z; 29h 9m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15580] _id=6ad2b8b6de269131f9e84552 ts=2026-10-16T23:52:21.7730000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15628] _id=6ad452b0de269131f9e88fc2 ts=2026-10-18T05:01:36.6740000Z; 23h 33m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3037] _id=6ac64f8dde269131f9ba2efb ts=2026-10-07T13:56:28.7060000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[3098] _id=6ac79af1de269131f9c041bc ts=2026-10-08T13:30:24.2560000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 283 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[10406] _id=6ad1027ade269131f9ddc2e1 ts=2026-10-15T16:42:33.9740000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[10407] _id=6ad1027ade269131f9ddc2e2 ts=2026-10-15T16:42:33.9740000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[10407] _id=6ad1027ade269131f9ddc2e2 ts=2026-10-15T16:42:33.9740000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[10408] _id=6ad1027ade269131f9ddc2e3 ts=2026-10-15T16:42:33.9740000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[10885] _id=6ad1052ede269131f9de064a ts=2026-10-15T16:54:05.5420000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[10886] _id=6ad1052ede269131f9de064b ts=2026-10-15T16:54:05.5420000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 120h 17m 
  - Evidence: 120h 17m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4156] _id=6ac79d9dde269131f9c0b90c ts=2026-10-08T13:41:48.3490000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4920] _id=6ace394fde269131f9ceffb1 ts=2026-10-13T13:59:43.1080000Z; 29h 12m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15582] _id=6ad2b8bade269131f9e84557 ts=2026-10-16T23:52:26.5090000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15708] _id=6ad45392de269131f9e891ef ts=2026-10-18T05:05:22.7630000Z; 23h 38m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3005] _id=6ac64f53de269131f9ba2bdf ts=2026-10-07T13:55:30.8100000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[3163] _id=6ac79bb8de269131f9c0604c ts=2026-10-08T13:33:44.1030000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[13598] _id=6ad22c52de269131f9e424c7 ts=2026-10-16T13:53:22.0230000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13599] _id=6ad22c52de269131f9e424c8 ts=2026-10-16T13:53:22.0230000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[13697] _id=6ad22cadde269131f9e42f6e ts=2026-10-16T13:54:52.7660000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13698] _id=6ad22cadde269131f9e42f6f ts=2026-10-16T13:54:52.7660000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[14025] _id=6ad25675de269131f9e634e4 ts=2026-10-16T16:53:08.9470000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[14026] _id=6ad25675de269131f9e634e5 ts=2026-10-16T16:53:08.9470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4504] _id=6ac7a19fde269131f9c158bf ts=2026-10-08T13:58:54.3210000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4516] _id=6ace2fcbde269131f9ce942e ts=2026-10-13T13:19:00.2190000Z; 23h 30m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3085] _id=6ac65052de269131f9ba3c51 ts=2026-10-07T13:59:45.8300000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[3096] _id=6ac79aefde269131f9c0417b ts=2026-10-08T13:30:18.2820000Z; 23h 28m: 6ab9a88e9a8420a1e6b56ae0.jsonl[431] _id=6ac4fec0de269131f9b2335d ts=2026-10-06T13:59:28.0460000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[439] _id=6ac648fede269131f9b91ca5 ts=2026-10-07T13:28:27.2070000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 39m 
  - Evidence: 143h 39m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4128] _id=6ac79d62de269131f9c0af0e ts=2026-10-08T13:40:48.6200000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[5226] _id=6acf8179de269131f9d2e827 ts=2026-10-14T13:19:51.6820000Z; 39h 14m: 6ab9a88e9a8420a1e6b56ae0.jsonl[13395] _id=6ad22ac2de269131f9e3f532 ts=2026-10-16T13:46:39.9070000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15603] _id=6ad4528fde269131f9e88f6b ts=2026-10-18T05:01:01.6960000Z; 24h 17m: 6ab9a88e9a8420a1e6b56ae0.jsonl[6319] _id=6acf838cde269131f9d315ec ts=2026-10-14T13:28:42.3130000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[8863] _id=6ad0d922de269131f9db04e4 ts=2026-10-15T13:46:09.1640000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2049 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[1000] _id=6ac64cccde269131f9b9e5c6 ts=2026-10-07T13:42:48.7930000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[983] _id=6ac64cccde269131f9b9e5c8 ts=2026-10-07T13:42:48.7930000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[1001] _id=6ac64cccde269131f9b9e5cc ts=2026-10-07T13:42:51.4640000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[984] _id=6ac64cccde269131f9b9e5ce ts=2026-10-07T13:42:51.4640000Z; 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[1002] _id=6ac64cccde269131f9b9e5d0 ts=2026-10-07T13:42:51.4640000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[998] _id=6ac64cccde269131f9b9e5d4 ts=2026-10-07T13:42:51.4640000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 17m 
  - Evidence: 120h 17m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4157] _id=6ac79da0de269131f9c0b9ce ts=2026-10-08T13:41:51.3080000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4910] _id=6ace394fde269131f9ceffaf ts=2026-10-13T13:59:43.1030000Z; 24h 1m: 6ab9a88e9a8420a1e6b56ae0.jsonl[6592] _id=6acf86ebde269131f9d34b3d ts=2026-10-14T13:43:06.7620000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[8806] _id=6ad0d8d4de269131f9dafb57 ts=2026-10-15T13:44:52.1820000Z; 23h 46m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3006] _id=6ac64f56de269131f9ba2c20 ts=2026-10-07T13:55:33.7610000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4149] _id=6ac79d9dde269131f9c0b8fc ts=2026-10-08T13:41:48.3450000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 119h 28m 
  - Evidence: 119h 28m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4507] _id=6ac7a1a6de269131f9c15938 ts=2026-10-08T13:59:01.3550000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4641] _id=6ace31dade269131f9cea5b0 ts=2026-10-13T13:27:54.1100000Z; 24h 12m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4651] _id=6ace31efde269131f9cea674 ts=2026-10-13T13:28:15.2640000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[6546] _id=6acf864ede269131f9d3430b ts=2026-10-14T13:40:29.8640000Z; 23h 41m: 6ab9a88e9a8420a1e6b56ae0.jsonl[2693] _id=6ac64ebcde269131f9ba16ab ts=2026-10-07T13:52:59.6730000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[3176] _id=6ac79bd9de269131f9c06662 ts=2026-10-08T13:34:16.1780000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.038s shown 
  - Evidence: 23ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[4308] _id=6ac79f6cde269131f9c108ba ts=2026-10-08T13:49:31.9990000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4312] _id=6ac79f6cde269131f9c108be ts=2026-10-08T13:49:32.0220000Z; 38ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[4307] _id=6ac79f6cde269131f9c108b4 ts=2026-10-08T13:49:31.9610000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4308] _id=6ac79f6cde269131f9c108ba ts=2026-10-08T13:49:31.9990000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 168h 25m 
  - Evidence: 168h 25m: 6ab9a88e9a8420a1e6b56ae0.jsonl[525] _id=6ac649d9de269131f9b9544b ts=2026-10-07T13:32:08.5910000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7177] _id=6acf8a67de269131f9d3b26b ts=2026-10-14T13:57:58.7210000Z; 29h 57m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15229] _id=6ad2b4dfde269131f9e842b6 ts=2026-10-16T23:35:59.2870000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16557] _id=6ad45a37de269131f9e89c70 ts=2026-10-18T05:33:43.2720000Z; 24h 18m: 6ab9a88e9a8420a1e6b56ae0.jsonl[8652] _id=6ad0d7dade269131f9dad7d5 ts=2026-10-15T13:40:42.3510000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13813] _id=6ad22daade269131f9e44789 ts=2026-10-16T13:59:05.9170000Z
- **INFO / Info** `argumentationAnswerEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[13832] _id=6ad22de3de269131f9e44a8e ts=2026-10-16T14:00:02.4580000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13891] _id=6ad251dcde269131f9e5eb24 ts=2026-10-16T14:00:02.458Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 168h 24m 
  - Evidence: 168h 24m: 6ab9a88e9a8420a1e6b56ae0.jsonl[521] _id=6ac649d9de269131f9b95452 ts=2026-10-07T13:32:08.6120000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7116] _id=6acf8a25de269131f9d3a775 ts=2026-10-14T13:56:52.6070000Z; 29h 57m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15248] _id=6ad2b4dfde269131f9e842bb ts=2026-10-16T23:35:59.3340000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16525] _id=6ad45a1ede269131f9e89c43 ts=2026-10-18T05:33:18.2330000Z; 24h 16m: 6ab9a88e9a8420a1e6b56ae0.jsonl[8656] _id=6ad0d7dade269131f9dad7da ts=2026-10-15T13:40:42.4120000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13768] _id=6ad22d50de269131f9e43ec8 ts=2026-10-16T13:57:36.2230000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.027s..0.035s shown 
  - Evidence: 27ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[15230] _id=6ad2b4dfde269131f9e842b8 ts=2026-10-16T23:35:59.3070000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15248] _id=6ad2b4dfde269131f9e842bb ts=2026-10-16T23:35:59.3340000Z; 35ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[8653] _id=6ad0d7dade269131f9dad7d7 ts=2026-10-15T13:40:42.3770000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[8656] _id=6ad0d7dade269131f9dad7da ts=2026-10-15T13:40:42.4120000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 168h 25m 
  - Evidence: 168h 25m: 6ab9a88e9a8420a1e6b56ae0.jsonl[495] _id=6ac649d6de269131f9b953c8 ts=2026-10-07T13:32:05.8860000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7128] _id=6acf8a35de269131f9d3aa4b ts=2026-10-14T13:57:08.0820000Z; 29h 57m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15228] _id=6ad2b4ddde269131f9e842b4 ts=2026-10-16T23:35:57.6480000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16538] _id=6ad45a21de269131f9e89c4a ts=2026-10-18T05:33:21.4630000Z; 24h 16m: 6ab9a88e9a8420a1e6b56ae0.jsonl[8643] _id=6ad0d7d5de269131f9dad739 ts=2026-10-15T13:40:36.8620000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[13751] _id=6ad22d3fde269131f9e43ce9 ts=2026-10-16T13:57:18.8730000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 75 interval(s) ≤ 0.018s..0.018s shown 
  - Evidence: 18ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[14896] _id=6ad2b37fde269131f9e83d6e ts=2026-10-16T23:30:07.6800000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[14897] _id=6ad2b37fde269131f9e83d70 ts=2026-10-16T23:30:07.6980000Z; 18ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[14948] _id=6ad2b3bede269131f9e83e24 ts=2026-10-16T23:31:10.0890000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[14962] _id=6ad2b3bede269131f9e83e26 ts=2026-10-16T23:31:10.1070000Z; 18ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[15093] _id=6ad2b443de269131f9e841a0 ts=2026-10-16T23:33:22.8490000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15094] _id=6ad2b443de269131f9e841a2 ts=2026-10-16T23:33:22.8670000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 255h 18m 
  - Evidence: 255h 18m: 6ab9a88e9a8420a1e6b56ae0.jsonl[819] _id=6ac64c43de269131f9b9d8f9 ts=2026-10-07T13:42:26.8030000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15597] _id=6ad45285de269131f9e88f58 ts=2026-10-18T05:00:52.8530000Z; 18h 3m: 6ab9a88e9a8420a1e6b56ae0.jsonl[16366] _id=6ad4587dde269131f9e89a49 ts=2026-10-18T05:26:21.6710000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16694] _id=6ad5568bde269131f9e8de3a ts=2026-10-18T23:30:19.3070000Z; 15m 56s: 6ab9a88e9a8420a1e6b56ae0.jsonl[15597] _id=6ad45285de269131f9e88f58 ts=2026-10-18T05:00:52.8530000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16111] _id=6ad45641de269131f9e8975c ts=2026-10-18T05:16:49.7040000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3125] _id=6ac79b51de269131f9c04cd6 ts=2026-10-08T13:32:00.9920000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4512] _id=6ace2fb7de269131f9ce92d8 ts=2026-10-13T13:18:47.1370000Z; 29h 45m: 6ab9a88e9a8420a1e6b56ae0.jsonl[14512] _id=6ad2b016de269131f9e839b6 ts=2026-10-16T23:15:34.3120000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15596] _id=6ad4527cde269131f9e88f4a ts=2026-10-18T05:00:44.3350000Z; 23h 54m: 6ab9a88e9a8420a1e6b56ae0.jsonl[1] _id=6ac4f8a1de269131f9b0c892 ts=2026-10-06T13:33:20.9590000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[437] _id=6ac648f1de269131f9b91a8a ts=2026-10-07T13:28:16.6050000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3130] _id=6ac79b61de269131f9c04f89 ts=2026-10-08T13:32:16.2090000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4511] _id=6ace2fb7de269131f9ce92d7 ts=2026-10-13T13:18:47.1370000Z; 29h 38m: 6ab9a88e9a8420a1e6b56ae0.jsonl[14487] _id=6ad2b190de269131f9e83b46 ts=2026-10-16T23:21:52.4290000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15595] _id=6ad4527cde269131f9e88f49 ts=2026-10-18T05:00:44.3350000Z; 23h 54m: 6ab9a88e9a8420a1e6b56ae0.jsonl[2] _id=6ac4f8a1de269131f9b0c88e ts=2026-10-06T13:33:20.9580000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[436] _id=6ac648f1de269131f9b91a89 ts=2026-10-07T13:28:16.6050000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 120h 28m 
  - Evidence: 120h 28m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3129] _id=6ac79b61de269131f9c04f88 ts=2026-10-08T13:32:16.2020000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4925] _id=6ace3a80de269131f9cefff9 ts=2026-10-13T14:00:26.489Z; 30h 31m: 6ab9a88e9a8420a1e6b56ae0.jsonl[14486] _id=6ad2b18fde269131f9e83b44 ts=2026-10-16T23:21:50.8330000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16689] _id=6ad5567fde269131f9e8de24 ts=2026-10-18T05:53:27.781Z; 25h 49m: 6ab9a88e9a8420a1e6b56ae0.jsonl[5014] _id=6acf7fbbde269131f9d2d06f ts=2026-10-13T14:09:18.886Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7320] _id=6acfa6b5de269131f9d50b41 ts=2026-10-14T15:58:44.3330000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[7554] _id=6acfd56fde269131f9d886a0 ts=2026-10-14T19:18:05.6980000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[7559] _id=6ad0d271de269131f9da5a8e ts=2026-10-14T19:18:05.698Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 119h 30m 
  - Evidence: 119h 30m: 6ab9a88e9a8420a1e6b56ae0.jsonl[4296] _id=6ac79f43de269131f9c100e2 ts=2026-10-08T13:48:51.0220000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[4519] _id=6ace2fcbde269131f9ce9431 ts=2026-10-13T13:19:05.6800000Z; 29h 8m: 6ab9a88e9a8420a1e6b56ae0.jsonl[15586] _id=6ad2b8bfde269131f9e8455e ts=2026-10-16T23:52:31.4840000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[15601] _id=6ad4528ade269131f9e88f63 ts=2026-10-18T05:00:57.4660000Z; 23h 34m: 6ab9a88e9a8420a1e6b56ae0.jsonl[3026] _id=6ac64f76de269131f9ba2dca ts=2026-10-07T13:56:06.1810000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[3097] _id=6ac79aefde269131f9c0417c ts=2026-10-08T13:30:20.5620000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[16621] _id=6ad45a92de269131f9e89cfa ts=2026-10-18T05:35:13.8340000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[16622] _id=6ad45a92de269131f9e89cfb ts=2026-10-18T05:35:13.8350000Z; 1ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[458] _id=6ac64917de269131f9b922df ts=2026-10-07T13:28:54.8330000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[459] _id=6ac64917de269131f9b922e0 ts=2026-10-07T13:28:54.8340000Z; 3ms: 6ab9a88e9a8420a1e6b56ae0.jsonl[373] _id=6ac4fde1de269131f9b1f42b ts=2026-10-06T13:55:44.4430000Z -> 6ab9a88e9a8420a1e6b56ae0.jsonl[377] _id=6ac4fde1de269131f9b1f456 ts=2026-10-06T13:55:44.4460000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[369] _id=6ac4fdd2de269131f9b1efd4 ts=2026-10-06T13:55:30.3350000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[6238] _id=6acf8376de269131f9d31391 ts=2026-10-14T13:28:21.2440000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[6421] _id=6acf84dede269131f9d32e9f ts=2026-10-14T13:34:21.3110000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[8656] _id=6ad0d7dade269131f9dad7da ts=2026-10-15T13:40:42.4120000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[15597] _id=6ad45285de269131f9e88f58 ts=2026-10-18T05:00:52.8530000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[16366] _id=6ad4587dde269131f9e89a49 ts=2026-10-18T05:26:21.6710000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[16694] _id=6ad5568bde269131f9e8de3a ts=2026-10-18T23:30:19.3070000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[2088] _id=6ac64e1fde269131f9ba0139 ts=?`; `6ab9a88e9a8420a1e6b56ae0.jsonl[3126] _id=6ac79b63de269131f9c04fc1 ts=?`; `6ab9a88e9a8420a1e6b56ae0.jsonl[5019] _id=6acf7fe9de269131f9d2d3bf ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 62 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[5332] _id=6acf821fde269131f9d2f42e ts=2026-10-14T13:22:36.4880000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[5360] _id=6acf8220de269131f9d2f445 ts=2026-10-14T13:22:36.7060000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[5361] _id=6acf8220de269131f9d2f446 ts=2026-10-14T13:22:36.7060000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 387 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[830] _id=6ac64c4ade269131f9b9d99a ts=2026-10-07T13:42:32.9340000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[831] _id=6ac64c4bde269131f9b9d9af ts=2026-10-07T13:42:32.9340000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[832] _id=6ac64c4bde269131f9b9d9b0 ts=2026-10-07T13:42:32.9550000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[4968] _id=6ace3ae7de269131f9cf004f ts=2026-10-13T14:06:31.0580000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[5204] _id=6acf8140de269131f9d2e3e9 ts=2026-10-14T13:18:55.2370000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[14327] _id=6ad2585cde269131f9e65680 ts=2026-10-16T17:01:16.0690000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[14750] _id=6ad2b2a6de269131f9e83bb9 ts=2026-10-16T23:26:30.6200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[7124] _id=6acf8a2fde269131f9d3a96a ts=2026-10-14T13:57:02.1220000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[7125] _id=6acf8a2fde269131f9d3a980 ts=2026-10-14T13:57:02.8110000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[7126] _id=6acf8a31de269131f9d3a9c1 ts=2026-10-14T13:57:04.9030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 507 start, 495 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 24 unmatched 'BecameVisible' (totals: 1448 open, 1424 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'Started' (totals: 7 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 9 open, 9 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 4 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'questActiveEvent' (totals: 60 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 418 of 17091 adjacent _id pairs reverse in client time; worst 215.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a88e9a8420a1e6b56ae0.jsonl[950] _id=6ac64cc7de269131f9b9e52d ts=2026-10-07T13:44:38.6340000Z`; `6ab9a88e9a8420a1e6b56ae0.jsonl[965] _id=6ac64cc8de269131f9b9e53a ts=2026-10-07T13:41:03.3770000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.64s, min -84597.28s, max -0.17s over 17092 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a88e9a8420a1e6b56ae0\coverage.yaml

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

### `InputEvent` — 5214 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1569); Unit 3 Dev (1087); Unit 3 Dungeon Dev (795); Unit 4 Dev - Dungeon (475); Unit 4 Dev - Anderson Base (447); Unit 4 Dev (278); Unit 5 Dev - Dungeon (252); Unit 5 Dev (157); Unit 1 Dev (154)
- **Intervals:** median 1.00s (p5 0.04s / p95 14.07s, n=5213)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5214/5214 records)
    "pressed"  x5214
data.actionType  (string, 5214/5214 records)
    "Move"  x3491
    "Interact"  x547
    "Jump"  x498
    "Pause"  x145
    "Hoverboard"  x142
    "Ascend"  x123
    "Sprint"  x107
    "Map"  x104
    "Descend"  x32
    "ToggleDebug"  x19
    "SkipCinematic"  x6
data.key  (string, 5214/5214 records, 42 empty-string)
    20 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5214/5214 records)
    "Player"  x3885
    "Drone"  x1329
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4500 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3204); Unit 4 Dev (732); Unit 3 Dungeon Dev (368); Unit 5 Dev - Dungeon (196)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.95s, n=4499)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4500/4500 records)
    "BecameVisible"  x1448
    "BecameInvisible"  x1424
    "BecameCameraCentered"  x814
    "BecameCameraUncentered"  x814
data.pieceId  (string, 4500/4500 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4500/4500 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2731 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (740); Unit 3 Dungeon Dev (411); Unit 4 Dev - Anderson Base (351); Unit 3 Dev (315); Unit 5 Dev (234); Unit 4 Dev (204); Unit 1 Dev (199); Unit 5 Dev - Dungeon (147); Unit 4 Dev - Dungeon (130)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.77s, n=2719)
- **Fields under `data`:**

```text
data.position  (object, 2731/2731 records)
data.position.x  (number, 2731/2731 records)
    numeric range -730.762 .. 1556.08 (853 unique)
data.position.y  (number, 2731/2731 records)
    numeric range -115.127 .. 222.005 (564 unique)
data.position.z  (number, 2731/2731 records)
    numeric range -1120.76 .. 1825.15 (852 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2642 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (737); Unit 3 Dev (345); Unit 3 Dungeon Dev (341); Unit 4 Dev - Anderson Base (291); Unit 5 Dev (271); Unit 4 Dev (270); Unit 1 Dev (210); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (78)
- **eventKey:** present on 1640 of 2642 records
- **Intervals:** median 3.74s (p5 0.00s / p95 44.05s, n=2641)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1640; [conversationId, dialogueEventType] x1002
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2642/2642 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2642/2642 records)
    "DialogueNodeEvent"  x1640
    "DialogueStartEvent"  x507
    "DialogueFinishEvent"  x495
data.nodeId  (number, 1640/2642 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 739 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (541); Unit 3 Dev (65); Unit 2 Prod (Refactor) (57); Unit 1 Dev (56); Unit 5 Dev (20)
- **Intervals:** median 0.71s (p5 0.04s / p95 8.53s, n=738)
- **Fields under `data`:**

```text
data.actionType  (string, 739/739 records)
    "argumentationNodeHoverEnd"  x315
    "argumentationNodeHoverStart"  x315
    "argumentationNodeAdd"  x69
    "argumentationNodeRemove"  x40
data.argumentationTitle  (string, 739/739 records)
    "Unit 4 - Flooding"  x541
    "Unit 3 - Pollution Upstream"  x65
    "Unit 2 – Watershed"  x57
    "Unit 1 - Argumentation Tutorial"  x29
    "Unit 1 - Freshwater"  x27
    "Unit 5"  x20
data.nodeName  (string, 739/739 records)
    "B"  x123
    "C"  x99
    "1"  x80
    "4"  x71
    "A"  x70
    "3"  x65
    "2"  x64
    "D"  x60
    "I"  x51
    "II"  x51
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 362 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (85); Unit 2 Prod (Refactor) (84); Unit 4 Dev - Dungeon (66); Unit 5 Dev (34); Unit 4 Dev - Anderson Base (27); Unit 4 Dev (21); Unit 5 Dev - Dungeon (20); Unit 3 Dev (14); Unit 1 Dev (11)
- **Intervals:** median 11.67s (p5 0.20s / p95 921.91s, n=361)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 362/362 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 362/362 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 183 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (117); Unit 2 Prod (Refactor) (64); Unit 4 Dev (2)
- **Intervals:** median 4.05s (p5 0.51s / p95 783.59s, n=182)
- **`data` key-set variants:** [actionType, featureUsed] x160; [actionType, featureUsed, location] x22; [actionType, featureUsed, legendName] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 183/183 records)
    "MapCloseEvent"  x80
    "MapOpenEvent"  x80
    "WaypointMoveEvent"  x14
    "WaypointSetEvent"  x8
    "Selected"  x1
data.featureUsed  (string, 183/183 records)
    "Map"  x160
    "Waypoint"  x22
    "Legend"  x1
data.legendName  (string, 1/183 records)
    "0 ft"  x1
data.location  (object, 22/183 records)
data.location.x  (number, 22/183 records)
    numeric range -355.965 .. 576.151 (17 unique)
data.location.y  (number, 22/183 records)
    numeric range -200.205 .. 192.179 (19 unique)
data.location.z  (number, 22/183 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DaniEvent` — 160 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (146); Unit 3 Dev (6); Unit 3 Dungeon Dev (6); Unit 5 Dev - Dungeon (2)
- **Intervals:** median 0.23s (p5 0.07s / p95 15.58s, n=159)
- **Fields under `data`:**

```text
data.actionType  (string, 160/160 records)
    "Close"  x80
    "Open"  x80
data.toolName  (string, 160/160 records, 152 empty-string)
    ""  x152
    "Settings"  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `Soil Key Puzzle` — 104 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (72); Unit 3 Dev (20); Unit 4 Dev (12)
- **Intervals:** median 1.47s (p5 0.16s / p95 742.24s, n=103)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x92; [Soil Key Puzzle Status, Unit] x12
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/104 records)
    "Started"  x7
    "Finished"  x5
data.Unit  (string, 12/104 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 92/104 records)
    "RightDrag"  x49
    "LeftDrag"  x43
data.currentSoilType  (string, 92/104 records)
    "CLAY"  x17
    "CLAYROCK"  x16
    "CLAYSAND"  x16
    "SAND"  x16
    "SANDGRAVEL"  x14
    "BEDROCK"  x7
    "GRAVEL"  x6
data.isCorrectSelection  (string, 92/104 records)
    "false"  x74
    "true"  x18
data.waterLevelStatus  (string, 92/104 records)
    "TooHigh"  x55
    "TooLow"  x19
    "Proper"  x18
data.waterRetentionChange  (string, 92/104 records)
    "Increase"  x47
    "Decrease"  x27
    "NoChange"  x18
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 94 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (25); Unit 1 Dev (15); Unit 3 Dev (12); Unit 4 Dev - Dungeon (9); Unit 5 Dev (9); Unit 4 Dev (8); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (5); Unit 4 Dev - Anderson Base (4)
- **eventKey:** present on 94 of 94 records
- **Intervals:** median 249.13s (p5 0.01s / p95 72193.10s, n=93)
- **`data` key-set variants:** [questEventType, questID, questName] x60; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Fields under `data`:**

```text
data.questEventType  (string, 94/94 records)
    "questActiveEvent"  x60
    "questFinishEvent"  x34
data.questID  (string, 94/94 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 94/94 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/94 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 73 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (58); Unit 2 Prod (Refactor) (8); Unit 1 Dev (3); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 8.62s (p5 0.17s / p95 84996.02s, n=72)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 73/73 records)
    "submitAnswerEvent"  x73
data.answerSubmitted  (string, 73/73 records)
    25 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 73/73 records)
    "Unit 4 - Flooding"  x58
    "Unit 2 – Watershed"  x8
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 58 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (28); Unit 2 Prod (Refactor) (21); Transition (5); Unit 3 Dungeon Dev (2); Unit 3 Dev (1); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 142.00s (p5 4.88s / p95 85344.19s, n=57)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 58/58 records)
    true  x58
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 54 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (24); Unit 2 Prod (Refactor) (11); Unit 3 Dev (5); Unit 4 Dev (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3); Unit 1 Dev (2); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 389.18s (p5 10.74s / p95 86003.62s, n=53)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "DebugMenuStateChanged"  x54
data.isOpened  (bool, 54/54 records)
    false  x54
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 46 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (46)
- **Intervals:** median 11.43s (p5 1.37s / p95 91.00s, n=45)
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "On"  x29
    "Off"  x17
data.floor  (string, 46/46 records)
    "3"  x34
    "4"  x7
    "2"  x3
    "1"  x2
data.machineNumber  (string, 46/46 records)
    "One"  x43
    "Two"  x3
data.machineType  (string, 46/46 records)
    "Condenser"  x21
    "DualChamber_Condenser"  x11
    "DualChamber_Evaporator"  x6
    "Evaporator"  x6
    "VentSwitch"  x2
data.room  (string, 46/46 records)
    "2"  x32
    "3"  x6
    "1"  x4
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 45 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (26); Transition (5); Unit 3 Dev (4); MainMenu (3); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 31.76s (p5 3.94s / p95 91898.48s, n=44)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 45/45 records)
    false  x45
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 25 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (25)
- **Intervals:** median 9759.84s (p5 161.11s / p95 103957.87s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6); Unit 4 Dev - Anderson Base (5); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 106.68s (p5 0.03s / p95 207527.92s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x9
data.argumentationDescription  (string, 18/18 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x5
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 18/18 records)
    "Unit 4 - Flooding"  x5
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 10 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (10)
- **Intervals:** median 29.55s (p5 1.76s / p95 158.69s, n=9)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "ChangeCanister"  x10
data.canisterType  (string, 10/10 records)
    "Clay"  x3
    "Gravel"  x3
    "Sand"  x3
    "Bedrock"  x1
data.floor  (string, 10/10 records)
    "4"  x5
    "5"  x4
    "3"  x1
data.machine  (string, 10/10 records)
    "1"  x9
    "2"  x1
data.row  (string, 10/10 records)
    "TopRow"  x8
    "BottomRow"  x2
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `SolarStillDesignEvent` — 9 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (9)
- **Intervals:** median 1.47s (p5 0.75s / p95 5.13s, n=8)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x8; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "optionSelected"  x8
    "DesignSubmitted"  x1
data.designSelections  (object, 1/9 records)
data.designSelections.glassRoofTemperature  (string, 1/9 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/9 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/9 records)
    "Tilted Out"  x1
data.featureUsed  (string, 9/9 records)
    "RoofStyle"  x5
    "GlassRoofTemperature"  x2
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 8/9 records, 1 empty-string)
    "Tilted In"  x2
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted Out"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 4.06s (p5 1.94s / p95 28.51s, n=8)
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x4
data.boxId  (string, 9/9 records)
    "0"  x5
    "1"  x2
    "2"  x2
data.soilType  (string, 9/9 records)
    "Sand"  x5
    "Clay"  x2
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `chatEvent` — 7 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 752.29s (p5 10.01s / p95 705588.95s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "Close"  x5
    "Open"  x2
data.chatID  (string, 7/7 records)
    "NA"  x5
    "[17-26, 18-21, 18-22, 18-24, 18-25]"  x1
    "[95-83, 95-79, 95-42, 95-41, 95-84]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 134702.03s (p5 93689.52s / p95 557184.73s, n=4)
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

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (4)
- **Intervals:** median 2.09s (p5 0.83s / p95 2.22s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 4/4 records)
    "Unit 2 – Watershed"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Watershed Graph"  x4
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x1
    "Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time."  x1
    "Permissions check failed"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 1 empty-string)
    ""  x1
    "NotAllowedError: Failed to execute 'requestPointerLock' on 'Element': Too many pointer lock requests in a short window of time.
    at requestPointerLock (blob:https://mhs.adroit.games/b8c0d538-47f8-4c19-b723-5f2ef04d9235:9:213829)
    at Object.runDeferredCalls (blob:https://mhs.adroit.games/b8c0d538-47f8-4c19-b723-5f2ef04d9235:9:204819)
    at HTMLCanvasElement.jsEventHandler (blob:https://mhs.adroit.games/b8c0d538-47f8-4c19-b723-5f2ef04d9235:9:205513)"  x1
    "TypeError: Permissions check failed"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x3
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `argumentationEvent` actionType: argumentation session: close without preceding open
- `chatEvent` actionType: chat open/close: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (72 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "Selected" (1x); "WaypointMoveEvent" (14x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Legend" (1x); "Waypoint" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (40x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*