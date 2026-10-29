# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b75

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b75
- **Game version string(s) in log:** 2.8.1, 2.9.1, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b75.jsonl
- **Records:** 13066 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b75
- **Time span:** 2026-10-05T18:48:36.774000+00:00 .. 2026-10-19T02:36:18.950000+00:00 (319h 47m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b75\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 13066 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 97 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3840 | 29.39 | 1 | 4 | 0 | 2026-10-06T19:12:33.370000+00:00 | 2026-10-19T01:38:20.320000+00:00 | 294h 25m |
| InputEvent | 3635 | 27.82 | 1 | 9 | 0 | 2026-10-06T18:37:21.073000+00:00 | 2026-10-19T02:36:18.950000+00:00 | 295h 58m |
| PlayerPositionEvent | 2331 | 17.84 | 1 | 9 | 0 | 2026-10-06T18:37:17.661000+00:00 | 2026-10-19T02:36:18.932000+00:00 | 295h 59m |
| DialogueEvent | 2216 | 16.96 | 1 | 9 | 1414 | 2026-10-06T18:37:37.501000+00:00 | 2026-10-19T02:35:41.878000+00:00 | 295h 58m |
| argumentationNodeEvent | 338 | 2.59 | 1 | 5 | 0 | 2026-10-06T19:01:15.619000+00:00 | 2026-10-19T02:11:14.024000+00:00 | 295h 9m |
| ObjectInterEvent | 296 | 2.27 | 1 | 9 | 0 | 2026-10-06T18:42:53.998000+00:00 | 2026-10-19T02:36:18.950000+00:00 | 295h 53m |
| questEvent | 84 | 0.64 | 1 | 9 | 84 | 2026-10-06T18:37:37.476000+00:00 | 2026-10-19T02:26:43.392000+00:00 | 295h 49m |
| TopographicMapEvent | 60 | 0.46 | 1 | 3 | 0 | 2026-10-06T19:13:04.329000+00:00 | 2026-10-15T19:18:44.302000+00:00 | 216h 5m |
| Soil Key Puzzle | 54 | 0.41 | 1 | 3 | 0 | 2026-10-08T18:59:46.283000+00:00 | 2026-10-16T16:56:27.740000+00:00 | 189h 56m |
| WaterChamberEvent | 34 | 0.26 | 1 | 1 | 0 | 2026-10-19T01:36:33.093000+00:00 | 2026-10-19T01:54:33.321000+00:00 | 18m 0s |
| DEBUGMenu | 28 | 0.21 | 1 | 9 | 0 | 2026-10-06T18:37:17.642000+00:00 | 2026-10-19T01:28:01.233000+00:00 | 294h 50m |
| argumentationAnswerEvent | 20 | 0.15 | 1 | 5 | 0 | 2026-10-06T19:02:28.533000+00:00 | 2026-10-19T02:11:15.361000+00:00 | 295h 8m |
| soilMachine | 19 | 0.15 | 1 | 1 | 0 | 2026-10-16T18:55:12.010000+00:00 | 2026-10-19T00:48:08.619000+00:00 | 53h 52m |
| DaniEvent | 16 | 0.12 | 1 | 1 | 0 | 2026-10-15T18:42:13.454000+00:00 | 2026-10-15T19:18:38.934000+00:00 | 36m 25s |
| gameWindowFocusEvent | 15 | 0.11 | 1 | 3 | 0 | 2026-10-05T18:48:36.774000+00:00 | 2026-10-19T02:33:01.651000+00:00 | 319h 44m |
| argumentationEvent | 14 | 0.11 | 1 | 5 | 0 | 2026-10-06T19:02:05.353000+00:00 | 2026-10-19T02:11:15.397000+00:00 | 295h 9m |
| argumentationToolEvent | 14 | 0.11 | 1 | 4 | 0 | 2026-10-06T19:02:05.315000+00:00 | 2026-10-19T02:10:54.871000+00:00 | 295h 8m |
| gameStartEvent | 13 | 0.1 | 1 | 1 | 0 | 2026-10-05T18:48:36.776000+00:00 | 2026-10-19T01:27:49.924000+00:00 | 318h 39m |
| SolarStillDesignEvent | 11 | 0.08 | 1 | 1 | 0 | 2026-10-19T02:20:39.948000+00:00 | 2026-10-19T02:22:13.370000+00:00 | 1m 33s |
| TerasGardenBox | 11 | 0.08 | 1 | 1 | 0 | 2026-10-19T01:16:05.295000+00:00 | 2026-10-19T01:18:43.837000+00:00 | 2m 38s |
| gameWindowUnfocusEvent | 8 | 0.06 | 1 | 4 | 0 | 2026-10-05T18:49:24.235000+00:00 | 2026-10-19T02:32:59.990000+00:00 | 319h 43m |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T19:07:55.117000+00:00 | 2026-10-19T02:36:18.939000+00:00 | 295h 28m |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-19T01:28:01.018000+00:00 | 2026-10-19T01:55:55.813000+00:00 | 27m 54s |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 210668.299s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.103s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.063s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — median interval between records changed substantially. 
  - Observed: 4.023s median 
  - Expected: 1.823s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.518s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 15.012s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 82727.229s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 56105.989s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 172286.232s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 14.927s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 16 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend; Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift; m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to place glyph 
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
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 240 ft; 270 ft; 30 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,II; A,4,II; A,C,2,II; A,D,2,II; C,2,II; C,D,2,II; C,D,3,II; D,1,II; D,A,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 8 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[154] _id=6ac541a7de269131f9b6d027 ts=2026-10-06T18:44:54.2550000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[216] _id=6ac542bade269131f9b6f49d ts=2026-10-06T18:49:29.3430000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[269] _id=6ac543dede269131f9b70d9d ts=2026-10-06T18:54:21.1870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[1] _id=6ac3f106de269131f9af62cb ts=2026-10-05T18:48:36.7760000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[8] _id=6ac53fcade269131f9b698e5 ts=2026-10-06T18:36:58.0450000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[604] _id=6ac5475fde269131f9b76483 ts=2026-10-06T19:09:18.9080000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 15 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 15} 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[0] _id=6ac3f105de269131f9af62c5 ts=2026-10-05T18:48:36.7740000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[9] _id=6ac53fcade269131f9b698e1 ts=2026-10-06T18:36:58.0430000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[605] _id=6ac5475fde269131f9b7647f ts=2026-10-06T19:09:18.9050000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 8 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 8} 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[2] _id=6ac3f135de269131f9af64b1 ts=2026-10-05T18:49:24.2350000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[1504] _id=6ac69333de269131f9bdfc74 ts=2026-10-06T19:17:42.939Z`; `6ab9a9279a8420a1e6b56b75.jsonl[4736] _id=6ac7ea56de269131f9c64c7d ts=2026-10-08T19:09:09.1710000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 15 of 60 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[733] _id=6ac54841de269131f9b7760b ts=2026-10-06T19:13:04.3290000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[738] _id=6ac54846de269131f9b776eb ts=2026-10-06T19:13:09.2050000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[744] _id=6ac54854de269131f9b778dd ts=2026-10-06T19:13:23.8250000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3839 | 0.0 | 0.063 | 276.1 | 1.479 | 429999.831 | 0.22 | 1687 | 7 |
| InputEvent | 3634 | 0.0 | 1.052 | 293.214 | 19.767 | 429961.787 | 0.2 | 76 | 9 |
| PlayerPositionEvent | 2319 | 0.0 | 10.0 | 367.0 | 10.084 | 429589.323 | 0.16 | 1 | 6 |
| DialogueEvent | 2215 | 0.0 | 4.565 | 481.031 | 37.443 | 429596.855 | 0.12 | 604 | 9 |
| argumentationNodeEvent | 337 | 0.004 | 0.736 | 3153.111 | 8.929 | 638027.163 | 0.02 | 21 | 4 |
| ObjectInterEvent | 295 | 0.0 | 12.103 | 3610.864 | 498.265 | 432560.925 | 0.02 | 3 | 15 |
| questEvent | 83 | 0.0 | 205.702 | 12830.674 | 84126.113 | 429748.213 | 0.0 | 16 | 19 |
| TopographicMapEvent | 59 | 0.021 | 7.518 | 13185.423 | 84864.664 | 432462.255 | 0.0 | 2 | 8 |
| Soil Key Puzzle | 53 | 0.31 | 1.531 | 12901.914 | 10.758 | 604418.015 | 0.0 | 0 | 2 |
| WaterChamberEvent | 33 | 2.513 | 20.241 | 32.734 | 92.531 | 114.865 | 1.83 | 0 | 0 |
| DEBUGMenu | 27 | 6.482 | 971.686 | 39312.726 | 176924.635 | 429994.652 | 0.0 | 0 | 16 |
| argumentationAnswerEvent | 19 | 0.916 | 15.012 | 55922.465 | 317609.18 | 638065.156 | 0.0 | 0 | 4 |
| soilMachine | 18 | 0.369 | 14.927 | 10776.478 | 29976.069 | 192182.713 | 0.01 | 0 | 2 |
| DaniEvent | 15 | 0.811 | 1.896 | 145.699 | 636.473 | 1990.952 | 0.41 | 0 | 1 |
| gameWindowFocusEvent | 14 | 1321.959 | 56105.989 | 82218.92 | 276261.731 | 430006.867 | 0.0 | 0 | 14 |
| argumentationEvent | 13 | 0.074 | 100.628 | 81734.619 | 424351.645 | 638010.343 | 0.0 | 0 | 4 |
| argumentationToolEvent | 13 | 3.444 | 12.99 | 81733.043 | 426666.712 | 638070.76 | 0.0 | 0 | 3 |
| gameStartEvent | 12 | 1321.958 | 82727.229 | 95596.096 | 299914.829 | 430006.867 | 0.0 | 0 | 12 |
| SolarStillDesignEvent | 10 | 0.001 | 4.023 | 9.342 | 33.568 | 53.316 | 6.42 | 2 | 0 |
| TerasGardenBox | 10 | 0.828 | 2.469 | 15.854 | 47.446 | 47.746 | 3.78 | 0 | 0 |
| gameWindowUnfocusEvent | 7 | 190.233 | 172286.232 | 164430.822 | 377630.275 | 431822.622 | 0.0 | 0 | 5 |
| EndOfUnit | 4 | 4125.189 | 210668.299 | 265925.955 | 584656.206 | 638242.036 | 0.0 | 0 | 4 |
| chatEvent | 1 | 1674.795 | 1674.795 | 1674.795 | 1674.795 | 1674.795 | 0.04 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 6 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[1508] _id=6ac69341de269131f9bdfede ts=2026-10-07T18:45:19.3390000Z == 6ab9a9279a8420a1e6b56b75.jsonl[1509] _id=6ac69341de269131f9bdfedf ts=2026-10-07T18:45:19.3390000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[4887] _id=6ace7a75de269131f9d0fdd8 ts=2026-10-13T18:37:40.1170000Z == 6ab9a9279a8420a1e6b56b75.jsonl[4888] _id=6ace7a75de269131f9d0fdd9 ts=2026-10-13T18:37:40.1170000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[8567] _id=6ad25798de269131f9e649e3 ts=2026-10-16T16:57:59.1500000Z == 6ab9a9279a8420a1e6b56b75.jsonl[8568] _id=6ad25798de269131f9e649e4 ts=2026-10-16T16:57:59.1500000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 64 group(s), 91 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[677] _id=6ac54823de269131f9b77253 ts=2026-10-06T19:12:33.3700000Z == 6ab9a9279a8420a1e6b56b75.jsonl[679] _id=6ac54823de269131f9b7725f ts=2026-10-06T19:12:33.3700000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[683] _id=6ac54823de269131f9b77261 ts=2026-10-06T19:12:33.5420000Z == 6ab9a9279a8420a1e6b56b75.jsonl[690] _id=6ac54823de269131f9b77265 ts=2026-10-06T19:12:33.5420000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[695] _id=6ac54824de269131f9b77287 ts=2026-10-06T19:12:34.0300000Z == 6ab9a9279a8420a1e6b56b75.jsonl[699] _id=6ac54824de269131f9b7728d ts=2026-10-06T19:12:34.0300000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[617] _id=6ac5477bde269131f9b766bd ts=? == 6ab9a9279a8420a1e6b56b75.jsonl[3515] _id=6ac7e594de269131f9c58a68 ts=?`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[12738] _id=6ad57cacde269131f9e93131 ts=2026-10-19T02:12:59.7590000Z == 6ab9a9279a8420a1e6b56b75.jsonl[12739] _id=6ad57cacde269131f9e93132 ts=2026-10-19T02:12:59.7590000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b75.jsonl[112] _id=6ac5412ede269131f9b6c2cf ts=2026-10-06T18:42:53.9980000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[110] _id=6ac5412fde269131f9b6c2db ts=2026-10-06T18:42:54.0030000Z`; `495ms: 6ab9a9279a8420a1e6b56b75.jsonl[9880] _id=6ad27335de269131f9e7784d ts=2026-10-16T18:55:48.8170000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[9878] _id=6ad27335de269131f9e77858 ts=2026-10-16T18:55:49.3120000Z`; `369ms: 6ab9a9279a8420a1e6b56b75.jsonl[9878] _id=6ad27335de269131f9e77858 ts=2026-10-16T18:55:49.3120000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[9872] _id=6ad27335de269131f9e77870 ts=2026-10-16T18:55:49.6810000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 102 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `337ms: 6ab9a9279a8420a1e6b56b75.jsonl[694] _id=6ac54824de269131f9b7727f ts=2026-10-06T19:12:33.6930000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[695] _id=6ac54824de269131f9b77287 ts=2026-10-06T19:12:34.0300000Z`; `279ms: 6ab9a9279a8420a1e6b56b75.jsonl[699] _id=6ac54824de269131f9b7728d ts=2026-10-06T19:12:34.0300000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[680] _id=6ac54824de269131f9b77291 ts=2026-10-06T19:12:34.3090000Z`; `56ms: 6ab9a9279a8420a1e6b56b75.jsonl[697] _id=6ac54826de269131f9b772d0 ts=2026-10-06T19:12:34.4740000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[686] _id=6ac54826de269131f9b772d3 ts=2026-10-06T19:12:34.5300000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `868ms: 6ab9a9279a8420a1e6b56b75.jsonl[11390] _id=6ad56fc1de269131f9e91014 ts=2026-10-19T01:17:52.9160000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[11391] _id=6ad56fc2de269131f9e9101a ts=2026-10-19T01:17:53.7840000Z`; `828ms: 6ab9a9279a8420a1e6b56b75.jsonl[11391] _id=6ad56fc2de269131f9e9101a ts=2026-10-19T01:17:53.7840000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[11399] _id=6ad56fc3de269131f9e9101e ts=2026-10-19T01:17:54.6120000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `979ms: 6ab9a9279a8420a1e6b56b75.jsonl[11127] _id=6ad56dcbde269131f9e90b65 ts=2026-10-19T01:09:30.5510000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[11128] _id=6ad56dccde269131f9e90b6b ts=2026-10-19T01:09:31.5300000Z`; `916ms: 6ab9a9279a8420a1e6b56b75.jsonl[11160] _id=6ad56dd4de269131f9e90b97 ts=2026-10-19T01:09:39.6860000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[11159] _id=6ad56dd5de269131f9e90ba6 ts=2026-10-19T01:09:40.6020000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `74ms: 6ab9a9279a8420a1e6b56b75.jsonl[7084] _id=6ad1200ede269131f9df55c8 ts=2026-10-15T18:48:45.6810000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[7060] _id=6ad1200ede269131f9df55d4 ts=2026-10-15T18:48:45.7550000Z`; `112ms: 6ab9a9279a8420a1e6b56b75.jsonl[11181] _id=6ad56e10de269131f9e90c84 ts=2026-10-19T01:10:39.9150000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[10978] _id=6ad56e10de269131f9e90c88 ts=2026-10-19T01:10:40.0270000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `119ms: 6ab9a9279a8420a1e6b56b75.jsonl[398] _id=6ac545b5de269131f9b72f05 ts=2026-10-06T19:02:12.1440000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[399] _id=6ac545b6de269131f9b72f09 ts=2026-10-06T19:02:12.2630000Z`; `302ms: 6ab9a9279a8420a1e6b56b75.jsonl[421] _id=6ac545b6de269131f9b72f13 ts=2026-10-06T19:02:13.5680000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[423] _id=6ac545b6de269131f9b72f21 ts=2026-10-06T19:02:13.8700000Z`; `382ms: 6ab9a9279a8420a1e6b56b75.jsonl[409] _id=6ac545b6de269131f9b72f1d ts=2026-10-06T19:02:13.7200000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[410] _id=6ac545b6de269131f9b72f27 ts=2026-10-06T19:02:14.1020000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a9279a8420a1e6b56b75.jsonl[4737] _id=6ac7ea60de269131f9c64d96 ts=2026-10-08T19:09:19.7140000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[4741] _id=6ac7eaadde269131f9c657d3 ts=2026-10-08T19:09:19.714Z`; `4ms: 6ab9a9279a8420a1e6b56b75.jsonl[12923] _id=6ad57f31de269131f9e933ef ts=2026-10-19T02:23:44.7470000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[12919] _id=6ad57f31de269131f9e933f1 ts=2026-10-19T02:23:44.7510000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `496ms: 6ab9a9279a8420a1e6b56b75.jsonl[9870] _id=6ad27335de269131f9e77849 ts=2026-10-16T18:55:48.8110000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[9877] _id=6ad27335de269131f9e77853 ts=2026-10-16T18:55:49.3070000Z`; `369ms: 6ab9a9279a8420a1e6b56b75.jsonl[9877] _id=6ad27335de269131f9e77853 ts=2026-10-16T18:55:49.3070000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[9871] _id=6ad27335de269131f9e7786a ts=2026-10-16T18:55:49.6760000Z`; `923ms: 6ab9a9279a8420a1e6b56b75.jsonl[9891] _id=6ad2733fde269131f9e7791b ts=2026-10-16T18:55:59.6220000Z ~ 6ab9a9279a8420a1e6b56b75.jsonl[9894] _id=6ad27340de269131f9e77936 ts=2026-10-16T18:56:00.5450000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b75.jsonl[4742] _id=6ac7eab9de269131f9c658fb ts=2026-10-08T19:10:48.8250000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4881] _id=6ace7a64de269131f9d0fce5 ts=2026-10-13T18:37:23.4770000Z; 53h 44m: 6ab9a9279a8420a1e6b56b75.jsonl[9171] _id=6ad26df3de269131f9e706bb ts=2026-10-16T18:33:23.4400000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10208] _id=6ad561b1de269131f9e8f43a ts=2026-10-19T00:17:52.8410000Z; 38h 25m: 6ab9a9279a8420a1e6b56b75.jsonl[5821] _id=6aceff11de269131f9d2b49a ts=2026-10-14T04:03:29.2030000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6400] _id=6ad11b62de269131f9dee82c ts=2026-10-15T18:28:49.3840000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 33m 10s 
  - Evidence: 33m 10s: 6ab9a9279a8420a1e6b56b75.jsonl[6834] _id=6ad11ea5de269131f9df212d ts=2026-10-15T18:42:44.4200000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7992] _id=6ad1266cde269131f9e03a56 ts=2026-10-15T19:15:55.3720000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b75.jsonl[4876] _id=6ac7ec58de269131f9c6873b ts=2026-10-08T19:17:43.2810000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4892] _id=6ace7a75de269131f9d0fddd ts=2026-10-13T18:37:40.1360000Z; 53h 19m: 6ab9a9279a8420a1e6b56b75.jsonl[10015] _id=6ad273f6de269131f9e785d7 ts=2026-10-16T18:59:01.9960000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10214] _id=6ad561bcde269131f9e8f444 ts=2026-10-19T00:18:03.9620000Z; 38h 3m: 6ab9a9279a8420a1e6b56b75.jsonl[6394] _id=6acf042dde269131f9d2b8fc ts=2026-10-14T04:25:17.1790000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6408] _id=6ad11b75de269131f9dee84b ts=2026-10-15T18:29:09.0220000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 604 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[11087] _id=6ad56da1de269131f9e90adc ts=2026-10-19T01:08:48.6360000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11108] _id=6ad56da1de269131f9e90add ts=2026-10-19T01:08:48.6360000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[11140] _id=6ad56dcbde269131f9e90b67 ts=2026-10-19T01:09:30.5670000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11141] _id=6ad56dcbde269131f9e90b68 ts=2026-10-19T01:09:30.5670000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[11169] _id=6ad56de4de269131f9e90bee ts=2026-10-19T01:09:55.6310000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11170] _id=6ad56de4de269131f9e90bef ts=2026-10-19T01:09:55.6310000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 177h 17m 
  - Evidence: 177h 17m: 6ab9a9279a8420a1e6b56b75.jsonl[603] _id=6ac5470bde269131f9b75e39 ts=2026-10-06T19:07:55.1170000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6391] _id=6acf042dde269131f9d2b8fa ts=2026-10-14T04:25:17.1530000Z; 78h 3m: 6ab9a9279a8420a1e6b56b75.jsonl[8162] _id=6ad1285bde269131f9e05303 ts=2026-10-15T19:24:10.5780000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11582] _id=6ad57206de269131f9e915bc ts=2026-10-19T01:27:33.7500000Z; 38h 58m: 6ab9a9279a8420a1e6b56b75.jsonl[6391] _id=6acf042dde269131f9d2b8fa ts=2026-10-14T04:25:17.1530000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[8162] _id=6ad1285bde269131f9e05303 ts=2026-10-15T19:24:10.5780000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b75.jsonl[4780] _id=6ac7eaebde269131f9c65dfb ts=2026-10-08T19:11:38.3280000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4886] _id=6ace7a75de269131f9d0fdd7 ts=2026-10-13T18:37:40.1150000Z; 53h 19m: 6ab9a9279a8420a1e6b56b75.jsonl[10008] _id=6ad273dcde269131f9e784b8 ts=2026-10-16T18:58:36.5300000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10202] _id=6ad561d7de269131f9e8f45b ts=2026-10-19T00:18:31.2080000Z; 38h 7m: 6ab9a9279a8420a1e6b56b75.jsonl[6367] _id=6acf03f3de269131f9d2b8d0 ts=2026-10-14T04:24:18.8600000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6440] _id=6ad11bfdde269131f9dee9ee ts=2026-10-15T18:31:24.7830000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 76 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[10810] _id=6ad56b6ade269131f9e905e0 ts=2026-10-19T00:59:22.1680000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10811] _id=6ad56b6ade269131f9e905e1 ts=2026-10-19T00:59:22.1680000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[1508] _id=6ac69341de269131f9bdfede ts=2026-10-07T18:45:19.3390000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[1509] _id=6ac69341de269131f9bdfedf ts=2026-10-07T18:45:19.3390000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[4887] _id=6ace7a75de269131f9d0fdd8 ts=2026-10-13T18:37:40.1170000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4888] _id=6ace7a75de269131f9d0fdd9 ts=2026-10-13T18:37:40.1170000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 120h 9m 
  - Evidence: 120h 9m: 6ab9a9279a8420a1e6b56b75.jsonl[4440] _id=6ac7e96dde269131f9c61cc9 ts=2026-10-08T19:05:16.0200000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[5685] _id=6ace831dde269131f9d1a8b6 ts=2026-10-13T19:14:36.9450000Z; 53h 19m: 6ab9a9279a8420a1e6b56b75.jsonl[10010] _id=6ad273dfde269131f9e784dc ts=2026-10-16T18:58:39.4510000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10206] _id=6ad561ddde269131f9e8f466 ts=2026-10-19T00:18:36.5080000Z; 38h 17m: 6ab9a9279a8420a1e6b56b75.jsonl[6188] _id=6acf01e8de269131f9d2b75c ts=2026-10-14T04:15:36.1330000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6413] _id=6ad11c77de269131f9deecdb ts=2026-10-15T18:33:26.7700000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[10892] _id=6ad56bcfde269131f9e906fd ts=2026-10-19T01:01:03.0180000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10893] _id=6ad56bcfde269131f9e906fe ts=2026-10-19T01:01:03.0180000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[10937] _id=6ad56c27de269131f9e907d8 ts=2026-10-19T01:02:31.2950000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10938] _id=6ad56c27de269131f9e907d9 ts=2026-10-19T01:02:31.2950000Z; 5ms: 6ab9a9279a8420a1e6b56b75.jsonl[112] _id=6ac5412ede269131f9b6c2cf ts=2026-10-06T18:42:53.9980000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[110] _id=6ac5412fde269131f9b6c2db ts=2026-10-06T18:42:54.0030000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 19m 
  - Evidence: 119h 19m: 6ab9a9279a8420a1e6b56b75.jsonl[4874] _id=6ac7ec5ade269131f9c68779 ts=2026-10-08T19:17:45.8660000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4885] _id=6ace7a75de269131f9d0fdd6 ts=2026-10-13T18:37:35.1890000Z; 53h 18m: 6ab9a9279a8420a1e6b56b75.jsonl[10197] _id=6ad561b1de269131f9e8f438 ts=2026-10-16T18:59:25.4Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10212] _id=6ad561bcde269131f9e8f442 ts=2026-10-19T00:18:02.1100000Z; 23h 31m: 6ab9a9279a8420a1e6b56b75.jsonl[3507] _id=6ac69abbde269131f9bf2090 ts=2026-10-07T19:17:14.2780000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[3513] _id=6ac7e591de269131f9c58a36 ts=2026-10-08T18:48:45.4330000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[10017] _id=6ad2740dde269131f9e7864d ts=2026-10-16T18:59:25.4000000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10197] _id=6ad561b1de269131f9e8f438 ts=2026-10-16T18:59:25.4Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b75.jsonl[4757] _id=6ac7eacfde269131f9c65ad7 ts=2026-10-08T19:11:09.9120000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4877] _id=6ace7a80de269131f9d0fe9f ts=2026-10-13T18:37:49.7430000Z; 55h 49m: 6ab9a9279a8420a1e6b56b75.jsonl[9072] _id=6ad25820de269131f9e65340 ts=2026-10-16T17:00:14.0750000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10548] _id=6ad56919de269131f9e8ff7a ts=2026-10-19T00:49:27.3760000Z; 48h 17m: 6ab9a9279a8420a1e6b56b75.jsonl[4934] _id=6ace7a84de269131f9d0ff79 ts=2026-10-13T18:37:54.9740000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7228] _id=6ad121a6de269131f9df8345 ts=2026-10-15T18:55:32.5350000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1687 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[1000] _id=6ac548b6de269131f9b785b1 ts=2026-10-06T19:14:59.9790000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[1008] _id=6ac548b6de269131f9b785b9 ts=2026-10-06T19:14:59.9790000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[10548] _id=6ad56919de269131f9e8ff7a ts=2026-10-19T00:49:27.3760000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10553] _id=6ad56919de269131f9e8ff7c ts=2026-10-19T00:49:27.3760000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[10549] _id=6ad56919de269131f9e8ff84 ts=2026-10-19T00:49:28.0400000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10557] _id=6ad56919de269131f9e8ff86 ts=2026-10-19T00:49:28.0400000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 167h 53m 
  - Evidence: 167h 53m: 6ab9a9279a8420a1e6b56b75.jsonl[3797] _id=6ac7e86cde269131f9c5ee06 ts=2026-10-08T19:00:59.7780000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7202] _id=6ad1216ede269131f9df7c98 ts=2026-10-15T18:54:37.7930000Z; 22h 1m: 6ab9a9279a8420a1e6b56b75.jsonl[7212] _id=6ad1217dde269131f9df7e78 ts=2026-10-15T18:54:52.7000000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[8234] _id=6ad2571ade269131f9e63fee ts=2026-10-16T16:55:53.4360000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.001s..0.006s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b75.jsonl[12841] _id=6ad57e8dde269131f9e93310 ts=2026-10-19T02:21:00.4910000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12842] _id=6ad57e8dde269131f9e93311 ts=2026-10-19T02:21:00.4920000Z; 6ms: 6ab9a9279a8420a1e6b56b75.jsonl[12840] _id=6ad57e8dde269131f9e9330e ts=2026-10-19T02:21:00.4850000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12841] _id=6ad57e8dde269131f9e93310 ts=2026-10-19T02:21:00.4910000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 7m 
  - Evidence: 120h 7m: 6ab9a9279a8420a1e6b56b75.jsonl[3551] _id=6ac7e606de269131f9c595fb ts=2026-10-08T18:50:45.8990000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[5190] _id=6ace7f54de269131f9d1369f ts=2026-10-13T18:58:28.1540000Z; 47h 20m: 6ab9a9279a8420a1e6b56b75.jsonl[5537] _id=6ace82a9de269131f9d193aa ts=2026-10-13T19:12:41.0420000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6472] _id=6ad11c64de269131f9deec12 ts=2026-10-15T18:33:08.0740000Z; 23h 36m: 6ab9a9279a8420a1e6b56b75.jsonl[3449] _id=6ac699e0de269131f9bf0cbf ts=2026-10-07T19:13:35.8690000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[3544] _id=6ac7e5f9de269131f9c593d1 ts=2026-10-08T18:50:32.5380000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.021s..0.022s shown 
  - Evidence: 21ms: 6ab9a9279a8420a1e6b56b75.jsonl[3265] _id=6ac6979ede269131f9becf9b ts=2026-10-07T19:03:57.8210000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[3269] _id=6ac6979ede269131f9becf9f ts=2026-10-07T19:03:57.8420000Z; 22ms: 6ab9a9279a8420a1e6b56b75.jsonl[3264] _id=6ac6979ede269131f9becf97 ts=2026-10-07T19:03:57.7990000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[3265] _id=6ac6979ede269131f9becf9b ts=2026-10-07T19:03:57.8210000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 177h 14m 
  - Evidence: 177h 14m: 6ab9a9279a8420a1e6b56b75.jsonl[470] _id=6ac54631de269131f9b73b85 ts=2026-10-06T19:04:16.6060000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6253] _id=6acf02a2de269131f9d2b7ea ts=2026-10-14T04:18:41.7620000Z; 78h 20m: 6ab9a9279a8420a1e6b56b75.jsonl[7087] _id=6ad1200ede269131f9df55c3 ts=2026-10-15T18:48:45.6550000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11094] _id=6ad56da1de269131f9e90ad8 ts=2026-10-19T01:08:48.6150000Z; 38h 28m: 6ab9a9279a8420a1e6b56b75.jsonl[6314] _id=6acf0301de269131f9d2b856 ts=2026-10-14T04:20:16.8760000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7087] _id=6ad1200ede269131f9df55c3 ts=2026-10-15T18:48:45.6550000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 177h 13m 
  - Evidence: 177h 13m: 6ab9a9279a8420a1e6b56b75.jsonl[481] _id=6ac54631de269131f9b73b8f ts=2026-10-06T19:04:16.6390000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6209] _id=6acf026bde269131f9d2b7ac ts=2026-10-14T04:17:46.9820000Z; 78h 18m: 6ab9a9279a8420a1e6b56b75.jsonl[7060] _id=6ad1200ede269131f9df55d4 ts=2026-10-15T18:48:45.7550000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11020] _id=6ad56d46de269131f9e909db ts=2026-10-19T01:07:18.2680000Z; 38h 27m: 6ab9a9279a8420a1e6b56b75.jsonl[6306] _id=6acf0301de269131f9d2b858 ts=2026-10-14T04:20:16.9060000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7033] _id=6ad11fc4de269131f9df4bcc ts=2026-10-15T18:47:31.8290000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 177h 13m 
  - Evidence: 177h 13m: 6ab9a9279a8420a1e6b56b75.jsonl[476] _id=6ac54628de269131f9b73a1f ts=2026-10-06T19:04:07.6950000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6227] _id=6acf0273de269131f9d2b7b3 ts=2026-10-14T04:17:54.8580000Z; 78h 18m: 6ab9a9279a8420a1e6b56b75.jsonl[7079] _id=6ad12003de269131f9df547a ts=2026-10-15T18:48:34.5300000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11019] _id=6ad56d45de269131f9e909d3 ts=2026-10-19T01:07:16.6110000Z; 38h 27m: 6ab9a9279a8420a1e6b56b75.jsonl[6313] _id=6acf0300de269131f9d2b854 ts=2026-10-14T04:20:15.5720000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7037] _id=6ad11fc8de269131f9df4c28 ts=2026-10-15T18:47:35.8820000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 21 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6ab9a9279a8420a1e6b56b75.jsonl[11053] _id=6ad56d6bde269131f9e90a2e ts=2026-10-19T01:07:55.1600000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[11047] _id=6ad56d6bde269131f9e90a30 ts=2026-10-19T01:07:55.1640000Z; 4ms: 6ab9a9279a8420a1e6b56b75.jsonl[12663] _id=6ad57c26de269131f9e92ffd ts=2026-10-19T02:10:45.9750000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12674] _id=6ad57c26de269131f9e92fff ts=2026-10-19T02:10:45.9790000Z; 5ms: 6ab9a9279a8420a1e6b56b75.jsonl[12615] _id=6ad57bf5de269131f9e92f94 ts=2026-10-19T02:09:56.6610000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12616] _id=6ad57bf5de269131f9e92f96 ts=2026-10-19T02:09:56.6660000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 177h 14m 
  - Evidence: 177h 14m: 6ab9a9279a8420a1e6b56b75.jsonl[472] _id=6ac54628de269131f9b73a0d ts=2026-10-06T19:04:07.4920000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6240] _id=6acf029ede269131f9d2b7e8 ts=2026-10-14T04:18:38.2520000Z; 79h 22m: 6ab9a9279a8420a1e6b56b75.jsonl[7081] _id=6ad12009de269131f9df5517 ts=2026-10-15T18:48:40.6310000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12679] _id=6ad57c2cde269131f9e93017 ts=2026-10-19T02:10:51.3110000Z; 38h 29m: 6ab9a9279a8420a1e6b56b75.jsonl[6263] _id=6acf02b9de269131f9d2b806 ts=2026-10-14T04:19:04.6970000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[7082] _id=6ad12006de269131f9df54cd ts=2026-10-15T18:48:37.1870000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 27m 54s 
  - Evidence: 27m 54s: 6ab9a9279a8420a1e6b56b75.jsonl[11586] _id=6ad57221de269131f9e91605 ts=2026-10-19T01:28:01.0180000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12421] _id=6ad578acde269131f9e9261e ts=2026-10-19T01:55:55.8130000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b75.jsonl[4740] _id=6ac7eaaede269131f9c657f1 ts=2026-10-08T19:10:36.9140000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4883] _id=6ace7a64de269131f9d0fce7 ts=2026-10-13T18:37:23.7810000Z; 53h 44m: 6ab9a9279a8420a1e6b56b75.jsonl[9169] _id=6ad26dedde269131f9e70620 ts=2026-10-16T18:33:17.0930000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10210] _id=6ad561b1de269131f9e8f43c ts=2026-10-19T00:17:52.9810000Z; 38h 25m: 6ab9a9279a8420a1e6b56b75.jsonl[5837] _id=6aceff06de269131f9d2b498 ts=2026-10-14T04:03:17.8010000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6402] _id=6ad11b62de269131f9dee831 ts=2026-10-15T18:28:49.5530000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 26m 
  - Evidence: 119h 26m: 6ab9a9279a8420a1e6b56b75.jsonl[4739] _id=6ac7eaaede269131f9c657f0 ts=2026-10-08T19:10:36.9140000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4882] _id=6ace7a64de269131f9d0fce6 ts=2026-10-13T18:37:23.7810000Z; 53h 44m: 6ab9a9279a8420a1e6b56b75.jsonl[9168] _id=6ad26dedde269131f9e7061f ts=2026-10-16T18:33:17.0920000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10209] _id=6ad561b1de269131f9e8f43b ts=2026-10-19T00:17:52.9810000Z; 38h 25m: 6ab9a9279a8420a1e6b56b75.jsonl[5836] _id=6aceff06de269131f9d2b497 ts=2026-10-14T04:03:17.8010000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6401] _id=6ad11b62de269131f9dee830 ts=2026-10-15T18:28:49.5530000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 57m 
  - Evidence: 119h 57m: 6ab9a9279a8420a1e6b56b75.jsonl[4880] _id=6ace7a63de269131f9d0fce3 ts=2026-10-08T19:17:49.712Z -> 6ab9a9279a8420a1e6b56b75.jsonl[5692] _id=6ace832cde269131f9d1ab1e ts=2026-10-13T19:14:52.3340000Z; 69h 46m: 6ab9a9279a8420a1e6b56b75.jsonl[5834] _id=6aceff06de269131f9d2b494 ts=2026-10-13T19:18:02.567Z -> 6ab9a9279a8420a1e6b56b75.jsonl[9166] _id=6ad26dedde269131f9e7061c ts=2026-10-16T17:04:24.032Z; 57h 28m: 6ab9a9279a8420a1e6b56b75.jsonl[9166] _id=6ad26dedde269131f9e7061c ts=2026-10-16T17:04:24.032Z -> 6ab9a9279a8420a1e6b56b75.jsonl[13038] _id=6ad5815cde269131f9e93542 ts=2026-10-19T02:32:59.9900000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6ab9a9279a8420a1e6b56b75.jsonl[4845] _id=6ac7ebc1de269131f9c675b3 ts=2026-10-08T19:15:11.9700000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4894] _id=6ace7a75de269131f9d0fddf ts=2026-10-13T18:37:40.1830000Z; 53h 25m: 6ab9a9279a8420a1e6b56b75.jsonl[9720] _id=6ad27272de269131f9e76956 ts=2026-10-16T18:52:33.7530000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10213] _id=6ad561bcde269131f9e8f443 ts=2026-10-19T00:18:03.7360000Z; 38h 5m: 6ab9a9279a8420a1e6b56b75.jsonl[6388] _id=6acf0426de269131f9d2b8f2 ts=2026-10-14T04:25:10.2670000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[6434] _id=6ad11beede269131f9dee9b7 ts=2026-10-15T18:31:09.5810000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[12738] _id=6ad57cacde269131f9e93131 ts=2026-10-19T02:12:59.7590000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[12739] _id=6ad57cacde269131f9e93132 ts=2026-10-19T02:12:59.7590000Z; 0ms: 6ab9a9279a8420a1e6b56b75.jsonl[4737] _id=6ac7ea60de269131f9c64d96 ts=2026-10-08T19:09:19.7140000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[4741] _id=6ac7eaadde269131f9c657d3 ts=2026-10-08T19:09:19.714Z; 2ms: 6ab9a9279a8420a1e6b56b75.jsonl[367] _id=6ac5455ede269131f9b7280f ts=2026-10-06T19:00:44.9290000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[368] _id=6ac5455ede269131f9b72815 ts=2026-10-06T19:00:44.9310000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 53h 23m 
  - Evidence: 53h 23m: 6ab9a9279a8420a1e6b56b75.jsonl[10007] _id=6ad273dade269131f9e784a1 ts=2026-10-16T18:58:34.0170000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10311] _id=6ad56291de269131f9e8f565 ts=2026-10-19T00:21:36.7300000Z; 22m 31s: 6ab9a9279a8420a1e6b56b75.jsonl[10095] _id=6ad56328de269131f9e8f657 ts=2026-10-19T00:24:07.4640000Z -> 6ab9a9279a8420a1e6b56b75.jsonl[10435] _id=6ad5686fde269131f9e8fdbb ts=2026-10-19T00:46:38.8310000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[362] _id=6ac54546de269131f9b725b3 ts=2026-10-06T19:00:21.8830000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[489] _id=6ac54646de269131f9b73e7c ts=2026-10-06T19:04:37.0680000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[3434] _id=6ac699a2de269131f9bf08cd ts=2026-10-07T19:12:33.1550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 18 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[927] _id=6ac548a1de269131f9b7821b ts=2026-10-06T19:14:37.3240000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[941] _id=6ac548a1de269131f9b78221 ts=2026-10-06T19:14:37.4130000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[937] _id=6ac548a1de269131f9b78227 ts=2026-10-06T19:14:37.4130000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 78 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[695] _id=6ac54824de269131f9b77287 ts=2026-10-06T19:12:34.0300000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[699] _id=6ac54824de269131f9b7728d ts=2026-10-06T19:12:34.0300000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[680] _id=6ac54824de269131f9b77291 ts=2026-10-06T19:12:34.3090000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[7060] _id=6ad1200ede269131f9df55d4 ts=2026-10-15T18:48:45.7550000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[10978] _id=6ad56e10de269131f9e90c88 ts=2026-10-19T01:10:40.0270000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[399] _id=6ac545b6de269131f9b72f09 ts=2026-10-06T19:02:12.2630000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[11586] _id=6ad57221de269131f9e91605 ts=2026-10-19T01:28:01.0180000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[12421] _id=6ad578acde269131f9e9261e ts=2026-10-19T01:55:55.8130000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[10218] _id=6ad561cdde269131f9e8f451 ts=2026-10-19T00:18:20.9120000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[617] _id=6ac5477bde269131f9b766bd ts=?`; `6ab9a9279a8420a1e6b56b75.jsonl[3515] _id=6ac7e594de269131f9c58a68 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 197 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[1040] _id=6ac548bcde269131f9b786a5 ts=2026-10-06T19:15:06.0710000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[1043] _id=6ac548bdde269131f9b786d6 ts=2026-10-06T19:15:06.3660000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[1006] _id=6ac548bdde269131f9b786d9 ts=2026-10-06T19:15:06.5880000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 661 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[679] _id=6ac54823de269131f9b7725f ts=2026-10-06T19:12:33.3700000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[683] _id=6ac54823de269131f9b77261 ts=2026-10-06T19:12:33.5420000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[690] _id=6ac54823de269131f9b77265 ts=2026-10-06T19:12:33.5420000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[453] _id=6ac5460bde269131f9b73611 ts=2026-10-06T19:03:38.8200000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[474] _id=6ac54624de269131f9b73976 ts=2026-10-06T19:04:03.5060000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[6262] _id=6acf02b5de269131f9d2b802 ts=2026-10-14T04:19:00.7500000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 404 start, 398 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 17 unmatched 'BecameCameraCentered' (totals: 697 open, 698 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 55 unmatched 'BecameVisible' (totals: 1211 open, 1234 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 8 unmatched 'argumentationToolOpen' (totals: 11 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'questActiveEvent' (totals: 47 start, 37 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 376 of 13063 adjacent _id pairs reverse in client time; worst 110.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b75.jsonl[806] _id=6ac54892de269131f9b77f89 ts=2026-10-06T19:14:25.4830000Z`; `6ab9a9279a8420a1e6b56b75.jsonl[799] _id=6ac54893de269131f9b77f99 ts=2026-10-06T19:12:35.2530000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.82s, min -429574.14s, max -0.17s over 13064 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b75\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3840 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2738); Unit 4 Dev (714); Unit 5 Dev - Dungeon (258); Unit 3 Dungeon Dev (130)
- **Intervals:** median 0.06s (p5 0.00s / p95 1.48s, n=3839)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3840/3840 records)
    "BecameInvisible"  x1234
    "BecameVisible"  x1211
    "BecameCameraUncentered"  x698
    "BecameCameraCentered"  x697
data.pieceId  (string, 3840/3840 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3840/3840 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3635 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1274); Unit 4 Dev - Dungeon (764); Unit 3 Dev (445); Unit 3 Dungeon Dev (301); Unit 5 Dev - Dungeon (280); Unit 4 Dev (258); Unit 4 Dev - Anderson Base (127); Unit 1 Dev (106); Unit 5 Dev (80)
- **Intervals:** median 1.05s (p5 0.12s / p95 19.77s, n=3634)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3635/3635 records)
    "pressed"  x3635
data.actionType  (string, 3635/3635 records)
    "Move"  x2926
    "Interact"  x421
    "Sprint"  x105
    "Ascend"  x87
    "Jump"  x68
    "Hoverboard"  x24
    "Pause"  x4
data.key  (string, 3635/3635 records, 6 empty-string)
    15 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3635/3635 records)
    "Player"  x2610
    "Drone"  x1025
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2331 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (770); Unit 4 Dev - Dungeon (363); Unit 5 Dev (233); Unit 3 Dev (216); Unit 4 Dev (213); Unit 1 Dev (183); Unit 5 Dev - Dungeon (165); Unit 3 Dungeon Dev (108); Unit 4 Dev - Anderson Base (80)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.08s, n=2319)
- **Fields under `data`:**

```text
data.position  (object, 2331/2331 records)
data.position.x  (number, 2331/2331 records)
    numeric range -700.06 .. 1557.72 (728 unique)
