# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26f

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4144c41b41dbac0c7f26f
- **Game version string(s) in log:** 2.8.1, 2.8.4, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4144c41b41dbac0c7f26f.jsonl
- **Records:** 19670 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4144c41b41dbac0c7f26f
- **Time span:** 2026-09-23T18:09:25.494000+00:00 .. 2026-10-08T15:14:14.957000+00:00 (357h 4m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26f\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **21 event types**, 19670 records, 11 scenes.
- Findings: **0 FAIL**, **35 WARNING**, 93 INFO, 0 NOT_TESTED, 86 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `questEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8246 | 41.92 | 1 | 9 | 0 | 2026-09-23T18:16:03.063000+00:00 | 2026-10-08T15:13:32.321000+00:00 | 356h 57m |
| PuzzlePieceVisibleEvent | 5242 | 26.65 | 1 | 4 | 0 | 2026-09-25T18:21:07.536000+00:00 | 2026-10-08T14:49:10.509000+00:00 | 308h 28m |
| PlayerPositionEvent | 2519 | 12.81 | 1 | 9 | 0 | 2026-09-23T18:15:57.648000+00:00 | 2026-10-08T15:14:14.957000+00:00 | 356h 58m |
| DialogueEvent | 2067 | 10.51 | 1 | 9 | 1249 | 2026-09-23T18:16:19.839000+00:00 | 2026-10-08T15:14:13.626000+00:00 | 356h 57m |
| argumentationNodeEvent | 617 | 3.14 | 1 | 4 | 0 | 2026-10-01T15:13:56.721000+00:00 | 2026-10-08T15:03:57.141000+00:00 | 167h 50m |
| ObjectInterEvent | 370 | 1.88 | 1 | 9 | 0 | 2026-09-23T18:35:43.152000+00:00 | 2026-10-08T15:13:33.489000+00:00 | 356h 37m |
| questEvent | 95 | 0.48 | 1 | 9 | 95 | 2026-09-23T18:16:19.805000+00:00 | 2026-10-08T15:05:07.748000+00:00 | 356h 48m |
| gameWindowFocusEvent | 80 | 0.41 | 1 | 8 | 0 | 2026-09-23T18:09:25.494000+00:00 | 2026-10-08T14:43:48.229000+00:00 | 356h 34m |
| Soil Key Puzzle | 78 | 0.4 | 1 | 3 | 0 | 2026-09-25T18:30:32.479000+00:00 | 2026-10-06T18:22:03.183000+00:00 | 263h 51m |
| argumentationAnswerEvent | 70 | 0.36 | 1 | 4 | 0 | 2026-10-01T15:14:59.492000+00:00 | 2026-10-08T15:03:59.514000+00:00 | 167h 49m |
| gameWindowUnfocusEvent | 57 | 0.29 | 1 | 8 | 0 | 2026-09-23T18:09:47.845000+00:00 | 2026-10-08T14:43:24.373000+00:00 | 356h 33m |
| TopographicMapEvent | 54 | 0.27 | 1 | 3 | 0 | 2026-09-23T18:33:59.675000+00:00 | 2026-10-06T15:08:37.182000+00:00 | 308h 34m |
| WaterChamberEvent | 53 | 0.27 | 1 | 1 | 0 | 2026-10-08T14:47:55.979000+00:00 | 2026-10-08T14:56:56.492000+00:00 | 9m 0s |
| DEBUGMenu | 44 | 0.22 | 1 | 9 | 0 | 2026-09-23T18:15:57.643000+00:00 | 2026-10-08T14:44:01.646000+00:00 | 356h 28m |
| gameStartEvent | 32 | 0.16 | 1 | 1 | 0 | 2026-09-23T18:09:25.495000+00:00 | 2026-10-08T14:43:48.229000+00:00 | 356h 34m |
| soilMachine | 22 | 0.11 | 1 | 1 | 0 | 2026-10-06T18:48:24.759000+00:00 | 2026-10-07T14:50:10.498000+00:00 | 20h 1m |
| argumentationEvent | 9 | 0.05 | 1 | 4 | 0 | 2026-10-01T15:13:57.975000+00:00 | 2026-10-08T15:03:59.535000+00:00 | 167h 50m |
| SolarStillDesignEvent | 8 | 0.04 | 1 | 1 | 0 | 2026-10-08T15:13:36.163000+00:00 | 2026-10-08T15:13:58.072000+00:00 | 21.9s |
| crash | 4 | 0.02 | 1 | 1 | 0 |  |  | ? |
| chatEvent | 2 | 0.01 | 1 | 2 | 0 | 2026-10-08T14:44:01.552000+00:00 | 2026-10-08T14:57:46.583000+00:00 | 13m 45s |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-10-06T18:14:11.738000+00:00 | 2026-10-06T18:14:11.738000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.042s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 8.74s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 3.796s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 2.964s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 403.002s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 250.724s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 9.595s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 3.7x vs baseline. 
  - Observed: 44 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 1; 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` — record volume changed 3.4x vs baseline. 
  - Observed: 8246 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightButton; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Press E To Place Cameras; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press [E/Action button] to enter escape pod  
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to go down; Press E to pick up; Press E to place glyph 
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
  - Observed: Flat 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — baseline categorical value(s) not seen this build. 
  - Observed: Tilted Out; Uncovered 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `SolarStillDesignEvent` `data.selectedOption` — categorical value(s) not seen in baseline. 
  - Observed: ; Covered; Flat; Tilted In 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 120 ft; 180 ft; 300 ft; 330 ft; 360 ft 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 14.0x vs baseline. 
  - Observed: 70 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,2,II; A,3,I; A,3,II; A,4,II; A,C,2,II; A,C,B,2,II; B,1,I; B,1,II; B,2,I; B,2,II; B,3,II; B,4,II; B,A,2,II; B,C,2,II; C,2,II; C,3,II; C,D,3,II; D,2,II; D,A,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit; Unit 1 - Does the planet WAT-247 have freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 4.4x vs baseline. 
  - Observed: 617 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 1 - Freshwater 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 5.3x vs baseline. 
  - Observed: 32 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 33; 34; 41; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Defend the Expedition; Desert Delicacies; Guru of Arguments; What Was That? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 4.4x vs baseline. 
  - Observed: 22 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 39 mismatch(es); e.g. 'DialogueNodeEvent:30:13' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9724] _id=6ac3e811de269131f9aec2df ts=2026-09-23T18:26:29.827Z`; `6aa4144c41b41dbac0c7f26f.jsonl[9732] _id=6ac3e811de269131f9aec2e3 ts=2026-09-23T18:26:33.343Z`; `6aa4144c41b41dbac0c7f26f.jsonl[9715] _id=6ac3e811de269131f9aec2e9 ts=2026-09-23T18:26:39.558Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 5 mismatch(es); e.g. 'questFinishEvent:28' vs expected 'questFinishEvent:29' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9881] _id=6ac3e81dde269131f9aec50b ts=2026-09-23T18:34:12.935Z`; `6aa4144c41b41dbac0c7f26f.jsonl[9896] _id=6ac3e81dde269131f9aec515 ts=2026-09-23T18:34:16.7Z`; `6aa4144c41b41dbac0c7f26f.jsonl[5385] _id=6abe5566485cab4c95a3dbff ts=2026-10-01T12:43:16.6070000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 32 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 32} 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[12] _id=6ab415d4485cab4c954f3672 ts=2026-09-23T18:09:25.4950000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[16] _id=6ab41754485cab4c954f36c4 ts=2026-09-23T18:15:48.7740000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[65] _id=6ab562f3485cab4c9553a4c2 ts=2026-09-24T17:50:42.9860000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 80 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 80} 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[10] _id=6ab415d4485cab4c954f3670 ts=2026-09-23T18:09:25.4940000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[15] _id=6ab41754485cab4c954f36c2 ts=2026-09-23T18:15:48.7730000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[2] _id=6ab41846485cab4c954f3be8 ts=2026-09-23T18:19:50.2610000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 57 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 57} 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[11] _id=6ab415eb485cab4c954f3674 ts=2026-09-23T18:09:47.8450000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[1] _id=6ab41844485cab4c954f3be1 ts=2026-09-23T18:19:48.8300000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[6] _id=6ab4186c485cab4c954f3ce4 ts=2026-09-23T18:20:28.7870000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 8 of 54 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9829] _id=6ac3e81cde269131f9aec4cb ts=2026-09-23T18:33:59.675Z`; `6aa4144c41b41dbac0c7f26f.jsonl[9851] _id=6ac3e81cde269131f9aec4cf ts=2026-09-23T18:34:01.902Z`; `6aa4144c41b41dbac0c7f26f.jsonl[541] _id=6ab6bbcf485cab4c955e1895 ts=2026-09-25T18:22:07.2420000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 8245 | 0.0 | 0.44 | 155.858 | 6.892 | 344953.464 | 0.38 | 381 | 16 |
