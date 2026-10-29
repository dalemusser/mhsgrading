# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b02

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b02
- **Game version string(s) in log:** 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b02.jsonl
- **Records:** 328 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b02
- **Time span:** 2026-10-05T15:15:59.336000+00:00 .. 2026-10-05T15:28:54.325000+00:00 (12m 54s)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b02\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **8 event types**, 328 records, 2 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 28 INFO, 6 NOT_TESTED, 26 PASS.
- Top items needing attention:
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `EndOfUnit`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationNodeEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowUnfocusEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `EndOfUnit`: event type present in baseline 09-23-26 but absent now

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 181 | 55.18 | 1 | 1 | 0 | 2026-10-05T15:16:13.210000+00:00 | 2026-10-05T15:27:39.806000+00:00 | 11m 26s |
| PlayerPositionEvent | 77 | 23.48 | 1 | 1 | 0 | 2026-10-05T15:16:09.744000+00:00 | 2026-10-05T15:28:54.325000+00:00 | 12m 44s |
| ObjectInterEvent | 46 | 14.02 | 1 | 1 | 0 | 2026-10-05T15:23:58.165000+00:00 | 2026-10-05T15:25:46.610000+00:00 | 1m 48s |
| DialogueEvent | 20 | 6.1 | 1 | 1 | 16 | 2026-10-05T15:16:29.704000+00:00 | 2026-10-05T15:19:14.140000+00:00 | 2m 44s |
| DEBUGMenu | 1 | 0.3 | 1 | 1 | 0 | 2026-10-05T15:16:09.722000+00:00 | 2026-10-05T15:16:09.722000+00:00 | 0.0s |
| gameStartEvent | 1 | 0.3 | 1 | 1 | 0 | 2026-10-05T15:15:59.337000+00:00 | 2026-10-05T15:15:59.337000+00:00 | 0.0s |
| gameWindowFocusEvent | 1 | 0.3 | 1 | 1 | 0 | 2026-10-05T15:15:59.336000+00:00 | 2026-10-05T15:15:59.336000+00:00 | 0.0s |
| questEvent | 1 | 0.3 | 1 | 1 | 1 | 2026-10-05T15:16:29.675000+00:00 | 2026-10-05T15:16:29.675000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `InputEvent` — median interval between records changed substantially. 
  - Observed: 1.567s median 
  - Expected: 0.583s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 0.224s median 
  - Expected: 5.979s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 38 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TerasGardenBox` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 11 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 83 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 14 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 140 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowUnfocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 76 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `questEvent` — baseline field(s) absent this build. 
  - Observed: data.questSuccessOrFailure 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: Transition; Unit 2 Prod (Refactor); Unit 3 Dev; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DEBUGMenu` — record volume changed 0.1x vs baseline. 
  - Observed: 1 records 
  - Expected: 12 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `DialogueEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 20 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 181 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend; Hoverboard; Map; Sprint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; a; d; h; leftShift; m; s; w 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 46 records 
  - Expected: 235 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Collect; Press E to Insert; Press E to Install; Press E to Open Locker; Press E to Operate; Press E to Pick Up; Press E to Pick up; Press E to Pickup Canister; Press E to Place; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Press [E/Action button] to enter escape pod ; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 77 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameStartEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 1 records 
  - Expected: 6 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `gameWindowFocusEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 1 records 
  - Expected: 82 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 1 records 
  - Expected: 71 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questEventType` — baseline categorical value(s) not seen this build. 
  - Observed: questFinishEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 21; 22; 23; 24; 25; 29; 31; 32; 33; 34; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Defend the Expedition; Desert Delicacies; Escape the Ruin; Foraged Forging; Forsaken Facility; Gear Up; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Info and Intros; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; TK, Reporting In!; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; What Was That?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 1 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 1} 
  - Examples: `6ab9a8bc9a8420a1e6b56b02.jsonl[4] _id=6ac3bf30de269131f9ace73f ts=2026-10-05T15:15:59.3370000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 1 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 1} 
  - Examples: `6ab9a8bc9a8420a1e6b56b02.jsonl[3] _id=6ac3bf30de269131f9ace73b ts=2026-10-05T15:15:59.3360000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 180 | 0.002 | 1.567 | 3.814 | 8.772 | 167.514 | 15.73 | 3 | 0 |
| PlayerPositionEvent | 76 | 9.879 | 10.002 | 10.06 | 10.104 | 13.78 | 5.96 | 0 | 0 |
| ObjectInterEvent | 45 | 0.008 | 0.224 | 2.41 | 12.803 | 45.096 | 24.9 | 2 | 0 |
| DialogueEvent | 19 | 0.009 | 4.073 | 8.655 | 25.868 | 40.251 | 6.93 | 2 | 0 |
| DEBUGMenu | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameStartEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameWindowFocusEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| questEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 35 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `127ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[190] _id=6ac3c115de269131f9ad1cdb ts=2026-10-05T15:24:04.7300000Z ~ 6ab9a8bc9a8420a1e6b56b02.jsonl[194] _id=6ac3c115de269131f9ad1cf1 ts=2026-10-05T15:24:04.8570000Z`; `171ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[194] _id=6ac3c115de269131f9ad1cf1 ts=2026-10-05T15:24:04.8570000Z ~ 6ab9a8bc9a8420a1e6b56b02.jsonl[192] _id=6ac3c116de269131f9ad1d07 ts=2026-10-05T15:24:05.0280000Z`; `162ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[205] _id=6ac3c127de269131f9ad2019 ts=2026-10-05T15:24:22.4970000Z ~ 6ab9a8bc9a8420a1e6b56b02.jsonl[208] _id=6ac3c127de269131f9ad2024 ts=2026-10-05T15:24:22.6590000Z`
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.009s..0.013s shown 
  - Evidence: 9ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[44] _id=6ac3bfedde269131f9acf6f1 ts=2026-10-05T15:19:08.3190000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[38] _id=6ac3bfedde269131f9acf6fb ts=2026-10-05T15:19:08.3280000Z; 13ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[9] _id=6ac3bf4ede269131f9ace831 ts=2026-10-05T15:16:29.7040000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[12] _id=6ac3bf4ede269131f9ace835 ts=2026-10-05T15:16:29.7170000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 3 interval(s) ≤ 0.002s..0.043s shown 
  - Evidence: 2ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[1] _id=6ac3bf3ede269131f9ace7a3 ts=2026-10-05T15:16:13.2100000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[6] _id=6ac3bf3fde269131f9ace7a7 ts=2026-10-05T15:16:13.2120000Z; 6ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[213] _id=6ac3c13dde269131f9ad22df ts=2026-10-05T15:24:43.9780000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[255] _id=6ac3c13ede269131f9ad22e5 ts=2026-10-05T15:24:43.9840000Z; 43ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[272] _id=6ac3c140de269131f9ad2339 ts=2026-10-05T15:24:45.8620000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[273] _id=6ac3c141de269131f9ad233f ts=2026-10-05T15:24:45.9050000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.008s..0.042s shown 
  - Evidence: 8ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[212] _id=6ac3c13dde269131f9ad22dd ts=2026-10-05T15:24:43.9720000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[210] _id=6ac3c13dde269131f9ad22e3 ts=2026-10-05T15:24:43.9800000Z; 42ms: 6ab9a8bc9a8420a1e6b56b02.jsonl[248] _id=6ac3c140de269131f9ad2335 ts=2026-10-05T15:24:45.8570000Z -> 6ab9a8bc9a8420a1e6b56b02.jsonl[249] _id=6ac3c140de269131f9ad233d ts=2026-10-05T15:24:45.8990000Z

## 7. Sequence / Timing Findings

- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 1 unmatched 'questActiveEvent' (totals: 1 start, 0 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.77s, min -4.54s, max -0.76s over 328 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b02\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | skipped |
| Unit3 | skipped |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `EndOfUnit` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationNodeEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-node-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **NOT_TESTED / NotTested** `PuzzlePieceVisibleEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage manifest: ['skipped', 'skipped', 'skipped'] 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **NOT_TESTED / NotTested** `Soil Key Puzzle` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [3, 4] 
  - Evidence: coverage manifest: ['skipped', 'skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
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

### `InputEvent` — 181 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 1 Dev (181)
- **Intervals:** median 1.57s (p5 0.12s / p95 8.77s, n=180)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Value  (string, 181/181 records)
    "pressed"  x181
data.actionType  (string, 181/181 records)
    "Move"  x94
    "Interact"  x80
    "Jump"  x7
data.key  (string, 181/181 records)
    "upArrow"  x76
    "e"  x66
    "downArrow"  x18
    "leftButton"  x14
    "space"  x7
data.playerOrDrone  (string, 181/181 records)
    "Player"  x181
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 77 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 1 Dev (77)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.10s, n=76)
- **Fields under `data`:**

