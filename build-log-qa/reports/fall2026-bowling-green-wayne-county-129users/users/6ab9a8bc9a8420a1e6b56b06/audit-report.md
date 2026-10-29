# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b06

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8bc9a8420a1e6b56b06
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b06.jsonl
- **Records:** 12405 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b06
- **Time span:** 2026-10-05T15:15:59.236000+00:00 .. 2026-10-16T15:35:03.267000+00:00 (264h 19m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b06\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 12405 records, 10 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 91 INFO, 0 NOT_TESTED, 103 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PlayerPositionEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5639 | 45.46 | 1 | 9 | 0 | 2026-10-05T15:19:32.647000+00:00 | 2026-10-16T15:35:03.267000+00:00 | 264h 15m |
| DialogueEvent | 2275 | 18.34 | 1 | 9 | 1475 | 2026-10-05T15:16:27.721000+00:00 | 2026-10-16T15:34:59.405000+00:00 | 264h 18m |
| PuzzlePieceVisibleEvent | 1750 | 14.11 | 1 | 4 | 0 | 2026-10-07T15:33:06.868000+00:00 | 2026-10-16T15:06:50.753000+00:00 | 215h 33m |
| PlayerPositionEvent | 1739 | 14.02 | 1 | 9 | 0 | 2026-10-05T15:16:08.002000+00:00 | 2026-10-16T15:34:57.317000+00:00 | 264h 18m |
| argumentationNodeEvent | 319 | 2.57 | 1 | 5 | 0 | 2026-10-06T15:45:25.191000+00:00 | 2026-10-16T15:23:39.896000+00:00 | 239h 38m |
| ObjectInterEvent | 222 | 1.79 | 1 | 9 | 0 | 2026-10-05T15:20:28.061000+00:00 | 2026-10-16T15:35:03.267000+00:00 | 264h 14m |
| TopographicMapEvent | 93 | 0.75 | 1 | 3 | 0 | 2026-10-05T15:22:24.920000+00:00 | 2026-10-14T15:55:23.408000+00:00 | 216h 32m |
| questEvent | 92 | 0.74 | 1 | 9 | 92 | 2026-10-05T15:16:27.696000+00:00 | 2026-10-16T15:31:12.073000+00:00 | 264h 14m |
| Soil Key Puzzle | 47 | 0.38 | 1 | 3 | 0 | 2026-10-07T15:37:14.365000+00:00 | 2026-10-15T15:12:51.021000+00:00 | 191h 35m |
| argumentationAnswerEvent | 34 | 0.27 | 1 | 5 | 0 | 2026-10-06T15:46:16.682000+00:00 | 2026-10-16T15:23:42.203000+00:00 | 239h 37m |
| DEBUGMenu | 30 | 0.24 | 1 | 9 | 0 | 2026-10-05T15:16:07.988000+00:00 | 2026-10-16T15:00:50.506000+00:00 | 263h 44m |
| WaterChamberEvent | 25 | 0.2 | 1 | 1 | 0 | 2026-10-16T15:06:58.833000+00:00 | 2026-10-16T15:15:14.305000+00:00 | 8m 15s |
| soilMachine | 21 | 0.17 | 1 | 1 | 0 | 2026-10-15T15:25:53.131000+00:00 | 2026-10-15T15:36:13.755000+00:00 | 10m 20s |
| gameWindowFocusEvent | 20 | 0.16 | 1 | 4 | 0 | 2026-10-05T15:15:59.236000+00:00 | 2026-10-16T15:00:39.645000+00:00 | 263h 44m |
| argumentationEvent | 18 | 0.15 | 1 | 5 | 0 | 2026-10-06T15:45:55.552000+00:00 | 2026-10-16T15:23:42.235000+00:00 | 239h 37m |
| SolarStillDesignEvent | 16 | 0.13 | 1 | 1 | 0 | 2026-10-16T15:27:35.465000+00:00 | 2026-10-16T15:28:09.753000+00:00 | 34.3s |
| gameStartEvent | 14 | 0.11 | 1 | 1 | 0 | 2026-10-05T15:15:59.237000+00:00 | 2026-10-16T15:00:39.645000+00:00 | 263h 44m |
| argumentationToolEvent | 12 | 0.1 | 1 | 2 | 0 | 2026-10-06T15:45:55.472000+00:00 | 2026-10-14T13:54:59.067000+00:00 | 190h 9m |
| gameWindowUnfocusEvent | 11 | 0.09 | 1 | 3 | 0 | 2026-10-05T15:32:02.241000+00:00 | 2026-10-14T15:18:10.296000+00:00 | 215h 46m |
| chatEvent | 10 | 0.08 | 1 | 3 | 0 | 2026-10-14T15:19:28.027000+00:00 | 2026-10-16T15:16:02.377000+00:00 | 47h 56m |
| TerasGardenBox | 9 | 0.07 | 1 | 1 | 0 | 2026-10-15T15:58:40.040000+00:00 | 2026-10-15T15:59:34.072000+00:00 | 54.0s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-07T15:27:52.564000+00:00 | 2026-10-16T15:35:03.236000+00:00 | 216h 7m |
| DaniEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-10-14T15:19:21.631000+00:00 | 2026-10-14T15:19:27.792000+00:00 | 6.2s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 85612.082s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.816s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.569s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 3.828s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 6.713s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 34.31s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 11.442s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 78139.249s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 994.72s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 42104.435s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 14.006s median 
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
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 16 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.8x vs baseline. 
  - Observed: 34 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,C,B,2,II; A,D,1,II; A,D,2,II; A,D,C,2,II; B,C,2,II; C,2,II; C,A,2,II; C,D,2,II; C,D,3,II; C,D,4,3,II 
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
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` — field(s) not present in baseline schema. 
  - Observed: data.actionKey
- **INFO / Info** `chatEvent` — record volume changed 5.0x vs baseline. 
  - Observed: 10 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open; ScrollStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-217, 10-218, 11-224, 11-226, 11-23]; [11-224, 11-226, 11-23, 11-24]; [11-23, 11-24, 11-28, 11-230, 11-26]; [11-29, 11-230, 11-230, 11-27, 11-27] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 20 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 11 records 
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

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 13 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[189] _id=6ac3c0c5de269131f9ad129d ts=2026-10-05T15:22:45.2490000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[287] _id=6ac3c20dde269131f9ad2ee7 ts=2026-10-05T15:28:13.5030000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[452] _id=6ac3c46fde269131f9ad5269 ts=2026-10-05T15:38:22.6010000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[1] _id=6ac3bf2fde269131f9ace72d ts=2026-10-05T15:15:59.2370000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[350] _id=6ac3c379de269131f9ad419f ts=2026-10-05T15:34:16.9600000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[661] _id=6ac512d5de269131f9b45a6b ts=2026-10-06T15:25:08.4800000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[2] _id=6ac3bf2fde269131f9ace72b ts=2026-10-05T15:15:59.2360000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[349] _id=6ac3c2f4de269131f9ad3a54 ts=2026-10-05T15:32:04.3930000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[351] _id=6ac3c379de269131f9ad419a ts=2026-10-05T15:34:16.9590000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 11 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 11} 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[347] _id=6ac3c2f2de269131f9ad3a3e ts=2026-10-05T15:32:02.2410000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[659] _id=6ac512d4de269131f9b45a65 ts=2026-10-05T15:48:03.205Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[676] _id=6ac512fbde269131f9b45b21 ts=2026-10-06T15:25:46.7070000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5638 | 0.0 | 0.405 | 168.735 | 5.127 | 432037.224 | 0.36 | 471 | 9 |
| DialogueEvent | 2274 | 0.0 | 4.04 | 418.431 | 28.151 | 431815.35 | 0.14 | 629 | 8 |
| PuzzlePieceVisibleEvent | 1749 | 0.0 | 0.034 | 443.696 | 1.275 | 432051.987 | 0.14 | 917 | 7 |
| PlayerPositionEvent | 1727 | 0.0 | 10.003 | 452.872 | 10.15 | 431780.41 | 0.13 | 2 | 5 |
| argumentationNodeEvent | 318 | 0.006 | 0.673 | 2712.876 | 13.36 | 599322.855 | 0.02 | 26 | 5 |
| ObjectInterEvent | 221 | 0.0 | 12.816 | 4304.413 | 426.776 | 511638.04 | 0.01 | 5 | 8 |
| TopographicMapEvent | 92 | 0.024 | 3.828 | 8473.679 | 37663.024 | 433549.235 | 0.01 | 4 | 8 |
| questEvent | 91 | 0.0 | 168.886 | 10453.674 | 82839.491 | 431815.46 | 0.01 | 18 | 14 |
| Soil Key Puzzle | 46 | 0.267 | 2.569 | 14994.275 | 64114.48 | 516491.371 | 0.0 | 0 | 5 |
| argumentationAnswerEvent | 33 | 0.074 | 6.713 | 26140.773 | 86093.08 | 599409.035 | 0.0 | 0 | 5 |
| DEBUGMenu | 29 | 9.714 | 562.555 | 32740.776 | 85976.158 | 433271.298 | 0.0 | 0 | 14 |
| WaterChamberEvent | 24 | 1.256 | 12.924 | 20.645 | 57.796 | 81.119 | 2.91 | 0 | 0 |
| soilMachine | 20 | 0.204 | 14.006 | 31.031 | 164.939 | 173.888 | 1.93 | 0 | 0 |
| gameWindowFocusEvent | 19 | 42.297 | 994.72 | 49972.653 | 120721.611 | 432327.328 | 0.0 | 0 | 14 |
| argumentationEvent | 17 | 0.042 | 70.536 | 50745.099 | 190079.182 | 599294.864 | 0.0 | 1 | 5 |
| SolarStillDesignEvent | 15 | 0.0 | 2.239 | 2.286 | 5.666 | 8.814 | 26.25 | 2 | 0 |
| gameStartEvent | 13 | 500.145 | 78139.249 | 73036.954 | 224973.136 | 433284.711 | 0.0 | 0 | 11 |
| argumentationToolEvent | 11 | 2.25 | 34.31 | 62231.236 | 342114.924 | 599348.703 | 0.0 | 0 | 2 |
| gameWindowUnfocusEvent | 10 | 315.76 | 42104.435 | 77676.806 | 277119.82 | 433174.319 | 0.0 | 0 | 8 |
| chatEvent | 9 | 1.702 | 11.442 | 19177.15 | 103331.393 | 171610.813 | 0.0 | 0 | 2 |
| TerasGardenBox | 8 | 1.195 | 2.117 | 6.754 | 21.3 | 25.732 | 8.88 | 0 | 0 |
| EndOfUnit | 4 | 7273.349 | 85612.082 | 194507.668 | 522620.242 | 599533.159 | 0.0 | 0 | 4 |
| DaniEvent | 3 | 0.817 | 1.747 | 2.054 | 3.412 | 3.597 | 29.22 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 24 group(s), 48 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[1148] _id=6ac66328de269131f9bb9bf6 ts=2026-10-07T15:20:06.7390000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[1149] _id=6ac66328de269131f9bb9bf7 ts=2026-10-07T15:20:06.7390000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[1455] _id=6ac6656bde269131f9bbd8f3 ts=2026-10-07T15:29:45.5570000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[1456] _id=6ac6656bde269131f9bbd8f4 ts=2026-10-07T15:29:45.5570000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[1457] _id=6ac6656bde269131f9bbd8f5 ts=2026-10-07T15:29:45.5580000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[1458] _id=6ac6656bde269131f9bbd8f6 ts=2026-10-07T15:29:45.5580000Z`
- **WARNING / Medium** `PlayerPositionEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[10269] _id=6ad0f5ddde269131f9dce029 ts=2026-10-15T15:48:44.9420000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[10270] _id=6ad0f605de269131f9dce117 ts=2026-10-15T15:48:44.9420000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 30 group(s), 41 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[3151] _id=6ac7b83ede269131f9c3f5a9 ts=2026-10-08T15:35:26.1340000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[3148] _id=6ac7b83ede269131f9c3f5ab ts=2026-10-08T15:35:26.1340000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[3149] _id=6ac7b83ede269131f9c3f5af ts=2026-10-08T15:35:26.2610000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[3152] _id=6ac7b83ede269131f9c3f5b1 ts=2026-10-08T15:35:26.2610000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[3183] _id=6ac7b84bde269131f9c3f6d0 ts=2026-10-08T15:35:38.3530000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[3176] _id=6ac7b84bde269131f9c3f6d2 ts=2026-10-08T15:35:38.3530000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[12111] _id=6ad241cbde269131f9e52e4d ts=2026-10-16T15:24:59.1800000Z == 6ab9a8bc9a8420a1e6b56b06.jsonl[12119] _id=6ad241cbde269131f9e52e4e ts=2026-10-16T15:24:59.1800000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[104] _id=6ac3c03cde269131f9ad0327 ts=2026-10-05T15:20:28.0610000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[100] _id=6ac3c03cde269131f9ad0335 ts=2026-10-05T15:20:28.0660000Z`; `5ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[381] _id=6ac3c3c3de269131f9ad45a3 ts=2026-10-05T15:35:31.7330000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[385] _id=6ac3c3c3de269131f9ad45a5 ts=2026-10-05T15:35:31.7380000Z`; `1ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[729] _id=6ac51337de269131f9b45cb7 ts=2026-10-06T15:26:46.3010000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[730] _id=6ac51337de269131f9b45cb9 ts=2026-10-06T15:26:46.3020000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 12 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `639ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[1273] _id=6ac66448de269131f9bbb549 ts=2026-10-07T15:24:55.8160000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[1274] _id=6ac66449de269131f9bbb555 ts=2026-10-07T15:24:56.4550000Z`; `86ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[1274] _id=6ac66449de269131f9bbb555 ts=2026-10-07T15:24:56.4550000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[1271] _id=6ac66449de269131f9bbb55f ts=2026-10-07T15:24:56.5410000Z`; `782ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[1271] _id=6ac66449de269131f9bbb55f ts=2026-10-07T15:24:56.5410000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[1281] _id=6ac6644ade269131f9bbb573 ts=2026-10-07T15:24:57.3230000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `83ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[6085] _id=6acf9f8ede269131f9d4b164 ts=2026-10-14T15:28:14.1690000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[6088] _id=6acf9f8ede269131f9d4b168 ts=2026-10-14T15:28:14.2520000Z`; `42ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10501] _id=6ad0f743de269131f9dcedfe ts=2026-10-15T15:54:43.4310000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[10504] _id=6ad0f743de269131f9dcee01 ts=2026-10-15T15:54:43.4730000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `605ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[4836] _id=6acf898ade269131f9d39763 ts=2026-10-14T13:54:17.3160000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[4838] _id=6acf898ade269131f9d39771 ts=2026-10-14T13:54:17.9210000Z`; `792ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[4822] _id=6acf89a4de269131f9d39a3e ts=2026-10-14T13:54:44.0230000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[4864] _id=6acf89a5de269131f9d39a48 ts=2026-10-14T13:54:44.8150000Z`; `737ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[5897] _id=6acf9f54de269131f9d4ae7f ts=2026-10-14T15:27:16.0970000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[5891] _id=6acf9f55de269131f9d4ae89 ts=2026-10-14T15:27:16.8340000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[12284] _id=6ad242dede269131f9e53c4f ts=2026-10-16T15:29:34.4410000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[12285] _id=6ad242dede269131f9e53c51 ts=2026-10-16T15:29:34.4460000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `947ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[9544] _id=6ad0f29ade269131f9dcad01 ts=2026-10-15T15:34:50.0560000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[9551] _id=6ad0f29bde269131f9dcad1e ts=2026-10-15T15:34:51.0030000Z`; `571ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[9551] _id=6ad0f29bde269131f9dcad1e ts=2026-10-15T15:34:51.0030000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[9545] _id=6ad0f29bde269131f9dcad31 ts=2026-10-15T15:34:51.5740000Z`; `204ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[9545] _id=6ad0f29bde269131f9dcad31 ts=2026-10-15T15:34:51.5740000Z ~ 6ab9a8bc9a8420a1e6b56b06.jsonl[9554] _id=6ad0f29bde269131f9dcad40 ts=2026-10-15T15:34:51.7780000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2465] _id=6ac7b488de269131f9c38360 ts=2026-10-08T15:19:35.8850000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3867] _id=6ace50ffde269131f9cf39bd ts=2026-10-13T15:40:47.1830000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b06.jsonl[662] _id=6ac512dfde269131f9b45a93 ts=2026-10-06T15:25:18.7850000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1138] _id=6ac66312de269131f9bb9b11 ts=2026-10-07T15:19:45.1480000Z; 23h 50m: 6ab9a8bc9a8420a1e6b56b06.jsonl[355] _id=6ac3c38ede269131f9ad42af ts=2026-10-05T15:34:37.9340000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[662] _id=6ac512dfde269131f9b45a93 ts=2026-10-06T15:25:18.7850000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3854] _id=6ac7ba71de269131f9c41d6a ts=2026-10-08T15:44:49.3350000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3874] _id=6ace513bde269131f9cf3b4f ts=2026-10-13T15:41:44.6850000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b06.jsonl[639] _id=6ac3c6b1de269131f9ad7878 ts=2026-10-05T15:48:01.7980000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[672] _id=6ac51304de269131f9b45b4f ts=2026-10-06T15:25:56.3290000Z; 23h 33m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2459] _id=6ac66988de269131f9bc2f8c ts=2026-10-07T15:47:19.2090000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[2554] _id=6ac7b4bede269131f9c3883e ts=2026-10-08T15:20:29.8620000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 629 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10369] _id=6ad0f6afde269131f9dce5b3 ts=2026-10-15T15:52:14.7310000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10370] _id=6ad0f6afde269131f9dce5b4 ts=2026-10-15T15:52:14.7310000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10383] _id=6ad0f6bfde269131f9dce663 ts=2026-10-15T15:52:31.3980000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10384] _id=6ad0f6bfde269131f9dce664 ts=2026-10-15T15:52:31.3980000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10408] _id=6ad0f6e9de269131f9dce7d5 ts=2026-10-15T15:53:12.8080000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10415] _id=6ad0f6e9de269131f9dce7d6 ts=2026-10-15T15:53:12.8080000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 166h 32m 
  - Evidence: 166h 32m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1442] _id=6ac664f9de269131f9bbcdeb ts=2026-10-07T15:27:52.5640000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4966] _id=6acf8ae6de269131f9d3cdc9 ts=2026-10-14T14:00:05.7230000Z; 24h 6m: 6ab9a8bc9a8420a1e6b56b06.jsonl[7539] _id=6acfa74fde269131f9d51805 ts=2026-10-14T16:01:19.0720000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10927] _id=6ad0fa4bde269131f9dd3d07 ts=2026-10-15T16:07:39.4510000Z; 23h 27m: 6ab9a8bc9a8420a1e6b56b06.jsonl[10927] _id=6ad0fa4bde269131f9dd3d07 ts=2026-10-15T16:07:39.4510000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[12380] _id=6ad24427de269131f9e54ed3 ts=2026-10-16T15:35:03.2360000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3790] _id=6ac7b9a0de269131f9c41533 ts=2026-10-08T15:41:20.3700000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3892] _id=6ace5145de269131f9cf3bcb ts=2026-10-13T15:41:57.5940000Z; 23h 38m: 6ab9a8bc9a8420a1e6b56b06.jsonl[634] _id=6ac3c674de269131f9ad735f ts=2026-10-05T15:47:00.0410000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[658] _id=6ac512e2de269131f9b45aa1 ts=2026-10-06T15:25:20.5440000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1010] _id=6ac516f9de269131f9b4a2b7 ts=2026-10-06T15:42:49.2950000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1147] _id=6ac66328de269131f9bb9bf5 ts=2026-10-07T15:20:06.7370000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 471 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10002] _id=6ad0f3e4de269131f9dcc655 ts=2026-10-15T15:40:20.6080000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10003] _id=6ad0f3e4de269131f9dcc656 ts=2026-10-15T15:40:20.6080000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10114] _id=6ad0f48ede269131f9dccfb4 ts=2026-10-15T15:43:10.5770000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10115] _id=6ad0f48ede269131f9dccfb5 ts=2026-10-15T15:43:10.5770000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10276] _id=6ad0f605de269131f9dce11b ts=2026-10-15T15:49:04.8210000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10277] _id=6ad0f605de269131f9dce11c ts=2026-10-15T15:49:04.8210000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 142h 7m 
  - Evidence: 142h 7m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3565] _id=6ac7b8e6de269131f9c40995 ts=2026-10-08T15:38:13.7690000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4556] _id=6acf877cde269131f9d35675 ts=2026-10-14T13:45:31.8090000Z; 23h 55m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2243] _id=6ac6672bde269131f9bc0584 ts=2026-10-07T15:37:14.3710000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3032] _id=6ac7b792de269131f9c3e7f4 ts=2026-10-08T15:32:33.9650000Z; 23h 39m: 6ab9a8bc9a8420a1e6b56b06.jsonl[637] _id=6ac3c675de269131f9ad737e ts=2026-10-05T15:47:01.2950000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[729] _id=6ac51337de269131f9b45cb7 ts=2026-10-06T15:26:46.3010000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10166] _id=6ad0f565de269131f9dcdbdf ts=2026-10-15T15:46:44.8960000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10167] _id=6ad0f565de269131f9dcdbe0 ts=2026-10-15T15:46:44.8960000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10253] _id=6ad0f597de269131f9dcdead ts=2026-10-15T15:47:35.3170000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10255] _id=6ad0f597de269131f9dcdeae ts=2026-10-15T15:47:35.3170000Z; 1ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[729] _id=6ac51337de269131f9b45cb7 ts=2026-10-06T15:26:46.3010000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[730] _id=6ac51337de269131f9b45cb9 ts=2026-10-06T15:26:46.3020000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3857] _id=6ac7ba92de269131f9c41eba ts=2026-10-08T15:45:21.8270000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3873] _id=6ace513bde269131f9cf3b4e ts=2026-10-13T15:41:42.2370000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b06.jsonl[649] _id=6ac3c6b0de269131f9ad786f ts=2026-10-05T15:48:00.7900000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[657] _id=6ac512e1de269131f9b45a9f ts=2026-10-06T15:25:18.7960000Z; 23h 32m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1125] _id=6ac5180fde269131f9b4bdef ts=2026-10-06T15:47:26.4400000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1146] _id=6ac66328de269131f9bb9bf4 ts=2026-10-07T15:20:04.6020000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10269] _id=6ad0f5ddde269131f9dce029 ts=2026-10-15T15:48:44.9420000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10270] _id=6ad0f605de269131f9dce117 ts=2026-10-15T15:48:44.9420000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[7538] _id=6acfa74fde269131f9d51813 ts=2026-10-14T16:01:19.3340000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[7541] _id=6acfa75fde269131f9d5195f ts=2026-10-14T16:01:19.334Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3728] _id=6ac7b986de269131f9c41295 ts=2026-10-08T15:40:53.6900000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3871] _id=6ace513bde269131f9cf3b53 ts=2026-10-13T15:41:45.6770000Z; 23h 58m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2174] _id=6ac666e1de269131f9bc00c1 ts=2026-10-07T15:35:58.2930000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3112] _id=6ac7b7edde269131f9c3f05b ts=2026-10-08T15:34:05.2330000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b06.jsonl[6559] _id=6acfa0cfde269131f9d4bf22 ts=2026-10-14T15:33:33.0330000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[7719] _id=6ad0ed0fde269131f9dc4e93 ts=2026-10-15T15:11:11.1990000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 917 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10946] _id=6ad23c2bde269131f9e4c411 ts=2026-10-16T15:00:57.9020000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10941] _id=6ad23c2bde269131f9e4c418 ts=2026-10-16T15:00:57.9020000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10958] _id=6ad23c2ade269131f9e4c3fd ts=2026-10-16T15:00:57.5160000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10959] _id=6ad23c2ade269131f9e4c401 ts=2026-10-16T15:00:57.5160000Z; 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10959] _id=6ad23c2ade269131f9e4c401 ts=2026-10-16T15:00:57.5160000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10960] _id=6ad23c2ade269131f9e4c403 ts=2026-10-16T15:00:57.5160000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 143h 28m 
  - Evidence: 143h 28m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3130] _id=6ac7b856de269131f9c3f7c6 ts=2026-10-08T15:35:50.0170000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[5013] _id=6acf99e1de269131f9d44a38 ts=2026-10-14T15:04:01.3880000Z; 23h 49m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2329] _id=6ac66882de269131f9bc1bbc ts=2026-10-07T15:42:56.9560000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3031] _id=6ac7b792de269131f9c3e7ee ts=2026-10-08T15:32:33.9610000Z; 23h 39m: 6ab9a8bc9a8420a1e6b56b06.jsonl[6275] _id=6acfa03dde269131f9d4b83a ts=2026-10-14T15:31:09.2430000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[7689] _id=6ad0ecfade269131f9dc4d0b ts=2026-10-15T15:10:49.8860000Z
- **INFO / Info** `SolarStillDesignEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[12221] _id=6ad2427cde269131f9e53842 ts=2026-10-16T15:27:56.4870000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[12222] _id=6ad2427cde269131f9e53843 ts=2026-10-16T15:27:56.4870000Z; 5ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[12217] _id=6ad2427cde269131f9e5383e ts=2026-10-16T15:27:56.4820000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[12221] _id=6ad2427cde269131f9e53842 ts=2026-10-16T15:27:56.4870000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 25m 
  - Evidence: 120h 25m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3742] _id=6ac7b98fde269131f9c41388 ts=2026-10-08T15:41:03.4020000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4352] _id=6ace571dde269131f9cf56be ts=2026-10-13T16:06:52.6370000Z; 24h 7m: 6ab9a8bc9a8420a1e6b56b06.jsonl[716] _id=6ac51330de269131f9b45c77 ts=2026-10-06T15:26:39.4310000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1607] _id=6ac66655de269131f9bbf2b6 ts=2026-10-07T15:33:40.1820000Z; 24h 4m: 6ab9a8bc9a8420a1e6b56b06.jsonl[167] _id=6ac3c0b8de269131f9ad114d ts=2026-10-05T15:22:32.6360000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[656] _id=6ac5132cde269131f9b45c5f ts=2026-10-06T15:26:36.2650000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.024s..0.025s shown 
  - Evidence: 24ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[2421] _id=6ac66961de269131f9bc2bcf ts=2026-10-07T15:46:40.5870000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[2422] _id=6ac66961de269131f9bc2bd3 ts=2026-10-07T15:46:40.6110000Z; 24ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[2597] _id=6ac7b51ede269131f9c39233 ts=2026-10-08T15:22:05.6030000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[2601] _id=6ac7b51ede269131f9c39237 ts=2026-10-08T15:22:05.6270000Z; 25ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[2422] _id=6ac66961de269131f9bc2bd3 ts=2026-10-07T15:46:40.6110000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[2427] _id=6ac66961de269131f9bc2bd7 ts=2026-10-07T15:46:40.6360000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 166h 30m 
  - Evidence: 166h 30m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1287] _id=6ac66452de269131f9bbb630 ts=2026-10-07T15:25:05.3930000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4874] _id=6acf89c3de269131f9d39ca1 ts=2026-10-14T13:55:14.4280000Z; 24h 24m: 6ab9a8bc9a8420a1e6b56b06.jsonl[6084] _id=6acf9f8ede269131f9d4b162 ts=2026-10-14T15:28:14.1510000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10372] _id=6ad0f6aede269131f9dce5ae ts=2026-10-15T15:52:14.7020000Z; 23h 35m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1133] _id=6ac51814de269131f9b4be4b ts=2026-10-06T15:47:31.5900000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1235] _id=6ac663d4de269131f9bba925 ts=2026-10-07T15:22:59.6890000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 166h 28m 
  - Evidence: 166h 28m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1289] _id=6ac66452de269131f9bbb634 ts=2026-10-07T15:25:05.4250000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4799] _id=6acf8951de269131f9d38d7c ts=2026-10-14T13:53:20.2890000Z; 24h 22m: 6ab9a8bc9a8420a1e6b56b06.jsonl[6088] _id=6acf9f8ede269131f9d4b168 ts=2026-10-14T15:28:14.2520000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10328] _id=6ad0f66dde269131f9dce371 ts=2026-10-15T15:51:09.5140000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1134] _id=6ac51814de269131f9b4be4f ts=2026-10-06T15:47:31.6220000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1216] _id=6ac663a1de269131f9bba3ac ts=2026-10-07T15:22:08.6710000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.042s..0.042s shown 
  - Evidence: 42ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[10501] _id=6ad0f743de269131f9dcedfe ts=2026-10-15T15:54:43.4310000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10504] _id=6ad0f743de269131f9dcee01 ts=2026-10-15T15:54:43.4730000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 166h 28m 
  - Evidence: 166h 28m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1270] _id=6ac66443de269131f9bbb4c5 ts=2026-10-07T15:24:50.1210000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4805] _id=6acf895dde269131f9d38f61 ts=2026-10-14T13:53:32.9760000Z; 24h 22m: 6ab9a8bc9a8420a1e6b56b06.jsonl[6078] _id=6acf9f89de269131f9d4b111 ts=2026-10-14T15:28:09.5490000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10319] _id=6ad0f669de269131f9dce348 ts=2026-10-15T15:51:05.3830000Z; 23h 35m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1124] _id=6ac51812de269131f9b4be23 ts=2026-10-06T15:47:29.4800000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1224] _id=6ac663c4de269131f9bba744 ts=2026-10-07T15:22:43.6490000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 26 interval(s) ≤ 0.006s..0.024s shown 
  - Evidence: 6ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[12037] _id=6ad24159de269131f9e52766 ts=2026-10-16T15:23:05.0880000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[12043] _id=6ad24159de269131f9e5276c ts=2026-10-16T15:23:05.0940000Z; 24ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[12024] _id=6ad24145de269131f9e5265b ts=2026-10-16T15:22:44.7900000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[12028] _id=6ad24145de269131f9e5265d ts=2026-10-16T15:22:44.8140000Z; 24ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[6049] _id=6acf9f64de269131f9d4af3e ts=2026-10-14T15:27:32.1620000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[6050] _id=6acf9f64de269131f9d4af42 ts=2026-10-14T15:27:32.1860000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 166h 29m 
  - Evidence: 166h 29m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1257] _id=6ac6642cde269131f9bbb2f5 ts=2026-10-07T15:24:27.5710000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4806] _id=6acf8961de269131f9d38ffd ts=2026-10-14T13:53:36.2740000Z; 23h 34m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1122] _id=6ac5180cde269131f9b4bdaf ts=2026-10-06T15:47:23.8800000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1212] _id=6ac6639ede269131f9bba322 ts=2026-10-07T15:22:05.0260000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 47h 40m 
  - Evidence: 47h 40m: 6ab9a8bc9a8420a1e6b56b06.jsonl[5813] _id=6acf9dc7de269131f9d498dc ts=2026-10-14T15:20:39.3000000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10945] _id=6ad23c22de269131f9e4c383 ts=2026-10-16T15:00:50.1130000Z; 15m 12s: 6ab9a8bc9a8420a1e6b56b06.jsonl[10945] _id=6ad23c22de269131f9e4c383 ts=2026-10-16T15:00:50.1130000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[11799] _id=6ad23fb2de269131f9e51381 ts=2026-10-16T15:16:02.3770000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 120h 21m 
  - Evidence: 120h 21m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2464] _id=6ac7b47bde269131f9c38243 ts=2026-10-08T15:19:22.6120000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3869] _id=6ace50ffde269131f9cf39bf ts=2026-10-13T15:40:47.3230000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b06.jsonl[7546] _id=6ad0ebc5de269131f9dc290c ts=2026-10-15T15:05:40.8920000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10940] _id=6ad23c17de269131f9e4c2c3 ts=2026-10-16T15:00:39.6450000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b06.jsonl[661] _id=6ac512d5de269131f9b45a6b ts=2026-10-06T15:25:08.4800000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1140] _id=6ac66312de269131f9bb9b13 ts=2026-10-07T15:19:45.3030000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 120h 5m 
  - Evidence: 120h 5m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3143] _id=6ac7b838de269131f9c3f553 ts=2026-10-08T15:35:19.9950000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3868] _id=6ace50ffde269131f9cf39be ts=2026-10-13T15:40:47.3230000Z; 23h 54m: 6ab9a8bc9a8420a1e6b56b06.jsonl[7545] _id=6ad0ebc5de269131f9dc290b ts=2026-10-15T15:05:40.8920000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[10939] _id=6ad23c17de269131f9e4c2c2 ts=2026-10-16T15:00:39.6450000Z; 23h 50m: 6ab9a8bc9a8420a1e6b56b06.jsonl[351] _id=6ac3c379de269131f9ad419a ts=2026-10-05T15:34:16.9590000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[660] _id=6ac512d5de269131f9b45a69 ts=2026-10-06T15:25:08.4790000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 120h 19m 
  - Evidence: 120h 19m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3870] _id=6ace50ffde269131f9cf39bb ts=2026-10-08T15:45:30.043Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[4321] _id=6ace56b1de269131f9cf55af ts=2026-10-13T16:05:04.3620000Z; 23h 59m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1137] _id=6ac66312de269131f9bb9b0f ts=2026-10-06T15:47:34.318Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[2461] _id=6ac7b47bde269131f9c3823f ts=2026-10-07T15:47:20.862Z; 23h 47m: 6ab9a8bc9a8420a1e6b56b06.jsonl[2461] _id=6ac7b47bde269131f9c3823f ts=2026-10-07T15:47:20.862Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3145] _id=6ac7b838de269131f9c3f54d ts=2026-10-08T15:35:19.4540000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 56m 
  - Evidence: 119h 56m: 6ab9a8bc9a8420a1e6b56b06.jsonl[3849] _id=6ac7ba71de269131f9c41d5d ts=2026-10-08T15:44:49.3280000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[3876] _id=6ace513bde269131f9cf3b51 ts=2026-10-13T15:41:44.7880000Z; 23h 42m: 6ab9a8bc9a8420a1e6b56b06.jsonl[497] _id=6ac3c56dde269131f9ad608b ts=2026-10-05T15:42:37.3620000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[668] _id=6ac512e2de269131f9b45aa9 ts=2026-10-06T15:25:20.5900000Z; 23h 37m: 6ab9a8bc9a8420a1e6b56b06.jsonl[1049] _id=6ac516fbde269131f9b4a2eb ts=2026-10-06T15:42:50.2830000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1151] _id=6ac66328de269131f9bb9bf9 ts=2026-10-07T15:20:06.9040000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[12111] _id=6ad241cbde269131f9e52e4d ts=2026-10-16T15:24:59.1800000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[12119] _id=6ad241cbde269131f9e52e4e ts=2026-10-16T15:24:59.1800000Z; 1ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[1191] _id=6ac6633ede269131f9bb9d1d ts=2026-10-07T15:20:29.6700000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1192] _id=6ac6633ede269131f9bb9d1e ts=2026-10-07T15:20:29.6710000Z; 3ms: 6ab9a8bc9a8420a1e6b56b06.jsonl[1051] _id=6ac516fbde269131f9b4a2e9 ts=2026-10-06T15:42:50.2800000Z -> 6ab9a8bc9a8420a1e6b56b06.jsonl[1049] _id=6ac516fbde269131f9b4a2eb ts=2026-10-06T15:42:50.2830000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[1023] _id=6ac516d7de269131f9b49fc1 ts=2026-10-06T15:42:15.3250000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[1298] _id=6ac66470de269131f9bbb8e8 ts=2026-10-07T15:25:35.0680000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[2755] _id=6ac7b650de269131f9c3b75b ts=2026-10-08T15:27:12.1370000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[6088] _id=6acf9f8ede269131f9d4b168 ts=2026-10-14T15:28:14.2520000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[10504] _id=6ad0f743de269131f9dcee01 ts=2026-10-15T15:54:43.4730000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[10945] _id=6ad23c22de269131f9e4c383 ts=2026-10-16T15:00:50.1130000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[11799] _id=6ad23fb2de269131f9e51381 ts=2026-10-16T15:16:02.3770000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 26 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[3356] _id=6ac7b8c8de269131f9c40477 ts=2026-10-08T15:37:42.4220000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[3333] _id=6ac7b8c8de269131f9c4047f ts=2026-10-08T15:37:42.4990000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[3362] _id=6ac7b8c9de269131f9c40491 ts=2026-10-08T15:37:42.7660000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 45 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[3148] _id=6ac7b83ede269131f9c3f5ab ts=2026-10-08T15:35:26.1340000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[3164] _id=6ac7b84bde269131f9c3f6c8 ts=2026-10-08T15:35:37.8500000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[3175] _id=6ac7b84bde269131f9c3f6cd ts=2026-10-08T15:35:37.9210000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[1123] _id=6ac51809de269131f9b4bd79 ts=2026-10-06T15:47:21.2460000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[1257] _id=6ac6642cde269131f9bbb2f5 ts=2026-10-07T15:24:27.5710000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[4843] _id=6acf89b1de269131f9d39b47 ts=2026-10-14T13:54:56.2990000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 405 start, 395 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 528 open, 516 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 9 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 53 start, 39 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 309 of 12404 adjacent _id pairs reverse in client time; worst 96.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8bc9a8420a1e6b56b06.jsonl[1667] _id=6ac66694de269131f9bbf96f ts=2026-10-07T15:34:42.8710000Z`; `6ab9a8bc9a8420a1e6b56b06.jsonl[1659] _id=6ac66695de269131f9bbf978 ts=2026-10-07T15:33:06.8680000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.37s, min -431717.42s, max -0.11s over 12405 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8bc9a8420a1e6b56b06\coverage.yaml

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