data.position.y  (number, 2331/2331 records)
    numeric range -113.648 .. 222.898 (515 unique)
data.position.z  (number, 2331/2331 records)
    numeric range -1195.8 .. 2195.41 (731 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2216 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (764); Unit 3 Dev (292); Unit 4 Dev (255); Unit 5 Dev (228); Unit 1 Dev (212); Unit 4 Dev - Dungeon (159); Unit 3 Dungeon Dev (128); Unit 4 Dev - Anderson Base (97); Unit 5 Dev - Dungeon (81)
- **eventKey:** present on 1414 of 2216 records
- **Intervals:** median 4.57s (p5 0.00s / p95 37.44s, n=2215)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1414; [conversationId, dialogueEventType] x802
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2216/2216 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2216/2216 records)
    "DialogueNodeEvent"  x1414
    "DialogueStartEvent"  x404
    "DialogueFinishEvent"  x398
data.nodeId  (number, 1414/2216 records)
    numeric range 0 .. 290 (231 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 338 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (127); Unit 5 Dev (68); Unit 2 Prod (Refactor) (57); Unit 1 Dev (51); Unit 3 Dev (35)
- **Intervals:** median 0.74s (p5 0.05s / p95 8.93s, n=337)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 338/338 records)
    "argumentationNodeHoverEnd"  x147
    "argumentationNodeHoverStart"  x146
    "argumentationNodeAdd"  x32
    "argumentationNodeRemove"  x13
