# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f787

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc965d385e3b94310f787
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc965d385e3b94310f787.jsonl
- **Records:** 2112 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc965d385e3b94310f787
- **Time span:** 2026-04-14T14:01:25.406000+00:00 .. 2026-04-24T14:35:18.491000+00:00 (240h 33m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f787\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **12 event types**, 2112 records, 7 scenes.
- Findings: **0 FAIL**, **45 WARNING**, 60 INFO, 2 NOT_TESTED, 40 PASS.
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
| DialogueEvent | 1372 | 64.96 | 1 | 7 | 939 | 2026-04-14T14:01:43.402000+00:00 | 2026-04-24T14:35:09.766000+00:00 | 240h 33m |
| PlayerPositionEvent | 519 | 24.57 | 1 | 7 | 0 | 2026-04-14T14:01:25.406000+00:00 | 2026-04-24T14:35:18.491000+00:00 | 240h 33m |
| questEvent | 69 | 3.27 | 1 | 7 | 69 | 2026-04-14T14:01:43.387000+00:00 | 2026-04-24T14:34:24.438000+00:00 | 240h 32m |
| Topographic Map Event | 42 | 1.99 | 1 | 2 | 0 | 2026-04-16T14:16:53.461000+00:00 | 2026-04-22T14:01:43.150000+00:00 | 143h 44m |
| TopographicMapEvent | 28 | 1.33 | 1 | 2 | 0 | 2026-04-16T14:21:02.219000+00:00 | 2026-04-22T14:01:09.969000+00:00 | 143h 40m |
| soilMachine | 27 | 1.28 | 1 | 1 | 0 | 2026-04-24T14:02:42.706000+00:00 | 2026-04-24T14:17:24.429000+00:00 | 14m 41s |
| argumentationNodeEvent | 18 | 0.85 | 1 | 2 | 0 | 2026-04-14T14:28:12.985000+00:00 | 2026-04-20T14:06:53.371000+00:00 | 143h 38m |
| argumentationEvent | 12 | 0.57 | 1 | 3 | 0 | 2026-04-14T14:28:04.228000+00:00 | 2026-04-24T14:30:01.976000+00:00 | 240h 1m |
| argumentationToolEvent | 10 | 0.47 | 1 | 2 | 0 | 2026-04-20T14:05:17.159000+00:00 | 2026-04-24T14:32:38.616000+00:00 | 96h 27m |
| Soil Key Puzzle | 9 | 0.43 | 1 | 3 | 0 | 2026-04-16T14:07:50.963000+00:00 | 2026-04-22T14:15:32.697000+00:00 | 144h 7m |
| crash | 4 | 0.19 | 1 | 1 | 0 |  |  | ? |
| EndOfUnit | 2 | 0.09 | 1 | 2 | 0 | 2026-04-16T13:55:02.011000+00:00 | 2026-04-22T14:08:27.457000+00:00 | 144h 13m |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 519205.446s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
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
  - Observed: 989.117s median 
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
  - Observed: 8.223s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 20 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 12.462s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 3.713s median 
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
  - Observed: 4.572s median 
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
- **INFO / Info** `Soil Key Puzzle` — record volume changed 0.2x vs baseline. 
  - Observed: 9 records 
  - Expected: 38 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 42 records this build 
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
  - Observed: U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls; Unit 5 - What happened to the water when in Aryn's collection tanks 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 18 records 
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
  - Observed: 2; 3; 4; C; D; II 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Evaporation Flow Diagram; BackingInfoPanel - Heat Added/Released Chart; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 4 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `questEvent` `data.questID` — baseline categorical value(s) not seen this build. 
  - Observed: 25; 41; 43; 44; 45; 51; 52; 53; 54; 56; 57 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `questEvent` `data.questName` — baseline categorical value(s) not seen this build. 
  - Observed: Chief of Reasoning; Claim of Command; Desert Delicacies; Guru of Arguments; If I had a Nickel... - Floor 1; If I had a Nickel... - Floor 2; If I had a Nickel... - Floor 3; If I had a Nickel... - Floor 4; WAT Happened Here?; Water Problems Require Water Solutions; Which Watershed? 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `soilMachine` — record volume changed 5.4x vs baseline. 
  - Observed: 27 records 
  - Expected: 5 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 114 mismatch(es); e.g. 'DialogueNodeEvent:30:29' vs expected 'DialogueNodeEvent:30:104' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc965d385e3b94310f787.jsonl[314] _id=69e0e5577957a33870f4fa27 ts=2026-04-14T14:10:54.412Z`; `69cdc965d385e3b94310f787.jsonl[3] _id=69e0e5587957a33870f4fa43 ts=2026-04-14T14:11:07.724Z`; `69cdc965d385e3b94310f787.jsonl[310] _id=69e0e5597957a33870f4fa4f ts=2026-04-14T14:11:10.837Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 8 mismatch(es); e.g. 'questFinishEvent:28' vs expected 'questFinishEvent:33' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc965d385e3b94310f787.jsonl[2] _id=69e0e5587957a33870f4fa39 ts=2026-04-14T14:11:07.717Z`; `69cdc965d385e3b94310f787.jsonl[309] _id=69e0e5597957a33870f4fa4d ts=2026-04-14T14:11:10.746Z`; `69cdc965d385e3b94310f787.jsonl[17] _id=69e0e5617957a33870f4fabb ts=2026-04-14T14:13:25.419Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 42 records, TopographicMapEvent: 28 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 1371 | 0.0 | 3.543 | 631.66 | 49.865 | 341208.665 | 0.09 | 362 | 4 |
| PlayerPositionEvent | 509 | 29.84 | 30.008 | 1700.87 | 35.935 | 340940.065 | 0.04 | 0 | 4 |
| questEvent | 68 | 0.004 | 196.719 | 12734.721 | 110503.583 | 341243.739 | 0.0 | 11 | 10 |
| Topographic Map Event | 41 | 1.649 | 15.942 | 12621.7 | 1175.517 | 341506.231 | 0.0 | 0 | 4 |
| TopographicMapEvent | 27 | 0.612 | 8.223 | 19155.843 | 121305.397 | 341804.401 | 0.0 | 0 | 4 |
| soilMachine | 26 | 0.38 | 4.572 | 33.912 | 183.069 | 205.153 | 1.77 | 0 | 0 |
| argumentationNodeEvent | 17 | 2.564 | 12.462 | 30418.846 | 205565.463 | 346349.378 | 0.0 | 0 | 2 |
| argumentationEvent | 11 | 0.101 | 58.231 | 78556.159 | 346647.381 | 346960.881 | 0.0 | 0 | 3 |
| argumentationToolEvent | 9 | 0.001 | 3.713 | 38582.384 | 208303.586 | 347073.094 | 0.0 | 1 | 1 |
| Soil Key Puzzle | 8 | 3.041 | 989.117 | 64857.717 | 282521.238 | 341525.413 | 0.0 | 0 | 4 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| EndOfUnit | 1 | 519205.446 | 519205.446 | 519205.446 | 519205.446 | 519205.446 | 0.0 | 0 | 1 |

- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 2 group(s), 2 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc965d385e3b94310f787.jsonl[1395] _id=69e8cecd1724f0c9e2fa274d ts=? == 69cdc965d385e3b94310f787.jsonl[1525] _id=69e8d2621724f0c9e2fa40f9 ts=?`; `69cdc965d385e3b94310f787.jsonl[1671] _id=69e8d7661724f0c9e2fa60ed ts=? == 69cdc965d385e3b94310f787.jsonl[1827] _id=69eb790c1724f0c9e2fb8219 ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.008s (p5 29.96s, p95 35.94s, n=509) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `101ms: 69cdc965d385e3b94310f787.jsonl[1207] _id=69e6331a1724f0c9e2f88deb ts=2026-04-20T14:07:20.9940000Z ~ 69cdc965d385e3b94310f787.jsonl[1210] _id=69e6331a1724f0c9e2f88df3 ts=2026-04-20T14:07:21.0950000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `1ms: 69cdc965d385e3b94310f787.jsonl[2027] _id=69eb7e651724f0c9e2fb9c65 ts=2026-04-24T14:29:56.2690000Z ~ 69cdc965d385e3b94310f787.jsonl[249] _id=69eb7e651724f0c9e2fb9c67 ts=2026-04-24T14:29:56.2700000Z`
- **INFO / Info** `soilMachine` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 6 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `856ms: 69cdc965d385e3b94310f787.jsonl[1885] _id=69eb7a761724f0c9e2fb898d ts=2026-04-24T14:13:09.6080000Z ~ 69cdc965d385e3b94310f787.jsonl[1883] _id=69eb7a771724f0c9e2fb899f ts=2026-04-24T14:13:10.4640000Z`; `574ms: 69cdc965d385e3b94310f787.jsonl[1888] _id=69eb7a7d1724f0c9e2fb89b9 ts=2026-04-24T14:13:16.1180000Z ~ 69cdc965d385e3b94310f787.jsonl[1886] _id=69eb7a7d1724f0c9e2fb89be ts=2026-04-24T14:13:16.6920000Z`; `964ms: 69cdc965d385e3b94310f787.jsonl[1897] _id=69eb7ac31724f0c9e2fb8adb ts=2026-04-24T14:14:26.5170000Z ~ 69cdc965d385e3b94310f787.jsonl[1892] _id=69eb7ac41724f0c9e2fb8ae6 ts=2026-04-24T14:14:27.4810000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 46m 
  - Evidence: 94h 46m: 69cdc965d385e3b94310f787.jsonl[858] _id=69e0f2b17957a33870f54ff3 ts=2026-04-16T14:31:13.1580000Z -> 69cdc965d385e3b94310f787.jsonl[873] _id=69e6278c1724f0c9e2f84ab7 ts=2026-04-20T13:18:01.8230000Z; 47h 30m: 69cdc965d385e3b94310f787.jsonl[1776] _id=69e8db1c1724f0c9e2fa744b ts=2026-04-22T14:28:43.8990000Z -> 69cdc965d385e3b94310f787.jsonl[1780] _id=69eb771a1724f0c9e2fb77b1 ts=2026-04-24T13:58:49.5760000Z; 47h 2m: 69cdc965d385e3b94310f787.jsonl[119] _id=69e0e5867957a33870f4fd25 ts=2026-04-14T14:31:44.88Z -> 69cdc965d385e3b94310f787.jsonl[138] _id=69e0e5867957a33870f4fd35 ts=2026-04-16T13:34:40.1220000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 362 interval(s) ≤ 0.000s..0.003s shown 
  - Evidence: 0ms: 69cdc965d385e3b94310f787.jsonl[307] _id=69de4b1d7957a33870f349d3 ts=2026-04-14T14:10:51.3870000Z -> 69cdc965d385e3b94310f787.jsonl[313] _id=69e0e5567957a33870f4fa23 ts=2026-04-14T14:10:51.387Z; 2ms: 69cdc965d385e3b94310f787.jsonl[1334] _id=69e8cbb61724f0c9e2fa1341 ts=2026-04-22T13:23:01.0050000Z -> 69cdc965d385e3b94310f787.jsonl[1338] _id=69e8cbb61724f0c9e2fa1343 ts=2026-04-22T13:23:01.0070000Z; 3ms: 69cdc965d385e3b94310f787.jsonl[1478] _id=69e8d18a1724f0c9e2fa3c21 ts=2026-04-22T13:47:53.6500000Z -> 69cdc965d385e3b94310f787.jsonl[1498] _id=69e8d18a1724f0c9e2fa3c23 ts=2026-04-22T13:47:53.6530000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 144h 13m 
  - Evidence: 144h 13m: 69cdc965d385e3b94310f787.jsonl[591] _id=69e0ea367957a33870f51c61 ts=2026-04-16T13:55:02.0110000Z -> 69cdc965d385e3b94310f787.jsonl[1651] _id=69e8d65c1724f0c9e2fa5807 ts=2026-04-22T14:08:27.4570000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 42m 
  - Evidence: 94h 42m: 69cdc965d385e3b94310f787.jsonl[870] _id=69e0f3bb7957a33870f5590b ts=2026-04-16T14:35:39.4600000Z -> 69cdc965d385e3b94310f787.jsonl[872] _id=69e627891724f0c9e2f84ab3 ts=2026-04-20T13:17:59.5250000Z; 47h 30m: 69cdc965d385e3b94310f787.jsonl[1774] _id=69e8db191724f0c9e2fa7427 ts=2026-04-22T14:28:40.8450000Z -> 69cdc965d385e3b94310f787.jsonl[1779] _id=69eb77181724f0c9e2fb77a7 ts=2026-04-24T13:58:46.8640000Z; 47h 2m: 69cdc965d385e3b94310f787.jsonl[374] _id=69e0e5867957a33870f4fd29 ts=2026-04-14T14:31:48.4Z -> 69cdc965d385e3b94310f787.jsonl[120] _id=69e0e5867957a33870f4fd2f ts=2026-04-16T13:34:21.7070000Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 52m 
  - Evidence: 94h 52m: 69cdc965d385e3b94310f787.jsonl[857] _id=69e0f29f7957a33870f54f59 ts=2026-04-16T14:30:54.7790000Z -> 69cdc965d385e3b94310f787.jsonl[899] _id=69e628b51724f0c9e2f8502f ts=2026-04-20T13:23:00.1920000Z; 48h 2m: 69cdc965d385e3b94310f787.jsonl[1254] _id=69e6342c1724f0c9e2f893ad ts=2026-04-20T14:11:55.9010000Z -> 69cdc965d385e3b94310f787.jsonl[1682] _id=69e8d7ba1724f0c9e2fa62cd ts=2026-04-22T14:14:17.9580000Z; 38m 17s: 69cdc965d385e3b94310f787.jsonl[942] _id=69e62b0a1724f0c9e2f85dc3 ts=2026-04-20T13:32:57.6500000Z -> 69cdc965d385e3b94310f787.jsonl[1253] _id=69e634031724f0c9e2f8932b ts=2026-04-20T14:11:14.8660000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 51m 
  - Evidence: 94h 51m: 69cdc965d385e3b94310f787.jsonl[843] _id=69e0f22d7957a33870f54b97 ts=2026-04-16T14:29:00.9700000Z -> 69cdc965d385e3b94310f787.jsonl[883] _id=69e628301724f0c9e2f84ded ts=2026-04-20T13:20:47.2010000Z; 47h 56m: 69cdc965d385e3b94310f787.jsonl[1081] _id=69e62ff61724f0c9e2f87bcf ts=2026-04-20T13:53:57.9950000Z -> 69cdc965d385e3b94310f787.jsonl[1520] _id=69e8d2401724f0c9e2fa401e ts=2026-04-22T13:50:55.6410000Z; 19m 35s: 69cdc965d385e3b94310f787.jsonl[888] _id=69e628471724f0c9e2f84e4d ts=2026-04-20T13:21:10.4880000Z -> 69cdc965d385e3b94310f787.jsonl[989] _id=69e62cde1724f0c9e2f86c17 ts=2026-04-20T13:40:46.0050000Z
- **INFO / Info** `TopographicMapEvent` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 94h 56m 
  - Evidence: 94h 56m: 69cdc965d385e3b94310f787.jsonl[811] _id=69e0f1137957a33870f542c1 ts=2026-04-16T14:24:19.3030000Z -> 69cdc965d385e3b94310f787.jsonl[884] _id=69e628401724f0c9e2f84e35 ts=2026-04-20T13:21:03.7040000Z; 47h 59m: 69cdc965d385e3b94310f787.jsonl[1060] _id=69e62f591724f0c9e2f87857 ts=2026-04-20T13:51:20.4400000Z -> 69cdc965d385e3b94310f787.jsonl[1523] _id=69e8d2491724f0c9e2fa405f ts=2026-04-22T13:51:04.4900000Z; 19m 48s: 69cdc965d385e3b94310f787.jsonl[886] _id=69e628421724f0c9e2f84e39 ts=2026-04-20T13:21:06.0170000Z -> 69cdc965d385e3b94310f787.jsonl[990] _id=69e62ce71724f0c9e2f86c3f ts=2026-04-20T13:40:54.5580000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 96h 22m 
  - Evidence: 96h 22m: 69cdc965d385e3b94310f787.jsonl[1210] _id=69e6331a1724f0c9e2f88df3 ts=2026-04-20T14:07:21.0950000Z -> 69cdc965d385e3b94310f787.jsonl[250] _id=69eb7e6a1724f0c9e2fb9c75 ts=2026-04-24T14:30:01.9760000Z; 96h 12m: 69cdc965d385e3b94310f787.jsonl[546] _id=69e0e96e7957a33870f516c9 ts=2026-04-16T13:51:41.5810000Z -> 69cdc965d385e3b94310f787.jsonl[1182] _id=69e6324c1724f0c9e2f88929 ts=2026-04-20T14:03:55.4620000Z; 47h 19m: 69cdc965d385e3b94310f787.jsonl[125] _id=69e0e57e7957a33870f4fca5 ts=2026-04-14T14:30:25.036Z -> 69cdc965d385e3b94310f787.jsonl[521] _id=69e0e8e97957a33870f513b5 ts=2026-04-16T13:49:28.8510000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 2 gap(s), longest 96h 12m 
  - Evidence: 96h 12m: 69cdc965d385e3b94310f787.jsonl[545] _id=69e0e96a7957a33870f516b7 ts=2026-04-16T13:51:38.3620000Z -> 69cdc965d385e3b94310f787.jsonl[1183] _id=69e632581724f0c9e2f88971 ts=2026-04-20T14:04:07.7400000Z; 47h 19m: 69cdc965d385e3b94310f787.jsonl[123] _id=69e0e57e7957a33870f4fc9f ts=2026-04-14T14:30:03.902Z -> 69cdc965d385e3b94310f787.jsonl[527] _id=69e0e8ed7957a33870f513c5 ts=2026-04-16T13:49:33.3860000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 96h 24m 
  - Evidence: 96h 24m: 69cdc965d385e3b94310f787.jsonl[1186] _id=69e632a41724f0c9e2f88b27 ts=2026-04-20T14:05:23.1750000Z -> 69cdc965d385e3b94310f787.jsonl[2027] _id=69eb7e651724f0c9e2fb9c65 ts=2026-04-24T14:29:56.2690000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.001s..0.001s shown 
  - Evidence: 1ms: 69cdc965d385e3b94310f787.jsonl[2027] _id=69eb7e651724f0c9e2fb9c65 ts=2026-04-24T14:29:56.2690000Z -> 69cdc965d385e3b94310f787.jsonl[249] _id=69eb7e651724f0c9e2fb9c67 ts=2026-04-24T14:29:56.2700000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 10 gap(s), longest 94h 47m 
  - Evidence: 94h 47m: 69cdc965d385e3b94310f787.jsonl[850] _id=69e0f28f7957a33870f54e67 ts=2026-04-16T14:30:39.1940000Z -> 69cdc965d385e3b94310f787.jsonl[875] _id=69e6278d1724f0c9e2f84abb ts=2026-04-20T13:18:02.9330000Z; 47h 30m: 69cdc965d385e3b94310f787.jsonl[1744] _id=69e8daf71724f0c9e2fa7327 ts=2026-04-22T14:28:06.3660000Z -> 69cdc965d385e3b94310f787.jsonl[1778] _id=69eb771a1724f0c9e2fb77af ts=2026-04-24T13:58:49.3860000Z; 47h 10m: 69cdc965d385e3b94310f787.jsonl[1264] _id=69e634601724f0c9e2f894b3 ts=2026-04-20T14:12:47.1360000Z -> 69cdc965d385e3b94310f787.jsonl[1335] _id=69e8cba91724f0c9e2fa12f9 ts=2026-04-22T13:22:48.5340000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 11 interval(s) ≤ 0.004s..0.008s shown 
  - Evidence: 4ms: 69cdc965d385e3b94310f787.jsonl[511] _id=69e0e8c97957a33870f512dd ts=2026-04-16T13:48:56.4560000Z -> 69cdc965d385e3b94310f787.jsonl[150] _id=69e0e8c97957a33870f512df ts=2026-04-16T13:48:56.4600000Z; 7ms: 69cdc965d385e3b94310f787.jsonl[1818] _id=69eb78521724f0c9e2fb7ed7 ts=2026-04-24T14:04:01.3030000Z -> 69cdc965d385e3b94310f787.jsonl[1813] _id=69eb78521724f0c9e2fb7ed9 ts=2026-04-24T14:04:01.3100000Z; 8ms: 69cdc965d385e3b94310f787.jsonl[17] _id=69e0e5617957a33870f4fabb ts=2026-04-14T14:13:25.419Z -> 69cdc965d385e3b94310f787.jsonl[18] _id=69e0e5617957a33870f4fabd ts=2026-04-14T14:13:25.427Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 3 record(s) match the trigger in 69cdc965d385e3b94310f787.jsonl:69cdc965d385e3b94310f787, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc965d385e3b94310f787.jsonl[671] _id=69e0ed3a7957a33870f52c7b ts=2026-04-16T14:07:54.0040000Z`; `69cdc965d385e3b94310f787.jsonl[1254] _id=69e6342c1724f0c9e2f893ad ts=2026-04-20T14:11:55.9010000Z`; `69cdc965d385e3b94310f787.jsonl[1685] _id=69e8d8051724f0c9e2fa63f3 ts=2026-04-22T14:15:32.6970000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 28 record(s) match the trigger in 69cdc965d385e3b94310f787.jsonl:69cdc965d385e3b94310f787, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc965d385e3b94310f787.jsonl[785] _id=69e0f04e7957a33870f53ec5 ts=2026-04-16T14:21:02.2190000Z`; `69cdc965d385e3b94310f787.jsonl[786] _id=69e0f0547957a33870f53edb ts=2026-04-16T14:21:07.8090000Z`; `69cdc965d385e3b94310f787.jsonl[789] _id=69e0f0637957a33870f53f15 ts=2026-04-16T14:21:23.0750000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 3 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc965d385e3b94310f787.jsonl[1024] _id=69e62e241724f0c9e2f871af ts=2026-04-20T13:46:11.0940000Z`; `69cdc965d385e3b94310f787.jsonl[1049] _id=69e62edb1724f0c9e2f875eb ts=2026-04-20T13:49:14.0600000Z`; `69cdc965d385e3b94310f787.jsonl[1947] _id=69eb7c3c1724f0c9e2fb91f5 ts=2026-04-24T14:20:43.6900000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 5 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc965d385e3b94310f787.jsonl[100] _id=69e0e5797957a33870f4fc3d ts=2026-04-14T14:28:04.228Z`; `69cdc965d385e3b94310f787.jsonl[357] _id=69e0e57b7957a33870f4fc6d ts=2026-04-14T14:29:04.191Z`; `69cdc965d385e3b94310f787.jsonl[114] _id=69e0e57d7957a33870f4fc83 ts=2026-04-14T14:29:43.016Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc965d385e3b94310f787.jsonl[2027] _id=69eb7e651724f0c9e2fb9c65 ts=2026-04-24T14:29:56.2690000Z`; `69cdc965d385e3b94310f787.jsonl[249] _id=69eb7e651724f0c9e2fb9c67 ts=2026-04-24T14:29:56.2700000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 8 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc965d385e3b94310f787.jsonl[2] _id=69e0e5587957a33870f4fa39 ts=2026-04-14T14:11:07.717Z`; `69cdc965d385e3b94310f787.jsonl[17] _id=69e0e5617957a33870f4fabb ts=2026-04-14T14:13:25.419Z`; `69cdc965d385e3b94310f787.jsonl[31] _id=69e0e5687957a33870f4fb23 ts=2026-04-14T14:17:12.214Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 4 records 
  - Examples: `69cdc965d385e3b94310f787.jsonl[1395] _id=69e8cecd1724f0c9e2fa274d ts=?`; `69cdc965d385e3b94310f787.jsonl[1525] _id=69e8d2621724f0c9e2fa40f9 ts=?`; `69cdc965d385e3b94310f787.jsonl[1671] _id=69e8d7661724f0c9e2fa60ed ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 2 occurrence(s) 
  - Examples: `69cdc965d385e3b94310f787.jsonl[899] _id=69e628b51724f0c9e2f8502f ts=2026-04-20T13:23:00.1920000Z`; `69cdc965d385e3b94310f787.jsonl[942] _id=69e62b0a1724f0c9e2f85dc3 ts=2026-04-20T13:32:57.6500000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 172 unmatched 'DialogueStartEvent' (totals: 301 start, 132 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 3 unmatched 'Started' (totals: 6 open, 3 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 4 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 21 unmatched 'questActiveEvent' (totals: 41 start, 28 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.88s, min -170603.60s, max -0.33s over 2108 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc965d385e3b94310f787\coverage.yaml

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
  - Observed: 42 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 4 records 
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

### `DialogueEvent` — 1372 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 1 Dev (346); Unit 3 Dev (330); Unit 2 Prod (Refactor) (223); Unit 3 Dungeon Dev (148); Unit 4 Dev - Dungeon (129); Unit 4 Dev - Anderson Base (104); Unit 4 Dev (92)
- **eventKey:** present on 939 of 1372 records
- **Intervals:** median 3.54s (p5 0.01s / p95 49.86s, n=1371)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x939; [conversationId, dialogueEventType] x433
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 1372/1372 records)
    numeric range 10 .. 107 (34 unique)
data.dialogueEventType  (string, 1372/1372 records)
    "DialogueNodeEvent"  x939
    "DialogueStartEvent"  x301
    "DialogueFinishEvent"  x132
data.nodeId  (number, 939/1372 records)
    numeric range 0 .. 289 (198 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 519 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 3 Dev (111); Unit 2 Prod (Refactor) (107); Unit 1 Dev (102); Unit 3 Dungeon Dev (87); Unit 4 Dev - Dungeon (54); Unit 4 Dev (39); Unit 4 Dev - Anderson Base (19)
- **Intervals:** median 30.01s (p5 29.96s / p95 35.94s, n=509)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 519/519 records)
data.position.x  (number, 519/519 records)
    numeric range -694.5 .. 1484.9 (304 unique)
data.position.y  (number, 519/519 records)
    numeric range -114.326 .. 178.907 (226 unique)
data.position.z  (number, 519/519 records)
    numeric range -1108.69 .. 1893.33 (305 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 69 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 4 Dev - Dungeon (15); Unit 2 Prod (Refactor) (10); Unit 3 Dev (10); Unit 3 Dungeon Dev (4); Unit 4 Dev (4); Unit 4 Dev - Anderson Base (2)
- **eventKey:** present on 69 of 69 records
- **Intervals:** median 196.72s (p5 0.01s / p95 110503.58s, n=68)
- **`data` key-set variants:** [questEventType, questID, questName] x41; [questEventType, questID, questName, questSuccessOrFailure] x28
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 69/69 records)
    "questActiveEvent"  x41
    "questFinishEvent"  x28
data.questID  (string, 69/69 records)
    23 unique values (see csv/event_unique_values.csv)
data.questName  (string, 69/69 records)
    23 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 28/69 records)
    "Succeeded"  x28
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 42 records

- **Scenes:** Unit 3 Dev (22); Unit 2 Prod (Refactor) (20)
- **Intervals:** median 15.94s (p5 3.69s / p95 1175.52s, n=41)
- **Fields under `data`:**

```text
data.actionType  (string, 42/42 records)
    "MapCloseEvent"  x21
    "MapOpenEvent"  x21
data.featureUsed  (string, 42/42 records)
    "Map"  x42
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `TopographicMapEvent` — 28 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 3 Dev (20); Unit 2 Prod (Refactor) (8)
- **Intervals:** median 8.22s (p5 1.57s / p95 121305.40s, n=27)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "dragEnd"  x14
    "dragStart"  x14
data.featureUsed  (string, 28/28 records)
    "waypoint"  x28
data.location  (object, 28/28 records)
data.location.x  (number, 28/28 records)
    numeric range -770.79 .. 171.168 (15 unique)
data.location.y  (number, 28/28 records)
    numeric range -320.053 .. 246.527 (15 unique)
data.location.z  (number, 28/28 records)
    1 unique values (see csv/event_unique_values.csv)
```

Raw examples: `event_examples.json` -> `TopographicMapEvent`.

### `soilMachine` — 27 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (27)
- **Intervals:** median 4.57s (p5 0.57s / p95 183.07s, n=26)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 27/27 records)
    "ChangeCanister"  x27
data.canisterType  (string, 27/27 records)
    "Bedrock"  x14
    "Clay"  x8
    "Gravel"  x3
    "Sand"  x2
data.floor  (string, 27/27 records)
    "5"  x23
    "3"  x2
    "4"  x2
data.machine  (string, 27/27 records)
    "1"  x26
    "2"  x1
data.row  (string, 27/27 records)
    "TopRow"  x14
    "BottomRow"  x13
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `argumentationNodeEvent` — 18 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 1 Dev (13); Unit 3 Dev (5)
- **Intervals:** median 12.46s (p5 3.39s / p95 205565.46s, n=17)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 18/18 records)
    "argumentationNodeAdd"  x16
    "argumentationNodeRemove"  x2
