# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26e
- **Game version string(s) in log:** 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f26e.jsonl
- **Records:** 15052 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f26e
- **Time span:** 2026-09-23T18:15:36.321000+00:00 .. 2026-10-01T16:08:19.685000+00:00 (189h 52m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **23 event types**, 15052 records, 10 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 91 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `ObjectInterEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5446 | 36.18 | 1 | 4 | 0 | 2026-09-24T17:57:51.030000+00:00 | 2026-10-01T12:48:44.677000+00:00 | 162h 50m |
| InputEvent | 4107 | 27.29 | 1 | 9 | 0 | 2026-09-23T18:15:51.633000+00:00 | 2026-10-01T16:08:19.685000+00:00 | 189h 52m |
| DialogueEvent | 2350 | 15.61 | 1 | 9 | 1483 | 2026-09-23T18:16:08.050000+00:00 | 2026-10-01T16:08:06.680000+00:00 | 189h 51m |
| PlayerPositionEvent | 2001 | 13.29 | 1 | 9 | 0 | 2026-09-23T18:15:46.405000+00:00 | 2026-10-01T16:08:12.619000+00:00 | 189h 52m |
| argumentationNodeEvent | 433 | 2.88 | 1 | 5 | 0 | 2026-09-23T18:42:51.756000+00:00 | 2026-10-01T15:56:38.611000+00:00 | 189h 13m |
| ObjectInterEvent | 277 | 1.84 | 1 | 9 | 0 | 2026-09-23T18:24:49.227000+00:00 | 2026-10-01T16:08:19.684000+00:00 | 189h 43m |
| questEvent | 97 | 0.64 | 1 | 9 | 97 | 2026-09-23T18:16:08.031000+00:00 | 2026-10-01T16:02:02.667000+00:00 | 189h 45m |
| Soil Key Puzzle | 93 | 0.62 | 1 | 3 | 0 | 2026-09-24T18:10:52.680000+00:00 | 2026-09-30T23:57:31.602000+00:00 | 149h 46m |
| TopographicMapEvent | 37 | 0.25 | 1 | 2 | 0 | 2026-09-24T17:59:03.845000+00:00 | 2026-09-30T18:18:36.654000+00:00 | 144h 19m |
| argumentationAnswerEvent | 31 | 0.21 | 1 | 5 | 0 | 2026-09-23T18:43:36.911000+00:00 | 2026-10-01T15:56:39.590000+00:00 | 189h 13m |
| WaterChamberEvent | 30 | 0.2 | 1 | 1 | 0 | 2026-10-01T12:48:12.256000+00:00 | 2026-10-01T15:48:03.427000+00:00 | 2h 59m |
| gameWindowFocusEvent | 29 | 0.19 | 1 | 6 | 0 | 2026-09-23T18:15:36.321000+00:00 | 2026-10-01T15:41:07.226000+00:00 | 189h 25m |
| DEBUGMenu | 25 | 0.17 | 1 | 8 | 0 | 2026-09-23T18:15:46.397000+00:00 | 2026-10-01T15:41:18.848000+00:00 | 189h 25m |
| gameStartEvent | 19 | 0.13 | 1 | 1 | 0 | 2026-09-23T18:15:36.322000+00:00 | 2026-10-01T15:41:07.227000+00:00 | 189h 25m |
| argumentationEvent | 18 | 0.12 | 1 | 5 | 0 | 2026-09-23T18:43:18.575000+00:00 | 2026-10-01T15:56:39.618000+00:00 | 189h 13m |
| gameWindowUnfocusEvent | 12 | 0.08 | 1 | 5 | 0 | 2026-09-23T18:26:59.016000+00:00 | 2026-10-01T00:54:12.288000+00:00 | 174h 27m |
| SolarStillDesignEvent | 11 | 0.07 | 1 | 1 | 0 | 2026-10-01T15:59:20.997000+00:00 | 2026-10-01T15:59:39.019000+00:00 | 18.0s |
| DaniEvent | 8 | 0.05 | 1 | 2 | 0 | 2026-09-28T18:23:40.354000+00:00 | 2026-09-30T18:18:38.143000+00:00 | 47h 54m |
| TerasGardenBox | 8 | 0.05 | 1 | 1 | 0 | 2026-10-01T00:43:14.985000+00:00 | 2026-10-01T00:44:07.783000+00:00 | 52.8s |
| soilMachine | 8 | 0.05 | 1 | 1 | 0 | 2026-10-01T00:11:21.940000+00:00 | 2026-10-01T00:18:21.178000+00:00 | 6m 59s |
| EndOfUnit | 5 | 0.03 | 1 | 5 | 0 | 2026-09-24T17:53:11.374000+00:00 | 2026-10-01T16:08:19.655000+00:00 | 166h 15m |
| chatEvent | 4 | 0.03 | 1 | 2 | 0 | 2026-10-01T00:52:58.775000+00:00 | 2026-10-01T15:48:54.858000+00:00 | 14h 55m |
| argumentationToolEvent | 3 | 0.02 | 1 | 1 | 0 | 2026-09-23T18:43:15.456000+00:00 | 2026-09-23T18:45:50.743000+00:00 | 2m 35s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1980.53s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 70162.831s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 1.598s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 20.171s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 16.826s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 77.643s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 10697.589s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 9287.086s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1532.57s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 978.643s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: d 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `WaterChamberEvent` `data.machineType` — baseline categorical value(s) not seen this build. 
  - Observed: DualChamber_Evaporator 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 6.2x vs baseline. 
  - Observed: 31 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1,; A,3,I; A,C,2,II; B,1,II; C,1,II; C,2,II; C,3,4,II; C,3,II; C,B,2,II; C,D,2,II; D,1,II; D,3,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 433 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 3 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 12 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 37 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[226] _id=6ab419de485cab4c954f4ba6 ts=2026-09-23T18:26:38.4260000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[306] _id=6ab41ad9485cab4c954f52a4 ts=2026-09-23T18:30:49.3810000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[350] _id=6ab41b7c485cab4c954f574c ts=2026-09-23T18:33:32.7450000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[3850] _id=6ab6c0ea485cab4c955e6899 ts=2026-09-25T18:43:53.6240000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[3908] _id=6abaac5b485cab4c956f6ce5 ts=2026-09-28T18:05:13.0300000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[5660] _id=6abab5b7485cab4c957056f9 ts=2026-09-28T18:45:08.8720000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[32] _id=6ab41747485cab4c954f3694 ts=2026-09-23T18:15:36.3220000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[581] _id=6ab561e0485cab4c95539079 ts=2026-09-24T17:46:07.7940000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[827] _id=6ab563da485cab4c9553b932 ts=2026-09-24T17:54:34.0570000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 29 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 29} 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[31] _id=6ab41747485cab4c954f3692 ts=2026-09-23T18:15:36.3210000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[234] _id=6ab419f3485cab4c954f4c42 ts=2026-09-23T18:26:59.6260000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[229] _id=6ab419f4485cab4c954f4c4d ts=2026-09-23T18:27:00.1710000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 12 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 12} 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[228] _id=6ab419f3485cab4c954f4c3e ts=2026-09-23T18:26:59.0160000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[235] _id=6ab419f3485cab4c954f4c4a ts=2026-09-23T18:26:59.9770000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[245] _id=6ab41a18485cab4c954f4d7a ts=2026-09-23T18:27:36.7880000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5445 | 0.0 | 0.024 | 107.668 | 1.451 | 258602.555 | 0.56 | 3503 | 11 |
| InputEvent | 4106 | 0.0 | 0.895 | 166.475 | 18.296 | 256796.21 | 0.36 | 277 | 11 |
| DialogueEvent | 2349 | 0.0 | 3.466 | 290.983 | 28.865 | 256874.2 | 0.21 | 666 | 11 |
| PlayerPositionEvent | 1985 | 0.376 | 10.0 | 322.758 | 10.084 | 256782.191 | 0.19 | 0 | 9 |
| argumentationNodeEvent | 432 | 0.014 | 0.412 | 1576.914 | 9.482 | 435003.0 | 0.04 | 91 | 5 |
| ObjectInterEvent | 276 | 0.0 | 10.349 | 2474.676 | 674.727 | 257121.838 | 0.02 | 3 | 15 |
| questEvent | 96 | 0.001 | 161.648 | 7116.194 | 47963.353 | 256811.498 | 0.01 | 23 | 18 |
| Soil Key Puzzle | 92 | 0.148 | 1.097 | 5860.858 | 3955.367 | 257007.055 | 0.01 | 0 | 5 |
| TopographicMapEvent | 36 | 1.308 | 20.171 | 14432.578 | 86740.758 | 258416.799 | 0.0 | 0 | 7 |
| argumentationAnswerEvent | 30 | 0.791 | 16.826 | 22706.089 | 80312.932 | 435017.357 | 0.0 | 0 | 5 |
| WaterChamberEvent | 29 | 0.623 | 10.864 | 372.109 | 64.104 | 10283.649 | 0.16 | 0 | 1 |
| gameWindowFocusEvent | 28 | 0.545 | 1532.57 | 24354.675 | 85631.622 | 256870.657 | 0.0 | 0 | 19 |
| DEBUGMenu | 24 | 138.24 | 1980.53 | 28413.852 | 86991.778 | 256873.133 | 0.0 | 0 | 19 |
| gameStartEvent | 18 | 145.898 | 9287.086 | 37885.05 | 112826.359 | 256870.656 | 0.0 | 0 | 15 |
| argumentationEvent | 17 | 0.019 | 75.137 | 40070.65 | 153351.56 | 434999.65 | 0.0 | 2 | 5 |
| gameWindowUnfocusEvent | 11 | 0.961 | 978.643 | 57093.934 | 226898.786 | 347030.995 | 0.0 | 0 | 7 |
| SolarStillDesignEvent | 10 | 0.412 | 1.487 | 1.802 | 4.038 | 4.498 | 33.29 | 0 | 0 |
| DaniEvent | 7 | 1.482 | 3.635 | 24642.541 | 117413.605 | 164172.04 | 0.0 | 0 | 2 |
| TerasGardenBox | 7 | 1.032 | 1.598 | 7.543 | 22.964 | 23.728 | 7.95 | 0 | 0 |
| soilMachine | 7 | 2.513 | 45.758 | 59.891 | 158.969 | 183.228 | 1.0 | 0 | 0 |
| EndOfUnit | 4 | 23074.835 | 70162.831 | 149627.07 | 382644.146 | 435107.784 | 0.0 | 0 | 4 |
| chatEvent | 3 | 456.099 | 10697.589 | 17918.694 | 39411.914 | 42602.395 | 0.0 | 0 | 2 |
| argumentationToolEvent | 2 | 3.085 | 77.643 | 77.644 | 144.746 | 152.202 | 0.77 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 5 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[9593] _id=6abd344c485cab4c958d503e ts=2026-09-30T16:09:48.0690000Z == 6aa4144c41b41dbac0c7f26e.jsonl[9603] _id=6abd344c485cab4c958d5040 ts=2026-09-30T16:09:48.0690000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[10411] _id=6abd51aa485cab4c959108b3 ts=2026-09-30T18:15:05.5430000Z == 6aa4144c41b41dbac0c7f26e.jsonl[10390] _id=6abd51aa485cab4c959108bf ts=2026-09-30T18:15:05.5430000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[10391] _id=6abd51aa485cab4c959108c3 ts=2026-09-30T18:15:05.5440000Z == 6aa4144c41b41dbac0c7f26e.jsonl[10398] _id=6abd51aa485cab4c959108c9 ts=2026-09-30T18:15:05.5440000Z`
- **WARNING / Medium** `ObjectInterEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[13299] _id=6abda9b5485cab4c95a3cc32 ts=2026-10-01T00:30:44.8610000Z == 6aa4144c41b41dbac0c7f26e.jsonl[13287] _id=6abda9b5485cab4c95a3cc34 ts=2026-10-01T00:30:44.8610000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 259 group(s), 331 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[906] _id=6ab564d2485cab4c9553cd40 ts=2026-09-24T17:58:40.9970000Z == 6aa4144c41b41dbac0c7f26e.jsonl[897] _id=6ab564d2485cab4c9553cd44 ts=2026-09-24T17:58:40.9970000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[891] _id=6ab564d3485cab4c9553cd58 ts=2026-09-24T17:58:41.0300000Z == 6aa4144c41b41dbac0c7f26e.jsonl[910] _id=6ab564d3485cab4c9553cd5e ts=2026-09-24T17:58:41.0300000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[892] _id=6ab564d3485cab4c9553cd6e ts=2026-09-24T17:58:41.0450000Z == 6aa4144c41b41dbac0c7f26e.jsonl[912] _id=6ab564d3485cab4c9553cd74 ts=2026-09-24T17:58:41.0450000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa4144c41b41dbac0c7f26e.jsonl[184] _id=6ab41971485cab4c954f474a ts=2026-09-23T18:24:49.2270000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[187] _id=6ab41971485cab4c954f474c ts=2026-09-23T18:24:49.2300000Z`; `1ms: 6aa4144c41b41dbac0c7f26e.jsonl[13212] _id=6abda96f485cab4c95a3cb9c ts=2026-10-01T00:29:35.0840000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[13215] _id=6abda96f485cab4c95a3cb9e ts=2026-10-01T00:29:35.0850000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 782 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa4144c41b41dbac0c7f26e.jsonl[889] _id=6ab564d1485cab4c9553cd2c ts=2026-09-24T17:58:40.5190000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[896] _id=6ab564d1485cab4c9553cd30 ts=2026-09-24T17:58:40.5260000Z`; `15ms: 6aa4144c41b41dbac0c7f26e.jsonl[911] _id=6ab564d3485cab4c9553cd66 ts=2026-09-24T17:58:41.0300000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[892] _id=6ab564d3485cab4c9553cd6e ts=2026-09-24T17:58:41.0450000Z`; `105ms: 6aa4144c41b41dbac0c7f26e.jsonl[1107] _id=6ab56533485cab4c9553d855 ts=2026-09-24T17:58:42.1970000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[1098] _id=6ab56533485cab4c9553d85e ts=2026-09-24T17:58:42.3020000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `791ms: 6aa4144c41b41dbac0c7f26e.jsonl[710] _id=6ab562d3485cab4c9553a25a ts=2026-09-24T17:50:10.9860000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[728] _id=6ab562d3485cab4c9553a269 ts=2026-09-24T17:50:11.7770000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `24ms: 6aa4144c41b41dbac0c7f26e.jsonl[9450] _id=6abd334f485cab4c958d414e ts=2026-09-30T16:05:35.8370000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[9457] _id=6abd3350485cab4c958d4158 ts=2026-09-30T16:05:35.8610000Z`; `19ms: 6aa4144c41b41dbac0c7f26e.jsonl[13659] _id=6abdab93485cab4c95a3cf1a ts=2026-10-01T00:38:43.2940000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[13660] _id=6abdab93485cab4c95a3cf20 ts=2026-10-01T00:38:43.3130000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 54 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa4144c41b41dbac0c7f26e.jsonl[511] _id=6ab41dcf485cab4c954f6aa5 ts=2026-09-23T18:43:27.6170000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[505] _id=6ab41dcf485cab4c954f6aa7 ts=2026-09-23T18:43:27.6370000Z`; `731ms: 6aa4144c41b41dbac0c7f26e.jsonl[505] _id=6ab41dcf485cab4c954f6aa7 ts=2026-09-23T18:43:27.6370000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[514] _id=6ab41dd0485cab4c954f6aad ts=2026-09-23T18:43:28.3680000Z`; `24ms: 6aa4144c41b41dbac0c7f26e.jsonl[514] _id=6ab41dd0485cab4c954f6aad ts=2026-09-23T18:43:28.3680000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[506] _id=6ab41dd0485cab4c954f6ab1 ts=2026-09-23T18:43:28.3920000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `545ms: 6aa4144c41b41dbac0c7f26e.jsonl[234] _id=6ab419f3485cab4c954f4c42 ts=2026-09-23T18:26:59.6260000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[229] _id=6ab419f4485cab4c954f4c4d ts=2026-09-23T18:27:00.1710000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `961ms: 6aa4144c41b41dbac0c7f26e.jsonl[228] _id=6ab419f3485cab4c954f4c3e ts=2026-09-23T18:26:59.0160000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[235] _id=6ab419f3485cab4c954f4c4a ts=2026-09-23T18:26:59.9770000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 10 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `21ms: 6aa4144c41b41dbac0c7f26e.jsonl[3850] _id=6ab6c0ea485cab4c955e6899 ts=2026-09-25T18:43:53.6240000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[3840] _id=6ab6c0ea485cab4c955e689b ts=2026-09-25T18:43:53.6450000Z`; `5ms: 6aa4144c41b41dbac0c7f26e.jsonl[3908] _id=6abaac5b485cab4c956f6ce5 ts=2026-09-28T18:05:13.0300000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[3915] _id=6abaac5b485cab4c956f6ce9 ts=2026-09-28T18:05:13.0350000Z`; `7ms: 6aa4144c41b41dbac0c7f26e.jsonl[5660] _id=6abab5b7485cab4c957056f9 ts=2026-09-28T18:45:08.8720000Z ~ 6aa4144c41b41dbac0c7f26e.jsonl[5661] _id=6abab5b7485cab4c957056fb ts=2026-09-28T18:45:08.8790000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa4144c41b41dbac0c7f26e.jsonl[3844] _id=6ab6c0e8485cab4c955e687d ts=2026-09-25T18:43:52.7130000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3903] _id=6abaac51485cab4c956f6c93 ts=2026-09-28T18:05:05.8460000Z; 24h 16m: 6aa4144c41b41dbac0c7f26e.jsonl[828] _id=6ab563e0485cab4c9553b9a0 ts=2026-09-24T17:54:40.1430000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2708] _id=6ab6b950485cab4c955dbd1b ts=2026-09-25T18:11:28.5130000Z; 23h 30m: 6aa4144c41b41dbac0c7f26e.jsonl[30] _id=6ab41751485cab4c954f36b0 ts=2026-09-23T18:15:46.3970000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[583] _id=6ab561e9485cab4c95539118 ts=2026-09-24T17:46:17.4900000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 45h 36m 
  - Evidence: 45h 36m: 6aa4144c41b41dbac0c7f26e.jsonl[5184] _id=6abab0b8485cab4c956ff1a5 ts=2026-09-28T18:23:52.3110000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9173] _id=6abd3207485cab4c958d2b39 ts=2026-09-30T16:00:04.3510000Z; 2h 18m: 6aa4144c41b41dbac0c7f26e.jsonl[9183] _id=6abd3207485cab4c958d2b48 ts=2026-09-30T16:00:06.0720000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10425] _id=6abd527c485cab4c95912349 ts=2026-09-30T18:18:36.6610000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa4144c41b41dbac0c7f26e.jsonl[3871] _id=6ab6c12f485cab4c955e6987 ts=2026-09-25T18:45:03.5630000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3944] _id=6abaac99485cab4c956f6f75 ts=2026-09-28T18:06:17.7630000Z; 24h 2m: 6aa4144c41b41dbac0c7f26e.jsonl[2633] _id=6ab5673e485cab4c95541a02 ts=2026-09-24T18:09:02.2650000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2734] _id=6ab6b968485cab4c955dbf93 ts=2026-09-25T18:11:52.7040000Z; 23h 25m: 6aa4144c41b41dbac0c7f26e.jsonl[5648] _id=6abab62e485cab4c95706027 ts=2026-09-28T18:47:10.2270000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6042] _id=6abbff81485cab4c95842381 ts=2026-09-29T18:12:17.2300000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 666 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[13562] _id=6abdab47485cab4c95a3ce62 ts=2026-10-01T00:37:26.9650000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13574] _id=6abdab47485cab4c95a3ce64 ts=2026-10-01T00:37:26.9650000Z; 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[14785] _id=6abe82a8485cab4c95ab9bd8 ts=2026-10-01T15:56:24.4110000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[14784] _id=6abe82a8485cab4c95ab9bda ts=2026-10-01T15:56:24.4110000Z; 1ms: 6aa4144c41b41dbac0c7f26e.jsonl[10371] _id=6abd5165485cab4c959100c7 ts=2026-09-30T18:13:57.5030000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10372] _id=6abd5165485cab4c959100cb ts=2026-09-30T18:13:57.5040000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 51m 
  - Evidence: 120h 51m: 6aa4144c41b41dbac0c7f26e.jsonl[823] _id=6ab56387485cab4c9553b23a ts=2026-09-24T17:53:11.3740000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[7820] _id=6abc072b485cab4c9584bceb ts=2026-09-29T18:44:59.1580000Z; 23h 42m: 6aa4144c41b41dbac0c7f26e.jsonl[7820] _id=6abc072b485cab4c9584bceb ts=2026-09-29T18:44:59.1580000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10628] _id=6abd5491485cab4c95917a73 ts=2026-09-30T18:27:29.3570000Z; 15h 16m: 6aa4144c41b41dbac0c7f26e.jsonl[13924] _id=6abdaeb4485cab4c95a3d18c ts=2026-10-01T00:52:04.1920000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[15051] _id=6abe8573485cab4c95abc16e ts=2026-10-01T16:08:19.6550000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 19m 
  - Evidence: 71h 19m: 6aa4144c41b41dbac0c7f26e.jsonl[3885] _id=6ab6c13c485cab4c955e69cf ts=2026-09-25T18:45:16.7440000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3889] _id=6abaac59485cab4c956f6cad ts=2026-09-28T18:05:12.9540000Z; 23h 59m: 6aa4144c41b41dbac0c7f26e.jsonl[2694] _id=6ab567f9485cab4c95542216 ts=2026-09-24T18:12:09.3470000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2713] _id=6ab6b957485cab4c955dbda9 ts=2026-09-25T18:11:35.3460000Z; 23h 22m: 6aa4144c41b41dbac0c7f26e.jsonl[6005] _id=6abab648485cab4c957066a4 ts=2026-09-28T18:47:36.3690000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6125] _id=6abbfee6485cab4c95841b91 ts=2026-09-29T18:09:40.8150000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 277 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[10391] _id=6abd51aa485cab4c959108c3 ts=2026-09-30T18:15:05.5440000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10398] _id=6abd51aa485cab4c959108c9 ts=2026-09-30T18:15:05.5440000Z; 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[10411] _id=6abd51aa485cab4c959108b3 ts=2026-09-30T18:15:05.5430000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10390] _id=6abd51aa485cab4c959108bf ts=2026-09-30T18:15:05.5430000Z; 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[10414] _id=6abd51aa485cab4c959108d9 ts=2026-09-30T18:15:05.5460000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[8589] _id=6abd51aa485cab4c959108e2 ts=2026-09-30T18:15:05.5460000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 71h 25m 
  - Evidence: 71h 25m: 6aa4144c41b41dbac0c7f26e.jsonl[3780] _id=6ab6c04d485cab4c955e654b ts=2026-09-25T18:41:17.4070000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3958] _id=6abaacaf485cab4c956f7157 ts=2026-09-28T18:06:39.2450000Z; 24h 2m: 6aa4144c41b41dbac0c7f26e.jsonl[2664] _id=6ab567ac485cab4c95541f62 ts=2026-09-24T18:10:52.6830000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2753] _id=6ab6b9a6485cab4c955dc7e4 ts=2026-09-25T18:12:54.3930000Z; 23h 26m: 6aa4144c41b41dbac0c7f26e.jsonl[6008] _id=6abab648485cab4c9570669e ts=2026-09-28T18:47:36.3600000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6650] _id=6abbffd7485cab4c958426af ts=2026-09-29T18:13:43.8350000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[13299] _id=6abda9b5485cab4c95a3cc32 ts=2026-10-01T00:30:44.8610000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13287] _id=6abda9b5485cab4c95a3cc34 ts=2026-10-01T00:30:44.8610000Z; 1ms: 6aa4144c41b41dbac0c7f26e.jsonl[13212] _id=6abda96f485cab4c95a3cb9c ts=2026-10-01T00:29:35.0840000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13215] _id=6abda96f485cab4c95a3cb9e ts=2026-10-01T00:29:35.0850000Z; 3ms: 6aa4144c41b41dbac0c7f26e.jsonl[184] _id=6ab41971485cab4c954f474a ts=2026-09-23T18:24:49.2270000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[187] _id=6ab41971485cab4c954f474c ts=2026-09-23T18:24:49.2300000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 71h 19m 
  - Evidence: 71h 19m: 6aa4144c41b41dbac0c7f26e.jsonl[3886] _id=6ab6c143485cab4c955e69e9 ts=2026-09-25T18:45:23.6630000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3909] _id=6abaac59485cab4c956f6ca9 ts=2026-09-28T18:05:05.8540000Z; 23h 59m: 6aa4144c41b41dbac0c7f26e.jsonl[2697] _id=6ab56808485cab4c95542290 ts=2026-09-24T18:12:24.9350000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2717] _id=6ab6b957485cab4c955dbda3 ts=2026-09-25T18:11:28.5230000Z; 23h 21m: 6aa4144c41b41dbac0c7f26e.jsonl[6017] _id=6abab64b485cab4c957067a4 ts=2026-09-28T18:47:39.7830000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6124] _id=6abbfee5485cab4c95841b8f ts=2026-09-29T18:09:34.4930000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 71h 50m 
  - Evidence: 71h 50m: 6aa4144c41b41dbac0c7f26e.jsonl[3345] _id=6ab6bae9485cab4c955df373 ts=2026-09-25T18:18:15.9280000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3994] _id=6abaad12485cab4c956f775b ts=2026-09-28T18:08:18.4830000Z; 24h 6m: 6aa4144c41b41dbac0c7f26e.jsonl[2613] _id=6ab56716485cab4c95541692 ts=2026-09-24T18:08:21.2150000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2815] _id=6ab6ba6e485cab4c955de010 ts=2026-09-25T18:14:48.3370000Z; 23h 22m: 6aa4144c41b41dbac0c7f26e.jsonl[6019] _id=6abab64a485cab4c9570675c ts=2026-09-28T18:47:37.4050000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6139] _id=6abbfee8485cab4c95841ba5 ts=2026-09-29T18:09:43.7580000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3503 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[10005] _id=6abd4f1e485cab4c9590d583 ts=2026-09-30T18:04:13.9560000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9997] _id=6abd4f1f485cab4c9590d585 ts=2026-09-30T18:04:13.9560000Z; 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[10010] _id=6abd4f28485cab4c9590d5d3 ts=2026-09-30T18:04:23.6630000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10015] _id=6abd4f28485cab4c9590d5d5 ts=2026-09-30T18:04:23.6630000Z; 0ms: 6aa4144c41b41dbac0c7f26e.jsonl[10013] _id=6abd4f28485cab4c9590d5cd ts=2026-09-30T18:04:23.6630000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[10014] _id=6abd4f28485cab4c9590d5d1 ts=2026-09-30T18:04:23.6630000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 71h 23m 
  - Evidence: 71h 23m: 6aa4144c41b41dbac0c7f26e.jsonl[3811] _id=6ab6c0c0485cab4c955e67d9 ts=2026-09-25T18:43:12.1830000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3962] _id=6abaacaf485cab4c956f7155 ts=2026-09-28T18:06:39.2380000Z; 46h 0m: 6aa4144c41b41dbac0c7f26e.jsonl[3996] _id=6abaad22485cab4c956f7954 ts=2026-09-28T18:08:34.8770000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9559] _id=6abd340b485cab4c958d4ba0 ts=2026-09-30T16:08:43.3670000Z; 24h 30m: 6aa4144c41b41dbac0c7f26e.jsonl[2665] _id=6ab567af485cab4c95541f80 ts=2026-09-24T18:10:55.6650000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3779] _id=6ab6c04d485cab4c955e6547 ts=2026-09-25T18:41:17.4010000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 71h 46m 
  - Evidence: 71h 46m: 6aa4144c41b41dbac0c7f26e.jsonl[3691] _id=6ab6bf3f485cab4c955e5415 ts=2026-09-25T18:36:47.2010000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[5179] _id=6abab0b0485cab4c956ff11a ts=2026-09-28T18:23:44.0000000Z; 24h 14m: 6aa4144c41b41dbac0c7f26e.jsonl[927] _id=6ab564fc485cab4c9553d084 ts=2026-09-24T17:59:24.3780000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2777] _id=6ab6b9e9485cab4c955dcf17 ts=2026-09-25T18:14:01.4140000Z; 24h 2m: 6aa4144c41b41dbac0c7f26e.jsonl[5182] _id=6abab0b5485cab4c956ff185 ts=2026-09-28T18:23:49.8270000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[7259] _id=6abc02d7485cab4c95846d17 ts=2026-09-29T18:26:31.8260000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 2h 51m 
  - Evidence: 2h 51m: 6aa4144c41b41dbac0c7f26e.jsonl[14277] _id=6abe5716485cab4c95a3f8fd ts=2026-10-01T12:50:30.9850000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[14335] _id=6abe7f40485cab4c95ab285c ts=2026-10-01T15:41:54.6340000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 50m 
  - Evidence: 120h 50m: 6aa4144c41b41dbac0c7f26e.jsonl[729] _id=6ab562d6485cab4c9553a28a ts=2026-09-24T17:50:14.6320000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[7712] _id=6abc0620485cab4c9584a745 ts=2026-09-29T18:40:31.9890000Z; 23h 2m: 6aa4144c41b41dbac0c7f26e.jsonl[574] _id=6ab41e61485cab4c954f7045 ts=2026-09-23T18:45:53.3810000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[662] _id=6ab5626b485cab4c95539b00 ts=2026-09-24T17:48:27.0440000Z; 21h 24m: 6aa4144c41b41dbac0c7f26e.jsonl[7712] _id=6abc0620485cab4c9584a745 ts=2026-09-29T18:40:31.9890000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9433] _id=6abd333d485cab4c958d406c ts=2026-09-30T16:05:17.3600000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 49m 
  - Evidence: 120h 49m: 6aa4144c41b41dbac0c7f26e.jsonl[730] _id=6ab562d6485cab4c9553a28e ts=2026-09-24T17:50:14.6470000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[7697] _id=6abc060e485cab4c9584a5fd ts=2026-09-29T18:40:14.2970000Z; 23h 2m: 6aa4144c41b41dbac0c7f26e.jsonl[572] _id=6ab41e61485cab4c954f7049 ts=2026-09-23T18:45:53.4010000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[652] _id=6ab5625d485cab4c955399c3 ts=2026-09-24T17:48:12.9390000Z; 21h 24m: 6aa4144c41b41dbac0c7f26e.jsonl[7726] _id=6abc0620485cab4c9584a74b ts=2026-09-29T18:40:32.0130000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9399] _id=6abd331a485cab4c958d3e70 ts=2026-09-30T16:04:42.6740000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.024s shown 
  - Evidence: 19ms: 6aa4144c41b41dbac0c7f26e.jsonl[13659] _id=6abdab93485cab4c95a3cf1a ts=2026-10-01T00:38:43.2940000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13660] _id=6abdab93485cab4c95a3cf20 ts=2026-10-01T00:38:43.3130000Z; 24ms: 6aa4144c41b41dbac0c7f26e.jsonl[9450] _id=6abd334f485cab4c958d414e ts=2026-09-30T16:05:35.8370000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9457] _id=6abd3350485cab4c958d4158 ts=2026-09-30T16:05:35.8610000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 120h 50m 
  - Evidence: 120h 50m: 6aa4144c41b41dbac0c7f26e.jsonl[709] _id=6ab562d2485cab4c9553a254 ts=2026-09-24T17:50:10.0130000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[7693] _id=6abc060d485cab4c9584a5e9 ts=2026-09-29T18:40:13.0130000Z; 23h 1m: 6aa4144c41b41dbac0c7f26e.jsonl[570] _id=6ab41e5d485cab4c954f7027 ts=2026-09-23T18:45:49.1570000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[634] _id=6ab5622f485cab4c955395f6 ts=2026-09-24T17:47:27.6370000Z; 21h 24m: 6aa4144c41b41dbac0c7f26e.jsonl[7722] _id=6abc061e485cab4c9584a72b ts=2026-09-29T18:40:30.1670000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[9394] _id=6abd3317485cab4c958d3e58 ts=2026-09-30T16:04:39.7460000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 91 interval(s) ≤ 0.014s..0.015s shown 
  - Evidence: 14ms: 6aa4144c41b41dbac0c7f26e.jsonl[13370] _id=6abdaa4e485cab4c95a3ccc6 ts=2026-10-01T00:33:18.3260000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13371] _id=6abdaa4e485cab4c95a3ccc8 ts=2026-10-01T00:33:18.3400000Z; 14ms: 6aa4144c41b41dbac0c7f26e.jsonl[13656] _id=6abdab90485cab4c95a3cf10 ts=2026-10-01T00:38:40.2900000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13657] _id=6abdab90485cab4c95a3cf12 ts=2026-10-01T00:38:40.3040000Z; 15ms: 6aa4144c41b41dbac0c7f26e.jsonl[13444] _id=6abdaae4485cab4c95a3cd98 ts=2026-10-01T00:35:48.0330000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13445] _id=6abdaae4485cab4c95a3cd9a ts=2026-10-01T00:35:48.0480000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 11h 50m 
  - Evidence: 11h 50m: 6aa4144c41b41dbac0c7f26e.jsonl[13939] _id=6abdaeea485cab4c95a3d196 ts=2026-10-01T00:52:58.7750000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[13967] _id=6abe5553485cab4c95a3dba1 ts=2026-10-01T12:43:01.1700000Z; 2h 58m: 6aa4144c41b41dbac0c7f26e.jsonl[13967] _id=6abe5553485cab4c95a3dba1 ts=2026-10-01T12:43:01.1700000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[14297] _id=6abe7f1c485cab4c95ab1f16 ts=2026-10-01T15:41:18.7590000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa4144c41b41dbac0c7f26e.jsonl[3832] _id=6ab6c0e3485cab4c955e6877 ts=2026-09-25T18:43:47.0160000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3887] _id=6abaac49485cab4c956f6bd5 ts=2026-09-28T18:04:57.6720000Z; 24h 16m: 6aa4144c41b41dbac0c7f26e.jsonl[827] _id=6ab563da485cab4c9553b932 ts=2026-09-24T17:54:34.0570000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2705] _id=6ab6b948485cab4c955dbc15 ts=2026-09-25T18:11:20.8340000Z; 23h 30m: 6aa4144c41b41dbac0c7f26e.jsonl[32] _id=6ab41747485cab4c954f3694 ts=2026-09-23T18:15:36.3220000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[581] _id=6ab561e0485cab4c95539079 ts=2026-09-24T17:46:07.7940000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 71h 21m 
  - Evidence: 71h 21m: 6aa4144c41b41dbac0c7f26e.jsonl[3843] _id=6ab6c0e2485cab4c955e6875 ts=2026-09-25T18:43:47.0140000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3888] _id=6abaac49485cab4c956f6bcf ts=2026-09-28T18:04:57.6710000Z; 23h 59m: 6aa4144c41b41dbac0c7f26e.jsonl[2679] _id=6ab567ed485cab4c95542184 ts=2026-09-24T18:11:57.7980000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2706] _id=6ab6b948485cab4c955dbc11 ts=2026-09-25T18:11:20.8330000Z; 23h 24m: 6aa4144c41b41dbac0c7f26e.jsonl[5646] _id=6abab5a6485cab4c9570553b ts=2026-09-28T18:44:54.4940000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6131] _id=6abbfed7485cab4c95841b79 ts=2026-09-29T18:09:27.7790000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 23m 
  - Evidence: 96h 23m: 6aa4144c41b41dbac0c7f26e.jsonl[2696] _id=6ab56807485cab4c95542282 ts=2026-09-24T18:12:23.7710000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[5508] _id=6abab39e485cab4c95702545 ts=2026-09-28T18:36:14.7660000Z; 29h 39m: 6aa4144c41b41dbac0c7f26e.jsonl[6945] _id=6abc0036485cab4c958431bd ts=2026-09-29T18:15:18.5380000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[11435] _id=6abda145485cab4c95a3bd92 ts=2026-09-30T23:54:45.1160000Z; 23h 44m: 6aa4144c41b41dbac0c7f26e.jsonl[245] _id=6ab41a18485cab4c954f4d7a ts=2026-09-23T18:27:36.7880000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2674] _id=6ab567e5485cab4c95542110 ts=2026-09-24T18:11:49.0720000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 71h 20m 
  - Evidence: 71h 20m: 6aa4144c41b41dbac0c7f26e.jsonl[3866] _id=6ab6c12d485cab4c955e697d ts=2026-09-25T18:45:01.5320000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[3908] _id=6abaac5b485cab4c956f6ce5 ts=2026-09-28T18:05:13.0300000Z; 24h 15m: 6aa4144c41b41dbac0c7f26e.jsonl[703] _id=6ab5642c485cab4c9553bece ts=2026-09-24T17:55:56.3930000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[2732] _id=6ab6b959485cab4c955dbe2f ts=2026-09-25T18:11:35.4150000Z; 23h 24m: 6aa4144c41b41dbac0c7f26e.jsonl[5636] _id=6abab5b8485cab4c957056ff ts=2026-09-28T18:45:08.8830000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[6134] _id=6abbfee7485cab4c95841b9f ts=2026-09-29T18:09:40.8590000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 23 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa4144c41b41dbac0c7f26e.jsonl[14329] _id=6abe7f84485cab4c95ab35be ts=2026-10-01T15:43:03.0640000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[14323] _id=6abe7f84485cab4c95ab35ca ts=2026-10-01T15:43:03.0650000Z; 2ms: 6aa4144c41b41dbac0c7f26e.jsonl[14253] _id=6abe56dc485cab4c95a3f1ed ts=2026-10-01T12:49:32.8830000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[14254] _id=6abe56dc485cab4c95a3f1ef ts=2026-10-01T12:49:32.8850000Z; 2ms: 6aa4144c41b41dbac0c7f26e.jsonl[14846] _id=6abe82fd485cab4c95aba090 ts=2026-10-01T15:57:49.5550000Z -> 6aa4144c41b41dbac0c7f26e.jsonl[14834] _id=6abe82fd485cab4c95aba094 ts=2026-10-01T15:57:49.5570000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DaniEvent` `actionType` — tool open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' per toolName 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[9173] _id=6abd3207485cab4c958d2b39 ts=2026-09-30T16:00:04.3510000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[9183] _id=6abd3207485cab4c958d2b48 ts=2026-09-30T16:00:06.0720000Z` 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 13 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[457] _id=6ab41d5a485cab4c954f660d ts=2026-09-23T18:41:30.1790000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[739] _id=6ab562eb485cab4c9553a41e ts=2026-09-24T17:50:35.0820000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[3595] _id=6ab6be08485cab4c955e4771 ts=2026-09-25T18:31:36.2100000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 168 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[1235] _id=6ab5654f485cab4c9553dd80 ts=2026-09-24T18:00:46.4810000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[943] _id=6ab56553485cab4c9553de5e ts=2026-09-24T18:00:50.2490000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[944] _id=6ab56553485cab4c9553de62 ts=2026-09-24T18:00:50.3900000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 282 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[1108] _id=6ab56532485cab4c9553d7e2 ts=2026-09-24T17:58:38.2860000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[890] _id=6ab564d2485cab4c9553cd52 ts=2026-09-24T17:58:41.0150000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[910] _id=6ab564d3485cab4c9553cd5e ts=2026-09-24T17:58:41.0300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[9457] _id=6abd3350485cab4c958d4158 ts=2026-09-30T16:05:35.8610000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[13660] _id=6abdab93485cab4c95a3cf20 ts=2026-10-01T00:38:43.3130000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[511] _id=6ab41dcf485cab4c954f6aa5 ts=2026-09-23T18:43:27.6170000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[505] _id=6ab41dcf485cab4c954f6aa7 ts=2026-09-23T18:43:27.6370000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[506] _id=6ab41dd0485cab4c954f6ab1 ts=2026-09-23T18:43:28.3920000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[13939] _id=6abdaeea485cab4c95a3d196 ts=2026-10-01T00:52:58.7750000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[13967] _id=6abe5553485cab4c95a3dba1 ts=2026-10-01T12:43:01.1700000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[14297] _id=6abe7f1c485cab4c95ab1f16 ts=2026-10-01T15:41:18.7590000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[12338] _id=6abda3a7485cab4c95a3c4c2 ts=2026-10-01T00:04:55.7660000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 784 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[983] _id=6ab56556485cab4c9553df12 ts=2026-09-24T18:00:51.6530000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[1004] _id=6ab5655b485cab4c9553e01a ts=2026-09-24T18:00:57.9420000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[999] _id=6ab5655b485cab4c9553e060 ts=2026-09-24T18:00:58.7820000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1088 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[896] _id=6ab564d1485cab4c9553cd30 ts=2026-09-24T17:58:40.5260000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[906] _id=6ab564d2485cab4c9553cd40 ts=2026-09-24T17:58:40.9970000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[897] _id=6ab564d2485cab4c9553cd44 ts=2026-09-24T17:58:40.9970000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[3962] _id=6abaacaf485cab4c956f7155 ts=2026-09-28T18:06:39.2380000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[13594] _id=6abdab60485cab4c95a3ce9e ts=2026-10-01T00:37:52.7320000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[13609] _id=6abdab69485cab4c95a3cea8 ts=2026-10-01T00:38:01.2200000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[13610] _id=6abdab69485cab4c95a3ceac ts=2026-10-01T00:38:01.8070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** — single event attributed to a different scene between two runs of the same scene. 
  - Observed: 1 PlayerPositionEvent record in 'Unit 4 Dev' inside a 'Unit 4 Dev - Dungeon' period 
  - Expected: scene-consistent attribution (or a real quick scene hop) 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[12716] _id=6abda61b485cab4c95a3c790 ts=2026-10-01T00:15:23.4650000Z`
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'DialogueStartEvent' (totals: 438 start, 429 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 207 unmatched 'BecameCameraCentered' (totals: 1075 open, 1036 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 135 unmatched 'BecameVisible' (totals: 1594 open, 1741 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationNodeHoverStart' (totals: 187 open, 197 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 1 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 28 unmatched 'questActiveEvent' (totals: 62 start, 35 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 345 of 15051 adjacent _id pairs reverse in client time; worst 145.0s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f26e.jsonl[1040] _id=6ab56530485cab4c9553d788 ts=2026-09-24T18:00:15.9870000Z`; `6aa4144c41b41dbac0c7f26e.jsonl[1078] _id=6ab56530485cab4c9553d79a ts=2026-09-24T17:57:51.0300000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -146.00s, max +2.31s over 15052 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26e\coverage.yaml

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

### `PuzzlePieceVisibleEvent` — 5446 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3942); Unit 4 Dev (1098); Unit 3 Dungeon Dev (212); Unit 5 Dev - Dungeon (194)
- **Intervals:** median 0.02s (p5 0.00s / p95 1.45s, n=5445)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5446/5446 records)
    "BecameInvisible"  x1741
    "BecameVisible"  x1594
    "BecameCameraCentered"  x1075
    "BecameCameraUncentered"  x1036
data.pieceId  (string, 5446/5446 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5446/5446 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 4107 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1342); Unit 3 Dev (1205); Unit 4 Dev (409); Unit 4 Dev - Dungeon (313); Unit 3 Dungeon Dev (255); Unit 1 Dev (206); Unit 5 Dev - Dungeon (177); Unit 4 Dev - Anderson Base (146); Unit 5 Dev (54)
- **Intervals:** median 0.90s (p5 0.02s / p95 18.30s, n=4106)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 4107/4107 records)
    "pressed"  x4107
data.actionType  (string, 4107/4107 records)
    "Move"  x2963
    "Jump"  x507
    "Interact"  x436
    "Sprint"  x90
    "Ascend"  x63
    "Hoverboard"  x40
    "Map"  x5
    "SkipCinematic"  x2
    "Pause"  x1
data.key  (string, 4107/4107 records, 5 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 4107/4107 records)
    "Player"  x2746
    "Drone"  x1361
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2350 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (710); Unit 3 Dev (382); Unit 4 Dev (299); Unit 1 Dev (244); Unit 5 Dev (224); Unit 3 Dungeon Dev (185); Unit 4 Dev - Anderson Base (125); Unit 5 Dev - Dungeon (91); Unit 4 Dev - Dungeon (90)
- **eventKey:** present on 1483 of 2350 records
- **Intervals:** median 3.47s (p5 0.00s / p95 28.86s, n=2349)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1483; [conversationId, dialogueEventType] x867
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2350/2350 records)
    numeric range 8 .. 118 (56 unique)
data.dialogueEventType  (string, 2350/2350 records)
    "DialogueNodeEvent"  x1483
    "DialogueStartEvent"  x438
    "DialogueFinishEvent"  x429
data.nodeId  (number, 1483/2350 records)
    numeric range 0 .. 290 (226 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2001 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (764); Unit 3 Dev (283); Unit 4 Dev (225); Unit 1 Dev (223); Unit 5 Dev (114); Unit 4 Dev - Dungeon (110); Unit 3 Dungeon Dev (108); Unit 5 Dev - Dungeon (101); Unit 4 Dev - Anderson Base (73)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.08s, n=1985)
- **Fields under `data`:**

```text
data.position  (object, 2001/2001 records)
data.position.x  (number, 2001/2001 records)
    numeric range -1985.7 .. 1549.85 (752 unique)