data.argumentationTitle  (string, 338/338 records)
    "Unit 4 - Flooding"  x127
    "Unit 5"  x68
    "Unit 2 – Watershed"  x57
    "Unit 3 - Pollution Upstream"  x35
    "Unit 1 - Argumentation Tutorial"  x28
    "Unit 1 - Freshwater"  x23
data.nodeName  (string, 338/338 records)
    "A"  x52
    "C"  x50
    "D"  x44
    "I"  x39
    "1"  x35
    "2"  x33
    "B"  x28
    "II"  x21
    "4"  x16
    "3"  x15
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 296 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (118); Unit 2 Prod (Refactor) (71); Unit 3 Dungeon Dev (32); Unit 4 Dev (25); Unit 3 Dev (11); Unit 5 Dev (11); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (9)
- **Intervals:** median 12.10s (p5 2.63s / p95 498.26s, n=295)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 296/296 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 296/296 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 4 Dev - Dungeon (16); Unit 1 Dev (12); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 205.70s (p5 0.01s / p95 84126.11s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x47; [questEventType, questID, questName, questSuccessOrFailure] x37
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x47
    "questFinishEvent"  x37
data.questID  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 37/84 records)
    "Succeeded"  x37
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 60 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (40); Unit 3 Dev (18); Unit 3 Dungeon Dev (2)
- **Intervals:** median 7.52s (p5 0.94s / p95 84864.66s, n=59)
- **`data` key-set variants:** [actionType, featureUsed] x38; [actionType, featureUsed, legendName] x15; [actionType, featureUsed, location] x7
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 60/60 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
    "Selected"  x14
    "WaypointSetEvent"  x5
    "WaypointMoveEvent"  x2
    "Unselected"  x1
