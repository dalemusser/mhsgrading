# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f780

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f780
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f780.jsonl
- **Records:** 2427 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f780
- **Time span:** 2026-04-14T13:46:47.366000+00:00 .. 2026-04-24T14:35:07.974000+00:00 (240h 48m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f780\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **12 event types**, 2427 records, 7 scenes.
- Findings: **0 FAIL**, **45 WARNING**, 55 INFO, 2 NOT_TESTED, 41 PASS.
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
| DialogueEvent | 1556 | 64.11 | 1 | 7 | 1101 | 2026-04-14T13:47:05.704000+00:00 | 2026-04-24T14:35:07.974000+00:00 | 240h 48m |
| PlayerPositionEvent | 545 | 22.46 | 1 | 7 | 0 | 2026-04-14T13:46:47.366000+00:00 | 2026-04-24T14:34:59.690000+00:00 | 240h 48m |
| Topographic Map Event | 102 | 4.2 | 1 | 2 | 0 | 2026-04-16T13:59:56.418000+00:00 | 2026-04-24T14:02:31.380000+00:00 | 192h 2m |
| soilMachine | 66 | 2.72 | 1 | 1 | 0 | 2026-04-24T14:20:11.942000+00:00 | 2026-04-24T14:28:49.264000+00:00 | 8m 37s |
| questEvent | 62 | 2.55 | 1 | 7 | 62 | 2026-04-14T13:47:05.686000+00:00 | 2026-04-24T14:34:00.682000+00:00 | 240h 46m |
| TopographicMapEvent | 44 | 1.81 | 1 | 2 | 0 | 2026-04-16T14:00:18.437000+00:00 | 2026-04-24T14:02:29.091000+00:00 | 192h 2m |
| argumentationNodeEvent | 25 | 1.03 | 1 | 2 | 0 | 2026-04-14T14:05:03.488000+00:00 | 2026-04-20T14:24:11.388000+00:00 | 144h 19m |
| Soil Key Puzzle | 11 | 0.45 | 1 | 3 | 0 | 2026-04-14T14:26:43.612000+00:00 | 2026-04-24T14:09:59.587000+00:00 | 239h 43m |
| argumentationEvent | 7 | 0.29 | 1 | 2 | 0 | 2026-04-14T14:04:57.612000+00:00 | 2026-04-20T14:24:12.936000+00:00 | 144h 19m |
| argumentationToolEvent | 4 | 0.16 | 1 | 1 | 0 | 2026-04-20T14:23:28.503000+00:00 | 2026-04-20T14:23:32.180000+00:00 | 3.7s |
| crash | 3 | 0.12 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.08 | 1 | 2 | 0 | 2026-04-14T14:10:30.556000+00:00 | 2026-04-24T14:04:04.124000+00:00 | 239h 53m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.106s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 863613.568s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.004s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 402.63s median 
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
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 4.281s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 5.575s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 0.817s median 
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
  - Observed: 0.317s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition; Unit 5 Dev; Unit 5 Dev - Dungeon 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.2x vs baseline. 
  - Observed: 25 records 
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
  - Observed: 2; C; D; II 
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
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 13.2x vs baseline. 
  - Observed: 66 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 7 mismatch(es); e.g. 'DialogueNodeEvent:70:0' vs expected 'DialogueNodeEvent:70:7' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f780.jsonl[731] _id=69de4a1e7957a33870f342f7 ts=2026-04-14T14:07:25.9620000Z`; `69cdc965d385e3b94310f780.jsonl[57] _id=69e0e5dd7957a33870f4ffc3 ts=2026-04-16T13:36:29.2020000Z`; `69cdc965d385e3b94310f780.jsonl[1131] _id=69e0ee737957a33870f5352b ts=2026-04-16T14:13:06.5830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 102 records, TopographicMapEvent: 44 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1555 | 0.0 | 1.106 | 557.481 | 50.135 | 341298.582 | 0.11 | 383 | 6 |
| PlayerPositionEvent | 536 | 29.798 | 30.004 | 1616.786 | 41.03 | 340953.064 | 0.04 | 0 | 4 |
| Topographic Map Event | 101 | 0.12 | 8.786 | 6845.099 | 336.16 | 342214.25 | 0.01 | 0 | 5 |
| soilMachine | 65 | 0.111 | 0.317 | 7.959 | 38.458 | 138.193 | 7.54 | 0 | 0 |
| questEvent | 61 | 0.003 | 165.168 | 14210.082 | 168986.185 | 341101.198 | 0.0 | 7 | 10 |
| TopographicMapEvent | 43 | 0.115 | 4.281 | 16077.457 | 152766.519 | 345318.415 | 0.0 | 0 | 4 |
| argumentationNodeEvent | 24 | 1.006 | 5.575 | 21647.829 | 34.152 | 519358.3 | 0.0 | 0 | 1 |
| Soil Key Puzzle | 10 | 2.985 | 402.63 | 86299.598 | 266968.061 | 342145.877 | 0.0 | 0 | 5 |
| argumentationEvent | 6 | 0.093 | 56.121 | 86592.554 | 389532.914 | 519350.605 | 0.0 | 0 | 1 |
| argumentationToolEvent | 3 | 0.074 | 0.817 | 1.226 | 2.589 | 2.786 | 48.95 | 0 | 0 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 863613.568 | 863613.568 | 863613.568 | 863613.568 | 863613.568 | 0.0 | 0 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc965d385e3b94310f780.jsonl[326] _id=69e8ce921724f0c9e2fa25d5 ts=? == 69cdc965d385e3b94310f780.jsonl[2105] _id=69e8da471724f0c9e2fa6ed9 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.004s (p5 29.97s, p95 41.03s, n=536) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `93ms: 69cdc965d385e3b94310f780.jsonl[1752] _id=69e6370d1724f0c9e2f8a747 ts=2026-04-20T14:24:12.8430000Z ~ 69cdc965d385e3b94310f780.jsonl[295] _id=69e6370d1724f0c9e2f8a74f ts=2026-04-20T14:24:12.9360000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 43 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `745ms: 69cdc965d385e3b94310f780.jsonl[442] _id=69eb7c251724f0c9e2fb917f ts=2026-04-24T14:20:20.4830000Z ~ 69cdc965d385e3b94310f780.jsonl[2306] _id=69eb7c251724f0c9e2fb9181 ts=2026-04-24T14:20:21.2280000Z`; `235ms: 69cdc965d385e3b94310f780.jsonl[2306] _id=69eb7c251724f0c9e2fb9181 ts=2026-04-24T14:20:21.2280000Z ~ 69cdc965d385e3b94310f780.jsonl[443] _id=69eb7c261724f0c9e2fb9185 ts=2026-04-24T14:20:21.4630000Z`; `177ms: 69cdc965d385e3b94310f780.jsonl[443] _id=69eb7c261724f0c9e2fb9185 ts=2026-04-24T14:20:21.4630000Z ~ 69cdc965d385e3b94310f780.jsonl[2307] _id=69eb7c261724f0c9e2fb9189 ts=2026-04-24T14:20:21.6400000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 6 gap(s), longest 94h 48m 
  - Evidence: 94h 48m: 69cdc965d385e3b94310f780.jsonl[1333] _id=69e0f39a7957a33870f558a5 ts=2026-04-16T14:35:05.8300000Z -> 69cdc965d385e3b94310f780.jsonl[1354] _id=69e628cc1724f0c9e2f8509f ts=2026-04-20T13:23:24.4120000Z; 47h 32m: 69cdc965d385e3b94310f780.jsonl[354] _id=69e8daa71724f0c9e2fa7119 ts=2026-04-22T14:26:45.5400000Z -> 69cdc965d385e3b94310f780.jsonl[2146] _id=69eb77221724f0c9e2fb77e3 ts=2026-04-24T13:58:57.5050000Z; 47h 2m: 69cdc965d385e3b94310f780.jsonl[872] _id=69de4fb67957a33870f36a52 ts=2026-04-14T14:31:17.9150000Z -> 69cdc965d385e3b94310f780.jsonl[875] _id=69e0e5427957a33870f4f9cd ts=2026-04-16T13:33:54.0140000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 383 interval(s) ≤ 0.000s..0.002s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f780.jsonl[394] _id=69eb78551724f0c9e2fb7ef7 ts=2026-04-24T14:04:04.1340000Z -> 69cdc965d385e3b94310f780.jsonl[381] _id=69eb78641724f0c9e2fb7f67 ts=2026-04-24T14:04:04.134Z; 2ms: 69cdc965d385e3b94310f780.jsonl[1737] _id=69e636e41724f0c9e2f8a5fe ts=2026-04-20T14:23:32.2520000Z -> 69cdc965d385e3b94310f780.jsonl[1741] _id=69e636e41724f0c9e2f8a601 ts=2026-04-20T14:23:32.2540000Z; 2ms: 69cdc965d385e3b94310f780.jsonl[1894] _id=69e8cdc31724f0c9e2fa1fc7 ts=2026-04-22T13:31:45.5650000Z -> 69cdc965d385e3b94310f780.jsonl[1896] _id=69e8cdc31724f0c9e2fa1fc9 ts=2026-04-22T13:31:45.5670000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 239h 53m 
  - Evidence: 239h 53m: 69cdc965d385e3b94310f780.jsonl[765] _id=69de4ad67957a33870f34819 ts=2026-04-14T14:10:30.5560000Z -> 69cdc965d385e3b94310f780.jsonl[2173] _id=69eb78551724f0c9e2fb7ef2 ts=2026-04-24T14:04:04.1240000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc965d385e3b94310f780.jsonl[1334] _id=69e0f3b17957a33870f558fa ts=2026-04-16T14:35:29.1250000Z -> 69cdc965d385e3b94310f780.jsonl[1337] _id=69e6278a1724f0c9e2f84ab5 ts=2026-04-20T13:18:02.1890000Z; 47h 28m: 69cdc965d385e3b94310f780.jsonl[2142] _id=69e8db381724f0c9e2fa749b ts=2026-04-22T14:29:10.5380000Z -> 69cdc965d385e3b94310f780.jsonl[2144] _id=69eb76ec1724f0c9e2fb7705 ts=2026-04-24T13:58:03.3830000Z; 47h 2m: 69cdc965d385e3b94310f780.jsonl[861] _id=69de4fbf7957a33870f36a88 ts=2026-04-14T14:31:26.9250000Z -> 69cdc965d385e3b94310f780.jsonl[874] _id=69e0e53e7957a33870f4f9c5 ts=2026-04-16T13:33:49.2090000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 2m 
  - Evidence: 95h 2m: 69cdc965d385e3b94310f780.jsonl[1200] _id=69e0f0517957a33870f53ed5 ts=2026-04-16T14:21:05.0400000Z -> 69cdc965d385e3b94310f780.jsonl[1366] _id=69e628d31724f0c9e2f850e3 ts=2026-04-20T13:23:30.9170000Z; 48h 38m: 69cdc965d385e3b94310f780.jsonl[1891] _id=69e8cdb21724f0c9e2fa1f5d ts=2026-04-22T13:31:28.6240000Z -> 69cdc965d385e3b94310f780.jsonl[2243] _id=69eb799d1724f0c9e2fb84f3 ts=2026-04-24T14:09:32.6870000Z; 47h 57m: 69cdc965d385e3b94310f780.jsonl[1428] _id=69e62b401724f0c9e2f85f7b ts=2026-04-20T13:33:51.9410000Z -> 69cdc965d385e3b94310f780.jsonl[1873] _id=69e8cd961724f0c9e2fa1e65 ts=2026-04-22T13:31:01.2420000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 3m 
  - Evidence: 95h 3m: 69cdc965d385e3b94310f780.jsonl[1177] _id=69e0ef7b7957a33870f53b27 ts=2026-04-16T14:17:31.5340000Z -> 69cdc965d385e3b94310f780.jsonl[1340] _id=69e628421724f0c9e2f84e37 ts=2026-04-20T13:21:05.7840000Z; 48h 29m: 69cdc965d385e3b94310f780.jsonl[1869] _id=69e8cd371724f0c9e2fa1c29 ts=2026-04-22T13:29:26.0160000Z -> 69cdc965d385e3b94310f780.jsonl[2153] _id=69eb772b1724f0c9e2fb7825 ts=2026-04-24T13:59:07.0020000Z; 47h 8m: 69cdc965d385e3b94310f780.jsonl[1616] _id=69e635da1724f0c9e2f89ea0 ts=2026-04-20T14:19:06.0420000Z -> 69cdc965d385e3b94310f780.jsonl[1860] _id=69e8ccd31724f0c9e2fa19d3 ts=2026-04-22T13:27:46.2410000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 95h 55m 
  - Evidence: 95h 55m: 69cdc965d385e3b94310f780.jsonl[103] _id=69e0eb777957a33870f52371 ts=2026-04-16T14:00:22.7180000Z -> 69cdc965d385e3b94310f780.jsonl[1609] _id=69e6305d1724f0c9e2f87e01 ts=2026-04-20T13:55:41.1330000Z; 48h 30m: 69cdc965d385e3b94310f780.jsonl[323] _id=69e8ccd81724f0c9e2fa19eb ts=2026-04-22T13:27:51.2260000Z -> 69cdc965d385e3b94310f780.jsonl[2149] _id=69eb77131724f0c9e2fb778d ts=2026-04-24T13:58:42.7160000Z; 47h 7m: 69cdc965d385e3b94310f780.jsonl[1682] _id=69e635d31724f0c9e2f89e5b ts=2026-04-20T14:18:59.1340000Z -> 69cdc965d385e3b94310f780.jsonl[1853] _id=69e8cc9b1724f0c9e2fa1885 ts=2026-04-22T13:26:49.5240000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 15m 
  - Evidence: 144h 15m: 69cdc965d385e3b94310f780.jsonl[730] _id=69de4a1e7957a33870f342f5 ts=2026-04-14T14:07:25.9420000Z -> 69cdc965d385e3b94310f780.jsonl[1726] _id=69e636d41724f0c9e2f8a547 ts=2026-04-20T14:23:16.5470000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 15m 
  - Evidence: 144h 15m: 69cdc965d385e3b94310f780.jsonl[698] _id=69de4a1c7957a33870f342df ts=2026-04-14T14:07:24.3770000Z -> 69cdc965d385e3b94310f780.jsonl[1731] _id=69e636da1724f0c9e2f8a589 ts=2026-04-20T14:23:22.6770000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 45m 
  - Evidence: 94h 45m: 69cdc965d385e3b94310f780.jsonl[1312] _id=69e0f3207957a33870f5541b ts=2026-04-16T14:33:04.5780000Z -> 69cdc965d385e3b94310f780.jsonl[1336] _id=69e6278e1724f0c9e2f84ac1 ts=2026-04-20T13:18:05.7760000Z; 47h 31m: 69cdc965d385e3b94310f780.jsonl[365] _id=69e8daa41724f0c9e2fa7105 ts=2026-04-22T14:26:43.1730000Z -> 69cdc965d385e3b94310f780.jsonl[2145] _id=69eb76ef1724f0c9e2fb7711 ts=2026-04-24T13:58:07.0230000Z; 47h 3m: 69cdc965d385e3b94310f780.jsonl[862] _id=69de4f857957a33870f36922 ts=2026-04-14T14:30:29.2800000Z -> 69cdc965d385e3b94310f780.jsonl[873] _id=69e0e5417957a33870f4f9c7 ts=2026-04-16T13:33:52.5960000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 7 interval(s) ≤ 0.003s..0.007s shown 
  - Evidence: 3ms: 69cdc965d385e3b94310f780.jsonl[13] _id=69de496b7957a33870f33da7 ts=2026-04-14T14:04:26.6540000Z -> 69cdc965d385e3b94310f780.jsonl[14] _id=69de496b7957a33870f33da9 ts=2026-04-14T14:04:26.6570000Z; 7ms: 69cdc965d385e3b94310f780.jsonl[414] _id=69eb7ac51724f0c9e2fb8aef ts=2026-04-24T14:14:28.4320000Z -> 69cdc965d385e3b94310f780.jsonl[2280] _id=69eb7ac51724f0c9e2fb8af1 ts=2026-04-24T14:14:28.4390000Z; 7ms: 69cdc965d385e3b94310f780.jsonl[485] _id=69eb7ca71724f0c9e2fb9471 ts=2026-04-24T14:22:31.0320000Z -> 69cdc965d385e3b94310f780.jsonl[479] _id=69eb7ca71724f0c9e2fb9473 ts=2026-04-24T14:22:31.0390000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 5 record(s) match the trigger in 69cdc965d385e3b94310f780.jsonl:69cdc965d385e3b94310f780, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f780.jsonl[50] _id=69de4f5f7957a33870f367ac ts=2026-04-14T14:29:50.8330000Z`; `69cdc965d385e3b94310f780.jsonl[1200] _id=69e0f0517957a33870f53ed5 ts=2026-04-16T14:21:05.0400000Z`; `69cdc965d385e3b94310f780.jsonl[1428] _id=69e62b401724f0c9e2f85f7b ts=2026-04-20T13:33:51.9410000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 44 record(s) match the trigger in 69cdc965d385e3b94310f780.jsonl:69cdc965d385e3b94310f780, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f780.jsonl[1067] _id=69e0eb727957a33870f52361 ts=2026-04-16T14:00:18.4370000Z`; `69cdc965d385e3b94310f780.jsonl[103] _id=69e0eb777957a33870f52371 ts=2026-04-16T14:00:22.7180000Z`; `69cdc965d385e3b94310f780.jsonl[1609] _id=69e6305d1724f0c9e2f87e01 ts=2026-04-20T13:55:41.1330000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f780.jsonl[142] _id=69e0f32d7957a33870f55489 ts=2026-04-16T14:33:17.5570000Z`; `69cdc965d385e3b94310f780.jsonl[1585] _id=69e62fc51724f0c9e2f87ae1 ts=2026-04-20T13:53:09.5800000Z`; `69cdc965d385e3b94310f780.jsonl[250] _id=69e6302f1724f0c9e2f87d19 ts=2026-04-20T13:54:55.1410000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f780.jsonl[295] _id=69e6370d1724f0c9e2f8a74f ts=2026-04-20T14:24:12.9360000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f780.jsonl[1739] _id=69e636e11724f0c9e2f8a5d7 ts=2026-04-20T14:23:29.3200000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f780.jsonl[1821] _id=69e8cbae1724f0c9e2fa131d ts=2026-04-22T13:22:52.5710000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `69cdc965d385e3b94310f780.jsonl[326] _id=69e8ce921724f0c9e2fa25d5 ts=?`; `69cdc965d385e3b94310f780.jsonl[2105] _id=69e8da471724f0c9e2fa6ed9 ts=?`; `69cdc965d385e3b94310f780.jsonl[498] _id=69eb7da41724f0c9e2fb98c1 ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 1 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f780.jsonl[1429] _id=69e62b3d1724f0c9e2f85f6d ts=2026-04-20T13:33:48.9560000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 195 unmatched 'DialogueStartEvent' (totals: 323 start, 132 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 6 open, 5 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationToolOpen' (totals: 2 open, 2 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 13 unmatched 'questActiveEvent' (totals: 37 start, 25 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.48s, min -16.76s, max -0.19s over 2424 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f780\coverage.yaml

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
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
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

### `DialogueEvent` — 1556 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (659); Unit 3 Dev (373); Unit 1 Dev (182); Unit 3 Dungeon Dev (135); Unit 4 Dev - Dungeon (100); Unit 4 Dev (91); Unit 4 Dev - Anderson Base (16)
- **eventKey:** present on 1101 of 1556 records
- **Intervals:** median 1.11s (p5 0.01s / p95 50.14s, n=1555)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1101; [conversationId, dialogueEventType] x455
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1556/1556 records)
    numeric range 8 .. 107 (38 unique)
data.dialogueEventType  (string, 1556/1556 records)
    "DialogueNodeEvent"  x1101
    "DialogueStartEvent"  x323
    "DialogueFinishEvent"  x132
data.nodeId  (number, 1101/1556 records)
    numeric range 0 .. 286 (211 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 545 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (206); Unit 3 Dev (121); Unit 3 Dungeon Dev (107); Unit 1 Dev (48); Unit 4 Dev - Dungeon (36); Unit 4 Dev (24); Unit 4 Dev - Anderson Base (3)
- **Intervals:** median 30.00s (p5 29.97s / p95 41.03s, n=536)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 545/545 records)
data.position.x  (number, 545/545 records)
    numeric range -693.755 .. 1524.76 (311 unique)
data.position.y  (number, 545/545 records)
    numeric range -112.487 .. 155.544 (232 unique)
data.position.z  (number, 545/545 records)
    numeric range -1156.03 .. 1752.86 (311 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `Topographic Map Event` — 102 records

- **Scenes:** Unit 2 Prod (Refactor) (54); Unit 3 Dev (48)
- **Intervals:** median 8.79s (p5 1.13s / p95 336.16s, n=101)
- **Fields under `data`:**

```text
data.actionType  (string, 102/102 records)
    "MapCloseEvent"  x51
    "MapOpenEvent"  x51
data.featureUsed  (string, 102/102 records)
    "Map"  x102
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `soilMachine` — 66 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (66)
- **Intervals:** median 0.32s (p5 0.16s / p95 38.46s, n=65)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 66/66 records)
    "ChangeCanister"  x66
