# MHS Gameplay Log Audit Report — build fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75e

## 1. Build Information

- **Build ID:** fall2026-bowling-green-wayne-county / 69cdc937d385e3b94310f75e
- **Game version string(s) in log:** 2.2.4, 20260401-10923, 20260408-10923
- **Audit date:** 2026-10-25
- **Log file(s):** 69cdc937d385e3b94310f75e.jsonl
- **Records:** 3034 (0 malformed skipped)
- **Sessions (file x user):** 1
- **Player id(s):** 69cdc937d385e3b94310f75e
- **Time span:** 2026-04-13T19:26:34.119000+00:00 .. 2026-04-21T20:03:01.820000+00:00 (192h 36m)
- **Coverage:** manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75e\coverage.yaml
- **Baseline:** snapshot build-log-qa\reports\09-23-26\snapshot.json

## 2. Executive Summary

- **14 event types**, 3034 records, 9 scenes.
- Findings: **0 FAIL**, **48 WARNING**, 60 INFO, 0 NOT_TESTED, 56 PASS.
- Top items needing attention:
  - WARNING/Medium `DEBUGMenu`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `DaniEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `InputEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `ObjectInterEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `PuzzlePieceVisibleEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `SolarStillDesignEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `argumentationAnswerEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `chatEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameStartEvent`: expected event type absent although its content was played — possible logging failure
  - WARNING/Medium `gameWindowFocusEvent`: expected event type absent although its content was played — possible logging failure

## 3. Event Inventory

| eventType | record_count | percent_of_total | session_count | scene_count | eventKey_records | first_timestamp | last_timestamp | active_span |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2304 | 75.94 | 1 | 9 | 1633 | 2026-04-13T19:26:53.215000+00:00 | 2026-04-21T20:02:52.399000+00:00 | 192h 35m |
| PlayerPositionEvent | 450 | 14.83 | 1 | 9 | 0 | 2026-04-13T19:26:34.119000+00:00 | 2026-04-21T20:02:59.009000+00:00 | 192h 36m |
| questEvent | 101 | 3.33 | 1 | 9 | 101 | 2026-04-13T19:26:53.179000+00:00 | 2026-04-21T20:02:14.180000+00:00 | 192h 35m |
| Topographic Map Event | 34 | 1.12 | 1 | 2 | 0 | 2026-04-13T19:50:02.278000+00:00 | 2026-04-17T19:56:29.466000+00:00 | 96h 6m |
| WaterChamberEvent | 32 | 1.05 | 1 | 1 | 0 | 2026-04-21T19:43:41.512000+00:00 | 2026-04-21T19:47:58.016000+00:00 | 4m 16s |
| argumentationToolEvent | 28 | 0.92 | 1 | 2 | 0 | 2026-04-21T19:24:57.405000+00:00 | 2026-04-21T19:53:58.935000+00:00 | 29m 1s |
| argumentationNodeEvent | 20 | 0.66 | 1 | 3 | 0 | 2026-04-13T19:38:37.028000+00:00 | 2026-04-17T19:36:46.010000+00:00 | 95h 58m |
| argumentationEvent | 16 | 0.53 | 1 | 5 | 0 | 2026-04-13T19:37:49.138000+00:00 | 2026-04-21T19:54:58.357000+00:00 | 192h 17m |
| soilMachine | 14 | 0.46 | 1 | 1 | 0 | 2026-04-21T19:00:47.146000+00:00 | 2026-04-21T19:09:41.132000+00:00 | 8m 53s |
| Soil Key Puzzle | 13 | 0.43 | 1 | 3 | 0 | 2026-04-13T19:53:27.350000+00:00 | 2026-04-17T20:05:30.967000+00:00 | 96h 12m |
| TerasGardenBox | 11 | 0.36 | 1 | 1 | 0 | 2026-04-21T19:34:15.906000+00:00 | 2026-04-21T19:35:19.725000+00:00 | 1m 3s |
| EndOfUnit | 6 | 0.2 | 1 | 5 | 0 | 2026-04-13T19:41:46.006000+00:00 | 2026-04-21T20:03:01.820000+00:00 | 192h 21m |
| crash | 3 | 0.1 | 1 | 1 | 0 |  |  | ? |
| TopographicMapEvent | 2 | 0.07 | 1 | 1 | 0 | 2026-04-15T19:43:38.266000+00:00 | 2026-04-15T19:43:45.441000+00:00 | 7.2s |

Full details incl. observed scenes and data fields: `csv/event_type_summary.csv`.

## 4. New / Removed / Changed Events (vs baseline)

- **WARNING / Medium** `DEBUGMenu` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 12 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `DialogueEvent` — median interval between records changed substantially. 
  - Observed: 1.145s median 
  - Expected: 3.7s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `EndOfUnit` — median interval between records changed substantially. 
  - Observed: 171213.908s median 
  - Expected: 2855.05s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `InputEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 2411 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `ObjectInterEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 235 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `PlayerPositionEvent` — median interval between records changed substantially. 
  - Observed: 30.051s median 
  - Expected: 10.005s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5172 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `Soil Key Puzzle` — baseline field(s) absent this build. 
  - Observed: data.actionType; data.currentSoilType; data.isCorrectSelection; data.waterLevelStatus; data.waterRetentionChange 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `Soil Key Puzzle` — median interval between records changed substantially. 
  - Observed: 238.739s median 
  - Expected: 0.8s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `SolarStillDesignEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 4 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `TopographicMapEvent` — baseline field(s) absent this build. 
  - Observed: data.legendName 
  - Expected: schema change or conditional content — review
- **WARNING / Medium** `TopographicMapEvent` — median interval between records changed substantially. 
  - Observed: 7.175s median 
  - Expected: 1.827s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `WaterChamberEvent` — median interval between records changed substantially. 
  - Observed: 5.741s median 
  - Expected: 19.608s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationAnswerEvent` — event type present in baseline 09-23-26 but absent now. 
  - Observed: 0 records this build 
  - Expected: 5 records in baseline; check coverage before treating as a logging regression
- **WARNING / Medium** `argumentationNodeEvent` — median interval between records changed substantially. 
  - Observed: 8.39s median 
  - Expected: 0.467s in 09-23-26 
  - Evidence: regression candidate requiring review
- **WARNING / Medium** `argumentationToolEvent` — median interval between records changed substantially. 
  - Observed: 1.565s median 
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
  - Observed: 19.834s median 
  - Expected: 62.313s in 09-23-26 
  - Evidence: regression candidate requiring review
- **INFO / Info** — baseline scene name(s) absent this build. 
  - Observed: MainMenu; Transition 
  - Expected: renamed scene, removed content, or reduced coverage
- **INFO / Info** — scene name(s) not present in baseline. 
  - Observed: <missing sceneName> 
  - Expected: renamed scene, new content, or new coverage
