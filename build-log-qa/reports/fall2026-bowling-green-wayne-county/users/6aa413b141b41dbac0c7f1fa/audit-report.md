# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1fa

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa413b141b41dbac0c7f1fa
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1fa.jsonl
- **Records:** 16770 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1fa
- **Time span:** 2026-09-23T13:08:35.897000+00:00 .. 2026-10-07T13:40:59.017000+00:00 (336h 32m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1fa\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 16770 records, 7 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 99 INFO, 2 NOT_TESTED, 76 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `argumentationAnswerEvent`: median interval between records changed substantially
  - WARNING/Medium `argumentationEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5927 | 35.34 | 1 | 3 | 0 | 2026-09-24T13:25:25.667000+00:00 | 2026-10-07T13:37:41.937000+00:00 | 312h 12m |
| InputEvent | 5229 | 31.18 | 1 | 6 | 0 | 2026-09-23T13:08:52.175000+00:00 | 2026-10-07T13:40:43.257000+00:00 | 336h 31m |
| PlayerPositionEvent | 2190 | 13.06 | 1 | 6 | 0 | 2026-09-23T13:08:46.457000+00:00 | 2026-10-07T13:40:56.684000+00:00 | 336h 32m |
| DialogueEvent | 2115 | 12.61 | 1 | 6 | 1317 | 2026-09-23T13:09:08.769000+00:00 | 2026-10-07T13:37:27.798000+00:00 | 336h 28m |
| ObjectInterEvent | 508 | 3.03 | 1 | 6 | 0 | 2026-09-23T13:15:51.954000+00:00 | 2026-10-07T13:31:47.706000+00:00 | 336h 15m |
| TopographicMapEvent | 152 | 0.91 | 1 | 3 | 0 | 2026-09-24T13:25:46.412000+00:00 | 2026-10-07T13:40:56.501000+00:00 | 312h 15m |
| Soil Key Puzzle | 120 | 0.72 | 1 | 3 | 0 | 2026-09-25T13:12:38.053000+00:00 | 2026-10-01T13:24:36.023000+00:00 | 144h 11m |
| questEvent | 117 | 0.7 | 1 | 6 | 117 | 2026-09-23T13:09:08.758000+00:00 | 2026-10-07T13:37:23.312000+00:00 | 336h 28m |
| argumentationNodeEvent | 88 | 0.52 | 1 | 2 | 0 | 2026-09-24T13:16:07.061000+00:00 | 2026-09-30T13:30:22.678000+00:00 | 144h 14m |
| gameWindowFocusEvent | 88 | 0.52 | 1 | 7 | 0 | 2026-09-23T13:08:35.897000+00:00 | 2026-10-07T13:40:59.017000+00:00 | 336h 32m |
| gameWindowUnfocusEvent | 72 | 0.43 | 1 | 6 | 0 | 2026-09-23T13:14:51.911000+00:00 | 2026-10-07T13:40:59.007000+00:00 | 336h 26m |
| soilMachine | 70 | 0.42 | 1 | 1 | 0 | 2026-10-01T13:35:53.891000+00:00 | 2026-10-07T13:30:52.590000+00:00 | 143h 54m |
| DEBUGMenu | 30 | 0.18 | 1 | 7 | 0 | 2026-09-23T13:08:46.447000+00:00 | 2026-10-07T13:31:36.007000+00:00 | 336h 22m |
| gameStartEvent | 20 | 0.12 | 1 | 1 | 0 | 2026-09-23T13:08:35.898000+00:00 | 2026-10-07T13:11:37.166000+00:00 | 336h 3m |
| argumentationAnswerEvent | 19 | 0.11 | 1 | 2 | 0 | 2026-09-24T13:16:12.954000+00:00 | 2026-09-30T13:30:26.340000+00:00 | 144h 14m |
| argumentationToolEvent | 9 | 0.05 | 1 | 1 | 0 | 2026-09-24T13:15:51.995000+00:00 | 2026-09-24T13:17:05.503000+00:00 | 1m 13s |
| argumentationEvent | 7 | 0.04 | 1 | 2 | 0 | 2026-09-24T13:15:55.356000+00:00 | 2026-09-30T13:30:26.370000+00:00 | 144h 14m |
| DaniEvent | 4 | 0.02 | 1 | 1 | 0 | 2026-09-30T13:18:33.856000+00:00 | 2026-10-01T13:09:51.920000+00:00 | 23h 51m |
| crash | 3 | 0.02 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-24T13:20:46.385000+00:00 | 2026-10-01T13:18:30.489000+00:00 | 167h 57m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 604664.104s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 0.229s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 30.348s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.083s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 10027.99s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 232.026s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 6.587s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; leftArrow; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E To Place Cameras; Press E To Scan; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.2x vs baseline. 
  - Observed: 120 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 180 ft; 210 ft; 240 ft; 270 ft; 30 ft; 300 ft; 330 ft; 360 ft; 60 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 3.8x vs baseline. 
  - Observed: 19 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: A,1, 
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
  - Observed: 4; C; D 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.3x vs baseline. 
  - Observed: 20 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 14.0x vs baseline. 
  - Observed: 70 records 
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
  - Observed: 25 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[180] _id=6ab3d1a3485cab4c954bd2e2 ts=2026-09-23T13:18:27.3630000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[245] _id=6ab3d295485cab4c954bf418 ts=2026-09-23T13:22:29.5710000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[304] _id=6ab3d307485cab4c954c038e ts=2026-09-23T13:24:23.4550000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[5213] _id=6abbb59a485cab4c957c1960 ts=2026-09-29T12:56:57.9430000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[5248] _id=6abbb708485cab4c957c1a64 ts=2026-09-29T13:03:03.4840000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[5901] _id=6abbb98a485cab4c957c4e63 ts=2026-09-29T13:13:46.1450000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 20 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 20} 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[2] _id=6ab3cf53485cab4c954b87b0 ts=2026-09-23T13:08:35.8980000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[342] _id=6ab51e71485cab4c954fdf0b ts=2026-09-24T12:58:25.0020000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[905] _id=6ab523fc485cab4c9550ab41 ts=2026-09-24T13:22:04.7230000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 88 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 88} 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[3] _id=6ab3cf53485cab4c954b87ae ts=2026-09-23T13:08:35.8970000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[119] _id=6ab3d0cc485cab4c954ba6d8 ts=2026-09-23T13:14:51.9210000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[128] _id=6ab3d0fc485cab4c954baf6c ts=2026-09-23T13:15:40.2940000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 72 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 72} 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[120] _id=6ab3d0cb485cab4c954ba6ce ts=2026-09-23T13:14:51.9110000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[121] _id=6ab3d0cd485cab4c954ba730 ts=2026-09-23T13:14:53.6290000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[137] _id=6ab3d10b485cab4c954bb35e ts=2026-09-23T13:15:56.0450000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 31 of 152 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[1019] _id=6ab524da485cab4c9550e0a1 ts=2026-09-24T13:25:46.4120000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1020] _id=6ab524db485cab4c9550e0e0 ts=2026-09-24T13:25:47.6570000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1035] _id=6ab524ed485cab4c9550e433 ts=2026-09-24T13:26:05.7850000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 5926 | 0.0 | 0.03 | 189.662 | 1.145 | 345665.158 | 0.32 | 3669 | 12 |
| InputEvent | 5228 | 0.0 | 0.95 | 231.735 | 12.918 | 334912.698 | 0.26 | 198 | 12 |
| PlayerPositionEvent | 2176 | 8.74 | 10.0 | 517.79 | 10.14 | 334906.294 | 0.12 | 0 | 10 |
| DialogueEvent | 2114 | 0.001 | 4.745 | 572.989 | 45.703 | 335152.568 | 0.1 | 561 | 11 |
| ObjectInterEvent | 507 | 0.004 | 7.396 | 2387.684 | 241.964 | 334956.828 | 0.03 | 2 | 12 |
| TopographicMapEvent | 151 | 0.02 | 1.606 | 7444.438 | 292.899 | 519944.021 | 0.01 | 2 | 6 |
| Soil Key Puzzle | 119 | 0.13 | 0.55 | 4362.336 | 9.873 | 259386.527 | 0.01 | 0 | 3 |
| questEvent | 116 | 0.0 | 181.901 | 10442.194 | 84303.278 | 335182.835 | 0.01 | 25 | 16 |
| argumentationNodeEvent | 87 | 0.017 | 0.265 | 5968.455 | 1.417 | 519153.849 | 0.01 | 22 | 1 |
| gameWindowFocusEvent | 87 | 0.767 | 232.026 | 13925.783 | 84400.142 | 334898.87 | 0.0 | 0 | 26 |
| gameWindowUnfocusEvent | 71 | 0.164 | 199.02 | 17058.691 | 84764.168 | 335836.092 | 0.0 | 0 | 20 |
| soilMachine | 69 | 0.521 | 6.587 | 7508.677 | 4853.554 | 335097.862 | 0.01 | 0 | 4 |
| DEBUGMenu | 29 | 11.098 | 1273.338 | 41757.571 | 188861.408 | 335637.259 | 0.0 | 0 | 22 |
| gameStartEvent | 19 | 257.542 | 10027.99 | 63672.698 | 265170.728 | 335640.83 | 0.0 | 0 | 16 |
| argumentationAnswerEvent | 18 | 0.149 | 0.229 | 28847.41 | 77931.695 | 519169.153 | 0.0 | 0 | 1 |
| argumentationToolEvent | 8 | 0.134 | 1.083 | 9.188 | 42.926 | 64.255 | 6.53 | 0 | 0 |
| argumentationEvent | 6 | 0.02 | 30.348 | 86545.169 | 389370.723 | 519147.183 | 0.0 | 1 | 1 |
| DaniEvent | 3 | 0.689 | 3.058 | 28626.021 | 77287.191 | 85874.317 | 0.0 | 0 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 604664.104 | 604664.104 | 604664.104 | 604664.104 | 604664.104 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 3 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[9838] _id=6abe5b0d485cab4c95a43e89 ts=2026-10-01T13:07:25.6630000Z == 6aa413b141b41dbac0c7f1fa.jsonl[9840] _id=6abe5b0d485cab4c95a43e8f ts=2026-10-01T13:07:25.6630000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[9842] _id=6abe5b0e485cab4c95a43e97 ts=2026-10-01T13:07:25.6650000Z == 6aa413b141b41dbac0c7f1fa.jsonl[9839] _id=6abe5b0e485cab4c95a43e9d ts=2026-10-01T13:07:25.6650000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[15866] _id=6ac64699de269131f9b8c19a ts=2026-10-07T13:18:17.1060000Z == 6aa413b141b41dbac0c7f1fa.jsonl[15867] _id=6ac64699de269131f9b8c19b ts=2026-10-07T13:18:17.1060000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 293 group(s), 367 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[996] _id=6ab524ca485cab4c9550dd1f ts=2026-09-24T13:25:29.2900000Z == 6aa413b141b41dbac0c7f1fa.jsonl[1003] _id=6ab524ca485cab4c9550dd25 ts=2026-09-24T13:25:29.2900000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[993] _id=6ab524cb485cab4c9550dd61 ts=2026-09-24T13:25:29.4370000Z == 6aa413b141b41dbac0c7f1fa.jsonl[1005] _id=6ab524cb485cab4c9550dd67 ts=2026-09-24T13:25:29.4370000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1007] _id=6ab524cb485cab4c9550dd81 ts=2026-09-24T13:25:29.4590000Z == 6aa413b141b41dbac0c7f1fa.jsonl[1001] _id=6ab524cb485cab4c9550dd89 ts=2026-09-24T13:25:29.4590000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa413b141b41dbac0c7f1fa.jsonl[134] _id=6ab3d107485cab4c954bb25b ts=2026-09-23T13:15:51.9540000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[124] _id=6ab3d107485cab4c954bb265 ts=2026-09-23T13:15:51.9580000Z`; `7ms: 6aa413b141b41dbac0c7f1fa.jsonl[358] _id=6ab51e9d485cab4c954fe5c2 ts=2026-09-24T12:59:09.0710000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[352] _id=6ab51e9d485cab4c954fe5c9 ts=2026-09-24T12:59:09.0780000Z`; `601ms: 6aa413b141b41dbac0c7f1fa.jsonl[7868] _id=6abd1019485cab4c958895a8 ts=2026-09-30T13:35:21.8170000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[7873] _id=6abd101a485cab4c958895f0 ts=2026-09-30T13:35:22.4180000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1093 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa413b141b41dbac0c7f1fa.jsonl[1000] _id=6ab524ca485cab4c9550dd3f ts=2026-09-24T13:25:29.3710000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[1009] _id=6ab524ca485cab4c9550dd46 ts=2026-09-24T13:25:29.3780000Z`; `8ms: 6aa413b141b41dbac0c7f1fa.jsonl[1009] _id=6ab524ca485cab4c9550dd46 ts=2026-09-24T13:25:29.3780000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[992] _id=6ab524ca485cab4c9550dd51 ts=2026-09-24T13:25:29.3860000Z`; `22ms: 6aa413b141b41dbac0c7f1fa.jsonl[1006] _id=6ab524cb485cab4c9550dd77 ts=2026-09-24T13:25:29.4370000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[1007] _id=6ab524cb485cab4c9550dd81 ts=2026-09-24T13:25:29.4590000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 7 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `994ms: 6aa413b141b41dbac0c7f1fa.jsonl[3951] _id=6aba68ed485cab4c9567cabf ts=2026-09-28T13:17:33.7890000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[3959] _id=6aba68ee485cab4c9567cac3 ts=2026-09-28T13:17:34.7830000Z`; `979ms: 6aa413b141b41dbac0c7f1fa.jsonl[3958] _id=6aba68ee485cab4c9567cac1 ts=2026-09-28T13:17:34.0720000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[3960] _id=6aba68ef485cab4c9567cac5 ts=2026-09-28T13:17:35.0510000Z`; `971ms: 6aa413b141b41dbac0c7f1fa.jsonl[10206] _id=6abe5f10485cab4c95a556de ts=2026-10-01T13:24:32.5770000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[10202] _id=6abe5f11485cab4c95a55737 ts=2026-10-01T13:24:33.5480000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `23ms: 6aa413b141b41dbac0c7f1fa.jsonl[3235] _id=6ab67575485cab4c9554bd72 ts=2026-09-25T13:21:57.9690000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[3237] _id=6ab67576485cab4c9554bd90 ts=2026-09-25T13:21:57.9920000Z`; `761ms: 6aa413b141b41dbac0c7f1fa.jsonl[3667] _id=6ab67877485cab4c9555295e ts=2026-09-25T13:34:47.7560000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[3669] _id=6ab67878485cab4c95552972 ts=2026-09-25T13:34:48.5170000Z`; `963ms: 6aa413b141b41dbac0c7f1fa.jsonl[3814] _id=6aba6737485cab4c9567ae99 ts=2026-09-28T13:10:15.2480000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[3818] _id=6aba6738485cab4c9567aeaf ts=2026-09-28T13:10:16.2110000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 14 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `765ms: 6aa413b141b41dbac0c7f1fa.jsonl[752] _id=6ab522e1485cab4c955069bf ts=2026-09-24T13:17:21.9620000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[758] _id=6ab522e2485cab4c955069e9 ts=2026-09-24T13:17:22.7270000Z`; `175ms: 6aa413b141b41dbac0c7f1fa.jsonl[758] _id=6ab522e2485cab4c955069e9 ts=2026-09-24T13:17:22.7270000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[761] _id=6ab522e2485cab4c955069f7 ts=2026-09-24T13:17:22.9020000Z`; `207ms: 6aa413b141b41dbac0c7f1fa.jsonl[761] _id=6ab522e2485cab4c955069f7 ts=2026-09-24T13:17:22.9020000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[762] _id=6ab522e3485cab4c95506a07 ts=2026-09-24T13:17:23.1090000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `20ms: 6aa413b141b41dbac0c7f1fa.jsonl[7638] _id=6abd0ef2485cab4c958817f5 ts=2026-09-30T13:30:26.3500000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[7637] _id=6abd0ef2485cab4c9588180f ts=2026-09-30T13:30:26.3700000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 22 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `27ms: 6aa413b141b41dbac0c7f1fa.jsonl[687] _id=6ab52297485cab4c95506091 ts=2026-09-24T13:16:07.3820000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[683] _id=6ab52297485cab4c95506097 ts=2026-09-24T13:16:07.4090000Z`; `19ms: 6aa413b141b41dbac0c7f1fa.jsonl[690] _id=6ab52298485cab4c955060bf ts=2026-09-24T13:16:08.6670000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[693] _id=6ab52298485cab4c955060c1 ts=2026-09-24T13:16:08.6860000Z`; `18ms: 6aa413b141b41dbac0c7f1fa.jsonl[691] _id=6ab52299485cab4c955060df ts=2026-09-24T13:16:09.0920000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[692] _id=6ab52299485cab4c955060e5 ts=2026-09-24T13:16:09.1100000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `584ms: 6aa413b141b41dbac0c7f1fa.jsonl[714] _id=6ab522cf485cab4c95506747 ts=2026-09-24T13:17:03.0290000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[720] _id=6ab522cf485cab4c95506753 ts=2026-09-24T13:17:03.6130000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 4 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `913ms: 6aa413b141b41dbac0c7f1fa.jsonl[2059] _id=6ab525fe485cab4c95511bad ts=2026-09-24T13:30:38.2920000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[2057] _id=6ab525ff485cab4c95511bd3 ts=2026-09-24T13:30:39.2050000Z`; `807ms: 6aa413b141b41dbac0c7f1fa.jsonl[4057] _id=6aba698e485cab4c9567d679 ts=2026-09-28T13:20:14.4510000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[4059] _id=6aba698f485cab4c9567d685 ts=2026-09-28T13:20:15.2580000Z`; `991ms: 6aa413b141b41dbac0c7f1fa.jsonl[6714] _id=6abbbffa485cab4c957da28e ts=2026-09-29T13:41:14.7670000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[6712] _id=6abbbffb485cab4c957da2c8 ts=2026-09-29T13:41:15.7580000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `164ms: 6aa413b141b41dbac0c7f1fa.jsonl[2058] _id=6ab525fe485cab4c95511ba5 ts=2026-09-24T13:30:38.2840000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[2056] _id=6ab525fe485cab4c95511bb7 ts=2026-09-24T13:30:38.4480000Z`; `803ms: 6aa413b141b41dbac0c7f1fa.jsonl[4056] _id=6aba698e485cab4c9567d677 ts=2026-09-28T13:20:14.4400000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[4058] _id=6aba698f485cab4c9567d681 ts=2026-09-28T13:20:15.2430000Z`; `996ms: 6aa413b141b41dbac0c7f1fa.jsonl[6715] _id=6abbbffa485cab4c957da286 ts=2026-09-29T13:41:14.7520000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[6716] _id=6abbbffb485cab4c957da2be ts=2026-09-29T13:41:15.7480000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa413b141b41dbac0c7f1fa.jsonl[5213] _id=6abbb59a485cab4c957c1960 ts=2026-09-29T12:56:57.9430000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[5220] _id=6abbb59a485cab4c957c1962 ts=2026-09-29T12:56:57.9460000Z`; `1ms: 6aa413b141b41dbac0c7f1fa.jsonl[5248] _id=6abbb708485cab4c957c1a64 ts=2026-09-29T13:03:03.4840000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[5254] _id=6abbb708485cab4c957c1a66 ts=2026-09-29T13:03:03.4850000Z`; `3ms: 6aa413b141b41dbac0c7f1fa.jsonl[5901] _id=6abbb98a485cab4c957c4e63 ts=2026-09-29T13:13:46.1450000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[5915] _id=6abbb98a485cab4c957c4e6c ts=2026-09-29T13:13:46.1480000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `815ms: 6aa413b141b41dbac0c7f1fa.jsonl[11526] _id=6abe80d8485cab4c95ab76c8 ts=2026-10-01T15:48:41.1830000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[11517] _id=6abe80d9485cab4c95ab770a ts=2026-10-01T15:48:41.9980000Z`; `550ms: 6aa413b141b41dbac0c7f1fa.jsonl[11517] _id=6abe80d9485cab4c95ab770a ts=2026-10-01T15:48:41.9980000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[11534] _id=6abe80da485cab4c95ab7728 ts=2026-10-01T15:48:42.5480000Z`; `521ms: 6aa413b141b41dbac0c7f1fa.jsonl[16355] _id=6ac64967de269131f9b936b7 ts=2026-10-07T13:30:15.4890000Z ~ 6aa413b141b41dbac0c7f1fa.jsonl[16357] _id=6ac64968de269131f9b936e2 ts=2026-10-07T13:30:16.0100000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 22 gap(s), longest 93h 13m 
  - Evidence: 93h 13m: 6aa413b141b41dbac0c7f1fa.jsonl[11415] _id=6abe802f485cab4c95ab5ee8 ts=2026-10-01T15:45:52.3440000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11981] _id=6ac39f3fde269131f9a83fb4 ts=2026-10-05T12:59:49.6030000Z; 71h 29m: 6aa413b141b41dbac0c7f1fa.jsonl[3616] _id=6ab677da485cab4c95551524 ts=2026-09-25T13:32:10.7410000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3695] _id=6aba6519485cab4c956799e7 ts=2026-09-28T13:01:12.9270000Z; 23h 55m: 6aa413b141b41dbac0c7f1fa.jsonl[3695] _id=6aba6519485cab4c956799e7 ts=2026-09-28T13:01:12.9270000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[5212] _id=6abbb594485cab4c957c195a ts=2026-09-29T12:56:53.1670000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 23h 51m 
  - Evidence: 23h 51m: 6aa413b141b41dbac0c7f1fa.jsonl[7133] _id=6abd0c2c485cab4c9586dce5 ts=2026-09-30T13:18:36.9140000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[9932] _id=6abe5b9f485cab4c95a4592d ts=2026-10-01T13:09:51.2310000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 93h 5m 
  - Evidence: 93h 5m: 6aa413b141b41dbac0c7f1fa.jsonl[11727] _id=6abe821b485cab4c95ab91eb ts=2026-10-01T15:54:03.0520000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[12000] _id=6ac39f45de269131f9a83fe4 ts=2026-10-05T12:59:55.6200000Z; 71h 26m: 6aa413b141b41dbac0c7f1fa.jsonl[3681] _id=6ab678a0485cab4c95552d3a ts=2026-09-25T13:35:29.1950000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3723] _id=6aba6551485cab4c95679aff ts=2026-09-28T13:02:09.5130000Z; 23h 38m: 6aa413b141b41dbac0c7f1fa.jsonl[1377] _id=6ab52595485cab4c955109d7 ts=2026-09-24T13:28:53.1650000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[2082] _id=6ab671f4485cab4c95546c43 ts=2026-09-25T13:07:00.5060000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 561 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fa.jsonl[3199] _id=6ab67527485cab4c9554b5f6 ts=2026-09-25T13:20:39.5900000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3200] _id=6ab67527485cab4c9554b5f8 ts=2026-09-25T13:20:39.5910000Z; 1ms: 6aa413b141b41dbac0c7f1fa.jsonl[4906] _id=6aba6c1d485cab4c95680113 ts=2026-09-28T13:31:09.2540000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[4907] _id=6aba6c1d485cab4c95680115 ts=2026-09-28T13:31:09.2550000Z; 1ms: 6aa413b141b41dbac0c7f1fa.jsonl[5056] _id=6aba6bff485cab4c9567fffb ts=2026-09-28T13:30:39.8540000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[5054] _id=6aba6c00485cab4c95680000 ts=2026-09-28T13:30:39.8550000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 167h 57m 
  - Evidence: 167h 57m: 6aa413b141b41dbac0c7f1fa.jsonl[902] _id=6ab523ae485cab4c955098ff ts=2026-09-24T13:20:46.3850000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[10111] _id=6abe5da6485cab4c95a4b049 ts=2026-10-01T13:18:30.4890000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 93h 1m 
  - Evidence: 93h 1m: 6aa413b141b41dbac0c7f1fa.jsonl[11966] _id=6abe830a485cab4c95aba14a ts=2026-10-01T15:58:02.6980000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11982] _id=6ac39f45de269131f9a83fcc ts=2026-10-05T12:59:55.3960000Z; 71h 26m: 6aa413b141b41dbac0c7f1fa.jsonl[3676] _id=6ab67881485cab4c95552a32 ts=2026-09-25T13:34:57.5230000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3699] _id=6aba651f485cab4c95679a15 ts=2026-09-28T13:01:18.7420000Z; 23h 36m: 6aa413b141b41dbac0c7f1fa.jsonl[2054] _id=6ab525f9485cab4c95511ada ts=2026-09-24T13:30:33.0840000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[2091] _id=6ab671e5485cab4c95546b83 ts=2026-09-25T13:06:45.0240000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 198 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[15866] _id=6ac64699de269131f9b8c19a ts=2026-10-07T13:18:17.1060000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[15867] _id=6ac64699de269131f9b8c19b ts=2026-10-07T13:18:17.1060000Z; 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[9838] _id=6abe5b0d485cab4c95a43e89 ts=2026-10-01T13:07:25.6630000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[9840] _id=6abe5b0d485cab4c95a43e8f ts=2026-10-01T13:07:25.6630000Z; 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[9842] _id=6abe5b0e485cab4c95a43e97 ts=2026-10-01T13:07:25.6650000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[9839] _id=6abe5b0e485cab4c95a43e9d ts=2026-10-01T13:07:25.6650000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 93h 2m 
  - Evidence: 93h 2m: 6aa413b141b41dbac0c7f1fa.jsonl[11935] _id=6abe82f1485cab4c95ab9fa2 ts=2026-10-01T15:57:37.7880000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11987] _id=6ac39f58de269131f9a84037 ts=2026-10-05T13:00:14.6160000Z; 72h 4m: 6aa413b141b41dbac0c7f1fa.jsonl[2993] _id=6ab67345485cab4c955485fb ts=2026-09-25T13:12:38.0550000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3932] _id=6aba68d7485cab4c9567c959 ts=2026-09-28T13:17:11.1340000Z; 23h 54m: 6aa413b141b41dbac0c7f1fa.jsonl[6253] _id=6abbba55485cab4c957c702c ts=2026-09-29T13:17:09.3570000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[6886] _id=6abd0a7a485cab4c9586a301 ts=2026-09-30T13:11:22.2930000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6aa413b141b41dbac0c7f1fa.jsonl[134] _id=6ab3d107485cab4c954bb25b ts=2026-09-23T13:15:51.9540000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[124] _id=6ab3d107485cab4c954bb265 ts=2026-09-23T13:15:51.9580000Z; 7ms: 6aa413b141b41dbac0c7f1fa.jsonl[358] _id=6ab51e9d485cab4c954fe5c2 ts=2026-09-24T12:59:09.0710000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[352] _id=6ab51e9d485cab4c954fe5c9 ts=2026-09-24T12:59:09.0780000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 93h 1m 
  - Evidence: 93h 1m: 6aa413b141b41dbac0c7f1fa.jsonl[11963] _id=6abe830b485cab4c95aba14c ts=2026-10-01T15:58:03.3180000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11988] _id=6ac39f45de269131f9a83fca ts=2026-10-05T12:59:49.6120000Z; 71h 25m: 6aa413b141b41dbac0c7f1fa.jsonl[3682] _id=6ab6789c485cab4c95552cd2 ts=2026-09-25T13:35:24.4610000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3698] _id=6aba651f485cab4c95679a13 ts=2026-09-28T13:01:12.9340000Z; 23h 36m: 6aa413b141b41dbac0c7f1fa.jsonl[2041] _id=6ab525f7485cab4c95511a77 ts=2026-09-24T13:30:31.4180000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[2090] _id=6ab671e5485cab4c95546b80 ts=2026-09-25T13:06:39.0630000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 96h 1m 
  - Evidence: 96h 1m: 6aa413b141b41dbac0c7f1fa.jsonl[10649] _id=6abe5f89485cab4c95a58099 ts=2026-10-01T13:26:31.4060000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[12866] _id=6ac3a5c9de269131f9a9089f ts=2026-10-05T13:27:36.5640000Z; 72h 8m: 6aa413b141b41dbac0c7f1fa.jsonl[2968] _id=6ab67318485cab4c95548407 ts=2026-09-25T13:11:51.4990000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[4004] _id=6aba697c485cab4c9567d481 ts=2026-09-28T13:19:55.6270000Z; 24h 11m: 6aa413b141b41dbac0c7f1fa.jsonl[6430] _id=6abbbbb0485cab4c957cc2ab ts=2026-09-29T13:22:54.2920000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7907] _id=6abd0fd6485cab4c95887849 ts=2026-09-30T13:34:13.0610000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3669 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[1003] _id=6ab524ca485cab4c9550dd25 ts=2026-09-24T13:25:29.2900000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[994] _id=6ab524ca485cab4c9550dd2b ts=2026-09-24T13:25:29.2900000Z; 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[1004] _id=6ab524ca485cab4c9550dd2f ts=2026-09-24T13:25:29.2900000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[1008] _id=6ab524ca485cab4c9550dd34 ts=2026-09-24T13:25:29.2900000Z; 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[1005] _id=6ab524cb485cab4c9550dd67 ts=2026-09-24T13:25:29.4370000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[1011] _id=6ab524cb485cab4c9550dd71 ts=2026-09-24T13:25:29.4370000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 72h 3m 
  - Evidence: 72h 3m: 6aa413b141b41dbac0c7f1fa.jsonl[3053] _id=6ab6739c485cab4c95548c71 ts=2026-09-25T13:14:04.6010000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3931] _id=6aba68d7485cab4c9567c955 ts=2026-09-28T13:17:11.1280000Z; 48h 15m: 6aa413b141b41dbac0c7f1fa.jsonl[3962] _id=6aba68f0485cab4c9567cacb ts=2026-09-28T13:17:36.0410000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7761] _id=6abd0f9f485cab4c95885ed2 ts=2026-09-30T13:33:19.9260000Z; 23h 50m: 6aa413b141b41dbac0c7f1fa.jsonl[7778] _id=6abd0fb2485cab4c9588680b ts=2026-09-30T13:33:37.9740000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[10168] _id=6abe5f04485cab4c95a5527b ts=2026-10-01T13:24:20.5950000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 144h 25m 
  - Evidence: 144h 25m: 6aa413b141b41dbac0c7f1fa.jsonl[10035] _id=6abe5c8a485cab4c95a48189 ts=2026-10-01T13:13:46.5370000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[16694] _id=6ac64b92de269131f9b9bc0f ts=2026-10-07T13:39:30.5580000Z; 71h 31m: 6aa413b141b41dbac0c7f1fa.jsonl[3674] _id=6ab6787c485cab4c955529ce ts=2026-09-25T13:34:52.9240000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3774] _id=6aba6647485cab4c9567a25d ts=2026-09-28T13:06:15.0770000Z; 24h 23m: 6aa413b141b41dbac0c7f1fa.jsonl[3819] _id=6aba673c485cab4c9567af09 ts=2026-09-28T13:10:20.5960000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[6623] _id=6abbbe41485cab4c957d5618 ts=2026-09-29T13:33:53.1900000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.020s..0.023s shown 
  - Evidence: 20ms: 6aa413b141b41dbac0c7f1fa.jsonl[3234] _id=6ab67575485cab4c9554bd6e ts=2026-09-25T13:21:57.9490000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3235] _id=6ab67575485cab4c9554bd72 ts=2026-09-25T13:21:57.9690000Z; 23ms: 6aa413b141b41dbac0c7f1fa.jsonl[3235] _id=6ab67575485cab4c9554bd72 ts=2026-09-25T13:21:57.9690000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3237] _id=6ab67576485cab4c9554bd90 ts=2026-09-25T13:21:57.9920000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 6aa413b141b41dbac0c7f1fa.jsonl[792] _id=6ab522f1485cab4c95506d95 ts=2026-09-24T13:17:37.1870000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7634] _id=6abd0ef2485cab4c958817ef ts=2026-09-30T13:30:26.3400000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 6aa413b141b41dbac0c7f1fa.jsonl[789] _id=6ab522f1485cab4c95506d9f ts=2026-09-24T13:17:37.2110000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7588] _id=6abd0edc485cab4c95880da8 ts=2026-09-30T13:30:04.3940000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.020s..0.020s shown 
  - Evidence: 20ms: 6aa413b141b41dbac0c7f1fa.jsonl[7638] _id=6abd0ef2485cab4c958817f5 ts=2026-09-30T13:30:26.3500000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7637] _id=6abd0ef2485cab4c9588180f ts=2026-09-30T13:30:26.3700000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 12m 
  - Evidence: 144h 12m: 6aa413b141b41dbac0c7f1fa.jsonl[784] _id=6ab522ef485cab4c95506d5d ts=2026-09-24T13:17:35.8930000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7595] _id=6abd0ee1485cab4c95880f50 ts=2026-09-30T13:30:09.7420000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.017s..0.019s shown 
  - Evidence: 17ms: 6aa413b141b41dbac0c7f1fa.jsonl[7587] _id=6abd0ee7485cab4c958811e4 ts=2026-09-30T13:30:15.0430000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[7578] _id=6abd0ee7485cab4c958811f7 ts=2026-09-30T13:30:15.0600000Z; 18ms: 6aa413b141b41dbac0c7f1fa.jsonl[691] _id=6ab52299485cab4c955060df ts=2026-09-24T13:16:09.0920000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[692] _id=6ab52299485cab4c955060e5 ts=2026-09-24T13:16:09.1100000Z; 19ms: 6aa413b141b41dbac0c7f1fa.jsonl[690] _id=6ab52298485cab4c955060bf ts=2026-09-24T13:16:08.6670000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[693] _id=6ab52298485cab4c955060c1 ts=2026-09-24T13:16:08.6860000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 93h 14m 
  - Evidence: 93h 14m: 6aa413b141b41dbac0c7f1fa.jsonl[11414] _id=6abe8026485cab4c95ab5d1b ts=2026-10-01T15:45:42.7570000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11980] _id=6ac39f39de269131f9a83f7c ts=2026-10-05T12:59:43.5870000Z; 71h 29m: 6aa413b141b41dbac0c7f1fa.jsonl[3614] _id=6ab677d5485cab4c95551492 ts=2026-09-25T13:32:05.3460000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3694] _id=6aba6512485cab4c956799c3 ts=2026-09-28T13:01:06.0630000Z; 24h 14m: 6aa413b141b41dbac0c7f1fa.jsonl[13654] _id=6ac4f02ade269131f9affdd1 ts=2026-10-06T12:57:14.6130000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[15401] _id=6ac64509de269131f9b8b845 ts=2026-10-07T13:11:37.1660000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 26 gap(s), longest 93h 1m 
  - Evidence: 93h 1m: 6aa413b141b41dbac0c7f1fa.jsonl[11968] _id=6abe830c485cab4c95aba172 ts=2026-10-01T15:58:04.7160000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11975] _id=6ac39f39de269131f9a83f7a ts=2026-10-05T12:59:43.5860000Z; 71h 25m: 6aa413b141b41dbac0c7f1fa.jsonl[3685] _id=6ab678a2485cab4c95552d5e ts=2026-09-25T13:35:30.3840000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3693] _id=6aba6512485cab4c956799c1 ts=2026-09-28T13:01:06.0620000Z; 23h 35m: 6aa413b141b41dbac0c7f1fa.jsonl[2057] _id=6ab525ff485cab4c95511bd3 ts=2026-09-24T13:30:39.2050000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[2094] _id=6ab671d9485cab4c95546b17 ts=2026-09-25T13:06:33.3560000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 93h 17m 
  - Evidence: 93h 17m: 6aa413b141b41dbac0c7f1fa.jsonl[11969] _id=6abe830f485cab4c95aba198 ts=2026-10-01T15:58:07.0820000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[12474] _id=6ac3a2e4de269131f9a87db4 ts=2026-10-05T13:15:23.1740000Z; 71h 44m: 6aa413b141b41dbac0c7f1fa.jsonl[3684] _id=6ab678a2485cab4c95552d53 ts=2026-09-25T13:35:30.3750000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[4056] _id=6aba698e485cab4c9567d677 ts=2026-09-28T13:20:14.4400000Z; 23h 50m: 6aa413b141b41dbac0c7f1fa.jsonl[2056] _id=6ab525fe485cab4c95511bb7 ts=2026-09-24T13:30:38.4480000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3216] _id=6ab6753e485cab4c9554b81e ts=2026-09-25T13:21:02.6910000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 93h 6m 
  - Evidence: 93h 6m: 6aa413b141b41dbac0c7f1fa.jsonl[11664] _id=6abe81fc485cab4c95ab8f78 ts=2026-10-01T15:53:32.6230000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[11992] _id=6ac39f45de269131f9a83fe2 ts=2026-10-05T12:59:55.4580000Z; 71h 29m: 6aa413b141b41dbac0c7f1fa.jsonl[3619] _id=6ab677dc485cab4c9555156c ts=2026-09-25T13:32:11.5660000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[3706] _id=6aba6520485cab4c95679a33 ts=2026-09-28T13:01:18.8120000Z; 23h 43m: 6aa413b141b41dbac0c7f1fa.jsonl[939] _id=6ab52459485cab4c9550c5cf ts=2026-09-24T13:23:36.9740000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[2105] _id=6ab671e7485cab4c95546bb5 ts=2026-09-25T13:06:45.1120000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 25 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fa.jsonl[15403] _id=6ac64519de269131f9b8b862 ts=2026-10-07T13:11:53.1540000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[15404] _id=6ac64519de269131f9b8b863 ts=2026-10-07T13:11:53.1540000Z; 1ms: 6aa413b141b41dbac0c7f1fa.jsonl[5248] _id=6abbb708485cab4c957c1a64 ts=2026-09-29T13:03:03.4840000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[5254] _id=6abbb708485cab4c957c1a66 ts=2026-09-29T13:03:03.4850000Z; 2ms: 6aa413b141b41dbac0c7f1fa.jsonl[643] _id=6ab52234485cab4c95504a9a ts=2026-09-24T13:14:28.6030000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[644] _id=6ab52234485cab4c95504aa1 ts=2026-09-24T13:14:28.6050000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 93h 4m 
  - Evidence: 93h 4m: 6aa413b141b41dbac0c7f1fa.jsonl[11934] _id=6abe82f1485cab4c95ab9f9e ts=2026-10-01T15:57:37.7790000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[12119] _id=6ac39fe5de269131f9a8459a ts=2026-10-05T13:02:35.6410000Z; 23h 58m: 6aa413b141b41dbac0c7f1fa.jsonl[12822] _id=6ac3a561de269131f9a8f6b3 ts=2026-10-05T13:25:53.6670000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[14419] _id=6ac4f675de269131f9b068aa ts=2026-10-06T13:24:05.0680000Z; 23h 49m: 6aa413b141b41dbac0c7f1fa.jsonl[14733] _id=6ac4f892de269131f9b0c6cc ts=2026-10-06T13:33:06.8280000Z -> 6aa413b141b41dbac0c7f1fa.jsonl[16029] _id=6ac647acde269131f9b8d7f5 ts=2026-10-07T13:22:52.3160000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 17 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[637] _id=6ab52225485cab4c9550459b ts=2026-09-24T13:14:13.5770000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[802] _id=6ab52314485cab4c955075fd ts=2026-09-24T13:18:12.5670000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[3546] _id=6ab67749485cab4c955508d2 ts=2026-09-25T13:29:46.0520000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 151 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[1331] _id=6ab5258a485cab4c9551085b ts=2026-09-24T13:28:40.0200000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1334] _id=6ab5258a485cab4c95510869 ts=2026-09-24T13:28:40.2810000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1347] _id=6ab5258a485cab4c9551086f ts=2026-09-24T13:28:40.3090000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 469 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[1164] _id=6ab52553485cab4c9550fe9d ts=2026-09-24T13:25:26.2350000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[993] _id=6ab524cb485cab4c9550dd61 ts=2026-09-24T13:25:29.4370000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1005] _id=6ab524cb485cab4c9550dd67 ts=2026-09-24T13:25:29.4370000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[7637] _id=6abd0ef2485cab4c9588180f ts=2026-09-30T13:30:26.3700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[683] _id=6ab52297485cab4c95506097 ts=2026-09-24T13:16:07.4090000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[11423] _id=6abe803d485cab4c95ab60fb ts=2026-10-01T15:46:05.9080000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[12002] _id=6ac39f4cde269131f9a83ff8 ts=2026-10-05T13:00:03.0760000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[12489] _id=6ac3a33fde269131f9a88adf ts=2026-10-05T13:16:53.8200000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[5] _id=6ab3cf64485cab4c954b87ee ts=?`; `6aa413b141b41dbac0c7f1fa.jsonl[6723] _id=6abd081f485cab4c95867ddf ts=?`; `6aa413b141b41dbac0c7f1fa.jsonl[13640] _id=6ac4f03ade269131f9affded ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 962 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[1306] _id=6ab52587485cab4c955107d7 ts=2026-09-24T13:28:37.7850000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1374] _id=6ab5258f485cab4c95510943 ts=2026-09-24T13:28:45.8590000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1375] _id=6ab5258f485cab4c95510945 ts=2026-09-24T13:28:45.8800000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1329 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[1003] _id=6ab524ca485cab4c9550dd25 ts=2026-09-24T13:25:29.2900000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[994] _id=6ab524ca485cab4c9550dd2b ts=2026-09-24T13:25:29.2900000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1166] _id=6ab52554485cab4c9550feb5 ts=2026-09-24T13:25:30.2860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 27 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[3235] _id=6ab67575485cab4c9554bd72 ts=2026-09-25T13:21:57.9690000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[3237] _id=6ab67576485cab4c9554bd90 ts=2026-09-25T13:21:57.9920000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[3308] _id=6ab67640485cab4c9554de4e ts=2026-09-25T13:25:20.4850000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 9 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[693] _id=6ab52298485cab4c955060c1 ts=2026-09-24T13:16:08.6860000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[695] _id=6ab5229a485cab4c95506113 ts=2026-09-24T13:16:10.4280000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[732] _id=6ab522d7485cab4c9550684c ts=2026-09-24T13:17:11.0000000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[718] _id=6ab522ce485cab4c95506733 ts=2026-09-24T13:17:02.0180000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[719] _id=6ab522cf485cab4c9550674b ts=2026-09-24T13:17:03.1630000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[721] _id=6ab522d0485cab4c95506775 ts=2026-09-24T13:17:04.3470000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 25 unmatched 'DialogueStartEvent' (totals: 403 start, 395 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 268 unmatched 'BecameCameraCentered' (totals: 1148 open, 1031 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 177 unmatched 'BecameVisible' (totals: 1728 open, 2020 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 30 open, 28 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'argumentationNodeHoverStart' (totals: 40 open, 38 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 5 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 22 unmatched 'questActiveEvent' (totals: 65 start, 52 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 579 of 16766 adjacent _id pairs reverse in client time; worst 140.2s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1fa.jsonl[1089] _id=6ab52551485cab4c9550fe2b ts=2026-09-24T13:27:45.8280000Z`; `6aa413b141b41dbac0c7f1fa.jsonl[1120] _id=6ab52552485cab4c9550fe4b ts=2026-09-24T13:25:25.6670000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -142.01s, max +6.59s over 16767 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa413b141b41dbac0c7f1fa\coverage.yaml

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
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
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

### `PuzzlePieceVisibleEvent` — 5927 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3245); Unit 4 Dev (2072); Unit 3 Dungeon Dev (610)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.14s, n=5926)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5927/5927 records)
    "BecameInvisible"  x2020
    "BecameVisible"  x1728
    "BecameCameraCentered"  x1148
    "BecameCameraUncentered"  x1031
data.pieceId  (string, 5927/5927 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 5927/5927 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 5229 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1946); Unit 2 Prod (Refactor) (988); Unit 3 Dungeon Dev (804); Unit 3 Dev (646); Unit 4 Dev (588); Unit 1 Dev (257)
- **Intervals:** median 0.95s (p5 0.08s / p95 12.92s, n=5228)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5229/5229 records)
    "pressed"  x5229
data.actionType  (string, 5229/5229 records)
    "Move"  x3150
    "Interact"  x995
    "Sprint"  x497
    "Jump"  x480
    "Hoverboard"  x47
    "Ascend"  x33
    "Map"  x11
    "SkipCinematic"  x9
    "Pause"  x4
    "ToggleDebug"  x3
data.key  (string, 5229/5229 records, 15 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5229/5229 records)
    "Player"  x4891
    "Drone"  x338
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2190 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (675); Unit 4 Dev - Dungeon (524); Unit 4 Dev (286); Unit 1 Dev (236); Unit 3 Dev (235); Unit 3 Dungeon Dev (234)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.14s, n=2176)
- **Fields under `data`:**

```text
data.position  (object, 2190/2190 records)
data.position.x  (number, 2190/2190 records)
    numeric range -692.034 .. 1450.87 (878 unique)
data.position.y  (number, 2190/2190 records)
    numeric range -114.326 .. 157.105 (535 unique)
data.position.z  (number, 2190/2190 records)
    numeric range -1036.97 .. 2096.64 (879 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2115 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (632); Unit 4 Dev - Dungeon (407); Unit 3 Dev (320); Unit 3 Dungeon Dev (290); Unit 1 Dev (259); Unit 4 Dev (207)
- **eventKey:** present on 1317 of 2115 records
- **Intervals:** median 4.75s (p5 0.00s / p95 45.70s, n=2114)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1317; [conversationId, dialogueEventType] x798
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2115/2115 records)
    numeric range 8 .. 111 (40 unique)
data.dialogueEventType  (string, 2115/2115 records)
    "DialogueNodeEvent"  x1317
    "DialogueStartEvent"  x403
    "DialogueFinishEvent"  x395
data.nodeId  (number, 1317/2115 records)
    numeric range 0 .. 290 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 508 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (338); Unit 3 Dungeon Dev (80); Unit 2 Prod (Refactor) (39); Unit 4 Dev (24); Unit 1 Dev (15); Unit 3 Dev (12)
- **Intervals:** median 7.40s (p5 1.08s / p95 241.96s, n=507)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 508/508 records)
    30 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 508/508 records)
    76 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `TopographicMapEvent` — 152 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (92); Unit 3 Dev (39); Unit 4 Dev (21)
- **Intervals:** median 1.61s (p5 0.48s / p95 292.90s, n=151)
- **`data` key-set variants:** [actionType, featureUsed, location] x63; [actionType, featureUsed] x58; [actionType, featureUsed, legendName] x31
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 152/152 records)
    "WaypointMoveEvent"  x52
    "MapOpenEvent"  x30
    "MapCloseEvent"  x28
    "Selected"  x25
    "WaypointSetEvent"  x8
    "Unselected"  x6
    "WaypointResetEvent"  x3
data.featureUsed  (string, 152/152 records)
    "Waypoint"  x63
    "Map"  x58
    "Legend"  x31
data.legendName  (string, 31/152 records)
    "360 ft"  x7
    "300 ft"  x5
    "0 ft"  x3
    "60 ft"  x3
    "180 ft"  x2
    "210 ft"  x2
    "240 ft"  x2
    "270 ft"  x2
    "330 ft"  x2
    "30 ft"  x1
    "90 ft"  x1
    "Water"  x1
data.location  (object, 63/152 records)
data.location.x  (number, 63/152 records)
    numeric range -402.462 .. 564.12 (55 unique)
data.location.y  (number, 63/152 records)
    numeric range -311.18 .. 306.034 (57 unique)
data.location.z  (number, 63/152 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `Soil Key Puzzle` — 120 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (84); Unit 4 Dev (20); Unit 3 Dev (16)
- **Intervals:** median 0.55s (p5 0.18s / p95 9.87s, n=119)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x112; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/120 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/120 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 112/120 records)
    "RightDrag"  x59
    "LeftDrag"  x53
data.currentSoilType  (string, 112/120 records)
    "CLAYSAND"  x29
    "SAND"  x26
    "CLAY"  x22
    "SANDGRAVEL"  x20
    "CLAYROCK"  x7
    "GRAVEL"  x6
    "BEDROCK"  x2
data.isCorrectSelection  (string, 112/120 records)
    "false"  x78
    "true"  x34
data.waterLevelStatus  (string, 112/120 records)
    "Proper"  x52
    "TooLow"  x35
    "TooHigh"  x25
data.waterRetentionChange  (string, 112/120 records)
    "Decrease"  x47
    "NoChange"  x34
    "Increase"  x31
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 117 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (44); Unit 2 Prod (Refactor) (24); Unit 4 Dev (18); Unit 1 Dev (17); Unit 3 Dev (9); Unit 3 Dungeon Dev (5)
- **eventKey:** present on 117 of 117 records
- **Intervals:** median 181.90s (p5 0.00s / p95 84303.28s, n=116)
- **`data` key-set variants:** [questEventType, questID, questName] x65; [questEventType, questID, questName, questSuccessOrFailure] x52
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 117/117 records)
    "questActiveEvent"  x65
    "questFinishEvent"  x52
data.questID  (string, 117/117 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 117/117 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 52/117 records)
    "Succeeded"  x52
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 88 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (55); Unit 3 Dev (33)
- **Intervals:** median 0.27s (p5 0.02s / p95 1.42s, n=87)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 88/88 records)
    "argumentationNodeHoverStart"  x40
    "argumentationNodeHoverEnd"  x38
    "argumentationNodeAdd"  x8
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 88/88 records)
    "Unit 1 - Freshwater"  x43
    "Unit 3 - Pollution Upstream"  x33
    "Unit 1 - Argumentation Tutorial"  x12
data.nodeName  (string, 88/88 records)
    "A"  x29
    "II"  x16
    "I"  x15
    "1"  x13
    "2"  x8
    "5"  x3
    "3"  x2
    "B"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `gameWindowFocusEvent` — 88 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** Unit 2 Prod (Refactor) (23); MainMenu (20); Unit 4 Dev - Dungeon (13); Unit 1 Dev (10); Unit 4 Dev (9); Unit 3 Dungeon Dev (8); Unit 3 Dev (5)
- **Intervals:** median 232.03s (p5 1.74s / p95 84400.14s, n=87)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 88/88 records)
    true  x88
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameWindowUnfocusEvent` — 72 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 4 Dev - Dungeon (15); Unit 1 Dev (11); Unit 4 Dev (9); Unit 3 Dungeon Dev (8); Unit 3 Dev (5)
- **Intervals:** median 199.02s (p5 0.90s / p95 84764.17s, n=71)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 72/72 records)
    false  x72
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `soilMachine` — 70 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (70)
- **Intervals:** median 6.59s (p5 0.73s / p95 4853.55s, n=69)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 70/70 records)
    "ChangeCanister"  x70
data.canisterType  (string, 70/70 records)
    "Clay"  x23
    "Gravel"  x18
    "Sand"  x15
    "Bedrock"  x14
data.floor  (string, 70/70 records)
    "5"  x32
    "4"  x21
    "3"  x15
    "2"  x2
data.machine  (string, 70/70 records)
    "1"  x67
    "2"  x3
data.row  (string, 70/70 records)
    "TopRow"  x53
    "BottomRow"  x17
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 4 Dev - Dungeon (7); Unit 4 Dev (6); Unit 3 Dungeon Dev (3); Unit 1 Dev (2); Unit 3 Dev (2); MainMenu (1)
- **Intervals:** median 1273.34s (p5 251.67s / p95 188861.41s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 20 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (20)
- **Intervals:** median 10027.99s (p5 258.78s / p95 265170.73s, n=19)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 20/20 records)
    true  x20
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 19 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (18); Unit 3 Dev (1)
- **Intervals:** median 0.23s (p5 0.16s / p95 77931.69s, n=18)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 19/19 records)
    "submitAnswerEvent"  x19
