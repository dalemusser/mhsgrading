# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b2b

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6ab9a8e69a8420a1e6b56b2b
- **Game version string(s) in log:** 2.8.4, 20260914-, 20261005-12466, 20261016-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8e69a8420a1e6b56b2b.jsonl
- **Records:** 13813 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8e69a8420a1e6b56b2b
- **Time span:** 2026-10-05T16:32:57.782000+00:00 .. 2026-10-19T16:10:54.759000+00:00 (335h 37m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b2b\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 13813 records, 8 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 103 INFO, 2 NOT_TESTED, 83 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4850 | 35.11 | 1 | 3 | 0 | 2026-10-06T16:48:09.750000+00:00 | 2026-10-16T16:56:56.295000+00:00 | 240h 8m |
| InputEvent | 3934 | 28.48 | 1 | 7 | 0 | 2026-10-05T16:33:10.573000+00:00 | 2026-10-19T16:10:45.749000+00:00 | 335h 37m |
| DialogueEvent | 2031 | 14.7 | 1 | 7 | 1273 | 2026-10-05T16:33:27.040000+00:00 | 2026-10-19T16:10:48.947000+00:00 | 335h 37m |
| PlayerPositionEvent | 1972 | 14.28 | 1 | 7 | 0 | 2026-10-05T16:33:07.112000+00:00 | 2026-10-19T16:10:54.759000+00:00 | 335h 37m |
| ObjectInterEvent | 378 | 2.74 | 1 | 7 | 0 | 2026-10-05T16:39:41.775000+00:00 | 2026-10-19T16:10:46.926000+00:00 | 335h 31m |
| argumentationNodeEvent | 232 | 1.68 | 1 | 4 | 0 | 2026-10-05T16:57:33.225000+00:00 | 2026-10-19T16:05:11.667000+00:00 | 335h 7m |
| Soil Key Puzzle | 92 | 0.67 | 1 | 3 | 0 | 2026-10-13T16:35:30.201000+00:00 | 2026-10-16T16:18:52.824000+00:00 | 71h 43m |
| questEvent | 76 | 0.55 | 1 | 7 | 76 | 2026-10-05T16:33:27.012000+00:00 | 2026-10-19T16:08:21.984000+00:00 | 335h 34m |
| TopographicMapEvent | 75 | 0.54 | 1 | 2 | 0 | 2026-10-06T16:48:41.612000+00:00 | 2026-10-15T17:02:29.112000+00:00 | 216h 13m |
| DEBUGMenu | 40 | 0.29 | 1 | 8 | 0 | 2026-10-05T16:33:07.099000+00:00 | 2026-10-19T16:06:12.821000+00:00 | 335h 33m |
| gameWindowFocusEvent | 25 | 0.18 | 1 | 5 | 0 | 2026-10-05T16:32:57.782000+00:00 | 2026-10-19T15:58:35.493000+00:00 | 335h 25m |
| gameStartEvent | 18 | 0.13 | 1 | 1 | 0 | 2026-10-05T16:32:57.784000+00:00 | 2026-10-19T15:55:01.800000+00:00 | 335h 22m |
| soilMachine | 18 | 0.13 | 1 | 1 | 0 | 2026-10-16T16:41:30.690000+00:00 | 2026-10-16T16:51:50.693000+00:00 | 10m 20s |
| argumentationAnswerEvent | 16 | 0.12 | 1 | 4 | 0 | 2026-10-05T16:57:59.890000+00:00 | 2026-10-19T16:05:15.133000+00:00 | 335h 7m |
| gameWindowUnfocusEvent | 14 | 0.1 | 1 | 4 | 0 | 2026-10-05T17:04:35.868000+00:00 | 2026-10-19T15:58:33.838000+00:00 | 334h 53m |
| argumentationEvent | 12 | 0.09 | 1 | 4 | 0 | 2026-10-05T16:57:26.028000+00:00 | 2026-10-19T16:05:15.185000+00:00 | 335h 7m |
| argumentationToolEvent | 12 | 0.09 | 1 | 3 | 0 | 2026-10-05T16:57:25.904000+00:00 | 2026-10-15T16:30:24.867000+00:00 | 239h 32m |
| DaniEvent | 8 | 0.06 | 1 | 2 | 0 | 2026-10-08T16:39:19.405000+00:00 | 2026-10-16T16:25:57.972000+00:00 | 191h 46m |
| TerasGardenBox | 6 | 0.04 | 1 | 1 | 0 | 2026-10-19T16:09:47.524000+00:00 | 2026-10-19T16:10:16.018000+00:00 | 28.5s |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-10-05T17:02:26.774000+00:00 | 2026-10-15T20:59:43.989000+00:00 | 243h 57m |
| crash | 1 | 0.01 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 439118.608s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.284s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.095s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 0.746s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.695s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 24.31s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.879s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 17280.584s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 7990.724s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 16692.129s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.21s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.3x vs baseline. 
  - Observed: 40 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 8 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to Collect; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — baseline categorical value(s) not seen this build. 
  - Observed: Clay; Gravel; Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 16 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,I; A,2,II; A,C,2,II; B,1,I; B,2,II; C,1,I; C,2,II; C,A,2,II; D,2,II; D,4,II 
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
  - Observed: Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 1 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.0x vs baseline. 
  - Observed: 18 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 14 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 3.6x vs baseline. 
  - Observed: 18 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[218] _id=6ac3d367de269131f9adf3ab ts=2026-10-05T16:42:14.7660000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[317] _id=6ac3d491de269131f9ae1129 ts=2026-10-05T16:47:12.9880000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[339] _id=6ac3d4cede269131f9ae16c7 ts=2026-10-05T16:48:13.8310000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[13] _id=6ac3d13ade269131f9adca5f ts=2026-10-05T16:32:57.7840000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[668] _id=6ac3d87ade269131f9ae7039 ts=2026-10-05T17:03:53.7620000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[682] _id=6ac524c2de269131f9b527b3 ts=2026-10-06T16:41:37.8330000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[14] _id=6ac3d13ade269131f9adca5d ts=2026-10-05T16:32:57.7820000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[667] _id=6ac3d87ade269131f9ae7037 ts=2026-10-05T17:03:53.7600000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[681] _id=6ac524c2de269131f9b527b0 ts=2026-10-06T16:41:37.8310000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 14 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 14} 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[680] _id=6ac524c1de269131f9b527ab ts=2026-10-05T17:04:35.868Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[2808] _id=6ac6742fde269131f9bc8d9d ts=2026-10-06T17:04:24.869Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[5295] _id=6ace5d24de269131f9cf7bc8 ts=2026-10-08T16:45:59.82Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4849 | 0.0 | 0.095 | 178.29 | 2.697 | 517775.832 | 0.34 | 1693 | 9 |
