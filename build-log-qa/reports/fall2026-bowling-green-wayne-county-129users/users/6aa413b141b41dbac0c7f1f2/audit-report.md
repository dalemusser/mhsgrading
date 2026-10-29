# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f2

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f2
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f2.jsonl
- **Records:** 14845 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f2
- **Time span:** 2026-09-23T13:03:07.864000+00:00 .. 2026-10-07T13:40:55.651000+00:00 (336h 37m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f2\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 14845 records, 7 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 96 INFO, 2 NOT_TESTED, 82 PASS.
- Top items needing attention:
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
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
| InputEvent | 5680 | 38.26 | 1 | 5 | 0 | 2026-09-23T13:06:59.235000+00:00 | 2026-10-07T13:40:53.212000+00:00 | 336h 33m |
| PuzzlePieceVisibleEvent | 4740 | 31.93 | 1 | 2 | 0 | 2026-09-25T13:06:12.016000+00:00 | 2026-10-07T13:29:41.251000+00:00 | 288h 23m |
| PlayerPositionEvent | 2170 | 14.62 | 1 | 5 | 0 | 2026-09-23T13:06:53.803000+00:00 | 2026-10-07T13:40:55.651000+00:00 | 336h 34m |
| DialogueEvent | 1268 | 8.54 | 1 | 5 | 813 | 2026-09-23T13:07:15.935000+00:00 | 2026-10-07T13:40:48.848000+00:00 | 336h 33m |
| ObjectInterEvent | 386 | 2.6 | 1 | 4 | 0 | 2026-09-23T13:13:06.897000+00:00 | 2026-10-07T13:35:04.151000+00:00 | 336h 21m |
| argumentationNodeEvent | 141 | 0.95 | 1 | 1 | 0 | 2026-09-24T13:19:36.164000+00:00 | 2026-09-24T13:25:19.372000+00:00 | 5m 43s |
| TopographicMapEvent | 132 | 0.89 | 1 | 4 | 0 | 2026-09-25T13:04:50.209000+00:00 | 2026-10-01T13:34:39.264000+00:00 | 144h 29m |
| questEvent | 84 | 0.57 | 1 | 5 | 84 | 2026-09-23T13:07:15.914000+00:00 | 2026-10-07T13:33:08.679000+00:00 | 336h 25m |
| Soil Key Puzzle | 60 | 0.4 | 1 | 2 | 0 | 2026-09-25T13:15:10.152000+00:00 | 2026-10-01T13:04:46.012000+00:00 | 143h 49m |
| gameWindowFocusEvent | 39 | 0.26 | 1 | 7 | 0 | 2026-09-23T13:03:07.864000+00:00 | 2026-10-07T13:40:55.211000+00:00 | 336h 37m |
| soilMachine | 35 | 0.24 | 1 | 1 | 0 | 2026-10-05T13:09:34.125000+00:00 | 2026-10-06T13:35:32.947000+00:00 | 24h 25m |
| DEBUGMenu | 30 | 0.2 | 1 | 6 | 0 | 2026-09-23T13:06:53.793000+00:00 | 2026-10-07T13:30:04.899000+00:00 | 336h 23m |
| gameStartEvent | 21 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:03:07.865000+00:00 | 2026-10-07T13:21:45.267000+00:00 | 336h 18m |
| argumentationAnswerEvent | 20 | 0.13 | 1 | 1 | 0 | 2026-09-24T13:19:27.655000+00:00 | 2026-09-24T13:25:21.118000+00:00 | 5m 53s |
| gameWindowUnfocusEvent | 19 | 0.13 | 1 | 7 | 0 | 2026-09-23T13:40:32.331000+00:00 | 2026-10-07T13:40:55.193000+00:00 | 336h 0m |
| argumentationToolEvent | 7 | 0.05 | 1 | 1 | 0 | 2026-09-24T13:19:30.830000+00:00 | 2026-09-24T13:22:57.684000+00:00 | 3m 26s |
| DaniEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-09-30T13:00:46.654000+00:00 | 2026-09-30T13:24:11.310000+00:00 | 23m 24s |
| argumentationEvent | 4 | 0.03 | 1 | 1 | 0 | 2026-09-24T13:16:54.926000+00:00 | 2026-09-24T13:25:21.132000+00:00 | 8m 26s |
| chatEvent | 2 | 0.01 | 1 | 1 | 0 | 2026-09-30T13:00:52.023000+00:00 | 2026-09-30T13:00:54.032000+00:00 | 2.0s |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-24T13:28:12.796000+00:00 | 2026-09-24T13:28:12.796000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.176s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 5.811s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 14.03s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 7.248s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — median interval between records changed substantially. 
  - Observed: 2.009s median 
  - Expected: 924.377s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 594.179s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 1388.776s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 0.917s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; SkipCinematic 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: 3; downArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Pick Up; Press E To Place Cameras; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Plant Seed; Press E to Scan; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — baseline categorical value(s) not seen this build. 
  - Observed: 90 ft 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.legendName` — categorical value(s) not seen in baseline. 
  - Observed: 210 ft; 270 ft; 360 ft; Water 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 4.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 4 records 
  - Expected: 14 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; U3 – Pollution Upstream" equals "Where is the pollution site probably located?; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; B; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `chatEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Open 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `chatEvent` `data.chatID` — categorical value(s) not seen in baseline. 
  - Observed: [] 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.5x vs baseline. 
  - Observed: 21 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 17; 18; 19; 41; 43; 44; 45; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 7.0x vs baseline. 
  - Observed: 35 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 3 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 17 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[576] _id=6ab3d3cb485cab4c954c2ab4 ts=2026-09-23T13:27:39.3590000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[636] _id=6ab3d4c7485cab4c954c64b3 ts=2026-09-23T13:31:51.0600000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[689] _id=6ab3d572485cab4c954c81e7 ts=2026-09-23T13:34:42.7130000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 21 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 21} 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[2] _id=6ab3ce0b485cab4c954b845a ts=2026-09-23T13:03:07.8650000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[796] _id=6ab51d95485cab4c954fc28f ts=2026-09-24T12:54:45.5610000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1479] _id=6ab525cc485cab4c9551126d ts=2026-09-24T13:29:48.1840000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 39 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 39} 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1] _id=6ab3ce0b485cab4c954b8458 ts=2026-09-23T13:03:07.8640000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[789] _id=6ab3d6d0485cab4c954caf35 ts=2026-09-23T13:40:32.3530000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[798] _id=6ab51d95485cab4c954fc28d ts=2026-09-24T12:54:45.5600000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[786] _id=6ab3d6d0485cab4c954caf33 ts=2026-09-23T13:40:32.3310000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1522] _id=6ab5260e485cab4c95511d80 ts=2026-09-24T13:30:53.9940000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1553] _id=6ab67071485cab4c955454a5 ts=2026-09-25T13:00:33.2460000Z`
- **INFO / Info** `TopographicMapEvent` `data.legendName` — field present in only part of the records. 
  - Observed: 5 of 132 records contain data.legendName 
  - Expected: declare as conditional/optional in config if intended 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1645] _id=6ab67172485cab4c955466d1 ts=2026-09-25T13:04:50.2090000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1651] _id=6ab67174485cab4c9554671f ts=2026-09-25T13:04:52.5080000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1650] _id=6ab67177485cab4c9554674d ts=2026-09-25T13:04:55.2260000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 5679 | 0.0 | 1.176 | 213.353 | 10.621 | 343091.946 | 0.28 | 155 | 11 |
| PuzzlePieceVisibleEvent | 4739 | 0.0 | 0.032 | 219.078 | 1.838 | 346166.357 | 0.27 | 2922 | 6 |
| PlayerPositionEvent | 2157 | 9.688 | 10.001 | 522.106 | 10.247 | 343042.863 | 0.11 | 0 | 8 |
| DialogueEvent | 1267 | 0.001 | 5.775 | 956.285 | 61.994 | 343239.218 | 0.06 | 316 | 10 |
| ObjectInterEvent | 385 | 0.004 | 9.088 | 3145.24 | 220.714 | 343167.817 | 0.02 | 2 | 9 |
| argumentationNodeEvent | 140 | 0.019 | 0.296 | 2.451 | 5.553 | 109.409 | 24.47 | 41 | 0 |
| TopographicMapEvent | 131 | 0.022 | 5.811 | 3970.909 | 962.587 | 257442.924 | 0.02 | 2 | 9 |
| questEvent | 83 | 0.001 | 191.085 | 14592.202 | 84792.646 | 343384.134 | 0.0 | 17 | 19 |
| Soil Key Puzzle | 59 | 0.123 | 1.034 | 8775.862 | 16.075 | 259381.829 | 0.01 | 0 | 2 |
| gameWindowFocusEvent | 38 | 2.082 | 594.179 | 31891.246 | 111792.117 | 345467.74 | 0.0 | 0 | 19 |
| soilMachine | 34 | 0.181 | 0.917 | 2587.024 | 788.298 | 85422.594 | 0.02 | 0 | 2 |
| DEBUGMenu | 29 | 8.902 | 1160.791 | 41758.314 | 189439.898 | 344581.787 | 0.0 | 0 | 18 |
| gameStartEvent | 20 | 166.639 | 1752.608 | 60535.87 | 262325.274 | 345815.388 | 0.0 | 0 | 14 |
| argumentationAnswerEvent | 19 | 0.611 | 14.03 | 18.603 | 55.062 | 55.462 | 3.23 | 0 | 0 |
| gameWindowUnfocusEvent | 18 | 1.795 | 1388.776 | 67201.27 | 285076.89 | 433484.383 | 0.0 | 0 | 11 |
| argumentationToolEvent | 6 | 1.146 | 7.248 | 34.476 | 99.301 | 103.637 | 1.74 | 0 | 0 |
| DaniEvent | 5 | 1.642 | 5.201 | 280.931 | 1014.241 | 1225.186 | 0.21 | 0 | 1 |
| argumentationEvent | 3 | 42.608 | 80.922 | 168.735 | 352.501 | 382.676 | 0.36 | 0 | 0 |
| chatEvent | 1 | 2.009 | 2.009 | 2.009 | 2.009 | 2.009 | 29.87 | 0 | 0 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[14250] _id=6ac64777de269131f9b8d27a ts=2026-10-07T13:21:58.9400000Z == 6aa413b141b41dbac0c7f1f2.jsonl[14251] _id=6ac64777de269131f9b8d27b ts=2026-10-07T13:21:58.9400000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[14516] _id=6ac6487bde269131f9b8fc09 ts=2026-10-07T13:26:19.1340000Z == 6aa413b141b41dbac0c7f1f2.jsonl[14517] _id=6ac6487bde269131f9b8fc0a ts=2026-10-07T13:26:19.1340000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 206 group(s), 276 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1690] _id=6ab671c8485cab4c95546a39 ts=2026-09-25T13:06:16.6860000Z == 6aa413b141b41dbac0c7f1f2.jsonl[1691] _id=6ab671c8485cab4c95546a3b ts=2026-09-25T13:06:16.6860000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1694] _id=6ab671c9485cab4c95546a45 ts=2026-09-25T13:06:16.6860000Z == 6aa413b141b41dbac0c7f1f2.jsonl[1718] _id=6ab671c9485cab4c95546a47 ts=2026-09-25T13:06:16.6860000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1735] _id=6ab671cc485cab4c95546a8d ts=2026-09-25T13:06:19.6650000Z == 6aa413b141b41dbac0c7f1f2.jsonl[1736] _id=6ab671cc485cab4c95546a91 ts=2026-09-25T13:06:19.6650000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 28 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa413b141b41dbac0c7f1f2.jsonl[533] _id=6ab3d348485cab4c954c0b0c ts=2026-09-23T13:25:28.3040000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[534] _id=6ab3d348485cab4c954c0b12 ts=2026-09-23T13:25:28.3110000Z`; `4ms: 6aa413b141b41dbac0c7f1f2.jsonl[819] _id=6ab51dd1485cab4c954fca17 ts=2026-09-24T12:55:45.3920000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[820] _id=6ab51dd1485cab4c954fca19 ts=2026-09-24T12:55:45.3960000Z`; `817ms: 6aa413b141b41dbac0c7f1f2.jsonl[1621] _id=6ab67157485cab4c95546403 ts=2026-09-25T13:04:23.6990000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1623] _id=6ab67158485cab4c95546409 ts=2026-09-25T13:04:24.5160000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 586 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `80ms: 6aa413b141b41dbac0c7f1f2.jsonl[1718] _id=6ab671c9485cab4c95546a47 ts=2026-09-25T13:06:16.6860000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1695] _id=6ab671c9485cab4c95546a49 ts=2026-09-25T13:06:16.7660000Z`; `12ms: 6aa413b141b41dbac0c7f1f2.jsonl[1712] _id=6ab671cb485cab4c95546a68 ts=2026-09-25T13:06:17.3080000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1725] _id=6ab671cb485cab4c95546a6d ts=2026-09-25T13:06:17.3200000Z`; `977ms: 6aa413b141b41dbac0c7f1f2.jsonl[1725] _id=6ab671cb485cab4c95546a6d ts=2026-09-25T13:06:17.3200000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1696] _id=6ab671cb485cab4c95546a71 ts=2026-09-25T13:06:18.2970000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa413b141b41dbac0c7f1f2.jsonl[2958] _id=6ab67630485cab4c9554dae6 ts=2026-09-25T13:25:04.6410000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[2960] _id=6ab67630485cab4c9554db08 ts=2026-09-25T13:25:04.6630000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `611ms: 6aa413b141b41dbac0c7f1f2.jsonl[1153] _id=6ab52361485cab4c955085ab ts=2026-09-24T13:19:29.1860000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1155] _id=6ab52361485cab4c955085df ts=2026-09-24T13:19:29.7970000Z`; `616ms: 6aa413b141b41dbac0c7f1f2.jsonl[1253] _id=6ab52434485cab4c9550ba43 ts=2026-09-24T13:23:00.0780000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1259] _id=6ab52434485cab4c9550ba71 ts=2026-09-24T13:23:00.6940000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 30 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `219ms: 6aa413b141b41dbac0c7f1f2.jsonl[1166] _id=6ab5236b485cab4c95508847 ts=2026-09-24T13:19:39.6610000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1163] _id=6ab5236b485cab4c95508853 ts=2026-09-24T13:19:39.8800000Z`; `211ms: 6aa413b141b41dbac0c7f1f2.jsonl[1167] _id=6ab5236b485cab4c9550884b ts=2026-09-24T13:19:39.7060000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1168] _id=6ab5236b485cab4c95508859 ts=2026-09-24T13:19:39.9170000Z`; `446ms: 6aa413b141b41dbac0c7f1f2.jsonl[1163] _id=6ab5236b485cab4c95508853 ts=2026-09-24T13:19:39.8800000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[1169] _id=6ab5236c485cab4c95508871 ts=2026-09-24T13:19:40.3260000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `270ms: 6aa413b141b41dbac0c7f1f2.jsonl[9928] _id=6ac3a1f3de269131f9a8656c ts=2026-10-05T13:11:15.7930000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[9929] _id=6ac3a1f4de269131f9a86578 ts=2026-10-05T13:11:16.0630000Z`; `199ms: 6aa413b141b41dbac0c7f1f2.jsonl[9929] _id=6ac3a1f4de269131f9a86578 ts=2026-10-05T13:11:16.0630000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[9924] _id=6ac3a1f4de269131f9a86584 ts=2026-10-05T13:11:16.2620000Z`; `184ms: 6aa413b141b41dbac0c7f1f2.jsonl[9924] _id=6ac3a1f4de269131f9a86584 ts=2026-10-05T13:11:16.2620000Z ~ 6aa413b141b41dbac0c7f1f2.jsonl[9949] _id=6ac3a1f4de269131f9a8658a ts=2026-10-05T13:11:16.4460000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 18 gap(s), longest 95h 43m 
  - Evidence: 95h 43m: 6aa413b141b41dbac0c7f1f2.jsonl[8630] _id=6abe5cee485cab4c95a49223 ts=2026-10-01T13:15:26.4680000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9498] _id=6ac39ef4de269131f9a83e58 ts=2026-10-05T12:58:28.2550000Z; 71h 38m: 6aa413b141b41dbac0c7f1f2.jsonl[2865] _id=6ab67576485cab4c9554bdb1 ts=2026-09-25T13:21:59.1620000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3170] _id=6aba6504485cab4c95679993 ts=2026-09-28T13:00:52.5660000Z; 24h 4m: 6aa413b141b41dbac0c7f1f2.jsonl[3170] _id=6aba6504485cab4c95679993 ts=2026-09-28T13:00:52.5660000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[4796] _id=6abbb7b0485cab4c957c20ee ts=2026-09-29T13:05:52.2060000Z
- **INFO / Info** `DaniEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 20m 25s 
  - Evidence: 20m 25s: 6aa413b141b41dbac0c7f1f2.jsonl[5767] _id=6abd0803485cab4c95867ba9 ts=2026-09-30T13:00:51.8550000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[6264] _id=6abd0ccd485cab4c95871226 ts=2026-09-30T13:21:17.0410000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa413b141b41dbac0c7f1f2.jsonl[9440] _id=6abe6232485cab4c95a646b3 ts=2026-10-01T13:37:54.7230000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9500] _id=6ac39efade269131f9a83e76 ts=2026-10-05T12:58:33.9410000Z; 71h 29m: 6aa413b141b41dbac0c7f1f2.jsonl[3049] _id=6ab677fa485cab4c95551956 ts=2026-09-25T13:32:42.3180000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3203] _id=6aba655b485cab4c95679b1b ts=2026-09-28T13:02:19.1690000Z; 24h 10m: 6aa413b141b41dbac0c7f1f2.jsonl[4976] _id=6abbbc09485cab4c957cd75e ts=2026-09-29T13:24:25.1000000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[6783] _id=6abd1000485cab4c95888ae3 ts=2026-09-30T13:34:56.0900000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 316 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f2.jsonl[2929] _id=6ab675d9485cab4c9554cc9e ts=2026-09-25T13:23:37.6290000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[2926] _id=6ab675d9485cab4c9554cca4 ts=2026-09-25T13:23:37.6300000Z; 1ms: 6aa413b141b41dbac0c7f1f2.jsonl[4552] _id=6aba6ba2485cab4c9567fc21 ts=2026-09-28T13:29:06.2570000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[4554] _id=6aba6ba2485cab4c9567fc23 ts=2026-09-28T13:29:06.2580000Z; 2ms: 6aa413b141b41dbac0c7f1f2.jsonl[1101] _id=6ab52254485cab4c95505348 ts=2026-09-24T13:15:00.8630000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[1102] _id=6ab52255485cab4c95505355 ts=2026-09-24T13:15:00.8650000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1f2.jsonl[9484] _id=6abe62c5485cab4c95a674c7 ts=2026-10-01T13:40:21.7140000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9504] _id=6ac39efade269131f9a83e6c ts=2026-10-05T12:58:33.6600000Z; 71h 26m: 6aa413b141b41dbac0c7f1f2.jsonl[3148] _id=6ab6787c485cab4c955529ca ts=2026-09-25T13:34:52.8920000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3164] _id=6aba650c485cab4c956799a5 ts=2026-09-28T13:00:59.6030000Z; 23h 40m: 6aa413b141b41dbac0c7f1f2.jsonl[14238] _id=6ac4fa90de269131f9b12310 ts=2026-10-06T13:41:36.5650000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14250] _id=6ac64777de269131f9b8d27a ts=2026-10-07T13:21:58.9400000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 155 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f2.jsonl[14250] _id=6ac64777de269131f9b8d27a ts=2026-10-07T13:21:58.9400000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14251] _id=6ac64777de269131f9b8d27b ts=2026-10-07T13:21:58.9400000Z; 0ms: 6aa413b141b41dbac0c7f1f2.jsonl[14516] _id=6ac6487bde269131f9b8fc09 ts=2026-10-07T13:26:19.1340000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14517] _id=6ac6487bde269131f9b8fc0a ts=2026-10-07T13:26:19.1340000Z; 1ms: 6aa413b141b41dbac0c7f1f2.jsonl[14251] _id=6ac64777de269131f9b8d27b ts=2026-10-07T13:21:58.9400000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14252] _id=6ac64777de269131f9b8d27c ts=2026-10-07T13:21:58.9410000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa413b141b41dbac0c7f1f2.jsonl[9466] _id=6abe6298485cab4c95a668cf ts=2026-10-01T13:39:36.3980000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9511] _id=6ac39f18de269131f9a83ef2 ts=2026-10-05T12:59:04.2150000Z; 72h 3m: 6aa413b141b41dbac0c7f1f2.jsonl[2731] _id=6ab673de485cab4c95548ffb ts=2026-09-25T13:15:10.1590000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3583] _id=6aba6917485cab4c9567cd08 ts=2026-09-28T13:18:14.9650000Z; 71h 38m: 6aa413b141b41dbac0c7f1f2.jsonl[4398] _id=6aba6aa2485cab4c9567f101 ts=2026-09-28T13:24:50.4890000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[7101] _id=6abe5a14485cab4c95a420ad ts=2026-10-01T13:03:15.8580000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.004s..0.007s shown 
  - Evidence: 4ms: 6aa413b141b41dbac0c7f1f2.jsonl[819] _id=6ab51dd1485cab4c954fca17 ts=2026-09-24T12:55:45.3920000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[820] _id=6ab51dd1485cab4c954fca19 ts=2026-09-24T12:55:45.3960000Z; 7ms: 6aa413b141b41dbac0c7f1f2.jsonl[533] _id=6ab3d348485cab4c954c0b0c ts=2026-09-23T13:25:28.3040000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[534] _id=6ab3d348485cab4c954c0b12 ts=2026-09-23T13:25:28.3110000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa413b141b41dbac0c7f1f2.jsonl[9478] _id=6abe62f1485cab4c95a67ec9 ts=2026-10-01T13:41:05.4010000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9503] _id=6ac39efade269131f9a83e6a ts=2026-10-05T12:58:28.2640000Z; 71h 25m: 6aa413b141b41dbac0c7f1f2.jsonl[3151] _id=6ab67898485cab4c95552c72 ts=2026-09-25T13:35:20.3340000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3172] _id=6aba650c485cab4c956799a1 ts=2026-09-28T13:00:52.5740000Z; 23h 29m: 6aa413b141b41dbac0c7f1f2.jsonl[1531] _id=6ab5260f485cab4c95511da4 ts=2026-09-24T13:30:55.3760000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[1555] _id=6ab6707b485cab4c955454b3 ts=2026-09-25T13:00:40.4980000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 96h 9m 
  - Evidence: 96h 9m: 6aa413b141b41dbac0c7f1f2.jsonl[8615] _id=6abe5cb1485cab4c95a48973 ts=2026-10-01T13:14:23.8660000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[10494] _id=6ac3a4e7de269131f9a8d783 ts=2026-10-05T13:23:50.2230000Z; 72h 9m: 6aa413b141b41dbac0c7f1f2.jsonl[2595] _id=6ab67305485cab4c9554829d ts=2026-09-25T13:11:31.5770000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3644] _id=6aba69a2485cab4c9567d80b ts=2026-09-28T13:20:33.2880000Z; 71h 37m: 6aa413b141b41dbac0c7f1f2.jsonl[4517] _id=6aba6b4b485cab4c9567f89d ts=2026-09-28T13:27:37.4930000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[7151] _id=6abe5a72485cab4c95a42a0d ts=2026-10-01T13:04:50.0550000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2922 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f2.jsonl[10494] _id=6ac3a4e7de269131f9a8d783 ts=2026-10-05T13:23:50.2230000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[10492] _id=6ac3a4e7de269131f9a8d78f ts=2026-10-05T13:23:50.2230000Z; 0ms: 6aa413b141b41dbac0c7f1f2.jsonl[10502] _id=6ac3a4f4de269131f9a8db1f ts=2026-10-05T13:24:03.7400000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[10523] _id=6ac3a4f4de269131f9a8db2c ts=2026-10-05T13:24:03.7400000Z; 0ms: 6aa413b141b41dbac0c7f1f2.jsonl[10503] _id=6ac3a4f4de269131f9a8db33 ts=2026-10-05T13:24:03.7400000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[10519] _id=6ac3a4f4de269131f9a8db3a ts=2026-10-05T13:24:03.7400000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 72h 3m 
  - Evidence: 72h 3m: 6aa413b141b41dbac0c7f1f2.jsonl[2729] _id=6ab673e0485cab4c95549021 ts=2026-09-25T13:15:13.1270000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3584] _id=6aba6916485cab4c9567cd05 ts=2026-09-28T13:18:14.9560000Z; 71h 44m: 6aa413b141b41dbac0c7f1f2.jsonl[3605] _id=6aba694a485cab4c9567d0dd ts=2026-09-28T13:19:06.7900000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[7099] _id=6abe5a13485cab4c95a420ab ts=2026-10-01T13:03:15.8540000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 71h 30m 
  - Evidence: 71h 30m: 6aa413b141b41dbac0c7f1f2.jsonl[3050] _id=6ab677ff485cab4c955519c6 ts=2026-09-25T13:32:47.6730000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3229] _id=6aba65a2485cab4c95679e7d ts=2026-09-28T13:03:30.5970000Z; 23h 45m: 6aa413b141b41dbac0c7f1f2.jsonl[4697] _id=6aba6dc1485cab4c95681141 ts=2026-09-28T13:38:09.1480000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[4949] _id=6abbbbd3485cab4c957ccb02 ts=2026-09-29T13:23:30.9560000Z; 23h 30m: 6aa413b141b41dbac0c7f1f2.jsonl[5190] _id=6abbbd2b485cab4c957d1549 ts=2026-09-29T13:29:15.3490000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[5637] _id=6abd07dd485cab4c958679c1 ts=2026-09-30T13:00:13.5140000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.022s..0.028s shown 
  - Evidence: 22ms: 6aa413b141b41dbac0c7f1f2.jsonl[2958] _id=6ab67630485cab4c9554dae6 ts=2026-09-25T13:25:04.6410000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[2960] _id=6ab67630485cab4c9554db08 ts=2026-09-25T13:25:04.6630000Z; 28ms: 6aa413b141b41dbac0c7f1f2.jsonl[2962] _id=6ab67630485cab4c9554dadf ts=2026-09-25T13:25:04.6130000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[2958] _id=6ab67630485cab4c9554dae6 ts=2026-09-25T13:25:04.6410000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 41 interval(s) ≤ 0.019s..0.020s shown 
  - Evidence: 19ms: 6aa413b141b41dbac0c7f1f2.jsonl[1262] _id=6ab52436485cab4c9550baf4 ts=2026-09-24T13:23:02.2550000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[1267] _id=6ab52436485cab4c9550bafb ts=2026-09-24T13:23:02.2740000Z; 20ms: 6aa413b141b41dbac0c7f1f2.jsonl[1212] _id=6ab523dc485cab4c9550a451 ts=2026-09-24T13:21:32.9450000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[1213] _id=6ab523dd485cab4c9550a458 ts=2026-09-24T13:21:32.9650000Z; 20ms: 6aa413b141b41dbac0c7f1f2.jsonl[1215] _id=6ab523df485cab4c9550a4e6 ts=2026-09-24T13:21:35.1040000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[1211] _id=6ab523df485cab4c9550a4ef ts=2026-09-24T13:21:35.1240000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 96h 3m 
  - Evidence: 96h 3m: 6aa413b141b41dbac0c7f1f2.jsonl[6835] _id=6abe5817485cab4c95a3fe83 ts=2026-10-01T12:54:47.0690000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9502] _id=6ac39eeede269131f9a83e32 ts=2026-10-05T12:58:22.4570000Z; 71h 38m: 6aa413b141b41dbac0c7f1f2.jsonl[2864] _id=6ab67571485cab4c9554bcc4 ts=2026-09-25T13:21:53.4290000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3169] _id=6aba64fc485cab4c95679975 ts=2026-09-28T13:00:44.4860000Z; 24h 27m: 6aa413b141b41dbac0c7f1f2.jsonl[11651] _id=6ac4ef70de269131f9affb1f ts=2026-10-06T12:54:08.1920000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14241] _id=6ac64769de269131f9b8d06f ts=2026-10-07T13:21:45.2670000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 57m 
  - Evidence: 95h 57m: 6aa413b141b41dbac0c7f1f2.jsonl[6970] _id=6abe5972485cab4c95a415a8 ts=2026-10-01T13:00:34.7160000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9501] _id=6ac39eeede269131f9a83e30 ts=2026-10-05T12:58:22.4560000Z; 71h 25m: 6aa413b141b41dbac0c7f1f2.jsonl[3154] _id=6ab6789a485cab4c95552cb2 ts=2026-09-25T13:35:22.8670000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3168] _id=6aba64fc485cab4c95679971 ts=2026-09-28T13:00:44.4850000Z; 23h 55m: 6aa413b141b41dbac0c7f1f2.jsonl[9501] _id=6ac39eeede269131f9a83e30 ts=2026-10-05T12:58:22.4560000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[11650] _id=6ac4ef70de269131f9affb1c ts=2026-10-06T12:54:08.1910000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 120h 24m 
  - Evidence: 120h 24m: 6aa413b141b41dbac0c7f1f2.jsonl[6923] _id=6abe596e485cab4c95a41543 ts=2026-10-01T13:00:29.9640000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[13355] _id=6ac4f6bade269131f9b07998 ts=2026-10-06T13:25:14.3470000Z; 71h 54m: 6aa413b141b41dbac0c7f1f2.jsonl[3155] _id=6ab6789e485cab4c95552cf8 ts=2026-09-25T13:35:26.9380000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[4569] _id=6aba6be6485cab4c9567ff1b ts=2026-09-28T13:30:14.2700000Z; 24h 15m: 6aa413b141b41dbac0c7f1f2.jsonl[13355] _id=6ac4f6bade269131f9b07998 ts=2026-10-06T13:25:14.3470000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14843] _id=6ac64be7de269131f9b9cc05 ts=2026-10-07T13:40:55.1930000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 19 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa413b141b41dbac0c7f1f2.jsonl[9373] _id=6abe61a1485cab4c95a6190f ts=2026-10-01T13:35:29.5880000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[9506] _id=6ac39efade269131f9a83e72 ts=2026-10-05T12:58:33.7220000Z; 71h 36m: 6aa413b141b41dbac0c7f1f2.jsonl[2949] _id=6ab67617485cab4c9554d5d0 ts=2026-09-25T13:24:40.0220000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[3157] _id=6aba650c485cab4c956799ad ts=2026-09-28T13:00:59.6450000Z; 23h 41m: 6aa413b141b41dbac0c7f1f2.jsonl[14182] _id=6ac4fa60de269131f9b118a4 ts=2026-10-06T13:40:48.0280000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14253] _id=6ac64777de269131f9b8d27d ts=2026-10-07T13:21:59.1660000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 17 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f2.jsonl[1103] _id=6ab52255485cab4c95505362 ts=2026-09-24T13:15:00.8680000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[1098] _id=6ab52255485cab4c95505369 ts=2026-09-24T13:15:00.8690000Z; 1ms: 6aa413b141b41dbac0c7f1f2.jsonl[14253] _id=6ac64777de269131f9b8d27d ts=2026-10-07T13:21:59.1660000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14254] _id=6ac64777de269131f9b8d27e ts=2026-10-07T13:21:59.1670000Z; 2ms: 6aa413b141b41dbac0c7f1f2.jsonl[14254] _id=6ac64777de269131f9b8d27e ts=2026-10-07T13:21:59.1670000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[14255] _id=6ac64777de269131f9b8d27f ts=2026-10-07T13:21:59.1690000Z