data.argumentationTitle  (string, 18/18 records)
    "Unit 1 - Freshwater"  x9
    "Unit 3 - Pollution Upstream"  x5
    "Unit 1 - Argumentation Tutorial"  x4
data.nodeName  (string, 18/18 records)
    "B"  x7
    "1"  x6
    "I"  x3
    "5"  x1
    "A"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 12 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 58.23s (p5 16.24s / p95 346647.38s, n=11)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 12/12 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x4
data.argumentationDescription  (string, 12/12 records)
    "Unit 1 - Does the planet WAT-247 have freshwater"  x6
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 12/12 records)
    "Unit 1 - Freshwater"  x6
    "Unit 3 - Pollution Upstream"  x3
    "Unit 1 - Argumentation Tutorial"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `argumentationToolEvent` — 10 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (8); Unit 3 Dev (2)
- **Intervals:** median 3.71s (p5 0.03s / p95 208303.59s, n=9)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 10/10 records)
    "argumentationToolClose"  x6
    "argumentationToolOpen"  x4
data.argumentationTitle  (string, 10/10 records)
    "Unit 4 - Flooding"  x8
    "Unit 3 - Pollution Upstream"  x2
data.toolName  (string, 10/10 records)
    "BackingInfoPanel - Soil Flow Rates"  x4
    "BackingInfoPanel - Soil Layers and Fountain Data"  x4
    "BackingInfoPanel - Pollution Site Data"  x2
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `Soil Key Puzzle` — 9 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (5); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 989.12s (p5 16.34s / p95 282521.24s, n=8)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 9/9 records)
    "Started"  x6
    "Finished"  x3