### `InputEvent` — 5639 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1232); Unit 4 Dev - Dungeon (1148); Unit 3 Dev (975); Unit 4 Dev (615); Unit 1 Dev (566); Unit 3 Dungeon Dev (442); Unit 5 Dev - Dungeon (423); Unit 5 Dev (186); Unit 4 Dev - Anderson Base (52)
- **Intervals:** median 0.41s (p5 0.01s / p95 5.13s, n=5638)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5639/5639 records)
    "pressed"  x5639
data.actionType  (string, 5639/5639 records)
    "Move"  x4655
    "Interact"  x386
    "Jump"  x282
    "Sprint"  x129
    "Ascend"  x80
    "Hoverboard"  x66
    "Map"  x22
    "Pause"  x11
    "ToggleDebug"  x6
    "SkipCinematic"  x2
data.key  (string, 5639/5639 records, 21 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5639/5639 records)
    "Player"  x4977
    "Drone"  x662
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2275 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (678); Unit 1 Dev (370); Unit 3 Dev (335); Unit 4 Dev (248); Unit 5 Dev (239); Unit 3 Dungeon Dev (127); Unit 4 Dev - Anderson Base (102); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (77)
- **eventKey:** present on 1475 of 2275 records
- **Intervals:** median 4.04s (p5 0.00s / p95 28.15s, n=2274)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1475; [conversationId, dialogueEventType] x800
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2275/2275 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2275/2275 records)
    "DialogueNodeEvent"  x1475
    "DialogueStartEvent"  x405
    "DialogueFinishEvent"  x395
