# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1fb

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county-129users / 6aa413b141b41dbac0c7f1fb
- **Game version string(s) in log:** 2.8.1, 20260914-, 20261005-12466
- **Audit date:** 2026-10-25
- **Log file(s):** 6aa413b141b41dbac0c7f1fb.jsonl
- **Records:** 9188 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6aa413b141b41dbac0c7f1fb
- **Time span:** 2026-09-23T13:06:29.403000+00:00 .. 2026-10-07T13:40:22.936000+00:00 (336h 33m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1fb\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **17 event types**, 9188 records, 5 scenes.
- Findings: **0 FAIL**, **38 WARNING**, 71 INFO, 5 NOT_TESTED, 61 PASS.
- Top items needing attention:
  - WARNING/Medium `EndOfUnit`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `PuzzlePieceVisibleEvent`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `crash`: exact duplicate records (same timestamp, scene and data)
  - WARNING/Medium `DEBUGMenu`: median interval between records changed substantially
  - WARNING/Medium `EndOfUnit`: event type present in baseline 09-23-26 but absent now
  - WARNING/Medium `InputEvent`: median interval between records changed substantially
  - WARNING/Medium `SolarStillDesignEvent`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3752 | 40.84 | 1 | 1 | 0 | 2026-09-25T13:20:13.171000+00:00 | 2026-10-01T13:03:39.176000+00:00 | 143h 43m |
| InputEvent | 2025 | 22.04 | 1 | 3 | 0 | 2026-09-23T13:11:26.801000+00:00 | 2026-10-07T13:38:50.258000+00:00 | 336h 27m |
| PlayerPositionEvent | 1701 | 18.51 | 1 | 3 | 0 | 2026-09-23T13:06:40.640000+00:00 | 2026-10-07T13:40:22.936000+00:00 | 336h 33m |
| DialogueEvent | 1103 | 12.0 | 1 | 3 | 738 | 2026-09-23T13:07:02.815000+00:00 | 2026-10-07T13:38:47.884000+00:00 | 336h 31m |
| ObjectInterEvent | 237 | 2.58 | 1 | 3 | 0 | 2026-09-23T13:19:59.685000+00:00 | 2026-10-07T13:38:55.055000+00:00 | 336h 18m |
| argumentationNodeEvent | 158 | 1.72 | 1 | 2 | 0 | 2026-10-01T13:33:39.915000+00:00 | 2026-10-07T13:34:44.373000+00:00 | 144h 1m |
| Soil Key Puzzle | 57 | 0.62 | 1 | 2 | 0 | 2026-09-29T13:23:08.867000+00:00 | 2026-10-07T13:40:11.230000+00:00 | 192h 17m |
| questEvent | 43 | 0.47 | 1 | 3 | 43 | 2026-09-23T13:07:02.790000+00:00 | 2026-10-07T13:35:59.042000+00:00 | 336h 28m |
| TopographicMapEvent | 33 | 0.36 | 1 | 2 | 0 | 2026-09-25T13:21:30.974000+00:00 | 2026-10-06T13:30:53.423000+00:00 | 264h 9m |
| gameWindowFocusEvent | 18 | 0.2 | 1 | 3 | 0 | 2026-09-23T13:06:29.403000+00:00 | 2026-10-07T13:16:58.339000+00:00 | 336h 10m |
| DEBUGMenu | 17 | 0.19 | 1 | 4 | 0 | 2026-09-23T13:06:40.630000+00:00 | 2026-10-07T13:17:05.966000+00:00 | 336h 10m |
| gameStartEvent | 16 | 0.17 | 1 | 1 | 0 | 2026-09-23T13:06:29.404000+00:00 | 2026-10-07T13:16:58.339000+00:00 | 336h 10m |
| argumentationAnswerEvent | 12 | 0.13 | 1 | 2 | 0 | 2026-10-01T13:33:57.306000+00:00 | 2026-10-07T13:34:46.709000+00:00 | 144h 0m |
| argumentationEvent | 5 | 0.05 | 1 | 2 | 0 | 2026-10-01T13:33:32.508000+00:00 | 2026-10-07T13:34:46.757000+00:00 | 144h 1m |
| crash | 5 | 0.05 | 1 | 1 | 0 |  |  | ? |
| gameWindowUnfocusEvent | 4 | 0.04 | 1 | 3 | 0 | 2026-09-23T13:25:27.576000+00:00 | 2026-10-01T14:49:00.514000+00:00 | 193h 23m |
| DaniEvent | 2 | 0.02 | 1 | 1 | 0 | 2026-10-06T13:11:49.117000+00:00 | 2026-10-06T13:11:53.232000+00:00 | 4.1s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — median interval between records changed substantially. 
  - Observed: 6632.224s median 
  - Expected: 795.292s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 2.151s median 
  - Expected: 0.583s in 09-23-26 
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
  - Observed: 20.316s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — median interval between records changed substantially. 
  - Observed: 14.691s median 
  - Expected: 3024.27s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — median interval between records changed substantially. 
  - Observed: 6853.853s median 
  - Expected: 2479.84s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowFocusEvent` — median interval between records changed substantially. 
  - Observed: 6411.722s median 
  - Expected: 95.83s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `gameWindowUnfocusEvent` — median interval between records changed substantially. 
  - Observed: 86114.058s median 
  - Expected: 108.82s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 326.832s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `DaniEvent` — event type not present in baseline 09-23-26. 
  - Observed: 2 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; leftArrow; rightArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Open Locker; Press E to Pick Up; Press E to Pickup Canister; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Press [E/Action button] to enter escape pod  
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PuzzlePieceVisibleEvent` `data.pieceId` — baseline categorical value(s) not seen this build. 
  - Observed: Dissolving Particles Piece 1; Dissolving Particles Piece 2; Dissolving Particles Piece 3; Dissolving Particles Slot 2; Dissolving Particles Slot 3; Evaporation Puzzle Piece A; Evaporation Puzzle Piece B; Evaporation Puzzle Piece C; Evaporation Puzzle Piece D; Evaporation Puzzle Slot A; Evaporation Puzzle Slot B; Evaporation Puzzle Slot C; Evaporation Puzzle Slot D; Soil Infiltration Puzzle Piece Bedrock; Soil Infiltration Puzzle Piece Clay; Soil Infiltration Puzzle Piece Gravel; Soil Infiltration Puzzle Piece Sand; Soil Infiltration Puzzle Slot Bedrock; Soil Infiltration Puzzle Slot Clay; Soil Infiltration Puzzle Slot Gravel; Soil Infiltration Puzzle Slot Sand 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Selected; Unselected; WaypointResetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — baseline categorical value(s) not seen this build. 
  - Observed: A,1,I; A,C,D,2,II; D,C,3,II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationAnswerEvent` `data.answerSubmitted` — categorical value(s) not seen in baseline. 
  - Observed: 1,; B,1,I; B,1,II; B,C,1,II; C,1,II; D,1,II 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationAnswerEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit; Unit 1 - Does the planet WAT-247 have freshwater; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 1 - Freshwater; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 1 - Freshwater; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 5 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowUnfocusEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 4 records 
  - Expected: 76 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 31; 32; 33; 34; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Defend the Expedition; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Info and Intros; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; TK, Reporting In!; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; What Was That? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 11 mismatch(es); e.g. 'DialogueNodeEvent:20:111' vs expected 'DialogueNodeEvent:20:33' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[5334] _id=6abd09fe485cab4c95869c50 ts=2026-09-30T13:09:18.1450000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[5394] _id=6abd0ae9485cab4c9586acf5 ts=2026-09-30T13:13:13.0220000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[7384] _id=6abe5c70485cab4c95a47ca5 ts=2026-10-01T13:13:20.6710000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'questActiveEvent:22' vs expected 'questActiveEvent:24' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[6368] _id=6abd22af485cab4c958b8f5f ts=2026-09-30T14:54:39.2700000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[6516] _id=6abe5893485cab4c95a4030b ts=2026-10-01T12:56:49.3840000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 16 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 16} 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[8] _id=6ab3ced5485cab4c954b85be ts=2026-09-23T13:06:29.4040000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[406] _id=6ab3d356485cab4c954c0ca4 ts=2026-09-23T13:25:42.4530000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[598] _id=6ab51dbb485cab4c954fc75f ts=2026-09-24T12:55:24.1420000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 18 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 18} 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[7] _id=6ab3ced5485cab4c954b85bc ts=2026-09-23T13:06:29.4030000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[407] _id=6ab3d356485cab4c954c0c9d ts=2026-09-23T13:25:42.4520000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[599] _id=6ab51dbb485cab4c954fc759 ts=2026-09-24T12:55:24.1400000Z`
- **WARNING / Low** `gameWindowUnfocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 4 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 4} 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[405] _id=6ab3d347485cab4c954c0af8 ts=2026-09-23T13:25:27.5760000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1051] _id=6ab523a9485cab4c955097d5 ts=2026-09-24T13:20:41.6340000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[6513] _id=6abe5885485cab4c95a4029f ts=2026-10-01T12:56:37.1590000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PuzzlePieceVisibleEvent | 3751 | 0.0 | 0.033 | 137.938 | 1.56 | 344556.716 | 0.43 | 2182 | 4 |
| InputEvent | 2024 | 0.0 | 2.151 | 598.44 | 26.253 | 430111.048 | 0.1 | 13 | 9 |
| PlayerPositionEvent | 1698 | 9.712 | 10.0 | 713.509 | 10.023 | 425473.011 | 0.08 | 0 | 9 |
| DialogueEvent | 1102 | 0.001 | 4.921 | 1099.369 | 64.513 | 425541.746 | 0.05 | 291 | 12 |
| ObjectInterEvent | 236 | 0.132 | 5.849 | 5130.235 | 315.148 | 431994.54 | 0.01 | 0 | 9 |
| argumentationNodeEvent | 157 | 0.02 | 0.391 | 3302.321 | 7.568 | 518260.214 | 0.02 | 29 | 1 |
| Soil Key Puzzle | 56 | 0.208 | 0.773 | 12361.114 | 13.292 | 605681.221 | 0.0 | 0 | 2 |
| questEvent | 42 | 0.003 | 326.832 | 28841.339 | 85148.46 | 425588.942 | 0.0 | 2 | 17 |
| TopographicMapEvent | 32 | 0.02 | 20.316 | 29717.577 | 202804.332 | 431308.705 | 0.0 | 3 | 6 |
| gameWindowFocusEvent | 17 | 2.822 | 6411.722 | 71189.937 | 361208.412 | 425477.909 | 0.0 | 0 | 12 |
| DEBUGMenu | 16 | 8.116 | 6632.224 | 75639.083 | 365253.845 | 425583.729 | 0.0 | 0 | 12 |
| gameStartEvent | 15 | 221.071 | 6853.853 | 80681.929 | 369273.923 | 425584.029 | 0.0 | 0 | 12 |
| argumentationAnswerEvent | 11 | 3.331 | 14.691 | 47131.764 | 259171.013 | 518315.647 | 0.0 | 0 | 1 |
| argumentationEvent | 4 | 0.022 | 105.691 | 129618.562 | 440547.205 | 518262.844 | 0.0 | 1 | 1 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameWindowUnfocusEvent | 3 | 6743.355 | 86114.058 | 232070.979 | 551631.378 | 603355.525 | 0.0 | 0 | 3 |
| DaniEvent | 1 | 4.115 | 4.115 | 4.115 | 4.115 | 4.115 | 14.58 | 0 | 0 |

- **WARNING / Medium** `InputEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[2947] _id=6abbb826485cab4c957c2586 ts=2026-09-29T13:07:50.3500000Z == 6aa413b141b41dbac0c7f1fb.jsonl[2945] _id=6abbb826485cab4c957c2588 ts=2026-09-29T13:07:50.3500000Z`
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 129 group(s), 175 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[1697] _id=6ab67528485cab4c9554b612 ts=2026-09-25T13:20:39.5290000Z == 6aa413b141b41dbac0c7f1fb.jsonl[1704] _id=6ab67528485cab4c9554b616 ts=2026-09-25T13:20:39.5290000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1688] _id=6ab6753d485cab4c9554b806 ts=2026-09-25T13:21:01.1340000Z == 6aa413b141b41dbac0c7f1fb.jsonl[1727] _id=6ab6753e485cab4c9554b80a ts=2026-09-25T13:21:01.1340000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1743] _id=6ab67540485cab4c9554b854 ts=2026-09-25T13:21:04.2530000Z == 6aa413b141b41dbac0c7f1fb.jsonl[1745] _id=6ab67540485cab4c9554b85b ts=2026-09-25T13:21:04.2530000Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[369] _id=6ab3d314485cab4c954c055c ts=? == 6aa413b141b41dbac0c7f1fb.jsonl[944] _id=6ab5228f485cab4c95505fcb ts=?`; `6aa413b141b41dbac0c7f1fb.jsonl[2948] _id=6abbb826485cab4c957c257c ts=? == 6aa413b141b41dbac0c7f1fb.jsonl[5182] _id=6abd07f3485cab4c95867a97 ts=?`
- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 86 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `694ms: 6aa413b141b41dbac0c7f1fb.jsonl[238] _id=6ab3d201485cab4c954be174 ts=2026-09-23T13:20:01.3250000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[240] _id=6ab3d202485cab4c954be188 ts=2026-09-23T13:20:02.0190000Z`; `294ms: 6aa413b141b41dbac0c7f1fb.jsonl[240] _id=6ab3d202485cab4c954be188 ts=2026-09-23T13:20:02.0190000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[228] _id=6ab3d202485cab4c954be194 ts=2026-09-23T13:20:02.3130000Z`; `294ms: 6aa413b141b41dbac0c7f1fb.jsonl[228] _id=6ab3d202485cab4c954be194 ts=2026-09-23T13:20:02.3130000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[234] _id=6ab3d202485cab4c954be1a4 ts=2026-09-23T13:20:02.6070000Z`
- **INFO / Info** `PuzzlePieceVisibleEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 534 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `17ms: 6aa413b141b41dbac0c7f1fb.jsonl[1705] _id=6ab67528485cab4c9554b622 ts=2026-09-25T13:20:39.5370000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[1706] _id=6ab67528485cab4c9554b624 ts=2026-09-25T13:20:39.5540000Z`; `16ms: 6aa413b141b41dbac0c7f1fb.jsonl[1832] _id=6ab675a2485cab4c9554c414 ts=2026-09-25T13:20:47.5800000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[1837] _id=6ab675a2485cab4c9554c418 ts=2026-09-25T13:20:47.5960000Z`; `20ms: 6aa413b141b41dbac0c7f1fb.jsonl[1800] _id=6ab67594485cab4c9554c28a ts=2026-09-25T13:22:27.7960000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[1801] _id=6ab67594485cab4c9554c28e ts=2026-09-25T13:22:27.8160000Z`
- **INFO / Info** `TopographicMapEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `24ms: 6aa413b141b41dbac0c7f1fb.jsonl[5390] _id=6abd0ae9485cab4c9586acfb ts=2026-09-30T13:13:13.0300000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[5397] _id=6abd0ae9485cab4c9586ad00 ts=2026-09-30T13:13:13.0540000Z`; `20ms: 6aa413b141b41dbac0c7f1fb.jsonl[5397] _id=6abd0ae9485cab4c9586ad00 ts=2026-09-30T13:13:13.0540000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[5396] _id=6abd0ae9485cab4c9586ad19 ts=2026-09-30T13:13:13.0740000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `22ms: 6aa413b141b41dbac0c7f1fb.jsonl[9037] _id=6ac64a76de269131f9b9834c ts=2026-10-07T13:34:46.7350000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[9040] _id=6ac64a76de269131f9b9834f ts=2026-10-07T13:34:46.7570000Z`
- **INFO / Info** `argumentationNodeEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 17 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `43ms: 6aa413b141b41dbac0c7f1fb.jsonl[7834] _id=6abe6139485cab4c95a5fe51 ts=2026-10-01T13:33:45.1680000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[7835] _id=6abe6139485cab4c95a5fe61 ts=2026-10-01T13:33:45.2110000Z`; `407ms: 6aa413b141b41dbac0c7f1fb.jsonl[7843] _id=6abe613f485cab4c95a5ffe5 ts=2026-10-01T13:33:51.3530000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[7845] _id=6abe613f485cab4c95a60005 ts=2026-10-01T13:33:51.7600000Z`; `810ms: 6aa413b141b41dbac0c7f1fb.jsonl[7844] _id=6abe613f485cab4c95a5fff5 ts=2026-10-01T13:33:51.5590000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[7838] _id=6abe6140485cab4c95a60028 ts=2026-10-01T13:33:52.3690000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `3ms: 6aa413b141b41dbac0c7f1fb.jsonl[6368] _id=6abd22af485cab4c958b8f5f ts=2026-09-30T14:54:39.2700000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[6376] _id=6abd22af485cab4c958b8f61 ts=2026-09-30T14:54:39.2730000Z`; `3ms: 6aa413b141b41dbac0c7f1fb.jsonl[6516] _id=6abe5893485cab4c95a4030b ts=2026-10-01T12:56:49.3840000Z ~ 6aa413b141b41dbac0c7f1fb.jsonl[6517] _id=6abe5893485cab4c95a4030d ts=2026-10-01T12:56:49.3870000Z`
- **INFO / Info** `DEBUGMenu` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 118h 13m 
  - Evidence: 118h 13m: 6aa413b141b41dbac0c7f1fb.jsonl[8105] _id=6abe727b485cab4c95a95274 ts=2026-10-01T14:47:23.2290000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8135] _id=6ac4f0eade269131f9b00097 ts=2026-10-06T13:00:26.9580000Z; 95h 52m: 6aa413b141b41dbac0c7f1fb.jsonl[1574] _id=6ab673e8485cab4c95549085 ts=2026-09-25T13:15:20.6630000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2944] _id=6abbb820485cab4c957c2526 ts=2026-09-29T13:07:44.5460000Z; 24h 12m: 6aa413b141b41dbac0c7f1fb.jsonl[8164] _id=6ac4f1d1de269131f9b00c3a ts=2026-10-06T13:04:17.5290000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8640] _id=6ac64649de269131f9b8bfab ts=2026-10-07T13:16:57.8500000Z
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 118h 12m 
  - Evidence: 118h 12m: 6aa413b141b41dbac0c7f1fb.jsonl[8117] _id=6abe72ab485cab4c95a9591a ts=2026-10-01T14:48:11.1150000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8134] _id=6ac4f0f1de269131f9b000c3 ts=2026-10-06T13:00:32.8610000Z; 95h 39m: 6aa413b141b41dbac0c7f1fb.jsonl[2927] _id=6ab67730485cab4c955504dc ts=2026-09-25T13:29:21.0500000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2958] _id=6abbb84c485cab4c957c2812 ts=2026-09-29T13:08:28.8730000Z; 23h 38m: 6aa413b141b41dbac0c7f1fb.jsonl[8639] _id=6ac4fa3dde269131f9b111fb ts=2026-10-06T13:40:13.7430000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8667] _id=6ac646cdde269131f9b8c2a7 ts=2026-10-07T13:19:09.4910000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 291 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 6aa413b141b41dbac0c7f1fb.jsonl[5224] _id=6abd0859485cab4c95868403 ts=2026-09-30T13:02:16.7400000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5225] _id=6abd0859485cab4c95868405 ts=2026-09-30T13:02:16.7410000Z; 1ms: 6aa413b141b41dbac0c7f1fb.jsonl[6259] _id=6abd101f485cab4c95889833 ts=2026-09-30T13:35:27.1810000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[6266] _id=6abd101f485cab4c95889841 ts=2026-09-30T13:35:27.1820000Z; 1ms: 6aa413b141b41dbac0c7f1fb.jsonl[6309] _id=6abd105e485cab4c9588ae82 ts=2026-09-30T13:36:30.0580000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[6324] _id=6abd105e485cab4c9588ae8d ts=2026-09-30T13:36:30.0590000Z
- **INFO / Info** `InputEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 28m 
  - Evidence: 119h 28m: 6aa413b141b41dbac0c7f1fb.jsonl[8051] _id=6abe627e485cab4c95a65d89 ts=2026-10-01T13:39:10.3620000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8205] _id=6ac4f29dde269131f9b01b65 ts=2026-10-06T13:07:41.4100000Z; 95h 37m: 6aa413b141b41dbac0c7f1fb.jsonl[2939] _id=6ab67750485cab4c9555099c ts=2026-09-25T13:29:53.1090000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2951] _id=6abbb826485cab4c957c2584 ts=2026-09-29T13:07:50.3490000Z; 23h 40m: 6aa413b141b41dbac0c7f1fb.jsonl[8611] _id=6ac4f9a9de269131f9b0f819 ts=2026-10-06T13:37:45.4350000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8659] _id=6ac646afde269131f9b8c1fc ts=2026-10-07T13:18:39.9190000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.000s..0.001s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fb.jsonl[2947] _id=6abbb826485cab4c957c2586 ts=2026-09-29T13:07:50.3500000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2945] _id=6abbb826485cab4c957c2588 ts=2026-09-29T13:07:50.3500000Z; 1ms: 6aa413b141b41dbac0c7f1fb.jsonl[2945] _id=6abbb826485cab4c957c2588 ts=2026-09-29T13:07:50.3500000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2952] _id=6abbb827485cab4c957c258a ts=2026-09-29T13:07:50.3510000Z; 1ms: 6aa413b141b41dbac0c7f1fb.jsonl[2951] _id=6abbb826485cab4c957c2584 ts=2026-09-29T13:07:50.3490000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2947] _id=6abbb826485cab4c957c2586 ts=2026-09-29T13:07:50.3500000Z
