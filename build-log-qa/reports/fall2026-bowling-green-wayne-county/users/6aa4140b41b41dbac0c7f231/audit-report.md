# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f231

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f231
- **Game version string(s) in log:** 2.8.1, 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f231.jsonl
- **Records:** 17097 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f231
- **Time span:** 2026-09-22T14:14:35.493000+00:00 .. 2026-10-06T14:13:09.954000+00:00 (335h 58m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f231\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **24 event types**, 17097 records, 11 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 110 INFO, 0 NOT_TESTED, 98 PASS.
- Top items needing attention:
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially
  - WARNING/Medium `chatEvent`: median interval between records changed substantially
  - WARNING/Medium `gameStartEvent`: median interval between records changed substantially
  - WARNING/Medium `gameWindowFocusEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5272 | 30.84 | 1 | 4 | 0 | 2026-09-24T13:51:37.585000+00:00 | 2026-10-06T14:09:59.213000+00:00 | 288h 18m |
| InputEvent | 5221 | 30.54 | 1 | 9 | 0 | 2026-09-23T13:54:00.533000+00:00 | 2026-10-06T14:13:01.848000+00:00 | 312h 19m |
| DialogueEvent | 2474 | 14.47 | 1 | 9 | 1512 | 2026-09-23T13:54:17.310000+00:00 | 2026-10-06T14:12:03.290000+00:00 | 312h 17m |
| PlayerPositionEvent | 2061 | 12.05 | 1 | 9 | 0 | 2026-09-23T13:53:55.451000+00:00 | 2026-10-06T14:13:01.811000+00:00 | 312h 19m |
| argumentationNodeEvent | 760 | 4.45 | 1 | 4 | 0 | 2026-09-23T14:28:28.089000+00:00 | 2026-10-05T14:16:42.052000+00:00 | 287h 48m |
| ObjectInterEvent | 515 | 3.01 | 1 | 9 | 0 | 2026-09-23T14:03:17.763000+00:00 | 2026-10-06T13:58:48.717000+00:00 | 311h 55m |
| TopographicMapEvent | 187 | 1.09 | 1 | 3 | 0 | 2026-09-24T13:52:44.659000+00:00 | 2026-10-06T14:12:08.938000+00:00 | 288h 19m |
| Soil Key Puzzle | 112 | 0.66 | 1 | 3 | 0 | 2026-09-24T13:58:55.918000+00:00 | 2026-10-06T13:58:51.721000+00:00 | 287h 59m |
| questEvent | 109 | 0.64 | 1 | 9 | 109 | 2026-09-23T13:54:17.288000+00:00 | 2026-10-06T14:09:57.043000+00:00 | 312h 15m |
| soilMachine | 63 | 0.37 | 1 | 1 | 0 | 2026-09-28T14:24:12.393000+00:00 | 2026-09-29T14:06:33.992000+00:00 | 23h 42m |
| gameWindowFocusEvent | 51 | 0.3 | 1 | 7 | 0 | 2026-09-22T14:14:35.493000+00:00 | 2026-10-06T14:13:09.954000+00:00 | 335h 58m |
| DaniEvent | 38 | 0.22 | 1 | 2 | 0 | 2026-09-24T14:08:39.174000+00:00 | 2026-10-01T14:13:21.791000+00:00 | 168h 4m |
| WaterChamberEvent | 36 | 0.21 | 1 | 1 | 0 | 2026-09-30T14:03:05.463000+00:00 | 2026-09-30T14:12:45.333000+00:00 | 9m 39s |
| gameWindowUnfocusEvent | 36 | 0.21 | 1 | 7 | 0 | 2026-09-22T14:14:39.731000+00:00 | 2026-10-06T14:09:18.988000+00:00 | 335h 54m |
| argumentationAnswerEvent | 35 | 0.2 | 1 | 4 | 0 | 2026-09-24T13:42:10.832000+00:00 | 2026-10-05T14:16:47.992000+00:00 | 264h 34m |
| DEBUGMenu | 26 | 0.15 | 1 | 8 | 0 | 2026-09-23T13:53:55.446000+00:00 | 2026-10-06T14:09:56.375000+00:00 | 312h 16m |
| gameStartEvent | 23 | 0.13 | 1 | 1 | 0 | 2026-09-22T14:14:35.494000+00:00 | 2026-10-06T14:09:45.340000+00:00 | 335h 55m |
| SolarStillDesignEvent | 22 | 0.13 | 1 | 1 | 0 | 2026-09-30T14:26:11.463000+00:00 | 2026-10-01T13:49:15.164000+00:00 | 23h 23m |
| TerasGardenBox | 17 | 0.1 | 1 | 1 | 0 | 2026-09-30T13:45:30.758000+00:00 | 2026-09-30T13:49:55.722000+00:00 | 4m 24s |
| argumentationToolEvent | 16 | 0.09 | 1 | 3 | 0 | 2026-09-24T13:41:41.220000+00:00 | 2026-10-05T14:16:13.992000+00:00 | 264h 34m |
| argumentationEvent | 12 | 0.07 | 1 | 4 | 0 | 2026-09-24T13:41:46.638000+00:00 | 2026-10-05T14:16:48.097000+00:00 | 264h 35m |
| chatEvent | 5 | 0.03 | 1 | 3 | 0 | 2026-09-28T13:55:31.584000+00:00 | 2026-10-01T13:44:44.427000+00:00 | 71h 49m |
| EndOfUnit | 3 | 0.02 | 1 | 3 | 0 | 2026-09-24T13:47:30.910000+00:00 | 2026-10-01T13:55:14.126000+00:00 | 168h 7m |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 302631.608s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — median interval between records changed substantially. 
  - Observed: 2.03s median 
  - Expected: 4.06s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.431s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 12.79s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.961s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 42780.63s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 989.659s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 382.471s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 2.915s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 38 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E to Plant Seed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to pick up; Press E to place glyph 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` — record volume changed 5.5x vs baseline. 
  - Observed: 22 records 
  - Expected: 4 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Hot; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TerasGardenBox` `data.soilType` — categorical value(s) not seen in baseline. 
  - Observed: None 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 150 ft; 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 7.0x vs baseline. 
  - Observed: 35 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,2,II; B,2,II; B,4,I; B,C,2,II; B,C,A,2,II; B,C,D,1,II; B,D,1,I; B,D,1,II; B,D,2,II; C,2,II; C,A,2,II; C,D,3,II; D,B,1,II; D,C,3,2,II; D,C,A,4,II; D,C,B,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 5.4x vs baseline. 
  - Observed: 760 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Argumentation 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [11-29, 11-230, 11-27, 11-27, 11-29] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 23 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 54; 55 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Leader of Evidence; Part of a Balanced Ecosystem 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 12.6x vs baseline. 
  - Observed: 63 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 40 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[593] _id=6ab3de40485cab4c954d01ab ts=2026-09-23T14:12:16.9290000Z`; `6aa4140b41b41dbac0c7f231.jsonl[642] _id=6ab3df3d485cab4c954d0ad7 ts=2026-09-23T14:16:29.9010000Z`; `6aa4140b41b41dbac0c7f231.jsonl[674] _id=6ab3dfc9485cab4c954d11c9 ts=2026-09-23T14:18:49.2880000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[13759] _id=6ac3aaf5de269131f9a9dee6 ts=2026-10-05T13:49:39.2320000Z`; `6aa4140b41b41dbac0c7f231.jsonl[16972] _id=6ac50135de269131f9b26098 ts=2026-10-06T14:09:56.9900000Z`; `6aa4140b41b41dbac0c7f231.jsonl[16984] _id=6ac50135de269131f9b2609a ts=2026-10-06T14:09:57.0400000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[12] _id=6ab28d4b485cab4c9548c9d6 ts=2026-09-22T14:14:35.4940000Z`; `6aa4140b41b41dbac0c7f231.jsonl[19] _id=6ab3d9e9485cab4c954ce273 ts=2026-09-23T13:53:45.4630000Z`; `6aa4140b41b41dbac0c7f231.jsonl[533] _id=6ab3dd9d485cab4c954cfde9 ts=2026-09-23T14:09:33.5390000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 51 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 51} 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[11] _id=6ab28d4b485cab4c9548c9d4 ts=2026-09-22T14:14:35.4930000Z`; `6aa4140b41b41dbac0c7f231.jsonl[22] _id=6ab3d9e9485cab4c954ce271 ts=2026-09-23T13:53:45.4620000Z`; `6aa4140b41b41dbac0c7f231.jsonl[532] _id=6ab3dd9d485cab4c954cfde7 ts=2026-09-23T14:09:33.5380000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 36 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 36} 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[13] _id=6ab28d4f485cab4c9548c9d8 ts=2026-09-22T14:14:39.7310000Z`; `6aa4140b41b41dbac0c7f231.jsonl[865] _id=6ab3e211485cab4c954d2bb6 ts=2026-09-23T14:28:33.2650000Z`; `6aa4140b41b41dbac0c7f231.jsonl[884] _id=6ab3e22d485cab4c954d2cff ts=2026-09-23T14:29:01.3010000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 51 of 187 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1172] _id=6ab52b2c485cab4c95519ea5 ts=2026-09-24T13:52:44.6590000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1374] _id=6ab52b5d485cab4c9551a063 ts=2026-09-24T13:53:33.2290000Z`; `6aa4140b41b41dbac0c7f231.jsonl[2987] _id=6ab52e65485cab4c9551d0af ts=2026-09-24T14:06:29.6820000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5271 | 0.0 | 0.027 | 196.908 | 1.144 | 346321.88 | 0.3 | 3326 | 9 |
| InputEvent | 5220 | 0.0 | 0.857 | 215.391 | 11.975 | 343107.928 | 0.28 | 212 | 8 |
| DialogueEvent | 2473 | 0.001 | 3.551 | 454.616 | 28.154 | 343134.992 | 0.13 | 730 | 8 |
| PlayerPositionEvent | 2047 | 4.804 | 9.999 | 549.03 | 10.35 | 343096.499 | 0.11 | 0 | 9 |
| argumentationNodeEvent | 759 | 0.001 | 0.331 | 1365.078 | 5.691 | 434218.38 | 0.04 | 156 | 4 |
| ObjectInterEvent | 514 | 0.001 | 4.686 | 2184.691 | 215.348 | 343471.302 | 0.03 | 4 | 12 |
| TopographicMapEvent | 186 | 0.013 | 2.342 | 5580.453 | 430.806 | 345452.114 | 0.01 | 6 | 8 |
| Soil Key Puzzle | 111 | 0.135 | 1.035 | 9340.503 | 12.133 | 346159.471 | 0.01 | 0 | 5 |
| questEvent | 108 | 0.001 | 177.974 | 10408.701 | 83627.714 | 343233.792 | 0.01 | 23 | 15 |
| soilMachine | 62 | 0.382 | 2.915 | 1376.477 | 117.971 | 84269.02 | 0.04 | 0 | 1 |
| gameWindowFocusEvent | 50 | 1.51 | 382.471 | 24190.289 | 86391.059 | 343067.338 | 0.0 | 0 | 20 |
| DaniEvent | 37 | 0.002 | 2.572 | 16353.584 | 119989.574 | 260042.481 | 0.0 | 4 | 4 |
| WaterChamberEvent | 35 | 0.829 | 5.431 | 16.568 | 61.722 | 88.502 | 3.62 | 0 | 0 |
| gameWindowUnfocusEvent | 35 | 0.154 | 166.643 | 34550.836 | 196568.896 | 345012.166 | 0.0 | 0 | 12 |
| argumentationAnswerEvent | 34 | 0.589 | 12.79 | 28014.034 | 206931.095 | 434276.812 | 0.0 | 0 | 3 |
| DEBUGMenu | 25 | 70.618 | 896.316 | 44966.437 | 222804.055 | 345151.051 | 0.0 | 0 | 18 |
| gameStartEvent | 22 | 70.115 | 989.659 | 54968.629 | 248306.407 | 345137.721 | 0.0 | 0 | 16 |
| SolarStillDesignEvent | 21 | 0.236 | 1.266 | 4008.748 | 4.535 | 84153.192 | 0.01 | 0 | 1 |
| TerasGardenBox | 16 | 0.285 | 2.03 | 16.56 | 59.517 | 170.728 | 3.62 | 0 | 0 |
| argumentationToolEvent | 15 | 0.464 | 3.961 | 63498.185 | 458317.925 | 520545.063 | 0.0 | 0 | 2 |
| argumentationEvent | 11 | 0.025 | 92.657 | 86591.042 | 432871.107 | 434202.289 | 0.0 | 1 | 3 |
| chatEvent | 4 | 3.843 | 42780.63 | 64638.211 | 159739.467 | 172987.741 | 0.0 | 0 | 3 |
| EndOfUnit | 2 | 86218.326 | 302631.608 | 302631.608 | 497403.562 | 519044.89 | 0.0 | 0 | 2 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 4 group(s), 4 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[7481] _id=6abbc2f0485cab4c957e0877 ts=2026-09-29T13:53:52.2080000Z == 6aa4140b41b41dbac0c7f231.jsonl[7493] _id=6abbc2f0485cab4c957e0879 ts=2026-09-29T13:53:52.2080000Z`; `6aa4140b41b41dbac0c7f231.jsonl[8209] _id=6abbc645485cab4c957e5bbb ts=2026-09-29T14:08:05.0460000Z == 6aa4140b41b41dbac0c7f231.jsonl[8210] _id=6abbc645485cab4c957e5bbf ts=2026-09-29T14:08:05.0460000Z`; `6aa4140b41b41dbac0c7f231.jsonl[9354] _id=6abd1239485cab4c958918fd ts=2026-09-30T13:44:24.2410000Z == 6aa4140b41b41dbac0c7f231.jsonl[9355] _id=6abd1239485cab4c95891901 ts=2026-09-30T13:44:24.2410000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 205 group(s), 298 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1444] _id=6ab52b94485cab4c9551a409 ts=2026-09-24T13:51:38.0060000Z == 6aa4140b41b41dbac0c7f231.jsonl[1466] _id=6ab52b94485cab4c9551a40b ts=2026-09-24T13:51:38.0060000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1284] _id=6ab52af5485cab4c95519bdb ts=2026-09-24T13:51:48.2710000Z == 6aa4140b41b41dbac0c7f231.jsonl[1285] _id=6ab52af5485cab4c95519bdd ts=2026-09-24T13:51:48.2710000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1312] _id=6ab52b03485cab4c95519c5f ts=2026-09-24T13:52:02.6450000Z == 6aa4140b41b41dbac0c7f231.jsonl[1303] _id=6ab52b04485cab4c95519c61 ts=2026-09-24T13:52:02.6450000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 109 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `6ms: 6aa4140b41b41dbac0c7f231.jsonl[170] _id=6ab3dc25485cab4c954cf19f ts=2026-09-23T14:03:17.7630000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[168] _id=6ab3dc25485cab4c954cf1a1 ts=2026-09-23T14:03:17.7690000Z`; `783ms: 6aa4140b41b41dbac0c7f231.jsonl[227] _id=6ab3dccf485cab4c954cf661 ts=2026-09-23T14:06:07.8130000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[235] _id=6ab3dcd0485cab4c954cf669 ts=2026-09-23T14:06:08.5960000Z`; `360ms: 6aa4140b41b41dbac0c7f231.jsonl[235] _id=6ab3dcd0485cab4c954cf669 ts=2026-09-23T14:06:08.5960000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[229] _id=6ab3dcd0485cab4c954cf66d ts=2026-09-23T14:06:08.9560000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 622 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `33ms: 6aa4140b41b41dbac0c7f231.jsonl[1264] _id=6ab52af5485cab4c95519bd7 ts=2026-09-24T13:51:48.2050000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[1265] _id=6ab52af5485cab4c95519bd9 ts=2026-09-24T13:51:48.2380000Z`; `33ms: 6aa4140b41b41dbac0c7f231.jsonl[1265] _id=6ab52af5485cab4c95519bd9 ts=2026-09-24T13:51:48.2380000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[1284] _id=6ab52af5485cab4c95519bdb ts=2026-09-24T13:51:48.2710000Z`; `275ms: 6aa4140b41b41dbac0c7f231.jsonl[1285] _id=6ab52af5485cab4c95519bdd ts=2026-09-24T13:51:48.2710000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[1286] _id=6ab52af5485cab4c95519be1 ts=2026-09-24T13:51:48.5460000Z`
- **INFO / Info** `TerasGardenBox` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `285ms: 6aa4140b41b41dbac0c7f231.jsonl[9432] _id=6abd1297485cab4c95892db3 ts=2026-09-30T13:45:59.9050000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[9429] _id=6abd1298485cab4c95892dbf ts=2026-09-30T13:46:00.1900000Z`; `930ms: 6aa4140b41b41dbac0c7f231.jsonl[9516] _id=6abd136a485cab4c95894e99 ts=2026-09-30T13:49:30.0480000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[9534] _id=6abd136b485cab4c95894ea3 ts=2026-09-30T13:49:30.9780000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa4140b41b41dbac0c7f231.jsonl[2991] _id=6ab52e6c485cab4c9551d0e7 ts=2026-09-24T14:06:36.6850000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[2994] _id=6ab52e6d485cab4c9551d0ef ts=2026-09-24T14:06:36.7020000Z`; `208ms: 6aa4140b41b41dbac0c7f231.jsonl[4314] _id=6ab6856c485cab4c95564a3c ts=2026-09-25T14:30:03.5500000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[4297] _id=6ab6856d485cab4c95564a43 ts=2026-09-25T14:30:03.7580000Z`; `17ms: 6aa4140b41b41dbac0c7f231.jsonl[12284] _id=6abe69df485cab4c95a7a5cb ts=2026-10-01T14:10:38.9330000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[12287] _id=6abe69df485cab4c95a7a5d5 ts=2026-10-01T14:10:38.9500000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `589ms: 6aa4140b41b41dbac0c7f231.jsonl[1076] _id=6ab52948485cab4c95516943 ts=2026-09-24T13:44:40.1780000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[1075] _id=6ab52948485cab4c95516959 ts=2026-09-24T13:44:40.7670000Z`; `613ms: 6aa4140b41b41dbac0c7f231.jsonl[1075] _id=6ab52948485cab4c95516959 ts=2026-09-24T13:44:40.7670000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[1078] _id=6ab52949485cab4c9551697b ts=2026-09-24T13:44:41.3800000Z`; `764ms: 6aa4140b41b41dbac0c7f231.jsonl[8813] _id=6abbc9b5485cab4c957ea97b ts=2026-09-29T14:22:45.6750000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[8812] _id=6abbc9b6485cab4c957ea995 ts=2026-09-29T14:22:46.4390000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `25ms: 6aa4140b41b41dbac0c7f231.jsonl[9226] _id=6abbcb08485cab4c957ecf8f ts=2026-09-29T14:28:24.1580000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[9230] _id=6abbcb08485cab4c957ecf9b ts=2026-09-29T14:28:24.1830000Z`; `74ms: 6aa4140b41b41dbac0c7f231.jsonl[14962] _id=6ac3b150de269131f9ab270f ts=2026-10-05T14:16:48.0230000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[14966] _id=6ac3b150de269131f9ab272f ts=2026-10-05T14:16:48.0970000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 150 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `789ms: 6aa4140b41b41dbac0c7f231.jsonl[864] _id=6ab3e214485cab4c954d2bf7 ts=2026-09-23T14:28:36.2190000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[875] _id=6ab3e214485cab4c954d2c03 ts=2026-09-23T14:28:37.0080000Z`; `385ms: 6aa4140b41b41dbac0c7f231.jsonl[866] _id=6ab3e216485cab4c954d2c1d ts=2026-09-23T14:28:38.0700000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[876] _id=6ab3e216485cab4c954d2c27 ts=2026-09-23T14:28:38.4550000Z`; `97ms: 6aa4140b41b41dbac0c7f231.jsonl[867] _id=6ab3e216485cab4c954d2c23 ts=2026-09-23T14:28:38.3890000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[877] _id=6ab3e216485cab4c954d2c2b ts=2026-09-23T14:28:38.4860000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `559ms: 6aa4140b41b41dbac0c7f231.jsonl[10857] _id=6abd1aa6485cab4c958af32e ts=2026-09-30T14:20:22.6510000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[10858] _id=6abd1aa7485cab4c958af33c ts=2026-09-30T14:20:23.2100000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `154ms: 6aa4140b41b41dbac0c7f231.jsonl[884] _id=6ab3e22d485cab4c954d2cff ts=2026-09-23T14:29:01.3010000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[4476] _id=6aba6f91485cab4c95681ac1 ts=2026-09-23T14:29:01.455Z`; `394ms: 6aa4140b41b41dbac0c7f231.jsonl[16962] _id=6ac5010ede269131f9b25f3a ts=2026-10-06T14:09:18.5940000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[16968] _id=6ac5010fde269131f9b25f46 ts=2026-10-06T14:09:18.9880000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 6aa4140b41b41dbac0c7f231.jsonl[10928] _id=6abd1b04485cab4c958b0450 ts=2026-09-30T14:21:56.5450000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[10926] _id=6abd1b04485cab4c958b0456 ts=2026-09-30T14:21:56.5460000Z`; `4ms: 6aa4140b41b41dbac0c7f231.jsonl[11065] _id=6abd1c5f485cab4c958b3acb ts=2026-09-30T14:27:43.4870000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[11064] _id=6abd1c5f485cab4c958b3acd ts=2026-09-30T14:27:43.4910000Z`; `4ms: 6aa4140b41b41dbac0c7f231.jsonl[11137] _id=6abe63ce485cab4c95a6a5f1 ts=2026-10-01T13:44:45.3270000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[11126] _id=6abe63ce485cab4c95a6a5f9 ts=2026-10-01T13:44:45.3310000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 8 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `469ms: 6aa4140b41b41dbac0c7f231.jsonl[7910] _id=6abbc4e6485cab4c957e36bd ts=2026-09-29T14:02:14.2850000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[7923] _id=6abbc4e6485cab4c957e36cb ts=2026-09-29T14:02:14.7540000Z`; `534ms: 6aa4140b41b41dbac0c7f231.jsonl[8007] _id=6abbc53f485cab4c957e3ff4 ts=2026-09-29T14:03:43.6850000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[7970] _id=6abbc540485cab4c957e4018 ts=2026-09-29T14:03:44.2190000Z`; `465ms: 6aa4140b41b41dbac0c7f231.jsonl[8013] _id=6abbc541485cab4c957e405f ts=2026-09-29T14:03:45.2200000Z ~ 6aa4140b41b41dbac0c7f231.jsonl[7770] _id=6abbc541485cab4c957e4083 ts=2026-09-29T14:03:45.6850000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa4140b41b41dbac0c7f231.jsonl[11375] _id=6abe66ae485cab4c95a761c3 ts=2026-10-01T13:57:02.0060000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13727] _id=6ac3aaedde269131f9a9dd20 ts=2026-10-05T13:49:33.0570000Z; 71h 20m: 6aa4140b41b41dbac0c7f231.jsonl[4115] _id=6ab68470485cab4c95563bf4 ts=2026-09-25T14:25:52.1500000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4489] _id=6aba6f9b485cab4c95681acf ts=2026-09-28T13:46:03.5950000Z; 24h 6m: 6aa4140b41b41dbac0c7f231.jsonl[1179] _id=6ab52a46485cab4c95519263 ts=2026-09-24T13:48:54.2190000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3255] _id=6ab67d3c485cab4c9555a2d2 ts=2026-09-25T13:55:08.7160000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 72h 14m 
  - Evidence: 72h 14m: 6aa4140b41b41dbac0c7f231.jsonl[5342] _id=6aba7257485cab4c95685c35 ts=2026-09-28T13:57:43.5740000Z -> 6aa4140b41b41dbac0c7f231.jsonl[12307] _id=6abe6a22485cab4c95a7a801 ts=2026-10-01T14:11:46.0550000Z; 71h 25m: 6aa4140b41b41dbac0c7f231.jsonl[4310] _id=6ab6856b485cab4c95564a38 ts=2026-09-25T14:30:03.5440000Z -> 6aa4140b41b41dbac0c7f231.jsonl[5110] _id=6aba71d1485cab4c95684d81 ts=2026-09-28T13:55:29.1920000Z; 23h 48m: 6aa4140b41b41dbac0c7f231.jsonl[3047] _id=6ab52ee9485cab4c9551d641 ts=2026-09-24T14:08:41.7460000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3294] _id=6ab67db3485cab4c9555a9de ts=2026-09-25T13:57:07.3020000Z
- **INFO / Info** `DaniEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f231.jsonl[12310] _id=6abe6a26485cab4c95a7a83f ts=2026-10-01T14:11:50.8700000Z -> 6aa4140b41b41dbac0c7f231.jsonl[12311] _id=6abe6a26485cab4c95a7a843 ts=2026-10-01T14:11:50.8720000Z; 3ms: 6aa4140b41b41dbac0c7f231.jsonl[12308] _id=6abe6a24485cab4c95a7a813 ts=2026-10-01T14:11:48.3680000Z -> 6aa4140b41b41dbac0c7f231.jsonl[12306] _id=6abe6a24485cab4c95a7a815 ts=2026-10-01T14:11:48.3710000Z; 6ms: 6aa4140b41b41dbac0c7f231.jsonl[5113] _id=6aba71d9485cab4c95684ea3 ts=2026-09-28T13:55:37.2060000Z -> 6aa4140b41b41dbac0c7f231.jsonl[5116] _id=6aba71d9485cab4c95684ea9 ts=2026-09-28T13:55:37.2120000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f231.jsonl[13633] _id=6abe6e9e485cab4c95a8ab03 ts=2026-10-01T14:30:54.1440000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13788] _id=6ac3aafdde269131f9a9e0c2 ts=2026-10-05T13:49:49.1360000Z; 71h 15m: 6aa4140b41b41dbac0c7f231.jsonl[4437] _id=6ab685d1485cab4c95564bc2 ts=2026-09-25T14:31:45.7860000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4524] _id=6aba6fd4485cab4c95681b39 ts=2026-09-28T13:47:00.9330000Z; 23h 37m: 6aa4140b41b41dbac0c7f231.jsonl[3237] _id=6ab530fb485cab4c9551ef57 ts=2026-09-24T14:17:31.1260000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3265] _id=6ab67d45485cab4c9555a32c ts=2026-09-25T13:55:15.7400000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 730 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f231.jsonl[10618] _id=6abd1903485cab4c958aa656 ts=2026-09-30T14:13:23.7320000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10619] _id=6abd1903485cab4c958aa65c ts=2026-09-30T14:13:23.7330000Z; 1ms: 6aa4140b41b41dbac0c7f231.jsonl[10893] _id=6abd1ae5485cab4c958afee6 ts=2026-09-30T14:21:25.1760000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10891] _id=6abd1ae5485cab4c958afeea ts=2026-09-30T14:21:25.1770000Z; 1ms: 6aa4140b41b41dbac0c7f231.jsonl[10906] _id=6abd1af9485cab4c958b02b4 ts=2026-09-30T14:21:45.7020000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10922] _id=6abd1af9485cab4c958b02b8 ts=2026-09-30T14:21:45.7030000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 10m 
  - Evidence: 144h 10m: 6aa4140b41b41dbac0c7f231.jsonl[1170] _id=6ab529f2485cab4c955185df ts=2026-09-24T13:47:30.9100000Z -> 6aa4140b41b41dbac0c7f231.jsonl[9760] _id=6abd1577485cab4c95896b9f ts=2026-09-30T13:58:15.8000000Z; 23h 56m: 6aa4140b41b41dbac0c7f231.jsonl[9760] _id=6abd1577485cab4c95896b9f ts=2026-09-30T13:58:15.8000000Z -> 6aa4140b41b41dbac0c7f231.jsonl[11359] _id=6abe6642485cab4c95a74b13 ts=2026-10-01T13:55:14.1260000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f231.jsonl[13675] _id=6abe6eaf485cab4c95a8aea7 ts=2026-10-01T14:31:11.2350000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13731] _id=6ac3aaf4de269131f9a9dea4 ts=2026-10-05T13:49:39.1630000Z; 71h 7m: 6aa4140b41b41dbac0c7f231.jsonl[4468] _id=6ab68772485cab4c95564d36 ts=2026-09-25T14:38:42.6010000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4477] _id=6aba6fa1485cab4c95681adb ts=2026-09-28T13:46:08.6760000Z; 23h 37m: 6aa4140b41b41dbac0c7f231.jsonl[3239] _id=6ab53104485cab4c9551ef5d ts=2026-09-24T14:17:40.2160000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3242] _id=6ab67d44485cab4c9555a30e ts=2026-09-25T13:55:15.6940000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 212 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f231.jsonl[16033] _id=6ac4fd32de269131f9b1c2db ts=2026-10-06T13:52:49.5060000Z -> 6aa4140b41b41dbac0c7f231.jsonl[16037] _id=6ac4fd32de269131f9b1c2eb ts=2026-10-06T13:52:49.5060000Z; 0ms: 6aa4140b41b41dbac0c7f231.jsonl[7481] _id=6abbc2f0485cab4c957e0877 ts=2026-09-29T13:53:52.2080000Z -> 6aa4140b41b41dbac0c7f231.jsonl[7493] _id=6abbc2f0485cab4c957e0879 ts=2026-09-29T13:53:52.2080000Z; 0ms: 6aa4140b41b41dbac0c7f231.jsonl[8209] _id=6abbc645485cab4c957e5bbb ts=2026-09-29T14:08:05.0460000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8210] _id=6abbc645485cab4c957e5bbf ts=2026-09-29T14:08:05.0460000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4140b41b41dbac0c7f231.jsonl[13034] _id=6abe6dad485cab4c95a87251 ts=2026-10-01T14:26:53.3190000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13969] _id=6ac3ab5dde269131f9a9f403 ts=2026-10-05T13:51:24.6210000Z; 71h 21m: 6aa4140b41b41dbac0c7f231.jsonl[4181] _id=6ab68500485cab4c95564530 ts=2026-09-25T14:28:16.8350000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4590] _id=6aba7067485cab4c95681ff9 ts=2026-09-28T13:49:27.8700000Z; 24h 14m: 6aa4140b41b41dbac0c7f231.jsonl[2818] _id=6ab52ca0485cab4c9551ba9c ts=2026-09-24T13:58:55.9220000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3558] _id=6ab68181485cab4c9555e632 ts=2026-09-25T14:13:21.5620000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f231.jsonl[8450] _id=6abbc89d485cab4c957e89bb ts=2026-09-29T14:18:05.2870000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8451] _id=6abbc89d485cab4c957e89c0 ts=2026-09-29T14:18:05.2880000Z; 1ms: 6aa4140b41b41dbac0c7f231.jsonl[8665] _id=6abbc8e4485cab4c957e9331 ts=2026-09-29T14:19:16.3300000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8670] _id=6abbc8e4485cab4c957e9334 ts=2026-09-29T14:19:16.3310000Z; 4ms: 6aa4140b41b41dbac0c7f231.jsonl[548] _id=6ab3ddd5485cab4c954cff16 ts=2026-09-23T14:10:29.3020000Z -> 6aa4140b41b41dbac0c7f231.jsonl[220] _id=6ab3ddd5485cab4c954cff1b ts=2026-09-23T14:10:29.3060000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f231.jsonl[13699] _id=6abe6eb4485cab4c95a8af74 ts=2026-10-01T14:31:16.5650000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13733] _id=6ac3aaf4de269131f9a9de9d ts=2026-10-05T13:49:33.0640000Z; 71h 7m: 6aa4140b41b41dbac0c7f231.jsonl[4470] _id=6ab6877f485cab4c95564d56 ts=2026-09-25T14:38:55.2900000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4493] _id=6aba6fa1485cab4c95681ad9 ts=2026-09-28T13:46:03.6010000Z; 23h 37m: 6aa4140b41b41dbac0c7f231.jsonl[3236] _id=6ab5310b485cab4c9551ef61 ts=2026-09-24T14:17:47.3640000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3241] _id=6ab67d44485cab4c9555a30c ts=2026-09-25T13:55:08.7230000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 6aa4140b41b41dbac0c7f231.jsonl[2790] _id=6ab52c68485cab4c9551b8c1 ts=2026-09-24T13:57:59.2060000Z -> 6aa4140b41b41dbac0c7f231.jsonl[5646] _id=6aba753a485cab4c9568873e ts=2026-09-28T14:10:01.0860000Z; 95h 18m: 6aa4140b41b41dbac0c7f231.jsonl[13710] _id=6abe6eb6485cab4c95a8afad ts=2026-10-01T14:31:16.7990000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13760] _id=6ac3aaf5de269131f9a9deec ts=2026-10-05T13:49:39.2250000Z; 23h 55m: 6aa4140b41b41dbac0c7f231.jsonl[10314] _id=6abd16c7485cab4c9589ca65 ts=2026-09-30T14:03:47.8280000Z -> 6aa4140b41b41dbac0c7f231.jsonl[11500] _id=6abe6795485cab4c95a7834f ts=2026-10-01T13:59:46.9330000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3326 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f231.jsonl[10007] _id=6abd164c485cab4c958993f4 ts=2026-09-30T14:01:47.0340000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10008] _id=6abd164c485cab4c958993f9 ts=2026-09-30T14:01:47.0340000Z; 0ms: 6aa4140b41b41dbac0c7f231.jsonl[10011] _id=6abd1650485cab4c9589948c ts=2026-09-30T14:01:51.3210000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10020] _id=6abd1650485cab4c9589948f ts=2026-09-30T14:01:51.3210000Z; 0ms: 6aa4140b41b41dbac0c7f231.jsonl[10038] _id=6abd1656485cab4c95899607 ts=2026-09-30T14:01:57.0240000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10041] _id=6abd1656485cab4c95899610 ts=2026-09-30T14:01:57.0240000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 6aa4140b41b41dbac0c7f231.jsonl[2802] _id=6ab52ca2485cab4c9551baa9 ts=2026-09-24T13:58:58.8950000Z -> 6aa4140b41b41dbac0c7f231.jsonl[5581] _id=6aba74d2485cab4c956880c1 ts=2026-09-28T14:08:18.3660000Z; 95h 56m: 6aa4140b41b41dbac0c7f231.jsonl[12655] _id=6abe6cf2485cab4c95a84d81 ts=2026-10-01T14:23:46.8520000Z -> 6aa4140b41b41dbac0c7f231.jsonl[15118] _id=6ac3b22bde269131f9ab64ee ts=2026-10-05T14:20:27.5160000Z; 71h 54m: 6aa4140b41b41dbac0c7f231.jsonl[5653] _id=6aba7525485cab4c956885d5 ts=2026-09-28T14:09:40.9900000Z -> 6aa4140b41b41dbac0c7f231.jsonl[12107] _id=6abe6842485cab4c95a79401 ts=2026-10-01T14:03:46.3410000Z