| PuzzlePieceVisibleEvent | 5241 | 0.0 | 0.042 | 211.884 | 1.122 | 357745.363 | 0.28 | 2810 | 13 |
| PlayerPositionEvent | 2506 | 0.47 | 9.999 | 449.347 | 10.033 | 344131.033 | 0.13 | 0 | 14 |
| DialogueEvent | 2066 | 0.0 | 4.347 | 622.011 | 48.172 | 344142.925 | 0.1 | 593 | 17 |
| argumentationNodeEvent | 616 | 0.008 | 0.288 | 980.845 | 6.014 | 357077.542 | 0.06 | 146 | 3 |
| ObjectInterEvent | 369 | 0.0 | 7.624 | 3479.323 | 441.821 | 345149.565 | 0.02 | 5 | 17 |
| questEvent | 94 | 0.0 | 200.161 | 13665.191 | 76018.325 | 345413.433 | 0.0 | 16 | 23 |
| gameWindowFocusEvent | 79 | 1.533 | 250.724 | 16248.895 | 83483.251 | 344125.849 | 0.0 | 0 | 29 |
| Soil Key Puzzle | 77 | 0.171 | 1.089 | 12336.243 | 17421.55 | 432114.381 | 0.0 | 0 | 4 |
| argumentationAnswerEvent | 69 | 0.131 | 2.964 | 8755.652 | 114.264 | 357131.194 | 0.01 | 0 | 3 |
| gameWindowUnfocusEvent | 56 | 0.0 | 159.776 | 22921.724 | 105755.218 | 344306.146 | 0.0 | 1 | 23 |
| TopographicMapEvent | 53 | 0.019 | 8.74 | 20959.953 | 164506.193 | 345871.766 | 0.0 | 2 | 7 |
| WaterChamberEvent | 52 | 0.517 | 3.796 | 10.394 | 41.569 | 75.891 | 5.77 | 0 | 0 |
| DEBUGMenu | 43 | 5.679 | 655.981 | 29843.814 | 153552.374 | 346118.304 | 0.0 | 0 | 22 |
| gameStartEvent | 31 | 65.946 | 1827.929 | 41408.475 | 209931.415 | 346116.184 | 0.0 | 0 | 21 |
| soilMachine | 21 | 0.686 | 9.595 | 3433.607 | 251.982 | 71374.9 | 0.02 | 0 | 1 |
| argumentationEvent | 8 | 0.022 | 403.002 | 75525.195 | 292962.995 | 357149.091 | 0.0 | 2 | 4 |
| SolarStillDesignEvent | 7 | 1.283 | 2.303 | 3.13 | 7.081 | 8.57 | 19.17 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| chatEvent | 1 | 825.031 | 825.031 | 825.031 | 825.031 | 825.031 | 0.07 | 0 | 1 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 5 group(s), 7 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[14] _id=6ab41763485cab4c954f372e ts=2026-09-23T18:16:03.0640000Z == 6aa4144c41b41dbac0c7f26f.jsonl[24] _id=6ab41764485cab4c954f3738 ts=2026-09-23T18:16:03.0640000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[15658] _id=6ac65a03de269131f9baff91 ts=2026-10-07T14:41:08.5280000Z == 6aa4144c41b41dbac0c7f26f.jsonl[15659] _id=6ac65a03de269131f9baff92 ts=2026-10-07T14:41:08.5280000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[15660] _id=6ac65a03de269131f9baff93 ts=2026-10-07T14:41:08.5290000Z == 6aa4144c41b41dbac0c7f26f.jsonl[15661] _id=6ac65a03de269131f9baff94 ts=2026-10-07T14:41:08.5290000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 238 group(s), 343 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[510] _id=6ab6bbb2485cab4c955e161b ts=2026-09-25T18:21:37.0880000Z == 6aa4144c41b41dbac0c7f26f.jsonl[515] _id=6ab6bbb2485cab4c955e161d ts=2026-09-25T18:21:37.0880000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[580] _id=6ab6bc64485cab4c955e2411 ts=2026-09-25T18:24:35.4000000Z == 6aa4144c41b41dbac0c7f26f.jsonl[588] _id=6ab6bc64485cab4c955e2413 ts=2026-09-25T18:24:35.4000000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[593] _id=6ab6bc64485cab4c955e241b ts=2026-09-25T18:24:35.5330000Z == 6aa4144c41b41dbac0c7f26f.jsonl[583] _id=6ab6bc64485cab4c955e241d ts=2026-09-25T18:24:35.5330000Z`
- **WARNING / Medium** `questEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[19548] _id=6ac7b123de269131f9c2f6d7 ts=2026-10-08T15:05:07.7480000Z == 6aa4144c41b41dbac0c7f26f.jsonl[19549] _id=6ac7b123de269131f9c2f6d8 ts=2026-10-08T15:05:07.7480000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `13ms: 6aa4144c41b41dbac0c7f26f.jsonl[9877] _id=6ac3e821de269131f9aec5cc ts=2026-09-23T18:35:43.152Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[9921] _id=6ac3e821de269131f9aec5cf ts=2026-09-23T18:35:43.165Z`; `4ms: 6aa4144c41b41dbac0c7f26f.jsonl[97] _id=6ab56341485cab4c9553acb8 ts=2026-09-24T17:52:01.1570000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[101] _id=6ab56341485cab4c9553acbe ts=2026-09-24T17:52:01.1610000Z`; `286ms: 6aa4144c41b41dbac0c7f26f.jsonl[10707] _id=6ac3ee99de269131f9af2fab ts=2026-10-05T18:38:17.6030000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[10699] _id=6ac3ee99de269131f9af2fbc ts=2026-10-05T18:38:17.8890000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 869 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `136ms: 6aa4144c41b41dbac0c7f26f.jsonl[498] _id=6ab6bbb1485cab4c955e1601 ts=2026-09-25T18:21:36.7410000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[513] _id=6ab6bbb1485cab4c955e1603 ts=2026-09-25T18:21:36.8770000Z`; `31ms: 6aa4144c41b41dbac0c7f26f.jsonl[513] _id=6ab6bbb1485cab4c955e1603 ts=2026-09-25T18:21:36.8770000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[514] _id=6ab6bbb1485cab4c955e1607 ts=2026-09-25T18:21:36.9080000Z`; `131ms: 6aa4144c41b41dbac0c7f26f.jsonl[533] _id=6ab6bbb4485cab4c955e1657 ts=2026-09-25T18:21:38.4090000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[527] _id=6ab6bbb4485cab4c955e1659 ts=2026-09-25T18:21:38.5400000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `19ms: 6aa4144c41b41dbac0c7f26f.jsonl[3064] _id=6abab16e485cab4c956ffce7 ts=2026-09-28T18:26:54.0690000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[3066] _id=6abab16e485cab4c956ffcf3 ts=2026-09-28T18:26:54.0880000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `605ms: 6aa4144c41b41dbac0c7f26f.jsonl[10310] _id=6ac3ebfede269131f9af00f5 ts=2026-10-05T18:27:10.6860000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[10309] _id=6ac3ebffde269131f9af0109 ts=2026-10-05T18:27:11.2910000Z`; `481ms: 6aa4144c41b41dbac0c7f26f.jsonl[17747] _id=6ac6939dde269131f9be0a5d ts=2026-10-07T18:46:53.8860000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[17572] _id=6ac6939ede269131f9be0a71 ts=2026-10-07T18:46:54.3670000Z`; `185ms: 6aa4144c41b41dbac0c7f26f.jsonl[17572] _id=6ac6939ede269131f9be0a71 ts=2026-10-07T18:46:54.3670000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[17573] _id=6ac6939ede269131f9be0a77 ts=2026-10-07T18:46:54.5520000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6aa4144c41b41dbac0c7f26f.jsonl[10389] _id=6ac3ec72de269131f9af0ae7 ts=2026-10-05T18:29:06.0900000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[10330] _id=6ac3ec72de269131f9af0af3 ts=2026-10-05T18:29:06.1190000Z`; `22ms: 6aa4144c41b41dbac0c7f26f.jsonl[18196] _id=6ac695b9de269131f9be7ad4 ts=2026-10-07T18:55:53.3430000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[18199] _id=6ac695b9de269131f9be7ad7 ts=2026-10-07T18:55:53.3650000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 112 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `147ms: 6aa4144c41b41dbac0c7f26f.jsonl[8827] _id=6abe78c3485cab4c95a9f4a2 ts=2026-10-01T15:14:11.4750000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[8820] _id=6abe78c3485cab4c95a9f4ac ts=2026-10-01T15:14:11.6220000Z`; `143ms: 6aa4144c41b41dbac0c7f26f.jsonl[8819] _id=6abe78c3485cab4c95a9f4a8 ts=2026-10-01T15:14:11.5070000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[8831] _id=6abe78c3485cab4c95a9f4b0 ts=2026-10-01T15:14:11.6500000Z`; `334ms: 6aa4144c41b41dbac0c7f26f.jsonl[8820] _id=6abe78c3485cab4c95a9f4ac ts=2026-10-01T15:14:11.6220000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[8829] _id=6abe78c3485cab4c95a9f4b8 ts=2026-10-01T15:14:11.9560000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `160ms: 6aa4144c41b41dbac0c7f26f.jsonl[6] _id=6ab4186c485cab4c954f3ce4 ts=2026-09-23T18:20:28.7870000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[9] _id=6ab4186c485cab4c954f3cec ts=2026-09-23T18:20:28.9470000Z`; `0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17293] _id=6ac665acde269131f9bbdf80 ts=2026-10-07T15:30:52.7610000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[17295] _id=6ac665bcde269131f9bbe099 ts=2026-10-07T15:30:52.761Z`; `376ms: 6aa4144c41b41dbac0c7f26f.jsonl[17384] _id=6ac691b1de269131f9bdd947 ts=2026-10-07T18:38:41.5680000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[17383] _id=6ac691b2de269131f9bdd959 ts=2026-10-07T18:38:41.9440000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4144c41b41dbac0c7f26f.jsonl[5385] _id=6abe5566485cab4c95a3dbff ts=2026-10-01T12:43:16.6070000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[5390] _id=6abe5566485cab4c95a3dc01 ts=2026-10-01T12:43:16.6110000Z`; `3ms: 6aa4144c41b41dbac0c7f26f.jsonl[5472] _id=6abe55f4485cab4c95a3dfd3 ts=2026-10-01T12:45:40.4300000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[5475] _id=6abe55f4485cab4c95a3dfd5 ts=2026-10-01T12:45:40.4330000Z`; `5ms: 6aa4144c41b41dbac0c7f26f.jsonl[6513] _id=6abe714a485cab4c95a91380 ts=2026-10-01T14:42:16.8600000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[6514] _id=6abe714a485cab4c95a91382 ts=2026-10-01T14:42:16.8650000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `686ms: 6aa4144c41b41dbac0c7f26f.jsonl[15849] _id=6ac65a82de269131f9bb0844 ts=2026-10-07T14:43:15.9040000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[15843] _id=6ac65a83de269131f9bb085d ts=2026-10-07T14:43:16.5900000Z`; `911ms: 6aa4144c41b41dbac0c7f26f.jsonl[15843] _id=6ac65a83de269131f9bb085d ts=2026-10-07T14:43:16.5900000Z ~ 6aa4144c41b41dbac0c7f26f.jsonl[15855] _id=6ac65a84de269131f9bb086c ts=2026-10-07T14:43:17.5010000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 96h 8m 
  - Evidence: 96h 8m: 6aa4144c41b41dbac0c7f26f.jsonl[6507] _id=6abe7142485cab4c95a9125e ts=2026-10-01T14:42:10.6730000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8922] _id=6ac3b940de269131f9acb133 ts=2026-10-05T14:50:48.9770000Z; 71h 56m: 6aa4144c41b41dbac0c7f26f.jsonl[352] _id=6ab6ba10485cab4c955dd346 ts=2026-09-25T18:14:40.7740000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1578] _id=6abaadc7485cab4c956f91d5 ts=2026-09-28T18:11:19.8940000Z; 44h 41m: 6aa4144c41b41dbac0c7f26f.jsonl[1578] _id=6abaadc7485cab4c956f91d5 ts=2026-09-28T18:11:19.8940000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3339] _id=6abd222b485cab4c958b89cf ts=2026-09-30T14:52:27.7370000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa4144c41b41dbac0c7f26f.jsonl[8911] _id=6abe7900485cab4c95a9fce4 ts=2026-10-01T15:15:12.6220000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8924] _id=6ac3b948de269131f9acb18f ts=2026-10-05T14:50:55.5470000Z; 71h 30m: 6aa4144c41b41dbac0c7f26f.jsonl[1575] _id=6ab6c059485cab4c955e65bb ts=2026-09-25T18:41:30.0550000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1608] _id=6abaade4485cab4c956f979f ts=2026-09-28T18:11:48.1400000Z; 44h 5m: 6aa4144c41b41dbac0c7f26f.jsonl[3318] _id=6abab621485cab4c95705f53 ts=2026-09-28T18:46:57.2190000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3353] _id=6abd2243485cab4c958b8a4f ts=2026-09-30T14:52:51.7040000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 593 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17636] _id=6ac69349de269131f9bdffb7 ts=2026-10-07T18:45:29.9010000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17637] _id=6ac69349de269131f9bdffb8 ts=2026-10-07T18:45:29.9010000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17713] _id=6ac69385de269131f9be0748 ts=2026-10-07T18:46:29.2320000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17714] _id=6ac69385de269131f9be0749 ts=2026-10-07T18:46:29.2320000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17852] _id=6ac693e9de269131f9be16a0 ts=2026-10-07T18:48:09.8600000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17853] _id=6ac693e9de269131f9be16a1 ts=2026-10-07T18:48:09.8600000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 49m 
  - Evidence: 95h 49m: 6aa4144c41b41dbac0c7f26f.jsonl[8783] _id=6abe7839485cab4c95a9e536 ts=2026-10-01T15:11:53.3990000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[9021] _id=6ac3bbb2de269131f9acc3d4 ts=2026-10-05T15:01:06.8630000Z; 71h 39m: 6aa4144c41b41dbac0c7f26f.jsonl[1501] _id=6ab6be23485cab4c955e485f ts=2026-09-25T18:32:03.9020000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1580] _id=6abaadce485cab4c956f937b ts=2026-09-28T18:11:26.2470000Z; 44h 5m: 6aa4144c41b41dbac0c7f26f.jsonl[3323] _id=6abab63b485cab4c95706282 ts=2026-09-28T18:47:23.5960000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3338] _id=6abd2234485cab4c958b89f3 ts=2026-09-30T14:52:34.8310000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 381 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[11756] _id=6ac507dede269131f9b3828e ts=2026-10-06T14:38:21.9260000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[11782] _id=6ac507dede269131f9b38291 ts=2026-10-06T14:38:21.9260000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[14] _id=6ab41763485cab4c954f372e ts=2026-09-23T18:16:03.0640000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[24] _id=6ab41764485cab4c954f3738 ts=2026-09-23T18:16:03.0640000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[15658] _id=6ac65a03de269131f9baff91 ts=2026-10-07T14:41:08.5280000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[15659] _id=6ac65a03de269131f9baff92 ts=2026-10-07T14:41:08.5280000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 6aa4144c41b41dbac0c7f26f.jsonl[8767] _id=6abe780d485cab4c95a9e03a ts=2026-10-01T15:11:09.8290000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[9100] _id=6ac3bc4bde269131f9accb6b ts=2026-10-05T15:03:39.3940000Z; 71h 42m: 6aa4144c41b41dbac0c7f26f.jsonl[1423] _id=6ab6bdc8485cab4c955e451f ts=2026-09-25T18:30:32.4840000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1641] _id=6abaae1e485cab4c956f9e09 ts=2026-09-28T18:12:46.3830000Z; 48h 4m: 6aa4144c41b41dbac0c7f26f.jsonl[2907] _id=6abaafbc485cab4c956fd305 ts=2026-09-28T18:19:40.0290000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[4709] _id=6abd53bf485cab4c95915893 ts=2026-09-30T18:23:58.9180000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 5 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17226] _id=6ac66539de269131f9bbd44a ts=2026-10-07T15:28:58.4000000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17227] _id=6ac66539de269131f9bbd44b ts=2026-10-07T15:28:58.4000000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17479] _id=6ac69237de269131f9bde24b ts=2026-10-07T18:40:56.3500000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17480] _id=6ac69237de269131f9bde24c ts=2026-10-07T18:40:56.3500000Z; 1ms: 6aa4144c41b41dbac0c7f26f.jsonl[17539] _id=6ac69279de269131f9bde84b ts=2026-10-07T18:42:01.5650000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17540] _id=6ac69279de269131f9bde84c ts=2026-10-07T18:42:01.5660000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa4144c41b41dbac0c7f26f.jsonl[8913] _id=6abe7906485cab4c95a9fdb0 ts=2026-10-01T15:15:17.9530000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8925] _id=6ac3b948de269131f9acb189 ts=2026-10-05T14:50:48.9860000Z; 71h 29m: 6aa4144c41b41dbac0c7f26f.jsonl[1572] _id=6ab6c05e485cab4c955e65d1 ts=2026-09-25T18:41:34.6140000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1579] _id=6abaadce485cab4c956f9373 ts=2026-09-28T18:11:19.9010000Z; 24h 0m: 6aa4144c41b41dbac0c7f26f.jsonl[332] _id=6ab5681f485cab4c95542330 ts=2026-09-24T18:12:47.4960000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[340] _id=6ab6b9a9485cab4c955dc899 ts=2026-09-25T18:12:51.8220000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 99h 22m 
  - Evidence: 99h 22m: 6aa4144c41b41dbac0c7f26f.jsonl[8781] _id=6abe7835485cab4c95a9e4a6 ts=2026-10-01T15:11:49.3120000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[10629] _id=6ac3eda7de269131f9af217f ts=2026-10-05T18:34:14.6750000Z; 71h 45m: 6aa4144c41b41dbac0c7f26f.jsonl[1307] _id=6ab6bd30485cab4c955e3d03 ts=2026-09-25T18:27:57.9740000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1800] _id=6abaaecd485cab4c956fae1b ts=2026-09-28T18:13:20.1790000Z; 44h 44m: 6aa4144c41b41dbac0c7f26f.jsonl[2885] _id=6abaaf8b485cab4c956fcd28 ts=2026-09-28T18:18:49.4150000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3522] _id=6abd24a9485cab4c958ba629 ts=2026-09-30T15:03:04.6890000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2810 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[1017] _id=6ab6bce0485cab4c955e3425 ts=2026-09-25T18:26:39.1270000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1012] _id=6ab6bce0485cab4c955e3427 ts=2026-09-25T18:26:39.1270000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[1018] _id=6ab6bce0485cab4c955e3429 ts=2026-09-25T18:26:39.1880000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1019] _id=6ab6bce0485cab4c955e342d ts=2026-09-25T18:26:39.1880000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[1020] _id=6ab6bce0485cab4c955e3433 ts=2026-09-25T18:26:39.2650000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1021] _id=6ab6bce0485cab4c955e3437 ts=2026-09-25T18:26:39.2650000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 120h 1m 
  - Evidence: 120h 1m: 6aa4144c41b41dbac0c7f26f.jsonl[5144] _id=6abd5558485cab4c95919bc5 ts=2026-09-30T18:30:48.8230000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[10609] _id=6ac3ed4bde269131f9af1be5 ts=2026-10-05T18:32:43.2040000Z; 71h 49m: 6aa4144c41b41dbac0c7f26f.jsonl[1431] _id=6ab6bdcb485cab4c955e4539 ts=2026-09-25T18:30:35.4440000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[2910] _id=6abaafbc485cab4c956fd303 ts=2026-09-28T18:19:40.0240000Z; 48h 4m: 6aa4144c41b41dbac0c7f26f.jsonl[2911] _id=6abaafbf485cab4c956fd341 ts=2026-09-28T18:19:42.9970000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[4726] _id=6abd53be485cab4c9591588d ts=2026-09-30T18:23:58.9140000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 4m 
  - Evidence: 96h 4m: 6aa4144c41b41dbac0c7f26f.jsonl[8315] _id=6abe752c485cab4c95a98398 ts=2026-10-01T14:58:52.5640000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[9094] _id=6ac3bc3cde269131f9acca9f ts=2026-10-05T15:03:24.3300000Z; 71h 51m: 6aa4144c41b41dbac0c7f26f.jsonl[557] _id=6ab6bbff485cab4c955e1b57 ts=2026-09-25T18:22:55.9190000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1742] _id=6abaae80485cab4c956fa859 ts=2026-09-28T18:14:24.6460000Z; 47h 48m: 6aa4144c41b41dbac0c7f26f.jsonl[9851] _id=6ac3e81cde269131f9aec4cf ts=2026-09-23T18:34:01.902Z -> 6aa4144c41b41dbac0c7f26f.jsonl[541] _id=6ab6bbcf485cab4c955e1895 ts=2026-09-25T18:22:07.2420000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.019s..0.019s shown 
  - Evidence: 19ms: 6aa4144c41b41dbac0c7f26f.jsonl[3064] _id=6abab16e485cab4c956ffce7 ts=2026-09-28T18:26:54.0690000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3066] _id=6abab16e485cab4c956ffcf3 ts=2026-09-28T18:26:54.0880000Z; 19ms: 6aa4144c41b41dbac0c7f26f.jsonl[3067] _id=6abab16e485cab4c956ffce4 ts=2026-09-28T18:26:54.0500000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3064] _id=6abab16e485cab4c956ffce7 ts=2026-09-28T18:26:54.0690000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 99h 12m 
  - Evidence: 99h 12m: 6aa4144c41b41dbac0c7f26f.jsonl[8898] _id=6abe78f3485cab4c95a9fb14 ts=2026-10-01T15:14:59.4920000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[10310] _id=6ac3ebfede269131f9af00f5 ts=2026-10-05T18:27:10.6860000Z; 48h 16m: 6aa4144c41b41dbac0c7f26f.jsonl[10388] _id=6ac3ec72de269131f9af0ae3 ts=2026-10-05T18:29:06.0510000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17641] _id=6ac69349de269131f9bdffb5 ts=2026-10-07T18:45:29.8780000Z; 20h 7m: 6aa4144c41b41dbac0c7f26f.jsonl[18195] _id=6ac695b9de269131f9be7acc ts=2026-10-07T18:55:53.3170000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[19424] _id=6ac7b0d4de269131f9c2ea1a ts=2026-10-08T15:03:48.6270000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 99h 12m 
  - Evidence: 99h 12m: 6aa4144c41b41dbac0c7f26f.jsonl[8815] _id=6abe78b6485cab4c95a9f2fb ts=2026-10-01T15:13:57.9750000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[10259] _id=6ac3ebd3de269131f9aefccb ts=2026-10-05T18:26:27.0660000Z; 48h 16m: 6aa4144c41b41dbac0c7f26f.jsonl[10330] _id=6ac3ec72de269131f9af0af3 ts=2026-10-05T18:29:06.1190000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17594] _id=6ac69332de269131f9bdfc48 ts=2026-10-07T18:45:06.3640000Z; 20h 7m: 6aa4144c41b41dbac0c7f26f.jsonl[18199] _id=6ac695b9de269131f9be7ad7 ts=2026-10-07T18:55:53.3650000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[19438] _id=6ac7b0a9de269131f9c2e3f4 ts=2026-10-08T15:03:05.1930000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.029s shown 
  - Evidence: 22ms: 6aa4144c41b41dbac0c7f26f.jsonl[18196] _id=6ac695b9de269131f9be7ad4 ts=2026-10-07T18:55:53.3430000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[18199] _id=6ac695b9de269131f9be7ad7 ts=2026-10-07T18:55:53.3650000Z; 29ms: 6aa4144c41b41dbac0c7f26f.jsonl[10389] _id=6ac3ec72de269131f9af0ae7 ts=2026-10-05T18:29:06.0900000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[10330] _id=6ac3ec72de269131f9af0af3 ts=2026-10-05T18:29:06.1190000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 99h 11m 
  - Evidence: 99h 11m: 6aa4144c41b41dbac0c7f26f.jsonl[8910] _id=6abe78fc485cab4c95a9fc45 ts=2026-10-01T15:15:08.3150000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[10256] _id=6ac3ebd1de269131f9aefc9d ts=2026-10-05T18:26:25.8570000Z; 48h 16m: 6aa4144c41b41dbac0c7f26f.jsonl[10369] _id=6ac3ec70de269131f9af0ad3 ts=2026-10-05T18:29:04.3010000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17596] _id=6ac69330de269131f9bdfc09 ts=2026-10-07T18:45:05.0110000Z; 20h 7m: 6aa4144c41b41dbac0c7f26f.jsonl[18194] _id=6ac695b8de269131f9be7a9f ts=2026-10-07T18:55:52.3180000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[19443] _id=6ac7b0aade269131f9c2e420 ts=2026-10-08T15:03:06.7410000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 146 interval(s) ≤ 0.008s..0.019s shown 
  - Evidence: 8ms: 6aa4144c41b41dbac0c7f26f.jsonl[19453] _id=6ac7b0b0de269131f9c2e4c8 ts=2026-10-08T15:03:12.7100000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[19454] _id=6ac7b0b0de269131f9c2e4ca ts=2026-10-08T15:03:12.7180000Z; 18ms: 6aa4144c41b41dbac0c7f26f.jsonl[18066] _id=6ac69545de269131f9be5cf8 ts=2026-10-07T18:53:57.0420000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[18067] _id=6ac69545de269131f9be5cf9 ts=2026-10-07T18:53:57.0600000Z; 19ms: 6aa4144c41b41dbac0c7f26f.jsonl[17738] _id=6ac69399de269131f9be09a4 ts=2026-10-07T18:46:49.2730000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17739] _id=6ac69399de269131f9be09ad ts=2026-10-07T18:46:49.2920000Z
- **INFO / Info** `chatEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 13m 45s 
  - Evidence: 13m 45s: 6aa4144c41b41dbac0c7f26f.jsonl[18278] _id=6ac7ac32de269131f9c2405a ts=2026-10-08T14:44:01.5520000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[19234] _id=6ac7af6ade269131f9c2b12f ts=2026-10-08T14:57:46.5830000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 21 gap(s), longest 96h 8m 
  - Evidence: 96h 8m: 6aa4144c41b41dbac0c7f26f.jsonl[6493] _id=6abe713b485cab4c95a91190 ts=2026-10-01T14:42:04.3740000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8921] _id=6ac3b938de269131f9acb0e1 ts=2026-10-05T14:50:40.5580000Z; 71h 56m: 6aa4144c41b41dbac0c7f26f.jsonl[354] _id=6ab6ba09485cab4c955dd2df ts=2026-09-25T18:14:33.9120000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1576] _id=6abaadc1485cab4c956f9090 ts=2026-09-28T18:11:13.0190000Z; 44h 41m: 6aa4144c41b41dbac0c7f26f.jsonl[1576] _id=6abaadc1485cab4c956f9090 ts=2026-09-28T18:11:13.0190000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3337] _id=6abd2220485cab4c958b8991 ts=2026-09-30T14:52:16.7410000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 29 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa4144c41b41dbac0c7f26f.jsonl[8909] _id=6abe7902485cab4c95a9fd3f ts=2026-10-01T15:15:14.7080000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8920] _id=6ac3b938de269131f9acb0df ts=2026-10-05T14:50:40.5570000Z; 71h 29m: 6aa4144c41b41dbac0c7f26f.jsonl[1574] _id=6ab6c058485cab4c955e65ab ts=2026-09-25T18:41:28.3310000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1577] _id=6abaadc1485cab4c956f907b ts=2026-09-28T18:11:13.0180000Z; 44h 4m: 6aa4144c41b41dbac0c7f26f.jsonl[3326] _id=6abab64a485cab4c95706765 ts=2026-09-28T18:47:38.5650000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3336] _id=6abd2220485cab4c958b898d ts=2026-09-30T14:52:16.7400000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa4144c41b41dbac0c7f26f.jsonl[8912] _id=6abe7902485cab4c95a9fd33 ts=2026-10-01T15:15:14.6970000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8948] _id=6ac3b9eede269131f9acb569 ts=2026-10-05T14:53:40.8430000Z; 71h 33m: 6aa4144c41b41dbac0c7f26f.jsonl[1571] _id=6ab6c058485cab4c955e65a7 ts=2026-09-25T18:41:28.3110000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1748] _id=6abaaea2485cab4c956faae8 ts=2026-09-28T18:14:58.5540000Z; 44h 22m: 6aa4144c41b41dbac0c7f26f.jsonl[3325] _id=6abab64a485cab4c9570675e ts=2026-09-28T18:47:38.5520000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3825] _id=6abd2634485cab4c958bc569 ts=2026-09-30T15:09:40.8140000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[17293] _id=6ac665acde269131f9bbdf80 ts=2026-10-07T15:30:52.7610000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[17295] _id=6ac665bcde269131f9bbe099 ts=2026-10-07T15:30:52.761Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 23 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 6aa4144c41b41dbac0c7f26f.jsonl[8219] _id=6abe740a485cab4c95a975ed ts=2026-10-01T14:54:02.1040000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[8926] _id=6ac3b948de269131f9acb18b ts=2026-10-05T14:50:55.5370000Z; 71h 39m: 6aa4144c41b41dbac0c7f26f.jsonl[1505] _id=6ab6be2c485cab4c955e48a1 ts=2026-09-25T18:32:12.3980000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[1582] _id=6abaadce485cab4c956f937f ts=2026-09-28T18:11:26.2670000Z; 44h 26m: 6aa4144c41b41dbac0c7f26f.jsonl[3054] _id=6abab155485cab4c956ffb93 ts=2026-09-28T18:26:29.1730000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[3356] _id=6abd2243485cab4c958b8a4d ts=2026-09-30T14:52:51.6840000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[18787] _id=6ac7ad8dde269131f9c2734d ts=2026-10-08T14:49:49.6640000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[18788] _id=6ac7ad8dde269131f9c2734e ts=2026-10-08T14:49:49.6640000Z; 0ms: 6aa4144c41b41dbac0c7f26f.jsonl[19548] _id=6ac7b123de269131f9c2f6d7 ts=2026-10-08T15:05:07.7480000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[19549] _id=6ac7b123de269131f9c2f6d8 ts=2026-10-08T15:05:07.7480000Z; 2ms: 6aa4144c41b41dbac0c7f26f.jsonl[18984] _id=6ac7ae89de269131f9c2915a ts=2026-10-08T14:54:01.6560000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[18986] _id=6ac7ae89de269131f9c29166 ts=2026-10-08T14:54:01.6580000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 19h 49m 
  - Evidence: 19h 49m: 6aa4144c41b41dbac0c7f26f.jsonl[15604] _id=6ac543b1de269131f9b70987 ts=2026-10-06T18:53:37.3820000Z -> 6aa4144c41b41dbac0c7f26f.jsonl[15824] _id=6ac65a7fde269131f9bb0814 ts=2026-10-07T14:43:12.2820000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9720] _id=6ac3e812de269131f9aec327 ts=2026-09-23T18:27:48.619Z`; `6aa4144c41b41dbac0c7f26f.jsonl[8003] _id=6abe72f4485cab4c95a962ec ts=2026-10-01T14:49:24.9720000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[8252] _id=6abe7489485cab4c95a97dc6 ts=2026-10-01T14:56:09.8530000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 119 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[798] _id=6ab6bcb0485cab4c955e2d4f ts=2026-09-25T18:25:51.5890000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[820] _id=6ab6bcb3485cab4c955e2da7 ts=2026-09-25T18:25:54.3100000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[872] _id=6ab6bcc1485cab4c955e2fcd ts=2026-09-25T18:26:09.0550000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 264 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[660] _id=6ab6bc82485cab4c955e2701 ts=2026-09-25T18:21:27.0150000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[520] _id=6ab6bbb3485cab4c955e1631 ts=2026-09-25T18:21:37.4010000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[534] _id=6ab6bbb5485cab4c955e1665 ts=2026-09-25T18:21:38.9170000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` `actionType` — map open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'MapCloseEvent' preceded by 'MapOpenEvent' 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9829] _id=6ac3e81cde269131f9aec4cb ts=2026-09-23T18:33:59.675Z`; `6aa4144c41b41dbac0c7f26f.jsonl[9851] _id=6ac3e81cde269131f9aec4cf ts=2026-09-23T18:34:01.902Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[10330] _id=6ac3ec72de269131f9af0af3 ts=2026-10-05T18:29:06.1190000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[18199] _id=6ac695b9de269131f9be7ad7 ts=2026-10-07T18:55:53.3650000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `chatEvent` `actionType` — chat open/close: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Close' preceded by 'Open' 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[18278] _id=6ac7ac32de269131f9c2405a ts=2026-10-08T14:44:01.5520000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[19234] _id=6ac7af6ade269131f9c2b12f ts=2026-10-08T14:57:46.5830000Z` 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9881] _id=6ac3e81dde269131f9aec50b ts=2026-09-23T18:34:12.935Z`; `6aa4144c41b41dbac0c7f26f.jsonl[10001] _id=6ac3e824de269131f9aec667 ts=2026-09-23T18:44:33.948Z`; `6aa4144c41b41dbac0c7f26f.jsonl[14919] _id=6ac541e2de269131f9b6d75a ts=2026-10-06T18:45:54.8000000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[68] _id=6ab56309485cab4c9553a6d4 ts=?`; `6aa4144c41b41dbac0c7f26f.jsonl[1581] _id=6abaadce485cab4c956f936a ts=?`; `6aa4144c41b41dbac0c7f26f.jsonl[8919] _id=6ac3b947de269131f9acb185 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 679 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[866] _id=6ab6bcbf485cab4c955e2f71 ts=2026-09-25T18:26:07.0120000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[851] _id=6ab6bcbf485cab4c955e2f73 ts=2026-09-25T18:26:07.2060000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[884] _id=6ab6bcc3485cab4c955e3019 ts=2026-09-25T18:26:09.9090000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1190 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[458] _id=6ab6bc83485cab4c955e2750 ts=2026-09-25T18:21:29.0560000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[513] _id=6ab6bbb1485cab4c955e1603 ts=2026-09-25T18:21:36.8770000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[514] _id=6ab6bbb1485cab4c955e1607 ts=2026-09-25T18:21:36.9080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 15 occurrence(s) 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[3064] _id=6abab16e485cab4c956ffce7 ts=2026-09-28T18:26:54.0690000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[3066] _id=6abab16e485cab4c956ffcf3 ts=2026-09-28T18:26:54.0880000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[3202] _id=6abab37c485cab4c95702239 ts=2026-09-28T18:35:40.7900000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'DialogueStartEvent' (totals: 413 start, 405 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 215 unmatched 'BecameCameraCentered' (totals: 968 open, 872 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 134 unmatched 'BecameVisible' (totals: 1636 open, 1766 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 18 open, 18 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 40 unmatched 'questActiveEvent' (totals: 65 start, 30 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 772 of 19665 adjacent _id pairs reverse in client time; worst 1025309.3s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4144c41b41dbac0c7f26f.jsonl[9693] _id=6ac3bebfde269131f9ace301 ts=2026-10-05T15:14:07.5610000Z`; `6aa4144c41b41dbac0c7f26f.jsonl[9709] _id=6ac3e810de269131f9aec2bd ts=2026-09-23T18:25:38.233Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -1035886.26s, max +8.01s over 19666 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4144c41b41dbac0c7f26f\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | partial |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=complete, Unit5=partial 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `InputEvent` — 8246 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (2763); Unit 4 Dev - Dungeon (1844); Unit 3 Dungeon Dev (1251); Unit 3 Dev (986); Unit 5 Dev - Dungeon (464); Unit 4 Dev (313); Unit 4 Dev - Anderson Base (275); Unit 1 Dev (213); Unit 5 Dev (137)
- **Intervals:** median 0.44s (p5 0.05s / p95 6.89s, n=8245)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 8246/8246 records)
    "pressed"  x8246
data.actionType  (string, 8246/8246 records)
    "Move"  x6059
    "Jump"  x925
    "Interact"  x729
    "Sprint"  x360
    "Ascend"  x112
    "Hoverboard"  x43
    "Map"  x8
    "SkipCinematic"  x6
    "Descend"  x3
    "Pause"  x1
data.key  (string, 8246/8246 records, 5 empty-string)
    19 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 8246/8246 records)
    "Player"  x7321
    "Drone"  x925
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 5242 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3904); Unit 4 Dev (626); Unit 3 Dungeon Dev (442); Unit 5 Dev - Dungeon (270)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.12s, n=5241)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5242/5242 records)
    "BecameInvisible"  x1766
    "BecameVisible"  x1636
    "BecameCameraCentered"  x968
    "BecameCameraUncentered"  x872
