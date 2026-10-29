# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba6

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a9439a8420a1e6b56ba6
- **Game version string(s) in log:** 2.8.4, 2.8.7, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9439a8420a1e6b56ba6.jsonl
- **Records:** 10161 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9439a8420a1e6b56ba6
- **Time span:** 2026-10-05T20:02:00.320000+00:00 .. 2026-10-19T16:10:31.036000+00:00 (332h 8m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba6\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **22 event types**, 10161 records, 11 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 92 INFO, 0 NOT_TESTED, 90 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2853 | 28.08 | 1 | 4 | 0 | 2026-10-06T19:51:52.283000+00:00 | 2026-10-16T16:03:46.197000+00:00 | 236h 11m |
| InputEvent | 2536 | 24.96 | 1 | 9 | 0 | 2026-10-05T20:02:46.654000+00:00 | 2026-10-19T16:09:45.522000+00:00 | 332h 6m |
| DialogueEvent | 2099 | 20.66 | 1 | 9 | 1306 | 2026-10-05T20:02:34.188000+00:00 | 2026-10-19T16:10:31.036000+00:00 | 332h 7m |
| PlayerPositionEvent | 1757 | 17.29 | 1 | 9 | 0 | 2026-10-05T20:02:13.842000+00:00 | 2026-10-19T16:10:27.031000+00:00 | 332h 8m |
| argumentationNodeEvent | 253 | 2.49 | 1 | 4 | 0 | 2026-10-06T19:41:14.140000+00:00 | 2026-10-15T19:50:51.801000+00:00 | 216h 9m |
| ObjectInterEvent | 236 | 2.32 | 1 | 9 | 0 | 2026-10-05T20:07:38.633000+00:00 | 2026-10-19T16:08:55.455000+00:00 | 332h 1m |
| questEvent | 87 | 0.86 | 1 | 9 | 87 | 2026-10-05T20:02:34.158000+00:00 | 2026-10-19T16:06:14.618000+00:00 | 332h 3m |
| TopographicMapEvent | 62 | 0.61 | 1 | 2 | 0 | 2026-10-06T19:52:20.710000+00:00 | 2026-10-14T16:07:28.093000+00:00 | 188h 15m |
| Soil Key Puzzle | 49 | 0.48 | 1 | 3 | 0 | 2026-10-06T20:00:09.452000+00:00 | 2026-10-14T19:38:16.126000+00:00 | 191h 38m |
| WaterChamberEvent | 44 | 0.43 | 1 | 1 | 0 | 2026-10-16T16:01:05.529000+00:00 | 2026-10-19T16:02:07.055000+00:00 | 72h 1m |
| DEBUGMenu | 40 | 0.39 | 1 | 9 | 0 | 2026-10-05T20:02:13.823000+00:00 | 2026-10-19T15:56:11.933000+00:00 | 331h 53m |
| gameWindowFocusEvent | 31 | 0.31 | 1 | 7 | 0 | 2026-10-05T20:02:00.320000+00:00 | 2026-10-19T16:10:28.916000+00:00 | 332h 8m |
| argumentationAnswerEvent | 26 | 0.26 | 1 | 4 | 0 | 2026-10-06T19:42:23.608000+00:00 | 2026-10-15T19:50:57.028000+00:00 | 216h 8m |
| gameWindowUnfocusEvent | 19 | 0.19 | 1 | 8 | 0 | 2026-10-05T20:02:50.685000+00:00 | 2026-10-19T16:10:26.414000+00:00 | 332h 7m |
| gameStartEvent | 18 | 0.18 | 1 | 1 | 0 | 2026-10-05T20:02:00.321000+00:00 | 2026-10-19T15:56:04.397000+00:00 | 331h 54m |
| argumentationEvent | 12 | 0.12 | 1 | 4 | 0 | 2026-10-06T19:42:07.190000+00:00 | 2026-10-15T19:50:57.093000+00:00 | 216h 8m |
| TerasGardenBox | 11 | 0.11 | 1 | 1 | 0 | 2026-10-15T19:57:14.368000+00:00 | 2026-10-15T19:58:44.635000+00:00 | 1m 30s |
| soilMachine | 11 | 0.11 | 1 | 1 | 0 | 2026-10-14T20:01:14.727000+00:00 | 2026-10-14T20:05:51.951000+00:00 | 4m 37s |
| chatEvent | 6 | 0.06 | 1 | 2 | 0 | 2026-10-15T20:09:49.574000+00:00 | 2026-10-19T16:03:23.682000+00:00 | 91h 53m |
| argumentationToolEvent | 5 | 0.05 | 1 | 1 | 0 | 2026-10-06T19:42:04.267000+00:00 | 2026-10-06T19:43:34.297000+00:00 | 1m 30s |
| EndOfUnit | 4 | 0.04 | 1 | 4 | 0 | 2026-10-06T19:46:54.542000+00:00 | 2026-10-15T20:09:24.607000+00:00 | 216h 22m |
| crash | 2 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 254155.798s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.247s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 12.616s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.036s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.767s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 20.08s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.031s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 15096.637s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 57692.613s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1924.084s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1403.267s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 9.814s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.3x vs baseline. 
  - Observed: 40 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up 
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
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,C,B,2,II; B,1,I; B,2,II; C,1,II; C,2,II; C,3,II; C,4,II; C,A,2,II; C,D,2,II; C,D,A,2,II; D,1,II; D,2,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
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
- **INFO / Info** `chatEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 6 records 
  - Expected: 2 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 45; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Guru of Arguments; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[144] _id=6ac4040dde269131f9af953b ts=2026-10-05T20:09:48.2270000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[6] _id=6ac40239de269131f9af8b5f ts=2026-10-05T20:02:00.3210000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[174] _id=6ac54b7bde269131f9b79e93 ts=2026-10-06T19:26:50.5420000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[602] _id=6ac55086de269131f9b7b954 ts=2026-10-06T19:48:21.8720000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 31 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 31} 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[3] _id=6ac40239de269131f9af8b5d ts=2026-10-05T20:02:00.3200000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[21] _id=6ac40271de269131f9af8ca5 ts=2026-10-05T20:02:56.2490000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[173] _id=6ac54b7bde269131f9b79e92 ts=2026-10-06T19:26:50.5410000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[20] _id=6ac4026cde269131f9af8c93 ts=2026-10-05T20:02:50.6850000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[171] _id=6ac54b7bde269131f9b79e8f ts=2026-10-05T20:11:22.459Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[1763] _id=6ac552bcde269131f9b7e1e1 ts=2026-10-06T19:57:47.2660000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 2852 | 0.0 | 0.036 | 298.147 | 1.899 | 433585.913 | 0.2 | 1519 | 11 |
| InputEvent | 2535 | 0.0 | 1.247 | 471.645 | 24.039 | 349850.668 | 0.13 | 87 | 16 |
| DialogueEvent | 2098 | 0.0 | 4.194 | 569.913 | 30.838 | 349658.389 | 0.11 | 607 | 14 |
| PlayerPositionEvent | 1745 | 9.719 | 10.002 | 482.447 | 10.264 | 243877.931 | 0.12 | 0 | 16 |
| argumentationNodeEvent | 252 | 0.007 | 0.759 | 3088.007 | 13.449 | 431552.398 | 0.02 | 18 | 3 |
| ObjectInterEvent | 235 | 0.0 | 12.616 | 5086.284 | 1952.302 | 430835.428 | 0.01 | 4 | 14 |
| questEvent | 86 | 0.001 | 193.688 | 13900.238 | 82852.21 | 349806.295 | 0.0 | 15 | 21 |
| TopographicMapEvent | 61 | 0.021 | 5.767 | 11109.957 | 72543.701 | 431558.926 | 0.01 | 3 | 7 |
| Soil Key Puzzle | 48 | 0.029 | 1.011 | 14372.639 | 85592.105 | 432458.919 | 0.0 | 1 | 4 |
| WaterChamberEvent | 43 | 0.266 | 10.586 | 6029.338 | 122.755 | 243939.34 | 0.01 | 0 | 2 |
| DEBUGMenu | 39 | 6.602 | 699.654 | 30636.875 | 102308.189 | 349622.404 | 0.0 | 0 | 21 |
| gameWindowFocusEvent | 30 | 4.293 | 1924.084 | 39856.953 | 173131.79 | 349622.56 | 0.0 | 0 | 19 |
| argumentationAnswerEvent | 25 | 0.76 | 20.08 | 31124.537 | 173772.772 | 431589.802 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 18 | 5.024 | 1403.267 | 66425.318 | 272534.15 | 429609.482 | 0.0 | 0 | 11 |
| gameStartEvent | 17 | 241.657 | 57692.613 | 70284.946 | 265149.645 | 349622.56 | 0.0 | 0 | 16 |
| argumentationEvent | 11 | 0.045 | 40.538 | 70739.082 | 302903.3 | 431552.761 | 0.0 | 2 | 3 |
| TerasGardenBox | 10 | 0.969 | 4.361 | 9.027 | 25.456 | 26.186 | 6.65 | 0 | 0 |
| soilMachine | 10 | 1.551 | 9.814 | 27.722 | 111.959 | 173.601 | 2.16 | 0 | 0 |
| chatEvent | 5 | 431.96 | 15096.637 | 66162.822 | 208137.669 | 244023.251 | 0.0 | 0 | 4 |
| argumentationToolEvent | 4 | 1.11 | 2.031 | 22.508 | 72.555 | 84.858 | 2.67 | 0 | 0 |
| EndOfUnit | 3 | 92748.526 | 254155.798 | 259650.022 | 414256.747 | 432045.741 | 0.0 | 0 | 3 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 11 group(s), 32 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[606] _id=6ac55094de269131f9b7b9e1 ts=2026-10-06T19:48:34.7120000Z == 6ab9a9439a8420a1e6b56ba6.jsonl[607] _id=6ac55094de269131f9b7b9e2 ts=2026-10-06T19:48:34.7120000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[2039] _id=6ac69f46de269131f9bf2226 ts=2026-10-07T19:36:35.2220000Z == 6ab9a9439a8420a1e6b56ba6.jsonl[2040] _id=6ac69f46de269131f9bf2227 ts=2026-10-07T19:36:35.2220000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[4295] _id=6ac9302ade269131f9cae14f ts=2026-10-09T18:19:20.4490000Z == 6ab9a9439a8420a1e6b56ba6.jsonl[4301] _id=6ac9302ade269131f9cae150 ts=2026-10-09T18:19:20.4490000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 64 group(s), 101 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[704] _id=6ac55160de269131f9b7c37a ts=2026-10-06T19:51:58.6750000Z == 6ab9a9439a8420a1e6b56ba6.jsonl[705] _id=6ac55160de269131f9b7c37b ts=2026-10-06T19:51:58.6750000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[687] _id=6ac55162de269131f9b7c397 ts=2026-10-06T19:51:58.9690000Z == 6ab9a9439a8420a1e6b56ba6.jsonl[688] _id=6ac55162de269131f9b7c39d ts=2026-10-06T19:51:58.9690000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[695] _id=6ac55162de269131f9b7c3a8 ts=2026-10-06T19:51:59.0250000Z == 6ab9a9439a8420a1e6b56ba6.jsonl[690] _id=6ac55163de269131f9b7c3aa ts=2026-10-06T19:51:59.0250000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a9439a8420a1e6b56ba6.jsonl[102] _id=6ac4038bde269131f9af91cf ts=2026-10-05T20:07:38.6330000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[103] _id=6ac4038bde269131f9af91d1 ts=2026-10-05T20:07:38.6380000Z`; `6ms: 6ab9a9439a8420a1e6b56ba6.jsonl[193] _id=6ac54bb0de269131f9b79f79 ts=2026-10-06T19:27:43.4720000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[194] _id=6ac54bb0de269131f9b79f7b ts=2026-10-06T19:27:43.4780000Z`; `308ms: 6ab9a9439a8420a1e6b56ba6.jsonl[272] _id=6ac54cdfde269131f9b7a341 ts=2026-10-06T19:32:46.6440000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[270] _id=6ac54cdfde269131f9b7a344 ts=2026-10-06T19:32:46.9520000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `644ms: 6ab9a9439a8420a1e6b56ba6.jsonl[4546] _id=6ace8a50de269131f9d218fa ts=2026-10-13T19:45:19.7300000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[4548] _id=6ace8a51de269131f9d218fe ts=2026-10-13T19:45:20.3740000Z`; `607ms: 6ab9a9439a8420a1e6b56ba6.jsonl[4548] _id=6ace8a51de269131f9d218fe ts=2026-10-13T19:45:20.3740000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[4547] _id=6ace8a51de269131f9d21902 ts=2026-10-13T19:45:20.9810000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `760ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8436] _id=6ad12d2ede269131f9e0b7bc ts=2026-10-15T19:44:45.4020000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[8439] _id=6ad12d2ede269131f9e0b7c8 ts=2026-10-15T19:44:46.1620000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `45ms: 6ab9a9439a8420a1e6b56ba6.jsonl[5266] _id=6ace8e47de269131f9d24386 ts=2026-10-13T20:02:15.0490000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[5269] _id=6ace8e47de269131f9d24389 ts=2026-10-13T20:02:15.0940000Z`; `49ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8662] _id=6ad12ea1de269131f9e0ccaa ts=2026-10-15T19:50:57.0440000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[8666] _id=6ad12ea1de269131f9e0ccae ts=2026-10-15T19:50:57.0930000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `373ms: 6ab9a9439a8420a1e6b56ba6.jsonl[424] _id=6ac54ee4de269131f9b7ad28 ts=2026-10-06T19:41:23.7350000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[429] _id=6ac54ee4de269131f9b7ad2e ts=2026-10-06T19:41:24.1080000Z`; `659ms: 6ab9a9439a8420a1e6b56ba6.jsonl[412] _id=6ac54ef1de269131f9b7adb4 ts=2026-10-06T19:41:36.7530000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[413] _id=6ac54ef2de269131f9b7adc0 ts=2026-10-06T19:41:37.4120000Z`; `281ms: 6ab9a9439a8420a1e6b56ba6.jsonl[4206] _id=6ac7f83ade269131f9c73ee4 ts=2026-10-08T20:08:25.9000000Z ~ 6ab9a9439a8420a1e6b56ba6.jsonl[4202] _id=6ac7f83ade269131f9c73eee ts=2026-10-08T20:08:26.1810000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 97h 7m 
  - Evidence: 97h 7m: 6ab9a9439a8420a1e6b56ba6.jsonl[4380] _id=6ac93109de269131f9cae654 ts=2026-10-09T18:23:04.4990000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4383] _id=6ace86bfde269131f9d1f1bb ts=2026-10-13T19:30:06.9030000Z; 67h 46m: 6ab9a9439a8420a1e6b56ba6.jsonl[9715] _id=6ad2846ade269131f9e7fe41 ts=2026-10-16T20:09:08.5800000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9778] _id=6ad63d95de269131f9e988af ts=2026-10-19T15:56:04.2390000Z; 24h 2m: 6ab9a9439a8420a1e6b56ba6.jsonl[2036] _id=6ac69f41de269131f9bf220c ts=2026-10-07T19:36:32.6360000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3465] _id=6ac7f164de269131f9c6ae87 ts=2026-10-08T19:39:15.5500000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 97h 7m 
  - Evidence: 97h 7m: 6ab9a9439a8420a1e6b56ba6.jsonl[4371] _id=6ac930fbde269131f9cae623 ts=2026-10-09T18:22:50.3600000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4411] _id=6ace86d5de269131f9d1f315 ts=2026-10-13T19:30:28.7490000Z; 67h 45m: 6ab9a9439a8420a1e6b56ba6.jsonl[9749] _id=6ad284bade269131f9e801ca ts=2026-10-16T20:10:33.1910000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9790] _id=6ad63da6de269131f9e988f2 ts=2026-10-19T15:56:21.6790000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba6.jsonl[3449] _id=6ac6a6dade269131f9bf89a1 ts=2026-10-07T20:08:56.8960000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3460] _id=6ac7f173de269131f9c6af6d ts=2026-10-08T19:39:29.5740000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 607 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8442] _id=6ad12d32de269131f9e0b7e4 ts=2026-10-15T19:44:49.5660000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8443] _id=6ad12d32de269131f9e0b7e5 ts=2026-10-15T19:44:49.5660000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8531] _id=6ad12dbede269131f9e0bf3a ts=2026-10-15T19:47:09.6680000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8532] _id=6ad12dbede269131f9e0bf3b ts=2026-10-15T19:47:09.6680000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8556] _id=6ad12e12de269131f9e0c40c ts=2026-10-15T19:48:33.8880000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8557] _id=6ad12e12de269131f9e0c40d ts=2026-10-15T19:48:33.8880000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6ab9a9439a8420a1e6b56ba6.jsonl[4377] _id=6ac930fbde269131f9cae621 ts=2026-10-09T18:22:50.3400000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[6349] _id=6acfc8a9de269131f9d70826 ts=2026-10-14T18:23:36.0810000Z; 70h 35m: 6ab9a9439a8420a1e6b56ba6.jsonl[598] _id=6ac5502fde269131f9b7b697 ts=2026-10-06T19:46:54.5420000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4377] _id=6ac930fbde269131f9cae621 ts=2026-10-09T18:22:50.3400000Z; 25h 45m: 6ab9a9439a8420a1e6b56ba6.jsonl[6349] _id=6acfc8a9de269131f9d70826 ts=2026-10-14T18:23:36.0810000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9047] _id=6ad132f5de269131f9e11cb2 ts=2026-10-15T20:09:24.6070000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 97h 10m 
  - Evidence: 97h 10m: 6ab9a9439a8420a1e6b56ba6.jsonl[4305] _id=6ac9302fde269131f9cae15e ts=2026-10-09T18:19:26.6430000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4386] _id=6ace86c9de269131f9d1f24c ts=2026-10-13T19:30:17.3110000Z; 67h 45m: 6ab9a9439a8420a1e6b56ba6.jsonl[9709] _id=6ad284f0de269131f9e803f4 ts=2026-10-16T20:11:27.0780000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9792] _id=6ad63db3de269131f9e98927 ts=2026-10-19T15:56:34.3210000Z; 23h 34m: 6ab9a9439a8420a1e6b56ba6.jsonl[3392] _id=6ac6a5fade269131f9bf77a7 ts=2026-10-07T20:05:12.9460000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3502] _id=6ac7f17bde269131f9c6b044 ts=2026-10-08T19:39:39.4880000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 87 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[2039] _id=6ac69f46de269131f9bf2226 ts=2026-10-07T19:36:35.2220000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2040] _id=6ac69f46de269131f9bf2227 ts=2026-10-07T19:36:35.2220000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[3881] _id=6ac7f57dde269131f9c6fa85 ts=2026-10-08T19:56:45.2970000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3882] _id=6ac7f57dde269131f9c6fa86 ts=2026-10-08T19:56:45.2970000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[3883] _id=6ac7f57dde269131f9c6fa87 ts=2026-10-08T19:56:45.2980000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3884] _id=6ac7f57dde269131f9c6fa88 ts=2026-10-08T19:56:45.2980000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 119h 40m 
  - Evidence: 119h 40m: 6ab9a9439a8420a1e6b56ba6.jsonl[4120] _id=6ac7f730de269131f9c728c3 ts=2026-10-08T20:03:59.8730000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4524] _id=6ace8a23de269131f9d217a4 ts=2026-10-13T19:44:35.3010000Z; 67h 45m: 6ab9a9439a8420a1e6b56ba6.jsonl[9769] _id=6ad284dfde269131f9e80331 ts=2026-10-16T20:11:11.0050000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9817] _id=6ad63dd1de269131f9e98a11 ts=2026-10-19T15:57:04.9110000Z; 23h 55m: 6ab9a9439a8420a1e6b56ba6.jsonl[3283] _id=6ac6a547de269131f9bf6e08 ts=2026-10-07T20:02:14.5390000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3869] _id=6ac7f5aede269131f9c6fdc0 ts=2026-10-08T19:57:34.3630000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.000s..0.005s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8293] _id=6ad12b9dde269131f9e098b5 ts=2026-10-15T19:38:05.0660000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8294] _id=6ad12b9dde269131f9e098b6 ts=2026-10-15T19:38:05.0660000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8343] _id=6ad12c63de269131f9e0abac ts=2026-10-15T19:41:23.0840000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8344] _id=6ad12c63de269131f9e0abad ts=2026-10-15T19:41:23.0840000Z; 5ms: 6ab9a9439a8420a1e6b56ba6.jsonl[102] _id=6ac4038bde269131f9af91cf ts=2026-10-05T20:07:38.6330000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[103] _id=6ac4038bde269131f9af91d1 ts=2026-10-05T20:07:38.6380000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 67h 44m 
  - Evidence: 67h 44m: 6ab9a9439a8420a1e6b56ba6.jsonl[9751] _id=6ad284f6de269131f9e8040f ts=2026-10-16T20:11:34.0090000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9783] _id=6ad63d9fde269131f9e988db ts=2026-10-19T15:56:11.9400000Z; 23h 30m: 6ab9a9439a8420a1e6b56ba6.jsonl[3454] _id=6ac6a6f1de269131f9bf8a6f ts=2026-10-07T20:09:20.1480000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3459] _id=6ac7f173de269131f9c6af6c ts=2026-10-08T19:39:26.5720000Z; 23h 26m: 6ab9a9439a8420a1e6b56ba6.jsonl[2025] _id=6ac5558cde269131f9b84d3f ts=2026-10-06T20:09:47.8530000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2037] _id=6ac69f46de269131f9bf2224 ts=2026-10-07T19:36:32.6600000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 120h 26m 
  - Evidence: 120h 26m: 6ab9a9439a8420a1e6b56ba6.jsonl[3516] _id=6ac7f190de269131f9c6b1d5 ts=2026-10-08T19:39:57.7120000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[5391] _id=6ace8f41de269131f9d24d77 ts=2026-10-13T20:06:23.6250000Z; 23h 57m: 6ab9a9439a8420a1e6b56ba6.jsonl[1817] _id=6ac552d7de269131f9b7eb93 ts=2026-10-06T19:58:13.5810000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2385] _id=6ac6a3c0de269131f9bf562f ts=2026-10-07T19:55:42.8360000Z; 23h 34m: 6ab9a9439a8420a1e6b56ba6.jsonl[3381] _id=6ac6a5e6de269131f9bf76d1 ts=2026-10-07T20:04:51.6760000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3470] _id=6ac7f173de269131f9c6af71 ts=2026-10-08T19:39:29.6430000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1519 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[1016] _id=6ac5520bde269131f9b7ceaa ts=2026-10-06T19:54:48.8500000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[1021] _id=6ac5520bde269131f9b7ceb2 ts=2026-10-06T19:54:48.8500000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[1025] _id=6ac5520cde269131f9b7cec2 ts=2026-10-06T19:54:49.7180000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[1026] _id=6ac5520cde269131f9b7cec3 ts=2026-10-06T19:54:49.7180000Z; 0ms: 6ab9a9439a8420a1e6b56ba6.jsonl[1028] _id=6ac5520cde269131f9b7cec5 ts=2026-10-06T19:54:50.6220000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[1000] _id=6ac5520dde269131f9b7cec9 ts=2026-10-06T19:54:50.6220000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 7m 
  - Evidence: 120h 7m: 6ab9a9439a8420a1e6b56ba6.jsonl[3922] _id=6ac7f5b8de269131f9c6fe6f ts=2026-10-08T19:57:44.3790000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[5357] _id=6ace8f04de269131f9d24b22 ts=2026-10-13T20:05:23.2980000Z; 24h 2m: 6ab9a9439a8420a1e6b56ba6.jsonl[2363] _id=6ac6a396de269131f9bf543e ts=2026-10-07T19:55:01.8860000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3919] _id=6ac7f5b7de269131f9c6fe61 ts=2026-10-08T19:57:43.1550000Z; 23h 54m: 6ab9a9439a8420a1e6b56ba6.jsonl[1851] _id=6ac5534dde269131f9b7fe26 ts=2026-10-06T20:00:12.2970000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2334] _id=6ac6a378de269131f9bf52a1 ts=2026-10-07T19:54:31.7210000Z
- **INFO / Info** `Soil Key Puzzle` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.029s..0.029s shown 
  - Evidence: 29ms: 6ab9a9439a8420a1e6b56ba6.jsonl[6464] _id=6acfda1fde269131f9d8ed26 ts=2026-10-14T19:38:06.4640000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[6465] _id=6acfda1fde269131f9d8ed2c ts=2026-10-14T19:38:06.4930000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a9439a8420a1e6b56ba6.jsonl[3794] _id=6ac7f44ade269131f9c6e6cf ts=2026-10-08T19:51:38.2230000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4520] _id=6ace8a11de269131f9d21722 ts=2026-10-13T19:44:17.1490000Z; 23h 52m: 6ab9a9439a8420a1e6b56ba6.jsonl[2249] _id=6ac6a23bde269131f9bf463e ts=2026-10-07T19:49:14.0800000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3604] _id=6ac7f1dede269131f9c6b7fb ts=2026-10-08T19:41:18.1260000Z; 23h 32m: 6ab9a9439a8420a1e6b56ba6.jsonl[1999] _id=6ac55519de269131f9b83fbc ts=2026-10-06T20:07:52.2470000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2102] _id=6ac6a021de269131f9bf25e0 ts=2026-10-07T19:40:16.6490000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.021s..0.032s shown 
  - Evidence: 21ms: 6ab9a9439a8420a1e6b56ba6.jsonl[2104] _id=6ac6a02ade269131f9bf2628 ts=2026-10-07T19:40:25.5720000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2108] _id=6ac6a02ade269131f9bf262c ts=2026-10-07T19:40:25.5930000Z; 24ms: 6ab9a9439a8420a1e6b56ba6.jsonl[1986] _id=6ac5550cde269131f9b83d32 ts=2026-10-06T20:07:39.0790000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[1990] _id=6ac5550cde269131f9b83d36 ts=2026-10-06T20:07:39.1030000Z; 32ms: 6ab9a9439a8420a1e6b56ba6.jsonl[2103] _id=6ac6a02ade269131f9bf2626 ts=2026-10-07T19:40:25.5400000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[2104] _id=6ac6a02ade269131f9bf2628 ts=2026-10-07T19:40:25.5720000Z
- **INFO / Info** `WaterChamberEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 67h 45m 
  - Evidence: 67h 45m: 6ab9a9439a8420a1e6b56ba6.jsonl[9766] _id=6ad284d2de269131f9e802e7 ts=2026-10-16T20:10:57.9910000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9797] _id=6ad63db6de269131f9e98933 ts=2026-10-19T15:56:37.3310000Z; 3h 59m: 6ab9a9439a8420a1e6b56ba6.jsonl[9681] _id=6ad24c74de269131f9e5a4f6 ts=2026-10-16T16:10:28.3760000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9729] _id=6ad28480de269131f9e7ff4a ts=2026-10-16T20:09:35.6470000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 53m 
  - Evidence: 119h 53m: 6ab9a9439a8420a1e6b56ba6.jsonl[4184] _id=6ac7f85dde269131f9c740ee ts=2026-10-08T20:09:01.7180000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[5262] _id=6ace8e44de269131f9d24368 ts=2026-10-13T20:02:11.5200000Z; 48h 24m: 6ab9a9439a8420a1e6b56ba6.jsonl[493] _id=6ac54f67de269131f9b7b129 ts=2026-10-06T19:43:34.4500000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4201] _id=6ac7f830de269131f9c73e0a ts=2026-10-08T20:08:15.9530000Z; 47h 42m: 6ab9a9439a8420a1e6b56ba6.jsonl[5264] _id=6ace8e47de269131f9d24384 ts=2026-10-13T20:02:15.0050000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8426] _id=6ad12d21de269131f9e0b6ef ts=2026-10-15T19:44:32.8530000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a9439a8420a1e6b56ba6.jsonl[4235] _id=6ac7f85ede269131f9c740f0 ts=2026-10-08T20:09:01.7500000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[5216] _id=6ace8e1fde269131f9d24292 ts=2026-10-13T20:01:34.5110000Z; 48h 24m: 6ab9a9439a8420a1e6b56ba6.jsonl[440] _id=6ac54f67de269131f9b7b12b ts=2026-10-06T19:43:34.4880000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4178] _id=6ac7f814de269131f9c73ba3 ts=2026-10-08T20:07:48.3270000Z; 47h 41m: 6ab9a9439a8420a1e6b56ba6.jsonl[5269] _id=6ace8e47de269131f9d24389 ts=2026-10-13T20:02:15.0940000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8401] _id=6ad12d02de269131f9e0b55c ts=2026-10-15T19:44:01.6070000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.045s..0.049s shown 
  - Evidence: 45ms: 6ab9a9439a8420a1e6b56ba6.jsonl[5266] _id=6ace8e47de269131f9d24386 ts=2026-10-13T20:02:15.0490000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[5269] _id=6ace8e47de269131f9d24389 ts=2026-10-13T20:02:15.0940000Z; 49ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8662] _id=6ad12ea1de269131f9e0ccaa ts=2026-10-15T19:50:57.0440000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8666] _id=6ad12ea1de269131f9e0ccae ts=2026-10-15T19:50:57.0930000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 119h 52m 
  - Evidence: 119h 52m: 6ab9a9439a8420a1e6b56ba6.jsonl[4234] _id=6ac7f85cde269131f9c740dd ts=2026-10-08T20:08:59.8380000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[5236] _id=6ace8e1cde269131f9d2427e ts=2026-10-13T20:01:32.2360000Z; 48h 24m: 6ab9a9439a8420a1e6b56ba6.jsonl[222] _id=6ac54f63de269131f9b7b119 ts=2026-10-06T19:43:29.7370000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4177] _id=6ac7f810de269131f9c73b72 ts=2026-10-08T20:07:44.5290000Z; 47h 41m: 6ab9a9439a8420a1e6b56ba6.jsonl[5260] _id=6ace8e42de269131f9d2435e ts=2026-10-13T20:02:09.8410000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8379] _id=6ad12cfede269131f9e0b53d ts=2026-10-15T19:43:58.2200000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.007s..0.022s shown 
  - Evidence: 7ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8516] _id=6ad12d9cde269131f9e0bce6 ts=2026-10-15T19:46:35.7270000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8517] _id=6ad12d9cde269131f9e0bce8 ts=2026-10-15T19:46:35.7340000Z; 11ms: 6ab9a9439a8420a1e6b56ba6.jsonl[8656] _id=6ad12e9bde269131f9e0cc2a ts=2026-10-15T19:50:50.3510000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[8658] _id=6ad12e9bde269131f9e0cc2c ts=2026-10-15T19:50:50.3620000Z; 22ms: 6ab9a9439a8420a1e6b56ba6.jsonl[449] _id=6ac54f16de269131f9b7aefc ts=2026-10-06T19:42:13.3600000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[450] _id=6ac54f16de269131f9b7aefd ts=2026-10-06T19:42:13.3820000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 67h 47m 
  - Evidence: 67h 47m: 6ab9a9439a8420a1e6b56ba6.jsonl[9713] _id=6ad28465de269131f9e7fe19 ts=2026-10-16T20:09:08.4710000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9789] _id=6ad63d9cde269131f9e988ce ts=2026-10-19T15:56:11.7220000Z; 17h 56m: 6ab9a9439a8420a1e6b56ba6.jsonl[9080] _id=6ad14d18de269131f9e1b88c ts=2026-10-15T22:00:56.4940000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9149] _id=6ad2496cde269131f9e56f64 ts=2026-10-16T15:57:31.8340000Z; 4h 11m: 6ab9a9439a8420a1e6b56ba6.jsonl[9149] _id=6ad2496cde269131f9e56f64 ts=2026-10-16T15:57:31.8340000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9713] _id=6ad28465de269131f9e7fe19 ts=2026-10-16T20:09:08.4710000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 97h 7m 
  - Evidence: 97h 7m: 6ab9a9439a8420a1e6b56ba6.jsonl[4381] _id=6ac93109de269131f9cae657 ts=2026-10-09T18:23:04.6870000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4385] _id=6ace86c0de269131f9d1f1c6 ts=2026-10-13T19:30:07.2470000Z; 67h 47m: 6ab9a9439a8420a1e6b56ba6.jsonl[9712] _id=6ad28455de269131f9e7fdfb ts=2026-10-16T20:08:52.9810000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9781] _id=6ad63d95de269131f9e988b2 ts=2026-10-19T15:56:04.3970000Z; 24h 2m: 6ab9a9439a8420a1e6b56ba6.jsonl[2035] _id=6ac69f35de269131f9bf21ef ts=2026-10-07T19:36:20.4160000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3467] _id=6ac7f164de269131f9c6ae8e ts=2026-10-08T19:39:15.7000000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 97h 7m 
  - Evidence: 97h 7m: 6ab9a9439a8420a1e6b56ba6.jsonl[4379] _id=6ac93109de269131f9cae656 ts=2026-10-09T18:23:04.6870000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4384] _id=6ace86c0de269131f9d1f1c5 ts=2026-10-13T19:30:07.2470000Z; 67h 45m: 6ab9a9439a8420a1e6b56ba6.jsonl[9743] _id=6ad284a6de269131f9e800fe ts=2026-10-16T20:10:13.6480000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9780] _id=6ad63d95de269131f9e988b1 ts=2026-10-19T15:56:04.3970000Z; 24h 2m: 6ab9a9439a8420a1e6b56ba6.jsonl[2034] _id=6ac69f35de269131f9bf21ee ts=2026-10-07T19:36:20.4160000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3466] _id=6ac7f164de269131f9c6ae8d ts=2026-10-08T19:39:15.7000000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 20m 
  - Evidence: 119h 20m: 6ab9a9439a8420a1e6b56ba6.jsonl[4288] _id=6ac93017de269131f9cae112 ts=2026-10-08T20:11:50.955Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4430] _id=6ace8731de269131f9d1f7a1 ts=2026-10-13T19:32:00.4370000Z; 68h 0m: 6ab9a9439a8420a1e6b56ba6.jsonl[9741] _id=6ad284a4de269131f9e800ea ts=2026-10-16T20:10:11.4400000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[10159] _id=6ad640f3de269131f9e9a519 ts=2026-10-19T16:10:26.4140000Z; 47h 50m: 6ab9a9439a8420a1e6b56ba6.jsonl[2032] _id=6ac69f35de269131f9bf21eb ts=2026-10-06T20:09:55.531Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4025] _id=6ac7f675de269131f9c71483 ts=2026-10-08T20:00:52.7510000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 97h 10m 
  - Evidence: 97h 10m: 6ab9a9439a8420a1e6b56ba6.jsonl[4374] _id=6ac930f4de269131f9cae5fc ts=2026-10-09T18:22:44.1270000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[4443] _id=6ace8763de269131f9d1f950 ts=2026-10-13T19:32:50.4220000Z; 67h 47m: 6ab9a9439a8420a1e6b56ba6.jsonl[9719] _id=6ad2846ade269131f9e7fe45 ts=2026-10-16T20:09:13.4800000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9784] _id=6ad63d9fde269131f9e988dc ts=2026-10-19T15:56:14.4540000Z; 23h 34m: 6ab9a9439a8420a1e6b56ba6.jsonl[3394] _id=6ac6a601de269131f9bf77e9 ts=2026-10-07T20:05:20.7310000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[3462] _id=6ac7f173de269131f9c6af6f ts=2026-10-08T19:39:29.6510000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 15 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6ab9a9439a8420a1e6b56ba6.jsonl[406] _id=6ac54ebade269131f9b7abe2 ts=2026-10-06T19:40:41.6460000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[407] _id=6ac54ebade269131f9b7abe3 ts=2026-10-06T19:40:41.6470000Z; 1ms: 6ab9a9439a8420a1e6b56ba6.jsonl[9896] _id=6ad63e5ade269131f9e98e1d ts=2026-10-19T15:59:20.7780000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[9897] _id=6ad63e5ade269131f9e98e1e ts=2026-10-19T15:59:20.7790000Z; 4ms: 6ab9a9439a8420a1e6b56ba6.jsonl[7203] _id=6acfde17de269131f9d93104 ts=2026-10-14T19:55:02.3800000Z -> 6ab9a9439a8420a1e6b56ba6.jsonl[7207] _id=6acfde17de269131f9d93108 ts=2026-10-14T19:55:02.3840000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[392] _id=6ac54ea7de269131f9b7ab93 ts=2026-10-06T19:40:22.8330000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[2190] _id=6ac6a17ade269131f9bf3bbe ts=2026-10-07T19:46:00.9480000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[3370] _id=6ac6a5dfde269131f9bf7689 ts=2026-10-07T20:04:46.2060000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[5269] _id=6ace8e47de269131f9d24389 ts=2026-10-13T20:02:15.0940000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[8666] _id=6ad12ea1de269131f9e0ccae ts=2026-10-15T19:50:57.0930000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[9055] _id=6ad1330ede269131f9e11ddf ts=2026-10-15T20:09:49.5740000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[9080] _id=6ad14d18de269131f9e1b88c ts=2026-10-15T22:00:56.4940000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[9149] _id=6ad2496cde269131f9e56f64 ts=2026-10-16T15:57:31.8340000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[9895] _id=6ad63e5ade269131f9e98e1c ts=2026-10-19T15:59:20.7470000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 2 records 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[6357] _id=6acfd849de269131f9d8be63 ts=?`; `6ab9a9439a8420a1e6b56ba6.jsonl[9714] _id=6ad2846ade269131f9e7fe3f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 103 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[2621] _id=6ac6a491de269131f9bf5fcc ts=2026-10-07T19:59:10.6780000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[2654] _id=6ac6a493de269131f9bf5ff8 ts=2026-10-07T19:59:12.5730000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[2655] _id=6ac6a493de269131f9bf5ffa ts=2026-10-07T19:59:12.6300000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 174 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[705] _id=6ac55160de269131f9b7c37b ts=2026-10-06T19:51:58.6750000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[687] _id=6ac55162de269131f9b7c397 ts=2026-10-06T19:51:58.9690000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[688] _id=6ac55162de269131f9b7c39d ts=2026-10-06T19:51:58.9690000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[492] _id=6ac54f66de269131f9b7b125 ts=2026-10-06T19:43:33.1870000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 23 unmatched 'DialogueStartEvent' (totals: 402 start, 391 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 11 unmatched 'BecameCameraCentered' (totals: 500 open, 489 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 20 unmatched 'BecameVisible' (totals: 942 open, 922 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 3 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 51 start, 36 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 253 of 10158 adjacent _id pairs reverse in client time; worst 103.4s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a9439a8420a1e6b56ba6.jsonl[736] _id=6ac551c0de269131f9b7c87f ts=2026-10-06T19:53:35.6660000Z`; `6ab9a9439a8420a1e6b56ba6.jsonl[737] _id=6ac551c1de269131f9b7c889 ts=2026-10-06T19:51:52.2830000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -1.01s, min -84385.87s, max -0.16s over 10159 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a9439a8420a1e6b56ba6\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=partial 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 2 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 2853 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (1852); Unit 4 Dev (550); Unit 5 Dev - Dungeon (253); Unit 3 Dungeon Dev (198)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.90s, n=2852)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2853/2853 records)
    "BecameVisible"  x942
    "BecameInvisible"  x922
    "BecameCameraCentered"  x500
    "BecameCameraUncentered"  x489
data.pieceId  (string, 2853/2853 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 2853/2853 records)
    1787 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2536 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (571); Unit 2 Prod (Refactor) (479); Unit 4 Dev - Dungeon (441); Unit 5 Dev - Dungeon (345); Unit 4 Dev (247); Unit 3 Dungeon Dev (242); Unit 1 Dev (106); Unit 5 Dev (56); Unit 4 Dev - Anderson Base (49)
- **Intervals:** median 1.25s (p5 0.12s / p95 24.04s, n=2535)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2536/2536 records)
    "pressed"  x2536
