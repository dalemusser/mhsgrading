# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f77d
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f77d.jsonl
- **Records:** 1889 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f77d
- **Time span:** 2026-04-14T14:06:28.749000+00:00 .. 2026-04-28T14:33:58.439000+00:00 (336h 27m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **10 event types**, 1889 records, 6 scenes.
- Findings: **0 FAIL**, **46 WARNING**, 51 INFO, 2 NOT_TESTED, 32 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `TerasGardenBox`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1202 | 63.63 | 1 | 6 | 823 | 2026-04-14T14:06:47.741000+00:00 | 2026-04-28T14:33:46.178000+00:00 | 336h 26m |
| PlayerPositionEvent | 531 | 28.11 | 1 | 6 | 0 | 2026-04-14T14:06:28.749000+00:00 | 2026-04-28T14:33:58.439000+00:00 | 336h 27m |
| questEvent | 56 | 2.96 | 1 | 6 | 56 | 2026-04-14T14:06:47.703000+00:00 | 2026-04-28T14:33:33.230000+00:00 | 336h 26m |
| Topographic Map Event | 55 | 2.91 | 1 | 3 | 0 | 2026-04-16T14:13:36.553000+00:00 | 2026-04-24T14:26:36.194000+00:00 | 192h 12m |
| argumentationNodeEvent | 21 | 1.11 | 1 | 2 | 0 | 2026-04-14T14:30:12.809000+00:00 | 2026-04-22T13:32:49.113000+00:00 | 191h 2m |
| argumentationEvent | 10 | 0.53 | 1 | 2 | 0 | 2026-04-14T14:29:24.878000+00:00 | 2026-04-22T13:32:51.411000+00:00 | 191h 3m |
| Soil Key Puzzle | 9 | 0.48 | 1 | 3 | 0 | 2026-04-16T14:03:58.592000+00:00 | 2026-04-28T14:30:15.638000+00:00 | 288h 26m |
| EndOfUnit | 2 | 0.11 | 1 | 2 | 0 | 2026-04-16T13:43:04.388000+00:00 | 2026-04-24T14:32:16.001000+00:00 | 192h 49m |
| argumentationToolEvent | 2 | 0.11 | 1 | 1 | 0 | 2026-04-22T13:31:31.633000+00:00 | 2026-04-22T13:31:33.758000+00:00 | 2.1s |
| TopographicMapEvent | 1 | 0.05 | 1 | 1 | 0 | 2026-04-16T14:13:45.161000+00:00 | 2026-04-16T14:13:45.161000+00:00 | 0.0s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 694151.613s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.009s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 312.907s median 
  - Expected: 0.8s in 09-23-26 
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
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationEvent` — median interval between records changed substantially. 
  - Observed: 29.504s median 
  - Expected: 66.927s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.694s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 2.125s median 
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
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 9 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 55 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 1 records 
  - Expected: 83 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: MapCloseEvent; MapOpenEvent; Selected; Unselected; WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: dragStart 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — baseline categorical value(s) not seen this build. 
  - Observed: Legend; Map; Waypoint 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.featureUsed` — categorical value(s) not seen in baseline. 
  - Observed: waypoint 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationEvent` `data.argumentationDescription` — baseline categorical value(s) not seen this build. 
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 21 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; C; D; II 
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
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 36; 40; 41; 43; 44; 45; 47; 48; 49; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 2; Power Play - Floor 3; Power Play - Floor 4; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 106 mismatch(es); e.g. 'DialogueNodeEvent:31:73' vs expected 'DialogueNodeEvent:31:74' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[99] _id=69de4f4b7957a33870f36666 ts=2026-04-14T14:29:30.6600000Z`; `69cdc965d385e3b94310f77d.jsonl[146] _id=69e0e6587957a33870f50259 ts=2026-04-16T13:38:32.6380000Z`; `69cdc965d385e3b94310f77d.jsonl[211] _id=69e0eee87957a33870f53801 ts=2026-04-16T13:58:38.0900000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'questFinishEvent:21' vs expected 'questFinishEvent:23' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[234] _id=69e0f33f7957a33870f5551b ts=2026-04-16T14:04:51.7300000Z`; `69cdc965d385e3b94310f77d.jsonl[266] _id=69e0f3477957a33870f555ab ts=2026-04-16T14:08:18.9810000Z`; `69cdc965d385e3b94310f77d.jsonl[1326] _id=69e62c2c1724f0c9e2f86677 ts=2026-04-20T13:37:46.7760000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 55 records, TopographicMapEvent: 1 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1201 | 0.0 | 2.297 | 1008.508 | 54.505 | 345132.965 | 0.06 | 317 | 7 |
| PlayerPositionEvent | 524 | 0.0 | 30.009 | 2310.879 | 40.156 | 345040.285 | 0.03 | 2 | 5 |
| questEvent | 55 | 0.001 | 192.393 | 22021.919 | 170087.115 | 345349.967 | 0.0 | 9 | 11 |
| Topographic Map Event | 54 | 1.24 | 22.492 | 12814.438 | 61143.889 | 344004.366 | 0.0 | 0 | 5 |
| argumentationNodeEvent | 20 | 1.229 | 5.694 | 34387.815 | 187025.999 | 518000.88 | 0.0 | 0 | 2 |
| argumentationEvent | 9 | 0.118 | 29.504 | 76422.948 | 378635.212 | 517976.362 | 0.0 | 0 | 2 |
| Soil Key Puzzle | 8 | 2.952 | 312.907 | 129797.131 | 459089.583 | 521505.736 | 0.0 | 0 | 3 |
| EndOfUnit | 1 | 694151.613 | 694151.613 | 694151.613 | 694151.613 | 694151.613 | 0.0 | 0 | 1 |
| argumentationToolEvent | 1 | 2.125 | 2.125 | 2.125 | 2.125 | 2.125 | 28.24 | 0 | 0 |
| TopographicMapEvent | 0 |  |  |  |  |  | 0.0 | 0 | 0 |

- **WARNING / Medium** `PlayerPositionEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[208] _id=69e0ea827957a33870f51e95 ts=2026-04-16T13:56:18.2630000Z == 69cdc965d385e3b94310f77d.jsonl[210] _id=69e0eec87957a33870f53773 ts=2026-04-16T13:56:18.2630000Z`; `69cdc965d385e3b94310f77d.jsonl[1226] _id=69e0ef447957a33870f53a03 ts=2026-04-16T14:01:51.0610000Z == 69cdc965d385e3b94310f77d.jsonl[1228] _id=69e0f33c7957a33870f554eb ts=2026-04-16T14:01:51.0610000Z`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.009s (p5 29.95s, p95 40.16s, n=524) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `118ms: 69cdc965d385e3b94310f77d.jsonl[1543] _id=69e8ce041724f0c9e2fa21c7 ts=2026-04-22T13:32:51.2930000Z ~ 69cdc965d385e3b94310f77d.jsonl[1542] _id=69e8ce041724f0c9e2fa21d3 ts=2026-04-22T13:32:51.4110000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 5 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `8ms: 69cdc965d385e3b94310f77d.jsonl[1326] _id=69e62c2c1724f0c9e2f86677 ts=2026-04-20T13:37:46.7760000Z ~ 69cdc965d385e3b94310f77d.jsonl[456] _id=69e62c2c1724f0c9e2f8667d ts=2026-04-20T13:37:46.7840000Z`; `1ms: 69cdc965d385e3b94310f77d.jsonl[1356] _id=69e62db21724f0c9e2f86fad ts=2026-04-20T13:44:16.6350000Z ~ 69cdc965d385e3b94310f77d.jsonl[473] _id=69e62db21724f0c9e2f86fb1 ts=2026-04-20T13:44:16.6360000Z`; `1ms: 69cdc965d385e3b94310f77d.jsonl[474] _id=69e62e121724f0c9e2f87161 ts=2026-04-20T13:45:52.2920000Z ~ 69cdc965d385e3b94310f77d.jsonl[1358] _id=69e62e121724f0c9e2f87165 ts=2026-04-20T13:45:52.2930000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 95h 52m 
  - Evidence: 95h 52m: 69cdc965d385e3b94310f77d.jsonl[923] _id=69eb7f1b1724f0c9e2fba07d ts=2026-04-24T14:32:58.5940000Z -> 69cdc965d385e3b94310f77d.jsonl[928] _id=69f0c3481724f0c9e2fcafa1 ts=2026-04-28T14:25:11.5590000Z; 94h 52m: 69cdc965d385e3b94310f77d.jsonl[366] _id=69e0f35c7957a33870f5571f ts=2026-04-16T14:30:37.0760000Z -> 69cdc965d385e3b94310f77d.jsonl[1251] _id=69e628c61724f0c9e2f85079 ts=2026-04-20T13:23:17.0570000Z; 47h 25m: 69cdc965d385e3b94310f77d.jsonl[1712] _id=69e8dbfb1724f0c9e2fa7587 ts=2026-04-22T14:32:27.0000000Z -> 69cdc965d385e3b94310f77d.jsonl[783] _id=69eb76eb1724f0c9e2fb76ff ts=2026-04-24T13:58:02.4270000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 317 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77d.jsonl[1877] _id=69eb7ef01724f0c9e2fb9f77 ts=2026-04-24T14:32:16.0330000Z -> 69cdc965d385e3b94310f77d.jsonl[1878] _id=69eb7f001724f0c9e2fb9fc5 ts=2026-04-24T14:32:16.033Z; 3ms: 69cdc965d385e3b94310f77d.jsonl[1559] _id=69e8cf5f1724f0c9e2fa2b49 ts=2026-04-22T13:38:38.2860000Z -> 69cdc965d385e3b94310f77d.jsonl[679] _id=69e8cf5f1724f0c9e2fa2b4b ts=2026-04-22T13:38:38.2890000Z; 3ms: 69cdc965d385e3b94310f77d.jsonl[160] _id=69e0e6b17957a33870f50495 ts=2026-04-16T13:40:01.7510000Z -> 69cdc965d385e3b94310f77d.jsonl[1158] _id=69e0e6b27957a33870f50499 ts=2026-04-16T13:40:01.7540000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 192h 49m 
  - Evidence: 192h 49m: 69cdc965d385e3b94310f77d.jsonl[1176] _id=69e0e7687957a33870f509f7 ts=2026-04-16T13:43:04.3880000Z -> 69cdc965d385e3b94310f77d.jsonl[1876] _id=69eb7ef01724f0c9e2fb9f75 ts=2026-04-24T14:32:16.0010000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 50m 
  - Evidence: 95h 50m: 69cdc965d385e3b94310f77d.jsonl[1880] _id=69eb7f661724f0c9e2fba261 ts=2026-04-24T14:34:13.8250000Z -> 69cdc965d385e3b94310f77d.jsonl[930] _id=69f0c3371724f0c9e2fcaf68 ts=2026-04-28T14:24:54.1100000Z; 94h 43m: 69cdc965d385e3b94310f77d.jsonl[1240] _id=69e0f3b17957a33870f558f9 ts=2026-04-16T14:35:29.4970000Z -> 69cdc965d385e3b94310f77d.jsonl[401] _id=69e627ae1724f0c9e2f84b4d ts=2026-04-20T13:18:36.9840000Z; 47h 25m: 69cdc965d385e3b94310f77d.jsonl[1714] _id=69e8dbf81724f0c9e2fa7585 ts=2026-04-22T14:32:24.3370000Z -> 69cdc965d385e3b94310f77d.jsonl[1716] _id=69eb76e91724f0c9e2fb76f5 ts=2026-04-24T13:58:00.4780000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 2 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f77d.jsonl[1226] _id=69e0ef447957a33870f53a03 ts=2026-04-16T14:01:51.0610000Z -> 69cdc965d385e3b94310f77d.jsonl[1228] _id=69e0f33c7957a33870f554eb ts=2026-04-16T14:01:51.0610000Z; 0ms: 69cdc965d385e3b94310f77d.jsonl[208] _id=69e0ea827957a33870f51e95 ts=2026-04-16T13:56:18.2630000Z -> 69cdc965d385e3b94310f77d.jsonl[210] _id=69e0eec87957a33870f53773 ts=2026-04-16T13:56:18.2630000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 144h 51m 
  - Evidence: 144h 51m: 69cdc965d385e3b94310f77d.jsonl[680] _id=69e8cf451724f0c9e2fa2a6f ts=2026-04-22T13:38:12.8930000Z -> 69cdc965d385e3b94310f77d.jsonl[956] _id=69f0c4671724f0c9e2fcb1d9 ts=2026-04-28T14:29:58.6290000Z; 95h 19m: 69cdc965d385e3b94310f77d.jsonl[231] _id=69e0f33e7957a33870f55515 ts=2026-04-16T14:04:01.6140000Z -> 69cdc965d385e3b94310f77d.jsonl[409] _id=69e628d81724f0c9e2f850f9 ts=2026-04-20T13:23:35.4850000Z; 48h 4m: 69cdc965d385e3b94310f77d.jsonl[1300] _id=69e62b301724f0c9e2f85f0f ts=2026-04-20T13:33:35.3760000Z -> 69cdc965d385e3b94310f77d.jsonl[676] _id=69e8cf281724f0c9e2fa29b3 ts=2026-04-22T13:37:44.0180000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 33m 
  - Evidence: 95h 33m: 69cdc965d385e3b94310f77d.jsonl[1237] _id=69e0f3567957a33870f556c5 ts=2026-04-16T14:26:03.3000000Z -> 69cdc965d385e3b94310f77d.jsonl[1395] _id=69e631401724f0c9e2f8829b ts=2026-04-20T13:59:27.6660000Z; 47h 58m: 69cdc965d385e3b94310f77d.jsonl[1692] _id=69e8da151724f0c9e2fa6d97 ts=2026-04-22T14:24:20.5580000Z -> 69cdc965d385e3b94310f77d.jsonl[882] _id=69eb7cb61724f0c9e2fb94b1 ts=2026-04-24T14:22:46.0340000Z; 46h 45m: 69cdc965d385e3b94310f77d.jsonl[554] _id=69e6399f1724f0c9e2f8b567 ts=2026-04-20T14:35:10.6530000Z -> 69cdc965d385e3b94310f77d.jsonl[1493] _id=69e8cb451724f0c9e2fa1105 ts=2026-04-22T13:21:08.8160000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 52m 
  - Evidence: 143h 52m: 69cdc965d385e3b94310f77d.jsonl[145] _id=69e0e6587957a33870f50257 ts=2026-04-16T13:38:32.6050000Z -> 69cdc965d385e3b94310f77d.jsonl[626] _id=69e8cdb11724f0c9e2fa1f4d ts=2026-04-22T13:31:28.9670000Z; 47h 7m: 69cdc965d385e3b94310f77d.jsonl[106] _id=69de4f5f7957a33870f367b0 ts=2026-04-14T14:29:50.8420000Z -> 69cdc965d385e3b94310f77d.jsonl[1141] _id=69e0e5f77957a33870f5005b ts=2026-04-16T13:36:54.3300000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 143h 53m 
  - Evidence: 143h 53m: 69cdc965d385e3b94310f77d.jsonl[1146] _id=69e0e6557957a33870f5024b ts=2026-04-16T13:38:29.8480000Z -> 69cdc965d385e3b94310f77d.jsonl[1537] _id=69e8cdc71724f0c9e2fa1fdd ts=2026-04-22T13:31:50.7280000Z; 47h 6m: 69cdc965d385e3b94310f77d.jsonl[1116] _id=69de4fbd7957a33870f36a7e ts=2026-04-14T14:31:24.9460000Z -> 69cdc965d385e3b94310f77d.jsonl[1145] _id=69e0e6437957a33870f501ef ts=2026-04-16T13:38:11.2140000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 11 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 69cdc965d385e3b94310f77d.jsonl[1875] _id=69eb7eec1724f0c9e2fb9f53 ts=2026-04-24T14:32:12.1600000Z -> 69cdc965d385e3b94310f77d.jsonl[926] _id=69f0c3f21724f0c9e2fcb119 ts=2026-04-28T14:28:02.1270000Z; 95h 5m: 69cdc965d385e3b94310f77d.jsonl[300] _id=69e0f34c7957a33870f55611 ts=2026-04-16T14:13:25.9140000Z -> 69cdc965d385e3b94310f77d.jsonl[1241] _id=69e627b31724f0c9e2f84b5f ts=2026-04-20T13:18:41.4040000Z; 47h 28m: 69cdc965d385e3b94310f77d.jsonl[770] _id=69e8db5e1724f0c9e2fa74d5 ts=2026-04-22T14:29:49.2280000Z -> 69cdc965d385e3b94310f77d.jsonl[782] _id=69eb76eb1724f0c9e2fb76fd ts=2026-04-24T13:58:02.2080000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 9 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 69cdc965d385e3b94310f77d.jsonl[1356] _id=69e62db21724f0c9e2f86fad ts=2026-04-20T13:44:16.6350000Z -> 69cdc965d385e3b94310f77d.jsonl[473] _id=69e62db21724f0c9e2f86fb1 ts=2026-04-20T13:44:16.6360000Z; 1ms: 69cdc965d385e3b94310f77d.jsonl[474] _id=69e62e121724f0c9e2f87161 ts=2026-04-20T13:45:52.2920000Z -> 69cdc965d385e3b94310f77d.jsonl[1358] _id=69e62e121724f0c9e2f87165 ts=2026-04-20T13:45:52.2930000Z; 1ms: 69cdc965d385e3b94310f77d.jsonl[476] _id=69e62ebc1724f0c9e2f87507 ts=2026-04-20T13:48:42.1450000Z -> 69cdc965d385e3b94310f77d.jsonl[1362] _id=69e62ebc1724f0c9e2f87509 ts=2026-04-20T13:48:42.1460000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc965d385e3b94310f77d.jsonl:69cdc965d385e3b94310f77d, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[226] _id=69e0f33e7957a33870f55511 ts=2026-04-16T14:03:58.5920000Z`; `69cdc965d385e3b94310f77d.jsonl[231] _id=69e0f33e7957a33870f55515 ts=2026-04-16T14:04:01.6140000Z`; `69cdc965d385e3b94310f77d.jsonl[1300] _id=69e62b301724f0c9e2f85f0f ts=2026-04-20T13:33:35.3760000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 1 record(s) match the trigger in 69cdc965d385e3b94310f77d.jsonl:69cdc965d385e3b94310f77d, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[302] _id=69e0f34d7957a33870f5561f ts=2026-04-16T14:13:45.1610000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[1220] _id=69e0eef67957a33870f53843 ts=2026-04-16T13:58:57.3040000Z`; `69cdc965d385e3b94310f77d.jsonl[1383] _id=69e631a21724f0c9e2f884fe ts=2026-04-20T14:01:06.3850000Z`; `69cdc965d385e3b94310f77d.jsonl[522] _id=69e632841724f0c9e2f88a67 ts=2026-04-20T14:04:51.6050000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'Finished' preceded by 'Started' per Unit 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[226] _id=69e0f33e7957a33870f55511 ts=2026-04-16T14:03:58.5920000Z`; `69cdc965d385e3b94310f77d.jsonl[231] _id=69e0f33e7957a33870f55515 ts=2026-04-16T14:04:01.6140000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[1542] _id=69e8ce041724f0c9e2fa21d3 ts=2026-04-22T13:32:51.4110000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[234] _id=69e0f33f7957a33870f5551b ts=2026-04-16T14:04:51.7300000Z`; `69cdc965d385e3b94310f77d.jsonl[298] _id=69e0f34c7957a33870f55609 ts=2026-04-16T14:13:06.5130000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[1297] _id=69e62b2d1724f0c9e2f85edb ts=2026-04-20T13:33:32.4240000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationEvent` `actionType` — argumentation session: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f77d.jsonl[140] _id=69e0e63b7957a33870f501c5 ts=2026-04-16T13:38:03.1010000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 170 unmatched 'DialogueStartEvent' (totals: 273 start, 106 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 4 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 5 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 26 unmatched 'questActiveEvent' (totals: 40 start, 16 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.82s, min -1901.73s, max +0.01s over 1889 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f77d\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | partial |
| Unit3 | complete |
| Unit4 | partial |
| Unit5 | skipped |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=partial, Unit3=complete, Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `TerasGardenBox` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/tara-garden-box.md
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=skipped 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=partial, Unit3=complete, Unit4=partial, Unit5=skipped 
  - Spec source: observed data
- **WARNING / Medium** `soilMachine` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [4] 
  - Evidence: coverage: Unit4=partial 
  - Spec source: 08-13-26/Investigation-results/soil-machine-investigation.md
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 55 records 
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

### `DialogueEvent` — 1202 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 3 Dev (322); Unit 2 Prod (Refactor) (311); Unit 3 Dungeon Dev (263); Unit 1 Dev (261); Unit 4 Dev (28); Unit 4 Dev - Dungeon (17)
- **eventKey:** present on 823 of 1202 records
- **Intervals:** median 2.30s (p5 0.01s / p95 54.51s, n=1201)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x823; [conversationId, dialogueEventType] x379
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1202/1202 records)
    numeric range 10 .. 104 (30 unique)
data.dialogueEventType  (string, 1202/1202 records)
    "DialogueNodeEvent"  x823
    "DialogueStartEvent"  x273
    "DialogueFinishEvent"  x106
data.nodeId  (number, 823/1202 records)
    numeric range 0 .. 286 (190 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 531 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dungeon Dev (150); Unit 2 Prod (Refactor) (149); Unit 3 Dev (142); Unit 1 Dev (67); Unit 4 Dev (20); Unit 4 Dev - Dungeon (3)
- **Intervals:** median 30.01s (p5 29.95s / p95 40.16s, n=524)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 531/531 records)
data.position.x  (number, 531/531 records)
    numeric range -705.862 .. 1599.06 (330 unique)
data.position.y  (number, 531/531 records)
    numeric range -112.49 .. 158.463 (213 unique)
data.position.z  (number, 531/531 records)
    numeric range -1115.29 .. 2036.68 (329 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 56 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (20); Unit 1 Dev (15); Unit 3 Dev (12); Unit 3 Dungeon Dev (7); Unit 4 Dev (1); Unit 4 Dev - Dungeon (1)
- **eventKey:** present on 56 of 56 records
- **Intervals:** median 192.39s (p5 0.00s / p95 170087.11s, n=55)
- **`data` key-set variants:** [questEventType, questID, questName] x40; [questEventType, questID, questName, questSuccessOrFailure] x16
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 56/56 records)
    "questActiveEvent"  x40
    "questFinishEvent"  x16
data.questID  (string, 56/56 records)
    17 unique values (see csv/event_unique_values.csv)
data.questName  (string, 56/56 records)
    17 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 16/56 records)
    "Succeeded"  x16
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 55 records

- **Scenes:** Unit 3 Dev (47); Unit 2 Prod (Refactor) (6); Unit 3 Dungeon Dev (2)
- **Intervals:** median 22.49s (p5 3.89s / p95 61143.89s, n=54)
- **Fields under `data`:**

```text
data.actionType  (string, 55/55 records)
    "MapCloseEvent"  x30
    "MapOpenEvent"  x25
data.featureUsed  (string, 55/55 records)
    "Map"  x55
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `argumentationNodeEvent` — 21 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (16); Unit 3 Dev (5)
- **Intervals:** median 5.69s (p5 1.37s / p95 187026.00s, n=20)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 21/21 records)
    "argumentationNodeAdd"  x15
    "argumentationNodeRemove"  x6
data.argumentationTitle  (string, 21/21 records)
    "Unit 1 - Freshwater"  x16
    "Unit 3 - Pollution Upstream"  x5
data.nodeName  (string, 21/21 records)
    "B"  x7
    "I"  x5
    "1"  x4
    "A"  x4
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 10 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (7); Unit 3 Dev (3)
- **Intervals:** median 29.50s (p5 2.26s / p95 378635.21s, n=9)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationSessionClose"  x5
    "argumentationSessionOpen"  x5
data.argumentationDescription  (string, 10/10 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "Unit 1 - Does the planet WAT-247 have freshwater"  x3
data.argumentationTitle  (string, 10/10 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x3
    "Unit 3 - Pollution Upstream"  x3
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `Soil Key Puzzle` — 9 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 312.91s (p5 2.98s / p95 459089.58s, n=8)
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/9 records)
    "Finished"  x5
    "Started"  x4
data.Unit  (string, 9/9 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 694151.61s (p5 694151.61s / p95 694151.61s, n=1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 2/2 records)
    "1"  x1
    "3"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `argumentationToolEvent` — 2 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (2)
- **Intervals:** median 2.12s (p5 2.12s / p95 2.12s, n=1)
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

### `TopographicMapEvent` — 1 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (1)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 1/1 records)
    "dragStart"  x1
data.featureUsed  (string, 1/1 records)
    "waypoint"  x1
data.location  (object, 1/1 records)
data.location.x  (number, 1/1 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 1/1 records)
    1 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 1/1 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

## 10. Regression Comparison

Baseline: snapshot build-log-qa\reports\09-23-26\snapshot.json. See section 4 for the structural diff and `csv/regression_diff.csv` for every row.

## 11. Recommended Follow-Up

**Needs review (WARNING):**
- `DEBUGMenu` : expected event type absent although its content was played — possible logging failure
- `DaniEvent` : expected event type absent although its content was played — possible logging failure
- `InputEvent` : expected event type absent although its content was played — possible logging failure
- `ObjectInterEvent` : expected event type absent although its content was played — possible logging failure
- `PuzzlePieceVisibleEvent` : expected event type absent although its content was played — possible logging failure
- `TerasGardenBox` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `soilMachine` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : exact duplicate records (same timestamp, scene and data)

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (5 records)
- `TopographicMapEvent` data.actionType: "dragStart" (1x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (6x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*