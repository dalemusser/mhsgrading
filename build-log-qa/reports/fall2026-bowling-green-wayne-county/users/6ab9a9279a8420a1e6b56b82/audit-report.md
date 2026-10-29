# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b82

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 6ab9a9279a8420a1e6b56b82
- **Game version string(s) in log:** 20260914-
- **Audit date:** 2026-10-25
- **Log file(s):** 6ab9a9279a8420a1e6b56b82.jsonl
- **Records:** 805 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 6ab9a9279a8420a1e6b56b82
- **Time span:** 2026-10-06T18:33:19.585000+00:00 .. 2026-10-06T19:05:53.517000+00:00 (32m 33s)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b82\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **8 event types**, 805 records, 2 scenes.
- Findings: **0 FAIL**, **28 WARNING**, 26 INFO, 6 NOT_TESTED, 27 PASS.
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
  - WARNING/Medium `DialogueEvent`: median interval between records changed substantially

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 424 | 52.67 | 1 | 1 | 0 | 2026-10-06T18:34:39.042000+00:00 | 2026-10-06T19:05:47.120000+00:00 | 31m 8s |
| PlayerPositionEvent | 188 | 23.35 | 1 | 1 | 0 | 2026-10-06T18:34:35.627000+00:00 | 2026-10-06T19:05:53.517000+00:00 | 31m 17s |
| ObjectInterEvent | 112 | 13.91 | 1 | 1 | 0 | 2026-10-06T18:43:42.878000+00:00 | 2026-10-06T19:01:27.804000+00:00 | 17m 44s |
| DialogueEvent | 71 | 8.82 | 1 | 1 | 53 | 2026-10-06T18:34:55.481000+00:00 | 2026-10-06T19:01:58.970000+00:00 | 27m 3s |
| questEvent | 7 | 0.87 | 1 | 1 | 7 | 2026-10-06T18:34:55.457000+00:00 | 2026-10-06T18:57:06.732000+00:00 | 22m 11s |
| DEBUGMenu | 1 | 0.12 | 1 | 1 | 0 | 2026-10-06T18:34:35.607000+00:00 | 2026-10-06T18:34:35.607000+00:00 | 0.0s |
| gameStartEvent | 1 | 0.12 | 1 | 1 | 0 | 2026-10-06T18:33:19.586000+00:00 | 2026-10-06T18:33:19.586000+00:00 | 0.0s |
| gameWindowFocusEvent | 1 | 0.12 | 1 | 1 | 0 | 2026-10-06T18:33:19.585000+00:00 | 2026-10-06T18:33:19.585000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 9.139s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — median interval between records changed substantially. 
  - Observed: 0.259s median 
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
  - Observed: 71 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 424 records 
  - Expected: 2411 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `InputEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Ascend; Descend; Hoverboard; Map 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — baseline categorical value(s) not seen this build. 
  - Observed: ; h; m 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `InputEvent` `data.key` — categorical value(s) not seen in baseline. 
  - Observed: downArrow; rightShift; upArrow 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `InputEvent` `data.playerOrDrone` — baseline categorical value(s) not seen this build. 
  - Observed: Drone 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `ObjectInterEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: Inspect Alien Glyph; Place Cube; Press E; Press E To Change Direction; Press E To Collect Pipe; Press E To Pick Up; Press E To Place Cameras; Press E To Place Cube In Canal; Press E To Place Glyph; Press E To Return To Base; Press E To Scan; Press E to Collect; Press E to Insert; Press E to Install; Press E to Operate; Press E to Pick Up; Press E to Pick up; Press E to Pickup Canister; Press E to Place; Press E to Place Pipe Segment; Press E to Plant Seed; Press E to Scan; Press E to Switch Canister; Press E to collect cameras; Press E to collect mega turnips; Press E to collect super orange; Press E to collect ultra corn; Press E to deactivate the fountain; Press E to examine; Press E to inspect ; Press E to place; Press E to place canister; Press E to use; Press [E/Action button] to enter escape pod ; Push E To Grab Crate; Push E To Place Crate On Hoverboard 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 188 records 
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
  - Examples: `6ab9a9279a8420a1e6b56b82.jsonl[548] _id=6ac54336de269131f9b7018f ts=2026-10-06T18:51:34.0830000Z`; `6ab9a9279a8420a1e6b56b82.jsonl[727] _id=6ac54588de269131f9b72bbd ts=2026-10-06T19:01:27.8260000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** `gameStartEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 1 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 1} 
  - Examples: `6ab9a9279a8420a1e6b56b82.jsonl[7] _id=6ac53eefde269131f9b67f3c ts=2026-10-06T18:33:19.5860000Z`
