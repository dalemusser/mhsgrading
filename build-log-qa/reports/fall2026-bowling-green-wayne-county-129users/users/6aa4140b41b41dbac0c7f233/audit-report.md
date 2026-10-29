# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f233

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa4140b41b41dbac0c7f233
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f233.jsonl
- **Records:** 10907 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f233
- **Time span:** 2026-09-23T13:53:57.160000+00:00 .. 2026-10-07T14:40:38.175000+00:00 (336h 46m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f233\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 10907 records, 8 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 96 INFO, 2 NOT_TESTED, 79 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationToolEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4263 | 39.08 | 1 | 3 | 0 | 2026-09-25T14:09:38.391000+00:00 | 2026-10-06T14:13:54.496000+00:00 | 264h 4m |
| InputEvent | 2458 | 22.54 | 1 | 7 | 0 | 2026-09-23T13:54:13.962000+00:00 | 2026-10-07T14:40:05.924000+00:00 | 336h 45m |
| PlayerPositionEvent | 2034 | 18.65 | 1 | 7 | 0 | 2026-09-23T13:54:08.806000+00:00 | 2026-10-07T14:40:38.175000+00:00 | 336h 46m |
| DialogueEvent | 1402 | 12.85 | 1 | 7 | 909 | 2026-09-23T13:54:31.094000+00:00 | 2026-10-07T14:40:35.726000+00:00 | 336h 46m |
| ObjectInterEvent | 334 | 3.06 | 1 | 7 | 0 | 2026-09-23T14:04:07.913000+00:00 | 2026-10-07T14:40:07.423000+00:00 | 336h 35m |
| argumentationNodeEvent | 87 | 0.8 | 1 | 2 | 0 | 2026-09-24T14:09:47.367000+00:00 | 2026-09-30T14:24:45.863000+00:00 | 144h 14m |
| questEvent | 69 | 0.63 | 1 | 7 | 69 | 2026-09-23T13:54:31.059000+00:00 | 2026-10-07T14:39:17.471000+00:00 | 336h 44m |
| Soil Key Puzzle | 50 | 0.46 | 1 | 3 | 0 | 2026-09-25T14:20:33.572000+00:00 | 2026-10-05T14:08:09.941000+00:00 | 239h 47m |
| TopographicMapEvent | 44 | 0.4 | 1 | 2 | 0 | 2026-09-25T14:11:12.140000+00:00 | 2026-10-01T14:22:16.643000+00:00 | 144h 11m |
| soilMachine | 39 | 0.36 | 1 | 1 | 0 | 2026-10-05T14:21:12.163000+00:00 | 2026-10-06T14:03:52.864000+00:00 | 23h 42m |
| gameWindowFocusEvent | 32 | 0.29 | 1 | 7 | 0 | 2026-09-23T13:53:57.160000+00:00 | 2026-10-07T14:39:04.753000+00:00 | 336h 45m |
| DEBUGMenu | 23 | 0.21 | 1 | 8 | 0 | 2026-09-23T13:54:08.797000+00:00 | 2026-10-07T14:39:13.035000+00:00 | 336h 45m |
| gameWindowUnfocusEvent | 23 | 0.21 | 1 | 6 | 0 | 2026-09-23T13:57:04.102000+00:00 | 2026-10-06T15:08:57.183000+00:00 | 313h 11m |
| gameStartEvent | 17 | 0.16 | 1 | 1 | 0 | 2026-09-23T13:53:57.161000+00:00 | 2026-10-07T14:39:04.753000+00:00 | 336h 45m |
| argumentationToolEvent | 9 | 0.08 | 1 | 1 | 0 | 2026-09-24T14:09:27.447000+00:00 | 2026-09-24T14:12:06.775000+00:00 | 2m 39s |
| argumentationAnswerEvent | 8 | 0.07 | 1 | 2 | 0 | 2026-09-24T14:09:55.766000+00:00 | 2026-09-30T14:24:50.893000+00:00 | 144h 14m |
| argumentationEvent | 7 | 0.06 | 1 | 2 | 0 | 2026-09-24T14:09:27.476000+00:00 | 2026-09-30T14:24:50.934000+00:00 | 144h 15m |
| DaniEvent | 4 | 0.04 | 1 | 1 | 0 | 2026-09-30T14:16:39.982000+00:00 | 2026-09-30T14:16:46.058000+00:00 | 6.1s |
| EndOfUnit | 2 | 0.02 | 1 | 2 | 0 | 2026-09-24T14:15:16.058000+00:00 | 2026-10-05T13:52:20.207000+00:00 | 263h 37m |
| chatEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-09-30T14:16:42.294000+00:00 | 2026-09-30T14:16:45.110000+00:00 | 2.8s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 949024.149s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.261s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.62s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 4.634s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.553s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2.816s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 85561.125s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 526.601s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1093.291s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 3.748s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend; Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: leftShift; m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 0 ft; 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; A,3,I 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D 
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
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [10-217, 10-218, 11-224, 11-226, 11-230] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 23 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 7.8x vs baseline. 
  - Observed: 39 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — categorical value(s) not seen in baseline. 
  - Observed: 2 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 18 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[245] _id=6ab3dd64485cab4c954cfbed ts=2026-09-23T14:08:36.8890000Z`; `6aa4140b41b41dbac0c7f233.jsonl[313] _id=6ab3de97485cab4c954d0457 ts=2026-09-23T14:13:43.2560000Z`; `6aa4140b41b41dbac0c7f233.jsonl[419] _id=6ab3e1d3485cab4c954d296b ts=2026-09-23T14:27:31.4000000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[4620] _id=6abbc3c1485cab4c957e1837 ts=2026-09-29T13:57:20.6740000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 17 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 17} 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[9] _id=6ab3d9f5485cab4c954ce281 ts=2026-09-23T13:53:57.1610000Z`; `6aa4140b41b41dbac0c7f233.jsonl[447] _id=6ab527bc485cab4c9551396f ts=2026-09-24T13:38:03.8820000Z`; `6aa4140b41b41dbac0c7f233.jsonl[996] _id=6ab67dbb485cab4c9555aafc ts=2026-09-25T13:57:15.4400000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 32 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 32} 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[8] _id=6ab3d9f5485cab4c954ce27f ts=2026-09-23T13:53:57.1600000Z`; `6aa4140b41b41dbac0c7f233.jsonl[38] _id=6ab3dab5485cab4c954ce509 ts=2026-09-23T13:57:09.4210000Z`; `6aa4140b41b41dbac0c7f233.jsonl[439] _id=6ab3e25c485cab4c954d2e7a ts=2026-09-23T14:29:48.7060000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 23 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 23} 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[36] _id=6ab3dab0485cab4c954ce4ed ts=2026-09-23T13:57:04.1020000Z`; `6aa4140b41b41dbac0c7f233.jsonl[441] _id=6ab3e25b485cab4c954d2e42 ts=2026-09-23T14:29:46.9910000Z`; `6aa4140b41b41dbac0c7f233.jsonl[443] _id=6ab3e265485cab4c954d2fa4 ts=2026-09-23T14:29:57.6910000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 5 of 44 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1377] _id=6ab68100485cab4c9555d7b4 ts=2026-09-25T14:11:12.1400000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1381] _id=6ab6810b485cab4c9555d860 ts=2026-09-25T14:11:23.3430000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1385] _id=6ab68117485cab4c9555d936 ts=2026-09-25T14:11:35.0460000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 4262 | 0.0 | 0.035 | 223.054 | 1.114 | 346439.201 | 0.27 | 2474 | 6 |