data.featureUsed  (string, 60/60 records)
    "Map"  x38
    "Legend"  x15
    "Waypoint"  x7
data.legendName  (string, 15/60 records)
    "0 ft"  x3
    "120 ft"  x2
    "150 ft"  x1
    "180 ft"  x1
    "240 ft"  x1
    "270 ft"  x1
    "30 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
    "60 ft"  x1
    "90 ft"  x1
    "Water"  x1
data.location  (object, 7/60 records)
data.location.x  (number, 7/60 records)
    7 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 7/60 records)
    6 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 7/60 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 54 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 4 Dev (18); Unit 3 Dev (10)
- **Intervals:** median 1.53s (p5 0.47s / p95 10.76s, n=53)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x48; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/54 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/54 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 48/54 records)
    "RightDrag"  x27
    "LeftDrag"  x21
data.currentSoilType  (string, 48/54 records)
    "CLAYSAND"  x12
    "SAND"  x11
    "CLAY"  x9
    "CLAYROCK"  x7
    "SANDGRAVEL"  x5
    "BEDROCK"  x2
    "GRAVEL"  x2
data.isCorrectSelection  (string, 48/54 records)
    "false"  x35
    "true"  x13
data.waterLevelStatus  (string, 48/54 records)
    "TooHigh"  x21
    "TooLow"  x17
    "Proper"  x10