| InputEvent | 3933 | 0.0 | 1.284 | 307.21 | 16.035 | 431235.279 | 0.2 | 80 | 13 |
| DialogueEvent | 2030 | 0.0 | 4.231 | 595.193 | 36.349 | 431244.288 | 0.1 | 591 | 12 |
| PlayerPositionEvent | 1960 | 0.0 | 10.002 | 581.353 | 10.142 | 431212.348 | 0.1 | 3 | 11 |
| ObjectInterEvent | 377 | 0.0 | 10.224 | 3203.886 | 292.791 | 517614.815 | 0.02 | 5 | 13 |
| argumentationNodeEvent | 231 | 0.019 | 0.468 | 5222.764 | 9.284 | 777044.975 | 0.01 | 33 | 3 |
| Soil Key Puzzle | 91 | 0.161 | 0.921 | 2837.391 | 10.591 | 172625.74 | 0.02 | 0 | 3 |
| questEvent | 75 | 0.002 | 204.894 | 16107.933 | 84840.212 | 432027.776 | 0.0 | 12 | 19 |
| TopographicMapEvent | 74 | 0.008 | 7.695 | 10519.291 | 30730.731 | 517416.537 | 0.01 | 4 | 7 |
| DEBUGMenu | 39 | 7.822 | 661.376 | 30973.993 | 101647.884 | 432161.694 | 0.0 | 0 | 20 |
| gameWindowFocusEvent | 24 | 46.8 | 7990.724 | 50314.071 | 217265.146 | 432171.986 | 0.0 | 0 | 15 |
| gameStartEvent | 17 | 223.764 | 17280.584 | 71019.06 | 278948.291 | 432171.985 | 0.0 | 0 | 15 |
| soilMachine | 17 | 0.687 | 3.21 | 36.471 | 143.73 | 164.386 | 1.65 | 0 | 0 |
| argumentationAnswerEvent | 15 | 1.828 | 24.31 | 80429.016 | 473899.31 | 777092.488 | 0.0 | 0 | 3 |
| gameWindowUnfocusEvent | 13 | 0.0 | 16692.129 | 92741.382 | 317127.988 | 431912.643 | 0.0 | 1 | 9 |
| argumentationEvent | 11 | 0.038 | 63.535 | 109679.014 | 560478.86 | 777032.212 | 0.0 | 2 | 3 |
| argumentationToolEvent | 11 | 0.082 | 1.879 | 78398.088 | 431128.174 | 777088.148 | 0.0 | 0 | 2 |
| DaniEvent | 7 | 2.152 | 8.183 | 98628.367 | 379993.703 | 432203.174 | 0.0 | 0 | 2 |
| TerasGardenBox | 5 | 0.486 | 0.746 | 5.699 | 14.031 | 14.542 | 10.53 | 0 | 0 |
| EndOfUnit | 2 | 100960.874 | 439118.608 | 439118.607 | 743460.568 | 777276.341 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 8 group(s), 19 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[4974] _id=6ac7c506de269131f9c42b70 ts=2026-10-08T16:29:56.3140000Z == 6ab9a8e69a8420a1e6b56b2b.jsonl[4975] _id=6ac7c506de269131f9c42b71 ts=2026-10-08T16:29:56.3140000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[8117] _id=6acff520de269131f9d97ccb ts=2026-10-14T21:33:19.3760000Z == 6ab9a8e69a8420a1e6b56b2b.jsonl[8118] _id=6acff520de269131f9d97ccc ts=2026-10-14T21:33:19.3760000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[8150] _id=6ad0f71bde269131f9dcea13 ts=2026-10-15T15:54:02.2080000Z == 6ab9a8e69a8420a1e6b56b2b.jsonl[8151] _id=6ad0f71bde269131f9dcea14 ts=2026-10-15T15:54:02.2080000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 76 group(s), 114 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[1070] _id=6ac526b3de269131f9b56443 ts=2026-10-06T16:49:37.5660000Z == 6ab9a8e69a8420a1e6b56b2b.jsonl[1078] _id=6ac526b3de269131f9b56447 ts=2026-10-06T16:49:37.5660000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1072] _id=6ac526b3de269131f9b56450 ts=2026-10-06T16:49:37.7690000Z == 6ab9a8e69a8420a1e6b56b2b.jsonl[1080] _id=6ac526b3de269131f9b56455 ts=2026-10-06T16:49:37.7690000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1092] _id=6ac526b4de269131f9b56469 ts=2026-10-06T16:49:47.3080000Z == 6ab9a8e69a8420a1e6b56b2b.jsonl[1086] _id=6ac526b4de269131f9b5646f ts=2026-10-06T16:49:47.3080000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 60 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[148] _id=6ac3d2cede269131f9ade909 ts=2026-10-05T16:39:41.7750000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[149] _id=6ac3d2cede269131f9ade90b ts=2026-10-05T16:39:41.7800000Z`; `543ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[774] _id=6ac52595de269131f9b53a27 ts=2026-10-06T16:45:09.2380000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[781] _id=6ac52595de269131f9b53a35 ts=2026-10-06T16:45:09.7810000Z`; `643ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[781] _id=6ac52595de269131f9b53a35 ts=2026-10-06T16:45:09.7810000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[782] _id=6ac52596de269131f9b53a50 ts=2026-10-06T16:45:10.4240000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 207 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `136ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[1084] _id=6ac526b3de269131f9b5644b ts=2026-10-06T16:49:37.5660000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[1071] _id=6ac526b3de269131f9b5644d ts=2026-10-06T16:49:37.7020000Z`; `67ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[1071] _id=6ac526b3de269131f9b5644d ts=2026-10-06T16:49:37.7020000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[1072] _id=6ac526b3de269131f9b56450 ts=2026-10-06T16:49:37.7690000Z`; `24ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[1080] _id=6ac526b3de269131f9b56455 ts=2026-10-06T16:49:37.7690000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[1081] _id=6ac526b3de269131f9b56459 ts=2026-10-06T16:49:37.7930000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `734ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13768] _id=6ad640cbde269131f9e9a34d ts=2026-10-19T16:09:47.5240000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[13761] _id=6ad640ccde269131f9e9a362 ts=2026-10-19T16:09:48.2580000Z`; `746ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13761] _id=6ad640ccde269131f9e9a362 ts=2026-10-19T16:09:48.2580000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[13772] _id=6ad640cdde269131f9e9a372 ts=2026-10-19T16:09:49.0040000Z`; `486ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13784] _id=6ad640d9de269131f9e9a3f2 ts=2026-10-19T16:10:00.9900000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[13785] _id=6ad640d9de269131f9e9a3f7 ts=2026-10-19T16:10:01.4760000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `88ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5138] _id=6ac7c6edde269131f9c468f6 ts=2026-10-08T16:38:04.8340000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[5143] _id=6ac7c6eede269131f9c46903 ts=2026-10-08T16:38:04.9220000Z`; `78ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5140] _id=6ac7c6eede269131f9c46900 ts=2026-10-08T16:38:04.8520000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[5145] _id=6ac7c6eede269131f9c46905 ts=2026-10-08T16:38:04.9300000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `38ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[8985] _id=6ad0ffa3de269131f9dd91cf ts=2026-10-15T16:30:27.2710000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[8988] _id=6ad0ffa3de269131f9dd91d2 ts=2026-10-15T16:30:27.3090000Z`; `38ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13643] _id=6ad63fbbde269131f9e99ab3 ts=2026-10-19T16:05:15.1470000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[13646] _id=6ad63fbbde269131f9e99ab6 ts=2026-10-19T16:05:15.1850000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `53ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[490] _id=6ac3d6fede269131f9ae4bd0 ts=2026-10-05T16:57:33.6400000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[505] _id=6ac3d6fede269131f9ae4bd6 ts=2026-10-05T16:57:33.6930000Z`; `21ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[504] _id=6ac3d700de269131f9ae4bfd ts=2026-10-05T16:57:35.6100000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[493] _id=6ac3d700de269131f9ae4bff ts=2026-10-05T16:57:35.6310000Z`; `937ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[515] _id=6ac3d70ede269131f9ae4d67 ts=2026-10-05T16:57:50.1280000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[513] _id=6ac3d70fde269131f9ae4d73 ts=2026-10-05T16:57:51.0650000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `585ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[8981] _id=6ad0ffa0de269131f9dd9193 ts=2026-10-15T16:30:23.5590000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[8982] _id=6ad0ffa0de269131f9dd91a1 ts=2026-10-15T16:30:24.1440000Z`; `723ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[8982] _id=6ad0ffa0de269131f9dd91a1 ts=2026-10-15T16:30:24.1440000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[8983] _id=6ad0ffa1de269131f9dd91ac ts=2026-10-15T16:30:24.8670000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[6892] _id=6ace98cdde269131f9d25cbe ts=2026-10-13T20:47:08.8240000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[6896] _id=6acfab9ade269131f9d54f52 ts=2026-10-13T20:47:08.824Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `687ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[12293] _id=6ad253c5de269131f9e60586 ts=2026-10-16T16:41:41.0170000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[12308] _id=6ad253c6de269131f9e60593 ts=2026-10-16T16:41:41.7040000Z`; `782ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[12606] _id=6ad255b4de269131f9e62369 ts=2026-10-16T16:49:55.9970000Z ~ 6ab9a8e69a8420a1e6b56b2b.jsonl[12609] _id=6ad255b5de269131f9e6237c ts=2026-10-16T16:49:56.7790000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 120h 2m 
  - Evidence: 120h 2m: 6ab9a8e69a8420a1e6b56b2b.jsonl[4971] _id=6ac7c502de269131f9c42b4e ts=2026-10-08T16:29:53.8760000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5296] _id=6ace5d24de269131f9cf7bd2 ts=2026-10-13T16:32:35.5700000Z; 66h 50m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13089] _id=6ad2915bde269131f9e82419 ts=2026-10-16T21:04:27.0910000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13288] _id=6ad63d56de269131f9e987a9 ts=2026-10-19T15:55:01.6630000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b2b.jsonl[2812] _id=6ac6743bde269131f9bc8e9b ts=2026-10-07T16:32:58.8290000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[4965] _id=6ac7c4f9de269131f9c42a9d ts=2026-10-08T16:29:43.7480000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 120h 3m 
  - Evidence: 120h 3m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5169] _id=6ac7c73bde269131f9c471ad ts=2026-10-08T16:39:22.4150000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5780] _id=6ace5f86de269131f9cfaa05 ts=2026-10-13T16:42:45.5890000Z; 71h 42m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5779] _id=6ace5f8ede269131f9cfaa9d ts=2026-10-13T16:42:53.7720000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[11823] _id=6ad25009de269131f9e5d023 ts=2026-10-16T16:25:45.3770000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5287] _id=6ac7c8acde269131f9c49807 ts=2026-10-08T16:45:30.9250000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5301] _id=6ace5d38de269131f9cf7caf ts=2026-10-13T16:32:55.2130000Z; 66h 47m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13262] _id=6ad29222de269131f9e826a6 ts=2026-10-16T21:07:45.9450000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13285] _id=6ad63d62de269131f9e987c9 ts=2026-10-19T15:55:14.0670000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b2b.jsonl[675] _id=6ac3d897de269131f9ae727c ts=2026-10-05T17:04:22.5210000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[678] _id=6ac524d0de269131f9b52843 ts=2026-10-06T16:41:52.4580000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 591 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13548] _id=6ad63f51de269131f9e996e7 ts=2026-10-19T16:03:29.7140000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13549] _id=6ad63f51de269131f9e996e8 ts=2026-10-19T16:03:29.7140000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13566] _id=6ad63f75de269131f9e99810 ts=2026-10-19T16:04:04.8510000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13567] _id=6ad63f75de269131f9e99811 ts=2026-10-19T16:04:04.8510000Z; 1ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13427] _id=6ad63fe6de269131f9e99c23 ts=2026-10-19T16:05:58.4590000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13428] _id=6ad63fe6de269131f9e99c24 ts=2026-10-19T16:05:58.4600000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 54m 
  - Evidence: 215h 54m: 6ab9a8e69a8420a1e6b56b2b.jsonl[581] _id=6ac3d823de269131f9ae697f ts=2026-10-05T17:02:26.7740000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7971] _id=6acfb45fde269131f9d612f4 ts=2026-10-14T16:57:03.1150000Z; 28h 2m: 6ab9a8e69a8420a1e6b56b2b.jsonl[7971] _id=6acfb45fde269131f9d612f4 ts=2026-10-14T16:57:03.1150000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[10281] _id=6ad13ec0de269131f9e149a9 ts=2026-10-15T20:59:43.9890000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 119h 47m 
  - Evidence: 119h 47m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5292] _id=6ac7c8c2de269131f9c49aad ts=2026-10-08T16:45:52.9410000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5308] _id=6ace5d44de269131f9cf7d53 ts=2026-10-13T16:33:08.2200000Z; 66h 47m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13270] _id=6ad29232de269131f9e826dc ts=2026-10-16T21:08:02.0350000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13291] _id=6ad63d5fde269131f9e987bd ts=2026-10-19T15:55:11.4080000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b2b.jsonl[671] _id=6ac3d88fde269131f9ae721b ts=2026-10-05T17:04:13.9250000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[684] _id=6ac524d0de269131f9b52841 ts=2026-10-06T16:41:50.6710000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 80 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[10214] _id=6ad13dfcde269131f9e1434c ts=2026-10-15T20:56:27.1420000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[10215] _id=6ad13dfcde269131f9e1434d ts=2026-10-15T20:56:27.1420000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[10215] _id=6ad13dfcde269131f9e1434d ts=2026-10-15T20:56:27.1420000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[10223] _id=6ad13dfcde269131f9e1434e ts=2026-10-15T20:56:27.1420000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[10223] _id=6ad13dfcde269131f9e1434e ts=2026-10-15T20:56:27.1420000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[10224] _id=6ad13dfcde269131f9e1434f ts=2026-10-15T20:56:27.1420000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 143h 46m 
  - Evidence: 143h 46m: 6ab9a8e69a8420a1e6b56b2b.jsonl[4583] _id=6ac677e3de269131f9bd311e ts=2026-10-07T16:48:35.3900000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5363] _id=6ace5dd3de269131f9cf864c ts=2026-10-13T16:35:30.2050000Z; 66h 49m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13261] _id=6ad29215de269131f9e8268c ts=2026-10-16T21:07:32.8470000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13325] _id=6ad63dbede269131f9e9897e ts=2026-10-19T15:56:46.4110000Z; 23h 51m: 6ab9a8e69a8420a1e6b56b2b.jsonl[6393] _id=6ace6122de269131f9cfc673 ts=2026-10-13T16:49:38.2100000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7410] _id=6acfb092de269131f9d5afaf ts=2026-10-14T16:40:50.0580000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13071] _id=6ad25907de269131f9e65f8a ts=2026-10-16T17:04:06.6950000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13072] _id=6ad25907de269131f9e65f8b ts=2026-10-16T17:04:06.6950000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13245] _id=6ad291ffde269131f9e82652 ts=2026-10-16T21:07:11.2040000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13246] _id=6ad291ffde269131f9e82653 ts=2026-10-16T21:07:11.2040000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13379] _id=6ad63e41de269131f9e98d3d ts=2026-10-19T15:58:57.4740000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13380] _id=6ad63e41de269131f9e98d3e ts=2026-10-19T15:58:57.4740000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 119h 46m 
  - Evidence: 119h 46m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5293] _id=6ac7c8c7de269131f9c49b03 ts=2026-10-08T16:45:57.9650000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5300] _id=6ace5d38de269131f9cf7cae ts=2026-10-13T16:32:50.3130000Z; 66h 46m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13287] _id=6ad63d55de269131f9e987a7 ts=2026-10-16T21:08:28.825Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13293] _id=6ad63d61de269131f9e987c4 ts=2026-10-19T15:55:11.4480000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b2b.jsonl[676] _id=6ac3d8a3de269131f9ae7339 ts=2026-10-05T17:04:34.4730000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[677] _id=6ac524cfde269131f9b52839 ts=2026-10-06T16:41:48.4080000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[11291] _id=6ad1421bde269131f9e16f10 ts=2026-10-15T21:14:03.4380000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[11296] _id=6ad24dd3de269131f9e5a9a6 ts=2026-10-15T21:14:03.438Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13096] _id=6ad2924dde269131f9e826f6 ts=2026-10-16T21:08:28.8250000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13287] _id=6ad63d55de269131f9e987a7 ts=2026-10-16T21:08:28.825Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5650] _id=6ace5f0fde269131f9cfa0ac ts=2026-10-13T16:40:46.5550000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5651] _id=6ace5f21de269131f9cfa206 ts=2026-10-13T16:40:46.555Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 143h 49m 
  - Evidence: 143h 49m: 6ab9a8e69a8420a1e6b56b2b.jsonl[4595] _id=6ac677e6de269131f9bd3173 ts=2026-10-07T16:48:35.4340000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5452] _id=6ace5e74de269131f9cf9419 ts=2026-10-13T16:38:11.2660000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b2b.jsonl[7733] _id=6acfb24bde269131f9d5d9c6 ts=2026-10-14T16:48:10.2830000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[9098] _id=6ad100d1de269131f9dda362 ts=2026-10-15T16:35:27.8560000Z; 23h 32m: 6ab9a8e69a8420a1e6b56b2b.jsonl[2807] _id=6ac6742fde269131f9bc8d9c ts=2026-10-06T17:04:24.087Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[2966] _id=6ac67572de269131f9bcc321 ts=2026-10-07T16:36:42.8620000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1693 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[1027] _id=6ac526aede269131f9b56391 ts=2026-10-06T16:48:10.5430000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[1038] _id=6ac526aede269131f9b5639a ts=2026-10-06T16:48:10.5430000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[1028] _id=6ac526b0de269131f9b563cd ts=2026-10-06T16:48:12.5230000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[1053] _id=6ac526b0de269131f9b563d5 ts=2026-10-06T16:48:12.5230000Z; 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[1029] _id=6ac526b0de269131f9b563e7 ts=2026-10-06T16:49:36.2090000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[1064] _id=6ac526b0de269131f9b563ef ts=2026-10-06T16:49:36.2090000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 57m 
  - Evidence: 47h 57m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5426] _id=6ace5e36de269131f9cf8ea6 ts=2026-10-13T16:37:09.8250000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[9080] _id=6ad10088de269131f9dd9f70 ts=2026-10-15T16:34:15.5650000Z; 19h 12m: 6ab9a8e69a8420a1e6b56b2b.jsonl[10362] _id=6ad1404ade269131f9e15680 ts=2026-10-15T21:06:18.2850000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[11368] _id=6ad24e5cde269131f9e5b17f ts=2026-10-16T16:18:36.0900000Z; 4h 31m: 6ab9a8e69a8420a1e6b56b2b.jsonl[9094] _id=6ad100a4de269131f9dda11d ts=2026-10-15T16:34:44.3720000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[10361] _id=6ad1403ade269131f9e155e1 ts=2026-10-15T21:06:02.1690000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 143h 43m 
  - Evidence: 143h 43m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5288] _id=6ac7c8adde269131f9c49830 ts=2026-10-08T16:45:32.0340000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7083] _id=6acfadd5de269131f9d579d5 ts=2026-10-14T16:29:08.5710000Z; 23h 47m: 6ab9a8e69a8420a1e6b56b2b.jsonl[1008] _id=6ac5267fde269131f9b55ef7 ts=2026-10-06T16:49:03.1860000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[2899] _id=6ac6752ede269131f9bcb314 ts=2026-10-07T16:37:01.8160000Z; 23h 32m: 6ab9a8e69a8420a1e6b56b2b.jsonl[4843] _id=6ac67a89de269131f9bd7293 ts=2026-10-07T16:59:53.3550000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5051] _id=6ac7c5abde269131f9c43b7f ts=2026-10-08T16:32:42.4510000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.008s..0.020s shown 
  - Evidence: 8ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5143] _id=6ac7c6eede269131f9c46903 ts=2026-10-08T16:38:04.9220000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5145] _id=6ac7c6eede269131f9c46905 ts=2026-10-08T16:38:04.9300000Z; 18ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5138] _id=6ac7c6edde269131f9c468f6 ts=2026-10-08T16:38:04.8340000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5140] _id=6ac7c6eede269131f9c46900 ts=2026-10-08T16:38:04.8520000Z; 20ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[4833] _id=6ac67a7cde269131f9bd7142 ts=2026-10-07T16:59:39.7530000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[4837] _id=6ac67a7cde269131f9bd7146 ts=2026-10-07T16:59:39.7730000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 51m 
  - Evidence: 215h 51m: 6ab9a8e69a8420a1e6b56b2b.jsonl[559] _id=6ac3d769de269131f9ae5663 ts=2026-10-05T16:59:21.2490000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7820] _id=6acfb2eede269131f9d5f373 ts=2026-10-14T16:50:53.7370000Z; 95h 32m: 6ab9a8e69a8420a1e6b56b2b.jsonl[8984] _id=6ad0ffa3de269131f9dd91cd ts=2026-10-15T16:30:27.2530000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13532] _id=6ad63f3ade269131f9e9960a ts=2026-10-19T16:03:06.6300000Z; 23h 38m: 6ab9a8e69a8420a1e6b56b2b.jsonl[7869] _id=6acfb339de269131f9d5fb26 ts=2026-10-14T16:52:09.0560000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[8984] _id=6ad0ffa3de269131f9dd91cd ts=2026-10-15T16:30:27.2530000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 50m 
  - Evidence: 215h 50m: 6ab9a8e69a8420a1e6b56b2b.jsonl[554] _id=6ac3d76ade269131f9ae5667 ts=2026-10-05T16:59:21.2690000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7767] _id=6acfb2b2de269131f9d5ea9f ts=2026-10-14T16:49:53.4810000Z; 95h 32m: 6ab9a8e69a8420a1e6b56b2b.jsonl[8988] _id=6ad0ffa3de269131f9dd91d2 ts=2026-10-15T16:30:27.3090000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13502] _id=6ad63f18de269131f9e994a6 ts=2026-10-19T16:02:32.8170000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b2b.jsonl[7878] _id=6acfb339de269131f9d5fb2a ts=2026-10-14T16:52:09.0730000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[8927] _id=6ad0ff64de269131f9dd8d13 ts=2026-10-15T16:29:23.7360000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.038s..0.038s shown 
  - Evidence: 38ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13643] _id=6ad63fbbde269131f9e99ab3 ts=2026-10-19T16:05:15.1470000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13646] _id=6ad63fbbde269131f9e99ab6 ts=2026-10-19T16:05:15.1850000Z; 38ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[8985] _id=6ad0ffa3de269131f9dd91cf ts=2026-10-15T16:30:27.2710000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[8988] _id=6ad0ffa3de269131f9dd91d2 ts=2026-10-15T16:30:27.3090000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 215h 50m 
  - Evidence: 215h 50m: 6ab9a8e69a8420a1e6b56b2b.jsonl[548] _id=6ac3d761de269131f9ae5543 ts=2026-10-05T16:59:12.4410000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7769] _id=6acfb2b6de269131f9d5eba6 ts=2026-10-14T16:49:57.4160000Z; 95h 32m: 6ab9a8e69a8420a1e6b56b2b.jsonl[8978] _id=6ad0ff96de269131f9dd90f4 ts=2026-10-15T16:30:13.8140000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13508] _id=6ad63f21de269131f9e9950d ts=2026-10-19T16:02:41.0370000Z; 23h 37m: 6ab9a8e69a8420a1e6b56b2b.jsonl[7877] _id=6acfb337de269131f9d5faf7 ts=2026-10-14T16:52:06.7860000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[8932] _id=6ad0ff68de269131f9dd8d72 ts=2026-10-15T16:29:28.2370000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 33 interval(s) ≤ 0.019s..0.022s shown 
  - Evidence: 19ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[8948] _id=6ad0ff83de269131f9dd8fa7 ts=2026-10-15T16:29:54.5860000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[8949] _id=6ad0ff83de269131f9dd8fab ts=2026-10-15T16:29:54.6050000Z; 21ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[504] _id=6ac3d700de269131f9ae4bfd ts=2026-10-05T16:57:35.6100000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[493] _id=6ac3d700de269131f9ae4bff ts=2026-10-05T16:57:35.6310000Z; 22ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[13507] _id=6ad63f23de269131f9e99524 ts=2026-10-19T16:02:43.3070000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13509] _id=6ad63f23de269131f9e99526 ts=2026-10-19T16:02:43.3290000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 215h 51m 
  - Evidence: 215h 51m: 6ab9a8e69a8420a1e6b56b2b.jsonl[558] _id=6ac3d769de269131f9ae5661 ts=2026-10-05T16:59:21.2390000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[7816] _id=6acfb2eade269131f9d5f2ef ts=2026-10-14T16:50:49.3870000Z; 23h 39m: 6ab9a8e69a8420a1e6b56b2b.jsonl[7816] _id=6acfb2eade269131f9d5f2ef ts=2026-10-14T16:50:49.3870000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[8979] _id=6ad0ff9ade269131f9dd912e ts=2026-10-15T16:30:17.5870000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 120h 2m 
  - Evidence: 120h 2m: 6ab9a8e69a8420a1e6b56b2b.jsonl[4967] _id=6ac7c4f9de269131f9c42a9f ts=2026-10-08T16:29:43.8960000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5298] _id=6ace5d24de269131f9cf7bd4 ts=2026-10-13T16:32:35.8810000Z; 66h 50m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13088] _id=6ad29153de269131f9e82413 ts=2026-10-16T21:04:19.4320000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13290] _id=6ad63d56de269131f9e987ab ts=2026-10-19T15:55:01.8000000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b2b.jsonl[2811] _id=6ac6742fde269131f9bc8da9 ts=2026-10-07T16:32:46.7650000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[4967] _id=6ac7c4f9de269131f9c42a9f ts=2026-10-08T16:29:43.8960000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 120h 2m 
  - Evidence: 120h 2m: 6ab9a8e69a8420a1e6b56b2b.jsonl[4966] _id=6ac7c4f9de269131f9c42a9e ts=2026-10-08T16:29:43.8950000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5297] _id=6ace5d24de269131f9cf7bd3 ts=2026-10-13T16:32:35.8810000Z; 66h 46m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13284] _id=6ad2924ede269131f9e826fa ts=2026-10-16T21:08:30.5340000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13289] _id=6ad63d56de269131f9e987aa ts=2026-10-19T15:55:01.8000000Z; 23h 56m: 6ab9a8e69a8420a1e6b56b2b.jsonl[2810] _id=6ac6742fde269131f9bc8da8 ts=2026-10-07T16:32:46.7650000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[4966] _id=6ac7c4f9de269131f9c42a9e ts=2026-10-08T16:29:43.8950000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 58m 
  - Evidence: 119h 58m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5295] _id=6ace5d24de269131f9cf7bc8 ts=2026-10-08T16:45:59.82Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5860] _id=6ace5ff1de269131f9cfb115 ts=2026-10-13T16:44:32.4630000Z; 66h 50m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13283] _id=6ad2924dde269131f9e826f8 ts=2026-10-16T21:08:28.9540000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13357] _id=6ad63e2ade269131f9e98c92 ts=2026-10-19T15:58:33.8380000Z; 47h 41m: 6ab9a8e69a8420a1e6b56b2b.jsonl[2808] _id=6ac6742fde269131f9bc8d9d ts=2026-10-06T17:04:24.869Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5295] _id=6ace5d24de269131f9cf7bc8 ts=2026-10-08T16:45:59.82Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[6892] _id=6ace98cdde269131f9d25cbe ts=2026-10-13T20:47:08.8240000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[6896] _id=6acfab9ade269131f9d54f52 ts=2026-10-13T20:47:08.824Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 120h 0m 
  - Evidence: 120h 0m: 6ab9a8e69a8420a1e6b56b2b.jsonl[5044] _id=6ac7c59cde269131f9c439a1 ts=2026-10-08T16:32:27.5220000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5303] _id=6ace5d38de269131f9cf7cb1 ts=2026-10-13T16:32:55.2980000Z; 66h 50m: 6ab9a8e69a8420a1e6b56b2b.jsonl[13103] _id=6ad2915dde269131f9e82420 ts=2026-10-16T21:04:28.3790000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[13296] _id=6ad63d61de269131f9e987c7 ts=2026-10-19T15:55:12.7720000Z; 23h 49m: 6ab9a8e69a8420a1e6b56b2b.jsonl[713] _id=6ac52529de269131f9b52eb3 ts=2026-10-06T16:43:21.6340000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[2815] _id=6ac6743ede269131f9bc8eee ts=2026-10-07T16:33:01.4270000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.002s..0.004s shown 
  - Evidence: 2ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[469] _id=6ac3d6a8de269131f9ae4355 ts=2026-10-05T16:56:07.4420000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[470] _id=6ac3d6a8de269131f9ae4357 ts=2026-10-05T16:56:07.4440000Z; 3ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5629] _id=6ace5f31de269131f9cfa321 ts=2026-10-13T16:41:20.1760000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5630] _id=6ace5f31de269131f9cfa322 ts=2026-10-13T16:41:20.1790000Z; 4ms: 6ab9a8e69a8420a1e6b56b2b.jsonl[5616] _id=6ace5f31de269131f9cfa320 ts=2026-10-13T16:41:20.1720000Z -> 6ab9a8e69a8420a1e6b56b2b.jsonl[5629] _id=6ace5f31de269131f9cfa321 ts=2026-10-13T16:41:20.1760000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[453] _id=6ac3d691de269131f9ae40fb ts=2026-10-05T16:55:44.8010000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[564] _id=6ac3d77fde269131f9ae58b0 ts=2026-10-05T16:59:42.2860000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[6474] _id=6ace6203de269131f9cfd5d7 ts=2026-10-13T16:53:22.8310000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 57 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[1101] _id=6ac526bbde269131f9b5655c ts=2026-10-06T16:50:00.3460000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1102] _id=6ac526bbde269131f9b56563 ts=2026-10-06T16:50:00.9940000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1125] _id=6ac526bbde269131f9b56569 ts=2026-10-06T16:50:00.9950000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 94 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[1043] _id=6ac526afde269131f9b563c7 ts=2026-10-06T16:48:11.8670000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1066] _id=6ac526b1de269131f9b563fb ts=2026-10-06T16:49:36.3060000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1056] _id=6ac526b1de269131f9b56417 ts=2026-10-06T16:49:36.6520000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[8988] _id=6ad0ffa3de269131f9dd91d2 ts=2026-10-15T16:30:27.3090000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[13646] _id=6ad63fbbde269131f9e99ab6 ts=2026-10-19T16:05:15.1850000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[505] _id=6ac3d6fede269131f9ae4bd6 ts=2026-10-05T16:57:33.6930000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[493] _id=6ac3d700de269131f9ae4bff ts=2026-10-05T16:57:35.6310000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[11941] _id=6ad250dcde269131f9e5dd80 ts=2026-10-16T16:29:16.0450000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 1 records 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[10286] _id=6ad13eedde269131f9e14b5f ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 398 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[1149] _id=6ac526c7de269131f9b566cd ts=2026-10-06T16:50:13.3520000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1187] _id=6ac526d8de269131f9b56895 ts=2026-10-06T16:50:31.4880000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1213] _id=6ac526e2de269131f9b569a1 ts=2026-10-06T16:50:41.8150000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 742 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[1050] _id=6ac526afde269131f9b563b7 ts=2026-10-06T16:48:10.7480000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1054] _id=6ac526b0de269131f9b563de ts=2026-10-06T16:48:12.5230000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1086] _id=6ac526b4de269131f9b5646f ts=2026-10-06T16:49:47.3080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[551] _id=6ac3d767de269131f9ae5611 ts=2026-10-05T16:59:18.9010000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[553] _id=6ac3d768de269131f9ae5638 ts=2026-10-05T16:59:19.9660000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[8981] _id=6ad0ffa0de269131f9dd9193 ts=2026-10-15T16:30:23.5590000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 20 unmatched 'DialogueStartEvent' (totals: 384 start, 374 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 47 unmatched 'BecameCameraCentered' (totals: 925 open, 935 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 94 unmatched 'BecameVisible' (totals: 1495 open, 1495 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 6 unmatched 'argumentationToolOpen' (totals: 9 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 25 unmatched 'questActiveEvent' (totals: 50 start, 26 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 480 of 13811 adjacent _id pairs reverse in client time; worst 99.1s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6ab9a8e69a8420a1e6b56b2b.jsonl[1023] _id=6ac526adde269131f9b56361 ts=2026-10-06T16:49:48.8600000Z`; `6ab9a8e69a8420a1e6b56b2b.jsonl[1030] _id=6ac526aede269131f9b56375 ts=2026-10-06T16:48:09.7500000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.65s, min -431196.48s, max -0.11s over 13812 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6ab9a8e69a8420a1e6b56b2b\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 1 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4850 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3518); Unit 4 Dev (1054); Unit 3 Dungeon Dev (278)
- **Intervals:** median 0.10s (p5 0.00s / p95 2.70s, n=4849)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4850/4850 records)
    "BecameInvisible"  x1495
    "BecameVisible"  x1495
    "BecameCameraUncentered"  x935
    "BecameCameraCentered"  x925
data.pieceId  (string, 4850/4850 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4850/4850 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3934 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (1680); Unit 4 Dev - Dungeon (576); Unit 3 Dev (568); Unit 4 Dev - Anderson Base (331); Unit 4 Dev (317); Unit 3 Dungeon Dev (251); Unit 1 Dev (211)
- **Intervals:** median 1.28s (p5 0.15s / p95 16.03s, n=3933)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3934/3934 records)
    "pressed"  x3934
data.actionType  (string, 3934/3934 records)
    "Move"  x2987
    "Interact"  x631
    "Jump"  x146
    "Hoverboard"  x60
    "Ascend"  x41
    "Descend"  x26
    "Sprint"  x24
    "Map"  x15
    "ToggleDebug"  x3
    "Pause"  x1
data.key  (string, 3934/3934 records, 14 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3934/3934 records)
    "Player"  x2911
    "Drone"  x1023
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2031 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (813); Unit 3 Dev (442); Unit 4 Dev (212); Unit 1 Dev (197); Unit 4 Dev - Anderson Base (137); Unit 3 Dungeon Dev (126); Unit 4 Dev - Dungeon (104)
- **eventKey:** present on 1273 of 2031 records
- **Intervals:** median 4.23s (p5 0.00s / p95 36.35s, n=2030)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1273; [conversationId, dialogueEventType] x758
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2031/2031 records)
    numeric range 8 .. 114 (44 unique)
data.dialogueEventType  (string, 2031/2031 records)
    "DialogueNodeEvent"  x1273
    "DialogueStartEvent"  x384
    "DialogueFinishEvent"  x374
data.nodeId  (number, 1273/2031 records)
    numeric range 0 .. 290 (228 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 1972 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (865); Unit 3 Dev (340); Unit 4 Dev (192); Unit 4 Dev - Dungeon (187); Unit 1 Dev (176); Unit 4 Dev - Anderson Base (110); Unit 3 Dungeon Dev (102)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.14s, n=1960)
- **Fields under `data`:**

```text
data.position  (object, 1972/1972 records)
data.position.x  (number, 1972/1972 records)
    numeric range -694.272 .. 1553.72 (750 unique)