- **INFO / Info** `TerasGardenBox` — field(s) not present in baseline schema. 
  - Observed: data.boxID
- **INFO / Info** `TerasGardenBox` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `TerasGardenBox` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: soilSelected 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `Topographic Map Event` — event type not present in baseline 09-23-26. 
  - Observed: 34 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `TopographicMapEvent` — record volume changed 0.0x vs baseline. 
  - Observed: 2 records 
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
- **INFO / Info** `argumentationNodeEvent` — record volume changed 0.1x vs baseline. 
  - Observed: 20 records 
  - Expected: 140 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — baseline categorical value(s) not seen this build. 
  - Observed: argumentationNodeHoverEnd; argumentationNodeHoverStart 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationNodeRemove 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationNodeEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Argumentation Tutorial; Unit 4 - Flooding; Unit 5 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationNodeEvent` `data.nodeName` — baseline categorical value(s) not seen this build. 
  - Observed: 2; 3; 4; C 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` — record volume changed 3.1x vs baseline. 
  - Observed: 28 records 
  - Expected: 9 in 09-23-26 
  - Evidence: regression candidate: gameplay length, coverage, or logging-rate change
- **INFO / Info** `argumentationToolEvent` `data.actionType` — categorical value(s) not seen in baseline. 
  - Observed: argumentationToolClose 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — baseline categorical value(s) not seen this build. 
  - Observed: Unit 1 - Freshwater; Unit 2 – Watershed; Unit 3 - Pollution Upstream 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.argumentationTitle` — categorical value(s) not seen in baseline. 
  - Observed: Unit 4 - Flooding 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — baseline categorical value(s) not seen this build. 
  - Observed: BackingInfoPanel - ; BackingInfoPanel - Pollution Site Data; BackingInfoPanel - Waterfall Data; BackingInfoPanel - Watershed Graph; BackingInfoPanel - Watershed Image 
  - Expected: may simply not have been exercised — review
- **INFO / Info** `argumentationToolEvent` `data.toolName` — categorical value(s) not seen in baseline. 
  - Observed: BackingInfoPanel - Soil Flow Rates; BackingInfoPanel - Soil Layers and Fountain Data 
  - Expected: new design, renamed value, or new coverage — review
- **INFO / Info** `crash` — event type not present in baseline 09-23-26. 
  - Observed: 3 records this build 
  - Expected: new logging or newly exercised content — review
- **INFO / Info** `soilMachine` `data.canisterType` — categorical value(s) not seen in baseline. 
  - Observed: Bedrock 
  - Expected: new design, renamed value, or new coverage — review

Full diff: `csv/regression_diff.csv`.

## 5. Schema Findings

- **WARNING / Medium** `DialogueEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 181 mismatch(es); e.g. 'DialogueNodeEvent:36:52' vs expected 'DialogueNodeEvent:36:55' 
  - Expected: {data.dialogueEventType}:{data.conversationId}:{data.nodeId} 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[809] _id=69dd45007957a33870f29dd5 ts=2026-04-13T19:33:19.2350000Z`; `69cdc937d385e3b94310f75e.jsonl[859] _id=69dd46607957a33870f2a23d ts=2026-04-13T19:39:11.6910000Z`; `69cdc937d385e3b94310f75e.jsonl[158] _id=69dd4bbf7957a33870f2b62b ts=2026-04-13T20:02:06.3870000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `questEvent` `eventKey` — eventKey does not match its documented format. 
  - Observed: 1 mismatch(es); e.g. 'questActiveEvent:21' vs expected 'questActiveEvent:22' 
  - Expected: {data.questEventType}:{data.questID} 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[1381] _id=69dfe9027957a33870f48055 ts=2026-04-15T19:37:36.5410000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Low** — eventType name variants that differ only in spelling/case. 
  - Observed: Topographic Map Event, TopographicMapEvent 
  - Expected: one canonical eventType name 
  - Evidence: Topographic Map Event: 34 records, TopographicMapEvent: 2 records
- **WARNING / Low** `TerasGardenBox` — field-name variants that differ only in spelling/case. 
  - Observed: data.boxID, data.boxId 
  - Expected: one canonical field name 
  - Evidence: data.boxID: 7 records, data.boxId: 4 records

## 6. Frequency Findings

| eventType | n_intervals | interval_min_s | interval_median_s | interval_mean_s | interval_p95_s | interval_max_s | records_per_active_minute | burst_pairs | long_gaps |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DialogueEvent | 2303 | 0.0 | 1.145 | 301.068 | 27.222 | 341028.017 | 0.2 | 556 | 3 |
| PlayerPositionEvent | 432 | 0.0 | 30.051 | 1601.839 | 37.761 | 341008.705 | 0.04 | 1 | 3 |
| questEvent | 100 | 0.002 | 106.409 | 6933.21 | 489.524 | 341002.897 | 0.01 | 18 | 5 |
| Topographic Map Event | 33 | 0.472 | 22.291 | 10484.46 | 68888.908 | 171858.666 | 0.01 | 0 | 4 |
| WaterChamberEvent | 31 | 0.72 | 5.741 | 8.274 | 18.902 | 37.141 | 7.25 | 0 | 0 |
| argumentationToolEvent | 27 | 0.002 | 1.565 | 64.501 | 101.343 | 1478.854 | 0.93 | 4 | 1 |
| argumentationNodeEvent | 19 | 0.612 | 8.39 | 18183.631 | 171199.233 | 171989.409 | 0.0 | 0 | 3 |
| argumentationEvent | 15 | 0.095 | 60.628 | 46148.615 | 223838.451 | 344891.791 | 0.0 | 0 | 5 |
| soilMachine | 13 | 0.441 | 19.834 | 41.076 | 114.254 | 128.738 | 1.46 | 0 | 0 |
| Soil Key Puzzle | 12 | 2.676 | 238.739 | 28860.301 | 171291.607 | 172363.211 | 0.0 | 0 | 4 |
| TerasGardenBox | 10 | 0.604 | 2.949 | 6.382 | 18.678 | 20.38 | 9.4 | 0 | 0 |
| EndOfUnit | 5 | 1381.785 | 171213.908 | 138495.163 | 310002.489 | 344510.825 | 0.0 | 0 | 5 |
| crash | 0 |  |  |  |  |  | 0.0 | 0 | 0 |
| TopographicMapEvent | 1 | 7.175 | 7.175 | 7.175 | 7.175 | 7.175 | 8.36 | 0 | 0 |