data.actionType  (string, 2536/2536 records)
    "Move"  x1705
    "Interact"  x345
    "Jump"  x287
    "Sprint"  x94
    "Ascend"  x51
    "Hoverboard"  x37
    "Map"  x7
    "Descend"  x5
    "Pause"  x4
    "ToggleDebug"  x1
data.key  (string, 2536/2536 records, 8 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2536/2536 records)
    "Player"  x1970
    "Drone"  x566
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2099 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (714); Unit 3 Dev (341); Unit 4 Dev (300); Unit 1 Dev (220); Unit 3 Dungeon Dev (148); Unit 4 Dev - Anderson Base (130); Unit 4 Dev - Dungeon (99); Unit 5 Dev - Dungeon (99); Unit 5 Dev (48)
- **eventKey:** present on 1306 of 2099 records
- **Intervals:** median 4.19s (p5 0.00s / p95 30.84s, n=2098)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1306; [conversationId, dialogueEventType] x793
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2099/2099 records)
    numeric range 8 .. 116 (50 unique)
data.dialogueEventType  (string, 2099/2099 records)
    "DialogueNodeEvent"  x1306
    "DialogueStartEvent"  x402
    "DialogueFinishEvent"  x391
data.nodeId  (number, 1306/2099 records)
    numeric range 0 .. 290 (229 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1757 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (532); Unit 4 Dev (279); Unit 3 Dev (235); Unit 1 Dev (174); Unit 5 Dev - Dungeon (154); Unit 4 Dev - Dungeon (150); Unit 3 Dungeon Dev (95); Unit 4 Dev - Anderson Base (95); Unit 5 Dev (43)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.26s, n=1745)
