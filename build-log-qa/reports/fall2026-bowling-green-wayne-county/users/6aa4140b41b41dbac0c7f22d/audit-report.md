# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6aa4140b41b41dbac0c7f22d
- **Game version string(s) in log:** 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa4140b41b41dbac0c7f22d.jsonl
- **Records:** 13698 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa4140b41b41dbac0c7f22d
- **Time span:** 2026-09-23T13:54:19.034000+00:00 .. 2026-10-07T16:17:04.687000+00:00 (338h 22m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **20 event types**, 13698 records, 8 scenes.
- Findings: **0 FAIL**, **37 WARNING**, 89 INFO, 2 NOT_TESTED, 82 PASS.
- Top items needing attention:
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: median interval between records changed substantially
  - WARNING/Medium `ObjectInterEvent`: median interval between records changed substantially
  - WARNING/Medium `PuzzlePieceVisibleEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3580 | 26.14 | 1 | 3 | 0 | 2026-09-25T14:09:25.963000+00:00 | 2026-10-05T15:44:09.239000+00:00 | 241h 34m |
| InputEvent | 3576 | 26.11 | 1 | 7 | 0 | 2026-09-23T14:00:50.859000+00:00 | 2026-10-07T16:15:33.356000+00:00 | 338h 14m |
| PlayerPositionEvent | 2439 | 17.81 | 1 | 7 | 0 | 2026-09-23T13:54:44.152000+00:00 | 2026-10-07T16:17:04.422000+00:00 | 338h 22m |
| DialogueEvent | 2102 | 15.35 | 1 | 7 | 1340 | 2026-09-23T13:55:05.857000+00:00 | 2026-10-07T16:17:01.741000+00:00 | 338h 21m |
| argumentationNodeEvent | 1320 | 9.64 | 1 | 3 | 0 | 2026-09-24T14:14:47.483000+00:00 | 2026-10-07T16:02:53.836000+00:00 | 313h 48m |
| ObjectInterEvent | 240 | 1.75 | 1 | 7 | 0 | 2026-09-23T14:04:17.388000+00:00 | 2026-10-07T16:11:50.736000+00:00 | 338h 7m |
| Soil Key Puzzle | 129 | 0.94 | 1 | 3 | 0 | 2026-09-25T14:20:31.792000+00:00 | 2026-10-07T16:13:03.562000+00:00 | 289h 52m |
| questEvent | 79 | 0.58 | 1 | 7 | 79 | 2026-09-23T13:55:05.839000+00:00 | 2026-10-07T16:15:21.754000+00:00 | 338h 20m |
| argumentationAnswerEvent | 62 | 0.45 | 1 | 3 | 0 | 2026-09-24T14:14:52.404000+00:00 | 2026-10-07T16:03:08.512000+00:00 | 313h 48m |
| TopographicMapEvent | 34 | 0.25 | 1 | 4 | 0 | 2026-09-25T14:10:03.146000+00:00 | 2026-10-05T13:56:29.807000+00:00 | 239h 46m |
| DEBUGMenu | 28 | 0.2 | 1 | 8 | 0 | 2026-09-23T13:54:44.144000+00:00 | 2026-10-07T16:04:30.972000+00:00 | 338h 9m |
| gameWindowFocusEvent | 25 | 0.18 | 1 | 2 | 0 | 2026-09-23T13:54:19.034000+00:00 | 2026-10-07T15:37:49.165000+00:00 | 337h 43m |
| gameStartEvent | 19 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:54:19.035000+00:00 | 2026-10-07T15:37:49.165000+00:00 | 337h 43m |
| gameWindowUnfocusEvent | 18 | 0.13 | 1 | 6 | 0 | 2026-09-24T14:15:46.475000+00:00 | 2026-10-07T16:17:04.687000+00:00 | 314h 1m |
| argumentationEvent | 16 | 0.12 | 1 | 3 | 0 | 2026-09-24T14:14:19.804000+00:00 | 2026-10-07T16:03:08.578000+00:00 | 313h 48m |
| TerasGardenBox | 10 | 0.07 | 1 | 1 | 0 | 2026-10-07T16:09:12.643000+00:00 | 2026-10-07T16:11:00.169000+00:00 | 1m 47s |
| soilMachine | 8 | 0.06 | 1 | 1 | 0 | 2026-10-05T14:14:58.232000+00:00 | 2026-10-05T14:26:08.686000+00:00 | 11m 10s |
| DaniEvent | 6 | 0.04 | 1 | 1 | 0 | 2026-10-01T14:15:35.946000+00:00 | 2026-10-01T14:17:22.654000+00:00 | 1m 46s |
| argumentationToolEvent | 5 | 0.04 | 1 | 1 | 0 | 2026-09-30T14:24:53.277000+00:00 | 2026-09-30T14:25:17.288000+00:00 | 24.0s |
| EndOfUnit | 2 | 0.01 | 1 | 2 | 0 | 2026-09-25T14:02:49.121000+00:00 | 2026-10-01T14:26:53.071000+00:00 | 144h 24m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 1616.434s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 519843.95s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 16.779s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — median interval between records changed substantially. 
  - Observed: 0.039s median 
  - Expected: 0.018s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 26.492s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 19.482s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.357s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 43163.524s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 2017.26s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 6407.214s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 6 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Pause; ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; p; rightArrow; rightShift; tab; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Press E; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to examine 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: Press E to collect broccoli; Press E to collect peas; Press E to collect potatoes; Press E to go down 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 3.4x vs baseline. 
  - Observed: 129 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 12.4x vs baseline. 
  - Observed: 62 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: ; A,2,II; A,3,I; A,3,II; A,4,I; A,B,1,I; A,B,2,II; A,B,4,II; A,C,2,II; A,C,4,II; A,C,B,2,II; B,1,I; B,1,II; B,2,II; B,3,II; B,4,I; B,C,1,II; B,C,2,II; B,C,3,II; B,C,4,II; B,C,D,2,II; C,2,II; C,4,II; C,A,2,II; C,B,2,II; C,D,2,II; D,4,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 9.4x vs baseline. 
  - Observed: 1320 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `gameStartEvent` — record volume changed 3.2x vs baseline. 
  - Observed: 19 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 43; 44; 45; 51; 52; 53; 54; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Claim of Command; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 44 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[208] _id=6ab3dd38485cab4c954cfa53 ts=2026-09-23T14:07:52.6770000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[274] _id=6ab3de95485cab4c954d0445 ts=2026-09-23T14:13:41.3620000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[342] _id=6ab3df7d485cab4c954d0e22 ts=2026-09-23T14:17:33.3870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[4798] _id=6aba7971485cab4c9568e12b ts=2026-09-28T14:28:00.4260000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[4925] _id=6abbc35f485cab4c957e0e23 ts=2026-09-29T13:55:42.6960000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 19 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 19} 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[20] _id=6ab3da0b485cab4c954ce2ad ts=2026-09-23T13:54:19.0350000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[516] _id=6ab5284b485cab4c9551466d ts=2026-09-24T13:40:27.4800000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1052] _id=6ab67ceb485cab4c95559f9c ts=2026-09-25T13:53:47.6050000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[21] _id=6ab3da0a485cab4c954ce2ab ts=2026-09-23T13:54:19.0340000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[515] _id=6ab5284b485cab4c9551466b ts=2026-09-24T13:40:27.4790000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1050] _id=6ab67ceb485cab4c95559f98 ts=2026-09-25T13:53:47.6040000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1043] _id=6ab53092485cab4c9551ee6d ts=2026-09-24T14:15:46.4750000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[3510] _id=6ab68548485cab4c95564971 ts=2026-09-25T14:29:28.2160000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[4777] _id=6aba7802485cab4c9568cc23 ts=2026-09-28T14:21:54.9530000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3579 | 0.0 | 0.039 | 242.996 | 1.646 | 346008.496 | 0.25 | 1972 | 7 |
| InputEvent | 3575 | 0.0 | 0.797 | 340.61 | 15.685 | 343294.93 | 0.18 | 160 | 16 |
| PlayerPositionEvent | 2427 | 4.03 | 10.0 | 465.769 | 10.03 | 343066.76 | 0.13 | 0 | 11 |
| DialogueEvent | 2101 | 0.0 | 4.995 | 579.779 | 51.233 | 343247.184 | 0.1 | 601 | 12 |
| argumentationNodeEvent | 1319 | 0.003 | 0.345 | 856.472 | 7.886 | 437670.376 | 0.07 | 264 | 5 |
| ObjectInterEvent | 239 | 0.0 | 16.779 | 5093.11 | 1151.725 | 343670.086 | 0.01 | 10 | 16 |
| Soil Key Puzzle | 128 | 0.066 | 0.455 | 8152.748 | 9.674 | 429751.035 | 0.01 | 0 | 4 |
| questEvent | 78 | 0.001 | 273.664 | 15615.589 | 84994.718 | 343485.709 | 0.0 | 13 | 20 |
| argumentationAnswerEvent | 61 | 0.434 | 19.482 | 18519.608 | 85438.296 | 437742.189 | 0.0 | 0 | 5 |
| TopographicMapEvent | 33 | 0.536 | 26.492 | 26157.172 | 155393.12 | 344136.759 | 0.0 | 0 | 7 |
| DEBUGMenu | 27 | 7.046 | 1616.434 | 45088.401 | 207036.311 | 343238.193 | 0.0 | 0 | 20 |
| gameWindowFocusEvent | 24 | 2.642 | 2017.26 | 50658.755 | 232809.786 | 343247.745 | 0.0 | 0 | 16 |
| gameStartEvent | 18 | 146.747 | 43163.524 | 67545.007 | 270997.955 | 343247.744 | 0.0 | 0 | 15 |
| gameWindowUnfocusEvent | 17 | 0.0 | 6407.214 | 66498.718 | 276432.493 | 347175.517 | 0.0 | 1 | 12 |
| argumentationEvent | 15 | 0.037 | 101.116 | 75315.252 | 434750.823 | 437660.525 | 0.0 | 2 | 6 |
| TerasGardenBox | 9 | 1.525 | 5.019 | 11.947 | 40.248 | 52.182 | 5.02 | 0 | 0 |
| soilMachine | 7 | 4.027 | 40.493 | 95.779 | 259.988 | 292.168 | 0.63 | 0 | 0 |
| DaniEvent | 5 | 0.667 | 0.872 | 21.342 | 60.238 | 65.597 | 2.81 | 0 | 0 |
| argumentationToolEvent | 4 | 1.813 | 3.357 | 6.003 | 13.8 | 15.483 | 10.0 | 0 | 0 |
| EndOfUnit | 1 | 519843.95 | 519843.95 | 519843.95 | 519843.95 | 519843.95 | 0.0 | 0 | 1 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[10569] _id=6ac3c5cfde269131f9ad67cf ts=2026-10-05T15:44:15.5330000Z == 6aa4140b41b41dbac0c7f22d.jsonl[10570] _id=6ac3c5cfde269131f9ad67d5 ts=2026-10-05T15:44:15.5330000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 104 group(s), 144 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1577] _id=6ab6815b485cab4c9555df38 ts=2026-09-25T14:09:26.0530000Z == 6aa4140b41b41dbac0c7f22d.jsonl[1595] _id=6ab6815b485cab4c9555df3a ts=2026-09-25T14:09:26.0530000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1415] _id=6ab6809f485cab4c9555d274 ts=2026-09-25T14:09:33.5210000Z == 6aa4140b41b41dbac0c7f22d.jsonl[1398] _id=6ab6809f485cab4c9555d278 ts=2026-09-25T14:09:33.5210000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1419] _id=6ab680a1485cab4c9555d2c2 ts=2026-09-25T14:09:36.4520000Z == 6aa4140b41b41dbac0c7f22d.jsonl[1420] _id=6ab680a2485cab4c9555d2c6 ts=2026-09-25T14:09:36.4520000Z`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 21 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `7ms: 6aa4140b41b41dbac0c7f22d.jsonl[163] _id=6ab3dc61485cab4c954cf39b ts=2026-09-23T14:04:17.3880000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[164] _id=6ab3dc61485cab4c954cf39d ts=2026-09-23T14:04:17.3950000Z`; `4ms: 6aa4140b41b41dbac0c7f22d.jsonl[574] _id=6ab528a7485cab4c95515479 ts=2026-09-24T13:41:59.7020000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[573] _id=6ab528a7485cab4c95515483 ts=2026-09-24T13:41:59.7060000Z`; `682ms: 6aa4140b41b41dbac0c7f22d.jsonl[1316] _id=6ab68035485cab4c9555cec4 ts=2026-09-25T14:07:50.1220000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1323] _id=6ab68036485cab4c9555ceca ts=2026-09-25T14:07:50.8040000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 439 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `11ms: 6aa4140b41b41dbac0c7f22d.jsonl[1414] _id=6ab6809f485cab4c9555d272 ts=2026-09-25T14:09:33.5100000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1415] _id=6ab6809f485cab4c9555d274 ts=2026-09-25T14:09:33.5210000Z`; `35ms: 6aa4140b41b41dbac0c7f22d.jsonl[1398] _id=6ab6809f485cab4c9555d278 ts=2026-09-25T14:09:33.5210000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1378] _id=6ab6809f485cab4c9555d27c ts=2026-09-25T14:09:33.5560000Z`; `39ms: 6aa4140b41b41dbac0c7f22d.jsonl[1378] _id=6ab6809f485cab4c9555d27c ts=2026-09-25T14:09:33.5560000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1399] _id=6ab680a0485cab4c9555d27e ts=2026-09-25T14:09:33.5950000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `536ms: 6aa4140b41b41dbac0c7f22d.jsonl[3911] _id=6aba74f1485cab4c95688269 ts=2026-09-28T14:08:49.2620000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[3912] _id=6aba74f1485cab4c9568827f ts=2026-09-28T14:08:49.7980000Z`; `733ms: 6aa4140b41b41dbac0c7f22d.jsonl[3905] _id=6aba74f2485cab4c95688289 ts=2026-09-28T14:08:50.2970000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[3915] _id=6aba74f3485cab4c95688295 ts=2026-09-28T14:08:51.0300000Z`; `769ms: 6aa4140b41b41dbac0c7f22d.jsonl[3923] _id=6aba74f9485cab4c956882f7 ts=2026-09-28T14:08:57.4620000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[3924] _id=6aba74fa485cab4c9568830c ts=2026-09-28T14:08:58.2310000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `888ms: 6aa4140b41b41dbac0c7f22d.jsonl[7051] _id=6abd1bc9485cab4c958b2ba8 ts=2026-09-30T14:25:13.5230000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[7052] _id=6abd1bca485cab4c958b2bd2 ts=2026-09-30T14:25:14.4110000Z`; `510ms: 6aa4140b41b41dbac0c7f22d.jsonl[11327] _id=6ac3cbbdde269131f9ad9603 ts=2026-10-05T16:09:33.0640000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[11330] _id=6ac3cbbdde269131f9ad9611 ts=2026-10-05T16:09:33.5740000Z`; `434ms: 6aa4140b41b41dbac0c7f22d.jsonl[12323] _id=6ac4ffa9de269131f9b24610 ts=2026-10-06T14:03:21.6760000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[12326] _id=6ac4ffaade269131f9b24620 ts=2026-10-06T14:03:22.1100000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `60ms: 6aa4140b41b41dbac0c7f22d.jsonl[7080] _id=6abd1bdf485cab4c958b2f7b ts=2026-09-30T14:25:35.6450000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[7084] _id=6abd1be0485cab4c958b2f89 ts=2026-09-30T14:25:35.7050000Z`; `48ms: 6aa4140b41b41dbac0c7f22d.jsonl[12376] _id=6ac4ffd6de269131f9b24986 ts=2026-10-06T14:04:06.8010000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[12378] _id=6ac4ffd7de269131f9b24994 ts=2026-10-06T14:04:06.8490000Z`; `37ms: 6aa4140b41b41dbac0c7f22d.jsonl[13418] _id=6ac66d3cde269131f9bc4437 ts=2026-10-07T16:03:08.5410000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[13421] _id=6ac66d3cde269131f9bc443a ts=2026-10-07T16:03:08.5780000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 232 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `229ms: 6aa4140b41b41dbac0c7f22d.jsonl[1009] _id=6ab53057485cab4c9551ec05 ts=2026-09-24T14:14:47.4830000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1011] _id=6ab53057485cab4c9551ec09 ts=2026-09-24T14:14:47.7120000Z`; `873ms: 6aa4140b41b41dbac0c7f22d.jsonl[1019] _id=6ab5305e485cab4c9551eca3 ts=2026-09-24T14:14:54.2990000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1026] _id=6ab5305f485cab4c9551ecb3 ts=2026-09-24T14:14:55.1720000Z`; `863ms: 6aa4140b41b41dbac0c7f22d.jsonl[1027] _id=6ab53060485cab4c9551ecc7 ts=2026-09-24T14:14:56.1660000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[1020] _id=6ab53061485cab4c9551ecd3 ts=2026-09-24T14:14:57.0290000Z`
- **INFO / Info** `gameWindowUnfocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa4140b41b41dbac0c7f22d.jsonl[5978] _id=6abd1515485cab4c95896427 ts=2026-09-30T13:56:37.3640000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[5981] _id=6abd1529485cab4c958964e3 ts=2026-09-30T13:56:37.364Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa4140b41b41dbac0c7f22d.jsonl[4798] _id=6aba7971485cab4c9568e12b ts=2026-09-28T14:28:00.4260000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[4801] _id=6aba7971485cab4c9568e12e ts=2026-09-28T14:28:00.4300000Z`; `2ms: 6aa4140b41b41dbac0c7f22d.jsonl[4925] _id=6abbc35f485cab4c957e0e23 ts=2026-09-29T13:55:42.6960000Z ~ 6aa4140b41b41dbac0c7f22d.jsonl[4926] _id=6abbc35f485cab4c957e0e25 ts=2026-09-29T13:55:42.6980000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f22d.jsonl[8558] _id=6abe6dd1485cab4c95a87bcf ts=2026-10-01T14:27:29.4460000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8609] _id=6ac3aa97de269131f9a9ca70 ts=2026-10-05T13:48:07.6390000Z; 71h 44m: 6aa4140b41b41dbac0c7f22d.jsonl[1117] _id=6ab67f75485cab4c9555c488 ts=2026-09-25T14:04:37.6360000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3513] _id=6aba703a485cab4c95681d11 ts=2026-09-28T13:48:42.9170000Z; 24h 19m: 6aa4140b41b41dbac0c7f22d.jsonl[12404] _id=6ac50017de269131f9b24efa ts=2026-10-06T14:05:11.0770000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12431] _id=6ac65613de269131f9bacb23 ts=2026-10-07T14:24:19.7900000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f22d.jsonl[8590] _id=6abe6de1485cab4c95a87fb6 ts=2026-10-01T14:27:45.4560000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8613] _id=6ac3aab0de269131f9a9d034 ts=2026-10-05T13:48:32.6400000Z; 71h 21m: 6aa4140b41b41dbac0c7f22d.jsonl[3506] _id=6ab68528485cab4c95564787 ts=2026-09-25T14:28:56.9750000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3602] _id=6aba70ae485cab4c95682611 ts=2026-09-28T13:50:38.3710000Z; 24h 17m: 6aa4140b41b41dbac0c7f22d.jsonl[12430] _id=6ac50067de269131f9b2542a ts=2026-10-06T14:06:31.6490000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12438] _id=6ac6561fde269131f9bacc4c ts=2026-10-07T14:24:31.4580000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 601 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[12957] _id=6ac66ae7de269131f9bc387a ts=2026-10-07T15:53:11.4910000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12958] _id=6ac66ae7de269131f9bc387b ts=2026-10-07T15:53:11.4910000Z; 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[13235] _id=6ac66c43de269131f9bc3f00 ts=2026-10-07T15:58:59.2360000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[13236] _id=6ac66c43de269131f9bc3f01 ts=2026-10-07T15:58:59.2360000Z; 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[13287] _id=6ac66ca4de269131f9bc40f6 ts=2026-10-07T16:00:36.2810000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[13288] _id=6ac66ca4de269131f9bc40f7 ts=2026-10-07T16:00:36.2810000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 24m 
  - Evidence: 144h 24m: 6aa4140b41b41dbac0c7f22d.jsonl[1255] _id=6ab67f08485cab4c9555bf88 ts=2026-09-25T14:02:49.1210000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8583] _id=6abe6dad485cab4c95a87239 ts=2026-10-01T14:26:53.0710000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 21m 
  - Evidence: 95h 21m: 6aa4140b41b41dbac0c7f22d.jsonl[8574] _id=6abe6d9d485cab4c95a86e3b ts=2026-10-01T14:26:37.2850000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8611] _id=6ac3aa9cde269131f9a9cbb9 ts=2026-10-05T13:48:12.2150000Z; 71h 21m: 6aa4140b41b41dbac0c7f22d.jsonl[3436] _id=6ab684c7485cab4c955640ae ts=2026-09-25T14:27:19.1350000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3514] _id=6aba7046485cab4c95681dc9 ts=2026-09-28T13:48:54.0550000Z; 24h 20m: 6aa4140b41b41dbac0c7f22d.jsonl[12401] _id=6ac50011de269131f9b24ea0 ts=2026-10-06T14:05:05.5640000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12448] _id=6ac6566cde269131f9bad442 ts=2026-10-07T14:25:48.0930000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 160 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[10569] _id=6ac3c5cfde269131f9ad67cf ts=2026-10-05T15:44:15.5330000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10570] _id=6ac3c5cfde269131f9ad67d5 ts=2026-10-05T15:44:15.5330000Z; 1ms: 6aa4140b41b41dbac0c7f22d.jsonl[10568] _id=6ac3c5cfde269131f9ad67cd ts=2026-10-05T15:44:15.5320000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10569] _id=6ac3c5cfde269131f9ad67cf ts=2026-10-05T15:44:15.5330000Z; 1ms: 6aa4140b41b41dbac0c7f22d.jsonl[8017] _id=6abe6774485cab4c95a77ecd ts=2026-10-01T14:00:19.9940000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8018] _id=6abe6774485cab4c95a77ed3 ts=2026-10-01T14:00:19.9950000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 27m 
  - Evidence: 95h 27m: 6aa4140b41b41dbac0c7f22d.jsonl[8575] _id=6abe6d9e485cab4c95a86eb9 ts=2026-10-01T14:26:38.8090000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8736] _id=6ac3ac14de269131f9aa1f3e ts=2026-10-05T13:54:28.8950000Z; 71h 47m: 6aa4140b41b41dbac0c7f22d.jsonl[3276] _id=6ab6832f485cab4c95562aae ts=2026-09-25T14:20:31.7970000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3887] _id=6aba74c6485cab4c95688023 ts=2026-09-28T14:08:06.7840000Z; 24h 34m: 6aa4140b41b41dbac0c7f22d.jsonl[11907] _id=6ac4fcf8de269131f9b1b541 ts=2026-10-06T13:51:52.6510000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12477] _id=6ac65699de269131f9bad755 ts=2026-10-07T14:26:33.8290000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 10 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[12517] _id=6ac656e8de269131f9bada4c ts=2026-10-07T14:27:51.9200000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12519] _id=6ac656e8de269131f9bada4d ts=2026-10-07T14:27:51.9200000Z; 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[12589] _id=6ac65745de269131f9baddc9 ts=2026-10-07T14:29:25.8120000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12590] _id=6ac65745de269131f9baddca ts=2026-10-07T14:29:25.8120000Z; 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[12774] _id=6ac6694ade269131f9bc296f ts=2026-10-07T15:46:18.0760000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12775] _id=6ac6694ade269131f9bc2970 ts=2026-10-07T15:46:18.0760000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 17m 
  - Evidence: 95h 17m: 6aa4140b41b41dbac0c7f22d.jsonl[8605] _id=6abe6e7c485cab4c95a8a1f3 ts=2026-10-01T14:30:20.8910000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8610] _id=6ac3aa9cde269131f9a9cbb4 ts=2026-10-05T13:48:07.6510000Z; 71h 19m: 6aa4140b41b41dbac0c7f22d.jsonl[3509] _id=6ab68548485cab4c95564976 ts=2026-09-25T14:29:28.8850000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3515] _id=6aba7041485cab4c95681d6f ts=2026-09-28T13:48:42.9230000Z; 23h 38m: 6aa4140b41b41dbac0c7f22d.jsonl[1044] _id=6ab53091485cab4c9551ee67 ts=2026-09-24T14:15:44.9760000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[1053] _id=6ab67cfc485cab4c9555a010 ts=2026-09-25T13:53:58.1530000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 96h 6m 
  - Evidence: 96h 6m: 6aa4140b41b41dbac0c7f22d.jsonl[7570] _id=6abe6499485cab4c95a6d5d2 ts=2026-10-01T13:48:08.9430000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8774] _id=6ac3ac32de269131f9aa2622 ts=2026-10-05T13:54:57.4390000Z; 71h 50m: 6aa4140b41b41dbac0c7f22d.jsonl[3243] _id=6ab682f1485cab4c9556252a ts=2026-09-25T14:19:28.5070000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3952] _id=6aba753f485cab4c956887c3 ts=2026-09-28T14:10:06.9450000Z; 24h 25m: 6aa4140b41b41dbac0c7f22d.jsonl[5416] _id=6abbc60c485cab4c957e5883 ts=2026-09-29T14:07:07.1020000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[7424] _id=6abd1d8a485cab4c958b4a0f ts=2026-09-30T14:32:41.1490000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1972 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[10110] _id=6ac3b3e7de269131f9abcea6 ts=2026-10-05T14:27:51.0890000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10109] _id=6ac3b3e7de269131f9abceab ts=2026-10-05T14:27:51.0890000Z; 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[10111] _id=6ac3b3e8de269131f9abceb0 ts=2026-10-05T14:27:51.2110000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10112] _id=6ac3b3e8de269131f9abceb6 ts=2026-10-05T14:27:51.2110000Z; 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[10115] _id=6ac3b3f6de269131f9abd144 ts=2026-10-05T14:28:06.3060000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10116] _id=6ac3b3f6de269131f9abd146 ts=2026-10-05T14:28:06.3060000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 119h 22m 
  - Evidence: 119h 22m: 6aa4140b41b41dbac0c7f22d.jsonl[7406] _id=6abd1d5d485cab4c958b48cf ts=2026-09-30T14:31:57.8530000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8738] _id=6ac3ac14de269131f9aa1f38 ts=2026-10-05T13:54:28.8880000Z; 71h 47m: 6aa4140b41b41dbac0c7f22d.jsonl[3274] _id=6ab68332485cab4c95562ad4 ts=2026-09-25T14:20:34.7970000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3886] _id=6aba74c6485cab4c95688021 ts=2026-09-28T14:08:06.7790000Z; 50h 16m: 6aa4140b41b41dbac0c7f22d.jsonl[8982] _id=6ac3ac73de269131f9aa351b ts=2026-10-05T13:56:03.3340000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[13642] _id=6ac66f8ede269131f9bc5046 ts=2026-10-07T16:13:02.6240000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa4140b41b41dbac0c7f22d.jsonl[8453] _id=6abe6c44485cab4c95a81adc ts=2026-10-01T14:20:52.5120000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[9019] _id=6ac3ac8dde269131f9aa3a96 ts=2026-10-05T13:56:29.2710000Z; 71h 25m: 6aa4140b41b41dbac0c7f22d.jsonl[3504] _id=6ab68529485cab4c95564790 ts=2026-09-25T14:28:57.0010000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3649] _id=6aba7175485cab4c95683e37 ts=2026-09-28T13:53:57.5170000Z; 24h 19m: 6aa4140b41b41dbac0c7f22d.jsonl[3775] _id=6aba7320485cab4c956867c7 ts=2026-09-28T14:01:04.7080000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[5612] _id=6abbc944485cab4c957e9de9 ts=2026-09-29T14:20:52.8980000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 121h 35m 
  - Evidence: 121h 35m: 6aa4140b41b41dbac0c7f22d.jsonl[7082] _id=6abd1bdf485cab4c958b2f73 ts=2026-09-30T14:25:35.6170000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[11013] _id=6ac3c9cdde269131f9ad8981 ts=2026-10-05T16:01:17.8060000Z; 120h 26m: 6aa4140b41b41dbac0c7f22d.jsonl[1123] _id=6ab67e1a485cab4c9555b56a ts=2026-09-25T13:58:50.7000000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[7043] _id=6abd1bc7485cab4c958b2b38 ts=2026-09-30T14:25:11.1290000Z; 25h 49m: 6aa4140b41b41dbac0c7f22d.jsonl[12351] _id=6ac4ffd6de269131f9b24984 ts=2026-10-06T14:04:06.7750000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12956] _id=6ac66ae7de269131f9bc3879 ts=2026-10-07T15:53:11.4610000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 121h 34m 
  - Evidence: 121h 34m: 6aa4140b41b41dbac0c7f22d.jsonl[7084] _id=6abd1be0485cab4c958b2f89 ts=2026-09-30T14:25:35.7050000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10976] _id=6ac3c97cde269131f9ad8735 ts=2026-10-05T15:59:56.2300000Z; 120h 25m: 6aa4140b41b41dbac0c7f22d.jsonl[1131] _id=6ab67e1a485cab4c9555b56c ts=2026-09-25T13:58:50.7210000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[6961] _id=6abd1b7a485cab4c958b1d02 ts=2026-09-30T14:23:54.5290000Z; 25h 48m: 6aa4140b41b41dbac0c7f22d.jsonl[12378] _id=6ac4ffd7de269131f9b24994 ts=2026-10-06T14:04:06.8490000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12919] _id=6ac66ac4de269131f9bc378c ts=2026-10-07T15:52:36.7140000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.037s..0.048s shown 
  - Evidence: 37ms: 6aa4140b41b41dbac0c7f22d.jsonl[13418] _id=6ac66d3cde269131f9bc4437 ts=2026-10-07T16:03:08.5410000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[13421] _id=6ac66d3cde269131f9bc443a ts=2026-10-07T16:03:08.5780000Z; 48ms: 6aa4140b41b41dbac0c7f22d.jsonl[12376] _id=6ac4ffd6de269131f9b24986 ts=2026-10-06T14:04:06.8010000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12378] _id=6ac4ffd7de269131f9b24994 ts=2026-10-06T14:04:06.8490000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 121h 34m 
  - Evidence: 121h 34m: 6aa4140b41b41dbac0c7f22d.jsonl[7076] _id=6abd1bda485cab4c958b2e7f ts=2026-09-30T14:25:30.2060000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10978] _id=6ac3c980de269131f9ad874a ts=2026-10-05T16:00:00.5820000Z; 120h 25m: 6aa4140b41b41dbac0c7f22d.jsonl[1122] _id=6ab67e18485cab4c9555b54e ts=2026-09-25T13:58:49.0480000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[6967] _id=6abd1b86485cab4c958b1f42 ts=2026-09-30T14:24:06.5720000Z; 25h 48m: 6aa4140b41b41dbac0c7f22d.jsonl[12373] _id=6ac4ffd4de269131f9b2496a ts=2026-10-06T14:04:04.3440000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12924] _id=6ac66ac6de269131f9bc379d ts=2026-10-07T15:52:38.7680000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 264 interval(s) ≤ 0.003s..0.017s shown 
  - Evidence: 3ms: 6aa4140b41b41dbac0c7f22d.jsonl[11984] _id=6ac4fe3ede269131f9b20f48 ts=2026-10-06T13:57:18.4860000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[11977] _id=6ac4fe3ede269131f9b20f54 ts=2026-10-06T13:57:18.4890000Z; 3ms: 6aa4140b41b41dbac0c7f22d.jsonl[12073] _id=6ac4feb4de269131f9b230c1 ts=2026-10-06T13:59:15.9700000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12070] _id=6ac4feb4de269131f9b230c8 ts=2026-10-06T13:59:15.9730000Z; 17ms: 6aa4140b41b41dbac0c7f22d.jsonl[11059] _id=6ac3c9f2de269131f9ad8a7b ts=2026-10-05T16:01:54.3080000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[11060] _id=6ac3c9f2de269131f9ad8a7d ts=2026-10-05T16:01:54.3250000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f22d.jsonl[8586] _id=6abe6db9485cab4c95a875cb ts=2026-10-01T14:27:05.5590000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8607] _id=6ac3aa89de269131f9a9c885 ts=2026-10-05T13:47:53.3030000Z; 71h 44m: 6aa4140b41b41dbac0c7f22d.jsonl[1116] _id=6ab67f68485cab4c9555c42e ts=2026-09-25T14:04:24.4910000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3512] _id=6aba7030485cab4c95681cdd ts=2026-09-28T13:48:32.4830000Z; 24h 37m: 6aa4140b41b41dbac0c7f22d.jsonl[11727] _id=6ac4fbc0de269131f9b15e8d ts=2026-10-06T13:46:40.3500000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12433] _id=6ac65614de269131f9bacb2e ts=2026-10-07T14:24:20.2980000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 16 gap(s), longest 95h 20m 
  - Evidence: 95h 20m: 6aa4140b41b41dbac0c7f22d.jsonl[8585] _id=6abe6db9485cab4c95a875b9 ts=2026-10-01T14:27:05.5570000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8608] _id=6ac3aa89de269131f9a9c882 ts=2026-10-05T13:47:53.3020000Z; 71h 44m: 6aa4140b41b41dbac0c7f22d.jsonl[1115] _id=6ab67f68485cab4c9555c42c ts=2026-09-25T14:04:24.4900000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3511] _id=6aba7030485cab4c95681cdb ts=2026-09-28T13:48:32.4820000Z; 24h 37m: 6aa4140b41b41dbac0c7f22d.jsonl[11726] _id=6ac4fbc0de269131f9b15e87 ts=2026-10-06T13:46:40.3490000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12432] _id=6ac65614de269131f9bacb2d ts=2026-10-07T14:24:20.2980000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 96h 26m 
  - Evidence: 96h 26m: 6aa4140b41b41dbac0c7f22d.jsonl[8166] _id=6abe6847485cab4c95a79435 ts=2026-10-01T14:03:51.1410000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[10196] _id=6ac3b46ede269131f9abe339 ts=2026-10-05T14:30:06.6580000Z; 71h 52m: 6aa4140b41b41dbac0c7f22d.jsonl[3510] _id=6ab68548485cab4c95564971 ts=2026-09-25T14:29:28.2160000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[4777] _id=6aba7802485cab4c9568cc23 ts=2026-09-28T14:21:54.9530000Z; 24h 24m: 6aa4140b41b41dbac0c7f22d.jsonl[12427] _id=6ac50065de269131f9b253fe ts=2026-10-06T14:06:29.3470000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12636] _id=6ac657bbde269131f9bae2fb ts=2026-10-07T14:31:22.9730000Z
