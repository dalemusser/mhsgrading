# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b1d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8e69a8420a1e6b56b1d
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b1d.jsonl
- **Records:** 11644 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b1d
- **Time span:** 2026-10-05T16:31:44.630000+00:00 .. 2026-10-16T16:56:53.757000+00:00 (264h 25m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b1d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 11644 records, 11 scenes.
- Findings: **0 FAIL**, **30 WARNING**, 83 INFO, 0 NOT_TESTED, 101 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `Soil Key Puzzle`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3245 | 27.87 | 1 | 9 | 0 | 2026-10-05T16:32:12.689000+00:00 | 2026-10-16T16:56:53.757000+00:00 | 264h 24m |
| PuzzlePieceVisibleEvent | 2780 | 23.87 | 1 | 4 | 0 | 2026-10-07T16:34:24.173000+00:00 | 2026-10-16T16:24:20.816000+00:00 | 215h 49m |
| DialogueEvent | 2344 | 20.13 | 1 | 9 | 1470 | 2026-10-05T16:32:29.052000+00:00 | 2026-10-16T16:56:42.525000+00:00 | 264h 24m |
| PlayerPositionEvent | 2160 | 18.55 | 1 | 9 | 0 | 2026-10-05T16:32:09.166000+00:00 | 2026-10-16T16:56:47.783000+00:00 | 264h 24m |
| argumentationNodeEvent | 415 | 3.56 | 1 | 5 | 0 | 2026-10-05T16:59:24.254000+00:00 | 2026-10-16T16:43:13.812000+00:00 | 263h 43m |
| ObjectInterEvent | 256 | 2.2 | 1 | 9 | 0 | 2026-10-05T16:38:40.196000+00:00 | 2026-10-16T16:56:53.757000+00:00 | 264h 18m |
| TopographicMapEvent | 106 | 0.91 | 1 | 2 | 0 | 2026-10-06T17:03:49.633000+00:00 | 2026-10-14T16:43:02.475000+00:00 | 191h 39m |
| questEvent | 88 | 0.76 | 1 | 9 | 88 | 2026-10-05T16:32:29.028000+00:00 | 2026-10-16T16:53:06.759000+00:00 | 264h 20m |
| Soil Key Puzzle | 36 | 0.31 | 1 | 3 | 0 | 2026-10-09T14:27:53.148000+00:00 | 2026-10-14T16:58:43.695000+00:00 | 122h 30m |
| WaterChamberEvent | 33 | 0.28 | 1 | 1 | 0 | 2026-10-16T16:22:20.118000+00:00 | 2026-10-16T16:34:57.309000+00:00 | 12m 37s |
| DEBUGMenu | 32 | 0.27 | 1 | 9 | 0 | 2026-10-05T16:32:09.152000+00:00 | 2026-10-16T16:17:24.840000+00:00 | 263h 45m |
| argumentationAnswerEvent | 21 | 0.18 | 1 | 5 | 0 | 2026-10-05T17:00:37.889000+00:00 | 2026-10-16T16:43:17.085000+00:00 | 263h 42m |
| argumentationEvent | 21 | 0.18 | 1 | 5 | 0 | 2026-10-05T17:00:20.871000+00:00 | 2026-10-16T16:43:17.126000+00:00 | 263h 42m |
| DaniEvent | 18 | 0.15 | 1 | 1 | 0 | 2026-10-07T16:39:56.028000+00:00 | 2026-10-09T21:10:48.012000+00:00 | 52h 30m |
| gameWindowFocusEvent | 18 | 0.15 | 1 | 3 | 0 | 2026-10-05T16:31:44.630000+00:00 | 2026-10-16T16:17:05.269000+00:00 | 263h 45m |
| gameStartEvent | 14 | 0.12 | 1 | 1 | 0 | 2026-10-05T16:31:44.632000+00:00 | 2026-10-16T16:17:05.269000+00:00 | 263h 45m |
| argumentationToolEvent | 13 | 0.11 | 1 | 4 | 0 | 2026-10-05T17:00:16.341000+00:00 | 2026-10-16T16:41:55.914000+00:00 | 263h 41m |
| soilMachine | 12 | 0.1 | 1 | 1 | 0 | 2026-10-15T16:29:00.577000+00:00 | 2026-10-15T16:42:42.035000+00:00 | 13m 41s |
| TerasGardenBox | 11 | 0.09 | 1 | 1 | 0 | 2026-10-15T20:37:32.990000+00:00 | 2026-10-15T20:38:34.499000+00:00 | 1m 1s |
| SolarStillDesignEvent | 10 | 0.09 | 1 | 1 | 0 | 2026-10-16T16:48:52.308000+00:00 | 2026-10-16T16:50:33.043000+00:00 | 1m 40s |
| EndOfUnit | 5 | 0.04 | 1 | 5 | 0 | 2026-10-06T16:58:07.724000+00:00 | 2026-10-16T16:56:53.737000+00:00 | 239h 58m |
| gameWindowUnfocusEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-08T16:29:18.583000+00:00 | 2026-10-14T16:55:26.956000+00:00 | 144h 26m |
| chatEvent | 2 | 0.02 | 1 | 2 | 0 | 2026-10-16T16:17:24.623000+00:00 | 2026-10-16T16:35:53.096000+00:00 | 18m 28s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 188574.603s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.691s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 15.135s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.072s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 2.126s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.849s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 36.675s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.824s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 79013.108s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 23654.628s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 103831.112s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 18 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Collect 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Soil Key Puzzle` `data.currentSoilType` — baseline categorical value(s) not seen this build. 
  - Observed: BEDROCK 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.2x vs baseline. 
  - Observed: 21 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,2,II; A,D,2,II; A,D,B,2,II; A,D,C,2,II; B,2,II; C,2,II; C,3,4,II; C,3,II; C,D,3,II; D,2,II; D,A,2,II; D,B,A,2,II 
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
  - Observed: Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 4 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 9 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[165] _id=6ac3d348de269131f9adf1dd ts=2026-10-05T16:41:43.8320000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[227] _id=6ac3d465de269131f9ae0b46 ts=2026-10-05T16:46:28.7610000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[249] _id=6ac3d49ede269131f9ae12fd ts=2026-10-05T16:47:26.0380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[0] _id=6ac3d0f1de269131f9adbfd0 ts=2026-10-05T16:31:44.6320000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[554] _id=6ac526dede269131f9b56945 ts=2026-10-06T16:50:37.8960000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[758] _id=6ac528f2de269131f9b5d44b ts=2026-10-06T16:59:30.2690000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[9] _id=6ac3d0f1de269131f9adbfc7 ts=2026-10-05T16:31:44.6300000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[553] _id=6ac526dede269131f9b56941 ts=2026-10-06T16:50:37.8950000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[757] _id=6ac528f2de269131f9b5d445 ts=2026-10-06T16:59:30.2680000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 4 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 4} 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[2718] _id=6ac7c4dfde269131f9c42945 ts=2026-10-08T16:29:18.5830000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[4895] _id=6ac95a76de269131f9cb188c ts=2026-10-09T21:19:49.6950000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[7861] _id=6acfb2e5de269131f9d5f231 ts=2026-10-14T16:50:43.8750000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 3244 | 0.0 | 1.691 | 293.428 | 20.319 | 326228.25 | 0.2 | 41 | 11 |
| PuzzlePieceVisibleEvent | 2779 | 0.0 | 0.072 | 279.596 | 2.454 | 329676.7 | 0.21 | 1141 | 8 |
| DialogueEvent | 2343 | 0.0 | 3.825 | 406.254 | 30.942 | 326179.548 | 0.15 | 667 | 12 |
| PlayerPositionEvent | 2146 | 9.772 | 10.001 | 253.133 | 10.12 | 85590.772 | 0.24 | 0 | 7 |
| argumentationNodeEvent | 414 | 0.004 | 0.691 | 2293.308 | 9.83 | 328088.672 | 0.03 | 31 | 6 |
| ObjectInterEvent | 255 | 0.0 | 15.135 | 3731.347 | 486.344 | 326940.303 | 0.02 | 5 | 12 |
| TopographicMapEvent | 105 | 0.017 | 4.849 | 6570.979 | 19559.592 | 327114.479 | 0.01 | 2 | 9 |
| questEvent | 87 | 0.0 | 209.09 | 10938.365 | 84139.165 | 326328.752 | 0.01 | 17 | 19 |
| Soil Key Puzzle | 35 | 0.176 | 2.126 | 12601.444 | 26025.894 | 354194.225 | 0.0 | 0 | 2 |
| WaterChamberEvent | 32 | 1.845 | 12.456 | 23.662 | 59.099 | 130.466 | 2.54 | 0 | 0 |
| DEBUGMenu | 31 | 8.331 | 753.079 | 30629.538 | 86855.877 | 327494.364 | 0.0 | 0 | 17 |
| argumentationAnswerEvent | 20 | 3.944 | 36.675 | 47467.96 | 278838.514 | 328175.683 | 0.0 | 0 | 6 |
| argumentationEvent | 20 | 0.07 | 50.785 | 47468.813 | 278797.334 | 328090.486 | 0.0 | 0 | 6 |
| DaniEvent | 17 | 0.006 | 2.592 | 11120.705 | 88373.064 | 103057.233 | 0.01 | 2 | 3 |
| gameWindowFocusEvent | 17 | 4.425 | 23654.628 | 55854.155 | 135526.119 | 327497.534 | 0.0 | 0 | 12 |
| gameStartEvent | 13 | 532.373 | 79013.108 | 73040.049 | 183526.606 | 327516.62 | 0.0 | 0 | 12 |
| argumentationToolEvent | 12 | 0.775 | 3.824 | 79108.298 | 343478.588 | 362253.398 | 0.0 | 0 | 3 |
| soilMachine | 11 | 1.314 | 58.907 | 74.678 | 211.07 | 304.912 | 0.8 | 0 | 0 |
| TerasGardenBox | 10 | 0.904 | 2.781 | 6.151 | 17.729 | 18.157 | 9.75 | 0 | 0 |
| SolarStillDesignEvent | 9 | 0.707 | 2.919 | 11.193 | 49.145 | 77.966 | 5.36 | 0 | 0 |
| EndOfUnit | 4 | 72564.209 | 188574.603 | 215981.503 | 393522.463 | 414212.598 | 0.0 | 0 | 4 |
| gameWindowUnfocusEvent | 3 | 283.081 | 103831.112 | 173322.791 | 384651.873 | 415854.18 | 0.0 | 0 | 2 |
| chatEvent | 1 | 1108.473 | 1108.473 | 1108.473 | 1108.473 | 1108.473 | 0.05 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[858] _id=6ac67431de269131f9bc8de2 ts=2026-10-07T16:32:47.8480000Z == 6ab9a8e69a8420a1e6b56b1d.jsonl[859] _id=6ac67431de269131f9bc8de3 ts=2026-10-07T16:32:47.8480000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 37 group(s), 57 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[3577] _id=6ac8faa7de269131f9c8cbef ts=2026-10-09T14:31:03.1650000Z == 6ab9a8e69a8420a1e6b56b1d.jsonl[3579] _id=6ac8faa7de269131f9c8cbf3 ts=2026-10-09T14:31:03.1650000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[3580] _id=6ac8faa9de269131f9c8cbfb ts=2026-10-09T14:31:03.3800000Z == 6ab9a8e69a8420a1e6b56b1d.jsonl[3581] _id=6ac8faa9de269131f9c8cbfc ts=2026-10-09T14:31:03.3800000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[3597] _id=6ac8fab5de269131f9c8cc28 ts=2026-10-09T14:31:16.4950000Z == 6ab9a8e69a8420a1e6b56b1d.jsonl[3599] _id=6ac8fab5de269131f9c8cc2a ts=2026-10-09T14:31:16.4950000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[11397] _id=6ad2546cde269131f9e60e95 ts=2026-10-16T16:44:27.5190000Z == 6ab9a8e69a8420a1e6b56b1d.jsonl[11398] _id=6ad2546cde269131f9e60e96 ts=2026-10-16T16:44:27.5190000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[112] _id=6ac3d291de269131f9ade45d ts=2026-10-05T16:38:40.1960000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[110] _id=6ac3d291de269131f9ade461 ts=2026-10-05T16:38:40.2020000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `204ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[2646] _id=6ac67abcde269131f9bd78e9 ts=2026-10-07T17:00:43.3400000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[2647] _id=6ac67abcde269131f9bd78f2 ts=2026-10-07T17:00:43.5440000Z`; `248ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[5232] _id=6ac95d4ede269131f9cb1a45 ts=2026-10-09T21:31:58.1330000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[5221] _id=6ac95d4ede269131f9cb1a47 ts=2026-10-09T21:31:58.3810000Z`; `753ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[5221] _id=6ac95d4ede269131f9cb1a47 ts=2026-10-09T21:31:58.3810000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[5233] _id=6ac95d4fde269131f9cb1a49 ts=2026-10-09T21:31:59.1340000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `70ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[6185] _id=6ace60c5de269131f9cfbf32 ts=2026-10-13T16:48:05.1360000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[6189] _id=6ace60c5de269131f9cfbf3b ts=2026-10-13T16:48:05.2060000Z`; `100ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[9669] _id=6ad10748de269131f9de3ecc ts=2026-10-15T17:03:03.1780000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[9759] _id=6ad10748de269131f9de3ed0 ts=2026-10-15T17:03:03.2780000Z`; `72ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[10033] _id=6ad13831de269131f9e1287b ts=2026-10-15T20:31:44.8050000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[10005] _id=6ad13831de269131f9e1287f ts=2026-10-15T20:31:44.8770000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 26 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `725ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[414] _id=6ac3d76dde269131f9ae56d2 ts=2026-10-05T16:59:24.2540000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[417] _id=6ac3d76dde269131f9ae56e7 ts=2026-10-05T16:59:24.9790000Z`; `22ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[469] _id=6ac3d7abde269131f9ae5d6f ts=2026-10-05T17:00:26.4160000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[472] _id=6ac3d7abde269131f9ae5d75 ts=2026-10-05T17:00:26.4380000Z`; `64ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[459] _id=6ac3d7b2de269131f9ae5e05 ts=2026-10-05T17:00:33.0850000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[466] _id=6ac3d7b2de269131f9ae5e0b ts=2026-10-05T17:00:33.1490000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[11535] _id=6ad25620de269131f9e62dfd ts=2026-10-16T16:51:43.9470000Z ~ 6ab9a8e69a8420a1e6b56b1d.jsonl[11536] _id=6ad25620de269131f9e62e03 ts=2026-10-16T16:51:43.9540000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 90h 58m 
  - Evidence: 90h 58m: 6ab9a8e69a8420a1e6b56b1d.jsonl[4988] _id=6ac95a86de269131f9cb1890 ts=2026-10-09T21:20:06.3030000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5481] _id=6ace59cdde269131f9cf58dd ts=2026-10-13T16:18:20.6670000Z; 24h 18m: 6ab9a8e69a8420a1e6b56b1d.jsonl[10] _id=6ac3d10ade269131f9adc32e ts=2026-10-05T16:32:09.1520000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[555] _id=6ac526eede269131f9b56b55 ts=2026-10-06T16:50:54.5470000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b1d.jsonl[855] _id=6ac6742dde269131f9bc8d8a ts=2026-10-07T16:32:44.9810000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2715] _id=6ac7c4d7de269131f9c42905 ts=2026-10-08T16:29:11.3400000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 28h 37m 
  - Evidence: 28h 37m: 6ab9a8e69a8420a1e6b56b1d.jsonl[2803] _id=6ac7c5bade269131f9c43db0 ts=2026-10-08T16:32:57.7960000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4561] _id=6ac9584bde269131f9cb1530 ts=2026-10-09T21:10:35.0290000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b1d.jsonl[2649] _id=6ac67adbde269131f9bd7c6b ts=2026-10-07T17:01:14.1960000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2804] _id=6ac7c5b8de269131f9c43d85 ts=2026-10-08T16:32:56.2180000Z; 16m 51s: 6ab9a8e69a8420a1e6b56b1d.jsonl[1940] _id=6ac676e5de269131f9bd080b ts=2026-10-07T16:44:20.9160000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2654] _id=6ac67ad9de269131f9bd7c4a ts=2026-10-07T17:01:12.8900000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.006s..0.007s shown 
  - Evidence: 6ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[4567] _id=6ac95857de269131f9cb1538 ts=2026-10-09T21:10:46.5340000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4568] _id=6ac95857de269131f9cb153a ts=2026-10-09T21:10:46.5400000Z; 7ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[4565] _id=6ac95852de269131f9cb1534 ts=2026-10-09T21:10:42.0950000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4566] _id=6ac95852de269131f9cb1536 ts=2026-10-09T21:10:42.1020000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 90h 36m 
  - Evidence: 90h 36m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5480] _id=6ac95fd6de269131f9cb1c54 ts=2026-10-09T21:42:46.1060000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5484] _id=6ace59f9de269131f9cf594d ts=2026-10-13T16:19:05.6540000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b1d.jsonl[538] _id=6ac3d860de269131f9ae6e3f ts=2026-10-05T17:03:27.1640000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[566] _id=6ac52715de269131f9b57113 ts=2026-10-06T16:51:32.6950000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b1d.jsonl[846] _id=6ac52a0ade269131f9b60835 ts=2026-10-06T17:04:09.9410000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[866] _id=6ac6744bde269131f9bc8ffa ts=2026-10-07T16:33:14.0970000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 667 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[10009] _id=6ad13814de269131f9e1281b ts=2026-10-15T20:31:15.7010000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[10010] _id=6ad13814de269131f9e1281c ts=2026-10-15T20:31:15.7010000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[10023] _id=6ad13820de269131f9e12852 ts=2026-10-15T20:31:28.4720000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[10024] _id=6ad13820de269131f9e12853 ts=2026-10-15T20:31:28.4720000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[11319] _id=6ad253fdde269131f9e60917 ts=2026-10-16T16:42:36.7370000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[11320] _id=6ad253fdde269131f9e60918 ts=2026-10-16T16:42:36.7370000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 115h 3m 
  - Evidence: 115h 3m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5475] _id=6ac95fd6de269131f9cb1c52 ts=2026-10-09T21:42:46.0890000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[7830] _id=6acfb1dbde269131f9d5cd2a ts=2026-10-14T16:46:18.6870000Z; 76h 44m: 6ab9a8e69a8420a1e6b56b1d.jsonl[753] _id=6ac528a0de269131f9b5c296 ts=2026-10-06T16:58:07.7240000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5475] _id=6ac95fd6de269131f9cb1c52 ts=2026-10-09T21:42:46.0890000Z; 28h 1m: 6ab9a8e69a8420a1e6b56b1d.jsonl[7830] _id=6acfb1dbde269131f9d5cd2a ts=2026-10-14T16:46:18.6870000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[10371] _id=6ad13be1de269131f9e13716 ts=2026-10-15T20:47:29.5280000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 90h 37m 
  - Evidence: 90h 37m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5456] _id=6ac95f9dde269131f9cb1c28 ts=2026-10-09T21:41:49.2510000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5487] _id=6ace59f2de269131f9cf5931 ts=2026-10-13T16:18:57.5010000Z; 23h 46m: 6ab9a8e69a8420a1e6b56b1d.jsonl[550] _id=6ac3d888de269131f9ae717d ts=2026-10-05T17:04:07.3580000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[559] _id=6ac526fbde269131f9b56d2e ts=2026-10-06T16:51:07.2220000Z; 23h 29m: 6ab9a8e69a8420a1e6b56b1d.jsonl[768] _id=6ac529e0de269131f9b60081 ts=2026-10-06T17:03:28.0990000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[857] _id=6ac67431de269131f9bc8de1 ts=2026-10-07T16:32:47.8460000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 41 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[4531] _id=6ac95816de269131f9cb14fb ts=2026-10-09T21:09:41.6550000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4547] _id=6ac95816de269131f9cb14fc ts=2026-10-09T21:09:41.6550000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[4931] _id=6ac95a1ade269131f9cb1806 ts=2026-10-09T21:18:18.0850000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4932] _id=6ac95a1ade269131f9cb1807 ts=2026-10-09T21:18:18.0850000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[858] _id=6ac67431de269131f9bc8de2 ts=2026-10-07T16:32:47.8480000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[859] _id=6ac67431de269131f9bc8de3 ts=2026-10-07T16:32:47.8480000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 90h 49m 
  - Evidence: 90h 49m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5349] _id=6ac95e11de269131f9cb1b28 ts=2026-10-09T21:35:12.9200000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5584] _id=6ace5b2dde269131f9cf634b ts=2026-10-13T16:24:13.2230000Z; 45h 40m: 6ab9a8e69a8420a1e6b56b1d.jsonl[2416] _id=6ac67789de269131f9bd256d ts=2026-10-07T16:47:04.8700000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[3445] _id=6ac8f9e9de269131f9c8ca12 ts=2026-10-09T14:27:53.1530000Z; 23h 52m: 6ab9a8e69a8420a1e6b56b1d.jsonl[407] _id=6ac3d746de269131f9ae5249 ts=2026-10-05T16:58:45.2330000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2] _id=6ac52714de269131f9b5710f ts=2026-10-06T16:51:32.6740000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[9402] _id=6ad10513de269131f9de03bc ts=2026-10-15T16:53:38.1310000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9404] _id=6ad10513de269131f9de03bd ts=2026-10-15T16:53:38.1310000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[9463] _id=6ad10566de269131f9de0de4 ts=2026-10-15T16:55:01.6390000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9464] _id=6ad10566de269131f9de0de5 ts=2026-10-15T16:55:01.6390000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[9873] _id=6ad13704de269131f9e12578 ts=2026-10-15T20:26:44.5790000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9874] _id=6ad13704de269131f9e12579 ts=2026-10-15T20:26:44.5790000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 23h 46m 
  - Evidence: 23h 46m: 6ab9a8e69a8420a1e6b56b1d.jsonl[551] _id=6ac3d898de269131f9ae7293 ts=2026-10-05T17:04:23.7910000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[557] _id=6ac526f1de269131f9b56bad ts=2026-10-06T16:50:54.5630000Z; 23h 28m: 6ab9a8e69a8420a1e6b56b1d.jsonl[848] _id=6ac52a0dde269131f9b608d9 ts=2026-10-06T17:04:13.1840000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[856] _id=6ac67431de269131f9bc8de0 ts=2026-10-07T16:32:45.0060000Z; 23h 25m: 6ab9a8e69a8420a1e6b56b1d.jsonl[2713] _id=6ac67b89de269131f9bd8ecd ts=2026-10-07T17:04:07.9700000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2722] _id=6ac7c4e9de269131f9c429f1 ts=2026-10-08T16:29:24.4000000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 91h 34m 
  - Evidence: 91h 34m: 6ab9a8e69a8420a1e6b56b1d.jsonl[4976] _id=6ac95a4dde269131f9cb1863 ts=2026-10-09T21:19:08.5670000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[6482] _id=6ace621ade269131f9cfd89f ts=2026-10-13T16:53:45.2670000Z; 24h 2m: 6ab9a8e69a8420a1e6b56b1d.jsonl[2430] _id=6ac6778cde269131f9bd25d0 ts=2026-10-07T16:47:04.9560000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[3127] _id=6ac7c9a3de269131f9c4abc7 ts=2026-10-08T16:49:38.5950000Z; 23h 42m: 6ab9a8e69a8420a1e6b56b1d.jsonl[8373] _id=6acfb585de269131f9d63719 ts=2026-10-14T17:01:54.9020000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9120] _id=6ad102cdde269131f9ddcae3 ts=2026-10-15T16:43:55.1920000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1141 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[1007] _id=6ac67512de269131f9bcacf0 ts=2026-10-07T16:36:33.1840000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[1013] _id=6ac67512de269131f9bcacf6 ts=2026-10-07T16:36:33.1840000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[1013] _id=6ac67512de269131f9bcacf6 ts=2026-10-07T16:36:33.1840000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[1014] _id=6ac67513de269131f9bcacfb ts=2026-10-07T16:36:33.1840000Z; 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[10377] _id=6ad24eccde269131f9e5ba9c ts=2026-10-16T16:20:27.5160000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[10378] _id=6ad24eccde269131f9e5baa0 ts=2026-10-16T16:20:27.5160000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 98h 23m 
  - Evidence: 98h 23m: 6ab9a8e69a8420a1e6b56b1d.jsonl[3526] _id=6ac8fa44de269131f9c8cafb ts=2026-10-09T14:29:24.3690000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[6581] _id=6ace61d6de269131f9cfd285 ts=2026-10-13T16:52:38.5940000Z; 24h 5m: 6ab9a8e69a8420a1e6b56b1d.jsonl[6605] _id=6ace61f2de269131f9cfd464 ts=2026-10-13T16:53:06.2810000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[7910] _id=6acfb4a5de269131f9d618ef ts=2026-10-14T16:58:12.5370000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 90h 51m 
  - Evidence: 90h 51m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5222] _id=6ac95d55de269131f9cb1a4f ts=2026-10-09T21:32:04.5260000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5578] _id=6ace5b1fde269131f9cf62e1 ts=2026-10-13T16:23:59.0050000Z; 23h 55m: 6ab9a8e69a8420a1e6b56b1d.jsonl[6133] _id=6ace5f33de269131f9cfa338 ts=2026-10-13T16:41:22.8850000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[7577] _id=6acfafb8de269131f9d59b80 ts=2026-10-14T16:37:11.5600000Z; 23h 30m: 6ab9a8e69a8420a1e6b56b1d.jsonl[847] _id=6ac52a0ade269131f9b6083d ts=2026-10-06T17:04:10.0240000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[902] _id=6ac674bcde269131f9bc9c73 ts=2026-10-07T16:35:07.7180000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.017s..0.023s shown 
  - Evidence: 17ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[2596] _id=6ac67a57de269131f9bd6ccc ts=2026-10-07T16:59:02.4350000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2603] _id=6ac67a57de269131f9bd6cd4 ts=2026-10-07T16:59:02.4520000Z; 23ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[2603] _id=6ac67a57de269131f9bd6cd4 ts=2026-10-07T16:59:02.4520000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[2607] _id=6ac67a57de269131f9bd6cd8 ts=2026-10-07T16:59:02.4750000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 91h 9m 
  - Evidence: 91h 9m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5399] _id=6ac95ed6de269131f9cb1bb9 ts=2026-10-09T21:38:29.4360000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[6449] _id=6ace60c5de269131f9cfbf2e ts=2026-10-13T16:48:05.1190000Z; 76h 44m: 6ab9a8e69a8420a1e6b56b1d.jsonl[649] _id=6ac527c3de269131f9b58ddf ts=2026-10-06T16:54:27.6150000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5399] _id=6ac95ed6de269131f9cb1bb9 ts=2026-10-09T21:38:29.4360000Z; 48h 10m: 6ab9a8e69a8420a1e6b56b1d.jsonl[6449] _id=6ace60c5de269131f9cfbf2e ts=2026-10-13T16:48:05.1190000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9551] _id=6ad10649de269131f9de2550 ts=2026-10-15T16:58:48.6430000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 91h 8m 
  - Evidence: 91h 8m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5400] _id=6ac95ed6de269131f9cb1bba ts=2026-10-09T21:38:29.4570000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[6402] _id=6ace6070de269131f9cfb937 ts=2026-10-13T16:46:39.9430000Z; 76h 43m: 6ab9a8e69a8420a1e6b56b1d.jsonl[652] _id=6ac527c3de269131f9b58de7 ts=2026-10-06T16:54:27.6450000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5347] _id=6ac95eafde269131f9cb1b82 ts=2026-10-09T21:37:50.6030000Z; 48h 9m: 6ab9a8e69a8420a1e6b56b1d.jsonl[6189] _id=6ace60c5de269131f9cfbf3b ts=2026-10-13T16:48:05.2060000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9506] _id=6ad105e6de269131f9de1bec ts=2026-10-15T16:57:10.0930000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 91h 8m 
  - Evidence: 91h 8m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5397] _id=6ac95ed4de269131f9cb1bb5 ts=2026-10-09T21:38:27.8180000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[6400] _id=6ace606cde269131f9cfb8dc ts=2026-10-13T16:46:36.4900000Z; 76h 43m: 6ab9a8e69a8420a1e6b56b1d.jsonl[644] _id=6ac527bede269131f9b58cb3 ts=2026-10-06T16:54:21.7370000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5344] _id=6ac95ea9de269131f9cb1b7c ts=2026-10-09T21:37:44.9740000Z; 48h 9m: 6ab9a8e69a8420a1e6b56b1d.jsonl[6461] _id=6ace60c3de269131f9cfbf18 ts=2026-10-13T16:48:03.0840000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[9511] _id=6ad105ecde269131f9de1c63 ts=2026-10-15T16:57:15.9010000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 31 interval(s) ≤ 0.004s..0.008s shown 
  - Evidence: 4ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[497] _id=6ac3d7edde269131f9ae63c9 ts=2026-10-05T17:01:32.5230000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[498] _id=6ac3d7edde269131f9ae63cb ts=2026-10-05T17:01:32.5270000Z; 5ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[11310] _id=6ad253e9de269131f9e607ed ts=2026-10-16T16:42:17.4230000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[11311] _id=6ad253e9de269131f9e607ef ts=2026-10-16T16:42:17.4280000Z; 8ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[424] _id=6ac3d775de269131f9ae57af ts=2026-10-05T16:59:32.4010000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[418] _id=6ac3d775de269131f9ae57b5 ts=2026-10-05T16:59:32.4090000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 100h 37m 
  - Evidence: 100h 37m: 6ab9a8e69a8420a1e6b56b1d.jsonl[467] _id=6ac3d7a5de269131f9ae5ce9 ts=2026-10-05T17:00:20.8000000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5376] _id=6ac95eb2de269131f9cb1b87 ts=2026-10-09T21:37:54.1980000Z; 91h 8m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5378] _id=6ac95ebfde269131f9cb1b8d ts=2026-10-09T21:38:06.7610000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[6407] _id=6ace6074de269131f9cfb9a7 ts=2026-10-13T16:46:44.1410000Z; 71h 54m: 6ab9a8e69a8420a1e6b56b1d.jsonl[6415] _id=6ace6085de269131f9cfbadd ts=2026-10-13T16:47:01.1810000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[11290] _id=6ad253d1de269131f9e60690 ts=2026-10-16T16:41:52.7260000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 18m 28s 
  - Evidence: 18m 28s: 6ab9a8e69a8420a1e6b56b1d.jsonl[10391] _id=6ad24e14de269131f9e5ab96 ts=2026-10-16T16:17:24.6230000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[11146] _id=6ad25269de269131f9e5f31e ts=2026-10-16T16:35:53.0960000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 90h 58m 
  - Evidence: 90h 58m: 6ab9a8e69a8420a1e6b56b1d.jsonl[4894] _id=6ac95a70de269131f9cb188a ts=2026-10-09T21:19:44.3830000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5483] _id=6ace59cdde269131f9cf58e0 ts=2026-10-13T16:18:21.0030000Z; 24h 18m: 6ab9a8e69a8420a1e6b56b1d.jsonl[0] _id=6ac3d0f1de269131f9adbfd0 ts=2026-10-05T16:31:44.6320000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[554] _id=6ac526dede269131f9b56945 ts=2026-10-06T16:50:37.8960000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5483] _id=6ace59cdde269131f9cf58e0 ts=2026-10-13T16:18:21.0030000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[7076] _id=6acfab77de269131f9d54d44 ts=2026-10-14T16:19:02.0450000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 90h 58m 
  - Evidence: 90h 58m: 6ab9a8e69a8420a1e6b56b1d.jsonl[4896] _id=6ac95a84de269131f9cb188e ts=2026-10-09T21:20:03.4690000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5482] _id=6ace59cdde269131f9cf58df ts=2026-10-13T16:18:21.0030000Z; 24h 18m: 6ab9a8e69a8420a1e6b56b1d.jsonl[9] _id=6ac3d0f1de269131f9adbfc7 ts=2026-10-05T16:31:44.6300000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[553] _id=6ac526dede269131f9b56941 ts=2026-10-06T16:50:37.8950000Z; 24h 0m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5482] _id=6ace59cdde269131f9cf58df ts=2026-10-13T16:18:21.0030000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[7075] _id=6acfab77de269131f9d54d43 ts=2026-10-14T16:19:02.0450000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 115h 30m 
  - Evidence: 115h 30m: 6ab9a8e69a8420a1e6b56b1d.jsonl[4895] _id=6ac95a76de269131f9cb188c ts=2026-10-09T21:19:49.6950000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[7861] _id=6acfb2e5de269131f9d5f231 ts=2026-10-14T16:50:43.8750000Z; 28h 50m: 6ab9a8e69a8420a1e6b56b1d.jsonl[2718] _id=6ac7c4dfde269131f9c42945 ts=2026-10-08T16:29:18.5830000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4895] _id=6ac95a76de269131f9cb188c ts=2026-10-09T21:19:49.6950000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 90h 38m 
  - Evidence: 90h 38m: 6ab9a8e69a8420a1e6b56b1d.jsonl[5477] _id=6ac95fd0de269131f9cb1c4c ts=2026-10-09T21:42:39.6470000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[5520] _id=6ace5a88de269131f9cf5d7f ts=2026-10-13T16:21:28.3990000Z; 23h 48m: 6ab9a8e69a8420a1e6b56b1d.jsonl[519] _id=6ac3d836de269131f9ae6afb ts=2026-10-05T17:02:45.7160000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[556] _id=6ac526f1de269131f9b56bb1 ts=2026-10-06T16:50:56.4240000Z; 23h 31m: 6ab9a8e69a8420a1e6b56b1d.jsonl[787] _id=6ac52958de269131f9b5e6e0 ts=2026-10-06T17:01:11.7520000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[860] _id=6ac67431de269131f9bc8de4 ts=2026-10-07T16:32:47.8820000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[11397] _id=6ad2546cde269131f9e60e95 ts=2026-10-16T16:44:27.5190000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[11398] _id=6ad2546cde269131f9e60e96 ts=2026-10-16T16:44:27.5190000Z; 2ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[405] _id=6ac3d746de269131f9ae5257 ts=2026-10-05T16:58:45.2610000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[406] _id=6ac3d746de269131f9ae5259 ts=2026-10-05T16:58:45.2630000Z; 4ms: 6ab9a8e69a8420a1e6b56b1d.jsonl[4333] _id=6ac955f0de269131f9cb1326 ts=2026-10-09T21:00:31.2680000Z -> 6ab9a8e69a8420a1e6b56b1d.jsonl[4334] _id=6ac955f0de269131f9cb1327 ts=2026-10-09T21:00:31.2720000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[390] _id=6ac3d724de269131f9ae4f28 ts=2026-10-05T16:58:11.3280000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[435] _id=6ac3d826de269131f9ae69a7 ts=2026-10-05T17:02:29.3780000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[660] _id=6ac527e3de269131f9b59579 ts=2026-10-06T16:54:58.6850000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[6189] _id=6ace60c5de269131f9cfbf3b ts=2026-10-13T16:48:05.2060000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[9759] _id=6ad10748de269131f9de3ed0 ts=2026-10-15T17:03:03.2780000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[10005] _id=6ad13831de269131f9e1287f ts=2026-10-15T20:31:44.8770000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[472] _id=6ac3d7abde269131f9ae5d75 ts=2026-10-05T17:00:26.4380000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[466] _id=6ac3d7b2de269131f9ae5e0b ts=2026-10-05T17:00:33.1490000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[10391] _id=6ad24e14de269131f9e5ab96 ts=2026-10-16T16:17:24.6230000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[11146] _id=6ad25269de269131f9e5f31e ts=2026-10-16T16:35:53.0960000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 31 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[3673] _id=6ac8fb15de269131f9c8cd4f ts=2026-10-09T14:32:49.2720000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[3674] _id=6ac8fb15de269131f9c8cd51 ts=2026-10-09T14:32:49.2720000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[3676] _id=6ac8fb15de269131f9c8cd53 ts=2026-10-09T14:32:49.2720000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 53 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[3579] _id=6ac8faa7de269131f9c8cbf3 ts=2026-10-09T14:31:03.1650000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[3599] _id=6ac8fab5de269131f9c8cc2a ts=2026-10-09T14:31:16.4950000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[3606] _id=6ac8fab6de269131f9c8cc32 ts=2026-10-09T14:31:16.5570000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 6 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[5377] _id=6ac95ebdde269131f9cb1b8b ts=2026-10-09T21:38:04.6000000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[5378] _id=6ac95ebfde269131f9cb1b8d ts=2026-10-09T21:38:06.7610000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[6408] _id=6ace6076de269131f9cfb9be ts=2026-10-13T16:46:45.6950000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 441 start, 433 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 12 unmatched 'BecameVisible' (totals: 813 open, 801 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'argumentationToolOpen' (totals: 12 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'questActiveEvent' (totals: 54 start, 34 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 225 of 11643 adjacent _id pairs reverse in client time; worst 119.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b1d.jsonl[937] _id=6ac67509de269131f9bcaac0 ts=2026-10-07T16:36:23.9780000Z`; `6ab9a8e69a8420a1e6b56b1d.jsonl[935] _id=6ac67509de269131f9bcaaf8 ts=2026-10-07T16:34:24.1730000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.83s, min -121.78s, max -0.26s over 11644 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8e69a8420a1e6b56b1d\coverage.yaml

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

### `InputEvent` — 3245 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1295); Unit 3 Dev (656); Unit 4 Dev - Dungeon (345); Unit 3 Dungeon Dev (268); Unit 5 Dev - Dungeon (188); Unit 4 Dev - Anderson Base (162); Unit 1 Dev (133); Unit 4 Dev (117); Unit 5 Dev (81)
- **Intervals:** median 1.69s (p5 0.18s / p95 20.32s, n=3244)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3245/3245 records)
    "pressed"  x3245
data.actionType  (string, 3245/3245 records)
    "Move"  x2586
    "Interact"  x432
    "Ascend"  x124
    "Jump"  x44
    "Hoverboard"  x34
    "Sprint"  x14
    "Map"  x7
    "Descend"  x2
    "Pause"  x2
data.key  (string, 3245/3245 records, 10 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3245/3245 records)
    "Player"  x2031
    "Drone"  x1214
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 2780 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1712); Unit 4 Dev (454); Unit 5 Dev - Dungeon (334); Unit 3 Dungeon Dev (280)
- **Intervals:** median 0.07s (p5 0.00s / p95 2.45s, n=2779)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2780/2780 records)
    "BecameVisible"  x813
    "BecameInvisible"  x801
    "BecameCameraCentered"  x583
    "BecameCameraUncentered"  x583