- **INFO / Info** `ObjectInterEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 119h 59m 
  - Evidence: 119h 59m: 6aa413b141b41dbac0c7f1fb.jsonl[7776] _id=6abe6076485cab4c95a5c1fd ts=2026-10-01T13:30:30.3630000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8490] _id=6ac4f7f0de269131f9b0af10 ts=2026-10-06T13:30:24.9030000Z; 95h 40m: 6aa413b141b41dbac0c7f1fb.jsonl[2924] _id=6ab67727485cab4c95550358 ts=2026-09-25T13:29:12.0980000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2985] _id=6abbb89d485cab4c957c31fe ts=2026-09-29T13:09:49.2510000Z; 24h 0m: 6aa413b141b41dbac0c7f1fb.jsonl[4858] _id=6abbbbbc485cab4c957cc4d6 ts=2026-09-29T13:23:08.8700000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5585] _id=6abd0d53485cab4c958751aa ts=2026-09-30T13:23:31.6570000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 9 gap(s), longest 118h 11m 
  - Evidence: 118h 11m: 6aa413b141b41dbac0c7f1fb.jsonl[8126] _id=6abe72e9485cab4c95a9616e ts=2026-10-01T14:49:13.9550000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8132] _id=6ac4f0f1de269131f9b000bf ts=2026-10-06T13:00:26.9660000Z; 95h 37m: 6aa413b141b41dbac0c7f1fb.jsonl[2941] _id=6ab6775b485cab4c95550ad1 ts=2026-09-25T13:30:03.5600000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2949] _id=6abbb826485cab4c957c2580 ts=2026-09-29T13:07:44.5510000Z; 23h 36m: 6aa413b141b41dbac0c7f1fb.jsonl[8638] _id=6ac4fa3ade269131f9b11155 ts=2026-10-06T13:40:10.9150000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8643] _id=6ac64657de269131f9b8bffa ts=2026-10-07T13:17:05.9730000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 6aa413b141b41dbac0c7f1fb.jsonl[2912] _id=6ab67707485cab4c9554fe02 ts=2026-09-25T13:28:38.7880000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[3017] _id=6abbb8f3485cab4c957c3cfe ts=2026-09-29T13:11:15.5040000Z; 24h 4m: 6aa413b141b41dbac0c7f1fb.jsonl[4831] _id=6abbbb6d485cab4c957cb26f ts=2026-09-29T13:21:48.0300000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5648] _id=6abd0df5485cab4c9587a3f3 ts=2026-09-30T13:26:12.7340000Z; 22h 1m: 6aa413b141b41dbac0c7f1fb.jsonl[6411] _id=6abd22c9485cab4c958b90e5 ts=2026-09-30T14:55:03.9530000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[6518] _id=6abe5893485cab4c95a4030f ts=2026-10-01T12:56:49.7900000Z
- **INFO / Info** `PuzzlePieceVisibleEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2182 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 6aa413b141b41dbac0c7f1fb.jsonl[1688] _id=6ab6753d485cab4c9554b806 ts=2026-09-25T13:21:01.1340000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[1727] _id=6ab6753e485cab4c9554b80a ts=2026-09-25T13:21:01.1340000Z; 0ms: 6aa413b141b41dbac0c7f1fb.jsonl[1689] _id=6ab6753e485cab4c9554b813 ts=2026-09-25T13:21:01.1340000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[1740] _id=6ab6753e485cab4c9554b81b ts=2026-09-25T13:21:01.1340000Z; 0ms: 6aa413b141b41dbac0c7f1fb.jsonl[1694] _id=6ab67528485cab4c9554b600 ts=2026-09-25T13:20:39.4060000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[1700] _id=6ab67528485cab4c9554b602 ts=2026-09-25T13:20:39.4060000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 168h 14m 
  - Evidence: 168h 14m: 6aa413b141b41dbac0c7f1fb.jsonl[5608] _id=6abd0d7d485cab4c958763d9 ts=2026-09-30T13:24:13.8300000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[9140] _id=6ac64b6fde269131f9b9b4a0 ts=2026-10-07T13:38:55.0510000Z; 24h 0m: 6aa413b141b41dbac0c7f1fb.jsonl[4864] _id=6abbbbbf485cab4c957cc584 ts=2026-09-29T13:23:11.8440000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5584] _id=6abd0d53485cab4c95875199 ts=2026-09-30T13:23:31.6530000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 119h 48m 
  - Evidence: 119h 48m: 6aa413b141b41dbac0c7f1fb.jsonl[7584] _id=6abe5ec4485cab4c95a538c3 ts=2026-10-01T13:23:16.5890000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8284] _id=6ac4f391de269131f9b024fb ts=2026-10-06T13:11:45.2940000Z; 95h 50m: 6aa413b141b41dbac0c7f1fb.jsonl[1768] _id=6ab6756b485cab4c9554bbc2 ts=2026-09-25T13:21:47.4360000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[3051] _id=6abbb91f485cab4c957c4216 ts=2026-09-29T13:11:59.0610000Z; 24h 0m: 6aa413b141b41dbac0c7f1fb.jsonl[5406] _id=6abd0b16485cab4c9586b273 ts=2026-09-30T13:13:58.0550000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[7425] _id=6abe5cca485cab4c95a48d81 ts=2026-10-01T13:14:50.9660000Z
