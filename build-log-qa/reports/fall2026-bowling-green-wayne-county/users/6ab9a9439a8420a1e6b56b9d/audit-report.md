# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9439a8420a1e6b56b9d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9439a8420a1e6b56b9d
- **Game version string(s) in log:** 2.9.1, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56b9d.jsonl
- **Records:** 12158 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56b9d
- **Time span:** 2026-10-06T19:32:15.969000+00:00 .. 2026-10-18T14:20:28.450000+00:00 (282h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9439a8420a1e6b56b9d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 12158 records, 11 scenes.
- Findings: **0 FAIL**, **31 WARNING**, 97 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3450 | 28.38 | 1 | 9 | 0 | 2026-10-06T19:36:55.019000+00:00 | 2026-10-18T14:20:28.251000+00:00 | 282h 43m |
| PuzzlePieceVisibleEvent | 2890 | 23.77 | 1 | 4 | 0 | 2026-10-07T17:39:28.734000+00:00 | 2026-10-18T13:47:20.885000+00:00 | 260h 7m |
| PlayerPositionEvent | 2344 | 19.28 | 1 | 9 | 0 | 2026-10-06T19:33:14.816000+00:00 | 2026-10-18T14:20:28.450000+00:00 | 282h 47m |
| DialogueEvent | 2193 | 18.04 | 1 | 9 | 1386 | 2026-10-06T19:33:34.673000+00:00 | 2026-10-18T14:20:08.881000+00:00 | 282h 46m |
| argumentationNodeEvent | 442 | 3.64 | 1 | 5 | 0 | 2026-10-06T20:01:56.614000+00:00 | 2026-10-18T14:06:47.349000+00:00 | 282h 4m |
| ObjectInterEvent | 309 | 2.54 | 1 | 9 | 0 | 2026-10-06T19:39:22.167000+00:00 | 2026-10-18T14:20:28.251000+00:00 | 282h 41m |
| TopographicMapEvent | 122 | 1.0 | 1 | 3 | 0 | 2026-10-07T17:37:39.959000+00:00 | 2026-10-14T19:50:08.428000+00:00 | 170h 12m |
| questEvent | 80 | 0.66 | 1 | 9 | 80 | 2026-10-06T19:33:34.641000+00:00 | 2026-10-18T14:16:09.025000+00:00 | 282h 42m |
| DaniEvent | 48 | 0.39 | 1 | 2 | 0 | 2026-10-07T17:37:34.969000+00:00 | 2026-10-13T20:05:30.581000+00:00 | 146h 27m |
| Soil Key Puzzle | 44 | 0.36 | 1 | 3 | 0 | 2026-10-07T17:50:22.659000+00:00 | 2026-10-15T19:28:35.026000+00:00 | 193h 38m |
| DEBUGMenu | 38 | 0.31 | 1 | 9 | 0 | 2026-10-06T19:32:15.969000+00:00 | 2026-10-18T13:43:02.622000+00:00 | 282h 10m |
| WaterChamberEvent | 34 | 0.28 | 1 | 1 | 0 | 2026-10-18T13:46:28.801000+00:00 | 2026-10-18T13:57:34.368000+00:00 | 11m 5s |
| argumentationAnswerEvent | 26 | 0.21 | 1 | 5 | 0 | 2026-10-06T20:02:12.037000+00:00 | 2026-10-18T14:06:49.169000+00:00 | 282h 4m |
| soilMachine | 21 | 0.17 | 1 | 1 | 0 | 2026-10-15T19:46:43.178000+00:00 | 2026-10-15T19:54:59.051000+00:00 | 8m 15s |
| gameWindowFocusEvent | 20 | 0.16 | 1 | 4 | 0 | 2026-10-06T19:32:16.298000+00:00 | 2026-10-18T13:42:55.797000+00:00 | 282h 10m |
| TerasGardenBox | 17 | 0.14 | 1 | 1 | 0 | 2026-10-15T21:49:36.522000+00:00 | 2026-10-16T15:54:21.347000+00:00 | 18h 4m |
| argumentationEvent | 17 | 0.14 | 1 | 5 | 0 | 2026-10-06T20:01:48.197000+00:00 | 2026-10-18T14:06:49.207000+00:00 | 282h 5m |
| chatEvent | 17 | 0.14 | 1 | 4 | 0 | 2026-10-07T18:40:26.455000+00:00 | 2026-10-18T13:58:41.243000+00:00 | 259h 18m |
| gameStartEvent | 17 | 0.14 | 1 | 1 | 0 | 2026-10-06T19:32:16.298000+00:00 | 2026-10-18T13:42:55.797000+00:00 | 282h 10m |
| SolarStillDesignEvent | 11 | 0.09 | 1 | 1 | 0 | 2026-10-18T14:12:35.132000+00:00 | 2026-10-18T14:13:01.022000+00:00 | 25.9s |
| gameWindowUnfocusEvent | 8 | 0.07 | 1 | 4 | 0 | 2026-10-06T20:10:43.318000+00:00 | 2026-10-16T16:03:30.975000+00:00 | 235h 52m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T20:06:35.318000+00:00 | 2026-10-18T14:20:28.236000+00:00 | 282h 13m |
| argumentationToolEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-07T23:13:02.514000+00:00 | 2026-10-08T20:09:12.088000+00:00 | 20h 56m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 162633.532s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.42s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.752s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.062s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.996s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 26.028s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.011s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 275.085s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 14184.26s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 5362.731s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 14422.909s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.821s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.2x vs baseline. 
  - Observed: 38 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 48 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.2x vs baseline. 
  - Observed: 26 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,D,C,2,II; B,2,II; B,3,I; C,2,II; D,2,II; D,3,II; D,4,II; D,A,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 442 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` — record volume changed 8.5x vs baseline. 
  - Observed: 17 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [18-287, 18-289]; [22-46, 22-48, 22-27, 18-287, 18-289]; [23-36, 23-38, 23-39, 23-41, 23-42]; [79-77, 79-74, 79-75, 79-76, 79-70] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[2] _id=6ac54cc0de269131f9b7a2cc ts=2026-10-06T19:32:16.2980000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[616] _id=6ac55527de269131f9b841a4 ts=2026-10-06T20:08:07.3370000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[672] _id=6ac6822dde269131f9bd95a9 ts=2026-10-07T17:32:28.6090000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[1] _id=6ac54cc0de269131f9b7a2cb ts=2026-10-06T19:32:16.2980000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[615] _id=6ac55527de269131f9b841a3 ts=2026-10-06T20:08:07.3370000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[671] _id=6ac6822dde269131f9bd95a8 ts=2026-10-07T17:32:28.6090000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[651] _id=6ac6822dde269131f9bd95a5 ts=2026-10-06T20:10:43.318Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[2105] _id=6ac68a99de269131f9bdab35 ts=2026-10-07T18:08:24.3750000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[2664] _id=6ac69440de269131f9be25ee ts=2026-10-07T18:49:35.6910000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3449 | 0.0 | 1.42 | 295.104 | 21.812 | 429766.662 | 0.2 | 40 | 13 |
| PuzzlePieceVisibleEvent | 2889 | 0.0 | 0.062 | 324.151 | 2.24 | 506387.977 | 0.19 | 1325 | 10 |
| PlayerPositionEvent | 2332 | 0.0 | 10.001 | 398.934 | 10.127 | 429559.423 | 0.15 | 1 | 8 |
| DialogueEvent | 2192 | 0.0 | 4.981 | 464.413 | 35.74 | 429809.997 | 0.13 | 624 | 12 |
| argumentationNodeEvent | 441 | 0.006 | 0.668 | 2302.7 | 11.067 | 430284.081 | 0.03 | 34 | 7 |
| ObjectInterEvent | 308 | 0.0 | 12.752 | 3304.111 | 488.132 | 430632.076 | 0.02 | 4 | 12 |
| TopographicMapEvent | 121 | 0.023 | 3.996 | 5064.037 | 1002.064 | 431782.175 | 0.01 | 2 | 8 |
| questEvent | 79 | 0.001 | 262.692 | 12882.967 | 77967.328 | 429617.306 | 0.0 | 14 | 20 |
| DaniEvent | 47 | 0.005 | 4.045 | 11218.63 | 3294.66 | 506545.44 | 0.01 | 8 | 4 |
| Soil Key Puzzle | 43 | 0.149 | 0.917 | 16211.45 | 15512.969 | 508074.797 | 0.0 | 0 | 3 |
| DEBUGMenu | 37 | 7.181 | 512.891 | 27455.315 | 98037.554 | 431394.524 | 0.0 | 0 | 18 |
| WaterChamberEvent | 33 | 1.641 | 10.412 | 20.169 | 57.521 | 82.873 | 2.97 | 0 | 0 |
| argumentationAnswerEvent | 25 | 3.574 | 26.028 | 40619.085 | 221328.92 | 430350.22 | 0.0 | 0 | 5 |
| soilMachine | 20 | 0.135 | 3.821 | 24.794 | 149.024 | 186.619 | 2.42 | 0 | 0 |
| gameWindowFocusEvent | 19 | 92.08 | 5362.731 | 53465.237 | 178009.345 | 431404.207 | 0.0 | 0 | 17 |
| TerasGardenBox | 16 | 1.211 | 3.24 | 4067.802 | 16257.264 | 64949.653 | 0.01 | 0 | 1 |
| argumentationEvent | 16 | 0.034 | 72.194 | 63468.813 | 281298.859 | 430281.446 | 0.0 | 2 | 5 |
| chatEvent | 16 | 3.91 | 275.085 | 58343.424 | 321033.009 | 506540.97 | 0.0 | 0 | 6 |
| gameStartEvent | 16 | 92.08 | 14184.26 | 63489.969 | 220241.822 | 431404.207 | 0.0 | 0 | 14 |
| SolarStillDesignEvent | 10 | 1.037 | 2.188 | 2.589 | 5.103 | 5.773 | 23.17 | 0 | 0 |
| gameWindowUnfocusEvent | 7 | 31.783 | 14422.909 | 121309.665 | 500229.408 | 680730.13 | 0.0 | 0 | 5 |
| EndOfUnit | 4 | 98617.179 | 162633.532 | 254008.23 | 528320.066 | 592148.675 | 0.0 | 0 | 4 |
| argumentationToolEvent | 3 | 4.163 | 7.011 | 25123.191 | 67823.261 | 75358.4 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[10261] _id=6ad1499ade269131f9e19e01 ts=2026-10-15T21:46:02.0970000Z == 6ab9a9439a8420a1e6b56b9d.jsonl[10262] _id=6ad1499ade269131f9e19e02 ts=2026-10-15T21:46:02.0970000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 33 group(s), 59 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[809] _id=6ac683dfde269131f9bd9704 ts=2026-10-07T17:39:41.9580000Z == 6ab9a9439a8420a1e6b56b9d.jsonl[759] _id=6ac683dfde269131f9bd9706 ts=2026-10-07T17:39:41.9580000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[827] _id=6ac683e3de269131f9bd972a ts=2026-10-07T17:39:44.7940000Z == 6ab9a9439a8420a1e6b56b9d.jsonl[843] _id=6ac683e3de269131f9bd972c ts=2026-10-07T17:39:44.7940000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[856] _id=6ac683edde269131f9bd973a ts=2026-10-07T17:39:55.6050000Z == 6ab9a9439a8420a1e6b56b9d.jsonl[848] _id=6ac683edde269131f9bd973c ts=2026-10-07T17:39:55.6050000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 46 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a9439a8420a1e6b56b9d.jsonl[117] _id=6ac54e6ade269131f9b7aa96 ts=2026-10-06T19:39:22.1670000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[98] _id=6ac54e6ade269131f9b7aa98 ts=2026-10-06T19:39:22.1730000Z`; `299ms: 6ab9a9439a8420a1e6b56b9d.jsonl[764] _id=6ac6837cde269131f9bd9680 ts=2026-10-07T17:38:03.7840000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[746] _id=6ac6837cde269131f9bd9684 ts=2026-10-07T17:38:04.0830000Z`; `242ms: 6ab9a9439a8420a1e6b56b9d.jsonl[746] _id=6ac6837cde269131f9bd9684 ts=2026-10-07T17:38:04.0830000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[775] _id=6ac6837dde269131f9bd9688 ts=2026-10-07T17:38:04.3250000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `800ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1997] _id=6ac688f9de269131f9bda9b8 ts=2026-10-07T18:01:28.7230000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[1982] _id=6ac688fade269131f9bda9ba ts=2026-10-07T18:01:29.5230000Z`; `698ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1999] _id=6ac688fede269131f9bda9c0 ts=2026-10-07T18:01:33.6570000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[1984] _id=6ac688ffde269131f9bda9c2 ts=2026-10-07T18:01:34.3550000Z`; `899ms: 6ab9a9439a8420a1e6b56b9d.jsonl[2063] _id=6ac68a4cde269131f9bdaad9 ts=2026-10-07T18:07:07.8870000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[2064] _id=6ac68a4dde269131f9bdaadb ts=2026-10-07T18:07:08.7860000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `34ms: 6ab9a9439a8420a1e6b56b9d.jsonl[5384] _id=6ac7f887de269131f9c74375 ts=2026-10-08T20:09:42.5450000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[5387] _id=6ac7f887de269131f9c74378 ts=2026-10-08T20:09:42.5790000Z`; `34ms: 6ab9a9439a8420a1e6b56b9d.jsonl[5695] _id=6ace8995de269131f9d21305 ts=2026-10-13T19:42:12.7560000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[5698] _id=6ace8995de269131f9d21308 ts=2026-10-13T19:42:12.7900000Z`; `111ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10233] _id=6ad14958de269131f9e19a70 ts=2026-10-15T21:44:55.4440000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[10236] _id=6ad14958de269131f9e19a76 ts=2026-10-15T21:44:55.5550000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 36 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `994ms: 6ab9a9439a8420a1e6b56b9d.jsonl[494] _id=6ac55406de269131f9b81826 ts=2026-10-06T20:03:18.3630000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[497] _id=6ac55407de269131f9b8183b ts=2026-10-06T20:03:19.3570000Z`; `864ms: 6ab9a9439a8420a1e6b56b9d.jsonl[513] _id=6ac55414de269131f9b819eb ts=2026-10-06T20:03:32.3860000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[514] _id=6ac55415de269131f9b81a15 ts=2026-10-06T20:03:33.2500000Z`; `634ms: 6ab9a9439a8420a1e6b56b9d.jsonl[512] _id=6ac55415de269131f9b81a03 ts=2026-10-06T20:03:32.8030000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[515] _id=6ac55415de269131f9b81a19 ts=2026-10-06T20:03:33.4370000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6ab9a9439a8420a1e6b56b9d.jsonl[11961] _id=6ad4d2c2de269131f9e8a4b8 ts=2026-10-18T14:08:01.8110000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[11962] _id=6ad4d2c2de269131f9e8a4b9 ts=2026-10-18T14:08:01.8120000Z`; `1ms: 6ab9a9439a8420a1e6b56b9d.jsonl[12048] _id=6ad4d43fde269131f9e8a5b6 ts=2026-10-18T14:14:21.9170000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[12049] _id=6ad4d43fde269131f9e8a5b7 ts=2026-10-18T14:14:21.9180000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `400ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9223] _id=6ad12f0ede269131f9e0d29a ts=2026-10-15T19:52:45.4260000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[9224] _id=6ad12f0ede269131f9e0d2a1 ts=2026-10-15T19:52:45.8260000Z`; `135ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9245] _id=6ad12f44de269131f9e0d756 ts=2026-10-15T19:53:39.3380000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[9248] _id=6ad12f44de269131f9e0d75a ts=2026-10-15T19:53:39.4730000Z`; `580ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9248] _id=6ad12f44de269131f9e0d75a ts=2026-10-15T19:53:39.4730000Z ~ 6ab9a9439a8420a1e6b56b9d.jsonl[9277] _id=6ad12f44de269131f9e0d76e ts=2026-10-15T19:53:40.0530000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 119h 49m 
  - Evidence: 119h 49m: 6ab9a9439a8420a1e6b56b9d.jsonl[4573] _id=6ac7f193de269131f9c6b1f2 ts=2026-10-08T19:40:02.7270000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5426] _id=6ace86b5de269131f9d1f152 ts=2026-10-13T19:29:57.2510000Z; 41h 37m: 6ab9a9439a8420a1e6b56b9d.jsonl[10754] _id=6ad28393de269131f9e7fa8d ts=2026-10-16T20:05:34.4830000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11116] _id=6ad4cce0de269131f9e89e7f ts=2026-10-18T13:42:55.4410000Z; 23h 38m: 6ab9a9439a8420a1e6b56b9d.jsonl[5840] _id=6ace8adede269131f9d21fd2 ts=2026-10-13T19:47:42.2490000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6576] _id=6acfd73dde269131f9d8a5a9 ts=2026-10-14T19:25:48.9520000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 140h 42m 
  - Evidence: 140h 42m: 6ab9a9439a8420a1e6b56b9d.jsonl[4091] _id=6ac6d213de269131f9bfc57a ts=2026-10-07T23:13:23.2130000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6209] _id=6ace8cc5de269131f9d2377f ts=2026-10-13T19:55:48.6530000Z; 3h 46m: 6ab9a9439a8420a1e6b56b9d.jsonl[2636] _id=6ac693a1de269131f9be0ad7 ts=2026-10-07T18:46:56.7290000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2788] _id=6ac6c8b6de269131f9bfb800 ts=2026-10-07T22:33:26.2280000Z; 1h 2m: 6ab9a9439a8420a1e6b56b9d.jsonl[735] _id=6ac68364de269131f9bd966a ts=2026-10-07T17:37:39.9400000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2495] _id=6ac69217de269131f9bde035 ts=2026-10-07T18:40:22.9410000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 8 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a9439a8420a1e6b56b9d.jsonl[2604] _id=6ac6935dde269131f9be0262 ts=2026-10-07T18:45:48.2110000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2598] _id=6ac6935dde269131f9be0266 ts=2026-10-07T18:45:48.2160000Z; 5ms: 6ab9a9439a8420a1e6b56b9d.jsonl[2741] _id=6ac6c95ade269131f9bfb8b1 ts=2026-10-07T22:36:10.3190000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2883] _id=6ac6c95ade269131f9bfb8b3 ts=2026-10-07T22:36:10.3240000Z; 7ms: 6ab9a9439a8420a1e6b56b9d.jsonl[2882] _id=6ac6c953de269131f9bfb8ad ts=2026-10-07T22:36:02.7910000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2869] _id=6ac6c953de269131f9bfb8af ts=2026-10-07T22:36:02.7980000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 23m 
  - Evidence: 119h 23m: 6ab9a9439a8420a1e6b56b9d.jsonl[5421] _id=6ac7f8c8de269131f9c746d3 ts=2026-10-08T20:10:47.6200000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5477] _id=6ace87bade269131f9d1fd90 ts=2026-10-13T19:34:17.6170000Z; 41h 31m: 6ab9a9439a8420a1e6b56b9d.jsonl[11072] _id=6ad2850bde269131f9e8044d ts=2026-10-16T20:11:54.9430000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11139] _id=6ad4ccf6de269131f9e89ea0 ts=2026-10-18T13:43:17.7500000Z; 23h 32m: 6ab9a9439a8420a1e6b56b9d.jsonl[6188] _id=6ace8c90de269131f9d23511 ts=2026-10-13T19:54:55.6320000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6702] _id=6acfd79fde269131f9d8aed9 ts=2026-10-14T19:27:26.7570000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 624 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10067] _id=6ad1488cde269131f9e1935a ts=2026-10-15T21:41:32.2220000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10068] _id=6ad1488cde269131f9e1935b ts=2026-10-15T21:41:32.2220000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10088] _id=6ad148b8de269131f9e194af ts=2026-10-15T21:42:16.0530000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10089] _id=6ad148b8de269131f9e194b0 ts=2026-10-15T21:42:16.0530000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10137] _id=6ad148d7de269131f9e195e8 ts=2026-10-15T21:42:47.0840000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10138] _id=6ad148d7de269131f9e195e9 ts=2026-10-15T21:42:47.0840000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 164h 29m 
  - Evidence: 164h 29m: 6ab9a9439a8420a1e6b56b9d.jsonl[4559] _id=6ac6d605de269131f9bfc90f ts=2026-10-07T23:30:12.4970000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[7480] _id=6acfdf19de269131f9d93fec ts=2026-10-14T19:59:21.1720000Z; 46h 17m: 6ab9a9439a8420a1e6b56b9d.jsonl[10727] _id=6ad24acbde269131f9e5882a ts=2026-10-16T16:03:23.6190000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[12151] _id=6ad4d5acde269131f9e8a690 ts=2026-10-18T14:20:28.2360000Z; 44h 4m: 6ab9a9439a8420a1e6b56b9d.jsonl[7480] _id=6acfdf19de269131f9d93fec ts=2026-10-14T19:59:21.1720000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10727] _id=6ad24acbde269131f9e5882a ts=2026-10-16T16:03:23.6190000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9439a8420a1e6b56b9d.jsonl[5296] _id=6ac7f802de269131f9c73a29 ts=2026-10-08T20:07:29.9620000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5430] _id=6ace86c9de269131f9d1f242 ts=2026-10-13T19:30:16.6240000Z; 41h 32m: 6ab9a9439a8420a1e6b56b9d.jsonl[11052] _id=6ad284e1de269131f9e80347 ts=2026-10-16T20:11:13.1560000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11134] _id=6ad4ccf4de269131f9e89e8a ts=2026-10-18T13:43:15.5300000Z; 23h 18m: 6ab9a9439a8420a1e6b56b9d.jsonl[6549] _id=6ace8f7fde269131f9d24fe7 ts=2026-10-13T20:07:26.3480000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6590] _id=6acfd762de269131f9d8a8c2 ts=2026-10-14T19:26:25.9240000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 40 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10261] _id=6ad1499ade269131f9e19e01 ts=2026-10-15T21:46:02.0970000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10262] _id=6ad1499ade269131f9e19e02 ts=2026-10-15T21:46:02.0970000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10262] _id=6ad1499ade269131f9e19e02 ts=2026-10-15T21:46:02.0970000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10263] _id=6ad1499ade269131f9e19e03 ts=2026-10-15T21:46:02.0970000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[6947] _id=6acfd944de269131f9d8da6d ts=2026-10-14T19:34:28.4070000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6948] _id=6acfd944de269131f9d8da6e ts=2026-10-14T19:34:28.4070000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 37m 
  - Evidence: 119h 37m: 6ab9a9439a8420a1e6b56b9d.jsonl[5021] _id=6ac7f62ede269131f9c7098e ts=2026-10-08T19:59:41.4310000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5551] _id=6ace8856de269131f9d20407 ts=2026-10-13T19:36:53.5070000Z; 41h 34m: 6ab9a9439a8420a1e6b56b9d.jsonl[11028] _id=6ad284c3de269131f9e8023a ts=2026-10-16T20:10:43.0610000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11224] _id=6ad4cd78de269131f9e89f3a ts=2026-10-18T13:45:28.1990000Z; 23h 29m: 6ab9a9439a8420a1e6b56b9d.jsonl[7479] _id=6acfdf05de269131f9d93efc ts=2026-10-14T19:59:00.8700000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[7611] _id=6ad12955de269131f9e06333 ts=2026-10-15T19:28:20.4990000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9683] _id=6ad13250de269131f9e1105b ts=2026-10-15T20:06:39.3580000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9684] _id=6ad13250de269131f9e1105c ts=2026-10-15T20:06:39.3580000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9811] _id=6ad146aede269131f9e189b0 ts=2026-10-15T21:33:33.9040000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9812] _id=6ad146aede269131f9e189b1 ts=2026-10-15T21:33:33.9040000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9857] _id=6ad14708de269131f9e18bce ts=2026-10-15T21:35:03.9420000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9858] _id=6ad14708de269131f9e18bcf ts=2026-10-15T21:35:03.9420000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9439a8420a1e6b56b9d.jsonl[5422] _id=6ac7f8c8de269131f9c746db ts=2026-10-08T20:10:48.3020000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5428] _id=6ace86c4de269131f9d1f204 ts=2026-10-13T19:30:07.7250000Z; 41h 31m: 6ab9a9439a8420a1e6b56b9d.jsonl[11073] _id=6ad2850fde269131f9e80459 ts=2026-10-16T20:11:59.2620000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11132] _id=6ad4ccebde269131f9e89e87 ts=2026-10-18T13:43:02.6350000Z; 23h 18m: 6ab9a9439a8420a1e6b56b9d.jsonl[6573] _id=6ace8fa4de269131f9d250f4 ts=2026-10-13T20:08:04.0810000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6585] _id=6acfd75ade269131f9d8a835 ts=2026-10-14T19:26:16.2660000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[9716] _id=6ad132a0de269131f9e116f2 ts=2026-10-15T20:07:59.7540000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9717] _id=6ad145e7de269131f9e18320 ts=2026-10-15T20:07:59.754Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 140h 39m 
  - Evidence: 140h 39m: 6ab9a9439a8420a1e6b56b9d.jsonl[3884] _id=6ac6d0cbde269131f9bfc3c0 ts=2026-10-07T23:07:54.6280000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5841] _id=6ace8ae0de269131f9d21ffb ts=2026-10-13T19:47:42.6050000Z; 41h 31m: 6ab9a9439a8420a1e6b56b9d.jsonl[11069] _id=6ad284eade269131f9e803c9 ts=2026-10-16T20:11:21.0580000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11135] _id=6ad4ccf4de269131f9e89e8c ts=2026-10-18T13:43:15.5800000Z; 24h 0m: 6ab9a9439a8420a1e6b56b9d.jsonl[6711] _id=6acfd7bcde269131f9d8b191 ts=2026-10-14T19:27:55.1790000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[7624] _id=6ad12969de269131f9e064fe ts=2026-10-15T19:28:40.5950000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1325 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1007] _id=6ac68465de269131f9bd9868 ts=2026-10-07T17:41:55.5570000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[1008] _id=6ac68465de269131f9bd9869 ts=2026-10-07T17:41:55.5570000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1008] _id=6ac68465de269131f9bd9869 ts=2026-10-07T17:41:55.5570000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[1020] _id=6ac68465de269131f9bd986b ts=2026-10-07T17:41:55.5570000Z; 0ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1020] _id=6ac68465de269131f9bd986b ts=2026-10-07T17:41:55.5570000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[1021] _id=6ac68465de269131f9bd986c ts=2026-10-07T17:41:55.5570000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 141h 7m 
  - Evidence: 141h 7m: 6ab9a9439a8420a1e6b56b9d.jsonl[2939] _id=6ac6c9ddde269131f9bfb97b ts=2026-10-07T22:38:21.0040000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5795] _id=6ace8a88de269131f9d21af0 ts=2026-10-13T19:46:15.8010000Z; 47h 41m: 6ab9a9439a8420a1e6b56b9d.jsonl[5827] _id=6ace8ab5de269131f9d21d58 ts=2026-10-13T19:47:00.5440000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[7606] _id=6ad12955de269131f9e0632f ts=2026-10-15T19:28:20.4930000Z; 4h 47m: 6ab9a9439a8420a1e6b56b9d.jsonl[1793] _id=6ac68662de269131f9bd9f31 ts=2026-10-07T17:50:25.7150000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2925] _id=6ac6c9b3de269131f9bfb945 ts=2026-10-07T22:37:39.1150000Z
- **INFO / Info** `TerasGardenBox` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 18h 2m 
  - Evidence: 18h 2m: 6ab9a9439a8420a1e6b56b9d.jsonl[10411] _id=6ad14ac7de269131f9e1a5df ts=2026-10-15T21:51:02.5880000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10474] _id=6ad2487cde269131f9e56582 ts=2026-10-16T15:53:32.2410000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a9439a8420a1e6b56b9d.jsonl[5008] _id=6ac7f61bde269131f9c70708 ts=2026-10-08T19:59:23.2880000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6210] _id=6ace8cc2de269131f9d23761 ts=2026-10-13T19:55:45.4630000Z; 23h 42m: 6ab9a9439a8420a1e6b56b9d.jsonl[6490] _id=6ace8f09de269131f9d24b59 ts=2026-10-13T20:05:28.7660000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[7269] _id=6acfdc51de269131f9d9124e ts=2026-10-14T19:47:28.8770000Z; 20h 31m: 6ab9a9439a8420a1e6b56b9d.jsonl[3986] _id=6ac6d1d1de269131f9bfc53c ts=2026-10-07T23:12:17.3830000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[4625] _id=6ac7f287de269131f9c6c541 ts=2026-10-08T19:44:06.7340000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.023s..0.031s shown 
  - Evidence: 23ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1943] _id=6ac688eede269131f9bda9b0 ts=2026-10-07T18:01:17.8520000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[1996] _id=6ac688eede269131f9bda9b4 ts=2026-10-07T18:01:17.8750000Z; 31ms: 6ab9a9439a8420a1e6b56b9d.jsonl[1942] _id=6ac688eede269131f9bda9ae ts=2026-10-07T18:01:17.8210000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[1943] _id=6ac688eede269131f9bda9b0 ts=2026-10-07T18:01:17.8520000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 32m 
  - Evidence: 119h 32m: 6ab9a9439a8420a1e6b56b9d.jsonl[5383] _id=6ac7f887de269131f9c74373 ts=2026-10-08T20:09:42.5140000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5700] _id=6ace8995de269131f9d21303 ts=2026-10-13T19:42:12.7340000Z; 64h 21m: 6ab9a9439a8420a1e6b56b9d.jsonl[10232] _id=6ad14957de269131f9e19a6e ts=2026-10-15T21:44:55.4240000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11906] _id=6ad4d26cde269131f9e8a452 ts=2026-10-18T14:06:36.3720000Z; 49h 57m: 6ab9a9439a8420a1e6b56b9d.jsonl[5700] _id=6ace8995de269131f9d21303 ts=2026-10-13T19:42:12.7340000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9975] _id=6ad14816de269131f9e18fe7 ts=2026-10-15T21:39:33.5430000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a9439a8420a1e6b56b9d.jsonl[5387] _id=6ac7f887de269131f9c74378 ts=2026-10-08T20:09:42.5790000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5658] _id=6ace8950de269131f9d210a8 ts=2026-10-13T19:41:04.0250000Z; 64h 20m: 6ab9a9439a8420a1e6b56b9d.jsonl[10236] _id=6ad14958de269131f9e19a76 ts=2026-10-15T21:44:55.5550000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11863] _id=6ad4d22ede269131f9e8a3f5 ts=2026-10-18T14:05:33.5510000Z; 49h 56m: 6ab9a9439a8420a1e6b56b9d.jsonl[5698] _id=6ace8995de269131f9d21308 ts=2026-10-13T19:42:12.7900000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9934] _id=6ad147d0de269131f9e18e73 ts=2026-10-15T21:38:24.2400000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.034s..0.034s shown 
  - Evidence: 34ms: 6ab9a9439a8420a1e6b56b9d.jsonl[5384] _id=6ac7f887de269131f9c74375 ts=2026-10-08T20:09:42.5450000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5387] _id=6ac7f887de269131f9c74378 ts=2026-10-08T20:09:42.5790000Z; 34ms: 6ab9a9439a8420a1e6b56b9d.jsonl[5695] _id=6ace8995de269131f9d21305 ts=2026-10-13T19:42:12.7560000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5698] _id=6ace8995de269131f9d21308 ts=2026-10-13T19:42:12.7900000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 31m 
  - Evidence: 119h 31m: 6ab9a9439a8420a1e6b56b9d.jsonl[5379] _id=6ac7f882de269131f9c74327 ts=2026-10-08T20:09:37.4600000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5650] _id=6ace894ede269131f9d2108e ts=2026-10-13T19:41:01.5410000Z; 64h 20m: 6ab9a9439a8420a1e6b56b9d.jsonl[10215] _id=6ad14956de269131f9e19a5f ts=2026-10-15T21:44:53.8580000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11855] _id=6ad4d233de269131f9e8a3fc ts=2026-10-18T14:05:38.7960000Z; 49h 56m: 6ab9a9439a8420a1e6b56b9d.jsonl[5694] _id=6ace8992de269131f9d212f9 ts=2026-10-13T19:42:10.4630000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9939] _id=6ad147d7de269131f9e18e93 ts=2026-10-15T21:38:31.1980000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 34 interval(s) ≤ 0.006s..0.018s shown 
  - Evidence: 6ms: 6ab9a9439a8420a1e6b56b9d.jsonl[10101] _id=6ad148bede269131f9e194ed ts=2026-10-15T21:42:21.9570000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10105] _id=6ad148bede269131f9e194f1 ts=2026-10-15T21:42:21.9630000Z; 7ms: 6ab9a9439a8420a1e6b56b9d.jsonl[5319] _id=6ac7f825de269131f9c73cfe ts=2026-10-08T20:08:04.8870000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5320] _id=6ac7f825de269131f9c73d04 ts=2026-10-08T20:08:04.8940000Z; 18ms: 6ab9a9439a8420a1e6b56b9d.jsonl[5261] _id=6ac7f877de269131f9c74274 ts=2026-10-08T20:09:26.5240000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5277] _id=6ac7f877de269131f9c7427e ts=2026-10-08T20:09:26.5420000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 20h 55m 
  - Evidence: 20h 55m: 6ab9a9439a8420a1e6b56b9d.jsonl[4098] _id=6ac6d1ffde269131f9bfc56c ts=2026-10-07T23:13:02.5140000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5361] _id=6ac7f85dde269131f9c740ec ts=2026-10-08T20:09:00.9140000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 140h 42m 
  - Evidence: 140h 42m: 6ab9a9439a8420a1e6b56b9d.jsonl[4102] _id=6ac6d21ade269131f9bfc57e ts=2026-10-07T23:13:30.2800000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6215] _id=6ace8cc7de269131f9d2379d ts=2026-10-13T19:55:51.2500000Z; 71h 59m: 6ab9a9439a8420a1e6b56b9d.jsonl[6494] _id=6ace8f11de269131f9d24bc8 ts=2026-10-13T20:05:37.2360000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10752] _id=6ad2838ede269131f9e7fa7d ts=2026-10-16T20:05:34.2580000Z; 41h 37m: 6ab9a9439a8420a1e6b56b9d.jsonl[10752] _id=6ad2838ede269131f9e7fa7d ts=2026-10-16T20:05:34.2580000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11117] _id=6ad4cce7de269131f9e89e84 ts=2026-10-18T13:43:02.4760000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a9439a8420a1e6b56b9d.jsonl[4571] _id=6ac7f18ade269131f9c6b154 ts=2026-10-08T19:39:53.3810000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5424] _id=6ace86b6de269131f9d1f15d ts=2026-10-13T19:29:57.5880000Z; 41h 37m: 6ab9a9439a8420a1e6b56b9d.jsonl[10751] _id=6ad28382de269131f9e7fa6d ts=2026-10-16T20:05:21.4370000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11130] _id=6ad4cce0de269131f9e89e82 ts=2026-10-18T13:42:55.7970000Z; 23h 55m: 6ab9a9439a8420a1e6b56b9d.jsonl[5424] _id=6ace86b6de269131f9d1f15d ts=2026-10-13T19:29:57.5880000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6578] _id=6acfd73dde269131f9d8a5ae ts=2026-10-14T19:25:49.1120000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 119h 50m 
  - Evidence: 119h 50m: 6ab9a9439a8420a1e6b56b9d.jsonl[4570] _id=6ac7f18ade269131f9c6b153 ts=2026-10-08T19:39:53.3810000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5423] _id=6ace86b6de269131f9d1f15c ts=2026-10-13T19:29:57.5880000Z; 41h 37m: 6ab9a9439a8420a1e6b56b9d.jsonl[10750] _id=6ad28382de269131f9e7fa6c ts=2026-10-16T20:05:21.4370000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11103] _id=6ad4cce0de269131f9e89e81 ts=2026-10-18T13:42:55.7970000Z; 23h 55m: 6ab9a9439a8420a1e6b56b9d.jsonl[5423] _id=6ace86b6de269131f9d1f15c ts=2026-10-13T19:29:57.5880000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6577] _id=6acfd73dde269131f9d8a5ad ts=2026-10-14T19:25:49.1120000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 189h 5m 
  - Evidence: 189h 5m: 6ab9a9439a8420a1e6b56b9d.jsonl[3711] _id=6ac6cdd8de269131f9bfc10b ts=2026-10-07T22:55:19.7450000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[9546] _id=6ad130f2de269131f9e0faa2 ts=2026-10-15T20:00:49.8750000Z; 21h 57m: 6ab9a9439a8420a1e6b56b9d.jsonl[651] _id=6ac6822dde269131f9bd95a5 ts=2026-10-06T20:10:43.318Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[2105] _id=6ac68a99de269131f9bdab35 ts=2026-10-07T18:08:24.3750000Z; 20h 2m: 6ab9a9439a8420a1e6b56b9d.jsonl[9546] _id=6ad130f2de269131f9e0faa2 ts=2026-10-15T20:00:49.8750000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[10740] _id=6ad24ad3de269131f9e58907 ts=2026-10-16T16:03:30.9750000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9439a8420a1e6b56b9d.jsonl[5391] _id=6ac7f892de269131f9c74400 ts=2026-10-08T20:09:54.1930000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[5429] _id=6ace86c4de269131f9d1f205 ts=2026-10-13T19:30:11.4990000Z; 41h 37m: 6ab9a9439a8420a1e6b56b9d.jsonl[10753] _id=6ad28393de269131f9e7fa8c ts=2026-10-16T20:05:34.4700000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11133] _id=6ad4ccebde269131f9e89e88 ts=2026-10-18T13:43:06.8390000Z; 23h 38m: 6ab9a9439a8420a1e6b56b9d.jsonl[5851] _id=6ace8ae3de269131f9d22045 ts=2026-10-13T19:47:47.1010000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[6587] _id=6acfd75ade269131f9d8a836 ts=2026-10-14T19:26:17.5190000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56b9d.jsonl[11961] _id=6ad4d2c2de269131f9e8a4b8 ts=2026-10-18T14:08:01.8110000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[11962] _id=6ad4d2c2de269131f9e8a4b9 ts=2026-10-18T14:08:01.8120000Z; 1ms: 6ab9a9439a8420a1e6b56b9d.jsonl[12048] _id=6ad4d43fde269131f9e8a5b6 ts=2026-10-18T14:14:21.9170000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[12049] _id=6ad4d43fde269131f9e8a5b7 ts=2026-10-18T14:14:21.9180000Z; 1ms: 6ab9a9439a8420a1e6b56b9d.jsonl[428] _id=6ac55347de269131f9b7fcfb ts=2026-10-06T20:00:06.4160000Z -> 6ab9a9439a8420a1e6b56b9d.jsonl[429] _id=6ac55347de269131f9b7fcfc ts=2026-10-06T20:00:06.4170000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[415] _id=6ac55320de269131f9b7f880 ts=2026-10-06T19:59:28.0300000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[530] _id=6ac5542fde269131f9b81ddb ts=2026-10-06T20:03:59.1720000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[2153] _id=6ac68b7bde269131f9bdabaf ts=2026-10-07T18:12:10.8770000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[5387] _id=6ac7f887de269131f9c74378 ts=2026-10-08T20:09:42.5790000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[5698] _id=6ace8995de269131f9d21308 ts=2026-10-13T19:42:12.7900000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[10236] _id=6ad14958de269131f9e19a76 ts=2026-10-15T21:44:55.5550000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[10752] _id=6ad2838ede269131f9e7fa7d ts=2026-10-16T20:05:34.2580000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[11117] _id=6ad4cce7de269131f9e89e84 ts=2026-10-18T13:43:02.4760000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[11703] _id=6ad4d091de269131f9e8a2e5 ts=2026-10-18T13:58:41.2430000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[8771] _id=6ad12bd7de269131f9e09f7a ts=2026-10-15T19:39:02.4210000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[2682] _id=6ac694e1de269131f9be449c ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 29 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[3141] _id=6ac6cac1de269131f9bfbb9d ts=2026-10-07T22:42:08.3530000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[3157] _id=6ac6cac5de269131f9bfbbb1 ts=2026-10-07T22:42:13.0000000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[3148] _id=6ac6cac8de269131f9bfbbbb ts=2026-10-07T22:42:14.7010000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 64 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[759] _id=6ac683dfde269131f9bd9706 ts=2026-10-07T17:39:41.9580000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[810] _id=6ac683dfde269131f9bd9709 ts=2026-10-07T17:39:41.9580000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[830] _id=6ac683dfde269131f9bd970b ts=2026-10-07T17:39:41.9580000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 28 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[2149] _id=6ac68b6bde269131f9bdaba1 ts=2026-10-07T18:11:54.2990000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[2166] _id=6ac68bb3de269131f9bdabdb ts=2026-10-07T18:13:06.5420000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[2240] _id=6ac68c88de269131f9bdaf1f ts=2026-10-07T18:16:39.8080000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[5368] _id=6ac7f864de269131f9c7414a ts=2026-10-08T20:09:07.9250000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 406 start, 401 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 774 open, 762 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 35 open, 34 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationToolOpen' (totals: 4 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 47 start, 33 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 239 of 12156 adjacent _id pairs reverse in client time; worst 119.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56b9d.jsonl[906] _id=6ac68449de269131f9bd97b0 ts=2026-10-07T17:41:28.0900000Z`; `6ab9a9439a8420a1e6b56b9d.jsonl[918] _id=6ac68449de269131f9bd97b2 ts=2026-10-07T17:39:28.7340000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.64s, min -76905.86s, max -0.26s over 12157 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9439a8420a1e6b56b9d\coverage.yaml

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

### `InputEvent` — 3450 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1026); Unit 3 Dungeon Dev (598); Unit 3 Dev (561); Unit 4 Dev - Dungeon (437); Unit 4 Dev (261); Unit 5 Dev - Dungeon (213); Unit 4 Dev - Anderson Base (156); Unit 1 Dev (120); Unit 5 Dev (78)
- **Intervals:** median 1.42s (p5 0.18s / p95 21.81s, n=3449)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3450/3450 records)
    "pressed"  x3450
data.actionType  (string, 3450/3450 records)
    "Move"  x2586
    "Interact"  x492
    "Jump"  x151
    "Ascend"  x108
    "Hoverboard"  x52
    "Sprint"  x36
    "Map"  x21
    "Pause"  x4
data.key  (string, 3450/3450 records, 16 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3450/3450 records)
    "Player"  x2569
    "Drone"  x881
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2890 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1270); Unit 4 Dev (944); Unit 5 Dev - Dungeon (414); Unit 3 Dungeon Dev (262)
- **Intervals:** median 0.06s (p5 0.00s / p95 2.24s, n=2889)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2890/2890 records)
    "BecameVisible"  x774
    "BecameInvisible"  x762
    "BecameCameraCentered"  x677
    "BecameCameraUncentered"  x677
data.pieceId  (string, 2890/2890 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2890/2890 records)
    1936 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2344 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (807); Unit 3 Dev (379); Unit 4 Dev (235); Unit 3 Dungeon Dev (215); Unit 1 Dev (200); Unit 4 Dev - Dungeon (133); Unit 5 Dev - Dungeon (132); Unit 5 Dev (128); Unit 4 Dev - Anderson Base (115)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.13s, n=2332)
- **Fields under `data`:**

```text
data.position  (object, 2344/2344 records)
data.position.x  (number, 2344/2344 records)
    numeric range -655.582 .. 1670.54 (779 unique)