- **INFO / Info** `gameWindowUnfocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa4140b41b41dbac0c7f22d.jsonl[5978] _id=6abd1515485cab4c95896427 ts=2026-09-30T13:56:37.3640000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[5981] _id=6abd1529485cab4c958964e3 ts=2026-09-30T13:56:37.364Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 20 gap(s), longest 95h 24m 
  - Evidence: 95h 24m: 6aa4140b41b41dbac0c7f22d.jsonl[8580] _id=6abe6da4485cab4c95a86fd5 ts=2026-10-01T14:26:44.0940000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[8635] _id=6ac3ab61de269131f9a9f51c ts=2026-10-05T13:51:29.8030000Z; 71h 20m: 6aa4140b41b41dbac0c7f22d.jsonl[3499] _id=6ab68516485cab4c9556468a ts=2026-09-25T14:28:38.6150000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[3516] _id=6aba7041485cab4c95681d71 ts=2026-09-28T13:48:49.3410000Z; 24h 19m: 6aa4140b41b41dbac0c7f22d.jsonl[12386] _id=6ac4fffbde269131f9b24cde ts=2026-10-06T14:04:43.5540000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[12437] _id=6ac6561ede269131f9bacc39 ts=2026-10-07T14:24:30.3610000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa4140b41b41dbac0c7f22d.jsonl[974] _id=6ab52fc7485cab4c9551e27d ts=2026-09-24T14:12:23.5080000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[975] _id=6ab52fc7485cab4c9551e283 ts=2026-09-24T14:12:23.5090000Z; 2ms: 6aa4140b41b41dbac0c7f22d.jsonl[4925] _id=6abbc35f485cab4c957e0e23 ts=2026-09-29T13:55:42.6960000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[4926] _id=6abbc35f485cab4c957e0e25 ts=2026-09-29T13:55:42.6980000Z; 3ms: 6aa4140b41b41dbac0c7f22d.jsonl[1065] _id=6ab67d25485cab4c9555a1f8 ts=2026-09-25T13:54:45.7350000Z -> 6aa4140b41b41dbac0c7f22d.jsonl[1066] _id=6ab67d25485cab4c9555a1fa ts=2026-09-25T13:54:45.7380000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 11 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[950] _id=6ab52faa485cab4c9551e0eb ts=2026-09-24T14:11:54.7560000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[3772] _id=6aba731c485cab4c95686756 ts=2026-09-28T14:01:00.6170000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[4655] _id=6aba7776485cab4c9568c4d3 ts=2026-09-28T14:19:34.0350000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 93 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1958] _id=6ab68182485cab4c9555e650 ts=2026-09-25T14:13:20.6680000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1961] _id=6ab68184485cab4c9555e6e6 ts=2026-09-25T14:13:23.5040000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1962] _id=6ab68184485cab4c9555e6ef ts=2026-09-25T14:13:23.5360000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 210 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1576] _id=6ab6815b485cab4c9555df34 ts=2026-09-25T14:09:26.0530000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1595] _id=6ab6815b485cab4c9555df3a ts=2026-09-25T14:09:26.0530000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1415] _id=6ab6809f485cab4c9555d274 ts=2026-09-25T14:09:33.5210000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[7084] _id=6abd1be0485cab4c958b2f89 ts=2026-09-30T14:25:35.7050000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[13421] _id=6ac66d3cde269131f9bc443a ts=2026-10-07T16:03:08.5780000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 35 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1029] _id=6ab53064485cab4c9551ed0f ts=2026-09-24T14:15:00.7240000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1032] _id=6ab53064485cab4c9551ed11 ts=2026-09-24T14:15:00.7420000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[6976] _id=6abd1bb2485cab4c958b27b3 ts=2026-09-30T14:24:49.9920000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[8218] _id=6abe692d485cab4c95a79fa5 ts=2026-10-01T14:07:41.3030000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 354 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1956] _id=6ab68181485cab4c9555e61c ts=2026-09-25T14:13:20.3110000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1976] _id=6ab68185485cab4c9555e736 ts=2026-09-25T14:13:24.6340000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[2025] _id=6ab6818f485cab4c9555e8f8 ts=2026-09-25T14:13:34.0860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 767 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1394] _id=6ab6809e485cab4c9555d250 ts=2026-09-25T14:09:33.3330000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1383] _id=6ab680a1485cab4c9555d296 ts=2026-09-25T14:09:35.2550000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1437] _id=6ab680ab485cab4c9555d3a8 ts=2026-09-25T14:09:47.1860000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 13 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[3649] _id=6aba7175485cab4c95683e37 ts=2026-09-28T13:53:57.5170000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[3729] _id=6aba727e485cab4c95685e5d ts=2026-09-28T13:58:22.0890000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[3769] _id=6aba7306485cab4c95686537 ts=2026-09-28T14:00:38.2160000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[11954] _id=6ac4fd9cde269131f9b1df61 ts=2026-10-06T13:54:36.3270000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Low** `argumentationNodeEvent` `actionType` — node hover: repeated open with no intervening close. 
  - Observed: 254 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1030] _id=6ab53067485cab4c9551ed3b ts=2026-09-24T14:15:02.8330000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1124] _id=6ab67e14485cab4c9555b510 ts=2026-09-25T13:58:44.2920000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1128] _id=6ab67e17485cab4c9555b52e ts=2026-09-25T13:58:47.9480000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 4 occurrence(s) 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[7004] _id=6abd1bb9485cab4c958b28f4 ts=2026-09-30T14:24:57.5420000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[7007] _id=6abd1bbc485cab4c958b2962 ts=2026-09-30T14:24:59.9920000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[7053] _id=6abd1bcb485cab4c958b2c00 ts=2026-09-30T14:25:15.4750000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'DialogueStartEvent' (totals: 386 start, 376 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 91 unmatched 'BecameCameraCentered' (totals: 587 open, 589 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 86 unmatched 'BecameVisible' (totals: 1140 open, 1264 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'MapOpenEvent' (totals: 15 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `argumentationNodeEvent` `actionType` — node hover: open(s) never closed (may be legitimate at session end). 
  - Observed: 7 unmatched 'argumentationNodeHoverStart' (totals: 570 open, 598 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 5 unmatched 'argumentationToolOpen' (totals: 5 open, 0 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'questActiveEvent' (totals: 48 start, 31 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 261 of 13697 adjacent _id pairs reverse in client time; worst 195.6s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa4140b41b41dbac0c7f22d.jsonl[1590] _id=6ab68159485cab4c9555df0a ts=2026-09-25T14:12:41.6010000Z`; `6aa4140b41b41dbac0c7f22d.jsonl[1585] _id=6ab6815a485cab4c9555df1c ts=2026-09-25T14:09:25.9630000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -197.92s, max +0.40s over 13698 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6aa4140b41b41dbac0c7f22d\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3580 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (2662); Unit 4 Dev (808); Unit 3 Dungeon Dev (110)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.65s, n=3579)
- **Open findings:** 6 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3580/3580 records)
    "BecameInvisible"  x1264
    "BecameVisible"  x1140
    "BecameCameraUncentered"  x589
    "BecameCameraCentered"  x587
data.pieceId  (string, 3580/3580 records)
    32 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3580/3580 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3576 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (1026); Unit 2 Prod (Refactor) (721); Unit 4 Dev - Anderson Base (500); Unit 4 Dev - Dungeon (435); Unit 1 Dev (388); Unit 3 Dungeon Dev (305); Unit 4 Dev (201)
- **Intervals:** median 0.80s (p5 0.06s / p95 15.68s, n=3575)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 3576/3576 records)
    "pressed"  x3576
data.actionType  (string, 3576/3576 records)
    "Move"  x2782
    "Jump"  x390
    "Interact"  x274
    "Ascend"  x62
    "Hoverboard"  x24
    "Sprint"  x16
    "Descend"  x10
    "Map"  x10
    "Pause"  x7
    "ToggleDebug"  x1
data.key  (string, 3576/3576 records, 2 empty-string)
    18 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3576/3576 records)
    "Player"  x2419
    "Drone"  x1157
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 2439 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (635); Unit 4 Dev - Anderson Base (480); Unit 1 Dev (464); Unit 3 Dev (356); Unit 4 Dev (248); Unit 4 Dev - Dungeon (161); Unit 3 Dungeon Dev (95)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=2427)
- **Fields under `data`:**

```text
data.position  (object, 2439/2439 records)
data.position.x  (number, 2439/2439 records)
    numeric range -707.331 .. 1554.53 (588 unique)