- **WARNING / Medium** `DialogueEvent` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[439] _id=69e286a91724f0c9e2f7a37a ts=2026-04-17T19:10:48.645Z == 69cdc937d385e3b94310f75e.jsonl[1954] _id=69e286b91724f0c9e2f7a3c8 ts=2026-04-17T19:10:48.645Z`
- **WARNING / Medium** `crash` — exact duplicate records (same timestamp, scene and data). 
  - Observed: 1 group(s), 1 redundant record(s) 
  - Expected: each gameplay moment logged once 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[2543] _id=69e7ce431724f0c9e2f9d135 ts=? == 69cdc937d385e3b94310f75e.jsonl[2808] _id=69e7d2921724f0c9e2f9e71f ts=?`
- **WARNING / Medium** `PlayerPositionEvent` — continuous cadence differs from expectation. 
  - Observed: median interval 30.051s (p5 29.96s, p95 37.76s, n=432) 
  - Expected: ~10s (±0.6s) 
  - Evidence: regression candidate: cadence change or logging change 
  - Spec source: 08-13-26/Investigation-results/position-event-investigation.md
- **INFO / Info** `Topographic Map Event` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `472ms: 69cdc937d385e3b94310f75e.jsonl[1693] _id=69dff0307957a33870f49e27 ts=2026-04-15T20:08:14.0980000Z ~ 69cdc937d385e3b94310f75e.jsonl[1694] _id=69dff0327957a33870f49e34 ts=2026-04-15T20:08:14.5700000Z`
- **INFO / Info** `argumentationEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 1 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `95ms: 69cdc937d385e3b94310f75e.jsonl[2033] _id=69e28bd01724f0c9e2f7b762 ts=2026-04-17T19:36:47.9230000Z ~ 69cdc937d385e3b94310f75e.jsonl[501] _id=69e28bd11724f0c9e2f7b768 ts=2026-04-17T19:36:48.0180000Z`
- **INFO / Info** `argumentationToolEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 2 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc937d385e3b94310f75e.jsonl[643] _id=69e7cf0a1724f0c9e2f9d437 ts=2026-04-21T19:24:57.4050000Z ~ 69cdc937d385e3b94310f75e.jsonl[644] _id=69e7cf0a1724f0c9e2f9d439 ts=2026-04-21T19:24:57.4070000Z`; `620ms: 69cdc937d385e3b94310f75e.jsonl[2941] _id=69e7d5d41724f0c9e2f9f2e5 ts=2026-04-21T19:53:56.0530000Z ~ 69cdc937d385e3b94310f75e.jsonl[2943] _id=69e7d5d51724f0c9e2f9f2e9 ts=2026-04-21T19:53:56.6730000Z`
- **INFO / Info** `questEvent` — near-duplicate records within 1s (identical data, different timestamp). 
  - Observed: 3 pair(s) 
  - Expected: review whether the interaction really fired twice 
  - Examples: `2ms: 69cdc937d385e3b94310f75e.jsonl[1381] _id=69dfe9027957a33870f48055 ts=2026-04-15T19:37:36.5410000Z ~ 69cdc937d385e3b94310f75e.jsonl[1376] _id=69dfe9037957a33870f4805d ts=2026-04-15T19:37:36.5430000Z`; `7ms: 69cdc937d385e3b94310f75e.jsonl[696] _id=69e7d6271724f0c9e2f9f42f ts=2026-04-21T19:55:18.4770000Z ~ 69cdc937d385e3b94310f75e.jsonl[697] _id=69e7d6271724f0c9e2f9f431 ts=2026-04-21T19:55:18.4840000Z`; `8ms: 69cdc937d385e3b94310f75e.jsonl[713] _id=69e7d7ac1724f0c9e2f9faa5 ts=2026-04-21T20:01:48.2950000Z ~ 69cdc937d385e3b94310f75e.jsonl[714] _id=69e7d7ad1724f0c9e2f9faa7 ts=2026-04-21T20:01:48.3030000Z`
- **INFO / Info** `DialogueEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc937d385e3b94310f75e.jsonl[2293] _id=69e293721724f0c9e2f7dc1c ts=2026-04-17T20:09:21.7110000Z -> 69cdc937d385e3b94310f75e.jsonl[2297] _id=69e7c7961724f0c9e2f9acb1 ts=2026-04-21T18:53:09.7280000Z; 47h 3m: 69cdc937d385e3b94310f75e.jsonl[1087] _id=69dd4d817957a33870f2bc4f ts=2026-04-13T20:09:36.7100000Z -> 69cdc937d385e3b94310f75e.jsonl[1111] _id=69dfe35d7957a33870f469f9 ts=2026-04-15T19:13:33.0460000Z; 46h 42m: 69cdc937d385e3b94310f75e.jsonl[361] _id=69dff0527957a33870f49f2c ts=2026-04-15T20:08:49.3850000Z -> 69cdc937d385e3b94310f75e.jsonl[1732] _id=69e281191724f0c9e2f78eb8 ts=2026-04-17T18:51:05.1540000Z
- **INFO / Info** `DialogueEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 556 interval(s) ≤ 0.000s..0.004s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75e.jsonl[439] _id=69e286a91724f0c9e2f7a37a ts=2026-04-17T19:10:48.645Z -> 69cdc937d385e3b94310f75e.jsonl[1954] _id=69e286b91724f0c9e2f7a3c8 ts=2026-04-17T19:10:48.645Z; 0ms: 69cdc937d385e3b94310f75e.jsonl[580] _id=69e290d21724f0c9e2f7d0ba ts=2026-04-17T19:58:09.2300000Z -> 69cdc937d385e3b94310f75e.jsonl[1725] _id=69e2914e1724f0c9e2f7d1d6 ts=2026-04-17T19:58:09.23Z; 4ms: 69cdc937d385e3b94310f75e.jsonl[1018] _id=69dd4af57957a33870f2b2d5 ts=2026-04-13T19:58:44.6830000Z -> 69cdc937d385e3b94310f75e.jsonl[138] _id=69dd4af57957a33870f2b2d9 ts=2026-04-13T19:58:44.6870000Z
- **INFO / Info** `EndOfUnit` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 41m 
  - Evidence: 95h 41m: 69cdc937d385e3b94310f75e.jsonl[579] _id=69e290d21724f0c9e2f7d0b8 ts=2026-04-17T19:58:09.2100000Z -> 69cdc937d385e3b94310f75e.jsonl[2809] _id=69e7d2901724f0c9e2f9e717 ts=2026-04-21T19:40:00.0350000Z; 47h 46m: 69cdc937d385e3b94310f75e.jsonl[887] _id=69dd46fa7957a33870f2a453 ts=2026-04-13T19:41:46.0060000Z -> 69cdc937d385e3b94310f75e.jsonl[1288] _id=69dfe6bb7957a33870f477ff ts=2026-04-15T19:27:55.1530000Z; 47h 33m: 69cdc937d385e3b94310f75e.jsonl[1288] _id=69dfe6bb7957a33870f477ff ts=2026-04-15T19:27:55.1530000Z -> 69cdc937d385e3b94310f75e.jsonl[402] _id=69e283891724f0c9e2f79798 ts=2026-04-17T19:01:29.0610000Z
- **INFO / Info** `PlayerPositionEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc937d385e3b94310f75e.jsonl[2290] _id=69e293691724f0c9e2f7dbee ts=2026-04-17T20:09:12.3970000Z -> 69cdc937d385e3b94310f75e.jsonl[2294] _id=69e7c77a1724f0c9e2f9ac1d ts=2026-04-21T18:52:41.1020000Z; 46h 59m: 69cdc937d385e3b94310f75e.jsonl[1088] _id=69dd4da67957a33870f2bcab ts=2026-04-13T20:10:13.7030000Z -> 69cdc937d385e3b94310f75e.jsonl[1091] _id=69dfe2707957a33870f4672b ts=2026-04-15T19:09:35.5550000Z; 46h 42m: 69cdc937d385e3b94310f75e.jsonl[1704] _id=69dff0397957a33870f49e63 ts=2026-04-15T20:08:24.9990000Z -> 69cdc937d385e3b94310f75e.jsonl[1730] _id=69e2810a1724f0c9e2f78e8e ts=2026-04-17T18:50:49.8670000Z
- **INFO / Info** `PlayerPositionEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 1 interval(s) ≤ 0.000s..0.000s shown 
  - Evidence: 0ms: 69cdc937d385e3b94310f75e.jsonl[1977] _id=69e287a71724f0c9e2f7a79e ts=2026-04-17T19:17:00.9250000Z -> 69cdc937d385e3b94310f75e.jsonl[1981] _id=69e28a6b1724f0c9e2f7b27e ts=2026-04-17T19:17:00.925Z
- **INFO / Info** `Soil Key Puzzle` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 52m 
  - Evidence: 47h 52m: 69cdc937d385e3b94310f75e.jsonl[1521] _id=69dfebba7957a33870f48a85 ts=2026-04-15T19:49:14.1730000Z -> 69cdc937d385e3b94310f75e.jsonl[521] _id=69e28d061724f0c9e2f7bbd6 ts=2026-04-17T19:41:57.3840000Z; 47h 20m: 69cdc937d385e3b94310f75e.jsonl[103] _id=69dd49ba7957a33870f2aeb5 ts=2026-04-13T19:53:30.0260000Z -> 69cdc937d385e3b94310f75e.jsonl[1117] _id=69dfe3697957a33870f46a2d ts=2026-04-15T19:13:44.8660000Z; 22m 44s: 69cdc937d385e3b94310f75e.jsonl[2064] _id=69e28d251724f0c9e2f7bc56 ts=2026-04-17T19:42:28.2090000Z -> 69cdc937d385e3b94310f75e.jsonl[2252] _id=69e292791724f0c9e2f7d708 ts=2026-04-17T20:05:12.8760000Z
- **INFO / Info** `Topographic Map Event` — unusually long gaps between records. 
  - Observed: 4 gap(s), longest 47h 44m 
  - Evidence: 47h 44m: 69cdc937d385e3b94310f75e.jsonl[1694] _id=69dff0327957a33870f49e34 ts=2026-04-15T20:08:14.5700000Z -> 69cdc937d385e3b94310f75e.jsonl[2166] _id=69e28f821724f0c9e2f7cd46 ts=2026-04-17T19:52:33.2360000Z; 47h 4m: 69cdc937d385e3b94310f75e.jsonl[1068] _id=69dd4c9d7957a33870f2b9f3 ts=2026-04-13T20:05:49.0700000Z -> 69cdc937d385e3b94310f75e.jsonl[1092] _id=69dfe27f7957a33870f4673d ts=2026-04-15T19:09:50.4250000Z; 30m 53s: 69cdc937d385e3b94310f75e.jsonl[1103] _id=69dfe3247957a33870f4696d ts=2026-04-15T19:12:35.7510000Z -> 69cdc937d385e3b94310f75e.jsonl[1452] _id=69dfea647957a33870f48623 ts=2026-04-15T19:43:29.6940000Z
- **INFO / Info** `argumentationEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 95h 48m 
  - Evidence: 95h 48m: 69cdc937d385e3b94310f75e.jsonl[501] _id=69e28bd11724f0c9e2f7b768 ts=2026-04-17T19:36:48.0180000Z -> 69cdc937d385e3b94310f75e.jsonl[2584] _id=69e7cf0c1724f0c9e2f9d441 ts=2026-04-21T19:24:59.8090000Z; 47h 45m: 69cdc937d385e3b94310f75e.jsonl[45] _id=69dd46607957a33870f2a23b ts=2026-04-13T19:39:11.6550000Z -> 69cdc937d385e3b94310f75e.jsonl[199] _id=69dfe6167957a33870f474eb ts=2026-04-15T19:25:10.1030000Z; 47h 31m: 69cdc937d385e3b94310f75e.jsonl[1242] _id=69dfe6367957a33870f4754d ts=2026-04-15T19:25:41.7370000Z -> 69cdc937d385e3b94310f75e.jsonl[1815] _id=69e282861724f0c9e2f793ba ts=2026-04-17T18:57:09.9190000Z