data.Unit  (string, 9/9 records)
    "Unit 2 Prod (Refactor)"  x5
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `crash` — 4 records

- **Scenes:** <missing sceneName> (4)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 4/4 records)
    true  x4
data.message  (string, 4/4 records)
    "Uncaught ReferenceError: onResize is not defined"  x4
data.phase  (string, 4/4 records)
    "running"  x4
data.stack  (string, 4/4 records)
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit3:831:9)"  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit4:831:9)"  x2
data.type  (string, 4/4 records)
    "runtime_error"  x4
data.unitId  (string, 4/4 records)
    "unit3"  x2
    "unit4"  x2
data.workspace  (string, 4/4 records)
    "mhs"  x4
```

Raw examples: `event_examples.json` -> `crash`.

### `EndOfUnit` — 2 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (1); Unit 3 Dev (1)
- **Intervals:** median 519205.45s (p5 519205.45s / p95 519205.45s, n=1)
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
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (5 records)
- `TopographicMapEvent` data.actionType: "dragStart" (14x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (2x)
- `soilMachine` data.canisterType: "Bedrock" (14x)

**Additional gameplay testing (content not exercised):**
- `SolarStillDesignEvent`: expected event type absent, but its content was not exercised this playthrough
- `WaterChamberEvent`: expected event type absent, but its content was not exercised this playthrough


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*