- **INFO / Info** `SolarStillDesignEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 22m 
  - Evidence: 23h 22m: 6aa4140b41b41dbac0c7f231.jsonl[11027] _id=6abd1c13485cab4c958b34e0 ts=2026-09-30T14:26:27.2810000Z -> 6aa4140b41b41dbac0c7f231.jsonl[11205] _id=6abe64cc485cab4c95a6e503 ts=2026-10-01T13:49:00.4730000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa4140b41b41dbac0c7f231.jsonl[12567] _id=6abe6c7c485cab4c95a832be ts=2026-10-01T14:21:48.2610000Z -> 6aa4140b41b41dbac0c7f231.jsonl[15053] _id=6ac3b1e8de269131f9ab519a ts=2026-10-05T14:19:20.3750000Z; 72h 1m: 6aa4140b41b41dbac0c7f231.jsonl[5356] _id=6aba7271485cab4c95685dbf ts=2026-09-28T13:58:09.2050000Z -> 6aa4140b41b41dbac0c7f231.jsonl[11479] _id=6abe6769485cab4c95a77d6b ts=2026-10-01T14:00:05.9600000Z; 71h 16m: 6aa4140b41b41dbac0c7f231.jsonl[4297] _id=6ab6856d485cab4c95564a43 ts=2026-09-25T14:30:03.7580000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4502] _id=6aba6fbe485cab4c95681b05 ts=2026-09-28T13:46:38.3200000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.013s..0.016s shown 
  - Evidence: 13ms: 6aa4140b41b41dbac0c7f231.jsonl[2978] _id=6ab52e6c485cab4c9551d0e5 ts=2026-09-24T14:06:36.6720000Z -> 6aa4140b41b41dbac0c7f231.jsonl[2991] _id=6ab52e6c485cab4c9551d0e7 ts=2026-09-24T14:06:36.6850000Z; 14ms: 6aa4140b41b41dbac0c7f231.jsonl[16763] _id=6ac500b3de269131f9b258d4 ts=2026-10-06T14:07:47.1590000Z -> 6aa4140b41b41dbac0c7f231.jsonl[16766] _id=6ac500b3de269131f9b258d8 ts=2026-10-06T14:07:47.1730000Z; 16ms: 6aa4140b41b41dbac0c7f231.jsonl[16766] _id=6ac500b3de269131f9b258d8 ts=2026-10-06T14:07:47.1730000Z -> 6aa4140b41b41dbac0c7f231.jsonl[16765] _id=6ac500b3de269131f9b258e0 ts=2026-10-06T14:07:47.1890000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 37m 
  - Evidence: 120h 37m: 6aa4140b41b41dbac0c7f231.jsonl[1083] _id=6ab52950485cab4c95516ad9 ts=2026-09-24T13:44:48.8630000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8813] _id=6abbc9b5485cab4c957ea97b ts=2026-09-29T14:22:45.6750000Z; 119h 54m: 6aa4140b41b41dbac0c7f231.jsonl[10863] _id=6abd1aba485cab4c958af6ce ts=2026-09-30T14:20:42.2730000Z -> 6aa4140b41b41dbac0c7f231.jsonl[14846] _id=6ac3b0eade269131f9ab0952 ts=2026-10-05T14:15:06.3970000Z; 23h 52m: 6aa4140b41b41dbac0c7f231.jsonl[9229] _id=6abbcb08485cab4c957ecf8b ts=2026-09-29T14:28:24.1450000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10841] _id=6abd1aa9485cab4c958af37e ts=2026-09-30T14:20:25.1480000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 120h 36m 
  - Evidence: 120h 36m: 6aa4140b41b41dbac0c7f231.jsonl[1084] _id=6ab52950485cab4c95516adc ts=2026-09-24T13:44:48.8870000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8745] _id=6abbc96b485cab4c957ea193 ts=2026-09-29T14:21:31.1760000Z; 119h 52m: 6aa4140b41b41dbac0c7f231.jsonl[10869] _id=6abd1aba485cab4c958af6e2 ts=2026-09-30T14:20:42.2930000Z -> 6aa4140b41b41dbac0c7f231.jsonl[14731] _id=6ac3b06ede269131f9aaea23 ts=2026-10-05T14:13:02.2180000Z; 23h 50m: 6aa4140b41b41dbac0c7f231.jsonl[9230] _id=6abbcb08485cab4c957ecf9b ts=2026-09-29T14:28:24.1830000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10762] _id=6abd1a5d485cab4c958ae730 ts=2026-09-30T14:19:09.6360000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.025s..0.025s shown 
  - Evidence: 25ms: 6aa4140b41b41dbac0c7f231.jsonl[9226] _id=6abbcb08485cab4c957ecf8f ts=2026-09-29T14:28:24.1580000Z -> 6aa4140b41b41dbac0c7f231.jsonl[9230] _id=6abbcb08485cab4c957ecf9b ts=2026-09-29T14:28:24.1830000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 36m 
  - Evidence: 120h 36m: 6aa4140b41b41dbac0c7f231.jsonl[1072] _id=6ab52946485cab4c955168ed ts=2026-09-24T13:44:38.2090000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8744] _id=6abbc970485cab4c957ea219 ts=2026-09-29T14:21:36.5890000Z; 119h 52m: 6aa4140b41b41dbac0c7f231.jsonl[10865] _id=6abd1ab9485cab4c958af69c ts=2026-09-30T14:20:41.5360000Z -> 6aa4140b41b41dbac0c7f231.jsonl[14755] _id=6ac3b06cde269131f9aae9e1 ts=2026-10-05T14:13:00.3490000Z; 23h 50m: 6aa4140b41b41dbac0c7f231.jsonl[9181] _id=6abbcb07485cab4c957ecf71 ts=2026-09-29T14:28:23.0100000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10749] _id=6abd1a5a485cab4c958ae68c ts=2026-09-30T14:19:06.2370000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 156 interval(s) ≤ 0.001s..0.017s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f231.jsonl[8972] _id=6abbca2c485cab4c957eb637 ts=2026-09-29T14:24:44.1180000Z -> 6aa4140b41b41dbac0c7f231.jsonl[8983] _id=6abbca2c485cab4c957eb63d ts=2026-09-29T14:24:44.1190000Z; 9ms: 6aa4140b41b41dbac0c7f231.jsonl[14952] _id=6ac3b148de269131f9ab2441 ts=2026-10-05T14:16:40.2770000Z -> 6aa4140b41b41dbac0c7f231.jsonl[14955] _id=6ac3b148de269131f9ab2452 ts=2026-10-05T14:16:40.2860000Z; 17ms: 6aa4140b41b41dbac0c7f231.jsonl[10814] _id=6abd1a8d485cab4c958aee94 ts=2026-09-30T14:19:57.4120000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10768] _id=6abd1a8d485cab4c958aee98 ts=2026-09-30T14:19:57.4290000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 144h 35m 
  - Evidence: 144h 35m: 6aa4140b41b41dbac0c7f231.jsonl[1069] _id=6ab52944485cab4c9551688f ts=2026-09-24T13:44:36.6720000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10856] _id=6abd1aa5485cab4c958af316 ts=2026-09-30T14:20:21.7350000Z; 119h 54m: 6aa4140b41b41dbac0c7f231.jsonl[10858] _id=6abd1aa7485cab4c958af33c ts=2026-09-30T14:20:23.2100000Z -> 6aa4140b41b41dbac0c7f231.jsonl[14833] _id=6ac3b0c8de269131f9aafec5 ts=2026-10-05T14:14:32.3610000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 48h 3m 
  - Evidence: 48h 3m: 6aa4140b41b41dbac0c7f231.jsonl[5111] _id=6aba71d7485cab4c95684e61 ts=2026-09-28T13:55:35.4270000Z -> 6aa4140b41b41dbac0c7f231.jsonl[9767] _id=6abd1593485cab4c95896e6d ts=2026-09-30T13:58:43.1680000Z; 23h 31m: 6aa4140b41b41dbac0c7f231.jsonl[10558] _id=6abd1912485cab4c958aa966 ts=2026-09-30T14:13:38.5110000Z -> 6aa4140b41b41dbac0c7f231.jsonl[11117] _id=6abe63cc485cab4c95a6a587 ts=2026-10-01T13:44:44.4270000Z; 14m 55s: 6aa4140b41b41dbac0c7f231.jsonl[9767] _id=6abd1593485cab4c95896e6d ts=2026-09-30T13:58:43.1680000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10558] _id=6abd1912485cab4c958aa966 ts=2026-09-30T14:13:38.5110000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa4140b41b41dbac0c7f231.jsonl[11372] _id=6abe66a8485cab4c95a760e3 ts=2026-10-01T13:56:55.9010000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13724] _id=6ac3aad9de269131f9a9d906 ts=2026-10-05T13:49:13.6220000Z; 71h 20m: 6aa4140b41b41dbac0c7f231.jsonl[4113] _id=6ab68469485cab4c95563bc6 ts=2026-09-25T14:25:45.5530000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4488] _id=6aba6f92485cab4c95681acd ts=2026-09-28T13:45:53.6800000Z; 24h 6m: 6aa4140b41b41dbac0c7f231.jsonl[1175] _id=6ab52a40485cab4c955191a3 ts=2026-09-24T13:48:48.3850000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3254] _id=6ab67d36485cab4c9555a285 ts=2026-09-25T13:55:02.1130000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4140b41b41dbac0c7f231.jsonl[13712] _id=6abe6ebe485cab4c95a8b0cd ts=2026-10-01T14:31:26.2830000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13723] _id=6ac3aad9de269131f9a9d8fe ts=2026-10-05T13:49:13.6210000Z; 71h 20m: 6aa4140b41b41dbac0c7f231.jsonl[4112] _id=6ab68469485cab4c95563bc3 ts=2026-09-25T14:25:45.5520000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4487] _id=6aba6f91485cab4c95681acb ts=2026-09-28T13:45:53.6780000Z; 24h 6m: 6aa4140b41b41dbac0c7f231.jsonl[1174] _id=6ab52a40485cab4c9551919f ts=2026-09-24T13:48:48.3840000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3240] _id=6ab67d36485cab4c9555a27e ts=2026-09-25T13:55:02.1120000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 6aa4140b41b41dbac0c7f231.jsonl[13713] _id=6abe6ebf485cab4c95a8b0e7 ts=2026-10-01T14:31:27.1270000Z -> 6aa4140b41b41dbac0c7f231.jsonl[15151] _id=6ac3b273de269131f9ab7850 ts=2026-10-05T14:21:39.2930000Z; 71h 35m: 6aa4140b41b41dbac0c7f231.jsonl[4110] _id=6ab6844f485cab4c95563aa0 ts=2026-09-25T14:25:19.6990000Z -> 6aa4140b41b41dbac0c7f231.jsonl[5445] _id=6aba7324485cab4c9568683b ts=2026-09-28T14:01:08.9580000Z; 47h 19m: 6aa4140b41b41dbac0c7f231.jsonl[4491] _id=6aba6f91485cab4c95681ac7 ts=2026-09-23T14:39:48.167Z -> 6aa4140b41b41dbac0c7f231.jsonl[3391] _id=6ab67e20485cab4c9555b58c ts=2026-09-25T13:58:56.9070000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f231.jsonl[13597] _id=6abe6e31485cab4c95a88f5f ts=2026-10-01T14:29:05.4400000Z -> 6aa4140b41b41dbac0c7f231.jsonl[13759] _id=6ac3aaf5de269131f9a9dee6 ts=2026-10-05T13:49:39.2320000Z; 71h 18m: 6aa4140b41b41dbac0c7f231.jsonl[4154] _id=6ab684e6485cab4c955642ee ts=2026-09-25T14:27:50.2300000Z -> 6aa4140b41b41dbac0c7f231.jsonl[4504] _id=6aba6fa1485cab4c95681add ts=2026-09-28T13:46:08.7010000Z; 23h 49m: 6aa4140b41b41dbac0c7f231.jsonl[2855] _id=6ab52e56485cab4c9551d011 ts=2026-09-24T14:06:14.7970000Z -> 6aa4140b41b41dbac0c7f231.jsonl[3267] _id=6ab67d45485cab4c9555a330 ts=2026-09-25T13:55:15.7990000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 23 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f231.jsonl[10357] _id=6abd16fe485cab4c9589ec10 ts=2026-09-30T14:04:46.6640000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10344] _id=6abd16ff485cab4c9589ec23 ts=2026-09-30T14:04:46.6650000Z; 1ms: 6aa4140b41b41dbac0c7f231.jsonl[10928] _id=6abd1b04485cab4c958b0450 ts=2026-09-30T14:21:56.5450000Z -> 6aa4140b41b41dbac0c7f231.jsonl[10926] _id=6abd1b04485cab4c958b0456 ts=2026-09-30T14:21:56.5460000Z; 1ms: 6aa4140b41b41dbac0c7f231.jsonl[845] _id=6ab3e1e4485cab4c954d2a4d ts=2026-09-23T14:27:48.7110000Z -> 6aa4140b41b41dbac0c7f231.jsonl[842] _id=6ab3e1e4485cab4c954d2a4f ts=2026-09-23T14:27:48.7120000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 24m 
  - Evidence: 23h 24m: 6aa4140b41b41dbac0c7f231.jsonl[7450] _id=6aba7a5b485cab4c9568f2cf ts=2026-09-28T14:31:55.7150000Z -> 6aa4140b41b41dbac0c7f231.jsonl[7597] _id=6abbc388485cab4c957e121b ts=2026-09-29T13:56:24.7350000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 12 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[811] _id=6ab3e1b6485cab4c954d2845 ts=2026-09-23T14:27:02.4310000Z`; `6aa4140b41b41dbac0c7f231.jsonl[3645] _id=6ab68244485cab4c95560a88 ts=2026-09-25T14:16:36.2410000Z`; `6aa4140b41b41dbac0c7f231.jsonl[3709] _id=6ab682fc485cab4c95562584 ts=2026-09-25T14:19:40.6630000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 94 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1650] _id=6ab52ba7485cab4c9551a697 ts=2026-09-24T13:54:08.8080000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1708] _id=6ab52bac485cab4c9551a733 ts=2026-09-24T13:54:21.3300000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1672] _id=6ab52bac485cab4c9551a73f ts=2026-09-24T13:54:22.4770000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 242 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1458] _id=6ab52b94485cab4c9551a403 ts=2026-09-24T13:51:37.8650000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1281] _id=6ab52af5485cab4c95519bcf ts=2026-09-24T13:51:47.8590000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1284] _id=6ab52af5485cab4c95519bdb ts=2026-09-24T13:51:48.2710000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[9230] _id=6abbcb08485cab4c957ecf9b ts=2026-09-29T14:28:24.1830000Z`; `6aa4140b41b41dbac0c7f231.jsonl[14966] _id=6ac3b150de269131f9ab272f ts=2026-10-05T14:16:48.0970000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 18 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[8971] _id=6abbca2c485cab4c957eb633 ts=2026-09-29T14:24:44.0970000Z`; `6aa4140b41b41dbac0c7f231.jsonl[8972] _id=6abbca2c485cab4c957eb637 ts=2026-09-29T14:24:44.1180000Z`; `6aa4140b41b41dbac0c7f231.jsonl[8983] _id=6abbca2c485cab4c957eb63d ts=2026-09-29T14:24:44.1190000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[9767] _id=6abd1593485cab4c95896e6d ts=2026-09-30T13:58:43.1680000Z`; `6aa4140b41b41dbac0c7f231.jsonl[10558] _id=6abd1912485cab4c958aa966 ts=2026-09-30T14:13:38.5110000Z`; `6aa4140b41b41dbac0c7f231.jsonl[11117] _id=6abe63cc485cab4c95a6a587 ts=2026-10-01T13:44:44.4270000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[7495] _id=6abbc2f8485cab4c957e08bd ts=2026-09-29T13:54:00.0070000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[4492] _id=6aba6fa0485cab4c95681ad7 ts=?`; `6aa4140b41b41dbac0c7f231.jsonl[7491] _id=6abbc2f0485cab4c957e086f ts=?`; `6aa4140b41b41dbac0c7f231.jsonl[13732] _id=6ac3aaf3de269131f9a9de68 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 822 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1667] _id=6ab52baa485cab4c9551a6fe ts=2026-09-24T13:54:14.2860000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1695] _id=6ab52baa485cab4c9551a701 ts=2026-09-24T13:54:14.3360000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1633] _id=6ab52baa485cab4c9551a705 ts=2026-09-24T13:54:14.3540000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1069 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1466] _id=6ab52b94485cab4c9551a40b ts=2026-09-24T13:51:38.0060000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1445] _id=6ab52b94485cab4c9551a40d ts=2026-09-24T13:51:46.0430000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1278] _id=6ab52af4485cab4c95519bc5 ts=2026-09-24T13:51:47.6200000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 37 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[2991] _id=6ab52e6c485cab4c9551d0e7 ts=2026-09-24T14:06:36.6850000Z`; `6aa4140b41b41dbac0c7f231.jsonl[2994] _id=6ab52e6d485cab4c9551d0ef ts=2026-09-24T14:06:36.7020000Z`; `6aa4140b41b41dbac0c7f231.jsonl[3044] _id=6ab52edf485cab4c9551d5ad ts=2026-09-24T14:08:30.9980000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 36 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[975] _id=6ab528ac485cab4c9551553f ts=2026-09-24T13:42:04.7530000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1009] _id=6ab5291c485cab4c95516235 ts=2026-09-24T13:43:56.5530000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1011] _id=6ab5291c485cab4c95516243 ts=2026-09-24T13:43:56.8510000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[1059] _id=6ab5293a485cab4c955166f7 ts=2026-09-24T13:44:26.4140000Z`; `6aa4140b41b41dbac0c7f231.jsonl[1067] _id=6ab52942485cab4c9551681c ts=2026-09-24T13:44:34.3300000Z`; `6aa4140b41b41dbac0c7f231.jsonl[10858] _id=6abd1aa7485cab4c958af33c ts=2026-09-30T14:20:23.2100000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'DialogueStartEvent' (totals: 483 start, 479 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 271 unmatched 'BecameCameraCentered' (totals: 1124 open, 947 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 153 unmatched 'BecameVisible' (totals: 1556 open, 1645 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'MapOpenEvent' (totals: 44 open, 40 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationNodeHoverStart' (totals: 329 open, 343 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 10 unmatched 'argumentationToolOpen' (totals: 13 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'questActiveEvent' (totals: 67 start, 42 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 380 of 17093 adjacent _id pairs reverse in client time; worst 173393.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f231.jsonl[4470] _id=6ab6877f485cab4c95564d56 ts=2026-09-25T14:38:55.2900000Z`; `6aa4140b41b41dbac0c7f231.jsonl[4476] _id=6aba6f91485cab4c95681ac1 ts=2026-09-23T14:29:01.455Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -429411.68s, max +0.34s over 17094 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f231\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 5272 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3512); Unit 4 Dev (1018); Unit 5 Dev - Dungeon (426); Unit 3 Dungeon Dev (316)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.14s, n=5271)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5272/5272 records)
    "BecameInvisible"  x1645
    "BecameVisible"  x1556
    "BecameCameraCentered"  x1124
    "BecameCameraUncentered"  x947
data.pieceId  (string, 5272/5272 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5272/5272 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 5221 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1733); Unit 2 Prod (Refactor) (1184); Unit 4 Dev - Dungeon (881); Unit 4 Dev (385); Unit 1 Dev (370); Unit 3 Dungeon Dev (254); Unit 5 Dev - Dungeon (185); Unit 4 Dev - Anderson Base (120); Unit 5 Dev (109)
- **Intervals:** median 0.86s (p5 0.08s / p95 11.97s, n=5220)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5221/5221 records)
    "pressed"  x5221
data.actionType  (string, 5221/5221 records)
    "Move"  x3140
    "Interact"  x1228
    "Jump"  x524
    "Hoverboard"  x119
    "Ascend"  x81
    "Sprint"  x60
    "Map"  x50
    "Descend"  x8
    "ToggleDebug"  x7
    "SkipCinematic"  x4
data.key  (string, 5221/5221 records, 22 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5221/5221 records)
    "Player"  x3587
    "Drone"  x1634
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `DialogueEvent` — 2474 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (730); Unit 3 Dev (345); Unit 5 Dev (311); Unit 4 Dev (309); Unit 1 Dev (247); Unit 3 Dungeon Dev (159); Unit 4 Dev - Dungeon (145); Unit 4 Dev - Anderson Base (144); Unit 5 Dev - Dungeon (84)
- **eventKey:** present on 1512 of 2474 records
- **Intervals:** median 3.55s (p5 0.00s / p95 28.15s, n=2473)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1512; [conversationId, dialogueEventType] x962
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2474/2474 records)
    numeric range 8 .. 118 (52 unique)
data.dialogueEventType  (string, 2474/2474 records)
    "DialogueNodeEvent"  x1512
    "DialogueStartEvent"  x483
    "DialogueFinishEvent"  x479
data.nodeId  (number, 1512/2474 records)
    numeric range 0 .. 289 (180 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 2061 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (600); Unit 3 Dev (367); Unit 1 Dev (256); Unit 4 Dev (221); Unit 4 Dev - Dungeon (193); Unit 5 Dev (162); Unit 3 Dungeon Dev (95); Unit 5 Dev - Dungeon (89); Unit 4 Dev - Anderson Base (78)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.35s, n=2047)
- **Fields under `data`:**

```text
data.position  (object, 2061/2061 records)
data.position.x  (number, 2061/2061 records)
    numeric range -672.846 .. 1556.88 (745 unique)