- **INFO / Info** `argumentationNodeEvent` — unusually long gaps between records. 
  - Observed: 3 gap(s), longest 47h 46m 
  - Evidence: 47h 46m: 69cdc937d385e3b94310f75e.jsonl[857] _id=69dd46587957a33870f2a21f ts=2026-04-13T19:39:03.7310000Z -> 69cdc937d385e3b94310f75e.jsonl[1244] _id=69dfe62d7957a33870f47535 ts=2026-04-15T19:25:33.1400000Z; 47h 31m: 69cdc937d385e3b94310f75e.jsonl[1246] _id=69dfe6347957a33870f47547 ts=2026-04-15T19:25:39.9480000Z -> 69cdc937d385e3b94310f75e.jsonl[1821] _id=69e2829b1724f0c9e2f79400 ts=2026-04-17T18:57:31.3840000Z; 37m 15s: 69cdc937d385e3b94310f75e.jsonl[1839] _id=69e282e21724f0c9e2f794fc ts=2026-04-17T18:58:42.2200000Z -> 69cdc937d385e3b94310f75e.jsonl[2029] _id=69e28b9e1724f0c9e2f7b692 ts=2026-04-17T19:35:57.9750000Z
- **INFO / Info** `argumentationToolEvent` — unusually long gaps between records. 
  - Observed: 1 gap(s), longest 24m 38s 
  - Evidence: 24m 38s: 69cdc937d385e3b94310f75e.jsonl[2622] _id=69e7d0011724f0c9e2f9d8a1 ts=2026-04-21T19:29:04.5800000Z -> 69cdc937d385e3b94310f75e.jsonl[2933] _id=69e7d5c81724f0c9e2f9f297 ts=2026-04-21T19:53:43.4340000Z
