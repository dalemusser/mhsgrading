# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9279a8420a1e6b56b7f
- **Game version string(s) in log:** 2.9.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b7f.jsonl
- **Records:** 18671 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b7f
- **Time span:** 2026-10-05T19:11:48.488000+00:00 .. 2026-10-15T22:56:40.439000+00:00 (243h 44m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 18671 records, 10 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 101 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5740 | 30.74 | 1 | 4 | 0 | 2026-10-07T19:04:06.960000+00:00 | 2026-10-15T22:15:02.098000+00:00 | 195h 10m |
| InputEvent | 5456 | 29.22 | 1 | 9 | 0 | 2026-10-05T19:12:01.772000+00:00 | 2026-10-15T22:56:40.439000+00:00 | 243h 44m |
| PlayerPositionEvent | 3145 | 16.84 | 1 | 9 | 0 | 2026-10-05T19:11:58.268000+00:00 | 2026-10-15T22:56:31.306000+00:00 | 243h 44m |
| DialogueEvent | 2667 | 14.28 | 1 | 9 | 1663 | 2026-10-05T19:12:18.275000+00:00 | 2026-10-15T22:56:32.484000+00:00 | 243h 44m |
| ObjectInterEvent | 504 | 2.7 | 1 | 9 | 0 | 2026-10-06T18:32:48.552000+00:00 | 2026-10-15T22:56:40.439000+00:00 | 220h 23m |
| argumentationNodeEvent | 425 | 2.28 | 1 | 5 | 0 | 2026-10-06T19:07:31.245000+00:00 | 2026-10-15T22:42:31.970000+00:00 | 219h 35m |
| Soil Key Puzzle | 210 | 1.12 | 1 | 3 | 0 | 2026-10-08T19:10:46.457000+00:00 | 2026-10-15T00:37:11.867000+00:00 | 149h 26m |
| TopographicMapEvent | 113 | 0.61 | 1 | 4 | 0 | 2026-10-07T19:04:47.957000+00:00 | 2026-10-15T21:29:20.942000+00:00 | 194h 24m |
| questEvent | 99 | 0.53 | 1 | 9 | 99 | 2026-10-05T19:12:18.248000+00:00 | 2026-10-15T22:52:41.811000+00:00 | 243h 40m |
| WaterChamberEvent | 54 | 0.29 | 1 | 1 | 0 | 2026-10-15T22:12:20.447000+00:00 | 2026-10-15T22:33:47.304000+00:00 | 21m 26s |
| argumentationAnswerEvent | 49 | 0.26 | 1 | 5 | 0 | 2026-10-06T19:09:55.092000+00:00 | 2026-10-15T22:42:33.324000+00:00 | 219h 32m |
| DEBUGMenu | 48 | 0.26 | 1 | 9 | 0 | 2026-10-05T19:11:58.249000+00:00 | 2026-10-15T22:06:28.197000+00:00 | 242h 54m |
| gameWindowFocusEvent | 33 | 0.18 | 1 | 4 | 0 | 2026-10-05T19:11:48.488000+00:00 | 2026-10-15T22:06:13.530000+00:00 | 242h 54m |
| soilMachine | 24 | 0.13 | 1 | 1 | 0 | 2026-10-15T18:58:15.565000+00:00 | 2026-10-15T19:11:14.044000+00:00 | 12m 58s |
| gameStartEvent | 23 | 0.12 | 1 | 1 | 0 | 2026-10-05T19:11:48.489000+00:00 | 2026-10-15T22:06:13.530000+00:00 | 242h 54m |
| argumentationEvent | 21 | 0.11 | 1 | 5 | 0 | 2026-10-06T19:07:21.253000+00:00 | 2026-10-15T22:42:33.355000+00:00 | 219h 35m |
| gameWindowUnfocusEvent | 21 | 0.11 | 1 | 6 | 0 | 2026-10-05T19:18:03.974000+00:00 | 2026-10-15T19:17:14.873000+00:00 | 239h 59m |
| DaniEvent | 12 | 0.06 | 1 | 2 | 0 | 2026-10-10T01:47:12.315000+00:00 | 2026-10-13T18:53:58.288000+00:00 | 89h 6m |
| argumentationToolEvent | 9 | 0.05 | 1 | 1 | 0 | 2026-10-06T19:11:30.717000+00:00 | 2026-10-07T18:47:40.763000+00:00 | 23h 36m |
| TerasGardenBox | 6 | 0.03 | 1 | 1 | 0 | 2026-10-15T21:54:30.772000+00:00 | 2026-10-15T21:55:25.180000+00:00 | 54.4s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-10-07T18:56:55.501000+00:00 | 2026-10-15T22:56:40.413000+00:00 | 195h 59m |
| SolarStillDesignEvent | 4 | 0.02 | 1 | 1 | 0 | 2026-10-15T22:49:46.201000+00:00 | 2026-10-15T22:49:52.860000+00:00 | 6.7s |
| chatEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-10-15T22:06:27.942000+00:00 | 2026-10-15T22:34:44.764000+00:00 | 28m 16s |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 167267.585s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.375s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.049s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.624s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.018s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 8.69s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 9.982s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.535s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 9123.103s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1747.562s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 6299.851s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 4.56s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 4.0x vs baseline. 
  - Observed: 48 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 12 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 5.5x vs baseline. 
  - Observed: 210 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — baseline categorical value(s) not seen this build. 
  - Observed: Cold 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.glassRoofTemperature` — categorical value(s) not seen in baseline. 
  - Observed: Hot 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — baseline categorical value(s) not seen this build. 
  - Observed: Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofCovering` — categorical value(s) not seen in baseline. 
  - Observed: Covered 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.designSelections.roofStyle` — categorical value(s) not seen in baseline. 
  - Observed: Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Cold; Tilted Out; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: Covered; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 9.8x vs baseline. 
  - Observed: 49 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,; A,1,; A,2,I; A,2,II; A,3,I; A,4,II; A,C,2,II; A,II; B,2,II; C,2,II; C,3,II; C,A,2,II; C,D,2,II; C,D,3,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 425 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 21 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` — record volume changed 4.8x vs baseline. 
  - Observed: 24 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[649] _id=6ac54060de269131f9b6abdd ts=2026-10-06T18:39:28.0370000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[716] _id=6ac54156de269131f9b6c76f ts=2026-10-06T18:43:33.4180000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[815] _id=6ac54254de269131f9b6e7e3 ts=2026-10-06T18:47:47.4550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[4] _id=6ac3f674de269131f9af6abf ts=2026-10-05T19:11:48.4890000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[100] _id=6ac53e8ade269131f9b676bd ts=2026-10-06T18:31:37.1910000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1411] _id=6ac692b4de269131f9bdee6f ts=2026-10-07T18:42:58.5830000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 33 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 33} 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[1] _id=6ac3f674de269131f9af6abd ts=2026-10-05T19:11:48.4880000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[102] _id=6ac53e8ade269131f9b676b9 ts=2026-10-06T18:31:37.1890000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1142] _id=6ac5467bde269131f9b74677 ts=2026-10-06T19:05:30.5660000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[101] _id=6ac53e89de269131f9b676ac ts=2026-10-05T19:18:03.974Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1141] _id=6ac54678de269131f9b745f5 ts=2026-10-06T19:05:27.8650000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1413] _id=6ac692b4de269131f9bdee5d ts=2026-10-06T19:17:47.101Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5739 | 0.0 | 0.049 | 122.435 | 2.03 | 237656.583 | 0.49 | 2887 | 11 |