data.nodeId  (number, 1475/2275 records)
    numeric range 0 .. 290 (223 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PuzzlePieceVisibleEvent` — 1750 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (902); Unit 4 Dev (436); Unit 5 Dev - Dungeon (226); Unit 3 Dungeon Dev (186)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.27s, n=1749)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1750/1750 records)
    "BecameVisible"  x528
    "BecameInvisible"  x516
    "BecameCameraCentered"  x353
    "BecameCameraUncentered"  x353
data.pieceId  (string, 1750/1750 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 1750/1750 records)
    1103 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 1739 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (506); Unit 1 Dev (356); Unit 3 Dev (225); Unit 4 Dev (166); Unit 4 Dev - Dungeon (141); Unit 5 Dev (110); Unit 5 Dev - Dungeon (91); Unit 3 Dungeon Dev (80); Unit 4 Dev - Anderson Base (64)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.15s, n=1727)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 1739/1739 records)
data.position.x  (number, 1739/1739 records)
    numeric range -717.766 .. 1556.9 (496 unique)
data.position.y  (number, 1739/1739 records)
    numeric range -112.997 .. 222.006 (375 unique)
data.position.z  (number, 1739/1739 records)
    numeric range -1031.56 .. 1785.98 (496 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 319 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (119); Unit 2 Prod (Refactor) (69); Unit 3 Dev (45); Unit 1 Dev (44); Unit 5 Dev (42)
- **Intervals:** median 0.67s (p5 0.03s / p95 13.36s, n=318)
- **Fields under `data`:**

```text
data.actionType  (string, 319/319 records)
    "argumentationNodeHoverEnd"  x138
    "argumentationNodeHoverStart"  x138
    "argumentationNodeAdd"  x34
    "argumentationNodeRemove"  x9
data.argumentationTitle  (string, 319/319 records)
    "Unit 4 - Flooding"  x119
    "Unit 2 – Watershed"  x69
    "Unit 3 - Pollution Upstream"  x45
    "Unit 5"  x42
    "Unit 1 - Freshwater"  x24
    "Unit 1 - Argumentation Tutorial"  x20
data.nodeName  (string, 319/319 records)
    "A"  x57
    "B"  x42
    "D"  x40
    "1"  x37
    "I"  x33
    "II"  x27
    "C"  x22
    "4"  x20
    "2"  x17
    "3"  x17
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 222 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (77); Unit 3 Dungeon Dev (36); Unit 2 Prod (Refactor) (28); Unit 1 Dev (22); Unit 4 Dev (21); Unit 3 Dev (13); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (9); Unit 5 Dev (7)
- **Intervals:** median 12.82s (p5 0.88s / p95 426.78s, n=221)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 222/222 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 222/222 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 93 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (48); Unit 2 Prod (Refactor) (39); Unit 1 Dev (6)
- **Intervals:** median 3.83s (p5 0.78s / p95 37663.02s, n=92)
- **`data` key-set variants:** [actionType, featureUsed] x64; [actionType, featureUsed, location] x29
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 93/93 records)
    "MapCloseEvent"  x32
    "MapOpenEvent"  x32
    "WaypointMoveEvent"  x20
    "WaypointSetEvent"  x7
    "WaypointResetEvent"  x2