data.position.y  (number, 2439/2439 records)
    numeric range -115.127 .. 155.365 (441 unique)
data.position.z  (number, 2439/2439 records)
    numeric range -1144.48 .. 1794.63 (588 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 2102 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (550); Unit 4 Dev - Anderson Base (442); Unit 3 Dev (325); Unit 1 Dev (306); Unit 4 Dev (261); Unit 3 Dungeon Dev (124); Unit 4 Dev - Dungeon (94)
- **eventKey:** present on 1340 of 2102 records
- **Intervals:** median 5.00s (p5 0.00s / p95 51.23s, n=2101)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1340; [conversationId, dialogueEventType] x762
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2102/2102 records)
    numeric range 8 .. 114 (44 unique)
data.dialogueEventType  (string, 2102/2102 records)
    "DialogueNodeEvent"  x1340
    "DialogueStartEvent"  x386
    "DialogueFinishEvent"  x376
data.nodeId  (number, 1340/2102 records)
    numeric range 0 .. 290 (218 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `argumentationNodeEvent` — 1320 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (1196); Unit 3 Dev (93); Unit 1 Dev (31)
- **Intervals:** median 0.34s (p5 0.03s / p95 7.89s, n=1319)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1320/1320 records)
    "argumentationNodeHoverEnd"  x598
    "argumentationNodeHoverStart"  x570
    "argumentationNodeAdd"  x86
    "argumentationNodeRemove"  x66