| InputEvent | 5455 | 0.0 | 1.375 | 160.858 | 18.783 | 161571.535 | 0.37 | 105 | 15 |
| PlayerPositionEvent | 3133 | 9.783 | 10.002 | 235.107 | 10.103 | 161557.241 | 0.26 | 0 | 11 |
| DialogueEvent | 2666 | 0.0 | 4.619 | 329.128 | 37.376 | 161708.986 | 0.18 | 743 | 16 |
| ObjectInterEvent | 503 | 0.0 | 7.047 | 1577.399 | 384.63 | 164826.799 | 0.04 | 4 | 19 |
| argumentationNodeEvent | 424 | 0.005 | 0.645 | 1864.389 | 13.043 | 367509.819 | 0.03 | 42 | 6 |
| Soil Key Puzzle | 209 | 0.033 | 1.062 | 2574.093 | 21.398 | 240244.38 | 0.02 | 1 | 6 |
| TopographicMapEvent | 112 | 0.018 | 7.018 | 6248.866 | 39083.242 | 161771.827 | 0.01 | 4 | 14 |
| questEvent | 98 | 0.0 | 267.471 | 8951.261 | 83908.403 | 161558.637 | 0.01 | 14 | 21 |
| WaterChamberEvent | 53 | 0.001 | 8.69 | 24.28 | 98.348 | 164.397 | 2.47 | 1 | 0 |
| argumentationAnswerEvent | 48 | 0.103 | 9.982 | 16465.797 | 92932.529 | 367580.254 | 0.0 | 0 | 6 |
| DEBUGMenu | 47 | 6.311 | 719.749 | 18605.744 | 103100.846 | 161547.35 | 0.0 | 0 | 25 |
| gameWindowFocusEvent | 32 | 88.659 | 1747.562 | 27327.033 | 119886.776 | 161556.618 | 0.0 | 0 | 25 |
| soilMachine | 23 | 0.572 | 4.56 | 33.847 | 210.547 | 322.424 | 1.77 | 0 | 0 |
| gameStartEvent | 22 | 241.69 | 9123.103 | 39748.411 | 130884.078 | 161556.618 | 0.0 | 0 | 20 |
| argumentationEvent | 20 | 0.03 | 126.724 | 39525.605 | 162905.06 | 367499.061 | 0.0 | 2 | 6 |
| gameWindowUnfocusEvent | 20 | 25.895 | 6299.851 | 43197.545 | 134106.156 | 162962.936 | 0.0 | 0 | 15 |
| DaniEvent | 11 | 0.874 | 8.979 | 29164.179 | 157843.832 | 163754.027 | 0.0 | 0 | 4 |
| argumentationToolEvent | 8 | 0.062 | 2.535 | 10621.256 | 55192.85 | 84856.436 | 0.01 | 0 | 1 |
| TerasGardenBox | 5 | 1.093 | 1.624 | 10.882 | 26.589 | 27.454 | 5.51 | 0 | 0 |
| EndOfUnit | 4 | 3047.712 | 167267.585 | 176396.228 | 350033.331 | 368002.029 | 0.0 | 0 | 4 |
| SolarStillDesignEvent | 3 | 1.101 | 1.674 | 2.22 | 3.663 | 3.884 | 27.03 | 0 | 0 |
| chatEvent | 1 | 1696.822 | 1696.822 | 1696.822 | 1696.822 | 1696.822 | 0.04 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 8 group(s), 18 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[5417] _id=6ac9997dde269131f9cb2463 ts=2026-10-10T01:48:43.9120000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[5418] _id=6ac9997dde269131f9cb2464 ts=2026-10-10T01:48:43.9120000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[5419] _id=6ac9997dde269131f9cb2465 ts=2026-10-10T01:48:43.9130000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[5420] _id=6ac9997dde269131f9cb2466 ts=2026-10-10T01:48:43.9130000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[9243] _id=6ace3731de269131f9cee4e3 ts=2026-10-13T13:50:40.3970000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[9244] _id=6ace3731de269131f9cee4e4 ts=2026-10-13T13:50:40.3970000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 99 group(s), 234 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[1856] _id=6ac6983ade269131f9beea25 ts=2026-10-07T19:06:32.9560000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[1851] _id=6ac6983ade269131f9beea37 ts=2026-10-07T19:06:32.9560000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1862] _id=6ac6983bde269131f9beea6c ts=2026-10-07T19:06:33.4940000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[1863] _id=6ac6983bde269131f9beea6d ts=2026-10-07T19:06:33.4940000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1871] _id=6ac69842de269131f9beeb35 ts=2026-10-07T19:06:39.6860000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[1872] _id=6ac69842de269131f9beeb37 ts=2026-10-07T19:06:39.6860000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[18431] _id=6ad15722de269131f9e1dc71 ts=2026-10-15T22:43:45.3870000Z == 6ab9a9279a8420a1e6b56b7f.jsonl[18443] _id=6ad15722de269131f9e1dc72 ts=2026-10-15T22:43:45.3870000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 142 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `542ms: 6ab9a9279a8420a1e6b56b7f.jsonl[166] _id=6ac53ee7de269131f9b67e29 ts=2026-10-06T18:33:10.9650000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[170] _id=6ac53ee8de269131f9b67e37 ts=2026-10-06T18:33:11.5070000Z`; `196ms: 6ab9a9279a8420a1e6b56b7f.jsonl[170] _id=6ac53ee8de269131f9b67e37 ts=2026-10-06T18:33:11.5070000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[168] _id=6ac53ee8de269131f9b67e43 ts=2026-10-06T18:33:11.7030000Z`; `291ms: 6ab9a9279a8420a1e6b56b7f.jsonl[168] _id=6ac53ee8de269131f9b67e43 ts=2026-10-06T18:33:11.7030000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[116] _id=6ac53ee8de269131f9b67e4d ts=2026-10-06T18:33:11.9940000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `172ms: 6ab9a9279a8420a1e6b56b7f.jsonl[7155] _id=6acc1e5ede269131f9cb69ef ts=2026-10-11T23:40:13.8140000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[7083] _id=6acc1e5ede269131f9cb69f1 ts=2026-10-11T23:40:13.9860000Z`; `173ms: 6ab9a9279a8420a1e6b56b7f.jsonl[7083] _id=6acc1e5ede269131f9cb69f1 ts=2026-10-11T23:40:13.9860000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[7084] _id=6acc1e5ede269131f9cb69f3 ts=2026-10-11T23:40:14.1590000Z`; `114ms: 6ab9a9279a8420a1e6b56b7f.jsonl[7084] _id=6acc1e5ede269131f9cb69f3 ts=2026-10-11T23:40:14.1590000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[7085] _id=6acc1e5ede269131f9cb69f5 ts=2026-10-11T23:40:14.2730000Z`
- **INFO / Info** `WaterChamberEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `360ms: 6ab9a9279a8420a1e6b56b7f.jsonl[17816] _id=6ad15237de269131f9e1d23c ts=2026-10-15T22:22:46.3460000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[17857] _id=6ad15237de269131f9e1d245 ts=2026-10-15T22:22:46.7060000Z`; `274ms: 6ab9a9279a8420a1e6b56b7f.jsonl[18017] _id=6ad153adde269131f9e1d5f4 ts=2026-10-15T22:29:00.3130000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[18021] _id=6ad153adde269131f9e1d5fa ts=2026-10-15T22:29:00.5870000Z`; `672ms: 6ab9a9279a8420a1e6b56b7f.jsonl[18166] _id=6ad154a1de269131f9e1d85f ts=2026-10-15T22:33:04.8040000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[18169] _id=6ad154a2de269131f9e1d867 ts=2026-10-15T22:33:05.4760000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 9 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `301ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1291] _id=6ac547ecde269131f9b76e7b ts=2026-10-06T19:11:39.4480000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[1292] _id=6ac547ecde269131f9b76e7f ts=2026-10-06T19:11:39.7490000Z`; `258ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1292] _id=6ac547ecde269131f9b76e7f ts=2026-10-06T19:11:39.7490000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[1289] _id=6ac547ecde269131f9b76e87 ts=2026-10-06T19:11:40.0070000Z`; `301ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1289] _id=6ac547ecde269131f9b76e87 ts=2026-10-06T19:11:40.0070000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[1294] _id=6ac547edde269131f9b76e8f ts=2026-10-06T19:11:40.3080000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `32ms: 6ab9a9279a8420a1e6b56b7f.jsonl[10410] _id=6ace83a0de269131f9d1b92c ts=2026-10-13T19:16:47.6470000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[10422] _id=6ace83a0de269131f9d1b92f ts=2026-10-13T19:16:47.6790000Z`; `69ms: 6ab9a9279a8420a1e6b56b7f.jsonl[10879] _id=6acfcd8ede269131f9d77398 ts=2026-10-14T18:44:30.2270000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[10882] _id=6acfcd8ede269131f9d7739e ts=2026-10-14T18:44:30.2960000Z`; `30ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16743] _id=6ad14a5dde269131f9e1a409 ts=2026-10-15T21:49:16.4020000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[16746] _id=6ad14a5dde269131f9e1a40c ts=2026-10-15T21:49:16.4320000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `381ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1173] _id=6ac546f4de269131f9b75a5b ts=2026-10-06T19:07:31.2450000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[1182] _id=6ac546f4de269131f9b75a63 ts=2026-10-06T19:07:31.6260000Z`; `900ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1181] _id=6ac546f4de269131f9b75a61 ts=2026-10-06T19:07:31.3720000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[1185] _id=6ac546f5de269131f9b75a77 ts=2026-10-06T19:07:32.2720000Z`; `21ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1190] _id=6ac546f9de269131f9b75b1d ts=2026-10-06T19:07:37.0370000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[1189] _id=6ac546fade269131f9b75b23 ts=2026-10-06T19:07:37.0580000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9279a8420a1e6b56b7f.jsonl[18571] _id=6ad158ddde269131f9e1e104 ts=2026-10-15T22:51:09.0090000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[18572] _id=6ad158dede269131f9e1e108 ts=2026-10-15T22:51:09.0140000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `920ms: 6ab9a9279a8420a1e6b56b7f.jsonl[15549] _id=6ad1234cde269131f9dfbec4 ts=2026-10-15T19:02:35.9150000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[15547] _id=6ad1234dde269131f9dfbee8 ts=2026-10-15T19:02:36.8350000Z`; `687ms: 6ab9a9279a8420a1e6b56b7f.jsonl[15547] _id=6ad1234dde269131f9dfbee8 ts=2026-10-15T19:02:36.8350000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[15554] _id=6ad1234ede269131f9dfbf02 ts=2026-10-15T19:02:37.5220000Z`; `798ms: 6ab9a9279a8420a1e6b56b7f.jsonl[15566] _id=6ad1238ade269131f9dfc809 ts=2026-10-15T19:03:37.4210000Z ~ 6ab9a9279a8420a1e6b56b7f.jsonl[15610] _id=6ad1238bde269131f9dfc828 ts=2026-10-15T19:03:38.2190000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 44h 52m 
  - Evidence: 44h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[5414] _id=6ac99979de269131f9cb245f ts=2026-10-10T01:48:41.1010000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6140] _id=6acc1084de269131f9cb61f0 ts=2026-10-11T22:41:08.4510000Z; 36h 39m: 6ab9a9279a8420a1e6b56b7f.jsonl[9236] _id=6acc338cde269131f9cb84a6 ts=2026-10-12T01:10:35.6450000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9237] _id=6ace371bde269131f9cee39e ts=2026-10-13T13:50:19.0800000Z; 30h 32m: 6ab9a9279a8420a1e6b56b7f.jsonl[2574] _id=6ac7e5bade269131f9c58cf0 ts=2026-10-08T18:49:29.5080000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[4988] _id=6ac9934cde269131f9cb1c5a ts=2026-10-10T01:22:19.2630000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 45h 29m 
  - Evidence: 45h 29m: 6ab9a9279a8420a1e6b56b7f.jsonl[6096] _id=6ac99942de269131f9cb2420 ts=2026-10-10T01:47:45.6140000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6701] _id=6acc18ebde269131f9cb665c ts=2026-10-11T23:16:59.6410000Z; 42h 12m: 6ab9a9279a8420a1e6b56b7f.jsonl[8626] _id=6acc2cc8de269131f9cb768c ts=2026-10-12T00:41:43.7780000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9690] _id=6ace7e45de269131f9d130df ts=2026-10-13T18:53:57.4140000Z; 1h 3m: 6ab9a9279a8420a1e6b56b7f.jsonl[7094] _id=6acc1dd5de269131f9cb6973 ts=2026-10-11T23:37:57.7760000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[8707] _id=6acc2cc4de269131f9cb7683 ts=2026-10-12T00:41:39.8560000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 44h 55m 
  - Evidence: 44h 55m: 6ab9a9279a8420a1e6b56b7f.jsonl[6091] _id=6ac99935de269131f9cb2414 ts=2026-10-10T01:47:32.8350000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6173] _id=6acc10e1de269131f9cb621b ts=2026-10-11T22:42:41.8210000Z; 36h 40m: 6ab9a9279a8420a1e6b56b7f.jsonl[9234] _id=6acc337ade269131f9cb847a ts=2026-10-12T01:10:17.5490000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9255] _id=6ace3739de269131f9cee53e ts=2026-10-13T13:50:48.8600000Z; 30h 6m: 6ab9a9279a8420a1e6b56b7f.jsonl[4977] _id=6ac7ec35de269131f9c683cc ts=2026-10-08T19:17:09.1430000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5017] _id=6ac9937ede269131f9cb1c84 ts=2026-10-10T01:23:09.3960000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 743 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[10858] _id=6acfcd70de269131f9d76fd7 ts=2026-10-14T18:43:59.9450000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[10859] _id=6acfcd70de269131f9d76fd8 ts=2026-10-14T18:43:59.9450000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16572] _id=6ad1499ede269131f9e19e33 ts=2026-10-15T21:46:05.5390000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16573] _id=6ad1499ede269131f9e19e34 ts=2026-10-15T21:46:05.5390000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16604] _id=6ad149c2de269131f9e1a041 ts=2026-10-15T21:46:41.1930000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16605] _id=6ad149c2de269131f9e1a042 ts=2026-10-15T21:46:41.1930000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 102h 13m 
  - Evidence: 102h 13m: 6ab9a9279a8420a1e6b56b7f.jsonl[1684] _id=6ac695f8de269131f9be878c ts=2026-10-07T18:56:55.5010000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9233] _id=6acc337ade269131f9cb8478 ts=2026-10-12T01:10:17.5300000Z; 68h 56m: 6ab9a9279a8420a1e6b56b7f.jsonl[9233] _id=6acc337ade269131f9cb8478 ts=2026-10-12T01:10:17.5300000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[13309] _id=6acffd0cde269131f9d98d2b ts=2026-10-14T22:07:08.2380000Z; 23h 58m: 6ab9a9279a8420a1e6b56b7f.jsonl[13309] _id=6acffd0cde269131f9d98d2b ts=2026-10-14T22:07:08.2380000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[17071] _id=6ad14e41de269131f9e1c311 ts=2026-10-15T22:05:52.7010000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 44h 52m 
  - Evidence: 44h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[6112] _id=6ac9997dde269131f9cb2468 ts=2026-10-10T01:48:44.6400000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6144] _id=6acc10a0de269131f9cb61fb ts=2026-10-11T22:41:36.1750000Z; 36h 40m: 6ab9a9279a8420a1e6b56b7f.jsonl[9194] _id=6acc3357de269131f9cb8432 ts=2026-10-12T01:09:42.3560000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9242] _id=6ace3731de269131f9cee4e2 ts=2026-10-13T13:50:40.3940000Z; 30h 7m: 6ab9a9279a8420a1e6b56b7f.jsonl[4952] _id=6ac7ebcfde269131f9c6772b ts=2026-10-08T19:15:26.7420000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[4999] _id=6ac99367de269131f9cb1c66 ts=2026-10-10T01:22:46.3220000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 105 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[11094] _id=6acfcf55de269131f9d7a59d ts=2026-10-14T18:52:05.0470000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11095] _id=6acfcf55de269131f9d7a59e ts=2026-10-14T18:52:05.0470000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[11770] _id=6acfd159de269131f9d7dd5c ts=2026-10-14T19:00:40.5590000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11771] _id=6acfd159de269131f9d7dd5d ts=2026-10-14T19:00:40.5590000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[13321] _id=6ad01e7dde269131f9d9c456 ts=2026-10-15T00:29:48.6510000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[13322] _id=6ad01e7dde269131f9d9c457 ts=2026-10-15T00:29:48.6510000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 45h 47m 
  - Evidence: 45h 47m: 6ab9a9279a8420a1e6b56b7f.jsonl[5687] _id=6ac9951cde269131f9cb2139 ts=2026-10-10T01:30:03.8160000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6690] _id=6acc18f6de269131f9cb666a ts=2026-10-11T23:17:10.6150000Z; 41h 47m: 6ab9a9279a8420a1e6b56b7f.jsonl[8983] _id=6acc2fe1de269131f9cb7caf ts=2026-10-12T00:54:57.0960000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9339] _id=6ace7ba1de269131f9d110c4 ts=2026-10-13T18:42:40.7780000Z; 30h 13m: 6ab9a9279a8420a1e6b56b7f.jsonl[4807] _id=6ac7eab7de269131f9c658c2 ts=2026-10-08T19:10:46.4600000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5041] _id=6ac993a5de269131f9cb1ca1 ts=2026-10-10T01:23:49.0860000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16343] _id=6ad14852de269131f9e19166 ts=2026-10-15T21:40:33.2050000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16344] _id=6ad14852de269131f9e19167 ts=2026-10-15T21:40:33.2050000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16474] _id=6ad148aede269131f9e19453 ts=2026-10-15T21:42:05.0970000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16475] _id=6ad148aede269131f9e19454 ts=2026-10-15T21:42:05.0970000Z; 4ms: 6ab9a9279a8420a1e6b56b7f.jsonl[589] _id=6ac53faade269131f9b695bf ts=2026-10-06T18:36:25.3430000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[583] _id=6ac53faade269131f9b695c5 ts=2026-10-06T18:36:25.3470000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 44h 52m 
  - Evidence: 44h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[5415] _id=6ac9997dde269131f9cb2461 ts=2026-10-10T01:48:41.1130000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6135] _id=6acc1093de269131f9cb61f6 ts=2026-10-11T22:41:18.3540000Z; 30h 4m: 6ab9a9279a8420a1e6b56b7f.jsonl[4983] _id=6ac7ec65de269131f9c6884d ts=2026-10-08T19:17:56.4210000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[4996] _id=6ac9935bde269131f9cb1c61 ts=2026-10-10T01:22:31.5200000Z; 23h 32m: 6ab9a9279a8420a1e6b56b7f.jsonl[2569] _id=6ac69abbde269131f9bf2094 ts=2026-10-07T19:17:14.7400000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[2575] _id=6ac7e5bdde269131f9c58d2f ts=2026-10-08T18:49:29.5230000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 66h 0m 
  - Evidence: 66h 0m: 6ab9a9279a8420a1e6b56b7f.jsonl[8914] _id=6acc2efede269131f9cb7b83 ts=2026-10-12T00:51:08.4720000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11097] _id=6acfcf56de269131f9d7a5ad ts=2026-10-14T18:52:05.0550000Z; 45h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[5784] _id=6ac99567de269131f9cb21cc ts=2026-10-10T01:31:17.8810000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6803] _id=6acc1a7bde269131f9cb673f ts=2026-10-11T23:23:38.7130000Z; 30h 10m: 6ab9a9279a8420a1e6b56b7f.jsonl[4936] _id=6ac7eb96de269131f9c67163 ts=2026-10-08T19:14:28.1490000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5121] _id=6ac9946fde269131f9cb1d5f ts=2026-10-10T01:25:05.1770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2887 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[11097] _id=6acfcf56de269131f9d7a5ad ts=2026-10-14T18:52:05.0550000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11091] _id=6acfcf56de269131f9d7a5af ts=2026-10-14T18:52:05.0550000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[11106] _id=6acfcf6bde269131f9d7a7de ts=2026-10-14T18:52:25.7990000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11107] _id=6acfcf6bde269131f9d7a7ec ts=2026-10-14T18:52:25.7990000Z; 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[11115] _id=6acfcf71de269131f9d7a84a ts=2026-10-14T18:52:31.6460000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11116] _id=6acfcf71de269131f9d7a84b ts=2026-10-14T18:52:31.6460000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 66h 44m 
  - Evidence: 66h 44m: 6ab9a9279a8420a1e6b56b7f.jsonl[7304] _id=6acc2426de269131f9cb6b21 ts=2026-10-12T00:04:54.1900000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[11016] _id=6acfce9bde269131f9d79450 ts=2026-10-14T18:48:58.5700000Z; 45h 47m: 6ab9a9279a8420a1e6b56b7f.jsonl[5704] _id=6ac9951fde269131f9cb213d ts=2026-10-10T01:30:06.8390000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6705] _id=6acc18f6de269131f9cb6668 ts=2026-10-11T23:17:10.6100000Z; 30h 19m: 6ab9a9279a8420a1e6b56b7f.jsonl[4808] _id=6ac7eabade269131f9c65902 ts=2026-10-08T19:10:49.6260000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5686] _id=6ac9951cde269131f9cb2137 ts=2026-10-10T01:30:03.8110000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.033s..0.033s shown 
  - Evidence: 33ms: 6ab9a9279a8420a1e6b56b7f.jsonl[13458] _id=6ad02007de269131f9d9cb0c ts=2026-10-15T00:36:23.1150000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[13459] _id=6ad02008de269131f9d9cb0e ts=2026-10-15T00:36:23.1480000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 44h 56m 
  - Evidence: 44h 56m: 6ab9a9279a8420a1e6b56b7f.jsonl[6022] _id=6ac99957de269131f9cb2446 ts=2026-10-10T01:48:06.7910000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6196] _id=6acc1142de269131f9cb6261 ts=2026-10-11T22:44:18.6180000Z; 42h 0m: 6ab9a9279a8420a1e6b56b7f.jsonl[8629] _id=6acc2cd2de269131f9cb769a ts=2026-10-12T00:41:53.7080000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9340] _id=6ace7b90de269131f9d10fbe ts=2026-10-13T18:42:23.8310000Z; 30h 27m: 6ab9a9279a8420a1e6b56b7f.jsonl[2991] _id=6ac7e7c5de269131f9c5d63b ts=2026-10-08T18:58:12.3860000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5076] _id=6ac99406de269131f9cb1cfa ts=2026-10-10T01:25:25.5000000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.018s..0.027s shown 
  - Evidence: 18ms: 6ab9a9279a8420a1e6b56b7f.jsonl[5976] _id=6ac998afde269131f9cb2347 ts=2026-10-10T01:45:19.0800000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5980] _id=6ac998afde269131f9cb234b ts=2026-10-10T01:45:19.0980000Z; 23ms: 6ab9a9279a8420a1e6b56b7f.jsonl[6205] _id=6acc1155de269131f9cb6269 ts=2026-10-11T22:44:37.7250000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6209] _id=6acc1155de269131f9cb626d ts=2026-10-11T22:44:37.7480000Z; 27ms: 6ab9a9279a8420a1e6b56b7f.jsonl[5967] _id=6ac998afde269131f9cb2345 ts=2026-10-10T01:45:19.0530000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[5976] _id=6ac998afde269131f9cb2347 ts=2026-10-10T01:45:19.0800000Z
- **INFO / Info** `WaterChamberEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b7f.jsonl[18019] _id=6ad153adde269131f9e1d5f8 ts=2026-10-15T22:29:00.5860000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[18021] _id=6ad153adde269131f9e1d5fa ts=2026-10-15T22:29:00.5870000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 102h 6m 
  - Evidence: 102h 6m: 6ab9a9279a8420a1e6b56b7f.jsonl[1582] _id=6ac69533de269131f9be5898 ts=2026-10-07T18:53:38.8370000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9099] _id=6acc310fde269131f9cb7eb9 ts=2026-10-12T00:59:59.0910000Z; 42h 16m: 6ab9a9279a8420a1e6b56b7f.jsonl[9099] _id=6acc310fde269131f9cb7eb9 ts=2026-10-12T00:59:59.0910000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[10418] _id=6ace839fde269131f9d1b92a ts=2026-10-13T19:16:47.6310000Z; 27h 1m: 6ab9a9279a8420a1e6b56b7f.jsonl[10878] _id=6acfcd8ede269131f9d77392 ts=2026-10-14T18:44:30.2060000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16575] _id=6ad1499ede269131f9e19e31 ts=2026-10-15T21:46:05.5150000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 102h 4m 
  - Evidence: 102h 4m: 6ab9a9279a8420a1e6b56b7f.jsonl[1583] _id=6ac69533de269131f9be589c ts=2026-10-07T18:53:38.8680000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9043] _id=6acc30bede269131f9cb7de2 ts=2026-10-12T00:58:37.9290000Z; 42h 15m: 6ab9a9279a8420a1e6b56b7f.jsonl[9100] _id=6acc310fde269131f9cb7ebb ts=2026-10-12T00:59:59.1190000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[10378] _id=6ace8358de269131f9d1b147 ts=2026-10-13T19:15:36.0740000Z; 27h 0m: 6ab9a9279a8420a1e6b56b7f.jsonl[10882] _id=6acfcd8ede269131f9d7739e ts=2026-10-14T18:44:30.2960000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16525] _id=6ad14947de269131f9e199a7 ts=2026-10-15T21:44:38.5680000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.030s..0.032s shown 
  - Evidence: 30ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16743] _id=6ad14a5dde269131f9e1a409 ts=2026-10-15T21:49:16.4020000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16746] _id=6ad14a5dde269131f9e1a40c ts=2026-10-15T21:49:16.4320000Z; 32ms: 6ab9a9279a8420a1e6b56b7f.jsonl[10410] _id=6ace83a0de269131f9d1b92c ts=2026-10-13T19:16:47.6470000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[10422] _id=6ace83a0de269131f9d1b92f ts=2026-10-13T19:16:47.6790000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 102h 5m 
  - Evidence: 102h 5m: 6ab9a9279a8420a1e6b56b7f.jsonl[1581] _id=6ac69531de269131f9be5823 ts=2026-10-07T18:53:36.3580000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9040] _id=6acc30c6de269131f9cb7df7 ts=2026-10-12T00:58:46.1770000Z; 42h 15m: 6ab9a9279a8420a1e6b56b7f.jsonl[9087] _id=6acc3105de269131f9cb7ead ts=2026-10-12T00:59:48.4610000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[10380] _id=6ace835cde269131f9d1b18d ts=2026-10-13T19:15:40.5900000Z; 27h 0m: 6ab9a9279a8420a1e6b56b7f.jsonl[10877] _id=6acfcd8dde269131f9d77386 ts=2026-10-14T18:44:29.0600000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16522] _id=6ad14943de269131f9e19960 ts=2026-10-15T21:44:34.7100000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 42 interval(s) ≤ 0.005s..0.006s shown 
  - Evidence: 5ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16732] _id=6ad14a5cde269131f9e1a3ff ts=2026-10-15T21:49:15.4690000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16740] _id=6ad14a5cde269131f9e1a401 ts=2026-10-15T21:49:15.4740000Z; 5ms: 6ab9a9279a8420a1e6b56b7f.jsonl[18368] _id=6ad156bdde269131f9e1db81 ts=2026-10-15T22:42:04.0680000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[18364] _id=6ad156bdde269131f9e1db87 ts=2026-10-15T22:42:04.0730000Z; 6ms: 6ab9a9279a8420a1e6b56b7f.jsonl[16720] _id=6ad14a40de269131f9e1a38c ts=2026-10-15T21:48:47.9070000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[16723] _id=6ad14a40de269131f9e1a38e ts=2026-10-15T21:48:47.9130000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 34m 
  - Evidence: 23h 34m: 6ab9a9279a8420a1e6b56b7f.jsonl[1314] _id=6ac54852de269131f9b77881 ts=2026-10-06T19:13:21.5040000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[1495] _id=6ac693cade269131f9be11fe ts=2026-10-07T18:47:37.9400000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 28m 16s 
  - Evidence: 28m 16s: 6ab9a9279a8420a1e6b56b7f.jsonl[17087] _id=6ad14e64de269131f9e1c418 ts=2026-10-15T22:06:27.9420000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[18207] _id=6ad15505de269131f9e1d93b ts=2026-10-15T22:34:44.7640000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 44h 52m 
  - Evidence: 44h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[5413] _id=6ac99970de269131f9cb245d ts=2026-10-10T01:48:31.9920000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6142] _id=6acc1084de269131f9cb61f2 ts=2026-10-11T22:41:08.6100000Z; 36h 39m: 6ab9a9279a8420a1e6b56b7f.jsonl[9229] _id=6acc338cde269131f9cb84ab ts=2026-10-12T01:10:35.7950000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9239] _id=6ace371bde269131f9cee3aa ts=2026-10-13T13:50:19.6030000Z; 30h 33m: 6ab9a9279a8420a1e6b56b7f.jsonl[2573] _id=6ac7e5a7de269131f9c58b86 ts=2026-10-08T18:49:10.2280000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[4986] _id=6ac9934cde269131f9cb1c5d ts=2026-10-10T01:22:19.4320000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 25 gap(s), longest 44h 52m 
  - Evidence: 44h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[5412] _id=6ac99970de269131f9cb245c ts=2026-10-10T01:48:31.9920000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6141] _id=6acc1084de269131f9cb61f1 ts=2026-10-11T22:41:08.6100000Z; 36h 39m: 6ab9a9279a8420a1e6b56b7f.jsonl[9228] _id=6acc338cde269131f9cb84aa ts=2026-10-12T01:10:35.7940000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9238] _id=6ace371bde269131f9cee3a9 ts=2026-10-13T13:50:19.6030000Z; 30h 33m: 6ab9a9279a8420a1e6b56b7f.jsonl[2572] _id=6ac7e5a7de269131f9c58b85 ts=2026-10-08T18:49:10.2280000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[4985] _id=6ac9934cde269131f9cb1c5c ts=2026-10-10T01:22:19.4320000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 45h 16m 
  - Evidence: 45h 16m: 6ab9a9279a8420a1e6b56b7f.jsonl[6139] _id=6acc1084de269131f9cb61ee ts=2026-10-10T01:48:51.582Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6494] _id=6acc1616de269131f9cb649e ts=2026-10-11T23:04:54.5180000Z; 36h 49m: 6ab9a9279a8420a1e6b56b7f.jsonl[9128] _id=6acc3175de269131f9cb7f8a ts=2026-10-12T01:01:40.2420000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9266] _id=6ace7a46de269131f9d0fbb7 ts=2026-10-13T13:51:27.62Z; 30h 28m: 6ab9a9279a8420a1e6b56b7f.jsonl[4982] _id=6ac7ec62de269131f9c68825 ts=2026-10-08T19:17:53.3790000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6019] _id=6ac998f3de269131f9cb2398 ts=2026-10-10T01:46:26.4130000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 44h 52m 
  - Evidence: 44h 52m: 6ab9a9279a8420a1e6b56b7f.jsonl[5421] _id=6ac9997dde269131f9cb2467 ts=2026-10-10T01:48:44.0980000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[6136] _id=6acc1093de269131f9cb61f7 ts=2026-10-11T22:41:22.7350000Z; 41h 30m: 6ab9a9279a8420a1e6b56b7f.jsonl[9220] _id=6acc3370de269131f9cb8460 ts=2026-10-12T01:10:07.7890000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[9312] _id=6ace7b30de269131f9d10b8c ts=2026-10-13T18:40:47.9650000Z; 30h 6m: 6ab9a9279a8420a1e6b56b7f.jsonl[4955] _id=6ac7ebe8de269131f9c679aa ts=2026-10-08T19:15:52.0490000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[4997] _id=6ac9935bde269131f9cb1c62 ts=2026-10-10T01:22:33.9670000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 14 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6ab9a9279a8420a1e6b56b7f.jsonl[18431] _id=6ad15722de269131f9e1dc71 ts=2026-10-15T22:43:45.3870000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[18443] _id=6ad15722de269131f9e1dc72 ts=2026-10-15T22:43:45.3870000Z; 2ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1470] _id=6ac69353de269131f9be0105 ts=2026-10-07T18:45:38.8320000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[1471] _id=6ac69353de269131f9be0106 ts=2026-10-07T18:45:38.8340000Z; 3ms: 6ab9a9279a8420a1e6b56b7f.jsonl[1152] _id=6ac54693de269131f9b749ef ts=2026-10-06T19:05:54.5310000Z -> 6ab9a9279a8420a1e6b56b7f.jsonl[1153] _id=6ac54693de269131f9b749f5 ts=2026-10-06T19:05:54.5340000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 14 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[1004] _id=6ac5451cde269131f9b7223b ts=2026-10-06T18:59:39.7610000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1352] _id=6ac548a4de269131f9b7829d ts=2026-10-06T19:14:43.3710000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1591] _id=6ac6954ede269131f9be5f62 ts=2026-10-07T18:54:05.1430000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[10422] _id=6ace83a0de269131f9d1b92f ts=2026-10-13T19:16:47.6790000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[10882] _id=6acfcd8ede269131f9d7739e ts=2026-10-14T18:44:30.2960000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[16746] _id=6ad14a5dde269131f9e1a40c ts=2026-10-15T21:49:16.4320000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[1189] _id=6ac546fade269131f9b75b23 ts=2026-10-06T19:07:37.0580000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[17087] _id=6ad14e64de269131f9e1c418 ts=2026-10-15T22:06:27.9420000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[18207] _id=6ad15505de269131f9e1d93b ts=2026-10-15T22:34:44.7640000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[14977] _id=6ad11facde269131f9df49a0 ts=2026-10-15T18:47:07.7670000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[9162] _id=6acc32b4de269131f9cb82e1 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 36 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[7803] _id=6acc25a7de269131f9cb6f15 ts=2026-10-12T00:11:17.2930000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[7812] _id=6acc25a9de269131f9cb6f2b ts=2026-10-12T00:11:19.9860000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[7813] _id=6acc25a9de269131f9cb6f2d ts=2026-10-12T00:11:20.0770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 367 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[1855] _id=6ac6983ade269131f9beea24 ts=2026-10-07T19:06:32.8040000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1856] _id=6ac6983ade269131f9beea25 ts=2026-10-07T19:06:32.9560000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1851] _id=6ac6983ade269131f9beea37 ts=2026-10-07T19:06:32.9560000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[1281] _id=6ac547e6de269131f9b76e17 ts=2026-10-06T19:11:33.6440000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1283] _id=6ac547e7de269131f9b76e39 ts=2026-10-06T19:11:34.9670000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[1313] _id=6ac54850de269131f9b77837 ts=2026-10-06T19:13:19.2560000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 24 unmatched 'DialogueStartEvent' (totals: 507 start, 497 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 24 unmatched 'BecameVisible' (totals: 1997 open, 1973 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 59 start, 40 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 443 of 18669 adjacent _id pairs reverse in client time; worst 266.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9279a8420a1e6b56b7f.jsonl[3079] _id=6ac7e817de269131f9c5e182 ts=2026-10-08T18:59:34.5700000Z`; `6ab9a9279a8420a1e6b56b7f.jsonl[3078] _id=6ac7e818de269131f9c5e197 ts=2026-10-08T18:55:08.4300000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.88s, min -161537.08s, max -0.12s over 18670 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9279a8420a1e6b56b7f\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 5740 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3650); Unit 4 Dev (1060); Unit 3 Dungeon Dev (630); Unit 5 Dev - Dungeon (400)
- **Intervals:** median 0.05s (p5 0.00s / p95 2.03s, n=5739)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5740/5740 records)
    "BecameVisible"  x1997
    "BecameInvisible"  x1973
    "BecameCameraCentered"  x885
    "BecameCameraUncentered"  x885
