# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f6

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1f6
- **Game version string(s) in log:** 2.8.1, 2.8.9, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1f6.jsonl
- **Records:** 11094 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1f6
- **Time span:** 2026-09-23T13:03:50.774000+00:00 .. 2026-10-07T13:40:48.577000+00:00 (336h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f6\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **18 event types**, 11094 records, 4 scenes.
- Findings: **0 FAIL**, **33 WARNING**, 79 INFO, 5 NOT_TESTED, 65 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TerasGardenBox`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `TopographicMapEvent`: baseline field(s) absent this build
  - WARNING/Medium `TopographicMapEvent`: median interval between records changed substantially
  - WARNING/Medium `WaterChamberEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3826 | 34.49 | 1 | 1 | 0 | 2026-09-28T13:12:23.076000+00:00 | 2026-10-01T13:22:00.823000+00:00 | 72h 9m |
| InputEvent | 3735 | 33.67 | 1 | 3 | 0 | 2026-09-23T13:07:12.796000+00:00 | 2026-10-07T13:37:58.828000+00:00 | 336h 30m |
| PlayerPositionEvent | 1956 | 17.63 | 1 | 3 | 0 | 2026-09-23T13:07:07.159000+00:00 | 2026-10-07T13:40:47.669000+00:00 | 336h 33m |
| DialogueEvent | 1122 | 10.11 | 1 | 3 | 707 | 2026-09-23T13:07:29.638000+00:00 | 2026-10-07T13:40:41.607000+00:00 | 336h 33m |
| ObjectInterEvent | 94 | 0.85 | 1 | 3 | 0 | 2026-09-23T13:21:34.917000+00:00 | 2026-10-06T13:10:35.232000+00:00 | 311h 49m |
| argumentationNodeEvent | 81 | 0.73 | 1 | 1 | 0 | 2026-09-25T13:13:36.109000+00:00 | 2026-09-25T13:22:44.748000+00:00 | 9m 8s |
| TopographicMapEvent | 58 | 0.52 | 1 | 2 | 0 | 2026-09-28T13:13:21.728000+00:00 | 2026-10-07T13:37:01.726000+00:00 | 216h 23m |
| questEvent | 53 | 0.48 | 1 | 3 | 53 | 2026-09-23T13:07:29.619000+00:00 | 2026-10-07T13:33:56.688000+00:00 | 336h 26m |
| Soil Key Puzzle | 50 | 0.45 | 1 | 1 | 0 | 2026-09-28T13:23:16.063000+00:00 | 2026-09-30T13:26:58.669000+00:00 | 48h 3m |
| argumentationAnswerEvent | 27 | 0.24 | 1 | 1 | 0 | 2026-09-25T13:09:07.722000+00:00 | 2026-09-25T13:22:46.458000+00:00 | 13m 38s |
| gameWindowFocusEvent | 25 | 0.23 | 1 | 3 | 0 | 2026-09-23T13:03:50.774000+00:00 | 2026-10-07T13:28:40.271000+00:00 | 336h 24m |
| DEBUGMenu | 17 | 0.15 | 1 | 4 | 0 | 2026-09-23T13:07:07.153000+00:00 | 2026-10-07T13:28:50.770000+00:00 | 336h 21m |
| gameStartEvent | 16 | 0.14 | 1 | 1 | 0 | 2026-09-23T13:03:50.775000+00:00 | 2026-10-07T13:28:40.271000+00:00 | 336h 24m |
| gameWindowUnfocusEvent | 13 | 0.12 | 1 | 2 | 0 | 2026-09-28T13:17:32.313000+00:00 | 2026-10-07T13:40:48.577000+00:00 | 216h 23m |
| argumentationToolEvent | 7 | 0.06 | 1 | 1 | 0 | 2026-09-25T13:13:21.019000+00:00 | 2026-09-25T13:19:37.933000+00:00 | 6m 16s |
| crash | 7 | 0.06 | 1 | 1 | 0 |  |  | ? |
| argumentationEvent | 6 | 0.05 | 1 | 1 | 0 | 2026-09-24T13:26:42.175000+00:00 | 2026-09-25T13:22:46.524000+00:00 | 23h 56m |
| EndOfUnit | 1 | 0.01 | 1 | 1 | 0 | 2026-09-25T13:26:37.822000+00:00 | 2026-09-25T13:26:37.822000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 80385.19s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 17.206s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 1.088s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 164.106s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 40.338s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 85318.746s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 1521.233s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 3301.52s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 393.306s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `EndOfUnit` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: ToggleDebug 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightButton; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 3 Dev; Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` — record volume changed 5.4x vs baseline. 
  - Observed: 27 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,5,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 1 - Argumentation Tutorial 
  - Expected: new design, renamed value, or new coverage — review
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 7 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.3x vs baseline. 
  - Observed: 25 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 13 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 18; 19; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Forsaken Facility; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 16 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[645] _id=6ab3d4c0485cab4c954c639a ts=2026-09-23T13:31:44.2380000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[723] _id=6ab3d668485cab4c954ca3a7 ts=2026-09-23T13:38:48.3970000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[866] _id=6ab51f94485cab4c955006b9 ts=2026-09-24T13:03:16.2790000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 3 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[6625] _id=6abd3229485cab4c958d2dee ts=2026-09-30T16:00:39.4430000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[6817] _id=6abe58df485cab4c95a4063b ts=2026-10-01T12:58:06.0960000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[7673] _id=6abe5dd3485cab4c95a4c015 ts=2026-10-01T13:19:14.9980000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1] _id=6ab3ce36485cab4c954b847c ts=2026-09-23T13:03:50.7750000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[748] _id=6ab51dab485cab4c954fc4a5 ts=2026-09-24T12:55:06.9920000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1208] _id=6ab67109485cab4c95545e3b ts=2026-09-25T13:03:05.4970000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 25 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 25} 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[2] _id=6ab3ce36485cab4c954b847a ts=2026-09-23T13:03:50.7740000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[747] _id=6ab51dab485cab4c954fc49d ts=2026-09-24T12:55:06.9910000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1207] _id=6ab67109485cab4c95545e37 ts=2026-09-25T13:03:05.4950000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 13 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 13} 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[2997] _id=6aba68ec485cab4c9567caad ts=2026-09-28T13:17:32.3130000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[5332] _id=6abd09a6485cab4c958695b9 ts=2026-09-30T13:07:50.2040000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[6821] _id=6abe58d7485cab4c95a405f5 ts=2026-09-30T14:37:42.537Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3825 | 0.0 | 0.035 | 67.916 | 1.024 | 173159.009 | 0.88 | 2267 | 3 |
| InputEvent | 3734 | 0.001 | 0.913 | 324.437 | 8.607 | 343417.145 | 0.18 | 113 | 14 |
| PlayerPositionEvent | 1953 | 9.75 | 10.0 | 620.315 | 10.03 | 343131.515 | 0.1 | 0 | 12 |
| DialogueEvent | 1121 | 0.001 | 6.244 | 1080.814 | 86.21 | 343195.733 | 0.06 | 292 | 14 |
| ObjectInterEvent | 93 | 0.005 | 9.548 | 12070.326 | 84739.498 | 344146.839 | 0.0 | 2 | 9 |
| argumentationNodeEvent | 80 | 0.04 | 0.259 | 6.858 | 10.06 | 225.934 | 8.75 | 11 | 0 |
| TopographicMapEvent | 57 | 0.242 | 17.206 | 13667.018 | 85383.447 | 344296.209 | 0.0 | 0 | 8 |
| questEvent | 52 | 0.001 | 393.306 | 23292.059 | 86327.102 | 343323.923 | 0.0 | 9 | 17 |
| Soil Key Puzzle | 49 | 0.264 | 0.69 | 3531.074 | 10.08 | 172909.167 | 0.02 | 0 | 1 |
| argumentationAnswerEvent | 26 | 0.192 | 1.088 | 31.49 | 164.789 | 256.629 | 1.91 | 0 | 0 |
| gameWindowFocusEvent | 24 | 0.0 | 1521.233 | 50462.062 | 232354.237 | 344257.074 | 0.0 | 1 | 15 |
| DEBUGMenu | 16 | 11.032 | 80385.19 | 75681.476 | 279596.049 | 344253.298 | 0.0 | 0 | 13 |
| gameStartEvent | 15 | 116.848 | 85318.746 | 80739.3 | 283895.62 | 344257.074 | 0.0 | 0 | 13 |
| gameWindowUnfocusEvent | 12 | 14.447 | 3301.52 | 64916.355 | 285144.608 | 423166.15 | 0.0 | 0 | 8 |
| argumentationToolEvent | 6 | 1.093 | 40.338 | 62.819 | 171.207 | 195.859 | 0.96 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| argumentationEvent | 5 | 43.464 | 164.106 | 17232.87 | 68309.806 | 85224.777 | 0.0 | 0 | 2 |
| EndOfUnit | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 144 group(s), 208 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1763] _id=6aba67ce485cab4c9567b8b3 ts=2026-09-28T13:12:45.8080000Z == 6aa413b141b41dbac0c7f1f6.jsonl[1764] _id=6aba67ce485cab4c9567b8b5 ts=2026-09-28T13:12:45.8080000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1769] _id=6aba67d0485cab4c9567b8d3 ts=2026-09-28T13:12:46.3130000Z == 6aa413b141b41dbac0c7f1f6.jsonl[1771] _id=6aba67d0485cab4c9567b8d7 ts=2026-09-28T13:12:46.3130000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1773] _id=6aba67d0485cab4c9567b8dd ts=2026-09-28T13:12:46.3130000Z == 6aa413b141b41dbac0c7f1f6.jsonl[1785] _id=6aba67d0485cab4c9567b8df ts=2026-09-28T13:12:46.3130000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 3 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1662] _id=6aba66e9485cab4c9567a82d ts=? == 6aa413b141b41dbac0c7f1f6.jsonl[5189] _id=6abd07df485cab4c958679d3 ts=?`; `6aa413b141b41dbac0c7f1f6.jsonl[8230] _id=6ac39f73de269131f9a84122 ts=? == 6aa413b141b41dbac0c7f1f6.jsonl[10785] _id=6ac64918de269131f9b92306 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 16 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `419ms: 6aa413b141b41dbac0c7f1f6.jsonl[439] _id=6ab3d26d485cab4c954befd6 ts=2026-09-23T13:21:49.7010000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[434] _id=6ab3d26e485cab4c954befdd ts=2026-09-23T13:21:50.1200000Z`; `228ms: 6aa413b141b41dbac0c7f1f6.jsonl[434] _id=6ab3d26e485cab4c954befdd ts=2026-09-23T13:21:50.1200000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[431] _id=6ab3d26e485cab4c954befe2 ts=2026-09-23T13:21:50.3480000Z`; `202ms: 6aa413b141b41dbac0c7f1f6.jsonl[431] _id=6ab3d26e485cab4c954befe2 ts=2026-09-23T13:21:50.3480000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[432] _id=6ab3d26e485cab4c954befea ts=2026-09-23T13:21:50.5500000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 516 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `309ms: 6aa413b141b41dbac0c7f1f6.jsonl[1758] _id=6aba67cf485cab4c9567b8c9 ts=2026-09-28T13:12:45.8080000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1759] _id=6aba67cf485cab4c9567b8cd ts=2026-09-28T13:12:46.1170000Z`; `67ms: 6aa413b141b41dbac0c7f1f6.jsonl[1760] _id=6aba67d0485cab4c9567b8d1 ts=2026-09-28T13:12:46.2460000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1769] _id=6aba67d0485cab4c9567b8d3 ts=2026-09-28T13:12:46.3130000Z`; `509ms: 6aa413b141b41dbac0c7f1f6.jsonl[1780] _id=6aba67d2485cab4c9567b8fd ts=2026-09-28T13:12:46.9570000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1781] _id=6aba67d2485cab4c9567b901 ts=2026-09-28T13:12:47.4660000Z`
- **INFO / Info** `Soil Key Puzzle` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `968ms: 6aa413b141b41dbac0c7f1f6.jsonl[4379] _id=6aba6a78485cab4c9567eb77 ts=2026-09-28T13:24:08.4130000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[4381] _id=6aba6a79485cab4c9567eba7 ts=2026-09-28T13:24:09.3810000Z`
- **INFO / Info** `argumentationAnswerEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `532ms: 6aa413b141b41dbac0c7f1f6.jsonl[1308] _id=6ab67377485cab4c955488db ts=2026-09-25T13:13:27.3560000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1316] _id=6ab67377485cab4c955488ed ts=2026-09-25T13:13:27.8880000Z`; `289ms: 6aa413b141b41dbac0c7f1f6.jsonl[1316] _id=6ab67377485cab4c955488ed ts=2026-09-25T13:13:27.8880000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1317] _id=6ab67378485cab4c955488f5 ts=2026-09-25T13:13:28.1770000Z`; `821ms: 6aa413b141b41dbac0c7f1f6.jsonl[1314] _id=6ab67379485cab4c95548925 ts=2026-09-25T13:13:29.5320000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1309] _id=6ab6737a485cab4c95548946 ts=2026-09-25T13:13:30.3530000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 11 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `439ms: 6aa413b141b41dbac0c7f1f6.jsonl[1326] _id=6ab67380485cab4c95548a1f ts=2026-09-25T13:13:36.4940000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1331] _id=6ab67380485cab4c95548a31 ts=2026-09-25T13:13:36.9330000Z`; `774ms: 6aa413b141b41dbac0c7f1f6.jsonl[1327] _id=6ab67380485cab4c95548a25 ts=2026-09-25T13:13:36.5490000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1332] _id=6ab67381485cab4c95548a3d ts=2026-09-25T13:13:37.3230000Z`; `777ms: 6aa413b141b41dbac0c7f1f6.jsonl[1344] _id=6ab67384485cab4c95548aa5 ts=2026-09-25T13:13:40.3380000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[1346] _id=6ab67384485cab4c95548abf ts=2026-09-25T13:13:41.1150000Z`
- **INFO / Info** `gameWindowFocusEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `0ms: 6aa413b141b41dbac0c7f1f6.jsonl[9960] _id=6ac4ed0ade269131f9affa84 ts=2026-10-06T12:43:55.2560000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[9972] _id=6ac4ed1ede269131f9affa86 ts=2026-10-06T12:43:55.256Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `4ms: 6aa413b141b41dbac0c7f1f6.jsonl[6625] _id=6abd3229485cab4c958d2dee ts=2026-09-30T16:00:39.4430000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[6626] _id=6abd3229485cab4c958d2df2 ts=2026-09-30T16:00:39.4470000Z`; `4ms: 6aa413b141b41dbac0c7f1f6.jsonl[6817] _id=6abe58df485cab4c95a4063b ts=2026-10-01T12:58:06.0960000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[6805] _id=6abe58df485cab4c95a4063d ts=2026-10-01T12:58:06.1000000Z`; `6ms: 6aa413b141b41dbac0c7f1f6.jsonl[7673] _id=6abe5dd3485cab4c95a4c015 ts=2026-10-01T13:19:14.9980000Z ~ 6aa413b141b41dbac0c7f1f6.jsonl[7674] _id=6abe5dd3485cab4c95a4c01f ts=2026-10-01T13:19:15.0040000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa413b141b41dbac0c7f1f6.jsonl[7925] _id=6abe5eb0485cab4c95a52fab ts=2026-10-01T13:22:56.4690000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8232] _id=6ac39f6dde269131f9a840ff ts=2026-10-05T13:00:29.7670000Z; 71h 40m: 6aa413b141b41dbac0c7f1f6.jsonl[1622] _id=6ab676e7485cab4c9554f77e ts=2026-09-25T13:28:07.3930000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1660] _id=6aba66e3485cab4c9567a7a5 ts=2026-09-28T13:08:51.0260000Z; 24h 25m: 6aa413b141b41dbac0c7f1f6.jsonl[9976] _id=6ac4f17ede269131f9b0091e ts=2026-10-06T13:02:54.8420000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10782] _id=6ac64907de269131f9b91f36 ts=2026-10-07T13:28:39.7380000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 19m 
  - Evidence: 95h 19m: 6aa413b141b41dbac0c7f1f6.jsonl[8220] _id=6abe6310485cab4c95a6840b ts=2026-10-01T13:41:36.2880000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8256] _id=6ac39facde269131f9a84320 ts=2026-10-05T13:01:32.0210000Z; 71h 38m: 6aa413b141b41dbac0c7f1f6.jsonl[1648] _id=6ab6775d485cab4c95550ad5 ts=2026-09-25T13:30:05.4440000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1665] _id=6aba66ea485cab4c9567a845 ts=2026-09-28T13:08:58.3920000Z; 23h 51m: 6aa413b141b41dbac0c7f1f6.jsonl[10745] _id=6ac4f9d5de269131f9b0fca1 ts=2026-10-06T13:38:29.0150000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10813] _id=6ac64951de269131f9b93180 ts=2026-10-07T13:29:53.2680000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 292 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f6.jsonl[1363] _id=6ab673da485cab4c95548fc9 ts=2026-09-25T13:15:06.5400000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1364] _id=6ab673da485cab4c95548fcb ts=2026-09-25T13:15:06.5410000Z; 1ms: 6aa413b141b41dbac0c7f1f6.jsonl[1531] _id=6ab67602485cab4c9554d26c ts=2026-09-25T13:24:18.7710000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1528] _id=6ab67602485cab4c9554d271 ts=2026-09-25T13:24:18.7720000Z; 1ms: 6aa413b141b41dbac0c7f1f6.jsonl[1596] _id=6ab67666485cab4c9554e438 ts=2026-09-25T13:25:58.4670000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1597] _id=6ab67666485cab4c9554e43c ts=2026-09-25T13:25:58.4680000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 14 gap(s), longest 95h 23m 
  - Evidence: 95h 23m: 6aa413b141b41dbac0c7f1f6.jsonl[8174] _id=6abe620b485cab4c95a63cd9 ts=2026-10-01T13:37:15.4070000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8235] _id=6ac39f84de269131f9a841aa ts=2026-10-05T13:00:52.5520000Z; 71h 40m: 6aa413b141b41dbac0c7f1f6.jsonl[1635] _id=6ab67718485cab4c955500ec ts=2026-09-25T13:28:56.8000000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1667] _id=6aba66f8485cab4c9567a933 ts=2026-09-28T13:09:12.3430000Z; 23h 50m: 6aa413b141b41dbac0c7f1f6.jsonl[10776] _id=6ac4f9fcde269131f9b103dd ts=2026-10-06T13:39:08.9530000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10790] _id=6ac64925de269131f9b925cd ts=2026-10-07T13:29:09.4860000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 113 interval(s) ≤ 0.001s..0.003s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f6.jsonl[9235] _id=6ac3a47bde269131f9a8bc5d ts=2026-10-05T13:22:03.2440000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[9236] _id=6ac3a47bde269131f9a8bc65 ts=2026-10-05T13:22:03.2450000Z; 2ms: 6aa413b141b41dbac0c7f1f6.jsonl[6814] _id=6abe58de485cab4c95a40633 ts=2026-10-01T12:58:06.0220000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[6804] _id=6abe58de485cab4c95a40635 ts=2026-10-01T12:58:06.0240000Z; 3ms: 6aa413b141b41dbac0c7f1f6.jsonl[8493] _id=6ac3a229de269131f9a86914 ts=2026-10-05T13:12:09.2690000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8486] _id=6ac3a229de269131f9a86916 ts=2026-10-05T13:12:09.2720000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 95h 35m 
  - Evidence: 95h 35m: 6aa413b141b41dbac0c7f1f6.jsonl[8130] _id=6abe6163485cab4c95a6089d ts=2026-10-01T13:34:27.4450000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8369] _id=6ac3a1b6de269131f9a8610e ts=2026-10-05T13:10:14.2840000Z; 71h 45m: 6aa413b141b41dbac0c7f1f6.jsonl[1560] _id=6ab67664485cab4c9554e38e ts=2026-09-25T13:25:56.2330000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1707] _id=6aba678a485cab4c9567b489 ts=2026-09-28T13:11:38.4450000Z; 48h 3m: 6aa413b141b41dbac0c7f1f6.jsonl[4367] _id=6aba6a44485cab4c9567e3f6 ts=2026-09-28T13:23:16.0660000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[5605] _id=6abd0e0b485cab4c9587aea7 ts=2026-09-30T13:26:35.8030000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6aa413b141b41dbac0c7f1f6.jsonl[561] _id=6ab3d38c485cab4c954c1840 ts=2026-09-23T13:26:36.2430000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[562] _id=6ab3d38c485cab4c954c1849 ts=2026-09-23T13:26:36.2480000Z; 5ms: 6aa413b141b41dbac0c7f1f6.jsonl[801] _id=6ab51e4d485cab4c954fda23 ts=2026-09-24T12:57:49.4730000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[792] _id=6ab51e4d485cab4c954fda27 ts=2026-09-24T12:57:49.4780000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 18m 
  - Evidence: 95h 18m: 6aa413b141b41dbac0c7f1f6.jsonl[8221] _id=6abe6312485cab4c95a6846d ts=2026-10-01T13:41:38.2600000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8225] _id=6ac39f73de269131f9a84124 ts=2026-10-05T13:00:29.7750000Z; 71h 38m: 6aa413b141b41dbac0c7f1f6.jsonl[1649] _id=6ab67760485cab4c95550bb1 ts=2026-09-25T13:30:08.2960000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1663] _id=6aba66e9485cab4c9567a82f ts=2026-09-28T13:08:51.0330000Z; 23h 49m: 6aa413b141b41dbac0c7f1f6.jsonl[10780] _id=6ac4f9fede269131f9b10443 ts=2026-10-06T13:39:10.8260000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10786] _id=6ac64918de269131f9b9230a ts=2026-10-07T13:28:50.7770000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 48h 5m 
  - Evidence: 48h 5m: 6aa413b141b41dbac0c7f1f6.jsonl[4326] _id=6aba69f8485cab4c9567df1f ts=2026-09-28T13:21:59.1200000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[5639] _id=6abd0e5e485cab4c9587cfce ts=2026-09-30T13:27:58.1290000Z; 20h 56m: 6aa413b141b41dbac0c7f1f6.jsonl[6766] _id=6abd3255485cab4c958d31a2 ts=2026-09-30T16:01:24.0740000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[6818] _id=6abe58df485cab4c95a4063f ts=2026-10-01T12:58:06.5020000Z; 2h 19m: 6aa413b141b41dbac0c7f1f6.jsonl[6540] _id=6abd115d485cab4c9588f15b ts=2026-09-30T13:40:42.6470000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[6631] _id=6abd3229485cab4c958d2df4 ts=2026-09-30T16:00:39.8140000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2267 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f6.jsonl[1650] _id=6aba67df485cab4c9567b9a9 ts=2026-09-28T13:13:02.6690000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1809] _id=6aba67df485cab4c9567b9ad ts=2026-09-28T13:13:02.6690000Z; 0ms: 6aa413b141b41dbac0c7f1f6.jsonl[1652] _id=6aba67e0485cab4c9567b9b9 ts=2026-09-28T13:13:02.8780000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1653] _id=6aba67e0485cab4c9567b9bb ts=2026-09-28T13:13:02.8780000Z; 0ms: 6aa413b141b41dbac0c7f1f6.jsonl[1747] _id=6aba67da485cab4c9567b95b ts=2026-09-28T13:12:56.9860000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1811] _id=6aba67da485cab4c9567b95f ts=2026-09-28T13:12:56.9860000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 48h 1m 
  - Evidence: 48h 1m: 6aa413b141b41dbac0c7f1f6.jsonl[4414] _id=6aba6a9e485cab4c9567f0af ts=2026-09-28T13:24:46.6280000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[5623] _id=6abd0e0b485cab4c9587ae92 ts=2026-09-30T13:26:35.7950000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 95h 38m 
  - Evidence: 95h 38m: 6aa413b141b41dbac0c7f1f6.jsonl[8055] _id=6abe60bb485cab4c95a5d953 ts=2026-10-01T13:31:39.1660000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8345] _id=6ac3a1a3de269131f9a85ffe ts=2026-10-05T13:09:55.3750000Z; 24h 24m: 6aa413b141b41dbac0c7f1f6.jsonl[5305] _id=6abd0957485cab4c958690c3 ts=2026-09-30T13:06:31.3360000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8052] _id=6abe60b0485cab4c95a5d601 ts=2026-10-01T13:31:28.8720000Z; 24h 0m: 6aa413b141b41dbac0c7f1f6.jsonl[10643] _id=6ac4f8d6de269131f9b0cf81 ts=2026-10-06T13:34:14.6460000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10877] _id=6ac64a8cde269131f9b986a9 ts=2026-10-07T13:35:08.2610000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 23h 40m 
  - Evidence: 23h 40m: 6aa413b141b41dbac0c7f1f6.jsonl[1182] _id=6ab52564485cab4c955102a1 ts=2026-09-24T13:28:04.2550000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1260] _id=6ab6724c485cab4c955470e7 ts=2026-09-25T13:08:29.0320000Z; 10m 49s: 6aa413b141b41dbac0c7f1f6.jsonl[1297] _id=6ab6731c485cab4c95548419 ts=2026-09-25T13:11:56.6020000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1495] _id=6ab675a6485cab4c9554c48e ts=2026-09-25T13:22:46.5240000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.040s..0.045s shown 
  - Evidence: 40ms: 6aa413b141b41dbac0c7f1f6.jsonl[1420] _id=6ab6748a485cab4c9554a415 ts=2026-09-25T13:18:02.5610000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1416] _id=6ab6748a485cab4c9554a41b ts=2026-09-25T13:18:02.6010000Z; 43ms: 6aa413b141b41dbac0c7f1f6.jsonl[1436] _id=6ab674b6485cab4c9554abf7 ts=2026-09-25T13:18:46.7210000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1444] _id=6ab674b6485cab4c9554abfb ts=2026-09-25T13:18:46.7640000Z; 45ms: 6aa413b141b41dbac0c7f1f6.jsonl[1426] _id=6ab6748e485cab4c9554a4a9 ts=2026-09-25T13:18:06.2630000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1427] _id=6ab6748e485cab4c9554a4ad ts=2026-09-25T13:18:06.3080000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 13 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa413b141b41dbac0c7f1f6.jsonl[7922] _id=6abe5ea3485cab4c95a527ec ts=2026-10-01T13:22:43.4420000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8229] _id=6ac39f64de269131f9a840ba ts=2026-10-05T13:00:20.5160000Z; 71h 40m: 6aa413b141b41dbac0c7f1f6.jsonl[1620] _id=6ab676dd485cab4c9554f5d2 ts=2026-09-25T13:27:57.2480000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1659] _id=6aba66c7485cab4c9567a69f ts=2026-09-28T13:08:23.6740000Z; 24h 25m: 6aa413b141b41dbac0c7f1f6.jsonl[9975] _id=6ac4f175de269131f9b008d9 ts=2026-10-06T13:02:45.1200000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10784] _id=6ac64908de269131f9b91f5d ts=2026-10-07T13:28:40.2710000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 15 gap(s), longest 95h 37m 
  - Evidence: 95h 37m: 6aa413b141b41dbac0c7f1f6.jsonl[7923] _id=6abe5ea3485cab4c95a527d2 ts=2026-10-01T13:22:43.4410000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8228] _id=6ac39f64de269131f9a840b8 ts=2026-10-05T13:00:20.5150000Z; 71h 40m: 6aa413b141b41dbac0c7f1f6.jsonl[1619] _id=6ab676dd485cab4c9554f5ce ts=2026-09-25T13:27:57.2470000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1658] _id=6aba66c7485cab4c9567a69b ts=2026-09-28T13:08:23.6720000Z; 24h 7m: 6aa413b141b41dbac0c7f1f6.jsonl[747] _id=6ab51dab485cab4c954fc49d ts=2026-09-24T12:55:06.9910000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1207] _id=6ab67109485cab4c95545e37 ts=2026-09-25T13:03:05.4950000Z
- **INFO / Info** `gameWindowFocusEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1f6.jsonl[9960] _id=6ac4ed0ade269131f9affa84 ts=2026-10-06T12:43:55.2560000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[9972] _id=6ac4ed1ede269131f9affa86 ts=2026-10-06T12:43:55.256Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 8 gap(s), longest 117h 32m 
  - Evidence: 117h 32m: 6aa413b141b41dbac0c7f1f6.jsonl[6769] _id=6abd3257485cab4c958d31c4 ts=2026-09-30T16:01:27.4810000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[9693] _id=6ac3a755de269131f9a952d3 ts=2026-10-05T13:34:13.6310000Z; 47h 50m: 6aa413b141b41dbac0c7f1f6.jsonl[2997] _id=6aba68ec485cab4c9567caad ts=2026-09-28T13:17:32.3130000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[5332] _id=6abd09a6485cab4c958695b9 ts=2026-09-30T13:07:50.2040000Z; 24h 6m: 6aa413b141b41dbac0c7f1f6.jsonl[10645] _id=6ac4f8d9de269131f9b0cfcf ts=2026-10-06T13:34:17.5320000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[11086] _id=6ac64be0de269131f9b9cb0e ts=2026-10-07T13:40:48.5770000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 95h 22m 
  - Evidence: 95h 22m: 6aa413b141b41dbac0c7f1f6.jsonl[8188] _id=6abe6256485cab4c95a6511d ts=2026-10-01T13:38:30.9180000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[8231] _id=6ac39f73de269131f9a84128 ts=2026-10-05T13:00:34.8410000Z; 71h 44m: 6aa413b141b41dbac0c7f1f6.jsonl[1599] _id=6ab67666485cab4c9554e41d ts=2026-09-25T13:25:58.3880000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1686] _id=6aba674d485cab4c9567afff ts=2026-09-28T13:10:37.3160000Z; 24h 19m: 6aa413b141b41dbac0c7f1f6.jsonl[10050] _id=6ac4f31dde269131f9b02075 ts=2026-10-06T13:09:49.6090000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[10787] _id=6ac64918de269131f9b9230b ts=2026-10-07T13:28:55.7990000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.001s..0.004s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1f6.jsonl[1141] _id=6ab52482485cab4c9550cffd ts=2026-09-24T13:24:18.2210000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[1144] _id=6ab52482485cab4c9550d003 ts=2026-09-24T13:24:18.2220000Z; 4ms: 6aa413b141b41dbac0c7f1f6.jsonl[6625] _id=6abd3229485cab4c958d2dee ts=2026-09-30T16:00:39.4430000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[6626] _id=6abd3229485cab4c958d2df2 ts=2026-09-30T16:00:39.4470000Z; 4ms: 6aa413b141b41dbac0c7f1f6.jsonl[6817] _id=6abe58df485cab4c95a4063b ts=2026-10-01T12:58:06.0960000Z -> 6aa413b141b41dbac0c7f1f6.jsonl[6805] _id=6abe58df485cab4c95a4063d ts=2026-10-01T12:58:06.1000000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 7 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1125] _id=6ab52460485cab4c9550c7c2 ts=2026-09-24T13:23:44.4580000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[5303] _id=6abd0954485cab4c958690af ts=2026-09-30T13:06:28.8260000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[6541] _id=6abd1157485cab4c9588f027 ts=2026-09-30T13:40:39.5280000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 68 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[2375] _id=6aba6866485cab4c9567c281 ts=2026-09-28T13:15:16.6010000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[2402] _id=6aba6872485cab4c9567c31b ts=2026-09-28T13:15:28.8850000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[2479] _id=6aba6891485cab4c9567c48f ts=2026-09-28T13:15:59.6010000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 172 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1759] _id=6aba67cf485cab4c9567b8cd ts=2026-09-28T13:12:46.1170000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1768] _id=6aba67d0485cab4c9567b8cf ts=2026-09-28T13:12:46.2130000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1785] _id=6aba67d0485cab4c9567b8df ts=2026-09-28T13:12:46.3130000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1416] _id=6ab6748a485cab4c9554a41b ts=2026-09-25T13:18:02.6010000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 7 records 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1662] _id=6aba66e9485cab4c9567a82d ts=?`; `6aa413b141b41dbac0c7f1f6.jsonl[4725] _id=6abbb7ef485cab4c957c230c ts=?`; `6aa413b141b41dbac0c7f1f6.jsonl[5189] _id=6abd07df485cab4c958679d3 ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 412 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[2410] _id=6aba6874485cab4c9567c35f ts=2026-09-28T13:15:30.8000000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[2452] _id=6aba6876485cab4c9567c37d ts=2026-09-28T13:15:33.0370000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[2445] _id=6aba687c485cab4c9567c3cf ts=2026-09-28T13:15:38.5240000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1033 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1764] _id=6aba67ce485cab4c9567b8b5 ts=2026-09-28T13:12:45.8080000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1756] _id=6aba67cf485cab4c9567b8bd ts=2026-09-28T13:12:45.8080000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1765] _id=6aba67cf485cab4c9567b8c3 ts=2026-09-28T13:12:45.8080000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[1401] _id=6ab67434485cab4c9554987b ts=2026-09-25T13:16:36.8780000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1417] _id=6ab67485485cab4c9554a399 ts=2026-09-25T13:17:57.5530000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[1454] _id=6ab674e8485cab4c9554af8d ts=2026-09-25T13:19:36.8400000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 18 unmatched 'DialogueStartEvent' (totals: 213 start, 202 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 109 unmatched 'BecameCameraCentered' (totals: 581 open, 540 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 137 unmatched 'BecameVisible' (totals: 1335 open, 1370 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 4 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 33 start, 20 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 231 of 11086 adjacent _id pairs reverse in client time; worst 5050.9s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1f6.jsonl[6769] _id=6abd3257485cab4c958d31c4 ts=2026-09-30T16:01:27.4810000Z`; `6aa413b141b41dbac0c7f1f6.jsonl[6807] _id=6abe58d6485cab4c95a405d1 ts=2026-09-30T14:37:16.604Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.04s, min -80442.24s, max +0.77s over 11087 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1f6\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 7 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **NOT_TESTED / NotTested** `SolarStillDesignEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **NOT_TESTED / NotTested** `TerasGardenBox` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **NOT_TESTED / NotTested** `WaterChamberEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/water-chamber-event-investigation.md
- **NOT_TESTED / NotTested** `soilMachine` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md

## 9. Event-Type Details

### `PuzzlePieceVisibleEvent` — 3826 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3826)
- **Intervals:** median 0.04s (p5 0.00s / p95 1.02s, n=3825)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3826/3826 records)
    "BecameInvisible"  x1370
    "BecameVisible"  x1335
    "BecameCameraCentered"  x581
    "BecameCameraUncentered"  x540
data.pieceId  (string, 3826/3826 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3826/3826 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 3735 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 3 Dev (2140); Unit 2 Prod (Refactor) (1005); Unit 1 Dev (590)
- **Intervals:** median 0.91s (p5 0.09s / p95 8.61s, n=3734)
- **Fields under `data`:**

```text
data.Value  (string, 3735/3735 records)
    "pressed"  x3735
data.actionType  (string, 3735/3735 records)
    "Move"  x3150
    "Interact"  x350
    "Ascend"  x98
    "Jump"  x48
    "Hoverboard"  x30
    "Sprint"  x27
    "Descend"  x19
    "Map"  x8
    "ToggleDebug"  x5
data.key  (string, 3735/3735 records, 20 empty-string)
    17 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 3735/3735 records)
    "Drone"  x1978
    "Player"  x1757
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1956 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (812); Unit 3 Dev (593); Unit 1 Dev (551)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.03s, n=1953)
- **Fields under `data`:**

```text
data.position  (object, 1956/1956 records)
data.position.x  (number, 1956/1956 records)
    numeric range -18.6835 .. 1435.23 (456 unique)
data.position.y  (number, 1956/1956 records)
    numeric range -115.527 .. 161.521 (372 unique)
data.position.z  (number, 1956/1956 records)
    numeric range -391.943 .. 1910.56 (457 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1122 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (480); Unit 3 Dev (348); Unit 1 Dev (294)
- **eventKey:** present on 707 of 1122 records
- **Intervals:** median 6.24s (p5 0.01s / p95 86.21s, n=1121)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x707; [conversationId, dialogueEventType] x415
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1122/1122 records)
    numeric range 10 .. 101 (22 unique)
data.dialogueEventType  (string, 1122/1122 records)
    "DialogueNodeEvent"  x707
    "DialogueStartEvent"  x213
    "DialogueFinishEvent"  x202
data.nodeId  (number, 707/1122 records)
    numeric range 0 .. 289 (152 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 94 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 2 Prod (Refactor) (56); Unit 1 Dev (32); Unit 3 Dev (6)
- **Intervals:** median 9.55s (p5 0.21s / p95 84739.50s, n=93)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 94/94 records)
    14 unique values (see csv/event_unique_values.csv)
data.objectName  (string, 94/94 records)
    33 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 81 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (81)
- **Intervals:** median 0.26s (p5 0.05s / p95 10.06s, n=80)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 81/81 records)
    "argumentationNodeHoverEnd"  x34
    "argumentationNodeHoverStart"  x33
    "argumentationNodeAdd"  x8
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 81/81 records)
    "Unit 1 - Freshwater"  x81
data.nodeName  (string, 81/81 records)
    "1"  x25
    "A"  x25
    "II"  x16
    "I"  x15
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `TopographicMapEvent` — 58 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (36); Unit 2 Prod (Refactor) (22)
- **Intervals:** median 17.21s (p5 1.30s / p95 85383.45s, n=57)
- **`data` key-set variants:** [actionType, featureUsed] x46; [actionType, featureUsed, location] x12
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 58/58 records)
    "MapCloseEvent"  x23
    "MapOpenEvent"  x23
    "WaypointMoveEvent"  x7
    "WaypointSetEvent"  x4
    "WaypointResetEvent"  x1