- **Fields under `data`:**

```text
data.position  (object, 1757/1757 records)
data.position.x  (number, 1757/1757 records)
    numeric range -655.373 .. 1555.54 (545 unique)
data.position.y  (number, 1757/1757 records)
    numeric range -115.127 .. 222.005 (396 unique)
data.position.z  (number, 1757/1757 records)
    numeric range -1041.41 .. 1806.6 (545 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 253 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (145); Unit 1 Dev (48); Unit 2 Prod (Refactor) (41); Unit 3 Dev (19)
- **Intervals:** median 0.76s (p5 0.04s / p95 13.45s, n=252)
- **Fields under `data`:**

```text
data.actionType  (string, 253/253 records)
    "argumentationNodeHoverEnd"  x105
    "argumentationNodeHoverStart"  x105
    "argumentationNodeAdd"  x30
    "argumentationNodeRemove"  x13
data.argumentationTitle  (string, 253/253 records)
    "Unit 4 - Flooding"  x145
    "Unit 2 – Watershed"  x41
    "Unit 1 - Argumentation Tutorial"  x29
    "Unit 1 - Freshwater"  x19
    "Unit 3 - Pollution Upstream"  x19
data.nodeName  (string, 253/253 records)
    "I"  x39
    "B"  x36
    "A"  x35
    "1"  x31
    "D"  x27
    "2"  x21
    "C"  x21
    "II"  x18
    "4"  x12
    "3"  x10
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 236 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (78); Unit 2 Prod (Refactor) (51); Unit 3 Dungeon Dev (32); Unit 4 Dev (21); Unit 1 Dev (15); Unit 5 Dev - Dungeon (15); Unit 3 Dev (11); Unit 4 Dev - Anderson Base (9); Unit 5 Dev (4)
- **Intervals:** median 12.62s (p5 1.80s / p95 1952.30s, n=235)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 236/236 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 236/236 records)
    106 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 87 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (18); Unit 1 Dev (15); Unit 5 Dev - Dungeon (15); Unit 4 Dev (14); Unit 3 Dev (10); Unit 4 Dev - Dungeon (9); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2); Unit 5 Dev (1)