data.pieceId  (string, 5740/5740 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5740/5740 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 5456 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1583); Unit 3 Dev (960); Unit 4 Dev - Dungeon (897); Unit 1 Dev (674); Unit 3 Dungeon Dev (610); Unit 5 Dev - Dungeon (390); Unit 4 Dev (223); Unit 4 Dev - Anderson Base (68); Unit 5 Dev (51)
- **Intervals:** median 1.38s (p5 0.14s / p95 18.78s, n=5455)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5456/5456 records)
    "pressed"  x5456
data.actionType  (string, 5456/5456 records)
    "Move"  x3888
    "Interact"  x910
    "Jump"  x413
    "Ascend"  x82
    "Hoverboard"  x77
    "Descend"  x43
    "Sprint"  x27
    "Map"  x13
    "SkipCinematic"  x3
data.key  (string, 5456/5456 records, 24 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5456/5456 records)
    "Player"  x4535
    "Drone"  x921
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 3145 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (1192); Unit 3 Dev (481); Unit 1 Dev (396); Unit 3 Dungeon Dev (236); Unit 4 Dev (236); Unit 4 Dev - Dungeon (229); Unit 5 Dev - Dungeon (169); Unit 5 Dev (125); Unit 4 Dev - Anderson Base (81)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.10s, n=3133)
- **Fields under `data`:**