data.pieceId  (string, 5242/5242 records)
    40 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5242/5242 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2519 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (922); Unit 3 Dev (344); Unit 1 Dev (313); Unit 3 Dungeon Dev (241); Unit 4 Dev - Dungeon (219); Unit 4 Dev - Anderson Base (167); Unit 4 Dev (137); Unit 5 Dev (94); Unit 5 Dev - Dungeon (82)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2506)
- **Fields under `data`:**

```text
data.position  (object, 2519/2519 records)
data.position.x  (number, 2519/2519 records)
    numeric range -558.38 .. 1438.36 (871 unique)
data.position.y  (number, 2519/2519 records)
    numeric range -112.48 .. 253.017 (613 unique)
data.position.z  (number, 2519/2519 records)
    numeric range -1119.19 .. 2225.56 (872 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2067 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (638); Unit 3 Dev (343); Unit 3 Dungeon Dev (265); Unit 4 Dev - Anderson Base (188); Unit 4 Dev - Dungeon (171); Unit 4 Dev (135); Unit 5 Dev (132); Unit 1 Dev (126); Unit 5 Dev - Dungeon (69)
- **eventKey:** present on 1249 of 2067 records
- **Intervals:** median 4.35s (p5 0.00s / p95 48.17s, n=2066)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1249; [conversationId, dialogueEventType] x818
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2067/2067 records)
    numeric range 8 .. 117 (47 unique)
data.dialogueEventType  (string, 2067/2067 records)
    "DialogueNodeEvent"  x1249
    "DialogueStartEvent"  x413
    "DialogueFinishEvent"  x405
data.nodeId  (number, 1249/2067 records)
    numeric range 0 .. 290 (225 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 617 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (391); Unit 3 Dev (91); Unit 2 Prod (Refactor) (83); Unit 5 Dev (52)
- **Intervals:** median 0.29s (p5 0.02s / p95 6.01s, n=616)
- **Fields under `data`:**

```text
data.actionType  (string, 617/617 records)
    "argumentationNodeHoverEnd"  x270
    "argumentationNodeHoverStart"  x270
    "argumentationNodeAdd"  x46
    "argumentationNodeRemove"  x31
