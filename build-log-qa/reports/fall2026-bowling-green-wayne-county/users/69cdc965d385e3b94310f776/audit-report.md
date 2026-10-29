# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f776

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f776
- **Game version string(s) in log:** 20260401-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f776.jsonl
- **Records:** 309 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f776
- **Time span:** 2026-04-20T19:08:55.628000+00:00 .. 2026-04-20T19:40:01.640000+00:00 (31m 6s)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f776\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **8 event types**, 309 records, 2 scenes.
- Findings: **0 FAIL**, **36 WARNING**, 32 INFO, 6 NOT_TESTED, 30 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `EndOfUnit`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TopographicMapEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 213 | 68.93 | 1 | 2 | 137 | 2026-04-20T19:09:06.601000+00:00 | 2026-04-20T19:35:00.309000+00:00 | 25m 53s |
| PlayerPositionEvent | 62 | 20.06 | 1 | 2 | 0 | 2026-04-20T19:08:55.628000+00:00 | 2026-04-20T19:40:01.640000+00:00 | 31m 6s |
| argumentationNodeEvent | 17 | 5.5 | 1 | 1 | 0 | 2026-04-20T19:24:22.695000+00:00 | 2026-04-20T19:26:31.843000+00:00 | 2m 9s |
| questEvent | 6 | 1.94 | 1 | 2 | 6 | 2026-04-20T19:10:56.159000+00:00 | 2026-04-20T19:30:49.950000+00:00 | 19m 53s |
| Topographic Map Event | 4 | 1.29 | 1 | 1 | 0 | 2026-04-20T19:14:12.451000+00:00 | 2026-04-20T19:21:53.822000+00:00 | 7m 41s |
| argumentationEvent | 3 | 0.97 | 1 | 1 | 0 | 2026-04-20T19:23:34.981000+00:00 | 2026-04-20T19:26:36.705000+00:00 | 3m 1s |
| Soil Key Puzzle | 2 | 0.65 | 1 | 1 | 0 | 2026-04-20T19:29:25.983000+00:00 | 2026-04-20T19:30:09.211000+00:00 | 43.2s |
| argumentationToolEvent | 2 | 0.65 | 1 | 1 | 0 | 2026-04-20T19:25:30.101000+00:00 | 2026-04-20T19:25:36.263000+00:00 | 6.2s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
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
  - Observed: 30.008s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 43.228s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
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
  - Observed: 5.046s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 6.162s median 
  - Expected: 17.074s in 09-23-26 
  - Evidence: regression candidate requiring review
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
  - Observed: MainMenu; Transition; Unit 1 Dev; Unit 2 Prod (Refactor); Unit 4 Dev; Unit 4 Dev - Anderson Base; Unit 4 Dev - Dungeon; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `DialogueEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 213 records 
  - Expected: 1943 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `PlayerPositionEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 62 records 
  - Expected: 1304 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.1x vs baseline. 
  - Observed: 2 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Soil Key Puzzle` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 Prod (Refactor); Unit 4 Dev 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `argumentationEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 3 records 
  - Expected: 14 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit; U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 1 - Does the planet WAT-247 have freshwater; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 1 - Freshwater; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 17 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 1 - Freshwater; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 2 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 6 records 
  - Expected: 71 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 19; 21; 22; 23; 24; 25; 28; 29; 31; 32; 33; 34; 36; 39; 40; 41; 43; 44; 45; 46; 47; 48; 49; 50; 51; 52; 53; 54; 55; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Defend the Expedition; Desert Delicacies; Escape the Ruin; Foraged Forging; Gear Up; Getting Your Space Legs; Getting the Band Back Together; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Info and Intros; Investigate the Temple; Leader of Evidence; Part of a Balanced Ecosystem; Power Play; Power Play - Floor 1; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; TK, Reporting In!; WAT Happened Here?; Water Problems Require Water Solutions; Well, What Have We Here?; What Was That?; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'DialogueNodeEvent:84:0' vs expected 'DialogueNodeEvent:84:36' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f776.jsonl[254] _id=69e67ded1724f0c9e2f8ddd3 ts=2026-04-20T19:26:36.6650000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 212 | 0.003 | 2.026 | 7.329 | 34.643 | 92.043 | 8.19 | 69 | 0 |