data.position.y  (number, 1972/1972 records)
    numeric range -114.326 .. 158.037 (449 unique)
data.position.z  (number, 1972/1972 records)
    numeric range -1041.75 .. 2072.75 (748 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 378 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (187); Unit 4 Dev - Dungeon (88); Unit 3 Dungeon Dev (41); Unit 4 Dev (18); Unit 4 Dev - Anderson Base (18); Unit 3 Dev (16); Unit 1 Dev (10)
- **Intervals:** median 10.22s (p5 0.22s / p95 292.79s, n=377)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 378/378 records)
    37 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 378/378 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 232 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (85); Unit 2 Prod (Refactor) (77); Unit 1 Dev (35); Unit 3 Dev (35)
- **Intervals:** median 0.47s (p5 0.03s / p95 9.28s, n=231)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 232/232 records)
    "argumentationNodeHoverEnd"  x98
    "argumentationNodeHoverStart"  x96
    "argumentationNodeAdd"  x26
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 232/232 records)
    "Unit 4 - Flooding"  x85
    "Unit 2 – Watershed"  x77
    "Unit 3 - Pollution Upstream"  x35
    "Unit 1 - Argumentation Tutorial"  x24
    "Unit 1 - Freshwater"  x11
data.nodeName  (string, 232/232 records)
    "A"  x46
    "C"  x39
    "B"  x28
    "D"  x27
    "1"  x21
    "II"  x20
    "I"  x19
    "3"  x12
    "4"  x10
    "2"  x7
    "5"  x3
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 92 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (56); Unit 4 Dev (20); Unit 3 Dev (16)
- **Intervals:** median 0.92s (p5 0.18s / p95 10.59s, n=91)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x84; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/92 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/92 records)
    "Unit 4 Dev"  x4
    "Unit 2 Prod (Refactor)"  x2
    "Unit 3 Dev"  x2