```text
data.position  (object, 3145/3145 records)
data.position.x  (number, 3145/3145 records)
    numeric range -756.219 .. 1559.67 (1274 unique)
data.position.y  (number, 3145/3145 records)
    numeric range -114.337 .. 222.652 (786 unique)
data.position.z  (number, 3145/3145 records)
    numeric range -1045.06 .. 2123.73 (1271 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2667 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (739); Unit 3 Dev (566); Unit 1 Dev (292); Unit 4 Dev (289); Unit 3 Dungeon Dev (231); Unit 5 Dev (223); Unit 4 Dev - Dungeon (127); Unit 4 Dev - Anderson Base (111); Unit 5 Dev - Dungeon (89)
- **eventKey:** present on 1663 of 2667 records
- **Intervals:** median 4.62s (p5 0.00s / p95 37.38s, n=2666)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1663; [conversationId, dialogueEventType] x1004
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2667/2667 records)
    numeric range 8 .. 118 (57 unique)
data.dialogueEventType  (string, 2667/2667 records)
    "DialogueNodeEvent"  x1663
    "DialogueStartEvent"  x507
    "DialogueFinishEvent"  x497
data.nodeId  (number, 1663/2667 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 504 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (147); Unit 4 Dev - Dungeon (102); Unit 3 Dungeon Dev (91); Unit 2 Prod (Refactor) (90); Unit 4 Dev (20); Unit 5 Dev - Dungeon (20); Unit 3 Dev (14); Unit 5 Dev (11); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 7.05s (p5 0.16s / p95 384.63s, n=503)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 504/504 records)
    42 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 504/504 records)
    111 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 425 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (129); Unit 3 Dev (106); Unit 1 Dev (97); Unit 5 Dev (50); Unit 2 Prod (Refactor) (43)
- **Intervals:** median 0.64s (p5 0.03s / p95 13.04s, n=424)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 425/425 records)
    "argumentationNodeHoverEnd"  x181
    "argumentationNodeHoverStart"  x180
    "argumentationNodeAdd"  x46
    "argumentationNodeRemove"  x18
data.argumentationTitle  (string, 425/425 records)
    "Unit 4 - Flooding"  x129
    "Unit 3 - Pollution Upstream"  x106
    "Unit 1 - Freshwater"  x74
    "Unit 5"  x50
    "Unit 2 – Watershed"  x43
    "Unit 1 - Argumentation Tutorial"  x23
data.nodeName  (string, 425/425 records)
    "A"  x70
    "1"  x63
    "I"  x63
    "B"  x46
    "II"  x39
    "2"  x37
    "D"  x36
    "3"  x27
    "C"  x24
    "4"  x12
    "5"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 210 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (78); Unit 4 Dev (68); Unit 3 Dev (64)
- **Intervals:** median 1.06s (p5 0.14s / p95 21.40s, n=209)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x196; [Soil Key Puzzle Status, Unit] x14
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 14/210 records)
    "Finished"  x7
    "Started"  x7
data.Unit  (string, 14/210 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 196/210 records)
    "RightDrag"  x104
    "LeftDrag"  x92
data.currentSoilType  (string, 196/210 records)
    "SAND"  x38
    "CLAYSAND"  x36
    "CLAY"  x34
    "SANDGRAVEL"  x32
    "CLAYROCK"  x30
    "GRAVEL"  x14
    "BEDROCK"  x12
data.isCorrectSelection  (string, 196/210 records)
    "false"  x154
    "true"  x42
data.waterLevelStatus  (string, 196/210 records)
    "Proper"  x72
    "TooHigh"  x64
    "TooLow"  x60
data.waterRetentionChange  (string, 196/210 records)
    "Decrease"  x77
    "Increase"  x77
    "NoChange"  x42
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 113 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (88); Unit 3 Dev (21); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2)
- **Intervals:** median 7.02s (p5 0.15s / p95 39083.24s, n=112)
- **`data` key-set variants:** [actionType, featureUsed] x80; [actionType, featureUsed, location] x33
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 113/113 records)
    "MapCloseEvent"  x40
    "MapOpenEvent"  x40
    "WaypointMoveEvent"  x26
    "WaypointSetEvent"  x7
data.featureUsed  (string, 113/113 records)
    "Map"  x80
    "Waypoint"  x33
data.location  (object, 33/113 records)
data.location.x  (number, 33/113 records)
    numeric range -354.559 .. 285.434 (28 unique)
data.location.y  (number, 33/113 records)
    numeric range -184.94 .. 365.106 (30 unique)
data.location.z  (number, 33/113 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 99 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 1 Dev (18); Unit 3 Dev (16); Unit 4 Dev - Dungeon (12); Unit 4 Dev (11); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 99 of 99 records
- **Intervals:** median 267.47s (p5 0.01s / p95 83908.40s, n=98)
- **`data` key-set variants:** [questEventType, questID, questName] x59; [questEventType, questID, questName, questSuccessOrFailure] x40
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 99/99 records)
    "questActiveEvent"  x59
    "questFinishEvent"  x40
data.questID  (string, 99/99 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 99/99 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 40/99 records)
    "Succeeded"  x40
```