data.position.y  (number, 2061/2061 records)
    numeric range -113.155 .. 221.94 (558 unique)
data.position.z  (number, 2061/2061 records)
    numeric range -1138.65 .. 1749.59 (745 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 760 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (393); Unit 3 Dev (159); Unit 1 Dev (106); Unit 5 Dev (102)
- **Intervals:** median 0.33s (p5 0.02s / p95 5.69s, n=759)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 760/760 records)
    "argumentationNodeHoverEnd"  x343
    "argumentationNodeHoverStart"  x329
    "argumentationNodeAdd"  x51
    "argumentationNodeRemove"  x37
data.argumentationTitle  (string, 760/760 records)
    "Unit 4 - Flooding"  x393
    "Unit 3 - Pollution Upstream"  x159
    "Unit 5"  x102
    "Unit 1 - Freshwater"  x59
    "Unit 1 - Argumentation Tutorial"  x47
data.nodeName  (string, 760/760 records)
    "A"  x117
    "B"  x84
    "2"  x83
    "1"  x81
    "II"  x81
    "C"  x78
    "4"  x72
    "I"  x59
    "D"  x48
    "3"  x41
    "5"  x16
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 515 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (171); Unit 1 Dev (137); Unit 2 Prod (Refactor) (76); Unit 3 Dungeon Dev (41); Unit 4 Dev (40); Unit 5 Dev - Dungeon (21); Unit 5 Dev (11); Unit 3 Dev (9); Unit 4 Dev - Anderson Base (9)
- **Intervals:** median 4.69s (p5 0.17s / p95 215.35s, n=514)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 515/515 records)
    40 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 515/515 records)
    96 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 187 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (137); Unit 3 Dev (48); Unit 3 Dungeon Dev (2)