- **INFO / Info** `argumentationToolEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 4 interval(s) ≤ 0.002s..0.019s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f75e.jsonl[643] _id=69e7cf0a1724f0c9e2f9d437 ts=2026-04-21T19:24:57.4050000Z -> 69cdc937d385e3b94310f75e.jsonl[644] _id=69e7cf0a1724f0c9e2f9d439 ts=2026-04-21T19:24:57.4070000Z; 17ms: 69cdc937d385e3b94310f75e.jsonl[2937] _id=69e7d5ce1724f0c9e2f9f2bd ts=2026-04-21T19:53:50.2260000Z -> 69cdc937d385e3b94310f75e.jsonl[2940] _id=69e7d5cf1724f0c9e2f9f2bf ts=2026-04-21T19:53:50.2430000Z; 19ms: 69cdc937d385e3b94310f75e.jsonl[2942] _id=69e7d5d51724f0c9e2f9f2e7 ts=2026-04-21T19:53:56.6540000Z -> 69cdc937d385e3b94310f75e.jsonl[2943] _id=69e7d5d51724f0c9e2f9f2e9 ts=2026-04-21T19:53:56.6730000Z
- **INFO / Info** `questEvent` — unusually long gaps between records. 
  - Observed: 5 gap(s), longest 94h 43m 
  - Evidence: 94h 43m: 69cdc937d385e3b94310f75e.jsonl[2291] _id=69e293711724f0c9e2f7dc12 ts=2026-04-17T20:09:20.5230000Z -> 69cdc937d385e3b94310f75e.jsonl[2295] _id=69e7c77c1724f0c9e2f9ac29 ts=2026-04-21T18:52:43.4200000Z; 47h 10m: 69cdc937d385e3b94310f75e.jsonl[143] _id=69dd4b177957a33870f2b385 ts=2026-04-13T19:59:19.1150000Z -> 69cdc937d385e3b94310f75e.jsonl[1093] _id=69dfe2747957a33870f4672d ts=2026-04-15T19:09:39.3760000Z; 46h 51m: 69cdc937d385e3b94310f75e.jsonl[335] _id=69dfee2e7957a33870f494a9 ts=2026-04-15T19:59:41.7570000Z -> 69cdc937d385e3b94310f75e.jsonl[1731] _id=69e2810e1724f0c9e2f78e9c ts=2026-04-17T18:50:53.7330000Z
- **INFO / Info** `questEvent` — very rapid consecutive records (possible duplicates or multi-fire). 
  - Observed: 18 interval(s) ≤ 0.002s..0.006s shown 
  - Evidence: 2ms: 69cdc937d385e3b94310f75e.jsonl[1381] _id=69dfe9027957a33870f48055 ts=2026-04-15T19:37:36.5410000Z -> 69cdc937d385e3b94310f75e.jsonl[1376] _id=69dfe9037957a33870f4805d ts=2026-04-15T19:37:36.5430000Z; 4ms: 69cdc937d385e3b94310f75e.jsonl[1234] _id=69dfe6097957a33870f474b3 ts=2026-04-15T19:24:56.8770000Z -> 69cdc937d385e3b94310f75e.jsonl[194] _id=69dfe60a7957a33870f474b5 ts=2026-04-15T19:24:56.8810000Z; 6ms: 69cdc937d385e3b94310f75e.jsonl[1152] _id=69dfe4d47957a33870f46f1d ts=2026-04-15T19:19:48.0250000Z -> 69cdc937d385e3b94310f75e.jsonl[1156] _id=69dfe4d57957a33870f46f1f ts=2026-04-15T19:19:48.0310000Z

## 7. Sequence / Timing Findings

- **WARNING / Medium** — Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found. 
  - Observed: 6 record(s) match the trigger in 69cdc937d385e3b94310f75e.jsonl:69cdc937d385e3b94310f75e, none match the expectation 
  - Expected: Soil Key Puzzle with {'actionType': ['LeftDrag', 'RightDrag']} 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[103] _id=69dd49ba7957a33870f2aeb5 ts=2026-04-13T19:53:30.0260000Z`; `69cdc937d385e3b94310f75e.jsonl[1326] _id=69dfe80f7957a33870f47c9b ts=2026-04-15T19:33:34.9630000Z`; `69cdc937d385e3b94310f75e.jsonl[1405] _id=69dfe9c87957a33870f4833b ts=2026-04-15T19:40:56.1950000Z` 
  - Spec source: soil-key-puzzle-investigation.md
- **WARNING / Medium** — waypoint use implies the topographic map was opened: expected corroborating events not found. 
  - Observed: 2 record(s) match the trigger in 69cdc937d385e3b94310f75e.jsonl:69cdc937d385e3b94310f75e, none match the expectation 
  - Expected: TopographicMapEvent with {'actionType': 'MapOpenEvent'} 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[270] _id=69dfea6b7957a33870f48633 ts=2026-04-15T19:43:38.2660000Z`; `69cdc937d385e3b94310f75e.jsonl[1457] _id=69dfea727957a33870f4864d ts=2026-04-15T19:43:45.4410000Z` 
  - Spec source: topographic-map-event-investigation.md
- **WARNING / Medium** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: finish without preceding start. 
  - Observed: 4 occurrence(s) 
  - Expected: every 'DialogueFinishEvent' preceded by 'DialogueStartEvent' per conversationId 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[322] _id=69dfee337957a33870f494d0 ts=2026-04-15T19:59:44.6400000Z`; `69cdc937d385e3b94310f75e.jsonl[1935] _id=69e2853a1724f0c9e2f79e4e ts=2026-04-17T19:08:41.9070000Z`; `69cdc937d385e3b94310f75e.jsonl[1949] _id=69e285791724f0c9e2f79f58 ts=2026-04-17T19:09:40.7830000Z` 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **WARNING / Medium** `argumentationEvent` `actionType` — argumentation session: close without preceding open. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'argumentationSessionClose' preceded by 'argumentationSessionOpen' per argumentationTitle 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[501] _id=69e28bd11724f0c9e2f7b768 ts=2026-04-17T19:36:48.0180000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **WARNING / Medium** `argumentationToolEvent` `actionType` — backing-info panel: close without preceding open. 
  - Observed: 2 occurrence(s) 
  - Expected: every 'argumentationToolClose' preceded by 'argumentationToolOpen' per toolName 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[643] _id=69e7cf0a1724f0c9e2f9d437 ts=2026-04-21T19:24:57.4050000Z`; `69cdc937d385e3b94310f75e.jsonl[644] _id=69e7cf0a1724f0c9e2f9d439 ts=2026-04-21T19:24:57.4070000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **WARNING / Medium** `questEvent` `questEventType` — quest lifecycle: finish without preceding start. 
  - Observed: 1 occurrence(s) 
  - Expected: every 'questFinishEvent' preceded by 'questActiveEvent' per questID 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[1410] _id=69dfe9d77957a33870f4835d ts=2026-04-15T19:41:10.5510000Z` 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **WARNING / Medium** — records without a parseable client timestamp. 
  - Observed: 3 records 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[2543] _id=69e7ce431724f0c9e2f9d135 ts=?`; `69cdc937d385e3b94310f75e.jsonl[2808] _id=69e7d2921724f0c9e2f9e71f ts=?`; `69cdc937d385e3b94310f75e.jsonl[3033] _id=69e7d82b1724f0c9e2f9fc2b ts=?`