data.position.y  (number, 2344/2344 records)
    numeric range -115.127 .. 222.005 (531 unique)
data.position.z  (number, 2344/2344 records)
    numeric range -1039.25 .. 1984.45 (779 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2193 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (580); Unit 3 Dev (400); Unit 4 Dev (306); Unit 5 Dev (217); Unit 1 Dev (215); Unit 3 Dungeon Dev (165); Unit 4 Dev - Anderson Base (125); Unit 5 Dev - Dungeon (93); Unit 4 Dev - Dungeon (92)
- **eventKey:** present on 1386 of 2193 records
- **Intervals:** median 4.98s (p5 0.00s / p95 35.74s, n=2192)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1386; [conversationId, dialogueEventType] x807
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2193/2193 records)
    numeric range 8 .. 118 (55 unique)
data.dialogueEventType  (string, 2193/2193 records)
    "DialogueNodeEvent"  x1386
    "DialogueStartEvent"  x406
    "DialogueFinishEvent"  x401
data.nodeId  (number, 1386/2193 records)
    numeric range 0 .. 290 (230 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 442 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (211); Unit 3 Dev (104); Unit 1 Dev (44); Unit 2 Prod (Refactor) (43); Unit 5 Dev (40)
- **Intervals:** median 0.67s (p5 0.03s / p95 11.07s, n=441)
- **Fields under `data`:**

```text
data.actionType  (string, 442/442 records)
    "argumentationNodeHoverEnd"  x195
    "argumentationNodeHoverStart"  x195
    "argumentationNodeAdd"  x38
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 442/442 records)
    "Unit 4 - Flooding"  x211
    "Unit 3 - Pollution Upstream"  x104
    "Unit 2 – Watershed"  x43
    "Unit 5"  x40
    "Unit 1 - Freshwater"  x29
    "Unit 1 - Argumentation Tutorial"  x15
data.nodeName  (string, 442/442 records)
    "C"  x62
    "B"  x56
    "I"  x56
    "2"  x51
    "1"  x49
    "A"  x48
    "3"  x31
    "II"  x29
    "4"  x26
    "D"  x26
    "5"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 309 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 3 Dungeon Dev (85); Unit 4 Dev - Dungeon (83); Unit 2 Prod (Refactor) (51); Unit 4 Dev (29); Unit 5 Dev - Dungeon (15); Unit 4 Dev - Anderson Base (14); Unit 3 Dev (12); Unit 1 Dev (10); Unit 5 Dev (10)
- **Intervals:** median 12.75s (p5 0.19s / p95 488.13s, n=308)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 309/309 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 309/309 records)
    111 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 122 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (72); Unit 3 Dev (33); Unit 3 Dungeon Dev (17)
- **Intervals:** median 4.00s (p5 0.70s / p95 1002.06s, n=121)
- **`data` key-set variants:** [actionType, featureUsed] x69; [actionType, featureUsed, location] x53
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 122/122 records)
    "WaypointMoveEvent"  x47
    "MapOpenEvent"  x35
    "MapCloseEvent"  x34
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x1
data.featureUsed  (string, 122/122 records)
    "Map"  x69
    "Waypoint"  x53
data.location  (object, 53/122 records)
data.location.x  (number, 53/122 records)
    numeric range -324.034 .. 553.657 (37 unique)
data.location.y  (number, 53/122 records)
    numeric range -342.065 .. 301.84 (39 unique)
data.location.z  (number, 53/122 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 80 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (15); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev (11); Unit 4 Dev - Dungeon (8); Unit 5 Dev - Dungeon (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 80 of 80 records
- **Intervals:** median 262.69s (p5 0.01s / p95 77967.33s, n=79)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x33
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 80/80 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x33
data.questID  (string, 80/80 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 80/80 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 33/80 records)
    "Succeeded"  x33
```

Raw examples: `event_examples.json` -> `questEvent`.

### `DaniEvent` — 48 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (34); Unit 3 Dungeon Dev (14)
- **Intervals:** median 4.04s (p5 0.01s / p95 3294.66s, n=47)
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "Close"  x24
    "Open"  x24
data.toolName  (string, 48/48 records, 40 empty-string)
    ""  x40
    "Settings"  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `Soil Key Puzzle` — 44 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (12); Unit 4 Dev (10)
- **Intervals:** median 0.92s (p5 0.18s / p95 15512.97s, n=43)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x36; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/44 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/44 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 36/44 records)
    "RightDrag"  x21
    "LeftDrag"  x15