| PlayerPositionEvent | 60 | 29.941 | 30.008 | 30.742 | 32.884 | 48.203 | 1.95 | 0 | 0 |
| argumentationNodeEvent | 16 | 1.081 | 5.046 | 8.072 | 24.726 | 34.403 | 7.43 | 0 | 0 |
| questEvent | 5 | 26.451 | 183.321 | 238.758 | 470.46 | 478.501 | 0.25 | 0 | 0 |
| Topographic Map Event | 3 | 6.893 | 11.005 | 153.79 | 400.226 | 443.473 | 0.39 | 0 | 0 |
| argumentationEvent | 2 | 0.072 | 90.862 | 90.862 | 172.573 | 181.652 | 0.66 | 0 | 0 |
| Soil Key Puzzle | 1 | 43.228 | 43.228 | 43.228 | 43.228 | 43.228 | 1.39 | 0 | 0 |
| argumentationToolEvent | 1 | 6.162 | 6.162 | 6.162 | 6.162 | 6.162 | 9.74 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.96s, p95 32.88s, n=60) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `72ms: 69cdc965d385e3b94310f776.jsonl[255] _id=69e67dec1724f0c9e2f8ddd1 ts=2026-04-20T19:26:36.6330000Z ~ 69cdc965d385e3b94310f776.jsonl[106] _id=69e67ded1724f0c9e2f8ddd7 ts=2026-04-20T19:26:36.7050000Z`
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 69 interval(s) ≤ 0.003s..0.006s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f776.jsonl[283] _id=69e67ed01724f0c9e2f8e243 ts=2026-04-20T19:30:24.3850000Z -> 69cdc965d385e3b94310f776.jsonl[284] _id=69e67ed01724f0c9e2f8e245 ts=2026-04-20T19:30:24.3880000Z; 5ms: 69cdc965d385e3b94310f776.jsonl[254] _id=69e67ded1724f0c9e2f8ddd3 ts=2026-04-20T19:26:36.6650000Z -> 69cdc965d385e3b94310f776.jsonl[105] _id=69e67ded1724f0c9e2f8ddd5 ts=2026-04-20T19:26:36.6700000Z; 6ms: 69cdc965d385e3b94310f776.jsonl[197] _id=69e67c111724f0c9e2f8d4bd ts=2026-04-20T19:18:40.9320000Z -> 69cdc965d385e3b94310f776.jsonl[199] _id=69e67c111724f0c9e2f8d4c5 ts=2026-04-20T19:18:40.9380000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 1 record(s) match the trigger in 69cdc965d385e3b94310f776.jsonl:69cdc965d385e3b94310f776, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f776.jsonl[280] _id=69e67ec11724f0c9e2f8e211 ts=2026-04-20T19:30:09.2110000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f776.jsonl[190] _id=69e67bbf1724f0c9e2f8d37d ts=2026-04-20T19:17:18.8880000Z`; `69cdc965d385e3b94310f776.jsonl[199] _id=69e67c111724f0c9e2f8d4c5 ts=2026-04-20T19:18:40.9380000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f776.jsonl[106] _id=69e67ded1724f0c9e2f8ddd7 ts=2026-04-20T19:26:36.7050000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 48 unmatched 'DialogueStartEvent' (totals: 61 start, 15 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 2 unmatched 'questActiveEvent' (totals: 4 start, 2 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.28s, min -0.90s, max -0.25s over 309 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f776\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | skipped |
| Unit2 | skipped |
| Unit3 | partial |
| Unit4 | skipped |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `EndOfUnit` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=skipped, Unit3=partial, Unit4=skipped 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TopographicMapEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3] 
  - Evidence: coverage: Unit1=skipped, Unit3=partial 
  - Spec source: 08-13-26/Investigation-results/topographic-map-event-investigation.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=skipped, Unit2=skipped, Unit3=partial, Unit4=skipped, Unit5=skipped 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
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
- **NOT_TESTED / NotTested** `chatEvent` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage manifest: ['skipped', 'skipped'] 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **NOT_TESTED / NotTested** `soilMachine` — expected event type absent, but its content was not exercised this playthrough. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage manifest: ['skipped'] 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md

## 9. Event-Type Details

### `DialogueEvent` — 213 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (178); Unit 3 Dungeon Dev (35)
- **eventKey:** present on 137 of 213 records
- **Intervals:** median 2.03s (p5 0.01s / p95 34.64s, n=212)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x137; [conversationId, dialogueEventType] x76
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 213/213 records)
    8 unique values (see csv/event_unique_values.csv)