data.pieceId  (string, 2780/2780 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2780/2780 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `DialogueEvent` — 2344 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (712); Unit 3 Dev (334); Unit 4 Dev (272); Unit 1 Dev (250); Unit 5 Dev (221); Unit 3 Dungeon Dev (198); Unit 4 Dev - Anderson Base (173); Unit 4 Dev - Dungeon (111); Unit 5 Dev - Dungeon (73)
- **eventKey:** present on 1470 of 2344 records
- **Intervals:** median 3.83s (p5 0.00s / p95 30.94s, n=2343)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1470; [conversationId, dialogueEventType] x874
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2344/2344 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2344/2344 records)
    "DialogueNodeEvent"  x1470
    "DialogueStartEvent"  x441
    "DialogueFinishEvent"  x433
data.nodeId  (number, 1470/2344 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2160 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (782); Unit 3 Dev (266); Unit 1 Dev (237); Unit 4 Dev (197); Unit 4 Dev - Dungeon (164); Unit 3 Dungeon Dev (161); Unit 4 Dev - Anderson Base (128); Unit 5 Dev (115); Unit 5 Dev - Dungeon (110)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.12s, n=2146)
- **Fields under `data`:**

```text
data.position  (object, 2160/2160 records)
data.position.x  (number, 2160/2160 records)
    numeric range -680.42 .. 1555.4 (796 unique)
data.position.y  (number, 2160/2160 records)
    numeric range -114.162 .. 222.252 (566 unique)
data.position.z  (number, 2160/2160 records)
    numeric range -1148.04 .. 2222.7 (796 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 415 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (214); Unit 1 Dev (83); Unit 5 Dev (56); Unit 3 Dev (43); Unit 2 Prod (Refactor) (19)
- **Intervals:** median 0.69s (p5 0.04s / p95 9.83s, n=414)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 415/415 records)
    "argumentationNodeHoverEnd"  x184
    "argumentationNodeHoverStart"  x182
    "argumentationNodeAdd"  x39
    "argumentationNodeRemove"  x10
data.argumentationTitle  (string, 415/415 records)
    "Unit 4 - Flooding"  x214
    "Unit 5"  x56
    "Unit 3 - Pollution Upstream"  x43
    "Unit 1 - Freshwater"  x42
    "Unit 1 - Argumentation Tutorial"  x41
    "Unit 2 – Watershed"  x19
data.nodeName  (string, 415/415 records)
    "A"  x62
    "B"  x52
    "II"  x52
    "D"  x45
    "I"  x44
    "1"  x43
    "C"  x41
    "2"  x34
    "3"  x21
    "4"  x16
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 256 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (80); Unit 2 Prod (Refactor) (50); Unit 3 Dungeon Dev (45); Unit 4 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 5 Dev - Dungeon (16); Unit 3 Dev (12); Unit 1 Dev (11); Unit 5 Dev (6)
- **Intervals:** median 15.13s (p5 2.17s / p95 486.34s, n=255)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 256/256 records)
    41 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 256/256 records)
    107 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 106 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (59); Unit 3 Dev (47)
- **Intervals:** median 4.85s (p5 0.66s / p95 19559.59s, n=105)
- **`data` key-set variants:** [actionType, featureUsed] x58; [actionType, featureUsed, location] x48
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 106/106 records)
    "WaypointMoveEvent"  x35
    "MapCloseEvent"  x29
    "MapOpenEvent"  x29
    "WaypointSetEvent"  x8
    "WaypointResetEvent"  x5
data.featureUsed  (string, 106/106 records)
    "Map"  x58
    "Waypoint"  x48
data.location  (object, 48/106 records)
data.location.x  (number, 48/106 records)
    numeric range -343.312 .. 178.28 (32 unique)
data.location.y  (number, 48/106 records)
    numeric range -316.759 .. 231.545 (38 unique)
data.location.z  (number, 48/106 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 88 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 1 Dev (17); Unit 4 Dev - Dungeon (10); Unit 3 Dev (9); Unit 4 Dev (8); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 88 of 88 records
- **Intervals:** median 209.09s (p5 0.00s / p95 84139.16s, n=87)
- **`data` key-set variants:** [questEventType, questID, questName] x54; [questEventType, questID, questName, questSuccessOrFailure] x34
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 88/88 records)
    "questActiveEvent"  x54
    "questFinishEvent"  x34
data.questID  (string, 88/88 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 88/88 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 34/88 records)
    "Succeeded"  x34
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 36 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (8); Unit 4 Dev (4)
- **Intervals:** median 2.13s (p5 0.42s / p95 26025.89s, n=35)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x30; [Soil Key Puzzle Status, Unit] x6
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/36 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/36 records)
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 30/36 records)
    "RightDrag"  x18
    "LeftDrag"  x12
data.currentSoilType  (string, 30/36 records)
    "CLAYSAND"  x7
    "SAND"  x7
    "CLAY"  x6
    "SANDGRAVEL"  x5
    "CLAYROCK"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 30/36 records)
    "false"  x21
    "true"  x9
data.waterLevelStatus  (string, 30/36 records)
    "TooHigh"  x14
    "Proper"  x10
    "TooLow"  x6
data.waterRetentionChange  (string, 30/36 records)
    "Increase"  x11
    "Decrease"  x10
    "NoChange"  x9
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 33 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (33)
- **Intervals:** median 12.46s (p5 3.32s / p95 59.10s, n=32)
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "On"  x23
    "Off"  x10
data.floor  (string, 33/33 records)
    "3"  x15
    "4"  x13
    "2"  x3
    "1"  x2
data.machineNumber  (string, 33/33 records)
    "One"  x32
    "Two"  x1
data.machineType  (string, 33/33 records)
    "Condenser"  x13
    "Evaporator"  x10
    "DualChamber_Evaporator"  x6
    "DualChamber_Condenser"  x2
    "VentSwitch"  x2
data.room  (string, 33/33 records)
    "2"  x15
    "3"  x12
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 32 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (11); Unit 2 Prod (Refactor) (6); Unit 4 Dev (4); Unit 1 Dev (2); Unit 3 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev - Dungeon (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 753.08s (p5 9.14s / p95 86855.88s, n=31)
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "DebugMenuStateChanged"  x32
data.isOpened  (bool, 32/32 records)
    false  x32
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `argumentationAnswerEvent` — 21 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (11); Unit 1 Dev (5); Unit 5 Dev (3); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 36.67s (p5 12.34s / p95 278838.51s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "submitAnswerEvent"  x21
data.answerSubmitted  (string, 21/21 records)
    16 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 21/21 records)
    "Unit 4 - Flooding"  x11
    "Unit 1 - Freshwater"  x3
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 21 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 4 Dev - Anderson Base (6); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 50.78s (p5 0.07s / p95 278797.33s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "argumentationSessionClose"  x12
    "argumentationSessionOpen"  x9
data.argumentationDescription  (string, 21/21 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x6
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 21/21 records)
    "Unit 4 - Flooding"  x6
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 18 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (18)
- **Intervals:** median 2.59s (p5 0.01s / p95 88373.06s, n=17)
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "Close"  x9
    "Open"  x9
data.toolName  (string, 18/18 records, 16 empty-string)
    ""  x16
    "Settings"  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `gameWindowFocusEvent` — 18 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (14); Transition (2); Unit 4 Dev (2)
- **Intervals:** median 23654.63s (p5 7.57s / p95 135526.12s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 14 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (14)
- **Intervals:** median 79013.11s (p5 912.04s / p95 183526.61s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    true  x14
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 13 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (6); Unit 2 Prod (Refactor) (3); Unit 1 Dev (2); Unit 5 Dev (2)
- **Intervals:** median 3.82s (p5 1.03s / p95 343478.59s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 13/13 records)
    "argumentationToolOpen"  x12
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 13/13 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 2 – Watershed"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 5"  x2
data.toolName  (string, 13/13 records)
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Waterfall Data"  x3
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `soilMachine` — 12 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (12)
- **Intervals:** median 58.91s (p5 1.77s / p95 211.07s, n=11)
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "ChangeCanister"  x12
data.canisterType  (string, 12/12 records)
    "Gravel"  x5
    "Clay"  x4
    "Sand"  x2
    "Bedrock"  x1
data.floor  (string, 12/12 records)
    "4"  x6
    "5"  x5
    "3"  x1
data.machine  (string, 12/12 records)
    "1"  x11
    "2"  x1
data.row  (string, 12/12 records)
    "TopRow"  x9
    "BottomRow"  x3
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 2.78s (p5 0.97s / p95 17.73s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 7 empty-string)
    ""  x7
    "cameraPlaced"  x4
data.boxId  (string, 11/11 records)
    "0"  x5
    "1"  x4
    "2"  x2
data.soilType  (string, 11/11 records)
    "Gravel"  x6
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `SolarStillDesignEvent` — 10 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (10)
- **Intervals:** median 2.92s (p5 1.03s / p95 49.14s, n=9)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x9; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "optionSelected"  x9
    "DesignSubmitted"  x1
data.designSelections  (object, 1/10 records)
data.designSelections.glassRoofTemperature  (string, 1/10 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/10 records)
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/10 records)
    "Tilted Out"  x1
data.featureUsed  (string, 10/10 records)
    "GlassRoofTemperature"  x4
    "RoofStyle"  x4
    "ExtraCovering"  x1
    "Submit"  x1
data.selectedOption  (string, 9/10 records, 1 empty-string)
    "Cold"  x2
    "Tilted Out"  x2
    ""  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 188574.60s (p5 76810.20s / p95 393522.46s, n=4)
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

### `gameWindowUnfocusEvent` — 4 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Transition (2); Unit 4 Dev (2)
- **Intervals:** median 103831.11s (p5 10637.88s / p95 384651.87s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 4/4 records)
    false  x4
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 1108.47s (p5 1108.47s / p95 1108.47s, n=1)
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
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `Soil Key Puzzle` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (24 records)
- `TerasGardenBox` data.actionType: "" (7x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (35x); "WaypointResetEvent" (5x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (48x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (10x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*