- **INFO / Info** `TopographicMapEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.020s..0.029s shown 
  - Evidence: 20ms: 6aa413b141b41dbac0c7f1fb.jsonl[5397] _id=6abd0ae9485cab4c9586ad00 ts=2026-09-30T13:13:13.0540000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5396] _id=6abd0ae9485cab4c9586ad19 ts=2026-09-30T13:13:13.0740000Z; 24ms: 6aa413b141b41dbac0c7f1fb.jsonl[5390] _id=6abd0ae9485cab4c9586acfb ts=2026-09-30T13:13:13.0300000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5397] _id=6abd0ae9485cab4c9586ad00 ts=2026-09-30T13:13:13.0540000Z; 29ms: 6aa413b141b41dbac0c7f1fb.jsonl[5393] _id=6abd0ae9485cab4c9586acef ts=2026-09-30T13:13:13.0010000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[5390] _id=6abd0ae9485cab4c9586acfb ts=2026-09-30T13:13:13.0300000Z
- **INFO / Info** `argumentationAnswerEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 58m 
  - Evidence: 143h 58m: 6aa413b141b41dbac0c7f1fb.jsonl[7995] _id=6abe61cb485cab4c95a62679 ts=2026-10-01T13:36:11.0620000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[9036] _id=6ac64a76de269131f9b9834a ts=2026-10-07T13:34:46.7090000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 6aa413b141b41dbac0c7f1fb.jsonl[7992] _id=6abe61cb485cab4c95a62682 ts=2026-10-01T13:36:11.0920000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8986] _id=6ac64a41de269131f9b97184 ts=2026-10-07T13:33:53.9360000Z