data.currentSoilType  (string, 36/44 records)
    "CLAY"  x9
    "CLAYROCK"  x7
    "CLAYSAND"  x7
    "SAND"  x5
    "SANDGRAVEL"  x4
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 36/44 records)
    "false"  x26
    "true"  x10
data.waterLevelStatus  (string, 36/44 records)
    "TooLow"  x14
    "TooHigh"  x12
    "Proper"  x10
data.waterRetentionChange  (string, 36/44 records)
    "Decrease"  x13
    "Increase"  x13
    "NoChange"  x10
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `DEBUGMenu` — 38 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 2 Prod (Refactor) (5); Unit 4 Dev (5); Unit 3 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 5 Dev - Dungeon (2); Unit 1 Dev (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 512.89s (p5 9.42s / p95 98037.55s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "DebugMenuStateChanged"  x38
data.isOpened  (bool, 38/38 records)
    false  x38
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 34 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (34)
- **Intervals:** median 10.41s (p5 3.63s / p95 57.52s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "On"  x22
    "Off"  x12
data.floor  (string, 34/34 records)
    "3"  x16
    "4"  x8
    "2"  x7
    "1"  x3
data.machineNumber  (string, 34/34 records)
    "One"  x33
    "Two"  x1
data.machineType  (string, 34/34 records)
    "Condenser"  x17
    "Evaporator"  x6
    "DualChamber_Condenser"  x5
    "DualChamber_Evaporator"  x4
    "VentSwitch"  x2
data.room  (string, 34/34 records)
    "2"  x16
    "1"  x8
    "3"  x8
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 26 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (15); Unit 3 Dev (6); Unit 1 Dev (2); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 26.03s (p5 4.11s / p95 221328.92s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "submitAnswerEvent"  x26
data.answerSubmitted  (string, 26/26 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 26/26 records)
    "Unit 4 - Flooding"  x15
    "Unit 3 - Pollution Upstream"  x6
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 3.82s (p5 0.27s / p95 149.02s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Clay"  x12
    "Bedrock"  x6
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 21/21 records)
    "5"  x19
    "3"  x1
    "4"  x1
data.machine  (string, 21/21 records)
    "1"  x20
    "2"  x1
data.row  (string, 21/21 records)
    "BottomRow"  x15
    "TopRow"  x6
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (17); Transition (1); Unit 2 Prod (Refactor) (1); Unit 4 Dev (1)
- **Intervals:** median 5362.73s (p5 330.48s / p95 178009.34s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `TerasGardenBox` — 17 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (17)
- **Intervals:** median 3.24s (p5 1.31s / p95 16257.26s, n=16)
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records, 10 empty-string)
    ""  x10
    "cameraPlaced"  x7
data.boxId  (string, 17/17 records)
    "0"  x9
    "1"  x4
    "2"  x4
data.soilType  (string, 17/17 records)
    "Sand"  x6
    "Gravel"  x5
    "Clay"  x4
    "None"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationEvent` — 17 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (6); Unit 1 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 72.19s (p5 0.03s / p95 281298.86s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationSessionClose"  x10
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 17/17 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 17/17 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 17 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dungeon Dev (6); Unit 5 Dev - Dungeon (2); Unit 5 Dev (1)
- **Intervals:** median 275.08s (p5 5.73s / p95 321033.01s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "Close"  x10
    "Open"  x7
data.chatID  (string, 17/17 records)
    "NA"  x10
    "[79-77, 79-74, 79-75, 79-76, 79-70]"  x3
    "[22-46, 22-48, 22-27, 18-287, 18-289]"  x2
    "[18-287, 18-289]"  x1
    "[23-36, 23-38, 23-39, 23-41, 23-42]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 14184.26s (p5 290.75s / p95 220241.82s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 2.19s (p5 1.29s / p95 5.10s, n=10)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x10; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "optionSelected"  x10
    "DesignSubmitted"  x1
data.designSelections  (object, 1/11 records)
data.designSelections.glassRoofTemperature  (string, 1/11 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/11 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/11 records)
    "Tilted Out"  x1
data.featureUsed  (string, 11/11 records)
    "RoofStyle"  x5
    "ExtraCovering"  x3
    "GlassRoofTemperature"  x2
    "Submit"  x1
data.selectedOption  (string, 10/11 records)
    "Covered"  x2
    "Flat"  x2
    "Tilted Out"  x2
    "Cold"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); MainMenu (1); Transition (1); Unit 4 Dev (1)
- **Intervals:** median 14422.91s (p5 109.06s / p95 500229.41s, n=7)
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
- **Intervals:** median 162633.53s (p5 107620.97s / p95 528320.07s, n=4)
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

- **Scenes:** Unit 3 Dev (3); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 7.01s (p5 4.45s / p95 67823.26s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x1
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - Watershed Graph"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

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
    "unit2"  x1
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
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (12 records)
- `TerasGardenBox` data.actionType: "" (10x)
- `TerasGardenBox` data.soilType: "None" (2x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (47x); "WaypointResetEvent" (1x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (53x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*