data.dialogueEventType  (string, 213/213 records)
    "DialogueNodeEvent"  x137
    "DialogueStartEvent"  x61
    "DialogueFinishEvent"  x15
data.nodeId  (number, 137/213 records)
    numeric range 0 .. 230 (90 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 62 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (42); Unit 3 Dungeon Dev (20)
- **Intervals:** median 30.01s (p5 29.96s / p95 32.88s, n=60)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 62/62 records)
data.position.x  (number, 62/62 records)
    numeric range -562.503 .. 451.449 (30 unique)
data.position.y  (number, 62/62 records)
    numeric range -112.675 .. -30.8031 (26 unique)
data.position.z  (number, 62/62 records)
    numeric range -952.488 .. 284.874 (30 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `argumentationNodeEvent` — 17 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 3 Dev (17)
- **Intervals:** median 5.05s (p5 1.20s / p95 24.73s, n=16)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 17/17 records)
    "argumentationNodeAdd"  x10
    "argumentationNodeRemove"  x7
data.argumentationTitle  (string, 17/17 records)
    "Unit 3 - Pollution Upstream"  x17
data.nodeName  (string, 17/17 records)
    "2"  x4
    "I"  x3
    "1"  x2
    "3"  x2
    "4"  x2
    "B"  x2
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `questEvent` — 6 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 3 Dev (5); Unit 3 Dungeon Dev (1)
- **eventKey:** present on 6 of 6 records
- **Intervals:** median 183.32s (p5 34.60s / p95 470.46s, n=5)
- **`data` key-set variants:** [questEventType, questID, questName] x4; [questEventType, questID, questName, questSuccessOrFailure] x2
- **Fields under `data`:**

```text
data.questEventType  (string, 6/6 records)
    "questActiveEvent"  x4
    "questFinishEvent"  x2
data.questID  (string, 6/6 records)
    "16"  x2
    "17"  x2
    "18"  x2
data.questName  (string, 6/6 records)
    "Forsaken Facility"  x2
    "Pollution Solution"  x2
    "Supply Run"  x2
data.questSuccessOrFailure  (string, 2/6 records)
    "Succeeded"  x2
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 4 records

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 11.01s (p5 7.30s / p95 400.23s, n=3)
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "MapCloseEvent"  x2
    "MapOpenEvent"  x2
data.featureUsed  (string, 4/4 records)
    "Map"  x4
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationEvent` — 3 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 3 Dev (3)
- **Intervals:** median 90.86s (p5 9.15s / p95 172.57s, n=2)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 3/3 records)
    "argumentationSessionClose"  x2
    "argumentationSessionOpen"  x1
data.argumentationDescription  (string, 3/3 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
data.argumentationTitle  (string, 3/3 records)
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 2 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 43.23s (p5 43.23s / p95 43.23s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 2/2 records)
    "Finished"  x1
    "Started"  x1
data.Unit  (string, 2/2 records)
    "Unit 3 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 6.16s (p5 6.16s / p95 6.16s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "argumentationToolClose"  x1
    "argumentationToolOpen"  x1
data.argumentationTitle  (string, 2/2 records)
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 2/2 records)
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DEBUGMenu` : expected event type absent although its content was played — possible logging failure
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `EndOfUnit` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : expected event type absent although its content was played — possible logging failure
- `ObjectInterEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : expected event type absent although its content was played — possible logging failure
- `TopographicMapEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now
- `EndOfUnit` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (7x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `TerasGardenBox`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough
- `chatEvent`: expected event type absent, but its content was not exercised this playthrough
- `soilMachine`: expected event type absent, but its content was not exercised this playthrough
- `Soil Key Puzzle`: expected scene 'Unit 4 Dev' has no records of this event


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*