data.actionType  (string, 84/92 records)
    "RightDrag"  x45
    "LeftDrag"  x39
data.currentSoilType  (string, 84/92 records)
    "CLAY"  x19
    "CLAYSAND"  x16
    "SAND"  x15
    "CLAYROCK"  x14
    "SANDGRAVEL"  x12
    "BEDROCK"  x4
    "GRAVEL"  x4
data.isCorrectSelection  (string, 84/92 records)
    "false"  x64
    "true"  x20
data.waterLevelStatus  (string, 84/92 records)
    "TooHigh"  x38
    "Proper"  x35
    "TooLow"  x11
data.waterRetentionChange  (string, 84/92 records)
    "Increase"  x42
    "Decrease"  x22
    "NoChange"  x20
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 76 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (29); Unit 3 Dev (15); Unit 1 Dev (12); Unit 4 Dev - Dungeon (8); Unit 4 Dev (6); Unit 4 Dev - Anderson Base (4); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 76 of 76 records
- **Intervals:** median 204.89s (p5 0.00s / p95 84840.21s, n=75)
- **`data` key-set variants:** [questEventType, questID, questName] x50; [questEventType, questID, questName, questSuccessOrFailure] x26
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 76/76 records)
    "questActiveEvent"  x50
    "questFinishEvent"  x26