Raw examples: `event_examples.json` -> `questEvent`.

### `WaterChamberEvent` — 54 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (54)
- **Intervals:** median 8.69s (p5 0.26s / p95 98.35s, n=53)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "On"  x32
    "Off"  x22
data.floor  (string, 54/54 records)
    "3"  x32
    "4"  x17
    "2"  x3
    "1"  x2
data.machineNumber  (string, 54/54 records)
    "One"  x46
    "Two"  x8
data.machineType  (string, 54/54 records)
    "Condenser"  x40
    "Evaporator"  x6
    "DualChamber_Condenser"  x3
    "DualChamber_Evaporator"  x3
    "VentSwitch"  x2
data.room  (string, 54/54 records)
    "2"  x19
    "3"  x14
    "4"  x11
    "1"  x10
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationAnswerEvent` — 49 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (29); Unit 4 Dev - Anderson Base (13); Unit 3 Dev (4); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 9.98s (p5 0.18s / p95 92932.53s, n=48)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 49/49 records)
    "submitAnswerEvent"  x49
data.answerSubmitted  (string, 49/49 records)
    20 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 49/49 records)
    "Unit 1 - Freshwater"  x28
    "Unit 4 - Flooding"  x13
    "Unit 3 - Pollution Upstream"  x4
    "Unit 5"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 48 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (21); Unit 2 Prod (Refactor) (8); Unit 3 Dev (5); Unit 4 Dev (4); Unit 1 Dev (3); Unit 4 Dev - Dungeon (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 719.75s (p5 9.17s / p95 103100.85s, n=47)
- **Fields under `data`:**

```text
data.actionType  (string, 48/48 records)
    "DebugMenuStateChanged"  x48