- **INFO / Info** `argumentationEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.022s..0.022s shown 
  - Evidence: 22ms: 6aa413b141b41dbac0c7f1fb.jsonl[9037] _id=6ac64a76de269131f9b9834c ts=2026-10-07T13:34:46.7350000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[9040] _id=6ac64a76de269131f9b9834f ts=2026-10-07T13:34:46.7570000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 143h 57m 
  - Evidence: 143h 57m: 6aa413b141b41dbac0c7f1fb.jsonl[7991] _id=6abe61ca485cab4c95a62628 ts=2026-10-01T13:36:10.1830000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8981] _id=6ac64a3ede269131f9b970db ts=2026-10-07T13:33:50.3970000Z
- **INFO / Info** `argumentationNodeEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 29 interval(s) ≤ 0.020s..0.022s shown 
  - Evidence: 20ms: 6aa413b141b41dbac0c7f1fb.jsonl[8987] _id=6ac64a47de269131f9b97292 ts=2026-10-07T13:33:59.4480000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8990] _id=6ac64a47de269131f9b97297 ts=2026-10-07T13:33:59.4680000Z; 21ms: 6aa413b141b41dbac0c7f1fb.jsonl[7907] _id=6abe617f485cab4c95a60f56 ts=2026-10-01T13:34:55.2440000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[7904] _id=6abe617f485cab4c95a60f5b ts=2026-10-01T13:34:55.2650000Z; 22ms: 6aa413b141b41dbac0c7f1fb.jsonl[9010] _id=6ac64a56de269131f9b976db ts=2026-10-07T13:34:14.7410000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[9011] _id=6ac64a56de269131f9b976ec ts=2026-10-07T13:34:14.7630000Z