- **WARNING / Low** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: repeated open with no intervening close. 
  - Observed: 3 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[1338] _id=69dfe80c7957a33870f47c8f ts=2026-04-15T19:33:31.9850000Z`; `69cdc937d385e3b94310f75e.jsonl[252] _id=69dfe9c57957a33870f48333 ts=2026-04-15T19:40:53.1990000Z`; `69cdc937d385e3b94310f75e.jsonl[1517] _id=69dfeb937957a33870f48a09 ts=2026-04-15T19:48:34.9300000Z` 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **WARNING / Low** `argumentationToolEvent` `actionType` — backing-info panel: repeated open with no intervening close. 
  - Observed: 5 occurrence(s) 
  - Examples: `69cdc937d385e3b94310f75e.jsonl[2935] _id=69e7d5cb1724f0c9e2f9f2a9 ts=2026-04-21T19:53:47.2110000Z`; `69cdc937d385e3b94310f75e.jsonl[2939] _id=69e7d5cd1724f0c9e2f9f2b5 ts=2026-04-21T19:53:48.8440000Z`; `69cdc937d385e3b94310f75e.jsonl[2940] _id=69e7d5cf1724f0c9e2f9f2bf ts=2026-04-21T19:53:50.2430000Z` 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `DialogueEvent` `dialogueEventType` — dialogue lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 209 unmatched 'DialogueStartEvent' (totals: 438 start, 233 finish) 
  - Spec source: observed data (dialogue-event PDF not machine-readable)
- **INFO / Info** `Soil Key Puzzle` `Soil Key Puzzle Status` — puzzle start/finish: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'Started' (totals: 7 open, 6 close) 
  - Spec source: 08-13-26/Investigation-results/soil-key-puzzle-investigation.md
- **INFO / Info** `argumentationEvent` `actionType` — argumentation session: open(s) never closed (may be legitimate at session end). 
  - Observed: 1 unmatched 'argumentationSessionOpen' (totals: 8 open, 8 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-event-investigation.md
- **INFO / Info** `argumentationToolEvent` `actionType` — backing-info panel: open(s) never closed (may be legitimate at session end). 
  - Observed: 2 unmatched 'argumentationToolOpen' (totals: 14 open, 14 close) 
  - Spec source: 08-13-26/Investigation-results/argumentation-tool-event-investigation.md
- **INFO / Info** `questEvent` `questEventType` — quest lifecycle: start(s) never finishd (may be legitimate at session end). 
  - Observed: 16 unmatched 'questActiveEvent' (totals: 58 start, 43 finish) 
  - Spec source: 08-13-26/Investigation-results/quest-event-investigation.md
- **INFO / Info** — client vs server timestamp skew. 
  - Observed: median -0.76s, min -831.07s, max -0.20s over 3031 records 
  - Expected: small constant skew; large negatives = delayed uploads

## 8. Coverage Findings

Coverage source: manifest C:\Users\wenyi\OneDrive\Documents\GitHub\mhsgrading\build-log-qa\reports\fall2026-bowling-green-wayne-county\users\69cdc937d385e3b94310f75e\coverage.yaml

| unit | status |
| --- | --- |
| Unit1 | complete |
| Unit2 | complete |
| Unit3 | complete |
| Unit4 | complete |
| Unit5 | complete |
| notes | Generated by audit_per_user.py from the student's own log: complete = EndOfUnit fired for the unit; partial = a scene of the unit was entered but EndOfUnit never fired; skipped = no scene of the unit appears (content not reached). |

- **WARNING / Medium** `DEBUGMenu` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `DaniEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/dani-event-investigation.md
- **WARNING / Medium** `InputEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data (input-event PDF not machine-readable)
- **WARNING / Medium** `ObjectInterEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/objectinter-event-investigation.md
- **WARNING / Medium** `PuzzlePieceVisibleEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [2, 3, 4] 
  - Evidence: coverage: Unit2=complete, Unit3=complete, Unit4=complete 
  - Spec source: 08-13-26/Investigation-results/puzzle-piece-visible-event.md
- **WARNING / Medium** `SolarStillDesignEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [5] 
  - Evidence: coverage: Unit5=complete 
  - Spec source: observed data 08-25-26 (first appearance; no written spec yet)
- **WARNING / Medium** `argumentationAnswerEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/argumentation-answer-event-investigation.md
- **WARNING / Medium** `chatEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 5] 
  - Evidence: coverage: Unit1=complete, Unit5=complete 
  - Spec source: 08-13-26/Investigation-results/chat-event-investigation.md
- **WARNING / Medium** `gameStartEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowFocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **WARNING / Medium** `gameWindowUnfocusEvent` — expected event type absent although its content was played — possible logging failure. 
  - Expected: appears in Unit(s) [1, 2, 3, 4, 5] 
  - Evidence: coverage: Unit1=complete, Unit2=complete, Unit3=complete, Unit4=complete, Unit5=complete 
  - Spec source: observed data
- **INFO / Info** `Topographic Map Event` — no expectation rules configured — descriptive profiling only. 
  - Observed: 34 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks
- **INFO / Info** `crash` — no expectation rules configured — descriptive profiling only. 
  - Observed: 3 records 
  - Expected: add the event to event_expectations.yaml to enable expectation checks

## 9. Event-Type Details

### `DialogueEvent` — 2304 records

*Purpose:* Dialogue lifecycle — conversation start/finish and every node shown/selected.

- **Scenes:** Unit 2 Prod (Refactor) (846); Unit 1 Dev (340); Unit 3 Dev (318); Unit 4 Dev (230); Unit 5 Dev (217); Unit 4 Dev - Anderson Base (126); Unit 4 Dev - Dungeon (112); Unit 3 Dungeon Dev (94); Unit 5 Dev - Dungeon (21)
- **eventKey:** present on 1633 of 2304 records
- **Intervals:** median 1.15s (p5 0.01s / p95 27.22s, n=2303)
- **`data` key-set variants:** [conversationId, dialogueEventType, nodeId] x1633; [conversationId, dialogueEventType] x671
- **Open findings:** 4 — see sections 5-8
- **Fields under `data`:**

```text
data.conversationId  (number, 2304/2304 records)
    numeric range 8 .. 114 (52 unique)