data.argumentationTitle  (string, 617/617 records)
    "Unit 4 - Flooding"  x391
    "Unit 3 - Pollution Upstream"  x91
    "Unit 2 – Watershed"  x83
    "Unit 5"  x52
data.nodeName  (string, 617/617 records)
    "B"  x116
    "A"  x88
    "D"  x63
    "C"  x62
    "II"  x59
    "3"  x53
    "2"  x47
    "4"  x44
    "1"  x41
    "I"  x39
    "5"  x5
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 370 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (124); Unit 2 Prod (Refactor) (88); Unit 3 Dungeon Dev (88); Unit 5 Dev - Dungeon (18); Unit 4 Dev - Anderson Base (17); Unit 3 Dev (14); Unit 1 Dev (8); Unit 4 Dev (8); Unit 5 Dev (5)
- **Intervals:** median 7.62s (p5 0.73s / p95 441.82s, n=369)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 370/370 records)
    35 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 370/370 records)
    98 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `questEvent` — 95 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (23); Unit 4 Dev - Dungeon (19); Unit 3 Dev (13); Unit 1 Dev (12); Unit 4 Dev (7); Unit 5 Dev - Dungeon (7); Unit 4 Dev - Anderson Base (6); Unit 3 Dungeon Dev (4); Unit 5 Dev (4)
