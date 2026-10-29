# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75d

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75d
- **Game version string(s) in log:** 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f75d.jsonl
- **Records:** 2195 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f75d
- **Time span:** 2026-04-13T19:23:48.625000+00:00 .. 2026-04-23T20:10:44.752000+00:00 (240h 46m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75d\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **11 event types**, 2195 records, 6 scenes.
- Findings: **0 FAIL**, **40 WARNING**, 55 INFO, 2 NOT_TESTED, 41 PASS.
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
| DialogueEvent | 1427 | 65.01 | 1 | 6 | 963 | 2026-04-13T19:24:06.902000+00:00 | 2026-04-23T20:10:44.752000+00:00 | 240h 46m |
| PlayerPositionEvent | 542 | 24.69 | 1 | 6 | 0 | 2026-04-13T19:23:48.625000+00:00 | 2026-04-23T20:10:36.499000+00:00 | 240h 46m |
| Topographic Map Event | 102 | 4.65 | 1 | 2 | 0 | 2026-04-13T20:08:04.143000+00:00 | 2026-04-23T19:38:34.489000+00:00 | 239h 30m |
| questEvent | 60 | 2.73 | 1 | 6 | 60 | 2026-04-13T19:24:06.878000+00:00 | 2026-04-23T20:06:14.187000+00:00 | 240h 42m |
| TopographicMapEvent | 18 | 0.82 | 1 | 1 | 0 | 2026-04-15T19:21:25.101000+00:00 | 2026-04-15T19:42:17.780000+00:00 | 20m 52s |
| argumentationNodeEvent | 14 | 0.64 | 1 | 2 | 0 | 2026-04-13T19:42:59.414000+00:00 | 2026-04-21T19:08:45.436000+00:00 | 191h 25m |
| Soil Key Puzzle | 11 | 0.5 | 1 | 3 | 0 | 2026-04-13T20:02:29.530000+00:00 | 2026-04-23T19:49:32.836000+00:00 | 239h 47m |
| soilMachine | 8 | 0.36 | 1 | 1 | 0 | 2026-04-23T20:05:01.011000+00:00 | 2026-04-23T20:09:27.157000+00:00 | 4m 26s |
| argumentationEvent | 7 | 0.32 | 1 | 2 | 0 | 2026-04-13T19:42:36.841000+00:00 | 2026-04-21T19:08:56.245000+00:00 | 191h 26m |
| argumentationToolEvent | 4 | 0.18 | 1 | 1 | 0 | 2026-04-21T19:07:48.990000+00:00 | 2026-04-21T19:07:53.521000+00:00 | 4.5s |
| EndOfUnit | 2 | 0.09 | 1 | 2 | 0 | 2026-04-13T19:48:30.080000+00:00 | 2026-04-23T19:41:35.308000+00:00 | 239h 53m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863585.228s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.015s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 1192.034s median 
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
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 7.592s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.695s median 
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
- **WARNING / Medium** `soilMachine` — median interval between records changed substantially. 
  - Observed: 5.874s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 4 Dev - Anderson Base; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** `EndOfUnit` `data.Unit` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 4; 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.3x vs baseline. 
  - Observed: 11 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 102 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 18 records 
  - Expected: 83 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `TopographicMapEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: MapCloseEvent; MapOpenEvent; Selected; Unselected; WaypointMoveEvent; WaypointResetEvent; WaypointSetEvent 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TopographicMapEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: dragEnd; dragStart 
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
  - Observed: 14 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; C; D 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 36; 40; 41; 43; 44; 45; 50; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; Power Play; Power Play - Floor 5; Saving Cadet Anderson; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `soilMachine` `data.floor` — baseline categorical value(s) not seen this build. 
  - Observed: 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.machine` — baseline categorical value(s) not seen this build. 
  - Observed: 2 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` `data.row` — baseline categorical value(s) not seen this build. 
  - Observed: BottomRow 
  - Expected: may simply not have been exercised — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 4 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[580] _id=69dd47bd7957a33870f2a727 ts=2026-04-13T19:45:01.3950000Z`; `69cdc937d385e3b94310f75d.jsonl[881] _id=69dfe5ee7957a33870f47423 ts=2026-04-15T19:24:29.4240000Z`; `69cdc937d385e3b94310f75d.jsonl[295] _id=69dfe9847957a33870f48275 ts=2026-04-15T19:39:47.2590000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 102 records, TopographicMapEvent: 18 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1426 | 0.0 | 2.177 | 607.853 | 52.699 | 341171.026 | 0.1 | 401 | 5 |
| PlayerPositionEvent | 535 | 22.512 | 30.015 | 1619.642 | 38.632 | 341109.03 | 0.04 | 0 | 4 |
| Topographic Map Event | 101 | 0.366 | 8.277 | 8536.934 | 790.426 | 341442.463 | 0.01 | 0 | 7 |
| questEvent | 59 | 0.003 | 168.937 | 14686.904 | 168382.369 | 342889.886 | 0.0 | 6 | 12 |
| TopographicMapEvent | 17 | 0.348 | 3.41 | 73.687 | 308.291 | 804.642 | 0.81 | 0 | 1 |
| argumentationNodeEvent | 13 | 1.665 | 7.592 | 53011.232 | 275636.902 | 688986.317 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 10 | 3.137 | 1192.034 | 86322.331 | 268008.187 | 344578.314 | 0.0 | 0 | 5 |
| soilMachine | 7 | 1.174 | 5.874 | 38.021 | 109.396 | 120.087 | 1.58 | 0 | 0 |
| argumentationEvent | 6 | 0.108 | 48.783 | 114863.234 | 516739.578 | 688961.767 | 0.0 | 0 | 1 |
| argumentationToolEvent | 3 | 0.061 | 1.695 | 1.51 | 2.667 | 2.775 | 39.73 | 0 | 0 |
| EndOfUnit | 1 | 863585.228 | 863585.228 | 863585.228 | 863585.228 | 863585.228 | 0.0 | 0 | 1 |

- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.015s (p5 29.95s, p95 38.63s, n=535) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `108ms: 69cdc937d385e3b94310f75d.jsonl[1695] _id=69e7cb491724f0c9e2f9c0bd ts=2026-04-21T19:08:56.1370000Z ~ 69cdc937d385e3b94310f75d.jsonl[402] _id=69e7cb491724f0c9e2f9c0c7 ts=2026-04-21T19:08:56.2450000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc937d385e3b94310f75d.jsonl[1569] _id=69e293911724f0c9e2f7dc72 ts=2026-04-17T20:09:52.0840000Z -> 69cdc937d385e3b94310f75d.jsonl[1570] _id=69e7c8441724f0c9e2f9af75 ts=2026-04-21T18:56:03.1100000Z; 47h 31m: 69cdc937d385e3b94310f75d.jsonl[1978] _id=69e7d8941724f0c9e2f9fe5f ts=2026-04-21T20:05:39.6090000Z -> 69cdc937d385e3b94310f75d.jsonl[1994] _id=69ea74f31724f0c9e2fb560d ts=2026-04-23T19:37:22.5020000Z; 47h 3m: 69cdc937d385e3b94310f75d.jsonl[245] _id=69dd4cd47957a33870f2baad ts=2026-04-13T20:06:43.7990000Z -> 69cdc937d385e3b94310f75d.jsonl[731] _id=69dfe27e7957a33870f4673b ts=2026-04-15T19:09:50.3840000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 401 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75d.jsonl[467] _id=69ea75f01724f0c9e2fb58fb ts=2026-04-23T19:41:35.3700000Z -> 69cdc937d385e3b94310f75d.jsonl[2043] _id=69ea76001724f0c9e2fb5931 ts=2026-04-23T19:41:35.37Z; 3ms: 69cdc937d385e3b94310f75d.jsonl[1200] _id=69dfef5b7957a33870f49a0b ts=2026-04-15T20:04:42.4750000Z -> 69cdc937d385e3b94310f75d.jsonl[1201] _id=69dfef5b7957a33870f49a0d ts=2026-04-15T20:04:42.4780000Z; 3ms: 69cdc937d385e3b94310f75d.jsonl[1938] _id=69e7d84c1724f0c9e2f9fcbf ts=2026-04-21T20:04:27.7220000Z -> 69cdc937d385e3b94310f75d.jsonl[1939] _id=69e7d84d1724f0c9e2f9fcc1 ts=2026-04-21T20:04:27.7250000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 53m 
  - Evidence: 239h 53m: 69cdc937d385e3b94310f75d.jsonl[605] _id=69dd488e7957a33870f2aadb ts=2026-04-13T19:48:30.0800000Z -> 69cdc937d385e3b94310f75d.jsonl[466] _id=69ea75ef1724f0c9e2fb58f9 ts=2026-04-23T19:41:35.3080000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc937d385e3b94310f75d.jsonl[388] _id=69e2937e1724f0c9e2f7dc46 ts=2026-04-17T20:09:33.5590000Z -> 69cdc937d385e3b94310f75d.jsonl[1573] _id=69e7c7f31724f0c9e2f9ae23 ts=2026-04-21T18:54:42.5890000Z; 47h 30m: 69cdc937d385e3b94310f75d.jsonl[1976] _id=69e7d8881724f0c9e2f9fe13 ts=2026-04-21T20:05:27.9490000Z -> 69cdc937d385e3b94310f75d.jsonl[1979] _id=69ea74a01724f0c9e2fb5593 ts=2026-04-23T19:35:59.3310000Z; 46h 59m: 69cdc937d385e3b94310f75d.jsonl[251] _id=69dd4da97957a33870f2bcb3 ts=2026-04-13T20:10:16.5830000Z -> 69cdc937d385e3b94310f75d.jsonl[732] _id=69dfe27a7957a33870f46731 ts=2026-04-15T19:09:45.6880000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 42m 
  - Evidence: 95h 42m: 69cdc937d385e3b94310f75d.jsonl[1426] _id=69e28b361724f0c9e2f7b4e4 ts=2026-04-17T19:34:13.6960000Z -> 69cdc937d385e3b94310f75d.jsonl[1743] _id=69e7cd391724f0c9e2f9cd0d ts=2026-04-21T19:17:12.0100000Z; 48h 27m: 69cdc937d385e3b94310f75d.jsonl[1748] _id=69e7cdef1724f0c9e2f9d065 ts=2026-04-21T19:20:14.1060000Z -> 69cdc937d385e3b94310f75d.jsonl[2066] _id=69ea77451724f0c9e2fb5c5f ts=2026-04-23T19:47:16.5820000Z; 47h 50m: 69cdc937d385e3b94310f75d.jsonl[214] _id=69dd4bd97957a33870f2b667 ts=2026-04-13T20:02:32.6670000Z -> 69cdc937d385e3b94310f75d.jsonl[1127] _id=69dfeca77957a33870f48e1d ts=2026-04-15T19:53:10.2070000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 7 gap(s), longest 94h 50m 
  - Evidence: 94h 50m: 69cdc937d385e3b94310f75d.jsonl[1552] _id=69e2933e1724f0c9e2f7db06 ts=2026-04-17T20:08:29.9300000Z -> 69cdc937d385e3b94310f75d.jsonl[1604] _id=69e7c9011724f0c9e2f9b429 ts=2026-04-21T18:59:12.3930000Z; 48h 36m: 69cdc937d385e3b94310f75d.jsonl[1622] _id=69e7c94e1724f0c9e2f9b521 ts=2026-04-21T19:00:29.1230000Z -> 69cdc937d385e3b94310f75d.jsonl[1982] _id=69ea74c41724f0c9e2fb55bd ts=2026-04-23T19:36:35.6290000Z; 47h 20m: 69cdc937d385e3b94310f75d.jsonl[1117] _id=69dfec4d7957a33870f48cde ts=2026-04-15T19:51:40.8360000Z -> 69cdc937d385e3b94310f75d.jsonl[357] _id=69e286241724f0c9e2f7a1aa ts=2026-04-17T19:12:35.0660000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 13m 24s 
  - Evidence: 13m 24s: 69cdc937d385e3b94310f75d.jsonl[890] _id=69dfe6197957a33870f474ff ts=2026-04-15T19:25:12.4960000Z -> 69cdc937d385e3b94310f75d.jsonl[1032] _id=69dfe93d7957a33870f4813f ts=2026-04-15T19:38:37.1380000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 22m 
  - Evidence: 191h 22m: 69cdc937d385e3b94310f75d.jsonl[577] _id=69dd47bd7957a33870f2a725 ts=2026-04-13T19:45:01.3570000Z -> 69cdc937d385e3b94310f75d.jsonl[1672] _id=69e7cb001724f0c9e2f9bf21 ts=2026-04-21T19:07:43.1240000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 191h 23m 
  - Evidence: 191h 23m: 69cdc937d385e3b94310f75d.jsonl[574] _id=69dd47b37957a33870f2a6e7 ts=2026-04-13T19:44:51.1560000Z -> 69cdc937d385e3b94310f75d.jsonl[1681] _id=69e7cb0e1724f0c9e2f9bf79 ts=2026-04-21T19:07:57.4730000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 12 gap(s), longest 95h 14m 
  - Evidence: 95h 14m: 69cdc937d385e3b94310f75d.jsonl[376] _id=69e28c8c1724f0c9e2f7ba28 ts=2026-04-17T19:39:55.7670000Z -> 69cdc937d385e3b94310f75d.jsonl[1574] _id=69e7c7f71724f0c9e2f9ae2d ts=2026-04-21T18:54:45.6530000Z; 47h 30m: 69cdc937d385e3b94310f75d.jsonl[1974] _id=69e7d8941724f0c9e2f9fe59 ts=2026-04-21T20:05:39.3840000Z -> 69cdc937d385e3b94310f75d.jsonl[1980] _id=69ea74a31724f0c9e2fb559b ts=2026-04-23T19:36:02.5530000Z; 47h 3m: 69cdc937d385e3b94310f75d.jsonl[725] _id=69dd4cd27957a33870f2baa5 ts=2026-04-13T20:06:42.2900000Z -> 69cdc937d385e3b94310f75d.jsonl[733] _id=69dfe27d7957a33870f46737 ts=2026-04-15T19:09:48.8440000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 6 interval(s) ≤ 0.003s..0.012s shown 
  - Evidence: 3ms: 69cdc937d385e3b94310f75d.jsonl[554] _id=69dd46ee7957a33870f2a42f ts=2026-04-13T19:41:33.3170000Z -> 69cdc937d385e3b94310f75d.jsonl[115] _id=69dd46ee7957a33870f2a433 ts=2026-04-13T19:41:33.3200000Z; 10ms: 69cdc937d385e3b94310f75d.jsonl[517] _id=69dd451a7957a33870f29e34 ts=2026-04-13T19:33:45.9500000Z -> 69cdc937d385e3b94310f75d.jsonl[518] _id=69dd451a7957a33870f29e37 ts=2026-04-13T19:33:45.9600000Z; 12ms: 69cdc937d385e3b94310f75d.jsonl[497] _id=69ea7bb61724f0c9e2fb69b5 ts=2026-04-23T20:06:14.1750000Z -> 69cdc937d385e3b94310f75d.jsonl[2166] _id=69ea7bb61724f0c9e2fb69b9 ts=2026-04-23T20:06:14.1870000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 4 record(s) match the trigger in 69cdc937d385e3b94310f75d.jsonl:69cdc937d385e3b94310f75d, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[214] _id=69dd4bd97957a33870f2b667 ts=2026-04-13T20:02:32.6670000Z`; `69cdc937d385e3b94310f75d.jsonl[1138] _id=69dfed477957a33870f490e3 ts=2026-04-15T19:55:51.3450000Z`; `69cdc937d385e3b94310f75d.jsonl[1748] _id=69e7cdef1724f0c9e2f9d065 ts=2026-04-21T19:20:14.1060000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 18 record(s) match the trigger in 69cdc937d385e3b94310f75d.jsonl:69cdc937d385e3b94310f75d, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[850] _id=69dfe5357957a33870f470c9 ts=2026-04-15T19:21:25.1010000Z`; `69cdc937d385e3b94310f75d.jsonl[851] _id=69dfe53a7957a33870f470e9 ts=2026-04-15T19:21:30.3540000Z`; `69cdc937d385e3b94310f75d.jsonl[884] _id=69dfe5f37957a33870f47441 ts=2026-04-15T19:24:34.5570000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[334] _id=69dff0507957a33870f49f21 ts=2026-04-15T20:08:48.1090000Z`; `69cdc937d385e3b94310f75d.jsonl[1356] _id=69e287101724f0c9e2f7a536 ts=2026-04-17T19:16:31.4260000Z`; `69cdc937d385e3b94310f75d.jsonl[364] _id=69e287b31724f0c9e2f7a7e2 ts=2026-04-17T19:19:13.0120000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[402] _id=69e7cb491724f0c9e2f9c0c7 ts=2026-04-21T19:08:56.2450000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[1677] _id=69e7cb0a1724f0c9e2f9bf64 ts=2026-04-21T19:07:53.5210000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f75d.jsonl[346] _id=69e282ac1724f0c9e2f79438 ts=2026-04-17T18:57:46.7380000Z`; `69cdc937d385e3b94310f75d.jsonl[1743] _id=69e7cd391724f0c9e2f9cd0d ts=2026-04-21T19:17:12.0100000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 247 unmatched 'DialogueStartEvent' (totals: 354 start, 110 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Started' (totals: 7 open, 4 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 14 unmatched 'questActiveEvent' (totals: 37 start, 23 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.70s, min -16.86s, max -0.41s over 2195 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75d\coverage.yaml

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
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 102 records 
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

### `DialogueEvent` — 1427 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (610); Unit 3 Dev (387); Unit 1 Dev (178); Unit 3 Dungeon Dev (141); Unit 4 Dev - Dungeon (90); Unit 4 Dev (21)
- **eventKey:** present on 963 of 1427 records
- **Intervals:** median 2.18s (p5 0.01s / p95 52.70s, n=1426)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x963; [conversationId, dialogueEventType] x464
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1427/1427 records)
    numeric range 8 .. 104 (34 unique)
data.dialogueEventType  (string, 1427/1427 records)
    "DialogueNodeEvent"  x963
    "DialogueStartEvent"  x354
    "DialogueFinishEvent"  x110
data.nodeId  (number, 963/1427 records)
    numeric range 0 .. 286 (201 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 542 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (180); Unit 3 Dev (168); Unit 3 Dungeon Dev (86); Unit 1 Dev (50); Unit 4 Dev - Dungeon (36); Unit 4 Dev (22)
- **Intervals:** median 30.02s (p5 29.95s / p95 38.63s, n=535)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 542/542 records)
data.position.x  (number, 542/542 records)
    numeric range -689.693 .. 1593.17 (295 unique)
data.position.y  (number, 542/542 records)
    numeric range -112.487 .. 162.654 (206 unique)
data.position.z  (number, 542/542 records)
    numeric range -1134.81 .. 1868.73 (296 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 102 records

- **Scenes:** Unit 3 Dev (62); Unit 2 Prod (Refactor) (40)
- **Intervals:** median 8.28s (p5 1.30s / p95 790.43s, n=101)
- **Fields under `data`:**

```text
data.actionType  (string, 102/102 records)
    "MapCloseEvent"  x51
    "MapOpenEvent"  x51
data.featureUsed  (string, 102/102 records)
    "Map"  x102
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `questEvent` — 60 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 3 Dev (16); Unit 1 Dev (12); Unit 4 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev (1)
- **eventKey:** present on 60 of 60 records
- **Intervals:** median 168.94s (p5 0.01s / p95 168382.37s, n=59)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x23
- **Fields under `data`:**

```text
data.questEventType  (string, 60/60 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x23
data.questID  (string, 60/60 records)
    21 unique values (see csv/event_unique_values.csv)
data.questName  (string, 60/60 records)
    21 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 23/60 records)
    "Succeeded"  x23
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 18 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (18)
- **Intervals:** median 3.41s (p5 0.57s / p95 308.29s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "dragEnd"  x9
    "dragStart"  x9
data.featureUsed  (string, 18/18 records)
    "waypoint"  x18
data.location  (object, 18/18 records)
data.location.x  (number, 18/18 records)
    9 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 18/18 records)
    10 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 18/18 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 14 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (9); Unit 3 Dev (5)
- **Intervals:** median 7.59s (p5 1.70s / p95 275636.90s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "argumentationNodeAdd"  x11
    "argumentationNodeRemove"  x3
data.argumentationTitle  (string, 14/14 records)
    "Unit 1 - Freshwater"  x7
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x2
data.nodeName  (string, 14/14 records)
    "A"  x4
    "I"  x4
    "1"  x2
    "II"  x2
    "5"  x1
    "B"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 11 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (6); Unit 3 Dev (3); Unit 4 Dev (2)
- **Intervals:** median 1192.03s (p5 63.04s / p95 268008.19s, n=10)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/11 records)
    "Started"  x7
    "Finished"  x4
data.Unit  (string, 11/11 records)
    "Unit 2 Prod (Refactor)"  x6
    "Unit 3 Dev"  x3
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `soilMachine` — 8 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (8)
- **Intervals:** median 5.87s (p5 1.33s / p95 109.40s, n=7)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 8/8 records)
    "ChangeCanister"  x8
data.canisterType  (string, 8/8 records)
    "Bedrock"  x3
    "Gravel"  x2
    "Sand"  x2
    "Clay"  x1
data.floor  (string, 8/8 records)
    "4"  x7
    "3"  x1
data.machine  (string, 8/8 records)
    "1"  x8
data.row  (string, 8/8 records)
    "TopRow"  x8
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 48.78s (p5 11.82s / p95 516739.58s, n=6)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 7/7 records)
    "argumentationSessionClose"  x4
    "argumentationSessionOpen"  x3
data.argumentationDescription  (string, 7/7 records)
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 1 - Does the planet WAT-247 have freshwater"  x2
data.argumentationTitle  (string, 7/7 records)
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 1 - Freshwater"  x2
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 4 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 3 Dev (4)
- **Intervals:** median 1.70s (p5 0.22s / p95 2.67s, n=3)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 4/4 records)
    "argumentationToolClose"  x2
    "argumentationToolOpen"  x2
data.argumentationTitle  (string, 4/4 records)
    "Unit 3 - Pollution Upstream"  x4
data.toolName  (string, 4/4 records)
    "BackingInfoPanel - Pollution Site Data"  x2
    "BackingInfoPanel - "  x1
    "BackingInfoPanel - Watershed Image"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863585.23s (p5 863585.23s / p95 863585.23s, n=1)
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
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `PlayerPositionEvent` : continuous cadence differs from expectation
- `DEBUGMenu` : event type present in baseline 09-23-26 but absent now

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (6 records)
- `TopographicMapEvent` data.actionType: "dragStart" (9x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (3x)
- `soilMachine` data.canisterType: "Bedrock" (3x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*