data.argumentationTitle  (string, 1320/1320 records)
    "Unit 4 - Flooding"  x1196
    "Unit 3 - Pollution Upstream"  x93
    "Unit 1 - Argumentation Tutorial"  x22
    "Unit 1 - Freshwater"  x9
data.nodeName  (string, 1320/1320 records)
    "B"  x232
    "A"  x152
    "II"  x133
    "2"  x131
    "C"  x124
    "3"  x121
    "4"  x121
    "I"  x119
    "1"  x114
    "D"  x65
    "5"  x8
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `ObjectInterEvent` — 240 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 4 Dev - Dungeon (61); Unit 2 Prod (Refactor) (58); Unit 4 Dev - Anderson Base (36); Unit 3 Dungeon Dev (35); Unit 4 Dev (20); Unit 1 Dev (18); Unit 3 Dev (12)
- **Intervals:** median 16.78s (p5 0.19s / p95 1151.73s, n=239)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 240/240 records)
    38 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 240/240 records)
    93 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `Soil Key Puzzle` — 129 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (54); Unit 2 Prod (Refactor) (38); Unit 4 Dev (37)
- **Intervals:** median 0.45s (p5 0.17s / p95 9.67s, n=128)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x121; [Soil Key Puzzle Status, Unit] x8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 8/129 records)
    "Finished"  x4
    "Started"  x4