data.featureUsed  (string, 93/93 records)
    "Map"  x64
    "Waypoint"  x29
data.location  (object, 29/93 records)
data.location.x  (number, 29/93 records)
    numeric range -326.869 .. 612.705 (25 unique)
data.location.y  (number, 29/93 records)
    numeric range -284.423 .. 326.73 (25 unique)
data.location.z  (number, 29/93 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 92 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (25); Unit 2 Prod (Refactor) (22); Unit 3 Dev (10); Unit 4 Dev - Dungeon (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 92 of 92 records
- **Intervals:** median 168.89s (p5 0.01s / p95 82839.49s, n=91)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x39
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 92/92 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x39
data.questID  (string, 92/92 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 92/92 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 39/92 records)
    "Succeeded"  x39
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 47 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (19); Unit 2 Prod (Refactor) (18); Unit 3 Dev (10)
- **Intervals:** median 2.57s (p5 0.32s / p95 64114.48s, n=46)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x39; [Soil Key Puzzle Status, Unit] x8
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/47 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/47 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 39/47 records)
    "RightDrag"  x20
    "LeftDrag"  x19
data.currentSoilType  (string, 39/47 records)
    "CLAY"  x10
    "CLAYSAND"  x9
    "SAND"  x7
    "CLAYROCK"  x6
    "BEDROCK"  x3
    "SANDGRAVEL"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 39/47 records)
    "false"  x28
    "true"  x11