data.dialogueEventType  (string, 2304/2304 records)
    "DialogueNodeEvent"  x1633
    "DialogueStartEvent"  x438
    "DialogueFinishEvent"  x233
data.nodeId  (number, 1633/2304 records)
    numeric range 0 .. 286 (227 unique)
```

Raw examples: `event_examples.json` -> `DialogueEvent`.

### `PlayerPositionEvent` — 450 records

*Purpose:* Periodic snapshot of the player's world position.

- **Scenes:** Unit 2 Prod (Refactor) (160); Unit 3 Dev (65); Unit 1 Dev (51); Unit 4 Dev (41); Unit 4 Dev - Dungeon (38); Unit 4 Dev - Anderson Base (32); Unit 5 Dev (27); Unit 3 Dungeon Dev (20); Unit 5 Dev - Dungeon (16)
- **Intervals:** median 30.05s (p5 29.96s / p95 37.76s, n=432)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.position  (object, 450/450 records)
data.position.x  (number, 450/450 records)
    numeric range -691.964 .. 1557.34 (273 unique)
data.position.y  (number, 450/450 records)
    numeric range -115.127 .. 222.004 (230 unique)
data.position.z  (number, 450/450 records)
    numeric range -1131.94 .. 1949.88 (273 unique)
```

Raw examples: `event_examples.json` -> `PlayerPositionEvent`.

### `questEvent` — 101 records

*Purpose:* Quest activation and completion, the backbone of progress tracking.

- **Scenes:** Unit 1 Dev (24); Unit 2 Prod (Refactor) (23); Unit 3 Dev (13); Unit 4 Dev - Dungeon (12); Unit 4 Dev (9); Unit 5 Dev (7); Unit 5 Dev - Dungeon (7); Unit 3 Dungeon Dev (3); Unit 4 Dev - Anderson Base (3)
- **eventKey:** present on 101 of 101 records
- **Intervals:** median 106.41s (p5 0.01s / p95 489.52s, n=100)
- **`data` key-set variants:** [questEventType, questID, questName] x58; [questEventType, questID, questName, questSuccessOrFailure] x43
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.questEventType  (string, 101/101 records)
    "questActiveEvent"  x58
    "questFinishEvent"  x43
data.questID  (string, 101/101 records)
    34 unique values (see csv/event_unique_values.csv)
data.questName  (string, 101/101 records)
    34 unique values (see csv/event_unique_values.csv)
data.questSuccessOrFailure  (string, 43/101 records)
    "Succeeded"  x43
```

Raw examples: `event_examples.json` -> `questEvent`.

### `Topographic Map Event` — 34 records

- **Scenes:** Unit 2 Prod (Refactor) (24); Unit 3 Dev (10)
- **Intervals:** median 22.29s (p5 2.26s / p95 68888.91s, n=33)
- **Fields under `data`:**

```text
data.actionType  (string, 34/34 records)
    "MapCloseEvent"  x19
    "MapOpenEvent"  x15
data.featureUsed  (string, 34/34 records)
    "Map"  x34
```

Raw examples: `event_examples.json` -> `Topographic Map Event`.

### `WaterChamberEvent` — 32 records

*Purpose:* Water chamber machines (condenser/evaporator/vents) toggled in Unit 5 dungeon.

- **Scenes:** Unit 5 Dev - Dungeon (32)
- **Intervals:** median 5.74s (p5 1.68s / p95 18.90s, n=31)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 32/32 records)
    "On"  x21
    "Off"  x11
data.floor  (string, 32/32 records)
    "4"  x16
    "3"  x9
    "1"  x4
    "2"  x3
data.machineNumber  (string, 32/32 records)
    "One"  x31
    "Two"  x1
data.machineType  (string, 32/32 records)
    "Condenser"  x21
    "Evaporator"  x6
    "DualChamber_Evaporator"  x2
    "VentSwitch"  x2
    "DualChamber_Condenser"  x1
data.room  (string, 32/32 records)
    "2"  x12
    "3"  x10
    "1"  x8
    "4"  x2
```

Raw examples: `event_examples.json` -> `WaterChamberEvent`.

### `argumentationToolEvent` — 28 records

*Purpose:* Backing-info panel usage inside the argumentation tool.

- **Scenes:** Unit 4 Dev - Anderson Base (16); Unit 5 Dev (12)
- **Intervals:** median 1.56s (p5 0.02s / p95 101.34s, n=27)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 28/28 records)
    "argumentationToolClose"  x14
    "argumentationToolOpen"  x14
data.argumentationTitle  (string, 28/28 records)
    "Unit 4 - Flooding"  x16
    "Unit 5"  x12
data.toolName  (string, 28/28 records)
    "BackingInfoPanel - Heat Added/Released Chart"  x11
    "BackingInfoPanel - Soil Layers and Fountain Data"  x10
    "BackingInfoPanel - Soil Flow Rates"  x6
    "BackingInfoPanel - Evaporation Flow Diagram"  x1
```

Raw examples: `event_examples.json` -> `argumentationToolEvent`.

### `argumentationNodeEvent` — 20 records

*Purpose:* Hovering and adding claim/evidence/reasoning nodes in the argumentation tool.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 1 Dev (8); Unit 3 Dev (3)
- **Intervals:** median 8.39s (p5 1.83s / p95 171199.23s, n=19)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 20/20 records)
    "argumentationNodeAdd"  x16
    "argumentationNodeRemove"  x4
data.argumentationTitle  (string, 20/20 records)
    "Unit 2 – Watershed"  x9
    "Unit 1 - Freshwater"  x8
    "Unit 3 - Pollution Upstream"  x3
data.nodeName  (string, 20/20 records)
    "A"  x6
    "I"  x5
    "1"  x3
    "B"  x2
    "D"  x2
    "5"  x1
    "II"  x1
```

Raw examples: `event_examples.json` -> `argumentationNodeEvent`.

### `argumentationEvent` — 16 records

*Purpose:* Argumentation session open/close.

- **Scenes:** Unit 1 Dev (8); Unit 3 Dev (3); Unit 2 Prod (Refactor) (2); Unit 5 Dev (2); Unit 4 Dev - Anderson Base (1)
- **Intervals:** median 60.63s (p5 1.25s / p95 223838.45s, n=15)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 16/16 records)
    "argumentationSessionClose"  x8
    "argumentationSessionOpen"  x8
data.argumentationDescription  (string, 16/16 records)
    "U1 - Argumentation tutorial - Place the claim, reasoning, and evidence orbs in orbit"  x4
    "Unit 1 - Does the planet WAT-247 have freshwater"  x4
    "U3 – Pollution Upstream" equals "Where is the pollution site probably located?"  x3
    "U2 – Watershed - Which watershed is bigger based on collected evidence from eastern and western waterfalls"  x2
    "Unit 5 - What happened to the water when in Aryn's collection tanks"  x2
    "Unit 4 - Will the flooding in the workshop resolve after the fountain is turned off"  x1