data.waterRetentionChange  (string, 48/54 records)
    "Increase"  x21
    "Decrease"  x14
    "NoChange"  x13
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 34 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (34)
- **Intervals:** median 20.24s (p5 3.82s / p95 92.53s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "On"  x21
    "Off"  x13
data.floor  (string, 34/34 records)
    "4"  x16
    "3"  x9
    "1"  x5
    "2"  x4
data.machineNumber  (string, 34/34 records)
    "One"  x33
    "Two"  x1
data.machineType  (string, 34/34 records)
    "Condenser"  x15
    "Evaporator"  x14
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 34/34 records)
    "3"  x15
    "2"  x11
    "1"  x6
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (10); Unit 2 Prod (Refactor) (6); Unit 4 Dev (3); Unit 4 Dev - Dungeon (3); Unit 3 Dev (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 971.69s (p5 9.33s / p95 176924.63s, n=27)
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 20 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (11); Unit 2 Prod (Refactor) (3); Unit 5 Dev (3); Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 15.01s (p5 0.97s / p95 317609.18s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "submitAnswerEvent"  x20
data.answerSubmitted  (string, 20/20 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 20/20 records)
    "Unit 4 - Flooding"  x11
    "Unit 2 – Watershed"  x3
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `soilMachine` — 19 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (19)
- **Intervals:** median 14.93s (p5 0.48s / p95 29976.07s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "ChangeCanister"  x19
data.canisterType  (string, 19/19 records)
    "Bedrock"  x6
    "Clay"  x6
    "Gravel"  x4
    "Sand"  x3
data.floor  (string, 19/19 records)
    "5"  x14
    "4"  x4
    "3"  x1
data.machine  (string, 19/19 records)
    "1"  x15
    "2"  x4
data.row  (string, 19/19 records)
    "TopRow"  x12
    "BottomRow"  x7
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DaniEvent` — 16 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (16)
- **Intervals:** median 1.90s (p5 0.96s / p95 636.47s, n=15)
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "Close"  x8
    "Open"  x8
data.toolName  (string, 16/16 records, 16 empty-string)
    ""  x16
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowFocusEvent` — 15 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (13); Unit 2 Prod (Refactor) (1); Unit 5 Dev (1)
- **Intervals:** median 56105.99s (p5 1724.25s / p95 276261.73s, n=14)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 15/15 records)
    true  x15
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationEvent` — 14 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 100.63s (p5 0.10s / p95 424351.65s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x6
data.argumentationDescription  (string, 14/14 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 14/14 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 14 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 12.99s (p5 3.51s / p95 426666.71s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationToolOpen"  x11
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Freshwater"  x5
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
data.toolName  (string, 14/14 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
    "BackingInfoPanel - Pollution Site Data"  x1
    "BackingInfoPanel - Waterfall Data"  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameStartEvent` — 13 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (13)
- **Intervals:** median 82727.23s (p5 1662.36s / p95 299914.83s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    true  x13
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 4.02s (p5 0.00s / p95 33.57s, n=10)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x10; [actionType, designSelections, featureUsed] x1
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "optionSelected"  x10
    "DesignSubmitted"  x1
data.designSelections  (object, 1/11 records)
data.designSelections.glassRoofTemperature  (string, 1/11 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/11 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/11 records)
    "Tilted In"  x1
data.featureUsed  (string, 11/11 records)
    "GlassRoofTemperature"  x4
    "ExtraCovering"  x3
    "RoofStyle"  x3
    "Submit"  x1
data.selectedOption  (string, 10/11 records, 3 empty-string)
    ""  x3
    "Hot"  x2
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 2.47s (p5 0.85s / p95 47.45s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 4 empty-string)
    "cameraPlaced"  x7
    ""  x4
data.boxId  (string, 11/11 records)
    "1"  x5
    "0"  x4
    "2"  x2
data.soilType  (string, 11/11 records)
    "Sand"  x7
    "Clay"  x2
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `gameWindowUnfocusEvent` — 8 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); MainMenu (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev (1)
- **Intervals:** median 172286.23s (p5 289.33s / p95 377630.27s, n=7)
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
- **Intervals:** median 210668.30s (p5 24556.42s / p95 584656.21s, n=4)
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

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1674.80s (p5 1674.80s / p95 1674.80s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 2/2 records)
    true  x2
data.message  (string, 2/2 records)
    "A user gesture is required to request Pointer Lock."  x2
data.phase  (string, 2/2 records)
    "running"  x2
data.stack  (string, 2/2 records, 2 empty-string)
    ""  x2
data.type  (string, 2/2 records)
    "unhandled_rejection"  x2
data.unitId  (string, 2/2 records)
    "unit2"  x2
data.workspace  (string, 2/2 records)
    "mhs"  x2
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
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : median interval between records changed substantially
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (26 records)
- `TerasGardenBox` data.actionType: "" (4x)
- `TopographicMapEvent` data.actionType: "Selected" (14x); "Unselected" (1x); "WaypointMoveEvent" (2x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Legend" (15x); "Waypoint" (7x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (13x)
- `soilMachine` data.canisterType: "Bedrock" (6x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*