- **INFO / Info** `soilMachine` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 43m 
  - Evidence: 23h 43m: 6aa413b141b41dbac0c7f1f2.jsonl[10440] _id=6ac3a49ede269131f9a8c3a1 ts=2026-10-05T13:22:38.9110000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[12048] _id=6ac4f24dde269131f9b015c2 ts=2026-10-06T13:06:21.5050000Z; 28m 3s: 6aa413b141b41dbac0c7f1f2.jsonl[12082] _id=6ac4f291de269131f9b01aed ts=2026-10-06T13:07:29.1490000Z -> 6aa413b141b41dbac0c7f1f2.jsonl[13666] _id=6ac4f924de269131f9b0d995 ts=2026-10-06T13:35:32.9470000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 9 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1088] _id=6ab5223a485cab4c95504be3 ts=2026-09-24T13:14:34.3410000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1388] _id=6ab524d1485cab4c9550deed ts=2026-09-24T13:25:37.4770000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[3263] _id=6aba65ff485cab4c9567a12d ts=2026-09-28T13:05:03.8740000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 77 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1872] _id=6ab6724f485cab4c9554710f ts=2026-09-25T13:08:30.3270000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1886] _id=6ab6724f485cab4c95547111 ts=2026-09-25T13:08:30.3650000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1883] _id=6ab6724f485cab4c95547115 ts=2026-09-25T13:08:30.3790000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 256 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1722] _id=6ab671ca485cab4c95546a5d ts=2026-09-25T13:06:17.2030000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1724] _id=6ab671cc485cab4c95546a89 ts=2026-09-25T13:06:19.6650000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1731] _id=6ab671cd485cab4c95546a97 ts=2026-09-25T13:06:19.6650000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 6 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[9071] _id=6abe5fb2485cab4c95a58b71 ts=2026-10-01T13:27:14.0700000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[9514] _id=6ac39f05de269131f9a83ea2 ts=2026-10-05T12:58:45.9040000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[11476] _id=6ac3a72ede269131f9a94cc1 ts=2026-10-05T13:33:34.6480000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 875 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1894] _id=6ab67253485cab4c95547153 ts=2026-09-25T13:08:35.1270000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1860] _id=6ab67253485cab4c95547155 ts=2026-09-25T13:08:35.1700000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1967] _id=6ab67262485cab4c955472eb ts=2026-09-25T13:08:49.5860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 932 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1691] _id=6ab671c8485cab4c95546a3b ts=2026-09-25T13:06:16.6860000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1692] _id=6ab671c8485cab4c95546a3f ts=2026-09-25T13:06:16.6860000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1717] _id=6ab671c9485cab4c95546a41 ts=2026-09-25T13:06:16.6860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 55 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[2958] _id=6ab67630485cab4c9554dae6 ts=2026-09-25T13:25:04.6410000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[2960] _id=6ab67630485cab4c9554db08 ts=2026-09-25T13:25:04.6630000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[3075] _id=6ab67764485cab4c95550c06 ts=2026-09-25T13:30:12.4450000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1176] _id=6ab5236f485cab4c95508985 ts=2026-09-24T13:19:43.9130000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1207] _id=6ab523d8485cab4c9550a365 ts=2026-09-24T13:21:28.6960000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1252] _id=6ab52430485cab4c9550b8db ts=2026-09-24T13:22:56.4030000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 12 unmatched 'DialogueStartEvent' (totals: 229 start, 226 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 200 unmatched 'BecameCameraCentered' (totals: 1038 open, 915 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 113 unmatched 'BecameVisible' (totals: 1322 open, 1465 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 58 open, 56 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 28 unmatched 'questActiveEvent' (totals: 53 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 362 of 14844 adjacent _id pairs reverse in client time; worst 123.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f2.jsonl[1842] _id=6ab6723f485cab4c9554700f ts=2026-09-25T13:08:15.7760000Z`; `6aa413b141b41dbac0c7f1f2.jsonl[1831] _id=6ab67240485cab4c95547015 ts=2026-09-25T13:06:12.0160000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -124.51s, max +0.25s over 14845 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f2\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
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

### `InputEvent` — 5680 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 4 Dev - Dungeon (1959); Unit 3 Dev (1436); Unit 2 Prod (Refactor) (878); Unit 4 Dev (846); Unit 1 Dev (561)
- **Intervals:** median 1.18s (p5 0.11s / p95 10.62s, n=5679)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 5680/5680 records)
    "pressed"  x5680
data.actionType  (string, 5680/5680 records)
    "Move"  x3713
    "Interact"  x975
    "Jump"  x628
    "Sprint"  x238
    "Hoverboard"  x73
    "Map"  x49
    "SkipCinematic"  x3
    "Pause"  x1
data.key  (string, 5680/5680 records, 5 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 5680/5680 records)
    "Player"  x5680
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PuzzlePieceVisibleEvent` — 4740 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 4 Dev (3308); Unit 2 Prod (Refactor) (1432)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.84s, n=4739)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4740/4740 records)
    "BecameInvisible"  x1465
    "BecameVisible"  x1322
    "BecameCameraCentered"  x1038
    "BecameCameraUncentered"  x915
data.pieceId  (string, 4740/4740 records)
    27 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 4740/4740 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `PlayerPositionEvent` — 2170 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 4 Dev - Dungeon (613); Unit 2 Prod (Refactor) (534); Unit 1 Dev (404); Unit 4 Dev (323); Unit 3 Dev (296)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.25s, n=2157)
- **Fields under `data`:**

```text
data.position  (object, 2170/2170 records)
data.position.x  (number, 2170/2170 records)
    numeric range -106.956 .. 1742.22 (1133 unique)
data.position.y  (number, 2170/2170 records)
    numeric range -115.665 .. 159.727 (740 unique)
data.position.z  (number, 2170/2170 records)
    numeric range -700.107 .. 2082.96 (1140 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1268 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (422); Unit 4 Dev - Dungeon (316); Unit 1 Dev (304); Unit 4 Dev (202); Unit 3 Dev (24)
- **eventKey:** present on 813 of 1268 records
- **Intervals:** median 5.78s (p5 0.01s / p95 61.99s, n=1267)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x813; [conversationId, dialogueEventType] x455
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1268/1268 records)
    numeric range 8 .. 107 (29 unique)
data.dialogueEventType  (string, 1268/1268 records)
    "DialogueNodeEvent"  x813
    "DialogueStartEvent"  x229
    "DialogueFinishEvent"  x226
data.nodeId  (number, 813/1268 records)
    numeric range 0 .. 290 (161 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 386 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (303); Unit 2 Prod (Refactor) (38); Unit 4 Dev (26); Unit 1 Dev (19)
- **Intervals:** median 9.09s (p5 0.43s / p95 220.71s, n=385)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 386/386 records)
    21 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 386/386 records)
    57 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 141 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (141)
- **Intervals:** median 0.30s (p5 0.02s / p95 5.55s, n=140)
- **Fields under `data`:**

```text
data.actionType  (string, 141/141 records)
    "argumentationNodeHoverEnd"  x57
    "argumentationNodeHoverStart"  x57
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x12
data.argumentationTitle  (string, 141/141 records)
    "Unit 1 - Freshwater"  x141
data.nodeName  (string, 141/141 records)
    "II"  x72
    "A"  x33
    "1"  x19
    "I"  x17
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 132 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (64); Unit 2 Prod (Refactor) (41); Unit 4 Dev (23); Unit 4 Dev - Dungeon (4)
- **Intervals:** median 5.81s (p5 1.61s / p95 962.59s, n=131)
- **`data` key-set variants:** [actionType, featureUsed] x114; [actionType, featureUsed, location] x13; [actionType, featureUsed, legendName] x5
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 132/132 records)
    "MapOpenEvent"  x58
    "MapCloseEvent"  x56
    "WaypointMoveEvent"  x10
    "Selected"  x5
    "WaypointSetEvent"  x3
data.featureUsed  (string, 132/132 records)
    "Map"  x114
    "Waypoint"  x13
    "Legend"  x5
data.legendName  (string, 5/132 records)
    "0 ft"  x1
    "210 ft"  x1
    "270 ft"  x1
    "360 ft"  x1
    "Water"  x1
data.location  (object, 13/132 records)
data.location.x  (number, 13/132 records)
    numeric range -178.09 .. 408.91 (13 unique)
data.location.y  (number, 13/132 records)
    numeric range -343.5 .. 267.5 (13 unique)
data.location.z  (number, 13/132 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 84 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 4 Dev - Dungeon (30); Unit 1 Dev (17); Unit 4 Dev (16); Unit 2 Prod (Refactor) (13); Unit 3 Dev (8)
- **eventKey:** present on 84 of 84 records
- **Intervals:** median 191.09s (p5 0.01s / p95 84792.65s, n=83)
- **`data` key-set variants:** [questEventType, questID, questName] x53; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 84/84 records)
    "questActiveEvent"  x53
    "questFinishEvent"  x31
data.questID  (string, 84/84 records)
    20 unique values (see csv/event_unique_values.csv)
data.questName  (string, 84/84 records)
    20 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/84 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 60 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 4 Dev (38); Unit 2 Prod (Refactor) (22)
- **Intervals:** median 1.03s (p5 0.19s / p95 16.07s, n=59)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x54; [Soil Key Puzzle Status, Unit] x6
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 6/60 records)
    "Finished"  x3
    "Started"  x3
data.Unit  (string, 6/60 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 4 Dev"  x2
data.actionType  (string, 54/60 records)
    "RightDrag"  x29
    "LeftDrag"  x25
data.currentSoilType  (string, 54/60 records)
    "CLAYSAND"  x12
    "CLAY"  x11
    "CLAYROCK"  x10
    "SAND"  x10
    "SANDGRAVEL"  x5
    "BEDROCK"  x4
    "GRAVEL"  x2
data.isCorrectSelection  (string, 54/60 records)
    "false"  x42
    "true"  x12
data.waterLevelStatus  (string, 54/60 records)
    "TooHigh"  x28
    "TooLow"  x22
    "Proper"  x4
data.waterRetentionChange  (string, 54/60 records)
    "Increase"  x29
    "Decrease"  x13
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `gameWindowFocusEvent` — 39 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (22); Unit 2 Prod (Refactor) (7); Unit 3 Dev (3); Unit 4 Dev (3); Unit 4 Dev - Dungeon (2); Transition (1); Unit 1 Dev (1)
- **Intervals:** median 594.18s (p5 5.71s / p95 111792.12s, n=38)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 39/39 records)
    true  x39
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `soilMachine` — 35 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (35)
- **Intervals:** median 0.92s (p5 0.19s / p95 788.30s, n=34)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 35/35 records)
    "ChangeCanister"  x35
data.canisterType  (string, 35/35 records)
    "Sand"  x28
    "Gravel"  x4
    "Bedrock"  x2
    "Clay"  x1
data.floor  (string, 35/35 records)
    "4"  x27
    "5"  x8
data.machine  (string, 35/35 records)
    "1"  x27
    "2"  x8
data.row  (string, 35/35 records)
    "TopRow"  x35
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `DEBUGMenu` — 30 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 3 Dev (8); Unit 4 Dev - Dungeon (7); Unit 2 Prod (Refactor) (6); Unit 4 Dev (6); Unit 1 Dev (2); MainMenu (1)
- **Intervals:** median 1160.79s (p5 170.61s / p95 189439.90s, n=29)
- **Fields under `data`:**

```text
data.actionType  (string, 30/30 records)
    "DebugMenuStateChanged"  x30
data.isOpened  (bool, 30/30 records)
    false  x30
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 21 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (21)
- **Intervals:** median 1752.61s (p5 175.02s / p95 262325.27s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 21/21 records)
    true  x21
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 20 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (20)
- **Intervals:** median 14.03s (p5 0.62s / p95 55.06s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "submitAnswerEvent"  x20
data.answerSubmitted  (string, 20/20 records, 4 empty-string)
    "A,1,II"  x14
    ""  x4
    "A,1,I"  x1
    "II"  x1
data.argumentationTitle  (string, 20/20 records)
    "Unit 1 - Freshwater"  x20
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowUnfocusEvent` — 19 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 3 Dev (3); Unit 4 Dev (3); Unit 4 Dev - Dungeon (2); MainMenu (1); Transition (1); Unit 1 Dev (1)
- **Intervals:** median 1388.78s (p5 5.13s / p95 285076.89s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    false  x19
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 7.25s (p5 1.18s / p95 99.30s, n=6)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationToolOpen"  x4
    "argumentationToolClose"  x3
data.argumentationTitle  (string, 7/7 records)
    "Unit 1 - Freshwater"  x7
data.toolName  (string, 7/7 records)
    "BackingInfoPanel - "  x7
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (6)
- **Intervals:** median 5.20s (p5 1.75s / p95 1014.24s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 80.92s (p5 46.44s / p95 352.50s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationSessionClose"  x2
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 4/4 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `chatEvent` — 2 records

*Purpose:* Chat window usage (open, close, scrolling through chat history).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 2.01s (p5 2.01s / p95 2.01s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.chatID  (string, 2/2 records)
    "NA"  x1
    "[]"  x1
```

Raw examples: `event_examples.json` -> `chatEvent`.

### `EndOfUnit` — 1 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.Unit  (string, 1/1 records)
    "1"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : median interval between records changed substantially
- `gameWindowFocusEvent` : median interval between records changed substantially
- `gameWindowUnfocusEvent` : median interval between records changed substantially
- `soilMachine` : median interval between records changed substantially
- `DialogueEvent` eventKey: eventKey does not match its documented format

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (22 records)
- `TopographicMapEvent` data.actionType: "Selected" (5x); "WaypointMoveEvent" (10x); "WaypointSetEvent" (3x)
- `TopographicMapEvent` data.featureUsed: "Legend" (5x); "Waypoint" (13x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (12x)
- `soilMachine` data.canisterType: "Bedrock" (2x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*