- **eventKey:** present on 87 of 87 records
- **Intervals:** median 193.69s (p5 0.01s / p95 82852.21s, n=86)
- **`data` key-set variants:** [questEventType, questID, questName] x51; [questEventType, questID, questName, questSuccessOrFailure] x36
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 87/87 records)
    "questActiveEvent"  x51
    "questFinishEvent"  x36
data.questID  (string, 87/87 records)
    32 unique values (see csv/event_unique_values.csv)
data.questName  (string, 87/87 records)
    32 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 36/87 records)
    "Succeeded"  x36
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 62 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (35); Unit 3 Dev (27)
- **Intervals:** median 5.77s (p5 0.08s / p95 72543.70s, n=61)
- **`data` key-set variants:** [actionType, featureUsed] x38; [actionType, featureUsed, location] x24
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x19
    "WaypointMoveEvent"  x17
    "WaypointSetEvent"  x5
    "WaypointResetEvent"  x2
data.featureUsed  (string, 62/62 records)
    "Map"  x38
    "Waypoint"  x24
data.location  (object, 24/62 records)
data.location.x  (number, 24/62 records)
    numeric range -325.035 .. 629.576 (18 unique)
data.location.y  (number, 24/62 records)
    numeric range -294.264 .. 176.578 (19 unique)
