# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b04

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a8bc9a8420a1e6b56b04
- **Game version string(s) in log:** 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a8bc9a8420a1e6b56b04.jsonl
- **Records:** 346 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a8bc9a8420a1e6b56b04
- **Time span:** 2026-10-05T15:14:33.017000+00:00 .. 2026-10-05T15:29:19.226000+00:00 (14m 46s)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b04\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **8 event types**, 346 records, 2 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 27 INFO, 6 NOT_TESTED, 26 PASS.
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
| InputEvent | 174 | 50.29 | 1 | 1 | 0 | 2026-10-05T15:16:08.188000+00:00 | 2026-10-05T15:27:28.443000+00:00 | 11m 20s |
| PlayerPositionEvent | 80 | 23.12 | 1 | 1 | 0 | 2026-10-05T15:16:04.598000+00:00 | 2026-10-05T15:29:19.226000+00:00 | 13m 14s |
| DialogueEvent | 78 | 22.54 | 1 | 1 | 59 | 2026-10-05T15:16:24.747000+00:00 | 2026-10-05T15:29:06.993000+00:00 | 12m 42s |
| questEvent | 7 | 2.02 | 1 | 1 | 7 | 2026-10-05T15:16:24.721000+00:00 | 2026-10-05T15:27:06.680000+00:00 | 10m 41s |
| ObjectInterEvent | 4 | 1.16 | 1 | 1 | 0 | 2026-10-05T15:21:56.905000+00:00 | 2026-10-05T15:27:29.758000+00:00 | 5m 32s |
| DEBUGMenu | 1 | 0.29 | 1 | 1 | 0 | 2026-10-05T15:16:04.584000+00:00 | 2026-10-05T15:16:04.584000+00:00 | 0.0s |
| gameStartEvent | 1 | 0.29 | 1 | 1 | 0 | 2026-10-05T15:14:33.018000+00:00 | 2026-10-05T15:14:33.018000+00:00 | 0.0s |
| gameWindowFocusEvent | 1 | 0.29 | 1 | 1 | 0 | 2026-10-05T15:14:33.017000+00:00 | 2026-10-05T15:14:33.017000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `EndOfUnit` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 116.484s median 
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
- **WARNING / Medium** `questEvent` — median interval between records changed substantially. 
  - Observed: 72.951s median 
  - Expected: 147.974s in 09-23-26 
  - Evidence: regression candidate requiring review
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
  - Observed: 78 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 174 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend; Hoverboard; Map; Sprint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; h; leftShift; m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 4 records 
  - Expected: 235 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Collect; Press E to Insert; Press E to Install; Press E to Operate; Press E to Pick Up; Press E to Pick up; Press E to Pickup Canister; Press E to Place; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Press [E/Action button] to enter escape pod ; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 80 records 
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
- **INFO / Info** `questEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 7 records 
  - Expected: 71 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 21; 22; 23; 24; 25; 33; 34; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Defend the Expedition; Desert Delicacies; Escape the Ruin; Foraged Forging; Forsaken Facility; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; What Was That?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 2 mismatch(es); e.g. 'DialogueNodeEvent:31:0' vs expected 'DialogueNodeEvent:31:2' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `6ab9a8bc9a8420a1e6b56b04.jsonl[242] _id=6ac3c10ade269131f9ad1ae9 ts=2026-10-05T15:23:53.4140000Z`; `6ab9a8bc9a8420a1e6b56b04.jsonl[324] _id=6ac3c1e2de269131f9ad2bd9 ts=2026-10-05T15:27:29.7730000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 1 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 1} 
  - Examples: `6ab9a8bc9a8420a1e6b56b04.jsonl[4] _id=6ac3bed9de269131f9ace413 ts=2026-10-05T15:14:33.0180000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 1 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 1} 
  - Examples: `6ab9a8bc9a8420a1e6b56b04.jsonl[3] _id=6ac3bed9de269131f9ace411 ts=2026-10-05T15:14:33.0170000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 173 | 0.001 | 0.357 | 3.932 | 3.867 | 245.449 | 15.26 | 22 | 0 |