```text
data.position  (object, 77/77 records)
data.position.x  (number, 77/77 records)
    numeric range -18.3658 .. 22.1286 (35 unique)
data.position.y  (number, 77/77 records)
    numeric range -0.379993 .. 0.0203264 (28 unique)
data.position.z  (number, 77/77 records)
    numeric range -112.271 .. 11.8542 (35 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 46 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (46)
- **Intervals:** median 0.22s (p5 0.08s / p95 12.80s, n=45)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 46/46 records)
    "TalkTo"  x40
    "E to Talk"  x6
data.objectName  (string, 46/46 records)
    "Jasper"  x40
    "Anderson"  x6
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `DialogueEvent` — 20 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (20)
- **eventKey:** present on 16 of 20 records
- **Intervals:** median 4.07s (p5 0.01s / p95 25.87s, n=19)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x16; [conversationId, dialogueEventType] x4
- **Fields under `data`:**

```text
data.conversationId  (number, 20/20 records)
    1 unique values (see csv/event_unique_values.csv)
data.dialogueEventType  (string, 20/20 records)
    "DialogueNodeEvent"  x16
    "DialogueFinishEvent"  x2
    "DialogueStartEvent"  x2
data.nodeId  (number, 16/20 records)
    numeric range 1 .. 95 (16 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `DEBUGMenu` — 1 records

*Purpose:* Debug menu opened/closed — signals debug tooling was used in the playthrough.

- **Scenes:** Unit 1 Dev (1)
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "DebugMenuStateChanged"  x1
data.isOpened  (bool, 1/1 records)
    false  x1
```

Raw examples: `event_examples.json` -> `DEBUGMenu`.

### `gameStartEvent` — 1 records

*Purpose:* Game/application start marker.

- **Scenes:** MainMenu (1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 1/1 records)
    true  x1
```

Raw examples: `event_examples.json` -> `gameStartEvent`.

### `gameWindowFocusEvent` — 1 records

*Purpose:* Browser/game window gained focus.

- **Scenes:** MainMenu (1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.<empty>  (bool, 1/1 records)
    true  x1
```

Raw examples: `event_examples.json` -> `gameWindowFocusEvent`.

### `questEvent` — 1 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (1)
- **eventKey:** present on 1 of 1 records
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 1/1 records)
    "questActiveEvent"  x1
data.questID  (string, 1/1 records)
    "28"  x1
data.questName  (string, 1/1 records)
    "Getting Your Space Legs"  x1
```

Raw examples: `event_examples.json` -> `questEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `EndOfUnit` : expected event type absent although its content was played — possible logging failure
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationNodeEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `EndOfUnit` : event type present in baseline 09-23-26 but absent now
- `InputEvent` : median interval between records changed substantially
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : event type present in baseline 09-23-26 but absent now
- `Soil Key Puzzle` : event type present in baseline 09-23-26 but absent now
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now

**Additional gameplay testing (content not exercised):**
- `PuzzlePieceVisibleEvent`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected event type absent, but its content was not exercised this playthrough
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*