- **INFO / Info** `gameStartEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 118h 13m 
  - Evidence: 118h 13m: 6aa413b141b41dbac0c7f1fb.jsonl[8104] _id=6abe7274485cab4c95a9517e ts=2026-10-01T14:47:16.4500000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8130] _id=6ac4f0e4de269131f9b00063 ts=2026-10-06T13:00:20.4790000Z; 95h 52m: 6aa413b141b41dbac0c7f1fb.jsonl[1575] _id=6ab673e3485cab4c9554903d ts=2026-09-25T13:15:15.4080000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2943] _id=6abbb818485cab4c957c2498 ts=2026-09-29T13:07:36.4290000Z; 24h 12m: 6aa413b141b41dbac0c7f1fb.jsonl[8158] _id=6ac4f1c1de269131f9b00ba8 ts=2026-10-06T13:04:01.5500000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8642] _id=6ac6464ade269131f9b8bfb2 ts=2026-10-07T13:16:58.3390000Z
- **INFO / Info** `gameWindowFocusEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 118h 11m 
  - Evidence: 118h 11m: 6aa413b141b41dbac0c7f1fb.jsonl[8120] _id=6abe72de485cab4c95a95fa2 ts=2026-10-01T14:49:02.5690000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8131] _id=6ac4f0e4de269131f9b00061 ts=2026-10-06T13:00:20.4780000Z; 95h 52m: 6aa413b141b41dbac0c7f1fb.jsonl[1573] _id=6ab673e3485cab4c95549039 ts=2026-09-25T13:15:15.3910000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2942] _id=6abbb818485cab4c957c2496 ts=2026-09-29T13:07:36.4290000Z; 24h 12m: 6aa413b141b41dbac0c7f1fb.jsonl[8161] _id=6ac4f1c1de269131f9b00ba6 ts=2026-10-06T13:04:01.5490000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8641] _id=6ac6464ade269131f9b8bfb1 ts=2026-10-07T13:16:58.3390000Z