| InputEvent | 2457 | 0.004 | 1.261 | 493.428 | 23.441 | 343338.535 | 0.12 | 31 | 12 |
| PlayerPositionEvent | 2025 | 9.926 | 9.999 | 598.64 | 10.028 | 343103.679 | 0.1 | 0 | 11 |
| DialogueEvent | 1401 | 0.001 | 5.176 | 865.357 | 62.047 | 343140.117 | 0.07 | 369 | 10 |
| ObjectInterEvent | 333 | 0.003 | 5.46 | 3638.917 | 385.176 | 343603.601 | 0.02 | 2 | 14 |
| argumentationNodeEvent | 86 | 0.016 | 0.51 | 6038.355 | 4.292 | 519139.023 | 0.01 | 21 | 1 |
| questEvent | 68 | 0.002 | 251.709 | 17827.741 | 85655.417 | 343121.24 | 0.0 | 12 | 17 |
| Soil Key Puzzle | 49 | 0.207 | 1.33 | 17617.477 | 154714.684 | 346606.709 | 0.0 | 0 | 3 |
| TopographicMapEvent | 43 | 0.032 | 4.62 | 12071.268 | 87193.363 | 258139.231 | 0.0 | 2 | 4 |
| soilMachine | 38 | 0.567 | 3.748 | 2246.334 | 248.024 | 84149.355 | 0.03 | 0 | 1 |
| gameWindowFocusEvent | 31 | 19.287 | 526.601 | 39106.697 | 172891.781 | 343096.123 | 0.0 | 0 | 15 |
| DEBUGMenu | 22 | 8.773 | 1214.906 | 55104.738 | 249702.185 | 343673.841 | 0.0 | 0 | 14 |
| gameWindowUnfocusEvent | 22 | 3.115 | 1093.291 | 51250.595 | 252765.54 | 345389.961 | 0.0 | 0 | 12 |
| gameStartEvent | 16 | 97.408 | 85561.125 | 75769.224 | 280097.4 | 345693.587 | 0.0 | 0 | 10 |
| argumentationToolEvent | 8 | 0.821 | 3.553 | 19.916 | 87.247 | 124.018 | 3.01 | 0 | 0 |
| argumentationAnswerEvent | 7 | 0.474 | 4.634 | 74185.018 | 363430.617 | 519133.024 | 0.0 | 0 | 1 |
| argumentationEvent | 6 | 0.029 | 50.745 | 86553.91 | 389351.955 | 519111.462 | 0.0 | 1 | 1 |
| DaniEvent | 3 | 0.942 | 2.182 | 2.025 | 2.875 | 2.952 | 29.62 | 0 | 0 |
| EndOfUnit | 1 | 949024.149 | 949024.149 | 949024.149 | 949024.149 | 949024.149 | 0.0 | 0 | 1 |
| chatEvent | 1 | 2.816 | 2.816 | 2.816 | 2.816 | 2.816 | 21.31 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 172 group(s), 225 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1349] _id=6ab680a4485cab4c9555d312 ts=2026-09-25T14:09:38.6030000Z == 6aa4140b41b41dbac0c7f233.jsonl[1346] _id=6ab680a4485cab4c9555d314 ts=2026-09-25T14:09:38.6030000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1329] _id=6ab680a5485cab4c9555d328 ts=2026-09-25T14:09:39.3310000Z == 6aa4140b41b41dbac0c7f233.jsonl[1340] _id=6ab680a5485cab4c9555d32c ts=2026-09-25T14:09:39.3310000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1447] _id=6ab68143485cab4c9555dc54 ts=2026-09-25T14:10:00.4220000Z == 6aa4140b41b41dbac0c7f233.jsonl[1433] _id=6ab68143485cab4c9555dc56 ts=2026-09-25T14:10:00.4220000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 66 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 6aa4140b41b41dbac0c7f233.jsonl[161] _id=6ab3dc57485cab4c954cf349 ts=2026-09-23T14:04:07.9130000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[164] _id=6ab3dc58485cab4c954cf34b ts=2026-09-23T14:04:07.9210000Z`; `3ms: 6aa4140b41b41dbac0c7f233.jsonl[517] _id=6ab528d3485cab4c955159ab ts=2026-09-24T13:42:43.4080000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[511] _id=6ab528d3485cab4c955159af ts=2026-09-24T13:42:43.4110000Z`; `737ms: 6aa4140b41b41dbac0c7f233.jsonl[1032] _id=6ab67e35485cab4c9555b60c ts=2026-09-25T13:59:18.0440000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[1040] _id=6ab67e36485cab4c9555b614 ts=2026-09-25T13:59:18.7810000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 683 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `75ms: 6aa4140b41b41dbac0c7f233.jsonl[1327] _id=6ab680a4485cab4c9555d2fa ts=2026-09-25T14:09:38.4730000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[1345] _id=6ab680a4485cab4c9555d300 ts=2026-09-25T14:09:38.5480000Z`; `8ms: 6aa4140b41b41dbac0c7f233.jsonl[1347] _id=6ab680a4485cab4c9555d31c ts=2026-09-25T14:09:38.6030000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[1352] _id=6ab680a4485cab4c9555d320 ts=2026-09-25T14:09:38.6110000Z`; `633ms: 6aa4140b41b41dbac0c7f233.jsonl[1352] _id=6ab680a4485cab4c9555d320 ts=2026-09-25T14:09:38.6110000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[1339] _id=6ab680a4485cab4c9555d324 ts=2026-09-25T14:09:39.2440000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `37ms: 6aa4140b41b41dbac0c7f233.jsonl[3327] _id=6aba717b485cab4c95683ee4 ts=2026-09-28T13:54:02.9350000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[3333] _id=6aba717b485cab4c95683eff ts=2026-09-28T13:54:02.9720000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `474ms: 6aa4140b41b41dbac0c7f233.jsonl[902] _id=6ab52fb1485cab4c9551e127 ts=2026-09-24T14:12:01.8160000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[900] _id=6ab52fb2485cab4c9551e12f ts=2026-09-24T14:12:02.2900000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `29ms: 6aa4140b41b41dbac0c7f233.jsonl[6703] _id=6abd1bb3485cab4c958b27ee ts=2026-09-30T14:24:50.9050000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[6715] _id=6abd1bb3485cab4c958b27f6 ts=2026-09-30T14:24:50.9340000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `28ms: 6aa4140b41b41dbac0c7f233.jsonl[834] _id=6ab52f2b485cab4c9551dacb ts=2026-09-24T14:09:47.7980000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[832] _id=6ab52f2b485cab4c9551dacd ts=2026-09-24T14:09:47.8260000Z`; `855ms: 6aa4140b41b41dbac0c7f233.jsonl[833] _id=6ab52f2d485cab4c9551dad3 ts=2026-09-24T14:09:49.1210000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[839] _id=6ab52f2e485cab4c9551dadd ts=2026-09-24T14:09:49.9760000Z`; `874ms: 6aa4140b41b41dbac0c7f233.jsonl[838] _id=6ab52f2d485cab4c9551dad9 ts=2026-09-24T14:09:49.7360000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[835] _id=6ab52f2e485cab4c9551dadf ts=2026-09-24T14:09:50.6100000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 6aa4140b41b41dbac0c7f233.jsonl[4620] _id=6abbc3c1485cab4c957e1837 ts=2026-09-29T13:57:20.6740000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[4619] _id=6abbc3c2485cab4c957e1839 ts=2026-09-29T13:57:20.6760000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `700ms: 6aa4140b41b41dbac0c7f233.jsonl[10367] _id=6ac4ff7ede269131f9b2438e ts=2026-10-06T14:02:38.0990000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[10374] _id=6ac4ff7ede269131f9b243a6 ts=2026-10-06T14:02:38.7990000Z`; `567ms: 6aa4140b41b41dbac0c7f233.jsonl[10378] _id=6ac4ff80de269131f9b243c6 ts=2026-10-06T14:02:40.0320000Z ~ 6aa4140b41b41dbac0c7f233.jsonl[10361] _id=6ac4ff80de269131f9b243d4 ts=2026-10-06T14:02:40.5990000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 27m 
  - Evidence: 95h 27m: 6aa4140b41b41dbac0c7f233.jsonl[8009] _id=6abe6c13485cab4c95a8085f ts=2026-10-01T14:20:03.8380000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8209] _id=6ac3aa8dde269131f9a9c8ea ts=2026-10-05T13:47:57.6790000Z; 71h 43m: 6aa4140b41b41dbac0c7f233.jsonl[1237] _id=6ab67f8b485cab4c9555c504 ts=2026-09-25T14:04:59.3730000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3252] _id=6aba7047485cab4c95681ddb ts=2026-09-28T13:48:55.7310000Z; 24h 19m: 6aa4140b41b41dbac0c7f233.jsonl[451] _id=6ab527c5485cab4c95513a03 ts=2026-09-24T13:38:13.6550000Z -> 6aa4140b41b41dbac0c7f233.jsonl[1000] _id=6ab67dc6485cab4c9555ac90 ts=2026-09-25T13:57:26.5490000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa4140b41b41dbac0c7f233.jsonl[8196] _id=6abe6e41485cab4c95a892f0 ts=2026-10-01T14:29:21.3750000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8212] _id=6ac3aaa5de269131f9a9cdd4 ts=2026-10-05T13:48:21.4920000Z; 71h 22m: 6aa4140b41b41dbac0c7f233.jsonl[3245] _id=6ab68545485cab4c9556494c ts=2026-09-25T14:29:25.2320000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3282] _id=6aba7106485cab4c95682ee1 ts=2026-09-28T13:52:06.5300000Z; 23h 58m: 6aa4140b41b41dbac0c7f233.jsonl[10854] _id=6ac50860de269131f9b39832 ts=2026-10-06T14:40:32.1150000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10871] _id=6ac65995de269131f9bafa4e ts=2026-10-07T14:39:18.6970000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 369 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f233.jsonl[1286] _id=6ab68043485cab4c9555cfa2 ts=2026-09-25T14:08:03.3160000Z -> 6aa4140b41b41dbac0c7f233.jsonl[1288] _id=6ab68043485cab4c9555cfa7 ts=2026-09-25T14:08:03.3170000Z; 1ms: 6aa4140b41b41dbac0c7f233.jsonl[3228] _id=6ab68529485cab4c9556478a ts=2026-09-25T14:28:57.0570000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3227] _id=6ab68529485cab4c9556478e ts=2026-09-25T14:28:57.0580000Z; 1ms: 6aa4140b41b41dbac0c7f233.jsonl[3233] _id=6ab68525485cab4c95564768 ts=2026-09-25T14:28:53.1910000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3231] _id=6ab68525485cab4c9556476a ts=2026-09-25T14:28:53.1920000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 263h 37m 
  - Evidence: 263h 37m: 6aa4140b41b41dbac0c7f233.jsonl[989] _id=6ab53074485cab4c9551edc9 ts=2026-09-24T14:15:16.0580000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8276] _id=6ac3ab94de269131f9aa0276 ts=2026-10-05T13:52:20.2070000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa4140b41b41dbac0c7f233.jsonl[8154] _id=6abe6d74485cab4c95a865d1 ts=2026-10-01T14:25:56.8440000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8204] _id=6ac3aa9fde269131f9a9cc88 ts=2026-10-05T13:48:15.3790000Z; 71h 21m: 6aa4140b41b41dbac0c7f233.jsonl[3210] _id=6ab684d2485cab4c955641a4 ts=2026-09-25T14:27:30.8860000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3254] _id=6aba7051485cab4c95681e30 ts=2026-09-28T13:49:05.1500000Z; 23h 59m: 6aa4140b41b41dbac0c7f233.jsonl[10845] _id=6ac50846de269131f9b392a8 ts=2026-10-06T14:40:03.0630000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10870] _id=6ac6598fde269131f9bafa06 ts=2026-10-07T14:39:13.0120000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 31 interval(s) ≤ 0.004s..0.005s shown 
  - Evidence: 4ms: 6aa4140b41b41dbac0c7f233.jsonl[6090] _id=6abd17ac485cab4c958a51ae ts=2026-09-30T14:07:40.6830000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6089] _id=6abd17ac485cab4c958a51bc ts=2026-09-30T14:07:40.6870000Z; 5ms: 6aa4140b41b41dbac0c7f233.jsonl[6445] _id=6abd19da485cab4c958ad362 ts=2026-09-30T14:16:58.1320000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6443] _id=6abd19da485cab4c958ad364 ts=2026-09-30T14:16:58.1370000Z; 5ms: 6aa4140b41b41dbac0c7f233.jsonl[7878] _id=6abe6a5e485cab4c95a7ad13 ts=2026-10-01T14:12:46.6040000Z -> 6aa4140b41b41dbac0c7f233.jsonl[7879] _id=6abe6a5e485cab4c95a7ad18 ts=2026-10-01T14:12:46.6090000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 26m 
  - Evidence: 95h 26m: 6aa4140b41b41dbac0c7f233.jsonl[8146] _id=6abe6d42485cab4c95a85b53 ts=2026-10-01T14:25:06.8340000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8259] _id=6ac3ab76de269131f9a9fa46 ts=2026-10-05T13:51:50.4350000Z; 71h 51m: 6aa4140b41b41dbac0c7f233.jsonl[3082] _id=6ab68331485cab4c95562ac4 ts=2026-09-25T14:20:33.5750000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3593] _id=6aba75b5485cab4c95689bdd ts=2026-09-28T14:12:05.5930000Z; 24h 19m: 6aa4140b41b41dbac0c7f233.jsonl[10833] _id=6ac5039fde269131f9b2c4d0 ts=2026-10-06T14:20:15.4370000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10898] _id=6ac659c6de269131f9bafbf1 ts=2026-10-07T14:40:07.4230000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.008s shown 
  - Evidence: 3ms: 6aa4140b41b41dbac0c7f233.jsonl[517] _id=6ab528d3485cab4c955159ab ts=2026-09-24T13:42:43.4080000Z -> 6aa4140b41b41dbac0c7f233.jsonl[511] _id=6ab528d3485cab4c955159af ts=2026-09-24T13:42:43.4110000Z; 8ms: 6aa4140b41b41dbac0c7f233.jsonl[161] _id=6ab3dc57485cab4c954cf349 ts=2026-09-23T14:04:07.9130000Z -> 6aa4140b41b41dbac0c7f233.jsonl[164] _id=6ab3dc58485cab4c954cf34b ts=2026-09-23T14:04:07.9210000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f233.jsonl[8200] _id=6abe6e4e485cab4c95a896ba ts=2026-10-01T14:29:34.0070000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8210] _id=6ac3aa92de269131f9a9c96f ts=2026-10-05T13:47:57.6860000Z; 71h 19m: 6aa4140b41b41dbac0c7f233.jsonl[3244] _id=6ab68542485cab4c9556492e ts=2026-09-25T14:29:22.7620000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3253] _id=6aba704d485cab4c95681e01 ts=2026-09-28T13:48:55.7370000Z; 23h 42m: 6aa4140b41b41dbac0c7f233.jsonl[993] _id=6ab53072485cab4c9551edb3 ts=2026-09-24T14:15:14.7620000Z -> 6aa4140b41b41dbac0c7f233.jsonl[998] _id=6ab67dcd485cab4c9555ada2 ts=2026-09-25T13:57:26.5600000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 13m 
  - Evidence: 96h 13m: 6aa4140b41b41dbac0c7f233.jsonl[7367] _id=6abe660c485cab4c95a73f0d ts=2026-10-01T13:54:20.2860000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8429] _id=6ac3af53de269131f9aab31b ts=2026-10-05T14:08:19.4870000Z; 71h 45m: 6aa4140b41b41dbac0c7f233.jsonl[3017] _id=6ab682d5485cab4c95562384 ts=2026-09-25T14:18:59.8350000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3469] _id=6aba73f1485cab4c956875ef ts=2026-09-28T14:04:32.6640000Z; 47h 43m: 6aa4140b41b41dbac0c7f233.jsonl[5333] _id=6abbc65b485cab4c957e5ec9 ts=2026-09-29T14:08:26.5540000Z -> 6aa4140b41b41dbac0c7f233.jsonl[7010] _id=6abe656c485cab4c95a715d4 ts=2026-10-01T13:51:39.1930000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2474 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f233.jsonl[10474] _id=6ac50024de269131f9b24fd1 ts=2026-10-06T14:05:24.0290000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10503] _id=6ac50024de269131f9b24fd4 ts=2026-10-06T14:05:24.0290000Z; 0ms: 6aa4140b41b41dbac0c7f233.jsonl[10475] _id=6ac50025de269131f9b24fe3 ts=2026-10-06T14:05:24.1620000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10476] _id=6ac50025de269131f9b24fe8 ts=2026-10-06T14:05:24.1620000Z; 0ms: 6aa4140b41b41dbac0c7f233.jsonl[10478] _id=6ac50038de269131f9b2515c ts=2026-10-06T14:05:43.3830000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10559] _id=6ac50038de269131f9b2515e ts=2026-10-06T14:05:43.3830000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 16m 
  - Evidence: 96h 16m: 6aa4140b41b41dbac0c7f233.jsonl[6988] _id=6abe6546485cab4c95a70906 ts=2026-10-01T13:51:02.0810000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8405] _id=6ac3af34de269131f9aaad34 ts=2026-10-05T14:07:48.7900000Z; 71h 51m: 6aa4140b41b41dbac0c7f233.jsonl[3085] _id=6ab68334485cab4c95562ae6 ts=2026-09-25T14:20:36.5660000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3592] _id=6aba75b5485cab4c95689bd7 ts=2026-09-28T14:12:05.5870000Z; 71h 37m: 6aa4140b41b41dbac0c7f233.jsonl[3618] _id=6aba75dc485cab4c95689f95 ts=2026-09-28T14:12:44.9100000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6973] _id=6abe6513485cab4c95a6fae9 ts=2026-10-01T13:50:11.6780000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 71h 42m 
  - Evidence: 71h 42m: 6aa4140b41b41dbac0c7f233.jsonl[1385] _id=6ab68117485cab4c9555d936 ts=2026-09-25T14:11:35.0460000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3324] _id=6aba7172485cab4c95683dbd ts=2026-09-28T13:53:54.2770000Z; 24h 22m: 6aa4140b41b41dbac0c7f233.jsonl[3452] _id=6aba73b7485cab4c956872a3 ts=2026-09-28T14:03:35.6620000Z -> 6aa4140b41b41dbac0c7f233.jsonl[5762] _id=6abbca96485cab4c957ec162 ts=2026-09-29T14:26:30.0660000Z; 24h 17m: 6aa4140b41b41dbac0c7f233.jsonl[6014] _id=6abd16fd485cab4c9589eb7c ts=2026-09-30T14:04:45.9480000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8061] _id=6abe6c85485cab4c95a83514 ts=2026-10-01T14:21:57.6820000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.032s..0.037s shown 
  - Evidence: 32ms: 6aa4140b41b41dbac0c7f233.jsonl[3331] _id=6aba717b485cab4c95683edc ts=2026-09-28T13:54:02.9030000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3327] _id=6aba717b485cab4c95683ee4 ts=2026-09-28T13:54:02.9350000Z; 37ms: 6aa4140b41b41dbac0c7f233.jsonl[3327] _id=6aba717b485cab4c95683ee4 ts=2026-09-28T13:54:02.9350000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3333] _id=6aba717b485cab4c95683eff ts=2026-09-28T13:54:02.9720000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 6aa4140b41b41dbac0c7f233.jsonl[908] _id=6ab52fb6485cab4c9551e185 ts=2026-09-24T14:12:06.9240000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6727] _id=6abd1b93485cab4c958b21a0 ts=2026-09-30T14:24:19.9480000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 11m 
  - Evidence: 144h 11m: 6aa4140b41b41dbac0c7f233.jsonl[906] _id=6ab52fb7485cab4c9551e187 ts=2026-09-24T14:12:06.9520000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6687] _id=6abd1b7e485cab4c958b1dca ts=2026-09-30T14:23:58.4140000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.029s..0.029s shown 
  - Evidence: 29ms: 6aa4140b41b41dbac0c7f233.jsonl[6703] _id=6abd1bb3485cab4c958b27ee ts=2026-09-30T14:24:50.9050000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6715] _id=6abd1bb3485cab4c958b27f6 ts=2026-09-30T14:24:50.9340000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 6aa4140b41b41dbac0c7f233.jsonl[890] _id=6ab52f93485cab4c9551dfd1 ts=2026-09-24T14:11:31.0130000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6670] _id=6abd1b76485cab4c958b1c12 ts=2026-09-30T14:23:50.0360000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 21 interval(s) ≤ 0.016s..0.018s shown 
  - Evidence: 16ms: 6aa4140b41b41dbac0c7f233.jsonl[6671] _id=6abd1b76485cab4c958b1c1e ts=2026-09-30T14:23:50.1500000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6662] _id=6abd1b76485cab4c958b1c22 ts=2026-09-30T14:23:50.1660000Z; 18ms: 6aa4140b41b41dbac0c7f233.jsonl[6679] _id=6abd1b7a485cab4c958b1cde ts=2026-09-30T14:23:54.0020000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6677] _id=6abd1b7a485cab4c958b1ce2 ts=2026-09-30T14:23:54.0200000Z; 18ms: 6aa4140b41b41dbac0c7f233.jsonl[6711] _id=6abd1bad485cab4c958b26b5 ts=2026-09-30T14:24:45.8450000Z -> 6aa4140b41b41dbac0c7f233.jsonl[6712] _id=6abd1bad485cab4c958b26bb ts=2026-09-30T14:24:45.8630000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa4140b41b41dbac0c7f233.jsonl[6900] _id=6abe6425485cab4c95a6b6cd ts=2026-10-01T13:46:13.2700000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8205] _id=6ac3aa83de269131f9a9c7d8 ts=2026-10-05T13:47:46.8570000Z; 71h 43m: 6aa4140b41b41dbac0c7f233.jsonl[1234] _id=6ab67f85485cab4c9555c4e0 ts=2026-09-25T14:04:53.1450000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3250] _id=6aba703d485cab4c95681d40 ts=2026-09-28T13:48:45.1490000Z; 24h 19m: 6aa4140b41b41dbac0c7f233.jsonl[447] _id=6ab527bc485cab4c9551396f ts=2026-09-24T13:38:03.8820000Z -> 6aa4140b41b41dbac0c7f233.jsonl[996] _id=6ab67dbb485cab4c9555aafc ts=2026-09-25T13:57:15.4400000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f233.jsonl[8198] _id=6abe6e4a485cab4c95a895b5 ts=2026-10-01T14:29:30.7340000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8206] _id=6ac3aa83de269131f9a9c7d2 ts=2026-10-05T13:47:46.8570000Z; 71h 43m: 6aa4140b41b41dbac0c7f233.jsonl[1140] _id=6ab67f85485cab4c9555c4de ts=2026-09-25T14:04:53.1450000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3249] _id=6aba703d485cab4c95681d3b ts=2026-09-28T13:48:45.1490000Z; 24h 19m: 6aa4140b41b41dbac0c7f233.jsonl[449] _id=6ab527bb485cab4c9551396d ts=2026-09-24T13:38:03.8810000Z -> 6aa4140b41b41dbac0c7f233.jsonl[995] _id=6ab67dbb485cab4c9555aaf4 ts=2026-09-25T13:57:15.4390000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 56m 
  - Evidence: 95h 56m: 6aa4140b41b41dbac0c7f233.jsonl[8199] _id=6abe6e4d485cab4c95a896ad ts=2026-10-01T14:29:33.8460000Z -> 6aa4140b41b41dbac0c7f233.jsonl[9694] _id=6ac3b37bde269131f9abb61f ts=2026-10-05T14:26:03.8070000Z; 71h 22m: 6aa4140b41b41dbac0c7f233.jsonl[3246] _id=6ab68547485cab4c9556496c ts=2026-09-25T14:29:27.7440000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3290] _id=6aba7117485cab4c9568312f ts=2026-09-28T13:52:23.5730000Z; 47h 59m: 6aa4140b41b41dbac0c7f233.jsonl[443] _id=6ab3e265485cab4c954d2fa4 ts=2026-09-23T14:29:57.6910000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3246] _id=6ab68547485cab4c9556496c ts=2026-09-25T14:29:27.7440000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa4140b41b41dbac0c7f233.jsonl[8195] _id=6abe6e41485cab4c95a892eb ts=2026-10-01T14:29:21.3700000Z -> 6aa4140b41b41dbac0c7f233.jsonl[8214] _id=6ac3aa93de269131f9a9c973 ts=2026-10-05T13:48:02.6100000Z; 71h 24m: 6aa4140b41b41dbac0c7f233.jsonl[3133] _id=6ab6843b485cab4c955639bc ts=2026-09-25T14:24:59.2470000Z -> 6aa4140b41b41dbac0c7f233.jsonl[3251] _id=6aba704e485cab4c95681e03 ts=2026-09-28T13:49:01.6990000Z; 23h 59m: 6aa4140b41b41dbac0c7f233.jsonl[10846] _id=6ac50847de269131f9b392af ts=2026-10-06T14:40:06.5960000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10874] _id=6ac65994de269131f9bafa44 ts=2026-10-07T14:39:17.4710000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.002s..0.003s shown 
  - Evidence: 2ms: 6aa4140b41b41dbac0c7f233.jsonl[4620] _id=6abbc3c1485cab4c957e1837 ts=2026-09-29T13:57:20.6740000Z -> 6aa4140b41b41dbac0c7f233.jsonl[4619] _id=6abbc3c2485cab4c957e1839 ts=2026-09-29T13:57:20.6760000Z; 2ms: 6aa4140b41b41dbac0c7f233.jsonl[798] _id=6ab52eaa485cab4c9551d455 ts=2026-09-24T14:07:38.7410000Z -> 6aa4140b41b41dbac0c7f233.jsonl[799] _id=6ab52eaa485cab4c9551d457 ts=2026-09-24T14:07:38.7430000Z; 3ms: 6aa4140b41b41dbac0c7f233.jsonl[9501] _id=6ac3b1bade269131f9ab44ab ts=2026-10-05T14:18:34.4680000Z -> 6aa4140b41b41dbac0c7f233.jsonl[9500] _id=6ac3b1bade269131f9ab44b1 ts=2026-10-05T14:18:34.4710000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 22m 
  - Evidence: 23h 22m: 6aa4140b41b41dbac0c7f233.jsonl[9930] _id=6ac3b4f8de269131f9abf3ee ts=2026-10-05T14:32:24.6880000Z -> 6aa4140b41b41dbac0c7f233.jsonl[10064] _id=6ac4fdaede269131f9b1e419 ts=2026-10-06T13:54:54.0430000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[794] _id=6ab52e97485cab4c9551d381 ts=2026-09-24T14:07:19.6700000Z`; `6aa4140b41b41dbac0c7f233.jsonl[918] _id=6ab52fdd485cab4c9551e36b ts=2026-09-24T14:12:45.3980000Z`; `6aa4140b41b41dbac0c7f233.jsonl[3451] _id=6aba73ae485cab4c956871dd ts=2026-09-28T14:03:25.9790000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 98 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1643] _id=6ab68176485cab4c9555e47a ts=2026-09-25T14:13:09.7770000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1625] _id=6ab6817d485cab4c9555e54e ts=2026-09-25T14:13:16.3260000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1626] _id=6ab6817d485cab4c9555e552 ts=2026-09-25T14:13:16.3790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 320 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1338] _id=6ab680a4485cab4c9555d30a ts=2026-09-25T14:09:38.5630000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1348] _id=6ab680a4485cab4c9555d30d ts=2026-09-25T14:09:38.5790000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1346] _id=6ab680a4485cab4c9555d314 ts=2026-09-25T14:09:38.6030000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[6715] _id=6abd1bb3485cab4c958b27f6 ts=2026-09-30T14:24:50.9340000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[832] _id=6ab52f2b485cab4c9551dacd ts=2026-09-24T14:09:47.8260000Z`; `6aa4140b41b41dbac0c7f233.jsonl[6671] _id=6abd1b76485cab4c958b1c1e ts=2026-09-30T14:23:50.1500000Z`; `6aa4140b41b41dbac0c7f233.jsonl[6662] _id=6abd1b76485cab4c958b1c22 ts=2026-09-30T14:23:50.1660000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[6972] _id=6abe6567485cab4c95a71419 ts=2026-10-01T13:51:35.4600000Z`; `6aa4140b41b41dbac0c7f233.jsonl[9960] _id=6ac4fcd4de269131f9b1ad54 ts=2026-10-06T13:51:16.0710000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 581 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1672] _id=6ab6817e485cab4c9555e596 ts=2026-09-25T14:13:16.6190000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1684] _id=6ab6817e485cab4c9555e5a2 ts=2026-09-25T14:13:16.7070000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1685] _id=6ab6817e485cab4c9555e5a6 ts=2026-09-25T14:13:16.7290000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 892 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1344] _id=6ab680a3485cab4c9555d2f4 ts=2026-09-25T14:09:38.4560000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1326] _id=6ab680a3485cab4c9555d2f8 ts=2026-09-25T14:09:38.4560000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1357] _id=6ab680a8485cab4c9555d36c ts=2026-09-25T14:09:43.8310000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 8 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[3327] _id=6aba717b485cab4c95683ee4 ts=2026-09-28T13:54:02.9350000Z`; `6aa4140b41b41dbac0c7f233.jsonl[3333] _id=6aba717b485cab4c95683eff ts=2026-09-28T13:54:02.9720000Z`; `6aa4140b41b41dbac0c7f233.jsonl[3353] _id=6aba71e3485cab4c95685057 ts=2026-09-28T13:55:47.1890000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[878] _id=6ab52f8a485cab4c9551df6b ts=2026-09-24T14:11:22.6400000Z`; `6aa4140b41b41dbac0c7f233.jsonl[881] _id=6ab52f8a485cab4c9551df6d ts=2026-09-24T14:11:22.6600000Z`; `6aa4140b41b41dbac0c7f233.jsonl[6670] _id=6abd1b76485cab4c958b1c12 ts=2026-09-30T14:23:50.0360000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[894] _id=6ab52f97485cab4c9551e00f ts=2026-09-24T14:11:35.7870000Z`; `6aa4140b41b41dbac0c7f233.jsonl[899] _id=6ab52fab485cab4c9551e0fd ts=2026-09-24T14:11:55.5660000Z`; `6aa4140b41b41dbac0c7f233.jsonl[904] _id=6ab52fb5485cab4c9551e167 ts=2026-09-24T14:12:05.2330000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 19 unmatched 'DialogueStartEvent' (totals: 251 start, 242 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 159 unmatched 'BecameCameraCentered' (totals: 823 open, 762 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 112 unmatched 'BecameVisible' (totals: 1235 open, 1443 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 10 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 4 unmatched 'argumentationNodeHoverStart' (totals: 40 open, 39 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 17 unmatched 'questActiveEvent' (totals: 42 start, 27 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 288 of 10906 adjacent _id pairs reverse in client time; worst 151.5s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f233.jsonl[1408] _id=6ab68140485cab4c9555dbbc ts=2026-09-25T14:12:16.5120000Z`; `6aa4140b41b41dbac0c7f233.jsonl[1416] _id=6ab68141485cab4c9555dbd8 ts=2026-09-25T14:09:45.0390000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.13s, min -152.62s, max +1.19s over 10907 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa4140b41b41dbac0c7f233\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 4263 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3025); Unit 4 Dev (932); Unit 3 Dungeon Dev (306)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.11s, n=4262)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4263/4263 records)
    "BecameInvisible"  x1443
    "BecameVisible"  x1235
    "BecameCameraCentered"  x823
    "BecameCameraUncentered"  x762
data.pieceId  (string, 4263/4263 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4263/4263 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2458 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (631); Unit 4 Dev - Dungeon (550); Unit 2 Prod (Refactor) (406); Unit 3 Dungeon Dev (357); Unit 1 Dev (319); Unit 4 Dev (156); Unit 4 Dev - Anderson Base (39)
- **Intervals:** median 1.26s (p5 0.14s / p95 23.44s, n=2457)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2458/2458 records)
    "pressed"  x2458
data.actionType  (string, 2458/2458 records)
    "Move"  x1709
    "Interact"  x486
    "Jump"  x187
    "Sprint"  x43
    "Hoverboard"  x17
    "Ascend"  x16
data.key  (string, 2458/2458 records, 2 empty-string)
    14 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2458/2458 records)
    "Player"  x2046
    "Drone"  x412
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2034 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (636); Unit 1 Dev (475); Unit 3 Dev (312); Unit 4 Dev - Dungeon (208); Unit 4 Dev (201); Unit 3 Dungeon Dev (170); Unit 4 Dev - Anderson Base (32)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2025)
- **Fields under `data`:**