- **Intervals:** median 2.34s (p5 0.34s / p95 430.81s, n=186)
- **`data` key-set variants:** [actionType, featureUsed] x84; [actionType, featureUsed, location] x52; [actionType, featureUsed, legendName] x51
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 187/187 records)
    "MapOpenEvent"  x44
    "Selected"  x44
    "MapCloseEvent"  x40
    "WaypointMoveEvent"  x40
    "WaypointSetEvent"  x10
    "Unselected"  x7
    "WaypointResetEvent"  x2
data.featureUsed  (string, 187/187 records)
    "Map"  x84
    "Waypoint"  x52
    "Legend"  x51
data.legendName  (string, 51/187 records)
    14 unique values (see csv/event_unique_values.csv)
data.location  (object, 52/187 records)
data.location.x  (number, 52/187 records)
    numeric range -439.09 .. 135.91 (47 unique)
data.location.y  (number, 52/187 records)
    numeric range -281.694 .. 188.5 (43 unique)
data.location.z  (number, 52/187 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 112 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (62); Unit 2 Prod (Refactor) (38); Unit 3 Dev (12)
- **Intervals:** median 1.03s (p5 0.17s / p95 12.13s, n=111)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x100; [Soil Key Puzzle Status, Unit] x12
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/112 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/112 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 100/112 records)
    "RightDrag"  x53
    "LeftDrag"  x47