data.location.z  (number, 24/62 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 49 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 3 Dev (12); Unit 4 Dev (10)
- **Intervals:** median 1.01s (p5 0.12s / p95 85592.11s, n=48)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x41; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/49 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/49 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 41/49 records)
    "RightDrag"  x24
    "LeftDrag"  x17
data.currentSoilType  (string, 41/49 records)
    "SAND"  x8
    "CLAY"  x7
    "CLAYROCK"  x7
    "CLAYSAND"  x7
    "SANDGRAVEL"  x6
    "BEDROCK"  x3
    "GRAVEL"  x3
data.isCorrectSelection  (string, 41/49 records)
    "false"  x33
    "true"  x8
data.waterLevelStatus  (string, 41/49 records)
    "Proper"  x18
    "TooHigh"  x17
    "TooLow"  x6
data.waterRetentionChange  (string, 41/49 records)
    "Increase"  x18
    "Decrease"  x15
    "NoChange"  x8
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `WaterChamberEvent` — 44 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (44)
- **Intervals:** median 10.59s (p5 1.61s / p95 122.76s, n=43)
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "On"  x30
    "Off"  x14
data.floor  (string, 44/44 records)
    "3"  x26
    "4"  x11
    "2"  x5
    "1"  x2
data.machineNumber  (string, 44/44 records)
    "One"  x42
    "Two"  x2