data.position.y  (number, 2001/2001 records)
    numeric range -21054.4 .. 222.405 (570 unique)
data.position.z  (number, 2001/2001 records)
    numeric range -1040.97 .. 2237 (753 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 433 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (209); Unit 1 Dev (78); Unit 5 Dev (76); Unit 3 Dev (41); Unit 2 Prod (Refactor) (29)
- **Intervals:** median 0.41s (p5 0.02s / p95 9.48s, n=432)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 433/433 records)
    "argumentationNodeHoverEnd"  x197
    "argumentationNodeHoverStart"  x187
    "argumentationNodeAdd"  x35
    "argumentationNodeRemove"  x14
data.argumentationTitle  (string, 433/433 records)
    "Unit 4 - Flooding"  x209
    "Unit 5"  x76
    "Unit 3 - Pollution Upstream"  x41
    "Unit 1 - Freshwater"  x40
    "Unit 1 - Argumentation Tutorial"  x38
    "Unit 2 – Watershed"  x29
data.nodeName  (string, 433/433 records)
    "A"  x69
    "C"  x62
    "D"  x62
    "1"  x49
    "II"  x40
    "B"  x38
    "I"  x33
    "2"  x30
    "3"  x27
    "4"  x16
    "5"  x7
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 277 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (85); Unit 4 Dev - Dungeon (70); Unit 3 Dungeon Dev (46); Unit 4 Dev (29); Unit 3 Dev (12); Unit 1 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev - Dungeon (9); Unit 5 Dev (6)
- **Intervals:** median 10.35s (p5 2.41s / p95 674.73s, n=276)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 277/277 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 277/277 records)
    109 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 97 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (30); Unit 1 Dev (15); Unit 3 Dev (12); Unit 4 Dev (10); Unit 5 Dev - Dungeon (10); Unit 4 Dev - Dungeon (8); Unit 5 Dev (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 97 of 97 records
- **Intervals:** median 161.65s (p5 0.00s / p95 47963.35s, n=96)
- **`data` key-set variants:** [questEventType, questID, questName] x62; [questEventType, questID, questName, questSuccessOrFailure] x35
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 97/97 records)
    "questActiveEvent"  x62
    "questFinishEvent"  x35