data.Unit  (string, 8/129 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
data.actionType  (string, 121/129 records)
    "RightDrag"  x66
    "LeftDrag"  x55
data.currentSoilType  (string, 121/129 records)
    "CLAYSAND"  x27
    "CLAY"  x23
    "SAND"  x23
    "CLAYROCK"  x19
    "SANDGRAVEL"  x14
    "BEDROCK"  x9
    "GRAVEL"  x6
data.isCorrectSelection  (string, 121/129 records)
    "false"  x95
    "true"  x26
data.waterLevelStatus  (string, 121/129 records)
    "Proper"  x61
    "TooLow"  x31
    "TooHigh"  x29
data.waterRetentionChange  (string, 121/129 records)
    "Decrease"  x50
    "Increase"  x45
    "NoChange"  x26
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 79 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 1 Dev (20); Unit 3 Dev (11); Unit 4 Dev (9); Unit 4 Dev - Dungeon (9); Unit 4 Dev - Anderson Base (6); Unit 3 Dungeon Dev (3)
- **eventKey:** present on 79 of 79 records
- **Intervals:** median 273.66s (p5 0.00s / p95 84994.72s, n=78)
- **`data` key-set variants:** [questEventType, questID, questName] x48; [questEventType, questID, questName, questSuccessOrFailure] x31
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 79/79 records)
    "questActiveEvent"  x48
    "questFinishEvent"  x31