data.canisterType  (string, 66/66 records)
    "Bedrock"  x55
    "Clay"  x6
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 66/66 records)
    "3"  x53
    "5"  x9
    "4"  x4
data.machine  (string, 66/66 records)
    "1"  x65
    "2"  x1
data.row  (string, 66/66 records)
    "TopRow"  x62
    "BottomRow"  x4
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `questEvent` — 62 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 2 Prod (Refactor) (21); Unit 1 Dev (12); Unit 3 Dev (12); Unit 4 Dev - Dungeon (9); Unit 4 Dev (4); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (1)
- **eventKey:** present on 62 of 62 records
- **Intervals:** median 165.17s (p5 0.01s / p95 168986.18s, n=61)
- **`data` key-set variants:** [questEventType, questID, questName] x37; [questEventType, questID, questName, questSuccessOrFailure] x25
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 62/62 records)
    "questActiveEvent"  x37
    "questFinishEvent"  x25
data.questID  (string, 62/62 records)
    24 unique values (see csv/event_unique_values.csv)
data.questName  (string, 62/62 records)
    24 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 25/62 records)
    "Succeeded"  x25
```

Raw examples: `event_examples.json` -> `questEvent`.

### `TopographicMapEvent` — 44 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (42); Unit 2 Prod (Refactor) (2)
- **Intervals:** median 4.28s (p5 0.50s / p95 152766.52s, n=43)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 44/44 records)
    "dragEnd"  x22
    "dragStart"  x22
data.featureUsed  (string, 44/44 records)
    "waypoint"  x44
data.location  (object, 44/44 records)
data.location.x  (number, 44/44 records)
    numeric range -779.819 .. 296.293 (22 unique)
data.location.y  (number, 44/44 records)
    numeric range -334.112 .. 188.885 (23 unique)
data.location.z  (number, 44/44 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `argumentationNodeEvent` — 25 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (16); Unit 3 Dev (9)
- **Intervals:** median 5.58s (p5 1.06s / p95 34.15s, n=24)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 25/25 records)
    "argumentationNodeAdd"  x17
    "argumentationNodeRemove"  x8
data.argumentationTitle  (string, 25/25 records)
    "Unit 1 - Freshwater"  x11
    "Unit 3 - Pollution Upstream"  x9
    "Unit 1 - Argumentation Tutorial"  x5
data.nodeName  (string, 25/25 records)
    "A"  x8
    "B"  x5
    "I"  x5
    "1"  x2
    "3"  x2
    "4"  x2
    "5"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `Soil Key Puzzle` — 11 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (7); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 402.63s (p5 13.75s / p95 266968.06s, n=10)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 11/11 records)
    "Started"  x6
    "Finished"  x5
data.Unit  (string, 11/11 records)
    "Unit 2 Prod (Refactor)"  x7
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `argumentationEvent` — 7 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (4); Unit 3 Dev (3)
- **Intervals:** median 56.12s (p5 3.21s / p95 389532.91s, n=6)
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
- **Intervals:** median 0.82s (p5 0.15s / p95 2.59s, n=3)
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

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Uncaught ReferenceError: onResize is not defined"  x3
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x1
data.type  (string, 3/3 records)
    "runtime_error"  x3
data.unitId  (string, 3/3 records)
    "unit3"  x2
    "unit4"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 863613.57s (p5 863613.57s / p95 863613.57s, n=1)
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
- `crash` : exact duplicate records (same timestamp, scene and data)
- `PlayerPositionEvent` : continuous cadence differs from expectation

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (7 records)
- `TopographicMapEvent` data.actionType: "dragStart" (22x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (8x)
- `soilMachine` data.canisterType: "Bedrock" (55x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*