data.waterLevelStatus  (string, 39/47 records)
    "Proper"  x16
    "TooHigh"  x16
    "TooLow"  x7
data.waterRetentionChange  (string, 39/47 records)
    "Increase"  x19
    "NoChange"  x11
    "Decrease"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 34 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (18); Unit 4 Dev - Anderson Base (7); Unit 2 Prod (Refactor) (5); Unit 3 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 6.71s (p5 0.10s / p95 86093.08s, n=33)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "submitAnswerEvent"  x34
data.answerSubmitted  (string, 34/34 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 34/34 records)
    "Unit 1 - Freshwater"  x16
    "Unit 4 - Flooding"  x7
    "Unit 2 – Watershed"  x5
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (5); Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev (3); Unit 3 Dungeon Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 562.55s (p5 10.66s / p95 85976.16s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `WaterChamberEvent` — 25 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (25)
- **Intervals:** median 12.92s (p5 1.63s / p95 57.80s, n=24)
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "On"  x18
    "Off"  x7
data.floor  (string, 25/25 records)
    "4"  x11
    "3"  x9
    "2"  x3
    "1"  x2
data.machineNumber  (string, 25/25 records)
    "One"  x24
    "Two"  x1
data.machineType  (string, 25/25 records)
    "Condenser"  x14
    "Evaporator"  x6
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

### `soilMachine` — 21 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (21)
- **Intervals:** median 14.01s (p5 0.55s / p95 164.94s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "ChangeCanister"  x21
data.canisterType  (string, 21/21 records)
    "Clay"  x9
    "Sand"  x6
    "Bedrock"  x3
    "Gravel"  x3
data.floor  (string, 21/21 records)
    "5"  x13
    "4"  x5
    "3"  x3
data.machine  (string, 21/21 records)
    "1"  x19
    "2"  x2
data.row  (string, 21/21 records)
    "TopRow"  x18
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 20 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Unit 1 Dev (3); Unit 2 Prod (Refactor) (2); Unit 3 Dev (1)
- **Intervals:** median 994.72s (p5 123.54s / p95 120721.61s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 70.54s (p5 0.07s / p95 190079.18s, n=17)
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

### `SolarStillDesignEvent` — 16 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (16)
- **Intervals:** median 2.24s (p5 0.00s / p95 5.67s, n=15)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x15; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "optionSelected"  x15
    "DesignSubmitted"  x1
data.designSelections  (object, 1/16 records)
data.designSelections.glassRoofTemperature  (string, 1/16 records)
    "Hot"  x1
data.designSelections.roofCovering  (string, 1/16 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/16 records)
    "Tilted Out"  x1
data.featureUsed  (string, 16/16 records)
    "GlassRoofTemperature"  x6
    "RoofStyle"  x6
    "ExtraCovering"  x3
    "Submit"  x1
data.selectedOption  (string, 15/16 records, 4 empty-string)
    ""  x4
    "Hot"  x3
    "Flat"  x2
    "Tilted Out"  x2
    "Cold"  x1
    "Covered"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 78139.25s (p5 549.26s / p95 224973.14s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (8); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 34.31s (p5 2.34s / p95 342114.92s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 2 – Watershed"  x4
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - "  x4
    "BackingInfoPanel - Argumentation"  x4
    "BackingInfoPanel - Waterfall Data"  x2
    "BackingInfoPanel - Watershed Graph"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `gameWindowUnfocusEvent` — 11 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (5); Unit 2 Prod (Refactor) (5); Unit 3 Dev (1)
- **Intervals:** median 42104.43s (p5 339.68s / p95 277119.82s, n=10)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 11/11 records)
    false  x11
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 10 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (8); Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 11.44s (p5 1.77s / p95 103331.39s, n=9)
- **`data` key-set variants:** [actionType, chatID] x7; [actionKey, chatID] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionKey  (string, 3/10 records)
    "ScrollStop"  x3
data.actionType  (string, 7/10 records)
    "Close"  x3
    "ScrollStart"  x3
    "Open"  x1
data.chatID  (string, 10/10 records)
    "NA"  x6
    "[10-217, 10-218, 11-224, 11-226, 11-23]"  x1
    "[11-224, 11-226, 11-23, 11-24]"  x1
    "[11-23, 11-24, 11-28, 11-230, 11-26]"  x1
    "[11-29, 11-230, 11-230, 11-27, 11-27]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `TerasGardenBox` — 9 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (9)
- **Intervals:** median 2.12s (p5 1.22s / p95 21.30s, n=8)
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
    "Clay"  x5
    "Gravel"  x2
    "Sand"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 85612.08s (p5 18848.91s / p95 522620.24s, n=4)
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
- **Intervals:** median 1.75s (p5 0.91s / p95 3.41s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (20x); "WaypointResetEvent" (2x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (29x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (9x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*