- **WARNING / Low** `gameWindowFocusEvent` `data.<empty>` — field name is an empty string. 
  - Observed: path data.<empty> in 1 records 
  - Expected: a descriptive field name 
  - Evidence: types: {'bool': 1} 
  - Examples: `6ab9a9279a8420a1e6b56b82.jsonl[6] _id=6ac53eefde269131f9b67f39 ts=2026-10-06T18:33:19.5850000Z`

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| InputEvent | 423 | 0.001 | 0.616 | 4.416 | 6.893 | 432.595 | 13.59 | 16 | 0 |
| PlayerPositionEvent | 187 | 9.886 | 10.001 | 10.042 | 10.089 | 13.659 | 5.97 | 0 | 0 |
| ObjectInterEvent | 111 | 0.003 | 0.259 | 9.594 | 18.194 | 593.732 | 6.25 | 1 | 0 |
| DialogueEvent | 70 | 0.006 | 9.139 | 23.193 | 79.81 | 335.148 | 2.59 | 12 | 0 |
| questEvent | 6 | 0.009 | 197.243 | 221.879 | 477.765 | 487.152 | 0.27 | 2 | 0 |
| DEBUGMenu | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameStartEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| gameWindowFocusEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **INFO / Info** `ObjectInterEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 92 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `491ms: 6ab9a9279a8420a1e6b56b82.jsonl[169] _id=6ac5415fde269131f9b6c81f ts=2026-10-06T18:43:42.8780000Z ~ 6ab9a9279a8420a1e6b56b82.jsonl[164] _id=6ac5415fde269131f9b6c832 ts=2026-10-06T18:43:43.3690000Z`; `260ms: 6ab9a9279a8420a1e6b56b82.jsonl[164] _id=6ac5415fde269131f9b6c832 ts=2026-10-06T18:43:43.3690000Z ~ 6ab9a9279a8420a1e6b56b82.jsonl[175] _id=6ac5415fde269131f9b6c847 ts=2026-10-06T18:43:43.6290000Z`; `222ms: 6ab9a9279a8420a1e6b56b82.jsonl[175] _id=6ac5415fde269131f9b6c847 ts=2026-10-06T18:43:43.6290000Z ~ 6ab9a9279a8420a1e6b56b82.jsonl[170] _id=6ac54160de269131f9b6c853 ts=2026-10-06T18:43:43.8510000Z`
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 12 interval(s) ≤ 0.006s..0.007s shown 
  - Evidence: 6ms: 6ab9a9279a8420a1e6b56b82.jsonl[550] _id=6ac54336de269131f9b70191 ts=2026-10-06T18:51:34.0900000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[551] _id=6ac54336de269131f9b70197 ts=2026-10-06T18:51:34.0960000Z; 6ms: 6ab9a9279a8420a1e6b56b82.jsonl[728] _id=6ac54588de269131f9b72bc1 ts=2026-10-06T19:01:27.8410000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[729] _id=6ac54588de269131f9b72bc3 ts=2026-10-06T19:01:27.8470000Z; 7ms: 6ab9a9279a8420a1e6b56b82.jsonl[534] _id=6ac542f8de269131f9b6fc7d ts=2026-10-06T18:50:32.0960000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[541] _id=6ac542f8de269131f9b6fc83 ts=2026-10-06T18:50:32.1030000Z
- **INFO / Info** `InputEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 16 interval(s) ≤ 0.001s..0.002s shown 
  - Evidence: 1ms: 6ab9a9279a8420a1e6b56b82.jsonl[633] _id=6ac544cbde269131f9b71cf3 ts=2026-10-06T18:58:19.1950000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[628] _id=6ac544cbde269131f9b71cf5 ts=2026-10-06T18:58:19.1960000Z; 1ms: 6ab9a9279a8420a1e6b56b82.jsonl[698] _id=6ac54562de269131f9b72869 ts=2026-10-06T19:00:49.6540000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[699] _id=6ac54562de269131f9b7286d ts=2026-10-06T19:00:49.6550000Z; 2ms: 6ab9a9279a8420a1e6b56b82.jsonl[697] _id=6ac54562de269131f9b72867 ts=2026-10-06T19:00:49.6520000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[698] _id=6ac54562de269131f9b72869 ts=2026-10-06T19:00:49.6540000Z