data.currentSoilType  (string, 100/112 records)
    "CLAYSAND"  x19
    "SAND"  x19
    "CLAY"  x18
    "SANDGRAVEL"  x18
    "CLAYROCK"  x13
    "GRAVEL"  x8
    "BEDROCK"  x5
data.isCorrectSelection  (string, 100/112 records)
    "false"  x76
    "true"  x24
data.waterLevelStatus  (string, 100/112 records)
    "TooLow"  x41
    "Proper"  x30
    "TooHigh"  x29
data.waterRetentionChange  (string, 100/112 records)
    "Decrease"  x41
    "Increase"  x35
    "NoChange"  x24
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 109 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 1 Dev (18); Unit 3 Dev (15); Unit 4 Dev - Dungeon (15); Unit 5 Dev (12); Unit 4 Dev (10); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 109 of 109 records
- **Intervals:** median 177.97s (p5 0.00s / p95 83627.71s, n=108)
- **`data` key-set variants:** [questEventType, questID, questName] x67; [questEventType, questID, questName, questSuccessOrFailure] x42
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 109/109 records)
    "questActiveEvent"  x67
    "questFinishEvent"  x42
data.questID  (string, 109/109 records)
    31 unique values (see csv/event_unique_values.csv)
data.questName  (string, 109/109 records)
    31 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 42/109 records)
    "Succeeded"  x42