data.questID  (string, 76/76 records)
    26 unique values (see csv/event_unique_values.csv)
data.questName  (string, 76/76 records)
    26 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 26/76 records)
    "Succeeded"  x26
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 75 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (40); Unit 2 Prod (Refactor) (35)
- **Intervals:** median 7.70s (p5 0.06s / p95 30730.73s, n=74)
- **`data` key-set variants:** [actionType, featureUsed] x58; [actionType, featureUsed, location] x17
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 75/75 records)
    "MapCloseEvent"  x29
    "MapOpenEvent"  x29
    "WaypointMoveEvent"  x12
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x1
data.featureUsed  (string, 75/75 records)
    "Map"  x58
    "Waypoint"  x17
data.location  (object, 17/75 records)
data.location.x  (number, 17/75 records)
    numeric range -319.575 .. 133.291 (16 unique)
data.location.y  (number, 17/75 records)
    numeric range -360.537 .. 185.013 (16 unique)
data.location.z  (number, 17/75 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 40 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** MainMenu (15); Unit 2 Prod (Refactor) (8); Unit 3 Dev (6); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 4 Dev - Dungeon (2); Unit 1 Dev (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 661.38s (p5 9.45s / p95 101647.88s, n=39)
- **Fields under `data`:**

```text
data.actionType  (string, 40/40 records)
    "DebugMenuStateChanged"  x40
data.isOpened  (bool, 40/40 records)
    false  x40
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (18); Unit 2 Prod (Refactor) (3); Unit 4 Dev - Anderson Base (2); Unit 3 Dev (1); Unit 4 Dev (1)
- **Intervals:** median 7990.72s (p5 85.95s / p95 217265.15s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 18 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (18)
- **Intervals:** median 17280.58s (p5 451.83s / p95 278948.29s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 18 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (18)
- **Intervals:** median 3.21s (p5 0.76s / p95 143.73s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "ChangeCanister"  x18
data.canisterType  (string, 18/18 records)
    "Clay"  x6
    "Gravel"  x5
    "Bedrock"  x4
    "Sand"  x3
data.floor  (string, 18/18 records)
    "3"  x6
    "4"  x6
    "5"  x6
data.machine  (string, 18/18 records)
    "1"  x17
    "2"  x1
data.row  (string, 18/18 records)
    "TopRow"  x14
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationAnswerEvent` — 16 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (9); Unit 2 Prod (Refactor) (4); Unit 1 Dev (2); Unit 3 Dev (1)
- **Intervals:** median 24.31s (p5 7.90s / p95 473899.31s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "submitAnswerEvent"  x16
data.answerSubmitted  (string, 16/16 records)
    14 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 16/16 records)
    "Unit 4 - Flooding"  x9
    "Unit 2 – Watershed"  x4
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 14 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (2); Unit 4 Dev - Anderson Base (2); Unit 4 Dev (1)
- **Intervals:** median 16692.13s (p5 31.56s / p95 317127.99s, n=13)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 14/14 records)
    false  x14
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 63.53s (p5 0.04s / p95 560478.86s, n=11)
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

### `argumentationToolEvent` — 12 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (4); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 1.88s (p5 0.33s / p95 431128.17s, n=11)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationToolOpen"  x9
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Freshwater"  x5
    "Unit 3 - Pollution Upstream"  x4
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 2 – Watershed"  x1
data.toolName  (string, 12/12 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Watershed Graph"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 8 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 2 Prod (Refactor) (4); Unit 4 Dev - Dungeon (4)
- **Intervals:** median 8.18s (p5 2.15s / p95 379993.70s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "Close"  x4
    "Open"  x4
data.toolName  (string, 8/8 records, 8 empty-string)
    ""  x8
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `TerasGardenBox` — 6 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (6)
- **Intervals:** median 0.75s (p5 0.54s / p95 14.03s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "cameraPlaced"  x6
data.boxId  (string, 6/6 records)
    "0"  x3
    "1"  x2
    "2"  x1
data.soilType  (string, 6/6 records)
    "None"  x6
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1)
- **Intervals:** median 439118.61s (p5 134776.65s / p95 743460.57s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "2"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 1 records

- **Scenes:** <missing sceneName> (1)
- **Fields under `data`:**

```text
data.isPWA  (bool, 1/1 records)
    true  x1
data.message  (string, 1/1 records)
    "The root document of this element is not valid for pointer lock."  x1
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
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : median interval between records changed substantially
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (56 records)
- `TerasGardenBox` data.soilType: "None" (6x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (12x); "WaypointResetEvent" (1x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (17x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (4x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*