data.featureUsed  (string, 58/58 records)
    "Map"  x46
    "Waypoint"  x12
data.location  (object, 12/58 records)
data.location.x  (number, 12/58 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 12/58 records)
    5 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 12/58 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `questEvent` — 53 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (20); Unit 2 Prod (Refactor) (20); Unit 3 Dev (13)
- **eventKey:** present on 53 of 53 records
- **Intervals:** median 393.31s (p5 0.01s / p95 86327.10s, n=52)
- **`data` key-set variants:** [questEventType, questID, questName] x33; [questEventType, questID, questName, questSuccessOrFailure] x20
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 53/53 records)
    "questActiveEvent"  x33
    "questFinishEvent"  x20
data.questID  (string, 53/53 records)
    "16"  x10
    "24"  x9
    "22"  x5
    "32"  x5
    "23"  x4
    "29"  x4
    "31"  x4
    "17"  x3
    "33"  x3
    "21"  x2
    "28"  x2
    "34"  x2
data.questName  (string, 53/53 records)
    "Supply Run"  x10
    "Investigate the Temple"  x9
    "Getting the Band Back Together"  x5
    "Info and Intros"  x5
    "Foraged Forging"  x4
    "Gear Up"  x4
    "TK, Reporting In!"  x4
    "Defend the Expedition"  x3
    "Pollution Solution"  x3
    "Escape the Ruin"  x2
    "Getting Your Space Legs"  x2
    "What Was That?"  x2