data.machineType  (string, 44/44 records)
    "Condenser"  x19
    "DualChamber_Evaporator"  x10
    "Evaporator"  x8
    "VentSwitch"  x4
    "DualChamber_Condenser"  x3
data.room  (string, 44/44 records)
    "2"  x20
    "1"  x10
    "3"  x10
    "4"  x4
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 40 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (17); Unit 4 Dev (5); Unit 5 Dev - Dungeon (5); Unit 2 Prod (Refactor) (4); Unit 3 Dev (3); Unit 1 Dev (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Anderson Base (1); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 699.65s (p5 7.68s / p95 102308.19s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "DebugMenuStateChanged"  x40
data.isOpened  (bool, 40/40 records)
    false  x40
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 31 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 5 Dev - Dungeon (5); Unit 2 Prod (Refactor) (3); Unit 3 Dev (2); Transition (1); Unit 1 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1924.08s (p5 27.08s / p95 173131.79s, n=30)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 31/31 records)
    true  x31
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `argumentationAnswerEvent` — 26 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (19); Unit 2 Prod (Refactor) (3); Unit 1 Dev (2); Unit 3 Dev (2)
- **Intervals:** median 20.08s (p5 2.11s / p95 173772.77s, n=25)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "submitAnswerEvent"  x26
data.answerSubmitted  (string, 26/26 records)
    15 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 26/26 records)
    "Unit 4 - Flooding"  x19
    "Unit 2 – Watershed"  x3
    "Unit 3 - Pollution Upstream"  x2
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 5 Dev - Dungeon (6); Unit 2 Prod (Refactor) (5); Unit 1 Dev (2); Unit 3 Dev (2); Transition (1); Unit 3 Dungeon Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 1403.27s (p5 17.21s / p95 272534.15s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 57692.61s (p5 1081.40s / p95 265149.64s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 40.54s (p5 0.05s / p95 302903.30s, n=11)
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
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 4.36s (p5 1.08s / p95 25.46s, n=10)
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records, 6 empty-string)
    ""  x6
    "cameraPlaced"  x5
data.boxId  (string, 11/11 records)
    "0"  x5
    "1"  x4
    "2"  x2
data.soilType  (string, 11/11 records)
    "Sand"  x6
    "Gravel"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 11 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (11)
- **Intervals:** median 9.81s (p5 1.62s / p95 111.96s, n=10)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "ChangeCanister"  x11
data.canisterType  (string, 11/11 records)
    "Bedrock"  x4
    "Clay"  x3
    "Gravel"  x2
    "Sand"  x2
data.floor  (string, 11/11 records)
    "5"  x9
    "4"  x2
data.machine  (string, 11/11 records)
    "1"  x9
    "2"  x2
data.row  (string, 11/11 records)
    "BottomRow"  x6
    "TopRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `chatEvent` — 6 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev - Dungeon (5); Unit 5 Dev (1)
- **Intervals:** median 15096.64s (p5 1678.95s / p95 208137.67s, n=5)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x6
data.chatID  (string, 6/6 records)
    "NA"  x6
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (5)
- **Intervals:** median 2.03s (p5 1.13s / p95 72.56s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x3
    "argumentationToolClose"  x2
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - "  x3
    "BackingInfoPanel - Argumentation"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 4 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 254155.80s (p5 108889.25s / p95 414256.75s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 4/4 records)
    "1"  x1
    "2"  x1
    "3"  x1
    "4"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 2 records

- **Scenes:** <missing sceneName> (2)
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
    "unit4"  x1
    "unit5"  x1
data.workspace  (string, 2/2 records)
    "mhs"  x2
```

Raw examples: `event_examples.json` -> `crash`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (27 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (17x); "WaypointResetEvent" (2x); "WaypointSetEvent" (5x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (24x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (13x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*