```text
data.position  (object, 2034/2034 records)
data.position.x  (number, 2034/2034 records)
    numeric range -657.954 .. 1438.62 (602 unique)
data.position.y  (number, 2034/2034 records)
    numeric range -112.491 .. 156.543 (446 unique)
data.position.z  (number, 2034/2034 records)
    numeric range -1249.26 .. 2214.59 (599 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1402 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (453); Unit 3 Dev (297); Unit 1 Dev (269); Unit 4 Dev - Dungeon (143); Unit 3 Dungeon Dev (120); Unit 4 Dev (103); Unit 4 Dev - Anderson Base (17)
- **eventKey:** present on 909 of 1402 records
- **Intervals:** median 5.18s (p5 0.00s / p95 62.05s, n=1401)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x909; [conversationId, dialogueEventType] x493
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1402/1402 records)
    numeric range 8 .. 111 (39 unique)
data.dialogueEventType  (string, 1402/1402 records)
    "DialogueNodeEvent"  x909
    "DialogueStartEvent"  x251
    "DialogueFinishEvent"  x242
data.nodeId  (number, 909/1402 records)
    numeric range 0 .. 290 (221 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 334 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (131); Unit 1 Dev (84); Unit 2 Prod (Refactor) (49); Unit 3 Dungeon Dev (48); Unit 3 Dev (12); Unit 4 Dev (8); Unit 4 Dev - Anderson Base (2)
- **Intervals:** median 5.46s (p5 0.17s / p95 385.18s, n=333)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 334/334 records)
    31 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 334/334 records)
    77 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 87 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (53); Unit 1 Dev (34)
- **Intervals:** median 0.51s (p5 0.02s / p95 4.29s, n=86)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 87/87 records)
    "argumentationNodeHoverStart"  x40
    "argumentationNodeHoverEnd"  x39
    "argumentationNodeAdd"  x7
    "argumentationNodeRemove"  x1
data.argumentationTitle  (string, 87/87 records)
    "Unit 3 - Pollution Upstream"  x53
    "Unit 1 - Freshwater"  x25
    "Unit 1 - Argumentation Tutorial"  x9
data.nodeName  (string, 87/87 records)
    "I"  x22
    "II"  x16
    "A"  x14
    "3"  x12
    "1"  x10
    "5"  x7
    "2"  x2
    "4"  x2
    "B"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 69 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (17); Unit 2 Prod (Refactor) (16); Unit 4 Dev - Dungeon (15); Unit 3 Dev (12); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 3 Dungeon Dev (2)
- **eventKey:** present on 69 of 69 records
- **Intervals:** median 251.71s (p5 0.00s / p95 85655.42s, n=68)
- **`data` key-set variants:** [questEventType, questID, questName] x42; [questEventType, questID, questName, questSuccessOrFailure] x27
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 69/69 records)
    "questActiveEvent"  x42
    "questFinishEvent"  x27
data.questID  (string, 69/69 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 69/69 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 27/69 records)
    "Succeeded"  x27
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 50 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (22); Unit 3 Dev (18); Unit 4 Dev (10)
- **Intervals:** median 1.33s (p5 0.26s / p95 154714.68s, n=49)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x42; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/50 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/50 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 42/50 records)
    "RightDrag"  x24
    "LeftDrag"  x18
data.currentSoilType  (string, 42/50 records)
    "CLAY"  x11
    "CLAYROCK"  x9
    "CLAYSAND"  x9
    "SAND"  x6
    "BEDROCK"  x3
    "SANDGRAVEL"  x3
    "GRAVEL"  x1
data.isCorrectSelection  (string, 42/50 records)
    "false"  x30
    "true"  x12
data.waterLevelStatus  (string, 42/50 records)
    "TooHigh"  x20
    "Proper"  x15
    "TooLow"  x7
data.waterRetentionChange  (string, 42/50 records)
    "Increase"  x20
    "NoChange"  x12
    "Decrease"  x10
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TopographicMapEvent` — 44 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 3 Dev (17)
- **Intervals:** median 4.62s (p5 0.54s / p95 87193.36s, n=43)
- **`data` key-set variants:** [actionType, featureUsed, location] x21; [actionType, featureUsed] x18; [actionType, featureUsed, legendName] x5
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "WaypointMoveEvent"  x15
    "MapOpenEvent"  x10
    "MapCloseEvent"  x8
    "WaypointSetEvent"  x6
    "Selected"  x4
    "Unselected"  x1
