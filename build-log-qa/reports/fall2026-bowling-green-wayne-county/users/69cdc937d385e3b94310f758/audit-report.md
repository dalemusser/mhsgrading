# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f758

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f758
- **Game version string(s) in log:** 20260401-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f758.jsonl
- **Records:** 428 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f758
- **Time span:** 2026-04-13T19:38:22.803000+00:00 .. 2026-04-15T20:08:52.527000+00:00 (48h 30m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f758\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **5 event types**, 428 records, 1 scenes.
- Findings: **0 FAIL**, **34 WARNING**, 23 INFO, 6 NOT_TESTED, 23 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `EndOfUnit`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationToolEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 228 | 53.27 | 1 | 1 | 183 | 2026-04-13T19:38:41.438000+00:00 | 2026-04-15T20:08:49.381000+00:00 | 48h 30m |
| PlayerPositionEvent | 176 | 41.12 | 1 | 1 | 0 | 2026-04-13T19:38:22.803000+00:00 | 2026-04-15T20:08:52.527000+00:00 | 48h 30m |
| questEvent | 15 | 3.5 | 1 | 1 | 15 | 2026-04-13T19:38:41.397000+00:00 | 2026-04-15T20:08:04.073000+00:00 | 48h 29m |
| argumentationNodeEvent | 5 | 1.17 | 1 | 1 | 0 | 2026-04-15T20:04:02.444000+00:00 | 2026-04-15T20:07:12.597000+00:00 | 3m 10s |
| argumentationEvent | 4 | 0.93 | 1 | 1 | 0 | 2026-04-15T20:03:38.334000+00:00 | 2026-04-15T20:07:14.200000+00:00 | 3m 35s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 8.885s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.003s median 
  - Expected: 10.005s in 09-23-26 
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
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 16.822s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 9 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `chatEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameStartEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 6 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowFocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 82 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `gameWindowUnfocusEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 76 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `soilMachine` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 2 Prod (Refactor); Unit 3 Dev; Unit 3 Dungeon Dev; Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DialogueEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 228 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 176 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 5 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 3 - Pollution Upstream; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; 5; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 15 records 
  - Expected: 71 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 16; 17; 18; 19; 21; 22; 23; 24; 25; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Escape the Ruin; Foraged Forging; Forsaken Facility; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Pollution Solution; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; Supply Run; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f758.jsonl[396] _id=69dfeff27957a33870f49cc3 ts=2026-04-15T20:07:14.2230000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 227 | 0.003 | 8.885 | 769.198 | 75.306 | 169350.29 | 0.08 | 40 | 3 |
| PlayerPositionEvent | 175 | 29.903 | 30.003 | 997.884 | 30.576 | 169230.72 | 0.06 | 0 | 1 |
| questEvent | 14 | 0.004 | 239.317 | 12468.763 | 60303.443 | 169538.219 | 0.0 | 4 | 4 |
| argumentationNodeEvent | 4 | 2.602 | 16.822 | 47.538 | 134.658 | 153.908 | 1.26 | 0 | 0 |
| argumentationEvent | 3 | 39.855 | 71.222 | 71.955 | 101.432 | 104.789 | 0.83 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.003s (p5 29.97s, p95 30.58s, n=175) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 2m 
  - Evidence: 47h 2m: 69cdc937d385e3b94310f758.jsonl[147] _id=69dd4d757957a33870f2bc31 ts=2026-04-13T20:09:24.8160000Z -> 69cdc937d385e3b94310f758.jsonl[152] _id=69dfe2fb7957a33870f468cd ts=2026-04-15T19:11:55.1060000Z; 12m 24s: 69cdc937d385e3b94310f758.jsonl[183] _id=69dfe4a67957a33870f46e5b ts=2026-04-15T19:19:01.8810000Z -> 69cdc937d385e3b94310f758.jsonl[211] _id=69dfe78e7957a33870f47b01 ts=2026-04-15T19:31:26.5140000Z; 11m 2s: 69cdc937d385e3b94310f758.jsonl[66] _id=69dd48317957a33870f2a8b9 ts=2026-04-13T19:46:56.8050000Z -> 69cdc937d385e3b94310f758.jsonl[11] _id=69dd4ac87957a33870f2b1f9 ts=2026-04-13T19:57:59.5490000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 40 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f758.jsonl[425] _id=69dff0517957a33870f49f29 ts=2026-04-15T20:08:49.3780000Z -> 69cdc937d385e3b94310f758.jsonl[426] _id=69dff0527957a33870f49f2b ts=2026-04-15T20:08:49.3810000Z; 4ms: 69cdc937d385e3b94310f758.jsonl[407] _id=69dff01f7957a33870f49da5 ts=2026-04-15T20:07:58.6260000Z -> 69cdc937d385e3b94310f758.jsonl[412] _id=69dff01f7957a33870f49da7 ts=2026-04-15T20:07:58.6300000Z; 6ms: 69cdc937d385e3b94310f758.jsonl[155] _id=69dfe3847957a33870f46a81 ts=2026-04-15T19:14:11.6850000Z -> 69cdc937d385e3b94310f758.jsonl[156] _id=69dfe3847957a33870f46a83 ts=2026-04-15T19:14:11.6910000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 47h 0m 
  - Evidence: 47h 0m: 69cdc937d385e3b94310f758.jsonl[18] _id=69dd4de27957a33870f2bce9 ts=2026-04-13T20:11:13.9900000Z -> 69cdc937d385e3b94310f758.jsonl[149] _id=69dfe2f17957a33870f468ab ts=2026-04-15T19:11:44.7100000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 5m 
  - Evidence: 47h 5m: 69cdc937d385e3b94310f758.jsonl[136] _id=69dd4cb17957a33870f2ba35 ts=2026-04-13T20:06:08.6300000Z -> 69cdc937d385e3b94310f758.jsonl[151] _id=69dfe2f37957a33870f468b9 ts=2026-04-15T19:11:46.8490000Z; 24m 44s: 69cdc937d385e3b94310f758.jsonl[241] _id=69dfe8d17957a33870f47fa9 ts=2026-04-15T19:36:49.1030000Z -> 69cdc937d385e3b94310f758.jsonl[358] _id=69dfee9e7957a33870f4968f ts=2026-04-15T20:01:33.8200000Z; 19m 55s: 69cdc937d385e3b94310f758.jsonl[175] _id=69dfe4267957a33870f46cd3 ts=2026-04-15T19:16:53.4150000Z -> 69cdc937d385e3b94310f758.jsonl[236] _id=69dfe8d17957a33870f47fa5 ts=2026-04-15T19:36:49.0900000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.004s..0.015s shown 
  - Evidence: 4ms: 69cdc937d385e3b94310f758.jsonl[358] _id=69dfee9e7957a33870f4968f ts=2026-04-15T20:01:33.8200000Z -> 69cdc937d385e3b94310f758.jsonl[363] _id=69dfee9e7957a33870f49691 ts=2026-04-15T20:01:33.8240000Z; 13ms: 69cdc937d385e3b94310f758.jsonl[236] _id=69dfe8d17957a33870f47fa5 ts=2026-04-15T19:36:49.0900000Z -> 69cdc937d385e3b94310f758.jsonl[241] _id=69dfe8d17957a33870f47fa9 ts=2026-04-15T19:36:49.1030000Z; 15ms: 69cdc937d385e3b94310f758.jsonl[174] _id=69dfe4257957a33870f46ccf ts=2026-04-15T19:16:53.4000000Z -> 69cdc937d385e3b94310f758.jsonl[175] _id=69dfe4267957a33870f46cd3 ts=2026-04-15T19:16:53.4150000Z

## 7. Sequence / Timing Findings

- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 11 unmatched 'DialogueStartEvent' (totals: 28 start, 17 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 3 unmatched 'questActiveEvent' (totals: 9 start, 6 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.39s, min -0.95s, max -0.34s over 428 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f758\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | partial |
| Unit2 | skipped |
| Unit3 | skipped |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `EndOfUnit` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 5] 
  - Evidence: coverage: Unit1=partial, Unit3=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=partial, Unit2=skipped, Unit3=skipped, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
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

### `DialogueEvent` — 228 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (228)
- **eventKey:** present on 183 of 228 records
- **Intervals:** median 8.88s (p5 0.01s / p95 75.31s, n=227)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x183; [conversationId, dialogueEventType] x45
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 228/228 records)
    7 unique values (see csv/event_unique_values.csv)
data.dialogueEventType  (string, 228/228 records)
    "DialogueNodeEvent"  x183
    "DialogueStartEvent"  x28
    "DialogueFinishEvent"  x17
data.nodeId  (number, 183/228 records)
    numeric range 0 .. 104 (82 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 176 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 1 Dev (176)
- **Intervals:** median 30.00s (p5 29.97s / p95 30.58s, n=175)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 176/176 records)
data.position.x  (number, 176/176 records)
    numeric range -26.9548 .. 30.2367 (87 unique)
data.position.y  (number, 176/176 records)
    numeric range -5.5802 .. 0.0242198 (84 unique)
data.position.z  (number, 176/176 records)
    numeric range -130.306 .. 108.403 (87 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 15 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (15)
- **eventKey:** present on 15 of 15 records
- **Intervals:** median 239.32s (p5 0.01s / p95 60303.44s, n=14)
- **`data` key-set variants:** [questEventType, questID, questName] x9; [questEventType, questID, questName, questSuccessOrFailure] x6
- **Fields under `data`:**

```text
data.questEventType  (string, 15/15 records)
    "questActiveEvent"  x9
    "questFinishEvent"  x6
data.questID  (string, 15/15 records)
    "29"  x4
    "28"  x3
    "31"  x3
    "32"  x2
    "33"  x2
    "34"  x1
data.questName  (string, 15/15 records)
    "Gear Up"  x4
    "Getting Your Space Legs"  x3
    "TK, Reporting In!"  x3
    "Defend the Expedition"  x2
    "Info and Intros"  x2
    "What Was That?"  x1
data.questSuccessOrFailure  (string, 6/15 records)
    "Succeeded"  x6
```

Raw examples: `event_examples.json` -> `questEvent`.

### `argumentationNodeEvent` — 5 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (5)
- **Intervals:** median 16.82s (p5 3.42s / p95 134.66s, n=4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 5/5 records)
    "argumentationNodeAdd"  x5
data.argumentationTitle  (string, 5/5 records)
    "Unit 1 - Freshwater"  x3
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 5/5 records)
    "1"  x2
    "A"  x1
    "B"  x1
    "I"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 4 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4)
- **Intervals:** median 71.22s (p5 42.99s / p95 101.43s, n=3)
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

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DEBUGMenu` : expected event type absent although its content was played — possible logging failure
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `EndOfUnit` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : expected event type absent although its content was played — possible logging failure
- `ObjectInterEvent` : expected event type absent although its content was played — possible logging failure
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationToolEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now
- `DialogueEvent` : median interval between records changed substantially

**Additional gameplay testing (content not exercised):**
- `PuzzlePieceVisibleEvent`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected event type absent, but its content was not exercised this playthrough
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*