data.answerSubmitted  (string, 19/19 records)
    "A,1,II"  x16
    "A,1,"  x1
    "A,1,I"  x1
    "A,5,I"  x1
data.argumentationTitle  (string, 19/19 records)
    "Unit 1 - Freshwater"  x17
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationToolEvent` — 9 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (9)
- **Intervals:** median 1.08s (p5 0.24s / p95 42.93s, n=8)
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

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 30.35s (p5 5.46s / p95 389370.72s, n=6)
- **Open findings:** 2 — see sections 5-8
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
- **Intervals:** median 3.06s (p5 0.93s / p95 77287.19s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Close"  x2
    "Open"  x2
data.toolName  (string, 4/4 records, 4 empty-string)
    ""  x4
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Permissions check failed"  x2
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 1 empty-string)
    "TypeError: Permissions check failed"  x2
    ""  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x3
data.unitId  (string, 3/3 records)
    "unit1"  x1
    "unit2"  x1
    "unit4"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 604664.10s (p5 604664.10s / p95 604664.10s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `EndOfUnit` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (84 records)
- `TopographicMapEvent` data.actionType: "Selected" (25x); "Unselected" (6x); "WaypointMoveEvent" (52x); "WaypointResetEvent" (3x); "WaypointSetEvent" (8x)
- `TopographicMapEvent` data.featureUsed: "Legend" (31x); "Waypoint" (63x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (14x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*