```

Raw examples: `event_examples.json` -> `questEvent`.

### `soilMachine` — 63 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (63)
- **Intervals:** median 2.92s (p5 0.47s / p95 117.97s, n=62)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 63/63 records)
    "ChangeCanister"  x63
data.canisterType  (string, 63/63 records)
    "Clay"  x36
    "Bedrock"  x17
    "Sand"  x6
    "Gravel"  x4
data.floor  (string, 63/63 records)
    "5"  x48
    "4"  x9
    "3"  x6
data.machine  (string, 63/63 records)
    "1"  x62
    "2"  x1
data.row  (string, 63/63 records)
    "TopRow"  x39
    "BottomRow"  x24
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 51 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (23); Unit 2 Prod (Refactor) (10); Unit 5 Dev (6); Unit 3 Dev (5); Unit 1 Dev (3); Transition (2); Unit 3 Dungeon Dev (2)
- **Intervals:** median 382.47s (p5 2.56s / p95 86391.06s, n=50)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 51/51 records)
    true  x51
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DaniEvent` — 38 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (16)
- **Intervals:** median 2.57s (p5 0.01s / p95 119989.57s, n=37)
- **Fields under `data`:**

```text
data.actionType  (string, 38/38 records)
    "Close"  x19
    "Open"  x19
data.toolName  (string, 38/38 records, 34 empty-string)
    ""  x34
    "Settings"  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `WaterChamberEvent` — 36 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (36)
- **Intervals:** median 5.43s (p5 1.05s / p95 61.72s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 36/36 records)
    "On"  x22
    "Off"  x14
data.floor  (string, 36/36 records)
    "3"  x15
    "4"  x14
    "1"  x4
    "2"  x3
data.machineNumber  (string, 36/36 records)
    "One"  x35
    "Two"  x1
data.machineType  (string, 36/36 records)
    "Condenser"  x15
    "Evaporator"  x9
    "DualChamber_Evaporator"  x7
    "DualChamber_Condenser"  x3
    "VentSwitch"  x2
data.room  (string, 36/36 records)
    "2"  x16
    "3"  x14
    "1"  x4
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `gameWindowUnfocusEvent` — 36 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (13); Unit 5 Dev (7); Unit 3 Dev (6); Unit 1 Dev (4); Transition (3); Unit 3 Dungeon Dev (2); Unit 4 Dev (1)
- **Intervals:** median 166.64s (p5 1.43s / p95 196568.90s, n=35)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 36/36 records)
    false  x36
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationAnswerEvent` — 35 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (22); Unit 1 Dev (5); Unit 3 Dev (5); Unit 5 Dev (3)
- **Intervals:** median 12.79s (p5 0.71s / p95 206931.10s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "submitAnswerEvent"  x35
data.answerSubmitted  (string, 35/35 records)
    20 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 35/35 records)
    "Unit 4 - Flooding"  x22
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Freshwater"  x4
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `DEBUGMenu` — 26 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (5); Unit 4 Dev (5); Unit 1 Dev (3); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (2); Unit 4 Dev - Anderson Base (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 896.32s (p5 126.74s / p95 222804.06s, n=25)
- **Fields under `data`:**

```text
data.actionType  (string, 26/26 records)
    "DebugMenuStateChanged"  x26
data.isOpened  (bool, 26/26 records)
    false  x26
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 23 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (23)
- **Intervals:** median 989.66s (p5 139.95s / p95 248306.41s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    true  x23
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `SolarStillDesignEvent` — 22 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (22)
- **Intervals:** median 1.27s (p5 0.47s / p95 4.54s, n=21)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x20; [actionType, designSelections, featureUsed] x2
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "optionSelected"  x20
    "DesignSubmitted"  x2
data.designSelections  (object, 2/22 records)
data.designSelections.glassRoofTemperature  (string, 2/22 records)
    "Cold"  x2
data.designSelections.roofCovering  (string, 2/22 records)
    "Uncovered"  x2
data.designSelections.roofStyle  (string, 2/22 records)
    "Tilted Out"  x2
data.featureUsed  (string, 22/22 records)
    "RoofStyle"  x10
    "ExtraCovering"  x7
    "GlassRoofTemperature"  x3
    "Submit"  x2
data.selectedOption  (string, 20/22 records, 3 empty-string)
    "Tilted Out"  x5
    "Uncovered"  x4
    ""  x3
    "Covered"  x3
    "Cold"  x2
    "Flat"  x1
    "Hot"  x1
    "Tilted In"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `TerasGardenBox` — 17 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (17)
- **Intervals:** median 2.03s (p5 0.65s / p95 59.52s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records, 10 empty-string)
    ""  x10
    "cameraPlaced"  x7
data.boxId  (string, 17/17 records)
    "0"  x6
    "1"  x6
    "2"  x5
data.soilType  (string, 17/17 records)
    "Gravel"  x6
    "Clay"  x4
    "Sand"  x4
    "None"  x3
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `argumentationToolEvent` — 16 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (6); Unit 5 Dev (3)
- **Intervals:** median 3.96s (p5 0.53s / p95 458317.92s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationToolOpen"  x13
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 16/16 records)
    "Unit 3 - Pollution Upstream"  x6
    "Unit 1 - Freshwater"  x5
    "Unit 5"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.toolName  (string, 16/16 records)
    "BackingInfoPanel - "  x5
    "BackingInfoPanel - Pollution Site Data"  x4
    "BackingInfoPanel - Argumentation"  x2
    "BackingInfoPanel - Evaporation Flow Diagram"  x2
    "BackingInfoPanel - Watershed Image"  x2
    "BackingInfoPanel - Heat Added/Released Chart"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2)
- **Intervals:** median 92.66s (p5 0.05s / p95 432871.11s, n=11)
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
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
data.argumentationTitle  (string, 12/12 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
    "Unit 5"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 5 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2); Unit 5 Dev (2); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 42780.63s (p5 137.57s / p95 159739.47s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "Close"  x4
    "Open"  x1
data.chatID  (string, 5/5 records)
    "NA"  x4
    "[11-29, 11-230, 11-27, 11-27, 11-29]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 3 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 302631.61s (p5 107859.65s / p95 497403.56s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 3/3 records)
    "1"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "A user gesture is required to request Pointer Lock."  x2
    "Permissions check failed"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "TypeError: Permissions check failed"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit2"  x1
    "unit3"  x1
    "unit4"  x1
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
- `EndOfUnit` : median interval between records changed substantially
- `TerasGardenBox` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format
- `questEvent` eventKey: eventKey does not match its documented format
- `DialogueEvent` dialogueEventType: dialogue lifecycle: finish without preceding start
- `PuzzlePieceVisibleEvent` actionType: camera centering: close without preceding open

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (38 records)
- `TerasGardenBox` data.actionType: "" (10x)
- `TerasGardenBox` data.soilType: "None" (3x)
- `TopographicMapEvent` data.actionType: "Selected" (44x); "Unselected" (7x); "WaypointMoveEvent" (40x); "WaypointResetEvent" (2x); "WaypointSetEvent" (10x)
- `TopographicMapEvent` data.featureUsed: "Legend" (51x); "Waypoint" (52x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (37x)
- `soilMachine` data.canisterType: "Bedrock" (17x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*