data.questSuccessOrFailure  (string, 20/53 records)
    "Succeeded"  x20
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Soil Key Puzzle` — 50 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (50)
- **Intervals:** median 0.69s (p5 0.32s / p95 10.08s, n=49)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x46; [Soil Key Puzzle Status, Unit] x4
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 4/50 records)
    "Finished"  x2
    "Started"  x2
data.Unit  (string, 4/50 records)
    "Unit 2 Prod (Refactor)"  x4
data.actionType  (string, 46/50 records)
    "RightDrag"  x25
    "LeftDrag"  x21
data.currentSoilType  (string, 46/50 records)
    "CLAYSAND"  x11
    "CLAY"  x9
    "SAND"  x9
    "CLAYROCK"  x8
    "SANDGRAVEL"  x4
    "BEDROCK"  x3
    "GRAVEL"  x2
data.isCorrectSelection  (string, 46/50 records)
    "false"  x34
    "true"  x12
data.waterLevelStatus  (string, 46/50 records)
    "Proper"  x22
    "TooHigh"  x20
    "TooLow"  x4
data.waterRetentionChange  (string, 46/50 records)
    "Increase"  x22
    "Decrease"  x12
    "NoChange"  x12
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationAnswerEvent` — 27 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 1 Dev (27)
- **Intervals:** median 1.09s (p5 0.22s / p95 164.79s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "submitAnswerEvent"  x27
data.answerSubmitted  (string, 27/27 records, 22 empty-string)
    ""  x22
    "A,1,II"  x4
    "A,1,I"  x1
data.argumentationTitle  (string, 27/27 records)
    "Unit 1 - Freshwater"  x26
    "Unit 1 - Argumentation Tutorial"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `gameWindowFocusEvent` — 25 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Unit 3 Dev (7); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 1521.23s (p5 11.49s / p95 232354.24s, n=24)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 25/25 records)
    true  x25
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 17 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (6); Unit 1 Dev (3); MainMenu (1)
- **Intervals:** median 80385.19s (p5 96.89s / p95 279596.05s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "DebugMenuStateChanged"  x17
data.isOpened  (bool, 17/17 records)
    false  x17
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 16 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (16)
- **Intervals:** median 85318.75s (p5 201.08s / p95 283895.62s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowUnfocusEvent` — 13 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 3 Dev (9); Unit 2 Prod (Refactor) (4)
- **Intervals:** median 3301.52s (p5 21.30s / p95 285144.61s, n=12)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 13/13 records)
    false  x13
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `argumentationToolEvent` — 7 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 1 Dev (7)
- **Intervals:** median 40.34s (p5 1.33s / p95 171.21s, n=6)
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

### `crash` — 7 records

- **Scenes:** <missing sceneName> (7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 7/7 records)
    true  x7
data.message  (string, 7/7 records)
    "Permissions check failed"  x5
    "A user gesture is required to request Pointer Lock."  x1
    "not granted"  x1
data.phase  (string, 7/7 records)
    "running"  x7
data.stack  (string, 7/7 records, 1 empty-string)
    "TypeError: Permissions check failed"  x5
    ""  x1
    "TypeError: not granted"  x1
data.type  (string, 7/7 records)
    "unhandled_rejection"  x7
data.unitId  (string, 7/7 records)
    "unit2"  x4
    "unit3"  x3
data.workspace  (string, 7/7 records)
    "mhs"  x7
```

Raw examples: `event_examples.json` -> `crash`.

### `argumentationEvent` — 6 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (6)
- **Intervals:** median 164.11s (p5 51.19s / p95 68309.81s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 6/6 records)
    "argumentationSessionClose"  x3
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 6/6 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 6/6 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

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
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially
- `argumentationEvent` : median interval between records changed substantially
- `argumentationToolEvent` : median interval between records changed substantially
- `chatEvent` : event type present in baseline 09-23-26 but absent now
- `gameStartEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (50 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (7x); "WaypointResetEvent" (1x); "WaypointSetEvent" (4x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (12x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*