- **INFO / Info** `gameWindowUnfocusEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 167h 35m 
  - Evidence: 167h 35m: 6aa413b141b41dbac0c7f1fb.jsonl[1051] _id=6ab523a9485cab4c955097d5 ts=2026-09-24T13:20:41.6340000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[6513] _id=6abe5885485cab4c95a4029f ts=2026-10-01T12:56:37.1590000Z; 23h 55m: 6aa413b141b41dbac0c7f1fb.jsonl[405] _id=6ab3d347485cab4c954c0af8 ts=2026-09-23T13:25:27.5760000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[1051] _id=6ab523a9485cab4c955097d5 ts=2026-09-24T13:20:41.6340000Z; 1h 52m: 6aa413b141b41dbac0c7f1fb.jsonl[6513] _id=6abe5885485cab4c95a4029f ts=2026-10-01T12:56:37.1590000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8123] _id=6abe72dc485cab4c95a95f56 ts=2026-10-01T14:49:00.5140000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 17 gap(s), longest 118h 13m 
  - Evidence: 118h 13m: 6aa413b141b41dbac0c7f1fb.jsonl[8102] _id=6abe727c485cab4c95a952a6 ts=2026-10-01T14:47:23.9120000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[8133] _id=6ac4f0f1de269131f9b000c1 ts=2026-10-06T13:00:32.8540000Z; 95h 49m: 6aa413b141b41dbac0c7f1fb.jsonl[1629] _id=6ab6748b485cab4c9554a42d ts=2026-09-25T13:18:03.2190000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[2946] _id=6abbb827485cab4c957c258c ts=2026-09-29T13:07:50.3680000Z; 23h 39m: 6aa413b141b41dbac0c7f1fb.jsonl[1059] _id=6ab523e0485cab4c9550a56d ts=2026-09-24T13:21:36.8520000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[1243] _id=6ab6707d485cab4c955454c5 ts=2026-09-25T13:00:47.1370000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 6aa413b141b41dbac0c7f1fb.jsonl[6368] _id=6abd22af485cab4c958b8f5f ts=2026-09-30T14:54:39.2700000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[6376] _id=6abd22af485cab4c958b8f61 ts=2026-09-30T14:54:39.2730000Z; 3ms: 6aa413b141b41dbac0c7f1fb.jsonl[6516] _id=6abe5893485cab4c95a4030b ts=2026-10-01T12:56:49.3840000Z -> 6aa413b141b41dbac0c7f1fb.jsonl[6517] _id=6abe5893485cab4c95a4030d ts=2026-10-01T12:56:49.3870000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 10 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[5384] _id=6abd0abd485cab4c9586a8b5 ts=2026-09-30T13:12:29.8970000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[5398] _id=6abd0ae9485cab4c9586ad04 ts=2026-09-30T13:13:13.0600000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[6217] _id=6abd0f60485cab4c95884645 ts=2026-09-30T13:32:16.5330000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — camera centering: close without preceding open. 
  - Observed: 111 occurrence(s) 
  - Expected: every 'BecameCameraUncentered' preceded by 'BecameCameraCentered' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[1896] _id=6ab675b6485cab4c9554c693 ts=2026-09-25T13:23:01.8950000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1919] _id=6ab675b8485cab4c9554c710 ts=2026-09-25T13:23:02.8660000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1821] _id=6ab675b8485cab4c9554c716 ts=2026-09-25T13:23:03.1840000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: close without preceding open. 
  - Observed: 160 occurrence(s) 
  - Expected: every 'BecameInvisible' preceded by 'BecameVisible' per pieceId 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[1837] _id=6ab675a2485cab4c9554c418 ts=2026-09-25T13:20:47.5960000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1744] _id=6ab67540485cab4c9554b858 ts=2026-09-25T13:21:04.2530000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1788] _id=6ab67593485cab4c9554c25c ts=2026-09-25T13:22:26.7420000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[9040] _id=6ac64a76de269131f9b9834f ts=2026-10-07T13:34:46.7570000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` `actionType` — node hover: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationNodeHoverEnd' preceded by 'argumentationNodeHoverStart' per nodeName 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[7834] _id=6abe6139485cab4c95a5fe51 ts=2026-10-01T13:33:45.1680000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[7835] _id=6abe6139485cab4c95a5fe61 ts=2026-10-01T13:33:45.2110000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[8106] _id=6abe727c485cab4c95a95298 ts=2026-10-01T14:47:23.7750000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[8133] _id=6ac4f0f1de269131f9b000c1 ts=2026-10-06T13:00:32.8540000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 5 records 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[369] _id=6ab3d314485cab4c954c055c ts=?`; `6aa413b141b41dbac0c7f1fb.jsonl[411] _id=6ab3d368485cab4c954c0e86 ts=?`; `6aa413b141b41dbac0c7f1fb.jsonl[944] _id=6ab5228f485cab4c95505fcb ts=?`
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — camera centering: repeated open with no intervening close. 
  - Observed: 393 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[1993] _id=6ab675d0485cab4c9554cb3e ts=2026-09-25T13:23:28.7020000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1908] _id=6ab675dd485cab4c9554cd9a ts=2026-09-25T13:23:41.1950000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[2043] _id=6ab675e1485cab4c9554ce2c ts=2026-09-25T13:23:44.8330000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: repeated open with no intervening close. 
  - Observed: 1060 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[1695] _id=6ab67528485cab4c9554b604 ts=2026-09-25T13:20:39.4590000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1703] _id=6ab67528485cab4c9554b60c ts=2026-09-25T13:20:39.4850000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[1696] _id=6ab67528485cab4c9554b610 ts=2026-09-25T13:20:39.5040000Z` 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Low** `TopographicMapEvent` `actionType` — map open/close: repeated open with no intervening close. 
  - Observed: 7 occurrence(s) 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[5397] _id=6abd0ae9485cab4c9586ad00 ts=2026-09-30T13:13:13.0540000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[5396] _id=6abd0ae9485cab4c9586ad19 ts=2026-09-30T13:13:13.0740000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[7425] _id=6abe5cca485cab4c95a48d81 ts=2026-10-01T13:14:50.9660000Z` 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'DialogueStartEvent' (totals: 184 start, 181 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — camera centering: open(s) never closed (may be legitimate at session end). 
  - Observed: 133 unmatched 'BecameCameraCentered' (totals: 557 open, 535 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `PuzzlePieceVisibleEvent` `actionType` — piece visibility: open(s) never closed (may be legitimate at session end). 
  - Observed: 122 unmatched 'BecameVisible' (totals: 1311 open, 1349 close) 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 3 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `TopographicMapEvent` `actionType` — map open/close: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'MapOpenEvent' (totals: 16 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 15 unmatched 'questActiveEvent' (totals: 28 start, 15 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — _id (arrival) order disagrees with client-timestamp order. 
  - Observed: 195 of 9182 adjacent _id pairs reverse in client time; worst 155.8s 
  - Expected: expected for batched uploads; audits sort by client timestamp 
  - Examples: `6aa413b141b41dbac0c7f1fb.jsonl[3142] _id=6abbb99a485cab4c957c5050 ts=2026-09-29T13:14:02.0690000Z`; `6aa413b141b41dbac0c7f1fb.jsonl[3158] _id=6abbb99b485cab4c957c5060 ts=2026-09-29T13:11:26.2700000Z`
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.05s, min -157.23s, max +1.23s over 9183 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county-129users\users\6aa413b141b41dbac0c7f1fb\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | partial |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `EndOfUnit` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=partial, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 5 records 
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

### `PuzzlePieceVisibleEvent` — 3752 records

*Purpose:* Visibility / camera-centering state of drag-puzzle pieces and slots.

- **Scenes:** Unit 2 Prod (Refactor) (3752)
- **Intervals:** median 0.03s (p5 0.00s / p95 1.56s, n=3751)
- **Open findings:** 5 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3752/3752 records)
    "BecameInvisible"  x1349
    "BecameVisible"  x1311
    "BecameCameraCentered"  x557
    "BecameCameraUncentered"  x535
data.pieceId  (string, 3752/3752 records)
    19 unique values (see csv/event_unique_values.csv)
data.timestamp  (string, 3752/3752 records)
    2000 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `PuzzlePieceVisibleEvent`.

### `InputEvent` — 2025 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 2 Prod (Refactor) (870); Unit 1 Dev (782); Unit 3 Dev (373)
- **Intervals:** median 2.15s (p5 0.19s / p95 26.25s, n=2024)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 2025/2025 records)
    "pressed"  x2025
data.actionType  (string, 2025/2025 records)
    "Move"  x1486
    "Interact"  x384
    "Jump"  x56
    "Ascend"  x35
    "Hoverboard"  x29
    "Descend"  x17
    "Sprint"  x14
    "Map"  x4
data.key  (string, 2025/2025 records, 2 empty-string)
    16 unique values (see csv/event_unique_values.csv)
data.playerOrDrone  (string, 2025/2025 records)
    "Player"  x1719
    "Drone"  x306
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 1701 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (857); Unit 1 Dev (489); Unit 3 Dev (355)
- **Intervals:** median 10.00s (p5 9.98s / p95 10.02s, n=1698)
- **Fields under `data`:**

```text
data.position  (object, 1701/1701 records)
data.position.x  (number, 1701/1701 records)
    numeric range -686.7 .. 1458.65 (616 unique)
data.position.y  (number, 1701/1701 records)
    numeric range -114.326 .. 163.723 (404 unique)
data.position.z  (number, 1701/1701 records)
    numeric range -1101.02 .. 1976.42 (616 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 1103 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (790); Unit 3 Dev (186); Unit 1 Dev (127)
- **eventKey:** present on 738 of 1103 records
- **Intervals:** median 4.92s (p5 0.00s / p95 64.51s, n=1102)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x738; [conversationId, dialogueEventType] x365
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1103/1103 records)
    numeric range 8 .. 103 (24 unique)
data.dialogueEventType  (string, 1103/1103 records)
    "DialogueNodeEvent"  x738
    "DialogueStartEvent"  x184
    "DialogueFinishEvent"  x181
data.nodeId  (number, 738/1103 records)
    numeric range 0 .. 290 (188 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `ObjectInterEvent` — 237 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (142); Unit 2 Prod (Refactor) (89); Unit 3 Dev (6)
- **Intervals:** median 5.85s (p5 0.17s / p95 315.15s, n=236)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 237/237 records)
    "TalkTo"  x136
    "Press E to Pick up"  x37
    "Press E to Place"  x34
    "Press E to Scan"  x9
    "E to Talk"  x6
    "Press E to Install"  x4
    "Press E to Operate"  x3
    "Push E To Grab Crate"  x3
    "Press E to Collect"  x2
    "Press E To Pick Up"  x1
    "Press E to Insert"  x1
    "Push E To Place Crate On Hoverboard"  x1
data.objectName  (string, 237/237 records)
    35 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `argumentationNodeEvent` — 158 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (113); Unit 3 Dev (45)
- **Intervals:** median 0.39s (p5 0.03s / p95 7.57s, n=157)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 158/158 records)
    "argumentationNodeHoverEnd"  x69
    "argumentationNodeHoverStart"  x67
    "argumentationNodeAdd"  x14
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 158/158 records)
    "Unit 2 – Watershed"  x113
    "Unit 3 - Pollution Upstream"  x45
data.nodeName  (string, 158/158 records)
    "B"  x28
    "A"  x26
    "C"  x22
    "1"  x21
    "I"  x19
    "II"  x19
    "D"  x12
    "5"  x5
    "2"  x2
    "3"  x2
    "4"  x2
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 57 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (39); Unit 2 Prod (Refactor) (18)
- **Intervals:** median 0.77s (p5 0.22s / p95 13.29s, n=56)
- **`data` key-set variants:** [actionType, currentSoilType, isCorrectSelection, waterLevelStatus, waterRetentionChange] x52; [Soil Key Puzzle Status, Unit] x5
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 5/57 records)
    "Started"  x3
    "Finished"  x2
data.Unit  (string, 5/57 records)
    "Unit 2 Prod (Refactor)"  x4
    "Unit 3 Dev"  x1
data.actionType  (string, 52/57 records)
    "RightDrag"  x30
    "LeftDrag"  x22
data.currentSoilType  (string, 52/57 records)
    "CLAY"  x11
    "CLAYSAND"  x10
    "CLAYROCK"  x9
    "SAND"  x9
    "SANDGRAVEL"  x7
    "BEDROCK"  x3
    "GRAVEL"  x3
data.isCorrectSelection  (string, 52/57 records)
    "false"  x38
    "true"  x14
data.waterLevelStatus  (string, 52/57 records)
    "Proper"  x23
    "TooHigh"  x20
    "TooLow"  x9
data.waterRetentionChange  (string, 52/57 records)
    "Decrease"  x23
    "Increase"  x15
    "NoChange"  x14
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `questEvent` — 43 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (28); Unit 1 Dev (8); Unit 3 Dev (7)
- **eventKey:** present on 43 of 43 records
- **Intervals:** median 326.83s (p5 0.14s / p95 85148.46s, n=42)
- **`data` key-set variants:** [questEventType, questID, questName] x28; [questEventType, questID, questName, questSuccessOrFailure] x15
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 43/43 records)
    "questActiveEvent"  x28
    "questFinishEvent"  x15
data.questID  (string, 43/43 records)
    "24"  x7
    "28"  x7
    "25"  x6
    "16"  x4
    "22"  x4
    "23"  x4
    "54"  x4
    "21"  x3
    "17"  x2
    "18"  x1
    "29"  x1
data.questName  (string, 43/43 records)
    "Getting Your Space Legs"  x7
    "Investigate the Temple"  x7
    "Which Watershed?"  x6
    "Claim of Command"  x4
    "Foraged Forging"  x4
    "Getting the Band Back Together"  x4
    "Supply Run"  x4
    "Escape the Ruin"  x3
    "Pollution Solution"  x2
    "Forsaken Facility"  x1
    "Gear Up"  x1
data.questSuccessOrFailure  (string, 15/43 records)
    "Succeeded"  x15
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 33 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (27); Unit 3 Dev (6)
- **Intervals:** median 20.32s (p5 0.03s / p95 202804.33s, n=32)
- **`data` key-set variants:** [actionType, featureUsed] x30; [actionType, featureUsed, location] x3
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 33/33 records)
    "MapOpenEvent"  x16
    "MapCloseEvent"  x14
    "WaypointMoveEvent"  x2
    "WaypointSetEvent"  x1
data.featureUsed  (string, 33/33 records)
    "Map"  x30
    "Waypoint"  x3
data.location  (object, 3/33 records)
data.location.x  (number, 3/33 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 3/33 records)
    3 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 3/33 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `gameWindowFocusEvent` — 18 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (16); Transition (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 6411.72s (p5 85.46s / p95 361208.41s, n=17)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 18/18 records)
    true  x18
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `DEBUGMenu` — 17 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 2 Prod (Refactor) (8); Unit 1 Dev (6); Unit 3 Dev (2); MainMenu (1)
- **Intervals:** median 6632.22s (p5 172.66s / p95 365253.84s, n=16)
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
- **Intervals:** median 6853.85s (p5 225.53s / p95 369273.92s, n=15)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 16/16 records)
    true  x16
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `argumentationAnswerEvent` — 12 records

*Purpose:* Final argument submission per argumentation activity.

- **Scenes:** Unit 2 Prod (Refactor) (11); Unit 3 Dev (1)
- **Intervals:** median 14.69s (p5 4.18s / p95 259171.01s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "submitAnswerEvent"  x12
data.answerSubmitted  (string, 12/12 records)
    "B,1,I"  x3
    "B,1,II"  x2
    "C,1,II"  x2
    "1,"  x1
    "A,1,II"  x1
    "A,5,I"  x1
    "B,C,1,II"  x1
    "D,1,II"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 2 – Watershed"  x11
    "Unit 3 - Pollution Upstream"  x1
```

Raw examples: `event_examples.json` -> `argumentationAnswerEvent`.

### `argumentationEvent` — 5 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (3); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 105.69s (p5 7.94s / p95 440547.21s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationSessionClose"  x3
    "argumentationSessionOpen"  x2
data.argumentationDescription  (string, 5/5 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
data.argumentationTitle  (string, 5/5 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `crash` — 5 records

- **Scenes:** <missing sceneName> (5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 5/5 records)
    true  x5
data.message  (string, 5/5 records)
    "Permissions check failed"  x2
    "Pointer lock cannot be acquired immediately after the user has exited the lock."  x2
    "A user gesture is required to request Pointer Lock."  x1
data.phase  (string, 5/5 records)
    "running"  x5
data.stack  (string, 5/5 records, 3 empty-string)
    ""  x3
    "TypeError: Permissions check failed"  x2
data.type  (string, 5/5 records)
    "unhandled_rejection"  x5
data.unitId  (string, 5/5 records)
    "unit1"  x3
    "unit2"  x2
data.workspace  (string, 5/5 records)
    "mhs"  x5
```

Raw examples: `event_examples.json` -> `crash`.

### `gameWindowUnfocusEvent` — 4 records

*Purpose:* Browser/game window lost focus.

- **Scenes:** Unit 1 Dev (2); Transition (1); Unit 2 Prod (Refactor) (1)
- **Intervals:** median 86114.06s (p5 14680.43s / p95 551631.38s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 4/4 records)
    false  x4
```

Raw examples: `event_examples.json` -> `gameWindowUnfocusEvent`.

### `DaniEvent` — 2 records

*Purpose:* Dani assistant/toolbar usage (opening and closing player tools).

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 4.12s (p5 4.12s / p95 4.12s, n=1)
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "Close"  x1
    "Open"  x1
data.toolName  (string, 2/2 records, 2 empty-string)
    ""  x2
```

Raw examples: `event_examples.json` -> `DaniEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `EndOfUnit` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : exact duplicate records (same timestamp, scene and data)
- `PuzzlePieceVisibleEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)
- `DEBUGMenu` : median interval between records changed substantially
- `EndOfUnit` : event type present in baseline 09-23-26 but absent now
- `InputEvent` : median interval between records changed substantially
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now
- `TopographicMapEvent` : baseline field(s) absent this build
- `TopographicMapEvent` : median interval between records changed substantially
- `WaterChamberEvent` : event type present in baseline 09-23-26 but absent now
- `argumentationAnswerEvent` : median interval between records changed substantially

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (18 records)
- `TopographicMapEvent` data.actionType: "WaypointMoveEvent" (2x); "WaypointSetEvent" (1x)
- `TopographicMapEvent` data.featureUsed: "Waypoint" (3x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*