- **eventKey:** present on 95 of 95 records
- **Intervals:** median 200.16s (p5 0.00s / p95 76018.33s, n=94)
- **`data` key-set variants:** [questEventType, questID, questName] x65; [questEventType, questID, questName, questSuccessOrFailure] x30
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 95/95 records)
    "questActiveEvent"  x65
    "questFinishEvent"  x30
data.questID  (string, 95/95 records)
    28 unique values (see csv/event_unique_values.csv)
data.questName  (string, 95/95 records)
    28 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 30/95 records)
    "Succeeded"  x30
```

Raw examples: `event_examples.json` -> `questEvent`.

### `gameWindowFocusEvent` — 80 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (32); Unit 2 Prod (Refactor) (24); Unit 1 Dev (8); Unit 4 Dev - Anderson Base (6); Unit 3 Dev (4); Unit 4 Dev - Dungeon (3); Transition (2); Unit 3 Dungeon Dev (1)
- **Intervals:** median 250.72s (p5 7.88s / p95 83483.25s, n=79)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 80/80 records)
    true  x80
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `Soil Key Puzzle` — 78 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (42); Unit 4 Dev (24); Unit 3 Dev (12)
- **Intervals:** median 1.09s (p5 0.20s / p95 17421.55s, n=77)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x66; [Soil Key Puzzle Status, Unit] x12
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 12/78 records)
    "Finished"  x6
    "Started"  x6
data.Unit  (string, 12/78 records)
    "Unit 2 Prod (Refactor)"  x8
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 66/78 records)
    "RightDrag"  x38
    "LeftDrag"  x28
data.currentSoilType  (string, 66/78 records)
    "SAND"  x15
    "CLAYSAND"  x14
    "SANDGRAVEL"  x13
    "CLAY"  x11
    "CLAYROCK"  x6
    "GRAVEL"  x6
    "BEDROCK"  x1
data.isCorrectSelection  (string, 66/78 records)
    "false"  x50
    "true"  x16
data.waterLevelStatus  (string, 66/78 records)
    "TooHigh"  x32
    "Proper"  x22
    "TooLow"  x12
data.waterRetentionChange  (string, 66/78 records)
    "Decrease"  x29
    "Increase"  x21
    "NoChange"  x16
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 70 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (61); Unit 3 Dev (6); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 2.96s (p5 0.20s / p95 114.26s, n=69)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 70/70 records)
    "submitAnswerEvent"  x70
data.answerSubmitted  (string, 70/70 records)
    23 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 70/70 records)
    "Unit 4 - Flooding"  x61
    "Unit 3 - Pollution Upstream"  x6
    "Unit 5"  x2
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 57 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (26); Unit 1 Dev (10); Unit 4 Dev - Anderson Base (10); Unit 3 Dev (4); Unit 4 Dev - Dungeon (3); Transition (2); MainMenu (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 159.78s (p5 1.07s / p95 105755.22s, n=56)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 57/57 records)
    false  x57
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `TopographicMapEvent` — 54 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (33); Unit 3 Dev (19); Unit 1 Dev (2)
- **Intervals:** median 8.74s (p5 0.43s / p95 164506.19s, n=53)
- **`data` key-set variants:** [actionType, featureUsed] x36; [actionType, featureUsed, location] x10; [actionType, featureUsed, legendName] x8
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 54/54 records)
    "MapCloseEvent"  x18
    "MapOpenEvent"  x18
    "Selected"  x8
    "WaypointMoveEvent"  x6
    "WaypointSetEvent"  x4
data.featureUsed  (string, 54/54 records)
    "Map"  x36
    "Waypoint"  x10
    "Legend"  x8
data.legendName  (string, 8/54 records)
    "180 ft"  x2
    "0 ft"  x1
    "120 ft"  x1
    "300 ft"  x1
    "330 ft"  x1
    "360 ft"  x1
    "90 ft"  x1
data.location  (object, 10/54 records)
data.location.x  (number, 10/54 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 10/54 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 10/54 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `WaterChamberEvent` — 53 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (53)
- **Intervals:** median 3.80s (p5 0.55s / p95 41.57s, n=52)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 53/53 records)
    "On"  x32
    "Off"  x21
data.floor  (string, 53/53 records)
    "4"  x35
    "3"  x9
    "1"  x6
    "2"  x3
data.machineNumber  (string, 53/53 records)
    "One"  x52
    "Two"  x1
data.machineType  (string, 53/53 records)
    "Evaporator"  x26
    "Condenser"  x22
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 53/53 records)
    "2"  x30
    "3"  x16
    "1"  x5
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `DEBUGMenu` — 44 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (10); MainMenu (9); Unit 4 Dev - Anderson Base (6); Unit 1 Dev (4); Unit 3 Dev (4); Unit 4 Dev - Dungeon (4); Unit 3 Dungeon Dev (3); Unit 4 Dev (3); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 655.98s (p5 6.68s / p95 153552.37s, n=43)
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "DebugMenuStateChanged"  x44
data.isOpened  (bool, 44/44 records)
    false  x44
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 32 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (32)
- **Intervals:** median 1827.93s (p5 107.48s / p95 209931.41s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 32/32 records)
    true  x32
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `soilMachine` — 22 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (22)
- **Intervals:** median 9.60s (p5 0.91s / p95 251.98s, n=21)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 22/22 records)
    "ChangeCanister"  x22
data.canisterType  (string, 22/22 records)
    "Gravel"  x7
    "Sand"  x7
    "Bedrock"  x4
    "Clay"  x4
data.floor  (string, 22/22 records)
    "3"  x9
    "5"  x8
    "4"  x5
data.machine  (string, 22/22 records)
    "1"  x20
    "2"  x2
data.row  (string, 22/22 records)
    "TopRow"  x21
    "BottomRow"  x1
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 9 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (3); Unit 4 Dev - Anderson Base (3); Unit 5 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 403.00s (p5 0.02s / p95 292962.99s, n=8)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 9/9 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 9/9 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x3
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x1
data.argumentationTitle  (string, 9/9 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 4 - Flooding"  x3
    "Unit 5"  x2
    "Unit 2 – Watershed"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `SolarStillDesignEvent` — 8 records

*Purpose:* Solar still design activity — option selections and final submitted design.

- **Scenes:** Unit 5 Dev (8)
- **Intervals:** median 2.30s (p5 1.30s / p95 7.08s, n=7)
- **`data` key-set variants:** [actionType, featureUsed, selectedOption] x7; [actionType, designSelections, featureUsed] x1
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "optionSelected"  x7
    "DesignSubmitted"  x1
data.designSelections  (object, 1/8 records)
data.designSelections.glassRoofTemperature  (string, 1/8 records)
    "Cold"  x1
data.designSelections.roofCovering  (string, 1/8 records)
    "Covered"  x1
data.designSelections.roofStyle  (string, 1/8 records)
    "Flat"  x1
data.featureUsed  (string, 8/8 records)
    "RoofStyle"  x5
    "ExtraCovering"  x1
    "GlassRoofTemperature"  x1
    "Submit"  x1
data.selectedOption  (string, 7/8 records, 2 empty-string)
    ""  x2
    "Tilted In"  x2
    "Cold"  x1
    "Covered"  x1
    "Flat"  x1
```

Raw examples: `event_examples.json` -> `SolarStillDesignEvent`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "A user gesture is required to request Pointer Lock."  x3
    "Permissions check failed"  x1
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x1
data.type  (string, 4/4 records)
    "unhandled_rejection"  x4
data.unitId  (string, 4/4 records)
    "unit2"  x2
    "unit1"  x1
    "unit4"  x1
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 5 Dev (1); Unit 5 Dev - Dungeon (1)
- **Intervals:** median 825.03s (p5 825.03s / p95 825.03s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x2
data.chatID  (string, 2/2 records)
    "NA"  x2
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 3 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `questEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : median interval between records changed substantially
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : event type present in baseline 09-23-26 but absent now
- `gameWindowFocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (42 records)
- `TopographicMapEvent` data.actionType: "Selected" (8x); "WaypointMoveEvent" (6x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Legend" (8x); "Waypoint" (10x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (31x)
- `soilMachine` data.canisterType: "Bedrock" (4x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*