data.questID  (string, 79/79 records)
    26 unique values (see csv/event_unique_values.csv)
data.questName  (string, 79/79 records)
    26 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 31/79 records)
    "Succeeded"  x31
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationAnswerEvent` — 62 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 4 Dev - Anderson Base (55); Unit 3 Dev (5); Unit 1 Dev (2)
- **Intervals:** median 19.48s (p5 2.25s / p95 85438.30s, n=61)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 62/62 records)
    "submitAnswerEvent"  x62
data.answerSubmitted  (string, 62/62 records, 1 empty-string)
    30 unique values (see csv/event_unique_values.csv)
data.argumentationTitle  (string, 62/62 records)
    "Unit 4 - Flooding"  x55
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x1
    "Unit 1 - Freshwater"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `TopographicMapEvent` — 34 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (19); Unit 2 Prod (Refactor) (11); Unit 3 Dungeon Dev (2); Unit 4 Dev (2)
- **Intervals:** median 26.49s (p5 0.80s / p95 155393.12s, n=33)
- **`data` key-set variants:** [actionType, featureUsed] x29; [actionType, featureUsed, location] x5
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "MapOpenEvent"  x15
    "MapCloseEvent"  x14
    "WaypointMoveEvent"  x4
    "WaypointSetEvent"  x1
data.featureUsed  (string, 34/34 records)
    "Map"  x29
    "Waypoint"  x5
data.location  (object, 5/34 records)
data.location.x  (number, 5/34 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 5/34 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 5/34 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `DEBUGMenu` — 28 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 4 Dev (6); Unit 4 Dev - Anderson Base (4); Unit 1 Dev (3); Unit 3 Dev (3); MainMenu (2); Unit 3 Dungeon Dev (2); Unit 4 Dev - Dungeon (1)
- **Intervals:** median 1616.43s (p5 37.66s / p95 207036.31s, n=27)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "DebugMenuStateChanged"  x28
data.isOpened  (bool, 28/28 records)
    false  x28
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (19); Unit 2 Prod (Refactor) (6)
- **Intervals:** median 2017.26s (p5 29.95s / p95 232809.79s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `gameStartEvent` — 19 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (19)
- **Intervals:** median 43163.52s (p5 176.05s / p95 270997.95s, n=18)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 19/19 records)
    true  x19
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 18 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 2 Prod (Refactor) (10); Unit 4 Dev (3); Unit 4 Dev - Anderson Base (2); Unit 1 Dev (1); Unit 3 Dev (1); Unit 3 Dungeon Dev (1)
- **Intervals:** median 6407.21s (p5 2.51s / p95 276432.49s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    false  x18
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 4 Dev - Anderson Base (7); Unit 1 Dev (6); Unit 3 Dev (3)
- **Intervals:** median 101.12s (p5 0.04s / p95 434750.82s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x9
    "argumentationSessionOpen"  x7
data.argumentationDescription  (string, 16/16 records)
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x7
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 16/16 records)
    "Unit 4 - Flooding"  x7
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `TerasGardenBox` — 10 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (10)
- **Intervals:** median 5.02s (p5 1.57s / p95 40.25s, n=9)
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records, 6 empty-string)
    ""  x6
    "cameraPlaced"  x4
data.boxId  (string, 10/10 records)
    "1"  x4
    "0"  x3
    "2"  x3
data.soilType  (string, 10/10 records)
    "Gravel"  x5
    "Sand"  x3
    "Clay"  x2
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 40.49s (p5 5.28s / p95 259.99s, n=7)
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Gravel"  x4
    "Clay"  x3
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

### `DaniEvent` — 6 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (6)
- **Intervals:** median 0.87s (p5 0.69s / p95 60.24s, n=5)
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "Close"  x3
    "Open"  x3
data.toolName  (string, 6/6 records, 6 empty-string)
    ""  x6
```

Raw examples: `event_examples.json` -> `DaniEvent`.

### `argumentationToolEvent` — 5 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (5)
- **Intervals:** median 3.36s (p5 1.91s / p95 13.80s, n=4)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationToolOpen"  x5
data.argumentationTitle  (string, 5/5 records)
    "Unit 3 - Pollution Upstream"  x5
data.toolName  (string, 5/5 records)
    "BackingInfoPanel - Pollution Site Data"  x5
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 519843.95s (p5 519843.95s / p95 519843.95s, n=1)
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
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (38 records)
- `TerasGardenBox` data.actionType: "" (6x)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (4x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (5x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (66x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*