| PlayerPositionEvent | 79 | 9.92 | 10.003 | 10.059 | 10.091 | 13.927 | 5.97 | 0 | 0 |
| DialogueEvent | 77 | 0.005 | 7.328 | 9.899 | 26.855 | 81.04 | 6.06 | 13 | 0 |
| questEvent | 6 | 0.009 | 72.951 | 106.993 | 253.236 | 258.455 | 0.56 | 2 | 0 |
| ObjectInterEvent | 3 | 0.005 | 116.484 | 110.951 | 206.376 | 216.364 | 0.54 | 1 | 0 |
| DEBUGMenu | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameStartEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameWindowFocusEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `5ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[197] _id=6ac3c095de269131f9ad0d83 ts=2026-10-05T15:21:56.9050000Z ~ 6ab9a8bc9a8420a1e6b56b04.jsonl[198] _id=6ac3c095de269131f9ad0d87 ts=2026-10-05T15:21:56.9100000Z`
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 13 interval(s) ≤ 0.005s..0.007s shown 
  - Evidence: 5ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[242] _id=6ac3c10ade269131f9ad1ae9 ts=2026-10-05T15:23:53.4140000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[244] _id=6ac3c10ade269131f9ad1af5 ts=2026-10-05T15:23:53.4190000Z; 5ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[324] _id=6ac3c1e2de269131f9ad2bd9 ts=2026-10-05T15:27:29.7730000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[320] _id=6ac3c1e2de269131f9ad2bdb ts=2026-10-05T15:27:29.7780000Z; 7ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[126] _id=6ac3c04bde269131f9ad0555 ts=2026-10-05T15:20:43.1890000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[122] _id=6ac3c04bde269131f9ad055b ts=2026-10-05T15:20:43.1960000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 22 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[87] _id=6ac3c030de269131f9ad017f ts=2026-10-05T15:20:16.2640000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[88] _id=6ac3c030de269131f9ad0183 ts=2026-10-05T15:20:16.2650000Z; 2ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[12] _id=6ac3bf39de269131f9ace775 ts=2026-10-05T15:16:08.1900000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[13] _id=6ac3bf3ade269131f9ace779 ts=2026-10-05T15:16:08.1920000Z; 2ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[13] _id=6ac3bf3ade269131f9ace779 ts=2026-10-05T15:16:08.1920000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[14] _id=6ac3bf3ade269131f9ace77b ts=2026-10-05T15:16:08.1940000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.005s..0.005s shown 
  - Evidence: 5ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[197] _id=6ac3c095de269131f9ad0d83 ts=2026-10-05T15:21:56.9050000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[198] _id=6ac3c095de269131f9ad0d87 ts=2026-10-05T15:21:56.9100000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.009s..0.013s shown 
  - Evidence: 9ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[287] _id=6ac3c1cbde269131f9ad29f3 ts=2026-10-05T15:27:06.6710000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[285] _id=6ac3c1cbde269131f9ad29f5 ts=2026-10-05T15:27:06.6800000Z; 13ms: 6ab9a8bc9a8420a1e6b56b04.jsonl[220] _id=6ac3c0ddde269131f9ad14e9 ts=2026-10-05T15:23:09.0790000Z -> 6ab9a8bc9a8420a1e6b56b04.jsonl[222] _id=6ac3c0ddde269131f9ad14ef ts=2026-10-05T15:23:09.0920000Z

## 7. Sequence / Timing Findings

- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 1 unmatched 'DialogueStartEvent' (totals: 10 start, 9 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 1 unmatched 'questActiveEvent' (totals: 4 start, 3 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.50s, min -4.48s, max -0.49s over 346 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a8bc9a8420a1e6b56b04\coverage.yaml

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

### `InputEvent` — 174 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 1 Dev (174)
- **Intervals:** median 0.36s (p5 0.00s / p95 3.87s, n=173)
- **Fields under `data`:**

```text
data.Value  (string, 174/174 records)
    "pressed"  x174
data.actionType  (string, 174/174 records)
    "Move"  x162
    "Jump"  x9
    "Interact"  x3
data.key  (string, 174/174 records)
    "a"  x70
    "w"  x46
    "d"  x32
    "s"  x14
    "space"  x9
    "leftButton"  x2
    "e"  x1
data.playerOrDrone  (string, 174/174 records)
    "Player"  x174
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 80 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 1 Dev (80)
- **Intervals:** median 10.00s (p5 9.95s / p95 10.09s, n=79)
- **Fields under `data`:**

```text
data.position  (object, 80/80 records)
data.position.x  (number, 80/80 records)
    numeric range -20.5803 .. 25.5089 (19 unique)
data.position.y  (number, 80/80 records)
    numeric range 0 .. 0.0202867 (21 unique)
data.position.z  (number, 80/80 records)
    numeric range -99.392 .. -11.5343 (19 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `DialogueEvent` — 78 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (78)
- **eventKey:** present on 59 of 78 records
- **Intervals:** median 7.33s (p5 0.01s / p95 26.86s, n=77)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x59; [conversationId, dialogueEventType] x19
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 78/78 records)
    3 unique values (see csv/event_unique_values.csv)
data.dialogueEventType  (string, 78/78 records)
    "DialogueNodeEvent"  x59
    "DialogueStartEvent"  x10
    "DialogueFinishEvent"  x9
data.nodeId  (number, 59/78 records)
    numeric range 1 .. 97 (45 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `questEvent` — 7 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (7)
- **eventKey:** present on 7 of 7 records
- **Intervals:** median 72.95s (p5 0.01s / p95 253.24s, n=6)
- **`data` key-set variants:** [questEventType, questID, questName] x4; [questEventType, questID, questName, questSuccessOrFailure] x3
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 7/7 records)
    "questActiveEvent"  x4
    "questFinishEvent"  x3
data.questID  (string, 7/7 records)
    "28"  x2
    "29"  x2
    "31"  x2
    "32"  x1
data.questName  (string, 7/7 records)
    "Gear Up"  x2
    "Getting Your Space Legs"  x2
    "TK, Reporting In!"  x2
    "Info and Intros"  x1
data.questSuccessOrFailure  (string, 3/7 records)
    "Succeeded"  x3
```

Raw examples: `event_examples.json` -> `questEvent`.

### `ObjectInterEvent` — 4 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 116.48s (p5 11.65s / p95 206.38s, n=3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "Press E to Open Locker"  x2
    "E to Talk"  x1
    "TalkTo"  x1
data.objectName  (string, 4/4 records)
    "Player Locker"  x2
    "Aryn"  x1
    "Toppo"  x1
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

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
- `ObjectInterEvent` : median interval between records changed substantially
- `PuzzlePieceVisibleEvent` : event type present in baseline 09-23-26 but absent now
- `Soil Key Puzzle` : event type present in baseline 09-23-26 but absent now
- `SolarStillDesignEvent` : event type present in baseline 09-23-26 but absent now
- `TerasGardenBox` : event type present in baseline 09-23-26 but absent now

**Additional gameplay testing (content not exercised):**
- `PuzzlePieceVisibleEvent`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected event type absent, but its content was not exercised this playthrough
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*