data.argumentationTitle  (string, 16/16 records)
    "Unit 1 - Argumentation Tutorial"  x4
    "Unit 1 - Freshwater"  x4
    "Unit 3 - Pollution Upstream"  x3
    "Unit 2 – Watershed"  x2
    "Unit 5"  x2
    "Unit 4 - Flooding"  x1
```

Raw examples: `event_examples.json` -> `argumentationEvent`.

### `soilMachine` — 14 records

*Purpose:* Soil canister changes in the Unit 4 dungeon machines.

- **Scenes:** Unit 4 Dev - Dungeon (14)
- **Intervals:** median 19.83s (p5 0.83s / p95 114.25s, n=13)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 14/14 records)
    "ChangeCanister"  x14
data.canisterType  (string, 14/14 records)
    "Clay"  x5
    "Bedrock"  x3
    "Gravel"  x3
    "Sand"  x3
data.floor  (string, 14/14 records)
    "5"  x8
    "4"  x5
    "3"  x1
data.machine  (string, 14/14 records)
    "1"  x12
    "2"  x2
data.row  (string, 14/14 records)
    "TopRow"  x9
    "BottomRow"  x5
```

Raw examples: `event_examples.json` -> `soilMachine`.

### `Soil Key Puzzle` — 13 records

*Purpose:* Soil key puzzle — start/finish plus every soil-drag attempt.

- **Scenes:** Unit 2 Prod (Refactor) (9); Unit 3 Dev (2); Unit 4 Dev (2)
- **Intervals:** median 238.74s (p5 2.84s / p95 171291.61s, n=12)
- **Open findings:** 3 — see sections 5-8
- **Fields under `data`:**

```text
data.Soil Key Puzzle Status  (string, 13/13 records)
    "Started"  x7
    "Finished"  x6
data.Unit  (string, 13/13 records)
    "Unit 2 Prod (Refactor)"  x9
    "Unit 3 Dev"  x2
    "Unit 4 Dev"  x2
```

Raw examples: `event_examples.json` -> `Soil Key Puzzle`.

### `TerasGardenBox` — 11 records

*Purpose:* Tera's garden-box activity — soil selection and camera placement.

- **Scenes:** Unit 4 Dev (11)
- **Intervals:** median 2.95s (p5 0.90s / p95 18.68s, n=10)
- **`data` key-set variants:** [actionType, boxID, soilType] x7; [actionType, boxId, soilType] x4
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 11/11 records)
    "soilSelected"  x7
    "cameraPlaced"  x4
data.boxID  (string, 7/11 records)
    "1"  x4
    "0"  x2
    "2"  x1
data.boxId  (string, 4/11 records)
    "1"  x2
    "0"  x1
    "2"  x1
data.soilType  (string, 11/11 records)
    "Gravel"  x7
    "Sand"  x3
    "Clay"  x1
```

Raw examples: `event_examples.json` -> `TerasGardenBox`.

### `EndOfUnit` — 6 records

*Purpose:* Marks the completion of a game unit.

- **Scenes:** Unit 1 Dev (2); Unit 2 Prod (Refactor) (1); Unit 3 Dev (1); Unit 4 Dev (1); Unit 5 Dev (1)
- **Intervals:** median 171213.91s (p5 1785.46s / p95 310002.49s, n=5)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.Unit  (string, 6/6 records)
    "1"  x2
    "2"  x1
    "3"  x1
    "4"  x1
    "5"  x1
```

Raw examples: `event_examples.json` -> `EndOfUnit`.

### `crash` — 3 records

- **Scenes:** <missing sceneName> (3)
- **Open findings:** 1 — see sections 5-8
- **Fields under `data`:**

```text
data.isPWA  (bool, 3/3 records)
    true  x3
data.message  (string, 3/3 records)
    "Cannot close a closed AudioContext."  x2
    "Uncaught ReferenceError: onResize is not defined"  x1
data.phase  (string, 3/3 records)
    "running"  x3
data.stack  (string, 3/3 records, 2 empty-string)
    ""  x2
    "ReferenceError: onResize is not defined
    at HTMLDocument.onFullscreenChange (https://mhs.adroit.games/missionhydrosci/play/unit5:831:9)"  x1
data.type  (string, 3/3 records)
    "unhandled_rejection"  x2
    "runtime_error"  x1
data.unitId  (string, 3/3 records)
    "unit4"  x2
    "unit5"  x1
data.workspace  (string, 3/3 records)
    "mhs"  x3
```

Raw examples: `event_examples.json` -> `crash`.

### `TopographicMapEvent` — 2 records

*Purpose:* Topographic map tool usage — open/close and waypoint placement.

- **Scenes:** Unit 2 Prod (Refactor) (2)
- **Intervals:** median 7.17s (p5 7.17s / p95 7.17s, n=1)
- **Open findings:** 2 — see sections 5-8
- **Fields under `data`:**

```text
data.actionType  (string, 2/2 records)
    "dragEnd"  x1
    "dragStart"  x1
data.featureUsed  (string, 2/2 records)
    "waypoint"  x2
data.location  (object, 2/2 records)
data.location.x  (number, 2/2 records)
    2 unique values (see csv/event_unique_values.csv)
data.location.y  (number, 2/2 records)
    2 unique values (see csv/event_unique_values.csv)
data.location.z  (number, 2/2 records)
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
- `SolarStillDesignEvent` : expected event type absent although its content was played — possible logging failure
- `argumentationAnswerEvent` : expected event type absent although its content was played — possible logging failure
- `chatEvent` : expected event type absent although its content was played — possible logging failure
- `gameStartEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowFocusEvent` : expected event type absent although its content was played — possible logging failure
- `gameWindowUnfocusEvent` : expected event type absent although its content was played — possible logging failure
- `-` : Soil Key Puzzle finished implies soil drag interactions happened: expected corroborating events not found
- `-` : waypoint use implies the topographic map was opened: expected corroborating events not found
- `DialogueEvent` : exact duplicate records (same timestamp, scene and data)
- `crash` : exact duplicate records (same timestamp, scene and data)

**Documentation / specification clarification:**
- `Soil Key Puzzle` : Unit 2 Prod (Refactor) (9 records)
- `TopographicMapEvent` data.actionType: "dragStart" (1x)
- `argumentationNodeEvent` data.actionType: "argumentationNodeRemove" (4x)
- `soilMachine` data.canisterType: "Bedrock" (3x)


---
*Generated by build-log-qa / mhs_log_audit. All findings are traceable to raw records via the `file[index] _id=... ts=...` references; raw examples in `event_examples.json`.*