- **INFO / Info** `ObjectInterEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.003s..0.003s shown 
  - Evidence: 3ms: 6ab9a9279a8420a1e6b56b82.jsonl[491] _id=6ac54262de269131f9b6e98f ts=2026-10-06T18:48:02.0180000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[451] _id=6ac54262de269131f9b6e99f ts=2026-10-06T18:48:02.0210000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.009s..0.023s shown 
  - Evidence: 9ms: 6ab9a9279a8420a1e6b56b82.jsonl[605] _id=6ac54483de269131f9b7181b ts=2026-10-06T18:57:06.7230000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[602] _id=6ac54483de269131f9b71821 ts=2026-10-06T18:57:06.7320000Z; 23ms: 6ab9a9279a8420a1e6b56b82.jsonl[514] _id=6ac542c1de269131f9b6f591 ts=2026-10-06T18:49:37.0940000Z -> 6ab9a9279a8420a1e6b56b82.jsonl[515] _id=6ac542c1de269131f9b6f59b ts=2026-10-06T18:49:37.1170000Z

## 7. Sequence / Timing Findings

- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 1 unmatched 'questActiveEvent' (totals: 4 start, 3 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.32s, min -3.96s, max -0.29s over 805 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\6ab9a9279a8420a1e6b56b82\coverage.yaml

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

### `InputEvent` — 424 records

*Purpose:* Raw player input (movement keys, interaction clicks, mode toggles).

- **Scenes:** Unit 1 Dev (424)
- **Intervals:** median 0.62s (p5 0.09s / p95 6.89s, n=423)
- **Fields under `data`:**

```text
data.Value  (string, 424/424 records)
    "pressed"  x424
data.actionType  (string, 424/424 records)
    "Move"  x290
    "Interact"  x124
    "Sprint"  x6
    "Jump"  x4
data.key  (string, 424/424 records)
    "e"  x123
    "w"  x109
    "a"  x76
    "d"  x71
    "s"  x18
    "upArrow"  x10
    "downArrow"  x6
    "leftShift"  x4
    "space"  x4
    "rightShift"  x2
    "leftButton"  x1
data.playerOrDrone  (string, 424/424 records)
    "Player"  x424
```

Raw examples: `event_examples.json` -> `InputEvent`.

### `PlayerPositionEvent` — 188 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 1 Dev (188)
- **Intervals:** median 10.00s (p5 9.94s / p95 10.09s, n=187)
- **Fields under `data`:**

```text
data.position  (object, 188/188 records)
data.position.x  (number, 188/188 records)
    numeric range -24.9692 .. 26.2873 (50 unique)
data.position.y  (number, 188/188 records)
    numeric range 0 .. 0.0203034 (42 unique)
data.position.z  (number, 188/188 records)
    numeric range -119.002 .. 30.8311 (50 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `ObjectInterEvent` — 112 records

*Purpose:* Player interaction prompts with world objects and NPCs.

- **Scenes:** Unit 1 Dev (112)
- **Intervals:** median 0.26s (p5 0.16s / p95 18.19s, n=111)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 112/112 records)
    "E to Talk"  x108
    "Press E to Open Locker"  x2
    "TalkTo"  x2
data.objectName  (string, 112/112 records)
    "Aryn"  x108
    "Player Locker"  x2
    "Jasper"  x1
    "Toppo"  x1
```

Raw examples: `event_examples.json` -> `ObjectInterEvent`.

### `DialogueEvent` — 71 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (71)
- **eventKey:** present on 53 of 71 records
- **Intervals:** median 9.14s (p5 0.01s / p95 79.81s, n=70)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x53; [conversationId, dialogueEventType] x18
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 71/71 records)
    3 unique values (see csv/event_unique_values.csv)
data.dialogueEventType  (string, 71/71 records)
    "DialogueNodeEvent"  x53
    "DialogueFinishEvent"  x9
    "DialogueStartEvent"  x9
data.nodeId  (number, 53/71 records)
    numeric range 1 .. 97 (39 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `questEvent` — 7 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (7)
- **eventKey:** present on 7 of 7 records
- **Intervals:** median 197.24s (p5 0.01s / p95 477.77s, n=6)
- **`data` key-set variants:** [questEventType, questID, questName] x4; [questEventType, questID, questName, questSuccessOrFailure] x3
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
- `DialogueEvent` : median interval between records changed substantially
- `EndOfUnit` : event type present in baseline 09-23-26 but absent now
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