data.featureUsed  (string, 44/44 records)
    "Waypoint"  x21
    "Map"  x18
    "Legend"  x5
data.legendName  (string, 5/44 records)
    "Water"  x5
data.location  (object, 21/44 records)
data.location.x  (number, 21/44 records)
    numeric range -571.09 .. 330.91 (19 unique)
data.location.y  (number, 21/44 records)
    numeric range -195.5 .. 299.5 (19 unique)
data.location.z  (number, 21/44 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 39 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (39)
- **Intervals:** median 3.75s (p5 0.76s / p95 248.02s, n=38)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 39/39 records)
    "ChangeCanister"  x39
data.canisterType  (string, 39/39 records)
    "Clay"  x20
    "Bedrock"  x9
    "Gravel"  x7
    "Sand"  x3
data.floor  (string, 39/39 records)
    "5"  x25
    "3"  x7
    "4"  x5
    "2"  x2
data.machine  (string, 39/39 records)
    "1"  x38
    "2"  x1
data.row  (string, 39/39 records)
    "TopRow"  x22
    "BottomRow"  x17
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `gameWindowFocusEvent` — 32 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (17); Unit 4 Dev - Anderson Base (5); Unit 4 Dev - Dungeon (3); Unit 1 Dev (2); Unit 3 Dev (2); Unit 4 Dev (2); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 526.60s (p5 24.66s / p95 172891.78s, n=31)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 32/32 records)
    true  x32
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 23 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 1 Dev (4); Unit 3 Dev (4); Unit 4 Dev - Anderson Base (3); Unit 4 Dev (2); Unit 4 Dev - Dungeon (2); MainMenu (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 1214.91s (p5 93.48s / p95 249702.18s, n=22)
- **Fields under `data`:**

```text
data.actionType  (string, 23/23 records)
    "DebugMenuStateChanged"  x23
data.isOpened  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowUnfocusEvent` — 23 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 4 Dev - Anderson Base (6); Unit 2 Prod (Refactor) (4); Unit 3 Dev (4); Unit 4 Dev - Dungeon (4); Unit 1 Dev (3); Unit 4 Dev (2)
- **Intervals:** median 1093.29s (p5 3.26s / p95 252765.54s, n=22)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 23/23 records)
    false  x23
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `gameStartEvent` — 17 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (17)
- **Intervals:** median 85561.13s (p5 108.31s / p95 280097.40s, n=16)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 17/17 records)
    true  x17
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9)
- **Intervals:** median 3.55s (p5 1.01s / p95 87.25s, n=8)
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

### `argumentationAnswerEvent` — 8 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (5); Unit 3 Dev (3)
- **Intervals:** median 4.63s (p5 0.65s / p95 363430.62s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "submitAnswerEvent"  x8
data.answerSubmitted  (string, 8/8 records)
    "A,1,I"  x4
    "A,3,I"  x2
    "1,"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 8/8 records)
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 50.75s (p5 9.28s / p95 389351.95s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `DaniEvent` — 4 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 2.18s (p5 1.07s / p95 2.88s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 949024.15s (p5 949024.15s / p95 949024.15s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 2.82s (p5 2.82s / p95 2.82s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[10-217, 10-218, 11-224, 11-226, 11-230]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TopographicMapEvent` data.actionType: "Selected" (4x); "Unselected" (1x); "WaypointMoveEvent" (15x); "WaypointSetEvent" (6x)
- `TopographicMapEvent` data.featureUsed: "Legend" (5x); "Waypoint" (21x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (1x)
- `soilMachine` data.canisterType: "Bedrock" (9x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*