data.isOpened  (bool, 48/48 records)
    false  x48
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 33 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (23); Unit 2 Prod (Refactor) (6); Unit 3 Dev (3); Unit 1 Dev (1)
- **Intervals:** median 1747.56s (p5 119.41s / p95 119886.78s, n=32)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 33/33 records)
    true  x33
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 24 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (24)
- **Intervals:** median 4.56s (p5 0.70s / p95 210.55s, n=23)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 24/24 records)
    "ChangeCanister"  x24
data.canisterType  (string, 24/24 records)
    "Bedrock"  x11
    "Clay"  x10
    "Gravel"  x2
    "Sand"  x1
data.floor  (string, 24/24 records)
    "5"  x20
    "4"  x4
data.machine  (string, 24/24 records)
    "1"  x23
    "2"  x1
data.row  (string, 24/24 records)
    "TopRow"  x14
    "BottomRow"  x10
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 9123.10s (p5 502.67s / p95 130884.08s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 21 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (6); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 126.72s (p5 0.03s / p95 162905.06s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "argumentationSessionClose"  x12
    "argumentationSessionOpen"  x9
data.argumentationDescription  (string, 21/21 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x6
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 21/21 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 4 - Flooding"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `gameWindowUnfocusEvent` — 21 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (5); Unit 1 Dev (3); MainMenu (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1)
- **Intervals:** median 6299.85s (p5 139.21s / p95 134106.16s, n=20)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    false  x21
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 12 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 3 Dev (2)
- **Intervals:** median 8.98s (p5 0.92s / p95 157843.83s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "Close"  x6
    "Open"  x6
data.toolName  (string, 12/12 records, 12 empty-string)
    ""  x12
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9)
- **Intervals:** median 2.54s (p5 0.38s / p95 55192.85s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationToolOpen"  x5
    "argumentationToolClose"  x4
data.argumentationTitle  (string, 9/9 records)
    "Unit 1 - Freshwater"  x7
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 9/9 records)
    "BackingInfoPanel - "  x7
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 1.62s (p5 1.10s / p95 26.59s, n=5)
- **Open findings:** 1 — see sections 5-8
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

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 167267.59s (p5 15539.22s / p95 350033.33s, n=4)
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
- **Intervals:** median 1.67s (p5 1.16s / p95 3.66s, n=3)
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
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/4 records)
    "Tilted In"  x1
data.featureUsed  (string, 4/4 records)
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "RoofStyle"  x1
    "Submit"  x1
data.selectedOption  (string, 3/4 records)
    "Covered"  x1
    "Hot"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1696.82s (p5 1696.82s / p95 1696.82s, n=1)
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
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (78 records)
- `TerasGardenBox` data.actionType: "" (3x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (26x); "WaypointSetEvent" (7x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (33x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (18x)
- `soilMachine` data.canisterType: "Bedrock" (11x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*