data.questID  (string, 97/97 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 97/97 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 35/97 records)
    "Succeeded"  x35
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 93 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (56); Unit 4 Dev (25); Unit 3 Dev (12)
- **Intervals:** median 1.10s (p5 0.19s / p95 3955.37s, n=92)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x82; [Soil Key Puzzle Status, Unit] x11
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/93 records)
    "Started"  x6
    "Finished"  x5
data.Unit  (string, 11/93 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 4 Dev"  x4
    "Unit 3 Dev"  x2
data.actionType  (string, 82/93 records)
    "RightDrag"  x48
    "LeftDrag"  x34
data.currentSoilType  (string, 82/93 records)
    "CLAYSAND"  x19
    "CLAY"  x17
    "SAND"  x17
    "CLAYROCK"  x11
    "SANDGRAVEL"  x11
    "GRAVEL"  x4
    "BEDROCK"  x3
data.isCorrectSelection  (string, 82/93 records)
    "false"  x63
    "true"  x19
data.waterLevelStatus  (string, 82/93 records)
    "Proper"  x37
    "TooHigh"  x27
    "TooLow"  x18
data.waterRetentionChange  (string, 82/93 records)
    "Increase"  x40
    "Decrease"  x23
    "NoChange"  x19
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 37 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (21); Unit 2 Prod (Refactor) (16)
- **Intervals:** median 20.17s (p5 1.55s / p95 86740.76s, n=36)
- **`data` key-set variants:** [actionType, featureUsed] x34; [actionType, featureUsed, location] x3
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 37/37 records)
    "MapCloseEvent"  x17
    "MapOpenEvent"  x17
    "WaypointMoveEvent"  x2
    "WaypointSetEvent"  x1
data.featureUsed  (string, 37/37 records)
    "Map"  x34
    "Waypoint"  x3
data.location  (object, 3/37 records)
data.location.x  (number, 3/37 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 3/37 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 3/37 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationAnswerEvent` — 31 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (16); Unit 1 Dev (8); Unit 5 Dev (4); Unit 3 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 16.83s (p5 1.83s / p95 80312.93s, n=30)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 31/31 records)
    "submitAnswerEvent"  x31
data.answerSubmitted  (string, 31/31 records)
    17 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 31/31 records)
    "Unit 4 - Flooding"  x16
    "Unit 1 - Freshwater"  x6
    "Unit 5"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 3 - Pollution Upstream"  x2
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `WaterChamberEvent` — 30 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (30)
- **Intervals:** median 10.86s (p5 0.94s / p95 64.10s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "On"  x22
    "Off"  x8
data.floor  (string, 30/30 records)
    "4"  x15
    "3"  x8
    "2"  x5
    "1"  x2
data.machineNumber  (string, 30/30 records)
    "One"  x29
    "Two"  x1
data.machineType  (string, 30/30 records)
    "Condenser"  x16
    "Evaporator"  x11
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 30/30 records)
    "3"  x14
    "2"  x7
    "1"  x5
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowFocusEvent` — 29 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (4); Unit 1 Dev (3); Unit 4 Dev (1); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1532.57s (p5 44.02s / p95 85631.62s, n=28)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 29/29 records)
    true  x29
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 25 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 4 Dev (5); Unit 3 Dev (4); Unit 5 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1980.53s (p5 184.85s / p95 86991.78s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "DebugMenuStateChanged"  x25
data.isOpened  (bool, 25/25 records)
    false  x25
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 9287.09s (p5 153.38s / p95 112826.36s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 18 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2)
- **Intervals:** median 75.14s (p5 0.02s / p95 153351.56s, n=17)
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

### `gameWindowUnfocusEvent` — 12 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 1 Dev (3); Unit 4 Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 978.64s (p5 17.83s / p95 226898.79s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 12/12 records)
    false  x12
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `SolarStillDesignEvent` — 11 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (11)
- **Intervals:** median 1.49s (p5 0.53s / p95 4.04s, n=10)
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
    "Uncovered"  x1
data.designSelections.roofStyle  (string, 1/11 records)
    "Tilted Out"  x1
data.featureUsed  (string, 11/11 records)
    "RoofStyle"  x6
    "ExtraCovering"  x2
    "GlassRoofTemperature"  x2
    "Submit"  x1
data.selectedOption  (string, 10/11 records, 1 empty-string)
    "Tilted Out"  x3
    ""  x1
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
    "Uncovered"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 3 Dev (4)
- **Intervals:** median 3.63s (p5 1.55s / p95 117413.60s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x5
    "Open"  x3
data.toolName  (string, 8/8 records, 8 empty-string)
    ""  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 8 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (8)
- **Intervals:** median 1.60s (p5 1.13s / p95 22.96s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records, 5 empty-string)
    ""  x5
    "cameraPlaced"  x3
data.boxId  (string, 8/8 records)
    "0"  x4
    "1"  x2
    "2"  x2
data.soilType  (string, 8/8 records)
    "Clay"  x3
    "Sand"  x3
    "Gravel"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 45.76s (p5 2.55s / p95 158.97s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Clay"  x3
    "Gravel"  x3
    "Bedrock"  x1
    "Sand"  x1
data.floor  (string, 8/8 records)
    "4"  x4
    "5"  x3
    "3"  x1
data.machine  (string, 8/8 records)
    "1"  x7
    "2"  x1
data.row  (string, 8/8 records)
    "TopRow"  x7
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `EndOfUnit` — 5 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 70162.83s (p5 27859.93s / p95 382644.15s, n=4)
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

### `chatEvent` — 4 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (3); Unit 5 Dev (1)
- **Intervals:** median 10697.59s (p5 1480.25s / p95 39411.91s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x4
data.chatID  (string, 4/4 records)
    "NA"  x4
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationToolEvent` — 3 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (3)
- **Intervals:** median 77.64s (p5 10.54s / p95 144.75s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationToolOpen"  x2
    "argumentationToolClose"  x1
data.argumentationTitle  (string, 3/3 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x1
data.toolName  (string, 3/3 records)
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - "  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `ObjectInterEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (56 records)
- `TerasGardenBox` data.actionType: "" (5x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (2x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (14x)
- `soilMachine` data.canisterType: "Bedrock" (1x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*